# Make Noise Maths: Short Test Plan

Calibration sample plan for `modular/make_noise_maths_guide.md`. Format: `tooling/test_plan_template.md`, in short form. Part of the calibration sample tracked in `modular/test_plans/calibration_sample.md`.

| Field | Value |
|---|---|
| Module | Make Noise Maths |
| Guide | `modular/make_noise_maths_guide.md` |
| Role | MODULATOR |
| Open flags | none (CONTROL: expected to pass) |
| Plan type | Verification, short form |
| Tested on | Not yet tested |
| Status | Not started |

**Why this module is in the sample:** The control. It is the most written-about module there is, so its guide can be checked against ten thousand other sources. If the plan finds a failure here, the method is too strict.

## Tools

Mordax Data (scope and spectrum), multimeter, tape measure, tuner, sequencer with 1V/octave output and gate (Squarp Hermod+ or Marbles), stereo mixer.

## Measurement block

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth with the power cable fitted (guide: 38 mm) | Tape measure | |
| M2 | Current on +12V and -12V (guide: 90 mA and 90 mA) | Multimeter in the supply line | |

## Tests

Each prediction below is taken from the guide. For the tally sheet, mark each result as PASS, FAIL (the hardware contradicts the guide), or GAP (the guide is silent or too vague to test), and give the type: SPEC, RANGE, UI, JACK, BEHAV.

| ID | Setup | Prediction (guide) | Pass criterion | Result | Type | Clears |
|---|---|---|---|---|---|---|
| T1 | Channel 1 Rise and Fall at their extremes with a trigger, scope | Rise and Fall range from instant to 25 minutes | Shortest time and a slope measured at the longest setting, extrapolated to the full range | | | Essential Parameters, Rise and Fall Time |
| T2 | Cycle button on channel 1, scope on the Unity output | Cycle turns the envelope into an LFO | Output cycles with no trigger | | | Essential Parameters, Cycle Button |
| T3 | Channel 2 and 3 with nothing patched; Variable outputs into SUM, OR and AND | Channels 2 and 3 produce +10 V when unpatched; Variable outputs auto-mix to SUM | Voltage at the unpatched channels; SUM follows the Variable outputs | | | Interface Database, Maths |
| T4 | Same pulse into TRIG and into Signal, with a long gate | TRIG gives a one-shot regardless of gate length; Signal follows gate length (sustain) | Envelope length at gate lengths of 0.1 s and 2 s on each input | | | Interface Database, Maths |

## Closing steps

- [ ] Correct any guide text the hardware contradicts, following the failure handling in the template, in a separate commit.
- [ ] Remove any ⚠️ marker a result cleared.
- [ ] Enter the counts in `modular/test_plans/calibration_sample.md`.
