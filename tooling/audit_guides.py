#!/usr/bin/env python3
"""
Guide Audit Script
Scans all modular guide .md files against the current standards.

Usage:
    python3 tooling/audit_guides.py
    python3 tooling/audit_guides.py --modular-dir path/to/modular --output-dir path/to/output

Outputs (written to --output-dir, default: tooling/):
    audit_report.md    Human-readable markdown report with tables
    audit_report.json  Machine-readable findings per guide and per check

Severity levels:
    error    — Clearly wrong by current standards; fix before next commit
    warning  — Outdated standard; fix when the guide is next touched
    deferred — Known, tracked, low priority; listed for completeness

Adding a new check:
    1. Write a function:  check_something(file_path, content, lines, fm) -> list[Issue]
    2. Append it to the CHECKS list near the bottom of this file.
    The function receives the file path, full content string, lines list, and
    parsed frontmatter dict. Return an empty list if the file is clean for that check.
"""

import argparse
import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VALID_PRIMARY_ROLES = {
    "SOURCE", "SHAPER", "AMPLIFIER", "MODULATOR",
    "CONTROLLER", "ROUTER", "ANALYZER", "UTILITY",
    "EVENT_VOICE",  # Added v2: trigger-dependent sound engine
}

VALID_FORM_FACTORS = {
    "eurorack", "semi-modular", "standalone", "pedal", "rack",
    "guitar", "bass", "amplifier", "cabinet", "monitor", "headphones",
    "blank-panel",
}

VALID_FUNCTIONS = {
    # Sources
    "oscillator", "complex-oscillator", "fm-oscillator", "noise-source",
    "drum-voice", "sample-player", "granular", "physical-model", "string-instrument",
    # Shaping
    "filter", "wavefolder", "distortion", "resonator", "eq", "dynamics",
    "fx-time", "fx-modulation", "fx-pitch", "fx-spectral",
    # Modulation
    "envelope-generator", "lfo", "function-generator", "sample-hold",
    "random-source", "slew-limiter", "quantizer",
    # Sequencing & Timing
    "sequencer", "clock-source", "clock-divider", "clock-multiplier",
    "euclidean-generator",
    # Routing & Utility
    "vca", "mixer", "attenuator", "mult", "switch-router", "signal-router",
    "logic-processor", "cv-processor",
    # System
    "preamp", "power-amp", "audio-interface", "oscilloscope", "tuner",
    "power-distribution", "transducer", "microphone",
}

VALID_BEHAVIOR_TAGS = {
    # Stability
    "stable", "unstable", "chaotic",
    # Temporal character
    "percussive", "sustained", "evolving", "static", "free-running", "gated",
    # Sonic character
    "clean", "dirty", "warm", "harsh", "dark", "bright",
    "metallic", "noisy", "harmonic", "inharmonic",
    # Control character
    "linear", "nonlinear", "sensitive", "reactive", "performance-oriented",
    # Behavioral flags
    "self-modulating", "generative", "stochastic",
}

VALID_GRADUATED = {"none", "basic", "full"}
VALID_BOOL      = {"true", "false"}

# Files that live in modular/ but are not standard module guides
NON_GUIDE_FILES = {
    "README.md",
    "pkhia_corrections.md",
    "semi_modular_integration_guide.md",
}

# Severity
ERROR    = "error"
WARNING  = "warning"
DEFERRED = "deferred"

SEVERITY_RANK  = {ERROR: 0, WARNING: 1, DEFERRED: 2}
SEVERITY_LABEL = {ERROR: "❌ error", WARNING: "⚠️  warning", DEFERRED: "📌 deferred"}

# Issue categories (controls display order in the report)
CAT_YAML     = "YAML Frontmatter"
CAT_SECTIONS = "Missing or Misplaced Sections"
CAT_FORMAT   = "Format Issues"
CAT_DEFERRED = "Deferred Items"

CATEGORY_ORDER = [CAT_YAML, CAT_SECTIONS, CAT_FORMAT, CAT_DEFERRED]


# ---------------------------------------------------------------------------
# Issue data structure
# ---------------------------------------------------------------------------

class Issue:
    def __init__(self, check_id, category, severity, detail, line=None):
        self.check_id = check_id
        self.category = category
        self.severity = severity
        self.detail   = detail
        self.line     = line  # 1-based line number, or None

    def to_dict(self):
        d = {
            "check_id": self.check_id,
            "category": self.category,
            "severity": self.severity,
            "detail":   self.detail,
        }
        if self.line is not None:
            d["line"] = self.line
        return d


# ---------------------------------------------------------------------------
# Frontmatter parser (no external dependencies)
# ---------------------------------------------------------------------------

def parse_frontmatter(content):
    """
    Extract YAML frontmatter into a flat dict.
    Only handles simple key: value pairs — enough for our schema.
    Returns {} if no frontmatter is present.
    """
    if not content.startswith("---"):
        return {}
    end = content.find("\n---", 3)
    if end == -1:
        return {}
    fm_text = content[4:end].strip()
    result = {}
    for line in fm_text.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            result[key.strip()] = val.strip()
    return result


def has_frontmatter(content):
    return content.startswith("---\n") and "\n---" in content[4:]


def parse_yaml_array(val):
    """
    Parse a YAML inline array string like '[item1, item2]' into a list of strings.
    Returns None if the value is not in array format.
    Returns [] for an empty array '[]'.
    """
    val = val.strip()
    if not (val.startswith("[") and val.endswith("]")):
        return None
    inner = val[1:-1].strip()
    if not inner:
        return []
    return [item.strip() for item in inner.split(",") if item.strip()]


# ---------------------------------------------------------------------------
# Line-context helpers
# ---------------------------------------------------------------------------

def prose_lines(lines):
    """
    Yield (1-based lineno, line) for lines that are NOT in:
      - YAML frontmatter block
      - Fenced code blocks (``` ... ```)
    Useful for checks that should only fire on human-readable prose.
    """
    in_fm = False
    in_code = False

    for i, line in enumerate(lines, 1):
        # Frontmatter detection
        if i == 1 and line.strip() == "---":
            in_fm = True
            continue
        if in_fm:
            if line.strip() == "---":
                in_fm = False
            continue
        # Code block toggle
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        yield i, line


def get_headings(lines):
    """Return list of (lineno, level, text) for all ATX headings."""
    result = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            result.append((i, len(m.group(1)), m.group(2).strip()))
    return result


def find_heading(headings, pattern, flags=re.IGNORECASE):
    """Return (lineno, text) of first heading whose text matches pattern, else None."""
    for lineno, level, text in headings:
        if re.search(pattern, text, flags):
            return lineno, text
    return None


# ---------------------------------------------------------------------------
# YAML frontmatter checks
# ---------------------------------------------------------------------------

def check_yaml_present(fp, content, lines, fm):
    if not has_frontmatter(content):
        return [Issue("yaml_present", CAT_YAML, ERROR, "No YAML frontmatter found")]
    return []


def check_yaml_title(fp, content, lines, fm):
    if not has_frontmatter(content):
        return []
    if "title" not in fm:
        return [Issue("yaml_title", CAT_YAML, ERROR, "Missing `title` field")]
    return []


def check_yaml_manufacturer(fp, content, lines, fm):
    if not has_frontmatter(content):
        return []
    if "manufacturer" not in fm:
        return [Issue("yaml_manufacturer", CAT_YAML, ERROR, "Missing `manufacturer` field")]
    return []


def check_yaml_primary_role(fp, content, lines, fm):
    if not has_frontmatter(content):
        return []
    if "primary_role" not in fm:
        return [Issue("yaml_primary_role", CAT_YAML, ERROR, "Missing `primary_role` field")]
    role = fm["primary_role"].strip().upper()
    if role not in VALID_PRIMARY_ROLES:
        valid = ", ".join(sorted(VALID_PRIMARY_ROLES))
        return [Issue("yaml_primary_role_valid", CAT_YAML, ERROR,
                      f"`primary_role` value \"{fm['primary_role']}\" not in valid set: {valid}")]
    return []


def check_yaml_secondary_roles(fp, content, lines, fm):
    if not has_frontmatter(content):
        return []
    if "secondary_roles" not in fm:
        return []  # Field is optional; absence is fine
    val = fm["secondary_roles"].strip()
    if not (val.startswith("[") and val.endswith("]")):
        return [Issue("yaml_secondary_roles_array", CAT_YAML, ERROR,
                      f"`secondary_roles` must be array format `[VALUE]` or `[]`, got: `{val}`")]
    return []


def check_yaml_hp(fp, content, lines, fm):
    if not has_frontmatter(content):
        return []
    if "hp" not in fm:
        return [Issue("yaml_hp", CAT_YAML, WARNING, "Missing `hp` field")]
    return []


# ---------------------------------------------------------------------------
# Required section checks
# ---------------------------------------------------------------------------

def check_section_historical_context(fp, content, lines, fm):
    # historical_context: false in frontmatter means the author has decided
    # this module has no meaningful historical context — skip the check.
    if str(fm.get("historical_context", "")).strip().lower() == "false":
        return []
    headings = get_headings(lines)
    if not find_heading(headings, r"historical context"):
        return [Issue("section_historical_context", CAT_SECTIONS, WARNING,
                      "Missing `## Historical Context` section")]
    return []


def check_section_why_excels(fp, content, lines, fm):
    """
    Checks for presence of any 'Why' section (Excels, Rocks, Works variants all count).
    A separate deferred check flags the old 'Rocks' wording for eventual renaming.
    """
    headings = get_headings(lines)
    # Broad match: any heading starting with "Why" at the ## level
    if not find_heading(headings, r"^why\b"):
        return [Issue("section_why_excels", CAT_SECTIONS, ERROR,
                      "Missing `## Why [Module] Excels` section (no 'Why' heading found)")]
    return []


def check_why_section_old_wording(fp, content, lines, fm):
    """
    Gen-1 guides used 'Why This Module Rocks' / 'Why X Rocks'.
    Current standard is 'Why [Module] Excels'. Flag for eventual renaming.
    """
    headings = get_headings(lines)
    result = find_heading(headings, r"^why\b.*\brocks\b")
    if result:
        return [Issue("why_section_old_wording", CAT_DEFERRED, DEFERRED,
                      f"Gen-1 'Rocks' wording: \"{result[1]}\" — rename to `## Why [Module] Excels`",
                      line=result[0])]
    return []


def check_section_common_mistakes(fp, content, lines, fm):
    headings = get_headings(lines)
    if not find_heading(headings, r"common mistakes"):
        return [Issue("section_common_mistakes", CAT_SECTIONS, WARNING,
                      "Missing `## Common Mistakes` section")]
    return []


def check_section_pairs_well(fp, content, lines, fm):
    headings = get_headings(lines)
    if not find_heading(headings, r"pairs well|works well"):
        return [Issue("section_pairs_well", CAT_SECTIONS, WARNING,
                      "Missing `## Pairs Well With` section")]
    return []


def check_section_alp(fp, content, lines, fm):
    """Advanced Learning Path — checks for presence under any spelling."""
    headings = get_headings(lines)
    if not find_heading(headings, r"learning path|advanced learning|advanced techniques"):
        return [Issue("section_alp", CAT_SECTIONS, WARNING,
                      "Missing `## Advanced Learning Path` section")]
    return []


# ---------------------------------------------------------------------------
# Section order checks
# ---------------------------------------------------------------------------

def check_why_excels_before_patches(fp, content, lines, fm):
    """
    Why This Excels must appear before the first patch example heading.
    The April 2026 audit found several guides where this was reversed.
    """
    headings = get_headings(lines)
    why   = find_heading(headings, r"why\b.*excels")
    patch = find_heading(headings, r"patch \d|patch examples|^patch$")
    if why and patch and why[0] > patch[0]:
        return [Issue("why_excels_order", CAT_SECTIONS, ERROR,
                      f"`Why This Excels` (line {why[0]}) appears AFTER first patch heading "
                      f"(line {patch[0]}); must precede patch examples")]
    return []


# ---------------------------------------------------------------------------
# Format issue checks
# ---------------------------------------------------------------------------

def check_em_dashes(fp, content, lines, fm):
    """
    Em dash (—, U+2014) is prohibited in guide prose.
    Fix: rewrite the sentence using a colon, semicolon, or parentheses.
    Skips frontmatter and fenced code blocks.
    """
    EM = "\u2014"
    issues = []
    for lineno, line in prose_lines(lines):
        if EM in line:
            issues.append(Issue("em_dash", CAT_FORMAT, WARNING,
                                f"Em dash in prose: \"{line.strip()[:90]}\"",
                                line=lineno))
    return issues


def check_emoji_labels(fp, content, lines, fm):
    """
    Old emoji color labels (🔴🔵🟡) should be replaced with [A] [C] [G].
    Retired April 2026.
    """
    emoji_re = re.compile(r"[🔴🔵🟡]")
    issues = []
    for lineno, line in prose_lines(lines):
        if emoji_re.search(line):
            issues.append(Issue("emoji_labels", CAT_FORMAT, WARNING,
                                f"Old emoji color label: \"{line.strip()[:90]}\"",
                                line=lineno))
    return issues


def check_color_labels(fp, content, lines, fm):
    """
    Old (Blue) / (Red) / (Yellow) color labels in patch diagrams.
    Should be [A] / [C] / [G] inline notation.
    """
    color_re = re.compile(r"\((Blue|Red|Yellow|Green)\)", re.IGNORECASE)
    issues = []
    for lineno, line in prose_lines(lines):
        if color_re.search(line):
            issues.append(Issue("color_labels", CAT_FORMAT, WARNING,
                                f"Old color label: \"{line.strip()[:90]}\"",
                                line=lineno))
    return issues


def check_bullet_setup_sections(fp, content, lines, fm):
    """
    Bullet-list Setup sections (- Source ---[A]---> Dest) should now be
    fenced code blocks. Introduced as standard in the diagram format update.
    """
    bullet_arrow = re.compile(r"^- .*---\[")
    issues = []
    for lineno, line in prose_lines(lines):
        if bullet_arrow.match(line):
            issues.append(Issue("bullet_setup", CAT_FORMAT, WARNING,
                                f"Bullet-list Setup line (should be fenced block): "
                                f"\"{line.strip()[:90]}\"",
                                line=lineno))
    return issues


def check_image_url_format(fp, content, lines, fm):
    """
    Image links should use the standard GitHub raw URL:
    https://github.com/Shadoe-42/music/raw/main/...
    Relative paths or other hosts are flagged.
    """
    img_re      = re.compile(r"!\[.*?\]\(([^)]+)\)")
    correct_re  = re.compile(r"https://github\.com/Shadoe-42/music/raw/main/")
    issues = []
    for i, line in enumerate(lines, 1):
        for m in img_re.finditer(line):
            url = m.group(1)
            if url.startswith("http") and not correct_re.search(url):
                issues.append(Issue("image_url_external", CAT_FORMAT, WARNING,
                                    f"Image URL not on standard GitHub raw path: \"{url[:80]}\"",
                                    line=i))
            elif not url.startswith("http"):
                issues.append(Issue("image_url_relative", CAT_FORMAT, WARNING,
                                    f"Image uses relative URL (should be GitHub raw): \"{url[:80]}\"",
                                    line=i))
    return issues


# ---------------------------------------------------------------------------
# Deferred items (tracked, low priority)
# ---------------------------------------------------------------------------

def check_alp_bold_heading(fp, content, lines, fm):
    """
    `## **Advanced Learning Path**` — bold inside a heading.
    Should be `## Advanced Learning Path`.
    """
    bold_re = re.compile(r"^#{1,3}\s+\*\*.*learning path.*\*\*", re.IGNORECASE)
    issues = []
    for i, line in enumerate(lines, 1):
        if bold_re.match(line):
            issues.append(Issue("alp_bold_heading", CAT_DEFERRED, DEFERRED,
                                f"ALP heading has bold formatting inside: \"{line.strip()}\"",
                                line=i))
    return issues


def check_alp_variant_heading(fp, content, lines, fm):
    """
    Non-standard ALP heading spellings from earlier generations.
    Known variants: 'Learning Path', 'Modular Learning Path',
    'Multi-Function Learning Path'.
    """
    variant_re = re.compile(
        r"^#{1,3}\s+(learning path|modular learning path|multi-function learning path)\s*$",
        re.IGNORECASE,
    )
    issues = []
    for i, line in enumerate(lines, 1):
        if variant_re.match(line):
            issues.append(Issue("alp_variant_heading", CAT_DEFERRED, DEFERRED,
                                f"Non-standard ALP heading: \"{line.strip()}\" "
                                f"(should be `## Advanced Learning Path`)",
                                line=i))
    return issues


def check_phase_2_heading(fp, content, lines, fm):
    """
    'Phase 2' headings are a gen-1 artifact. Should be 'Advanced Learning Path'.
    Batch-fixed in April 2026; flag any that were missed or re-introduced.
    """
    phase2_re = re.compile(r"^#{1,3}\s+phase 2", re.IGNORECASE)
    issues = []
    for i, line in enumerate(lines, 1):
        if phase2_re.match(line):
            issues.append(Issue("phase_2_heading", CAT_DEFERRED, DEFERRED,
                                f"Old 'Phase 2' heading: \"{line.strip()}\"",
                                line=i))
    return issues


# ---------------------------------------------------------------------------
# v2 schema checks
# ---------------------------------------------------------------------------

def check_yaml_form_factor(fp, content, lines, fm):
    if not has_frontmatter(content):
        return []
    if "form_factor" not in fm:
        return [Issue("yaml_form_factor", CAT_YAML, WARNING,
                      "Missing `form_factor` field (v2 schema)")]
    val = fm["form_factor"].strip().lower()
    if val not in VALID_FORM_FACTORS:
        valid = ", ".join(sorted(VALID_FORM_FACTORS))
        return [Issue("yaml_form_factor_valid", CAT_YAML, ERROR,
                      f"`form_factor` value \"{fm['form_factor']}\" not in valid set: {valid}")]
    return []


def check_yaml_functions(fp, content, lines, fm):
    if not has_frontmatter(content):
        return []
    if "functions" not in fm:
        return [Issue("yaml_functions", CAT_YAML, WARNING,
                      "Missing `functions` field (v2 schema)")]
    items = parse_yaml_array(fm["functions"])
    if items is None:
        return [Issue("yaml_functions_format", CAT_YAML, ERROR,
                      f"`functions` must be array format, got: `{fm['functions']}`")]
    if len(items) == 0:
        return []  # blank panels legitimately have empty functions
    issues = []
    if len(items) > 3:
        issues.append(Issue("yaml_functions_count", CAT_YAML, WARNING,
                            f"`functions` has {len(items)} items; maximum is 3"))
    for item in items:
        if item.lower() not in VALID_FUNCTIONS:
            issues.append(Issue("yaml_functions_vocab", CAT_YAML, ERROR,
                                f"`functions` contains unknown term: \"{item}\""))
    return issues


def check_yaml_behavior_tags(fp, content, lines, fm):
    if not has_frontmatter(content):
        return []
    if "behavior_tags" not in fm:
        return [Issue("yaml_behavior_tags", CAT_YAML, WARNING,
                      "Missing `behavior_tags` field (v2 schema)")]
    items = parse_yaml_array(fm["behavior_tags"])
    if items is None:
        return [Issue("yaml_behavior_tags_format", CAT_YAML, ERROR,
                      f"`behavior_tags` must be array format, got: `{fm['behavior_tags']}`")]
    issues = []
    if len(items) < 3:
        issues.append(Issue("yaml_behavior_tags_count_low", CAT_YAML, WARNING,
                            f"`behavior_tags` has {len(items)} items; minimum is 3"))
    if len(items) > 8:
        issues.append(Issue("yaml_behavior_tags_count_high", CAT_YAML, WARNING,
                            f"`behavior_tags` has {len(items)} items; maximum is 8"))
    for item in items:
        if item.lower() not in VALID_BEHAVIOR_TAGS:
            issues.append(Issue("yaml_behavior_tags_vocab", CAT_YAML, ERROR,
                                f"`behavior_tags` contains unknown term: \"{item}\""))
    return issues


def check_yaml_use_cases(fp, content, lines, fm):
    if not has_frontmatter(content):
        return []
    if "use_cases" not in fm:
        return [Issue("yaml_use_cases", CAT_YAML, WARNING,
                      "Missing `use_cases` field (v2 schema)")]
    items = parse_yaml_array(fm["use_cases"])
    if items is None:
        return [Issue("yaml_use_cases_format", CAT_YAML, ERROR,
                      f"`use_cases` must be array format, got: `{fm['use_cases']}`")]
    issues = []
    if len(items) > 4:
        issues.append(Issue("yaml_use_cases_count", CAT_YAML, WARNING,
                            f"`use_cases` has {len(items)} items; maximum is 4"))
    for item in items:
        word_count = len(item.split())
        if word_count < 2:
            issues.append(Issue("yaml_use_cases_too_short", CAT_YAML, WARNING,
                                f"`use_cases` item too short ({word_count} word): \"{item}\""))
        if word_count > 7:
            issues.append(Issue("yaml_use_cases_too_long", CAT_YAML, WARNING,
                                f"`use_cases` item too long ({word_count} words): \"{item}\""))
    return issues


def check_yaml_capability_flags(fp, content, lines, fm):
    """Validate memory, cv (graduated: none/basic/full), transport (none/receive/full),
    screen, hybrid (boolean) if present."""
    if not has_frontmatter(content):
        return []
    issues = []
    # memory and cv use the standard graduated vocabulary: none / basic / full
    for field in ("memory", "cv"):
        if field in fm:
            val = fm[field].strip().lower()
            if val not in VALID_GRADUATED:
                issues.append(Issue(f"yaml_{field}_valid", CAT_YAML, ERROR,
                                    f"`{field}` value \"{fm[field]}\" must be: "
                                    f"none, basic, or full"))
    # transport uses its own vocabulary: none / receive / full
    if "transport" in fm:
        val = fm["transport"].strip().lower()
        if val not in {"none", "receive", "full"}:
            issues.append(Issue("yaml_transport_valid", CAT_YAML, ERROR,
                                f"`transport` value \"{fm['transport']}\" must be: "
                                f"none, receive, or full"))
    for field in ("screen", "hybrid"):
        if field in fm:
            val = fm[field].strip().lower()
            if val not in VALID_BOOL:
                issues.append(Issue(f"yaml_{field}_valid", CAT_YAML, ERROR,
                                    f"`{field}` value \"{fm[field]}\" must be: "
                                    f"true or false"))
    return issues


# ---------------------------------------------------------------------------
# Check registry — add new functions here to include them in every audit run
# ---------------------------------------------------------------------------

CHECKS = [
    # YAML frontmatter — v1
    check_yaml_present,
    check_yaml_title,
    check_yaml_manufacturer,
    check_yaml_primary_role,
    check_yaml_secondary_roles,
    check_yaml_hp,
    # YAML frontmatter — v2
    check_yaml_form_factor,
    check_yaml_functions,
    check_yaml_behavior_tags,
    check_yaml_use_cases,
    check_yaml_capability_flags,
    # Required sections
    check_section_historical_context,
    check_section_why_excels,
    check_section_common_mistakes,
    check_section_pairs_well,
    check_section_alp,
    # Section order
    check_why_excels_before_patches,
    # Format issues
    check_em_dashes,
    check_emoji_labels,
    check_color_labels,
    check_bullet_setup_sections,
    check_image_url_format,
    # Deferred
    check_alp_bold_heading,
    check_alp_variant_heading,
    check_phase_2_heading,
    check_why_section_old_wording,
]


# ---------------------------------------------------------------------------
# Audit runner
# ---------------------------------------------------------------------------

def audit_file(file_path):
    """Run all checks on one file. Returns list of Issue objects."""
    content = file_path.read_text(encoding="utf-8")
    lines   = content.splitlines()
    fm      = parse_frontmatter(content)
    issues  = []
    for fn in CHECKS:
        try:
            issues.extend(fn(file_path, content, lines, fm))
        except Exception as exc:
            issues.append(Issue("check_error", CAT_FORMAT, ERROR,
                                f"Check {fn.__name__} raised {type(exc).__name__}: {exc}"))
    return issues


def audit_directory(modular_dir):
    """
    Audit every guide .md in modular_dir.
    Returns dict: filename (str) -> list[Issue].
    """
    results = {}
    for path in sorted(modular_dir.glob("*.md")):
        if path.name in NON_GUIDE_FILES:
            continue
        results[path.name] = audit_file(path)
    return results


# ---------------------------------------------------------------------------
# Markdown report
# ---------------------------------------------------------------------------

def write_markdown_report(results, output_path, generated_date):
    total  = len(results)
    clean  = [f for f, iss in results.items() if not iss]
    dirty  = total - len(clean)
    flat   = [(f, i) for f, iss in results.items() for i in iss]
    n_err  = sum(1 for _, i in flat if i.severity == ERROR)
    n_warn = sum(1 for _, i in flat if i.severity == WARNING)
    n_def  = sum(1 for _, i in flat if i.severity == DEFERRED)

    by_cat = defaultdict(list)
    for fname, issue in flat:
        by_cat[issue.category].append((fname, issue))

    lines = []

    def w(*args):
        lines.append(" ".join(str(a) for a in args))

    w("# Guide Audit Report")
    w()
    w(f"Generated: {generated_date}")
    w()
    w("---")
    w()
    w("## Summary")
    w()
    w("| Metric | Count |")
    w("|--------|-------|")
    w(f"| Guides scanned | {total} |")
    w(f"| Guides with issues | {dirty} |")
    w(f"| Guides clean | {len(clean)} |")
    w(f"| Total issues | {len(flat)} |")
    w(f"| ❌ Errors (fix now) | {n_err} |")
    w(f"| ⚠️  Warnings (fix when touching) | {n_warn} |")
    w(f"| 📌 Deferred (tracked, low priority) | {n_def} |")
    w()
    w("---")
    w()
    w("## Issues by Category")
    w()

    for cat in CATEGORY_ORDER:
        items = by_cat.get(cat)
        if not items:
            continue
        w(f"### {cat}")
        w()
        w("| File | Line | Severity | Issue |")
        w("|------|------|----------|-------|")
        for fname, issue in sorted(items, key=lambda x: (SEVERITY_RANK[x[1].severity], x[0])):
            sev  = SEVERITY_LABEL[issue.severity]
            ln   = str(issue.line) if issue.line else "—"
            det  = issue.detail.replace("|", "\\|")
            w(f"| `{fname}` | {ln} | {sev} | {det} |")
        w()

    w("---")
    w()
    w("## Per-Guide Detail")
    w()
    for fname, issues in sorted(results.items()):
        if not issues:
            continue
        ec = sum(1 for i in issues if i.severity == ERROR)
        wc = sum(1 for i in issues if i.severity == WARNING)
        dc = sum(1 for i in issues if i.severity == DEFERRED)
        parts = []
        if ec: parts.append(f"{ec} error{'s' if ec > 1 else ''}")
        if wc: parts.append(f"{wc} warning{'s' if wc > 1 else ''}")
        if dc: parts.append(f"{dc} deferred")
        w(f"**`{fname}`** — {', '.join(parts)}")
        for issue in sorted(issues, key=lambda i: SEVERITY_RANK[i.severity]):
            icon = SEVERITY_LABEL[issue.severity].split()[0]
            ln   = f" *(line {issue.line})*" if issue.line else ""
            w(f"  - {icon} `{issue.check_id}` — {issue.detail}{ln}")
        w()

    w("---")
    w()
    w(f"## Clean Guides ({len(clean)})")
    w()
    w("No issues detected:")
    w()
    for f in sorted(clean):
        w(f"- `{f}`")
    w()

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  Markdown report → {output_path}")


# ---------------------------------------------------------------------------
# JSON report
# ---------------------------------------------------------------------------

def write_json_report(results, output_path, generated_date):
    flat = [(f, i) for f, iss in results.items() for i in iss]

    by_check = defaultdict(list)
    for fname, issue in flat:
        by_check[issue.check_id].append({"file": fname, **issue.to_dict()})

    guides_json = {}
    for fname, issues in results.items():
        guides_json[fname] = {
            "clean":          not issues,
            "issue_count":    len(issues),
            "error_count":    sum(1 for i in issues if i.severity == ERROR),
            "warning_count":  sum(1 for i in issues if i.severity == WARNING),
            "deferred_count": sum(1 for i in issues if i.severity == DEFERRED),
            "issues":         [i.to_dict() for i in
                               sorted(issues, key=lambda i: SEVERITY_RANK[i.severity])],
        }

    report = {
        "generated": generated_date,
        "summary": {
            "total_guides":       len(results),
            "guides_with_issues": sum(1 for iss in results.values() if iss),
            "guides_clean":       sum(1 for iss in results.values() if not iss),
            "total_issues":       len(flat),
            "error_count":        sum(1 for _, i in flat if i.severity == ERROR),
            "warning_count":      sum(1 for _, i in flat if i.severity == WARNING),
            "deferred_count":     sum(1 for _, i in flat if i.severity == DEFERRED),
        },
        "guides":   guides_json,
        "by_check": dict(by_check),
    }

    output_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"  JSON report    → {output_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Audit modular guide .md files against current standards."
    )
    parser.add_argument(
        "--modular-dir",
        type=Path,
        default=Path(__file__).parent.parent / "modular",
        help="Path to guides directory (default: ../modular relative to this script)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).parent,
        help="Where to write reports (default: same directory as this script)",
    )
    args = parser.parse_args()

    if not args.modular_dir.is_dir():
        print(f"Error: modular directory not found: {args.modular_dir}")
        return 1

    print(f"Auditing: {args.modular_dir}")
    results = audit_directory(args.modular_dir)

    today = date.today().isoformat()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    write_markdown_report(results, args.output_dir / "audit_report.md",   today)
    write_json_report    (results, args.output_dir / "audit_report.json",  today)

    total = len(results)
    clean = sum(1 for iss in results.values() if not iss)
    errs  = sum(1 for iss in results.values() for i in iss if i.severity == ERROR)
    warns = sum(1 for iss in results.values() for i in iss if i.severity == WARNING)
    defs  = sum(1 for iss in results.values() for i in iss if i.severity == DEFERRED)

    print()
    print(f"  {total} guides scanned — {clean} clean, {total - clean} with issues")
    print(f"  {errs} errors  |  {warns} warnings  |  {defs} deferred")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
