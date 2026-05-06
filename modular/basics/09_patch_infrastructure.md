# Patch Infrastructure

**The modules and methods that carry signals from place to place, and why not all signal splitting is equal.**

Most of the work in a modular patch is conceptually visible: oscillators make tones, filters shape them, envelopes articulate them, effects process them. Patch infrastructure is the part that is easy to overlook because its job is to be invisible. It moves signals reliably from where they are to where they need to go: splitting one source to multiple destinations, bridging physical distance across a large case or between two cases, and doing all of this without degrading the signal in the process.

Get this layer right and signals arrive where you send them at the voltage you sent them, in time, without loading each other. Get it wrong and you spend a session troubleshooting pitch tracking that drifts when you add a second destination, or wondering why the left and right sides of your rack do not seem to communicate cleanly.

This guide covers the core concept of passive versus buffered splitting, and the two modules in this system that handle patch infrastructure: the Frap Tools 333 and the After Later Audio Light Rail.

---

## Passive Versus Buffered Splitting

When you want to send one signal to more than one destination, you have two options: a passive multiple or a buffered multiple. The difference matters more than it appears at first.

### Passive Multiples

A passive multiple is electrically simple: a single input jack wired to two or more output jacks with nothing in between. No power, no active components, just copper connecting the jacks in parallel. When you patch into a passive mult's input, the same wire is now connected to everything patched into its outputs simultaneously.

This works in many situations. Audio signals distributed to two destinations through a passive mult will generally sound fine. The problem is what happens to the signal when it drives multiple loads at once.

Every module input presents an electrical load: a resistance that the source signal has to drive. A single destination loads the source in one way. Two destinations in parallel halve the effective load resistance the source sees. Four destinations quarter it. As the load gets heavier, the source voltage drops. For audio signals with relatively low-impedance sources, this voltage drop is often small enough to be inaudible. For 1V/octave pitch CV, it is not: even a small voltage drop produces a pitch shift. A sequencer output that tracks perfectly when sending to one oscillator may drift measurably when split passively to three oscillators through a passive mult. The oscillators will play different pitches from the same sequencer step.

Passive mults also allow signals to interact with each other in ways that should not happen. If two outputs of a passive mult are connected to two different CV sources, those sources see each other through the mult and voltage-add unpredictably. Passive mults are one-input-to-many-outputs tools; they should not have signals arriving at their outputs from multiple sources.

### Buffered Multiples

A buffered multiple places an active circuit between the input and each output. The circuit reads the input voltage precisely, then drives each output independently from its own low-impedance source. Each output sees only the load of its own destination, not the combined load of all destinations. The input sees only the buffer's input impedance, which is typically very high, rather than the combined load of all connected modules.

The practical result: the signal arriving at each output is an accurate copy of the input signal regardless of how many outputs are in use. Pitch CV sent through a buffered mult arrives at each oscillator at the same voltage it left the sequencer. Adding a third or fourth oscillator to the split does not change what the first two receive.

Buffered mults require power and active components, which is why passive mults exist as an alternative for situations where precision does not matter. For audio signals going to two or three destinations, a passive mult is usually adequate. For 1V/octave pitch CV going to any number of destinations, a buffered mult is the correct choice.

---

## Frap Tools 333

The 333 is described on its panel as "utility" and by users as "a buffered mult." Both are accurate. What the module actually is, once you understand its architecture, is a triple buffered distribution and summing system that can handle several infrastructure jobs simultaneously depending on how it is configured.

The module has three identical sections, color-coded red, yellow, and green for visual identification. Each section is independently useful and all three can interact through a normalling architecture.

### Each Section

Every section has three inputs and three outputs. The three inputs feed a summing amplifier: whatever arrives at inputs A, B, and C is summed together and the result drives all three outputs simultaneously. The three outputs are independently buffered, meaning each one drives its destination independently without loading the others.

Used in isolation, a single section has three operating configurations depending on what is patched:

**1-to-3 buffered mult:** Patch one signal into input A. Leave inputs B and C empty. The summing amplifier sees only the one signal, and all three outputs carry buffered copies of it. This is the classic mult behavior: one source, three destinations, no loading, no drift.

**2- or 3-input mixer to 3 outputs:** Patch signals into two or three of the inputs. The summing amplifier adds them together. All three outputs carry the same sum, buffered. This is a simple, precise mixer: DC-coupled, so CVs sum accurately, and the outputs are driven independently. Three LFOs summing to three destinations in one section.

**Any combination:** Any inputs left unpatched contribute zero to the sum. The behavior scales continuously from single-source mult to full three-input mixer depending only on what is connected.

### The Normalling Architecture

The three sections are semi-normalled in series: the output of the red section is normalled to one of yellow's inputs, and the output of yellow is normalled to one of green's inputs. The normalling breaks when something is patched into those inputs directly.

This normalling allows the sections to chain. With nothing patched into yellow's normalled input jack, yellow receives red's output as one of its inputs automatically. The signal continues through: red sums, yellow receives red's output plus anything patched into its other inputs, and green receives yellow's output plus anything patched into its other inputs.

The practical consequence is that one signal patched into red's input A can propagate through all three sections and appear at all nine outputs. The 333 becomes a 1-to-9 buffered mult without any additional patching. As the sections fill with additional sources, the normalling connection is interrupted at each patched input, and the sections become increasingly independent.

### The -6dB Switch

Each section has a small switch that inserts a -6dB attenuation into that section's output stage. At -6dB, the output amplitude is halved relative to the input sum. Because the sections are normalled in series, the attenuation cascades: activating the switch on red attenuates red's output before it reaches yellow via the normal. Yellow then passes this attenuated signal to green. Activating all three switches produces -18dB total attenuation at green's outputs.

For audio, this is a level management tool. For CV, it is a precision divider: a pitch CV at 1V/octave arriving at red's input exits yellow at 0.5V/octave (with both switches active) and green at 0.25V/octave. Combined with the summing inputs, this allows the 333 to build simple CV arithmetic relationships: the same pitch information at three different scales simultaneously.

### DC Coupling

All inputs are DC-coupled. Slowly moving voltages, static offset voltages, and gate signals pass through without filtering or distortion. This is what allows the 333 to handle CV and gate signals with the same fidelity as audio. A 333 used for pitch CV distribution is receiving exactly the same electrical treatment as if it were used for audio distribution.

### In Practice

In this system, the 333 handles situations where one source needs to reach multiple destinations without voltage loss, or where a small number of sources need to reach a common destination without a dedicated mixer module. Common uses include distributing a clock signal to several modules that need tempo synchronization, sending a 1V/octave pitch source to multiple oscillators tuned to the same note, and summing two or three modulation sources before they reach a single CV destination.

The -6dB switches and normalling make the 333 a more versatile infrastructure module than its "buffered mult" description suggests. At minimum it is a precise signal distribution tool. At maximum it is a compact signal arithmetic module that handles distribution, summing, and scaling in six HP.

---

## After Later Audio Light Rail

As a rack grows in module count, the physical layout creates a problem that has nothing to do with the modules themselves: distance. A sequencer on the left side of a large case needs to send pitch and gate signals to oscillators on the right. Patch cables run across the front of the case, become difficult to trace, make the patch visually and physically dense, and can introduce noise or interference when they run near power supply areas inside the case.

The After Later Audio Light Rail addresses this by moving signals through the space behind the panel rather than across the front. It uses a standard CAT7e Ethernet cable to carry up to eight channels of CV or audio between two points in the rack.

### The Pair Architecture

Light Rail is always purchased and used as a matched pair: two identical modules with a CAT7e cable connecting them. One module sits at the source location in the rack; the other sits at the destination. Each module has eight jacks on its front panel.

The cable between them carries the signals. The CAT7e cable format uses twisted pairs of conductors that provide shielding against interference and can run significant lengths without signal degradation. A standard 3-foot cable is included with the pair, which is sufficient for most single-case routing. Longer cables can be used for connecting two physically separate cases.

### Eight Channels, Bidirectional

All eight channels are bi-directional by default. A signal patched into jack 1 on the left module appears at jack 1 on the right module. A signal patched into jack 5 on the right module appears at jack 5 on the left module. The direction is determined by where the signal originates, not by any switch or mode setting.

This bidirectionality is a significant practical advantage in live patching. The same cable that carries pitch and gate from a sequencer leftward to voices can simultaneously carry audio rightward from an effects module back to the mixing stage. The eight channels can run in different directions simultaneously as long as no single channel is being driven from both ends at the same time.

### Buffered Mode

The default unbuffered mode passes signals through the cable with no active circuitry. For most signals this is fine. For 1V/octave pitch CV where loading matters, buffering is available.

Each module can buffer up to four of its eight channels. In buffered mode, those channels take the signal arriving at the jack, buffer it locally (providing a local copy at the same jack, making an implicit mult), and send the buffered copy through the cable to the other module. The local copy is available for use at the sending end without requiring a separate mult module.

The constraint: buffered channels on one side become one-directional. If channels 1-4 on the left module are in buffered mode, those four channels send from left to right only. The remaining four channels (5-8) retain their bidirectional behavior. This asymmetry is worth planning around before building a patch that assumes bidirectionality on all eight channels.

### Cable Management as a Feature

The most immediate benefit of the Light Rail is visible rather than electrical. Eight signals that would otherwise cross the case as eight individual patch cables are consolidated into one CAT7e cable running behind the panel. The front panel of the case remains clear of long horizontal runs. Modules that logically belong together in the signal chain can be placed together physically, even if the sources and destinations are at opposite ends of the case.

In a two-case setup, the Light Rail cable connects the cases directly. A voice in one case can receive pitch from a sequencer in another without a bundle of exposed cables between them. The connection is robust enough to handle the mechanical stress of cables between cases.

### Signal Quality

The CAT7e cable is a shielded Ethernet format with individually shielded twisted pairs. Analog signals sent over it arrive at the destination without meaningful degradation at the distances typical of Eurorack use. The module makes no claim of lossless perfect reproduction for all signal types, and very fast audio transients or high-frequency audio may behave differently than CV signals in the unbuffered path, but for the primary use cases of CV routing and rhythmic audio distribution, the signal fidelity is adequate.

---

## Routing Diagrams

### Single-Source to Multiple Oscillators via 333

```
[Sequencer pitch output] [C]
         │
         ▼
[333 Section 1: Input A]
         │
         │  buffered sum (single source)
         ├─────────────────────────────────────────┐
         │                                         │
         ▼                                         ▼
[333 Output 1A → Oscillator 1 V/Oct] [C]  [333 Output 1B → Oscillator 2 V/Oct] [C]
                                          [333 Output 1C → Oscillator 3 V/Oct] [C]
```

All three oscillators receive the identical pitch voltage regardless of how many are connected. Adding or removing oscillators from the 333 outputs does not affect pitch accuracy at the remaining connections.

---

### Two Modulation Sources Summed to One Destination via 333

```
[LFO 1 output: slow triangle] [C]
[LFO 2 output: faster sine]   [C]
         │
         ▼
[333 Section 2, Input A: LFO 1]
[333 Section 2, Input B: LFO 2]
         │
         │  summed CV
         ▼
[333 Output 2A → Filter cutoff CV] [C]
[333 Output 2B → VCA level CV]     [C]
```

The filter and VCA both receive the same composite modulation from two sources. Section 2 acts as mixer and mult simultaneously without occupying a separate mixer module.

---

### Cross-Case Signal Bundle via Light Rail

```
Case A (left case):
[Sequencer pitch out]  [C] → [Light Rail A: Jack 1]
[Sequencer gate out]   [G] → [Light Rail A: Jack 2]
[Clock out]            [G] → [Light Rail A: Jack 3]
[Accent gate out]      [G] → [Light Rail A: Jack 4]

                    CAT7e cable

Case B (right case):
[Light Rail B: Jack 1] → [Oscillator V/Oct] [C]
[Light Rail B: Jack 2] → [Envelope trigger] [G]
[Light Rail B: Jack 3] → [Clock destination] [G]
[Light Rail B: Jack 4] → [Accent input]      [G]

Return path (same cable, channels 5-8):
[Effects send]  [A] ← [Light Rail B: Jack 5]
[Effects return][A] → [Light Rail A: Jack 5]
```

Four signals travel from Case A to Case B. One audio signal (effects send/return) travels in the opposite direction simultaneously on the same cable. The front panels of both cases remain clear of cross-case patch cables.

---

## Common Mistakes

**Using a passive mult for 1V/octave pitch.** The most common patch infrastructure error, and the source of tuning problems that are difficult to diagnose without understanding the underlying cause. If oscillators drift out of tune when more of them are added to a mult, the mult is almost certainly passive. Replace it with the 333 or any buffered mult. The sequencer and oscillators are likely both working correctly; the signal path between them is the problem.

**Patching signals into the 333's normalled inputs without checking what is already normalled there.** The semi-normalling between sections means that certain inputs are already receiving a signal from the previous section unless something is patched there directly. Patching a second signal into a normalled input adds it to whatever was already arriving from the normal. The result is an unexpected sum rather than the independent routing you intended. Check the normalling path before assuming a section's inputs are empty.

**Expecting the 333 to be transparent when all three -6dB switches are active.** Three active -6dB switches cascade to produce -18dB, which is significant attenuation. If a signal seems weaker than expected at the 333's outputs, check the switch positions on all three sections before looking elsewhere.

**Driving a Light Rail channel from both ends simultaneously.** The Light Rail channels are bidirectional, but driving the same channel from both ends creates a signal conflict: two sources fighting over the same conductor. The voltage at each end becomes unpredictable. Plan the direction of each channel before patching, and treat each channel as either sending from the left module or sending from the right module, not both.

**Using the Light Rail unbuffered for precise 1V/octave pitch over long cable runs.** The unbuffered path is appropriate for most CV and audio signals at typical Eurorack cable lengths. For precise pitch tracking over longer runs or when loading from the destination modules is a concern, use the Light Rail's buffered mode on those channels. The buffered copy at the sending end also serves as a local mult, which may save a separate mult module in some patches.

**Treating the Light Rail cable as ordinary patch cable.** The CAT7e cable carries up to eight channels simultaneously and is a physical connection between rack sections or cases. Unplugging it during a running patch interrupts all eight channels at once. This is obvious once stated, but easy to forget in a dense patch where the cable runs behind panels out of view. Treat Light Rail reconnection the same way you would treat rebuilding eight individual patch connections.
