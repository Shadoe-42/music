#!/usr/bin/env python3
"""
Guide Triage Script — Phase 2 of the generational cleanup plan.

Grades all modular guides against tooling/triage_rubric.md and assigns each
a tier for the generational cleanup project.

    Tier 3: Full rebuild required
    Tier 2: Structural cleanup — one dedicated session
    Tier 1: Surface/cosmetic fixes — batchable
    Clean:  No issues detected

Usage (from Music/ directory):
    python3 tooling/triage_guides.py
    python3 tooling/triage_guides.py --modular-dir path/to/modular --output-dir path/to/tooling

Output:
    tooling/guide_triage_2026.md
"""

import argparse
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Confirmed Tier 3 from prior session review — skip re-triage, mark directly
# NOTE: Cleared 2026-04-28 — all four previously confirmed guides have been
# fully rebuilt to current spec. Let the script evaluate them fresh.
CONFIRMED_TIER_3 = {}

NON_GUIDE_FILES = {
    "README.md",
    "pkhia_corrections.md",
    "semi_modular_integration_guide.md",
}

# Anchor sections in required canonical order
ANCHOR_DEFINITIONS = [
    ("quick_start",        r"^## quick start"),
    ("why_excels",         r"^## why\b"),
    ("historical_context", r"^## historical context"),
    ("essential_params",   r"^## essential param"),
    ("patches",            r"^## (?:patch(?:es)?(?:\s|$)|progressive patch|beginner patch)"),
    ("common_mistakes",    r"^## (?:common mistakes|beginner.{0,15}gotcha)"),
    ("alp",                r"^## (?:advanced learning|learning path|advanced techniques)"),
    ("pairs_well",         r"^## (?:pairs well|works well)"),
]

# Phase 2 / ecosystem-framing detection phrases
PHASE2_PHRASES = [
    r"\bphase 2\b",
    r"phase 2 ecosystem",
    r"advanced ecosystem",
    r"under your (?:creative )?(?:direction|guidance)",
    r"guide sophisticated",
    r"transforms .{5,40} intelligence",
    r"pattern generation systems?",
]

# Old-generation ALP sub-section headings: (pattern, readable_name)
# Patterns require bold heading format (**text:**) to avoid matching prose.
ALP_SUBSECTION_HEADINGS = [
    (r"^\*\*recommended study progression\*\*",  "Recommended Study Progression"),
    (r"^\*\*cross-?module learning",             "Cross-Module Learning Opportunities"),
    (r"^\*\*skill development milestones\*\*",   "Skill Development Milestones"),
    (r"^\*\*performance applications\*\*",       "Performance Applications"),
    (r"^\*\*advanced .{3,30} concepts\*\*",      "Advanced [X] Concepts"),
]

# Old-generation patch table column headers (Tier 3 signal)
# Must appear as actual table cells (surrounded by | delimiters)
TIER3_TABLE_COLUMNS = [
    r"\|\s*advanced synergy\s*\|",
    r"\|\s*advanced concept\s*\|",
    r"\|\s*algorithmic synergy\s*\|",
    r"\|\s*organic result\s*\|",
    r"\|\s*mathematical synergy\s*\|",
    r"\|\s*phase 2 integration\s*\|",
    r"\|\s*phase 2 synergy\s*\|",
]

# Cosmetic markers (Tier 1 only)
COSMETIC_CHECKS = [
    ("beginners_title",   r"beginner'?s?\s+guide",                 "title/heading contains 'Beginner's Guide'"),
    ("guide_suffix",      r"^# .+ - guide\s*$",                   "H1 title has ' - Guide' suffix"),
    ("big_six",           r"\bthe big 6\b",                        "Essential Parameters heading says 'The Big 6'"),
    ("beginner_patches",  r"^## beginner patch ideas",             "patch section named 'Beginner Patch Ideas'"),
    ("beginner_gotchas",  r"^## beginner.{0,15}gotcha",           "section named 'Beginner Gotchas & Pro Tips'"),
    ("bottom_line",       r"^\*{0,2}bottom line\b",               "'Bottom Line:' closing paragraph present"),
    ("emoji_headings",    r"^#{1,3}[^#].*[⚠️🎵🔴🔵🟡🏠🎛️📚🎭🎸🔊🏴🥁🎹🌌🔬🎶🎼]", "emoji present in a heading"),
    ("why_full_mfr",      r"^## why (?:mutable instruments?|rossum|blue lantern|make noise|"
                          r"noise engineering|doepfer|intellijel|erica synths?|endorphin|"
                          r"cre8audio|4ms|qubit|alm busy|divkid|instruo|squarp|tiptop|"
                          r"winterbloom|patching panda|bizarre jezabel|behringer|mordax|soma|"
                          r"atovproject|expert sleepers|after later)",
                          "Why heading uses full manufacturer name instead of 'Why This Instrument Excels'"),
    ("alp_bold_heading",  r"^#+\s+\*\*.*learning path.*\*\*",    "ALP heading has bold formatting inside it"),
    ("key_specs_bullets", r"^- \*\*(?:width|depth|power|hp):\*\*", "Key Specs uses old bullet format instead of table"),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_frontmatter(content):
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


def get_headings(lines):
    """Return list of (lineno, level, text) for all ATX headings."""
    result = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            result.append((i, len(m.group(1)), m.group(2).strip()))
    return result


def get_section_lines(lines, pattern):
    """
    Return body lines of the first section whose ## heading matches pattern.
    Stops at the next ## heading (exclusive). Returns [] if not found.
    """
    in_section = False
    result = []
    for line in lines:
        if re.match(r"^## ", line):
            if re.search(pattern, line, re.IGNORECASE):
                in_section = True
                result = []
                continue
            elif in_section:
                break
        if in_section:
            result.append(line)
    return result


def section_text(lines, pattern):
    return "\n".join(get_section_lines(lines, pattern))


# ---------------------------------------------------------------------------
# Anchor section detection
# ---------------------------------------------------------------------------

def detect_anchors(lines):
    """
    Returns:
        present  — dict: anchor_key -> line_number
        missing  — list of anchor keys not found
        seq      — list of anchor keys in the order they appear
    """
    present = {}
    seq = []
    for i, line in enumerate(lines, 1):
        for key, pattern in ANCHOR_DEFINITIONS:
            if key not in present and re.match(pattern, line, re.IGNORECASE):
                present[key] = i
                seq.append(key)
    missing = [k for k, _ in ANCHOR_DEFINITIONS if k not in present]
    return present, missing, seq


# ---------------------------------------------------------------------------
# Tier 3 detection
# ---------------------------------------------------------------------------

def t3_broken_patch_numbers(headings):
    """Duplicate patch numbers in headings."""
    nums = []
    for _, level, text in headings:
        m = re.search(r"\bpatch\s+(\d+)\b", text, re.IGNORECASE)
        if m:
            nums.append(int(m.group(1)))
    if len(nums) < 2:
        return False, []
    dupes = sorted({n for n in nums if nums.count(n) > 1})
    return bool(dupes), dupes


def t3_old_table_columns(content):
    """Patch tables contain old-gen column headers."""
    found = []
    for p in TIER3_TABLE_COLUMNS:
        if re.search(p, content, re.IGNORECASE):
            found.append(re.search(p, content, re.IGNORECASE).group())
    return bool(found), found


def t3_alp_no_numbered_list(lines):
    """
    ALP section has old-gen sub-sections AND no numbered list at all.
    If there IS a numbered list, the ALP is salvageable (Tier 2).
    """
    alp = get_section_lines(lines, r"^## (?:advanced learning|learning path|advanced techniques)")
    if not alp:
        return False, []
    alp_text = "\n".join(alp)
    found_subs = [name for pat, name in ALP_SUBSECTION_HEADINGS
                  if re.search(pat, alp_text, re.IGNORECASE | re.MULTILINE)]
    has_numbered = bool(re.search(r"^\d+\.", alp_text, re.MULTILINE))
    if found_subs and not has_numbered:
        return True, found_subs
    return False, found_subs


def t3_why_excels_phase2(lines):
    """
    Why Excels section is organized around Phase 2 ecosystem framing
    (2+ distinct patterns present = the organizing logic, not incidental).
    """
    why_text = section_text(lines, r"^## why\b")
    if not why_text:
        return False, []
    matches = [p for p in PHASE2_PHRASES if re.search(p, why_text, re.IGNORECASE)]
    return len(matches) >= 2, matches


# ---------------------------------------------------------------------------
# Tier 2 detection
# ---------------------------------------------------------------------------

def t2_why_excels_subsections(lines):
    """Why Excels section contains ### sub-headings."""
    why_lines = get_section_lines(lines, r"^## why\b")
    return any(line.startswith("###") for line in why_lines)


def t2_alp_subsections_with_numbered(lines):
    """
    ALP has old-gen sub-section headings but ALSO has a numbered list
    (content is present and salvageable with editing).
    Returns (bool, list_of_found_patterns).
    """
    alp = get_section_lines(lines, r"^## (?:advanced learning|learning path|advanced techniques)")
    if not alp:
        return False, []
    alp_text = "\n".join(alp)
    found_subs = [name for pat, name in ALP_SUBSECTION_HEADINGS
                  if re.search(pat, alp_text, re.IGNORECASE | re.MULTILINE)]
    # Also flag any ### headings inside ALP even without named patterns
    has_any_hash3 = any(line.startswith("###") for line in alp)
    has_numbered = bool(re.search(r"^\d+\.", alp_text, re.MULTILINE))
    if (found_subs or has_any_hash3) and has_numbered:
        subs_report = found_subs if found_subs else ["### sub-headings present"]
        return True, subs_report
    return False, []


def t2_pairs_subheaders(lines):
    """Pairs Well With section has ### sub-headers."""
    pairs_lines = get_section_lines(lines, r"^## (?:pairs well|works well)")
    return any(line.startswith("###") for line in pairs_lines)


def t2_phase2_in_patches(lines):
    """
    Phase 2 / ecosystem framing in the patches section.
    Returns count of matching phrases (≥4 = pervasive Tier 2, 1-3 = Tier 1 flag).
    """
    patches_text = section_text(lines, r"^## (?:patch(?:es)?(?:\s|$)|progressive patch|beginner patch)")
    if not patches_text:
        return 0
    count = sum(
        len(re.findall(p, patches_text, re.IGNORECASE))
        for p in PHASE2_PHRASES
    )
    return count


# ---------------------------------------------------------------------------
# Cosmetic checks (Tier 1)
# ---------------------------------------------------------------------------

def check_cosmetics(lines):
    """Return list of (key, description) for cosmetic issues found."""
    found = []
    for key, pattern, description in COSMETIC_CHECKS:
        for line in lines:
            if re.search(pattern, line, re.IGNORECASE):
                found.append((key, description))
                break
    return found


# ---------------------------------------------------------------------------
# HC status
# ---------------------------------------------------------------------------

def hc_status(lines, fm):
    if str(fm.get("historical_context", "")).strip().lower() == "false":
        return "suppressed (historical_context: false)"
    for line in lines:
        if re.match(r"^## historical context", line, re.IGNORECASE):
            return "written"
    return "needed"


# ---------------------------------------------------------------------------
# Main grading function
# ---------------------------------------------------------------------------

def grade_guide(file_path):
    content = file_path.read_text(encoding="utf-8")
    lines   = content.splitlines()
    fm      = parse_frontmatter(content)
    headings = get_headings(lines)

    result = {
        "filename":        file_path.name,
        "tier":            None,
        "tier3_signals":   [],
        "tier2_signals":   [],
        "tier1_signals":   [],
        "missing_anchors": [],
        "hc_status":       hc_status(lines, fm),
        "notes":           [],
    }

    # Pre-confirmed — no need to re-analyse
    if file_path.name in CONFIRMED_TIER_3:
        result["tier"] = 3
        result["notes"].append("Pre-confirmed Tier 3 from prior session review.")
        return result

    # --- Anchor section inventory ---
    _, missing, _ = detect_anchors(lines)
    # If historical_context is suppressed via YAML, do not count it as missing
    if str(fm.get("historical_context", "")).strip().lower() == "false":
        missing = [m for m in missing if m != "historical_context"]
    result["missing_anchors"] = missing

    # --- Tier 3 signals ---

    if len(missing) >= 3:
        result["tier3_signals"].append(
            f"{len(missing)} anchor sections missing: {', '.join(missing)}"
        )

    broken, dupes = t3_broken_patch_numbers(headings)
    if broken:
        result["tier3_signals"].append(f"Duplicate patch numbers detected: {dupes}")

    has_cols, cols = t3_old_table_columns(content)
    if has_cols:
        result["tier3_signals"].append(
            f"Old-gen table column headers present: {', '.join(cols)}"
        )

    alp_t3, alp_t3_subs = t3_alp_no_numbered_list(lines)
    if alp_t3:
        result["tier3_signals"].append(
            f"ALP has only sub-sections, no numbered list "
            f"(found: {', '.join(alp_t3_subs)})"
        )

    why_t3, why_t3_patterns = t3_why_excels_phase2(lines)
    if why_t3:
        result["tier3_signals"].append(
            f"Why Excels is organized around Phase 2 ecosystem framing "
            f"({len(why_t3_patterns)} patterns matched)"
        )

    # --- Tier 2 signals (evaluated regardless of Tier 3 — gives full picture) ---

    if 1 <= len(missing) <= 2:
        result["tier2_signals"].append(
            f"{len(missing)} anchor section(s) missing: {', '.join(missing)}"
        )

    if t2_why_excels_subsections(lines):
        result["tier2_signals"].append("Why Excels section contains ### sub-headings")

    alp_t2, alp_t2_subs = t2_alp_subsections_with_numbered(lines)
    if alp_t2:
        result["tier2_signals"].append(
            f"ALP has sub-sections but numbered list is present (salvageable): "
            f"{', '.join(alp_t2_subs)}"
        )

    if t2_pairs_subheaders(lines):
        result["tier2_signals"].append("Pairs Well With section has ### sub-headers")

    phase2_count = t2_phase2_in_patches(lines)
    if phase2_count >= 4:
        result["tier2_signals"].append(
            f"Phase 2 / ecosystem framing pervasive in patches section "
            f"({phase2_count} phrase matches)"
        )
    elif phase2_count >= 1:
        result["tier1_signals"].append(
            f"Phase 2 framing present in patches section "
            f"({phase2_count} phrase match{'es' if phase2_count > 1 else ''}) — flag for review"
        )

    # --- Tier 1 cosmetic signals ---

    for key, description in check_cosmetics(lines):
        result["tier1_signals"].append(description)

    # --- Assign tier ---
    if result["tier3_signals"]:
        result["tier"] = 3
    elif result["tier2_signals"]:
        result["tier"] = 2
    elif result["tier1_signals"]:
        result["tier"] = 1
    else:
        result["tier"] = 0

    return result


# ---------------------------------------------------------------------------
# Report writer
# ---------------------------------------------------------------------------

def write_triage_report(results, output_path, generated_date):
    tier_counts = defaultdict(int)
    for r in results:
        tier_counts[r["tier"]] += 1

    out = []

    def w(text=""):
        out.append(text)

    w("# Guide Triage Report 2026")
    w()
    w(f"Generated: {generated_date}")
    w(f"Rubric: `tooling/triage_rubric.md`")
    w()
    w("---")
    w()
    w("## Summary")
    w()
    w("| Tier | Count | Description |")
    w("|------|-------|-------------|")
    w(f"| Tier 3 | {tier_counts[3]} | Full rebuild required |")
    w(f"| Tier 2 | {tier_counts[2]} | Structural cleanup — one session per guide |")
    w(f"| Tier 1 | {tier_counts[1]} | Surface fixes — batchable |")
    w(f"| Clean  | {tier_counts[0]} | No issues detected |")
    w(f"| **Total** | **{len(results)}** | |")
    w()
    w("---")
    w()

    tier_labels = {
        3: "Tier 3 — Full Rebuild Required",
        2: "Tier 2 — Structural Cleanup",
        1: "Tier 1 — Surface Fixes (Batchable)",
        0: "Clean — No Issues Detected",
    }

    for tier in [3, 2, 1, 0]:
        tier_results = sorted(
            [r for r in results if r["tier"] == tier],
            key=lambda x: x["filename"]
        )
        if not tier_results:
            continue

        w(f"## {tier_labels[tier]} ({len(tier_results)})")
        w()

        for r in tier_results:
            w(f"### `{r['filename']}`")
            w()
            w(f"**HC status:** {r['hc_status']}")

            if r["missing_anchors"]:
                w(f"**Missing anchor sections:** {', '.join(r['missing_anchors'])}")

            if r["tier3_signals"]:
                w()
                w("**Tier 3 signals:**")
                for sig in r["tier3_signals"]:
                    w(f"- {sig}")

            if r["tier2_signals"]:
                w()
                w("**Tier 2 signals:**")
                for sig in r["tier2_signals"]:
                    w(f"- {sig}")

            if r["tier1_signals"]:
                w()
                w("**Tier 1 (cosmetic) signals:**")
                for sig in r["tier1_signals"]:
                    w(f"- {sig}")

            if r["notes"]:
                w()
                w("**Notes:**")
                for note in r["notes"]:
                    w(f"- {note}")

            if tier == 0:
                w()
                w("No issues detected.")

            w()

    w("---")
    w()
    w("*For the full standards audit, run `python3 tooling/audit_guides.py`.*")
    w("*This triage report focuses on generational rebuild prioritization only.*")

    output_path.write_text("\n".join(out), encoding="utf-8")
    print(f"  Triage report  → {output_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Triage modular guides for the generational cleanup project."
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
        help="Where to write the triage report (default: same directory as this script)",
    )
    args = parser.parse_args()

    if not args.modular_dir.is_dir():
        print(f"Error: modular directory not found: {args.modular_dir}")
        return 1

    print(f"Triaging: {args.modular_dir}")

    results = []
    for path in sorted(args.modular_dir.glob("*.md")):
        if path.name in NON_GUIDE_FILES:
            continue
        results.append(grade_guide(path))

    today = date.today().isoformat()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_triage_report(results, args.output_dir / "guide_triage_2026.md", today)

    tier_counts = defaultdict(int)
    for r in results:
        tier_counts[r["tier"]] += 1

    print()
    print(f"  {len(results)} guides triaged")
    print(f"  Tier 3 (full rebuild):  {tier_counts[3]}")
    print(f"  Tier 2 (cleanup):       {tier_counts[2]}")
    print(f"  Tier 1 (cosmetic):      {tier_counts[1]}")
    print(f"  Clean:                  {tier_counts[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
