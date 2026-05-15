---
title: Pico QUANT
manufacturer: Erica Synths
series: Pico
primary_role: UTILITY
secondary_roles: []
functions: [quantizer, cv-processor]
hp: 3
depth: 35mm
current_draw:
  plus12: 25mA
  minus12: 6mA
price_eur: 120
inputs: [CLK IN, CV IN]
outputs: [CV OUT, CLK OUT]
patch_format: v1
---

# Erica Synths Pico QUANT

![Erica Synths Pico QUANT](https://github.com/Shadoe-42/music/raw/main/modular/images/erica_synths/pico_quant/front_panel.jpg)

## Historical Context

The quantizer exists because voltage and pitch are not naturally the same thing. The 1V/oct standard maps each octave to one volt and each semitone to 83.3 millivolts, which means that a sequencer, LFO, or random source generating arbitrary voltages will produce arbitrary pitches unless something in the signal chain snaps those voltages to musically meaningful values. The quantizer is that something.

In the early decades of modular synthesis, quantizers were relatively rare and expensive. Patching an LFO into a VCO pitch input without one produced gliding, continuous pitch movement rather than discrete notes. That limitation shaped how early synthesists composed: pitch sources had to be carefully controlled, and random or generative pitch sequences were difficult to keep in key. The quantizer changed that. Once a random voltage source could be forced into a scale, the door opened to generative melodic sequencing, probabilistic composition, and the use of modulation sources as pitch sources.

The Pico QUANT takes that foundation and extends it in two directions: toward microtonality, with quarter-tone accuracy and a web-based interface for uploading custom scales, and toward interactivity, with a tolerance control that changes how aggressively the module commits to each new note. These two additions make the module as useful for non-Western tuning systems and experimental pitch spaces as it is for standard Western scales.

---

## Why Pico QUANT Excels

The Pico QUANT's clearest strength is what it does with chaotic or unstable CV. Feed it a random voltage source, a noise signal, an audio-rate LFO run slow, or a modulation signal from a module that was never intended as a pitch source, and it returns something that has melodic coherence while retaining the energy and unpredictability of the original. The patch does not sound composed. It sounds like the rack is making decisions.

The tolerance control is what gives the module its character in this role. At full CCW (50% tolerance), the quantizer is eager: it snaps to the next note as soon as the incoming CV crosses the midpoint between two scale degrees. The output moves frequently and responsively. At full CW (10% tolerance), the quantizer is stubborn: it holds the current note until the incoming CV gets very close to the next scale degree before committing. The output moves less often, and when it does, the change feels deliberate. The same CV source, the same scale, the same patch: the tolerance knob alone controls whether the result is restless or settled.

The CLK OUT jack adds a dimension that the manual does not emphasize. When nothing is patched to CLK IN, CLK OUT fires a trigger on every pitch change. This couples the melodic and rhythmic output of the quantizer: more active pitch movement produces more triggers, quieter pitch movement produces fewer. Patching CLK OUT to a percussion module or envelope generator creates a voice that fires in proportion to melodic activity rather than on a fixed clock grid.

Three HP. These capabilities in three HP is the other thing worth naming.

---

## Tolerance: The Counterintuitive Knob

Before the patches, one clarification is worth making explicitly.

The TOLERANCE knob does not work the way the label implies. Turning it clockwise does not give you more tolerance: it gives you less. Full CW (10% tolerance) means the quantizer will only advance to the next note when the incoming CV is within 10% of the gap between notes: very close, very committed, very reluctant to change. Full CCW (50% tolerance) means it advances at the midpoint: more forgiving, more willing to move.

Think of it as a stubbornness knob. CCW is loose and eager. CW is tight and stubborn. This direction will feel wrong the first time. It is worth internalizing before using the module under pressure.

---

## Patch Examples

All patches use the standard UTILITY First Voice: an external oscillator receives the quantized pitch CV from CV OUT, with an envelope and VCA shaping the amplitude. The Pico QUANT sits between the CV source and the VCO.

---

### Patch 1: Clocked vs. Unclocked Quantization

Clocking the quantizer changes its behavior from continuous pitch tracking to sample-and-hold style pitch selection: the module only reads the incoming CV on each clock pulse and holds that quantized value until the next pulse. This produces pitch changes that align to a rhythmic grid rather than following the source voltage in real time.

**First Voice**

Before connecting any CV source to the quantizer, establish a working voice:

```
  Sequencer gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  VCO audio out ──[A]──▶ VCA audio in ──▶ Mixer
  [Pico QUANT] CV OUT ──[C]──▶ VCO 1V/OCT
```

Verify the voice produces a clean tone before introducing the CV source. Set the SCALE button to Diatonic (black LED) as a starting point.

**Add the CV source, unclocked**

```
                    ┌─────────────────────────────┐
LFO ──[C, slow]──▶  │ CV IN          CV OUT        │──[C]──▶ VCO 1V/OCT
                    │                CLK OUT       │──[T]──▶ (leave unpatched for now)
                    └─────────────────────────────┘
                              Pico QUANT
```

Use an LFO such as 2hp LFO v2 (or Batumi) set to a slow triangle wave. Set the LFO to a unipolar output or offset it so it stays above 0V; the Pico QUANT ignores negative voltages, so any portion of the LFO swing below 0V will produce no pitch change.

- `LFO ──[C, slow]──▶ CV IN`: the rising and falling LFO voltage sweeps continuously through the scale. Each time the voltage crosses a tolerance threshold, the output snaps to the next scale degree. With 50% tolerance (CCW), the output ladders up and down the scale smoothly. With 10% tolerance (CW), the output holds each note longer before stepping.

**Move the cable: add the clock**

```
                    ┌─────────────────────────────┐
LFO ──[C, slow]──▶  │ CV IN          CV OUT        │──[C]──▶ VCO 1V/OCT
Clock ──[T]──▶      │ CLK IN         CLK OUT       │
                    └─────────────────────────────┘
                              Pico QUANT
```

Use a clock such as Pamela's Pro Workout (or Hermod+) at a moderate rate (eighth notes or quarter notes as a starting point).

What changed: the quantizer now samples the LFO only on each clock pulse. Pitch changes snap to the rhythmic grid rather than following the LFO continuously. The LFO still determines which note is selected, but the clock determines when the selection happens. Slow clock rates produce long held notes; fast rates produce busier melodic movement even with the same slow LFO.

**What to listen for**

Unclocked, the pitch should move smoothly through scale degrees as the LFO rises and falls. Clocked, pitch changes should align clearly to the beat. If pitch is not changing at all, the LFO is likely swinging below 0V; add a DC offset or switch to a unipolar LFO output. If the clocked output sounds identical to the unclocked output, confirm the clock is patched to CLK IN and not to CV IN.

---

### Patch 2: Random CV In, CLK OUT to Percussion

When nothing is patched to CLK IN, the CLK OUT jack fires a trigger on every pitch change. This creates a direct link between melodic and rhythmic density: a CV source that changes pitch often produces many triggers, while a source that holds pitches longer produces fewer. Feeding random voltage into the quantizer and routing CLK OUT to a percussion voice creates a patch where melodic and percussive activity are coupled rather than independent.

**First Voice**

```
  [Pico QUANT] CV OUT ──[C]──▶ VCO 1V/OCT
  VCO audio out ──[A]──▶ VCA audio in ──▶ Mixer
  [Pico QUANT] CLK OUT ──[T]──▶ EG gate in ──▶ VCA CV in
```

The CLK OUT drives the envelope directly. No sequencer gate is needed: the pitch change itself is the trigger.

**Add the random source**

```
                         ┌─────────────────────────────┐
Random CV ──[C]──▶       │ CV IN          CV OUT        │──[C]──▶ VCO 1V/OCT
                         │                CLK OUT       │──[T]──▶ EG gate in
                         └─────────────────────────────┘
                                    Pico QUANT
                                    (CLK IN unpatched)
```

Use a random CV source such as the Turing Machine (or Ornament and Crime in a random mode). Set the source to generate slowly evolving random voltages rather than fast noise. Ensure the output stays above 0V or add an offset; a random source that swings negative will produce fewer pitch changes as the negative portions are ignored.

- `Random CV ──[C]──▶ CV IN`: the quantizer snaps each random voltage to the nearest scale degree. The output is melodically organized but unpredictable in sequence.
- `CLK OUT ──[T]──▶ EG gate in`: each pitch change fires the envelope. The note sounds when the pitch changes and is silent when the pitch holds.

Now use the TOLERANCE knob as a real-time control. Turn it CCW: the quantizer snaps eagerly, producing more frequent pitch changes and more triggers. Turn it CW: the quantizer holds each note longer before committing, producing fewer triggers and a slower, sparser melodic line. The same random source, the same scale, the same patch: tolerance alone controls density.

**Move the cable**

Patch CLK OUT to a separate percussion module (drum voice or envelope on a different VCA) in addition to the melodic EG, leaving both connected.

```
                         ┌─────────────────────────────┐
Random CV ──[C]──▶       │ CV IN          CV OUT        │──[C]──▶ VCO 1V/OCT
                         │                CLK OUT       │──[T]──▶ Mult ──▶ Melodic EG
                         └─────────────────────────────┘                ──▶ Drum voice
                                    Pico QUANT
```

What changed: every pitch change now triggers both the melodic note and a percussion hit simultaneously. The two voices are rhythmically locked to the same source. Dense pitch activity produces dense, busy percussion; sparse pitch activity produces sparse, open percussion. The melodic and percussive layers breathe together.

**What to listen for**

The melody should be unpredictable but always in key. If you hear pitches that feel outside the selected scale, check that the random source is not producing voltages above +8V; the CV OUT ceiling is +8V, so very high input voltages may quantize to the top of the available range and repeat. The percussion hits should correlate directly with pitch changes: every audible note onset should correspond to a CLK OUT trigger. If hits feel out of sync with notes, verify the EG attack is short enough to respond cleanly to the trigger.

---

### Patch 3: Tolerance as Live Performance Control

Tolerance changes how committed the quantizer is to each note. With a slowly evolving CV source, dialing the TOLERANCE knob in real time is a performance control that shifts the character of the melodic output from restless and reactive to slow and deliberate without changing anything else in the patch.

**First Voice**

```
  [Pico QUANT] CV OUT ──[C]──▶ VCO 1V/OCT
  Sequencer gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  VCO audio out ──[A]──▶ VCF audio in ──▶ VCA audio in ──▶ Mixer
```

Using a VCF such as Erica Synths Black VCF (or Doepfer A-124) adds timbral variation that makes the effect of tolerance more audible.

**Add a slowly evolving CV source**

```
                              ┌─────────────────────────────┐
Slow evolving CV ──[C]──▶     │ CV IN          CV OUT        │──[C]──▶ VCO 1V/OCT
                              │                              │
                              └─────────────────────────────┘
                                         Pico QUANT
```

Use a very slow LFO or a slowly evolving random source (something that moves across several volts over eight to sixteen seconds). Select the Blues scale (green LED) or Pentatonic (dark blue LED) for a scale where the musical effect of tolerance is easy to hear.

Set the TOLERANCE knob to full CCW. The output should move frequently through the scale as the source voltage rises and falls. Now slowly turn the knob clockwise. The output will begin to hold notes longer before snapping to the next degree. At full CW, the melody slows considerably: each note holds until the incoming CV has moved well past the midpoint toward the next degree.

The GLIDE knob interacts with this. Add a small amount of glide (turn slightly CW from minimum) while using high tolerance. The combination produces a patch where pitch changes happen infrequently but slide smoothly into the next note when they do. With low tolerance (CCW) and no glide, the output snaps rapidly between notes. These two controls in combination cover a wide range of melodic character from a single CV source.

**What to listen for**

At low tolerance (CCW), the melody should feel active and changeable, following the contour of the CV source closely. At high tolerance (CW), the melody should feel settled, holding each note for longer and moving less frequently. If the output is not changing at all at any tolerance setting, the CV source is not moving enough: try a wider LFO range or a faster source. If the output changes at the same rate regardless of tolerance position, confirm the TOLERANCE knob is functioning and that the source CV is within the 0V to +8V range where tolerance has the most effect.

---

## Scale Upload

The Pico QUANT includes a web-based interface for uploading custom scales, accessible at [ericasynths.lv/quant](https://www.ericasynths.lv/quant/) (verify this URL is still active before use).

Upload works by sending scale data as audio from a laptop or smartphone headphone output into the CLK IN jack on the module. No USB or MIDI connection is required.

**Upload procedure:**

1. Open the web interface on a laptop or smartphone.
2. Connect the headphone output to CLK IN on the Pico QUANT using a 3.5mm to 3.5mm cable (or adapter to 3.5mm from the module's jack size).
3. In the interface, click SEMI/QUARTER to choose semitone or quarter-tone resolution.
4. Select a preset from the SCALES dropdown or click keys on the on-screen keyboard to build a custom scale. Dots appear on the keys to indicate active notes.
5. Hold the SCALE button on the module for two seconds. The LED blinks red, indicating upload mode.
6. In the interface, select the target slot (1 through 8, corresponding to LED colors) and click UPLOAD. The upload takes approximately one second. The LED blinks green once on success.
7. If a slot already has a scale loaded, uploading to that slot overwrites it.

Scales can be saved to and loaded from the laptop for reuse across sessions. The quarter-tone option enables microtonal scales with 24 pitches per octave rather than 12, which opens non-Western tuning systems, maqam-adjacent pitch sets, and experimental intonation.

The eight uploadable slots correspond to the same eight LED colors as the preset scales. Uploading replaces the preset for that slot; to restore factory presets, re-upload the preset values using the SCALES dropdown in the web interface.

---

## Controls Reference

**TOLERANCE knob.** CCW = 50% tolerance (snaps to next note at the midpoint between scale degrees, eager). CW = 10% tolerance (snaps only when incoming CV is very close to the next degree, stubborn). Note: clockwise means tighter, not looser.

**GLIDE knob.** Sets glide time from 0 to 1 second between quantized notes. At fast sequences, acts as a wet/dry control: CCW applies quantization cleanly with no glide, CW introduces portamento between pitch changes.

**SCALE button.** Press briefly to step through 8 scale slots. Hold for 2 seconds to enter scale upload mode (LED blinks red). The RGB LED color indicates the active scale.

**CLK IN.** Patch a clock signal here for clocked (sample-and-hold style) quantization. When CLK IN is patched, the quantizer reads CV IN only on each incoming clock pulse.

**CV IN.** Unquantized CV input. Range: -10V to +10V. Negative voltages are ignored; only 0V to +10V produces output pitch values.

**CV OUT.** Quantized CV output. Range: 0V to +8V.

**CLK OUT.** Trigger output. When CLK IN is unpatched: fires on every CV step change (pitch change trigger). When CLK IN is patched: follows the incoming clock. LED blinks on each CV change.

---

## Preset Scales

| LED Color | Scale |
|-----------|-------|
| Black (off) | Diatonic |
| Red | Double Harmonic Major (Arabian) |
| Yellow | Harmonic Minor |
| Green | Blues |
| Cyan | Diminished |
| Dark Blue | Pentatonic |
| Magenta | Whole-tone |
| White | Chromatic |

---

## Key Specs

| Parameter | Value |
|-----------|-------|
| HP | 3 |
| Depth | 35mm |
| +12V | 25mA |
| -12V | 6mA |
| CV IN range | -10V to +10V (negative ignored) |
| CV OUT range | 0V to +8V |
| Glide time | 0 to 1 second |
| Minimum accuracy | 1/4 tone |
| Preset scales | 8 |
| Uploadable scale slots | 8 |

---

## Common Errors

**Patching a bipolar LFO directly into CV IN and getting fewer notes than expected.** The Pico QUANT ignores negative voltages. A bipolar LFO swinging from -5V to +5V only produces output pitch values during the positive half of its cycle. Use a unipolar LFO output, or add a DC offset to shift the LFO above 0V.

**Turning TOLERANCE clockwise expecting looser behavior.** Clockwise is tighter (10% tolerance, more stubborn). Counterclockwise is looser (50% tolerance, more eager). This is the opposite of the intuitive direction. Internalize it before performing.

**Expecting CLK OUT to fire on a clock grid without patching CLK IN.** CLK OUT follows pitch changes, not a clock, when CLK IN is unpatched. It fires when the quantized output changes value, which depends on the incoming CV source and the tolerance setting. Patch CLK IN if you need clock-synchronized trigger output.

**Uploading a scale to the wrong slot.** The slot selector in the web interface determines which LED color slot receives the upload. Uploading to an occupied slot overwrites it silently. Keep a record of which custom scales are loaded in which slots, or save them to disk before overwriting.

**Sending the upload audio signal at the wrong volume.** The scale upload uses the headphone output to transmit data via audio. If the headphone volume is too low, the upload may fail or produce a corrupted scale. If too high, it may also fail. Start at 60-70% volume and adjust if the LED does not blink green on completion.

---

## Notes

The Pico QUANT CV OUT ceiling of +8V means it covers approximately eight octaves of the 1V/oct standard (0V to +8V). Sources producing voltages above +8V will quantize to the highest available pitch in the selected scale and hold there. If a sequence is unexpectedly stuck at a high pitch, check that the CV source is not exceeding +8V.

The glide control interacts with tolerance in musically useful ways. High tolerance (CW) with a small amount of glide produces infrequent pitch changes that slide smoothly into each new note. Low tolerance (CCW) with no glide produces fast, snappy pitch movement. The combination of both controls covers the range from legato, considered melodic movement to rapid, percussive pitch activity.

Full documentation and scale upload interface are available at [ericasynths.lv/quant](https://www.ericasynths.lv/quant/).
