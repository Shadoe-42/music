#!/usr/bin/env python3
"""
generate_readme.py — Regenerate role-based module tables in modular/README.md
from YAML frontmatter.

Usage (from Music/ directory):
    python3 tooling/generate_readme.py          # update in place
    python3 tooling/generate_readme.py --dry-run # print generated section, no write

Architecture:
    extract_modules()  →  list of module dicts from YAML frontmatter
    organize_by_role() →  dict of role → sorted list of modules
    render_tables()    →  markdown string for the generated section
    update_readme()    →  in-place replacement between marker comments
"""

import os
import re
import sys

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

MODULAR_DIR = "modular"
README_PATH = os.path.join(MODULAR_DIR, "README.md")

MARKER_START = "<!-- GENERATED:role_tables:start -->"
MARKER_END   = "<!-- GENERATED:role_tables:end -->"

# Role display order and descriptions
ROLE_ORDER = [
    "SOURCE",
    "SHAPER",
    "AMPLIFIER",
    "MODULATOR",
    "CONTROLLER",
    "ROUTER",
    "ANALYZER",
    "EVENT_VOICE",
    "UTILITY",
]

ROLE_DESCRIPTIONS = {
    "SOURCE":      "Generates signal — audio, CV, gates, or noise.",
    "SHAPER":      "Transforms signal character — timbre, spectrum, space, texture.",
    "AMPLIFIER":   "Controls signal level — gain staging, mixing, dynamics.",
    "MODULATOR":   "Generates time-varying control signals — envelopes, LFOs, random, function generators.",
    "CONTROLLER":  "Defines timing, sequencing, and performance structure.",
    "ROUTER":      "Distributes, combines, switches, or applies logic to signal paths.",
    "ANALYZER":    "Observes, measures, and displays signal behavior.",
    "EVENT_VOICE": "Trigger-dependent sound engine with internally managed amplitude envelope.",
    "UTILITY":     "Multi-function, hybrid, or cross-category modules.",
}

# Common acronyms that should appear fully uppercase
ACRONYMS = {
    "vco", "lfo", "vca", "vcf", "fm", "cv", "adsr", "ar",
    "eq", "dsp", "midi", "usb", "dc", "fx",
}

# ---------------------------------------------------------------------------
# YAML parsing (stdlib only)
# ---------------------------------------------------------------------------

def parse_frontmatter(content):
    """Return dict of YAML frontmatter fields, or None if absent/unparseable."""
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    block = content[3:end].strip()
    result = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, rest = line.partition(":")
        rest = rest.strip()
        # Inline array: [a, b, c]
        if rest.startswith("[") and rest.endswith("]"):
            inner = rest[1:-1]
            result[key.strip()] = [
                v.strip().strip("'\"") for v in inner.split(",") if v.strip()
            ]
        else:
            result[key.strip()] = rest.strip().strip("'\"")
    return result


# ---------------------------------------------------------------------------
# Data extraction
# ---------------------------------------------------------------------------

def extract_modules(modular_dir):
    """
    Read all *_guide.md files in modular_dir and return a list of dicts:
        title, manufacturer, primary_role, functions, filename
    Skips files without parseable frontmatter or missing required fields.
    """
    modules = []
    for fname in os.listdir(modular_dir):
        if not fname.endswith("_guide.md"):
            continue
        path = os.path.join(modular_dir, fname)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        fm = parse_frontmatter(content)
        if not fm:
            continue
        role = fm.get("primary_role", "").strip().upper()
        title = fm.get("title", "").strip()
        if not role or not title:
            continue
        modules.append({
            "title":        title,
            "manufacturer": fm.get("manufacturer", "").strip(),
            "primary_role": role,
            "functions":    fm.get("functions", []),
            "filename":     fname,
        })
    return modules


# ---------------------------------------------------------------------------
# Data organization
# ---------------------------------------------------------------------------

def organize_by_role(modules):
    """
    Return dict of role → list of module dicts, sorted by title within each role.
    Roles not in ROLE_ORDER are placed in a catch-all bucket at the end.
    """
    by_role = {role: [] for role in ROLE_ORDER}
    other = {}

    for m in modules:
        role = m["primary_role"]
        if role in by_role:
            by_role[role].append(m)
        else:
            other.setdefault(role, []).append(m)

    # Sort each role's list by title (case-insensitive)
    for role in by_role:
        by_role[role].sort(key=lambda m: m["title"].lower())
    for role in other:
        other[role].sort(key=lambda m: m["title"].lower())

    return by_role, other


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def format_term(term):
    """
    Format a single functions vocabulary term for display.
    'clock-divider' → 'Clock Divider'
    'vco'           → 'VCO'
    'fm-oscillator' → 'FM Oscillator'
    """
    words = term.replace("-", " ").split()
    return " ".join(w.upper() if w.lower() in ACRONYMS else w.title() for w in words)


def format_functions(func_list):
    """
    Format the functions list into a readable one-line description.
    ['vco', 'fm']              → 'VCO, FM'
    ['clock-divider']          → 'Clock Divider'
    ['filter', 'wavefolder']   → 'Filter, Wavefolder'
    Empty list returns an em-dash placeholder.
    """
    if not func_list:
        return "—"
    return ", ".join(format_term(t) for t in func_list)


def render_tables(by_role, other):
    """
    Render the complete generated section as a markdown string.
    Wrapped in the MARKER comments.
    """
    lines = [MARKER_START]

    roles_to_render = [(r, by_role[r]) for r in ROLE_ORDER if by_role.get(r)]
    for role, unknown_role in other.items():
        roles_to_render.append((role, unknown_role))

    for i, (role, modules) in enumerate(roles_to_render):
        desc = ROLE_DESCRIPTIONS.get(role, "")
        lines.append(f"### {role}")
        if desc:
            lines.append(f"*{desc}*")
        lines.append("")
        lines.append("| Module | Function | Guide |")
        lines.append("|--------|----------|-------|")
        for m in modules:
            func_str = format_functions(m["functions"])
            guide_link = f"[Guide]({m['filename']})"
            lines.append(f"| {m['title']} | {func_str} | {guide_link} |")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append(MARKER_END)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# README update
# ---------------------------------------------------------------------------

def update_readme(readme_path, generated_section, dry_run=False):
    """
    Replace the content between marker comments in readme_path with
    generated_section.  Returns (changed: bool, message: str).
    """
    with open(readme_path, encoding="utf-8") as f:
        content = f.read()

    if MARKER_START not in content or MARKER_END not in content:
        return False, (
            f"Markers not found in {readme_path}.\n"
            f"Add '{MARKER_START}' and '{MARKER_END}' to mark the generated region."
        )

    pattern = re.compile(
        re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
        re.DOTALL,
    )
    new_content = pattern.sub(generated_section, content)

    if new_content == content:
        return False, "No changes — generated output matches existing content."

    if not dry_run:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True, f"Updated {readme_path}."
    else:
        # Print the generated section for review
        print(generated_section)
        return True, "(dry-run) Changes would be written."


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    dry_run = "--dry-run" in sys.argv

    # Resolve paths relative to the Music/ directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    music_dir  = os.path.dirname(script_dir)
    os.chdir(music_dir)

    modules = extract_modules(MODULAR_DIR)
    if not modules:
        print("ERROR: No modules found. Check MODULAR_DIR path.", file=sys.stderr)
        sys.exit(1)

    by_role, other = organize_by_role(modules)

    if other:
        print(f"WARNING: {sum(len(v) for v in other.values())} module(s) have "
              f"unrecognized roles: {list(other.keys())}", file=sys.stderr)

    generated = render_tables(by_role, other)
    changed, msg = update_readme(README_PATH, generated, dry_run=dry_run)
    print(msg)

    # Summary
    total = sum(len(v) for v in by_role.values())
    print(f"{total} modules across {sum(1 for v in by_role.values() if v)} roles.")


if __name__ == "__main__":
    main()
