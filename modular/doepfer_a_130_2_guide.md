---
title: Doepfer A-130-2
manufacturer: Doepfer
primary_role: AMPLIFIER
secondary_roles: []
form_factor: eurorack
functions: [vca]
behavior_tags: [clean, stable, linear, reactive]
use_cases: [envelope shaping, audio mixing and routing, CV-controlled attenuation]
hp: 4
---

# Doepfer A-130-2 Guide

**Dual Linear/Exponential VCA (Slim Line)**  
**Manufacturer:** Doepfer  
**Format:** Eurorack  
**Width:** 4HP | **Depth:** ~25mm | **Power:** +/- 12V

![Doepfer A-130-2](https://github.com/Shadoe-42/music/raw/main/modular/images/doepfer/a_130_2/front_panel.jpg)  
*4HP dual VCA with switchable linear/exponential response and center-mute position. Two complete, independent amplifier channels in minimal space.*

---

## Quick Start

**What you need:** An audio or CV source, an envelope or gate, and a destination.

**Minimum viable patch:**
1. Patch your oscillator OUT ---[A]---> A-130-2 IN (top channel)
2. Patch your envelope OUT ---[C]---> A-130-2 CV (top channel)
3. Patch A-130-2 OUT ---[A]---> your mixer or filter
4. Set the Gain knob (Initial Gain) fully counterclockwise
5. Set the CV attenuator fully clockwise
6. Set the lin/exp switch to lin (left position)
7. Trigger your envelope; the audio opens and closes with the envelope shape

**Key Specifications:**

| Spec | Value |
|------|--------|
| Width | 4HP |
| Channels | 2 (independent) |
| Response | Linear or Exponential (switchable) |
| Max amplification | 1× (unity gain, 0dB) |
| CV for max gain | +5V minimum (with CV attenuator fully CW, Gain fully CCW) |
| Max input signal | 16Vpp (±8V) without distortion |
| DC coupling | Yes (audio and CV both supported) |
| Switch positions | lin / mute (center) / exp |

---

## What Is a VCA?

A voltage controlled amplifier is the module that determines whether you hear a sound and how loud it is at any given moment. Without a VCA between your oscillator and your output, your oscillator plays continuously at full volume. A VCA gives you a way to shape that level over time using a control voltage.

The most common CV source for a VCA is an envelope generator. The envelope produces a voltage that rises when triggered, sustains while a gate is held, and falls when the gate closes. That voltage, patched into the VCA's CV input, directly controls the amplifier's gain. The result is the classic synthesizer note shape: the sound swells in, sustains, and fades out.

But VCAs are not limited to amplitude envelopes on audio signals. Because the A-130-2 is DC-coupled, it can process any signal, including control voltages. Patching an LFO into IN and an envelope into CV produces an LFO whose depth is shaped by the envelope: full depth at the envelope's peak, zero depth when the envelope is closed. This is VCA as CV processor, and it is used constantly in complex patches.

The Doepfer A-130-2 is the space-efficient version of this function. Two independent VCAs in 4HP, each with full manual and CV control. It is not a feature-rich module; it is a reliable utility whose value compounds as your system grows.

---

## Essential Parameters

### Gain (Initial Gain)

The manual gain control sets the VCA's resting level before any CV is applied. When set fully counterclockwise, the channel passes no signal without CV. When set clockwise, the channel passes signal even without any CV patched. This is useful for static level control (no CV, just the knob) or for setting a "floor" level that CV then adds to.

The Gain and CV attenuator interact: the total gain at any moment is the combination of the manual Gain position and whatever voltage the CV attenuator is passing to the VCA circuit. Understanding this interaction is the key to using the module confidently.

### CV Attenuator

Controls how much of the incoming CV voltage reaches the VCA. At fully clockwise, the full CV signal is applied. At fully counterclockwise, no CV reaches the VCA regardless of what is patched into the CV jack. This attenuator does not invert the signal.

The practical consequence: if your envelope is outputting 8V at its peak and you need unity gain at 5V, turn the CV attenuator down until the VCA reaches unity at the envelope's peak without clipping. The module clips gain at 1× regardless of CV level, so over-driving the CV input just means the VCA hits unity earlier in the envelope's rise.

### lin/exp Switch

Three-position switch:
- **Left (lin):** Linear response. The gain tracks the CV voltage proportionally. A CV at half of maximum produces half the gain. Used when the mathematical relationship between CV and gain needs to be exact; preferred for CV processing applications and for modulation depth control.
- **Center:** Mute. The channel is completely silent regardless of CV or manual Gain setting. This is a useful performance function that most users overlook: the center position is a hard mute, not a default or bypass.
- **Right (exp):** Exponential response. The gain curve is shaped to correspond more closely with human loudness perception. Human hearing is logarithmic: equal-ratio volume changes are perceived as equal loudness steps. An exponential VCA response means that envelope shapes translate more naturally into perceived volume changes. For audio amplitude control with standard ADSR envelopes, exponential response usually sounds more musical.

The choice between linear and exponential is context-dependent, not a quality judgment. For CV-on-CV processing, linear is correct. For audio amplitude envelopes where you want natural-sounding dynamics, exponential is usually preferred.

---

## Historical Context

Doepfer Musikelektronik, founded by Dieter Doepfer in Munich, created the Eurorack format in 1995 with the A-100 modular system. The A-130 series has been part of that system from near the beginning. Doepfer's design philosophy favors functional simplicity, affordability, and standardization: modules that do one thing correctly without embellishment.

The A-130-2 belongs to the Slim Line series, which applies the same circuit designs as the standard-width modules in half the panel space. This reflects a practical engineering ethos: the same signal processing in a smaller footprint, no additional features, no reduction in quality. For builders filling a case with infrastructure modules, the Slim Line series offers functional density that other manufacturers rarely match.

The A-130-2 is the direct slim counterpart of the A-132-3 Dual VCA, which is an 8HP module with identical circuitry. If space is the primary constraint, the A-130-2 is the appropriate choice. If panel access and knob spacing matter more, the A-132-3 gives more room to work.

---

## Why This Excels

The A-130-2's value is density and reliability. Two complete, independent VCA channels with full CV control and response switching in 4HP is a specification that very few modules match. As a system grows, the number of VCAs needed grows with it: amplitude shaping, CV depth control, dynamic voice management, and mixing all consume VCA channels. The A-130-2 allows filling those needs without sacrificing significant panel space.

The lin/exp switch is more useful than it first appears. Having both response curves available on the same module means a single A-130-2 can serve as both an audio amplitude VCA (exponential) and a CV processor (linear) simultaneously, using one channel for each application.

DC coupling is often not highlighted on VCAs but matters practically. Any signal in the modular system (audio, envelope, LFO, pitch CV) can be patched into the A-130-2's input and controlled by any other signal at the CV input. This flexibility is why experienced builders often reach for a simple dual VCA first when a patch calls for CV-controlled modulation depth.

---

## Patch Examples

### Patch 1: Standard Voice Amplitude Control

**Goal:** Shape a synthesizer voice's volume with an envelope.

**Setup:**
```
VCO OUT               ---[A]---> A-130-2 IN (ch1)
ENV OUT               ---[C]---> A-130-2 CV (ch1)
A-130-2 OUT (ch1)     ---[A]---> Filter or Mixer
Gate OUT              ---[G]---> ENV GATE
```

**Procedure:**
1. Set lin/exp to exp
2. Set Gain fully CCW, CV attenuator fully CW
3. Play a gate; the VCA opens with the envelope and closes when the gate ends
4. Adjust ENV attack and release to shape the volume contour
5. Compare: switch lin/exp to lin and play the same gate. Notice the more mechanical, less natural-sounding opening shape

**What to listen for:** The exponential curve makes the attack feel more immediate and the decay feel more gradual, closer to how acoustic instruments behave. The linear curve traces the exact envelope voltage shape, which is mathematically precise but often sounds slower to open and faster to close than the exponential equivalent.

---

### Patch 2: CV Depth Control (LFO Modulation Shaping)

**Goal:** Use the A-130-2 to control how deeply an LFO modulates a target, with that depth shaped by an envelope.

**Setup:**
```
LFO OUT               ---[C]---> A-130-2 IN (ch1)
ENV OUT               ---[C]---> A-130-2 CV (ch1)
A-130-2 OUT (ch1)     ---[C]---> Filter FM or VCO FM input
Gate                  ---[G]---> ENV GATE
```

**Procedure:**
1. Set lin/exp to lin (CV processing requires linear response)
2. Set Gain fully CCW, CV attenuator to 12 o'clock
3. Trigger the envelope; the LFO depth increases with the envelope's attack and fades with its release
4. The filter or oscillator receives LFO modulation only when the envelope is open

**What to listen for:** The LFO modulation swells in and out with the note shape instead of running continuously. This technique (a VCA on a modulation source rather than an audio source) is one of the most used techniques in Eurorack synthesis. The A-130-2's linear response in this application ensures the LFO depth tracks the envelope voltage accurately.

---

### Patch 3: Parallel Voice Management

**Goal:** Use both channels independently for two separate voices in one module.

**Setup:**
```
VCO 1 OUT             ---[A]---> A-130-2 IN (ch1)
ENV 1 OUT             ---[C]---> A-130-2 CV (ch1)
A-130-2 OUT (ch1)     ---[A]---> Mixer ch1

VCO 2 OUT             ---[A]---> A-130-2 IN (ch2)
ENV 2 OUT             ---[C]---> A-130-2 CV (ch2)
A-130-2 OUT (ch2)     ---[A]---> Mixer ch2
```

**Procedure:**
1. Set ch1 to exp for the melodic voice
2. Set ch2 to lin if ch2 is processing a CV signal, or exp if it is a second audio voice
3. Set both Gain knobs to the appropriate resting position
4. Both voices now operate completely independently through one 4HP module

**What to listen for:** Two independent amplitude-shaped voices in 4HP. This is the core use case for the Slim Line format: infrastructure density in systems where every HP matters.

---

## Common Mistakes

**Leaving the switch in the center mute position**  
The three-position switch has a fully silent center position. If a channel produces no output and CV and Gain both appear correct, check the switch. Center is mute, not a neutral default. This catches many experienced users off guard the first time.

**Expecting gain beyond unity**  
The A-130-2 amplifies up to 1× maximum. It cannot boost signal levels. If your source is too quiet, attenuate at a later stage or add a preamp before the VCA. Driving the CV above the 5V unity threshold does not increase the output level; the gain clips at 1×.

**Using exponential response for CV processing**  
The exponential curve compresses the relationship between CV voltage and gain in a way that makes CV signal processing unpredictable. If you are using the A-130-2 to attenuate or shape a CV signal (LFO depth, envelope depth, pitch CV scaling), always use the linear position. The exponential position is for audio amplitude shaping only.

**CV attenuator at zero wondering why nothing happens**  
With the CV attenuator fully counterclockwise, no CV reaches the VCA regardless of what is patched. The Gain knob then controls the level statically. If you want envelope-controlled amplitude, the CV attenuator must be open (clockwise). This interaction between Gain and CV attenuator confuses first-time users more than any other aspect of the module.

---

## Pairs Well With

**Any envelope generator:** The A-130-2's primary application is envelope-to-amplitude control. Any envelope in the system works; ADSR, function generator, or Zadar shapes all drive it cleanly.

**Maths or similar function generators:** A single Maths output driving A-130-2 CV on both channels independently (using both Maths outputs) covers two-voice amplitude control from a single source module.

**LFOs for CV depth control:** Patch any LFO into IN and an envelope into CV for dynamic modulation depth control on any target. This is the most productive non-obvious application of a simple VCA.

**Ground Control (Endorphin.es) or any sequencer:** A sequenced CV output into A-130-2's CV creates rhythmically shaped amplitude patterns. Each step's voltage becomes a gain level, producing rhythmic volume accents synchronized to the sequence.

---

## Advanced Learning Path

**Step 1: Internalize the lin/exp difference by ear**  
Patch a sustained drone through the VCA with a slow envelope. Switch between lin and exp while the envelope is running and listen to the gain curve change in real time. Do this until the difference is immediately audible without thinking about it.

**Step 2: Use VCAs on every modulation source**  
Identify every LFO or modulation signal in your current patch. Route each one through a VCA before its destination. Use envelopes or other CVs to control the modulation depth dynamically. This practice fundamentally changes how patches breathe and move.

**Step 3: Explore the mute position as a performance tool**  
In a live patch, use the center mute position to silence a channel instantly without disturbing any patch cables or CV settings. This is a clean, immediate gate that requires no additional modules.

**Step 4: Compare with Cloaks and Mingles**  
The Cloaks (After Later Audio) is a four-channel linear VCA with a different physical layout. Mingles adds CV-controlled panning. Comparing the A-130-2 against both reveals how the same fundamental function (voltage-controlled amplitude) maps to different design priorities and use cases across manufacturers.
