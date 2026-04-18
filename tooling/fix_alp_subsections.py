"""
fix_alp_subsections.py

Strips sub-section blocks from Advanced Learning Path sections.
Keeps only the numbered progression items under "Recommended Study Progression:".
Drops: Cross-Module Learning Opportunities, Skill Development Milestones,
       Advanced [X] Concepts, Performance Applications.

Target guides: 11 Tier 2 guides with ALP-only issues.
"""

import re
from pathlib import Path

MODULAR_DIR = Path(__file__).parent.parent / "modular"

TARGET_GUIDES = [
    "4ms_company_metamodule_guide.md",
    "alm_busy_circuits_mco_alm021_guide.md",
    "bizarre_jezabel_pkhia_mk2_guide.md",
    "blue_lantern_modules_blm_looping_simple_adsr_v21_guide.md",
    "cre8audio_chipz_guide.md",
    "erica_synths_black_envelope_generator_2_guide.md",
    "erica_synths_black_quad_vca2_guide.md",
    "erica_synths_pico_drum2_guide.md",
    "intellijel_stomp_guide.md",
    "mutable_instruments_links_guide.md",
    "tiptop_audio_miso_guide.md",
]

# Bold sub-headings that introduce junk sub-sections
JUNK_HEADINGS = re.compile(
    r'^\*\*(Cross-Module Learning Opportunities|Skill Development Milestones|'
    r'Advanced .+ Concepts|Performance Applications)[:\*]',
    re.IGNORECASE | re.MULTILINE
)

# The "Recommended Study Progression:" label line (keep the numbered items, drop this)
PROGRESSION_LABEL = re.compile(
    r'^\*\*Recommended Study Progression:\*\*\s*$',
    re.MULTILINE
)


def clean_alp_section(alp_text):
    """
    Given the raw ALP section text (from ## Advanced Learning Path to the next ---),
    return a cleaned version with only the numbered items.
    """
    lines = alp_text.split('\n')
    output = []
    skip_mode = False  # True when inside a junk sub-section

    for line in lines:
        # Drop the "Recommended Study Progression:" label
        if PROGRESSION_LABEL.match(line):
            continue

        # Detect start of a junk sub-section
        if JUNK_HEADINGS.match(line):
            skip_mode = True
            continue

        # Detect start of a new real numbered item — exit skip mode
        if re.match(r'^\d+\.', line):
            skip_mode = False

        if skip_mode:
            continue

        output.append(line)

    # Strip trailing blank lines before the closing ---
    while output and output[-1].strip() == '':
        output.pop()

    return '\n'.join(output)


def process_guide(path):
    text = path.read_text(encoding='utf-8')

    # Find the ALP section
    alp_match = re.search(r'(## Advanced Learning Path\n)', text)
    if not alp_match:
        print(f"  SKIP: no ALP found in {path.name}")
        return False

    alp_start = alp_match.start()

    # Find the end: next ## heading, --- divider, or end of file
    after_alp = text[alp_match.end():]
    next_section = re.search(r'\n(## |---)', after_alp)
    if next_section:
        alp_end = alp_match.end() + next_section.start()
    else:
        alp_end = len(text)

    alp_body = text[alp_match.end():alp_end]

    # Check whether this ALP actually has the junk sub-sections
    if not JUNK_HEADINGS.search(alp_body) and not PROGRESSION_LABEL.search(alp_body):
        print(f"  SKIP: {path.name} — ALP already clean")
        return False

    cleaned_body = clean_alp_section(alp_body)

    new_text = text[:alp_match.end()] + cleaned_body + '\n' + text[alp_end:]
    path.write_text(new_text, encoding='utf-8')
    return True


def main():
    changed = 0
    skipped = 0
    for name in TARGET_GUIDES:
        path = MODULAR_DIR / name
        if not path.exists():
            print(f"  MISSING: {name}")
            continue
        print(f"Processing: {name}")
        if process_guide(path):
            print(f"  FIXED")
            changed += 1
        else:
            skipped += 1

    print(f"\nDone. {changed} guides fixed, {skipped} skipped.")


if __name__ == '__main__':
    main()
