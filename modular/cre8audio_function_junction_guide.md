---
title: Cre8audio Function Junction
manufacturer: Cre8audio
primary_role: ROUTER
secondary_roles: [MODULATOR]
form_factor: eurorack
functions: [envelope, function-generator, lfo, attenuverting-mixer]
behavior_tags: [stable, linear, reactive, performance-oriented]
use_cases: [envelope generation, filter modulation, LFO source, CV mixing, modulation processing]
hp: 16
historical_context: false
---

# Cre8audio Function Junction

**Four-Section Modulation Hub**

![Cre8audio Function Junction](https://github.com/Shadoe-42/music/raw/main/modular/images/cre8audio/function_junction/front_panel.jpg)  
*Cre8audio Function Junction: ADSR envelope, function generator, LFO, and three-channel attenuverting mixer in 16HP, co-designed with Pittsburgh Modular*

---

## Quick Start

**What is Function Junction?** Four modulation tools in one module: a full ADSR envelope, a function generator with curve shaping, an LFO, and a three-channel attenuverting mixer. Each section can be used independently, and the mixer is internally normalled to all three generators so it works immediately without any patch cables.

### Your First Envelope

1. Connect a gate source (sequencer or keyboard) to the **A IN** jack
2. Connect **A OUT** to the CV input of a VCA
3. Connect an audio source to the VCA audio input
4. Set Attack, Decay, and Release to around 9 o'clock; set Sustain to noon
5. Trigger a gate and hear the envelope shape the amplitude of the audio

---

## Key Specifications

| Parameter | Value |
|-----------|-------|
| Width | 16HP |
| Depth | 38mm |
| Power | 85mA +12V, 5mA -12V, 0mA 5V |
| ADSR inputs | A IN (gate/trigger) |
| ADSR outputs | A OUT; A LOOP jack (external loop gate) |
| ADSR controls | A, D, S, R knobs; LOOP button; LONG button |
| Function Generator inputs | F IN (trigger); F MOD CV |
| Function Generator outputs | F OUT; F TRIG (end-of-decay trigger) |
| Function Generator controls | Attack, Decay, Curve knobs; MOD button + knob; SUSTAIN button; LOOP button |
| LFO outputs | L TRI, L SQR |
| LFO controls | Rate knob |
| Mixer channels | 3 (Ch1 normalled to ADSR, Ch2 normalled to Function, Ch3 normalled to LFO) |
| Mixer outputs | 1 OUT, 2 OUT (individual channels 1 and 2); MIX (sum of all three); +OR (peak selector) |

---

## Essential Parameters

The ADSR section generates a standard four-stage envelope. Attack sets the rise time from zero to peak. Decay sets the fall time from peak to the Sustain level. Sustain is a level parameter, not a time parameter: it sets the voltage the envelope holds as long as the gate remains high. Release sets the fall time from Sustain level to zero when the gate closes. The LOOP button makes the envelope cycle continuously without an external gate; the A LOOP jack allows an external gate to switch looping on and off during performance. The LONG button doubles all time values, extending the range into slow, sweeping territory without changing the knob positions.

The function generator is a two-stage slope with curve shaping. Attack sets the rise time; Decay sets the fall time. The CURVE knob changes the shape of both slopes simultaneously: fully counterclockwise produces an exponential curve, center position produces a linear slope, and fully clockwise produces a logarithmic curve. This curve control is what distinguishes the function generator from the ADSR: the shape of the voltage change is a controllable parameter, not a fixed characteristic. The F TRIG output produces a trigger pulse when the decay phase completes, regardless of whether an external gate is present. The MOD button cycles through three modulation target assignments (Attack, Decay, both), and the MOD knob plus the F MOD CV input control how much incoming voltage modifies the selected time parameter. The SUSTAIN button makes the function hold at peak voltage as long as the triggering gate is high, creating an ASR (attack-sustain-release) behavior. The LOOP button makes the function cycle continuously.

The LFO section produces two simultaneous outputs from a single rate control: a triangle waveform on L TRI and a square waveform on L SQR. The Rate knob controls the speed of both. There are no separate waveform controls; triangle and square are always available simultaneously.

The mixer section has three channels, each with a single attenuverter knob. An attenuverter is bidirectional: at the fully counterclockwise position it passes the full signal inverted, at center (noon) it passes nothing, and at fully clockwise it passes the full signal positive. This means noon is zero, not unity. Turning clockwise from center increases positive signal; turning counterclockwise from center increases inverted signal. Channels 1, 2, and 3 are normalled to the ADSR output, the function generator output, and the LFO triangle output respectively. When nothing is patched into a mixer channel input, it receives its normalled signal automatically. Patching a cable into a mixer input overrides the normalled connection. The MIX output sums all three channels; the +OR output outputs only the highest voltage among the three channels at any given moment. Channels 1 and 2 also have individual outputs (1 OUT and 2 OUT) that carry those channels before the sum.

---

## Why Function Junction Excels

The central design problem Function Junction solves is that a working modular system needs multiple modulation types simultaneously: a gate needs to trigger an envelope, a filter needs a slow LFO sweep, and both of those signals may need to be scaled or combined before reaching their destinations. Assembling that capability from separate modules requires four or more modules and takes 30 to 40HP. Function Junction provides all four elements in 16HP, and the normalling system means the mixer is already connected to all three generators before the first patch cable is placed. The default state of the module is a functional modulation system.

The normalling architecture is a deliberate design choice, not a space-saving compromise. Each mixer channel receives its corresponding internal generator signal by default, so the attenuverter knobs immediately control how much of each generator contributes to the MIX output. A performer can set three modulation amounts and use the MIX output as a composite modulation source without patching anything beyond the input trigger. When an external signal needs to replace a normalled source, patching into the channel input overrides it. When both the internal and external signals are needed together, the individual section output and an external mixer handle that combination. The normalling provides a working default; the override system provides full flexibility.

The function generator section offers something the ADSR does not: curve control over both slopes simultaneously. An ADSR envelope always rises and falls according to the same fixed curve shape determined by its circuit. The function generator's CURVE knob shifts both slopes from exponential through linear to logarithmic in a single control, which means the same attack and decay time settings produce a percussive spike at one extreme, a linear ramp at center, and a slow-building swell at the other. The F TRIG output adds a second dimension: a trigger that fires specifically when the decay completes. In a patch where the function generator is looping, F TRIG produces a periodic pulse at the function cycle rate, independent of any external clock. That output can cascade into other envelope inputs, advance a sequencer, or trigger another event in the system without requiring an external clock module.

The +OR output on the mixer deserves specific attention because it functions differently from MIX. Where MIX adds the three channel voltages together, +OR passes only the highest voltage present among the three channels at any moment. If the ADSR is at 5V, the function generator is at 3V, and the LFO is at 1V, MIX outputs 9V and +OR outputs 5V. As the patch evolves and different sources peak at different times, +OR produces a kind of modulation that follows whichever source is currently dominant rather than blending all three. The musical result is a complex, time-varying waveform that switches allegiance between sources rather than combining them linearly, which produces textures that neither a simple sum nor a single modulation source can replicate.

---

## Patches

### Patch 1: Classic VCA Envelope

This patch establishes the fundamental gate-to-envelope-to-VCA signal chain using the ADSR section.

```
[Gate Source] ──▶ A IN
                   A OUT ──▶ [VCA CV Input]
[Audio Source] ──▶ [VCA Audio Input]
                   [VCA Audio Output] ──▶ [MixUp or Output]
```

**Setup:** Connect a gate output from a sequencer or keyboard to A IN. Connect A OUT to the CV input of a VCA. Connect an audio source to the VCA audio input. Connect the VCA audio output to a mixer or output module.

**Controls:** Set Attack to 9 o'clock for a quick rise. Set Decay to 10 o'clock for a short decay. Set Sustain to 2 o'clock so the envelope holds at a useful level while the gate is high. Set Release to 10 o'clock for a natural tail. Trigger gates and adjust each knob individually to hear its effect on the envelope shape. Then try the LONG button to double all times; notice that the same knob positions now produce a slower-moving envelope without any knob adjustment. Confirm that LOOP is off for this patch; if LOOP is on, the ADSR will cycle without responding to gates.

**Result:** Standard synthesizer amplitude shaping with a gate-triggered envelope controlling the VCA. The four ADSR knobs each affect a distinct phase of the envelope, and the relationship between gate length and the Sustain phase becomes immediately clear: short gates pass through Attack and Decay before the gate closes, while long gates hold the envelope at the Sustain level until the gate goes low.

---

### Patch 2: Function Generator as Slope Shaper

This patch uses the function generator section to produce shaped modulation for a filter, demonstrating how the CURVE knob changes the character of identical attack and decay times.

```
[Gate or Trigger Source] ──▶ F IN
                              F OUT ──▶ [Filter Cutoff CV]
                              F TRIG ──▶ [Second Destination or unpatched]
[Audio Source] ──────────────▶ [Filter Audio Input]
                              [Filter Audio Output] ──▶ [MixUp or Output]
```

**Setup:** Connect a gate or trigger source to F IN. Connect F OUT to the cutoff CV input of a filter. Connect an audio source through the filter to a mixer or output module. Leave F TRIG unpatched for now.

**Controls:** Set Attack and Decay both to noon. Set CURVE to fully counterclockwise (exponential). Trigger the function and listen to the filter opening and closing with a sharp exponential shape. Then move CURVE to center (linear) and listen again: same timing, different character. Then move CURVE to fully clockwise (logarithmic): the filter opens slowly and closes quickly. The three CURVE positions produce audibly distinct filter modulation shapes from the same knob positions on Attack and Decay. Once the CURVE behavior is clear, patch F TRIG to a second destination, such as the A IN jack on the ADSR section, so that each function completion triggers the ADSR as a derived event.

**Result:** Filter modulation whose shape is directly controllable via CURVE, independent of the time settings. The F TRIG output produces a pulse at each decay completion, which becomes a useful timing source for cascading modulation or advancing other events in the patch.

---

### Patch 3: Normalled Three-Source Mixer

This patch uses the mixer section with all three internal generators simultaneously, demonstrating the normalling system and the difference between MIX and +OR.

```
[Gate Source] ──▶ A IN        (triggers ADSR, normalled to Ch1)
[Gate Source] ──▶ F IN        (triggers Function, normalled to Ch2)
                               LFO runs free (normalled to Ch3)

                   MIX ──▶ [Filter Cutoff CV or other modulation target]
                   +OR ──▶ [Second modulation target]
```

**Setup:** Connect a gate source to A IN and to F IN (split from the same gate, or use separate gate sources at different rates). Leave all three mixer channel inputs unpatched so the normalling connects Ch1 to the ADSR, Ch2 to the function generator, and Ch3 to the LFO automatically. Connect MIX to a filter cutoff input. Connect +OR to a second modulation target such as VCA CV or oscillator pitch.

**Controls:** Set all three attenuverters to fully clockwise to start with maximum positive contribution from each source. Listen to MIX: the filter receives the sum of all three modulation sources simultaneously. Then listen to +OR on the second destination: it follows whichever source has the highest voltage at each moment rather than summing them. Reduce the LFO attenuverter (Ch3) toward noon and notice that +OR becomes less influenced by the LFO whenever the ADSR or function generator is active. Experiment with the ADSR loop mode: with LOOP engaged, the ADSR cycles and contributes a consistent rising-falling shape to the MIX alongside the LFO and function generator.

**Result:** A composite modulation output from three simultaneous sources, with MIX providing their sum and +OR providing peak selection. The normalling system means the entire patch works without any cables in the mixer section itself; the three internal generators are already connected.

---

### Patch 4: Cascading Envelope Chain

This patch uses the F TRIG output to create a derived envelope sequence where the function generator's decay completion triggers the ADSR, producing a two-stage modulation cascade from a single input trigger.

```
[Gate Source] ──▶ F IN
                   F OUT ──▶ [First Modulation Destination]
                   F TRIG ──▶ A IN
                   A OUT ──▶ [Second Modulation Destination]
[Audio Source] passes through both destinations to [MixUp or Output]
```

**Setup:** Connect a single gate or trigger source to F IN only; leave A IN unpatched except for the F TRIG connection. Connect F OUT to a first modulation destination (filter cutoff, VCA CV, or oscillator FM). Connect F TRIG to A IN. Connect A OUT to a second modulation destination.

**Controls:** Set the function generator to a moderate Attack and Decay (both around 10 o'clock). Set CURVE to center. Set the ADSR to a longer Attack (noon) and longer Decay and Release (both around 1 o'clock). Trigger a gate into F IN. The function generator fires first, modulating the first destination through its attack and decay. When the function generator's decay completes, F TRIG fires, which triggers the ADSR. The ADSR then modulates the second destination through its own attack, decay, sustain, and release stages. The two modulation events are sequential and time-locked by the function decay time, not by any external clock. Adjust the function decay time to change how long after the initial trigger the ADSR fires.

**Result:** A two-stage modulation sequence derived from a single trigger input. The function generator handles the immediate transient response; the ADSR handles a longer, secondary event that begins when the function completes. This cascade technique produces complex modulation behavior without any additional modules beyond the two sections already on Function Junction.

---

## Common Mistakes

### "I patched a signal into the mixer and now the modulation I expected disappeared"

The mixer channels are normalled to internal generators by default: Channel 1 receives the ADSR output, Channel 2 receives the function generator output, and Channel 3 receives the LFO. Patching any cable into a mixer channel input breaks that normalled connection and replaces it with whatever is patched. If the ADSR modulation disappeared after patching an external signal into Channel 1 input, the normalled ADSR connection was replaced by the external signal. The ADSR output did not stop; it simply no longer feeds the mixer channel.

**Fix:** To use an external signal in a mixer channel while also retaining the internal generator, take the generator's dedicated output (A OUT, F OUT, or L TRI) to an external mixer and combine the signals there before patching the result into the mixer channel. Alternatively, use the generator's output directly to its destination and use the mixer channel for the external signal only.

---

### "The attenuverter knobs do nothing at 12 o'clock"

Attenuverter knobs pass zero signal at the center (noon) position. Noon is not medium level; noon is off. Turning clockwise from center increases positive signal from zero to maximum. Turning counterclockwise from center increases inverted signal from zero to maximum negative. A knob sitting at noon contributes nothing to the output regardless of what is patched into or normalled to that channel.

**Fix:** Start attenuverter knobs at noon (zero) as a reference point only, then turn clockwise to introduce signal at positive polarity or counterclockwise for inverted. Treat noon as the zero crossing rather than as unity gain.

---

### "The ADSR keeps cycling and will not respond to my gate triggers"

The LOOP button makes the ADSR cycle continuously without waiting for gate input. In loop mode, the envelope self-triggers at the end of each release stage and ignores incoming gates entirely. If LOOP was accidentally engaged, the ADSR will appear to ignore gates because it is operating in a self-triggering mode rather than an externally-triggered one.

**Fix:** Check the LOOP button LED. If it is lit, press LOOP to disable cycling and return the ADSR to externally-triggered behavior. The A LOOP jack accepts an external gate to switch loop mode on and off during performance without pressing the button.

---

### "I cannot determine which parameter the F MOD input is modulating"

The function generator's MOD button cycles through three modulation target assignments: Attack only, Decay only, and both Attack and Decay simultaneously. The currently selected target is indicated by the MOD LED, but the LED behavior is easy to miss. The F MOD knob controls the amount of modulation applied to the selected target; if the knob is at noon (zero), no modulation reaches the target regardless of the button assignment or the signal level at F MOD.

**Fix:** Press the MOD button once and observe the LED change to identify which target is selected. Confirm the F MOD knob is turned clockwise from noon to pass positive modulation (or counterclockwise for negative modulation). Test with a slow LFO into F MOD: the selected time parameter should visibly change speed as the LFO voltage rises and falls.

---

## Advanced Learning Path

1. Work through the four ADSR knobs systematically before using them in complex patches. Patch a long gate (two or more seconds) into A IN and hold it. Sweep each knob individually from minimum to maximum while the gate is held, listening to how each stage changes. The critical distinction is that Sustain behaves differently from Attack, Decay, and Release: it sets a voltage level, not a time. With a long gate held, raising Sustain increases the voltage the envelope holds between the Decay and Release phases. Lowering Sustain reduces it toward zero. The other three knobs all set durations. Understanding this distinction before using the ADSR in a patch prevents most ADSR confusion.

2. Use the function generator's CURVE knob as a primary timbral control rather than a secondary adjustment. Set Attack and Decay to fixed positions and then sweep CURVE slowly from one extreme to the other while the function generator is looping into a filter cutoff. The same time settings produce a percussive spike, a linear ramp, and a slow swell depending on CURVE position. Once the three curve characters are clear by ear, start assigning CV to the F MOD input (set to Both) to shift the curve feel dynamically during a patch. This is modulation of modulation: the shape of the envelope changes while the envelope itself is modulating something else.

3. Build a patch that uses only the normalled mixer connections before introducing any additional patch cables into the mixer section. Trigger the ADSR with a gate, trigger the function generator with a different gate rate, and let the LFO run free. Use MIX as the sole modulation source for a filter. Spend time learning the attenuverter behavior: set all three to maximum clockwise, then reduce them one at a time to understand each generator's contribution to the summed output. This exercise makes the normalling system intuitive before the additional complexity of external signals overriding channels is introduced.

4. Explore the difference between MIX and +OR on the same source material. In the normalled mixer configuration described above, connect both MIX and +OR to two different parameters simultaneously. MIX produces a compound modulation that is the arithmetic sum of all three channels; +OR produces a selection modulation that follows only the highest voltage at each moment. The two outputs respond to the same three sources but produce fundamentally different modulation characters. Understanding when sum versus peak selection is musically useful is a practical skill: sum creates additive complexity, peak selection creates a kind of modulation priority that tends toward sharper, more switchlike behavior.

5. Use F TRIG as a timing resource rather than only as a cascade trigger. In loop mode, the function generator outputs a trigger at the end of each decay cycle, which makes F TRIG a clock source whose rate is set by the function's attack and decay times. This clock is not quantized to an external reference; it runs at whatever speed the function timing produces. Patch F TRIG to the trigger input of a sample-and-hold, a sequencer step advance, or the A IN jack of the ADSR section. The function generator's timing determines when the downstream event fires, and changing the function attack or decay time changes the clock rate without touching any clock module.

6. Practice using the attenuverter knobs as real-time performance controls during a running patch. With the normalled mixer configuration active and MIX connected to filter cutoff, set all three attenuverters to a fixed balance that produces a useful composite modulation. Then, during playback, manually reduce one attenuverter to noon to remove that source from the mix entirely, and increase it again to reintroduce it. The three attenuverters effectively become real-time faders for three simultaneous modulation sources. This workflow, using Function Junction's mixer section as a live modulation mixing surface, is distinct from using it as a static routing utility.

---

## Pairs Well With

**Instruo Cs-L** gives Function Junction's envelope and function generator outputs meaningful targets in this system. The ADSR output maps naturally to Cs-L's INDEX depth input to control the amount of cross-modulation between the two oscillator cores over time; a gate-triggered ADSR opening the INDEX depth produces FM sweeps that articulate with each note event. The function generator, with its CURVE control, is particularly useful for shaping the INDEX depth attack and decay character: exponential curve for sharp FM transients, logarithmic for slow spectral swells. The LFO triangle output can drive Cs-L's wavefold CV input for slow timbral cycling. Function Junction's mixer section can combine all three of those modulation streams into a single CV that drives a Cs-L parameter, scaling each contribution independently.

**Cre8audio Cellz** is a natural gate and trigger source for Function Junction's ADSR and function generator inputs. Each Cellz pad outputs a gate when touched and a CV value based on touch pressure or position; those gates feed A IN and F IN to trigger envelopes in direct response to performance gestures. Because both modules are Cre8audio products designed to work together, the gate voltage levels are matched and the workflow is complementary: Cellz provides event timing and CV values, Function Junction shapes those events into modulation contours and mixes them into composite CVs for downstream synthesis parameters. The 3-channel mixer receives Cellz position or pressure CVs through its inputs (overriding the normalled internal sources) and scales each with the attenuverters before summing to MIX.

**4ms RCD v2** provides a range of clock division outputs that become trigger sources for Function Junction's two trigger inputs simultaneously at different rates. Patching RCD's divide-by-2 output to A IN and divide-by-3 output to F IN creates a patch where the ADSR fires at one rhythmic rate and the function generator fires at a different rhythmic rate, with both outputs available through the normalled mixer channels. The MIX output then carries a composite of two differently-timed modulation contours summed and scaled. F TRIG from the function generator, which fires on each function completion, can feed back to RCD's reset input for synchronized polyrhythmic relationships between the clock divider and the function timing.

**Instruo Arbhar** is a direct beneficiary of Function Junction's mixer section in this system. Arbhar's four primary CV inputs (SCAN, INTENSITY, LENGTH, SPRAY) accept external modulation, and Function Junction's three mixer outputs (1 OUT, 2 OUT, MIX) provide three independent modulation paths at attenuverter-controlled levels. A configuration that routes the ADSR to SCAN, the function generator to LENGTH, and the LFO to SPRAY via the normalled mixer channels gives Arbhar continuously active modulation across three parameters from a single module, with the attenuverters acting as depth controls for each. The +OR output, tracking whichever of the three generators is currently highest, can feed a fourth Arbhar CV input (such as INTENSITY) for peak-following modulation behavior.

---

*Cre8audio Function Junction documentation: [Cre8audio](https://cre8audio.com/product/function-junction/)*
