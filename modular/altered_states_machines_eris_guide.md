---
title: "Altered States Machines Eris"
manufacturer: "Altered States Machines"
primary_role: UTILITY
secondary_roles: []
historical_context: true
form_factor: eurorack
functions: [mixer, cv-processor, switch-router]
behavior_tags: [generative, self-modulating, performance-oriented]
use_cases: [audio and CV matrix routing, submixing multiple sources to one output, feedback loop signal path, effects send and return integration]
hp: 12
depth: 26mm
memory: none
transport: none
screen: false
hybrid: false
cv: none
---

![Altered States Machines Eris front panel](https://github.com/Shadoe-42/music/raw/main/modular/images/altered_states_machines/eris/front_panel.jpg)

## Historical Context

The mixing console has a fixed topology: a predetermined set of sources feed a predetermined set of destinations through a routing architecture that the console designer chose in advance. A studio console from the 1960s routes each input channel to a small number of bus outputs: stereo left and right, a few group buses, the monitor mix. The number of destinations is fixed. The relationship between sources and destinations is fixed. The operator has control only over the level and treatment of the signal along that predetermined path.

A matrix mixer removes that fixedness. Every input can reach every output, at any level the operator sets. There are no predetermined routing decisions embedded in the hardware; the topology of the patch is determined entirely by the sixteen gain settings across four inputs and four outputs. This is a fundamentally different instrument from a console, even though both involve mixing.

The implications for feedback composition are significant. In a fixed-topology mixer, routing an output back to an input requires external patching around the console's intended architecture. In a matrix mixer, feedback routing is as natural as any other routing: set the gain from an output back to an input, and the system begins to loop. The level of that feedback determines whether the loop is stable, gradually building, or runaway. Electronic music composers recognized this possibility early.

Gordon Mumma's cybersonic work in the 1960s used analog circuits with feedback as generative composition systems. Alvin Lucier's "I Am Sitting in a Room" (1969) is the most famous example of acoustic feedback as a compositional mechanism: a recording is played back into the space it was recorded in, re-recorded, and played back again repeatedly. The room's resonant frequencies accumulate with each cycle until the original speech is entirely replaced by the room's acoustic signature. David Tudor's "Rainforest" series (1968 onward) used feedback networks as instruments in themselves: circuits whose outputs fed their own inputs through deliberately unpredictable paths. In all of these works, the feedback matrix is not a mistake to be corrected but the compositional mechanism itself.

In modular synthesis, feedback matrices appear in several forms. The Buchla 200 series included matrix mixer modules specifically for feedback routing. Self-patching within a single module or across multiple modules to create feedback loops is a standard compositional technique. The key parameter in all feedback contexts is the same: how much of the output is returned to the input, and what happens to the signal on each cycle through the loop.

The Eris by Altered States Machines brings this architecture into 12HP with a practical addition: an auxiliary channel with a Vactrol-based soft mute designed for performance use. The Vactrol (a photoresistor coupled to an LED inside an opaque package, used as a voltage-controlled resistor) produces a gentle, click-free transition when the auxiliary channel is gated, which is the behavior needed when bringing an effects return in and out of a live mix. This is console engineering and experimental feedback patching in the same module.

## Quick Start

1. Patch four audio or CV sources into inputs 1 through 4.
2. Each input has four potentiometers, one for each output (outputs 1, 2, 3, and 4). Turn input 1's output-1 pot clockwise. Input 1 now contributes to output 1 at that gain level.
3. Patch output 1 to any audio destination. Adjust the level of input 1's output-1 pot to set the contribution. This is the simplest configuration: one input, one output, one pot.
4. Turn input 2's output-1 pot clockwise as well. Output 1 now carries a mix of inputs 1 and 2. Adjust both pots independently to set the relative levels.
5. Turn input 1's output-2 pot clockwise. Output 2 now carries input 1 at an independently set level, simultaneously with output 1. The same source contributes to two different outputs at two different levels without any additional modules.

## Key Specifications

| Specification | Value |
|---|---|
| Width | 12 HP |
| Depth | 26 mm |
| +12V Current | 17 mA |
| -12V Current | 3 mA |
| +5V Current | 0 mA |
| Matrix | 4 inputs × 4 outputs (16 gain pots) |
| Gain range | Up to 4× per path |
| Aux input | Vactrol soft mute; unity or ×2 gain (back-panel toggle) |

**Power note:** The asymmetric current draw (17 mA on +12V, only 3 mA on -12V) reflects the module's predominantly positive-rail analog design. The Vactrol circuit and op-amp configuration draw primarily from +12V.

## Essential Parameters

**Inputs 1 through 4 (four jacks).** The four input jacks accept any signal type: audio, CV, gate, or clock. The module is DC-coupled, so static voltages and slowly moving CVs pass through without filtering. Each input feeds four potentiometers, one for each output. Patching a source into an input makes it available to all four outputs simultaneously; which outputs it actually reaches depends on how the relevant pots are set.

**Matrix pots (16 total, four per input).** Each input has four pots: one controlling its contribution to output 1, one for output 2, one for output 3, and one for output 4. Center position is minimum gain (zero or near-zero contribution to that output). Clockwise rotation increases gain, up to a maximum of four times the input signal amplitude. All sixteen pots are independent; changing one does not affect any other. The full 4×4 routing matrix means: input 1 can send to all four outputs simultaneously at different levels; output 1 can receive from all four inputs simultaneously at different levels; or any combination of partial routing in between.

**Gain above unity (up to 4×).** Unlike a standard mixer where maximum gain is unity (1×), the Eris allows each routing path to amplify the source up to four times its input amplitude. This serves two purposes. For weak signals, it provides make-up gain without requiring a separate amplifier. For strong signals or deliberate overdriving, increasing gain beyond unity adds saturation character to the output. The 4× maximum also makes small CV signals more useful: a modulation source at one volt can be amplified to four volts at the output pot alone.

**Outputs 1 through 4 (four jacks).** Each output carries the sum of whatever contributions the four inputs are making to that output through their respective pots. With all sixteen pots at minimum, all four outputs are silent regardless of what is at the inputs. With multiple inputs contributing to the same output, that output's level reflects the sum of all contributing inputs scaled by their respective pot settings. It is possible to saturate an output by routing multiple high-level inputs to it at high gain settings.

**Auxiliary input.** The auxiliary input is a fifth signal path that bypasses the 4×4 matrix and sums directly with output 1's signal before reaching the output 1 jack. Its level is controlled by a Vactrol-based circuit rather than a standard pot: the Vactrol provides a soft, click-free mute when the auxiliary channel is switched off. A back-panel toggle sets the auxiliary input gain to either unity (1×) or double (2×). The auxiliary channel is designed for effects returns: send output 1 (or any source) to an external effect, return the processed signal through the auxiliary input, and the dry and wet signals are summed at output 1 before leaving the module. The soft mute allows the auxiliary return to be brought in and out of the mix during performance without audible clicks or pops.

## Why the Eris Excels

A matrix mixer's value is in making routing decisions audible rather than structural. In a conventional patch, the question "what connects to what" is answered when you insert a cable; changing that answer requires replugging. With the Eris, the question "what contributes to which output, and at what level" is answered by sixteen pot positions that can be adjusted continuously during a performance. Every routing relationship is a continuous variable rather than a binary connection.

The 4x gain maximum changes what a matrix mixer can do with weak signals. A quiet oscillator, a low-level contact microphone output, or a modulation source that produces only a fraction of a volt can be amplified to useful levels within the Eris without an external amplifier. Combined with the matrix routing, this means that even small signals become manageable within the patch without additional utility modules.

The cybernetic feedback use case is the Eris's most experimental and most open-ended application. Routing output 2 back to input 3 (for example) at a controlled gain level creates a loop that feeds on itself at a rate determined by the pot setting and the round-trip time through the signal chain. At low gain, the feedback adds sustain or reverb-like accumulation. At higher gain, the loop builds until the output saturates or reaches a stable resonant state. The four-output architecture means multiple feedback loops can coexist simultaneously; output 2 back to input 3 and output 4 back to input 1 are independent loops that interact only through whatever other routing connects them.

The auxiliary channel with Vactrol mute completes the module as a performance mixer. Effects processing typically requires send and return paths that can be controlled in real time. The auxiliary input's click-free mute handles the return side: bring an external reverb, delay, or other effect into the mix and remove it without introducing audible transients. The back-panel gain toggle accounts for the level difference between modular-level signals and line-level effects: unity gain for modular effects, double gain for line-level returns.

## Patch 1: Four-Input Submixer to Single Output

The simplest configuration: four sources routed to output 1 with independent level control per source. Introduction to the 4×4 matrix and per-input level setting.

**Setup:**
- Four audio or CV sources (oscillators, drum voices, envelope generators, or any combination)
- All matrix pots at minimum at start

**Patch:**
```
Source 1  [A] → Eris input 1
Source 2  [A] → Eris input 2
Source 3  [A] → Eris input 3
Source 4  [A] → Eris input 4
Eris output 1  [A] → Mixer or audio destination
```

**Procedure:**
1. Turn input 1's output-1 pot clockwise to a moderate position. Source 1 appears at output 1.
2. Turn input 2's output-1 pot clockwise to a different position. Output 1 now carries a mix of sources 1 and 2 at their respective levels.
3. Bring in inputs 3 and 4 at different output-1 pot positions. Output 1 is now a four-source mix with individually set levels.
4. Adjust any pot while listening to output 1. That source's contribution to the mix changes in real time. No other routing is affected.
5. Try pushing one input's output-1 pot to its maximum (4× gain). If the source is a quiet signal, this makes it present in the mix at a useful level. If the source is already at normal modular level, the output begins to saturate: the mix becomes louder and slightly distorted as the output clips.

**What to listen for:** Output 1 responds only to the pots assigned to output 1. The other output jacks are silent (all pots at minimum). The level of each source in the mix is directly controlled by its output-1 pot, independent of all other sources. This is the basic 4-to-1 submixer configuration.

## Patch 2: Parallel Routing with Auxiliary Effects Return

Sources are distributed to multiple outputs for parallel processing. An external effect processes output 1, and the processed signal returns through the auxiliary input, summing with output 1's dry signal.

**Setup:**
- Two or three sources
- External effect unit (reverb, delay, or other processing) with audio input and output
- Aux back-panel toggle: unity for modular-level effects, ×2 for line-level

**Patch:**
```
Source 1  [A] → Eris input 1
Source 2  [A] → Eris input 2
Source 3  [A] → Eris input 3

Eris output 1  [A] → External effect input
External effect output  [A] → Eris aux input

Eris output 1  [A] → (also to) Main audio destination (dry + wet sum)
Eris output 2  [A] → Secondary destination (dry only)
```

**Procedure:**
1. Set input 1's output-1 and output-2 pots to moderate levels. Source 1 appears at both outputs.
2. Set input 2's output-1 pot only. Source 2 goes to output 1 (and therefore to the external effect) but not to output 2.
3. Set input 3's output-2 pot only. Source 3 goes to output 2 but not to the effect send.
4. Bring the external effect return up by turning the aux input active (the Vactrol circuit brings it in smoothly). The processed signal sums with the dry signals at output 1.
5. Adjust the back-panel gain toggle if the effect return is too quiet (line-level effect at unity gain) or too loud (modular-level effect; set to unity).
6. Gate the auxiliary input on and off during performance. The Vactrol circuit mutes and unmutes the return without clicks.

**What to listen for:** Output 1 carries sources 1 and 2 dry, plus the processed return from the external effect. Output 2 carries sources 1 and 3 without any effect processing. The two outputs have different tonal characters because their routing configurations were set independently. Gating the aux return in and out changes the wet/dry balance at output 1 without affecting output 2 at all.

## Patch 3: Feedback Matrix

An output is routed back to an input through the matrix, creating a self-feeding loop. The feedback gain, controlled by the relevant pot, determines whether the loop stabilizes, builds slowly, or accumulates quickly.

**Warning:** Feedback loops can produce loud, sustained output at high gain settings. Monitor output levels and begin with all feedback pots at minimum, increasing slowly.

**Setup:**
- One or two initial sources
- Output 2 will be the feedback return (routed back to input 3)
- Begin with all pots at minimum

**Patch:**
```
Source 1  [A] → Eris input 1
Eris output 2  [A] → Eris input 3 (feedback path)

Eris output 1  [A] → Main audio destination
Eris output 2  [A] → (also routed to input 3 via split; same jack)
```

**Procedure:**
1. Set input 1's output-1 pot to a moderate level. Source 1 appears at output 1. Source 1 does not yet appear at output 2.
2. Set input 1's output-2 pot to a low level. Source 1 now feeds output 2 at a low level.
3. Very slowly turn input 3's output-2 pot clockwise from minimum. Input 3 is receiving the output-2 signal (via the feedback cable). This pot controls how much of output 2's signal is fed back into itself through input 3 and back to output 2. At a very low setting, the feedback adds a slight sustain or ringing quality. Higher settings cause the loop to build.
4. Listen to output 1 and output 2 simultaneously. Output 1 carries the original source plus any spillover from the feedback path (if input 3 also has an output-1 pot contribution). Output 2 is where the feedback loop lives.
5. Adjust input 3's output-2 pot to find the stable feedback level for the current patch: low enough that the loop sustains without building out of control, high enough to be audible.

**What to listen for:** The feedback path adds a tonal character that depends on the frequency content of source 1 and the gain of the feedback loop. At stable gain, the output accumulates a sustained resonant quality. Slowly increasing the feedback pot while listening reveals the transition from stable accumulation to unstable growth. The character of the feedback is different with different source material: a pure sine wave produces a single sustained tone; a complex noise or drum signal accumulates in complex, unpredictable ways.

## Patch 4: Drum Voice Distribution

Four percussive voices from a drum synthesizer or sequencer are distributed across four outputs in different combinations, creating two stereo submixes and two independent spot feeds.

**Context:** This patch reflects the direct use case of combining QD drum voices in the Eris before sending to a mixer. The same approach applies to any four percussive or rhythmic voices.

**Setup:**
- Four drum voice outputs (kick, snare, closed hat, open hat or similar)
- Outputs 1 and 2: stereo submix pair (left and right)
- Output 3: kick spot (isolated, for sidechain or separate processing)
- Output 4: full mix bus (all four voices combined)

**Patch:**
```
Kick out    [A] → Eris input 1
Snare out   [A] → Eris input 2
HH closed   [A] → Eris input 3
HH open     [A] → Eris input 4

Eris output 1  [A] → Left channel / MixUp or Cockpit 2 channel 1
Eris output 2  [A] → Right channel / MixUp or Cockpit 2 channel 2
Eris output 3  [A] → Sidechain input or separate compression channel
Eris output 4  [A] → Full drum bus to main mix
```

**Procedure:**
1. Set the output-4 pots for all four inputs to moderate levels. Output 4 is the full drum bus: all four voices summed.
2. Set the output-3 pot for input 1 (kick) only. Output 3 carries the kick in isolation, suitable for sidechain triggering or separate compression.
3. Set the output-1 and output-2 pots to create a stereo image. For example: kick at moderate level on both output 1 and 2 (center), snare slightly louder on output 1 than output 2 (left of center), closed hat more on output 2 (right of center), open hat at lower level on both (center-ish). Adjust to taste.
4. Adjust relative levels within each output bus independently. The kick level in output 4 (full bus) does not affect the kick level in outputs 1 and 2 (stereo submix), since those are separate pot settings.

**What to listen for:** The four outputs carry the same four source signals in completely different configurations simultaneously. Output 4 is a mono sum. Output 3 is a single voice. Outputs 1 and 2 are a stereo image of all four voices. All of this configuration is set by pot positions alone, without any external routing changes or additional modules.

## Common Mistakes

**Expecting unchanged level at maximum pot.** The Eris's maximum pot position is 4× gain, not unity. A source at normal Eurorack signal level (approximately 5V peak) will clip or saturate the output at or near maximum pot position. Set starting levels at roughly one-quarter to one-third of maximum rotation and increase from there.

**Confusing the auxiliary input with a fifth matrix input.** The auxiliary input does not participate in the 4×4 matrix. It has no routing pots to outputs 2, 3, or 4. It sums directly with output 1 only, always, at the gain level set by the back-panel toggle and controlled by the Vactrol mute. Using the auxiliary input as a fifth independent source for routing to multiple outputs is not possible with the current architecture.

**Feedback loops building unexpectedly.** Any patch that routes an output back to an input through a cable creates a feedback path. If the combined gain around the loop exceeds unity (input gain × output gain × feedback pot level), the loop will build. When building a matrix patch, check for unintended feedback paths: output N feeding input M, where input M has a nonzero contribution to output N. Reduce the relevant pot or remove the feedback cable if the accumulation is undesirable.

**Back-panel gain toggle set for the wrong signal level.** The auxiliary input gain toggle is on the back panel and affects the overall gain of the auxiliary return. At unity (1×), modular-level returns sound correct. At double (2×), modular-level signals are too hot. If the auxiliary return sounds distorted at low pot level, check the back-panel toggle. The toggle is intended for line-level versus modular-level source compensation and should be set at installation rather than changed frequently.

**Setting all sixteen pots to high levels simultaneously.** Output buses that receive high contributions from multiple inputs will saturate. A bus receiving four inputs each at 4× gain is receiving sixteen times the signal level of one input at unity. Start with conservative levels, especially when building complex routing patterns, and increase individual pot levels as needed rather than starting at maximum.

## Advanced Learning Path

1. **Build and understand the basic 4-to-1 submixer.** Set all sixteen pots to minimum. Route four sources to all four inputs. Slowly bring up the output-1 pots for each input one at a time. Listen to how each new source contributes to output 1. This establishes the basic summing behavior before any complex routing.

2. **Explore the gain range deliberately.** Route a single source to input 1. Patch output 1 to a monitoring destination. Turn the output-1 pot from minimum to maximum while listening. Note where the signal becomes audible, where it reaches a comfortable level, and where it begins to saturate. This establishes the practical working range of the pot.

3. **Use a single source at multiple outputs simultaneously.** Route one source to input 1. Set input 1's output-1, output-2, output-3, and output-4 pots to four different levels. Confirm that output 1 through 4 all carry the same source simultaneously at different levels. This demonstrates the fundamental capability of the matrix: one source, four simultaneous destinations, independently set.

4. **Build a controlled feedback loop from scratch.** Start with one source at input 1 going to output 2 at low level. Route output 2 back to input 3 via a cable. Slowly increase input 3's output-2 pot from minimum while listening to output 2. Find the threshold where the feedback loop just sustains without building. This is the practical definition of unity feedback gain for that patch. Increase the pot slightly above this threshold and observe how the loop builds.

5. **Route the same source to both a matrix output and the auxiliary path.** Set input 1 to output 1 at a moderate level. Route output 1 to an external effect and return the effect to the auxiliary input. The result at output 1 is the dry signal plus the processed return. Adjust input 1's output-1 pot to change both the dry send level (to the effect) and the dry contribution to the output simultaneously. This is the trade-off of send-return routing within a single output: dry and send levels are linked by the same pot.

6. **Set a complete routing matrix for a performance context.** Decide in advance what all sixteen pots should be set to for a specific patch configuration. Write down or photograph the settings. Perform with this configuration, then gradually adjust individual pots during performance to modify the routing in real time. This establishes the Eris as a performance instrument rather than a static patch component.

7. **Compare the Eris and YYS in the same patch.** Route modulation sources through the YYS (bipolar mixing to A and B buses) and audio voices through the Eris (four-output matrix distribution). Observe how the two modules handle mixing differently: the YYS operates on the level of adding and subtracting CV; the Eris operates on the level of routing signals to destinations. Together they cover different layers of the signal flow.

## Pairs Well With

**VPME QD Drum Workstation.** The QD's four drum voice outputs map directly to the Eris's four inputs. The matrix routing allows the four voices to be combined and distributed to multiple outputs in any combination: a full mix bus, a stereo submix, individual spot outputs, and a sidechain feed can all be configured simultaneously from the same four sources.

**DSP Coffee YYS.** The YYS handles bipolar CV mixing and modulation distribution; the Eris handles signal routing and gain-above-unity amplification for audio or CV. Using both in the same patch assigns each module to a distinct layer: YYS manages modulation relationships, Eris manages signal routing and level. The two matrix-style modules are complementary rather than redundant.

**Intellijel MixUp / Endorphin.es Cockpit 2.** The Eris's multiple outputs feed naturally into a final performance mixer. Output 1 as a full drum bus, output 2 as a reverb send, outputs 3 and 4 as individual voices can each become separate channels on the MixUp or Cockpit 2 for final level balancing before the studio mixer or recording interface.

**Any external effects unit with audio input and output.** The auxiliary input's Vactrol soft mute is designed specifically for effects return integration. A hardware reverb, delay, chorus, or any other processing unit can be inserted into output 1's signal path: send from output 1 to the effect, return to auxiliary input, and the processed and dry signals sum at output 1. The Vactrol mute allows the return to be brought in and out of performance without audible clicks.

**Patching Panda Etna.** The Etna's three filter channels accept audio from multiple sources. Routing three oscillators or voices through the Eris matrix before the Etna allows the pre-filter mix to be configured and adjusted with individual level control per voice, before the combined signal reaches the filter chain.

## What's Next

The Eris covers matrix routing and effects integration. The natural prior step for understanding why matrix routing matters is the DSP Coffee YYS guide, which covers the bipolar attenuverting approach to mixing: a two-bus matrix where gain can be negative as well as positive.

For the broader context of signal flow and how routing utilities fit into a patch architecture, the signal chain basics document (`basics/06_signal_chain.md`) covers signal types, the difference between audio and CV paths, and how modulation sources and audio signals travel through a patch toward their destinations.
