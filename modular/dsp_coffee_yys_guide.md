---
title: "DSP Coffee YYS"
manufacturer: "DSP Coffee"
primary_role: UTILITY
secondary_roles: []
historical_context: true
form_factor: eurorack
functions: [attenuator, mixer, cv-processor]
behavior_tags: [clean, linear, performance-oriented]
use_cases: [bipolar CV mixing and cancellation, distributing modulation with polarity control, stereo bus signal distribution, pre-patch signal monitoring]
hp: 8
depth: 20mm
memory: none
transport: none
screen: false
hybrid: false
cv: none
---

![DSP Coffee YYS front panel](https://github.com/Shadoe-42/music/raw/main/modular/images/dsp_coffee/yys/front_panel.jpg)

## Historical Context

The operational amplifier is not a synthesizer component that happens to handle audio. It is a precision analog computing circuit that synthesizer designers borrowed from a longer tradition of using electrical voltages as mathematical variables.

Vannevar Bush's differential analyzer at MIT (1931) was among the first large-scale machines built on the principle that a voltage could represent a number, and that physical circuits performing addition, subtraction, and integration could therefore solve differential equations. The summing amplifier was one of that tradition's core building blocks: route two voltages into a common node with precision resistors and an amplifier, and the output is their sum. Scale one input through a resistor of a different value, and the output is a weighted sum. Reverse the sign of the weighting, and you subtract rather than add. The same circuit computes all of these operations depending only on its configuration.

George Philbrick commercialized the operational amplifier in the early 1950s. His K2-W op-amp (1952) made the building block accessible to engineers outside research laboratories, and the analog computing tradition it enabled spread into instrumentation, control systems, and eventually electronic music. When Robert Moog designed the circuits for his synthesizers in the 1960s and Don Buchla designed his, both drew directly on that op-amp heritage. The summing amplifier inside a mixer, the scaling amplifier inside a VCA, the inverting amplifier that flips a signal's polarity: these are not separate inventions. They are configurations of the same foundational circuit applied to audio and control voltages.

The A/B bus architecture of professional mixing consoles added a spatial dimension to that mathematics. When stereo recording became standard in the 1950s and 1960s, console designers needed a way to route any source to a left bus, a right bus, or any proportion of both. The pan pot (panoramic potentiometer) solved this by distributing each source between the two buses. Neve, API, and SSL all refined this architecture through the 1960s and 1970s, and the A/B stereo bus became the standard mental model for thinking about where sound lives in a mix.

The attenuverter extends the pan pot concept beyond panning. A pan pot distributes signal between two buses with the constraint that the total contribution is conserved: as more goes to the left bus, less goes to the right. An attenuverter applies independent gain to each bus, including negative gain. One source can contribute positively to bus A and negatively to bus B, or fully to A and nothing to B, or equally to both in the same polarity, or opposing polarities simultaneously. These are not panning decisions; they are arithmetic decisions about the relationship between the two bus voltages.

DSP Coffee's YYS takes this architecture into modular synthesis directly: four inputs, each with two independent bipolar attenuverters, summing to two output buses with both normal and inverted output jacks and buffered LED monitoring per channel. The name "Bipolar Motion Consolidator" describes the function precisely: bipolar signals (positive and negative) in motion (CV or audio) consolidated (summed to buses) from multiple sources.

## Quick Start

1. Patch a slow LFO into input 1. Turn the A-attenuverter for input 1 clockwise past center. A scaled version of the LFO appears at output A and its inverse appears at output A-inv. The bipolar LED for input 1 lights in alternating colors corresponding to positive and negative phases of the LFO.
2. Patch a second LFO at a different rate into input 2. Turn the A-attenuverter for input 2 counterclockwise past center. Input 2 now contributes an inverted version of its LFO to bus A. Output A carries the sum of LFO 1 positive and LFO 2 inverted: complex motion, not a simple combined LFO.
3. Patch output A to a filter cutoff. Adjust the A-attenuverter amounts for inputs 1 and 2. The filter cutoff moves in a composite pattern that reflects both LFO rates and their polarities.
4. Turn the B-attenuverter for input 1 clockwise. Output B now receives the same LFO 1 as bus A, but at an independently set level. Patch output B to a VCA. The same source drives two different targets with potentially different contributions.

## Key Specifications

| Specification | Value |
|---|---|
| Width | 8 HP |
| Depth | 20 mm |
| +12V Current | 24 mA |
| -12V Current | 24 mA |
| +5V Current | 0 mA |
| Inputs | 4 |
| Outputs | 4 (A, A-inv, B, B-inv) |
| Attenuverter knobs | 8 (two per input) |

**Power note:** Equal draw on the +12V and -12V rails (24 mA each) is typical for a bipolar op-amp design. The symmetric draw confirms the module operates with a bipolar voltage supply throughout and that the negative rail carries real load.

## Essential Parameters

**Inputs (4 jacks).** The four input jacks accept any signal: audio, CV, gate, or clock. The module is DC-coupled, so slowly moving voltages (offset CVs, sustained gates, steady pitch offsets) pass through alongside audio-rate signals without distortion or filtering. Each input feeds both attenuverter knobs for that channel simultaneously; what goes into input 1 is always available to both the A-attenuverter and the B-attenuverter for channel 1.

**A-attenuverter per channel (4 knobs).** Each channel has one knob controlling how much of that input's signal goes to bus A, and in what polarity. Center position is zero: no contribution to bus A from that channel. Turning clockwise from center sends a positive-polarity, increasingly scaled version of the input to bus A. Turning counterclockwise from center sends a negative-polarity (inverted), increasingly scaled version of the input to bus A. The same input can contribute positively to bus A while its B-attenuverter contributes negatively to bus B, or vice versa.

**B-attenuverter per channel (4 knobs).** Identical in behavior to the A-attenuverter, but routing to bus B independently. Channels 1 through 4 each contribute to bus B according to their own B-attenuverter settings, summed together at the B output. The A-attenuverter and B-attenuverter for any given channel are completely independent: one can be at full CW while the other is at full CCW, or both at center, or any combination.

**Outputs A and B.** Output A carries the summed, attenuverter-scaled contributions of all four channels to bus A. Output B carries the summed contributions of all four channels to bus B. These outputs are affected by all eight A-attenuverter and B-attenuverter settings simultaneously. Changing any attenuverter changes the relevant bus output in real time.

**Outputs A-inv and B-inv.** The A-inv output is the mathematical inverse of output A: wherever A is positive, A-inv is equally negative, and wherever A is negative, A-inv is equally positive. B-inv is the same relationship to output B. These are not separate buses with independent routing; they are derived from A and B respectively. Patching A and A-inv simultaneously to two different destinations gives two signals with an exact mirror relationship: when one rises, the other falls by the same amount. This is available at no additional cost; A-inv and B-inv are always present without any additional configuration.

**Bipolar LEDs (4, one per channel).** Each channel has a dedicated bipolar LED that monitors the signal at that input. The LEDs are buffered separately from the signal path, meaning they do not load or affect the input signal or the bus outputs. Green light indicates positive voltage at the input; red light indicates negative voltage. The brightness of the LED corresponds to the signal amplitude. Checking the LED before setting attenuverter positions confirms that the source is present and shows its polarity and approximate level without requiring a cable at the output. This is the intended pre-patch monitoring workflow.

## Why the YYS Excels

Standard mixing in modular synthesis is additive: sources go in, levels are set, the sum comes out. The result is always more than any individual source, in the same direction. The YYS makes subtraction available. Any input can be sent to a bus with negative gain, which means it pulls the bus output downward while other inputs push it upward. Two inputs of equal amplitude, one positive and one negative at the same level, cancel each other completely. Two inputs at similar amplitudes with opposing polarities produce a complex remainder: sometimes canceling, sometimes reinforcing, moving between these states as the inputs change.

For CV this creates modulation shapes that no single LFO or envelope can produce. Two LFOs at slightly different rates, one positive and one inverted in the same bus, produce a beat-frequency-like pattern: the sum grows larger when they partially align and shrinks toward zero when they oppose. The resulting bus output has a rhythm derived from the relationship between the two sources rather than the properties of either source alone.

The four-output architecture (A, A-inv, B, B-inv) multiplies the options without multiplying the modules. A single patch of sources into the YYS produces four related but distinct output signals simultaneously. Using A for one target and A-inv for another creates an automatic opposing relationship: what drives one parameter up drives the other down at the same rate and amount. This is inherently useful for any pair of parameters where inverse movement is desirable: filter opening while VCA closes, pitch rising while resonance falls, one oscillator's FM increasing while another's decreases.

The LED monitoring workflow is a specific and practical benefit that the description identifies explicitly: the LEDs are buffered separately so they can be read without affecting the circuit. In practice this means checking the YYS is a visual step that happens before patching the output to a destination, not after. Seeing the polarity and approximate level of each source at the input allows attenuverter positions to be set with some foreknowledge of the result rather than purely by ear.

## Patch 1: Two-LFO Cancellation at Bus A

An introduction to attenuverting mixing and the cancellation relationship. Two LFOs at different rates are mixed into bus A with opposing polarities, producing a composite modulation that is more complex than either source.

**Setup:**
- LFO 1: medium rate, triangle wave (or any waveshape)
- LFO 2: slightly different rate from LFO 1, triangle wave
- All attenuverters: center (zero) at start

**Patch:**
```
LFO 1 out  [C] → YYS input 1
LFO 2 out  [C] → YYS input 2
YYS A out  [C] → Filter cutoff CV in
```

**Procedure:**
1. Turn input 1's A-attenuverter to roughly three-quarters CW. Bus A receives a scaled positive version of LFO 1. Filter cutoff moves with LFO 1's rate.
2. Turn input 2's A-attenuverter to a matching position CCW. Bus A now receives LFO 2 inverted at the same level. The LEDs on inputs 1 and 2 alternate between green and red, out of phase with each other.
3. Listen to the filter. The cutoff no longer moves at a single LFO rate. When the two LFOs are in partial alignment (both positive or both negative at the same moment), their contributions partially cancel at bus A and the filter cutoff settles near center. When they are maximally opposed (one fully positive, one fully negative), their contributions reinforce at bus A (one pushing up, one inverted down) and the filter moves more dramatically.
4. Adjust the relative attenuverter amounts for inputs 1 and 2. Equal amounts produce maximum cancellation at alignment; unequal amounts allow one LFO to partially dominate.

**What to listen for:** The filter cutoff does not move at a regular rate. Its movement is faster and wider when the two LFOs happen to oppose each other, and slower and narrower when they align. The period of this behavior is determined by how close the two LFO rates are: rates that are nearly identical will cycle through alignment and cancellation very slowly; rates that are farther apart will cycle faster.

## Patch 2: Four Sources to Two Independent Targets

Four modulation sources are distributed to bus A and bus B with different attenuverter configurations, creating two distinct modulation characters from the same source pool.

**Setup:**
- Four modulation sources: two LFOs and two envelopes (or any four sources)
- Bus A target: filter cutoff
- Bus B target: VCA level or oscillator FM

**Patch:**
```
LFO 1 out       [C] → YYS input 1
LFO 2 out       [C] → YYS input 2
Envelope 1 out  [C] → YYS input 3
Envelope 2 out  [C] → YYS input 4
YYS A out       [C] → Filter cutoff CV in
YYS B out       [C] → VCA level CV in
```

**Procedure:**
1. Set all A-attenuverters first. Input 1: moderate CW. Input 2: moderate CCW (inverted). Inputs 3 and 4: both CW at lower levels. Bus A receives two LFOs with opposing polarities and two envelopes in the same direction. Filter cutoff has continuous LFO movement with additional envelope transients on top.
2. Set the B-attenuverters differently. Input 1: low CW. Input 2: low CW (not inverted this time). Inputs 3 and 4: input 3 at CW, input 4 at CCW. Bus B receives the two LFOs in the same direction (adding) and the two envelopes opposing each other. VCA level responds to a broad LFO swell with competing envelope activity.
3. Trigger the envelopes. Bus A and bus B now respond to the same trigger event with different shapes: bus A's filter response includes both envelopes pulling in the same direction; bus B's VCA response has the envelopes partially canceling.

**What to listen for:** The filter and VCA both respond to the same sources but with different characters because their buses were configured independently. Changing one attenuverter affects only the bus it is assigned to; the same source can have completely different roles in the A and B mix simultaneously.

## Patch 3: Normal and Inverted Outputs Simultaneously

Bus A's normal and inverted outputs drive two parameters in opposing directions from the same composite signal, creating an automatic mirror relationship with no additional modules.

**Setup:**
- Two or three modulation sources into YYS inputs
- Output A: one modulation target
- Output A-inv: a second modulation target that should move in the opposite direction

**Patch:**
```
LFO 1 out       [C] → YYS input 1
Envelope out    [C] → YYS input 2
YYS A out       [C] → Filter cutoff CV in
YYS A-inv out   [C] → Resonance CV in (or second filter, or oscillator FM)
```

**Procedure:**
1. Set input 1 A-attenuverter CW at a moderate level. Set input 2 A-attenuverter CW at a lower level. Bus A receives continuous LFO motion with envelope transients adding to it on each trigger.
2. Patch A to filter cutoff and A-inv to resonance. When the LFO pushes the filter cutoff upward (opening the filter), A-inv simultaneously pulls resonance downward. When the envelope fires, cutoff gets a positive transient and resonance gets a negative transient at the same moment.
3. Adjust attenuverter amounts to control the depth of this opposing movement. Large amounts create dramatic opposing swings; small amounts create subtle complementary movement.
4. Try replacing the resonance target with a second oscillator's FM input. The first oscillator's FM opens as the LFO rises; the second oscillator's FM drops simultaneously. The two oscillators drift apart in pitch when the bus is at maximum positive and converge when it approaches zero.

**What to listen for:** The opposing movement is exactly mirrored: A and A-inv are always equal in magnitude and opposite in direction. This creates a coupled relationship between the two targets that does not require any additional patching or modules to maintain.

## Patch 4: Stereo Field Distribution

Four sources are distributed to bus A (left) and bus B (right) with different attenuverter configurations, producing a stereo field where each source occupies a different position and polarity relationship between the two channels.

**Note:** This patch requires a stereo-capable effects module or DAW return that accepts separate left and right signals. The YYS outputs audio-rate or CV; confirm your destination accepts the signal type being patched.

**Setup:**
- Four audio sources (or four modulation sources driving a stereo-capable module)
- Output A: left channel
- Output B: right channel
- Output A-inv and B-inv available as additional stereo sends if needed

**Patch:**
```
Source 1  [A] → YYS input 1
Source 2  [A] → YYS input 2
Source 3  [A] → YYS input 3
Source 4  [A] → YYS input 4
YYS A out [A] → Left channel in
YYS B out [A] → Right channel in
```

**Procedure:**
1. Set input 1: A-attenuverter fully CW, B-attenuverter at center. Source 1 appears only in the left channel. This is a hard-left pan.
2. Set input 2: A-attenuverter at center, B-attenuverter fully CW. Source 2 appears only in the right channel. Hard right.
3. Set input 3: A-attenuverter at moderate CW, B-attenuverter at moderate CW. Source 3 appears in both channels equally. Center pan.
4. Set input 4: A-attenuverter at moderate CW, B-attenuverter at moderate CCW. Source 4 appears in the left channel positive and in the right channel inverted. This produces a phase-split stereo image: the signal is wide because the two channels are phase-opposed, not simply panned.
5. Compare the stereo image of input 4 with input 3. Input 3 is a mono source placed in the center. Input 4 is a wide source where the left and right channels are in opposition. Listen to how the stereo width differs.

**What to listen for:** The phase-split configuration of input 4 creates stereo width through polarity inversion rather than level difference. This is a different effect from standard panning and is particularly useful for creating a wide image from a mono source without the comb filtering artifacts of some other widening techniques. For CV-only patches, this four-output distribution approach applies equally: A goes to one destination, B to another, A-inv to a third, B-inv to a fourth, all from the same four sources configured once.

## Common Mistakes

**Center position, expecting signal.** The attenuverter knobs are bipolar, with zero output at center. If a source is present at an input (the LED is lighting) but nothing is appearing at output A or B, all relevant attenuverter knobs are at or near center. Rotate any attenuverter knob in either direction from center to bring that channel's contribution into the bus.

**Treating A-inv as an independent bus.** Output A-inv is the mathematical inverse of output A; it is not a separate routing destination. The signal at A-inv is always exactly the inverse of whatever is at A. Routing a source's A-attenuverter CCW (inverted) does not change what A-inv outputs; it changes what A outputs, which then changes A-inv as a result. A and A-inv are always mirror images. The same relationship applies to B and B-inv.

**Using it for V/Oct pitch signals.** Attenuverter circuits have finite precision: the tracking between a knob position and the exact output gain is not as accurate as a dedicated precision adder. For transposing or offsetting V/Oct pitch signals, use a dedicated precision CV utility such as the Frap Tools 333. The YYS is suited for modulation CVs, audio signals, and non-pitch control voltages where small gain variations are not musically significant.

**Treating A and B as linked buses.** Unlike a pan pot, where increasing the signal in bus A automatically decreases it in bus B, the YYS A-attenuverter and B-attenuverter for each channel are completely independent. Turning input 1's A-attenuverter up has no effect on bus B unless the B-attenuverter for input 1 is also adjusted. There is no law of conservation between the two buses.

**Ignoring the LED monitoring.** The bipolar LEDs are buffered to avoid affecting the signal path, which means they can be read at any time without cost. Checking the LED before setting attenuverter positions confirms polarity and presence. A source that is positive (LED green) will move bus A upward when the A-attenuverter is turned CW; a source that is currently negative (LED red) will move bus A downward under the same condition. Reading the LED before committing an attenuverter setting makes the result more predictable.

## Advanced Learning Path

1. **Understand the attenuverter range by feel.** Patch a single constant voltage (a sustained gate, a fixed CV from an offset module, or the output of a tuned oscillator held at a steady pitch) into input 1. Turn the A-attenuverter slowly from full CCW through center to full CW while monitoring output A. Center is silence. Both extremes produce output; one is positive, one is negative. The amplitude grows as the knob moves away from center in either direction. This is the full attenuverter range.

2. **Produce cancellation deliberately.** Patch the same signal into inputs 1 and 2 (use a passive mult or stackcable). Set input 1's A-attenuverter to a position CW from center. Set input 2's A-attenuverter to the same distance CCW from center. Output A should be at or near zero: the positive contribution from input 1 cancels the negative (inverted) contribution from input 2. Small adjustments to either knob will break the cancellation in one direction or the other.

3. **Explore the A and A-inv relationship directly.** Patch a single LFO to input 1, A-attenuverter CW. Patch output A to one destination and output A-inv to a second destination. Monitor both destinations simultaneously (use a scope, two LEDs, or listen to their effect on a patch). Confirm that the two outputs are always opposite: when A is at its peak, A-inv is at its trough, and vice versa. Adjust the A-attenuverter amount; both A and A-inv change in proportion.

4. **Build a four-source mix and adjust one attenuverter at a time.** Patch four different sources into all four inputs with all A-attenuverters at moderate CW. Listen to output A. Then slowly turn input 3's A-attenuverter from CW through center to CCW while listening. The bus output changes as input 3 goes from contributing positively to contributing negatively. This exercise makes the summing behavior of the bus concrete: each attenuverter change adds or subtracts from the total.

5. **Use A and B simultaneously for different modulation contexts.** Patch four sources into all four inputs. Set A-attenuverters for a modulation character that suits one patch target. Set B-attenuverters for a different character aimed at a second target. This is the module's primary advantage: one set of source relationships, two different bus configurations, two different destinations, without additional modules.

6. **Explore audio-rate signals through the attenuverters.** Patch an audio oscillator into one input and set the A-attenuverter to a moderate level. Patch output A to an audio destination. Then slowly turn the A-attenuverter through center: at center the signal disappears completely, and crossing center inverts the waveform phase. At audio rate, inversion is a polarity flip: the waveform shape does not change, but its phase relationship to other signals in the mix does. This is useful for creating or canceling comb filtering effects when mixing two signals at audio rate.

7. **Combine audio and CV in the same bus.** Patch an LFO into input 1 and an audio oscillator into input 2. Send both to bus A with attenuverters set. The bus output carries both signals simultaneously. This works because the module is DC-coupled and does not distinguish between audio and CV signals. The result is an audio signal with a slow DC offset riding on it (from the LFO), which can function as amplitude modulation or simply as a mixed signal depending on the destination.

## Pairs Well With

**Tesseract Modular Selam.** The Selam's six slope generator outputs and two mix bus outputs provide a rich set of bipolar CV signals. Routing different Selam channels into YYS inputs allows the two modules to compose CV together: Selam generates complex slopes, YYS distributes and inverts them toward two targets simultaneously. The Selam's ±4.8V bipolar range is well-matched to the YYS's bipolar attenuverter range.

**Patching Panda Etna.** The Etna's three filter channels each accept independent frequency CV. Routing the YYS's A and A-inv outputs to two of the Etna's filters creates an automatic opposing relationship between two filter cutoffs: as bus A opens one filter, A-inv closes another. A and B buses can address different filter pairs independently.

**After Later Audio Mingles.** Mingles' stereo panning and level CVs accept YYS bus outputs for automated stereo positioning. Using A for left pan CV and B-inv for right pan CV (or any combination) creates stereo movement patterns that are directly configured from the YYS attenuverter settings.

**Altered States Machines Eris.** The Eris's 4x4 matrix routing and the YYS's A/B bus distribution address different aspects of signal routing. Combining them in a patch allows the Eris to handle independent channel routing while the YYS handles the mixing of modulation sources toward two control buses.

**Frap Tools 333.** The 333 handles buffered mult and summing duties for signals that need precise voltage relationships. YYS handles attenuverting mixing where signal scaling, inversion, and distribution are the goals. Using both in the same patch covers both precision signal distribution (333) and expressive CV composition (YYS) without overlap.

## What's Next

The YYS covers the attenuverting matrix mixer concept. The natural next step is the Altered States Machines Eris, which extends matrix mixing to a 4x4 architecture where each input can route independently to any of four outputs at variable gain, rather than distributing to two summing buses. Reading the Eris guide alongside this one makes the difference between two-bus distribution (YYS) and true matrix routing (Eris) concrete.

For the broader context of how CV signals travel through a patch and how mixing and distribution utilities fit into signal flow, the signal chain basics document (`basics/06_signal_chain.md`) covers signal types, CV path logic, and how modulation sources connect to modulation destinations.
