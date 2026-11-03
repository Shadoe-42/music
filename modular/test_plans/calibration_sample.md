# Calibration Sample: Tally Sheet

Purpose: decide whether the rest of the corpus needs test plans, by testing a sample of ten modules and counting what fails. Agreed 2026-11-02. Plans are short-form (measurement block plus 4 or 5 of the claims most likely to be wrong), in this folder.

## How to count

For every test row, mark the result as one of:

- **PASS:** the hardware matches the guide.
- **FAIL:** the hardware contradicts the guide. The guide text is corrected.
- **GAP:** the guide is silent or too vague to test. This is a missing-detail finding, not an error.

Give each row a type: **SPEC** (depth, current, width), **RANGE** (a voltage, time, or frequency range), **UI** (a button, menu, LED, or procedure), **JACK** (a jack or control name), **BEHAV** (what the module does in response to an input).

## Sample

| Module | Role | Why | Tests | PASS | FAIL | GAP | Notes |
|---|---|---|---|---|---|---|---|
| Winterbloom Castor & Pollux II | SOURCE | 2 open ⚠️ (depth, power) | 5 | | | | |
| Expert Sleepers disting mk4 | UTILITY | none, menu-heavy digital | 4 | | | | |
| After Later Audio Scenes | MODULATOR | 3 open ⚠️ (clock ratio positions, HOLD interaction, gate removal) | 5 | | | | |
| ATOV Project lx-euclid | CONTROLLER | none | 5 | | | | |
| Endorphin.es Grand Terminal | SHAPER | none | 4 | | | | |
| Qu-Bit Electronix Stardust | SHAPER | none | 4 | | | | |
| Gamechanger Audio Plasma Voice | EVENT_VOICE | none | 4 | | | | |
| Noise Engineering Manis Iteritas Alia (MIA) | EVENT_VOICE | 2 open ⚠️ (depth and power, two sources disagree) | 4 | | | | |
| Tiptop Audio MISO | AMPLIFIER | none | 3 | | | | |
| Make Noise Maths | MODULATOR | none (CONTROL: expected to pass) | 4 | | | | |
| **Total** | | | | | | | |

Maths is the control. It is expected to pass; a FAIL there means the method is too strict, not that the guide is wrong.

## Reading the result

These are rules of thumb for the decision, not a statistical test. The sample is ten modules.

- **Few failures overall (about one in ten rows or fewer):** the existing verification holds. Stop here. The Kharper, Oneiroi, Fold 6, Pizza and GTE plans cover the guides written before the hardware arrived.
- **Failures cluster in one type** (for example SPEC or UI): add a check for that type to the tooling, and audit only the guides most likely to share the weakness (for example, every guide with a numeric depth or current and no source).
- **Failures spread across all types:** the verification was weaker than the project notes say, and a wider pass is justified, starting with guides that have open ⚠️ flags.
- **Many GAP rows:** the guides are accurate but thin. That is a writing task, not a testing task.
- **A FAIL in the control (Maths):** stop and check the method before counting anything else.

## Bench order

1. Scenes, MIA, Castor & Pollux (open flags: a pass clears something).
2. Disting mk4, Grand Terminal, Plasma Voice (hard numbers and digital behavior).
3. Stardust, lx-euclid, MISO.
4. Maths (the control), last.
