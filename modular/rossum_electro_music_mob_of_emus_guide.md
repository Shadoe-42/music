---
title: Rossum Electro-Music Mob of Emus
manufacturer: Rossum Electro-Music
primary_role: SOURCE
secondary_roles: [CONTROLLER]
historical_context: true
form_factor: eurorack
functions: [fm-oscillator]
behavior_tags: [harmonic, inharmonic, stable, performance-oriented, nonlinear]
use_cases: [lead voice, chord voice, complex FM texture, metallic percussion voice]
hp: 16
memory: full
transport: none
screen: true
hybrid: false
cv: full
---

# Rossum Electro-Music Mob of Emus

![Rossum Electro-Music Mob of Emus](https://github.com/Shadoe-42/music/raw/main/modular/images/rossum_electro-music/mob_of_emus/front_panel.jpg)

*Six-channel polyfunctional harmonic synthesis module: each channel independently configurable as oscillator, LFO, envelope, or trigger pattern generator, unified by a harmonic series architecture that makes mathematically coherent timbral and rhythmic relationships immediately accessible*

---

## Historical Context

Joseph Fourier proved in 1822 that any periodic waveform can be expressed as a sum of sinusoidal components at integer multiples of a fundamental frequency. This is not a claim about synthesis; it is a mathematical description of how all periodic sound works. The practical implication for instrument builders was immediate and vast: if any timbre is a weighted sum of harmonics, then a machine that controls the amplitude of each harmonic independently can produce any timbre at all. Thaddeus Cahill's Telharmonium, built between 1897 and 1906, was the first instrument to take this principle seriously at scale: a 200-ton electromechanical instrument that generated precise sinusoidal tones at harmonic frequencies and mixed them electrically, transmitting the result over telephone lines to subscribers in New York. The Telharmonium was impractical but theoretically complete. Laurens Hammond's Tonewheel Organ of 1935 made additive synthesis commercially viable by reducing the Telharmonium's enormous machinery to a compact set of spinning metal wheels, each generating one harmonic. The Hammond B3's nine drawbars are still the most direct physical implementation of additive synthesis available to a performer: nine sliders controlling nine harmonic amplitudes, the entire additive synthesis architecture in a wooden cabinet that fits on a stage.

The synthesis methods that followed in the late 20th century (FM synthesis, subtractive synthesis, wavetable) were in many ways responses to the computational cost of real-time additive synthesis. Controlling dozens of individual partial amplitudes simultaneously required more processing power than early analog and digital hardware could spare. FM synthesis, developed by John Chowning at Stanford in 1967, produced harmonically complex spectra from only two or three operators by exploiting the mathematical relationship between frequency modulation and the Bessel function distribution of sidebands. It was a shortcut that worked: the DX7 produced timbres that additive synthesis would have required ten times the hardware to generate directly. But FM is not additive synthesis; it approximates harmonic spectra indirectly. As digital processing became cheaper through the 1990s, true real-time additive synthesis became feasible in software. The remaining design challenge was performance interface: how to give a musician meaningful control over a six-oscillator harmonic stack without requiring them to set thirty-six independent parameters.

Dave Rossum co-founded E-mu Systems in 1971 with Scott Wedge in Santa Cruz, California. Over the next four decades, E-mu built several of the most commercially significant digital instruments in the history of recorded music. The Emulator (1981) was among the first affordable digital samplers, bringing sampling out of expensive studio systems and onto stages. The SP-1200 (1987) became a foundational tool of hip-hop production through its 12-bit sampling and compressed sound character, audible on a generation of recordings. E-mu's Proteus and Orbit synthesis engines provided the sample-based voices in tens of thousands of keyboards and rack units through the 1990s. Rossum left E-mu in 2014 when the company was absorbed into its parent organization, and founded Rossum Electro-Music. The stated goal was to bring the synthesis engineering depth he had developed over four decades into the Eurorack format, in the hands of a new generation of instrument builders and performers.

The Mob of Emus addresses the additive synthesis controllability problem directly. Rather than exposing six independent oscillators with six sets of parameters, the module organizes the six channels around a harmonic series system: 15 preset series derived from acoustic physics, musical mathematics, and rhythmic traditions provide immediate access to coherent harmonic relationships. In Hex mode, a single set of controls adjusts all six channels simultaneously while preserving their individual relationships. The same harmonic number architecture that governs additive synthesis timbres also governs polyrhythmic timing: a channel set to harmonic number 4 runs at four times the speed of a channel at harmonic number 1, whether that speed is in the audio range (producing a fourth harmonic partial) or the LFO range (producing a quarter-note pulse relative to a whole-note fundamental). This unified mathematical framework is the architectural insight that makes the module tractable: six channels of independent synthesis, organized by a system of relationships that musicians have understood for centuries.

---

## Quick Start

The Mob of Emus is six independently configurable synthesis channels sharing a harmonic series architecture. Each channel can operate as an audio oscillator, LFO, envelope, or trigger pattern generator, and the harmonic number system governs the relationship between them regardless of mode. Starting with a factory preset gives you a working patch before touching any deep programming.

1. Load Preset 1 ("Warp This") by pressing the Preset button and turning the encoder to position 1.
2. Connect the Mix output to a VCA or filter input.
3. Connect your sequencer or keyboard V/OCT to the Full CV input.
4. Play a note. You should hear a harmonically rich oscillator stack tracking pitch.
5. Turn the FREQ knob to adjust the overall pitch of all six channels simultaneously.
6. Hold the Option button and turn the HARM#/SERIES knob to cycle through harmonic series presets. Listen to how the timbral character of the mix changes as the harmonic relationships between channels shift.
7. Hold the Option button and turn the Variation/Warp knob to hear the frequency warping effect: slight clockwise movement from center adds chorus-like detuning across all channels.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 16 HP |
| Depth | 42 mm ⚠️ |
| Power | 130 mA +12V ⚠️ / 15 mA -12V ⚠️ / 0 mA +5V |

---

## Essential Parameters

The Channel Selector buttons choose which of the six channels is active for individual editing. When no channel is selected, knob movements apply only in Hex mode (affecting all channels simultaneously). When a channel is selected (its LED lit), knob movements affect only that channel. The LED chase pattern that appears when no channel is selected is the module indicating that individual edits are not active; clicking any channel button resolves it. This is the most common source of confusion for new users.

FREQ/FINE/SEMI sets the frequency of each channel. In its primary function, the FREQ knob sweeps pitch or rate across a broad range. Held with the Option button, it becomes a fine-tune control for precise detuning. Held with a second Option press, it steps in semitones for musical interval programming. OCTAVE/2X sets the octave range: high positive values place channels in the audio range; negative values bring them into LFO territory. The distinction between audio rate and LFO rate is entirely determined by OCTAVE: there is no separate mode switch. Setting some channels to audio rate and others to LFO rate simultaneously is a valid and musically useful configuration.

WAVE/ENV/PAT selects the operating mode of each channel. The primary bank (no button held) selects classic waveforms: sine, sawtooth, square, triangle, sample-and-hold. Held with Option, it selects envelope shapes: various attack-decay profiles and smoothed random. Held with a second Option press, it selects rhythm patterns: kick, snare, hi-hat, and clave trigger patterns derived from euclidean distributions. These three mode banks make the Mob of Emus effectively three different instruments sharing one set of controls.

HARM#/SERIES sets the harmonic number of the selected channel in individual mode: a multiplier from 1 to 32 that scales the channel's frequency relative to the module's base frequency. Setting channels to harmonic numbers 1, 2, 3, 4, 5, and 6 produces the natural harmonic series; setting them to 1, 3, 5, 7, 9, and 11 produces odd harmonics only, which have a hollow clarinet-like character. Held with Option in Hex mode, HARM#/SERIES cycles through 15 preset harmonic series that apply the chosen relationships to all six channels simultaneously. The 15 presets include natural harmonic series, powers of 2 (appropriate for 4/4 rhythmic relationships), 3/4 and 12/8 rhythmic series, Fibonacci series, and others derived from mathematical and acoustic traditions.

H.GAIN/MIX controls the amplitude of the selected channel. In Hex mode it functions as a harmonic gain control: turning it counterclockwise emphasizes channels with lower harmonic numbers (the fundamental and lower partials), while clockwise emphasizes higher-numbered channels. Held with Option in individual mode, it controls whether the channel's output is included in the Mix output; channels can be active and generating signal while excluded from the mix, making them available only on their individual outputs.

Hex mode, engaged by the HEX button, applies all subsequent knob movements as offsets to all six channels simultaneously without disturbing their individual settings. It is a conductor layer: the per-channel programming beneath Hex mode remains intact, and Hex mode adds relative adjustments on top of it. This is the primary performance interface for real-time control over complex patches: Hex mode FREQ sweeps all channels together in pitch, Hex mode H.GAIN shapes the harmonic balance of all six, Hex mode WAVE shifts all waveforms simultaneously.

The Variation and Warp controls add probabilistic and deterministic variation to the harmonic structure. Variation controls the probability of ratcheting (a channel briefly doubling its frequency) and dropping (a channel temporarily halving). Small clockwise amounts add rhythmic interest without disrupting the fundamental pattern; larger amounts produce increasingly chaotic results. Warp shifts all six channel frequencies in a non-linear spreading pattern: at 12 o'clock there is no effect; slight clockwise produces a chorus-like detuning; more clockwise spreads the channels further into a frequency-shift effect. The Warp sweet spot for additive synthesis use is a small amount clockwise.

---

## Why This Instrument Excels

The harmonic series architecture means the six channels are not independent oscillators that happen to share a module; they are voices in a mathematical relationship. Setting the six channels to any harmonic series produces timbral results that are acoustically coherent because the harmonic series is the same mathematical structure that makes acoustic instruments sound the way they do. A Hammond organ sounds different from a flute not because different oscillators are used but because the relative amplitudes of the same harmonic series are weighted differently. The Mob of Emus exposes this relationship directly: changing the harmonic series preset changes which partials are present, and the HARM# knob controls their exact ratios. The timbral results are musically intelligible in a way that six random oscillators are not, because the ear hears the harmonic relationships as part of a single instrument rather than as coincidental unison.

The three operating modes of each channel (oscillator, envelope, pattern generator) make the module genuinely three different instruments with three different musical applications. In WAVE mode it is an additive synthesis engine. In ENV mode it is a six-channel modulation source generating related but varied envelope shapes that evolve together. In PAT mode it is a polyrhythmic trigger generator that applies the same harmonic number relationships to rhythmic timing: a channel at harmonic number 4 fires four triggers for every one trigger from a channel at harmonic number 1. The fact that all three modes share the same HARM# architecture means that the mathematical relationship that governs timbre in oscillator mode governs rhythm in pattern mode. A musician who understands one mode understands the underlying logic of all three.

Hex mode addresses the performance interface problem of additive synthesis directly. Without it, shaping a six-oscillator patch in real time would require moving six independent knobs for every parameter change: sixty-knob movements to adjust FREQ, WAVE, and H.GAIN across all channels simultaneously. With Hex mode active, a single knob movement applies to all six channels at once, preserving their individual harmonic relationships while shifting the entire stack. The individual programming remains intact beneath the Hex layer: it is not overwritten but offset. This makes complex harmonic patches performable in real time by a single person without sacrificing the detailed programming that makes the patch interesting.

The CV input reassignment capability means the module's single CV input per channel is not fixed to one destination. Any of the channel CV inputs can be reassigned to modulate frequency, trigger, gain, waveform, variation, or quantizer function on that channel. In Hex mode, CV inputs can be assigned to affect all six channels simultaneously. This architecture turns a sixteen-parameter module into a sixty-parameter modulation destination without adding more jacks. A patch that uses only one or two external CV sources can still target the most musically relevant parameters for the current application, and those assignments survive as part of the preset memory.

---

## Patches

### Patch 1: Additive Synthesis Voice

This patch uses the natural harmonic series preset to build a complete additive synthesis voice with external pitch control.

```
[Sequencer]──V/OCT──[C]──▶ MOB Full CV In
[Envelope Gen] OUT──[C]──▶ VCA CV In
                           MOB Mix Out ──[A]──▶ VCF In
                           VCF Out ──────[A]──▶ VCA In
                                               VCA Out ──[A]──▶ [Mixer]
```

**Setup:** Connect a sequencer V/OCT to the Full CV input. Connect an envelope generator output to a VCA control input. Route the Mix output through a filter into the VCA.

**Controls:** Load Preset 1 or configure manually: engage Hex mode, select the "All" harmonic series preset (1, 2, 3, 4, 5, 6) using Option + HARM#/SERIES. Set OCTAVE to place all channels in the audio range. Set WAVE to sine on all channels for clean additive synthesis, or sawtooth for a brighter starting timbre. Turn Hex mode H.GAIN counterclockwise to emphasize the fundamental; clockwise to bring up higher partials. Slight clockwise Warp adds a subtle chorus quality without disturbing pitch accuracy. Apply the envelope to the VCA for shaped amplitude.

**Result:** A harmonically rich, pitched voice where the balance between fundamental and overtones is controllable in real time through a single Hex mode H.GAIN movement. The natural harmonic series produces a timbre with the characteristic warmth of acoustic instruments: each partial is a whole-number ratio above the fundamental, so the combined tone sounds unified rather than dissonant.

---

### Patch 2: Polyrhythmic Modulation Bank

This patch repurposes the six channels as a synchronized polyrhythmic LFO bank using the Powers of 2 harmonic series.

```
[Clock/Tap] ──────── [G]──▶ MOB Tap/Trig In
                           MOB Ch1 Out ──[C]──▶ [VCF Cutoff CV]
                           MOB Ch2 Out ──[C]──▶ [VCA CV]
                           MOB Ch3 Out ──[C]──▶ [LFO Rate CV]
                           MOB Ch4 Out ──[C]──▶ [Reverb Send]
                           MOB Ch5 Out ──[C]──▶ [Oscillator FM]
                           MOB Ch6 Out ──[C]──▶ [Second VCA CV]
```

**Setup:** Connect a clock or tap the Tap/Trig button to set the master tempo. Connect the six individual channel outputs to six different modulation destinations across the patch. No audio output from this patch; Mob of Emus operates entirely as a modulation source.

**Controls:** Engage Hex mode and select the "Powers of 2" harmonic series: {1, 2, 4, 8, 16, 32}. Set OCTAVE for all channels into LFO range (around -3 to -4). Channel 1 runs at the fundamental tempo; channel 2 at double speed; channel 3 at quadruple; and so on through six orders of magnitude. Set WAVE to triangle for smooth LFO shapes, or square for rhythmic gate-like modulation. The six modulation destinations will now change at six related but different rates, all locked to the master tempo.

**Result:** A synchronized modulation matrix where every parameter changes at a musically related rate. Unlike six independent LFOs, the polyrhythmic relationships between the six channels are exact and non-drifting because they share a common clock. Slight Variation clockwise adds probabilistic skips and ratchets that prevent the modulation from sounding mechanical.

---

### Patch 3: Mixed Audio and LFO Channels

This patch demonstrates the power of operating some channels in audio range and others in LFO range simultaneously within the same harmonic framework.

```
[Sequencer]──V/OCT──[C]──▶ MOB Full CV In
                           MOB Ch1 Out ──[A]──▶ VCF In (audio oscillator, H# 1)
                           MOB Ch2 Out ──[A]──▶ VCF In (audio oscillator, H# 2)
                           MOB Ch3 Out ──[A]──▶ VCF In (audio oscillator, H# 3)
                           MOB Ch4 Out ──[C]──▶ VCF Cutoff CV (LFO, H# 4)
                           MOB Ch5 Out ──[C]──▶ VCA CV (envelope, H# 1)
                           MOB Ch6 Out ──[C]──▶ Reverb Send (LFO, H# 3)
VCF Out ──────────── [A]──▶ VCA In
                           VCA Out ──[A]──▶ [Mixer]
```

**Setup:** Set channels 1, 2, and 3 to audio rate using OCTAVE (+2 to +4 range), WAVE mode with different waveforms. Set channels 4 and 6 to LFO rate (OCTAVE -2 to -3), and channel 5 to ENV mode for amplitude shaping. Route audio channels to a filter input and control channels to their respective destinations.

**Controls:** Set the harmonic numbers for channels 1, 2, and 3 to 1, 2, and 3 for a three-partial additive stack. Set channel 4's harmonic number to 4: it will now move at four times the LFO frequency of a channel at H#1, making the filter cutoff variation rhythmically related to the audio content. Set channel 5 to ENV mode for a natural envelope shape on the VCA.

**Result:** A voice where the LFO modulations are harmonically related to the audio content because they share the same harmonic number system. A filter LFO at four times the pitch LFO rate produces a subtle but perceptible rhythmic relationship between pitch and filter movement that does not occur when LFO rates are set independently.

---

### Patch 4: Generative Harmonic Voice with Marbles

This patch uses Mutable Instruments Marbles to drive pitch and trigger inputs while Mob of Emus handles harmonic timbre and the modulation of the mix.

```
MARBLES X1 ──────── [C]──▶ MOB Full CV In
MARBLES t1 ──────── [G]──▶ MOB Tap/Trig In
[Slow LFO] ──────── [C]──▶ MOB H.GAIN CV (Hex mode)
                           MOB Mix Out ──[A]──▶ VCF In
[Envelope] ──────── [C]──▶ VCA CV In
VCF Out ──────────── [A]──▶ VCA In
                           VCA Out ──[A]──▶ [Mixer]
```

**Setup:** Connect Marbles X1 to the Full CV input for pitch tracking, Marbles t1 to Tap/Trig for rhythmic excitation. A slow LFO goes to the H.GAIN CV input with Hex mode engaged; an envelope generator triggered by Marbles t1 drives the VCA.

**Controls:** Load Preset 1 or configure an additive synthesis patch as in Patch 1. Set Marbles to generate quantized melodic content from X1 and rhythmic gate patterns from t1. In Hex mode, the LFO on H.GAIN slowly shifts the harmonic balance of the mix over time: over long periods the timbre thickens as upper harmonics are boosted, then thins back as they recede. Adjust Marbles DEJA VU to control the degree of melodic repetition. Try switching harmonic series presets in real time while the sequence plays.

**Result:** A generative harmonic voice where the pitch content comes from Marbles' controlled randomness and the timbral evolution comes from the slow harmonic balance shift. The patch runs largely without intervention once established, with the harmonic series preset as the primary real-time performance control.

---

## Common Mistakes

### "Nothing is coming out of the Mix output"

Each channel must be explicitly included in the Mix output. In Individual mode, hold Option and turn H.GAIN/MIX clockwise from center to include the selected channel. If the knob is at center or counterclockwise, the channel is excluded from the mix and appears only on its individual output jack. This is intentional: individual outputs and the Mix output are independent routing destinations. Check each channel with the channel selector and confirm the include status before assuming the module is not producing audio.

### "I am turning knobs and nothing is changing"

Two distinct causes produce this symptom. First: in Individual mode, no channel is selected for editing. Click any Channel Selector button to select a channel; the module confirms selection by stopping the LED chase pattern. Second: knob positions after loading a preset do not match the saved values, and parameters only update when the physical knob reaches the saved value (pickup behavior). A knob that is at the wrong position does nothing until it crosses the stored value. The screen shows the current stored value; move the knob toward it and observe when the displayed value begins to change.

### "My CV input is patched but it is modulating the wrong thing"

The CV input destination is assignable per channel and persists as part of preset memory. The default assignment may not match your intended use. To reassign: hold Option and double-click the Preset button while a channel is selected, then choose the new destination from the assignment menu. Available destinations include FREQ, TRIG, GAIN, WAVE, VARIATION, and the external quantizer. In Hex mode, the assignment can control the same parameter across all six channels simultaneously. If a preset was saved with a non-default assignment, the assignment came with the preset.

### "The Warp control is sending all my channel pitches to the same frequency"

Turning Warp fully counterclockwise causes all channel frequencies to converge toward channel 1's frequency. This is the designed behavior of the Warp function at the counterclockwise extreme: it sweeps all channels toward the fundamental. At 12 o'clock there is no warping effect. The useful range for additive synthesis use is 12 o'clock to about 1 o'clock, where the effect adds subtle chorusing. Full counterclockwise is a performance technique for dramatic timbral collapse, not a default operating position.

### "The Variation control is making my rhythmic patterns fall apart"

Variation introduces probability-based ratcheting and dropping into channel outputs. At small amounts it adds musical interest; at higher amounts it disrupts the timing relationships significantly. The control is not a subtle adjustment: a small clockwise turn produces audible rhythmic variation, and a moderate turn produces frequent tempo disruptions. For tight rhythmic applications, leave Variation at center or just slightly clockwise. Reserve higher Variation settings for intentional textural use rather than as a default setting.

---

## Advanced Learning Path

1. Start with a single oscillator in WAVE mode. Run a sine wave, tune it to a root, and listen to how the 15 harmonic series presets change the spectral structure by themselves. The goal is to hear what harmonic ratios do to timbre before any complex programming. This is the foundation everything else rests on.

2. Understand the difference between WAVE, ENV, and PAT modes. These three modes make the six-channel bank do three fundamentally different things: static timbre generation, envelope-driven dynamics, and euclidean gate patterns respectively. They are three separate instruments sharing one module. Master each independently before combining them.

3. Use PAT mode as a polyrhythmic gate source driving external destinations. The euclidean gate outputs in PAT mode can trigger envelope generators, VCAs, or other modules rather than producing audio. Patching the gate outputs to external destinations turns the Mob of Emus into a rhythmic control center. Set the six channels to different harmonic numbers in PAT mode and feed the individual outputs to six different envelope generators for a complete polyrhythmic modulation system from a single clock source.

4. Study the HARM# and SERIES control to develop fluency with the preset harmonic relationships. The 15 preset series are not arbitrary; they correspond to acoustic, mathematical, and rhythmic structures. Work through each preset while the module is producing audio and identify which series produces which timbral character. Odd harmonics produce a hollow, clarinet-like tone. Powers of 2 produce a sharp, sawtooth-wave equivalent. Fibonacci series produces an unusual, slightly inharmonic timbre with a characteristic mathematical strangeness.

5. Explore the external quantizer function. The Mob of Emus can accept an external CV and quantize it to the current harmonic series as a set of pitches. This turns the harmonic number relationships into a scale: feeding a random or sequenced CV through the quantizer function maps incoming notes to harmonically related intervals. The resulting melodic content has an inherent harmonic coherence with whatever additive synthesis timbre the module is also producing, because both are derived from the same harmonic series.

6. Build a complete self-contained harmonic voice using only the Mob of Emus as source, envelope, and pitch reference. V/OCT into Full CV, ENV mode on one channel for amplitude shaping, WAVE mode on the remaining channels for audio. Route the Mix output through an external filter and VCA controlled by the ENV channel output. If the resulting voice has clear character and internal harmonic logic, the module is understood at depth.

7. Explore CV input reassignment deliberately. Choose a patch and reassign the CV inputs to targets that are not the defaults: put CV on VARIATION for one channel, on WAVE for another, on GAIN for a third. Understand how CV modulation of these parameters changes the patch behavior. The reassignment system is the most underexplored area of the module and provides the most direct path to patches that could not be made any other way.

8. Combine audio-rate and LFO-rate channels in the same harmonic series. Set channels 1, 2, and 3 to audio rate with harmonic numbers 1, 2, and 3 for an additive timbre. Set channels 4, 5, and 6 to LFO rate with harmonic numbers 4, 5, and 6. The LFO rates will be mathematically related to the audio rates by the same integer ratios: LFO channel 4 moves at four times the LFO channel 1 rate, just as audio channel 4 is the fourth harmonic of audio channel 1. Route the LFO outputs to synthesis parameters and listen for the rhythmic relationship between the modulation and the audio content.

---

## Pairs Well With

**Mutable Instruments Plaits** provides a single-module synthesis voice that covers the timbral range Mob of Emus does not: FM, wavetable, granular, and speech synthesis models alongside its own complex oscillator mode. The two together cover nearly every synthesis method without significant overlap. Mob of Emus' Mix output driving Plaits' FM input produces additive-synthesis-modulated FM, where the harmonic content of the additive stack shapes the sidebands of the FM synthesis. Individual channel outputs from Mob of Emus driving Plaits' HARMONICS, TIMBRE, and MORPH CV inputs create a coordinated modulation architecture where all three parameters change at harmonically related rates.

**Make Noise Maths** handles the function generation and envelope processing that Mob of Emus' ENV mode initiates but does not finish. Maths channels in envelope mode, triggered by Mob of Emus PAT mode gate outputs, produce shaped amplitude and timbral events with the logarithmic, physical curve character that Maths' analog circuitry provides. Maths' end-of-rise outputs fed back into Mob of Emus Tap/Trig create recursive timing relationships where Maths envelope duration determines the next trigger time. The combination produces self-referential timing structures that neither module can produce alone.

**Mordax Data** provides real-time visualization of the six-channel harmonic content. Connecting individual Mob of Emus channel outputs to Mordax Data's analysis inputs while programming harmonic series makes the mathematical relationships visible: the spectral display shows each harmonic partial at its correct frequency position, and changes to HARM# settings produce immediately visible shifts in the partial structure. For a module whose primary design feature is harmonic mathematics, having a visual analysis tool available is not a luxury; it accelerates learning and confirms that the programming is producing the intended harmonic relationships.

**4ms Company RCD v2** provides clock division that integrates cleanly with Mob of Emus' Tap/Trig-based polyrhythmic architecture. Where Mob of Emus generates six outputs from one clock via harmonic number ratios, the RCD generates eight clock divisions from one clock via mathematical division. Feeding the RCD's output into Mob of Emus Tap/Trig, or vice versa, creates timing systems where the two modules' mathematical frameworks interact: RCD divisions trigger Mob of Emus to advance, while Mob of Emus PAT mode outputs drive RCD reset inputs. The result is polyrhythmic structures whose period and internal relationships change as the two modules' cycles drift in and out of alignment.

**Mutable Instruments Marbles** provides controlled random pitch and gate generation that feeds the Mob of Emus' harmonic synthesis without overriding its mathematical internal structure. Marbles' quantized X output tracks the Full CV input, placing the harmonic stack in different pitch contexts while preserving the internal harmonic relationships. Marbles' t output drives Tap/Trig, so the rhythmic timing of the harmonic progression comes from a controlled random source rather than a strict clock. The DEJA VU control on Marbles shapes how much the pitch and rhythm material repeats, giving the generative patch a degree of compositional structure without removing its variability.

---

*Official documentation: [Rossum Electro-Music Mob of Emus](http://www.rossum-electro.com/products/mob-of-emus/)*
