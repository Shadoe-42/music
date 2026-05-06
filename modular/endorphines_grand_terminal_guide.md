---
title: "Endorphin.es Grand Terminal"
manufacturer: "Endorphin.es"
primary_role: FILTER
secondary_roles: [MODULATOR, SHAPER]
historical_context: true
form_factor: eurorack
functions: [filter, envelope, effects-processor, mixer]
behavior_tags: [dual-filter, digital, cv-controlled, stereo, multi-mode, self-contained-voice, effects, looping-envelope]
use_cases:
  - "Complete synthesizer voice processing: dual envelopes controlling dual filters with integrated stereo effects"
  - "Multi-mode filter exploration across eight modeled filter architectures in a single module"
  - "External audio processing at modular or line level with reverb, delay, and modulation effects"
  - "Drone and ambient texture work using Airplane loop mode as LFO driving filter modulation and effects"
  - "Parallel, stereo, or serial dual-filter routing for complex timbral shaping"
hp: 26
depth: 25mm
memory: true
transport: none
screen: false
hybrid: true
cv: full
---

![Endorphin.es Grand Terminal front panel](images/endorphines/grand_terminal/front_panel.jpg)

## Historical Context

The synthesizer has always oscillated between two organizing philosophies. One says that every functional block deserves its own dedicated module: an oscillator is an oscillator, a filter is a filter, an envelope is an envelope, and the musician assembles them in whatever configuration the music requires. The other says that integration serves performance: a complete voice in a single instrument, ready to play without a patch cable in sight.

Robert Moog's Minimoog (1970) became the archetype of the integrated approach. Designed by Bill Hemsath and Robert Moog after observing that performers at concerts consistently patched the same signal path through their Moog modular systems, the Minimoog hardwired that path: three oscillators, a mixer, the transistor ladder filter, and a contour generator in a single portable keyboard. The transistor ladder filter had been Moog's invention in 1965, a four-pole low-pass circuit built around a cascade of transistors in a ladder configuration that produced a sound unlike any earlier filter. The Minimoog made that filter the center of a complete instrument rather than a module waiting to be connected.

That single instrument generated a reference vocabulary that persists across synthesizer history. The filter resonance sweep. The envelope-driven brightness contour. The hard attack and the long release. These are Minimoog sounds, and they became the baseline against which all subsequent synthesizer voices were measured.

Every filter in the Grand Terminal references a different moment in that history. The transistor ladder is Moog's original circuit, modeled here after the Minimoog implementation. The diode ladder is inspired by the Roland TB-303 (1981) and the EMS Synthi A, two instruments whose filter character defined entire genres: the TB-303 diode ladder became the sound of acid house after Roland discontinued the machine and producers discovered what the instrument could do when pushed into resonance. The vactrol low-pass gate comes from Don Buchla's work at the San Francisco Tape Music Center in the 1970s, a circuit that combines a light-emitting diode with a photoresistor inside a single package to control filter cutoff and amplitude simultaneously, producing the natural exponential decay associated with Buchla's instrument voice design. The state variable filter appears in the Oberheim SEM (1974) and the Korg MS-10 and MS-20, a topology that simultaneously produces low-pass, high-pass, and band-pass outputs from a single circuit. The comb filter models a series of notch filters that, when modulated, produce the sweeping resonant character of flanging and phasing.

Endorphin.es, operating as Furth Barcelona, S.L., is based in Barcelona, Spain. Founded around 2013 and active through a period of considerable growth in the Eurorack market, the company's catalog is distinguished by consistent use of aviation as a design metaphor. The Grand Terminal carries this language throughout: envelopes are Airplanes, attack is Take Off, decay is Landing, the effects section is the Cabin Pressure processor. The metaphor is not merely cosmetic. It reflects an approach to synthesis performance as travel: a departure, a duration, and an arrival, with the passenger's comfort managed by systems running in the background.

The Grand Terminal integrates the dual envelope, dual filter, and stereo effects into a 26HP module designed to function as a complete voice processing chain when paired with an oscillator, or as a self-sufficient experimental instrument when the Airplane envelopes run in loop mode. It runs a dedicated ARM Cortex-M4 DSP processor for the filters and effects at 16-bit, 48kHz.

## Quick Start

1. Patch an oscillator output into Gate A input (labeled "To The Gates"). Set the Gate A input trim knob (small knob above the input) to the left of center for modular-level input. Select filter type 1 (Transistor Ladder) by pressing the Mode A button until a single LED illuminates at full brightness.
2. Patch a gate or trigger into the Check-In input of Airplane A (left envelope). Set the Trip Selector to the middle position (Transient/AD mode). The envelope fires on each trigger: Take Off rises, then Landing falls.
3. Connect Airplane A's unipolar output (0V to +8V) to the Gate A X CV input to modulate filter cutoff with the envelope. Set the X knob to about 9 o'clock as an attenuverter. The filter opens on each trigger and closes as the envelope falls.
4. Take the stereo output (or mono output for modular-level routing to a mixer) from the Final Out section at the top center of the module.
5. Press the Cabin Pressure TYPE button to select an effect. Turn the Cabin Pressure knob clockwise to introduce reverb or delay into the output. The signal now has filtering, envelope shaping, and spatial processing from a single module.

## Key Specifications

| Specification | Value |
|---|---|
| Width | 26 HP |
| Depth | 25 mm |
| +12V Current | 230 mA |
| -12V Current | 65 mA |
| +5V Current | 0 mA |
| DSP | ARM Cortex-M4, 16-bit / 48 kHz |
| Filter Types | 8 per channel (A and B independent) |
| Envelope Modes | 3 (Cruise/ASR, Transient/AD, Loop/LFO) |
| Effect Slots | 8 (from two firmware banks) |
| Stereo Output | Line level, headphone-capable (~0 dBu nominal, up to +4 dBu) |
| Mono Output | Modular level (~±5V), L+R summed |
| Firmware Update | USB (or audio injection into Gate A input) |
| Price | $679 |

**Power note:** At 230 mA on the +12V rail, the Grand Terminal draws more current than any other module in this guide series. Plan rack power carefully. If this module and the Plasma Voice (220 mA) are in the same case, those two modules alone account for 450 mA before any other module is considered. A case with a 1A +12V rail is not sufficient for a populated rack that includes both modules. Verify total rail capacity against total draw before powering up a new configuration.

**Firmware note:** The Grand Terminal supports firmware updates via USB or audio injection. Features described in this guide reflect the module's documented behavior as of the TOTAL NIGHTMARE firmware family. Effects available from the module depend on which firmware bank is loaded. Consult the Endorphin.es documentation for current firmware releases and feature sets.

## The Airplanes: Dual Envelope Generators

The two envelope generators, Airplane A (left) and Airplane B (right), are transient function generators with three operating modes, continuously variable slope shapes, and two outputs each. Endorphin.es calls them Airplanes because of the design metaphor that runs through the module: the envelope is a flight, with a departure, a cruise, and a landing.

Each Airplane has two stages: Take Off (attack) and Landing (decay or release depending on mode). Each stage has a dedicated knob that controls duration from 1 millisecond to 10 seconds when no CV is applied. The same knob serves a second function when CV is connected to the stage's CV input: it becomes an attenuverter controlling the amount of CV applied to the stage time. The range of CV accepted is ±5V. A positive voltage with the attenuverter clockwise lengthens the stage; a negative voltage or clockwise attenuverter with inverted CV shortens it.

The slope shape of each stage is also continuously variable. When no CV is patched into the stage input, the stage time knob controls duration as described above, but turning it toward center produces a linear slope while turning toward either extreme curves the slope toward exponential or logarithmic shapes. The knob therefore simultaneously controls duration and slope shape in its unplugged state: a dual-function design that rewards careful reading of the panel position.

### Airplane Modes

The Trip Selector switch sets the operating mode for each Airplane independently.

**Cruise mode (far right position):** The Airplane operates as an AR or ASR envelope. A trigger or gate arriving at the Check-In input initiates Take Off. The Airplane rises to maximum voltage and holds there for as long as the gate remains high. When the gate falls, Landing begins and the Airplane descends to rest. This is the sustained envelope behavior found on most synthesizers: the sound holds while the key is held and releases when the key is released. If a trigger arrives during Landing, the Airplane immediately begins Take Off again from its current level.

**Transient mode (middle position):** The Airplane operates as an AD envelope. Any trigger or gate above approximately 0.65V initiates Take Off. The Airplane rises, then immediately begins Landing without waiting for the gate to fall. The gate length does not affect the envelope duration; only the Take Off and Landing knob positions determine timing. A second trigger during Landing causes the Airplane to immediately begin a new Take Off. This mode produces percussive envelope shapes that complete regardless of gate length, making it appropriate for drum and pluck sounds.

**Loop mode (far left position):** The Airplane cycles continuously without requiring a trigger. Take Off rises to maximum, then Landing descends to minimum, then Take Off begins again, repeating indefinitely. The Airplane functions as an LFO generating a shape defined by the Take Off and Landing knob positions. At slow speeds with linear slopes, this produces a triangle-like wave. At fast speeds, the sloped waveform enters audio rate and the output functions as a band-limited oscillator. In Loop mode, the Check-In input can reset or synchronize the cycle.

### Airplane Outputs

Each Airplane has two output types:

**Unipolar output (0V to +8V):** Positive voltage only. At rest, the output is 0V. At the top of Take Off, the output reaches approximately +8V. This output is appropriate for controlling destinations that expect only positive CV, including filter cutoff via the Grand Terminal's own X/Y inputs.

**Bipolar output (-5V to +5V):** Centered at 0V at rest, rising to +5V at the peak of Take Off and capable of swinging to -5V in some configurations. The bipolar output is appropriate for destinations that benefit from both positive and negative modulation, such as the oscillator pitch, VCA polarization, or any parameter where negative CV creates meaningful behavior.

The relative brightness and color of the LEDs adjacent to each output indicates the current output voltage: green light when the voltage is positive, red light when negative, with brightness indicating amplitude.

### End-of-Stage Triggers

Each Airplane has outputs that fire a short 1ms trigger at the end of the Take Off stage and at the end of the Landing stage. These are configurable via jumpers on the back panel of the module. Connecting the end-of-Landing output of Airplane A to the Check-In of Airplane B creates a sequenced double envelope: B fires after A completes its descent. Connecting end-of-stage outputs to clock inputs elsewhere in the patch creates divisions of the envelope's natural rate.

---

## The Filters: Dual Multi-Mode Gates

The two filters, Gate A (left) and Gate B (right), are labeled "To The Gates" on the panel. Each accepts audio at either modular or line level, selected by the small trim knob above each input jack. Each filter independently cycles through eight modeled filter architectures. The filters run on the module's DSP processor at 16-bit, 48kHz.

### Input Level

The input trim knob for each filter gate sets the gain of the audio input:

**Fully counterclockwise (CCW):** The input accepts modular-level audio at approximately ±5V. Signals exceeding approximately ±6.9V are soft-clipped at this input stage. This is the setting for audio arriving from other modules at standard Eurorack level.

**Fully clockwise (CW):** The input gain shifts to accommodate line-level sources approximately ten times quieter than modular level, corresponding to a nominal 1Vpp signal. This allows the Grand Terminal to process audio from an external synthesizer, recording interface output, or any line-level source without a separate level converter. The full range of trim positions between CCW and CW scales the input gain continuously.

Gate A accepts a stereo signal when a TRS (stereo) 3.5mm cable is inserted: the right channel of the stereo source routes through the switched connection into Gate B. This allows a single stereo source to feed both filters simultaneously when using TRS: one cable connecting a stereo instrument to both filter channels.

### Filter Type Selection

Pressing the Mode button for Gate A or Gate B cycles through the eight filter types one at a time. The row of four LEDs between the X and Y knobs indicates the current selection: a fully illuminated LED corresponds to one of the first four filter types (lower row), while a dimly illuminated LED corresponds to one of the second four filter types (upper row). The four LED positions combined with the two brightness levels encode all eight positions.

### The Eight Filter Types

**Type 1: Transistor Ladder (24 dB/octave low-pass)** modeled after the Minimoog filter. Four-pole slope, rich low-frequency response, self-oscillates at full resonance. The most versatile filter type in the set and the appropriate starting point for synthesizer bass and lead sounds. Frequency response to 16kHz.

**Type 2: Diode Ladder (18 dB/octave low-pass)** inspired by the Roland TB-303 and EMS Synthi A. Three-pole slope with distinct character in the resonance behavior. The resonance produces the nasal, aggressive quality associated with acid basslines. Frequency response to 18kHz.

**Type 3: Vactrol Low-Pass Gate (12 dB/octave, non-resonant)** modeled after the Buchla low-pass gate. The Y control in this filter type does not set resonance; it sets the decay time of the virtual vactrol's closing response, ranging from approximately 120 milliseconds at full CCW to 4 seconds at full CW. Pinging this filter type with a short trigger produces the characteristic Buchla percussion sound: a fast opening followed by a slow exponential decay governed by the vactrol's simulated closing time. Frequency response to 17kHz.

**Type 4: Resonant Vactrol Low-Pass Gate (12 dB/octave)** is a variation with a fixed decay time set to approximate a standard fast vactrol, restoring Y to resonance control. The decay behavior is consistent rather than user-variable, preserving the vactrol's natural response while adding resonance.

**Type 5: State Variable Low-Pass (12 dB/octave)** based on the Oberheim SEM and Korg MS-10/MS-20 topology. Cleaner slope than the ladder filters, less harmonically dense, with resonance loudness compensation that maintains output amplitude as resonance increases. Frequency response to 16kHz.

**Type 6: State Variable High-Pass (12 dB/octave)** passes high frequencies and attenuates low frequencies. At minimum resonance with the cutoff fully open, this filter removes all low frequencies including the fundamental of many bass sounds. Use carefully at low cutoff settings.

**Type 7: State Variable Band-Pass (12 dB/octave)** passes a defined band of frequencies. X controls the band center frequency; Y controls the bandwidth of the band rather than resonance. Narrowing the band produces a peaked, telephonic quality. Widening it approaches the character of the low-pass with attenuated bass.

**Type 8: Comb Filter** creates a series of harmonically related notch filters. In its static state it resembles a phaser. With the X parameter modulated, it approaches flanging. At maximum resonance, it functions as a resonator, reinforcing harmonic partials of the input signal.

### X and Y Parameters

X and Y are the two main parameters for each filter. X typically controls cutoff frequency and Y typically controls resonance, but the assignment varies per filter type as described above. The X and Y knobs function as manual offsets when no CV is applied and as attenuverters when CV is connected to the corresponding CV inputs.

**Critical:** The X and Y CV inputs accept **unipolar voltage only, from 0V to +5V**. Voltages above +5V are saturated. Negative voltages are not effective at these inputs. This is different from most Eurorack CV inputs that accept bipolar signals. Envelopes, LFOs, and other sources that swing below 0V must be attenuated and offset to a unipolar range before connecting to the Grand Terminal's filter CV inputs. The Airplane unipolar outputs (0V to +8V, attenuated to 0V to +5V via the X/Y knob as attenuverter) are the most convenient internal source for filter CV.

### Filter Routing Modes

Pressing both Mode buttons simultaneously for approximately one second cycles through three routing configurations for the two filter channels.

**Parallel mode (default, both LEDs off):** Gate A and Gate B are completely independent. Each processes its own audio input with its own filter type and settings. Their outputs sum together at the Final Out stereo and mono outputs, with the Cabin Pressure effects applied to the combined mix. In this mode, pressing the TYPE button for Gate A bypasses the Cabin Pressure processor for that channel only, allowing Gate B to receive effects while Gate A remains dry.

**Stereo mode (both LEDs red):** Gate A and Gate B are linked. The X and Y knobs and Mode button of Gate B become inactive. Gate A's X and Y knobs control both filters simultaneously, and both filters share the same filter type. The default panning places Gate A far left and Gate B far right in the stereo field. Pressing the TYPE button in Stereo mode spreads Gate A to hard left and Gate B to hard right regardless of previous panning settings.

**Serial mode:** The audio inputs of Gate A and Gate B are summed together and pass through Gate A first, then through Gate B in series. The output of Gate A feeds the input of Gate B. Two different filter types applied in series produce a combined transfer function: a vactrol LPG followed by a transistor ladder produces a different sound than either alone. Pressing the TYPE button in Serial mode swaps the filter types assigned to Gate A and Gate B with each other.

### Secondary Mode: Volume and Panning

Holding either Mode button for longer than one second accesses secondary controls for that filter channel. In secondary mode, the X knob controls stereo panning (center position = equal left and right power), and the Y knob controls the volume of that channel's output. Turning Y past approximately the 2 o'clock position introduces additional gain that pushes into deliberate distortion at the filter channel's output stage. The Mode LED blinks red when crossing into the distortion region and green when the level returns to normal. This distortion is independent of the input trim and occurs after the filter processing.

---

## Cabin Pressure: The Effects Processor

The Cabin Pressure section is a stereo effects processor applied to the summed output of both filter channels. It operates entirely in the digital domain at 16-bit, 48kHz, using the same DSP core as the filters.

### Effect Selection

The TYPE button in the Cabin Pressure area cycles through eight effect slots, with the specific effects available depending on the firmware bank loaded. Two banks are documented: the Airways Bank and the Darkwaves Bank, each containing eight distinct effects. The 8 LEDs between the Cabin Pressure X and Y sections indicate the current effect position; the specific bank loaded determines which effects occupy those eight positions.

**Airways Bank effects:** Hall Reverb, Shimmer Reverb (hall with pitch-shifted layer), Stereo Room Reverb, Plate Reverb, Spring Reverb, Ping-Pong Delay, Tape Echo (three fixed playback heads), Chorus.

**Darkwaves Bank effects:** Gated Reverb (plate reverb with noise gate), Spring Reverb (different character), Reversed Reverb, Flanger, Ring Modulator (internal sine oscillator multiplied with signal), Overdrive, Peak Compressor (threshold, ratio, and attack controls), Freezer/Looper (granular freeze triggered by gate).

### Cabin Pressure Knob and CV

The Cabin Pressure knob controls the dry/wet balance for the active effect. Fully counterclockwise is completely dry (no effect). Fully clockwise is 100% wet (effect only, no dry signal). The Cabin Pressure CV input accepts bipolar voltage (-5V to +5V). When a cable is inserted, the Cabin Pressure knob becomes an attenuverter for the incoming CV rather than a direct dry/wet control.

### Cabin Fever Knob, TAP, and Secondary Parameters

The Cabin Fever knob and its corresponding CV input control the primary effect-specific parameter for the active effect. For reverbs, this is typically decay time or room size. For delays, it is feedback amount. For the ring modulator, it is oscillator speed. For the chorus, it is feedback depth.

Each effect also has a secondary Cabin Fever parameter accessed by holding the TAP button for longer than one second. The LED in the Cabin Fever area blinks red once to confirm entry into secondary mode, and the effect slot LED strobes twice per period instead of once. Secondary parameters include items such as high-pass filter on reverb tails, pre-delay amount, noise gate threshold (gated reverb), pitch-shifter mix (shimmer), stereo spread (room reverb), and feedback for the flanger. Pressing and holding TAP for one second again returns to primary mode.

The TAP button in primary mode sets tempo for delay effects by rapid tapping, and triggers the spring pluck effect in the spring reverb.

The Freezer/Looper effect deserves specific mention: when the Cabin Fever CV input receives a gate signal (or the TAP button is held), the incoming audio is looped at a grain length set by the Cabin Fever knob, at a speed set by the Cabin Pressure knob. This is a simple granular freeze that holds the current audio content and loops it until the gate is released.

---

## Output Section

The Final Out section at the top center of the module provides two simultaneous output types.

**Stereo output (two 3.5mm jacks, L and R):** True stereo line-level output. The nominal level is approximately 0 dBu; the maximum is approximately +4 dBu. This output has sufficient current to drive headphones directly, making the Grand Terminal useful as a self-contained headphone synthesizer during practice or travel. Panning settings from the filter secondary modes and from the Stereo routing mode affect the stereo field of this output.

**Mono output (single 3.5mm jack):** Modular-level output with the left and right channels summed to a single signal at approximately ±5V. Panning adjustments in secondary mode affect the stereo output but not the mono output, since both channels always sum to center in mono.

The master volume blue knob at the top center controls the amplitude of both outputs simultaneously. This is the final gain stage before the output jacks.

Endorphin.es supplies a stereo-to-dual-mono adapter cable with the Grand Terminal for routing the stereo output to two separate modular inputs without requiring a TRS-to-TS splitter from another source.

---

## Why Grand Terminal Excels

The Grand Terminal's defining characteristic is density of function in performance. A performer has access to dual filter shaping, dual envelope generation, and stereo effects without patch cables connecting any of these elements together. The envelopes are already positioned to control the filters they share a panel with. The effects are already on the output of those filters. The integration is not accidental; it is the point.

The eight filter types represent eight genuinely different timbral philosophies. The transistor ladder and diode ladder are both low-pass filters but sound different enough to warrant separate consideration: one has the smooth, musical resonance of Moog circuits, the other has the nasal, aggressive character of Roland's acid bass machine. The vactrol LPG has no resonance in its base form but the variable decay time turns it into a percussion shaping tool that no other filter type in the set can replicate. The state variable types give high-pass and band-pass behaviors not available from the ladder filters. The comb filter is categorically different from all the others: it shapes by reinforcing and canceling harmonics rather than by attenuating a frequency band. Having all eight accessible on one filter channel, switchable during performance, makes the Grand Terminal more flexible than most dedicated filter modules.

The Airplane Loop mode as LFO is not a secondary feature; it is a primary use case for ambient and experimental work. Both Airplanes in Loop mode with different rates and slope shapes, each routed to a different filter's X or Y input, produces continuous filter motion without any external modulation source. The Cabin Pressure effects on top of this create a self-contained ambient instrument that requires nothing from the rest of the rack except an oscillator and a trigger source.

The stereo line output changes the module's role in the studio chain. The Grand Terminal does not need the MixUp and Cockpit 2 in the path if its output is going directly to headphones or directly to an audio interface. For studio use where the Grand Terminal is the primary processing stage for a voice, it can bypass the standard in-rack output chain entirely.

---

## Patch Examples

### Patch 1: Complete Synthesizer Voice with Furthrrrr Generator

**What this demonstrates:** The intended pairing: oscillator into dual filters with envelope control, effects on output.

Set Gate A filter type to Type 1 (Transistor Ladder). Set Gate B filter type to Type 5 (State Variable LP). Set Filter Routing to Parallel mode. Set both Airplanes to Transient (AD) mode. Select Plate Reverb from Cabin Pressure.

```
[Furthrrrr Generator oscillator output] [A]
         │
         ├──────────────────────────────────────────────────────┐
         ▼                                                      ▼
[Gate A input: Transistor Ladder]                 [Gate B input: State Variable LP]
[Gate A X CV: Airplane A unipolar out] [C]        [Gate B X CV: Airplane B unipolar out] [C]
         │                                                      │
         └──────────────────┬───────────────────────────────────┘
                            │
                            ▼
                [Cabin Pressure: Plate Reverb, 30% wet]
                            │
                            ▼
                 [Stereo Output: to interface] [A]
```

Airplane A trigger arrives at each note. Gate A opens with the transistor ladder's warm, musical response. Airplane B fires simultaneously with a slightly longer decay, opening the state variable filter with a cooler, cleaner curve. The two filtered signals sum in parallel with the reverb tail behind them. Adjusting each filter type to different values gives two independent timbral perspectives on the same oscillator simultaneously.

---

### Patch 2: External Synthesizer Processing

**What this demonstrates:** Using the Grand Terminal as an effects and filter unit for an external line-level instrument.

Set Gate A input trim to CW (line level input). Select Vactrol LPG (Type 3). Set Filter Routing to Serial mode. Select Shimmer Reverb from Cabin Pressure.

```
[External synthesizer line output]
         │
         ▼
[Gate A input: Vactrol LPG, trim knob CW for line level] [A]
[Gate A Y knob: 10 o'clock, vactrol decay time control]
[Gate A X knob: set cutoff position]
         │  serial: Gate A feeds Gate B
         ▼
[Gate B: Comb Filter]
[Gate B X: cutoff (comb center), Y: resonance (comb bandwidth)]
         │
         ▼
[Cabin Pressure: Shimmer Reverb, 40% wet]
[Cabin Fever: decay time, moderate]
         │
         ▼
[Stereo Output: to interface] [A]
```

The external synthesizer passes through the vactrol LPG first, which softens transients and shapes the amplitude envelope with its natural exponential decay. That shaped signal feeds into the comb filter in serial, adding resonant coloration. Shimmer reverb gives the output a diffuse, pitch-shifted ambience. The external instrument is processed as thoroughly as any internally generated voice.

---

### Patch 3: Dual-Rate Airplane LFO Filter Modulation

**What this demonstrates:** Both Airplanes in Loop mode as LFOs driving independent filter channels with no external modulation needed.

Set Airplane A to Loop mode, slow Take Off and Landing (both knobs at 8-9 o'clock), linear slope. Set Airplane B to Loop mode, faster rate (Take Off and Landing at 10-11 o'clock). Set Gate A to Type 2 (Diode Ladder), Gate B to Type 8 (Comb Filter). Set Filter Routing to Parallel. Select Chorus from Cabin Pressure.

```
[Airplane A Loop mode: slow triangle] [C] → [Gate A X CV: Diode Ladder cutoff]
[Airplane B Loop mode: faster rate]   [C] → [Gate B X CV: Comb Filter center]
[Oscillator or any audio source]       [A] → [Gate A and Gate B inputs]
         │
         ▼
[Cabin Pressure: Chorus, 50% wet]
         │
         ▼
[Stereo Output] [A]
```

Gate A sweeps slowly through the diode ladder's resonant range: the acid filter character rises and falls at its own rate. Gate B sweeps the comb filter's center frequency faster, producing a phasing sweep that moves against Gate A's slower motion. The chorus adds stereo width and slight pitch movement to the output. No external LFO or modulation source is required; the module generates its own modulation internally.

---

### Patch 4: Granular Freeze with Envelope Gate

**What this demonstrates:** Using the Freezer/Looper effect with an Airplane end-of-stage trigger to create gated granular holds.

Load the Darkwaves Bank firmware. Select Freezer/Looper effect. Set Airplane A to Transient (AD) mode with a moderate decay (Landing knob at noon). Route the end-of-Landing trigger from Airplane A to the Cabin Fever CV input.

```
[Gate or trigger source] [G] → [Airplane A Check-In]
[Airplane A unipolar output]  → [Gate A X CV: filter cutoff] [C]
[Airplane A end-of-Landing trigger] → [Cabin Fever CV input: Freezer gate] [G]
[Oscillator or audio source] [A] → [Gate A input]
         │
         ▼
[Cabin Pressure: Freezer/Looper]
[Cabin Pressure knob: freeze playback speed]
[Cabin Fever knob: grain length]
         │
         ▼
[Stereo Output] [A]
```

On each trigger: Airplane A fires, the filter opens and closes through the vactrol or ladder curve. At the moment of the envelope's end-of-Landing trigger, the Freezer/Looper activates and holds whatever audio was present at that instant. The frozen audio plays at the speed and grain length set by the Cabin Pressure and Cabin Fever knobs until the next trigger arrives and the cycle repeats. The result is a performance texture where each note triggers both a live filtered sound and a granular hold of the previous moment.

---

## Common Mistakes

**Patching bipolar CV to the filter X and Y inputs.** The X and Y CV inputs for the filters accept only unipolar voltage from 0V to +5V. An LFO that swings from -5V to +5V will only produce audible filter movement during its positive phase; the negative phase is clamped and has no effect. Either use a source that is naturally unipolar (the Airplane unipolar outputs are ideal) or offset and attenuate a bipolar source to a 0-5V range before connecting it to these inputs.

**Setting the input trim knob to line level for modular-level audio.** The input trim controls the gain of the audio input. When the trim is fully CW (line level setting), a modular-level signal of ±5V is approximately ten times louder than the input stage expects. The result is severe clipping at the filter input before the filter has any effect on the sound. Set the trim CCW for modular-level sources and CW only for true line-level external sources.

**Expecting Gate B's X/Y controls to work in Stereo routing mode.** In Stereo mode, Gate B's X and Y knobs are inactive. Gate A's X and Y control both filters simultaneously. Patching CV to Gate B's X or Y input in Stereo mode has no effect. This is intentional but easy to forget if you switch routing modes mid-patch.

**Missing the unipolar and bipolar Airplane output distinction.** The two outputs per Airplane carry different voltage ranges. Patching the bipolar output (-5V to +5V) to the filter X or Y CV input sends negative voltages during the lower part of the envelope, which are clamped and produce no additional effect. Use the unipolar output (0V to +8V) for filter cutoff modulation, and use the X or Y attenuverter knob to scale it appropriately. Reserve the bipolar output for destinations that benefit from negative CV.

**Adjusting the master volume while in secondary filter mode.** The blue master volume knob affects the Final Out level at all times. If the output seems suddenly louder or quieter during a secondary mode adjustment session, check whether the master volume was accidentally moved.

**Losing filter type and effect settings after a firmware update.** The manual explicitly warns that firmware updates erase stored filter and effect configurations. Before updating firmware, note the current filter type and effect selection for both channels if you want to restore them afterward.

**Using the mono modular output and expecting stereo panning to be audible.** The mono output is the sum of both stereo channels. Any panning set in secondary filter mode affects only the stereo output. The mono output always carries the equal sum of left and right regardless of panning position. If panning decisions matter for the patch, route to the stereo output.
