---
title: Scenes
manufacturer: After Later Audio
primary_role: MODULATOR
secondary_roles: [CONTROLLER]
form_factor: eurorack
functions: [envelope-generator, lfo, step-sequencer, function-generator]
behavior_tags: [evolving, adaptive, performative]
use_cases: [multi-stage envelope, simultaneous-lfo-and-envelope, step-sequencer, per-note-envelope-shaping]
hp: 14
depth: 25mm
memory: none
transport: none
screen: false
hybrid: false
cv: basic
patch_format: v1
---

# After Later Audio Scenes

**Segment generator: configurable envelopes, LFOs, step sequencer, and function generators from a single module**

![After Later Audio Scenes](https://github.com/Shadoe-42/music/raw/main/modular/images/after_later_audio/scenes/front_panel.jpg)

*Scenes is an exact hardware replica of the Mutable Instruments Stages. All technical specifications, behaviors, and firmware are identical. The full Mutable Instruments Stages manual is available at mutable-instruments.net/modules/stages/manual and is the authoritative reference for exhaustive detail. This guide teaches the conceptual model and practical application.*

---

## Historical Context

The ADSR envelope — Attack, Decay, Sustain, Release — was not an inevitable design. It was a practical compromise. Robert Moog's decision in the 1960s to describe amplitude evolution as four phases with four dedicated knobs produced something teachable, standardized, and functional across a wide range of musical applications. The ADSR became the default envelope shape for synthesizers precisely because its simplicity matched what most players needed most of the time.

But the ADSR makes assumptions. It assumes the envelope has a single peak. It assumes that peak happens once per gate event. It assumes the sustain is a fixed voltage rather than itself an evolving shape. Electronic music composition, particularly in the tradition extending from Edgard Varèse through Karlheinz Stockhausen and the composers working at Buchla's San Francisco Tape Music Center, often needed more than four phases. A note that swells, plateaus, dips, swells again, and releases with a secondary echo requires something the ADSR cannot express cleanly.

Don Buchla's response was the arbitrary function generator: a circuit that could be programmed to trace any voltage path over time, not just a fixed attack-sustain-decay-release arc. The resulting envelopes could be complex, asymmetric, multi-peak, or continuously cycling. The limitation was complexity: programming an arbitrary function generator required understanding a more abstract interface than four labeled knobs.

Mutable Instruments Stages, released in 2018, approached the same problem from a different angle. Rather than providing a single complex envelope with many parameters, it provided six simple building blocks called segments. Each segment does one of three things: ramp from one voltage to another, hold a voltage for a duration, or step to a target voltage and wait for a trigger. Combining these segments in sequence produces any envelope shape expressible as a path through voltage over time. The ADSR is four segments arranged in a specific order. A two-peak swell is six segments. A cycling LFO is one segment set to loop. The same hardware generates all of them depending only on how the segments are configured and which gate inputs are patched.

Scenes is After Later Audio's hardware-identical replica of Stages, running the same firmware on the same circuit.

---

## How Scenes Thinks

Before quick start, before parameters, before patches: Scenes requires a conceptual model. Without it, the module's behavior is bewildering. With it, everything follows logically.

**The segment** is the atom. Scenes has six of them, numbered 1 through 6 left to right. Each segment has its own knob (Shape/Time), button, slider (Time/Level), CV input, gate input, and output jack. A segment does exactly one thing: it generates a voltage that changes in one of three ways depending on its type.

**The group** is formed by patching a gate input. When you insert a cable into a gate input, that segment becomes the start of a group. Every unpatched segment to the right of it (within the same module) joins that group automatically. The first output of a group generates the envelope signal: the voltage that traces through all the segments in sequence. The remaining outputs of the group generate segment activity signals — ramps from 8V down to 0V that indicate when each subsequent segment is active.

That is the whole rule. Every behavior of Scenes follows from it.

If no gate inputs are patched: all six segments are independent, free-running. They produce whatever their type and loop setting dictates, without waiting for a gate signal. Six separate LFOs or six separate function generators.

If only gate input 1 is patched: segments 1 through 6 form a single group. One gate drives a six-stage envelope. Output 1 carries the full envelope. Outputs 2 through 6 carry segment activity signals.

If gate inputs 1 and 5 are patched: segments 1-4 form one group (four-stage envelope on output 1), segments 5-6 form a second group (two-stage envelope on output 5). Two independent envelopes, each driven by its own gate, from the same module simultaneously.

If all six gate inputs are patched: six independent single-segment envelopes.

**Patch from right to left.** This is the practical tip the Stages manual offers and it is genuinely useful. If you need a two-segment AD envelope and also want LFOs from the remaining segments, patch the gate into segment 5. Segments 5 and 6 become your envelope; segments 1 through 4 are free for anything else. Starting from the right preserves the left segments as available resources.

---

## Quick Start

1. Start with no cables patched to any gate input.
2. Set the button on segment 1 to RAMP (teal LED, the default).
3. Hold the button on segment 1 for one second until the LED blinks. Segment 1 is now looping.
4. Patch the output jack of segment 1 to a filter cutoff CV input.
5. Set the slider on segment 1 to noon. You should hear the filter sweeping at a moderate rate.
6. Turn the knob on segment 1 to change the LFO waveform. Turn the slider to change the rate.
7. Now patch a gate signal into gate input 6.
8. Set segment 6 to RAMP (teal LED), not looping.
9. Patch the output jack of segment 6 to a VCA CV input. Segment 6 now functions as a decay envelope: each gate produces a single ramp-down. Segment 1 continues as a free-running LFO.

You have just built a two-function patch: a running LFO on one segment and a gate-triggered decay envelope on another, simultaneously, from the same module.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 14 HP |
| Depth | 25 mm |
| Power | 80 mA +12V / 20 mA -12V |
| Price | $279 USD |
| Segments | 6 |
| Chaining | Up to 6 units via 3-pin TX/RX cable |
| Firmware | Mutable Instruments Stages (identical) |

---

## The Three Segment Types

Each segment is set to one of three types by pressing its button. The LED color indicates the current type. Pressing the button cycles through the three options.

### RAMP (Teal LED)

A RAMP segment generates a voltage that moves smoothly from one value to another over a set time. The slider and CV input set the duration. The knob sets the curve shape: counterclockwise is logarithmic (fast initial movement, slow approach to target), center is linear, clockwise is exponential (slow initial movement, fast final approach).

When a RAMP is the first segment in a group, it ramps up toward 8V from the current output voltage. When it is the last segment in a group, it ramps down to 0V. The knob's curve control applies to both directions.

When set to loop on its own as an isolated segment, a RAMP becomes an LFO. The knob now selects from a set of waveforms rather than simply setting curve shape: variable-slope saw/triangle (counterclockwise through center), sine (near center), and variable-slope trapezoid (center through clockwise). The slider sets the frequency when no gate is patched. When a gate is patched to a looping RAMP, the LFO syncs to the gate tempo with a clock division or multiplication factor set by the slider (1/4 to 4x).

A non-looping isolated RAMP is a decay envelope: it ramps down from 8V to 0V once per gate trigger.

### STEP (Orange LED)

A STEP segment glides to a target voltage set by its slider and CV input, holds that voltage, and waits. It does not advance to the next segment until it receives a trigger at its gate input. The knob controls the glide amount from the previous voltage to the target.

A STEP segment within an envelope group pauses the envelope at its target voltage until the next trigger arrives. Multiple STEP segments in sequence create a sequence that advances trigger by trigger, each step gliding to its target and holding until the next push.

An isolated STEP segment with a gate patched works as a sample-and-hold: at each rising gate edge, it captures and holds the voltage at the CV input. The knob sets the glide rate on the captured value.

An isolated STEP segment without a gate patched continuously tracks the slider and CV input with a glide effect set by the knob.

### HOLD (Pink/Red LED)

A HOLD segment stays at a fixed voltage for a set duration before passing control to the next segment. The slider and CV input set the voltage level (0V to 8V). The knob sets the duration of the hold.

A HOLD segment in the middle of an envelope group sets the sustain level and holds it for the duration controlled by the knob, then proceeds to the next segment regardless of gate state. This makes it useful as the S in an ADSR when combined with a loop — see the looping section below.

An isolated HOLD segment with a gate patched functions as a pulse generator: the slider sets the pulse voltage and the knob sets the pulse duration. With looping enabled, the pulse lasts for as long as the gate is high.

An isolated HOLD segment without a gate patched behaves as a CV delay: the voltage set by the slider is sent to the output with a delay set by the knob. This works as a slew-limited CV source even without any external signal.

---

## Looping

Any segment or span of segments can be set to loop. This is the mechanism that turns a RAMP into an LFO, a HOLD into a gate-controlled pulse, and an ADSR decay into a sustain that holds as long as the gate is open.

**Single-segment loop:** Hold the button for one second until the LED blinks. The segment now repeats indefinitely. A looping RAMP with no gate is a free-running LFO. A looping RAMP with a gate syncs to the gate tempo.

**Multi-segment loop:** Simultaneously press the button of the first and last segments of the desired loop range. Both LEDs blink to confirm the loop. The envelope progresses normally until it enters the loop, cycles through the looped segments while the gate is high, then exits the loop and continues to the remaining segments when the gate goes low.

**The sustain mechanism:** A classic ADSR sustain is built with a looping segment. Set segment 3 (the S position) to HOLD, then set it to loop. While the gate remains high, the envelope holds at segment 3's voltage indefinitely. When the gate goes low, the envelope breaks out of the HOLD loop and proceeds to segment 4 (the release RAMP). This is not a continuous sustain at a fixed voltage; it is a looped hold, which means the sustain voltage is controlled by the HOLD slider rather than implied by the attack peak.

**Disabling a loop:** Hold the button of the start or end segment of the loop for one second.

---

## Building Envelopes

The segment rules govern how consecutive segments within a group connect to each other:

The first RAMP in a group ramps up to 8V from the current output level. The last RAMP in a group ramps down to 0V. A HOLD or STEP segment between two RAMPs sets the voltage at which the first RAMP ends and the second RAMP begins. If a RAMP's target level cannot be determined by its neighbors, the knob sets it explicitly.

From these rules, most standard envelope shapes emerge naturally:

AD (two segments, gate input on left): RAMP up, RAMP down.

ADSR (four segments, gate input on left): RAMP up (A), RAMP down to sustain level (D), HOLD looping at sustain voltage (S), RAMP down to 0V (R). The gate breaking the HOLD loop triggers the release.

AHDSR (five segments): RAMP up (A), HOLD for a set duration (H), RAMP down to sustain (D), HOLD looping (S), RAMP down (R). The pre-sustain hold is controlled by segment 2's knob independently of the sustain level.

The segment activity signals on outputs 2 through 6 (within a group) are ramps from 8V to 0V while each segment is active. These can modulate other parameters in sync with specific envelope phases: open a secondary filter only during the attack, apply reverb only during the release, and so on.

---

## Patch Examples

Scenes requires a note before patch examples. Because the module reconfigures based on which gate inputs are patched, each patch begins by specifying the segment layout — which segments are grouped, which are isolated — before describing connections.

### 1. Single LFO from One Segment

A looping RAMP segment with no gate patched runs freely as an LFO, producing a continuously repeating waveform whose shape is controlled by the knob and whose frequency is set by the slider.

**First Voice**

Before adding the LFO, establish a working voice:

```
  Sequencer CV out ──[C]──▶ VCO 1V/OCT
  Sequencer gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  VCO audio out ──[A]──▶ Filter audio in
  Filter audio out ──[A]──▶ VCA audio in ──▶ Mixer
```

Set filter cutoff to minimum. Verify a pitched, gated voice before connecting Scenes.

**Configure Scenes and connect**

Segment layout: all six gate inputs unpatched. Segment 1 in RAMP mode, looping (button held until LED blinks).

```
                    ┌──────────────────────────────────────────┐
                    │ SEGMENT 1: RAMP, looping                  │
                    │ Knob: noon (sine waveform)                 │
                    │ Slider: noon (medium rate)                 │
                    │             OUTPUT 1                       │──[C]──▶ Filter cutoff CV
                    └──────────────────────────────────────────┘
                                   Scenes (segment 1 only)
```

No gate needed. The LFO runs continuously at the rate set by the slider.

- `Output 1 ──[C]──▶ Filter cutoff CV`: the looping RAMP produces a repeating voltage shape; with the knob at noon it is a sine wave. With filter cutoff at minimum, the full LFO sweep opens and closes the filter on each cycle.

**Move the cable**

Leave the LFO running. Unplug the cable from filter cutoff CV and plug it into the VCO's FM or pitch CV input instead.

```
                    ┌──────────────────────────────────────────┐
                    │ SEGMENT 1: RAMP, looping                  │
                    │             OUTPUT 1                       │──[C]──▶ VCO FM in
                    └──────────────────────────────────────────┘
```

What changed: the LFO now modulates pitch rather than timbre. Turn the knob counterclockwise for a triangle/saw waveform for a more abrupt pitch oscillation. The same segment, same rate, same configuration — destination determines musical function.

**What to listen for**

With the LFO on the filter: the filter should open and close smoothly at the LFO rate. Turn the slider up to increase speed; the sweep should accelerate continuously from slow breath to fast tremolo and into audio-rate territory at maximum. Turn the knob from counterclockwise through center to clockwise to move through saw, triangle, sine, and trapezoid shapes. The sine at center should produce the smoothest, most rounded sweep. In the Move, pitch vibrato should be clearly audible. At very slow rates the pitch wanders gently; at fast rates it becomes FM-like coloration.

---

### 2. Simultaneous LFO and Envelope from One Module

Patching a gate into segment 5 creates a two-segment envelope from segments 5 and 6, while leaving segments 1 through 4 as free-running modulation sources.

**First Voice**

```
  Sequencer CV out ──[C]──▶ VCO 1V/OCT
  VCO audio out ──[A]──▶ Filter audio in
  Filter audio out ──[A]──▶ VCA audio in ──▶ Mixer
```

Note: no external EG. Scenes will provide the amplitude envelope.

**Configure Scenes and connect**

Segment layout: gate input 5 patched, gate inputs 1-4 and 6 unpatched. Segments 1-4 isolated and free-running. Segments 5-6 grouped (AD envelope).

Segment 1: RAMP, looping, knob at noon (sine LFO).
Segment 5: RAMP, not looping (attack).
Segment 6: RAMP, not looping (decay).

```
                    ┌──────────────────────────────────────────────┐
                    │ SEGMENT 1: RAMP, looping                      │
                    │ Slider: noon (medium LFO rate)                │
                    │            OUTPUT 1                           │──[C]──▶ Filter cutoff CV
                    └──────────────────────────────────────────────┘
                                   Scenes (segment 1, isolated)

Sequencer gate ──[G]──▶
                    ┌──────────────────────────────────────────────┐
                    │ GATE 5        SEG 5: RAMP (attack)            │
                    │               SEG 6: RAMP (decay)             │
                    │               OUTPUT 5                        │──[C]──▶ VCA CV in
                    └──────────────────────────────────────────────┘
                                   Scenes (segments 5-6 group)
                    Slider 5: short (attack time)
                    Slider 6: medium (decay time)
```

- `Output 1 ──[C]──▶ Filter cutoff CV`: segment 1 runs as an independent LFO regardless of gate events on segment 5; the filter sweeps continuously.
- `Sequencer gate ──[G]──▶ Gate 5`: each gate triggers the two-segment AD envelope; the VCA opens on attack and closes on decay.
- `Output 5 ──[C]──▶ VCA CV in`: the AD envelope controls amplitude. There is no sustain: the VCA begins closing immediately after the attack peak.

**Move the cable**

Change segment 6 from RAMP to HOLD by pressing its button once. The envelope now becomes Attack-Hold: it ramps up on the attack, then holds at 8V for a duration set by segment 6's knob, then drops immediately when the HOLD duration expires.

What changed: the note now sustains at full level for a fixed time set by slider 6, then cuts. This is distinct from a gate-controlled sustain; the hold duration is set by the knob, not by how long the gate is held. Short knob setting produces a staccato gate-cut; long knob setting produces a held note with a specific release point regardless of when the gate closes.

**What to listen for**

The LFO on the filter should be audible between notes as continuous timbral movement. On each note trigger, the amplitude envelope should cause the note to appear with a clear attack and decay. If the filter LFO and the amplitude envelope are at similar rates, they will interact: the filter may be closing as the amplitude peaks, producing a darker note. Misalign the rates intentionally — slow filter LFO, fast amplitude decay — to produce notes that each catch a different moment in the filter sweep. In the Move, each note should have a precise, timer-controlled sustain duration independent of sequencer timing.

---

### 3. Four-Segment ADSR

Patching gate input 1 groups segments 1 through 4 into a four-stage ADSR envelope: Attack (segment 1), Decay (segment 2), Sustain (segment 3, looping HOLD), Release (segment 4).

**First Voice**

```
  Sequencer CV out ──[C]──▶ VCO 1V/OCT
  VCO audio out ──[A]──▶ Filter audio in
  Filter audio out ──[A]──▶ VCA audio in ──▶ Mixer
```

No external EG. Scenes provides the full ADSR.

**Configure Scenes**

Segment layout: gate input 1 patched. Segments 1-4 grouped; segments 5-6 unpatched (available for other use).

- Segment 1: RAMP (attack). Slider sets attack time. Knob sets curve.
- Segment 2: RAMP (decay). Slider sets decay time. Knob sets curve.
- Segment 3: HOLD (sustain). Slider sets sustain voltage. Set to loop (hold button 1 second until LED blinks).
- Segment 4: RAMP (release). Slider sets release time. Knob sets curve.

```
Sequencer gate ──[G]──▶
                    ┌────────────────────────────────────────────────────────┐
                    │ GATE 1    SEG 1: RAMP   SEG 2: RAMP   SEG 3: HOLD(loop)  SEG 4: RAMP │
                    │                                                          OUTPUT 1     │──[C]──▶ VCA CV in
                    └────────────────────────────────────────────────────────┘
                                             Scenes (segments 1-4 group)
```

Use a sequencer such as Hermod+ (or Pamela's Pro Workout) for gate output.

- `Sequencer gate ──[G]──▶ Gate 1`: the gate triggers the envelope group. While the gate is high, the envelope progresses through attack and decay, then loops in the sustain HOLD. When the gate goes low, the HOLD loop is broken and the release RAMP begins.
- `Output 1 ──[C]──▶ VCA CV in`: the first output of the group carries the full ADSR envelope. The VCA opens and closes with the envelope shape.

**Move the cable**

Unplug the envelope from the VCA CV and patch it to the filter cutoff CV instead. Patch a separate EG gate out to the VCA CV to control amplitude independently.

```
                    ┌──────────────────────────────────────────┐
                    │             OUTPUT 1                      │──[C]──▶ Filter cutoff CV
                    └──────────────────────────────────────────┘

Separate EG ──[C]──▶ VCA CV in (simpler AR from external EG)
```

What changed: the complex ADSR now shapes timbre rather than amplitude. The filter opens and closes with a four-stage profile while amplitude is handled separately by a simpler external envelope. The timbral evolution of each note (attack brightness, decay character, sustain brightness level, release tail) is now controlled independently from how loud the note is.

**What to listen for**

The ADSR envelope on the VCA should produce clearly distinguishable attack, decay, sustain, and release phases. Adjust slider 3 (sustain voltage) to set how much the signal level drops after the attack peak; at maximum, the sustain matches the attack peak and the decay has no audible effect. Set slider 4 (release) to a longer time than the note length to hear the release tail. In the Move, the filter sweep should show the ADSR profile as timbral evolution: bright attack, slightly darker decay, held sustain brightness, then gradual filter closure on release. The filter and amplitude behaviors should be independently adjustable.

---

## Essential Parameters

**Segment type button.** Short press cycles through RAMP (teal), STEP (orange), HOLD (red). Long press (1 second) toggles loop on the selected segment; LED blinks to indicate looping. Simultaneous press of two buttons within the same group creates a loop spanning those segments.

**Knob [A] — Shape/Time.** Function depends on segment type. RAMP: curve shape (logarithmic to exponential), or waveform when looping (saw/triangle, sine, trapezoid). STEP: glide amount. HOLD: duration of hold (when independent); waveform is not applicable.

**Slider [C] — Time/Level.** Function depends on segment type and context. RAMP: time/frequency (duration of the ramp, or LFO speed when looping). STEP: target voltage (0V-8V). HOLD: held voltage level (0V-8V); also duration when used as pulse generator. CV input [1] adds to the slider position.

**Gate input.** Patching a gate marks the start of a group. Within a group: rising gate edge triggers the envelope; falling gate edge exits any loop and begins the remaining segments. For looping isolated segments: RAMP — syncs LFO to gate tempo. HOLD — pulse generator (output high for knob-set duration per gate). STEP — sample-and-hold (captures CV on each rising edge).

**Output jacks.** First output of a group: full envelope signal. Subsequent outputs: segment activity signals (8V to 0V while that segment is active). Isolated segments: the function generator output of that segment.

**CV inputs [1].** One per segment. Additive to the slider position. Accepts external CV to voltage-control the slider parameter: rate for RAMP/LFO, level for STEP/HOLD.

**Chaining.** Connect two Scenes modules with the included 3-pin cable (TX to RX, RX to TX). Power off before connecting. Chained modules behave as one larger Scenes with 12 segments. Up to six units can be chained for 36 segments.

---

## Why Scenes Excels

Scenes does not do one thing. It does not do one thing very well and a few adjacent things adequately. It does whatever the combination of patched gate inputs and segment configurations produces, and the range of possible results spans from a single decay envelope to a complex evolving step sequence to six simultaneous LFOs with independent waveforms and rates. The entire range is available from the same 14HP of panel space.

The specific achievement is that this flexibility does not require a menu or screen. The state of the module is visible on the panel: teal LEDs for RAMP segments, orange for STEP, red for HOLD, blinking for looping. Which gate inputs are patched indicates the group structure. The slider positions indicate levels and times. Reading the panel tells you what the module is configured to do without any hidden state. This matters at the rack, under performance conditions, where reconfiguring a patch needs to happen by feel and observation rather than by navigating menus.

The group mechanism in particular deserves attention. The rule is simple — a patched gate starts a group, unpatched segments to its right join the group — but its consequences are not. Moving one cable changes the module from a six-LFO bank to a two-voice envelope system. Patching gate 1 while segments 2-6 are running freely absorbs those segments into a six-stage envelope group. Removing that cable releases them back to independence. The module's identity reconfigures in real time without touching any button or knob.

The segment activity outputs (outputs 2-6 within a multi-segment group) are frequently overlooked but worth developing a practice around. While the first output carries the main envelope, each subsequent output carries a 8V-to-0V ramp timed to its segment's activity. The decay segment's activity output is active only during the decay phase. The sustain segment's activity output is high during sustain. Routing these to secondary destinations produces phase-synchronized modulation: the filter opens only during the attack, the reverb wet level increases only during the release. One gate event produces a coordinated multi-parameter response across the entire signal chain.

---

## Advanced Learning Path

**Self-patching: LFO rate modulated by another segment.** Configure segment 1 as a looping RAMP (LFO). Configure segment 2 as an isolated looping RAMP at a much slower rate. Patch output 2 into CV input 1 of segment 1. The slow LFO from segment 2 continuously modulates the speed of the LFO on segment 1. The rate of segment 1 rises and falls with the cycle of segment 2, producing a continuously evolving modulation rate without any external CV.

**Gate-synced LFO with clock division.** Configure a segment as a looping RAMP. Patch a clock signal (such as from Pamela's Pro Workout) into the gate input. The LFO phase-locks to the clock. The slider then controls the clock division or multiplication ratio (1/4 to 4x). Changing the slider changes the LFO's rhythmic relationship to the master clock without breaking sync. ⚠️ The exact slider positions for each division/multiplication ratio are not labeled; verify by ear with a clock source.

**Step sequencer with external pitch CV.** Configure multiple segments as STEP type with gate input on the leftmost. Patch external pitch CV from a keyboard or MIDI converter into each segment's CV input. On each trigger, the envelope advances to the next STEP, captures the external pitch CV at that moment, and holds it. The sequence advances trigger by trigger, each step holding the incoming pitch when the trigger arrived. External performance input determines the pitch content; the module provides the step-advance mechanism.

**Multi-output phase relationships.** With a four-segment group (gate on segment 1), segments 2, 3, and 4 produce activity outputs. Patch output 2 (decay activity) to a filter. Patch output 3 (sustain activity) to a reverb wet level. Patch output 4 (release activity) to a secondary oscillator level. Each note event now produces a coordinated multi-stage response across several parameters, all driven by one gate and one module.

**Segment activity as trigger source.** The segment activity output transitions from 8V to 0V when the segment becomes active and returns to 0V at the end. This transition can be used as a trigger for other modules: the falling edge at the end of the activity signal triggers a secondary envelope generator, advances a sample-and-hold, or fires a drum voice. A multi-stage envelope becomes a multi-event performance trigger from one gate.

---

## Pairs Well With

**Pamela's Pro Workout (ALM Busy Circuits).** Pamela's multiple clock outputs at different divisions provide gate signals for multiple Scenes gate inputs simultaneously, creating independent envelope timing for each group without needing multiple gate sources. A gate at segment 1 on every beat and a gate at segment 5 every four beats produces a fast-triggered short envelope and a slow-triggered long envelope from the same module.

**MISO (Tiptop Audio).** Segment activity signals (8V-to-0V ramps) may need scaling or inversion before driving destinations that expect a different voltage range or polarity. MISO's attenuverter section scales and inverts segment activity outputs for destinations that need a positive-going signal or a reduced amplitude range.

**Endorphin.es New Godspeed.** The INDEX CV and TIMBRE CV inputs on New Godspeed accept segment activity outputs from Scenes. Routing the decay activity signal to INDEX CV makes FM depth swell during the decay phase only, adding harmonic complexity during the note's fall without affecting the attack or sustain character.

**Endorphin.es Grand Terminal.** The two Airplane envelope inputs accept external CV. Routing a Scenes envelope to the Airplane input modulates the Grand Terminal's own internal envelope response time dynamically. Longer Scenes envelopes slow the Airplane's response; shorter ones speed it up.

**Patching Panda Etna.** Etna's three filter channels each accept independent frequency CV. Routing segment activity outputs to individual channel FREQ inputs applies filter modulation only during specific envelope phases: bright attack on one channel, subdued sustain on another, opening release on a third.

**4ms Percussion Interface + PI Expander.** The PI's Gate Out, triggered by live audio input, drives a Scenes gate input. Acoustic drum hits trigger Scenes envelope groups in real time, allowing live percussion to perform complex synthesizer modulation events rather than simply clocking a sequencer.

---

## Common Mistakes

**Expecting a fixed behavior before patching.** With no gate inputs patched, Scenes outputs whatever each isolated segment's type and loop setting produces. Patching a gate changes the configuration immediately. The module does not have a default mode; it has a current configuration determined by the patch state.

**Forgetting that unpatched segments join the nearest group to their left.** Patching gate 1 absorbs segments 2-6 into a single six-segment group. If you want segments 3-6 to remain independent while segment 1-2 form a group, there is no way to do this with one gate — you would need to patch gate 3 as well, which starts a second group. Understand the group formation rule before assuming segment independence.

**Trying to set sustain level with the knob in HOLD mode.** In a HOLD segment acting as sustain, the slider sets the sustain voltage, not the knob. The knob sets the hold duration in non-looping HOLD mode. For a gate-controlled sustain (sustain lasts as long as gate is high), set the HOLD to loop; the duration knob then controls how long the HOLD cycles before the gate releases it. ⚠️ Verify the interaction between HOLD knob and gate behavior in looping vs. non-looping modes.

**Not using the activity outputs.** The outputs for segments 2-6 within a group are segment activity signals, not duplicate envelope outputs. They carry a different voltage and timing from output 1. Routing all outputs to the same destination as output 1 will produce unexpected results. Use them as independent modulation sources for other parameters.

**Building a loop with a STEP segment inside it.** A loop containing a STEP segment cannot exit until it receives the next trigger to advance past the STEP. If the loop end point is reached but a STEP inside the loop has not been advanced, the loop is effectively infinite. Avoid placing STEP segments inside loops unless the intention is a trigger-advanced loop.

**Removing gate cables without resetting segment configuration.** If a gate cable is removed while the envelope is mid-cycle, the behavior depends on the current segment state. The module does not reset cleanly on cable removal in all cases. ⚠️ Verify behavior when removing gate cables during active envelope cycles.

---

## Extended Firmware Note

A community-developed alternate firmware for Mutable Instruments Stages exists, commonly known as Stages Extended (maintained by user qiemem). It adds features including a slow LFO mode, additional envelope shapes, and additional single-segment behaviors not present in the stock firmware. Since Scenes ships with the stock Mutable Instruments firmware, none of these extended features apply. Users who wish to explore extended capabilities can install the alternate firmware; the process is the same as for the original Stages. This guide covers only stock firmware behavior.

---

## What's Next

Scenes occupies the MODULATOR role at its most compositional: not a single LFO or a single envelope, but a toolkit for building whatever modulation the patch requires. The guides for Pamela's Pro Workout and Hermod+ cover the clock and gate infrastructure that drives Scenes envelope groups in a larger patch context.

The PI guide covers audio-to-gate conversion for feeding Scenes from live percussion. The basics signal chain guide covers how envelope, LFO, and function generator outputs connect to the modules downstream of them in the standard audio and CV path.

The full Mutable Instruments Stages manual at mutable-instruments.net/modules/stages/manual covers exhaustive detail on segment rules, all single-segment behaviors, chaining configuration, and calibration. It is the authoritative reference for everything this guide introduces.

---

*Depth: 25mm. Power: 80mA +12V / 20mA -12V. Exact hardware replica of Mutable Instruments Stages.*
