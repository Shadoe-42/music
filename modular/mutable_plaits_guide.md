---
title: Mutable Instruments Plaits
manufacturer: Mutable Instruments
primary_role: SOURCE
secondary_roles: [SHAPER]
historical_context: true
form_factor: eurorack
functions: [complex-oscillator, drum-voice]
behavior_tags: [harmonic, stable, warm, gated, performance-oriented]
use_cases: [lead voice, bass voice, percussive voice, chord voice]
hp: 12
memory: none
transport: none
screen: false
hybrid: false
cv: full
---

# Mutable Instruments Plaits

![Mutable Instruments Plaits](https://github.com/Shadoe-42/music/raw/main/modular/images/mutable_instruments/plaits/front_panel.jpg)

*16-model macro-oscillator with integrated low-pass gate: a complete synthesis voice spanning analog waveforms, FM, wavetable, granular, chord, and percussion without requiring external shaping modules*

---

## Historical Context

The problem that Plaits addresses is older than digital synthesis: how do you make a fundamentally different class of sound available to a performer without requiring them to rebuild their instrument? Every major synthesis method, from analog subtractive to FM to granular, grew from separate research traditions, with separate instruments, separate vocabularies, and separate physical hardware. A musician who wanted to move between these worlds required either multiple instruments or an unsatisfying compromise. The macro-oscillator concept, as Mutable Instruments developed it, proposed a different answer: implement each synthesis method as a discrete algorithm with a shared, consistent control interface, so that the performer navigates between complete synthesis engines rather than between modules.

The synthesis methods collected in Plaits each carry their own lineage. FM synthesis derives from John Chowning's research at Stanford in 1967, commercialized through the Yamaha DX7 in 1983, which put complex inharmonic and bell-like timbres into the hands of a generation of producers. Wavetable synthesis traces to Wolfgang Palm's PPG Wave instruments of 1979 and 1982, which first made morphing between static waveforms a real-time performance technique. Granular synthesis extends from Iannis Xenakis's theoretical work in the 1950s, later implemented computationally by Curtis Roads and others, which treated sound as a stream of microsonic events rather than a continuous waveform. Physical modeling and modal synthesis emerged from Julius O. Smith's waveguide research at Stanford's Center for Computer Research in Music and Acoustics through the late 1980s and 1990s. Plaits does not merely reference these traditions; it implements them, each with enough fidelity that the characteristic behavior of the original technique is audible.

Émilie Gillet founded Mutable Instruments around 2011, following work at Google and Last.fm. The company's defining commitment was open-source hardware and firmware: every circuit diagram and every line of code for every module was published freely. This was not incidental to the musical culture of Mutable Instruments; it was central to it. The modules were designed to be modified, cloned, and studied. Plaits exists in the racks of thousands of musicians today in both original and clone form, and its firmware and circuit design have been read and learned from by engineers building their own instruments. When Gillet closed Mutable Instruments in April 2022, the entire catalog moved to fully open-source release. The knowledge is preserved, and the instruments continue to be manufactured under license.

Plaits was released in 2018 as a successor to Braids, the earlier Mutable Instruments macro-oscillator from 2013. Braids had established the concept but required navigating a menu system to select synthesis models, which interrupted performance flow. Plaits redesigned the interface entirely: two buttons select from two banks of eight models each, and a dedicated CV input allows model selection under voltage control. A built-in low-pass gate accepts a LEVEL CV input and a TRIGGER input, providing the amplitude and filter shaping that would otherwise require a separate module. The HARMONICS, TIMBRE, and MORPH controls serve different functions in each synthesis engine, but their physical positions remain consistent, so a performer develops spatial memory for the interface regardless of which model is active.

---

## Quick Start

Plaits is a multi-model oscillator and complete synthesis voice. Power it, connect V/OCT to the V/OCT input and a cable from OUT to your mixer, and you have a working sound source immediately. The built-in low-pass gate means you can patch a gate or envelope to LEVEL and hear a complete note with attack and decay without any additional modules.

1. Connect a sequencer or keyboard V/OCT output to the Plaits V/OCT input.
2. Connect Plaits OUT to a mixer or audio interface.
3. Confirm the first LED in the left bank is lit (first model: virtual analog dual oscillator).
4. Press play on your sequencer or play a note. You should hear pitched audio.
5. Connect a gate or envelope to the LEVEL input. The built-in low-pass gate will now shape each note.
6. Turn the HARMONICS, TIMBRE, and MORPH knobs to explore the sound of the first model.
7. Press the left button to advance through the eight melodic models. Press the right button to access the eight percussion models.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 12 HP |
| Depth | 25 mm ⚠️ |
| Power | 50 mA +12V ⚠️ / 5 mA -12V ⚠️ / 0 mA +5V |

---

## Essential Parameters

The left button cycles through eight melodic synthesis models. The right button cycles through eight percussion and noise models. Both buttons respond to a single press to advance one step, or to a CV input at the MODEL jack to select any model under voltage control. The 16 LEDs indicate the current model position clearly. This is the most consequential control on the module: the entire synthesis architecture changes with each model selection.

HARMONICS controls a parameter related to spectral content or tuning within the current synthesis engine. In the virtual analog model it sets detuning and waveform balance between two oscillators. In the FM model it selects the ratio between carrier and modulator. In chord models it selects the chord voicing. In percussion models it shapes the character of the noise burst or transient. Because it operates differently in each engine, HARMONICS rewards exploration rather than systematic mental modeling. A CV input with an attenuverter allows voltage control of this parameter.

TIMBRE controls the primary timbral character of the synthesis engine. In most models this maps to something like brightness or spectral density. In the virtual analog model it controls pulse width and waveform selection. In wavetable models it scans through the wavetable. In speech models it selects phoneme position. In percussion models it shapes the frequency and decay of the transient. A CV input with an attenuverter provides voltage control. When nothing is patched to the TIMBRE CV input, the attenuverter acts as a direct offset control, meaning turning it clockwise adds a positive offset to the knob value.

MORPH controls a secondary timbral dimension that the synthesis engine exposes as a second axis of exploration. In the virtual analog model it sweeps through waveform shapes. In the FM model it sets modulation index. In granular models it controls grain characteristics. MORPH often reveals variation that TIMBRE alone cannot access, and the most interesting timbral positions frequently involve both controls set away from their center positions simultaneously. Like TIMBRE and HARMONICS, MORPH has a CV input with an attenuverter.

FREQUENCY sets the base pitch of the oscillator in a range spanning roughly eight octaves when no V/OCT signal is present. With a V/OCT source connected, FREQUENCY becomes a coarse transpose control. The V/OCT input tracks 1V/octave standard. A second FREQ CV input modulates pitch directly without 1V/octave scaling, suitable for FM modulation or pitch vibrato from an LFO.

The built-in low-pass gate uses the LEVEL input and TRIGGER input to provide amplitude and filter shaping without external modules. LEVEL accepts a 0-8V CV signal that controls both the volume and the cutoff frequency of the low-pass gate simultaneously: a higher LEVEL CV produces a louder and brighter output. TRIGGER accepts a gate or trigger signal that plucks the LPG with a fixed internal envelope. When nothing is patched to LEVEL, the attenuverter for that input controls the resting level of the gate, allowing the LPG to act as a simple VCA offset. The LPG response time can be adjusted by holding the left model button while turning TIMBRE (vactrol-like response) and MORPH (decay time).

---

## Why This Instrument Excels

Plaits is not a multi-function module in the sense of a utility that does several unrelated things. It is a curated collection of synthesis engines, each implemented with the full fidelity of its method. The FM engine produces genuine Chowning-style inharmonic timbres. The wavetable engine produces the PPG-style spectral morphing that defined a generation of synthesizers. The granular engine scatters and reconstructs audio with real microsonic behavior. These are not simplified approximations; they are working implementations of historically significant synthesis techniques, accessible from a 12HP module with a consistent physical interface. The breadth of coverage is the point: a single Plaits replaces what would otherwise require separate dedicated hardware for each method.

The built-in low-pass gate elevates Plaits from a sound source to a complete voice. In standard Eurorack signal flow, an oscillator requires a filter and a VCA to produce a shaped note: three modules minimum, plus envelope generators to drive them. Plaits collapses this to a single module. The LPG behaves like an analog Buchla-style vactrol circuit in its interaction of amplitude and timbre, not like a digital VCA simply multiplying a signal by an envelope. Notes have the softening at the attack and natural decay of a physical pluck rather than the mechanical precision of a digital gate. For small systems, or for a secondary voice in a larger system where panel space is limited, this matters: a complete synthesis voice occupies 12HP.

The CV architecture scales from minimal to deeply modulated. In its simplest state, Plaits requires only V/OCT and a cable to an audio destination. As the patch grows, LEVEL accepts envelope CVs, TIMBRE and MORPH accept LFO or random modulation through their attenuverters, HARMONICS responds to stepped sequences or slow ramps, and the MODEL input accepts voltages from a sequencer to automatically cycle through synthesis engines. Each attenuverter is bipolar, meaning both positive and negative modulation are available from a single CV source without external attenuation or inversion. The module never exceeds the modulation depth available to it: it always has more inputs than a small system will fill.

The instrument rewards long-term use in a way that depends on the 16-model architecture. A performer who has used only two or three models for months discovers, when exploring the remainder of the bank, that new synthesis methods with entirely different modulation responses are available on the same hardware. Each model is a different instrument in the physical sense: the same gesture with the same knob produces fundamentally different results depending on which synthesis engine is active. This depth is not apparent in an initial evaluation; it accumulates over time and gives Plaits unusual longevity relative to single-method oscillators.

---

## Patches

### Patch 1: Complete Synthesis Voice

This patch establishes Plaits as a self-contained synthesizer voice using only the built-in LPG for shaping.

```
[Sequencer]──V/OCT──[C]──▶ PLAITS V/OCT
[Sequencer]──GATE───[G]──▶ [Envelope Gen] GATE IN
[Envelope Gen] OUT──[C]──▶ PLAITS LEVEL
                           PLAITS OUT ──[A]──▶ [Mixer]
```

**Setup:** Connect the sequencer V/OCT to Plaits V/OCT. Connect the sequencer gate to an envelope generator gate input. Connect the envelope generator output to Plaits LEVEL. Connect Plaits OUT to a mixer channel.

**Controls:** Select model 1 (first LED, virtual analog). Set FREQUENCY at noon. Set the envelope generator for a moderate attack (100-200ms) and release (500ms-1s). Turn HARMONICS to about 9 o'clock to hear detuning between the two virtual oscillators. Adjust TIMBRE to control pulse width and MORPH to sweep between waveform shapes.

**Result:** A complete synthesizer voice: pitched, melodically sequenced, and dynamically shaped. The LPG provides simultaneous amplitude and brightness response to the envelope CV, so the note opens and closes with the natural softening of an analog low-pass gate rather than the hard on/off of a VCA alone.

---

### Patch 2: Percussion Bank with Tuned Kick

This patch explores the eight percussion models and demonstrates how a single tuned kick relates to melodic sequences.

```
[Clock]──TRIG──[G]──▶ PLAITS TRIG
[Sequencer]──V/OCT──[C]──▶ PLAITS V/OCT
                           PLAITS OUT ──[A]──▶ [Mixer]
                           PLAITS AUX ──[A]──▶ [Mixer]
```

**Setup:** Connect a clock or trigger sequencer output to Plaits TRIG. Connect a sequencer or keyboard V/OCT to Plaits V/OCT. Connect both Plaits OUT and AUX to separate mixer channels.

**Controls:** Press the right model button to enter the percussion bank. Navigate to model 9 (first percussion model: analog bass drum). Set FREQUENCY below noon to bring the kick into a low register. Turn HARMONICS to adjust the snap of the transient. Adjust TIMBRE for the attack character and MORPH for the decay length. Note that V/OCT controls the pitch of the kick, so a step sequencer creating a melodic pattern will pitch the kick accordingly. AUX on percussion models often carries a complementary signal; monitor both.

**Result:** A tuned, V/OCT-responsive kick drum or bass drum synth voice. Advancing through the percussion models with the right button reveals snare, hat, and noise models, each responsive to the same three controls with different sonic results.

---

### Patch 3: FM Self-Modulation

This patch routes the AUX output into the FM input to create complex, self-modulating FM textures in the dedicated FM synthesis model.

```
[Sequencer]──V/OCT──[C]──▶ PLAITS V/OCT
[Envelope Gen] OUT──[C]──▶ PLAITS LEVEL
PLAITS AUX ─────────[C]──▶ PLAITS FM (via attenuverter)
                           PLAITS OUT ──[A]──▶ [Filter or Mixer]
```

**Setup:** Connect sequencer V/OCT to Plaits V/OCT and an envelope generator to LEVEL as in Patch 1. Patch Plaits AUX to the FM CV input. Set the FM CV attenuverter to a low level (7-9 o'clock position) to start.

**Controls:** Select model 3 or 4 (FM synthesis models in the left bank; exact positions depend on firmware version). Set HARMONICS to select an FM ratio in the 1:2 or 1:3 range. Slowly increase the FM attenuverter to introduce self-modulation. The AUX output carries a complementary signal from the FM engine that, when fed back into FM CV, destabilizes the ratio relationship and produces metallic sidebands, chaotic partials, and feedback tones that change with pitch. Adjust TIMBRE and MORPH while the self-modulation is active.

**Result:** FM synthesis with feedback-driven timbral complexity. The patch is sensitive to attenuverter level: small changes produce large differences. This behavior is more pronounced at certain ratios than others. The same patch applied to other synthesis models produces different results because AUX carries different signal content per model.

---

### Patch 4: Generative Synthesis with Mutable Instruments Marbles

This patch uses Mutable Instruments Marbles to drive Plaits V/OCT, TRIG, and MODEL CV simultaneously, creating an evolving, semi-random synthesis voice.

```
MARBLES X1 ──[C]──▶ PLAITS V/OCT
MARBLES t1 ──[G]──▶ PLAITS TRIG
MARBLES X3 ──[C]──▶ PLAITS MODEL (via attenuverter)
[LFO] OUT ───[C]──▶ PLAITS TIMBRE CV (via attenuverter)
              PLAITS OUT ──[A]──▶ [Reverb] ──[A]──▶ [Mixer]
              PLAITS AUX ──[A]──▶ [Mixer]
```

**Setup:** Connect Marbles X1 to Plaits V/OCT and Marbles t1 to Plaits TRIG. Connect Marbles X3 to Plaits MODEL CV through the attenuverter. Connect a slow LFO to Plaits TIMBRE CV. Send Plaits OUT through a reverb module and Plaits AUX directly to a mixer.

**Controls:** Set Marbles to generate quantized melodic patterns from X1 (STEPS at noon, BIAS slightly right of center). Set the MODEL attenuverter to a low level so Marbles X3 shifts between two or three synthesis models rather than sweeping all sixteen. With the LFO modulating TIMBRE slowly, the synthesis engine timbral character evolves as each new note triggers. Adjust Marbles DEJA VU to increase pattern repetition and shape the degree of randomness.

**Result:** A generative synthesis voice that recombines synthesis methods, pitch content, and timbral evolution over time. No two passes through the same sequence produce exactly the same result, but the DEJA VU control on Marbles keeps the output within a recognizable melodic region. The reverb tail on OUT and the dry signal on AUX create natural stereo width without any additional processing.

---

## Common Mistakes

### "My pitch is wrong after I switch models"

Model switching on Plaits does not reset the FREQUENCY knob position, but some models have different default pitch centers or tuning offsets. The FREQUENCY knob spans eight octaves at full range, and a position that placed the virtual analog model in the mid-register may place an FM model in a different octave due to how that model calculates its base frequency. The fix: after selecting a new model, return FREQUENCY to its noon position as a calibration baseline, then adjust from there.

### "I patched LEVEL CV but the notes still sound the same volume"

Plaits has internal attenuverters for all CV inputs. If the LEVEL attenuverter is turned fully counterclockwise, incoming CV has no effect. The attenuverters are the smaller knobs immediately below the CV input jacks. Return the LEVEL attenuverter to its noon position to restore full CV response, then reduce it if the LPG response is too dramatic. When nothing is patched to LEVEL, the attenuverter sets the resting open level of the gate, which is why notes are audible at all without a CV source: the gate is held partially or fully open by the attenuverter position.

### "The AUX output sounds identical to OUT"

AUX carries model-dependent complementary signal content that ranges from a sub-oscillator to an entirely different signal derived from the same synthesis engine. In the virtual analog model, AUX carries the second oscillator separately. In FM models, AUX carries the raw modulator waveform. In granular models, AUX carries a second grain stream with different parameters. AUX is not a copy of OUT; it is a second synthesis output derived from the same engine with different characteristics. Patch both to separate mixer channels and listen to each before combining them. On many models, AUX is the more interesting signal.

### "My sequencer pitch works but the notes all sound staccato regardless of my envelope settings"

This occurs when the TRIG input is receiving a signal simultaneously with the LEVEL CV. The TRIG input fires the internal LPG envelope, which shapes the note independently. If both TRIG and LEVEL CV are active at the same time, the TRIG envelope and the external LEVEL CV can conflict, producing inconsistent dynamics. Use one input or the other deliberately: LEVEL CV for continuous dynamic shaping driven by an envelope generator, or TRIG for percussive plucks. If you need both behaviors in the same patch, attenuate the LEVEL CV so the TRIG envelope retains control at its peak.

### "I cannot reproduce a sound I found yesterday"

Each of the 16 models responds to the same four knobs (HARMONICS, TIMBRE, MORPH, FREQUENCY) differently. A position that produces a specific timbre in model 3 produces an entirely different sound in model 7. Plaits has no patch memory. When a useful sound is found, the reliable way to document it is to write down the model number and the approximate position of all four knobs. Without that note, the interaction of four continuous controls across 16 models makes exact reproduction difficult. Treat discovery as the working method: systematic documentation of good positions is worth the brief interruption.

---

## Advanced Learning Path

1. Work through all eight melodic models in sequence with the same V/OCT source and envelope. For each model, map what HARMONICS, TIMBRE, and MORPH actually control by moving only one at a time. This is slower than random exploration, but it builds a working mental model of each synthesis engine that enables deliberate sound selection later.

2. Repeat the same systematic survey for the eight percussion models. Focus on how V/OCT affects each percussion model differently: in some models it tunes a pitched transient; in others it adjusts the frequency content of a noise burst; in a few it has minimal effect. Understanding which percussion models track pitch reliably opens them for use as tuned percussion voices in melodic contexts.

3. Patch AUX to a separate mixer channel for every model while working through them. Document which models produce the most complementary content on AUX relative to OUT. Several models produce their most useful material on AUX, and treating it as a bonus output rather than a primary one undersells the module significantly.

4. Introduce model CV switching with a stepped sequencer. Set the MODEL attenuverter to cover only 2-3 model positions so that the sequence cycles through a curated set of synthesis engines rather than all 16 at random. Explore how melody sequences change character as the synthesis engine changes beneath them. Adjust the attenuverter range and offset to dial in which models participate in the rotation.

5. Build the FM self-modulation patch from Patch 3 and map the parameter space deliberately. Change the FM ratio with HARMONICS, change the feedback level with the attenuverter, and note which combinations produce stable timbral complexity versus uncontrolled chaotic feedback. This maps directly to understanding feedback in physical FM synthesizers and in analog oscillator self-modulation.

6. Explore the LPG response controls. Hold the left model button and turn TIMBRE to adjust the vactrol response character (slower or faster attack softening) and turn MORPH to adjust the decay time. These settings persist across model changes until the module is powered off. Find a LPG response that suits your playing context, ranging from the fast response needed for percussion to the slow natural decay appropriate for plucked strings or marimba-like voices.

7. Drive TIMBRE, MORPH, and HARMONICS simultaneously with three different modulation sources. Use an LFO on TIMBRE, a random voltage on HARMONICS, and an envelope on MORPH, each through its attenuverter at a low modulation depth. This is the entry point to true multi-dimensional timbral evolution: the synthesis engine does not simply move along one axis but through a three-dimensional parameter space in real time. Start with modulation depths that are almost inaudible individually; their combination is often more dramatic than any single modulator alone.

8. Pair Plaits with an external filter and VCA after the output, bypassing the internal LPG entirely. Set the LPG LEVEL attenuverter fully open so Plaits OUT carries unshaped synthesis audio. Use the external filter for tone shaping and the external VCA for amplitude control. This approach recovers the full dynamics and tone-shaping capacity of a dedicated filter and gives access to filter resonance and character that the LPG does not provide. The comparison between the internal LPG approach and the external filter approach is one of the most instructive experiments available on Plaits: both are correct; they produce fundamentally different note behavior.

---

## Pairs Well With

**Mutable Instruments Marbles** provides the most direct synthesis partner relationship available for Plaits in Eurorack. Marbles generates quantized V/OCT from its X outputs and gate patterns from its t outputs, both derived from a single source of controlled randomness. Its X3 output, used as MODEL CV through Plaits' attenuverter, creates an evolving synthesis palette where the harmonic character of the voice changes alongside its pitch and rhythm. The two modules share design philosophy and CV scaling: they were made to interact, and the combination produces generative melodic content that requires no additional modules to be musically coherent.

**Make Noise Maths** covers the envelope and function generation that Plaits' internal LPG accepts as LEVEL CV. Maths channels running in envelope mode drive LEVEL with attack and decay contours that range from percussive snaps to multi-second swells. Maths channels running as LFOs drive TIMBRE or MORPH for timbral modulation. The fourth Maths channel summing the other three creates complex composite modulation shapes that a single envelope generator cannot produce. Plaits and Maths together constitute a complete, deeply modulated synthesis voice in 30HP.

**Intellijel Scales** sits between a random or stepped V/OCT source and Plaits' V/OCT input to constrain pitch output to a chosen key and scale. When driving Plaits from a chaotic or random source, unquantized V/OCT produces pitches with no musical relationship. Scales converts that raw voltage stream into notes within a defined harmonic context, allowing the random timing and timbral evolution of a generative patch to produce tonally coherent melody. The combination of a random source, Scales, and Plaits produces generative melodic content that sounds composed rather than arbitrary.

**4ms Company Listen IO** bridges the modular signal chain and the wider studio. Plaits' output through Listen IO reaches guitar amplifiers, bass amplifiers, and recording interfaces that expect instrument-level or line-level signals rather than Eurorack hot levels. The Intellijel Stomp module serves the same function and enables the physical modeling and granular synthesis models in Plaits to be heard through amplifier cabinets with speaker character and room response, which transforms the already complex synthesis output into something closer to an acoustic instrument recording. This is one of the most direct paths to making modular synthesis sound organic rather than electronic.

**Noise Engineering Numeric Repetitor** drives Plaits' TRIG input with rhythmically complex gate patterns derived from mathematical progressions. The percussion models in Plaits respond to trigger timing directly, and Numeric Repetitor's patterns create rhythmic structures that a simple clock division cannot produce. Pairing the pitched models with Numeric Repetitor TRIG patterns and a melody sequencer on V/OCT creates a voice with independent rhythmic and melodic content, each under its own clock or sequence source.

---

*Official documentation and firmware source: [Mutable Instruments Plaits](https://mutable-instruments.net/modules/plaits)*
