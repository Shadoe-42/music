---
title: Bastl Instruments Pizza
manufacturer: Bastl Instruments
primary_role: SOURCE
secondary_roles: []
historical_context: true
form_factor: eurorack
functions: [fm-oscillator, wavefolder]
behavior_tags: [harmonic, inharmonic, nonlinear, sensitive, performance-oriented]
use_cases: [lead voice, bass voice, bell and metallic tones, self-contained pluck voice]
hp: 8
price_eur: 297
memory: basic
transport: none
screen: false
hybrid: false
cv: full
inputs: [V/OCT, SYNC, EXT, FM INDEX CV, SHAPE CV, CTRL CV]
outputs: [MAIN, OCT OSC, PULSE]
patch_format: v1
---

# Bastl Instruments Pizza

**Digital phase-modulation oscillator with a user-set ratio oscillator, two folders, ring modulation, and an assignable control in 8 HP**

![Bastl Instruments Pizza](https://github.com/Shadoe-42/music/raw/main/modular/images/bastl_instruments/pizza/front_panel.jpg)
*Bastl Instruments Pizza: PITCH knob and button, FM INDEX fader, INDEX MOD knob, OCT OSC and RATIO OSC buttons, SHAPE fader and button, CTRL knob, and the jacks for V/OCT, SYNC, EXT, FM INDEX CV, SHAPE CV, CTRL CV, PULSE, MAIN, and OCT OSC*

> **Draft status (2026-11-02):** Written from the official Bastl Pizza manual (22 pages, firmware 1.1) and press coverage from the May 2022 announcement, before the module was in hand. Every control, range, and button combination comes from that manual. All four patches are untested on hardware and are marked ⚠️. Open items to clear on hardware: (1) every patch setting and every "What to listen for" result; (2) depth and current draw, which neither the manual nor the coverage gives, and which are measured on the module; (3) whether CV at FM INDEX CV, SHAPE CV, and CTRL CV adds to the fader or knob position or replaces it, which the manual does not state; (4) the contradiction between the manual's two firmware update entries (hold PITCH while plugging in USB on page 19, hold TUNE at power-up on page 20); (5) which settings make the PULSE output audibly noisy; (6) the trigger threshold of SYNC and how the envelope VCA mode behaves when SYNC is also resetting the oscillator phases; (7) the board revision on the shipped unit (the manual shows V0.6 on the cover and V1.0 in the back-of-board diagram); (8) the front panel image link below points to the location for the photograph taken in the test plan, and shows nothing until that photograph is added. Remove this block when the items are cleared.

---

## Historical Context

The synthesis at the center of the Pizza was found by accident on a mainframe. In the autumn of 1967, John Chowning was modeling two sine-wave oscillators on the computer in Stanford's artificial intelligence laboratory. He raised the rate of a vibrato beyond what a human touch could produce, and the effect stopped sounding like a pitch wobble and became a change of timbre; more rate and depth gave more and more complexity. He later took the observation to an undergraduate mathematics student, and the two found that the equations of FM radio transmission matched what he heard. Stanford, to which Chowning had assigned his patents, looked for licensees in the early 1970s, and Yamaha sent the engineer Kazukiyo Ishimura to meet him; the F-70 came out in 1981, seven years after the license by Yamaha's own account, and the DX7 followed in 1983. The Pizza follows this lineage in its structure: the manual describes digital FM, with a main oscillator as the carrier and two other oscillators as modulators, applied as phase modulation.

The shaping section borrows from a different tradition. Don Buchla's Model 259 Complex Waveform Generator, dated by the Buchla Archives to about 1976, passes a sine wave from its principal oscillator through a Timbre control that sets its amplitude before a waveshaper: at minimum the output is roughly a sine, and as the amplitude rises the curve exceeds a threshold, folds back over itself, and gains more folds and more overtones, which the archive describes as a complex, jagged, and harmonically rich shape. An internal modulation oscillator can move that amplitude. The Pizza manual credits this design directly: the left side of its FOLD mode is inspired by the Buchla 259 and yields mainly odd harmonics, while the right side uses an original digital algorithm based on Chebyshev polynomials that folds one sine peak asymmetrically and produces all harmonic intervals. Ring modulation, the third mode of the same SHAPE fader, multiplies the main oscillator by one of the modulators.

Bastl Instruments came out of art and music in Brno. By its own history page, the company began in 2011 as the art project Standuino and became Bastl Instruments in 2013, founded by Ondřej Merta and Václav Peloušek, who started as bandmates and artists. Bastl is the Czech word for DIY, and the history page names Casper Electronics' Peter Edwards as a collaborator and Binary Labs in Dresden as a partner. The Pizza was announced at Superbooth 22 in May 2022 as an 8 HP digital oscillator at 297 euros (270 US dollars), and Synth Anatomy reported that development had taken about three and a half years. The manual credits Florian Helling and Martin Klecl with development, Peloušek with supervision, and Lennart Schierling of Binary Labs with the bootloader.

Three things set the Pizza apart from a plain FM voice. Two modulators share one carrier, one with a fixed octave relationship and one whose ratio the player sets from a numerator and denominator, each from 1 to 16. A single SHAPE fader holds two folders and a ring modulator, neutral at the center. And one assignable control, CTRL, can be pointed at fifteen destinations, including a built-in envelope and amplifier that turn the oscillator into a complete voice.

---

## Quick Start: First Sound in 5 Minutes

The Pizza is a carrier oscillator with two modulators and a shaping section. With the FM INDEX fader at its center and the SHAPE fader at its center, MAIN is a plain sine. Every step below moves one control away from that starting point, so each change is audible by itself. ⚠️ Untested on hardware.

1. **Power the module with the red stripe toward -12 V.** The manual requires +12 V and -12 V and shows protection circuits, but accepts no responsibility for a reversed ribbon. Disconnect power before connecting the cable.
2. **Patch a pitch CV into V/OCT.** The input accepts -5 V to +8 V. If the module boots with two flashes near the OCT OSC button and the lights on the left pointing down, patch the OCT OSC output into V/OCT for a few seconds and unplug it (see Calibration and Boot Settings).
3. **Patch MAIN to a mixer channel with the level low.** MAIN swings about -5 V to +5 V.
4. **Hear the plain sine.** With FM INDEX at the center, the manual says MAIN is a sine with no shaping.
5. **Move the FM INDEX fader to the left.** The RATIO oscillator now modulates the carrier. Press the RATIO OSC button to step through its four ratios and hear the timbre change at each.
6. **Move FM INDEX to the right.** The OCT oscillator modulates instead. Press the OCT OSC button to step through four octaves.
7. **Press the SHAPE button to choose WAVE, FOLD, or RING.** Move the SHAPE fader away from the center in FOLD mode; the folds add overtones, and the left and right halves fold differently.
8. **Press the PITCH button to switch between OCTAVE and DETUNE.** DETUNE moves the two modulators away from the carrier.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 8 HP |
| Depth | Not published; measured in the test plan ⚠️ |
| Power | Not published ⚠️ +12V / Not published ⚠️ -12V / 0 mA +5V ⚠️ |
| Oscillators | Three: MAIN (carrier), OCT OSC and RATIO OSC (modulators) |
| Synthesis | Digital FM, applied as phase modulation |
| Shaping | WAVE, FOLD, RING on one fader; second shaper through CTRL |
| Controls | PITCH knob and button, FM INDEX fader, INDEX MOD knob, OCT OSC and RATIO OSC buttons, SHAPE fader and button, CTRL knob |
| Inputs | V/OCT (-5 V to +8 V), SYNC (-6 V to +6 V), EXT (-6 V to +6 V), FM INDEX CV, SHAPE CV, CTRL CV (each -6 V to +6 V) |
| Outputs | MAIN, OCT OSC, PULSE (each -5 V to +5 V) |
| Price | 297 euros at announcement (270 US dollars) |
| Firmware | Updated over micro-USB from a computer; the manual covers version 1.1 |

The manual gives no width, depth, current draw, or price; width and price come from the announcement coverage, and depth and current are blank until the module is measured. The manual lists +12 V and -12 V and no +5 V rail. A micro-USB socket on the back of the board is for firmware only.

---

## Essential Parameters

**PITCH, OCTAVE, and DETUNE.** A short press of the PITCH button toggles the knob between OCTAVE and DETUNE. In OCTAVE the knob moves the pitch across plus or minus four octaves. In DETUNE the knob moves the two modulators away from the carrier: to the right of center the detune is exponential, scaling with pitch, and to the left it is linear in hertz, so the beating rate stays constant at every pitch. A long press enters TUNE: the TUNE and OCTAVE LEDs alternate and the knob transposes plus or minus 12 semitones; a second press alternates TUNE and DETUNE and the knob fine-tunes plus or minus 120 cents; a third long press returns to normal. Holding the PITCH button for six seconds enters a coarse pitch mode with a very wide frequency range, and holding it for two seconds leaves it.

**FM INDEX and INDEX MOD.** The FM INDEX fader sets how much frequency modulation reaches the carrier and from which modulator. At the center there is no modulation. Left of center the RATIO oscillator modulates; right of center the OCT oscillator does. The INDEX MOD knob is an attenuverter for the FM INDEX CV input, which accepts -6 V to +6 V: right of center applies the voltage as it comes, and left of center inverts it. ⚠️ The manual does not say whether the incoming voltage is added to the fader position or replaces it.

**OCT OSC, RATIO OSC, and EXT.** The OCT OSC button chooses one of four octaves for the octave oscillator. The RATIO OSC button chooses one of four ratios that the player sets. A long press on RATIO OSC enters RATIO SETTING mode: click the button to pick which of the four ratios to edit, set the numerator and denominator each from 1 to 16 (the PITCH button toggles between them, with the OCTAVE LED lit for the numerator and the DETUNE LED lit for the denominator), and long press to leave. The TUNE LED blinks on each change so the value can be counted. The manual's example is 3/2, a perfect fifth, with numerator 3 and denominator 2. Its interval table lists 1/1 unison, 16/15 minor second, 9/8 major second, 6/5 minor third, 5/4 major third, 4/3 fourth, 3/2 fifth, 8/5 minor sixth, 5/3 major sixth, 16/9 minor seventh, 15/8 major seventh, 2/1 octave, 9/4 major ninth, 12/5 minor tenth, and 5/2 major tenth. A cable in EXT replaces the octave oscillator as the modulator with whatever signal is patched, from -6 V to +6 V.

**SHAPE fader and SHAPE button.** The SHAPE button picks one of three modes, WAVE, FOLD, or RING, and the fader (with the SHAPE CV input at -6 V to +6 V) is neutral at the center with an effect on each side. In WAVE mode the fader shapes the OCT and RATIO oscillators as square, sine, or saw; this is heard on MAIN only when FM INDEX or RING is engaged, and it also changes the OCT OSC output. In FOLD mode the left side applies the Buchla 259-inspired fold, harsher with mainly odd harmonics, and the right side applies the Chebyshev-based digital fold, which produces all harmonic intervals. The manual's figures show fold ratios from 1:1 to 9:1, and the range can be extended by CV or by assigning CTRL to FOLD. Folding weakens the fundamental, so the bass thins out; the manual's stated remedy is to mix the oscillator outputs. In RING mode the fader works like FM INDEX: the RATIO oscillator is ring-modulated with MAIN on the left, the OCT oscillator on the right, and nothing at the center. The manual's tip is to use FM INDEX with RATIO and RING with OCT, or the reverse, so that both modulators act at once.

**CTRL.** CTRL is one knob that can be assigned to a destination from the list below. With nothing patched to the CTRL CV input the knob is a static control; with a voltage patched (-6 V to +6 V) the knob becomes an attenuverter for it. To assign, hold the SHAPE button for a few seconds; the LEDs show the current destination, and pressing the button nearest the destination you want selects it. A long press on SHAPE leaves assignment. The assignment is stored with the user settings. ⚠️ How the knob and the voltage combine is not stated in the manual.

**SYNC, V/OCT, and the outputs.** SYNC (-6 V to +6 V) resets the phases of all three oscillators, which makes a hard sync and also cleans up FM transients; in the envelope VCA mode it also triggers the built-in envelope. V/OCT accepts -5 V to +8 V. MAIN is the carrier after FM, FOLD, and RING and passes through the built-in VCA when CTRL is assigned to it. OCT OSC is the octave oscillator after WAVE shaping, suggested by the manual as a sub-oscillator or as a way to reinforce the fundamental. PULSE is a pulse version of the carrier taken before the FM, with a width set by FM INDEX and its modulation. The manual describes PULSE as using a lower-quality converter that may produce audible noise in some settings. ⚠️ Which settings produce the noise is unknown until the module is tested.

---

## CTRL Destinations

The manual lists fifteen destinations. The LEDs shown at assignment are given in parentheses.

| Destination | LEDs | What it does |
|---|---|---|
| Octave | OCTAVE | Octave of the whole voice |
| Detune | DETUNE | Detune of the two modulators |
| Linear FM | TUNE | Linear FM amount |
| Exponential FM | OCTAVE and DETUNE | Exponential FM amount |
| OCT OSC ratio | top OCT LED | Octave of the octave oscillator |
| OCT OSC exponential FM | both OCT LEDs | Exponential FM from the octave oscillator |
| RATIO OSC ratio | top RATIO LED | Ratio of the ratio oscillator |
| RATIO OSC exponential FM | both RATIO LEDs | Exponential FM from the ratio oscillator |
| FM INDEX modulation | top RATIO and OCT LEDs (press both buttons together) | A second path to the FM index |
| Second FM INDEX modulation | bottom RATIO and OCT LEDs (press both buttons together) | An independent second FM index control |
| Waveshape | WAVE | WAVE shaping amount |
| Folding | FOLD | FOLD amount |
| Ring modulation | RING | RING amount |
| Bipolar VCA | RING and FOLD | A built-in bipolar VCA on MAIN and OCT OSC |
| Envelope VCA mode | WAVE, RING, and FOLD | Built-in AD envelope triggered by SYNC |

Assigning CTRL to a different shape mode than the one the SHAPE button shows runs two shapers at once. In the envelope VCA mode, the CTRL knob (or its CV) is a macro for the envelope: to the right of 12 o'clock it adds only decay, and to the left it adds both attack and decay. The envelope drives the built-in VCA and is normalled to the FM INDEX input: with nothing patched into the FM INDEX CV jack, opening INDEX MOD modulates the FM index with the envelope. The VCA modes do not apply to the PULSE output, except when PULSE carries the RATIO oscillator.

---

## Calibration and Boot Settings

**V/OCT calibration.** If the module boots with two flashes near the OCT OSC button and the lights on the left pointing down, the V/OCT input needs recalibration; the manual says this can happen when the rails in a new case are balanced differently from the last one. The quick fix is to patch the OCT OSC output into V/OCT, wait a few seconds, and unplug it. To enter calibration mode, hold the SHAPE and PITCH buttons; all LEDs light, and the SHAPE button toggles between quantized and unquantized V/OCT. For automatic calibration, press PITCH, patch OCT OSC into V/OCT, and unplug it when all LEDs are on. For external calibration, press OCT OSC, patch the V/OCT source, apply 0 V when "0" blinks and press OCT OSC, then apply 2 V when "2" blinks and press OCT OSC. Leave calibration by pressing SHAPE and PITCH together.

**Boot settings.** Buttons held while powering up change the module's state. Hold SHAPE to reset the user settings (the RATIO oscillator ratios and the CTRL destination). Hold SHAPE and OCTAVE for a factory reset of user settings and calibration. Hold SHAPE and RATIO for the factory test mode. Hold RATIO and OCT OSC to toggle the PULSE output between the carrier pulse and the RATIO oscillator; the module remembers the choice. ⚠️ The manual gives two different ways to enter firmware update mode, which are in the Firmware paragraph of the Common Mistakes section.

---

## Why This Instrument Excels

The Pizza treats frequency modulation as a relationship between three oscillators and not a depth knob. The carrier is modulated by an octave oscillator with a fixed relationship and by a second oscillator whose ratio the player writes as a fraction from 1 to 16 over 1 to 16, so the harmonic or inharmonic character of the sound is chosen deliberately. One fader moves between the two modulators and sets how much of either reaches the carrier, and an external signal can replace the octave oscillator, so the instrument spans a fixed sub-octave relationship, a tuned interval, and an outside modulator without re-patching the core.

The shaping section is a single fader with a different meaning for each button mode, and the neutral center means that the player always knows where the plain sound is. The two fold algorithms give two different spectra, odd-harmonic on the left from the Buchla lineage and all-harmonic on the right from the digital design, and ring modulation shares the same fader so that FM and ring modulation can use different modulators at the same time. Because CTRL can address a second shaper, the same module can run two shapers at once, which most dedicated folders cannot.

The assignable CTRL turns a fixed panel into an instrument whose center can move. One knob and one CV input reach fifteen destinations, from the octave to the amount of ring modulation to the FM index through a second path. When CTRL is set to the envelope VCA mode, the Pizza gains a built-in attack and decay envelope and an amplifier triggered at SYNC, with the envelope also reaching the FM index, so the module alone becomes a plucked voice with a brightness that decays with the loudness, a result that normally takes an envelope generator, a VCA, and several cables.

The housekeeping is part of the design. The module calibrates its V/OCT input automatically from its own octave oscillator, accepts an external calibration, remembers the ratios and the CTRL assignment, and fits in 8 HP, so it can sit in a small case as the only oscillator. The cost is that the manual is terse about specifications: depth and current are not given, and the behavior of CV against the faders is not described. Those gaps stay marked until the module has been measured.

---
## Patch Examples

The Pizza is a SOURCE, so the First Voice uses the standard oscillator chain: a sequencer for pitch and gate, an envelope generator, and a VCA. Patch 2 is the exception, because CTRL assigned to the envelope VCA mode gives the module its own envelope and amplifier. Maths supplies the envelope in Patches 1 and 4 and appears again in the Pairs Well With section.

All four patches are drafts written from the manual and are untested on hardware ⚠️. Knob positions describe intent, and every "What to listen for" result is a prediction until the module has been patched. The manual does not say whether CV at FM INDEX CV, SHAPE CV, or CTRL CV adds to the position of the fader or knob or replaces it, so the patches begin with the control near its neutral position and tell you what to check if the result goes the wrong way. ⚠️

---

### Patch 1: FM Brightness Follows an Envelope ⚠️

This patch demonstrates that the FM index is a brightness control and the ratio is a choice of timbre family: one envelope moves the index while the ratio stays fixed on a fifth.

**First Voice**

Before introducing anything specific to the Pizza, establish a working voice:

```
  Squarp Hermod+ CV out ──[C]──▶ Pizza V/OCT
  Squarp Hermod+ gate out ──[G]──▶ Maths Ch1 TRIG
  Maths Ch1 Unity ──[C]──▶ VCA CV in
  Pizza MAIN ──[A]──▶ VCA audio in ──▶ Mixer
```

Use a sequencer such as Squarp Hermod+ (or Mutable Instruments Marbles, with X1 for pitch and t2 for gate), an envelope generator such as Make Noise Maths (or Blue Lantern BLM Looping Simple ADSR), and a VCA such as Vostok Instruments Ceres (or Erica Synths Pico VCA2). Set the sequencer to repeat a single note and the Pizza FM INDEX fader to the center. Confirm that a plain sine sounds on each gate and follows the note.

**Add the index envelope**

```
                          ┌──────────────────────────────────┐
Sequencer ──[C]──▶        │ V/OCT                       MAIN │──[A]──▶ VCA ──▶ Mixer
Maths Ch1 Variable ──[C]─▶│ FM INDEX CV                      │
                          │ FM INDEX  INDEX MOD  RATIO OSC   │
                          └──────────────────────────────────┘
                                  Bastl Instruments Pizza
```

- `Maths Ch1 Variable ──[C]──▶ FM INDEX CV`: the same envelope that opens the VCA also drives the FM index through the Variable output, so brightness rises and falls with loudness and the note sounds struck.
- `Sequencer CV ──[C]──▶ V/OCT`: a steady pitch keeps attention on the change of timbre.

Move the FM INDEX fader slightly to the left of center so the RATIO oscillator is the modulator. Press RATIO OSC to select a ratio, then hold the button to enter RATIO SETTING, set the numerator to 3 and the denominator to 2 (a fifth), and long press to leave. Turn INDEX MOD to the right of center to let the envelope in, and scale the Maths Ch1 attenuverter to taste. This patch uses six cables.

**What to listen for**

Each note should start bright and settle toward a plainer tone as the envelope falls, with the fifth giving a bell-like, harmonic character. Moving the fader further from the center or raising INDEX MOD should make the bright part longer and more extreme. If the envelope makes the note darker at the start instead of brighter, the voltage is working against the fader position; turn INDEX MOD to the other side of center. ⚠️ Whether CV adds to the fader position or replaces it is unverified, and the fader may need to rest at the center for the envelope alone to set the index.

---

### Patch 2: A Complete Voice with CTRL ⚠️

This patch demonstrates that CTRL assigned to the envelope VCA mode gives the Pizza its own envelope and amplifier, so a gate and a pitch are enough to make a note.

**First Voice**

Use the same pitch source as Patch 1, but remove the external envelope and VCA. The Pizza is both oscillator and amplifier in this patch.

**Add the built-in envelope**

```
                          ┌──────────────────────────────────┐
Sequencer CV ──[C]──▶     │ V/OCT                       MAIN │──[A]──▶ Mixer
Sequencer gate ──[G]──▶   │ SYNC                             │
                          │ CTRL (envelope VCA)  INDEX MOD   │
                          └──────────────────────────────────┘
                                  Bastl Instruments Pizza
```

- `Sequencer CV ──[C]──▶ V/OCT`: the note pitch still comes from outside.
- `Sequencer gate ──[G]──▶ SYNC`: the gate triggers the built-in envelope, and because SYNC also resets the oscillator phases, every note starts from the same point in the cycle. Taking the gate from the same sequencer as the pitch keeps each note's timing and pitch together.
- `MAIN ──[A]──▶ Mixer`: the amplifier is inside the module, so MAIN goes straight to the mix.

Use a sequencer such as Squarp Hermod+ (or ALM Busy Circuits Pamela's PRO Workout for the gate, with OUT 1 set to a square wave). Hold the SHAPE button to enter assignment and select the envelope VCA mode (the WAVE, RING, and FOLD LEDs together), then long press SHAPE to leave. Leave the FM INDEX CV jack empty and the fader slightly to the left of center, then turn INDEX MOD to the right of center. Turn the CTRL knob to the left of 12 o'clock for both attack and decay, and to the right for decay only. This patch uses three cables.

**What to listen for**

Each gate should produce a note that rises and falls by itself, shorter as the CTRL knob moves right, and the brightness should fall with the loudness because the envelope is normalled to the FM index. With INDEX MOD at the center the note should still sound but without the brightness change. If there is no sound, check that the gate reaches SYNC and that CTRL is in the envelope VCA mode. If the pitch sounds slightly different on each note, the SYNC reset is restarting the cycle; this is the expected behavior and it should make every attack identical. ⚠️ SYNC trigger threshold and the interaction of the phase reset with the envelope are unverified.

---

### Patch 3: A Beating Drone with Two Modulators ⚠️

This patch demonstrates that FM and ring modulation can use different modulators at once, and that a linear detune keeps the beating rate constant at any pitch.

**First Voice**

Use the same pitch source as Patch 1 and hold a single note. A drone needs no envelope, so MAIN goes to the mixer directly.

**Add the second modulator and the slow motion**

```
                          ┌──────────────────────────────────┐
Sequencer ──[C]──▶        │ V/OCT                       MAIN │──[A]──▶ Mixer CH1
2hp LFO v2 ──[C, slow]──▶ │ SHAPE CV                 OCT OSC │──[A]──▶ Mixer CH2
                          │ FM INDEX (right)                 │
                          │ SHAPE, RING (left)               │
                          └──────────────────────────────────┘
                                  Bastl Instruments Pizza
```

- `Sequencer CV ──[C]──▶ V/OCT`: one held note makes the beating the only movement.
- `2hp LFO v2 ──[C, slow]──▶ SHAPE CV`: a slow unipolar sweep moves the ring modulation amount, so the sound brightens and clears over many seconds.
- `MAIN ──[A]──▶ Mixer CH1`: the full folded and ring-modulated sound.
- `OCT OSC ──[A]──▶ Mixer CH2`: the octave oscillator reinforces the fundamental, which the manual notes is weakened by folding and ring modulation.

Use a slow modulation source such as 2hp LFO v2 (or Make Noise Wogglebug, smooth output) and a two-channel mixer such as Intellijel MixUp. Press the SHAPE button to RING and move the fader left of center, so the RATIO oscillator is the ring-modulation partner. Move FM INDEX to the right of center so the OCT oscillator is the FM modulator. Press the PITCH button until the DETUNE LED is lit and turn the knob left of center for the linear detune, which gives a constant beating rate in hertz. Set the LFO to its slow range. This patch uses five cables.

**Move the cable**

Unplug the LFO from SHAPE CV and plug it into FM INDEX CV. Leave every knob where it is.

```
                          ┌──────────────────────────────────┐
Sequencer ──[C]──▶        │ V/OCT                       MAIN │──[A]──▶ Mixer CH1
2hp LFO v2 ──[C, slow]──▶ │ FM INDEX CV              OCT OSC │──[A]──▶ Mixer CH2
                          │ FM INDEX (right)                 │
                          │ SHAPE, RING (left)               │
                          └──────────────────────────────────┘
                                  Bastl Instruments Pizza
```

What changed: the slow motion now moves the octave oscillator's FM amount, while the ring modulation by the RATIO oscillator stays fixed, so the sweep changes the brightness through one modulator and leaves the other as a constant color.

**What to listen for**

The sound should shimmer at a steady rate that does not change when the pitch changes, and the slow LFO should bring the ring modulation in and out over many seconds. Turning the detune knob to the right of center should make the beating speed change with pitch instead. If the sound is thin, raise the OCT OSC channel in the mix. If the sound is harsh, lower FM INDEX before touching the shape. ⚠️ The effect of a unipolar LFO against the rest position of the SHAPE fader is unverified.

---

### Patch 4: CTRL as an Arpeggiator ⚠️

This patch demonstrates that CTRL assigned to the octave turns a random voltage into jumps across the octaves, so one pitch line becomes an arpeggio.

**First Voice**

Use the same voice as Patch 1, with the Pizza MAIN output into the VCA and Maths Ch1 as the envelope. Replace the Hermod+ with Mutable Instruments Marbles for the pitch and the gate.

**Add the quantizer and the octave control**

```
                          ┌──────────────────────────────────┐
Pico QUANT CV OUT ──[C]─▶ │ V/OCT                       MAIN │──[A]──▶ VCA ──▶ Mixer
Marbles X2 ──[C]──▶       │ CTRL CV (OCTAVE)                 │
                          └──────────────────────────────────┘
                                  Bastl Instruments Pizza

  Marbles X1 ──[C]──▶ Pico QUANT CV IN
  Marbles t2 ──[G]──▶ Maths Ch1 TRIG
  Maths Ch1 Unity ──[C]──▶ VCA CV in
```

- `Marbles X1 ──[C]──▶ Pico QUANT CV IN`: the random line is quantized, so the arpeggio plays notes of a scale.
- `Pico QUANT CV OUT ──[C]──▶ V/OCT`: the quantized voltage sets the pitch of the Pizza.
- `Marbles X2 ──[C]──▶ CTRL CV`: a second output of the same random source moves the octave, so the register changes from note to note.
- `Marbles t2 ──[G]──▶ Maths Ch1 TRIG`: each gate triggers the envelope and lines up with the pitch changes.
- `Maths Ch1 Unity ──[C]──▶ VCA CV in` and `Pizza MAIN ──[A]──▶ VCA audio in`: the voice is shaped as in Patch 1.

Use a probability source such as Mutable Instruments Marbles (or Squarp Hermod+ with two CV lanes) and a quantizer such as Erica Synths Pico QUANT (see the Pico QUANT guide in this corpus). Assign CTRL to the octave (hold SHAPE, select OCTAVE, long press SHAPE). Set the CTRL knob to its center, then turn it to let X2 in, and set Marbles DEJA VU around 11 o'clock so the pattern repeats. This patch uses seven cables, below the ten-cable ceiling.

**What to listen for**

The notes should stay inside the chosen scale while the register jumps across octaves, and a locked DEJA VU should make the arpeggio repeat. Turning the CTRL knob should change how far the jumps go. If every note is in the same octave, check that X2 reaches CTRL CV and that CTRL is assigned to OCTAVE. ⚠️ The voltage span of Marbles X1 against the 0 V floor of Pico QUANT CV IN, and of X2 against the octave range of CTRL, are unverified; set the Marbles voltage range so that X1 stays positive.

---

## Common Mistakes

### "I moved the FM INDEX fader to the center and the FM disappeared"

The center of the FM INDEX fader is the no-modulation position, by design. Left of center the RATIO oscillator modulates and right of center the OCT oscillator does, so the sound is a plain sine only at the center. Move the fader away from the center to bring in either modulator, and use INDEX MOD for the amount that arrives by CV. The same rule applies to the SHAPE fader: the center is neutral in WAVE, FOLD, and RING.

### "My pitch is off, or the module boots with two flashing lights and no tuning"

The V/OCT input needs recalibration when the rails in the new case differ from the last one, and the module shows it with two flashes near the OCT OSC button and the lights on the left pointing down. Patch the OCT OSC output into V/OCT, wait a few seconds, and unplug it; the module boots to normal operation. For a permanent result, use the automatic or the external calibration in Calibration and Boot Settings.

### "I turned up FOLD and the bass went away"

Folding weakens the fundamental, so the sound gets bright and thin as the folds multiply. The manual's remedy is to mix oscillator outputs: bring up the OCT OSC output beside MAIN to reinforce the fundamental. Fold less if the module is the only source in the voice.

### "The PULSE output hisses"

The manual says the PULSE output uses a lower-quality converter that may produce audible noise in some settings, and the noise is worse when the output is carrying the RATIO oscillator. Use MAIN for audio and keep PULSE for pulse-wave or modulation duties. ⚠️ Which settings make the noise audible is unverified.

### "I held a button at power-up and my ratios and CTRL assignment are gone"

Holding SHAPE at power-up resets the user settings, including the four RATIO oscillator ratios and the CTRL destination, and holding SHAPE and OCTAVE resets the calibration as well. Do not hold those buttons while powering the rack. If the settings were lost, set the ratios again in RATIO SETTING mode and reassign CTRL; after a factory reset, calibrate V/OCT again.

### "My envelope never plays in the envelope VCA mode"

The built-in envelope is triggered by the SYNC input, so a gate or trigger at SYNC is required. The envelope is also normalled to the FM index only when nothing is patched into the FM INDEX CV jack, and the INDEX MOD knob has to be open for the envelope to move the index. Check the cable at SYNC, confirm that CTRL is in the envelope VCA mode, and open INDEX MOD.

**Firmware.** The manual gives two ways to enter the firmware update. Page 19 says to hold the PITCH button while plugging the USB cable into the computer, and page 20 says to hold TUNE at power-up. Disconnect the module from the rack before updating, and try the PITCH method first; if the module does not appear as a disk, try the other. ⚠️ Neither method is verified.

---

## Advanced Learning Path

1. Set the four ratios to a harmonic family (1/1, 2/1, 3/2, 5/4) and then to an inharmonic family (9/4, 12/5, 16/15, 15/8), and play the same melody through each to hear the difference between bell and gong characters.
2. Compare the linear detune to the exponential detune on a melody that spans three octaves, listening for the constant beating on one side and the pitch-scaled beating on the other.
3. Assign CTRL to the exponential FM of the octave oscillator, as the manual suggests, and use the knob as a free frequency control to move the modulator without changing the carrier.
4. Run two shapers at once by assigning CTRL to a shape mode different from the one the SHAPE button shows, and keep one on FOLD and the other on RING.
5. Patch an outside oscillator into EXT so that the octave oscillator is replaced by a modulator you control, and play the two in different ratios from separate sequencer lanes.
6. Assign CTRL to the bipolar VCA and feed it an audio-rate oscillator for an external ring modulator, as the manual suggests.
7. Send MAIN and the OCT OSC output to a scope in XY mode with a static voltage at EXT, and watch the phase relationships change as the ratios and FM index move.
8. Calibrate V/OCT externally against a precise source, then compare the tracking across five octaves with a tuner, and write down the error in cents.

---

## Pairs Well With

**Make Noise Maths:** The Pizza's envelope-controlled brightness is the first thing most players want, and Make Noise Maths supplies the envelope and a second, scaled copy of it from one channel. The Unity output opens the VCA and the Variable output sets the FM index, so loudness and brightness share one gesture. In cycle mode the same channel becomes an LFO for the index. ⚠️

**Mutable Instruments Marbles:** Mutable Instruments Marbles provides a random pitch from X1, a second random voltage from X2 for the CTRL input, and gates from t2, so a single module plays the Pizza as an arpeggiator and moves its octave at once. A locked DEJA VU makes the pattern repeat while the CTRL knob changes how far the register moves. ⚠️

**Erica Synths Pico QUANT:** Erica Synths Pico QUANT keeps the random line in a scale, which matters on an FM voice where a note slightly off a harmonic ratio sounds sour. Its tolerance control lets the pitch hold longer before it steps, and the clock out can trigger the envelope each time the note changes. ⚠️

**Erica Synths Black Polyvoks VCF:** FM and folding both create upper harmonics, and a filter after the Pizza removes the ones that are too harsh. The manual's first tip is to mix all three outputs into a filter, and Erica Synths Black Polyvoks VCF takes the mix and shapes it with a cutoff that follows an envelope. ⚠️

**2hp LFO v2:** A slow, unipolar sweep from 2hp LFO v2 is enough to animate the SHAPE fader or the FM index over many seconds, and its wave morph changes the shape of the motion. The RESET input can align the sweep to a clock so the timbre change lines up with the bar. ⚠️

**Endorphin.es New Godspeed:** The EXT input accepts a signal in place of the octave oscillator, and Endorphin.es New Godspeed provides a stable sine to modulate the Pizza's carrier from outside. Its pitch can follow the same sequencer at a different interval, so the ratio between carrier and modulator moves with the music instead of staying at a set fraction. ⚠️
