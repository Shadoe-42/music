# Endorphin.es Grand Terminal: Short Test Plan

Calibration sample plan for `modular/endorphines_grand_terminal_guide.md`. Format: `tooling/test_plan_template.md`, in short form. Part of the calibration sample tracked in `modular/test_plans/calibration_sample.md`.

| Field | Value |
|---|---|
| Module | Endorphin.es Grand Terminal |
| Guide | `modular/endorphines_grand_terminal_guide.md` |
| Role | SHAPER |
| Open flags | none |
| Plan type | Verification, short form |
| Tested on | Not yet tested |
| Status | Not started |

**Why this module is in the sample:** Exact electrical figures (230 mA, 25 mm for a 26 HP panel, envelope times and output ranges) that a measurement can confirm or contradict.

## Tools

Mordax Data (scope and spectrum), multimeter, tape measure, tuner, sequencer with 1V/octave output and gate (Squarp Hermod+ or Marbles), stereo mixer.

## Measurement block

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth with the power cable fitted (guide: 25 mm for a 26 HP module) | Tape measure | |
| M2 | Current on +12V, -12V, +5V (guide: 230 mA, 65 mA, 0 mA) | Multimeter in the supply line | |

## Tests

Each prediction below is taken from the guide. For the tally sheet, mark each result as PASS, FAIL (the hardware contradicts the guide), or GAP (the guide is silent or too vague to test), and give the type: SPEC, RANGE, UI, JACK, BEHAV.

| ID | Setup | Prediction (guide) | Pass criterion | Result | Type | Clears |
|---|---|---|---|---|---|---|
| T1 | Airplane A in Transient mode, gate pulses of 0.5 V, 0.8 V and 2 V, scope on the envelope | A trigger above about 0.65 V initiates Take Off | Threshold between 0.5 V and 0.8 V | | | Airplane Modes, Transient |
| T2 | Airplane A knobs at their extremes, no CV, scope | Each stage runs from 1 millisecond to 10 seconds | Shortest and longest Take Off and Landing times | | | The Airplanes |
| T3 | Airplane A unipolar and bipolar outputs at the peak | Unipolar 0 V to about +8 V; bipolar centered at 0 V rising to +5 V and swinging to -5 V in some configurations | Peak voltages on both outputs; which configuration reaches -5 V | | | Airplane Outputs |
| T4 | Cruise mode with a 2 s gate, then Loop mode with no gate | Cruise holds at maximum while the gate is high; Loop cycles with no trigger | Hold behavior during the gate; Loop runs unaided | | | Airplane Modes |

## Closing steps

- [ ] Correct any guide text the hardware contradicts, following the failure handling in the template, in a separate commit.
- [ ] Remove any ⚠️ marker a result cleared.
- [ ] Enter the counts in `modular/test_plans/calibration_sample.md`.
