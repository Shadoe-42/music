---
title: "Qu-Bit Electronix Nautilus"
manufacturer: "Qu-Bit Electronix"
module: "Nautilus"
format: "Eurorack"
type: "Complex Delay Network"
tags: ["delay", "stereo", "feedback", "shimmer", "reverb", "cv-generator", "intermediate", "advanced"]
roles: ["sound-designer", "ambient-artist", "experimental", "producer"]
hc: true
---

![Qu-Bit Electronix Nautilus](../images/qubit_nautilus.jpg)

# Qu-Bit Electronix Nautilus

Nautilus is a stereo complex delay network built on eight configurable delay lines, four per channel, each capable of up to 20 seconds of audio. Clock-synced or free-running, the delay lines can be spread, reversed, and filtered independently within the feedback path. Sensors controls how many delay lines are active. Dispersal sets the spacing between them. Reversal selects which lines play backward. Chroma applies one of six effects inside the feedback path, with Depth controlling the amount. Four Delay modes and four Feedback modes change the fundamental topology of the network. The Sonar output generates an algorithmically derived CV or gate signal from the delay state, turning the delay network into a modulation source.

---

## Historical Context

In Kingston, Jamaica in the 1950s, outdoor dances were powered by traveling sound systems: amplifiers, speaker stacks, and record collections hauled between neighborhoods and competed against one another for crowd approval. The selectors who ran these systems were judged not only by their music but by the quality of their sound — the weight of the bass, the clarity of the highs, and eventually the effects applied live to the records. Echo and reverb were not studio finishing touches in this context. They were weapons.

Osbourne Ruddock, who worked under the name King Tubby, grew up in Kingston and taught himself electronics by repairing radios and televisions. He built his own hi-fi amplifiers, assembled his own sound system, and eventually began working as an engineer in Jamaica's recording industry. What distinguished him was not simply technical skill but a particular musical instinct: he understood that the echo return from a tape delay machine was not decoration but melody, and that the feedback path was not noise but drama. Working from his own studio on Dromilly Avenue, and in collaboration with producers including Lee "Scratch" Perry and Augustus Pablo, Tubby began treating the mixing board as an instrument. Tracks were cut as dub plates — instrumental versions stripped of vocals — and then remixed live at the board, with channels dropped in and out, echo returns pushed up as lead lines, and feedback allowed to build and dissolve. The result was dub: a genre defined not by what was added but by what was removed, and by the space that echo filled when it was gone.

The technology underlying this work was the tape echo machine. Magnetic tape looped past a series of playback heads at staggered positions produced repeats at intervals determined by the tape speed and the distance between heads. Slowing the tape stretched the delay time and introduced pitch drift. Running the echo return back into the input built feedback loops that could sustain indefinitely or collapse into noise. By the mid-1970s, the Bucket Brigade Device — a string of capacitor stages through which audio passed like water through a chain of buckets — moved analog delay out of studios and into instruments: the Roland Space Echo RE-201 became one of the defining sounds of dub production. Each BBD stage introduced a small amount of noise and degradation, giving the repeats a warmth and density that engineers either fought against or exploited. King Tubby exploited it.

Digital delay arrived in the 1980s and removed the degradation. Repeats became clean replicas of the input, capable of looping indefinitely without accumulating noise. What was gained in fidelity was lost in character: the feedback path that had given dub its physical texture became transparent. Nautilus approaches delay from a different direction than either tape or BBD. Rather than a single delay line with a feedback knob, it is a network of eight independently configurable lines that interact through topology. The complexity that King Tubby generated through instinct and hardware limitation, Nautilus generates through architecture — a structured system for building the kinds of layered, intersecting delay relationships that dub producers discovered by accident.

---

## Quick Start

1. Patch a sound source into Nautilus's left audio input. The left input normals to both channels when the right input is unpatched.
2. Patch Nautilus's left and right outputs to MixUp CH3 L and CH3 R.
3. Set Mix to 12 o'clock. Set Feedback to 9 o'clock (moderate repeats, not infinite). Set Sensors to minimum (CCW, one delay line per channel).
4. Tap the Clock button twice at the tempo of your patch. Nautilus establishes its internal clock from at least two taps. The Kelp LEDs pulse at the established rate.
5. Set Resolution to the quarter-note position (12 o'clock). This syncs the delay time to one beat of the tapped tempo.
6. Listen to the delay repeat once per beat. Raise Feedback to extend the echo trail. Stay below the fully-CW position to avoid infinite accumulation.
7. Raise Sensors to add a second delay line. The two delay lines fire in close succession by default. Raise Dispersal to open the spacing between them.
8. Try each Delay mode using the Delay mode button: Fade (blue, crossfades delay time changes), Doppler (green, pitch shifts on time changes), Shimmer (orange, one octave above input), De-Shimmer (purple, one octave below).
9. Try each Feedback mode using the Feedback mode button: Normal (blue, stereo follows input), Ping Pong (green, bounces between channels), Cascade (orange, delay lines feed each other in series), Adrift (purple, lines feed across stereo channels).
10. For external clock sync, patch a gate signal from your sequencer or clock source into the Clock In input instead of using Tap Tempo.

---

## Key Specs

| Parameter | Value |
|---|---|
| Format | Eurorack |
| Width | 14HP |
| Depth | 22mm |
| +12V | 151mA |
| -12V | 6mA |
| +5V | 0mA |
| Price (MSRP) | $399 |

---

## Essential Parameters

**Mix** blends dry and wet signal. Fully CCW is dry only. Fully CW is wet only. The mix curve is adjustable via the Narwhal configurator (linear, constant power, transition, or wet-amount-only modes).

**Clock In / Tap Tempo** establishes the time base for all delay lines. Tap the button at least twice to set an internal tempo. Patch a gate signal to the Clock In input to sync externally. The default internal rate at boot is 120bpm. Clock range spans 0.25Hz (4 seconds per beat) to 1kHz (1 millisecond per beat).

**Resolution** divides or multiplies the clock rate and applies the result as the delay time. The range covers 16 settings from 2-bar delays down to 512th-note divisions. At moderate Sensor counts, different Resolution settings produce rhythmically varied echo patterns from the same clock source. A secondary function (Tap+Resolution) adds a tail reverb to both dry and wet signals, with fully CW producing maximum reverb length.

**Feedback** controls how long the delay repeats. Fully CCW produces one repeat. Fully CW produces infinite self-sustaining feedback. The Feedback attenuverter modulates the Feedback CV input: fully CW is unattenuated, 12 o'clock is fully attenuated, fully CCW is fully inverted. The attenuverter can be reassigned to any CV input via the configurator.

**Sensors** sets how many delay lines are active per channel. Minimum (fully CCW) activates one line per channel, two total. Maximum (fully CW) activates four lines per channel, eight total. Adding Sensors with Dispersal at minimum produces delay lines firing in tight succession. Adding Dispersal opens the spacing. In Cascade and Adrift modes, Sensors also controls which delay line outputs are sent to the wet signal.

**Dispersal** adjusts the spacing between active delay lines. With one Sensor active, Dispersal offsets the left and right channel delay frequencies independently, functioning as fine-tuning for stereo imaging. With multiple Sensors active, Dispersal spaces the lines apart from near-simultaneous into distinct rhythmic separations. The Dispersal attenuverter behaves identically to the Feedback attenuverter and is reassignable.

**Reversal** determines which delay lines play backward. With one Sensor active, the range covers no reversal, left-channel reversal, and both-channel reversal. With more Sensors active, Reversal incrementally reverses each line in the order: first left, first right, second left, second right, and so on. Reversed lines remain reversed until the knob returns below their threshold position.

**Chroma** selects which internal effect is applied within the feedback path. Six options, each indicated by a Kelp base LED color: Oceanic Absorption (blue, 4-pole lowpass filter), White Water (green, 4-pole highpass filter), Refraction Interference (purple, bit-crushing and sample-rate reduction), Pulse Amplification (orange, soft saturation), Receptor Malfunction (cyan, wavefolder), SOS (red, heavy distortion). Each effect is applied independently to individual delay lines, allowing different lines to carry different Chroma characters simultaneously as they pass through the feedback path.

**Depth** controls the amount of the selected Chroma effect. Fully CCW is no effect. Fully CW is maximum. The exception is Refraction Interference, which selects from a fixed set of bit-crushing and sample-rate configurations rather than a continuous amount. The Kelp LEDs shift toward the Chroma effect color as Depth increases.

**Delay Modes** (button, four options): Fade (crossfades between delay times when Resolution or clock changes — smooth transitions), Doppler (vari-speed pitch shift on time changes — classic tape-effect pitch bend), Shimmer (pitch shifts the delay up one octave, rising further with each feedback pass), De-Shimmer (pitch shifts the delay down one octave, descending with each pass). Shimmer and De-Shimmer transposition intervals are adjustable in semitone steps via the configurator.

**Feedback Modes** (button, four options): Normal (delay stays in the stereo position of the input signal), Ping Pong (delay bounces between left and right channels, width relative to input stereo position), Cascade (delay lines feed into each other in series, capable of up to 80-second delays), Adrift (lines feed across stereo channels alternately, producing unpredictable spatial movement). Summed Mono mode (Tap+Feedback Mode button) sums the dry signal to mono while keeping the wet signal stereo — necessary for guitar-style Ping Pong from a mono source.

**Freeze** (button and gate input, threshold 0.4V) locks the current delay buffer and holds it as a beat-repeat machine. While frozen, Resolution changes rearrange the frozen buffer rhythmically in sync with the clock. Freeze behavior is configurable: normal (Mix knob unchanged), punch-in (forces full wet when Mix is dry), always-wet (forces full wet regardless). Quantize Freeze (configurable) delays activation to the next clock pulse rather than engaging immediately.

**Purge** (button and gate input, threshold 0.4V) clears all delay lines from the wet signal. Continuous Purge mode (configurable) keeps the lines cleared for as long as the button is held or the gate is high.

**Sonar** (CV output, 0V to +5V) generates signals algorithmically derived from Nautilus's delay state. Three configurable modes: Stepped Voltage (additive CV sequence built from overlapping delay analysis — default), Variable Clock (clock output derived from Resolution rate), Master Clock (passes the Clock In signal through). In Stepped Voltage mode, Sonar creates an ever-changing sequence that reflects the current delay topology and can be used to modulate other modules or self-patch Nautilus.

---

## Why This Excels

The essential difference between Nautilus and a conventional delay module is the network architecture. A standard delay has one time, one feedback amount, and one output. Nautilus has eight delay lines that can be spaced, reversed, and filtered independently, and whose interactions change based on which Feedback mode is active. Cascade alone can produce delays longer than most modules are capable of by chaining four lines in series per channel. Adrift can produce spatial movement that no static stereo delay can replicate because the routing changes with each feedback pass.

Sensors and Dispersal are the two controls that define the character of the delay network, and they operate orthogonally. Sensors determines density: how many lines are active. Dispersal determines geometry: how far apart they are. Used together, they can produce anything from a tight doubling effect with subtle stereo spread to a wide polyrhythmic cascade of distinct echoes from a single voice. The interaction between these two knobs is where most of Nautilus's core character lives, and it rewards deliberate exploration rather than casual adjustment.

Chroma applies effects inside the feedback path rather than after it. This means the effect accumulates across feedback passes. A small amount of Reversal Interference at low Depth produces subtle degradation that deepens with each repeat, simulating the way BBD or tape repeats accumulated noise over successive passes. A wavefolder in the Receptor Malfunction position at high Depth can turn a simple melodic delay into a harmonically dense spectral accumulation that bears almost no resemblance to the input after several feedback cycles. The temporal scale of this accumulation is determined by Feedback — slower decay gives more time to hear the transformation unfold.

Sonar is the most underused dimension of Nautilus. In Stepped Voltage mode, it produces a CV sequence that is derived from the delay state rather than from any external sequencer or LFO. As the delay network evolves, Sonar's output evolves with it. This means Sonar can modulate parameters inside Nautilus — creating self-reinforcing feedback loops between the delay state and its own CV inputs — or it can drive external modules in ways that are synchronized to the delay activity without being reducible to a simple clock division. It is a gate and CV generator that thinks in delay time, not in note time.

---

## Patches

### Patch 1: Clocked Melodic Delay

Winterbloom Castor and Pollux II into Nautilus in Ping Pong with external clock sync, producing a stereo melodic echo that tracks the patch tempo and expands a single voice into a wide stereo field.

```
[Castor & Pollux II Thru Out] ───────────▶ [Nautilus Left In]
[Hermod+ Clock Out] ─────────────────────▶ [Nautilus Clock In]

                                            Delay Mode: Fade
                                            Feedback Mode: Ping Pong
                                            Resolution: quarter note (12 o'clock)
                                            Feedback: 9-10 o'clock
                                            Sensors: minimum (CCW)
                                            Dispersal: 12 o'clock
                                            Reversal: fully CCW
                                            Mix: 10-11 o'clock
                                            Chroma: none (Depth fully CCW)

[Nautilus Left Out] ─────────────────────▶ [MixUp CH3 L]
[Nautilus Right Out] ────────────────────▶ [MixUp CH3 R]
```

**Setup:** Castor and Pollux II Thru output passes the dry oscillator signal into Nautilus while allowing the signal to continue to other destinations in the patch. Hermod+ clock syncs the delay time to the patch tempo. With one Sensor active and Feedback mode set to Ping Pong, the delay repeats bounce between the left and right channels relative to the input's stereo position.

**Controls:** Resolution at 12 o'clock produces quarter-note repeats. Adjusting Resolution while the patch runs changes the delay time with a smooth crossfade in Fade mode, keeping transitions musical rather than glitchy. Feedback at 9 to 10 o'clock produces 3 to 5 repeats before the trail fades, enough to fill the space between notes without cluttering faster melodic passages. Mix slightly below 12 o'clock preserves enough dry signal for the oscillator voice to retain its presence against the repeats. Lowering Resolution to a dotted quarter or half note slows the bouncing to a wider, more spacious feel. Raising Sensors to 2 and opening Dispersal adds a second echo trail at a different spacing, creating a denser stereo image from the same source.

**Result:** A stereo Ping Pong delay on a melodic oscillator voice, synced to the patch clock, with smooth delay time transitions and controllable repeat density. This is the foundational Nautilus workflow for melodic sources.

---

### Patch 2: Shimmer Cascade on Sustained Voice

Instruo Cs-L sine output into Nautilus in Shimmer and Cascade mode, producing a rising harmonic shimmer that accumulates upward through octaves as the feedback path extends.

```
[Cs-L Sine Out] ─────────────────────────▶ [Nautilus Left In]
[Hermod+ Clock Out] ─────────────────────▶ [Nautilus Clock In]

                                            Delay Mode: Shimmer
                                            Feedback Mode: Cascade
                                            Resolution: dotted half note or longer
                                            Feedback: 10-11 o'clock
                                            Sensors: 2-3 (two to three lines per channel)
                                            Dispersal: 10-11 o'clock
                                            Reversal: fully CCW
                                            Mix: 12-1 o'clock
                                            Chroma: Oceanic Absorption (blue)
                                            Depth: 9-10 o'clock (light lowpass)

[Nautilus Left Out] ─────────────────────▶ [MixUp CH3 L]
[Nautilus Right Out] ────────────────────▶ [MixUp CH3 R]
```

**Setup:** Cs-L sine output provides a clean, harmonically simple voice that gives the shimmer room to build without competing harmonic content. Slow Resolution and Cascade mode combine to create long delay times: in Cascade mode, delay lines feed each other in series, multiplying the base delay length. Each pass through the cascade adds another octave of pitch shift from Shimmer mode.

**Controls:** Resolution at a dotted half note or longer keeps the shimmer from accumulating too quickly. Feedback at 10 to 11 o'clock allows enough passes for the first two octave shifts to become audible before the trail decays. Sensors at 2 to 3 with moderate Dispersal spaces the delay lines enough that each shimmer arrival is distinct rather than smeared. A light lowpass filter via Chroma set to Oceanic Absorption with low Depth rolls off the harshness that accumulates in the upper octaves as the shimmer rises, keeping the shimmer warm rather than bright. Raising Sensors further adds more stages to the cascade and more octaves to the shimmer but also accelerates feedback buildup — monitor Feedback carefully. Lower Mix if the shimmer overwhelms the source voice.

**Result:** A rising octave shimmer built from a sustained sine voice, with Cascade mode extending the delay chain and each pass adding another pitch-shifted layer filtered by Chroma. The shimmer builds and decays in a long arc determined by the Feedback and Resolution settings.

---

### Patch 3: Sonar Self-Patch and External Modulation

Nautilus's Sonar output patched to the Resolution CV input and to an external destination, creating a delay network that modulates its own timing while simultaneously driving another module from its internal state.

```
[Castor & Pollux II Thru Out] ───────────▶ [Nautilus Left In]
[Hermod+ Clock Out] ─────────────────────▶ [Nautilus Clock In]

                                            Delay Mode: Fade
                                            Feedback Mode: Ping Pong
                                            Resolution: 12 o'clock (starting position)
                                            Feedback: 9 o'clock
                                            Sensors: 3
                                            Dispersal: 1 o'clock
                                            Mix: 12 o'clock
                                            Sonar: Stepped Voltage mode (default)

[Nautilus Sonar Out] ────────────────────▶ [Nautilus Resolution CV]
[Nautilus Sonar Out] via mult ───────────▶ [Zadar CH1 CV In]

[Nautilus Left Out] ─────────────────────▶ [MixUp CH3 L]
[Nautilus Right Out] ────────────────────▶ [MixUp CH3 R]
```

**Setup:** Sonar output in Stepped Voltage mode generates a CV sequence derived from the overlapping delay analysis. Patching it back into the Resolution CV input causes the delay timing to change based on the current delay state — the network begins to self-modulate its own time structure. A mult splits Sonar to also drive Zadar CH1 CV input, so the same derived signal modulates an envelope shape elsewhere in the patch.

**Controls:** The Sonar output will immediately begin altering Resolution from its set 12 o'clock position as the delay lines interact. The degree of modulation depends on the current Sensor count and Dispersal setting: with 3 Sensors and open Dispersal, the overlapping delay analysis produces more varied CV output and wider Resolution variation. With the Resolution Attenuverter (if assigned to Resolution CV via configurator), the depth of the self-modulation can be dialed back. The Zadar CV input responds to the same Sonar output, linking an envelope somewhere else in the patch to Nautilus's internal delay state. The result is a patch where delay timing, envelope behavior, and the delay output itself share a common source and evolve together. To reset the feedback loop without Purging the delays, tap a new tempo to override the Resolution drift.

**Result:** A self-modulating delay network where Sonar drives the delay timing and simultaneously outputs to an external modulation destination. The patch evolves based on Nautilus's own internal state rather than any external LFO or sequencer.

---

### Patch 4: Dub-Style Drop and Rebuild

Slow percussive or bass voice into Nautilus in Normal feedback mode with live Chroma and Feedback adjustment, building a dense echo texture and then purging it for rhythmic contrast.

```
[Castor & Pollux II Saw Out] ────────────▶ [Nautilus Left In]
[Hermod+ Clock Out] ─────────────────────▶ [Nautilus Clock In]
[Hermod+ Gate Out] ──────────────────────▶ [Nautilus Purge Gate In]

                                            Delay Mode: Doppler
                                            Feedback Mode: Normal
                                            Resolution: quarter note or dotted eighth
                                            Feedback: 10 o'clock initially
                                            Sensors: 2
                                            Dispersal: 10-11 o'clock
                                            Reversal: fully CCW
                                            Mix: 1-2 o'clock (mostly wet)
                                            Chroma: Pulse Amplification (orange)
                                            Depth: 11 o'clock

[Nautilus Left Out] ─────────────────────▶ [MixUp CH3 L]
[Nautilus Right Out] ────────────────────▶ [MixUp CH3 R]
```

**Setup:** Castor and Pollux II saw output provides a harmonically dense voice suitable for a dub-style texture. Hermod+ gate out drives Nautilus's Purge input, so a programmed gate in the sequence triggers a delay clear at a specific point in the pattern. Doppler mode introduces pitch-drift artifacts when Resolution or clock changes, which adds the slight pitch instability associated with tape delay.

**Controls:** Set Feedback to 10 o'clock and allow the echo to build across several bars. The saw voice through Pulse Amplification at moderate Depth adds soft saturation to each pass, warming the repeats and giving the accumulation a density reminiscent of tape echo color. At a chosen structural point, the Hermod+ gate fires into Purge, clearing all delay lines instantly and creating a moment of silence before the next input phrase enters. After the Purge, the echo rebuilds from the new material. Raise Feedback to 11 o'clock or higher to allow the rebuilding phase to reach higher density before the next Purge. Adjusting Resolution during a build changes the delay time with a Doppler pitch-shift artifact. Bringing Mix down before a Purge and then raising it after creates an additional dynamic contour separate from the Purge itself.

**Result:** A rhythmically structured echo texture with deliberate Purge events that create dub-style drop-and-rebuild dynamics, with Pulse Amplification adding warmth to the feedback accumulation and Doppler mode introducing pitch artifacts on time changes.

---

## Common Mistakes

**"I turned up Sensors but the delay sounds like mush."** Adding delay lines without opening Dispersal keeps all lines firing in near-simultaneous succession. They blend into a smeared cluster rather than distinct echoes. Sensors and Dispersal always operate together: after adding a Sensor, raise Dispersal until the spacing between lines is audible. The right amount depends on Resolution and tempo — at faster clocks, even a small Dispersal increment creates separation.

**"The feedback got out of control and now it is very loud."** Feedback fully CW produces infinite sustain. Without a Purge or a Mix reduction, the accumulated signal has no natural ceiling. The Purge button clears all delay lines immediately. For less drastic recovery, lower Mix first (which does not stop the accumulation but removes it from the output), then lower Feedback, then raise Mix again. Going forward: treat the Purge gate input as a safety valve and keep it accessible in any high-feedback patch.

**"Cascade mode sounds the same as the other feedback modes."** Cascade mode requires multiple Sensors to demonstrate its effect. With one Sensor active, all four feedback modes produce similar results because there is only one delay line per channel to route. Set Sensors to 3 or 4 and moderate Feedback before switching to Cascade. The serial chaining of lines at that point produces delay times that are multiples of the single-line duration — audibly and dramatically longer than Normal or Ping Pong at the same settings.

**"Shimmer keeps getting too high and disappears."** Shimmer mode pitch-shifts the delay up one octave per pass through the feedback path. With high Feedback and fast Resolution, the shimmer rises through audible frequencies and disappears into ultrasonic territory quickly. Two adjustments: lower Feedback to reduce the number of audible passes before decay, and lower Resolution to slow the accumulation rate. A light Oceanic Absorption Chroma filter also rolls off the extreme high content before it exits the audible range.

**"I am not using the Sonar output."** Sonar is a CV generator derived from Nautilus's internal delay analysis. In Stepped Voltage mode, it produces a sequence that changes as the delay network changes. Patched to any CV input — Resolution, Dispersal, Feedback, or an external module — it introduces modulation that is intrinsically linked to the delay state. At minimum, patch Sonar to a destination outside Nautilus and listen to how the delay activity drives something else in the patch. The interaction between the delay output and the Sonar-driven modulation is one of Nautilus's most distinctive capabilities and one of the most overlooked.

---

## Annotated Learning Path

Start with one Sensor, Fade mode, Normal feedback, and a clock from Hermod+. Set Resolution to a quarter note and Feedback to 9 o'clock. This is the simplest state of the delay network: one line per channel, smooth time transitions, moderate decay. Understand the basic delay behavior here before adding complexity.

With the basic delay established, work through the four Resolution positions surrounding 12 o'clock — dotted eighth, quarter, dotted quarter, half note — and listen to how the same Feedback and Sensor settings produce rhythmically distinct results at different resolutions. Resolution is the primary rhythmic control, and its range is wide enough to be the only variable that needs to change across many patches.

Add a second Sensor and explore Dispersal's full range. At minimum Dispersal, the two lines fire nearly together. At maximum, they are separated to the full extent of the current Resolution. The point where the two lines feel like a natural stereo doubling versus two distinct rhythmic events varies by source material. Find that threshold for the voice you are working with.

Try all four Feedback modes with two Sensors active and moderate Dispersal. Normal, Ping Pong, Cascade, and Adrift each produce fundamentally different spatial behavior. Cascade in particular changes the perceived delay time, not just the routing. Spend time in each mode before forming preferences.

Introduce Reversal with three Sensors active. Start with the knob at minimum and raise it slowly. The first reversal (first left channel line) changes the texture noticeably but subtly. The second reversal (first right channel line) creates asymmetry between the stereo channels. By the time multiple lines are reversed, the delay output has a different temporal logic than the forward network. Reversal at intermediate positions — not all forward, not all backward — is where the most useful design space lies.

Patch Sonar to the Resolution CV input and listen to the self-modulation. Then reassign it to Dispersal or Depth and compare. Each destination produces a different character of self-reference because each parameter shapes a different dimension of the network. Sonar into Resolution changes timing. Sonar into Depth changes Chroma intensity. Understanding which destination creates the kind of self-modulation relevant to the current patch requires trying several.

Use the Tap+Resolution secondary function to add end-of-chain reverb and compare the result to patching Nautilus into Aurora. The built-in reverb affects both dry and wet signal, which Aurora does not — it is a different compositional choice rather than a substitute. For patches where Nautilus and Aurora are both available, combining them places the spectral reverb after the delay network, which allows the reverb tail to blur the delay echoes rather than blurring the source before it enters the delay.

---

## Patches Well With

- **Instruo Cs-L** — Complex oscillator providing sustained, harmonically rich tonal material; the Cs-L's wavefolder output enters Nautilus with enough spectral content for Chroma effects to work on, and the sine output provides a clean shimmer source.
- **Winterbloom Castor and Pollux II** — Primary melodic source for Nautilus in the studio; the Thru output passes the signal to Nautilus while keeping the oscillator available elsewhere; the DCO's stable pitch makes Ping Pong and Shimmer delays track reliably.
- **Xaoc Devices Zadar** — Four-channel envelope/function generator for modulating Nautilus CV inputs; Zadar's infinite-repeat mode driving Dispersal or Sensors CV produces slow evolving changes to the delay network geometry; Sonar output into Zadar CV input links the delay state to envelope behavior.
- **Intellijel MixUp** — Downstream stereo destination; Nautilus outputs feed CH3 for the full stereo delay image; Mix and Feedback adjustments on Nautilus complement MixUp's channel attenuation for final level management.
