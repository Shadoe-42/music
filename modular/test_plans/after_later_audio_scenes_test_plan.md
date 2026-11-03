# After Later Audio Scenes: Short Test Plan

Calibration sample plan for `modular/after_later_audio_scenes_guide.md`. Format: `tooling/test_plan_template.md`, in short form. Part of the calibration sample tracked in `modular/test_plans/calibration_sample.md`.

| Field | Value |
|---|---|
| Module | After Later Audio Scenes |
| Guide | `modular/after_later_audio_scenes_guide.md` |
| Role | MODULATOR |
| Open flags | 3 open ⚠️ (clock ratio positions, HOLD interaction, gate removal) |
| Plan type | Verification, short form |
| Tested on | Not yet tested |
| Status | Not started |

**Why this module is in the sample:** Three open flags, all about behavior the guide could not confirm. Passing or failing them clears real items.

## Tools

Mordax Data (scope and spectrum), multimeter, tape measure, tuner, sequencer with 1V/octave output and gate (Squarp Hermod+ or Marbles), stereo mixer.

## Measurement block

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth with the power cable fitted (guide: 25 mm) | Tape measure | |
| M2 | Current on +12V and -12V (guide: 80 mA and 20 mA) | Multimeter in the supply line | |

## Tests

Each prediction below is taken from the guide. For the tally sheet, mark each result as PASS, FAIL (the hardware contradicts the guide), or GAP (the guide is silent or too vague to test), and give the type: SPEC, RANGE, UI, JACK, BEHAV.

| ID | Setup | Prediction (guide) | Pass criterion | Result | Type | Clears |
|---|---|---|---|---|---|---|
| T1 | Looping RAMP as an isolated segment, a clock from Pamela's PRO Workout into its gate, slider stepped through its range | Gate-synced LFO: the slider selects a clock division or multiplication from 1/4 to 4x; exact positions unverified | Record the ratio at each slider position against the clock, and whether the range is 1/4 to 4x | | | Gate-synced LFO paragraph ⚠️ |
| T2 | HOLD segment as sustain in an envelope group; slider and knob moved separately, then HOLD looped with the gate held high | The slider sets the sustain voltage and the knob sets the hold duration; looped HOLD makes sustain last as long as the gate is high; interaction unverified | Which control sets which parameter; how long sustain lasts with a gate held for 1 s and 5 s | | | Common Mistakes, HOLD sustain ⚠️ |
| T3 | Remove the gate cable during an active envelope cycle, at three different segments | The module does not reset cleanly on cable removal in all cases | Behavior at each segment: continues, stops, resets, or holds a level | | | Common Mistakes, gate removal ⚠️ |
| T4 | Press a segment button through its three types; long press for one second | RAMP teal, STEP orange, HOLD red or pink; long press toggles loop and the LED blinks | LED colors and the one-second threshold | | | Essential Parameters, Segment type button |
| T5 | STEP target and RAMP top, multimeter or scope | STEP target 0 V to 8 V; a first-segment RAMP rises toward 8 V | Voltage limits measured | | | Three Segment Types |

## Closing steps

- [ ] Correct any guide text the hardware contradicts, following the failure handling in the template, in a separate commit.
- [ ] Remove any ⚠️ marker a result cleared.
- [ ] Enter the counts in `modular/test_plans/calibration_sample.md`.
