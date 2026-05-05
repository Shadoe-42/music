# Signal Chain Literacy

**How voltage moves through a patch — the three paths, where they meet, and why the chain breaks when one is missing.**

The module guides in this series explain what each module does. Manufacturer manuals explain what each module does. Neither shows what a complete patch looks like from the first cable to the last, why each connection is there, or how to find the broken link when something is not working. This document fills that gap.

The organizing insight: even the simplest patch that produces a single shaped note has three separate signal paths running in parallel. All three must be complete and connected correctly for sound to occur. Most patching failures are not random — they are a specific missing or misrouted path. Once you can see the three paths as distinct, you can build them deliberately and diagnose them quickly when something goes wrong.

This document builds a complete voice from one cable to many, explains each path as it is added, and then covers the infrastructure concepts that determine whether the patch behaves the way you intended: signal conditioning, VCAs as dynamic controllers, coupling, and the output stage. Signal types — what audio, CV, and gates are — are covered in the previous basics guide. This document assumes that foundation and builds from it.

---

## The Simplest Possible Patch

Start with one cable.

```
[VCO Audio Out] ────────────[A]──────▶ [Mixer In]
```

An oscillator (VCO — voltage controlled oscillator, the module that generates the raw tone) connected directly to a mixer. The result: a tone that starts when the system powers on and never stops. It plays at one fixed pitch with no dynamics. It is the sound of a complete audio path with nothing else.

This patch has exactly one path: audio. The oscillator generates a waveform oscillating at its set frequency; the mixer receives it and passes it to the output. That is all that is happening.

Everything missing from this patch is what the rest of this document is about.

---

## Adding the Door: The VCA

A voice that never stops is not a musical instrument. To shape when sound begins and ends, a module must sit between the oscillator and the mixer with the ability to open and close the signal path on command. That module is a VCA (voltage controlled amplifier — a module whose gain, and therefore the volume of whatever passes through it, responds to a control voltage).

```
[VCO Audio Out] ────────────[A]──────▶ [VCA Audio In]
[VCA Audio Out] ────────────[A]──────▶ [Mixer In]
```

The VCA is now in the audio path. But with nothing controlling it, its gain is zero and it is closed. The audio path exists and is connected, but no signal passes. Adding the VCA without adding anything to control it produces silence.

The VCA is a door. It needs a key.

---

## Adding the Key: The Gate and Envelope Path

The key is a second signal path that runs in parallel with the audio path and never carries audio itself. It carries timing and shape information: when to open the door and how to open it.

A sequencer (or any source that generates gates) outputs a gate signal — a voltage that goes high when a note is active and drops when the note ends. That gate triggers an envelope generator, which converts the on/off gate into a shaped voltage contour: a rise, a hold, a fall. The envelope generator's output is control voltage. It goes to the VCA's CV input.

```
GATE / ENVELOPE PATH

[Sequencer Gate Out] ───────[G]──────▶ [Envelope Trigger In]
[Envelope CV Out] ───────────[C]──────▶ [VCA CV In]


AUDIO PATH

[VCO Audio Out] ─────────────[A]──────▶ [VCA Audio In]
[VCA Audio Out] ─────────────[A]──────▶ [Mixer In]
```

Now when the sequencer fires a gate, the envelope triggers, its CV output rises, the VCA opens in response to that rising voltage, and audio passes. When the gate drops, the envelope releases, the CV falls, and the VCA closes. The patch produces shaped note events that start and stop with musical timing.

The VCA is where the audio path and the gate/envelope path converge. The audio path flows through the VCA. The gate/envelope path terminates at the VCA's CV input. These two paths share one point of contact: the VCA. Everywhere else they are completely separate.

---

## Adding Pitch: The Third Path

With the patch above, the oscillator plays one fixed pitch for every note event. The gate path determines when notes happen; the audio path carries the sound; but there is nothing telling the oscillator what pitch to play. That is the third path.

```
PITCH PATH

[Sequencer Pitch CV Out] ────[C]──────▶ [VCO V/Oct In]


GATE / ENVELOPE PATH

[Sequencer Gate Out] ────────[G]──────▶ [Envelope Trigger In]
[Envelope CV Out] ────────────[C]──────▶ [VCA CV In]


AUDIO PATH

[VCO Audio Out] ──────────────[A]──────▶ [VCA Audio In]
[VCA Audio Out] ──────────────[A]──────▶ [Mixer In]
```

The pitch path carries 1V/oct control voltage from the sequencer to the oscillator's pitch input. The oscillator reads this voltage and sets its frequency accordingly: 0V produces one pitch, 1V produces a pitch one octave higher, 2V produces a pitch two octaves higher, and so on. This is the V/oct (volts per octave) standard.

The pitch path terminates at the oscillator. It does not merge with the audio path or the gate path anywhere. The oscillator uses the pitch CV to set its frequency and then generates audio; the audio path begins at the oscillator's audio output. The pitch information is consumed at the oscillator and is not present in the audio signal itself.

---

## The Complete Three-Path Voice

```
PITCH PATH (ends at VCO)

[Sequencer Pitch CV Out] ────[C]──────▶ [VCO V/Oct In]
                                                │
                                         (sets frequency)
                                                │
                                                ▼
AUDIO PATH (source to output)           [VCO Audio Out] ──[A]──▶ [VCA Audio In] ──[A]──▶ [Mixer]
                                                                          ▲
                                                              (paths converge here)
                                                                          │
GATE / ENVELOPE PATH (ends at VCA CV)                                    │
                                                                          │
[Sequencer Gate Out] ────────[G]──────▶ [Envelope Trigger In]            │
[Envelope CV Out] ────────────[C]──────────────────────────────────────────
```

Three paths. Three signal types. Two places where paths end without merging (the VCO and the envelope), and one place where two paths converge (the VCA).

This structure holds for patches of any complexity. A patch with four voices has four audio paths, four gate/envelope paths, and four pitch paths. An effects chain extends the audio path through processors before the mixer. Modulation sources (LFOs, secondary envelopes) add branches to the gate/envelope path that reach other CV inputs. The three-path model scales with the patch, but the fundamental structure does not change.

---

## Diagnosing a Broken Patch

Most patching failures map directly to one of the three paths. The failure mode tells you which path to trace.

**Sound, but no dynamics — the note plays continuously and does not shape with the gate.** The gate/envelope path is broken or bypassed. Check that the sequencer gate is reaching the envelope trigger input; check that the envelope CV output is reaching the VCA CV input; check that the VCA CV attenuator is turned up enough to open the gate. A VCA with its CV attenuator at zero hears the envelope but does not respond to it.

**The envelope fires visually, but no audio passes.** The audio path is broken. The VCA is opening but nothing is arriving at its audio input, or its audio output is not reaching the mixer. Trace the audio path from the oscillator output: is audio present at the VCA input? Is the VCA audio output patched to the mixer, not a CV input?

**Pitch changes in the sequence are not audible — the voice plays, but all notes sound the same.** The pitch path may be broken or not patched. Check that the sequencer pitch output is reaching the oscillator V/oct input, and that the V/oct input is the correct jack — many oscillators have multiple CV inputs, and some attenuate or offset pitch differently than the dedicated V/oct input.

**No sound at all.** Any of the three paths could be the problem. Trace the audio path first: is audio present at the oscillator output? Then check the VCA: is it receiving CV and opening? Then check whether GAIN is up — a VCA with initial gain at zero will pass nothing regardless of CV. The 100 Grit in this rack requires GAIN to be above zero before any signal passes from either output. Most other VCAs in the rack default to closed without CV.

The diagnostic principle: isolate each path and confirm it is complete before assuming something is broken at the hardware level. The vast majority of silent patches have a missing cable, a closed VCA, or a CV input turned to zero.

---

## When Paths Split: The Mult as Context-Splitter

A multiple (mult) sends one output signal to two or more destinations simultaneously. It does not change the signal. It puts the same voltage into two different contexts, and the context — the destination module and how it interprets the incoming voltage — determines what happens at each end.

```
                                     ┌──[A]──▶ [Mixer Ch1]      (heard as audio voice)
[VCO Audio Out] ────[A]──▶ [Mult] ───┤
                                     └──[A]──▶ [VCO 2 FM In]    (heard as FM modulation)
```

The signal leaving the mult is identical at both outputs. At the mixer, it is heard as a voice. At VCO 2's FM input, it is interpreted as audio-rate frequency modulation of VCO 2's pitch, producing sidebands and complex harmonic content. Both results are heard simultaneously and they are coupled: changing VCO 1's pitch changes both the voice in the mixer and the FM character of VCO 2.

The mult is not a passive convenience. It is what allows one signal to exist in multiple roles simultaneously. Patching intentionally means knowing what role each branch plays and whether the level at each destination is appropriate for that role.

**Level management per branch:** the same signal going to two destinations often needs different treatment at each. An FM input expecting 0-5V receiving a full ±5V audio signal gets double the expected modulation depth. A mixer input expecting line-adjacent levels from a VCA receiving a raw oscillator output at ±5V may be too hot for comfortable mixing. Each branch of a mult may need independent conditioning before it reaches its destination. The mult splits; the attenuverter shapes each branch to match what the destination expects.

For passive versus buffered mult selection in pitch CV applications, refer to the previous basics guide. The rule carries forward here: buffered mult for 1V/oct pitch CV to multiple oscillators; passive mult acceptable for audio and non-critical CV.

---

## Signal Conditioning: The Invisible Layer

Most documentation shows patches as source → destination. The actual path is often source → conditioner → destination. Conditioning is the step that translates the signal you have into the signal the destination expects. It is called invisible because it does not produce sound and is not the subject of any module guide; it is infrastructure.

Why conditioning is necessary: Eurorack has no enforced compatibility standard between module outputs and inputs. A module outputs whatever voltage it produces; an input expects whatever voltage it was designed for. These two voltages are frequently different. A signal arriving outside a module's expected range does not produce an error — it produces an uncontrolled result. Conditioning converts uncontrolled into intentional.

```
[LFO Out ±5V] ──────[C]──────▶ [MISO In] ────────[C]──────▶ [Filter Cutoff CV]
                                (attenuate to 0–3V,
                                 invert if needed)
```

**Attenuation** reduces the voltage range. An LFO swinging ±5V patched directly to a filter cutoff CV input produces maximum modulation depth — the filter sweeps its entire range on every LFO cycle. If the intention is subtle movement, an attenuverter (a module that attenuates and optionally inverts a signal) between the LFO and the filter cutoff reduces the LFO's effective voltage range to whatever produces the desired modulation depth.

**Inversion** flips polarity. If a modulation source is going in the wrong direction — a rising envelope is closing a filter rather than opening it — inverting the signal before it reaches the input reverses the direction without changing the source.

**Offset** shifts the voltage range. A bipolar signal swinging ±5V (centered on 0V) offsetting to a unipolar range of 0-10V moves the center point up. This matters when a destination expects only positive voltage: a bipolar LFO modulating a parameter that has no meaningful behavior below 0V is wasting half of its swing.

**The MISO in this rack** provides two independent channels of attenuation and inversion. It has no musical transformation — it does not filter, distort, or add harmonics. It scales, inverts, and offsets. It is signal management before a destination, not a sound design tool in itself.

**The Eris in this rack** (Altered States Machines Eris) is a 4x4 matrix router: four inputs, four outputs, with independent gain at each routing intersection. This is conditioning and routing combined. Any of the four inputs can be routed to any of the four outputs, at any level, simultaneously. If VCO 1 audio needs to go to the mixer at full level and also to VCO 2's FM input at reduced level and also to a filter's CV input at a further reduced level, the Eris handles all three branches with independent attenuation per path. The distinction between a matrix router and an attenuverter bank is one of scale: the Eris does both routing decisions and level decisions at each intersection.

When a modulation source is behaving unexpectedly — too much effect, too little, going the wrong direction, or shifting a parameter in an unintended range — the answer is almost always conditioning, not a different source. Attenuate to reduce depth. Invert to reverse direction. Offset to shift the effective range.

---

## VCAs: The Universal Dynamic Controller

A VCA (voltage controlled amplifier) is a module whose gain responds to a control voltage. This definition sounds narrow. The applications are not.

```
AMPLITUDE CONTROL (audio through a VCA):

[VCO Audio Out] ────[A]──────▶ [VCA Audio In]
[Envelope CV Out] ──[C]──────▶ [VCA CV In]
[VCA Audio Out] ─────────────▶ [Mixer]

Result: audio starts and stops with musical shaping


MODULATION DEPTH CONTROL (CV through a VCA):

[LFO Out] ──────────[C]──────▶ [VCA Audio In]
[Envelope CV Out] ──[C]──────▶ [VCA CV In]
[VCA Audio Out] ─────────────▶ [Filter Cutoff CV]

Result: LFO depth grows and fades with each note
```

In the first configuration, the VCA controls the amplitude of audio — the standard voice envelope application. In the second, the VCA controls the amplitude of a CV signal — specifically, how deep an LFO modulates a filter cutoff. When the envelope is high, the LFO sweeps the filter through its full attenuated range. When the envelope drops, the LFO modulation fades with it. The depth of the modulation itself has become a dynamic parameter.

This is the principle behind "you never have enough VCAs." Every voice needs at least one VCA for amplitude shaping. Every modulation destination where the depth needs to change dynamically over time needs a VCA in the modulation path. Every send level in an effect routing that needs to open and close needs a VCA. These are independent applications requiring independent VCAs; they cannot share.

**Linear versus exponential curve:** a linear VCA responds proportionally to its control voltage — halve the CV, halve the gain. An exponential (logarithmic) VCA follows a curve matched to human hearing, where perceived loudness is proportional to the logarithm of amplitude. A linear VCA with a standard decay envelope will sound like it sustains too long, then cuts off sharply at the end: the last portion of a linear decay represents a small absolute voltage change, but that small change is audible as a sharp drop because human hearing is most sensitive to level differences at low amplitudes. The same envelope on an exponential VCA sounds like a natural fade because the curve matches the ear's response. The curve is a perceptual matching tool, not a tone control. If a decay shape sounds wrong — sluggish and then sudden, rather than smooth — the curve setting is the first thing to check.

**Initial gain (bias):** many VCAs include a manual gain control that sets a base amplitude level without any CV present. This allows the VCA to pass signal at a fixed level when CV is not patched — functioning as a static attenuator — and to use CV to modulate above or below that base level when CV is present. A VCA with initial gain set to 50% and no CV is an attenuator at half level. The same VCA with an envelope on the CV input swings between 0% and the envelope's peak, offset by the initial gain setting.

---

## DC Coupling and AC Coupling: An Invisible Failure Mode

Eurorack modules use two different coupling approaches at their inputs, and the difference determines what kinds of signals can pass correctly. This distinction is not typically labeled on panels and is often not mentioned in manuals, which makes it one of the most common silent failure modes in patching.

**DC coupling** passes the full signal, including any constant voltage offset and very slow changes. A pitch CV of 2.5V — a steady, non-oscillating voltage — passes through a DC-coupled input without loss.

**AC coupling** blocks the DC component and passes only the time-varying portion of the signal. The coupling capacitor at the input filters out anything below a cutoff frequency, typically around 10-20Hz. Signals that change quickly (audio) pass without loss. Signals that change slowly (envelopes, slow LFOs, pitch CV) are filtered out substantially or entirely.

Audio inputs on most Eurorack modules are AC-coupled. This is correct behavior for audio: it removes any DC offset that would waste amplifier headroom and could damage speakers. CV inputs on most modules are DC-coupled, because the slow, steady voltages that CVs carry need to reach their destinations without being filtered away.

```
WORKING: slow LFO to DC-coupled CV input

[LFO Out 0.1Hz] ────[C]──────▶ [Filter Cutoff CV In]   ✓ full sweep audible


FAILING: slow LFO to AC-coupled audio input

[LFO Out 0.1Hz] ────[C]──────▶ [VCA Audio In]           ✗ almost no signal passes
                                (AC coupling blocks
                                 the slow LFO content)
```

The failure mode: a slow LFO is producing a waveform that, at any given moment, appears nearly constant to the coupling capacitor. The capacitor blocks it. The result sounds weak or completely absent. The LFO is working. The cable is connected. The destination module is receiving voltage. Nothing appears broken from the outside. The coupling is the mismatch.

**The practical rule:** slow CV — envelopes, slow LFOs, pitch voltage, any signal that changes on timescales longer than about 20ms — must reach DC-coupled inputs. CV inputs are almost always DC-coupled; audio inputs are almost always AC-coupled. The failure occurs when a CV signal is accidentally routed to an audio input rather than the correct CV input on the destination module. If a modulation source appears to have no effect and all cables are connected, check whether the destination jack is an audio input rather than a CV input.

At audio rates, the distinction matters less: a fast LFO or an audio-rate signal passes through AC-coupled inputs without significant loss, because the signal changes fast enough that the coupling capacitor cannot block it. This is the territory where audio-as-modulation works: an oscillator's audio output used as FM into another oscillator's CV input passes through correctly because both signals are fast enough for either coupling type.

---

## The Output Stage: Where the Chain Ends

The audio path terminates at the output stage, which is the interface between the modular system and everything outside it. This stage is not decorative infrastructure. It performs a specific electrical translation that the rest of the chain cannot.

Eurorack audio operates at ±5V (10 volts peak-to-peak), which is significantly louder than line level. Professional line level is approximately +4dBu (roughly 1.2V peak); consumer line level is approximately -10dBV (roughly 0.3V peak). Patching a Eurorack audio output directly into a recording interface input, studio monitors, or a guitar amplifier sends a signal four to ten times hotter than those inputs expect. The result is clipping at the receiving device, excessive volume, and in some cases damage.

```
AUDIO PATH THROUGH OUTPUT STAGE

[VCA Audio Out] ──────[A]──────▶ [MixUp CH1 In]
                                          │
                            (mix multiple voices here)
                                          │
[MixUp Main Out L] ───[A]──────▶ [Cockpit 2 In L]
[MixUp Main Out R] ───[A]──────▶ [Cockpit 2 In R]
                                          │
                            (level conversion here)
                                          │
[Cockpit 2 Out L] ────[A]──────▶ [Interface / Monitors]
[Cockpit 2 Out R] ────[A]──────▶ [Interface / Monitors]
```

**The Cockpit 2 in this rack** (Endorphin.es Cockpit 2) is the output stage. It accepts audio at Eurorack levels, mixes up to four inputs to a stereo bus, and outputs at a level appropriate for line-level destinations — a recording interface, studio monitors, or a performance mixer. The level knob on the Cockpit 2 controls the output level going out to the interface; it is not a makeup gain or a creative control. It is a practical level management tool at the system boundary.

**The MixUp in this rack** (Intellijel MixUp) is a mixing stage that precedes the output stage, not a replacement for it. MixUp balances the levels of multiple voices against each other before the combined signal reaches Cockpit 2. These are different functions at different points in the chain: MixUp manages the internal mix relationship; Cockpit 2 manages the interface with the external world. Having both is not redundant.

**Stereo and TRS adapters:** some output modules accept stereo signals through a single TRS (tip-ring-sleeve) jack. A standard Eurorack patch cable is TS (tip-sleeve) and carries one channel. Connecting a TS cable to a TRS stereo input sends only one channel; the other side of the stereo field is silent or absent. TRS adapters or a TRS-to-dual-TS (insert cable) split the stereo signal correctly. This is a physical connection issue with no electrical error indicator — the audio works, but the stereo field is collapsed to one side. If a stereo module appears to produce only mono output, check whether a TRS connection is being driven by a TS cable.

**Why not patch directly to monitors without an output module:** a direct Eurorack output into studio monitors skips the level translation stage. The monitors receive a signal at four to ten times their expected input level, which causes their input amplifier to clip. Even at moderate modular levels, the dynamic range is compressed at the monitor's input stage before the monitor's own amplifier has a chance to manage it musically. The output module is not optional when the destination is a playback system or a recording interface.

---

## The Complete Chain in One View

A full single-voice patch with output routing, showing all three signal paths plus conditioning and the output stage:

```
PITCH PATH

[Hermod+ Pitch CV] ──────────────────[C]──────▶ [VCO V/Oct In]


GATE / ENVELOPE PATH

[Hermod+ Gate Out] ──────────────────[G]──────▶ [Envelope Trigger In]
[Envelope CV Out] ───────────────────[C]──────▶ [MISO In] ──[C]──▶ [VCA CV In]
                                                 (attenuate
                                                  to taste)

AUDIO PATH

[VCO Audio Out] ─────────────────────[A]──────▶ [Filter Audio In]
[Filter Audio Out] ──────────────────[A]──────▶ [VCA Audio In]
[VCA Audio Out] ─────────────────────[A]──────▶ [MixUp CH1]
[MixUp Main Out L/R] ────────────────[A]──────▶ [Cockpit 2 In L/R]
[Cockpit 2 Out L/R] ─────────────────[A]──────▶ [Interface]


MODULATION (branch of gate/envelope path)

[LFO Out] ───────────────────────────[C]──────▶ [MISO Ch2 In]
[MISO Ch2 Out] ──────────────────────[C]──────▶ [Filter Cutoff CV]
                                                 (LFO depth set
                                                  by MISO level)
```

The pitch path ends at the VCO. The gate/envelope path branches: the primary branch shapes the VCA amplitude; the secondary branch carries the LFO through MISO conditioning to the filter. The audio path runs from the VCO through the filter and VCA to the mixer and out through the output stage. The VCA is where the audio path and the envelope path converge. The filter is where the audio path and the modulation branch meet. Every connection has a reason; every signal type is appropriate for its destination.

---

## What This Document Is Not the End Of

This document covers one voice, understood completely. It does not cover multiple simultaneous voices and how they share infrastructure, CV mixing and summing before shared destinations, gate and trigger logic (AND/OR operations on gate signals), or the full depth of modulation routing in complex patches. Those concepts build on the three-path foundation established here and are the subject of follow-on documents in this series.

If a patch is not working and you cannot identify the problem, return to the three-path diagram. Trace the audio path from source to output. Trace the gate/envelope path from the gate source to the VCA CV input. Trace the pitch path from the sequencer to the oscillator. One of them is incomplete. When you find it, the patch will work.

---

*This guide is part of a progressive series building foundational modular understanding. Previous guide: 05_signal_types_and_mults.md*
