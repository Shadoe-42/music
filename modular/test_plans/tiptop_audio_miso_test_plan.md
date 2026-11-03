# Tiptop Audio MISO: Short Test Plan

Calibration sample plan for `modular/tiptop_audio_miso_guide.md`. Format: `tooling/test_plan_template.md`, in short form. Part of the calibration sample tracked in `modular/test_plans/calibration_sample.md`.

| Field | Value |
|---|---|
| Module | Tiptop Audio MISO |
| Guide | `modular/tiptop_audio_miso_guide.md` |
| Role | AMPLIFIER |
| Open flags | none |
| Plan type | Verification, short form |
| Tested on | Not yet tested |
| Status | Not started |

**Why this module is in the sample:** The only AMPLIFIER in the sample. The guide gives behavior but few numbers, so the plan measures the numbers it lacks.

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
| T1 | A 2 V DC source into channel 1; attenuverter at 12 o'clock, clockwise, counterclockwise; multimeter on the output | 12 o'clock gives no signal; clockwise gives normal polarity; counterclockwise inverts | Output voltage at the three positions and the maximum gain at each end | | | Essential Parameters, Four Attenuverters |
| T2 | No input, offset control end to end, multimeter | With no input, the offset control generates a constant voltage; 12 o'clock is no offset | Offset range in volts, positive and negative | | | Essential Parameters, Offset Controls |
| T3 | Signals into channels 1, 2, A and B together | Each channel has its own input, output and attenuverter and works separately or in groups | Whether outputs mix or normal into each other when unpatched; record the grouping rules | | | Essential Parameters, Four Attenuverters |

## Closing steps

- [ ] Correct any guide text the hardware contradicts, following the failure handling in the template, in a separate commit.
- [ ] Remove any ⚠️ marker a result cleared.
- [ ] Enter the counts in `modular/test_plans/calibration_sample.md`.
