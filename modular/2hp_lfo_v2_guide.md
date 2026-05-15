---
title: 2hp LFO v2
manufacturer: 2hp
primary_role: MODULATOR
secondary_roles: []
form_factor: eurorack
functions: [lfo]
behavior_tags: [clean, evolving, performance-oriented]
use_cases: [unipolar modulation source, filter cutoff sweep, clock-synced modulation, dual-path modulation]
hp: 2
depth: 42mm
memory: none
transport: none
screen: false
hybrid: false
cv: basic
patch_format: v1
---

# 2hp LFO v2

**Dual-output voltage-controlled LFO with waveform morphing and clock reset**

![2hp LFO v2](https://github.com/Shadoe-42/music/raw/main/modular/images/2hp/lfo/front_panel.jpg)

## Historical Context

The distinction between audio-rate oscillation and sub-audio oscillation was not always a formal design category. Early synthesizers used oscillators for both purposes: an oscillator tuned below 20Hz produces the same kind of voltage as one tuned to 440Hz, just cycling slowly enough to function as a modulation source rather than an audible signal. Buchla's 200 Series included oscillators that spanned both roles without a hard boundary between them. The Minimoog (1970) formalized the dedicated modulation oscillator as a separate circuit: a low-frequency oscillator feeding the pitch and filter cutoff of the audio signal path, producing vibrato and tremolo as controllable performance parameters. That architectural choice, a dedicated oscillator for modulation and separate oscillators for audio, became foundational to virtually every subsequent synthesizer design.

In Eurorack, the LFO is the MODULATOR role in its most direct form. Where an envelope generator produces a voltage that rises and falls once in response to a gate and stops, an LFO produces continuous, repeating voltage movement independent of any triggering event. That ongoing movement is what animates a patch: filter cutoff breathing open and closed, pitch oscillating for vibrato, amplitude pulsing for tremolo, any parameter that becomes more interesting in motion than at rest. The LFO does not generate audio; it generates the change that makes audio interesting over time.

The 2hp module format, introduced around 2016, imposed a specific horizontal constraint: every module fits in 2HP (approximately 10mm wide). The LFO's response to that constraint is to share one RATE knob and one WAVE knob across two simultaneous outputs, each producing a different waveform family. The controls are shared; the outputs are not copies of each other.

---

## Quick Start

The 2hp LFO produces two simultaneous, continuously repeating voltage signals that move up and down at the rate set by the RATE knob. Both outputs are unipolar: they move from 0V to 5V, not from -5V to +5V.

1. Patch the primary output (jack 5, upper output) to a filter cutoff CV input.
2. Set the RANGE toggle to the left position (slow range).
3. Set the RATE knob to noon.
4. Set the WAVE knob to the 9 o'clock position (triangle waveform).
5. Set the filter cutoff knob to its minimum.
6. You should hear the filter opening and closing smoothly at a medium rate.
7. Turn the RATE knob to change the speed. Turn the WAVE knob to change the modulation shape.
8. Patch the secondary output (jack 6, lower output) to a second destination to hear both outputs simultaneously.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 2 HP |
| Depth | 42 mm |
| Power | 40 mA +12V / 6 mA -12V |
| Price | Approx. 88 EUR |

Both outputs are unipolar (0V to 5V). Rate CV and Wave CV inputs are unipolar (0-5V), additive to the knob position.

---

## Unipolar Output: A Design Feature

Most LFO modules output bipolar signals, moving from -5V to +5V and oscillating equally above and below zero. The 2hp LFO outputs a unipolar signal, moving from 0V to 5V. The distinction matters at the rack.

A bipolar LFO connected to a filter cutoff causes the filter to sweep above and below the knob position equally. The knob sets the center point of the sweep. A unipolar LFO connected to the same input causes the filter to sweep upward from the knob position. The knob sets the floor of the sweep, not the center. Set the filter cutoff at minimum, and the LFO sweeps the full range upward. Set it at noon, and the LFO sweeps the upper half of the range only, never closing below noon.

This behavior is predictable and deliberate. The unipolar output means the knob position at the destination defines the minimum state, and the LFO defines how far above that minimum the parameter travels. For filter sweeps, amplitude swells, and pitch ornaments where a one-directional push is the right gesture, a unipolar source does that work directly without requiring an offset or attenuverter to shift a bipolar signal into range.

The Rate CV and Wave CV inputs follow the same principle: both are unipolar (0-5V) and additive to the knob position. CV can push rate faster from the knob setting; it cannot pull it slower. CV can push the waveform position higher from the knob setting; it cannot pull it lower. To voltage-control the full range of either parameter, start the corresponding knob at its minimum.

---

## Waveforms

The WAVE knob selects between four positions, with smooth interpolation between all of them. The primary and secondary outputs produce different waveforms at each position, sharing the same knob.

| WAVE position | Primary output | Secondary output |
|---------------|---------------|------------------|
| 1 (fully counterclockwise) | Cosine | FM Sines |
| 2 | Triangle | Inverted Triangle |
| 3 | Saw | Ramp |
| 4 (fully clockwise) | Square | Stepped Triangle |

The WAVE knob does not switch between these positions; it morphs continuously. Between positions 2 and 3, the primary output gradually transitions from triangle to saw, passing through every blend of the two shapes. The modulation character shifts continuously rather than jumping. Wave CV adds to the knob position and enables voltage-controlled morphing: an envelope applied to Wave CV sweeps through waveform shapes over the note duration, changing the modulation character per gate event without manual intervention.

The primary and secondary pairs are related. At position 2, the primary produces a triangle and the secondary produces an inverted triangle: when one rises, the other falls. At position 3, primary produces a downward sawtooth and secondary produces a rising ramp: complementary slopes from the same cycle. At position 4, primary produces a square and secondary produces a stepped triangle, a triangle wave that advances in discrete voltage steps rather than a continuous slope. At position 1, the primary produces a cosine (a sine wave offset so it starts at its peak) and the secondary produces FM Sines, a more complex oscillating shape with additional peaks and valleys derived from frequency-modulated sine components.

⚠️ The exact slope direction of the Saw and Ramp waveforms (which rises and which falls) is not specified in the manual; verify against your unit.

---

## Rate

The RANGE toggle sets two operating ranges. Left position: 27 seconds per cycle minimum to 20Hz maximum. Right position: 3.3 seconds per cycle minimum to 152Hz maximum. The RATE knob sets the actual speed within the active range. Rate CV (unipolar 0-5V) adds to the knob position.

In the right (fast) range, the upper rate of 152Hz puts the LFO into the lower audio spectrum. At audio rates, the output is no longer a modulation signal in the conventional sense: it becomes an audio frequency oscillator without 1V/octave pitch tracking. Patched to the FM input of an oscillator at these speeds, it produces sidebands and harmonic content rather than slow pitch or filter movement. The fast range supports this use even though the module is not designed as a VCO.

---

## Reset

A trigger or gate at the RESET input returns both outputs simultaneously to the beginning of their waveform cycle. The LFO continues running from that point at its current rate. The RESET input is the synchronization mechanism: sending a clock pulse to RESET forces the LFO cycle to align with the clock event, eliminating the phase drift that a free-running LFO accumulates over time.

With RESET connected to a clock source and the LFO rate set slower than the clock interval, the LFO cycle restarts on every clock pulse before completing a full cycle. The output traces the first portion of the waveform from zero to the reset point, producing a predictable, rhythmically structured sweep rather than a continuous oscillation. The clock controls the phrasing; the waveform and rate control the shape within each phrase.

---

## Patch Examples

### 1. Unipolar Filter Sweep

Routing a unipolar LFO to a filter cutoff with the cutoff knob at minimum produces a one-directional sweep where the knob position defines the floor and the LFO defines how far above that floor the filter travels on each cycle.

**First Voice**

Before connecting the LFO, establish a working voice:

```
  Sequencer CV out ──[C]──▶ VCO 1V/OCT
  Sequencer gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  VCO audio out ──[A]──▶ Filter audio in
  Filter audio out ──[A]──▶ VCA audio in ──▶ Mixer
```

Set the filter cutoff knob to minimum. Verify a gated, pitched voice before connecting the LFO.

**Connect the LFO**

```
                    ┌────────────────────────────────┐
                    │ RATE knob: slow-medium          │
                    │ WAVE knob: position 2 (triangle)│
LFO primary ──[C]──▶│ RATE CV        PRIMARY OUT     │──[C]──▶ Filter cutoff CV
                    └────────────────────────────────┘
                              2hp LFO v2
                    RANGE: left (slow)
```

Use a filter such as Patching Panda Etna (or Endorphin.es Grand Terminal).

- `LFO primary ──[C]──▶ Filter cutoff CV`: the unipolar 0-5V output adds to the cutoff knob position; with the knob at minimum, the LFO sweeps the filter from fully closed to fully open and back, the triangle waveform producing equal opening and closing durations.

**Move the cable**

Unplug the LFO primary from the filter cutoff CV and plug it into the VCA CV input instead. Unplug the EG from VCA CV and leave VCA CV receiving only the LFO.

```
                    ┌────────────────────────────────┐
LFO primary ──[C]──▶│ RATE CV        PRIMARY OUT     │──[C]──▶ VCA CV in
                    └────────────────────────────────┘
                              2hp LFO v2
```

What changed: the LFO now controls amplitude rather than timbre. The unipolar output means the VCA opens fully at the LFO peak and closes completely at 0V, producing a pulsing amplitude envelope. The same 0-5V signal produces a timbral sweep at the filter and an amplitude pulse at the VCA; destination determines musical function.

**What to listen for**

The filter sweep should open and close smoothly, with the closed position clearly audible as silence or near-silence if the cutoff knob is at minimum. The triangle waveform produces a symmetric sweep: equal time opening and closing. Advancing the WAVE knob toward position 3 (saw) makes the opening faster and the closing slower, or the reverse. In the Move, the amplitude pulse should be clearly rhythmic. If the amplitude never fully closes, the VCA CV attenuator is limiting the LFO's range; verify the attenuator is fully open.

---

### 2. Dual-Output Push-Pull Modulation

At WAVE position 2, the primary output produces a triangle and the secondary produces an inverted triangle; routing both simultaneously to complementary destinations creates push-pull modulation where one parameter opens as the other closes.

**First Voice**

```
  Sequencer CV out ──[C]──▶ VCO 1V/OCT
  Sequencer gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  VCO audio out ──[A]──▶ Filter audio in
  Filter audio out ──[A]──▶ VCA audio in ──▶ Mixer
```

Set filter cutoff at minimum. Set VCA CV attenuator at full. Verify a working voice before connecting the LFO.

**Connect both outputs**

```
                    ┌────────────────────────────────────┐
                    │ WAVE: position 2 (triangle/inv tri) │
LFO primary ──[C]──▶│            PRIMARY OUT              │──[C]──▶ Filter cutoff CV
LFO secondary──[C]──▶│           SECONDARY OUT            │──[C]──▶ VCA CV in
                    └────────────────────────────────────┘
                                  2hp LFO v2
                    RANGE: left. Rate: medium.
```

Both cables come from the same module at the same rate; both are unipolar. Set the WAVE knob to position 2.

- `LFO primary ──[C]──▶ Filter cutoff CV`: as the primary triangle rises, the filter opens, adding harmonic content to the signal.
- `LFO secondary ──[C]──▶ VCA CV`: the inverted triangle falls as the primary rises; amplitude decreases as the filter opens, and amplitude rises as the filter closes. The two parameters move in opposite directions from the same LFO cycle.

**What to listen for**

The sound should shift between two complementary states: bright and quiet when the filter is open and the VCA is low, dark and loud when the filter is closed and the VCA is high. If both parameters seem to move in the same direction, verify the secondary output is connected rather than a second cable from the primary. If the effect is subtle, increase the rate CV destination's attenuator depth. Advancing the WAVE knob through position 3 toward 4 changes the shape of the push-pull from smooth rotation (triangle) toward rhythmic alternation (square and stepped triangle).

---

### 3. Clock-Synchronized Sweep

Patching a clock trigger into RESET forces the LFO cycle to restart at every clock pulse, converting a free-running oscillator into a rhythmically structured modulation source whose phase is always aligned with the pattern.

**First Voice**

```
  Sequencer CV out ──[C]──▶ VCO 1V/OCT
  Sequencer gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  VCO audio out ──[A]──▶ Filter audio in
  Filter audio out ──[A]──▶ VCA audio in ──▶ Mixer
```

Verify the voice is working before connecting the LFO.

**Add clock reset and filter modulation**

```
                    ┌─────────────────────────────────────┐
Clock ──[G]──▶      │ RESET          PRIMARY OUT           │──[C]──▶ Filter cutoff CV
                    └─────────────────────────────────────┘
                                2hp LFO v2
                    WAVE: position 3 (saw). RANGE: left.
                    Rate: set so one cycle is longer than the clock interval.
```

Use a clock such as Pamela's Pro Workout (or Hermod+). Set the LFO rate so one full cycle takes slightly longer than the time between clock pulses.

- `Clock ──[G]──▶ RESET`: each clock pulse returns the LFO to the start of its waveform cycle before it completes; the filter sweep always begins from the minimum position on each clock event, making the modulation rhythmically structured rather than free-running.
- `LFO primary ──[C]──▶ Filter cutoff CV`: the saw waveform traces an asymmetric arc before the reset cuts it; the reset point determines the maximum the filter reaches on each clock step, which changes if the rate is adjusted while the clock runs.

**Move the cable**

Advance the WAVE knob from position 3 (saw) to position 4 (square).

What changed: the square wave produces a binary state rather than a sweep. The filter snaps fully open at the LFO high state and closes at the LFO low state. The RESET now resets a gate rather than a ramp, producing rhythmic on/off filter gating aligned to the clock rather than a swept filter that resets. The same RESET behavior, a different waveform, produces a fundamentally different modulation character.

**What to listen for**

With the saw waveform and RESET active, each clock pulse should produce a sweep that starts from the filter's minimum position and rises toward its maximum before the next reset. If the sweep reaches maximum before the reset, shorten the LFO cycle (increase rate) until the reset cuts it off before completion. In the Move, the filter should snap between open and closed states in clear rhythm with the clock. If the filter seems to close randomly rather than on clock pulses, verify the clock is sending a trigger signal within the RESET input's accepted voltage range.

---

## Essential Parameters

**RANGE toggle.** Left: 27 second cycle to 20Hz. Right: 3.3 second cycle to 152Hz. Sets the operating range for the RATE knob. The fast range reaches into the lower audio spectrum; at those speeds the output functions as an audio-rate oscillator rather than a modulation source.

**RESET input.** Trigger input. Returns both outputs to the beginning of their waveform cycle simultaneously. Used to synchronize LFO phase with an external clock. Does not affect rate or waveform; only resets position in the cycle.

**RATE knob and Rate CV.** The knob sets the cycle speed within the active RANGE. Rate CV (unipolar 0-5V) adds to the knob position; it can increase rate above the knob setting but cannot decrease it below.

**WAVE knob and Wave CV.** Selects and morphs between four waveform positions. Interpolation is continuous: any position between the four labeled points produces a blend of the adjacent waveforms. Wave CV (unipolar 0-5V) adds to the knob position; set the knob at minimum to voltage-control the full waveform range.

**Primary output (jack 5).** 0-5V unipolar. Waveforms: Cosine, Triangle, Saw, Square at positions 1-4. LED brightness corresponds to output voltage.

**Secondary output (jack 6).** 0-5V unipolar. Waveforms: FM Sines, Inverted Triangle, Ramp, Stepped Triangle at positions 1-4. LED brightness corresponds to output voltage. Not a copy of the primary output; produces a different waveform family at each WAVE position.

---

## Why 2hp LFO v2 Excels

The 2hp LFO's unipolar output is a considered design decision rather than a constraint. A unipolar source (0-5V) defines a floor at the destination: set the destination's knob and the LFO pushes the parameter above it, never below. For filter sweeps, amplitude pulses, and pitch ornaments where the modulation is always additive relative to the resting position, unipolar behavior is direct and predictable. There is no need to offset a bipolar signal into range; the knob position at the destination handles that. In a small system or a dense patch, fewer utility modules between the LFO and its destination is a real advantage.

The wave morphing distinguishes the LFO from simpler alternatives. The WAVE knob does not switch between waveforms with a click or detent; it blends between them continuously. Between triangle and saw, the modulation shape has a faster rise than fall or a faster fall than rise, depending on position. Applied through Wave CV from an envelope, the waveform shape changes per note, so the character of a filter sweep or an amplitude pulse evolves over the course of a gate event without any manual intervention. That is a more complex modulation result than rate alone can produce.

The dual-output architecture with paired but different waveforms means two complementary modulation signals from one 2HP module at one rate. The primary triangle and secondary inverted triangle at position 2 create push-pull behavior across two destinations simultaneously. The primary square and secondary stepped triangle at position 4 create binary gating on one destination and a rhythmic staircase on another. One module occupying the smallest practical panel width produces a two-channel modulation result that would otherwise require two separate modules and an attenuverter to manage their phase relationship.

At 2HP, it fits. In a small system where every horizontal pitch is contested, a full-featured LFO with dual outputs, wave morphing, rate CV, wave CV, and clock sync fits in the space most modules give to a single label.

---

## Advanced Learning Path

**Wave CV automation for per-note waveform character.** Set the WAVE knob at minimum. Patch an envelope into the Wave CV input. As the envelope rises on each gate event, the waveform morphs from cosine toward square on the primary output, changing the modulation character from smooth to hard-edged over the note duration. Adjusting the envelope time changes how quickly the waveform hardens. The result is a filter or amplitude sweep whose shape evolves dynamically rather than repeating identically on every note.

**Audio-rate FM with the fast range.** Switch RANGE to the right position. Increase RATE toward maximum. Patch the primary output to the FM or linear FM input of an oscillator. At rates above 20Hz, the LFO output becomes an audio-rate FM operator: it imposes sidebands on the target oscillator's spectrum whose position and spacing depend on the LFO frequency and waveform. At moderate depths, this adds harmonic content; at high depths, it produces inharmonic spectra. Rate CV at audio rates shifts the FM operator pitch, changing the sideband pattern in real time.

**Self-modulation: LFO rate controlled by its own secondary output.** Patch the secondary output to the Rate CV input. The LFO's secondary waveform then modulates its own rate. With the inverted triangle on secondary (position 2), the rate increases as the primary triangle falls and slows as it rises, producing a cycle that accelerates and decelerates within each period. The character of the self-modulation depends entirely on which waveform pair is active; stepped triangle into rate CV at position 4 produces a quantized sequence of rate changes.

**Polyrhythmic phase drift with periodic RESET.** Run the LFO at a rate that does not divide evenly into the master clock, and RESET only on every fourth or eighth clock pulse rather than every pulse. The LFO drifts in phase relative to the pattern between resets, producing gradual modulation evolution, and then snaps back to alignment at the reset point. The length between resets determines how far the phase drifts and how dramatic the snap-back is.

**Push-pull with rate offset using two LFO modules.** Two 2hp LFOs at slightly different rates but with their WAVE knobs at position 2 (triangle and inverted triangle respectively) produce push-pull modulation that gradually drifts in and out of phase. The rate difference creates a slow envelope over the push-pull relationship; at some points both move in unison before diverging again. RESET both LFOs from the same clock to periodically realign them.

---

## Pairs Well With

**Patching Panda Etna.** Three filter channels with individual FREQ CV inputs and a FREQ ALL CV input accept both the primary and secondary LFO outputs simultaneously. Routing primary to FREQ ALL and secondary to a single channel FREQ CV creates global sweeping with independent additional modulation on one filter voice.

**Endorphin.es Grand Terminal.** The two Airplane envelope CV inputs and the Gate A and Gate B X CV inputs provide multiple modulation destinations. A slow LFO sweep on one Airplane's response time changes how the filter's internal envelope behaves over time rather than directly modulating frequency.

**Endorphin.es New Godspeed.** The INDEX CV input accepts external modulation for FM depth. Routing LFO primary to INDEX CV and Wave CV from a slow secondary LFO (using a second module) creates evolving FM depth modulation that changes waveform character simultaneously.

**Pamela's Pro Workout (ALM Busy Circuits).** Multiple clock outputs from Pamela at different subdivisions provide RESET signals at different rhythmic rates. Switching the RESET source between Pamela outputs changes the phrase length of the synchronized sweep without touching the LFO controls.

**MISO (Tiptop Audio).** The MISO's attenuverter and offset section conditions the unipolar 0-5V output for destinations that expect a different voltage range. Scaling the 0-5V to 0-3V limits the modulation depth; adding a negative offset shifts the unipolar range toward bipolar territory for destinations that respond better to voltages centered on zero.

**Erica Synths Pico Quant.** Routing the LFO primary output through a quantizer before a pitch destination converts the smooth wave morphing into stepped pitch sequences. The waveform shape determines the pattern of pitch steps; triangle produces an up-down sequence, saw produces a staircase in one direction, and stepped triangle already produces discrete steps before quantization adds scale correction.

---

## Common Mistakes

**Expecting bipolar range from the outputs.** The primary and secondary outputs both run from 0V to 5V. If a destination expects a bipolar signal centered on 0V (common for pitch CV summing), the LFO will offset the pitch upward rather than adding vibrato around the original pitch. For pitch vibrato, route through an attenuverter and add a negative offset to center the modulation, or use the LFO for destinations where one-directional modulation is the goal.

**Rate CV cannot slow below the knob setting.** The Rate CV input is unipolar and additive. A CV of 0V changes nothing; a CV of 5V pushes the rate to its maximum from the knob position. To slow the rate via CV, start the RATE knob near minimum. Expecting CV to pull the rate slower than the knob setting will not work.

**Wave CV has the same unipolar limit.** The WAVE CV input works identically to Rate CV: it adds to the knob position. To voltage-control the waveform from position 1 through position 4, set the WAVE knob to minimum. With the knob at noon, Wave CV can only push toward position 4; the lower half of the waveform range is inaccessible via CV.

**RESET restarts the phase but does not lock the rate.** RESET does not make the LFO tempo-syncable in the traditional sense. It resets the cycle position at each trigger. If the LFO rate and the clock rate are not related by a consistent ratio, each reset will restart the cycle at different points in the musical phrase, producing irregular modulation rather than consistent rhythmic alignment. Set the LFO rate intentionally relative to the clock interval before engaging RESET.

**Secondary output waveforms are not copies of the primary.** Both outputs share the WAVE knob, but they produce different waveforms at every position. Expecting the same modulation shape on both channels and connecting them to the same destination type will produce different results per channel. Use the pairing intentionally: the relationship between primary and secondary at each WAVE position is the module's dual-output design logic.

---

## What's Next

The 2hp LFO introduces the core MODULATOR role: a continuously running voltage source that animates other parameters over time. Once the basic connections are established, the next useful concept is how to control the rate and depth of that modulation to serve the musical phrase rather than run independently of it.

The guides for Pamela's Pro Workout and Hermod+ cover clock generation and distribution, which provides the RESET source that converts a free-running LFO into a rhythmically organized modulation tool. The MISO guide covers attenuversion and offset, which conditions the unipolar LFO output for destinations with different voltage expectations.

---

*Depth: 42mm. Power: 40mA +12V / 6mA -12V.*
