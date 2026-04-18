#!/usr/bin/env python3
"""
Convert Key Specifications from bullet format to | Spec | Value | table.

Handles three power formats found in the guides:
  "52mA @ +12V / 15mA @ -12V / 0mA @ +5V"  →  "+52mA / -15mA"
  "+12V: 50mA / -12V: 10mA"                 →  "+50mA / -10mA"
  "+52mA / -15mA"                            →  (already correct, unchanged)

Usage (from Music/ directory):
    python3 tooling/fix_key_specs.py            # dry run
    python3 tooling/fix_key_specs.py --apply    # write changes
"""

import argparse
import re
from pathlib import Path

MODULAR_DIR = Path("modular")

# Guides confirmed to have Key Specs in bullet format
TARGET_GUIDES = [
    "4ms_scm_plus_guide.md",
    "blue_lantern_astroid_guide.md",
    "blue_lantern_cmos_party_guide.md",
    "dspcoffee_kali_guide.md",
    "endorphines_ground_control_guide.md",
    "erica_synths_pico_dsp_guide.md",
    "make_noise_maths_guide.md",
]

# ---------------------------------------------------------------------------
# Spec value normalizers
# ---------------------------------------------------------------------------

def normalize_width(val: str) -> str:
    """'12 HP' → '12HP'  |  '⚠️ ...' left as-is."""
    return re.sub(r"\s+(?=HP)", "", val)


def normalize_depth(val: str) -> str:
    """'24 mm (0.95")' → '24mm'  |  '35mm' unchanged."""
    # Strip parenthetical imperial annotation
    val = re.sub(r"\s*\([^)]*\"\)", "", val)
    # Remove space before mm
    val = re.sub(r"\s+(?=mm)", "", val)
    return val.strip()


def normalize_power(val: str) -> str:
    """Normalize the three power formats to '+XmA / -YmA'."""
    # Pattern A: "52mA @ +12V / 15mA @ -12V [/ 0mA @ +5V]"
    m = re.match(
        r"(\d+)\s*mA?\s*@\s*\+12V\s*/\s*(\d+)\s*mA?\s*@\s*-12V",
        val,
        re.IGNORECASE,
    )
    if m:
        pos, neg = m.group(1), m.group(2)
        neg_str = f"-{neg}mA" if neg != "0" else "0mA"
        return f"+{pos}mA / {neg_str}"

    # Pattern B: "+12V: 50mA / -12V: 10mA"
    m = re.match(
        r"\+12V:\s*(\d+)\s*mA?\s*/\s*-12V:\s*(\d+)\s*mA?",
        val,
        re.IGNORECASE,
    )
    if m:
        pos, neg = m.group(1), m.group(2)
        neg_str = f"-{neg}mA" if neg != "0" else "0mA"
        return f"+{pos}mA / {neg_str}"

    # Pattern C: already "+50mA / -10mA" — leave as-is
    return val.strip()


NORMALIZERS = {
    "width": normalize_width,
    "depth": normalize_depth,
    "power": normalize_power,
}


def normalize_spec_value(name: str, value: str) -> str:
    key = name.lower().strip()
    fn = NORMALIZERS.get(key)
    return fn(value) if fn else value.strip()


# ---------------------------------------------------------------------------
# Block detection and conversion
# ---------------------------------------------------------------------------

def bullet_to_table(block_lines: list[str]) -> list[str]:
    """
    Convert a list of bullet lines like:
        - **Width:** 12HP
    to a markdown table.
    Returns the table as a list of lines (with newlines).
    """
    rows = []
    for line in block_lines:
        m = re.match(r"-\s+\*\*([^*]+)\*\*:?\s*(.*)", line.rstrip())
        if not m:
            continue
        name  = m.group(1).strip().rstrip(":")
        value = normalize_spec_value(name, m.group(2))
        rows.append((name, value))

    if not rows:
        return block_lines  # unchanged if nothing matched

    table = [
        "| Spec | Value |\n",
        "|------|-------|\n",
    ]
    for name, value in rows:
        table.append(f"| {name} | {value} |\n")
    return table


def convert_key_specs(text: str) -> tuple[str, bool]:
    """
    Find the **Key Specifications:** block and convert bullets to table.
    Returns (new_text, changed).
    """
    # Match: **Key Specifications:**\n followed by one or more bullet lines
    pattern = re.compile(
        r"(\*\*Key Specifications:\*\*\n)"
        r"((?:-\s+\*\*[^\n]+\n)+)",
        re.MULTILINE,
    )

    def replace(m):
        header      = m.group(1)          # "**Key Specifications:**\n"
        bullet_text = m.group(2)
        bullet_lines = bullet_text.splitlines(keepends=True)
        table_lines  = bullet_to_table(bullet_lines)
        return header + "\n" + "".join(table_lines)

    new_text, n = pattern.subn(replace, text)
    return new_text, n > 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Convert Key Specs bullets to table")
    parser.add_argument("--apply", action="store_true", help="Write changes to disk")
    args = parser.parse_args()

    for filename in TARGET_GUIDES:
        path = MODULAR_DIR / filename
        if not path.exists():
            print(f"SKIP (not found): {filename}")
            continue

        original = path.read_text(encoding="utf-8")
        new_text, changed = convert_key_specs(original)

        if changed:
            print(f"  CHANGED: {filename}")
            if args.apply:
                path.write_text(new_text, encoding="utf-8")
        else:
            print(f"  no change: {filename}")

    if not args.apply:
        print("\n(Dry run. Pass --apply to write.)")


if __name__ == "__main__":
    main()
