---
title: 2HP Swarm
manufacturer: 2HP
primary_role: SOURCE
secondary_roles: []
form_factor: eurorack
functions: [oscillator]
behavior_tags: [harmonic, bright, warm, sustained, stable, linear]
use_cases: [harmonic pad, drone foundation, sustained pad]
hp: 2
memory: none
transport: none
screen: false
hybrid: false
cv: full
---

![2HP Swarm](https://github.com/Shadoe-42/music/raw/main/modular/images/2hp/swarm/front_panel.jpg)

# 2HP Swarm

Swarm is a hyper oscillator that stacks up to 88 simultaneous detuned saw waves, or up to 55 detuned pulse waves, into a single summed audio output. Three knobs control Voices, Detune, and Freq. Each has a dedicated CV input. A toggle switches between sawtooth and pulse waveforms. The V/Oct input tracks pitch across all active voices simultaneously. Swarm produces the dense, detuned unison character of a supersaw at any voice count from 1 to maximum, with Detune scaling from precise chorus to full spectral chaos.

---

## Historical Context

Detuning multiple voices to the same pitch has been a deliberate instrument design strategy for centuries. Pipe organ builders discovered early that tuning two pipes to the same note and allowing them to drift slightly against each other produced a richer, more sustained tone than either pipe alone. The Voix Céleste stop, meaning "heavenly voice," paired a slightly flat rank of pipes against a standard tuned rank. The acoustical beating between them created the slow, shimmering tremulant character that defined the Romantic organ sound from the nineteenth century onward. The principle was simple: two slightly wrong notes combine into one more interesting right note.

The same principle moved into electronic instruments without changing its fundamentals. String machines of the 1970s — the Eminent 310 Unique, the ARP String Ensemble, the Solina — used divide-down oscillator technology that generated all pitches from a single master oscillator. Their characteristic richness came not from multiple discrete oscillators but from analog ensemble circuits built around bucket brigade device chips. These circuits copied the signal through slightly different delay times and summed the results, producing apparent detuning from a single source. The Eminent 310 reached its most famous application through David Gilmour and Richard Wright, whose "Shine On You Crazy Diamond" opening built its entire harmonic world from the ensemble circuit's shimmering output. Players were reaching for the sound of the Voix Céleste without knowing they were reaching for the same thing.

Discrete detuned oscillators became practical at the synthesizer level as digital polyphony matured. Roland's 1996 JP-8000 synthesizer made the architecture explicit and gave it a name: Super Saw. The JP-8000's Super Saw oscillator ran seven independent sawtooth waves simultaneously, each offset in pitch by an adjustable amount. At narrow detune settings, the seven voices produced the dense, self-reinforcing pad character that defined the sound of trance music through the late 1990s and early 2000s. At wider settings, the voices spread into dissonant spectral clusters. The JP-8000's engineering team had built the Voix Céleste principle into a single oscillator and handed it to producers. The supersaw became the defining texture of an entire era of electronic music — from Ferry Corsten to early Daft Punk to the melodic trance sound that followed, all of it built on Roland's seven detuned saws summed at the output stage.

Hardware supersaw implementations multiplied as digital processing became cheaper. Software synthesizers replicated and extended the architecture. Eurorack module designers compressed it into compact formats, raising the voice count well beyond the JP-8000's seven. 2HP Swarm extends the JP-8000's original architecture to 88 simultaneous voices in a two-HP panel. The principle has not changed since the pipe organ builders discovered it: controlled imprecision between identical voices produces richness that no single voice can produce alone.

---

## Quick Start

1. Patch a pitch CV source (sequencer or keyboard) into Swarm's V/Oct input.
2. Patch Swarm's audio output into a VCA audio input. Swarm produces continuous audio; a VCA is required to shape amplitude and allow notes to start and stop.
3. Patch an envelope generator's output into the VCA's CV input. Trigger the envelope from the same gate source that is driving your sequence.
4. Patch the VCA output into MixUp CH1.
5. Set Voices to 12 o'clock (approximately 20 voices for saw, proportionally fewer for pulse).
6. Set Detune to 9 o'clock. This is a light chorus amount — enough to hear the characteristic detuned richness without spreading into obvious dissonance.
7. Set Freq to 12 o'clock (center, standard pitch).
8. Verify the waveform toggle is set to sawtooth (left position). Saw is the denser starting point.
9. Play a sequence and adjust Detune slowly upward to hear the character shift from tight chorus through lush unison into spectral chaos as the knob approaches its upper range.
10. Raise Voices toward 3 o'clock to increase density. Back Detune off as voice count increases — more voices at wide detune creates uncontrolled beating. More voices at narrow detune creates wall-of-sound density.

---

## Key Specifications

| Parameter | Value |
|---|---|
| Format | Eurorack |
| Width | 2HP |
| Depth | 45mm |
| +12V | 85mA |
| -12V | 7mA |
| +5V | 0mA |

---

## Essential Parameters

**Voices** controls the number of simultaneous oscillators from 1 at fully CCW to 88 (sawtooth) or 55 (pulse) at fully CW. Center position produces approximately 20 voices. The CV input accepts -5V to +5V and shifts the voice count up or down from the knob position. Low voice counts allow individual detuned voices to be heard as discrete layers. High voice counts merge into a continuous spectral mass where individual oscillators are no longer distinguishable. The character at maximum voices on saw is closer to synthesized string orchestra or noise-adjacent density than to a conventional oscillator sound.

**Detune** controls the pitch spread between active voices. Fully CCW produces no detune — all voices are in unison at the Freq pitch, which sounds like a single oscillator. The first half of the knob range covers tasteful chorus territory: subtle, lush, and musical. The second half becomes increasingly chaotic as voices spread across wider pitch intervals, producing beating, dissonance, and eventually dense spectral noise. The boundary between musical and chaotic is not a cliff; there is a wide usable range in the upper first half and lower second half that is aggressive but still pitched. The CV input accepts -5V to +5V and modulates detune amount dynamically, which allows the detuning character to evolve over time without manual intervention.

**Freq** sets the macro pitch of all active voices simultaneously. The knob adjusts the base pitch across an approximately 8-octave range. The V/Oct input tracks 1V/Oct across the full range, accepting -5V to +5V, which allows Swarm to follow a sequencer or keyboard CV at standard Eurorack pitch tracking. All voices shift together when Freq or V/Oct changes — the individual inter-voice detune relationships remain constant; only the center pitch moves.

**Waveform toggle** selects sawtooth (left) or pulse (right). Saw produces the richer, denser output with more harmonic content and supports up to 88 simultaneous voices. Pulse produces a hollow, buzzing character with a narrower harmonic profile and supports up to 55 voices at maximum. The two waveforms are not interchangeable in character: saw is warm and dense; pulse is hard and cutting. Detuned pulse at high voice counts produces a sound with significantly more aggressive frequency content than the equivalent saw setting. The toggle is a binary control with no intermediate position.

**Audio output** sums all active voices to a single mono output at 10Vpp. Swarm does not produce stereo output internally. Stereo width requires a downstream stereo effect (chorus, reverb, or delay with stereo output) or a dedicated stereo processing module.

---

## Why This Instrument Excels

Swarm does one thing and exposes every dimension of it. The supersaw architecture is not a new idea — Roland made it commercially definitive in 1996 — but Swarm raises the ceiling from seven voices to 88 and gives the voice count its own CV input. This turns what Roland fixed at the hardware level into a modulatable synthesis parameter. The number of detuned voices can be swept in real time by an envelope, an LFO, or a sequencer, which allows the density of the unison to evolve within a patch rather than being set and left.

The two-stage character of the Detune knob is a deliberate design choice that rewards attention. The first half of the range is a precision chorus tool: narrow detune intervals that produce the self-reinforcing pad thickness without audible beating or dissonance. The second half is a spectral instrument: wide detune intervals that produce beating, dissonance, and chaotic interactions between voices. These are not two poles of the same continuum so much as two different behaviors available from the same control. Understanding where the transition point is for the current voice count — and how that transition point shifts as Voices changes — is the core skill Swarm develops.

The 2HP format is a constraint that functions as a design advantage in context. Swarm requires nothing for basic operation except a pitch source and a downstream VCA. It produces a complete, dense, usable voice from three knobs and one toggle. This makes it a slot-efficient way to add supersaw thickness to a small rack, or a reliable voice source in a larger rack when the patch calls for unison density without complexity.

Detuned pulse at high voice counts is the least-discussed mode and the most distinctive. The hollow, hard character of the pulse waveform combined with heavy detuning and high voice count produces a sound with significant presence in upper harmonics: aggressive, buzzing, and abrasive in a way that sits in a mix very differently from the saw mode. It does not replace saw — it is a different instrument sharing the same panel.

---

## Patches

### Patch 1: Long Gate Pad

Slow-attack, slow-release pad from Swarm saw into a filter and delay, shaped by a Zadar evolving envelope.

```
[Hermod+ Pitch CV] ─────────────[C]──────▶ [Swarm V/Oct]
[Hermod+ Gate Out] ─────────────[G]──────▶ [Zadar Trigger CH1]

[Zadar CH1 Env Out] ────────────[C]──────▶ [VCA CV In]
[Swarm Audio Out] ──────────────[A]──────▶ [VCA Audio In]

[VCA Audio Out] ────────────────[A]──────▶ [Moon Phase Filter In]
[Moon Phase Filter Out] ────────[A]──────▶ [Nautilus Left In]
[Nautilus Left Out] ────────────[A]──────▶ [MixUp CH1]

                                            Voices: 12 o'clock (~20 voices)
                                            Detune: 9-10 o'clock (light chorus)
                                            Freq: 12 o'clock (CV controlled)
                                            Waveform: Sawtooth

                                            Zadar CH1: slow attack (2-3 s),
                                            long decay/release, low sustain,
                                            or evolving multi-stage shape
```

**Setup:** Hermod+ provides pitch CV to Swarm V/Oct and a gate to trigger Zadar channel 1. Zadar's envelope output drives the VCA CV, shaping the amplitude of Swarm's audio. The VCA output passes into Moon Phase for tonal filtering, then into Nautilus for delay. Use a long gate from Hermod+ — at minimum 2 seconds, ideally 4 or more — so the Zadar envelope has time to reach sustain and the pad character develops fully. A short gate collapses the pad before it blooms.

**Controls:** With Zadar programmed for slow attack (2 to 3 seconds) and a long decay or sustain, the pad takes time to open. This is intentional: the slow attack allows Swarm's dense unison to fade in rather than transient-attack, which makes the detuning character audible before the full amplitude arrives. Moon Phase in a low-pass configuration rolls off the upper spectral energy from the supersaw, which softens the brightness and makes the pad sit further back in the mix. Nautilus adds spatial depth through delay — Ping Pong or Fade mode at moderate feedback. Keep Detune in the first half of the range; light chorus detune at 20 voices reads as richness rather than spread. Raising Voices toward 2 to 3 o'clock at this detune setting increases density without introducing audible voice separation.

**Result:** A lush, slow-building supersaw pad with filtered warmth and delayed depth. This is the foundational Swarm patch for ambient and atmospheric contexts.

---

### Patch 2: Punchy Stab

High voice count, fast Zadar envelope, Moon Phase filter with resonance — dense supersaw stabs at sequencer rate.

```
[Hermod+ Pitch CV] ─────────────[C]──────▶ [Swarm V/Oct]
[Hermod+ Gate Out] ─────────────[G]──────▶ [Zadar Trigger CH1]

[Zadar CH1 Env Out] ────────────[C]──────▶ [VCA CV In]
[Swarm Audio Out] ──────────────[A]──────▶ [VCA Audio In]

[VCA Audio Out] ────────────────[A]──────▶ [Moon Phase Filter In]
[Moon Phase Filter Out] ────────[A]──────▶ [MixUp CH1]

                                            Voices: 3 o'clock (high density)
                                            Detune: 10-11 o'clock (moderate)
                                            Freq: 12 o'clock (CV controlled)
                                            Waveform: Sawtooth

                                            Zadar CH1: fast attack (<50ms),
                                            short decay (100-300ms),
                                            no sustain, fast release
```

**Setup:** Same routing as Patch 1 but without delay. The patch depends on contrast between a very fast Zadar attack and a short decay: the full amplitude of the high-voice-count Swarm hits immediately, then collapses before the next gate. High Voices at this setting produces wall-of-sound density on the hit. Moon Phase adds tonal shaping — a moderate low-pass cutoff rolls off some of the stab's upper harshness, and a touch of resonance gives the cutoff frequency a slight peak that adds definition to the hit.

**Controls:** Raise Voices toward 3 o'clock — the stab application benefits from density, and the fast envelope means the dense pad never has time to bloom into lush territory; it hits and cuts. Detune in the 10 to 11 o'clock range is more aggressive than the pad patch — slightly wider spread adds a buzzing, layered quality to the stab attack. Moon Phase cutoff frequency is the primary tonal control: too open passes harsh high-frequency content from the detuned saw; too closed loses the impact. Adjust until the stab hits with presence but not harshness. Gate duration from Hermod+ matters: too long defeats the stab character and produces an abrupt pad. Keep gates short — 100 to 200ms — so the Zadar envelope has room to decay before the gate closes.

**Result:** A dense, punchy supersaw stab that hits and clears quickly. The high voice count produces the thick textural impact; the fast Zadar envelope controls the dynamics; Moon Phase shapes the tonality. Sits against a drum pattern in a way the pad configuration does not.

---

### Patch 3: Detune Drift

Zadar slow ramp or triangle into Swarm's Detune CV input, sweeping the detuning character from chorus to chaos and back over a sustained note.

```
[Hermod+ Pitch CV] ─────────────[C]──────▶ [Swarm V/Oct]
[Hermod+ Gate Out] ─────────────[G]──────▶ [Zadar Trigger CH2]

[Zadar CH2 Slow Env Out] ───────[C]──────▶ [Swarm Detune CV]

[Zadar CH1 Env Out] ────────────[C]──────▶ [VCA CV In]
[Swarm Audio Out] ──────────────[A]──────▶ [VCA Audio In]

[VCA Audio Out] ────────────────[A]──────▶ [MixUp CH1]

                                            Voices: 2-3 o'clock (high)
                                            Detune: 9 o'clock (base, CV adds to this)
                                            Freq: 12 o'clock (CV controlled)
                                            Waveform: Sawtooth

                                            Zadar CH2: slow rising shape (8-16 s),
                                            triangle or slow attack/decay
                                            Zadar CH1: sustain envelope for VCA
```

**Setup:** Zadar channel 2 provides a slow-moving voltage to Swarm's Detune CV input. Set Zadar CH2 to a triangle or slow rising shape with a long cycle — 8 to 16 seconds allows the detune sweep to move through its full range slowly enough to be musical rather than a rapid modulation effect. Zadar CH1 provides a sustained envelope to the VCA to hold the note open for the full duration of the detune sweep. Set the Detune knob to 9 o'clock as the base position; the CV sweeps upward from there into the second half of the Detune range and back.

**Controls:** With the base Detune at 9 o'clock and the Zadar CV sweeping up to +5V, the Detune parameter moves from light chorus territory through the first half of its range and into the second half's chaotic register. The result is a drone that starts controlled — lush unison chorus — and slowly loses cohesion as voices spread apart, then resolves back as the CV returns to zero. High voice count (Voices at 2 to 3 o'clock) is essential for this patch: at low voice counts the detune spread is audible as discrete pitch separation; at high voice counts the spread merges into a mass of activity that sounds like spectral rather than tonal change. A gate from Hermod+ triggers both Zadar channels; a long gate or sustained gate holds the note for the full sweep.

**Result:** A slowly evolving drone that moves through different detuning characters over time — from tight chorus richness to open, beating chaos — driven entirely by CV modulation of Detune. Demonstrates Detune CV as a musical parameter rather than a set-and-forget control.

---

### Patch 4: Spectral Supersaw via Aurora

Swarm saw into Aurora at FFT 4096 for a spectrally blurred pad with reverb tail that reflects the harmonic density of the supersaw input.

```
[Hermod+ Pitch CV] ─────────────[C]──────▶ [Swarm V/Oct]
[Hermod+ Gate Out] ─────────────[G]──────▶ [Zadar Trigger CH1]
[Hermod+ Pitch CV] ─────────────[C]──────▶ [Aurora Warp CV]

[Zadar CH1 Env Out] ────────────[C]──────▶ [VCA CV In]
[Swarm Audio Out] ──────────────[A]──────▶ [VCA Audio In]

[VCA Audio Out] ────────────────[A]──────▶ [Aurora Left In]

[Aurora Left Out] ──────────────[A]──────▶ [MixUp CH3 L]
[Aurora Right Out] ─────────────[A]──────▶ [MixUp CH3 R]

                                            Voices: 12 o'clock (~20 voices)
                                            Detune: 9 o'clock (light chorus)
                                            Freq: 12 o'clock (CV controlled)
                                            Waveform: Sawtooth

                                            FFT Size: 4096 (blue)
                                            Warp: 12 o'clock (CV active)
                                            Time: 2 o'clock
                                            Blur: 9 o'clock (minimal)
                                            Mix: 10-11 o'clock
                                            Atmosphere: 12 o'clock
```

**Setup:** Hermod+ pitch CV drives both Swarm V/Oct and Aurora's Warp CV input. Aurora processes only one pitch source at a time through Warp; sending the same pitch CV that drives Swarm ensures that any pitch-shifted spectral content from Warp tracks the melody. Patching only Aurora's left input normals the mono Swarm signal to both channels, producing stereo output at CH3 L and R.

**Controls:** The supersaw is a harmonically dense input: multiple detuned voices feeding Aurora's FFT analysis produces a richer spectral field than a sine or simple saw wave would. Keep Voices at approximately 20 (center) and Detune light for this patch — Aurora's Time blurring will add its own form of spectral richness; the Swarm input does not need to be at maximum density. Time at 2 o'clock provides reverb-like amplitude blurring with a long tail. Keep Blur low (9 o'clock or below) to avoid adding frequency-domain artifacts to the already complex supersaw harmonic content — Blur interacts with Swarm's harmonics in ways that become uncontrolled quickly. Mix at 10 to 11 o'clock preserves enough dry signal to hear the pad's attack before the reverb tail takes over. With Hermod+ pitch CV at Warp, Aurora's spectral output tracks the sequence, reinforcing the harmonic relationship between the dry pad and the spectral reverb.

**Result:** A stereo spectral reverb pad built from a supersaw source, with Aurora's frequency-domain blurring amplifying the harmonic complexity of the detuned input and Warp CV tying the spectral field to the sequence pitch.

---

## Common Mistakes

### "I never go past halfway on Detune — the upper range sounds chaotic and unusable"

The first half of the Detune range is precision chorus territory and the second half is deliberately chaotic. Stopping at the midpoint misses half the module. The second half's beating and dissonance is intentional design territory, not a warning zone. The usable range of the second half depends on voice count and context: at lower voice counts the individual intervals are more audible and the chaos is more dissonant; at high voice counts the same detune spread merges into spectral mass rather than obvious dissonance.

**Fix:** Explore the full Detune range at different Voices settings before deciding the upper half is not useful. At high voice counts, the upper half of Detune produces spectral density rather than obvious pitched dissonance. The chaos is real; the question is whether it is the right sound for the current context. Explore this territory systematically, with voice count as the primary control over whether chaos reads as spectral texture or as dissonant interference.

---

### "I switched from saw to pulse and now everything sounds wrong — I had to dial in from scratch"

The pulse switch produces a fundamentally different character, not a slightly different version of the saw sound. Pulse at high voice counts with heavy detune is harder, more aggressive, and occupies the frequency spectrum differently than saw under the same conditions. The two waveforms need different Detune and Voices settings to produce comparable density impressions. The toggle is a choice between two distinct instruments sharing the same panel, not a tonal variation on a single instrument.

**Fix:** When switching to pulse, treat it as a fresh start rather than a copy of the saw settings. Pulse generally benefits from less Detune than saw to achieve a similar chorus density impression, because the narrower harmonic profile interacts with detuning differently than saw's richer spectrum. Start from center Voices and 9 o'clock Detune as a neutral point and build from there.

---

### "I patched Swarm into my mixer but I cannot control when notes start or stop — the volume does not respond to gates at all"

Swarm produces continuous audio output. There is no built-in VCA, envelope, or amplitude control. Patching Swarm directly to a mixer channel means the audio is always present at full amplitude with no dynamics. Every Swarm patch needs an external VCA in the signal path with an envelope generator driving the VCA CV. The gate from the sequencer triggers the envelope; the envelope shapes the VCA; the VCA controls when the Swarm audio is heard.

**Fix:** Insert a VCA between Swarm's audio output and the mixer. Drive the VCA's CV input from an envelope generator triggered by the same gate source driving the pitch sequence. This is the minimum required infrastructure for any Swarm patch that needs musical dynamics. A Swarm patch without a VCA is a drone, not a voice.

---

### "I set Voices and Detune both to maximum and now it just sounds like noise — I cannot find a useful setting from here"

Maximum voices at maximum detune produces spectral noise: dense, chaotic, and difficult to place in a pitched musical context. This is not a malfunction; it is a specific sound that results from 88 voices spreading across the widest possible pitch intervals. The two controls interact strongly — high voice count at narrow detune produces wall-of-sound density; high voice count at wide detune produces spectral mass. Most musical applications live in the interaction between them, not at the extremes of both simultaneously.

**Fix:** Set voice count first based on the desired density impression, then adjust Detune to the appropriate spread for that density. As voice count increases, less Detune is required to achieve a given richness. A useful reference point: at center Voices (approximately 20 voices), the boundary between chorus and chaos is around 11 o'clock on Detune. At high Voices (3 o'clock), that boundary moves earlier. Work from voice count toward detune, not from both extremes simultaneously.

---

### "Swarm sounds static once I dial in a setting — it just sits there and does not change"

A fixed Detune knob position is only one dimension of what Swarm can produce. The Detune CV input accepts -5V to +5V and shifts the detuning character dynamically from whatever the knob sets. A slow LFO or envelope into Detune CV moves the sound through the chorus range and into chaos over time, turning a fixed texture into an evolving one. The Voices CV input does the same for voice count. Swarm with both parameters modulated behaves like a different instrument from Swarm with both fixed.

**Fix:** Patch a slow-moving modulation source (Zadar envelope, LFO, or slow function generator) into the Detune CV input and set a long cycle time — 8 to 16 seconds for a gradual sweep. Listen to how the character evolves as the CV moves through the Detune range. Modulating Detune CV is the primary tool for making Swarm sounds feel alive rather than static.

---

## Advanced Learning Path

**Entry point:** Set Voices to center, Detune to 9 o'clock, waveform to saw. Patch a steady pitch CV source and a sustained gate through a VCA to MixUp. Listen to the baseline character of 20-voice detuned saw. Adjust Detune slowly clockwise and stop every 10 degrees to hear the transition through the chorus range and into the chaotic range. Locate the point where the character changes from musical to dissonant; that boundary is the primary usable range of the module.

**Step 2:** While holding Voices and pitch constant, sweep Detune through its full range from fully CCW to fully CW. Do this slowly enough to hear each stage. Identify the three zones: unison (fully CCW), chorus (first half), chaos (second half). These zones shift as Voices changes; repeat the sweep at low Voices (9 o'clock) and high Voices (3 o'clock) to hear how voice count affects the character of each zone.

**Step 3:** Switch the waveform toggle to pulse. With the same Voices and Detune settings, listen to the character shift. Adjust Voices and Detune from scratch to find the pulse mode's usable ranges — they will be different from saw. This establishes pulse as a separate instrument mode rather than a tonal variation.

**Step 4:** Patch a slow envelope or LFO (Zadar at a slow setting) into the Detune CV input. Let it sweep the detune range automatically while a sustained note plays. Adjust the Zadar's rate and shape to slow the sweep to a musical timescale (8 to 16 seconds). This is the foundation of Patch 3 and demonstrates Detune as a modulation target rather than a fixed setting.

**Step 5:** Patch Voices CV from any modulation source — a faster envelope, a stepped sequence, a random voltage from Zadar or another generator. Hear how dynamic voice count changes the density of the pad in real time. A patch that sweeps Voices upward on an envelope attack and downward on the decay creates a swelling, dense attack that opens and then thins as the note fades.

**Step 6:** Route Swarm into Aurora for Patch 4. Hear how the supersaw's dense harmonic content feeds the spectral reverb differently than a simple sine or triangle wave would. Compare Aurora's Time and Blur behavior on a Swarm source versus a single-voice oscillator source. This step establishes Swarm as a source module whose character propagates through downstream processors.

---

## Pairs Well With

- **Xaoc Devices Zadar** — Four independent envelope generators for VCA amplitude and Detune CV modulation; Zadar's wide variety of envelope shapes produces pad behaviors that a simple ADSR cannot approach, and its slow-moving outputs make Detune CV modulation musically viable.
- **Qu-Bit Aurora** — Aurora's spectral reverb responds to Swarm's harmonically dense supersaw input with a richer spectral field than simpler sources produce; the FFT-domain blurring of a multi-voice detuned saw extends the pad character into frequency-domain territory the VCA and filter alone cannot reach.
- **Instruo Moon Phase** — Filter shaping of Swarm's dense saw output; Moon Phase downstream of the VCA controls the tonal character of the pad or stab and adds stereo processing that Swarm's mono output does not produce natively.
- **Squarp Hermod+** — Pitch and gate sequencing for Swarm voice control; Hermod+ provides the structured pitch information that makes Swarm's detuned unison sound melodically intentional rather than textural noise.
