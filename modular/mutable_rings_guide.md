---
title: Mutable Instruments Rings
manufacturer: Mutable Instruments
primary_role: SOURCE
secondary_roles: [SHAPER]
historical_context: true
form_factor: eurorack
functions: [resonator, physical-model]
behavior_tags: [harmonic, sustained, metallic, evolving, performance-oriented]
use_cases: [harmonic pad, evolving ambient texture, chord voice, drone foundation]
hp: 14
memory: none
transport: none
screen: false
hybrid: false
cv: full
---

# Mutable Instruments Rings

![Mutable Instruments Rings](https://github.com/Shadoe-42/music/raw/main/modular/images/mutable_instruments/rings/front_panel.jpg)

*Three-algorithm physical modeling resonator with polyphonic voice management and dual harmonic outputs: modal, sympathetic strings, and nonlinear string physics in 14HP*

---

## Historical Context

The central problem physical modeling synthesis addresses is not timbre but behavior. An electronic oscillator can approximate the harmonic spectrum of a bell or a plucked string at a given instant, but it cannot replicate the way those harmonics evolve over time under the physical constraints of mass, tension, and material damping. Acoustic instruments do not produce static spectra; they produce dynamic systems where each partial decays at its own rate, where striking harder changes the relationship between modes, where the position of the excitation point shifts the timbral emphasis. Kevin Karplus and Alex Strong described a computationally minimal model of this behavior in 1983: a delay line with a single low-pass filter in the feedback path, initialized with white noise, produces a convincing approximation of a plucked string because the delay time sets the pitch and the filter models the faster decay of upper harmonics. The Karplus-Strong algorithm was not a curiosity; it was the beginning of a synthesis discipline.

Julius O. Smith III at Stanford's Center for Computer Research in Music and Acoustics extended this approach through the 1980s and 1990s into waveguide synthesis: a more general framework that models acoustic resonators by simulating the traveling pressure waves within them, accounting for the physics of reflection, transmission, and loss at the boundaries of the resonating object. Smith's work produced models of bowed strings, wind instruments, and percussion bodies with a fidelity that could not be achieved through additive or subtractive methods. Parallel to waveguide research, modal synthesis developed as a distinct approach: rather than simulating wave propagation, modal synthesis models the resonant mode structure of an object directly, computing how each resonant frequency is excited and how it decays. Jean-Marie Adrien's work on modal synthesis in the late 1980s established the mathematical foundation that underlies the modal resonator in Rings. These two lineages, waveguide and modal, are not interchangeable; they produce physically distinct behaviors and produce different sonic results even when tuned to the same fundamental frequency.

Commercial physical modeling synthesis arrived in the mid-1990s. Yamaha released the VL1 in 1994, the first commercially available physical modeling synthesizer, implementing waveguide models of acoustic instruments. The VL1 was exceptional and expensive, initially limited to two voices. Korg introduced physical modeling in the Prophecy in 1995 at a lower price point, reaching more musicians. Neither instrument fully displaced other synthesis methods, but they established that physical modeling belonged in the toolkit alongside FM, wavetable, and analog subtractive synthesis. The sounds they produced, particularly the intimate response of string and wind models to performance dynamics, had no equivalent from any other synthesis approach.

Mutable Instruments Rings was released in 2015, bringing three physical modeling paradigms into Eurorack form in 14HP. Émilie Gillet implemented the modal resonator based on the Adrien lineage, a sympathetic strings algorithm modeling the resonance coupling between multiple strings tuned in harmonic relationships, and a string model with nonlinear behavior incorporating the kind of saturation and irregularity present in real bowed and plucked string instruments. The module accepts external audio at its IN input, allowing any sound to become the excitation material for the resonator, and separates the odd and even harmonics of the resonating body to two discrete outputs. Rings is one of three modules in the Mutable Instruments catalog that implement physical modeling, alongside Elements, which provides a complete physical modeling voice chain; Rings focuses specifically on the resonant body, designed to be driven by the rest of a modular system and to integrate into existing patches as a timbral transformation stage as readily as it operates as a standalone voice.

---

## Quick Start

Rings is a physical modeling resonator. It simulates the resonant behavior of acoustic objects: bells, strings, and resonating bodies. It can generate sound entirely on its own when triggered, or it can process external audio by treating that audio as the excitation that drives the resonator. The three algorithm modes and four polyphony levels are all accessible from the front panel with two buttons.

1. Connect a sequencer or keyboard V/OCT output to the Rings V/OCT input.
2. Connect a gate or trigger to the Rings STRUM input.
3. Connect Rings ODD output to a mixer or audio interface.
4. Press play or play a note. You should hear a decaying, pitched resonance with no external audio source required: the module uses an internal noise burst as its exciter when IN is unpatched.
5. Press the right button to change the resonator algorithm: the LED indicates green (modal), orange (sympathetic strings), or red (string model).
6. Turn DAMPING to adjust the decay time from short percussive plucks to sustained, ringing tones.
7. Turn STRUCTURE to change the harmonic character of the resonating body.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 14 HP |
| Depth | 24 mm ⚠️ |
| Power | 75 mA +12V ⚠️ / 25 mA -12V ⚠️ / 0 mA +5V |

---

## Essential Parameters

The right button selects the resonator algorithm, cycling through three modes indicated by LED color. Green is the modal resonator, modeling the resonant mode structure of objects such as bells, metal bars, and tuned plates. Orange is the sympathetic strings model, simulating the coupled resonance of multiple strings that ring in response to a played note through harmonic relationships. Red is the string model, incorporating nonlinear physics including the saturation and irregularity of real bowed and plucked string vibration. Each algorithm exposes different acoustic behavior through the same set of controls. Switching algorithms mid-patch produces immediate and substantial timbral changes.

The left button sets the number of simultaneous voices: one, two, or four, indicated by the number of lit LEDs in the left indicator group. In one-voice mode, all computational resources are allocated to a single voice, producing the highest fidelity per note. In four-voice mode, computational resources are divided, reducing fidelity per voice but enabling harmonic layering as multiple notes accumulate and decay together. Rings polyphony is not keyboard polyphony; it does not respond to multiple simultaneous V/OCT sources. Instead, each new STRUM trigger allocates one of the available voices to the incoming pitch, and prior voices continue to decay. Four-voice mode with melodic triggering creates the kind of overlapping resonance characteristic of a struck chime or fingerpicked guitar.

FREQUENCY sets the base tuning of the resonator independently of V/OCT input. Without V/OCT patched, it sweeps the pitch continuously across roughly five octaves. With V/OCT patched, FREQUENCY becomes a quantized transpose control in semitone steps, shifting the entire V/OCT range up or down. The V/OCT input tracks 1V/octave standard.

STRUCTURE controls the harmonic relationship between the resonant modes of the active algorithm. In the modal resonator, it shifts the partial spacings from values consistent with metallic and bell-like timbres toward more string-like and inharmonic configurations. In the sympathetic strings model, it controls the intervals between the sympathetic strings relative to the played note. In the string model, it adjusts the physical properties of the string including nonlinear tension and damping. A CV input with an attenuverter allows voltage control of STRUCTURE; slowly modulating STRUCTURE with an LFO transforms the perceived material of the resonating body over time.

BRIGHTNESS controls the spectral content of the sound, operating as a high-frequency emphasis control that affects how much upper harmonic content the resonator sustains. At low settings the output is darker and warmer, with upper partials decaying faster. At high settings more upper harmonic content is preserved throughout the decay. A CV input allows BRIGHTNESS to be modulated; an envelope with a fast attack and slow decay applied to BRIGHTNESS creates the characteristic timbral arc of a real struck bell, bright at the attack and darkening through the sustain.

DAMPING controls the decay time of the resonance, ranging from very short percussive plucks to sustained tones of ten seconds or more. DAMPING interacts with the algorithm: in the modal resonator, high DAMPING produces bell-like sustain; in the string model, high DAMPING produces bowed-string sustain with different upper harmonic behavior. A CV input enables dynamic control. Modulating DAMPING in real time changes the character of notes already sounding.

POSITION controls the point on the resonating body where the excitation energy is applied. In acoustic instruments, striking or plucking at different positions along the string or plate emphasizes different harmonics: plucking at the midpoint of a guitar string produces a full tone; plucking close to the bridge produces a thin, bright tone. POSITION in Rings models this behavior. The difference between a noon POSITION and a fully clockwise POSITION can be dramatic in the modal algorithm.

The STRUM input receives gate or trigger signals to excite the resonator. With no external audio at IN, a STRUM event uses an internal noise burst as the exciter. With audio present at IN, STRUM controls when that audio is coupled into the resonator. The ODD output carries the odd-numbered harmonics of the resonating body; the EVEN output carries the even-numbered harmonics. These are not copies of each other and are not a stereo pair, although routing them to separate channels in a stereo mix creates genuine stereo imaging derived from the harmonic structure of the model.

The IN input accepts external audio as the excitation material for the resonator. Any audio fed here replaces the internal noise burst exciter. The module processes the incoming audio through the active physical model, applying the resonant coloration of the selected algorithm to the input material. Drums, voice, another oscillator, or noise all produce distinctly different results because the physical model responds to the spectral content of its excitation.

---

## Why This Instrument Excels

Physical modeling synthesis does not approximate acoustic timbres; it simulates acoustic physics. The harmonic relationships in a bell are not arbitrary: they arise from the geometry and material of the resonating object, and a modal resonator that accurately models those relationships produces the characteristic inharmonic overtone series that makes a bell sound like a bell and not like an additive synthesis approximation. Rings implements this correctly in all three of its algorithms. The result is that even without reverb or processing, notes from Rings decay with the natural modal distribution of a real resonating body: upper harmonics disappearing first, the fundamental sustaining longest, the precise decay envelope of each partial determined by the physics of the model and not by a manually drawn envelope shape.

The three algorithms are not variations on a theme; they are acoustically distinct physical models with different underlying mathematics. The modal resonator computes the resonant mode structure of an object directly. The sympathetic strings model simulates the harmonic coupling that occurs when multiple strings share a resonant body and ring in response to each other's excitation. The string model includes nonlinear physical effects, saturation, and the particular behavior of a string's vibration at different excitation intensities. These distinctions are audible and significant: a patch built around the modal algorithm sounds like metal and glass; the same patch with the sympathetic strings algorithm sounds like a sitar or a multi-string acoustic instrument; the string model in the same patch sounds like a bowed or plucked instrument with perceptible physical irregularity. Three algorithms means three genuinely different classes of acoustic sound from one module.

The IN input architecture is a fundamental design decision that makes Rings more than an acoustic voice. Any audio patched to IN becomes the excitation for the physical model: the resonator does not care what that audio is. A percussive hit driven into the modal resonator produces a ringing metallic tone. A noise burst produces a gentler pluck. Another oscillator produces a tone filtered through the resonant modes of the model. The physical model acts as a timbral stage that imposes acoustic coherence on whatever audio passes through it, and the result sounds natural in a way that is difficult to replicate through filtering alone, because the decay behavior across partials is physically determined rather than manually shaped.

The ODD/EVEN output separation is not a convenience feature. The modal resonator distributes energy across its resonant modes, and those modes do not all occupy the same physical space in the acoustic model: odd-numbered modes and even-numbered modes have different amplitude and decay relationships. Separating them to different outputs allows them to be processed independently: different reverb tails, different panning positions, different filtering. Routing ODD hard left and EVEN hard right through identical reverbs produces a stereo image that has internal coherence because the two channels carry harmonically related but physically distinct components of the same resonating event. This kind of stereo width sounds organic rather than artificial precisely because it arises from the physics of the model.

---

## Patches

### Patch 1: Modal Resonator Voice

This patch uses the modal resonator as a complete melodic voice, demonstrating the self-contained note generation capability of Rings without external audio.

```
[Sequencer]──V/OCT──[C]──▶ RINGS V/OCT
[Sequencer]──GATE───[G]──▶ RINGS STRUM
                           RINGS ODD ──[A]──▶ [Mixer Left]
                           RINGS EVEN──[A]──▶ [Mixer Right]
```

**Setup:** Connect the sequencer V/OCT to Rings V/OCT and the sequencer gate to Rings STRUM. Connect ODD and EVEN to two mixer channels panned apart. No external audio at IN.

**Controls:** Select modal algorithm (green LED) and one voice. Set DAMPING to about 2 o'clock for a sustaining bell-like decay. Set BRIGHTNESS to about 2 o'clock. Set STRUCTURE to about 10 o'clock for a metallic bell character. Play the sequence and listen to the two outputs separately and combined. Adjust POSITION from noon toward fully clockwise to hear how the tone thins near the bridge position.

**Result:** A melodic bell or chime voice with a natural modal decay. The ODD and EVEN outputs panned apart produce stereo width from the harmonic structure of the model, not from any added processing. Adding reverb to the stereo mix extends the decay and places the instrument in an acoustic space.

---

### Patch 2: Audio Input Processing

This patch routes an external oscillator through Rings as an excitation source, transforming the oscillator's tone through the resonator's physics.

```
[Plaits OUT]──────────[A]──▶ RINGS IN
[Clock/Trig]──────────[G]──▶ RINGS STRUM
[Sequencer]──V/OCT───[C]──▶ RINGS V/OCT
                             RINGS ODD ──[A]──▶ [Mixer]
```

**Setup:** Connect Mutable Instruments Plaits OUT or any oscillator output to Rings IN. Connect a clock or trigger to Rings STRUM. Connect a V/OCT source to Rings V/OCT.

**Controls:** Select the modal algorithm (green LED), one voice. Set DAMPING at noon. Adjust STRUCTURE and BRIGHTNESS while the sequence plays. The Rings resonator now imposes its harmonic mode structure on the Plaits audio: the output has the spectral character of Plaits but filtered through the decay physics of the modal resonator. Try switching to the string algorithm (red LED) and then the sympathetic strings algorithm (orange LED) to hear how the same input audio produces different acoustic colorations.

**Result:** The input oscillator's harmonic content is distributed across the resonant modes of the active algorithm. Notes with harmonics that align with the resonator's mode structure are reinforced; others are suppressed. The combination of the two modules' harmonic content produces tones that neither module produces alone.

---

### Patch 3: Polyphonic Sympathetic Strings

This patch explores four-voice polyphony in the sympathetic strings algorithm to create layered chord textures where multiple note decays accumulate.

```
[Sequencer]──V/OCT──[C]──▶ RINGS V/OCT
[Clock]──────────── [G]──▶ RINGS STRUM
[Slow LFO]──────────[C]──▶ RINGS STRUCTURE CV (via attenuverter)
                           RINGS ODD ──[A]──▶ [Reverb] ──[A]──▶ [Mixer]
                           RINGS EVEN──[A]──▶ [Reverb] ──[A]──▶ [Mixer]
```

**Setup:** Connect a melody sequencer V/OCT to Rings V/OCT, a clock to STRUM, and a slow LFO to STRUCTURE CV with the attenuverter at a low setting. Route both outputs through separate reverb inputs.

**Controls:** Select sympathetic strings algorithm (orange LED) and four voices. Set DAMPING to about 3 o'clock for long, overlapping decays. Set STRUCTURE near noon and let the LFO slowly sweep it. As the clock triggers new notes, previous voices continue decaying while new ones start, creating an accumulating harmonic texture. The slow STRUCTURE modulation gradually shifts the interval relationships between the sympathetic strings, producing a gentle evolution in the chord color.

**Result:** A slowly evolving harmonic pad where the polyphony creates natural layering of sympathetic resonances. The combination of clock-driven new notes and LFO-swept STRUCTURE produces a texture that sounds composed but generative: it has internal coherence from the physical model's interval relationships and ongoing change from the modulation.

---

### Patch 4: Generative Resonant Voice with Marbles

This patch uses Mutable Instruments Marbles to drive Rings as a generative melodic instrument, with envelope control over BRIGHTNESS for natural timbral arc.

```
MARBLES X1 ──────────[C]──▶ RINGS V/OCT
MARBLES t1 ──────────[G]──▶ RINGS STRUM
[Envelope] ──────────[C]──▶ RINGS BRIGHTNESS CV (via attenuverter)
[LFO slow]───────────[C]──▶ RINGS DAMPING CV (via attenuverter)
                            RINGS ODD ──[A]──▶ [Reverb/Delay] ──[A]──▶ [Mixer]
                            RINGS EVEN──[A]──▶ [Mixer]
```

**Setup:** Connect Marbles X1 to Rings V/OCT, Marbles t1 to Rings STRUM. Connect an envelope generator output (triggered by Marbles t1) to BRIGHTNESS CV and a slow LFO to DAMPING CV. Route ODD through a reverb or delay and EVEN directly to a mixer channel.

**Controls:** Select modal algorithm (green LED), one or two voices. Set the envelope generator for a fast attack and medium decay. The BRIGHTNESS CV will open and darken with each note, producing the timbral arc of a real struck bell: bright at the moment of excitation and darkening through the sustain. The slow LFO on DAMPING gradually lengthens and shortens the overall decay across the phrase. Adjust Marbles' DEJA VU to shape the degree of melodic repetition.

**Result:** A generative bell-like melodic voice with physically accurate timbral evolution per note. The envelope-driven BRIGHTNESS produces the characteristic brightness attack and warm sustain of a real metallic instrument without any filter envelope in the signal path: it arises from the physical model's response to excitation intensity, modeled through CV.

---

## Common Mistakes

### "Rings is not making any sound when I patch nothing to IN"

Rings does not require external audio. When the IN input is unpatched, Rings uses an internal noise burst as its exciter every time STRUM receives a trigger or gate. The internal exciter produces the correct impulse for each algorithm. Most users discover the module's self-contained sound generation within seconds of patching V/OCT and STRUM alone. External audio at IN is an additional capability, not a prerequisite.

### "My ODD and EVEN outputs sound identical"

They carry different harmonic content, not copies of the same signal. ODD carries the odd-numbered resonant modes of the active algorithm; EVEN carries the even-numbered modes. In the modal resonator, these modes have different frequencies, different amplitude ratios, and different decay rates: they are related but genuinely distinct. The difference is most apparent when the outputs are compared in isolation on separate mixer channels with no additional processing. If they sound similar in context, it is likely because both are feeding the same reverb or being summed in mono before monitoring.

### "My FREQUENCY knob stopped sweeping pitch after I patched V/OCT"

This is correct behavior. Once a V/OCT source is connected, FREQUENCY shifts to a semitone-quantized transpose mode and no longer sweeps continuously. It adjusts the pitch offset in semitone steps. To restore continuous pitch sweep, remove the V/OCT cable. To transpose the V/OCT range, use FREQUENCY; each step of the knob is one semitone.

### "Four-voice mode sounds muddier than one-voice mode"

It is. Four voices divides the available computational precision among four simultaneous resonators, and each individual voice has less resolution than in one-voice mode. The tradeoff is intentional: four-voice mode produces natural harmonic layering where multiple notes accumulate and decay simultaneously, which is musically useful for chord textures but requires accepting lower fidelity per voice. For single-note melodic lines where the full decay quality of the physical model is important, one-voice mode is the correct choice.

### "Patching audio to IN changes the behavior completely and I cannot figure out what it is doing"

IN changes Rings from an instrument that generates its own excitation into a resonator that processes the excitation provided. Whatever is patched to IN becomes the material that drives the physical model. The resonator then applies its modal structure and decay physics to that material: its pitches are reinforced, its attack transients are colored by the resonant modes. If the input audio has strong harmonics that fall near the resonator's mode frequencies, they are amplified; others are attenuated. The result often sounds unlike either the input audio or the resonator alone. Treating this as a feature rather than a complication opens significant sound design territory.

---

## Advanced Learning Path

1. Spend dedicated time with each of the three algorithms in isolation. Use the same V/OCT sequence and STRUM pattern for each, changing only the algorithm. Document what STRUCTURE controls in each case and where the most musically useful STRUCTURE positions are per algorithm. This builds the working knowledge necessary to make algorithm selection intentional rather than exploratory.

2. Explore the polyphony modes systematically. Use a clock triggering STRUM at a steady rate while a melody sequencer drives V/OCT, and cycle through one, two, and four voices. Observe how the number of voices changes the harmonic density and decay overlap of the phrase. Note the fidelity difference between one-voice and four-voice modes. Understand when the decay layering of four voices adds to the music and when the reduced fidelity per voice detracts from it.

3. Process a range of audio types through IN. Start with a simple sine wave from an oscillator, then a complex wavetable voice, then a drum hit, then noise, then a voice or field recording. Compare how each input type interacts with the modal algorithm versus the string algorithm. The physical model imposes its resonant structure on whatever is fed in, but different input materials produce radically different results because the mode reinforcement depends on the input's spectral content.

4. Explore the interaction between POSITION and the algorithm choice. In the modal resonator, POSITION strongly affects which modes are emphasized: the midpoint position reinforces low modes while the bridge position emphasizes higher modes. In the string model, POSITION has a similar but acoustically different character. Build a patch where an LFO slowly sweeps POSITION while notes sustain, and observe the timbral evolution this produces.

5. Use BRIGHTNESS CV with an envelope to simulate the timbral arc of a real struck instrument: fast attack on the envelope opens BRIGHTNESS to full at the moment of excitation, then the slow decay returns it to a darker, warmer sustained tone. This mimics the physical reality of metallic instruments and produces a perceptually more convincing resonating body sound than a static BRIGHTNESS setting.

6. Patch ODD and EVEN through separate processing chains before mixing to stereo. Try different reverb types on each output, different delay times, or a subtle pitch shift on one channel. The harmonic separation means the two processing chains are working on harmonically complementary material, and their interaction in the final mix has an internal coherence that arbitrary stereo spread lacks.

7. Combine Rings with Mutable Instruments Plaits as an excitation source. Route Plaits OUT to Rings IN and use Plaits' synthesis models as the material that drives the resonator. The FM models, wavetable models, and speech models each produce different spectral content that the physical model distributes across its resonant modes differently. This combination treats two complete synthesis architectures as a single layered instrument.

8. In four-voice mode with the sympathetic strings algorithm, use a slow sequence with long DAMPING and modulate STRUCTURE with a gentle LFO. As voices accumulate and decay, the slow STRUCTURE change shifts the harmonic relationship between the sympathetic strings in all active voices simultaneously. The result is a chordal texture whose internal harmonic relationships evolve gradually without any change in the notes themselves. This technique requires patience to hear fully, as the evolution happens over the timescale of many note events rather than within a single note.

---

## Pairs Well With

**Mutable Instruments Plaits** is the most direct synthesis partner for Rings in the Mutable Instruments catalog. Plaits' OUT can drive Rings' IN as an excitation source, and the two modules share design vocabulary: both are open-source Mutable Instruments designs with CV attenuverters, both produce dual outputs, and both scale from simple single-patch use to deeply modulated performance instruments. The FM and wavetable models from Plaits produce spectral content that interacts particularly richly with the modal resonator, because their harmonic content aligns with the modal algorithm's mode frequencies in musically coherent ways. The percussion models from Plaits driven into Rings IN produce transient-excited resonances with combined timbral character.

**Make Noise Maths** provides envelope generation and function generation for Rings' CV inputs in one module with enough flexibility to drive BRIGHTNESS, DAMPING, and STRUCTURE simultaneously. Maths' end-of-rise and end-of-cycle outputs can drive Rings STRUM independently of an external clock, creating self-clocking patch configurations where the resonator triggers itself. The logarithmic curve shapes available from Maths produce physically plausible BRIGHTNESS envelopes for the bell attack and decay arc. A single Maths and Rings constitute a complete, dynamically shaped resonant voice without any additional modules.

**Mutable Instruments Marbles** controls both V/OCT and STRUM from the same randomness source, producing melodic patterns with rhythmic articulation that shares a common underlying probability distribution. When Marbles' DEJA VU is set toward repetition, the Rings voice produces recognizable melodic material with occasional variation; when DEJA VU is set toward exploration, the material evolves continuously. The shared design philosophy and CV scaling between these two Mutable Instruments modules means their interaction produces results that are more musically coherent than pairing with a generic random source.

**Intellijel Quadrax** provides four simultaneous envelope channels, each independently configurable, which addresses the multiple-CV-input architecture of Rings directly. With Quadrax' Qx expander, all four Rings CV inputs (STRUCTURE, BRIGHTNESS, DAMPING, POSITION) can be driven by independent envelopes with different shapes and times, each triggered from the same gate source. This produces a note event where every timbral dimension has its own independent trajectory: BRIGHTNESS arcing open and closed, STRUCTURE shifting material at the sustain peak, POSITION sweeping through the decay. The result is a note behavior that approaches the complexity of a real acoustic instrument's multi-dimensional physical response.

**4ms Company Listen IO** sends Rings' output into guitar amplifiers and recording chains. The resonant, decaying character of Rings is well-suited to amplifier character: the slow onset of long decays reveals amplifier harmonics and speaker response in ways that a hard-attack synthesis voice does not. Routing Rings ODD and EVEN to separate channels of a stereo amplifier setup, or through the Intellijel Stomp into a guitar amplifier and microphone combination, adds the acoustic space and physical resonance of a real speaker cabinet to an already physically-modeled instrument voice. The combination records in a way that makes modular synthesis indistinguishable from a mic'd acoustic instrument.

---

*Official documentation and firmware source: [Mutable Instruments Rings](https://mutable-instruments.net/modules/rings)*
