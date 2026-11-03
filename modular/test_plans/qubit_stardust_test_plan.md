# Qu-Bit Electronix Stardust: Short Test Plan

Calibration sample plan for `modular/qubit_stardust_guide.md`. Format: `tooling/test_plan_template.md`, in short form. Part of the calibration sample tracked in `modular/test_plans/calibration_sample.md`.

| Field | Value |
|---|---|
| Module | Qu-Bit Electronix Stardust |
| Guide | `modular/qubit_stardust_guide.md` |
| Role | SHAPER |
| Open flags | none |
| Plan type | Verification, short form |
| Tested on | Not yet tested |
| Status | Not started |

**Why this module is in the sample:** Time, range and count claims on a looper with a long list of controls: easy to measure, and a digital module whose behavior depends on firmware.

## Tools

Mordax Data (scope and spectrum), multimeter, tape measure, tuner, sequencer with 1V/octave output and gate (Squarp Hermod+ or Marbles), stereo mixer.

## Measurement block

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth with the power cable fitted (guide: 22 mm) | Tape measure | |
| M2 | Current on +12V, -12V, +5V (guide: none given) | Multimeter in the supply line | |
| M3 | Firmware version | Read at boot if shown; record it | |

## Tests

Each prediction below is taken from the guide. For the tally sheet, mark each result as PASS, FAIL (the hardware contradicts the guide), or GAP (the guide is silent or too vague to test), and give the type: SPEC, RANGE, UI, JACK, BEHAV.

| ID | Setup | Prediction (guide) | Pass criterion | Result | Type | Clears |
|---|---|---|---|---|---|---|
| T1 | Varispeed encoder from slowest to fastest with a recorded tone, spectrum | Playback range from one-quarter speed (minus two octaves) upward; speed and pitch move together | Lowest and highest pitch ratios measured; check the guide's stated upper limit | | | Essential Parameters, Varispeed |
| T2 | Inertia fully clockwise, then a Varispeed change | Lag from none to a two-second motor failure simulation | Time to reach the new speed at minimum and maximum Inertia | | | Essential Parameters, Inertia |
| T3 | Size fully counterclockwise, then clockwise; Slice stepped | Size starts at 5 ms; Slice gives 2, 4, 8, 16 splice points, to a minimum slice length of 62 ms | Minimum loop length; slice counts at each knob region | | | Essential Parameters, Start and Size, Slice and Skip |
| T4 | Record, overdub twice, then Undo once; hold Erase for more than two seconds | Undo removes only the latest layer; holding Erase beyond two seconds cancels the erase | Buffer contents after each action | | | Essential Parameters, Erase and Undo |

## Closing steps

- [ ] Correct any guide text the hardware contradicts, following the failure handling in the template, in a separate commit.
- [ ] Remove any ⚠️ marker a result cleared.
- [ ] Enter the counts in `modular/test_plans/calibration_sample.md`.
