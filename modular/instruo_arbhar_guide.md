---
title: Instruo Arbhar
manufacturer: Instruo
primary_role: SHAPER
secondary_roles: [SOURCE]
form_factor: eurorack
functions: [granular]
behavior_tags: [evolving, nonlinear, stochastic, generative, performance-oriented]
use_cases: [granular texture bed, evolving ambient texture, dark atmospheric layer, rhythmic grain bursts, pitched granular voice]
hp: 18
---

# Instruo Arbhar

**Six-Layer Granular Processor**

![Instruo Arbhar](https://github.com/Shadoe-42/music/raw/main/modular/images/instruo/arbhar/front_panel.jpg)  
![Instruo Arbhar Expander](https://github.com/Shadoe-42/music/raw/main/modular/images/instruo/arbhar/exp_panel.jpg)  
![Instruo Arbhar USB Expander](https://github.com/Shadoe-42/music/raw/main/modular/images/instruo/arbhar/usb_exp_panel.jpg)  
*Instruo Arbhar: Granular processor with 6-layer memory system, built-in microphone, and full CV control over all primary parameters*

---

## Historical Context

Dennis Gabor, a Hungarian-British physicist working on communication theory, published "Theory of Communication" in 1946 and developed his acoustic quanta framework the following year. His core proposal was that sound could be decomposed into elementary events, each defined by a specific frequency and a specific duration, in direct analogy to quantum physics. He called these events acoustic quanta. The implication was that synthesis did not require continuous waveforms; it could operate by generating and distributing discrete sound particles. Gabor built experimental apparatus to demonstrate his theory but did not develop a working musical instrument. His framework defined the conceptual space that granular synthesis would eventually inhabit.

Iannis Xenakis, working in Paris in the late 1950s and early 1960s, developed stochastic composition as a method for constructing sonic events from probability distributions. His 1955 orchestral work Metastaseis treated individual instrumental notes as particles in a statistical field rather than as melodic units. Xenakis translated this compositional philosophy into synthesis theory explicitly: a sound could be constructed from a cloud of grains distributed according to mathematical probability functions, with the character of the sound emerging from the statistical parameters of the cloud rather than from the shape of any single waveform. His 1971 book Formalized Music articulated the connection between stochastic mathematics and granular sound production in detail that practitioners could apply.

Curtis Roads brought granular synthesis into computer music implementation. His 1978 paper at IRCAM (Institut de Recherche et Coordination Acoustique/Musique) in Paris, "Automated Granular Synthesis of Sound," described the first software implementation of grain-based synthesis and established the vocabulary that the field still uses: grain duration, grain density, grain position, scatter. Barry Truax, working at Simon Fraser University in Burnaby, developed real-time granular synthesis in the 1980s using the DMX-1000 signal processor. His 1988 paper "Real-Time Granular Synthesis with a Digital Signal Processor" demonstrated that the technique was computationally feasible outside of offline batch processing, which was a necessary precondition for any practical musical application. These two implementations together moved granular synthesis from theoretical framework to working compositional tool.

The translation from academic computer music to standalone hardware took decades because the computational requirements were substantial relative to available processing. As embedded processors became capable of handling real-time grain scheduling at musically useful densities, manufacturers began producing dedicated granular hardware. Instruo, working from Glasgow, designed Arbhar to address a specific gap in the available hardware: most granular processors treated CV control as secondary, exposing a subset of parameters to external modulation while leaving others accessible only through manual adjustment. Arbhar exposes every primary parameter to CV simultaneously, which means that the grain cloud can be sculpted in real time by external modulation sources at all four dimensions at once. The 6-layer memory architecture reflects a particular view of granular performance: not a single captured moment held frozen in one buffer, but a collection of up to six distinct captured moments that can be recalled, combined, and played simultaneously. The built-in microphone is not a convenience feature. It is a statement that the instrument should function in immediate physical context without requiring a dedicated audio source chain first. Granular synthesis is framed here as temporal deconstruction, not time-stretching: the instrument does not slow audio down or speed it up. It dissolves it into particles and reassembles them according to parameters you control.

---

## Quick Start

**What is Arbhar?** A granular processor: it captures audio into memory and plays it back as streams of short overlapping grains, each with controllable position, duration, density, pitch, and spatial distribution.

### Your First Granular Sound

1. Connect any audio source to the IN jack, or leave IN empty to use the built-in microphone
2. Set Input Level to noon
3. Press CAPTURE; the LED lights amber while recording
4. Allow 5 to 10 seconds of recording, then let it complete automatically or press CAPTURE again to stop
5. Adjust SCAN to move the playback position within the captured buffer
6. Adjust INTENSITY to control grain density
7. Adjust LENGTH to set grain duration
8. Adjust SPRAY to scatter grain positions randomly

---

## Key Specifications

| Parameter | Value |
|-----------|-------|
| Width | 18HP |
| Depth | 42mm |
| Power | 250mA +12V, 30mA -12V, 0mA 5V |
| Memory layers | 6 independent (alpha, beta, gamma, delta, epsilon, zeta) |
| Buffer length per layer | 10 seconds |
| Grain duration range | 4ms to 3 seconds |
| Built-in microphone | Active when IN jack is unpatched |
| CV inputs | SCAN, INTENSITY, LENGTH, SPRAY, PITCH, 1V/OCT, STRIKE |
| Outputs | OUT 1, OUT 2 (stereo) |
| Expander | 2HP, 20mm depth, no power draw |
| USB Expander | 2HP, 25mm depth, no power draw |

---

## Essential Parameters

The CAPTURE button records audio into the currently selected memory layer. Pressing it once begins recording; the amber LED confirms that recording is active. Each layer holds up to 10 seconds. The recording does not loop automatically; what is captured is a static snapshot of that audio, which the granular engine then reads. Nothing is erased until a new CAPTURE on the same layer overwrites it.

SCAN determines where within the captured buffer the granular engine is reading. At fully counterclockwise, grains are drawn from the beginning of the recording. At fully clockwise, grains are drawn from the end. Intermediate positions address the corresponding moment in the captured material. Modulating SCAN with a slow LFO or function generator moves the read position through the buffer automatically, producing evolving textures as different moments of the capture are granulated over time. Manual SCAN adjustment is its own performance technique: scrubbing slowly through a capture produces fundamentally different results than holding the position fixed.

INTENSITY controls grain density: how many grains are playing simultaneously at any given moment. At the noon position, grain density is at its maximum. Moving the knob in either direction from center reduces the number of simultaneous grains. This center-maximum behavior is specific to Arbhar and runs counter to the expectation that clockwise always means more. Musical application: noon for thick, lush texture; either edge for sparse, individual grain events.

LENGTH sets the duration of individual grains, ranging from approximately 4ms to 3 seconds. Short lengths (below 20ms) produce textural results because grains are too brief for the auditory system to extract pitch information; the output sounds granular and noise-adjacent. Longer lengths (above 100ms) allow individual grains to carry pitch content and produce stretched, tonal material. The range from 20ms to 100ms produces dense granular clouds with emerging pitch character. These are not gradations on a single effect; they are different perceptual categories of granular output, each appropriate to different musical contexts.

SPRAY randomizes grain position around the SCAN point. At minimum, all grains are drawn from the exact SCAN position, producing focused playback of that moment. Increasing SPRAY distributes grains across a widening window around SCAN, adding diffusion and spatial spread. High SPRAY values scatter grains across a large portion of the buffer, producing ambient clouds with no clear relationship to SCAN position. SPRAY is not a reverb or a blur; it is a spatial distribution parameter that determines how wide the read window is relative to the SCAN anchor.

The PITCH knob transposes the granular output in semitone increments without affecting playback speed. The 1V/OCT input accepts standard pitch voltage from a sequencer or keyboard controller, allowing the granular field to track melodic input across the usable pitch range. PITCH and 1V/OCT work independently: PITCH offsets the base pitch by a fixed interval, and 1V/OCT controls it dynamically from the incoming voltage. For melodic granular playing, LENGTH must be long enough (above 100ms) for grains to carry pitch information; short grain settings will not produce trackable pitch regardless of what arrives at 1V/OCT.

The STRIKE input accepts gate or trigger signals to generate discrete grain bursts on demand. STRIKE operates alongside the continuous grain engine rather than replacing it; patching a gate source into STRIKE does not stop the ongoing grain stream. The STRIKE-triggered bursts add rhythmically timed events on top of whatever the continuous engine is producing. Clock sources, gate sequences, and envelope triggers all work as STRIKE sources.

The LAYER selector chooses which of the six memory layers is active for recording and playback. Each layer retains its captured content independently; switching layers during performance changes the source material without affecting what is stored in any other layer. The OMEGA position at the far clockwise end of the LAYER selector combines all six layers simultaneously, allowing their granular outputs to blend into a single composite output. OMEGA is a mixing position, not a playback mode; the character of the OMEGA output is determined entirely by what has been captured across all six layers.

---

## Why Arbhar Excels

Granular synthesis has an access problem. Gabor's acoustic quanta framework describes how sound can be understood as discrete particles, but understanding the theory is not required to turn a SCAN knob. What is required is an instrument whose controls map directly to the perceptual consequences of granular synthesis rather than to its internal mathematics. Arbhar's four primary controls (SCAN, INTENSITY, LENGTH, SPRAY) each address a distinct perceptual dimension of the granular output: position within the captured material, density of the grain cloud, duration of individual grains, and spatial distribution of grain read positions. A single move on LENGTH changes the perceptual category of the output from texture to pitch. A single move on SPRAY changes the output from focused to diffuse. The architecture is organized around what the performer hears, not around what the algorithm computes.

The 6-layer memory system is the feature that separates Arbhar from simpler granular processors. Most hardware granular instruments hold one buffer. Arbhar holds six independent ones, each independently recordable and each retaining its content regardless of what happens in adjacent layers. A working method that is impossible on a single-buffer device becomes straightforward: capture a drone on alpha, capture a percussive transient on beta, capture an environmental recording on gamma, and navigate between them during performance using the LAYER selector. The OMEGA position adds a layer of granular density that neither pure layering nor individual selection can produce alone: all six captured moments granulate simultaneously through the same SCAN, INTENSITY, LENGTH, and SPRAY settings, producing a composite texture that carries the character of each source while belonging fully to none of them.

Every primary parameter accepts CV input simultaneously, which means the grain cloud is not limited to what a performer can control manually. Patching a function generator to SCAN moves the read position through the buffer over time without manual interaction. Patching an envelope to LENGTH makes individual grains grow from texture to pitch with each articulation. Patching a sequencer to 1V/OCT turns the granular field into a playable melodic voice. This is not CV over some parameters with manual control of the rest; Arbhar was designed so that all four primary parameters, pitch, and STRIKE respond to CV simultaneously, which means fully automated granular performance is architecturally possible alongside fully manual operation.

The built-in microphone reflects a particular position on the relationship between the instrument and the physical context it operates in. Arbhar can function without any other modules: leave IN unpatched, point the microphone toward a sound source, press CAPTURE, and the instrument has material immediately. This capability makes the instrument viable in improvised and field recording contexts where an extended signal chain is not practical. The deeper implication is that the physical environment is always a valid source: room tone, acoustic instruments, incidental sound, and voice are all directly accessible to the granular engine without conversion or preparation. The microphone is not a shortcut. It is a design statement about what counts as legitimate source material.

---

## Patches

### Patch 1: First Granular Freeze

This patch establishes the core Arbhar workflow: capturing audio into a single layer and shaping the resulting granular texture with the four primary parameter controls.

```
[Audio Source] ──▶ IN
                   CAPTURE (press to record)
                   OUT 1 ──▶ [Output or Mixer]
                   OUT 2 ──▶ [Output or Mixer]
```

**Setup:** Connect an audio source to IN. If no external source is available, leave IN unpatched and use the built-in microphone. Press CAPTURE to begin recording into the alpha layer; the amber LED confirms recording is active. Allow the recording to complete (approximately 10 seconds) or press CAPTURE again to stop at any point. Connect OUT 1 and OUT 2 to a mixer or output module.

**Controls:** Set SCAN to noon to begin from the center of the captured buffer. Set INTENSITY to noon for maximum grain density. Set LENGTH to the 10 o'clock position for short grains in the texture range. Set SPRAY to minimum for focused playback of the SCAN position. From this starting configuration, adjust one parameter at a time: advance SCAN slowly to move through the captured material, increase LENGTH toward the 2 o'clock position to bring pitched content forward, and increase SPRAY incrementally to diffuse the texture. Each parameter affects the output in a distinct and audible way; understanding what each one does in isolation is the prerequisite to using them together.

**Result:** A controlled granular texture derived from the captured source. Moving SCAN manually is the immediate demonstration of what granular synthesis does: the same source material produces fundamentally different textural output depending on which portion of the buffer the engine is reading.

---

### Patch 2: Rhythmic Grain Bursts

This patch routes an external gate source into the STRIKE input to produce rhythmically timed granular events alongside the continuous grain stream.

```
[Clock or Gate Source] ──▶ STRIKE
[Audio Source] ──────────▶ IN
                            OUT 1 ──▶ [Output or Mixer]
                            OUT 2 ──▶ [Output or Mixer]
```

**Setup:** Capture audio into the alpha layer first using the standard capture procedure. Then connect a clock output, gate sequence, or trigger source to the STRIKE input. Connect OUT 1 and OUT 2 to a mixer or output module.

**Controls:** Set LENGTH to the 8 to 9 o'clock range for short, percussive grain durations. Set INTENSITY lower than noon (9 to 10 o'clock) so the continuous grain stream stays sparse and the STRIKE bursts are distinct against it. Set SPRAY to minimum to keep each burst focused on the current SCAN position. Move SCAN to different positions in the buffer to change which moment of the captured material each STRIKE event addresses. The rhythmic pattern of the granular output follows the incoming gate source directly; changing the clock rate, gate pattern, or gate density changes the character and rhythm of the granular events.

**Result:** Percussive granular hits timed to an external rhythmic source, layered over a continuous grain stream. The STRIKE input turns the granular output into a rhythmically articulated voice rather than a pure continuous texture. Source material with clear transients responds especially well to this treatment: a drum hit, a plucked string, a consonant; each granulates differently when struck rhythmically than when processed as a continuous stream.

---

### Patch 3: Pitched Granular Voice

This patch routes 1V/OCT pitch voltage into Arbhar so the granular field tracks melodic input from a sequencer or keyboard controller.

```
[Sequencer CV Out] ──▶ 1V/OCT
[Sequencer Gate Out] ─▶ STRIKE (optional)
[Audio Source] ───────▶ IN
                         OUT 1 ──▶ [Output or Mixer]
                         OUT 2 ──▶ [Output or Mixer]
```

**Setup:** Capture a harmonically rich and sustained source into the alpha layer: complex oscillator output, a bowed tone, a held chord, or a sustained drone. Connect the CV output of a sequencer or keyboard to the 1V/OCT input. Optionally connect the gate output to STRIKE so that individual note events generate grain bursts on each step.

**Controls:** Set LENGTH to the 1 to 2 o'clock range so grains are long enough to carry pitch information; grain durations below approximately 50ms produce textural output regardless of 1V/OCT input. Set INTENSITY to noon. Set SPRAY to minimum or a small amount. Set PITCH to noon for zero transposition offset. Step through the sequencer and listen to how the granular output tracks the pitch sequence. Adjust SCAN to find a position in the buffer where the captured material is steady and harmonically clear; transients and attacks in the buffer do not track pitch as cleanly as sustained content. The best SCAN position is typically the body of a sustained note or chord, away from the onset.

**Result:** A granular voice that follows the pitch sequence from the sequencer, using the captured audio as its timbral source. This is not sample playback at different rates; granular pitch control shifts the playback rate of individual grains while the grain cloud density and position remain independently controlled. The output is unmistakably granular in character even when tracking a clear melody.

---

### Patch 4: Six-Layer Collage

This patch builds a multi-layer granular collage by capturing different source materials into separate memory layers and combining them at the OMEGA position.

```
[Source 1] ──▶ IN  (LAYER selector at alpha, press CAPTURE)
[Source 2] ──▶ IN  (LAYER selector at beta, press CAPTURE)
[Source 3] ──▶ IN  (LAYER selector at gamma, press CAPTURE)

LAYER selector ──▶ OMEGA position
OUT 1 ──▶ [MixUp or Output]
OUT 2 ──▶ [MixUp or Output]
```

**Setup:** Begin with the LAYER selector at the alpha position. Connect a first audio source to IN and press CAPTURE. When the recording completes, advance the LAYER selector to beta. Connect a second audio source to IN and press CAPTURE again. Continue through as many layers as needed, capturing a different source or a different moment into each. Using genuinely different source types produces the most useful results: a sustained drone for one layer, a percussive transient for another, an environmental recording or a pitched voice for a third. After loading at least three layers, advance the LAYER selector to OMEGA.

**Controls:** At OMEGA, the granular engine draws grains from all loaded layers simultaneously. SCAN moves the read position across all layers together. INTENSITY controls the total grain density of the combined output. LENGTH and SPRAY affect all layers uniformly. The character of the OMEGA blend depends entirely on what is in the individual layers and how different those sources are from each other: similar sources produce a thickened version of that character, while highly contrasting sources produce complex, layered textures in which no single source dominates. Adjust SCAN slowly through the OMEGA position to find blend points where the layers interact interestingly.

**Result:** A granular texture that combines multiple independent captures into a single output. Moving to OMEGA at a specific moment in a performance, after spending time building the layer collection, is a performance gesture unique to Arbhar. The instrument accumulates material throughout a session, and OMEGA is the mode in which all of that accumulated material becomes simultaneously active.

---

## Common Mistakes

### "I recorded audio but the playback sounds like noise rather than my source"

This is granular synthesis working as designed, not a malfunction. When LENGTH is set short (below approximately 20ms), individual grains are too brief for the auditory system to perceive pitch; the output is textured and noise-adjacent rather than recognizable as the captured source. Arbhar does not reproduce audio the way a looper does. It atomizes audio into particles and plays those particles back according to the current parameter settings. Short LENGTH settings are a deliberate timbral choice.

**Fix:** Increase LENGTH toward the 1 to 2 o'clock range to produce grains long enough for pitch content to emerge. At longer settings, the relationship between the captured source and the granular output becomes audible. If textural output is not the goal, LENGTH is the first knob to adjust.

---

### "I am trying to layer multiple recordings but earlier layers are bleeding into new ones"

Layer content does not bleed between slots. The LAYER selector determines which of the six memory slots is active for both recording and playback. If the selector is not advanced before pressing CAPTURE, the new recording overwrites the material already stored in the current layer. What sounds like bleed is almost always a missed LAYER selector advance before a new capture, not interference between slots.

**Fix:** Before pressing CAPTURE for a new recording, confirm the LAYER selector is pointing to a different position from the one just recorded. Check the layer indicator LED to verify which slot is active. Each layer is independent; recording to beta writes only to beta and does not affect alpha or any other slot.

---

### "I cannot get melodic results from Arbhar; everything sounds ambient or atmospheric"

Melodic output from 1V/OCT tracking depends on three conditions being met simultaneously: LENGTH must be long enough for grains to carry pitch information (above approximately 100ms), SCAN must be positioned in a steady-state section of the captured buffer rather than on a transient, and the captured source itself must contain clear pitch information. Capturing noise, percussion, or highly complex material and then applying 1V/OCT does not produce melodic output. The conditions must be met at the source, the buffer position, and the grain duration simultaneously.

**Fix:** Capture a sustained, harmonically clear source (a steady oscillator output, a bowed tone, a held chord). Set LENGTH to the 1 to 2 o'clock range. Position SCAN away from any attack or transient in the buffer, in the sustained body of the captured sound. Then patch 1V/OCT. In this configuration, the granular output tracks pitch input in a way that is melodically useful, though it will always sound granular rather than like conventional sample playback.

---

### "The built-in microphone is picking up room noise I did not intend to capture"

The condenser microphone is active whenever nothing is patched into the IN jack. If IN is unpatched when CAPTURE is pressed, the microphone is the audio source regardless of what else is happening in the patch. Ambient room sound, fan noise, conversation, and incidental audio are all captured along with any intended acoustic source in range of the microphone.

**Fix:** Patch an audio signal into IN to disable the microphone and route external audio to the capture engine. If working without a dedicated audio source, press CAPTURE only in environments where the ambient sound is intentional source material. There is no panel control that disables the microphone independently of the IN jack; the presence of a cable in IN is the switch.

---

## Advanced Learning Path

1. Begin with single-layer capture before exploring the full layer system. Record one source, hold it in alpha, and spend time navigating SCAN manually through the entire buffer. Listen to how the granular character changes as SCAN moves across different moments of the recording: a drum hit granulates differently than the decay after it, a vowel granulates differently than the consonant that precedes it, a moment of room tone granulates differently than the peak of a sustained note. This slow manual exploration of a single captured buffer develops the intuition required to work with the full layer system intentionally rather than accidentally.

2. Develop a precise understanding of how LENGTH affects the perceptual category of the output. Capture a sustained note and then move LENGTH from its minimum to its maximum in small increments, pausing to listen at each position. Below approximately 20ms, the output is texture with no perceivable pitch. Between 20ms and 100ms, the output is a granular cloud with emerging pitch character. Above 100ms, the output approaches stretched, tonal audio in which the source pitch is recognizable. Knowing where these thresholds sit on the LENGTH control in practice is more useful than knowing them as abstract values, because the exact positions depend on the source material and the monitoring context.

3. Modulate SCAN with a slow function generator or LFO rather than advancing it manually. Patch the output of a slow rising-falling function generator or a triangle LFO into the SCAN CV input and set the modulation period to 20 to 60 seconds for slow movement through the buffer, or to 4 to 8 seconds for movement that remains rhythmically perceptible. The read position moves through the captured material automatically, allowing complex source material to surface and recede without manual intervention. This is the core workflow for long-form granular processing where the performer manages modulation sources and layer content rather than operating parameters directly.

4. Use the STRIKE input alongside the continuous grain engine to build a two-plane texture. With nothing in STRIKE, Arbhar produces a continuous stream. Patching STRIKE does not disable the continuous engine; it adds triggered burst events on top of the ongoing stream. Set the continuous stream to a different SCAN position than the one the STRIKE bursts address (accomplished by adjusting SCAN while monitoring, or by using two different layers), and the result is a two-plane granular texture: an ambient continuous layer and a rhythmically articulated foreground layer drawn from different source material simultaneously.

5. Build the layer collection systematically before moving to OMEGA. The temptation is to load one or two layers and immediately activate OMEGA, but the quality of the OMEGA blend depends entirely on the diversity of what has been captured across the six layers. Record genuinely different source types into six layers before combining them: a drone, a percussive transient, an environmental recording, a complex oscillator output, a pitched voice, and a single sustained tone. Then switch to OMEGA and listen to what the granular engine produces from that diversity. The OMEGA blend is not a feature that works on one or two similar sources; it is a feature that reveals itself when the layer collection has genuine variety.

6. Treat SPRAY and SCAN modulation as interacting parameters rather than independent ones. SCAN determines the center of the read position; SPRAY determines how wide the distribution window is around that center. A patch with a slow envelope modulating SCAN while SPRAY holds at a moderate fixed setting produces a granular texture that moves through the buffer over time while simultaneously diffusing grain positions within a window around the current SCAN position. Increasing SPRAY while SCAN is being modulated broadens the apparent time range of the granular output: the engine is reading from a wider and wider window as it moves, producing increasingly atmospheric results. Decreasing SPRAY while SCAN modulates narrows that window, keeping the output focused on a moving point rather than a moving region.

7. Treat multi-generation capture as a compositional method. Route Arbhar's output back into its own IN, or capture the granular output with an external recorder and feed that recording back in as source material. Granulating already-granulated material produces textures with no remaining resemblance to the original source; the source character dissolves progressively with each generation. Plan a session in which the first capture is a clear, identifiable tone, the second capture is a recording of the granular output from that first capture, and the third is a recording of the second generation. Listen to how each generation transforms the material and loses contact with the original. This is granular synthesis used as a transformation engine: the identity of the source is not preserved, it is dissolved.

---

## Pairs Well With

**Xaoc Zadar** is the most architecturally coherent CV source for Arbhar's four primary parameter inputs. Zadar provides four independent function generators with individually configurable envelope shapes, each with its own CV input and its own loop behavior. A direct configuration routes Zadar's four outputs to Arbhar's SCAN, INTENSITY, LENGTH, and SPRAY CV inputs, with each Zadar channel set to a different curve shape and a different loop time. The four granular parameters modulate simultaneously but at independent rates and with different shapes, producing a granular texture that evolves across multiple time axes at once. Zadar's per-channel depth control allows precise calibration of how far each parameter moves versus how much it stays anchored to the knob position. This is the modulation pairing that makes fully automated granular performance practical without requiring manual intervention during a performance.

**Altered States Machines Eris** provides the routing infrastructure for working with Arbhar's stereo outputs across multiple signal chains. Eris is a 4x4 matrix mixer: four inputs, four outputs, with individually adjustable gain at each intersection point. Arbhar's OUT 1 and OUT 2 feed into two Eris input columns; the matrix then distributes those signals to multiple effect chains simultaneously at independently set levels. Rather than choosing one effects path for the granular output, Eris allows the stereo granular signal to enter reverb, delay, filter, and distortion chains in parallel, with a different amount of granular signal feeding each destination. The result is a granular texture that exists simultaneously in multiple treatment contexts, each contributing to the final mix at Eris-controlled proportions. This is a confirmed working configuration in this system.

**Instruo Cs-L** is the most natural source module to feed into Arbhar from within this system. Cs-L's wavefolded and FM-processed oscillator output is harmonically complex in a way that responds well to granulation: the spectral content produced by wavefolding distributes across the grain cloud differently than a simple waveform does, producing granular textures that carry the harmonic identity of the oscillator without reproducing its waveform directly. The 1V/OCT tracking on both modules means that a single pitch CV source can address Cs-L's pitch and Arbhar's pitch simultaneously, keeping the granular output and the oscillator source in the same key while each processes its function independently. The combination of complex oscillator output as source material and granular processing as the treatment layer is one of the defining signal relationships in this system.

**Intellijel MixUp** is the direct downstream destination for Arbhar's stereo output. MixUp's Channel 3 accepts a stereo input with a shared level knob and mute switch, which is the appropriate destination for a stereo granular processor: OUT 1 and OUT 2 from Arbhar land in CH3 IN L and CH3 IN R, and the CH3 LEVEL knob controls the overall contribution of the granular texture to the mix without touching the Arbhar patch. The CH3 MUTE switch removes the granular layer from the mix entirely during sections where it is not needed. When Arbhar's output passes through Altered States Machines Eris before reaching MixUp, the effect returns from each Eris output occupy separate MixUp channels, with the granular signal on CH3 and processed returns on CH1 and CH2.

---

*Instruo Arbhar documentation: [Instruo](https://www.instruomodular.com)*
