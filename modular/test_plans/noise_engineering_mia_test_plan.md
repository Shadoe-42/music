# Noise Engineering Manis Iteritas Alia (MIA): Short Test Plan

Calibration sample plan for `modular/noise_engineering_mia_guide.md`. Format: `tooling/test_plan_template.md`, in short form. Part of the calibration sample tracked in `modular/test_plans/calibration_sample.md`.

| Field | Value |
|---|---|
| Module | Noise Engineering Manis Iteritas Alia (MIA) |
| Guide | `modular/noise_engineering_mia_guide.md` |
| Role | EVENT_VOICE |
| Open flags | 2 open ⚠️ (depth and power, two sources disagree) |
| Plan type | Verification, short form |
| Tested on | Not yet tested |
| Status | Not started |

**Why this module is in the sample:** The guide itself records a conflict between its measured values and the manual: depth 25 mm against about 38 mm, current 100 mA and 15 mA against 105 mA and 10 mA. Measurement settles it.

## Tools

Mordax Data (scope and spectrum), multimeter, tape measure, tuner, sequencer with 1V/octave output and gate (Squarp Hermod+ or Marbles), stereo mixer.

## Measurement block

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth with the power cable fitted (guide: 25 mm; manual: about 38 mm) | Tape measure | |
| M2 | Current on +12V, -12V, +5V (guide: 100 mA, 15 mA, 0 mA; manual: 105 mA, 10 mA) | Multimeter in the supply line | |

## Tests

Each prediction below is taken from the guide. For the tally sheet, mark each result as PASS, FAIL (the hardware contradicts the guide), or GAP (the guide is silent or too vague to test), and give the type: SPEC, RANGE, UI, JACK, BEHAV.

| ID | Setup | Prediction (guide) | Pass criterion | Result | Type | Clears |
|---|---|---|---|---|---|---|
| T1 | Trigger levels of 1 V, 1.5 V, 2 V and 3 V into Trig | The trigger threshold is about 1.8 V | Threshold between the tested levels | | | Essential Parameters, Trigger and Hit |
| T2 | Pitch encoder: turn, then press while turning | Fine steps by default; pressing while turning gives semitone steps | Step size in cents in each mode | | | Essential Parameters, Pitch |
| T3 | Skin, Liquid and Metal modes with the Bass, Alto and Treble switch | Alto raises the pitch two octaves from Bass and Treble four octaves from Bass; 1V/oct tracking | Pitch ratio between the three positions, tuner | | | Essential Parameters, Bass / Alto / Treble |
| T4 | Bash at 12 o'clock, then clockwise and counterclockwise | At 12 o'clock Bash has no effect; turning applies positive or negative envelope modulation to Smash, Profundity and LPF | No change at 12; opposite directions each side | | | Essential Parameters, Bash |

## Closing steps

- [ ] Correct any guide text the hardware contradicts, following the failure handling in the template, in a separate commit.
- [ ] Remove any ⚠️ marker a result cleared.
- [ ] Enter the counts in `modular/test_plans/calibration_sample.md`.
