---
title: Doepfer A-124 Wasp SE
manufacturer: Doepfer
primary_role: SHAPER
secondary_roles: [SOURCE]
form_factor: eurorack
functions: [filter]
behavior_tags: [dirty, warm, harmonic, nonlinear, unstable]
use_cases: [timbral movement and shaping, dirty filter character, lead voice when self-oscillating]
hp: 8
---

# Doepfer A-124 Wasp SE

**CMOS Filter with Self-Oscillation**

![Doepfer A124 Wasp SE](https://github.com/Shadoe-42/music/raw/main/modular/images/doepfer/a_124_wasp_se/front_panel.jpg)  
*Doepfer A-124 Wasp SE: recreation of the Electronic Dream Plant Wasp filter circuit, 8HP*

---

## Historical Context

Chris Huggett and Nick Eastwood founded Electronic Dream Plant in England in the mid-1970s and released the EDP Wasp synthesizer in 1978 at a retail price of approximately £199. That price point was considerably lower than competing instruments of the era, and the cost reduction came from an unconventional design choice: where analog synthesizers of the time used precision components (Curtis or SSM filter chips, or discrete transistor ladder circuits), the Wasp used CMOS digital logic chips, specifically 4007 series inverters, operated at the edge of their linear region to function as voltage-controlled filter elements. The filter was not a ladder filter. It was a CMOS filter, and the distinction matters because everything distinctive about its sound comes directly from that topology.

CMOS inverters are not precision linear devices. They clip asymmetrically, they saturate at relatively low voltage levels, and their behavior changes nonlinearly with input signal level. Running them in a filter application produces a circuit that colors audio in ways that precision linear components are specifically designed to avoid: odd-order harmonics from asymmetric clipping, saturation that adds grit and density at higher input levels, and self-oscillation with an irregular character that sits between a pure sine and something rougher. The Wasp's sonic identity was not designed in; it emerged from the imprecision of components doing something they were not engineered to do. This is a meaningful distinction from distortion circuits or analog saturation stages that are deliberately designed to add harmonic content. The Wasp filter adds character as a byproduct of its architecture.

Chris Huggett went on to co-design the OSCar synthesizer (1983) for the Oxford Synthesiser Company, another British instrument that became highly regarded. The Wasp itself was affordable enough that it reached musicians who could not access more expensive instruments, and the filter's character became part of a particular strand of British electronic music production across the late 1970s and 1980s.

Doepfer Musikelektronik, the German company responsible for establishing the Eurorack format in 1995, produced the A-124 as a faithful circuit recreation of the EDP Wasp filter topology. Dieter Doepfer's approach to the Eurorack format was rooted in affordability and accessibility, the same design philosophy that produced the original Wasp, and the A-124 preserves the CMOS nonlinearity of the original circuit rather than substituting a cleaner or more conventional filter design. The module sounds like the original because it uses the same fundamental circuit approach.

---

## Quick Start

**What is the Wasp SE?** A recreation of the EDP Wasp's CMOS filter circuit: nonlinear, dirty-sounding, and capable of self-oscillation at high resonance. It does not aim for transparency; it adds character to whatever passes through it.

### Your First Wasp Sound

1. Connect an oscillator or audio source to the audio input
2. Connect the audio output to a VCA or mixer
3. Set Cutoff to noon
4. Slowly advance Resonance clockwise; the filter becomes more aggressive and eventually self-oscillates
5. Sweep Cutoff while Resonance is high to hear the classic Wasp character

---

## Key Specifications

| Parameter | Value |
|-----------|-------|
| Width | 8HP |
| Depth | 30mm |
| Power | 30mA +12V, 10mA -12V, 0mA 5V |
| Filter topology | CMOS inverter-based (not ladder) |
| Cutoff range | 20Hz to 20kHz |
| Self-oscillation | Yes; tracks 1V/octave for melodic use |
| CV inputs | Cutoff CV (two inputs with attenuators); Resonance CV |
| Audio output | Approximately ±5V |

---

## Essential Parameters

The Cutoff knob sets the frequency at which the filter begins attenuating audio. Below the cutoff, frequencies pass through with minimal attenuation; above it, frequencies are progressively reduced. The full range covers the audible spectrum from 20Hz to 20kHz. The CMOS topology means the filter is not neutral at any setting: even with cutoff fully open, the circuit imparts a subtle color on the signal rather than passing it transparently.

Resonance controls the amount of emphasis applied to frequencies near the cutoff point. At low settings, the filter adds a mild presence peak around the cutoff. As resonance increases, the peak becomes more pronounced and the filter character becomes increasingly aggressive. At high resonance settings, the filter enters self-oscillation: it begins generating its own tone at the cutoff frequency without any input audio needed. This self-oscillating tone tracks pitch via the 1V/octave input, making the filter usable as a sine-wave oscillator. The self-oscillation character of the Wasp is not a clean sine; the CMOS topology gives it a slight roughness that distinguishes it from oscillator-based sine generation.

The Level control sets how hard the audio signal drives the filter input. Because the CMOS inverters saturate at relatively low voltages, input level is not a passive gain control; it directly shapes how the filter clips and saturates. At low input levels, the filter applies relatively clean (by Wasp standards) frequency shaping. As the input level increases, the CMOS clipping becomes more prominent, adding harmonic content and grit that compounds with the filter's existing character. Hot signals drive the CMOS chips into saturation earlier in the signal path, producing a denser, more distorted texture. This input-level sensitivity is a deliberate feature of the original circuit and an important performance variable.

The two Cutoff CV inputs each have their own attenuator knob. Both sum into the cutoff frequency, so multiple modulation sources can be applied simultaneously at individually set amounts. The Resonance CV input accepts external voltage to modulate resonance amount dynamically.

---

## Why Wasp SE Excels

The central argument for the Wasp SE is its topology. Most filters in Eurorack are designed to be transparent at neutral settings and to add controlled, predictable character when pushed. The Wasp SE does not have a neutral setting. The CMOS inverter circuit colors the signal at every point in the control range, which means there is no "clean" version of the Wasp sound and no need to push it into extremes to get character. A moderate cutoff with moderate resonance and moderate drive produces an immediately identifiable texture. The Wasp SE earns its place in a system not as a general-purpose filter that can do everything, but as a character filter with a specific sonic identity that is available at all times and not just at extremes.

Self-oscillation on the Wasp SE is a usable sound source, not a byproduct to be avoided. At high resonance with no audio input, the filter generates a tone at the cutoff frequency that responds to 1V/octave pitch voltage, which allows it to function as a second voice or a doubling oscillator with a different timbral character than a conventional VCO. The self-oscillating tone has the CMOS roughness of the filter topology: it is not a pure sine but something between a sine and a slightly saturated waveform. For melodic lines that benefit from that texture, including acid basslines, filter-lead material, and simple one-note sequences, the self-oscillating Wasp is a practical sound source independent of any oscillator module.

The input level sensitivity creates a performance variable that most filters do not offer in the same direct form. Because the CMOS chips saturate at relatively low voltages, driving the input harder does not simply make the output louder; it changes the degree of saturation and therefore the harmonic content and character of the filtered signal. This makes the Level control a timbral shaping tool as much as a gain control. Patching a VCA before the Wasp input and controlling that VCA with an envelope or LFO produces dynamic timbral evolution through input-level modulation rather than through cutoff or resonance movement. The three modulation axes (cutoff, resonance, and input level) are meaningfully different in character from each other, which means the Wasp SE responds to complex modulation in ways that produce genuinely varied sonic results rather than multiple versions of the same filter sweep.

The 8HP footprint and the A-124's price position it as a character addition to an existing system rather than a primary filter requiring dedicated supporting infrastructure. It covers filter, self-oscillating sine-wave oscillator, and saturation processor in 8HP. A system that already has a cleaner or more surgical filter benefits from the Wasp SE as a second voice with a distinct character, not a replacement for precision filtering but a complement to it.

---

## Patches

### Patch 1: Classic Filter Envelope Sweep

This patch establishes the foundational Wasp workflow: an oscillator as audio source, an envelope shaping the cutoff frequency over time.

```
[Oscillator] ──────────▶ Audio In
[Gate Source] ─────────▶ [Envelope] ──▶ Cutoff CV 1
                          Audio Out ──▶ [VCA] ──▶ [MixUp or Output]
```

**Setup:** Connect an oscillator with a harmonically rich waveform (sawtooth or square) to the audio input. Set Level to around noon. Connect a gate source to an envelope generator and route the envelope output to Cutoff CV 1. Patch the Wasp output through a VCA to a mixer or output module.

**Controls:** Set Cutoff to around 9 o'clock (relatively closed). Set Resonance to 1 o'clock for Wasp character without self-oscillation. Set Cutoff CV 1 attenuator to around 2 o'clock. Trigger the envelope: the filter opens as the envelope rises and closes as it falls. Increase Resonance to 2 o'clock and listen to how the peak at the cutoff frequency becomes more pronounced during the filter opening phase. Vary Level between 9 o'clock and 3 o'clock to hear how CMOS saturation interacts with the envelope sweep; higher Level makes the saturation more prominent as the filter opens.

**Result:** The classic filter sweep sound with Wasp character: each triggered note opens the filter, revealing harmonics with a specific CMOS texture that distinguishes it from ladder or state-variable filter sweeps on the same source.

---

### Patch 2: Self-Oscillating Lead

This patch uses the filter as the sole sound source by driving it into self-oscillation and controlling the pitch via a sequencer's 1V/octave output.

```
[Sequencer CV Out] ──▶ Cutoff CV 1
                        (no audio input)
                        Audio Out ──▶ [VCA or direct to MixUp]
```

**Setup:** Connect a sequencer's 1V/octave output to Cutoff CV 1. Leave the audio input unpatched. Set Resonance to fully clockwise or near fully clockwise until the filter self-oscillates (a clear tone appears from the output). Set Level to minimum since there is no audio to drive.

**Controls:** Set the Cutoff CV 1 attenuator to around 2 o'clock and step through the sequencer. The self-oscillating tone tracks the pitch sequence. Adjust the base Cutoff knob to set the pitch register of the self-oscillating tone in relation to the rest of the patch. Back off Resonance slightly if the tone sounds too rough; the threshold between self-oscillation and stability is narrow, and the character of the self-oscillating tone changes across that range. If audio is present at the input, self-oscillation competes with it and becomes unreliable; keep the audio input unpatched for clean pitch tracking.

**Result:** A single-voice melodic lead produced entirely by the filter. The self-oscillating tone has the CMOS texture of the Wasp circuit: not a pure sine, but a slightly rough, slightly harmonically complex waveform that has a character of its own distinct from oscillator-generated material.

---

### Patch 3: CMOS Saturation Processor

This patch uses the Wasp SE primarily as a saturation and character processor rather than as a sweep filter, with cutoff held open and Level used as the primary timbral control.

```
[Mutable Plaits or Instruo Cs-L] ──▶ Audio In
[Slow LFO] ────────────────────────▶ Cutoff CV 1
                                      Audio Out ──▶ [MixUp]
```

**Setup:** Connect a harmonically rich source to the audio input: Plaits in a complex synthesis model or Cs-L with wavefolding active. Connect a slow LFO to Cutoff CV 1. Set the Cutoff CV 1 attenuator low (9 to 10 o'clock) so the LFO produces gentle cutoff movement rather than full sweeps.

**Controls:** Set Cutoff to 3 o'clock (mostly open). Set Resonance to 11 o'clock (mild character without self-oscillation). Now focus on Level: advance it from minimum to maximum slowly and listen to how the CMOS saturation changes the sound at each position. Below noon, the filter adds subtle harmonic color. Above noon, the saturation becomes increasingly present, adding density and grit. The slow LFO on Cutoff adds gentle spectral movement on top of the saturation character. The Wasp in this configuration is not functioning as a traditional filter sweep tool; it is functioning as a CMOS character processor that adds a specific kind of harmonic distortion to whatever passes through it.

**Result:** A source signal that has been transformed by CMOS saturation rather than by frequency sculpting. The Wasp's character is most apparent when the input signal is complex: the saturation interacts with the harmonic content of the source differently at different frequency components, producing a result that is richer than simple broadband distortion.

---

### Patch 4: Dual Modulation Sweep

This patch modulates both Cutoff and Resonance simultaneously from two independent sources, using the interaction between the two parameters to produce complex filter movement.

```
[Oscillator] ──────────────────────▶ Audio In
[Envelope or Function Generator] ──▶ Cutoff CV 1
[Slow LFO] ────────────────────────▶ Resonance CV
                                      Audio Out ──▶ [MixUp or Output]
```

**Setup:** Connect an audio source to the input. Route an envelope or function generator output to Cutoff CV 1. Route a slow LFO to the Resonance CV input. Connect the output to a mixer.

**Controls:** Set base Cutoff to 9 o'clock. Set base Resonance to noon. Set Cutoff CV 1 attenuator to 2 o'clock. Set the LFO rate to 0.2 to 0.5 Hz for slow resonance movement. Trigger the envelope: the cutoff opens dynamically while the LFO simultaneously moves resonance between a mild and aggressive setting. At moments when the envelope peak coincides with the LFO pushing resonance toward self-oscillation, the filter becomes most aggressive. At moments when the envelope has decayed and the LFO has pulled resonance back, the filter is at its most subdued. The character at each moment depends on the phase relationship between the two modulation sources.

**Result:** Filter behavior that varies across two independent axes simultaneously, producing a range of textures within a single patch. The interaction between envelope-driven cutoff movement and LFO-driven resonance movement is the core of sophisticated filter performance: each parameter modulated separately produces predictable results, but modulating both produces combinations that neither parameter alone can create.

---

## Common Mistakes

### "I cannot dial in a clean sound; everything through the Wasp sounds dirty"

The CMOS filter topology produces harmonic coloration at all settings. There is no bypass mode, and there is no neutral position where the circuit passes audio transparently. The Wasp SE is not a precision filter that can be switched between character and clarity; it is a character filter at all times. Expecting it to pass a clean signal is working against its design.

**Fix:** Use the Wasp SE where its character is a contribution, not a problem. For clean filtering, use a different module. For audio where CMOS saturation and the Wasp's frequency coloring add something, use the Wasp. Treating the character as a limitation misidentifies it as a flaw; it is the instrument's entire sonic identity.

---

### "I cannot get stable self-oscillation while playing audio through the filter"

Self-oscillation and audio input compete for dominance in the filter circuit. At high audio input levels, the input signal suppresses the self-oscillating tone. At low audio levels, self-oscillation may appear but will be masked. Consistent melodic self-oscillation requires either no audio input or a very low-level input that does not override the resonance feedback loop.

**Fix:** For melodic self-oscillation, remove the audio input entirely. The filter will generate a tone from its own feedback at high resonance settings, trackable via the Cutoff CV 1V/octave response. For a blend of self-oscillation and a processed audio signal, attenuate the audio source heavily before the input; the self-oscillation will be audible but the patch will be sensitive to Level adjustments.

---

### "The filter stops responding when I increase the Level control too far"

Excessive input level drives the CMOS inverters fully into saturation, at which point they clip the input signal rather than filter it. The filter's frequency-shaping behavior depends on the CMOS chips operating in their partially-linear region. When the input is too hot, the chips are operating in full saturation and the cutoff and resonance controls have diminishing effect on the output character; the output becomes a clipped, compressed version of the input regardless of filter settings.

**Fix:** Reduce Level to the point where filter cutoff and resonance changes produce audible results in the output. For most sources, this is between 9 o'clock and 2 o'clock on the Level control. If the source signal is very hot, attenuate it before the Wasp input rather than relying on the Level control to manage it.

---

### "The self-oscillating pitch is not tracking my sequencer accurately"

Self-oscillation pitch tracking depends on the accuracy and cleanliness of the CV source. The filter's 1V/octave response is in the Cutoff CV input; any noise, offset voltage, or scaling error in the CV source translates directly to pitch tracking error. Multiple CV signals summing at the Cutoff CV inputs (such as a manual cutoff offset plus a pitch CV) will produce pitch that is offset by the non-pitch CV contribution.

**Fix:** Use only one Cutoff CV input for pitch control when using the filter as an oscillator, and set the attenuator on that input carefully. Verify the CV source with a tuner or tuned oscillator before patching it to the Wasp. Set the base Cutoff knob to set the register and leave it; do not use the Cutoff knob as a transpose while also using CV for pitch, as the knob adds an unscaled offset to the tracked pitch.

---

## Advanced Learning Path

1. Work through Resonance systematically at a fixed Cutoff position before introducing CV modulation. Set Cutoff to noon and advance Resonance slowly from minimum to maximum in small increments, stopping at each position to identify the character change. Note where the filter peak becomes audible, where it begins to dominate the source signal, where self-oscillation begins, and where the self-oscillating tone stabilizes. The Wasp's Resonance range covers meaningfully different behaviors across its travel, and knowing those zones by ear is the prerequisite for using Resonance musically rather than accidentally.

2. Study the Level control as a timbral parameter, not a gain control. Patch a steady-state tone (a sustained oscillator with no envelope, or a drone) into the audio input. Hold Cutoff and Resonance constant and sweep Level from minimum to maximum slowly. Listen to what changes at each Level position: the onset of CMOS saturation, the increase in harmonic density, the point where the saturation begins to compress the dynamic character of the input. This is a different kind of timbral control from cutoff and resonance, and understanding its sonic territory before using it in a patch prevents the common mistake of accidentally driving it into full saturation.

3. Use the filter as a self-oscillating oscillator in a complete patch before relying on it as a filter. Patch the self-oscillating Wasp into a VCA with an envelope, connect a sequencer to Cutoff CV 1, and build a monophonic patch that uses only the Wasp as its sound source. The goal is to internalize the self-oscillating tone's character and how it tracks pitch, so that in future patches you can make an informed choice between using the Wasp as a filter on another source versus using it as an independent voice.

4. Compare envelope-to-cutoff modulation against LFO-to-cutoff modulation on the same patch. With an oscillator running through the Wasp, first use an envelope on Cutoff CV 1 and listen to the triggered, transient-style filter movement. Then replace the envelope with a slow LFO at the same modulation amount and listen to the cyclic, continuous filter movement. Then run both simultaneously through the two Cutoff CV inputs at reduced attenuator levels. The combination of triggered and cyclic filter modulation is one of the core filter performance techniques, and the Wasp's character makes the difference between the two modulation types distinctly audible.

5. Listen to the Wasp on source material that is not a standard sawtooth or square oscillator. Run a granular processor output through it. Run a complex oscillator with active wavefolding through it. Run a drum sound through it. The CMOS topology interacts with harmonic content in the source rather than simply removing frequencies, and sources with complex or evolving harmonic content produce different results from the Wasp than simple waveforms do. Understanding the filter as a character processor for complex sources, not just a cutoff control for simple oscillators, expands the practical use cases considerably.

6. Practice self-oscillation as a performance technique. Set the filter to just below the self-oscillation threshold and then manually advance Resonance past the threshold during a running patch. Note how quickly the self-oscillating tone appears, how stable it is, and how the pitch changes as you adjust Cutoff while self-oscillating. Then back Resonance off below the threshold again. The transition into and out of self-oscillation is a performance gesture with musical applications beyond simply using the Wasp as a fixed-resonance filter or a fixed-resonance oscillator.

---

## Pairs Well With

**Mutable Instruments Plaits** is a practical audio source for the Wasp SE because its synthesis models vary in harmonic complexity in ways that interact differently with the CMOS topology. Plaits in a wavetable or FM model produces source material that the Wasp's asymmetric saturation treats differently than a simple sawtooth; the saturation interacts with the spectral content of the wavetable or FM sidebands rather than just with harmonics of a fixed waveform. Patching Plaits' main output into the Wasp audio input and using Plaits' 1V/OCT input alongside the Wasp's self-oscillation tracking input from the same pitch source creates a configuration where both the source and the filter character respond to the same pitch sequence, keeping timbral changes harmonically related.

**Cre8audio Function Junction** provides the most immediate modulation pair for the Wasp SE. Function Junction's ADSR output routes to Cutoff CV 1 for triggered filter sweeps; its function generator output, with CURVE shaping, routes to Cutoff CV 2 for a second, differently-shaped envelope modulating the same destination. The two Cutoff CV inputs with separate attenuators allow the ADSR and function generator contributions to be balanced independently, so the filter opening shape is a combination of two envelope characters rather than one. Function Junction's LFO triangle output routes to Resonance CV for slow resonance movement layered on top of the cutoff modulation. Three modulation sources, three Wasp CV targets, from a single module.

**Xaoc Zadar** is the CV source that most fully explores the Wasp SE's dual-cutoff-CV architecture. Zadar's four independent function generators each produce a configurable envelope shape with its own loop behavior and CV control. Two Zadar channels route to the two Cutoff CV inputs for compound cutoff modulation with independent shapes and rates; a third Zadar channel routes to Resonance CV for independently timed resonance movement. The fourth Zadar channel can address a downstream element or loop back to Level if that input accepts CV in the specific A-124 variant. With all four channels set to different curve shapes and loop times, the Wasp operates under four-axis modulation with no two parameters moving in parallel, producing filter textures that evolve across multiple independent time scales simultaneously.

**Intellijel MixUp** is the downstream destination where the Wasp SE's output integrates with the rest of the system. Channel 3 on MixUp accepts a stereo input, but the Wasp SE's mono output patches naturally to Channel 1 or Channel 2 as a mono source with level control and mute access. When the Wasp is being used as a self-oscillating voice alongside other oscillator sources, each voice occupies a separate MixUp channel so their relative levels can be balanced independently. When the Wasp is processing a granular or complex source, the processed output on one MixUp channel and the dry source on another allows wet/dry blend to be managed at the mixer rather than requiring a dedicated mix module in the signal chain.

---

*Doepfer A-124 Wasp SE documentation: [Doepfer](https://doepfer.de/a100_man/a124_man.pdf)*
