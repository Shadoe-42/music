---
title: Intellijel MixUp
manufacturer: Intellijel
primary_role: AMPLIFIER
secondary_roles: [ROUTER]
form_factor: eurorack
functions: [mixer]
behavior_tags: [clean, stable, linear]
use_cases: [audio mixing and routing, signal summing, stereo bus mixing]
hp: 6
historical_context: false
---

# Intellijel MixUp

**Four-Channel Stereo Mixer with Chained Expansion**

![Intellijel MixUp](https://github.com/Shadoe-42/music/raw/main/modular/images/intellijel/mixup/front_panel.jpg)  
*6HP stereo mixer: three controlled channels plus one unity-gain stereo input, chainable via back-panel headers*

---

## Quick Start

**What is MixUp?** A four-channel stereo mixer in 6HP. Channels 1 and 2 accept mono signals with independent level knobs and mute switches. Channel 3 accepts a stereo pair with a shared level knob and mute switch. Channel 4 accepts a stereo pair at fixed unity gain with no panel controls. All four channels sum to the stereo MIX L and MIX R outputs at the bottom of the panel. Multiple MixUp units can be linked via back-panel headers to expand the input count without taking additional front-panel connections.

### First Mix

1. Connect a voice to CH1 IN and bring CH1 LEVEL to about noon
2. Connect a second voice to CH2 IN and bring CH2 LEVEL to about noon
3. Connect stereo outputs from a reverb or effects module to CH3 IN L and CH3 IN R
4. Take MIX L and MIX R to your audio interface or output module
5. Use the three mute switches to bring voices in and out while the patch runs

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 6HP |
| Depth | 29mm |
| Power | 15mA +12V, 16mA -12V, 0mA 5V |
| Channel 1 | Mono input, attenuator, mute switch |
| Channel 2 | Mono input, attenuator, mute switch |
| Channel 3 | Stereo input, shared attenuator, shared mute switch |
| Channel 4 | Stereo input, fixed unity gain, no panel controls |
| Outputs | MIX L and MIX R (red jacks, stereo sum of all channels) |
| Expansion | Back-panel chain headers for linking multiple MixUp units |
| Clip indicator | LED monitors mix bus overload |

---

## Essential Parameters

**Channels 1 and 2** each accept a mono signal. The LEVEL knob controls the amount of that channel contributed to both MIX L and MIX R simultaneously, panning the mono source to center in the stereo field. The MUTE switch removes the channel from the mix entirely when engaged. The mute circuit is AC-coupled to minimize pops when toggling during a live patch.

**Channel 3** accepts a stereo pair via two jacks (IN 3L and IN 3R). A single shared LEVEL knob controls both the left and right signals together; raising or lowering the knob affects both sides equally. A single shared MUTE switch silences both sides together. If only IN 3L is connected, the signal appears on both MIX L and MIX R outputs. Channel 3 is the intended destination for stereo effects returns, stereo oscillators, and any source where maintaining a left/right relationship matters.

**Channel 4** accepts a stereo pair at fixed unity gain. There are no knobs or switches for Channel 4 on the front panel; whatever is patched in passes directly to the mix at full level. This makes Channel 4 appropriate for signals that are already at the correct level and do not need manual adjustment, such as a submix from another module or a reference signal. Because there is no attenuation, CH4 contributes fully to the mix bus from the moment a cable is inserted.

**The CLIP LED** monitors the mix bus and lights when the combined output of all channels exceeds the clean output range. It responds to all channels simultaneously, including any signal arriving from a chained unit. When it lights, the sum of active inputs is too hot; the correct response is to reduce one or more LEVEL knobs rather than to reduce the level downstream of MixUp.

**Back-panel chain headers** allow two or more MixUp units to be linked so that the output of one feeds directly into the input of the next without using front-panel jacks. The first unit in the chain contributes its mix internally to the second unit's bus. The final unit in the chain provides the combined output at its MIX L and MIX R jacks. This architecture allows a six- or nine-channel mixing system to be built from multiple 6HP units while each unit retains full individual level and mute control over its own channels.

---

## Why This Excels

MixUp addresses the mixing problem that appears in every Eurorack system once the voice count exceeds two or three: multiple sources need to reach a single stereo output, and the options for doing so with adequate individual level control at low HP cost are limited. A dedicated stereo mixer at 6HP with four channels and per-channel mute switches is genuinely compact. The alternatives either sacrifice individual control (passive mixers, simple summers) or consume significantly more rack space.

The four-channel layout covers the most common mixing scenario in a single module: two mono voices, one stereo effects return, and one overflow input for a submix or a utility signal. That structure matches the actual signal flow of most patches closely enough that MixUp fits without compromise in arrangements where a dedicated mixer has a clear role.

The chain architecture is the feature that extends MixUp's value beyond its panel. Because chained units sum internally through back-panel connectors, expanding from four to eight channels adds only 6HP and does not require any front-panel routing changes. Each unit in a chain retains complete individual control over its own channels. In a system where rack space is a constraint and mixing needs grow with the system, the ability to add one more 6HP unit and immediately have four more controlled inputs is meaningfully different from buying a new, larger mixer every time the channel count grows.

---

## Patches

### Patch 1: Three-Voice Stereo Mix

This patch establishes the basic MixUp workflow: two mono voices and one stereo effects return combined into a single stereo output for monitoring or recording.

```
[Oscillator + Filter] ──▶ CH1 IN
[Second Voice] ────────▶ CH2 IN
[Reverb L] ────────────▶ CH3 IN L
[Reverb R] ────────────▶ CH3 IN R
                          MIX L ──▶ [Listen IO or Output]
                          MIX R ──▶ [Listen IO or Output]
```

**Setup:** Connect a complete synthesizer voice (oscillator through filter and VCA) to CH1 IN. Connect a second independent voice to CH2 IN. Route the left and right outputs of a reverb module to CH3 IN L and CH3 IN R. Connect MIX L and MIX R to a monitoring or recording destination.

**Controls:** Set CH1 LEVEL and CH2 LEVEL to around noon. Set CH3 LEVEL lower, around 9 o'clock, so the reverb return supports rather than dominates the mix. Watch the CLIP LED; if it illuminates consistently, reduce one or more levels before the transients are clipping. Use the three mute switches to toggle voices in and out while the patch runs. The mute switches are the primary performance controls on this module.

**Result:** A clean stereo mix of two melodic voices with a shared reverb space. The stereo reverb return on CH3 maintains left/right imaging; the two mono voices sit in the center of the field. This is the foundational configuration for any patch that needs to reach an audio interface or speaker system.

---

### Patch 2: Mute-Switch Performance Control

This patch uses the three mute switches as rhythmic performance controls, building and stripping a drum-and-bass arrangement in real time.

```
[Kick/Bass Drum] ──▶ CH1 IN       [CH1 MUTE switch = performance control]
[Melodic Voice] ───▶ CH2 IN       [CH2 MUTE switch = performance control]
[Drum Submix L] ───▶ CH3 IN L     [CH3 MUTE switch = performance control]
[Drum Submix R] ───▶ CH3 IN R
                     MIX L/R ──▶ [Output]
```

**Setup:** Assign the kick or bass to CH1, a melodic lead to CH2, and a stereo drum submix to CH3. Set levels so each channel sounds balanced when all are unmuted. The CLIP LED should be off or only occasionally lighting with all three channels active.

**Controls:** Practice switching channels in and out as performance gestures. Muting CH3 removes the drum bed and leaves only the kick and melody, an immediate density reduction. Muting CH1 and CH3 together isolates the lead voice for a breakdown. Reintroducing channels by flipping mutes back up is as rhythmically significant as any sequenced event. The AC-coupled mute design keeps transitions click-free, so mute events can happen on any beat subdivision without introducing noise.

**Result:** A live performance technique built entirely around the hardware switching on the module. The three independent mutes give six binary combinations of active voices, which is enough structure to build a full arrangement from intro through verse through breakdown and back without touching any other module.

---

### Patch 3: Chained Six-Channel Mix

This patch links two MixUp units via back-panel headers to combine six channels into a single stereo output, with each unit retaining independent control over its own channels.

```
MixUp A:                          MixUp B:
[Voice 1] ──▶ CH1 IN              [Voice 4] ──▶ CH1 IN
[Voice 2] ──▶ CH2 IN              [Voice 5] ──▶ CH2 IN
[Stereo FX] ─▶ CH3 IN L/R         [Drums L/R] ─▶ CH3 IN L/R
[CHAIN-OUT] ──────────────────────▶ [CHAIN-IN]
                                   MIX L ──▶ [Output]
                                   MIX R ──▶ [Output]
```

**Setup:** Connect the two MixUp units with a link cable between the back-panel CHAIN-OUT header on MixUp A and the CHAIN-IN header on MixUp B. MixUp A's front-panel MIX outputs are not used in this configuration; MixUp B's MIX L and MIX R carry the combined output of all six channels.

**Controls:** All six LEVEL knobs and six MUTE switches across both units remain fully functional. Setting levels and muting channels on MixUp A affects only those channels in the combined output; the same is true for MixUp B. The CLIP LED on MixUp B monitors the full six-channel sum. Balance the overall mix by managing levels on both units independently. If the LED is frequently lighting, reduce levels across the board on both units rather than only on the output unit.

**Result:** A six-channel stereo mix in 12HP with complete individual control over each channel. The chain architecture produces a transparent signal path with no degradation from the additional unit. This configuration is the most common reason to own two MixUp modules.

---

### Patch 4: Drum Submix into a Larger Mix

This patch uses CH4's unity-gain input to receive a pre-leveled drum submix from a second mixer, keeping the drum mix balanced internally while treating the whole drum section as a single input to MixUp.

```
[Kick] ──▶ [Submixer CH1]
[Snare] ─▶ [Submixer CH2]    Submixer MIX L ──▶ MixUp CH4 IN L
[Hat] ───▶ [Submixer CH3]    Submixer MIX R ──▶ MixUp CH4 IN R
[Perc] ──▶ [Submixer CH4]

[Voice 1] ──────────────────▶ MixUp CH1 IN
[Voice 2] ──────────────────▶ MixUp CH2 IN
[Stereo Reverb] ────────────▶ MixUp CH3 IN L/R
                               MixUp MIX L/R ──▶ [Output]
```

**Setup:** Balance the drum mix on the submixer so the kick, snare, hat, and percussion are well-proportioned relative to each other. Route that balanced stereo output to MixUp CH4 IN L and CH4 IN R. Use CH1 and CH2 for melodic voices and CH3 for reverb.

**Controls:** The drum level within the drum mix is set at the submixer and does not change when you adjust MixUp. Because CH4 has no level control on MixUp, the only way to change how loud the drums are in the final mix is to return to the submixer. This is intentional: it enforces a discipline where the internal drum balance is set and locked at the submixer, and the final output mix adjusts the other three channels relative to a fixed drum level. Use CH1, CH2, and CH3 levels to balance the melodic material against the drums.

**Result:** A clean four-group mix (two mono voices, one stereo reverb, one full drum section) where the drum balance is fixed and the remaining elements are adjusted around it. The CH4 unity-gain design makes this workflow natural: patch the drums in at the correct level once, then work on everything else.

---

## Common Mistakes

### "My mix is clipping even though each voice sounds fine individually"

Clipping on a summing bus is caused by addition, not by any single input being too loud. Four channels each contributing a moderate signal can sum to a total that exceeds the clean output range, even if no individual channel would clip alone. The CLIP LED monitors the bus total. The fix is to reduce LEVEL knobs across multiple channels rather than searching for one culprit; in a four-channel mix, bringing all four levels down by the same small amount is usually the fastest path to a clean output.

**Fix:** Reduce LEVEL knobs proportionally across all active channels until the CLIP LED stops lighting consistently.

---

### "Channel 4 is too loud and I cannot turn it down"

Channel 4 has no level knob or mute switch. It passes whatever is patched into it at unity gain directly to the mix bus. If the signal going into CH4 is too hot relative to the other channels, the level adjustment must happen upstream before MixUp. Use a VCA, an attenuator, or the output level control on the source module to set CH4's contribution before patching it in. There is no panel control on MixUp that addresses CH4 gain.

**Fix:** Attenuate the signal before it reaches CH4 IN, either at the source module or with an inline attenuator.

---

### "I cannot mute my Channel 4 source for a breakdown"

Because CH4 has no mute switch, the only way to silence it during a performance is to physically remove the patch cable. Planning performance breaks requires either keeping CH4 for sources that stay present throughout the piece, or routing that source to CH1, CH2, or CH3 instead so a mute switch is available. CH4 is best used for signals you want consistently present at a fixed level (a continuous drone, a locked drum submix, a persistent pad) rather than for voices you intend to bring in and out.

**Fix:** Use CH1, CH2, or CH3 for any source you need to mute during performance; reserve CH4 for always-on elements.

---

### "Chaining two MixUps but only getting audio from one of them"

The chain connection requires a specific cable between the back-panel CHAIN-OUT header on the upstream unit and the CHAIN-IN header on the downstream unit. The front-panel MIX outputs on the upstream unit do not feed the downstream unit; the chain runs through the back panel only. If the cable is not seated correctly on both headers, or if the headers are connected in the wrong direction, the upstream unit's audio does not reach the downstream unit's output. The downstream unit's MIX L and MIX R jacks carry the combined output.

**Fix:** Confirm the chain cable is connecting CHAIN-OUT on unit A to CHAIN-IN on unit B, and take the final output from unit B's MIX L and MIX R jacks.

---

## Advanced Learning Path

1. Work through the four LEVEL knob positions systematically on a single-voice patch before mixing multiple sources. Connect one oscillator to CH1 and sweep LEVEL 1 from fully counterclockwise to fully clockwise while listening. Notice that the knob taper is logarithmic: the first half of the rotation covers most of the usable gain range, and the upper half adds relatively little additional volume. This is intentional audio taper behavior designed to match how humans perceive loudness. Understanding the taper prevents setting all levels near maximum and then running out of headroom when more voices are added.

2. Practice mute switch timing as a musical skill. Set up a three-voice patch with a repeating sequence and practice toggling the three mute switches in time with the sequence. Try muting on beat 1, on the off-beat, across bar lines, and in combinations. The switches have tactile feedback; with practice, simultaneous two-switch mutes become reliable. Mute switch precision is a learnable technique that has direct application in live performance, and MixUp is a good module to develop it on because the three switches are physically close together.

3. Investigate gain staging discipline across a full signal chain. Patch an oscillator through a VCA and into CH1, and set the VCA to approximately unity gain. Set CH1 LEVEL at noon. Monitor the output at MIX L. Now reduce the VCA level to minimum and watch the signal disappear upstream. Now raise CH1 LEVEL to maximum. Note that the signal does not reappear; maximum LEVEL on MixUp cannot recover a signal that has been attenuated before the input. This demonstrates that MixUp is a mixing stage, not a gain recovery stage; correct levels must arrive at the inputs.

4. Build a patch that uses CH4 deliberately. Route a drone oscillator or a pad module to CH4 IN L and CH4 IN R. Set the output level of that source module so the drone sits at a useful level in the mix. Now patch melodic material into CH1 and CH2 and set levels relative to the drone. Observe that the drone does not change level regardless of what you do to CH1 and CH2; it is an anchor. Build a complete patch around a fixed-level foundation and notice how having one immovable reference point changes how you set the other channels.

5. Use the CLIP LED as a real-time gain staging diagnostic rather than a warning to ignore. In a mixing session, deliberately drive all four channels hot enough to light the LED consistently. Listen to what clipping sounds like on the mix bus: it is a specific kind of harmonic distortion, not silence. Then reduce levels until the LED only flashes occasionally on transient peaks. Learn the sonic difference between occasional transient clipping (often acceptable) and consistent clipping (audible distortion). The LED communicates the mix bus state in real time; treating it as a diagnostic rather than an alarm produces better results.

---

## Pairs Well With

**4ms Company Listen IO** is the most direct downstream partner for MixUp. MixUp sums multiple modular voices to stereo; Listen IO converts that stereo modular signal to headphone and line levels for monitoring and recording. The two modules together cover the full path from multiple voice sources to a recording interface or studio monitors. MIX L and MIX R from MixUp patch directly to the two Listen IO Mod In jacks, and the Listen IO Level knob controls the final output volume without touching any MixUp settings.

**Endorphin.es Ghost** and similar stereo reverb/delay modules make natural Channel 3 sources. Ghost produces a stereo wet signal; CH3's stereo input with shared level control is exactly the right destination for an effects return. Setting CH3 LEVEL lower than CH1 and CH2 keeps the reverb in support rather than dominance, and the CH3 MUTE switch allows the reverb return to be cut during dry sections. Any stereo effect module (reverb, delay, chorus, shimmer) fits this workflow.

**Erica Synths Black Quad VCA2** upstream of MixUp handles per-voice amplitude shaping before signals reach the mixer. MixUp's LEVEL knobs set the static balance between voices; the Quad VCA2 handles dynamic amplitude control from envelopes and LFOs per voice. Using a VCA before the mixer rather than relying on the mixer's level knob for dynamic control is correct gain staging: VCAs shape the voice, mixers combine voices. The two modules together cover both functions cleanly.

**A second MixUp** via back-panel chain is the intended expansion path. Two units in a chain give six independently controlled channels in 12HP. The chain connection is transparent and does not degrade signal quality. For a system with five or six voices, two MixUps is often the most HP-efficient mixing solution available, and the chain architecture means both units remain fully functional with independent level and mute control over all channels.

---

*Intellijel MixUp documentation: [Intellijel](https://intellijel.com)*
