"""
fix_tier2_headings.py

Targeted heading renames and structural fixes for Tier 2 guides.
No content changes — heading normalization only.

Fixes applied:
  - Rename non-standard patch section headings to ## Patches
  - Rename Quick Reference → ## Quick Start: ... for reference guides
  - Rename per-parameter sections to ## Essential Parameters where appropriate
  - Rename ## Essential Architecture → ## Essential Parameters
  - Remove duplicate ## Advanced Learning Path sections (keep first)
  - Rename ## Utility Learning Path → ## Advanced Learning Path
  - Fix VPME Euclidean Circles structural issues
"""

import re
from pathlib import Path

MODULAR_DIR = Path(__file__).parent.parent / "modular"


def rename_heading(text, old_heading, new_heading):
    """Replace an exact ## heading line."""
    # Match the heading as its own line (case-sensitive, full line match)
    pattern = re.compile(r'^' + re.escape(old_heading) + r'\s*$', re.MULTILINE)
    return pattern.sub(new_heading, text)


def remove_duplicate_alp(text):
    """Keep the first ## Advanced Learning Path; remove all subsequent ones."""
    lines = text.split('\n')
    alp_count = 0
    skip_until_next_h2 = False
    output = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r'^## Advanced Learning Path', line, re.IGNORECASE):
            alp_count += 1
            if alp_count > 1:
                # Start skipping until next ## heading
                skip_until_next_h2 = True
                i += 1
                continue
            else:
                skip_until_next_h2 = False
        elif re.match(r'^## ', line) and skip_until_next_h2:
            skip_until_next_h2 = False
        if skip_until_next_h2:
            i += 1
            continue
        output.append(line)
        i += 1
    return '\n'.join(output)


def fix_guide(name, operations):
    path = MODULAR_DIR / name
    if not path.exists():
        print(f"  MISSING: {name}")
        return
    text = path.read_text(encoding='utf-8')
    original = text
    for op, *args in operations:
        if op == 'rename':
            text = rename_heading(text, args[0], args[1])
        elif op == 'dedup_alp':
            text = remove_duplicate_alp(text)
        elif op == 'replace':
            text = text.replace(args[0], args[1])
    if text != original:
        path.write_text(text, encoding='utf-8')
        print(f"  FIXED: {name}")
    else:
        print(f"  UNCHANGED: {name} (no matching headings found)")


def main():
    fixes = [
        # --- Patch section renames ---
        ("behringer_dual_envelope_generator_1003_utility_guide.md", [
            ("rename", "## Utility Patches", "## Patches"),
        ]),
        ("erica_synths_pico_lfo_sh_guide.md", [
            ("rename", "## Utility Patch Applications", "## Patches"),
            ("dedup_alp",),
        ]),
        ("erica_synths_pico_vca2_guide.md", [
            ("rename", "## Utility Patch Applications", "## Patches"),
            ("rename", "## Utility Learning Path", "## Advanced Learning Path"),
        ]),
        ("expert_sleepers_disting_mk4_guide.md", [
            ("rename", "## Multi-Function Patch Applications", "## Patches"),
            ("dedup_alp",),
        ]),

        # --- Reference guide: Quick Reference → Quick Start ---
        ("alm_busy_circuits_pamelas_pro_workout_guide.md", [
            ("rename", "## Quick Reference", "## Quick Start: First Sound in 5 Minutes"),
            ("rename", "## Per-Output Parameters", "## Essential Parameters (Per-Output Controls)"),
        ]),
        ("endorphines_queen_of_pentacles_guide.md", [
            ("rename", "## Quick Reference", "## Quick Start: First Sound in 5 Minutes"),
            ("rename", "## The Analog Voices", "## Essential Parameters (The Voice Controls)"),
        ]),
        ("xaoc_devices_zadar_nin_guide.md", [
            ("rename", "## Quick Reference", "## Quick Start: First Sound in 5 Minutes"),
            ("rename", "## Per-Channel Parameters", "## Essential Parameters (The Channel Controls)"),
        ]),
        ("endorphines_blck_noir_guide.md", [
            ("rename", "## Triggering Your Drums", "## Quick Start: Trigger Your First Voice in 5 Minutes"),
            ("rename", "## Per-Voice Parameters", "## Essential Parameters (The Voice Controls)"),
        ]),

        # --- VPME Drum Workstation ---
        ("vpme_qd_qex_drum_workstation_guide.md", [
            ("rename", "## Essential Architecture (The Professional Drum Brain)",
             "## Essential Parameters (The Professional Drum Brain)"),
        ]),

        # --- VPME Euclidean Circles: missed by earlier batch fix ---
        ("vpme_qd_qex_euclidean_circles_ecosystem_guide.md", [
            ("replace", "# VPME QD/QEX + Euclidean Circles - Guide",
             "# VPME QD/QEX + Euclidean Circles"),
            ("rename", "## Beginner Patch Ideas", "## Patches"),
            ("rename", "## Beginner Gotchas & Pro Tips", "## Common Mistakes and How to Avoid Them"),
        ]),
    ]

    for name, operations in fixes:
        fix_guide(name, operations)

    print("\nDone.")


if __name__ == '__main__':
    main()
