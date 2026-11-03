# Winterbloom Castor & Pollux II: Short Test Plan

Calibration sample plan for `modular/winterbloom_castor_pollux_ii_guide.md`. Format: `tooling/test_plan_template.md`, in short form. Part of the calibration sample tracked in `modular/test_plans/calibration_sample.md`.

| Field | Value |
|---|---|
| Module | Winterbloom Castor & Pollux II |
| Guide | `modular/winterbloom_castor_pollux_ii_guide.md` |
| Role | SOURCE |
| Open flags | 2 open ⚠️ (depth, power) |
| Plan type | Verification, short form |
| Tested on | Not yet tested |
| Status | Not started |

**Why this module is in the sample:** Two guide flags are open (depth and power), so a pass clears something real. Also a calibratable DCO whose tracking claim is easy to measure.

## Tools

Mordax Data (scope and spectrum), multimeter, tape measure, tuner, sequencer with 1V/octave output and gate (Squarp Hermod+ or Marbles), stereo mixer.

## Measurement block

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth with the power cable fitted (guide: unverified) | Tape measure | |
| M2 | Current on +12V, -12V, +5V (guide: unverified) | Multimeter in the supply line | |

## Tests

Each prediction below is taken from the guide. For the tally sheet, mark each result as PASS, FAIL (the hardware contradicts the guide), or GAP (the guide is silent or too vague to test), and give the type: SPEC, RANGE, UI, JACK, BEHAV.

| ID | Setup | Prediction (guide) | Pass criterion | Result | Type | Clears |
|---|---|---|---|---|---|---|
| T1 | Hold MODE and turn the pitch knob end to end on one oscillator; tuner | Fine tune access: hold MODE plus the pitch knob gives plus or minus 2.5 semitones | Measured span within 10 cents of 5 semitones total | | | Key Specifications, Fine tune access |
| T2 | Sequencer CV 0 V to 5 V in 1 V steps into Castor V/OCT; tuner or spectrum | V/OCT tracking is 1V/octave, calibratable via the web editor | Error in cents per octave before any calibration; note if the web editor is needed to reach 5 cents | | | Key Specifications, V/OCT tracking |
| T3 | Tap MODE and watch the LED through a full cycle | Three modes by tap: Chorus (blue), LFO FM (green), Hard Sync (LED color indicates the mode) | Order of modes and LED colors as stated; record the Hard Sync color, which the guide does not give | | | Essential Parameters, MODE button |
| T4 | CROSSFADE knob end to end, Castor and Pollux at the same pitch and waveform | Fully counterclockwise only Castor is audible; fully clockwise only Pollux; noon equal | Level of each oscillator at the three positions, in volts peak to peak | | | Essential Parameters, CROSSFADE |
| T5 | RAMP, PULSE and SUB trims one at a time, spectrum | SUB is one octave below pitch | SUB fundamental at half the frequency of the oscillator | | | Key Specifications, Waveforms per oscillator |

## Closing steps

- [ ] Correct any guide text the hardware contradicts, following the failure handling in the template, in a separate commit.
- [ ] Remove any ⚠️ marker a result cleared.
- [ ] Enter the counts in `modular/test_plans/calibration_sample.md`.
