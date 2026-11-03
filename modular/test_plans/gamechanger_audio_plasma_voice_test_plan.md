# Gamechanger Audio Plasma Voice: Short Test Plan

Calibration sample plan for `modular/gamechanger_audio_plasma_voice_guide.md`. Format: `tooling/test_plan_template.md`, in short form. Part of the calibration sample tracked in `modular/test_plans/calibration_sample.md`.

| Field | Value |
|---|---|
| Module | Gamechanger Audio Plasma Voice |
| Guide | `modular/gamechanger_audio_plasma_voice_guide.md` |
| Role | EVENT_VOICE |
| Open flags | none |
| Plan type | Verification, short form |
| Tested on | Not yet tested |
| Status | Not started |

**Why this module is in the sample:** A voice with its own envelope, a high-voltage tube, and a MULTICV menu. The guide has hard numbers on power and pitch, and its safety notes must be correct.

## Tools

Mordax Data (scope and spectrum), multimeter, tape measure, tuner, sequencer with 1V/octave output and gate (Squarp Hermod+ or Marbles), stereo mixer.

## Measurement block

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth with the power cable fitted (guide: 35 mm) | Tape measure | |
| M2 | Current on +12V, -12V, +5V (guide: 220 mA, 35 mA, 0 mA) | Multimeter in the supply line | |

## Tests

Each prediction below is taken from the guide. For the tally sheet, mark each result as PASS, FAIL (the hardware contradicts the guide), or GAP (the guide is silent or too vague to test), and give the type: SPEC, RANGE, UI, JACK, BEHAV.

| ID | Setup | Prediction (guide) | Pass criterion | Result | Type | Clears |
|---|---|---|---|---|---|---|
| T1 | PITCH knob end to end with nothing in V/OCT, tuner | PITCH moves the base pitch within plus or minus one octave of center | Measured span in octaves | | | Essential Parameters, PITCH |
| T2 | Sequencer CV 0 V to 4 V in 1 V steps into V/OCT, tuner | V/OCT is standard 1V/octave tracking | Error in cents per octave | | | Essential Parameters, 1V/OCT |
| T3 | Open the MULTICV assignment menu and list every destination | The guide advises studying the MULTICV assignment menu as a session of its own | Number and names of destinations; any the guide does not mention | | | Advanced Learning Path, MULTICV |
| T4 | DRIVE end to end with a steady tone on the scope | DRIVE is analog soft clipping, not digital clipping | Scope shows rounded clipping, not hard flat tops | | | Essential Parameters, DRIVE |

## Closing steps

- [ ] Correct any guide text the hardware contradicts, following the failure handling in the template, in a separate commit.
- [ ] Remove any ⚠️ marker a result cleared.
- [ ] Enter the counts in `modular/test_plans/calibration_sample.md`.
