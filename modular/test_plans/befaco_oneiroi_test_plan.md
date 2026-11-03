# Befaco Oneiroi: Test Plan

Verification plan for `modular/befaco_oneiroi_guide.md`. Format: `tooling/test_plan_template.md`. Clears the draft status block and every ⚠️ in the guide.

| Field | Value |
|---|---|
| Module | Befaco Oneiroi |
| Guide | `modular/befaco_oneiroi_guide.md` (draft, 2026-10-24) |
| Plan type | Verification |
| Firmware | Not yet read (M5) |
| Tested on | Not yet tested |
| Sources | Befaco Oneiroi user manual, last updated 2025-03-03 |
| Status | Not started |

## Tools

Mordax Data (scope and spectrum), multimeter, tuner, sequencer with 1V/octave output and a clock (Squarp Hermod+ or Marbles X1 and t outputs), Mutable Instruments Rings (Patch 2 source), 4ms RCD v2, Pamela's PRO Workout, Endorphin.es Ground Control, Marbles, stereo mixer, a slow LFO for CV tests. Safety: start with the mixer low for every test that involves resonance, echo repeats, sound-on-sound, or a loop.

## Measurement block (run first)

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth with the 10-pin to 16-pin cable fitted (guide: 25 mm) | Tape measure | |
| M2 | Current on +12V, -12V, +5V (guide: 200 mA, 80 mA, 0 mA) | Multimeter in the supply line, at idle and with all faders up | |
| M3 | Power connector polarity marking | Photograph the board header | |
| M4 | Front-panel photograph | Square on, even light, no hands, no cables | |
| M5 | Firmware version (guide: from patch 1.1 the RECORD LED blinks major, RANDOM LED blinks minor, at boot) | Power on and watch the LEDs | |

## Test order

M block, then T1 to T5 (basic voice and pitch, everything else depends on it), then T6 to T14 (effects and the Shift layer), then T15 to T26 (looper), then T27 to T40 (mapping, randomizer, save), then T41 to T52 (clocked patch). Pitch first because Patches 1, 3 and 4 all assume a tracking V/OCT. Clock lock before any clocked claim because Patch 4 depends on it.

## Tests

| ID | Setup | Prediction (guide) | Pass criterion | Result | Clears |
|---|---|---|---|---|---|
| T1 | Quick Start 1 and 3: OUT L to mixer only, SINE fader up, nothing else | The left output normals to the right; one cable gives a mono signal | With only OUT L patched, record what reaches both mixer channels. With OUT L and OUT R patched, record whether the two channels differ on the scope with the supersaw detuned | | Quick Start step 1; Patch intro paragraph |
| T2 | Sequencer CV 0 V to 5 V in 1 V steps into V/OCT, SINE fader only, PITCH centered, tuner or spectrum | V/OCT sums with PITCH and tracks one octave per volt | Peak frequency doubles per volt within 10 cents per octave; record the error per octave | | Essential Parameters, oscillators |
| T3 | As T2, extend 0 V to 10 V | The input tracks ten octaves across 0 V to 10 V and clips outside the range | Record where tracking stops at top and bottom. Also record the audible range: the guide states both "eight octaves, C0 to C7" and "ten octaves across 0 V to 10 V", which disagree | | Essential Parameters, oscillators; resolves the eight-versus-ten-octave statement |
| T4 | PITCH knob end to end with V/OCT at 0 V; then SHIFT plus PITCH through the octave positions | PITCH is centered on C and spans six semitones either side; SHIFT plus PITCH picks the octave | Measured span within 6 semitones either side (cents); octave steps are one octave each | | Essential Parameters, oscillators |
| T5 | Patch 1 First Voice: sequencer CV to V/OCT, OUT L and OUT R to the mixer, SINE only | A steady tone appears at both channels and follows the note | Tone present on both channels; pitch follows a changed note | | Patch 1 First Voice |
| T6 | Oscillator switch up, SS/WT fader up with SINE up, DETUNE from center up | The seven saws spread apart as DETUNE rises | Spectrum shows the saw cluster widening monotonically; count the distinct peaks at a small detune | | Quick Start step 4 and 5; Patch 1 |
| T7 | Oscillator switch down, SS/WT up, DETUNE (OFFSET) end to end | OFFSET selects one of 32 wavetables extracted from the looper buffer | Count distinct timbres across the range; record the number of steps. Repeat after recording new audio and confirm the timbres change | | Essential Parameters, DETUNE |
| T8 | SHIFT plus DETUNE, supersaw on | 50 percent is unison, 0 percent is an octave down, 100 percent an octave up | Measured interval at 0, 50 and 100 percent | | Essential Parameters, UNISON |
| T9 | FILTER fader up, SHIFT plus CUTOFF stepped through all positions, sweep CUTOFF on a supersaw | Low-pass, band-pass, high-pass and comb modes; CUTOFF spans about 10 Hz to 22 kHz | Four modes identified on the spectrum; record the lowest and highest cutoff frequencies | | Patch 1 listening; Essential Parameters, Filter |
| T10 | RESO past 75 percent with no input | A chaotic noise generator activates, audible with no input | Output present with all source faders down. Mixer low | | Essential Parameters, Filter |
| T11 | SHIFT plus RESO through the four positions | The filter sits at the beginning, between resonator and echo, between echo and ambience, or at the end | Four distinct behaviors; record each against the guide's list | | How Oneiroi Is Organized |
| T12 | AMBIENCE fader up, DECAY from minimum to maximum, a held note | The reverb tail lengthens with DECAY | Measure tail length with the scope at three DECAY settings | | Quick Start step 6; Patch 1 |
| T13 | SPACETIME from 0 to 50 to 100 percent with a short note | At 50 percent the size is smallest and brightest; at 0 or 100 percent largest and darkest; below 50 percent reverses the input | Size order confirmed; reversal audible below 50 percent | | Essential Parameters, Ambience |
| T14 | Effect fader at its lowest position with a source playing | The signal passes to the next unit unaffected, not muted | Signal present with all four effect faders down | | Patch 1 listening; How Oneiroi Is Organized |
| T15 | RESONATOR fader up, TUNE and FEEDBACK sweep, FEEDBACK at 100 percent | Three comb instances; at 100 percent it self-oscillates; SHIFT plus TUNE adds dissonance | Self-oscillation present at 100 percent; three tuning peaks on the spectrum; dissonance raises the spacing. Mixer low | | Essential Parameters, Resonator |
| T16 | ECHO fader up, DENSITY end to end, REPEATS 0 to 100 percent, no clock | DENSITY sets 10 ms to 4 s; REPEATS from one repeat to infinite | Measure the shortest and longest delay on the scope; count repeats at 0 percent; infinite at 100 percent. Mixer low | | Essential Parameters, Echo |
| T17 | IN GAIN in each of its three positions with a Eurorack-level source, then a line-level source | Top for high impedance, middle for line, bottom for Eurorack level; the LED is green for signal, red for clipping | Record the level at which the LED turns red in each position | | Essential Parameters, input and gain |
| T18 | PRE/POST switch with RECORD held: PRE then POST | LED monitors the input on PRE and the module output on POST | LED follows the input on PRE and the output on POST | | Essential Parameters, input and gain |
| T19 | Looper fader up before any recording | The buffer is prefilled with white noise | Noise present; spectrum is flat | | Quick Start step 7 |
| T20 | RECORD tap to start and tap to stop; then hold to record and release | A single press toggles recording; holding records until release | Both behaviors confirmed; record LED behavior | | Essential Parameters, looper |
| T21 | RECORD IN gate: 2 V, 0.5 V and 5 V gates | Records while high, above 1 V, stops at 0 V | Threshold between 0.5 V and 2 V confirmed | | Essential Parameters, looper |
| T22 | Record a click, play the loop at full LENGTH, time the repeat on the scope | The buffer is about five seconds | Loop period in seconds | | Key Specifications, Looper |
| T23 | LENGTH to minimum, VARISPEED at +1x, 0 and -1x, then 2x; spectrum | At minimum length the looper is an oscillator: C3 at plus or minus 1x, C2 at 0.5x, C4 at 2x, and it does not track V/OCT | Pitches measured against the stated notes; V/OCT changes it or does not | | Essential Parameters, looper |
| T24 | VARISPEED end to end with a recorded loop | Reverse at twice speed at 0 percent, forward at twice at 100 percent, stalled only at 12 o'clock | Direction and speed at the three positions; the stall point | | Patch 2 Move the cable; Essential Parameters |
| T25 | SHIFT plus START (SOS) at 0, 50 and 100 percent, record over a loop | At 0 percent the old material is constantly replaced; at 100 percent it never fades | Number of passes before the old layer is inaudible, at each setting | | Patch 2; Essential Parameters |
| T26 | SHIFT plus LENGTH during sound-on-sound: noon, clockwise, counterclockwise | Noon applies no filter; clockwise high-pass; counterclockwise low-pass | Spectrum of the decaying layer at each position | | Essential Parameters, looper |
| T27 | Patch 2 full: Rings ODD to IN L, Rings EVEN to IN R, IN GAIN bottom, PRE, record Rings, then LOOPER up and INPUT down | The loop repeats the Rings phrase and new passes stack on older material | Loop repeats; layers stack; the older layer fades at the SOS setting | | Patch 2 setup and listening |
| T28 | Rings recorded with VARISPEED at 100 percent and 0 percent | Twice speed forward rises an octave; reverse sounds backward | Octave shift measured; reversal heard | | Patch 2 listening |
| T29 | SHIFT plus RECORD (clear) | Erases the buffer | Buffer silent or restored to noise afterwards; record which | | Essential Parameters, looper |
| T30 | MOD AMT pressed once | The button blinks red; turning a knob sets how much internal modulation that parameter receives | LED color red; modulation reaches the knob's parameter | | Patch 3; How Oneiroi Is Organized |
| T31 | SHIFT plus MOD AMT | The button blinks green; turning a knob sets how much of its CV the parameter receives, 100 percent by default | LED color green; default is 100 percent | | How Oneiroi Is Organized |
| T32 | From the red page, find how to leave it (try MOD AMT, SHIFT, waiting) | Not stated in the manual | Record the exact method that exits the page | | Draft block item 5; Patch 3 ⚠️ |
| T33 | RECORD plus RANDOM on each page | Clears the mapping of whichever page is open | Mapping cleared on the open page only | | How Oneiroi Is Organized |
| T34 | Patch 3: map DETUNE and SPACETIME, raise MOD LEVEL, SPEED slow, SHIFT plus SPEED through all seven types | Seven types morph smoothly: chaos, sine, ramp, sawtooth, square, sample and hold, envelope follower | Seven distinct behaviors seen on the modulation LED or the destination | | Patch 3; Essential Parameters, modulation |
| T35 | SPEED end to end, unsynced, measure LFO rate with the scope on the modulation LED or a mapped destination | The base is about 0.2 Hz; range about 0.01 Hz to about 3 Hz | Measured minimum and maximum rate | | Essential Parameters, modulation |
| T36 | Envelope follower type with PRE then POST | It follows the input or the output depending on PRE/POST | Follower tracks the input on PRE and the output on POST | | Essential Parameters, modulation |
| T37 | TARGET at oscillators, AMOUNT at the middle position, press RANDOM ten times; then AMOUNT top and bottom | Variation of plus or minus 20 percent in the middle position and plus or minus 2 percent in the lower; faders excluded; pitch in semitones | Pitch changes are whole semitones; faders do not move; size of change by position | | Patch 3; Essential Parameters, randomizer |
| T38 | SHIFT plus RANDOM, then again | Undoes, then redoes | Previous sound returns, then the new one | | Patch 3; Quick Start step 8 |
| T39 | Hold RANDOM for several seconds and release | A gradual morph; the button flashes twice when it finishes | Morph audible; two flashes at the end | | Essential Parameters, randomizer |
| T40 | Hold MOD AMT for two seconds, power off, power on | The LED blinks to confirm the save; parameters and mappings return; the looper buffer does not | LED behavior recorded exactly; settings return; buffer returns as noise | | Patch 3 save; draft block item 5 |
| T41 | Catch and jump: startup with RECORD and RANDOM held, then SHIFT to toggle; move a knob after RANDOM | Catch ignores the knob until it reaches the stored value; jump follows at once; jump is the default | Default is jump; catch behavior confirmed; record the LED colors for a catch state | | Draft block item 2; Common Mistakes, "I turned a knob and nothing happens" |
| T42 | SHIFT plus RECORD plus RANDOM | Resets every parameter to the actual position of its control | Every parameter matches its knob afterwards | | Essential Parameters, randomizer |
| T43 | SYNC IN with a clock, no divider: 1 V, 0.5 V, 5 V triggers | Triggers of at least 1 V are accepted | Threshold between 0.5 V and 2 V | | Key Specifications |
| T44 | SYNC IN lock: start a bar-rate clock, time from first trigger until the echo and auto-pan settle | A couple of seconds to lock | Seconds to lock, three runs | | Draft block item 4; Patch 4 |
| T45 | Remove the SYNC cable, time the return to the internal clock | A similar time; internal clock about 0.2 Hz | Seconds to fall back; internal period measured on the SYNC LED (expected about 5 s, one buffer) | | Patch 4; How Oneiroi Is Organized |
| T46 | External clock at 30 BPM, 120 BPM and 300 BPM, one trigger per beat | Supported speeds run from 30 BPM to 300 BPM | Lock at the extremes; behavior outside them | | How Oneiroi Is Organized |
| T47 | Clock at one trigger per beat versus one per bar | The manual advises one trigger per bar or slower | Describe what changes in echo, auto-pan and modulation at the faster rate | | Patch 4 |
| T48 | Marbles X1 into V/OCT, read X1 range with the multimeter at the Marbles voltage range settings | X1 must stay positive, since V/OCT is 0 V to 10 V | Measured X1 span at each range setting; whether any note clips | | Draft block item 3; Patch 4 ⚠️ |
| T49 | Marbles t2 into RANDOM IN, effects target, middle amount | Each trigger above 1 V runs the randomizer | Randomization on each trigger; threshold between 0.5 V and 2 V; the gradual morph is not available from this input | | Patch 4 |
| T50 | Bar-rate table: RCD v2 fed a quarter-note clock at /4 and /8; 16th-note clock at /16 | One trigger per bar at the stated divisions; /16 needs Max Div 16 or higher | One trigger per bar measured; which output carries /16 | | Patch 4 ⚠️ (RCD v2 line) |
| T51 | Pamela's PRO Workout: PPQN set to match a 24 PPQN clock, an output at /4 | One trigger every four beats, which is one bar | One pulse per bar measured | | Patch 4 ⚠️ (Pamela's line) |
| T52 | Ground Control clock out set to one bar, straight to SYNC IN | The clock output has dividers from 1/32 to 4 bars and needs no divider module | Divider range confirmed; lock achieved | | Patch 4 ⚠️ (Ground Control line) |
| T53 | Hermod+ system menu, look for a clock divider; otherwise a one-step-in-sixteen track | The guide does not document a divider; a spare track with a step 1 trigger works | Menu finding recorded; spare-track method gives one gate per bar | | Patch 4 ⚠️ (Hermod+ line) |
| T54 | Patch 4 full: clock, divider, Marbles X1 and t2, effects target, middle amount | After a few seconds echo time and auto-pan settle to ratios of the clock, modulation follows the beat, X1 changes pitch, t2 changes the effects | All four events observed; DENSITY works as a divider of the clock | | Patch 4 listening |

## Failure handling

Follow the template. In particular, T3 (the eight-versus-ten-octave disagreement) and T32 (the unknown exit from the mapping page) are expected to change guide text, not only clear flags.

## Closing steps

- [ ] Remove the draft status block from the guide.
- [ ] Remove the ⚠️ markers the results above cleared, and only those.
- [ ] Replace Depth and Power in Key Specifications with measured values, marked as the user's own measurements.
- [ ] Commit the guide changes separately from the results in this file.
- [ ] Mark this plan "Complete" with the date.
