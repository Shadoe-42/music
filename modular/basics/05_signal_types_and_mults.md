# Signal Types and Mults

**What's actually flowing through those cables — and how to split it without breaking anything.**

You've built voices, shaped them, sequenced them, and triggered percussion. At this point you've patched dozens of connections without thinking too hard about what kind of voltage was flowing through each cable. That works fine for simple patches. As your system grows and patches get more complex, the distinction starts to matter — and mult selection becomes a real decision rather than a grab-whatever-is-nearby choice.

This guide covers the three signal types, the full range of what generates CV, and how to split signals correctly.

---

## The Three Signal Types

Every cable in your system carries one of three types of voltage: audio, control voltage (CV), or gate/trigger. They're not locked to specific cables — a 3.5mm TS patch cable carries whatever voltage you put through it. The type is defined by what the source generates and what the destination expects.

---

### Audio

**What it is:** Voltage oscillating at frequencies the human ear perceives as sound — roughly 20 to 20,000 cycles per second. Audio voltage is bipolar: it swings above and below 0V in continuous waveforms.

**What generates it:** Oscillators, noise sources, sample players, audio effects, anything with a sound output.

**Where it goes:** Filters, VCAs, effects modules, output modules, speakers (via proper level conversion).

**How much voltage:** Eurorack audio signals are typically ±5V (10Vpp), though some modules run hotter. Audio levels are significantly higher than most other gear — your modular is loud relative to a guitar pedal's expectations. This matters when you're interfacing with external equipment.

**The key thing about audio:** Its meaning comes from the oscillation itself. A sine wave at 440Hz doesn't carry the information "this is A4" — it *is* the 440Hz vibration. Audio signals are real-time waveform data, not messages about pitch or timing.

---

### Control Voltage (CV)

**What it is:** Voltage used to control the behavior of another module rather than produce sound directly. CV is the nervous system of a modular patch — it carries information about pitch, brightness, depth, speed, amount, direction, and anything else that can be expressed as a voltage value.

**Where it goes:** Any CV input — filter cutoff, oscillator pitch, VCA level, LFO rate, reverb decay, effect blend, and hundreds of other destinations.

**The critical distinction:** CV doesn't have a fixed waveform shape or frequency the way audio does. It's a representation of a value or a changing value over time. When you patch an envelope to a filter's CV input, the filter cutoff tracks the envelope's voltage contour. When you patch a sequencer's pitch output to an oscillator's V/Oct input, the oscillator plays the notes the sequencer specifies.

**CV is versatile.** The same voltage range can mean different things to different destinations. 5V patched to a VCA might mean "fully open." 5V patched to an oscillator's V/Oct input means "five octaves up from the base pitch." The module decides the meaning. You decide the routing.

#### What Generates CV

This is where the real variety lives. CV isn't just envelopes — it's everything that produces a voltage intended to control something else.

**Envelopes**
Time-based voltage contours triggered by gates. The classic ADSR: attack rises from 0V, decays to sustain level, holds while gate is open, releases back to 0V when gate closes. The output voltage represents a value changing over time — most commonly used to shape amplitude (via VCA) or brightness (via filter cutoff). Envelopes are gated: they wait for a trigger before doing anything.

**LFOs (Low Frequency Oscillators)**
Oscillators running below audio rate — typically 0.01Hz to 20Hz. They produce the same waveform shapes as audio oscillators (sine, triangle, square, ramp, random) but slowly enough that you hear the *effect* on whatever they're modulating rather than the LFO itself as a tone. A sine LFO on filter cutoff creates tremolo-like brightness movement. A ramp LFO on oscillator pitch creates a glide. A square LFO switching between two values creates alternating states. LFOs are free-running: they cycle continuously without waiting for a trigger.

**Sample and Hold (S&H)**
A circuit that samples a voltage at the moment of a trigger and holds that value until the next trigger. Classic application: trigger on each clock pulse, sample a noise source, hold the value. Output is a staircase of random voltages, each held steady for exactly one clock cycle. Patch that to a quantizer and you get a random melody that steps in sync with your clock. S&H outputs are always stepped — the voltage jumps to a new held value, stays there, then jumps again.

**Random Sources**
Voltage that varies without a regular pattern, generated continuously rather than by sampling. Random sources come in two flavors. **Stepped random** changes abruptly from one value to another at irregular intervals — the voltage jumps without smoothing. **Smooth random** (sometimes called slewed random or random walk) transitions continuously between values, flowing between levels without sharp steps. Many modules provide both outputs simultaneously. Random CV modulating a filter cutoff creates drift. Modulating reverb size creates evolving space. The patch lives and breathes without you touching anything.

**Noise (as CV)**
White or pink noise is technically audio-rate randomness — it's oscillating at all frequencies simultaneously. But noise becomes a useful CV source when you slow it down or process it. Run noise through a slew limiter (lag processor) and the fast random movement smooths into drifting slow change. Run it through a low-pass filter and the output is a continuous gentle wander. Run it into a sample-and-hold and you get random stepped values. Raw noise into a CV input sounds like rapid chaotic scrambling; processed noise into a CV input creates organic movement.

**Sequencers (pitch output)**
The pitch output of a step sequencer generates 1V/octave voltage in a programmed pattern. This is CV. Each step stores a voltage value; the sequencer outputs them in order, advancing on each clock trigger. Unlike LFOs and random sources, sequencer pitch CV is intentional: you chose those pitches. The gate output of a sequencer is separate and belongs in the next section.

**The unified picture:** All of these — envelopes, LFOs, S&H, random, noise, sequencers — are voltage sources that change over time in different ways. Envelopes change in response to triggers. LFOs change periodically and continuously. S&H changes in discrete jumps when triggered. Random sources change unpredictably. Noise processed through slew changes slowly and organically. Any of these can go anywhere a CV input exists. The musical result depends on what changes make sense at that destination.

---

### Gates and Triggers

**What they are:** On/off voltage signals that communicate timing information — when something should start, stop, or happen.

**Gate:** A sustained voltage signal — typically 0V (off) or +5V (on). A gate stays high for as long as the event is active. On a keyboard controller, the gate is high while you hold a key and drops when you release it. Envelope generators use the gate's length to determine sustain duration.

**Trigger:** A brief voltage pulse — very short, typically 1-10ms. Triggers communicate "now," not "until further notice." Percussion envelopes often prefer triggers because they handle their own timing through the decay setting. A trigger says "fire," a gate says "fire and hold."

**Clock signals:** A repeating stream of triggers at regular intervals. This is how your system stays in time — a clock module outputs triggers at your BPM, and every other module that needs to stay synchronized follows those triggers. Clock dividers and multipliers create related pulses (half tempo, double tempo, etc.) by processing clock triggers.

**Gate vs. trigger in practice:** Many modules accept either interchangeably. Envelope generators typically respond to both — a short trigger fires the envelope and the module handles timing internally, while a gate can sustain the envelope's hold stage. If something's not responding to your timing signal, try the other type.

---

## When Signal Types Cross Over

The three types are conventions, not hard barriers. Voltage doesn't know what category it's in — only the destination module interprets it.

**LFO at audio rate:** Increase an LFO's frequency into the audio range (above ~20Hz) and it starts producing a tone. This is FM synthesis: an oscillator (the "modulator") applied to another oscillator's frequency CV input produces sidebands and complex harmonic content. The line between "control voltage" and "audio" is exactly where FM lives.

**Audio as modulation:** Run a filtered or slewed audio signal into a CV input. The waveform becomes a control signal, modulating whatever the destination controls. Run a bass oscillator's output into a filter's CV input and the filter cutoff tracks the bass waveform — not pitch-synced modulation, but waveform-driven scrubbing of the filter. Run audio through a rectifier module and you get an envelope follower: audio rate becomes control rate.

**Noise as everything:** White noise occupies all frequencies simultaneously. At audio rate it's texture. Slowed down, it's random CV. Run through a sample-and-hold it becomes stepped values. Filtered heavily it approaches a pitch. Noise is the most versatile raw material in the system precisely because it has no fixed identity.

**Why this matters:** When you understand that signal types are defined by behavior and destination rather than by some inherent property of the cable, the system becomes genuinely flexible. The question stops being "is this an audio signal or a CV signal?" and becomes "what will this voltage do at that destination?" That's modular thinking.

---

## Multiples: Passive vs Buffered

A multiple (mult) splits one output to several destinations. You want to send your sequencer's pitch CV to two oscillators, or route your master clock to three modules, or use one LFO to simultaneously modulate filter cutoff and reverb size. Mults make this possible.

The choice between passive and buffered matters more than most beginners realize — and it matters for a specific, concrete reason.

### Passive Multiples

A passive mult has no active circuitry. It's wires connected together — the input jack, the output jacks, metal touching metal. No power required. No electronics between input and output.

**What works fine through passive mults:**
- Audio signals
- Gate and trigger signals
- LFO and envelope CV where precision isn't critical

**The problem with passive mults and precision CV:** Every module input has input impedance — it presents a small electrical load to the signal source. A single destination loads the source slightly. Multiple destinations load it more. Each additional passive mult output adds another load, and that load causes a small voltage drop across the source's output impedance. The result is that the voltage arriving at each destination is slightly lower than the output voltage — and when you have several destinations, each one may receive a slightly different voltage depending on the exact impedance of each input.

For LFOs and gates, this barely matters. For 1V/octave pitch CV, it matters significantly. A 10mV voltage drop on a pitch CV means a 1/10 of a semitone pitch error. Distribute one pitch CV to three oscillators through a passive mult, and they may all play slightly different pitches. The larger your system and the more complex your pitch routing, the more noticeable this becomes.

### Buffered Multiples

A buffered mult has an active circuit — an op-amp buffer — on each output. The input is sampled, and the buffer regenerates the exact voltage at each output independently. Each destination receives the same voltage as the source, regardless of how many outputs are loaded. Buffered mults require power.

**Use buffered mults for:**
- 1V/octave pitch CV to multiple oscillators — this is the primary use case
- Any precision CV where exact voltage reproduction matters
- Long cable runs where passive voltage loss might accumulate

**The practical test:** If you're sending pitch CV from a sequencer to one oscillator and it plays in tune, then you add a second oscillator through a passive mult and the first one suddenly goes slightly sharp or flat — you need a buffered mult in that signal path.

### The Rule of Thumb

Passive mult for audio and gates. Buffered mult for pitch CV. For everything else, passive works until it doesn't — if you hear unexpected behavior when splitting a CV signal (parameter responding differently with one destination vs two), switch to buffered.

One buffered mult module covering your pitch CV distribution is usually sufficient. Two or three passive mults handle everything else.

---

## Signal Labels in These Guides

Throughout the module guides in this corpus, patch diagrams use a three-symbol system:

- **[A]** = Audio signal
- **[C]** = Control Voltage
- **[G]** = Gate or Trigger

These labels appear on patch cable endpoints and signal paths in diagrams. When you see a cable labeled [C] going from a module's output to a filter's cutoff input, it's telling you that the signal being routed is control voltage. When you see [G] going from a sequencer to an envelope, it's a gate signal triggering the envelope.

The labels exist because the same physical jack can sometimes accept different signal types, and because understanding what's flowing through a patch matters more than just knowing which jack connects to which. Reading a patch diagram fluently means understanding not just the routing but the signal character at each point.

---

## Common Mistakes

**Using a passive mult for pitch CV to multiple oscillators.** This is the most common tuning mystery in modular. Everything sounds fine with one oscillator, then you add a second voice and something's subtly off. Passive mults cause voltage drop under load. Switch to a buffered mult for any 1V/Oct signal going to more than one destination.

**Treating CV and audio as completely separate worlds.** They're not. LFOs become oscillators. Audio becomes modulation. Noise becomes CV. The categories describe typical behavior, not hard limits. Once you understand this, accidental cross-connections become experiments rather than mistakes.

**Confusing gates and triggers.** Some envelopes care about the difference; many don't. If a module isn't responding to your timing signal the way you expect, try the other type. Short triggers from a clock may not sustain an envelope's hold stage the way a gate from a sequencer would.

**Assuming noise-as-CV is just random chaos.** Raw noise into a CV input is chaotic, yes. But noise through a slew limiter is organic drift. Noise through an S&H is structured randomness. Noise is a raw material, not a finished signal.

---

## What's Next

You now have a working picture of what's flowing through your cables and why mult choice matters. The next practical step is understanding how these signal types interact at the system level — specifically, how to build patches that route voltage efficiently without running out of connections or creating unintended interactions.

The module guides referenced throughout this series use [A], [C], and [G] labels throughout their patch diagrams. With the signal type foundation in place, those diagrams become fully readable. Each labeled connection tells you not just where the cable goes, but what it's carrying and why.

---

*This guide is part of a progressive series building foundational modular understanding. Previous guide: 04_rhythm_and_percussion.md*
