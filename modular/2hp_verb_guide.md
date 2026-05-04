---
title: "2HP Verb"
manufacturer: "2HP"
module: "Verb"
format: "Eurorack"
type: "Stereo Reverb"
tags: ["reverb", "stereo", "algorithmic", "drums", "ambient", "space", "shaper"]
roles: ["sound-designer", "producer", "ambient-artist"]
hc: true
---

![2HP Verb](https://github.com/Shadoe-42/music/raw/main/modular/images/2hp/verb/front_panel.jpg)

# 2HP Verb

Verb is a stereo algorithmic reverb with three controls and one CV input. Time sets reverb length from tight room to infinite wash. Damp controls high-frequency absorption in the reverb tail from fully dark to fully bright. Mix blends dry and wet signal inline, and a CV input adds to the Mix knob position from 0V to 5V. Stereo inputs and outputs accept any source; a mono signal patched to IN L normals to both outputs, producing stereo reverb from a single cable.

---

## Historical Context

Every enclosed space produces reverberation. Sound energy radiates outward from its source, reflects off surfaces, reflects again, and continues reflecting and decaying until the energy is absorbed. The time this takes depends on the size of the space and the reflective properties of its surfaces. Hard surfaces — stone, concrete, glass — reflect most of the energy and extend the decay. Soft surfaces — fabric, wood paneling, carpet — absorb energy and shorten it. High frequencies are absorbed more readily than low frequencies by both air and soft materials, which means reverb tails naturally grow darker with distance and time regardless of the space.

Wallace Clement Sabine, a physicist at Harvard, spent the years around 1900 measuring reverberation time in lecture halls by carrying seat cushions into rooms and timing how long sound took to become inaudible with different amounts of absorptive material present. His reverberation equation — RT60, the time for sound to decay by 60 decibels — gave architects and engineers a mathematical tool for predicting and controlling the acoustic character of built spaces. The formula is still in use. Every concert hall, recording studio, and performance venue built since 1900 was designed with some version of Sabine's equation as a constraint.

Recording introduced a new problem. A studio that sounds appropriate for speech or classical performance sounds wrong for a drum kit or an electric guitar. Engineers found themselves wanting to add reverb to dry recordings after the fact, placing a dry signal inside a convincingly reverberant space that did not physically exist at the time of recording. The first practical solution was dedicated echo chambers: rooms built specifically to be reverberant, with a loudspeaker driving the space and microphones picking up the reflections. Capitol Records built echo chambers under the Capitol Records Tower in Hollywood in 1956. Abbey Road had multiple dedicated chambers. These solutions worked but were expensive, fixed in character, and permanently attached to the building.

The EMT 140 plate reverb, introduced by the German manufacturer Elektromesstechnik in 1957, offered the first mechanical alternative that studios considered truly musical. A large steel plate suspended in a frame — approximately two meters by one meter — was driven by a transducer at its surface; contact microphones at the plate's perimeter picked up the vibrations. Steel reflects sound energy efficiently, producing a dense, smooth decay that studios found more flattering than spring reverb and more controllable than chambers. Abbey Road eventually owned eight EMT 140s. The plate reverb defined the sound of recorded music through the 1960s and into the 1970s, and its character is directly audible in the Verb's brightest Damp setting: no high-frequency absorption, clean reflective decay, the metallic shimmer of a plate.

Manfred Schroeder at Bell Labs published "Natural Sounding Artificial Reverberation" in the Journal of the Audio Engineering Society in 1962. His paper proposed simulating the dense reflective behavior of a reverberant space using parallel comb filters — to build up reflection density over time — followed by allpass filters — to diffuse the result without introducing tonal coloration. The architecture required no physical space, no plate, no spring. It was purely mathematical: a set of signal processing operations that approximated what acoustics does mechanically. In 1962, the required computation was not possible in real time. By 1978, it was. The Lexicon 224, released that year, was the first commercially successful digital reverb built on the Schroeder architecture. It cost seven thousand dollars and was present in nearly every major commercial studio within a decade. Every digital reverb made since, including the one running inside Verb, descends from Schroeder's 1962 paper.

The Damp control in Verb directly models Sabine's physical observation: high frequencies decay faster than low frequencies in real acoustic spaces because air and soft surfaces absorb them more readily. Fully CCW damps the reverb tail aggressively toward the low end, producing the character of a large, soft-surfaced space absorbing high-frequency content over the length of the decay. Fully CW applies no dampening, allowing the full high-frequency content of the reverb tail to persist — which is what a steel plate does. The knob sweeps between padded hall and EMT 140 without leaving the module.

---

## Quick Start

1. Patch a sound source into IN L. For a mono source, patching only IN L normals the signal to both OUT L and OUT R, producing stereo reverb output from a single input cable.
2. Patch OUT L to MixUp CH3 L and OUT R to MixUp CH3 R.
3. Set Time to 12 o'clock.
4. Set Damp to 12 o'clock.
5. Set Mix to 12 o'clock (equal dry and wet).
6. Play the source and listen to the reverb character at these neutral settings.
7. Adjust Time to hear the range: fully CCW produces a tight room character; fully CW produces a long, washing decay that extends well beyond the source note.
8. With Time set, sweep Damp from fully CCW to fully CW. Fully CCW is dark and absorbed; fully CW is bright and plate-like. Find the Damp position that suits the source and context.
9. Adjust Mix to taste. Fully CCW is dry only; fully CW is wet only. For drums, a Mix between 9 and 11 o'clock typically adds reverb character without overwhelming the dry transient.
10. If a stereo source is patched, use both IN L and IN R. Note that IN R signals emit only from OUT R; IN L signals normal to both outputs only when IN R is unpatched.

---

## Key Specs

| Parameter | Value |
|---|---|
| Format | Eurorack |
| Width | 2HP |
| Depth | 47mm |
| +12V | 81mA |
| -12V | 28mA |
| +5V | 0mA |
| Price (MSRP) | $149 |

---

## Essential Parameters

**Time** sets the length of the reverb decay from the shortest possible tail at fully CCW to the longest at fully CW. Short Time settings produce room and chamber character; the reverb decays before the next transient arrives. Long Time settings produce hall and wash character; the decay extends far beyond the source event and accumulates at fast tempos. For drums, Time is the primary control over how much the reverb affects the rhythmic clarity of the pattern: too long at fast tempos and snare hits begin stepping on each other's tails; too short and the reverb contributes nothing beyond a slight thickening of the transient.

**Damp** controls high-frequency absorption in the reverb tail. Fully CCW applies maximum dampening: the reverb tail rolls off high frequencies aggressively, producing a dark, warm, distant character that simulates a large space with absorptive surfaces. Fully CW applies no dampening: the full high-frequency content of the reverb tail persists through the entire decay, producing a bright, metallic, plate-like character. The Damp direction is inverted from what some controls call "color" or "tone": turning left makes it darker, turning right makes it brighter. This maps directly to the physics of acoustic absorption — the knob adjusts how much the reverb behaves like an absorptive room versus how much it behaves like a reflective plate.

**Mix** blends the dry input signal with the reverb wet signal. Fully CCW is fully dry; fully CW is fully wet. Mix operates inline: the dry signal passes through Verb and appears at the outputs alongside the reverb, so the module does not need to be used in a send/return configuration. For drums, a low Mix setting (9 to 11 o'clock) adds spatial character while preserving the punch of the dry transient. Higher Mix settings reduce the dry signal and move the reverb toward a processing-forward role.

**Mix CV** accepts a control voltage of 0V to 5V. The voltage adds to the knob position rather than replacing it, which means the knob sets the floor and the CV pushes the mix wetter from that point. A CV of 0V leaves the Mix at the knob position. A CV of 5V pushes the Mix to fully wet regardless of knob position. To use an envelope for automated wet/dry control, set the Mix knob to fully CCW (dry) and let the envelope sweep the mix from dry to wet. To set a wet floor and have CV add above it, position the knob at the desired minimum and let the CV drive from there.

**IN L / IN R normalling:** Patching only IN L normals that signal to both OUT L and OUT R. This is the correct approach for a mono source; one cable into Verb produces a stereo reverb output. Patching a signal to IN R routes that signal only to OUT R and breaks the normal from IN L to OUT R. For two independent mono sources feeding the reverb, both inputs must be patched. For a stereo source, use both inputs.

---

## Why This Excels

Verb solves a specific problem efficiently: a stereo reverb that can live inline in a patch without requiring a separate mixer channel for dry/wet management. Most Eurorack reverbs output a fully wet signal and depend on an external mixer to blend in the dry source. Verb's Mix control means the blend happens inside the module, and the output is the finished combination. For a drum voice going directly to MixUp CH3, one less patch decision is required: the reverb amount is set at Verb, and MixUp receives a complete signal rather than two parallel paths to balance.

The Damp control gives Verb a wider timbral range than its control count suggests. At fully CCW, the module produces a dark, ambient reverb that sits behind the source rather than competing with it. At fully CW, it produces a bright, percussive reverb tail that reads as a feature of the sound rather than a spatial treatment. These are not minor variations; they are genuinely different reverb characters. A snare with Damp fully CW sounds like a plate reverb hit; the same snare with Damp fully CCW sounds like a room hit. The same module produces both without switching algorithms or reconfiguring the patch.

The Mix CV input enables reverb automation that knob-only designs cannot do. An envelope triggered by the same gate that triggers a drum hit can sweep the Mix from dry to wet and back across the duration of the note. The result is a reverb that opens after the transient — letting the initial punch through dry — and closes before the next hit, which eliminates the reverb accumulation that muddies drum patterns at fast tempos. This behavior is closer to how a live drummer in a room actually sounds: the transient arrives dry and the tail develops behind it rather than blending with the impact.

---

## Patches

### Patch 1: Drum Room

vpme.de QD percussion voice into Verb inline, short Time, moderate Damp — adding room character to a drum hit without obscuring the transient.

```
[Hermod+ Gate Out] ──────────────────────▶ [QD Trigger In]

[QD Voice Out] ──────────────────────────▶ [Verb IN L]

                                            Time: 9-10 o'clock (short)
                                            Damp: 10-11 o'clock (moderately dark)
                                            Mix: 9-10 o'clock (mostly dry)

[Verb OUT L] ────────────────────────────▶ [MixUp CH3 L]
[Verb OUT R] ────────────────────────────▶ [MixUp CH3 R]
```

**Setup:** QD voice output feeds Verb IN L directly. Patching only IN L normals the mono drum signal to both outputs, producing stereo reverb from the single drum voice. Hermod+ provides gate timing to QD. Verb sits inline between the drum voice and MixUp CH3.

**Controls:** Time at 9 to 10 o'clock produces a short reverb tail — enough to add perceived room size without extending past the next drum hit at moderate tempos. Damp at 10 to 11 o'clock absorbs the upper high-frequency content of the tail, pulling it toward a slightly dark, convincing room character rather than plate brightness. Mix at 9 to 10 o'clock is mostly dry, adding reverb as a spatial effect behind the transient rather than as an equal-presence effect layer. Adjust Mix first: if the drum hits begin sounding washy, reduce it. Adjust Time second: if reverb tails are audibly stepping on each other in the pattern, shorten it. Damp last: use Damp to shift between room character (CCW) and plate character (CW) once Time and Mix are dialed.

**Result:** A drum voice with inline room reverb that adds spatial depth and body without obscuring the attack or muddying the rhythmic pattern. This is the foundational Verb configuration for percussive material.

---

### Patch 2: Plate Snare

QD snare voice into Verb with Damp fully CW and medium Time — simulating the EMT 140 plate reverb character on a snare hit.

```
[Hermod+ Gate Out] ──────────────────────▶ [QD Trigger In (Snare Voice)]

[QD Snare Out] ──────────────────────────▶ [Verb IN L]

                                            Time: 11 o'clock to 12 o'clock
                                            Damp: fully CW (no dampening)
                                            Mix: 11 o'clock to 12 o'clock

[Verb OUT L] ────────────────────────────▶ [MixUp CH3 L]
[Verb OUT R] ────────────────────────────▶ [MixUp CH3 R]
```

**Setup:** Same routing as Patch 1 but with the Damp control at fully CW, which removes all high-frequency absorption from the reverb tail. This is the plate reverb setting: the decay is bright, the tail has presence in the upper frequencies throughout its duration, and the character reads as a studio plate rather than a room.

**Controls:** Damp fully CW is the central setting for this patch — it defines the plate character. Time at 11 o'clock to 12 o'clock produces a medium reverb length appropriate for snare: long enough for the plate character to fully develop, short enough to decay before the pattern repeats. Mix at 11 o'clock to 12 o'clock gives the plate reverb more presence in the output than the room patch — plate reverb on snare is a feature of the sound, not a subtle spatial treatment, and the mix should reflect that. A brighter snare voice from QD suits this patch more than a darker one; the plate reverb extends the brightness. If the tail is too present, pull Mix back before adjusting Time.

**Result:** A snare voice with bright, plate-style reverb that extends the tail with high-frequency content throughout the decay. Audibly different from the room character of Patch 1; the plate setting reads as a deliberate sonic treatment rather than ambient space.

---

### Patch 3: Envelope-Controlled Mix

Gate-triggered Zadar envelope into Verb's Mix CV with the Mix knob at fully CCW — automating the wet/dry blend so reverb opens after the transient and closes before the next hit.

```
[Hermod+ Gate Out] ──────────────────────▶ [QD Trigger In]
[Hermod+ Gate Out] ──────────────────────▶ [Zadar Trigger CH1]

[Zadar CH1 Env Out] ─────────────────────▶ [Verb Mix CV]
[QD Voice Out] ──────────────────────────▶ [Verb IN L]

                                            Time: 12 o'clock
                                            Damp: 11 o'clock
                                            Mix knob: fully CCW (CV controls blend)
                                            Zadar CH1: fast attack (<30ms),
                                            medium decay (200-500ms), no sustain

[Verb OUT L] ────────────────────────────▶ [MixUp CH3 L]
[Verb OUT R] ────────────────────────────▶ [MixUp CH3 R]
```

**Setup:** Hermod+ gate simultaneously triggers QD and Zadar channel 1. Zadar CV output goes to Verb's Mix CV input. With the Mix knob at fully CCW (dry), the Mix CV controls the entire blend from 0V (fully dry) to 5V (fully wet). The Zadar envelope sets the shape of the reverb blend over time.

**Controls:** The key relationship: the Mix knob sets the dry floor and CV adds above it. With the knob at fully CCW, the envelope controls the entire range from dry to wet. A Zadar envelope with a fast attack (under 30ms) allows the drum transient to hit dry before the reverb opens. A medium decay (200 to 500ms) brings the reverb in over the sustain portion of the hit and fades it before the next gate. No sustain means the blend returns to dry between hits, preventing accumulation. The result is a reverb that behaves more like a real acoustic event: the transient arrives first, the tail develops behind it, and the space clears before the next hit. Adjust Zadar's decay to control how long the reverb blend remains open; a longer decay at fast tempos will cause tails to overlap.

**Result:** Automated reverb blend triggered by the gate, with the transient arriving dry and the reverb opening in the decay portion of each hit. Demonstrates Mix CV as a dynamic control rather than a static blend setting.

---

### Patch 4: Long Wash on Pad

2HP Swarm saw pad into Verb with long Time and moderate Damp — using Verb as a spatial processor on a melodic source, pushing the mix toward fully wet for an immersive pad treatment.

```
[Hermod+ Pitch CV] ──────────────────────▶ [Swarm V/Oct]
[Hermod+ Gate Out] ──────────────────────▶ [Zadar Trigger CH1]

[Zadar CH1 Env Out] ─────────────────────▶ [VCA CV In]
[Swarm Audio Out] ───────────────────────▶ [VCA Audio In]
[VCA Audio Out] ─────────────────────────▶ [Verb IN L]

                                            Time: 2-3 o'clock (long)
                                            Damp: 11 o'clock (slightly dark)
                                            Mix: 2-3 o'clock (mostly wet)

[Verb OUT L] ────────────────────────────▶ [MixUp CH3 L]
[Verb OUT R] ────────────────────────────▶ [MixUp CH3 R]
```

**Setup:** Swarm saw with light Detune feeds through a VCA shaped by Zadar, then into Verb. Long Time and a high Mix setting shift Verb from a spatial add-on into a primary character of the sound. Patching only IN L normals the mono Swarm output to both outputs, widening the detuned pad into stereo through the reverb.

**Controls:** Time at 2 to 3 o'clock produces a long reverb tail that extends well beyond the note duration — appropriate for a pad application where sustained space is the goal rather than rhythmic clarity. Damp at 11 o'clock is slightly dark, which smooths the high-frequency energy from Swarm's detuned saw voices and prevents the reverb tail from becoming harsh. Mix at 2 to 3 o'clock pushes toward wet, reducing the dry signal and letting the reverb dominate. The pad's supersaw density feeds the algorithmic reverb with enough harmonic content to produce a full, rich wash; simpler waveforms produce thinner results at the same settings. Zadar's slow-attack envelope prevents the pad from transient-attacking into the reverb; the reverb tail builds gradually as the pad opens.

**Result:** A stereo reverb wash built from a supersaw pad source, with Verb operating as the primary spatial and timbral character of the sound rather than a subtle room effect. Demonstrates Verb in a melodic context as an alternative to drum-focused use.

---

## Common Mistakes

### "I turned Damp up to add brightness but the reverb got darker"

The Damp control direction is inverted from the label's intuitive reading. Fully CCW applies maximum dampening, meaning maximum high-frequency absorption — the reverb tail is darkest at this position. Fully CW applies no dampening, meaning no absorption — the reverb tail is brightest at this position. "More Damp" at lower knob positions means more absorption, not more dampening effect in the direction of brightness. Think of it as "amount of darkening" increasing counterclockwise rather than as a brightness control that follows the knob's clockwise direction.

**Fix:** For brighter reverb, turn Damp clockwise toward fully CW. For darker reverb, turn Damp counterclockwise toward fully CCW. Fully CW = plate character. Fully CCW = padded room character.

---

### "The reverb is making my drum pattern sound muddy even at low Mix settings"

Time is too long for the tempo and pattern density. At fast tempos, a reverb tail that extends beyond the time between drum hits accumulates — each hit's tail bleeds into the next hit's transient, obscuring the attack and blurring the rhythm. This happens regardless of Mix setting; a low Mix still allows tails to accumulate if Time is long enough relative to the pattern tempo.

**Fix:** Shorten Time before adjusting Mix. The reverb tail should decay below audibility before the next hit in the pattern arrives. At fast tempos, Time below 10 o'clock often produces the most rhythmically clean results. If the reverb sounds effective at slow tempos but muddy at fast ones, Time is the variable — not Mix.

---

### "I patched an envelope into Mix CV but it is not doing what I expected"

The Mix CV input adds to the knob position rather than replacing it, and its range is 0V to 5V unipolar. If the Mix knob is not at fully CCW, the CV is adding to a non-zero floor: a +2V envelope with the knob at 12 o'clock pushes the mix wetter than 12 o'clock, but cannot pull it drier than 12 o'clock. The CV cannot subtract from the knob; it can only add to it. Additionally, if the CV source is bipolar (going negative), the negative portion has no effect — only 0V to 5V influences Mix.

**Fix:** Set the Mix knob to fully CCW to allow the CV to control the full range from dry to wet. Confirm the CV source is unipolar (0V to 5V) or use only the positive portion of a bipolar source. Zadar envelopes default to 0-5V positive output and are directly compatible with the Mix CV input without attenuation or offset.

---

### "I patched OUT L and OUT R to MixUp CH1 and CH2 separately but the stereo image collapsed"

MixUp CH1 and CH2 are mono inputs. Patching a stereo reverb's left and right outputs to two separate mono channels does not preserve the stereo image — each channel sums independently to the mono bus, and the stereo spread of the reverb tail is lost. Verb's stereo output requires a stereo destination to function as designed.

**Fix:** Route Verb OUT L and OUT R to MixUp CH3 L and CH3 R. Channel 3 is the stereo channel on the MixUp and accepts a stereo signal correctly. The reverb's left-right information is preserved through CH3 to the main mix output.

---

### "I patched a signal to both IN L and IN R expecting independent reverb processing per channel"

Verb processes a stereo pair through one shared reverb algorithm, not two independent reverbs. Patching two different mono sources to IN L and IN R does not give each source its own reverb treatment. IN R breaks the IN L normal so that IN L emits only from OUT L and IN R emits only from OUT R, but the reverb algorithm processes both inputs together. Two different sources entering Verb simultaneously will produce combined reverb output, not independent per-channel processing.

**Fix:** For independent reverb on two sources, two reverb modules are required. For a single mono source, patch only IN L and allow the normal to produce stereo output. For a stereo source (left and right channels of the same signal), use both inputs as intended.

---

## Annotated Learning Path

**Entry point:** Patch a single audio source into IN L, route OUT L and OUT R to MixUp CH3 L and R, and sweep Time from fully CCW to fully CW slowly while the source plays. Stop at several positions and listen to how the reverb character changes: the very short end produces ambience; the middle range produces room and chamber character; the long end produces hall and wash. Locate the range where Time produces reverb that complements the current source without extending obviously beyond it.

**Step 2:** With Time set to a working position, sweep Damp from fully CCW to fully CW. Listen to the transition from dark and absorbed to bright and plate-like. Identify where the reverb changes from sounding like a room to sounding like a plate; that transition point is different for every source and every Time setting. Knowing the Damp range matters more than memorizing what a given knob position sounds like in abstract.

**Step 3:** Try Damp fully CW on a percussive source and listen to what plate reverb character actually contributes to that sound. Compare the same source with Damp fully CCW. The two positions are different reverb characters, not just tonal variations on one character. This step is most productive on snare or a similar transient-forward voice.

**Step 4:** Set the Mix knob to fully CCW and patch a Zadar envelope (set to a short rise and medium decay) into the Mix CV input. Trigger the envelope from the same gate source driving the voice. Listen to the difference between this automated blend and a fixed Mix knob: the dry transient arrives before the reverb opens, which is a fundamentally different spatial result from having the reverb present at the moment of impact.

**Step 5:** Move Verb into a melodic patch — a slow pad or sustained oscillator voice — and push Time toward 2 to 3 o'clock with Mix high. Listen to how the same algorithm that produced tight drum room at short Time settings becomes a spatial wash at long settings. Verb does not change behavior based on source type; the source type determines how useful each setting range is.

**Step 6:** Experiment with fully wet Mix on a melodic source and use Damp to shape the tone of the reverb tail as the primary timbral control. With no dry signal present, Damp becomes the dominant spectral shaping tool — pulling it toward CCW shifts the wash darker; CW shifts it brighter. This use treats Verb as a processing tool rather than a spatial effect, and requires source material with enough harmonic content to produce a rich reverb tail at fully wet settings.

---

## Patches Well With

- **vpme.de QD** — Percussion voices are the primary use case for Verb in this system; QD's individual voice outputs allow Verb to process a specific drum voice independently rather than treating the full mix, giving each voice its own spatial placement.
- **Xaoc Devices Zadar** — Four-channel envelope generator with 0V to 5V positive output directly compatible with Verb's Mix CV input; Zadar's wide variety of attack and decay shapes makes Mix CV automation musically varied rather than limited to standard ADSR shapes.
- **2HP Swarm** — Swarm's mono supersaw output feeds Verb IN L for stereo reverb treatment; the harmonic density of a multi-voice detuned oscillator produces a richer reverb tail than simple waveforms at the same Time and Damp settings.
- **Intellijel MixUp** — Direct downstream destination for Verb's stereo output; Verb OUT L and OUT R route to MixUp CH3 L and R for correct stereo handling in the main mix.
