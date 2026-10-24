---
title: Befaco Oneiroi
manufacturer: Befaco
primary_role: SOURCE
secondary_roles: [SHAPER]
historical_context: true
form_factor: eurorack
functions: [oscillator, looper, fx-time]
behavior_tags: [sustained, evolving, harmonic, generative, performance-oriented]
use_cases: [evolving ambient texture, drone foundation, harmonic pad, dark atmospheric layer]
hp: 30
memory: basic
transport: receive
screen: false
hybrid: true
cv: full
patch_format: v1
---

# Befaco Oneiroi

**Stereo drone and pad voice: sine, supersaw, and looper-fed wavetable oscillators, a five-second looper, four effects in series, self-modulation, and a randomizer in 30 HP**

![Befaco Oneiroi](https://github.com/Shadoe-42/music/raw/main/modular/images/befaco/oneiroi/front_panel.jpg)
*Befaco Oneiroi: stereo input and output, looper, oscillator, source faders, filter, resonator, echo, ambience, modulation, and randomizer sections*

> **Draft status (2026-10-24):** Written from the official Befaco Oneiroi user manual (last updated March 3, 2025) and cross-checked against the front panel image, before the module was in hand. Every specification, control, range, and button combination comes from that manual. All four patches are untested on hardware and are marked ⚠️. Open items to clear on hardware: (1) every patch setting and every "What to listen for" result; (2) the behavior of the catch and jump knob modes and the LED colors, which come from the manual alone; (3) the voltage span of Marbles X1 relative to the V/OCT input range (Patch 4); (4) how quickly SYNC IN locks to an external clock; (5) how the mapping pages are exited and the exact LED behavior of the save (Patch 3). Remove this block when the items are cleared.

---

## Historical Context

The core of Oneiroi's looper is an idea from tape. Frippertronics is an analogue delay system of two side-by-side reel-to-reel tape recorders: the tape runs from the supply reel of the first machine to the take-up reel of the second, so sound recorded at the first plays back at the second, and the output of the second is routed back to the first. The delayed signal repeats while new audio is mixed on top, building layer upon layer in real time. The delay length, usually three to five seconds, is set by the distance between the machines, and the number of repeats by the volume at the second machine. The method grew out of studio systems of the 1960s developed by composers including Terry Riley and Pauline Oliveros, and Brian Eno introduced it to Robert Fripp in his home studio; it reached records with the Fripp and Eno album (No Pussyfooting) in 1973 and became a foundation of ambient music through Eno's Discreet Music in 1975. Oneiroi's five-second buffer sits inside that three-to-five-second range, its sound-on-sound level plays the role of the second machine's volume, and its varispeed replaces tape speed.

The oscillator and effects sections draw on two other lineages. The stereo supersaw is described in the manual as inspired by the Roland JP-8000, whose supersaw stacks several detuned sawtooth waves into a single oscillator and became so closely tied to trance that many call it simply the trance sound; the 2HP Swarm guide in this corpus covers the stacking principle in more detail. The wavetable oscillator reads the looper buffer, so the recorded audio itself becomes the source of the waveforms. The Ambience reverb is described as loosely based on a Schroeder reverberator, the design approach initiated in the early 1960s by Manfred Schroeder that combines a parallel bank of feedback comb filters with a series chain of allpass filters; the comb filter returns in Oneiroi as both a filter mode and the basis of the three-band resonator.

Oneiroi runs on Rebel Technology's OWL platform, specifically the mk3 revision, with 24-bit 48 kHz stereo audio and 32-bit internal processing. Rebel Technology introduced the OWL Modular in 2015 as a Eurorack incarnation of its open-source OWL effects pedal: a programmable DSP module whose code could be written in C++, FAUST, or Pure Data, with a library of more than seventy effects and patches loaded over USB. The Oneiroi manual credits the module to three parties: Roberto Noris as programmer and concept designer, Rebel Technology for the platform, and the Befaco team in Barcelona for making it real. Befaco announced Oneiroi on May 14, 2024, ahead of Superbooth 2024, and reported it available on July 19, 2024; a VCV Rack version followed in December 2024. The name comes from Greek mythology, where the Oneiroi are dark-winged creatures that emerge from their cave each night to deliver dreams and nightmares, and the manual presents the module as a more practical way to receive their messages while awake.

---

## Quick Start: First Drone in 5 Minutes

Oneiroi is a stereo synth voice built for pads and drones: three oscillators (two of them mutually exclusive), a five-second looper, four effects in series, self-modulation, and a randomizer. Sources go in through four faders, and effects are blended in through four more. This quick start produces a layered drone with space around it, without touching the looper. ⚠️ Untested on hardware.

1. **Patch OUT L and OUT R to a stereo mixer.** The left output normals to the right, so a single cable gives a mono signal; use both for stereo.
2. **Patch a pitch CV into V/OCT.** A sequencer or keyboard works. The input tracks across 0 V to 10 V.
3. **Raise the SINE fader.** A pure sine tone appears at the pitch of the PITCH knob and V/OCT together.
4. **Raise the SS/WT fader with the oscillator mode switch up.** Up is supersaw; down is wavetable.
5. **Turn DETUNE.** The seven saws of the supersaw spread apart as the knob rises.
6. **Raise the AMBIENCE fader at the right.** This is the dry/wet balance of the reverb. Adjust DECAY to lengthen the tail.
7. **Leave the LOOPER fader down for now.** The loop buffer is prefilled with white noise, so raising that fader before recording produces noise.
8. **Press RANDOM once, then hold SHIFT and press RANDOM to undo.** This shows how the randomizer changes the sound and how to step back.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 30 HP |
| Depth | 25 mm |
| Power | 200 mA +12V / 80 mA -12V / 0 mA +5V |
| Audio | 24-bit, 48 kHz stereo; 32-bit internal processing |
| Platform | Rebel Technology OWL mk3 |
| Inputs | Stereo IN (left normals to right), V/OCT, SYNC IN, RECORD IN, RANDOM IN, four volume CVs, four dry/wet CVs, CV inputs for looper speed, start, and length, oscillator detune, filter cutoff, resonator tune, echo density, and ambience spacetime |
| Outputs | Stereo OUT (left normals to right) |
| Input gain | Three positions: high gain, line, and Eurorack level |
| Looper | About 5 seconds; records the stereo input or the module output |
| CV ranges | Volume and dry/wet CVs: 0 V to 10 V; parameter CVs: -5 V to 10 V; V/OCT: 0 V to 10 V |
| Triggers | SYNC IN, RECORD IN, RANDOM IN respond above 1 V |
| Power connection | 10-pin to 16-pin cable |

The manual and the Befaco product page agree on width, depth, and current draw, so no flags are carried. The manual's power section gives +5V as 0 mA.

---

## How Oneiroi Is Organized

**Sources and effects.** The audio engine has two halves. The sources are the sine oscillator, the supersaw and wavetable oscillator (a single slot, with a switch choosing which one is active), the looper, the external stereo input, and, only when recording in POST mode, a resample of the module's own output. The effects are the Filter, the Resonator, the Echo, and the Ambience reverb, connected in series. The sine oscillator and the supersaw or wavetable oscillator share one pitch control but have separate volume faders. The external input and the resample are mutually exclusive as recording sources, but the external input also has its own fader that sends it directly into the effects chain.

**Faders do the mixing.** The four faders on the left of the lower panel set source levels: LOOPER, SINE, SS/WT, and INPUT. The four faders on the right set the dry/wet balance of each effect: FILTER, RESONATOR, ECHO, and AMBIENCE. At the lowest position of an effect fader, the signal passes to the next unit unaffected. When a CV is patched into the equivalent jack at the top of the panel, the fader stops acting as a level control and becomes an attenuator for the incoming CV. The Filter is the only effect that can move along the chain; its position is set with SHIFT and the RESO knob, with four options: the beginning of the chain, between the resonator and the echo, between the echo and the ambience, or the end of the chain.

**The Shift layer.** Most knobs and both buttons carry a second function, labeled on the panel in white-background text. Hold SHIFT while turning a knob for a momentary change, or press SHIFT once to toggle the layer on and off. Parameters with only one label ignore SHIFT. Changes made on the Shift layer, like every other change, are lost at power-off unless saved.

| Panel control | Primary function | Shift function |
|---|---|---|
| START | Looper start position | SOS: sound-on-sound level |
| LENGTH | Looper loop length | FILTER: DJ-style filter on the sound-on-sound recording |
| PITCH | Oscillator pitch | OCTAVE: octave selection |
| DETUNE / OFFSET | Supersaw detune, or wavetable offset | UNISON: interval between the oscillators |
| CUTOFF | Filter cutoff or comb position | MODE: filter type |
| RESO | Filter resonance | POS: position of the filter in the chain |
| TUNE | Resonator base frequency | DISSONANCE: how dissonant the three tunings are |
| DENSITY | Echo time | FILTER: DJ-style filter on the echo |
| SPACETIME | Reverb size, filtering, and direction | AUTOPAN: auto-pan amount and ratio |
| SPEED | Modulation speed | TYPE: modulation type |
| MOD AMT | Modulation mapping mode | CV AMT: CV mapping mode |
| RECORD | Looper record | CLEAR: erase the buffer |
| RANDOM | Randomize | UNDO/REDO: step back or forward through randomization |

**The two mapping modes.** The MOD AMT button opens the modulation mapping page; the button blinks red. In that mode, turning any knob (except the modulation knobs themselves) sets how much of the internal modulation that parameter receives. Holding SHIFT and pressing MOD AMT opens the CV mapping page instead; the button blinks green. In that mode, turning a knob sets how much of its external CV the parameter receives, from 0 to 100 percent, with 100 percent as the default for all primary parameters. The four effect CVs, which start assigned to the main effect parameters, can also be reassigned to secondary parameters. Pressing RECORD and RANDOM together clears the mapping of whichever page is open.

**Saving.** There are no presets or slots. Oneiroi keeps one stored state, and it is written only on request: hold the MOD AMT button for two seconds, and the button LED blinks to confirm. The save stores parameter state so that all parameters survive a power cycle, including parameters where the knob position does not match the stored value. The looper buffer is never saved. Anything not saved is lost when the module powers off.

**Sync.** SYNC IN accepts triggers of at least 1 V and does three jobs at once: it restarts the looper at the START point, it clocks the internal modulation, and it synchronizes the echo time and the ambience auto-pan. With nothing patched, the module runs on an internal clock of about 0.2 Hz derived from the looper buffer, and the SYNC LED shows activity. The module needs a couple of seconds to align to an external clock and takes a similar time to return to the internal clock when the cable is removed. Supported external clock speeds run from 30 BPM to 300 BPM. Because one clock serves all three jobs, the manual advises a clock of one trigger per bar or slower, such as one trigger every four bars.

---

## Essential Parameters

**Input and gain.** The stereo IN has its left jack normalled to the right, so a mono source in the left jack feeds both channels through the stereo path. The IN GAIN switch has three positions: the top position gives the most gain and suits high-impedance sources such as contact microphones, the middle position suits line-level sources, and the bottom position suits the outputs of other Eurorack modules. A two-color LED shows peak level, green for the signal and red for clipping; it monitors the input when the PRE/POST switch is on PRE and the module output when it is on POST. The INPUT fader sets the level of the external signal sent directly to the effects chain; its CV input takes 0 V to 10 V.

**Looper: VARISPEED, START, and LENGTH.** The looper records and plays back about five seconds of audio. VARISPEED controls both playback direction and speed: reverse at twice speed at 0 percent, forward at twice speed at 100 percent, and stalled only at the 12 o'clock position, with virtual detents at -1x, 0, and 1x. START picks the starting point of the loop. LENGTH sets the loop size on an exponential curve, from about 8 ms at 0 percent to the full buffer at 100 percent. At the minimum length, the looper acts as an oscillator, giving C3 at plus or minus 1x speed, C2 at plus or minus 0.5x, and C4 at plus or minus 2x; the manual notes that this does not track V/OCT. START, LENGTH, and VARISPEED each have a CV input with a range of -5 V to 10 V. A pulse at SYNC IN restarts the loop at the START point.

**Looper: RECORD, PRE/POST, and sound-on-sound.** The RECORD button works in two ways: a single press toggles recording on and off, and holding it records until release. RECORD IN is a gate input that records while high, above 1 V, and stops at 0 V. The PRE/POST switch chooses what is recorded: PRE records the external stereo input, and POST records the module's own output, which allows resampling. The buffer is prefilled with white noise, so the looper makes sound before anything is recorded. SHIFT plus RECORD clears the buffer. The SOS level, set with SHIFT plus START, controls how much old material survives each pass: at 0 percent it is constantly replaced, at 100 percent it never fades, and values between fade it progressively more slowly. During recording the old material passes through a DJ-style filter set with SHIFT plus LENGTH: noon applies no filter, clockwise applies a high-pass filter, and counterclockwise applies a low-pass filter.

**Oscillators: PITCH, V/OCT, and OCTAVE.** The module provides a stereo sine oscillator, a stereo supersaw oscillator, and a wavetable oscillator. The supersaw and the wavetable share a slot, chosen with the oscillator mode switch (up for supersaw, down for wavetable). The sine can be used alone with either. The full pitch range is eight octaves, from C0 to C7. PITCH is centered on C and spans six semitones on either side; SHIFT plus PITCH picks the octave. The V/OCT input is common to all three oscillators, sums with the PITCH knob, and tracks ten octaves across 0 V to 10 V, clipping outside the supported range. The sine and the SS/WT slot each have their own source fader.

**Oscillators: DETUNE, OFFSET, and UNISON.** DETUNE has two roles depending on the mode switch. In supersaw mode it sets the detuning of the seven saws; in wavetable mode, as OFFSET, it selects one of 32 wavetables that the module extracts dynamically from the looper buffer. The wavetable is a 2048-sample table and the manual describes it as aliased. Holding SHIFT while turning the knob sets the interval between the oscillators: at 50 percent (the default) they are in unison; at 0 percent the interval moves down an octave, and at 100 percent it moves up an octave. DETUNE and OFFSET have a CV input of -5 V to 10 V.

**Filter.** The filter is a two-pole multimode design with low-pass, band-pass, and high-pass modes, plus a comb mode; hold SHIFT and turn CUTOFF to choose. In the multimode modes, CUTOFF sets the cutoff from roughly 10 Hz to 22 kHz; in comb mode it sets the position of the notches. RESONANCE has a special region: past 75 percent a chaotic noise generator activates, and its output is combined with the input and filtered, audible even with no input. SHIFT plus RESO places the filter at one of four positions in the effects chain. CUTOFF has a CV input of -5 V to 10 V, and the FILTER fader sets the dry/wet balance.

**Resonator.** The resonator is three separate instances of a stereo comb filter, tuned to related frequency bands. TUNE changes the base frequency of the three using three different ratios. FEEDBACK produces sustained resonance and, at 100 percent, makes the unit self-oscillate. SHIFT plus TUNE makes the resonance more dissonant, with a default of 0 percent. TUNE has a CV input of -5 V to 10 V.

**Echo.** The echo is a two-tap ping-pong delay. DENSITY sets the delay time from 10 ms to 4 seconds. REPEATS sets how many times the delay recirculates, from one repeat at 0 percent to infinite at 100 percent. When a clock is present at SYNC IN, DENSITY becomes a divider of that clock. SHIFT plus DENSITY runs the echo through a DJ-style filter: noon applies none, clockwise applies a high-pass filter, counterclockwise a low-pass filter. DENSITY has a CV input of -5 V to 10 V.

**Ambience.** The reverb is loosely based on a Schroeder reverberator. SPACETIME is a macro control for size, filtering, and direction: at 50 percent the size is smallest and the tone brightest, and at 0 or 100 percent the size is largest and the tone darkest. The manual states that values below 50 percent reverse the input signal. DECAY sets how long the tail takes to fade. An auto-panner is synchronized to the external sync input or to the frequency of one looper cycle; SHIFT plus SPACETIME sets the amount and the division or multiplication of its frequency at once: 0 percent is no auto-pan, 100 percent is full auto-pan at eight times the base frequency, with sixteen ratios in between and a default of 50 percent. SPACETIME has a CV input of -5 V to 10 V.

**Modulation: MOD LEVEL, SPEED, and TYPE.** Seven internal modulation types can be mapped to any parameter with a knob except the modulation controls themselves: chaos, sine LFO, ramp LFO, sawtooth LFO, square LFO, sample and hold, and envelope follower. Choose the type with SHIFT plus SPEED; the types morph smoothly from one to the next. MOD LEVEL is the master amount and overrides all mappings. SPEED scales the base frequency from one sixteenth to sixteen times using common divisions and multiplications. Unsynced, the base is about 0.2 Hz, so the range runs from about 0.01 Hz to about 3 Hz; synced, the base is the received clock, and the maximum is capped at 80 Hz. The envelope follower sits just before the looper, so it follows the input or the output depending on the PRE/POST switch, and SPEED sets the slope of its response from slow at 0 percent to fast at 100 percent. By default the modulation is sent to the filter CUTOFF; all other destinations are assigned in modulation mapping mode, and the modulation LED shows the current voltage.

**Randomizer: TARGET, AMOUNT, and RANDOM.** The TARGET switch picks what the randomizer changes: all units, oscillators only, looper only, or effects only. The AMOUNT switch sets the size of the change: the top position randomizes across the full range, the middle position applies a variation of plus or minus 20 percent, and the lower position plus or minus 2 percent. Pitch is randomized in semitones. The faders, the supersaw and wavetable selector, and everything accessed through SHIFT, the modulation mapping, and the CV mapping are excluded. Press RANDOM or send a trigger above 1 V to RANDOM IN to randomize. Holding RANDOM for the desired duration and releasing starts a gradual morph to the new values; the button flashes twice when the morph finishes, and this morph is not available from the RANDOM input. SHIFT plus RANDOM undoes a randomization, and doing it again redoes it. SHIFT plus RECORD plus RANDOM resets every parameter to the actual position of its control.

---

## Why This Instrument Excels

Oneiroi is a complete stereo voice with its own space. Sources enter through four faders, effects are blended in through four more, and the order of the chain is part of the instrument: the Filter can sit at the start, the middle, or the end, which changes whether the resonator and reverb process a filtered or an unfiltered signal. A single module takes a pitch CV and returns a finished, wide, sustained texture with a tail, which is the opposite of the usual Eurorack approach of assembling the same result from five or six separate modules and a pile of cables. The design assumes the patch is a drone or a pad and builds everything toward that assumption.

The looper is not an accessory but a source that feeds the rest of the module. The wavetable oscillator reads its waveforms from the looper buffer, so recording a sound turns that sound into the raw material of an oscillator, with DETUNE acting as OFFSET to move between 32 extracted tables. In POST mode the looper records the module's own output, so a texture can be captured, layered with sound-on-sound, and played back through the same effects chain. At minimum length the looper becomes an oscillator of its own. This closed loop between recording, oscillator, and effects is what separates Oneiroi from a synth with a delay and from a looper with a filter.

The depth of the control surface comes from layering rather than menus. Every knob has a Shift function, a mapped amount of internal modulation, and a mapped amount of external CV; the four effect CVs can be reassigned to secondary parameters; seven modulation types morph into each other with a single control. There is no screen and no menu diving; every state is visible on the panel or shown by the catch LEDs. The startup settings let each player choose how the interface behaves: jump or catch knobs, unipolar attenuators or bipolar attenuverters on both the modulation and CV amounts. The result is a module that rewards learning in the same way an instrument does.

The randomizer is scoped, reversible, and musical. Four targets limit what changes, three amounts limit how far it changes, pitch moves in semitones so randomized notes stay in tune with the system, and holding the button turns an abrupt change into a gradual morph. Undo and redo mean experimentation is cheap, and the reset to manual positions means a lost patch can always be recovered. Together with an external clock at SYNC IN, which synchronizes the echo, the auto-pan, and the modulation to one source, Oneiroi becomes an instrument that evolves on its own but stays inside boundaries the player sets.

---

## Patch Examples

Oneiroi is a SOURCE, and a stereo one: it makes sound on its own, so the First Voice is a pitched drone rather than a gated note. The cabling below replaces the usual oscillator, envelope, and VCA chain with a pitch CV and two audio outputs. An envelope generator and VCA are optional; if you add them, place them after the module and expect the Ambience tail to be cut off by a closing VCA. The module returns a mono-normalled signal if only OUT L is patched, so use both outputs for the stereo image.

All four patches below are drafts written from the manual and are untested on hardware ⚠️. Knob positions describe intent, and every "What to listen for" result is a prediction until the module has been patched.

---

### Patch 1: A Drone Through the Fader Chain ⚠️

This patch demonstrates that Oneiroi builds sound in two layers: source faders choose what is playing, and effect faders choose how much each effect contributes.

**First Voice**

Before introducing anything specific to Oneiroi, establish a working voice:

```
  Sequencer CV out ──[C]──▶ Oneiroi V/OCT
  Oneiroi OUT L ──[A]──▶ Mixer L
  Oneiroi OUT R ──[A]──▶ Mixer R
```

Use a sequencer such as Squarp Hermod+ (or Mutable Instruments Marbles, with X1 for pitch). Set the sequencer to hold a single note. Raise only the SINE fader and confirm that a steady tone appears at both mixer channels and follows the sequencer note.

**Add the supersaw and the chain**

```
                          ┌──────────────────────────────────┐
Sequencer ──[C]──▶        │ V/OCT                      OUT L │──[A]──▶ Mixer L
                          │                            OUT R │──[A]──▶ Mixer R
                          │ SINE  SS/WT  FILTER  AMBIENCE    │
                          └──────────────────────────────────┘
                                      Befaco Oneiroi
```

- `Sequencer CV out ──[C]──▶ V/OCT`: the pitch input is shared by all three oscillators, so one cable sets the pitch of the whole voice.
- `OUT L ──[A]──▶ Mixer L` and `OUT R ──[A]──▶ Mixer R`: the two outputs carry the stereo image produced by the supersaw and the effects; a single cable would collapse it.

Set the oscillator mode switch up for supersaw. Raise the SS/WT fader with the SINE fader already up, then turn DETUNE from center upward and listen to the seven saws spread. Raise the FILTER fader and move CUTOFF through its range. Raise the AMBIENCE fader and lengthen DECAY. Hold SHIFT and turn CUTOFF to move through the filter modes.

**What to listen for**

The sine should stay steady and clear underneath the supersaw, which should thicken and widen as DETUNE rises. The filter should remove or emphasize parts of the supersaw as CUTOFF moves, and the reverb tail should extend the sound after each change of note. If the output is thin or mono, check that both OUT jacks are patched. If the tone is silent, check that at least one source fader is raised and that the effect faders are not the only faders up, since an effect fader at its lowest position passes the signal unaffected rather than muting it.

---

### Patch 2: Resampling an Instrument with the Looper ⚠️

This patch demonstrates the looper as a recording source: an external stereo signal is captured and held while new material is layered over it with sound-on-sound.

**First Voice**

Use the same voice as Patch 1 for the outputs. For the external source, use Mutable Instruments Rings, played from a sequencer.

```
  Sequencer CV out ──[C]──▶ Rings V/OCT
  Sequencer gate out ──[G]──▶ Rings STRUM
  Rings ODD ──[A]──▶ Oneiroi IN L
  Rings EVEN ──[A]──▶ Oneiroi IN R
  Oneiroi OUT L ──[A]──▶ Mixer L
  Oneiroi OUT R ──[A]──▶ Mixer R
```

Set IN GAIN to the bottom position for Eurorack-level signals. Set PRE/POST to PRE. Raise the INPUT fader and confirm that Rings is audible through Oneiroi.

**Add the loop**

```
                          ┌──────────────────────────────────┐
Rings ODD ──[A]──▶        │ IN L                       OUT L │──[A]──▶ Mixer L
Rings EVEN ──[A]──▶       │ IN R                       OUT R │──[A]──▶ Mixer R
                          │ LOOPER  VARISPEED  RECORD        │
                          └──────────────────────────────────┘
                                      Befaco Oneiroi
```

- `Rings ODD ──[A]──▶ IN L` and `Rings EVEN ──[A]──▶ IN R`: Rings produces two outputs that carry different parts of its resonance, so the stereo input records a wide texture instead of a mono one.
- `OUT L` and `OUT R` return to the mixer so the recorded material and the live input are both heard.

Lower the SINE and SS/WT faders. Press RECORD and play Rings for several seconds; press RECORD again to stop. Raise the LOOPER fader and lower the INPUT fader to hear the loop alone. Hold SHIFT and turn START to set the sound-on-sound level near the top of its range, press RECORD again, and play new notes over the loop.

**Move the cable**

Leave Rings patched, but turn VARISPEED to the 100 percent position, then to the 0 percent position.

What changed: the playback speed and direction of the recorded material, from twice speed forward to twice speed in reverse, with no change to anything patched.

**What to listen for**

The loop should repeat the Rings phrase, and each new pass of Rings should stack on top of the older material while the older layers fade slowly. At the high SOS setting the old material should persist for many passes. At twice speed the loop should rise an octave; in reverse the notes should sound backward. If only noise is audible, the buffer has not been recorded yet, since it is prefilled with white noise. If recording fails to start, press RECORD again and check the LED color for clipping.

---

### Patch 3: Mapping Modulation and Using the Randomizer ⚠️

This patch demonstrates the Shift layer in practice: internal modulation is routed to chosen parameters by moving knobs, a randomizer changes the sound within limits, and the result is saved.

**First Voice**

Use the same voice as Patch 1, with the SINE and SS/WT faders raised and the FILTER and AMBIENCE faders raised.

**Add the mapping**

```
                          ┌──────────────────────────────────┐
Sequencer ──[C]──▶        │ V/OCT                      OUT L │──[A]──▶ Mixer L
                          │ MOD AMT  MOD LEVEL  SPEED        │
                          │ RANDOM   TARGET     AMOUNT  OUT R│──[A]──▶ Mixer R
                          └──────────────────────────────────┘
                                      Befaco Oneiroi
```

- `Sequencer CV out ──[C]──▶ V/OCT`: a steady pitch lets the changes from modulation and the randomizer be heard as timbre.
- `OUT L` and `OUT R` to the mixer: the stereo image is where the auto-pan and the reverb show up.

Press MOD AMT; the button blinks red, which is the modulation mapping page. Turn DETUNE a short way, then SPACETIME a short way, so that the internal modulation reaches those two parameters. Leave the mapping page, raise MOD LEVEL, and set SPEED to a slow rate. Hold SHIFT and turn SPEED to choose a modulation type, from the seven available. Set TARGET to oscillators and AMOUNT to the middle position, then press RANDOM several times.

**Save the result**

Hold MOD AMT for two seconds. The LED should confirm the save. Power the rack off and on and check that the settings return. The looper buffer will not return, because it is never saved.

**What to listen for**

The supersaw spread and the reverb character should drift over time at the pace of SPEED. Each press of RANDOM should change pitch and oscillator settings by a limited amount while the faders stay where they are. SHIFT plus RANDOM should step back to the previous sound. After a power cycle, the saved knob positions and mappings should return. ⚠️ How to leave the mapping page, and the exact LED behavior of the save, come from the manual and are unverified on hardware.

---

### Patch 4: A Clocked, Self-Playing Drone ⚠️

This patch demonstrates that Oneiroi can run a full generative piece from a clock: a slow division synchronizes the modulation, echo, and auto-pan, a random source plays the pitch, and a random trigger moves the sound.

**First Voice**

Use the same voice as Patch 1, with a master clock in place of the sequencer and Marbles supplying pitch.

**Add the clock and the random sources**

```
                          ┌──────────────────────────────────┐
RCD Out 8 ──[T]──▶        │ SYNC IN                    OUT L │──[A]──▶ Mixer L
Marbles X1 ──[C]──▶       │ V/OCT                      OUT R │──[A]──▶ Mixer R
Marbles t2 ──[T]──▶       │ RANDOM IN                        │
                          └──────────────────────────────────┘
                                      Befaco Oneiroi
```

- `Master clock ──[T]──▶ 4ms RCD v2 Clock In`: the divider needs the beat it will divide.
- `Master clock ──[T]──▶ Marbles t clock input`: the same beat keeps Marbles in time with the divider.
- `RCD Out ──[T]──▶ SYNC IN`: choose an output that gives about one trigger per bar or less; the manual advises a slow clock because one clock serves the looper, the modulation, the echo, and the auto-pan.
- `Marbles X1 ──[C]──▶ V/OCT`: a random pitch source sets the notes the drone moves between.
- `Marbles t2 ──[T]──▶ RANDOM IN`: each trigger above 1 V runs the randomizer.
- `OUT L` and `OUT R ──[A]──▶ Mixer`: the stereo output.

Use a clock divider such as 4ms RCD v2 (or ALM Busy Circuits Pamela's PRO Workout). Set TARGET to effects and AMOUNT to the middle position. Allow a couple of seconds for SYNC IN to lock to the clock.

**What to listen for**

After a few seconds the echo time and auto-pan should settle to ratios of the clock, and the modulation should follow the same beat. Marbles should change the pitch of the drone, and each t2 trigger should change the effects within the limits of the randomizer. If nothing locks, check that the clock exceeds 1 V and that it is no faster than one trigger per bar. ⚠️ The voltage span of Marbles X1 against the 0 V to 10 V range of V/OCT is unverified; set the Marbles voltage range so that X1 stays positive, since the input clips outside its range.

---

## Firmware and Calibration

Oneiroi has three code layers: the Bootloader, the Firmware, and the Patch. Most players only ever touch the Patch layer, which is updated through a browser using the OpenWare Laboratory page. Download patch.syx from the Befaco Oneiroi releases on GitHub, open the OpenWare Laboratory in Chrome or Chromium, and store the file to slot 1. From patch version 1.1 onward, the module shows its version at boot: the RECORD LED blinks the major version and the RANDOM LED blinks the minor version. Updating from version 1.0 needs a config erase, which means deleting everything except oneiroi.cfg.

Calibration is needed only after assembly or after replacing a component. It requires a voltage source accurate to plus or minus 0.005 V, and the manual warns that a wrong calibration breaks the module, so do not attempt it on a working module.

Startup settings are chosen by holding RECORD and RANDOM while powering on. Then SHIFT toggles the knob behavior between catch (the parameter ignores a knob until the knob reaches the stored value) and jump (the parameter follows the knob at once), with jump as the default. RECORD toggles the modulation amount range between attenuverter and attenuator, and RANDOM toggles the CV amount range the same way.

**Notes on the manual.** Three details in the manual are easy to misread. It describes three oscillators, but the supersaw and the wavetable share one slot, so only two sound at once. It refers to Chapter 4.3 for saving, but saving is described in chapter 8. And it refers to the SHIFT and CV AMT buttons for CV mapping, where the physical button is labeled MOD AMT and the CV AMT label is the Shift function of that button.

---

## Common Mistakes

### "I raised the LOOPER fader and only hear noise"

The loop buffer is prefilled with white noise, so the looper makes sound before anything has been recorded. Lower the fader, record something, and raise it again. To remove an old recording, press SHIFT and RECORD to clear the buffer, which returns it to its starting state.

### "My settings are gone after I turned the rack off"

Oneiroi has no presets, and nothing is written to memory automatically. To keep the current state, hold MOD AMT for two seconds. The save covers the parameters, including the modulation and CV mappings, but the looper buffer is never saved, so any recording is lost when the power goes off. Save the settings you want before powering down, and plan to rerecord the loop.

### "I turned a knob and nothing happens"

Oneiroi has two knob behaviors, catch and jump. In catch mode, a parameter ignores the knob until the knob position reaches the stored value, which happens after a randomization, an undo, or a loaded state. In jump mode, the default, the parameter follows the knob immediately, and a sudden jump in sound is normal. Check the startup settings if the behavior differs from what you expect. ⚠️ The LED colors that indicate a catch state come from the manual and are unverified.

### "The randomizer ruined my sound"

Randomization is reversible. Press SHIFT and RANDOM to undo, and press the same combination again to redo. To return every parameter to the actual position of its knob, press SHIFT, RECORD, and RANDOM together. Limit the damage in advance by setting TARGET to the section you want to change, and AMOUNT to the middle or lower position. The faders and the oscillator mode switch are never randomized.

### "SYNC IN does not lock to my clock"

SYNC IN needs triggers above 1 V and takes a couple of seconds to align to a new clock. It returns to the internal clock of about 0.2 Hz in a similar time after the cable is removed. The clock should stay between 30 and 300 BPM, and the manual advises one trigger per bar or slower, since the same clock restarts the looper at the START point, clocks the modulation, and sets the echo time and auto-pan. A fast clock makes the looper restart constantly.

### "The modulation only moves the filter"

By default the internal modulation goes to the filter cutoff and nowhere else. To send it to other parameters, open the modulation mapping page with MOD AMT, then turn the knobs of the parameters you want. MOD LEVEL is the master amount and overrides every mapping, so a MOD LEVEL at zero silences all modulation even with a complete mapping. To remove a mapping, press RECORD and RANDOM together while the mapping page is open.

---

## Advanced Learning Path

1. **Learn the fader architecture.** Raise each source fader alone, then each effect fader alone, and listen to what the unprocessed and processed signals do. Then try each filter position by holding SHIFT and turning RESO, and notice how the order of the chain changes the character of the resonator and the reverb.

2. **Record, then play the loop as a source.** Record several seconds of an external instrument with PRE selected, then clear the input and play the loop alone. Move START and LENGTH, then VARISPEED, to hear how the same recording becomes different material. Reduce LENGTH to its minimum and listen to the looper act as an oscillator.

3. **Use filter comb mode and the chaos region.** Hold SHIFT and turn CUTOFF to select the comb mode and listen to the notches move. Then raise RESONANCE past 75 percent, where a chaotic noise generator activates, and notice that it sounds even with no input.

4. **Tune the resonator.** Raise the RESONATOR fader and move TUNE across its range. Raise FEEDBACK toward self-oscillation, then hold SHIFT and turn TUNE to make the three combs more dissonant. Play a sequencer pitch through it and compare consonant and dissonant settings.

5. **Map the internal modulation.** Open the modulation mapping page with MOD AMT and assign the modulation to three or four parameters at different amounts. Choose different modulation types with SHIFT and SPEED, and try the envelope follower, which responds to the input or the output depending on the PRE/POST switch.

6. **Map the CV inputs.** Open the CV mapping page by holding SHIFT and pressing MOD AMT, and set how much each parameter responds to its CV. Reassign an effect CV to a secondary parameter. Use the startup setting to switch the amount range to attenuverter and notice what changes.

7. **Morph with the randomizer.** Set TARGET and AMOUNT, then hold RANDOM for several seconds and release to start a gradual morph. Watch for the two flashes that mark its completion. Use the lowest AMOUNT setting to make subtle evolutions, and undo with SHIFT plus RANDOM when a result is wrong.

8. **Close the loop with POST and the wavetable.** Set PRE/POST to POST so the looper records the module's own output, and record a texture built from the sine, the supersaw, and the effects. Switch the oscillator mode to wavetable and move OFFSET, which selects among 32 tables extracted from that recording. The module then plays an oscillator made from its own sound.

---

## Pairs Well With

**4ms RCD v2:** The divider turns one clock into several related triggers, and SYNC IN needs exactly one slow beat that the rest of the module derives its timing from. A single output of 4ms RCD v2 set to one trigger per bar locks the echo, the auto-pan, and the modulation together, and the Rotate input moves which division feeds the module over time. ⚠️

**ALM Busy Circuits Pamela's PRO Workout:** Pamela's PRO Workout offers the same slow, stable beat through its division and swing outputs, with a range of timing variations that can change where the trigger falls in the bar. It can feed SYNC IN with a slow clock and RANDOM IN with a pattern of triggers from other outputs, which makes the randomizer follow a rhythm rather than a random source.

**Mutable Instruments Marbles:** X1 supplies the pitch for the V/OCT input and t2 supplies the triggers for RANDOM IN, so one module plays the drone and moves its character. DEJA VU locked makes the sequence repeat while the effects continue to evolve, and unlocked, the whole piece drifts. ⚠️ Confirm the X1 voltage span against the 0 V to 10 V range of V/OCT.

**Joranalogue Fold 6:** Placing Joranalogue Fold 6 ahead of the module, with MAIN feeding IN L and ALT feeding IN R, sends the two voicings of one fold into the two input channels. The folded harmonics then pass through the looper or the effects chain, so a simple sine becomes a rich stereo source. Set IN GAIN to the Eurorack position, and keep the module's fold depth moderate, since the output reaches about 10 Vpp.

**Mutable Instruments Rings:** Rings has two outputs, ODD and EVEN, that fill both input channels with different parts of a resonant texture, and its plucked notes make clean material for the looper. Recording Rings into the buffer and then playing it back at half speed or in reverse turns a struck string into a slow, bowed pad. The sound-on-sound level then controls how long old strums linger under new ones.

**Xaoc Devices Zadar:** The Zadar envelope and shape outputs run from 0 V to 10 V, which matches the range of the volume CV inputs on Oneiroi. A Zadar shape on a source fader CV makes that source swell on a pattern, and the fader then acts as an attenuator for the incoming CV. A second shape on a dry/wet CV moves one effect in and out of the sound on the same clock.

---

*Visit [befaco.org](https://www.befaco.org/oneiroi/) for the official manual and product information*
