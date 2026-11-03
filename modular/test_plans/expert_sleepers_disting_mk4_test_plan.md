# Expert Sleepers disting mk4: Short Test Plan

Calibration sample plan for `modular/expert_sleepers_disting_mk4_guide.md`. Format: `tooling/test_plan_template.md`, in short form. Part of the calibration sample tracked in `modular/test_plans/calibration_sample.md`.

| Field | Value |
|---|---|
| Module | Expert Sleepers disting mk4 |
| Guide | `modular/expert_sleepers_disting_mk4_guide.md` |
| Role | UTILITY |
| Open flags | none, menu-heavy digital |
| Plan type | Verification, short form |
| Tested on | Not yet tested |
| Status | Not started |

**Why this module is in the sample:** A 540-line guide with no flags and many menu and algorithm claims. Digital menu behavior changes with firmware, so this is where drift is most likely.

## Tools

Mordax Data (scope and spectrum), multimeter, tape measure, tuner, sequencer with 1V/octave output and gate (Squarp Hermod+ or Marbles), stereo mixer.

## Measurement block

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth with the power cable fitted (guide: 42 mm) | Tape measure | |
| M2 | Current on +12V and -12V (guide: 51 mA and 19 mA) | Multimeter in the supply line | |
| M3 | Firmware version | Read from the module at boot or in the settings, and record it so the other results are dated to a firmware | |

## Tests

Each prediction below is taken from the guide. For the tally sheet, mark each result as PASS, FAIL (the hardware contradicts the guide), or GAP (the guide is silent or too vague to test), and give the type: SPEC, RANGE, UI, JACK, BEHAV.

| ID | Setup | Prediction (guide) | Pass criterion | Result | Type | Clears |
|---|---|---|---|---|---|---|
| T1 | Algorithm selection as written | Press S twice, turn to select, press to confirm | The procedure works exactly as written on the installed firmware; record any difference | | | Essential Parameters, Algorithm Selection |
| T2 | Count the algorithms and read their categories | 80+ algorithms, in categories A to N (A=CV utilities, B=modulation, C=audio processing) | Number of algorithms on this firmware; whether the category letters and meanings match | | | Essential Parameters, Algorithm Selection |
| T3 | Z CV socket with a bipolar LFO at about plus and minus 5 V | The socket lights red for positive voltage and blue for negative | Colors for each polarity | | | Essential Parameters, Z Knob/CV |
| T4 | S knob on three algorithms, count the parameters | Up to 8 parameters per algorithm | Maximum number of parameters seen; any algorithm with more than 8 | | | Essential Parameters, S Knob |

## Closing steps

- [ ] Correct any guide text the hardware contradicts, following the failure handling in the template, in a separate commit.
- [ ] Remove any ⚠️ marker a result cleared.
- [ ] Enter the counts in `modular/test_plans/calibration_sample.md`.
