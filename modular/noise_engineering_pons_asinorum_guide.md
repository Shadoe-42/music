---
title: Pons Asinorum
manufacturer: Noise Engineering
primary_role: MODULATOR
secondary_roles: []
historical_context: true
form_factor: eurorack
functions: [envelope-generator, lfo]
behavior_tags: [linear, stable, gated, free-running, reactive, generative]
use_cases: [envelope shaping, modulation source, self-evolving patch element, stochastic modulation]
hp: 6
memory: none
transport: none
screen: false
hybrid: false
cv: full
---

# Pons Asinorum

**Four-channel linear envelope generator and LFO with voltage-controlled cycle length**

![Noise Engineering Pons Asinorum](https://github.com/Shadoe-42/music/raw/main/modular/images/noise_engineering/pons_asinorum/front_panel.jpg)

## Historical Context

The envelope generator predates the voltage-controlled synthesizer as a concept. When Robert Moog and Herbert Deutsch developed the first Moog transistor ladder synthesizer in 1964, they borrowed the ADSR (attack, decay, sustain, release) shape from the mechanical behavior of Hammond organ key contacts, which produced a characteristic signature as the contact closed, settled, held, and released. Moog's envelope circuits used exponential voltage curves because human perception of loudness and pitch is logarithmic; an exponentially decaying envelope sounds like a smooth natural fade because it matches the ear's own response curve. Don Buchla arrived at a different conclusion around the same period. Working in San Francisco with the Series 100 system beginning around 1963, Buchla designed envelope-like function generators with linear slopes because he was using them primarily as modulation sources rather than amplitude contours. A linear ramp is mathematically simpler, predictably scalable, and produces distinctly different timbral results when applied to pitch or filter frequency rather than amplitude. The choice between exponential and linear envelope shapes became one of the defining sonic differences between the two schools of modular synthesis that Moog and Buchla represented.

The combination of envelope generator and LFO into a single circuit was a natural convergence that several designers pursued independently. Serge Tcherepnin's Serge Modular system, developed at the California Institute of the Arts beginning in 1973, included the Dual Universal Slope Generator: a circuit that could function as an envelope, an LFO, a slew limiter, a comparator, or an oscillator depending on how it was patched and what its cycle time was set to. Tcherepnin's insight was that an envelope and an LFO are the same circuit operating at different time scales and triggering behaviors, and that building one flexible circuit served both functions better than building two dedicated ones. This lineage continued through the Make Noise Maths module designed by Tony Rolando in 2009, which adapted the function generator concept for the eurorack format and became one of the most widely used modules in that system, not because it was the most powerful or specialized but because a circuit that serves as envelope, LFO, slew, and offset simultaneously earns more rack space per function than anything dedicated to a single role.

The practical problem of multi-channel envelope density drove a parallel development thread. A single synthesizer voice needs at minimum one envelope for amplitude and one for filter, and a patch of any complexity quickly demands four or more independent envelope sources operating at different rates for different destinations. The 4ms Pingable Envelope Generator, released in 2010, addressed this by making cycle time directly settable by incoming clock pulses, which synchronized envelope behavior to musical tempo without a separate clock divider. The challenge all multi-channel solutions shared was panel economy: four fully featured ADSR generators with CV inputs and controls for each stage would occupy twenty or more HP, making the format impractical for small systems. The design tradeoff between per-channel flexibility and panel width produced a range of solutions where some parameters were shared across channels and others remained individually addressable.

Noise Engineering's path to the Pons Asinorum was longer than most of their releases. Designer Skyler King (known online as Kittyspit) originally proposed a compact dual decay module, and Noise Engineering worked on that concept for years without finding a version compelling enough to release. The breakthrough came when NE collaborator Dave Driggers mentioned the name of his band: Pons Asinorum, the medieval name for Proposition 5 of Book 1 of Euclid's Elements, the first theorem in the Elements that students historically found difficult enough to stop their progress. Euclid's proposition states that the base angles of an isosceles triangle are equal; it was called the bridge of asses because it was the passage that separated those who could continue in geometric study from those who could not cross it. The name reframed the module's design problem: a modulation generator that appears simple but opens into deep territory when the performer engages it fully. That framing prompted the expansion from decay only to all three shapes, ramp up, up/down, and ramp down, and the addition of attack as a first-class parameter. Markus Cancilla joined Noise Engineering as their first employee while the hardware was nearing completion and contributed substantially to the final design. The module that resulted is named after both the theorem and the band, and like both of its namesakes, rewards patience with the interface.

---

## Quick Start

The Noise Engineering Pons Asinorum is a four-channel linear envelope generator and LFO in 6HP. Each channel independently runs in envelope mode (triggered) or LFO mode (free-running), with three selectable shapes and voltage-controlled cycle length. A single encoder sets the cycle length of whichever channels are currently selected, making it possible to adjust multiple channels simultaneously or independently without separate controls for each.

1. Power up Pons Asinorum. All four channel LEDs will flash briefly on startup.
2. Patch a gate or trigger from Hermod+ into Trigger In 1.
3. Patch Output 1 to a VCA CV input or a filter cutoff CV input.
4. Press channel select button 1. The LED lights red or purple to indicate it is selected.
5. Turn the Length encoder clockwise to increase cycle length. Turn it counterclockwise to decrease.
6. Set the Mode switch to the center up/down position for an attack-release shape.
7. Send triggers from Hermod+. Channel 1 fires an envelope with each trigger.
8. Tap the Hit button to manually trigger Channel 1 without a patched trigger signal.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 6 HP |
| Depth | 26 mm |
| Power | 60 mA +12V / 50 mA -12V / 0 mA +5V |

The manual states a depth of .8 inch (~20 mm), which conflicts with the user-provided measurement of 26 mm. Both values are flagged pending hardware verification. Output voltage is 0V to 5V. CV inputs respond to 0V to 5V. Envelopes trigger on a rising edge of approximately 3V.

---

## Essential Parameters

**Channel Select Buttons 1-4.** Four buttons along the left side of the panel select which channels the Length encoder currently controls. Multiple channels can be selected simultaneously; the encoder adjusts the cycle length of all selected channels together, which makes it easy to set two channels to the same length or to move them in parallel. When a channel is selected, its LED lights red or purple: red indicates a shorter cycle length, purple indicates a longer one. When a channel is deselected, its LED is either unlit (indicating minimum length) or blue (indicating it has been set to a longer length but is not currently being edited). Deselecting all channels and reselecting one at a time is the workflow for setting independent cycle lengths across the four channels.

**Length Encoder.** The single encoder controls the cycle length of all currently selected channels. Turning clockwise increases cycle length; counterclockwise decreases it. The range via the encoder alone is 2.5 ms to 9 seconds. Pressing the encoder down resets selected channels to their minimum cycle length; pressing it again immediately undoes the reset. This press-to-reset behavior is useful for live performance: a channel can be snapped to its minimum length and restored in two taps without navigating a menu.

**Hit Button.** Tapping Hit manually triggers selected channels in envelope mode, producing an envelope without requiring a patched trigger input. In LFO mode, tapping Hit resets the phase of selected channels to the beginning of their cycle, which can be used to synchronize multiple LFO channels that have drifted out of alignment. Holding Hit for approximately two seconds toggles LFO mode on or off for the currently selected channels. On power-up, holding Hit before the module starts up changes the CV response behavior from continuous (default) to sample and hold, which is a global setting that persists until the next power cycle.

**Mode Switch.** A three-position switch sets the envelope shape for all four channels simultaneously. The three positions are ramp up (output rises from 0V to 5V over the cycle length), up/down (output rises to 5V and then falls back to 0V symmetrically, producing an AR or triangle shape), and ramp down (output starts at 5V and falls to 0V over the cycle length, producing a decay shape). This is a global switch; all four channels use the same shape. Independent per-channel shapes are not available.

**CV Inputs 1-4.** Each channel has its own CV input that extends its cycle length beyond the encoder's range. CV inputs respond to 0V to 5V. In the default short CV response range, a 5V input extends the maximum cycle length to approximately 95 seconds. In long CV response range, a 5V input extends it to approximately 320 seconds. The CV response range is set per channel by holding the encoder for approximately two seconds and then pressing the channel button to toggle between short (blue LED confirmation) and long (red LED confirmation). CV response can also be set globally to sample and hold behavior on power-up by holding Hit before the module initializes; in this mode, the module samples the CV input voltage only when a trigger is received rather than continuously tracking it.

**Trigger Inputs 1-4.** Each channel has its own trigger input. These inputs are circularly normalled: a trigger signal patched into Channel 1's trigger input with no cables patched into Channels 2, 3, or 4 will trigger all four channels simultaneously. Patching a separate trigger into Channel 2's trigger input breaks the normalling chain at that point; Channel 1's trigger no longer reaches Channels 2, 3, or 4, and Channel 2's trigger feeds Channels 2, 3, and 4. This normalling behavior means a single trigger source can drive all four channels without any mult, and independent trigger sources can be added per channel as needed. In LFO mode, a trigger resets the phase of that channel's LFO rather than starting an envelope.

**Outputs 1-4.** Each channel has its own output carrying the envelope or LFO signal, 0V to 5V.

---

## Why This Instrument Excels

The single encoder architecture is the Pons Asinorum's most underrated feature because its value only becomes apparent during live performance. A standard four-channel envelope module requires four separate controls, one per channel, which means adjusting the overall modulation rate of a patch requires four separate knob movements. The Pons Asinorum's channel select system means that all four channels can be selected simultaneously with one button press each, and a single encoder turn then shifts all four cycle lengths together, maintaining their relative spacing while changing the overall tempo. Then any channel can be deselected to isolate it for individual adjustment. This workflow — select all, adjust together, deselect and refine — is faster in performance than any collection of individual knobs for the same task, and it is the reason the module's apparently minimal panel surface area is not actually a limitation.

The linear envelope shape is not a compromise or a simplification; it is a distinct tonal choice with specific sonic consequences. An exponential envelope sounds natural for amplitude control because exponential decay matches how the ear perceives loudness reduction. A linear envelope applied to amplitude sounds mechanical in comparison: the level drops at a constant rate rather than in the perceptually smooth curve the ear expects. This mechanical quality becomes an asset when the envelope is used as a modulation source rather than an amplitude envelope. A linear ramp driving a filter cutoff sweeps frequency at a constant rate, producing a smooth, mathematically predictable sweep. A linear ramp driving pitch produces an even glide. In generative and ambient contexts where multiple linear slopes modulate multiple parameters simultaneously, the predictability of the linear shape means the modulation relationships between channels remain readable and controllable in ways that exponential shapes, which curve at different rates depending on their length settings, do not guarantee.

The per-channel LFO mode toggle makes the Pons Asinorum function as a mixed modulation bank where different channels serve entirely different musical roles simultaneously. In a standard patch, envelope generators and LFOs are separate modules drawing on separate HP and power budget. Pons Asinorum collapses this separation: Channel 1 can trigger as an envelope from the sequencer gate, Channel 2 can run as a slow free-running LFO for filter modulation, Channel 3 can trigger as a shorter envelope for a secondary parameter, and Channel 4 can run as a faster LFO for vibrato, all from the same 6HP module with a shared encoder for convenient rate adjustment. The CV inputs on each channel mean each of these can be voltage-controlled independently, producing a fully modulated four-channel modulation bus in a footprint that a single multi-stage envelope generator often requires.

The circular normalling on the trigger inputs is a design decision that rewards planning but reveals its depth slowly. The normalling chain means a single clock or gate source drives all four channels with one cable until a second cable breaks the chain. For straightforward patches where all envelopes fire on the same beat, this eliminates three cables. For more complex patches, the normalling chain can be broken strategically: patching Hermod+ into Channel 1 and a slower clock division into Channel 3 means Channels 1 and 2 fire together from the main clock and Channels 3 and 4 fire together from the division, producing rhythmic envelope relationships with two cables instead of four. Understanding where the normalling breaks and where it continues is the essential conceptual bridge the Pons Asinorum asks its user to cross, which is, intentionally, the proposition the module is named after.

---

## Patches

### Patch 1: Basic Envelope Voice

Noise Engineering Pons Asinorum with a single channel in envelope mode driving a VCA, establishing the fundamental triggered envelope workflow and demonstrating the encoder and mode switch controls.

```
[Hermod+ Gate Out] ──────────[G]──────▶ [Pons Asinorum Trig In 1]

[Pons Asinorum Out 1] ───────[C]──────▶ [VCA CV In]
[Cs-L Audio Out] ────────────[A]──────▶ [VCA Audio In]
[VCA Audio Out] ─────────────[A]──────▶ [MixUp CH1]

                                         Channel 1: selected
                                         Mode switch: up/down (AR)
                                         Length: medium (2-4 seconds)
                                         Channels 2-4: deselected
```

**Setup:** Patch Hermod+'s gate into Trigger In 1 and Out 1 into a VCA's CV input. Patch the Instruo Cs-L into the VCA's audio input and the VCA's output into a mixer. Press channel select button 1 to select it; the LED lights. Set the Mode switch to the center up/down position for a symmetric AR shape. Because only Channel 1's trigger input has a cable, the normalling chain does not reach Channels 2, 3, or 4; only Channel 1 fires.

**Controls:** Turn the encoder clockwise and the cycle length increases; counterclockwise decreases it. The envelope lengthens and shortens audibly at the VCA output. Switch the Mode switch to ramp up: the envelope now attacks slowly and releases immediately when the gate closes, producing a slow swell with a sharp cutoff. Switch to ramp down: the attack is immediate and the decay is gradual, producing a pluck and bloom. Switch back to up/down for the symmetric AR. Press the encoder while Channel 1 is selected to reset it to minimum length; the envelope becomes a snap. Press again to undo and restore the previous length. Tap Hit to fire Channel 1 manually without a trigger cable — useful for testing and performance.

**Result:** A single triggered envelope voice demonstrating the three mode shapes and the encoder's range. The press-to-reset and undo behavior of the encoder becomes immediately useful once the minimum-length snap is heard in contrast to longer settings.

---

### Patch 2: Four Channels, One Trigger

All four channels triggered from a single gate source via circular normalling, each set to different cycle lengths and routed to different destinations, showing how the normalling chain and the multi-select encoder workflow operate together.

```
[Hermod+ Gate Out] ──────────[G]──────▶ [Pons Asinorum Trig In 1]
                                         (normalled to channels 2, 3, 4)

[Pons Asinorum Out 1] ───────[C]──────▶ [VCA CV In]
[Pons Asinorum Out 2] ───────[C]──────▶ [SSF SSG Stereo Field FREQ CV]
[Pons Asinorum Out 3] ───────[C]──────▶ [Zadar Rate CV CH1]
[Pons Asinorum Out 4] ───────[C]──────▶ [Aurora Warp CV]

[Cs-L Audio Out] ────────────[A]──────▶ [VCA Audio In]
[VCA Audio Out] ─────────────[A]──────▶ [MixUp CH1]

                                         Channel 1: long (3-4 seconds), up/down
                                         Channel 2: medium (1-2 seconds), ramp down
                                         Channel 3: short (200-400 ms), ramp down
                                         Channel 4: long (5-8 seconds), up/down
                                         Mode switch: ramp down (set before programming)
```

**Setup:** Patch one gate cable from Hermod+ into Trigger In 1 only. Leave Trigger Ins 2, 3, and 4 unpatched; the normalling chain carries Channel 1's trigger to all four channels. Patch the four outputs to four separate destinations. To set independent lengths: press channel 1 alone, set its length; deselect 1, press channel 2, set its length; continue for 3 and 4. To set channels 1 and 2 to the same length, select both simultaneously by holding 1 and pressing 2, then adjust the encoder. The mode switch applies globally; set ramp down first, then adjust lengths, since changing the switch affects all channels.

**Controls:** Once running, select all four channels simultaneously (press all four select buttons) and turn the encoder to shift all cycle lengths proportionally upward or downward together. The relative spacing between channels is maintained. To change the rate at which only the longer channels evolve, deselect channels 1 and 4 and adjust 2 and 3 separately. Tap Hit to fire all four channels manually in sync; this is useful for resetting the envelope contours at a specific moment in performance. Patching a second trigger into Trig In 3 breaks the normalling at that point: Channels 1 and 2 then fire from Hermod+, and Channels 3 and 4 fire from the second trigger independently.

**Result:** A four-destination modulation bus from a single gate cable, with each channel shaping a different parameter at a different rate. The normalling chain does the work of four separate mult connections; the shared encoder manages the overall modulation tempo across all channels.

---

### Patch 3: Mixed Envelope and LFO Operation

Channels 1 and 2 in envelope mode for note-triggered behavior, Channels 3 and 4 in LFO mode for continuous ambient modulation, with CV control of LFO rates from a Zadar envelope producing evolving modulation depth.

```
[Hermod+ Gate Out] ──────────[G]──────▶ [Pons Asinorum Trig In 1]
                                         (normalled to channel 2)
[Hermod+ Gate Out] ──────────[G]──────▶ [Pons Asinorum Trig In 3]
                                         (normalled to channel 4)

[Zadar CH1 Env Out] ─────────[C]──────▶ [Pons Asinorum CV In 3]
[Zadar CH2 Env Out] ─────────[C]──────▶ [Pons Asinorum CV In 4]
[Hermod+ Gate Out] ──────────[G]──────▶ [Zadar Trigger CH1 + CH2]

[Pons Asinorum Out 1] ───────[C]──────▶ [VCA CV In]
[Pons Asinorum Out 2] ───────[C]──────▶ [SSF SSG Stereo Field FREQ CV]
[Pons Asinorum Out 3] ───────[C]──────▶ [Nautilus Resolution CV]
[Pons Asinorum Out 4] ───────[C]──────▶ [Aurora Warp CV]

[Cs-L Audio Out] ────────────[A]──────▶ [VCA Audio In]
[VCA Audio Out] ─────────────[A]──────▶ [MixUp CH1]

                                         Channels 1-2: envelope mode, up/down
                                         Channels 3-4: LFO mode, up/down
                                         Ch 3 base length: 4 seconds
                                         Ch 4 base length: 7 seconds
                                         Zadar Ch1: slow rising ramp
                                         Zadar Ch2: slow falling ramp
```

**Setup:** Patch Hermod+ gate into Trigger In 1 (normalled to 2) and into Trigger In 3 (normalled to 4). Because Trigger In 3 is patched, the normalling from Channel 1 breaks at Channel 3; Channels 1 and 2 receive the Hermod+ trigger through Channel 1's normalling, and Channels 3 and 4 receive it through Channel 3's normalling. To put Channels 3 and 4 into LFO mode: select them both, hold Hit for two seconds until the LEDs change. In LFO mode, the trigger input resets phase rather than triggering an envelope; the channels run continuously. Patch Zadar's two envelopes into CV Ins 3 and 4 to modulate their cycle lengths.

**Controls:** Channels 1 and 2 fire as envelopes on each gate event; Channels 3 and 4 run as continuous LFOs whose rates are being modulated by Zadar's envelopes. As Zadar's envelope rises, the LFO cycle length extends (slower LFO); as it falls, the cycle length compresses (faster LFO). This produces LFO rate variation that tracks the gate rhythm: each new note event fires Zadar, which in turn alters the LFO rates for the next phrase. Tap Hit to reset LFO phase on Channels 3 and 4 to synchronize them against each other; their relative phase will then drift apart at their current rates and can be reset again at the next musically appropriate moment.

**Result:** A modulation system where triggered events and free-running LFOs share the same 6HP module and interact through a shared gate source. The CV-controlled LFO rates produce modulation that changes character phrase by phrase rather than remaining static over the course of a patch.

---

### Patch 4: Quadrature LFO

All four channels in envelope mode forming a ring patch: each channel's output triggers the next channel's envelope, producing four envelope outputs cycling 90 degrees apart in phase from each other, equivalent to a four-phase quadrature LFO.

```
[Pons Asinorum Out 1] ───────[C]──────▶ [Nautilus Resolution CV]
[Pons Asinorum Out 1] ───────[C]──────▶ [Pons Asinorum Trig In 2]

[Pons Asinorum Out 2] ───────[C]──────▶ [SSF SSG Stereo Field FREQ CV]
[Pons Asinorum Out 2] ───────[C]──────▶ [Pons Asinorum Trig In 3]

[Pons Asinorum Out 3] ───────[C]──────▶ [Aurora Warp CV]
[Pons Asinorum Out 3] ───────[C]──────▶ [Pons Asinorum Trig In 4]

[Pons Asinorum Out 4] ───────[C]──────▶ [Bela Gliss CV/GATE]
[Pons Asinorum Out 4] ───────[C]──────▶ [Pons Asinorum Trig In 1]

                                         All 4 channels: envelope mode, up/down
                                         Mode switch: up/down (center)
                                         All channels: same length (4-8 seconds)
                                         TRIG IN 1: no external patch (ring closes here)
```

**Setup:** Set all four channels to envelope mode (the default; confirm none are in LFO mode). Set the Mode switch to the center up/down position. Select all four channels simultaneously by pressing all four select buttons and set the encoder to a long cycle length, approximately 4 to 8 seconds. Using a mult or stackable cables, patch Out 1 to both its modulation destination and to Trig In 2; Out 2 to its destination and to Trig In 3; Out 3 to its destination and to Trig In 4; Out 4 to its destination and to Trig In 1. This closes the ring: Channel 4's output triggers Channel 1, which triggers Channel 2, and so on. To start the loop, select only Channel 1 and tap Hit once. Channel 1 fires its envelope; when its output crosses the approximately 3V trigger threshold on the rising slope, it triggers Channel 2, which triggers Channel 3, and so on in sequence.

**Controls:** Because the up/down mode switch produces a symmetric rise and fall, each channel triggers the next at the midpoint of the rising slope. With all channels at the same cycle length, the four outputs are approximately 90 degrees apart in phase, producing a quadrature LFO-like behavior: Channel 1 peaks while Channel 2 is halfway up, Channel 3 is just starting to fall, and Channel 4 is still falling from its peak. Adjust the cycle length with all four channels selected to change the quadrature rate. To desynchronize the phases, deselect all but one channel and adjust its length slightly shorter or longer; the ring will drift and produce polyrhythmic phase relationships instead of the clean quadrature. To reset, tap Hit with Channel 1 selected to refire the starting channel and bring the ring back into alignment from that point.

**Result:** Four phase-offset modulation signals derived from a single Hit press, with no clock input and no LFO mode required. The phase relationship between channels is determined by the trigger threshold and the cycle length, and can be adjusted from clean quadrature to polyrhythmic drift by detuning individual channels from the common length.

---

## Common Mistakes

### "The module is not responding to my trigger — all four channels fire when I only want one"

The trigger inputs are circularly normalled. A trigger patched into Trigger In 1 with no cables in Trigger Ins 2, 3, or 4 reaches all four channels through the normalling chain. This is correct behavior; it is the default so that a single trigger source drives all four channels without a mult.

**Fix:** To trigger only Channel 1, patch a cable into Trigger In 2 from any source (even an unused output or a dummy cable). This breaks the normalling at Channel 2, which prevents Channel 1's trigger from reaching Channels 2, 3, and 4. The normalling only passes a trigger forward past an unpatched input; a patched input blocks the chain at that point.

---

### "I cannot figure out how to set different cycle lengths for different channels"

The encoder controls whichever channels are currently selected. If multiple channels are selected simultaneously, they all move together, which is the feature — but it makes independent setting non-obvious.

**Fix:** Deselect all channels first by pressing each lit select button until all LEDs are off or blue. Then press only the channel you want to set, adjust the encoder to the desired length, and deselect that channel. Press the next channel, adjust, and deselect. Repeating this for each channel sets them all independently. To set two channels to identical lengths, select both simultaneously, adjust, then deselect both. The blue LED on a deselected channel confirms it has been set to a non-minimum length and will remember its setting.

---

### "The encoder controls are not working — the cycle length is not changing even though I am turning it"

No channels are selected. The encoder only adjusts the cycle length of selected channels; if all channels are deselected, turning the encoder has no effect.

**Fix:** Press at least one channel select button to select a channel (the LED lights red or purple), then adjust the encoder. If the encoder turn still produces no audible change after selecting a channel, the channel may already be at its minimum or maximum length, or the CV input may be overriding the encoder position with a high voltage.

---

### "The LFO rate is jumping instead of smoothly tracking my CV input"

The module's CV response is set to sample and hold mode, which was activated by holding Hit during the last power-up. In S&H mode, the CV input is only sampled when a trigger is received; between triggers, the cycle length holds at the last sampled value. Turning the CV source produces no continuous response.

**Fix:** Power the module down and power it back up without holding Hit. After the initial LED flashing confirms standard boot, the CV response will be continuous and the LFO rate will track the CV input in real time. If you want S&H behavior intentionally, it is activated again by holding Hit on the next power-up.

---

### "My quadrature ring patch stopped cycling on its own"

The ring patch requires each channel's output to cross approximately 3V on its rising slope to trigger the next channel's envelope. If the cycle length is set too short, the output may not reach 3V before the envelope completes, which breaks the chain. If a channel's output reaches maximum and begins falling before the next channel receives a trigger, the ring stalls.

**Fix:** Increase the cycle length of all channels. In up/down mode, the 3V trigger threshold is crossed at approximately 60% of the peak voltage on the rising slope, which happens reliably when the cycle length is long enough for the output to fully develop. Cycle lengths between 2 and 10 seconds typically sustain the ring reliably. If the ring still stalls, check that the output voltage is reaching at least 3V at the patch point; cable length and impedance at the destination can reduce the voltage seen at the trigger input.

---

### "Changing the Mode switch mid-performance affects all channels at once, which breaks the patch"

The Mode switch is a global control that simultaneously changes the envelope shape of all four channels. There is no per-channel shape control; the three shapes (ramp up, up/down, ramp down) apply across the whole module.

**Fix:** Plan the envelope shape for the patch before programming the cycle lengths. If a patch genuinely requires different shapes on different channels simultaneously, use two separate modulation sources rather than relying on the PA alone for all four shapes. Within the PA's architecture, the global shape switch is a performance parameter that changes the character of all envelopes together, which is useful for shifting the whole modulation character of a patch in one move rather than a limitation to work around.

---

## Advanced Learning Path

Begin with the trigger normalling and spend time deliberately breaking and restoring the chain. Patch a trigger into Channel 1 and confirm that all four channels fire. Then patch a second trigger into Channel 2 and confirm that Channels 1's trigger no longer reaches Channels 2, 3, or 4. Then patch a third trigger into Channel 3 and confirm that Channel 2's trigger no longer reaches 3 or 4. Understanding exactly where the chain breaks and what each trigger source reaches is the foundational competency for all multi-trigger patches; it determines which channels share trigger sources and which are independent, and that relationship defines the rhythmic structure of any patch using the PA as its modulation core.

Work through the per-channel CV range settings systematically. Set a channel to its default short range, patch a 0-5V LFO into its CV input, and observe the cycle length extension from the encoder's base range up to approximately 95 seconds. Then switch that channel to long range (hold encoder for two seconds, press channel button until LED shows red) and observe the same LFO extending the cycle length to approximately 320 seconds. The practical difference between these ranges is the tempo of generative patches: short range suits rhythmic modulation that tracks a beat; long range suits ambient drift that evolves over minutes. Set different channels to different ranges for a modulation system where some channels operate in musical time and others in geological time simultaneously.

Explore the S&H CV mode as a distinct compositional tool rather than a misconfiguration to avoid. Activate S&H on power-up (hold Hit during boot until blue LEDs confirm). With a random CV source at the CV inputs and a gate from Hermod+ at the trigger inputs, each gate event samples a new random cycle length, which is then held until the next gate. This produces a modulation source whose rate changes discretely with each triggered note rather than continuously; the envelope length is selected by the timing of the gate rather than by a slowly moving LFO, making it rhythmically locked but randomly varying. Setting different channels to different CV sources in S&H mode produces four independently and randomly varying envelope lengths that are all updated in sync with the gate rhythm.

Investigate the relationship between the three Mode shapes and different modulation destinations. Route a single channel's output to three different destinations simultaneously via a mult and switch the Mode switch between ramp up, up/down, and ramp down while listening to each destination. A ramp-up shape driving filter cutoff produces a sweep that opens from dark to bright and stays bright until the gate closes; the same shape driving a reverb wet/dry mix pushes the reverb in over the course of the note; the same shape driving pitch produces a rising portamento that reaches target pitch at the end of the envelope rather than the beginning. Each shape produces a different musical result at each destination type, and understanding these combinations before building complex patches makes the global shape switch more useful rather than more restrictive.

Build the quadrature ring patch from the Patches section and then deliberately detune it. With all four channels in the ring and running at the same cycle length, the output is a clean quadrature LFO. Deselect Channels 2 and 4 and increase Channel 2's length by 10% and decrease Channel 4's by 10%. The ring continues to cycle but the phase relationships shift away from the clean 90-degree spacing, producing a slowly rotating polyrhythmic pattern. As the detune increases, the phase relationships continue to evolve and the four outputs produce modulation that no fixed-phase quadrature LFO can replicate. Experiment with how much detune the ring tolerates before it stalls; the stability boundary is itself a performance parameter.

Use the Hit button as a performance gesture independent of trigger patching. In a patch where all four channels run as LFOs, tapping Hit resets the phase of selected channels to zero. Selecting all four and tapping Hit synchronizes all four LFOs to the same phase starting point simultaneously, from which they drift apart at their respective rates. Selecting only one channel and tapping Hit resets only that channel, introducing a phase discontinuity that creates a rhythmic accent at that moment. In performance, this makes Hit a manual sync or phase-reset tool that works across both envelope and LFO modes and rewards practiced timing.

For a self-modulated patch without external CV sources, use the PA's own outputs to modulate each other's CV inputs. Route Out 1 to CV In 2, Out 2 to CV In 3, Out 3 to CV In 4, and Out 4 to CV In 1, in a separate ring from the trigger ring patch. With different channels at different base lengths, each channel's envelope extends the cycle length of the next channel in the ring, creating a system where longer envelopes produce longer descendants and shorter envelopes produce shorter descendants. The cycle length relationships in the ring evolve continuously without any external modulation source, and the result is a modulation system that generates its own variation from its initial state rather than from external input. Set the starting lengths carefully; the ring's behavior is sensitive to initial conditions and will produce different long-term patterns from small changes to the starting values.

---

## Pairs Well With

**Instruo Cs-L** benefits from Pons Asinorum's multi-channel independence because the Cs-L's most expressive patches use separate envelopes for amplitude, waveshaper amount, and linear FM depth simultaneously. Patching three PA channels to these three destinations with different cycle lengths produces a voice where every parameter evolves at its own rate from each gate event, and the single encoder's multi-select capability means the overall pace of all three can shift together in one encoder move during performance. The Cs-L's linear FM input in particular responds well to linear ramp shapes; a slow ramp-up envelope into the linear FM index builds FM complexity gradually over the course of a long note rather than applying it uniformly from the attack.

**Zadar** and Pons Asinorum cover adjacent but distinct parts of the modulation space and complement each other without redundancy. Zadar excels at complex, precisely shaped envelopes with flexible curve types per segment; Pons Asinorum excels at multiple simple linear shapes with per-channel cycle length CV and the quadrature ring behavior. In a combined patch, Zadar handles the primary amplitude and filter envelopes where curve shape matters most, while Pons Asinorum handles the secondary and tertiary modulation destinations where cycle length variation and simultaneous per-channel adjustment are more important than precise curve shape. The two modules share no overlapping strengths and cover each other's gaps.

**Qu-Bit Nautilus** receives Pons Asinorum's outputs well at its Resolution CV input because Resolution responds to the full 0-5V range and Nautilus's delay character shifts substantially across that range. In the quadrature ring patch, the four phase-offset outputs produce a slowly rotating modulation of Nautilus's internal delay timing that no single LFO replicates; the four signals arrive at different phases and can be routed to Resolution CV, Reverb Mix CV, and other Nautilus CV inputs simultaneously, each modulating a different parameter from a shared rhythmic structure. Nautilus's Sonar output in return makes an effective PA CV input source, coupling the reverb state back into the modulation rates and creating a reciprocal relationship between the two modules.

**SSF SSG Stereo Field** receives Pons Asinorum envelopes at its FREQ CV and TIMBRE CV inputs for rhythmically triggered filter and timbre modulation that follows the gate rhythm rather than running as a continuous LFO. The SSG's dual gate inputs (EXCITE and CV/GATE) can both receive PA outputs: Channel 1's shorter envelope into CV/GATE shapes the gate duration, and Channel 2's longer envelope into TIMBRE CV evolves the wavefolder depth over the course of the note. The PA's linear shapes produce a different timbral evolution at the SSG Stereo Field's FOLD input than a Zadar exponential curve would; the linear ramp drives the wavefolder through its harmonic range at a constant rate, producing a sweep whose harmonic content changes predictably rather than compressing near the envelope's peak.

**Bela Gliss** in CV/GATE mode receives a Pons Asinorum LFO channel as a continuously cycling gate that opens and closes the Gliss's low-pass gate behavior. Routing a PA ramp-down channel to Gliss's CV/GATE input produces a gate that opens immediately and closes gradually, which is a distinctly different articulation than a fixed-width gate from a sequencer. Simultaneously routing a second PA channel to Gliss's FIELD CV produces a linked spatial movement that tracks the same LFO cycle; the stereo field position and the gate depth evolve from the same source. In the quadrature ring patch, routing the four PA outputs to Gliss CV/GATE, FIELD CV, a downstream filter, and a VCA produces four parameters all cycling at 90-degree phase offsets from each other, creating a rotating spatial and dynamic modulation that changes character continuously without any additional input.

**Winterbloom Castor and Pollux II** uses Pons Asinorum envelopes at its CHORDET input and at its RAMP CV for per-note timbre and pitch variation. The RAMP CV input on Castor and Pollux II shifts the waveshaper ramp position; a slow ramp-up envelope from the PA drifts the wave character gradually over the course of each note rather than applying a fixed waveform. Combining this with a second PA channel into CHORDET produces a voice where both timbre and the polyphonic character shift on each note event, driven by the same trigger source but with independent cycle lengths, so the timbre variation and the waveshaping variation evolve at different rates and produce unpredictable combinations that no fixed modulation source sustains over time.
