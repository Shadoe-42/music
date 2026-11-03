# Joranalogue Fold 6: Test Plan

Verification plan for `modular/joranalogue_fold_6_guide.md`. Format: `tooling/test_plan_template.md`. Clears the draft status block and every ⚠️ in the guide.

| Field | Value |
|---|---|
| Module | Joranalogue Fold 6 |
| Guide | `modular/joranalogue_fold_6_guide.md` (draft, 2026-10-24) |
| Plan type | Verification |
| Firmware | Not applicable (analog) |
| Tested on | Not yet tested |
| Sources | Joranalogue manual, revision D, version 2023-06-26 |
| Status | Not started |

## Tools

Mordax Data (scope and spectrum), multimeter with DC volts, tape measure, Endorphin.es New Godspeed (sine source, TIMBRE at minimum), a slow bipolar LFO (2hp LFO v2), a sequencer with stepped CV (Hermod+ or Marbles), Xaoc Devices Zadar, Erica Synths Black Polyvoks VCF, Vostok Instruments Ceres or Pico VCA2, an envelope (Blue Lantern BLM Looping Simple ADSR or Maths), Intellijel MixUp. Safety: start the mixer low for every test, and keep it low for the feedback test.

## Measurement block (run first)

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth with the power cable fitted. The guide carries 40 mm from ModularGrid; the manual gives 35 mm including cable and 52 mm outer depth | Tape measure | |
| M2 | Current on +12V and -12V (guide: 40 mA each, no +5V) | Multimeter in the supply line, idle and with FOLD and SHAPE at maximum | |
| M3 | Power connector polarity marking | Photograph the header | |
| M4 | Front-panel photograph | Square on, even light, no hands, no cables | |
| M5 | Not applicable | | |

## Test order

M block, then T1 to T6 (baseline behavior), then T7 to T12 (CV behavior), then T13 to T18 (patches), then T19 to T20 (extremes). FOLD behavior first because every later test assumes it.

## Tests

| ID | Setup | Prediction (guide) | Pass criterion | Result | Clears |
|---|---|---|---|---|---|
| T1 | New Godspeed sine into IN, SHAPE minimum, SYMMETRY center, FOLD at minimum, MAIN to scope | At minimum FOLD the input is fully attenuated and the output is silent | Output flat. Record residual DC offset and noise floor in millivolts | | Quick Start step 4; Common Mistakes, "FOLD all the way down" |
| T2 | As T1, raise FOLD slowly, spectrum running | The plain sine appears first, then folds begin and overtones accumulate in stages | Record the FOLD position where the first fold appears and how many harmonics are visible at three FOLD positions | | Patch 1 listening; Quick Start step 4 |
| T3 | Sine amplitude measured at IN, then MAIN at a low FOLD before folding starts | Output reaches about 10 Vpp | Peak-to-peak at MAIN with the largest FOLD; compare with -5 V to +5 V | | Key Specifications, Output level |
| T4 | SHAPE minimum, then raised, FOLD fixed at a moderate setting | At minimum the overdrive is essentially disabled; raising it shapes the wave toward pulses with a harsher sound | Scope shows flattening at the peaks; the number of folds is unchanged by SHAPE | | Patch 2 listening; Essential Parameters, SHAPE |
| T5 | SHAPE CV with a stepped source: 0 V, +2.5 V, +5 V, then -2.5 V and -5 V, knob at minimum | 0 V no drive, +5 V maximum drive; negative voltages attenuate the output | Drive at the three positive voltages; output amplitude at the negative voltages in volts | | Essential Parameters, SHAPE; Common Mistakes on LFO and SHAPE |
| T6 | A bipolar LFO on SHAPE CV | A bipolar LFO makes the level pump, the negative half sounds like a volume dip | Output level dips on the negative half cycle; measure the dip depth | | Common Mistakes, "My LFO on SHAPE" |
| T7 | FOLD knob mid, patch a stepped CV into FOLD CV at 0 V, 2.5 V, 5 V | Whether the knob and the CV sum, or the knob scales the CV, is not stated | Four combinations of knob and CV compared on the spectrum or fold count: if knob mid plus 0 V equals knob at minimum plus a value, the inputs sum. Record which | | Draft block item 3; Essential Parameters, FOLD ⚠️ |
| T8 | FOLD CV stepped 0 V to 5 V in 1 V steps, knob at minimum | FOLD CV is linear: harmonic density moves in direct proportion to voltage | Fold count (scope peaks) against volts is a straight line within one fold; record the fold count at each voltage | | Essential Parameters, FOLD |
| T9 | FOLD CV above 5 V (up to 8 V or 10 V), knob at maximum | External voltage can drive the folder harder than the knob can | More folds than the knob alone gives; record the voltage at which no further change occurs | | Essential Parameters, FOLD |
| T10 | Sine into IN with SYMMETRY at center, then at each end | SYMMETRY adds an offset of -5 V to +5 V; folding becomes asymmetric | Spectrum: even harmonics appear off center and are low at center. Measure the offset at each end with the multimeter on a DC input | | Quick Start step 6; Essential Parameters, SYMMETRY |
| T11 | Offset source into IN (a DC voltage from a sequencer), SYMMETRY tuned to cancel it | SYMMETRY can re-center the folder when the incoming signal carries a DC offset | SYMMETRY position found that restores symmetric folding (even harmonics minimized) | | Essential Parameters, SYMMETRY; Common Mistakes on noise and DC |
| T12 | A sine in IN 1 and a second oscillator in IN 2, then swapped | The jacks are identical and mixed together | Identical output when swapped; both signals present together | | Essential Parameters, IN |
| T13 | MAIN versus ALT, same settings, matched level | ALT is a more mellow sound for most input signals; fold levels and directions vary between stages | Spectral centroid or high-harmonic level on ALT is lower than on MAIN at three FOLD settings; record where they are nearly identical (the guide predicts little difference at low fold) | | Quick Start step 7; Patch 2 listening; ⚠️ on how much outputs differ |
| T14 | Patch 1 full: First Voice, then Fold 6 inserted with SHAPE minimum | The sine appears first, then overtones in stages, ending in a dense bright spectrum | As T2 inside the voice; the VCA and envelope behave | | Patch 1 |
| T15 | Patch 2 full: FOLD fixed, SHAPE swept on MAIN, then cable to ALT | MAIN moves from folded and bell-like toward pulse-like and harsher; ALT sounds softer | Both findings, as T4 and T13 | | Patch 2 |
| T16 | Patch 3 full: Zadar OUT A (0 V to 10 V) into IN, MAIN to Black Polyvoks CV1, single-shot Bank A shape of one to two seconds | With FOLD low the cutoff opens and closes once per note; as FOLD rises the shape gains peaks; SYMMETRY changes which part folds | Record Zadar OUT A voltage range; peaks per note at three FOLD settings; effect of SYMMETRY. Measure MAIN voltage range as -5 V to +5 V | | Patch 3 ⚠️; draft block item 4 |
| T17 | Patch 3 at the cable move: same, ALT into CV1 | ALT gives a different contour shape | Contour shape differs from MAIN; record how | | Patch 3 Move the cable |
| T18 | Patch 3 failure case: raise FOLD until a negative portion of the contour closes the filter | The filter dives shut and stays there; lower FOLD or the attenuverter to recover | Failure reproduced; the stated fix recovers | | Patch 3 listening |
| T19 | Patch 4 full: Marbles X2 into FOLD CV, STEPS about 2 o'clock, DEJA VU about 11 o'clock, nine cables | Each note has its own harmonic density; ALT sounds softer and less filtered | Fold depth differs per note; nine cables counted; ALT layer behaves as stated | | Patch 4 |
| T20 | Marbles X2 voltage span measured at its default and at each range setting | X2 relative to the FOLD CV range is unverified; scale with an attenuator if too extreme | Measured X2 range in volts; whether any attenuation is needed; update the instruction to match | | Draft block item 4; Patch 4 ⚠️ |
| T21 | Feedback loop (Advanced Learning Path step 7): oscillator into one IN, MAIN back into the other, take audio from ALT. Mixer low | The path is DC-coupled, so a loop can latch at a fixed level or turn noisy; FOLD and SYMMETRY recover it; a slow modulation at FOLD CV keeps it moving | Describe which behavior occurs at which setting; record whether FOLD and SYMMETRY recover a latch | | Advanced Learning Path step 7 ⚠️ |
| T22 | FOLD and SHAPE at maximum, noise and DC measured at MAIN and ALT | Some noise and DC offset are to be expected, especially at high FOLD and SHAPE | DC offset in millivolts at both outputs; noise visible on the scope | | Common Mistakes, "noise and DC offset" |

Not tested: reverse-polarity protection (the guide states a MOSFET protects against it). It is destructive to test and is stated from the manual only.

## Failure handling

Follow the template. T7 and T13 are the likeliest to change guide text, since the manual is silent on the first and the guide predicts only a loose difference for the second.

## Closing steps

- [ ] Remove the draft status block from the guide.
- [ ] Remove the ⚠️ markers the results above cleared, and only those.
- [ ] Resolve Depth in Key Specifications to the measured value (M1), marked as the user's own measurement.
- [ ] Commit the guide changes separately from the results in this file.
- [ ] Mark this plan "Complete" with the date.
