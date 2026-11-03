# Bastl Instruments Pizza: Test Plan

Verification plan for `modular/bastl_instruments_pizza_guide.md`. Format: `tooling/test_plan_template.md`. Clears the draft status block and every ⚠️ in the guide.

| Field | Value |
|---|---|
| Module | Bastl Instruments Pizza |
| Guide | `modular/bastl_instruments_pizza_guide.md` (draft, 2026-11-02) |
| Plan type | Verification |
| Firmware | Not yet read (M5); the manual covers 1.1 |
| Tested on | Not yet tested; the module ships the week of 2026-11-02 |
| Sources | Bastl Pizza manual, firmware 1.1, 22 pages; Synth Anatomy announcement article, 2022-05-31 |
| Status | Not started |

## Tools

Mordax Data (scope and spectrum), multimeter, tape measure, tuner, sequencer with 1V/octave output and gate (Squarp Hermod+ or Marbles), Make Noise Maths, a VCA (Vostok Instruments Ceres or Erica Synths Pico VCA2), 2hp LFO v2, Erica Synths Pico QUANT, Marbles, a stereo mixer, a computer with a micro-USB cable (firmware tests). Safety: start with the mixer low for every test with FOLD, RING or high FM index.

## Measurement block (run first)

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth with the power cable fitted (guide: not published) | Tape measure | |
| M2 | Current on +12V and -12V (guide: not published; +5V expected none) | Multimeter in the supply line, at idle and with FOLD, RING and FM INDEX engaged | |
| M3 | Power connector polarity marking | Photograph the header; the manual says red stripe to -12 V | |
| M4 | Front-panel photograph | Square on, even light, no hands, no cables. Save as `modular/images/bastl_instruments/pizza/front_panel.jpg` and record the source in `images/SOURCES.md` | |
| M5 | Firmware version (the manual says it is shown as a static light of the LEDs at startup) and board revision (V0.6 on the manual cover, V1.0 in the back-of-board diagram) | Power on and watch the LEDs; read the back of the board | |

## Test order

M block, then T1 to T5 (boot, calibration, pitch), then T6 to T16 (FM, shape, CTRL), then T17 to T23 (outputs and envelope VCA), then T24 to T31 (patches), then T32 to T34 (firmware, last because it changes state). Calibration first because every pitch claim assumes a tracking V/OCT.

## Tests

| ID | Setup | Prediction (guide) | Pass criterion | Result | Clears |
|---|---|---|---|---|---|
| T1 | Power on in the rack | If the V/OCT input needs calibration, two flashes appear near the OCT OSC button with the lights on the left pointing down | Record whether the module boots to normal or shows the two flashes | | Common Mistakes, calibration |
| T2 | If T1 showed the flashes: patch OCT OSC into V/OCT, wait, unplug | The module boots to normal operation | Normal operation after the unplug; seconds needed | | Quick Start step 2; Common Mistakes |
| T3 | Hold SHAPE and PITCH; press PITCH; patch OCT OSC to V/OCT; unplug when all LEDs are on | Automatic calibration completes | LEDs behave as described; exit with SHAPE and PITCH together works | | Calibration and Boot Settings |
| T4 | Sequencer CV at 0 V to 5 V in 1 V steps into V/OCT, FM INDEX center, tuner | V/OCT is accepted from -5 V to +8 V and tracks 1 V per octave | Error in cents per octave; record the limits at -5 V and +8 V | | Key Specifications; Essential Parameters |
| T5 | PITCH button: short press OCTAVE then DETUNE; knob end to end in OCTAVE | OCTAVE spans plus or minus four octaves | Measured span in octaves | | Essential Parameters |
| T6 | FM INDEX at center, SHAPE at center, MAIN to scope and spectrum | MAIN is a plain sine | Spectrum shows a single peak; record harmonic distortion | | Quick Start step 4; Common Mistakes |
| T7 | FM INDEX left, RATIO OSC button stepped through the four ratios; then right, OCT OSC button through four octaves | Left uses the RATIO oscillator and right the OCT oscillator; four ratios and four octaves | Spectrum differs between the four positions on each side; count them | | Quick Start steps 5 and 6 |
| T8 | RATIO SETTING mode: set 3/2, then other fractions; check the LED behavior | Numerator and denominator each 1 to 16; PITCH toggles; OCTAVE LED for numerator and DETUNE LED for denominator; TUNE LED blinks on each change | Interval measured against a tuner for 3/2, 5/4, 2/1; LED behavior as stated | | Essential Parameters; Patch 1 |
| T9 | Set a ratio, power off and on, then hold SHAPE at power-up | Ratios and CTRL assignment are remembered; holding SHAPE at power-up resets them | Settings persist across a power cycle; reset restores defaults | | Calibration and Boot Settings; Common Mistakes |
| T10 | DETUNE: knob right of center, then left, at two pitches an octave apart | Right is exponential; left is linear in hertz with constant beating | Beat frequency measured at both pitches: it changes with pitch on the right and stays constant on the left | | Essential Parameters; Patch 3 |
| T11 | PITCH long press: TUNE mode, then second press | Knob transposes plus or minus 12 semitones, then fine tunes plus or minus 120 cents | Measured span of each | | Essential Parameters |
| T12 | PITCH held for six seconds, then two seconds | Coarse pitch mode with a very wide frequency range; two seconds leaves it | Frequency range measured at the extremes | | Essential Parameters |
| T13 | SHAPE in FOLD mode: fader left of center, then right, a fixed pitch | Left is the Buchla 259-inspired fold with mainly odd harmonics; right is the Chebyshev-based fold with all harmonic intervals | Spectrum on each side: odd harmonics dominate on the left, even and odd on the right | | Essential Parameters; Historical Context |
| T14 | FOLD at increasing amounts, fundamental level measured | Folding weakens the fundamental | Fundamental level against fold amount; the remedy (mixing OCT OSC) restores it | | Common Mistakes, bass |
| T15 | SHAPE in WAVE mode with FM INDEX engaged; SHAPE in RING mode, fader left then right | WAVE shapes the modulators; RING works like FM INDEX, RATIO on the left and OCT on the right | Audible changes as stated; ring modulation depth by side | | Essential Parameters |
| T16 | FM INDEX right with SHAPE in RING mode left | FM INDEX and RING can use different modulators at once | Both effects present together on the spectrum | | Patch 3; Why This Instrument Excels |
| T17 | FM INDEX CV: patch a stepped CV (0 V, 2.5 V, 5 V, then negative values) with the fader at center, then left of center; INDEX MOD right and left of center | The manual does not state whether CV adds to the fader or replaces it; INDEX MOD right applies the voltage as it comes and left inverts it | Compare the spectrum of fader-plus-CV against the fader alone at the same total position; record add, replace, or other | | Draft block item 3; Essential Parameters; Patch 1 |
| T18 | Repeat T17 on SHAPE CV and on CTRL CV (CTRL assigned to OCTAVE) | As T17 | Same method; record separately for each | | Draft block item 3; Essential Parameters |
| T19 | EXT with a sine from New Godspeed, then remove | A cable in EXT replaces the octave oscillator as the modulator, from -6 V to +6 V | Modulator changes; spectrum differs from the octave oscillator | | Essential Parameters; Pairs Well With |
| T20 | SYNC with a clock: record the phase reset on the scope; test thresholds 0.5 V, 2 V, 5 V | SYNC resets the phases of all three oscillators and accepts -6 V to +6 V | Reset visible on the scope; threshold between 0.5 V and 2 V | | Draft block item 6; Essential Parameters |
| T21 | Output levels: MAIN, OCT OSC and PULSE at high FOLD and FM | Each ranges about -5 V to +5 V | Peak to peak at each, in volts | | Key Specifications |
| T22 | PULSE output with FM INDEX and its modulation: read the width; then hold RATIO and OCT OSC at power-up | PULSE is a pulse version of MAIN before the FM, width set by FM INDEX; the power-up combination toggles it to the RATIO oscillator; the module remembers | Width changes with FM INDEX; toggle works; setting persists | | Essential Parameters; Calibration and Boot Settings |
| T23 | PULSE noise: scan the settings with the spectrum running | PULSE uses a lower-quality converter and may produce audible noise in some settings | Record the settings at which noise appears and its level | | Draft block item 5; Common Mistakes |
| T24 | Hold SHAPE, assign each CTRL destination in the table in turn, with CTRL CV from a slow LFO | Fifteen destinations with the LEDs in the table | Count the destinations; LEDs match the table; record any that differ | | CTRL Destinations |
| T25 | CTRL assigned to a shape mode different from the SHAPE button's mode | Two shapers run at once | Both effects present together | | CTRL Destinations; Advanced Learning Path step 4 |
| T26 | Envelope VCA mode (WAVE, RING and FOLD LEDs): gate into SYNC, MAIN to scope, CTRL left and right of 12 o'clock, FM INDEX CV empty, INDEX MOD right | Right of 12 adds decay only, left adds attack and decay; the envelope drives the built-in VCA and is normalled to FM INDEX | Attack and decay times measured at both knob positions; FM index follows the envelope | | Patch 2; CTRL Destinations; Draft block item 6 |
| T27 | Envelope VCA mode with a cable in the FM INDEX CV jack | The envelope is normalled to FM INDEX only when nothing is patched | Envelope no longer moves the index when a cable is present | | CTRL Destinations; Common Mistakes |
| T28 | Bipolar VCA (RING and FOLD LEDs) with an envelope in CTRL CV | The built-in VCA acts on MAIN and OCT OSC | Output level follows the envelope on both outputs | | CTRL Destinations; Advanced Learning Path step 6 |
| T29 | Patch 1 full: Hermod+ CV to V/OCT, gate to Maths Ch1 TRIG, Ch1 Unity to VCA, Ch1 Variable to FM INDEX CV, ratio 3/2 | Each note starts bright and settles to a plainer tone | Brightness falls with the envelope; direction correct, or flipped by INDEX MOD; six cables | | Patch 1 |
| T30 | Patch 2 full: gate into SYNC, CTRL in envelope VCA mode, MAIN to the mixer | Each gate produces a note that rises and falls; every attack is identical because SYNC resets the phase | Notes triggered by the gate; attacks identical over ten repeats; three cables | | Patch 2 |
| T31 | Patch 3 full: SHAPE in RING left, FM INDEX right, linear detune, 2hp LFO v2 on SHAPE CV, OCT OSC to a second channel; then the LFO moved to FM INDEX CV | A steady beating that does not change with pitch; slow motion of the ring modulation; moving the cable changes which modulation moves | Beat frequency constant across pitches; effect of each cable position | | Patch 3 |
| T32 | Patch 4 full: Marbles X1 through Pico QUANT to V/OCT, X2 into CTRL CV (OCTAVE), t2 to Maths Ch1 TRIG | Notes stay in the scale while the register jumps across octaves | Notes in scale; register jumps; X1 range stays positive; X2 span against the CTRL octave range; seven cables | | Patch 4 |
| T33 | Firmware update entry: try holding PITCH while plugging in USB, then holding TUNE at power-up | The manual gives both; neither is verified | Record which one makes the module appear as a disk. Do this last; the update changes state | | Draft block item 4; Common Mistakes, Firmware |
| T34 | Factory reset (SHAPE and OCTAVE) and calibration afterwards | Resets user settings and calibration | Settings and calibration restored to defaults; recalibration works | | Calibration and Boot Settings |

## Failure handling

Follow the template. T17 and T18 are expected to change guide text: the patches are written around the assumption that the fader starts near neutral.

## Closing steps

- [ ] Remove the draft status block from the guide.
- [ ] Remove the ⚠️ markers the results above cleared, and only those.
- [ ] Replace Depth and Power in Key Specifications with measured values, marked as the user's own measurements.
- [ ] Confirm that the front panel image link in the guide points to the photograph from M4.
- [ ] Commit the guide changes separately from the results in this file.
- [ ] Mark this plan "Complete" with the date.
