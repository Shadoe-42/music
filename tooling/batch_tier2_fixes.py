#!/usr/bin/env python3
"""
Batch Tier 2 mechanical fixes for modular guides.

Reads guide_triage_2026.md to identify Tier 2 guides, then applies
mechanical fixes that do not require content rewriting.

Changes applied:
  1. ### / #### sub-headings inside Why Excels, ALP, Pairs Well With → **bold**
  2. ## Why [anything] → ## Why This Instrument Excels  (unless already correct)
  3. ## Beginner Patch Ideas → ## Patches
  4. ## Beginner Gotchas... → ## Common Mistakes
  5. **Bottom Line:** lines → removed
  6. Emoji stripped from heading lines (##, ###, ####)
  7. ## Advanced Techniques / Learning Path / variant → ## Advanced Learning Path
  8. ## **Advanced Learning Path** → ## Advanced Learning Path  (remove bold from heading)
  9. # Title - Guide → # Title  (residual title suffix fix)

Usage (from Music/ directory):
    python3 tooling/batch_tier2_fixes.py            # dry run — shows counts only
    python3 tooling/batch_tier2_fixes.py --apply    # writes changes
    python3 tooling/batch_tier2_fixes.py --diff     # shows unified diff per file
"""

import argparse
import difflib
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

TRIAGE_REPORT  = Path("tooling/guide_triage_2026.md")
MODULAR_DIR    = Path("modular")

# Sections where ### / #### headings should become **bold**
FLATTEN_SECTIONS = [
    r"^## why\b",
    r"^## (?:advanced learning|learning path|advanced techniques|multi-function learning|modular learning path)",
    r"^## (?:pairs well|works well)",
]

# ALP variant headings (besides the main pattern above) that should normalize
ALP_VARIANTS = re.compile(
    r"^## (?:advanced techniques|learning path|multi-function learning path|modular learning path)\s*$",
    re.IGNORECASE,
)
ALP_BOLD = re.compile(r"^## \*\*advanced learning path\*\*\s*$", re.IGNORECASE)

# Why Excels: any "## Why ..." that isn't already the correct form
WHY_CORRECT   = re.compile(r"^## why this instrument excels\s*$", re.IGNORECASE)
WHY_ANY       = re.compile(r"^## why\b", re.IGNORECASE)

# Patch section heading normalization
BEGINNER_PATCHES = re.compile(r"^## beginner patch ideas\s*$", re.IGNORECASE)
BEGINNER_GOTCHAS = re.compile(r"^## beginner.{0,20}gotcha.*$", re.IGNORECASE)

# Bottom Line removal (whole line)
BOTTOM_LINE = re.compile(r"^\*{0,2}bottom line\b", re.IGNORECASE)

# Title suffix: "# Some Title - Guide"
TITLE_SUFFIX = re.compile(r"^(# .+) - guide\s*$", re.IGNORECASE)

# Emoji range — covers most common Unicode emoji blocks
EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"   # Misc symbols, emoticons, transport, etc.
    "\u2600-\u27BF"            # Misc symbols
    "\u2B00-\u2BFF"            # Misc symbols
    "\uFE00-\uFE0F"            # Variation selectors
    "\u2300-\u23FF"            # Technical symbols
    "⚠️"
    "]+",
    flags=re.UNICODE,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_tier2_guides(triage_path: Path) -> set:
    """Return set of filenames classified as Tier 2 in the triage report."""
    content = triage_path.read_text(encoding="utf-8")
    tier2_start = content.find("## Tier 2")
    # Tier 2 ends at the next ## section (Tier 1, Clean, or end)
    tier2_end = len(content)
    for marker in ("## Tier 1", "## Clean"):
        pos = content.find(marker, tier2_start + 1)
        if pos != -1 and pos < tier2_end:
            tier2_end = pos
    if tier2_start == -1:
        sys.exit("ERROR: Could not locate Tier 2 section in triage report.")
    tier2_block = content[tier2_start:tier2_end]
    return set(re.findall(r"`([^`]+\.md)`", tier2_block))


def is_in_flatten_section(line: str, section_pattern_compiled) -> bool:
    return bool(section_pattern_compiled.search(line))


def flatten_heading(line: str) -> str:
    """Convert a ### or #### heading line to **bold** text."""
    # Strip heading markers
    text = re.sub(r"^#{3,4}\s+", "", line).rstrip()
    if not text:
        return ""
    # If already starts with **, leave the bold as-is (may be **text** or **text:**)
    if text.startswith("**"):
        return text
    # Otherwise wrap in bold
    return f"**{text}**"


def strip_emoji_from_heading(line: str) -> str:
    """Remove emoji from a heading line, cleaning up extra spaces."""
    stripped = EMOJI_RE.sub("", line.rstrip())
    # Clean up any double spaces left behind
    stripped = re.sub(r"  +", " ", stripped)
    # Clean up "**  Text**" type artifacts
    stripped = re.sub(r"\*\*\s+", "**", stripped)
    return stripped


def apply_fixes(lines: list[str]) -> tuple[list[str], dict]:
    """Apply all mechanical fixes to a list of lines. Returns (new_lines, change_counts)."""
    counts = {
        "flatten_heading":   0,
        "why_normalized":    0,
        "beginner_patches":  0,
        "beginner_gotchas":  0,
        "bottom_line":       0,
        "emoji_heading":     0,
        "alp_variant":       0,
        "title_suffix":      0,
    }

    # Compile flatten-section patterns once
    flatten_compiled = re.compile(
        "|".join(FLATTEN_SECTIONS),
        re.IGNORECASE,
    )

    result = []
    in_flatten_section = False

    for line in lines:
        # Track which ## section we are in
        if re.match(r"^## ", line):
            in_flatten_section = bool(flatten_compiled.search(line))

        # ----------------------------------------------------------------
        # 1. Flatten ### / #### headings inside target sections
        # ----------------------------------------------------------------
        if in_flatten_section and re.match(r"^#{3,4}\s+", line):
            new_text = flatten_heading(line)
            if new_text:
                result.append(new_text + "\n")
            counts["flatten_heading"] += 1
            continue

        # ----------------------------------------------------------------
        # 2. Normalize Why Excels heading
        # ----------------------------------------------------------------
        if WHY_ANY.match(line) and not WHY_CORRECT.match(line):
            result.append("## Why This Instrument Excels\n")
            counts["why_normalized"] += 1
            continue

        # ----------------------------------------------------------------
        # 3. Beginner Patch Ideas → Patches
        # ----------------------------------------------------------------
        if BEGINNER_PATCHES.match(line):
            result.append("## Patches\n")
            counts["beginner_patches"] += 1
            continue

        # ----------------------------------------------------------------
        # 4. Beginner Gotchas → Common Mistakes
        # ----------------------------------------------------------------
        if BEGINNER_GOTCHAS.match(line):
            result.append("## Common Mistakes\n")
            counts["beginner_gotchas"] += 1
            continue

        # ----------------------------------------------------------------
        # 5. Remove Bottom Line lines
        # ----------------------------------------------------------------
        if BOTTOM_LINE.match(line.strip()):
            counts["bottom_line"] += 1
            continue  # skip the line entirely

        # ----------------------------------------------------------------
        # 6. Strip emoji from heading lines
        # ----------------------------------------------------------------
        if re.match(r"^#{1,4}\s+", line) and EMOJI_RE.search(line):
            new_line = strip_emoji_from_heading(line) + "\n"
            if new_line != line:
                result.append(new_line)
                counts["emoji_heading"] += 1
                continue

        # ----------------------------------------------------------------
        # 7. ALP variant headings → ## Advanced Learning Path
        # ----------------------------------------------------------------
        if ALP_VARIANTS.match(line) or ALP_BOLD.match(line):
            result.append("## Advanced Learning Path\n")
            counts["alp_variant"] += 1
            continue

        # ----------------------------------------------------------------
        # 8. Title suffix: "# Some Title - Guide" → "# Some Title"
        # ----------------------------------------------------------------
        m = TITLE_SUFFIX.match(line)
        if m:
            result.append(m.group(1) + "\n")
            counts["title_suffix"] += 1
            continue

        result.append(line)

    return result, counts


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Batch Tier 2 mechanical fixes")
    parser.add_argument("--apply", action="store_true", help="Write changes to disk")
    parser.add_argument("--diff",  action="store_true", help="Print unified diff per file")
    args = parser.parse_args()

    if not TRIAGE_REPORT.exists():
        sys.exit(f"ERROR: {TRIAGE_REPORT} not found. Run triage_guides.py first.")

    tier2_guides = load_tier2_guides(TRIAGE_REPORT)
    print(f"Tier 2 guides identified: {len(tier2_guides)}")

    total_files_changed = 0
    total_changes       = {}

    for filename in sorted(tier2_guides):
        path = MODULAR_DIR / filename
        if not path.exists():
            print(f"  SKIP (not found): {filename}")
            continue

        original = path.read_text(encoding="utf-8")
        lines    = original.splitlines(keepends=True)

        new_lines, counts = apply_fixes(lines)
        new_content = "".join(new_lines)

        changed = new_content != original
        file_total = sum(counts.values())

        if changed:
            total_files_changed += 1
            for k, v in counts.items():
                total_changes[k] = total_changes.get(k, 0) + v

            print(f"\n  {filename}")
            for k, v in counts.items():
                if v:
                    print(f"    {v:3d}  {k}")

            if args.diff:
                diff = difflib.unified_diff(
                    original.splitlines(keepends=True),
                    new_lines,
                    fromfile=f"a/{filename}",
                    tofile=f"b/{filename}",
                    n=2,
                )
                print("".join(diff))

            if args.apply:
                path.write_text(new_content, encoding="utf-8")

    print(f"\n{'─'*50}")
    print(f"Files with changes: {total_files_changed} / {len(tier2_guides)}")
    if total_changes:
        print("Change totals:")
        for k, v in sorted(total_changes.items(), key=lambda x: -x[1]):
            if v:
                print(f"  {v:4d}  {k}")
    if not args.apply:
        print("\n(Dry run — no files written. Pass --apply to apply changes.)")


if __name__ == "__main__":
    main()
