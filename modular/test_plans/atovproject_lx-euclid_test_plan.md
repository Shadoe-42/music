# ATOV Project lx-euclid: Short Test Plan

Calibration sample plan for `modular/atovproject_lx-euclid_guide.md`. Format: `tooling/test_plan_template.md`, in short form. Part of the calibration sample tracked in `modular/test_plans/calibration_sample.md`.

| Field | Value |
|---|---|
| Module | ATOV Project lx-euclid |
| Guide | `modular/atovproject_lx-euclid_guide.md` |
| Role | CONTROLLER |
| Open flags | none |
| Plan type | Verification, short form |
| Tested on | Not yet tested |
| Status | Not started |

**Why this module is in the sample:** A touch-and-display interface with output-level and input-range claims that are quick to measure. The guide gives no depth or current, which the measurement block fills.

## Tools

Mordax Data (scope and spectrum), multimeter, tape measure, tuner, sequencer with 1V/octave output and gate (Squarp Hermod+ or Marbles), stereo mixer.

## Measurement block

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth with the power cable fitted (guide: none given) | Tape measure | |
| M2 | Current on +12V and -12V (guide: none given) | Multimeter in the supply line | |

## Tests

Each prediction below is taken from the guide. For the tally sheet, mark each result as PASS, FAIL (the hardware contradicts the guide), or GAP (the guide is silent or too vague to test), and give the type: SPEC, RANGE, UI, JACK, BEHAV.

| ID | Setup | Prediction (guide) | Pass criterion | Result | Type | Clears |
|---|---|---|---|---|---|---|
| T1 | Gate outputs on the scope, one channel running | Outputs are 0 V when inactive and 10 V when active; gate length is configurable in milliseconds | High and low levels; gate length at two settings | | | Essential Parameters, D (Gate outputs) |
| T2 | A CV source from -5 V to +5 V into one B input assigned to a channel parameter | Each of the four CV inputs accepts -5 V to +5 V | Response across the range; behavior beyond plus or minus 5 V | | | Essential Parameters, B (CV inputs) |
| T3 | Tap the Tap button five times at a steady tempo; then hold and release it | Tap averages the intervals to set BPM; holding and releasing resets all channels to their first step | Measured BPM against the tap rate; all channels return to step 1 | | | Essential Parameters, Tap button |
| T4 | Rising edge into A; then self-patch a gate output into A | A rising edge resets all channels to their first step; self-patching shortens a pattern | Reset occurs on the edge; self-patched pattern length changes as described | | | Essential Parameters, A (Reset input) |
| T5 | Look at the four channel buttons | Channel 1 yellow, 2 red, 3 blue, 4 turquoise | Colors | | | Essential Parameters, Channel selection buttons |

## Closing steps

- [ ] Correct any guide text the hardware contradicts, following the failure handling in the template, in a separate commit.
- [ ] Remove any ⚠️ marker a result cleared.
- [ ] Enter the counts in `modular/test_plans/calibration_sample.md`.
