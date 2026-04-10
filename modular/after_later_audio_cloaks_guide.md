# After Later Audio Cloaks - Guide

**The Quad VCA and Voltage-Controlled Mixer**

![After Later Audio Cloaks](https://github.com/Shadoe-42/music/raw/main/modular/images/after_later_audio/cloaks/front_panel.jpeg)
*10HP quad VCA and cascaded mixer with variable response curve, offset control, and DC-coupled inputs for audio and CV*

---

## Quick Start: Get Your First VCA Sound in 5 Minutes

**What is Cloaks?** Four voltage-controlled amplifiers in 10HP. Each channel takes an audio or CV signal, a control voltage, and produces an amplified output. The channels cascade left to right — plug nothing into outputs 1, 2, and 3 and everything sums to output 4 automatically. Cloaks is a faithful reproduction of the Mutable Instruments Veils 2020 by After Later Audio, built to identical specifications.

**Key Specifications:**
- **Width:** 10 HP
- **Depth:** 25 mm
- **Power:** 50 mA @ +12V / 50 mA @ -12V / 0 mA @ +5V
- **Inputs:** DC-coupled, accepts audio and CV
- **Input impedance:** 100k all inputs
- **Gain scale:** +5V CV = gain of 1 (0dB) in both linear and exponential mode
- **Offset range:** 0V to +8V positive offset

### Your First VCA Patch
1. **Patch a sound source** into IN on channel 1 (signal input jack)
2. **Patch an envelope** into CV on channel 1 (gain CV input jack)
3. **Take output** from OUT on channel 1
4. **Set the slider (C)** to maximum
5. **Set response curve (A)** to center
6. **Trigger your envelope** — the sound opens and closes with it

**Congratulations** — you have a gated voice. Everything else Cloaks does builds from here.

---

## Essential Parameters

Each of the four channels has identical controls and jacks. All descriptions below apply to every channel.

### **A — Response Curve**
- **What it does:** Continuously morphs the VCA response between exponential (fully counterclockwise) and linear (fully clockwise)
- **Exponential:** Follows human hearing perception — sounds natural for envelopes shaping audio. Also achieves very high gains (above 100x) when combined with a large offset
- **Linear:** Proportional response, better for CV processing and amplitude modulation
- **Center position:** A practical starting point — slight exponential character suits most audio work
- **Warning:** Exponential mode with high CV and high offset can clip hard. The output indicator LED will tell you when you're there

### **B — Offset Control**
- **What it does:** Adds a positive DC offset (0V to +8V) to the CV signal before it hits the VCA
- **Primary use:** Opens the VCA partially or fully without any CV patched — turns the channel into a manually controlled fader
- **Secondary use:** Shifts a bipolar LFO upward so the full swing produces useful modulation rather than silence on the negative half
- **Critical understanding:** The offset affects the CV, not the audio signal
- **Formula:** Output = (CV × slider_amount + offset) × audio_input

### **C — Gain Slider**
- **What it does:** Controls the amount of CV modulation applied to the channel, or acts as a direct level fader when no CV is patched
- **With CV patched:** Scales how much the CV opens the VCA. At maximum, a +5V CV produces unity gain (0dB)
- **Without CV patched:** The CV input normalizes to +8V internally. The slider becomes a direct fader
- **Gain indicator LED (1):** Brightness is proportional to VCA gain on a dB scale. Off means muted

### **Jacks Per Channel**
- **CV input (2):** Gain control voltage. Normalized to +8V when nothing is patched — this is what makes the slider work as a fader with no CV connected
- **Signal input (3):** DC-coupled. Accepts audio or CV signals equally
- **Signal output (5):** When nothing is patched here, this channel's output routes into the next channel to the right — the cascade mixing behavior

### **Output Indicator LED (4)**
- Brightness represents signal level at the output
- Color represents polarity — green = positive signal
- Useful for monitoring both audio and CV signals passing through

---

## Historical Context

Veils appeared in Mutable Instruments' original lineup and became one of the most widely used modules in Eurorack. The original version used knobs. The 2020 redesign replaced them with sliders — a more ergonomic choice that made the mixer function more intuitive and visible at a glance. Émilie Gillet released all Mutable Instruments designs as open-source hardware before closing the company, and After Later Audio built Cloaks as an exact hardware replica under that Creative Commons license. The OPA1679 op-amps use a different physical package than the original but are electrically identical. The cascaded output normalization and variable response curve remain distinctive features that many designs have imitated.

---

## Why Cloaks Excels

VCAs are the most fundamental control element in a modular patch. Without them, signals either pass at full strength or not at all — there is no dynamic shaping, no opening and closing, no amplitude modulation. Cloaks gives you four of them in 10HP with three features that separate it from simpler VCA designs.

The variable response curve means one module covers both natural-sounding envelope shaping for audio and proportional control for CV. The offset control solves the real-world problem of bipolar modulation sources — LFOs that swing below zero can close a VCA unintentionally, and offset shifts the operating point up so the full swing produces useful modulation. The cascaded normalization turns four independent VCAs into a voltage-controlled mixer with no additional patching — leave outputs 1, 2, and 3 unpatched and everything sums to output 4 automatically.

The DC-coupling is significant. Cloaks processes CV signals just as cleanly as audio. A CV signal going through a VCA becomes a CV signal with voltage-controlled amplitude — a powerful technique for scaling modulation, creating shaped envelopes from gates, or building complex modulation from simpler sources.

---

## Patch Examples

### **Patch 1: Four-Voice Voltage-Controlled Mixer**

The most direct use of the cascade normalization. Nothing patched into outputs 1, 2, or 3 — everything sums to output 4.

```
🔴 Audio │ 🔵 CV │ 🟡 Gate

┌─ Voice 1 ──────┐    ┌─ Cloaks ─────────────────────────┐
│ Plaits OUT ○───┼────┼─▶ CH1 IN     CH1 OUT (unpatched)  │
└────────────────┘    │                                   │
                      │ CH1 slider: 3/4 up                │
┌─ Voice 2 ──────┐    │ CH1 curve: center                 │
│ Loquelic OUT ○─┼────┼─▶ CH2 IN     CH2 OUT (unpatched)  │
└────────────────┘    │                                   │
                      │ CH2 slider: 1/2 up                │
┌─ Voice 3 ──────┐    │                                   │
│ Rings OUT ○────┼────┼─▶ CH3 IN     CH3 OUT (unpatched)  │
└────────────────┘    │                                   │
                      │ CH3 slider: 1/2 up                │
┌─ Voice 4 ──────┐    │                                   │
│ Drum OUT ○─────┼────┼─▶ CH4 IN     CH4 OUT ○────────────┼──▶ Output
└────────────────┘    │                                   │
                      │ CH4 slider: full up               │
┌─ Envelopes ────┐    │                                   │
│ ENV 1 ○────────┼────┼─▶ CH1 CV                          │
│ ENV 2 ○────────┼────┼─▶ CH2 CV                          │
│ ENV 3 ○────────┼────┼─▶ CH3 CV                          │
│ ENV 4 ○────────┼────┼─▶ CH4 CV                          │
└────────────────┘    └───────────────────────────────────┘
```

Each voice has its own envelope shaping its amplitude. The sum appears at CH4 OUT. Adjust sliders to balance the mix — the slider scales how much each envelope opens its channel.

**Main Example:** Mutable Plaits + Noise Engineering Loquelic Iteritas + Mutable Rings + drum voice, each with independent envelope → single output
**Alternative Options:**
- **Budget:** Any four oscillators with a simple envelope generator feeding all CV inputs via a mult
- **Different character:** Replace one voice with a noise source for textural contrast in the mix
- **Premium:** Add Xaoc Devices Zadar for complex per-voice envelope shapes rather than simple ADSR

---

### **Patch 2: CV Amplitude Scaling**

DC-coupling makes Cloaks useful as a CV processor. Run a modulation source through a channel to scale it with voltage control.

```
🔴 Audio │ 🔵 CV │ 🟡 Gate

┌─ Marbles ──────┐    ┌─ Cloaks ─────────────┐    ┌─ Destination ──┐
│ t1 GATE ○──────┼────┼─▶ CH1 CV              │    │ Filter CUTOFF  │
│                │    │                       │    │                │
│ X1 CV ○────────┼────┼─▶ CH1 IN  CH1 OUT ○───┼────┼─▶ CV Input 🔵  │
└────────────────┘    │                       │    └────────────────┘
                      │ CH1 slider: variable  │
                      │ CH1 curve: linear     │
                      │ CH1 offset: 0         │
                      └───────────────────────┘
```

Marbles X output (random CV) goes into signal input. Marbles gate goes into CV input. The gate opens the channel only when a trigger fires — each trigger produces a brief CV pulse shaped by the gate duration. The slider scales the CV amplitude reaching the destination. Run a self-patching variation by connecting a channel's output back to its own CV input for amplitude self-modulation.

**Main Example:** Mutable Marbles random CV gated through Cloaks → filter cutoff for rhythmic timbral changes
**Alternative Options:**
- **Budget:** Any random voltage source + gate → Cloaks creates identical rhythmic CV behavior
- **Different character:** Use Make Noise Wogglebug random output through Cloaks for more chaotic, unpredictable amplitude scaling
- **Premium:** Befaco Oneiroi output through Cloaks for complex spectral CV amplitude shaping

---

### **Patch 3: Offset as Bipolar Modulation Correction**

The offset control solves a specific problem — a bipolar LFO swings below zero and closes the VCA on its negative half. Offset shifts the operating point so the whole swing produces useful modulation.

```
🔴 Audio │ 🔵 CV │ 🟡 Gate

┌─ Oscillator ───┐    ┌─ Cloaks ─────────────────────────┐
│ OSC OUT ○──────┼────┼─▶ CH1 IN     CH1 OUT ○────────────┼──▶ Output
└────────────────┘    │                                   │
                      │ CH1 slider: 2/3 up                │
┌─ Bipolar LFO ──┐    │ CH1 curve: exponential            │
│ LFO OUT ○──────┼────┼─▶ CH1 CV                          │
│ (+/-5V swing)  │    │                                   │
└────────────────┘    │ CH1 offset: dial up until         │
                      │ LFO no longer closes VCA          │
                      └───────────────────────────────────┘
```

Without offset: the LFO swings negative and closes the VCA on every downswing — choppy gated tremolo rather than smooth amplitude modulation. With offset dialed to approximately 3-4V: the entire LFO swing sits in positive territory and produces smooth continuous tremolo. Watch the gain indicator LED — it should never fully extinguish if the offset is working correctly.

**Main Example:** Bipolar LFO into Cloaks CV with offset correction → smooth tremolo on any audio source
**Alternative Options:**
- **Budget:** Same technique works identically with any bipolar LFO — Pico LFO, ochd outputs, anything available
- **Different character:** Use DivKid ochd directly (unipolar by default) to skip the offset correction entirely
- **Premium:** Xaoc Devices Batumi II with Poti II expander provides direct unipolar/bipolar switching per channel

---

## Common Mistakes

### **1. Expecting the Offset to Shift the Audio Signal**
The offset shifts the CV, not the audio. Turning up offset with no CV patched will open the VCA because the CV input is normalized to +8V and the offset adds to that — but the audio signal itself is not being DC-shifted. If you want to add a DC offset to an audio or CV signal, that requires a different utility. Understanding this prevents confusion when the offset behaves unexpectedly.

### **2. Misreading the Cascade Normalization**
If you patch a cable into output 1, that channel disconnects from the sum. Channels only cascade into each other through unpatched outputs. This means you can use channels 1 and 2 as a two-voice mixer summing to output 3 while using channel 4 as a completely independent VCA. The normalization is flexible, not all-or-nothing. A cable in any output breaks the chain at that point.

### **3. Overdriving Exponential Mode**
The exponential response curve achieves very high gains quickly. With a high CV and a high offset simultaneously, output levels can clip hard — the output indicator LED turning red is the signal. This is not always undesirable. Overdriving Cloaks in exponential mode produces a specific crisp distortion. But for clean amplification, pull back the offset or slider when the LED reddens.

### **4. Forgetting the +8V Normalization**
When nothing is patched into a CV input, the input sees +8V internally. This means the slider position directly sets VCA gain from 0 to above unity. If a channel is too loud at full slider with no CV patched, that is the normalization working as designed — +8V is above the +5V unity gain point, so full slider produces gain above 0dB. Pull the slider back slightly to reach unity.

### **5. Using Linear Mode for Audio Envelopes**
Linear mode sounds correct on paper — equal voltage steps produce equal gain steps. But human hearing is logarithmic, so linear VCA response sounds like the volume jumps up quickly then barely moves at the top. Exponential mode matches human hearing perception and produces natural-sounding envelope shapes for audio. Use linear mode for CV processing where proportional response matters. Use exponential or center position for audio shaping.

---

## Pairs Well With

**Envelope Generators:** Cloaks needs envelopes to shape voices. Erica Synths Black EG2, Make Noise Maths, Xaoc Devices Zadar, Behringer 1003 — all feed naturally into Cloaks CV inputs. One envelope per Cloaks channel gives independent dynamic shaping to every voice.

**Oscillators and Voice Modules:** Mutable Plaits, Noise Engineering Loquelic Iteritas, Endorphin.es Furthrrrr Generator, Qu-Bit Chord v2 — any voice module through Cloaks gains voltage-controlled amplitude. This is the fundamental voice → VCA → output chain that anchors most patches.

**Modulation Sources:** DivKid ochd, Xaoc Devices Batumi II, Mutable Marbles X outputs, Make Noise Wogglebug — all work as CV sources into Cloaks. Bipolar sources benefit from the offset control. Unipolar sources (ochd is unipolar by default) work without offset correction.

**Intellijel Mixup:** Cloaks handles the voltage-controlled mixing. Mixup adds stereo mixing capability downstream if needed. The two together cover most mixing and routing requirements in a patch.

**Make Noise Maths:** Maths outputs complex envelope and function shapes that complement Cloaks' variable response curve. A falling Maths output into a Cloaks CV input produces slow natural amplitude decay. Maths can also process CV signals through Cloaks by feeding one Maths output into a Cloaks IN and another into the same channel's CV — the result is a mathematically combined signal.

---

## Advanced Learning Path

1. **Master the four-voice mixer** — use all four channels as a simple sum mixer first, sliders as faders, no CV. Understand the cascade normalization by adding and removing cables from outputs and observing what changes.

2. **Add envelopes one channel at a time** — patch one envelope into one CV input and hear how the response curve changes the character of the envelope shape. Compare fully exponential against fully linear on the same envelope.

3. **Explore the offset control** — patch a bipolar LFO into a CV input with audio in the signal input. Dial in offset until the LFO produces smooth tremolo rather than gated amplitude. Understand why the offset amount needed correlates with the LFO amplitude.

4. **Process CV through Cloaks** — patch a CV signal into a signal input and another CV into the CV input. Watch the output on Mordax Data. Understand what voltage-controlled CV amplitude looks like and how it differs from audio processing.

5. **Self-patching** — patch one channel's output back into a different channel's CV input. The channel is now modulating another channel's amplitude. This is where Cloaks starts generating complex behavior from simple inputs.

---

*After Later Audio Cloaks is an exact hardware replica of the Mutable Instruments Veils 2020, designed by Émilie Gillet and released under Creative Commons CC-BY-SA license.*
