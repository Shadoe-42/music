---
title: Xaoc Devices Zadar + NIN
manufacturer: Xaoc Devices
primary_role: MODULATOR
secondary_roles: []
form_factor: eurorack
functions: [function-generator]
behavior_tags: [free-running, gated, evolving, nonlinear, generative, performance-oriented]
use_cases: [envelope shaping, modulation source, generative CV source, stochastic modulation]
hp: 10
memory: full
screen: true
historical_context: false
---

# Xaoc Devices Zadar & NIN Guide

**Quadruple Envelope Generator & Expander**  
**Manufacturer:** Xaoc Devices  
**Format:** Eurorack  
**Zadar:** 10HP | **Depth:** 31mm | **Power:** +50mA / -15mA  
**NIN:** 3HP | **Depth:** 31mm | **Power:** drawn from Zadar  
**Manual revision:** 1973/2.4

![Xaoc Devices Zadar](https://github.com/Shadoe-42/music/raw/main/modular/images/xaoc/zadar/front_panel.jpg)  
*10HP quadruple envelope generator with 270 vector shapes, two-dimensional deformation, chain and loop algorithms, and assignable CV. NIN expander adds manual triggers and a second CV layer.*

---

## Quick Start: First Sound in 5 Minutes
| Spec | Zadar | NIN |
|------|-------|-----|
| Width | 10HP | 3HP |
| Depth | 31mm | 31mm |
| Power | +50mA / -15mA | Drawn from Zadar |
| Channels | 4 (A, B, C, D) | N/A |
| Output voltage | 0–10V unipolar | N/A |
| TRIG input threshold | 1V | N/A |
| ASGN input range | -10V to +10V | N/A |
| ASGN2 input range | N/A | -10V to +10V |
| Shapes | 270 (27 banks × 10) | N/A |
| Time range | 0.85ms to 1800s (30 min) | N/A |
| Preset slots | 18 | N/A |

---

## What Is an Envelope Generator?

When a synthesizer voice plays a note, the sound does not simply appear at full volume and disappear cleanly. In nature, sounds have shape; a piano key has a sharp attack and a long decay; a bowed string swells gradually; a plucked instrument peaks quickly and fades. An envelope generator creates a control voltage that mimics this kind of shape over time. That voltage can then control amplitude, filter brightness, pitch, or any other parameter that accepts a CV input.

The traditional envelope model is called ADSR: Attack (how fast the voltage rises after a trigger), Decay (how fast it falls from peak toward sustain), Sustain (the level held while a gate is open), and Release (how fast it falls to zero after the gate closes). ADSR is useful and widely understood, but it describes only one family of shapes.

Zadar approaches the problem differently and more radically. Rather than building an envelope from four adjustable segments, it stores 270 complete shapes (pre-defined voltage trajectories made from vector curves) and gives you tools to stretch, warp, and deform them in real time. The entire shape is the envelope. You are not assembling it from parts; you are selecting and sculpting an existing form.

---

## Zadar's Approach: Vector Shapes

Each of Zadar's 270 shapes is a vector curve built from 3 to 1,000 breakpoints. The synthesis engine interpolates between those breakpoints in real time, which means the shapes scale perfectly to any duration, from a fraction of a millisecond to thirty minutes, without the jagged artifacts that would result from simple sample playback. Like vector graphics, these envelopes have infinite resolution regardless of how far you stretch or compress them in time.

The 270 shapes are organized into 27 banks of 10, labeled A through Z plus a default. Banks A through W are Xaoc's own shapes, ranging from simple rise-fall curves in Bank A to dense, multi-peaked organic forms in the later banks. The final three banks are artist signatures: Bank X (Septic Series by Shackleton), Bank Y (Inflections by Scanner), and Bank Z (Glitch & Hold by Richard Devine). The character of those three banks tells you something about the module's intended range; these are not gentle ADSR variations but complex rhythmic transients, micro-modulation textures, and controlled chaos.

The shapes chart shows all 270 at a glance. The visual spread (from a single clean peak to something that looks like a dense noise burst) illustrates what Zadar actually is: not an envelope generator that replaces ADSR, but a voltage shape library with deformation tools. Browsing the chart before patching is worthwhile.

**Two-dimensional deformation:** Once a shape is selected, WARP and RESPONSE allow real-time manipulation in two independent dimensions. WARP skews breakpoints along the time axis; compressing or expanding different parts of the shape's duration without changing the overall cycle length. RESPONSE bends the shape along the amplitude axis; inflating or deflating the vertical dimension of the curve. At moderate settings these are subtle adjustments; at maximum, they can radically alter a shape from its starting point.

---

## Panel Layout and Navigation

Zadar has four identical channels: A, B, C, D; each with its own TRIG input, ASGN input, and OUT jack. The channels share a single set of four encoders and one OLED display. This is the same navigational challenge as any multi-channel module with a shared interface: you are always working in one channel at a time.

**Controls:**

The **CHANNEL button** (blue, top right) cycles through which channel is currently being edited. The active channel's name is shown in the bottom right of the display. Check the display before turning any encoder.

The **four encoders** each have a dual function toggled by pressing:
- **SHAPE/REV**: turn to select shape and bank; push to reverse the shape
- **RTG/TIME**: turn to set duration; push to cycle through retrigger modes (DG / AN / NR)
- **WARP/RSP**: turn to adjust; push to toggle between WARP and RESPONSE
- **SUS/LEVEL**: turn to adjust; push to toggle between SUSTAIN and LEVEL

The **MENU button** (red, center) cycles through three menu pages: CV input assignments, chain and loop settings, and preset management. With NIN installed, a fourth page appears for the second CV assignments. Press MENU repeatedly to return to the main screen.

The **OLED display** shows the current shape, all active parameter values, and indicators for CHAIN, REPEAT, PHASE, and retrigger mode. The screen turns off after 10 minutes of inactivity; push or turn anything to wake it.

---

## Essential Parameters (The Channel Controls)
### Shape Selection

Turn the SHAPE/REV encoder to scroll through the 270 shapes. The bank letter and shape number are visible on screen during selection. Push the encoder to reverse the shape; useful for turning a sharp attack with a slow decay into a slow attack with a sharp decay.

### TIME: Duration

Turn the RTG/TIME encoder to set how long one complete cycle takes, from 0.85 milliseconds to 1,800 seconds (30 minutes). The exact millisecond value is shown while adjusting; an approximate percentage is shown in smaller text. The time range is not an accident: Zadar is equally capable of snappy percussive transients, conventional note envelopes, slow filter sweeps, and hour-scale generative shapes that evolve imperceptibly.

### Retrigger Modes

Push the RTG/TIME encoder to cycle between three behaviors when a new trigger arrives while the envelope is already playing:

| Mode | Behavior |
|------|----------|
| DG (Digital) | Restarts immediately from 0V; clean, precise, no memory of previous state |
| AN (Analog) | Restarts from the current output voltage; no click, natural feel, retains continuity |
| NR (No Retrigger) | Ignores incoming triggers while playing; completes the current cycle first |

The musical difference between DG and AN is audible. DG produces a sharp restart on every retrigger; AN produces a smooth continuation, as though the envelope picked up where it was and began again from there. NR is useful when a pattern is firing triggers faster than the envelope's duration, and you want the envelope to run its full course uninterrupted.

### WARP: Temporal Deformation

With WARP/RSP set to WARP, the encoder skews the shape's breakpoints along the time axis. A positive WARP value compresses the early portion of the shape and expands the later portion; the attack sharpens and the decay stretches. A negative WARP does the opposite. The overall cycle duration does not change; only the internal time distribution shifts.

### RESPONSE: Amplitude Deformation

With WARP/RSP set to RSP, the encoder bends the shape along the amplitude axis. Think of it as inflating or deflating the vertical dimension; a shape that peaked gently becomes more pronounced, or more compressed. RESPONSE adapts a shape to the response curve of the downstream module, such as matching the nonlinear response of a VCA.

### SUSTAIN: Hold Point Within the Shape

This parameter is different from traditional ADSR sustain and is worth understanding carefully.

In a standard ADSR envelope, the sustain stage is a voltage level; the envelope holds at that level as long as the gate is open. In Zadar, SUSTAIN is a *position within the shape*; a point in the envelope's trajectory where playback pauses while the gate is high. When the gate closes, the envelope resumes from that exact position and completes its remaining journey to the end.

The display shows a vertical dashed line marking the sustain position. Move it to any point in the shape to define where the pause occurs. To disable sustain entirely, move the position to the very end of the shape until the display reads OFF. Reversing the envelope does not move the sustain position; it remains at the same relative point in the shape.

### LEVEL: Amplitude Scaling

With SUS/LEVEL set to LEVEL, the encoder scales the output from 10V down to 10mV. This attenuates the envelope without changing its shape; useful for dialing in exactly how much voltage a destination module should receive.

### REPEAT: Looping

REPEAT defines how many times the envelope cycles after its first completion. At 0, it plays once and stops. At values 1–100, it repeats that many times. At ∞, it loops indefinitely.

At REPEAT ∞, Zadar's output becomes a continuous looping waveform; effectively a complex LFO. No trigger is needed to keep it running. The shape, TIME, WARP, and RESPONSE settings all apply, making this a highly flexible modulation source with a waveform library of 270 shapes.

---

## Output Voltage: 0–10V Unipolar

Zadar's outputs are unipolar; they always produce positive voltage between 0V and 10V. They never go negative. This is different from bipolar CV sources, where the voltage swings above and below zero (typically -5V to +5V).

Understanding the distinction matters for patching. Unipolar 0–10V works naturally for parameters that are always positive: VCA amplitude, filter cutoff, panning position; where a 0V means "minimum" and 10V means "maximum." It does not produce negative modulation without additional processing.

This characteristic is also an asset. Modules designed around positive-only CV, such as the SOMA Labs Pulsar-23, work directly and intuitively with Zadar's outputs without offset adjustment. If bipolar modulation is needed (for example, CV-controlling pitch with equal up and down sweep), run Zadar's output through an attenuverter or offset module to shift the range.

---

## CV Assignments (ASGN Inputs)

Each ASGN socket accepts -10V to +10V and can be routed to any of ten parameters on its channel. Assignments are made on the first menu page (press MENU once). On the CV assignment screen, push the corresponding channel encoder to select a destination parameter, then turn to set the attenuation level and polarity.

| Target | Parameter Controlled |
|--------|---------------------|
| SHP | Shape selection |
| TIM | Duration |
| WRP | Temporal warp |
| RSP | Response (amplitude bend) |
| LVL | Output level |
| REP | Number of repeats |
| PHS | Phase shift |
| REV | Shape reversal (binary) |
| SUS | Sustain point position |
| FRZ | Freeze envelope state (binary) |

REV and FRZ behave differently from the others; they respond to CV in a binary, comparator-like way. When the incoming voltage exceeds the set threshold, REV reverses the shape relative to the current panel setting; FRZ pauses the envelope and holds its current output voltage until the CV drops below threshold. These are performance and modulation tools that respond to gates and triggers as much as continuous CV.

CV control of SHP (shape selection) is particularly powerful: a slow LFO or sequence sweeping through shape values cycles through the entire bank, morphing the envelope character continuously.

---

## Chaining

Zadar's four channels can be combined into chains; sequences where one envelope triggers the next, or loops where the chain cycles continuously. This transforms four independent envelopes into a single multi-stage modulation structure of any complexity.

Chain settings are on the second menu page (press MENU twice). The chain algorithm is selected with the A encoder; there are 16 algorithms covering two-channel splits, three- and four-channel sequences, and looped versions of each. When a channel is chained to a previous one, its TRIG input becomes inactive; it receives its trigger internally from the preceding channel's completion.

**PHASE** defines when the chained envelope starts, expressed as a percentage of the preceding envelope's cycle:
- 0%: both start simultaneously
- 100%: the next starts exactly when the previous ends (sequential)
- 50%: the next starts at the halfway point of the previous
- Any value in between creates overlap or delay

**REPEAT** within a chain defines how many times a channel repeats before handing off to the next. Infinite repeat is disabled within looped chains.

**Important:** When a looped chain algorithm is selected, at least one PHASE value must be set to greater than zero for the loop to function correctly.

### Patch Example: Two-Channel Sequential Envelope

Channels A and B chained sequentially, each controlling a different destination:

```
┌──────────────────────────────────────────────┐
│             Xaoc Devices Zadar               │
│                                              │
│  TRIG A ◁──[G]────────────────── Gate source │
│   OUT A ○──[C]────────────────▶ VCA CV in    │
│   OUT B ○──[C]────────────────▶ VCF cutoff   │
└──────────────────────────────────────────────┘
```

Chain algorithm: A→B, PHASE 100% (B starts when A ends). OUT A handles amplitude; OUT B handles filter. The note blooms in amplitude first, then the filter opens on a different trajectory after the amplitude has settled. Both shapes, times, and WARP settings are independent.

### Patch Example: Looped Modulation Chain

All four channels in a looped chain, all outputs summed into a complex evolving LFO:

```
┌──────────────────────────────────────────────┐
│             Xaoc Devices Zadar               │
│                                              │
│   OUT A ○──[C]────────────────▶ Mixer in 1   │
│   OUT B ○──[C]────────────────▶ Mixer in 2   │
│   OUT C ○──[C]────────────────▶ Mixer in 3   │
│   OUT D ○──[C]────────────────▶ Mixer in 4   │
│                                              │
│              Mixer out ──[C]──▶ VCF CV in    │
└──────────────────────────────────────────────┘
```

Algorithm: A→B→C→D looped. PHASE on each channel set to 25% (each starts at quarter-cycle of the previous, creating constant forward movement). Each channel has a different shape and duration. The mixed result is a continuously evolving modulation voltage with no repeating cycle.

---

## Preset Management

Zadar stores 18 complete preset slots, each saving all channel settings across the module. Presets are managed on the third menu page (press MENU three times). The A encoder navigates between slots; pushing it opens the operations menu: SAVE, LOAD, CLEAR, and DEFAULT PRESET.

The default preset is recalled automatically on power-up. Zadar does not auto-save edited settings; if you want changes to persist, save them before powering down.

**Quick Save:** Hold the MENU button until MENU and CHANNEL flash once. This saves the current state to the default preset slot immediately, without navigating the menu.

**Channel Copy:** Hold the CHANNEL button to open the copy menu. The current channel's settings can be pasted to any individual channel or to all channels at once. Useful for building multi-channel patches from a single starting configuration.

---

## NIN Expander

![Xaoc Devices NIN Expander](https://github.com/Shadoe-42/music/raw/main/modular/images/xaoc/zadar/nin_exp_panel.jpg)

NIN is a 3HP expander that mounts directly adjacent to Zadar and connects to the expansion header on Zadar's PCB rear via a ribbon cable. It draws all power through Zadar: NIN has no power connector and must never be plugged into the bus board.

**Installation warning:** The expansion header and the power connector on Zadar's PCB rear are separate connectors in different locations. Confusing them and connecting NIN to a powered bus board will damage the module and void the warranty. Pre-2019 Zadar units require a firmware update to revision 2.0 before NIN will function.

**What NIN adds:**

**Manual trigger buttons (A, B, C, D):** Four tactile buttons that send a gate signal to their respective Zadar channel while held. Tap for a trigger; press and hold for a sustained gate. During patch building, these buttons remove the need for a patched trigger source entirely; you can audition shapes, dial in TIME and WARP, and hear how an envelope opens a filter or drives a VCA without committing to a clock or sequencer connection first. This also means REPEAT ∞ is not necessary just to hear a shape continuously; holding a NIN button achieves the same sustained result while keeping the channel in single-cycle mode.

**ASGN2 inputs (A, B, C, D):** A second set of assignable CV inputs, one per channel, accepting -10V to +10V. With NIN installed, Zadar gains a fourth menu page for ASGN2 assignment; using the same 10-target system as the primary ASGN inputs. The result is up to two simultaneously CV-controlled parameters per channel, enabling modulation of both shape and duration, or warp and level, at the same time from independent sources.

---

## Why This Instrument Excels

Most envelope generators give you four parameters (attack, decay, sustain, release) and a linear or exponential response curve. Zadar gives you any curve drawn from hundreds of pre-defined vector shapes, independent duration scaling, and output polarity control -- per channel, four channels simultaneously, each capable of looping or single-shot behavior. The conceptual distance from an ADSR to Zadar is larger than it first appears.

**Vector shapes cover the full range of envelope behavior in one module.** A standard ADSR can produce slow attacks and fast decays or fast attacks and slow decays, but the shape of the transition is always a fixed curve. Zadar's 100+ shapes include rising and falling exponential curves, S-curves, staircase functions, oscillating shapes, and waveforms that have no analog equivalent in standard envelope design. Selecting shape 1 versus shape 43 is not an aesthetic choice; it is a fundamentally different relationship between the trigger and whatever the envelope is controlling. A shape that rises in steps rather than a smooth curve produces a distinctly different filter opening than a smooth exponential, even at identical TIME settings.

**WARP scales the shape non-linearly without changing the shape selection.** WARP adjusts the distribution of time within the current shape: fully CCW compresses all the shape activity to the beginning of the envelope duration; fully CW stretches it to the end. A shape that normally rises quickly and falls slowly becomes, with WARP fully CW, one that barely moves for most of its duration then rises and falls abruptly at the end. Shape selection and WARP together create a two-dimensional space of envelope behavior that a single ADSR cannot address.

**Four independent channels in 10HP.** Each channel has its own TIME, WARP, SHAPE, LEVEL, LOOP, and REPEAT controls. Four Zadar channels can simultaneously serve as: amplitude envelope on a VCA, filter envelope on a VCF, pitch envelope on a VCO, and a slowly looping LFO for vibrato -- all from the same module. That would require a dedicated module for each function in a traditional rack.

**The NIN expander turns four channels into a performance instrument.** Without NIN, Zadar channels need patched gate signals to trigger. With NIN, four manual buttons (one per channel) allow immediate auditioning and triggering without any patching, plus a second set of CV assignment inputs per channel. During patch building, the NIN buttons eliminate the need for a separate trigger source while experimenting with shapes. During performance, they allow direct manual control of individual envelopes as expressive gestures.

---

## Patch Examples

### Patch 1: Single Channel Envelope for VCA

The most direct use: one channel triggered by a gate, output controlling a VCA's amplitude.

```
┌──────────────────────────────────────────────┐
│             Xaoc Devices Zadar               │
│                                              │
│  TRIG A ◁──[G]────────────────── Gate source │
│   OUT A ○──[C]────────────────▶ VCA CV in    │
└──────────────────────────────────────────────┘
```

| Parameter | Setting | Notes |
|-----------|---------|-------|
| Shape | Bank A, shape 1 | Simple rise-fall; start here |
| TIME | 200–800ms | Match to note length |
| Retrigger | AN | Smooth restarts on rapid notes |
| SUSTAIN | Set to peak | Holds at maximum while gate is open |
| LEVEL | 100% | Full 10V output |

**Try:** Switch to Bank U shape 1 for a sharper percussive transient. Adjust WARP to skew the attack steeper.

---

### Patch 2: LFO Mode: Two Independent Modulators

REPEAT set to ∞ on two channels, both running without triggers, providing continuous modulation on different destinations at different rates.

```
┌──────────────────────────────────────────────┐
│             Xaoc Devices Zadar               │
│                                              │
│   OUT B ○──[C]────────────────▶ VCF cutoff   │
│   OUT C ○──[C]────────────────▶ VCO PWM in   │
└──────────────────────────────────────────────┘
```

| Channel | Shape | TIME | REPEAT | Notes |
|---------|-------|------|--------|-------|
| B | Bank J, shape 1 (bell curve) | 4–8s | ∞ | Slow filter sweep |
| C | Bank A, shape 3 (sawtooth-like) | 500ms | ∞ | Faster PWM modulation |

No TRIG patching required. Both channels run continuously from power-up. The two rates create a slowly evolving relationship between filter brightness and timbre.

---

### Patch 3: Chained Envelope: Amplitude and Filter in Sequence

Channel A controls amplitude; Channel B controls filter brightness, starting after A completes. The note swells in level first, then the filter opens on a separate trajectory.

```
┌──────────────────────────────────────────────┐
│             Xaoc Devices Zadar               │
│                                              │
│  TRIG A ◁──[G]────────────────── Gate source │
│   OUT A ○──[C]────────────────▶ VCA CV in    │
│   OUT B ○──[C]────────────────▶ VCF cutoff   │
└──────────────────────────────────────────────┘
```

Chain algorithm: A→B. Channel B PHASE: 100% (starts when A ends). Channel A shape: Bank A shape 1, TIME 300ms. Channel B shape: Bank B shape 2 (multi-peak), TIME 600ms. The result is a two-stage envelope: a clean amplitude bloom followed by a textured filter movement.

---

## Common Mistakes

**Treating SUSTAIN as a voltage level.** Zadar's SUSTAIN is a position in the shape, not a held voltage. The envelope pauses at whatever voltage the shape has at that point; which depends entirely on the shape selected. If the sustain position falls on a downward slope, the held voltage will be wherever the shape is at that moment, not necessarily the peak.

**Looped chain not cycling.** When a looped chain algorithm is selected, at least one channel's PHASE value must be greater than zero. With all PHASE values at zero (the default), the chain cannot advance. Set at least one channel's PHASE to a non-zero value.

**Expecting negative output voltage.** Zadar outputs 0–10V only. It will never produce a negative voltage without an offset module downstream. If a patch sounds wrong and the envelope seems to have no effect, check that the destination is expecting positive CV; not a bipolar signal centered at 0V.

**Not saving before power-down.** Zadar does not auto-save. Edited channel settings are lost at power-off unless saved to a preset or Quick Saved to the default slot. Get in the habit of Quick Saving (hold MENU) at the end of a session.

**Editing the wrong channel.** All four encoders always affect the currently selected channel. After switching channels with the CHANNEL button to check something, it is easy to continue editing without noticing the switch. The active channel name is displayed in the bottom right corner; confirm it before adjusting parameters.

**NIN connected to the wrong header.** The expansion cable header and the power connector on Zadar's PCB rear are distinct. The power connector leads to the bus board; the expansion header leads to NIN. Connecting NIN to the power connector and then to a powered bus board will cause serious damage.

---

## Pairs Well With

**VCAs**: Zadar's primary role. Four independent channels can simultaneously control amplitude across four voices or layers, each with a distinct envelope character.

**VCFs**: Filter cutoff responds visibly and audibly to envelope shape. Complex shapes from the later banks create filter movements that would take many modules to replicate with traditional ADSR.

**Oscillators**: Slow LFO-mode outputs work as tempo-independent pitch modulation, PWM sources, and FM inputs. Bank I and Bank R shapes loop in interesting ways at audio or near-audio rates.

**Pamela's PRO Workout**: Pamela's gate outputs trigger Zadar channels at different rhythmic densities. One module drives the timing; the other defines the shape of each event.

**SOMA Labs Pulsar-23**: Designed around positive CV ranges. Zadar's 0–10V unipolar output maps naturally to Pulsar-23's CV inputs without offset adjustment.

**Attenuverters and offset modules**: When bipolar modulation is needed, an attenuverter downstream of Zadar's output shifts the range to -5V to +5V. Maths, Shades, or any offset module can perform this conversion.

**Mixers**: Summing two or more Zadar outputs creates compound modulation shapes that no single envelope could produce.

---

## Advanced Learning Path

**Two-dimensional shape deformation**: Explore WARP and RESPONSE simultaneously on a single shape. Understand how temporal skew and amplitude bend interact: the same shape can become many different envelopes before a single channel switch is made.

**CV-controlled shape selection**: Assign a slow LFO or sequencer to the SHP target. As the CV sweeps, the shape morphs continuously through the bank. This is generative envelope design; the modulation source changes what the envelope does, not just by how much.

**FRZ for performance**: Use a gate signal assigned to the FRZ target to freeze an envelope mid-flight. The output holds at whatever voltage the shape had at the moment of freeze, then resumes when the gate drops. This is a live performance tool for holding modulation states on command.

**Full four-channel chain design**: Build a complete A→B→C→D looped chain where each channel has a different shape, time, and PHASE offset. The resulting compound waveform cycles continuously and never obviously repeats. Study how PHASE percentage relates to perceived rhythm.

**Long-duration envelopes**: Set TIME to minutes or longer for generative and ambient applications. An envelope that takes ten minutes to complete from trigger to end becomes an automated compositional structure, not a note event.

**NIN ASGN2 for simultaneous modulation**: With NIN installed, assign ASGN to TIM and ASGN2 to WRP on the same channel. An LFO into each input simultaneously changes duration and temporal deformation in real time. The envelope shifts character continuously as both axes respond to independent CV sources.

**Artist signature banks**: Spend time with Banks X, Y, and Z. Shackleton's shapes have polyrhythmic transient character; Scanner's have fine micro-modulation texture; Richard Devine's are built for controlled glitch and artifact. These were designed with specific sonic intent; patch them into unexpected destinations and listen for what they suggest.

---

*Guide reflects Zadar/NIN manual revision 1973/2.4, firmware 2.0.*
