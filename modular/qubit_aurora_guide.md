---
title: "Qu-Bit Electronix Aurora"
manufacturer: "Qu-Bit Electronix"
module: "Aurora"
format: "Eurorack"
type: "Spectral Reverb"
tags: ["reverb", "spectral", "fft", "pitch-shifting", "freeze", "stereo", "intermediate", "advanced"]
roles: ["sound-designer", "ambient-artist", "experimental", "producer"]
hc: true
---

![Qu-Bit Electronix Aurora][(https://github.com/Shadoe-42/music/raw/main/modular/images/qubit/aurora/front_panel.jpg)]

# Qu-Bit Electronix Aurora

Aurora is a stereo spectral reverb built on a phase vocoder audio engine. It processes audio in the frequency domain rather than the time domain, producing reverb through spectral blurring of amplitude and frequency components. Six knobs control Warp, Time, Blur, Reflect, Mix, and Atmosphere, with CV inputs for each. Freeze and Reverse are gate-controlled. Four FFT sizes change the sonic character from lush and clean to alien and comb-like. The Warp knob tracks 1V/Oct for pitch-shifting within the spectral field.

---

## Historical Context

Jean-Baptiste Joseph Fourier published *Théorie analytique de la chaleur* in 1822 with a claim that still sounds improbable: any periodic function, no matter how complex, can be expressed as an infinite sum of sines and cosines. Applied to sound, this means any waveform can be decomposed into its constituent frequencies, manipulated in the frequency domain, and then reconstructed as audio. For the next century and a half, this remained a mathematical truth with limited practical application. Calculating a Fourier transform by hand was laborious. Calculating one fast enough to process audio in real time was impossible.

That changed in 1965 when James Cooley at IBM and John Tukey at Bell Labs published an algorithm that reduced the computation time for a Fourier transform from O(N²) to O(N log N). The Fast Fourier Transform made frequency-domain audio processing computationally viable. The following year, James Flanagan and R.M. Golden, also at Bell Labs, published the phase vocoder: a system that used overlapping short-time Fourier transforms to analyze, transform, and resynthesize audio. Their application was telephone speech compression. The phase vocoder separated the time and pitch components of a signal, allowing each to be manipulated independently without affecting the other.

Within a decade, musicians and researchers had begun exploring what Fourier decomposition could do beyond speech compression. Time-stretching audio without changing pitch, and pitch-shifting without changing duration, became the headline applications. By the 1980s, the phase vocoder had become a research tool at institutions like IRCAM in Paris, where composers were using it for granular and spectral transformations that had no acoustic equivalent. The commercial software implementations that followed turned spectral time-stretching into a standard studio tool. Every DAW's pitch-correction and time-stretching algorithm today descends directly from Flanagan and Golden's 1966 work.

Aurora is a different application of the same engine. Rather than using the phase vocoder for pitch-shifting or time-stretching, Qu-Bit uses it to generate reverb through spectral blurring. Time blurs the amplitude component of the frequency-domain signal, producing reverb-like decay that continuously responds to the input. Blur smears the frequency component, producing artifacts no acoustic space could generate. The result is a reverb that does not model any physical environment. It models the mathematical structure of sound itself.

---

## Quick Start

1. Patch a sound source into Aurora's left audio input. The left input normals to both channels when the right input is unpatched, so a mono source produces stereo output.
2. Patch Aurora's left and right outputs to MixUp CH3 L and CH3 R.
3. Set Mix to 12 o'clock (equal dry and wet).
4. Raise Time to 2 o'clock. This blurs the amplitude component of the signal and produces a reverb-like tail.
5. Raise Reflect to 11 o'clock. Reflect adds multi-tap delay time zones that extend the tail from the spectral blurring.
6. Adjust Mix to taste. Aurora has a full dry/wet control, so blend is adjustable from fully dry to fully wet.
7. FFT size defaults to 4096 (blue Reverse LED). To change it, hold Shift and press Reverse to cycle through 4096 (blue), 2048 (green), 1024 (cyan), and 512 (purple).
8. Leave Blur fully CCW on first pass. Blur introduces frequency-domain smearing that gets experimental quickly. Add it deliberately once the core reverb character is dialed in.
9. Leave Atmosphere at 12 o'clock (neutral). Moving it below center filters toward spectral whale-song territory; above center adds high-frequency content before giving way to a high-pass filter.
10. Warp at 12 o'clock produces no pitch shift. Patch a 1V/Oct CV source into the Warp CV input to track pitch and harmonize the spectral field with a sequence.

---

## Key Specs

| Parameter | Value |
|---|---|
| Format | Eurorack |
| Width | 12HP |
| Depth | 22mm |
| +12V | 215mA |
| -12V | 6mA |
| +5V | 0mA |
| Price (MSRP) | $379 |

---

## Essential Parameters

**Warp** adjusts frequency-domain pitch shifting from three octaves down to three octaves up. Center (12 o'clock) is no shift. The control tracks 1V/Oct via CV input, which allows Warp to follow a sequencer and turn Aurora into a harmonizing spectral voice. LEDs turn green and blue when Warp is on an exact octave; purple when off an octave.

**Time** blurs the amplitude component of the frequency-domain signal. Fully CCW is minimal blur. Fully CW is full amplitude blurring. The result sounds like a traditional reverb decay but responds continuously to the live input rather than producing a fixed tail from a trigger event. Time is the primary reverb control and the first knob to reach for when building a spectral reverb sound.

**Blur** smears the frequency component of the signal. Fully CCW is no blur. Fully CW is full frequency smearing. Where Time produces results that sound musical and decay-like, Blur produces alien artifacts: digitally stretched spectral effects with no acoustic reference. These two controls are distinct and operate on different axes of the spectral field.

**Reflect** morphs between different multi-tap delay time zones. Fully CCW adds no delay. Increasing the control moves through time zones from short early reflections to longer rhythmic combinations. Each stereo output receives complementary delay lengths. In combination with Time and Blur, Reflect can create extremely long reverb tails from short input transients.

**Mix** blends dry and wet signal. Fully CCW is dry only. Fully CW is wet only. This is a standard wet/dry control, unlike some Qu-Bit processors that output fully wet signals.

**Atmosphere** controls a combination of spectral and time-domain filters. Center is neutral. Below center filters toward lower frequencies, producing spectral artifacts described as whale songs and underwater textures. Above center adds high-frequency content for icy shimmer before giving way to a high-pass filter that carves out space for busier sources.

**Freeze** (button + gate input, threshold 0.4V) locks the current spectral characteristics of the input signal and sustains them until deactivated. While frozen, Warp, Time, Blur, Atmosphere, and Mix remain active. Freeze captures a spectral snapshot that can then be reshaped in real time. Gate input allows sequencer or envelope control.

**Reverse** (button + gate input, threshold 0.4V) plays the input signal backward. The LED pulse direction reverses as a visual indicator.

**FFT Size** (Shift + Reverse) cycles through four settings: 4096 (blue, lush and clean, ideal for pads and physical modeling voices), 2048 (green, balanced), 1024 (cyan, comb-like timbres, suits drum voices and simple waveforms), 512 (purple, alien character with low spectral resolution, suits drums and vocal sources for extreme effects).

**Stereo Width** (Shift + Reflect) adjusts the wet signal's stereo enhancement from 0 to 100%. Default is 75% (blue LEDs). Fully CW maximizes stereo spread.

**Input Level** (Shift + Mix) adjusts Aurora's internal audio input level from -6dB to +12dB. Default is 1x (blue LEDs). Raising input level allows line-level sources to patch directly. This control matters: Aurora's spectral processing responds to the relative amplitude of the input, and an undergained signal will produce a thin spectral field.

---

## Why This Excels

Aurora produces reverb that no acoustic space can produce. Convolution reverbs model physical rooms by convolving the input with an impulse response. Algorithmic reverbs approximate room behavior through tuned delay networks and feedback. Aurora blurs the signal in the frequency domain, which means the reverb is derived from the mathematical structure of the input itself rather than from any acoustic model. Inputs with rich harmonic content produce harmonically rich reverbs. Inputs with sparse frequency content produce sparse reverbs. The reverb is a transformation of what is actually in the signal.

The two axes of spectral blurring give Aurora a wider range than most reverbs. Time produces results that sit in a mix the way a hall reverb would. Blur produces results that do not sit in a mix at all because they were not designed to. Moving Blur up while Time remains at a working reverb setting shifts Aurora from a mix tool into a sound design instrument. These two axes can be dialed independently or combined, and the FFT size changes the character of both.

Warp's 1V/Oct tracking is what separates Aurora from other reverb modules in a typical rack. A sequencer driving the Warp CV turns Aurora into a second harmonic voice that tracks the patch's pitch information. The reverb tail follows the melody rather than sitting beneath it. Freeze captures a spectral moment and holds it while Warp shifts the pitch of the frozen content, which allows a single frozen chord or pad texture to be transposed in real time.

The Atmosphere control adds a filter dimension that most reverbs do not include. The whale-song territory below center produces textures that function more as pads than reverbs. Above center, the high-pass character allows Aurora to add shimmer to dense mixes without adding low-frequency mud. These filter behaviors interact with the spectral blurring, so Atmosphere is not a post-processing EQ; it shapes the spectral field itself.

---

## Patches

### Patch 1: Long Hall Reverb on Bass

Spectral hall reverb on a bass voice, using Time and Reflect for long, smooth decay without frequency-domain artifacts.

```
[Cs-L Sine Out] ─────────────────────────▶ [Aurora Left In]

                                            FFT Size: 4096 (blue)
                                            Warp: 12 o'clock (no shift)
                                            Time: 2-3 o'clock
                                            Blur: fully CCW
                                            Reflect: 11 o'clock
                                            Mix: 10-11 o'clock
                                            Atmosphere: 12 o'clock

[Aurora Left Out] ───────────────────────▶ [MixUp CH3 L]
[Aurora Right Out] ──────────────────────▶ [MixUp CH3 R]
```

**Setup:** Cs-L sine output provides a clean bass voice with strong fundamental and minimal high-frequency content. Patching only the left input normals the signal to both channels, producing stereo spectral output from a mono source. FFT size 4096 provides the cleanest spectral response with the most accurate frequency representation and the longest latency, which suits sustained bass lines well.

**Controls:** Time at 2 to 3 o'clock produces long amplitude blurring that extends the decay of each note far beyond its natural sustain. Reflect at 11 o'clock adds an early-reflection time zone that fills the space between note events without introducing obvious rhythm. Mix at 10 to 11 o'clock blends enough dry signal to preserve the attack and body of the bass voice while the spectral tail spreads beneath it. Keep Blur fully CCW for this patch: frequency blurring on a bass voice adds inharmonic content that muddies the low end quickly. Atmosphere at center passes the signal without spectral filtering. Lower Reflect if the reverb tail becomes rhythmically distracting.

**Result:** A sustained spectral hall reverb on a bass voice, with long amplitude-blurred tails that preserve the harmonic character of the source without adding frequency-domain artifacts. This is Aurora's foundational use case for bass and melodic voices.

---

### Patch 2: Sequenced Warp Shimmer

High melodic voice into Aurora with a sequencer driving Warp at 1V/Oct, producing pitch-shifting spectral shimmer that tracks the melody.

```
[Chord V2 Seventh Out] ──────────────────▶ [Aurora Left In]
[Hermod+ CV Out (Track 2)] ──────────────▶ [Aurora Warp CV]

                                            FFT Size: 4096 (blue)
                                            Warp: 12 o'clock (CV centered)
                                            Time: 1 o'clock
                                            Blur: 9-10 o'clock (light)
                                            Reflect: 9-10 o'clock
                                            Mix: 12 o'clock
                                            Atmosphere: 1-2 o'clock (slightly up)

[Aurora Left Out] ───────────────────────▶ [MixUp CH3 L]
[Aurora Right Out] ──────────────────────▶ [MixUp CH3 R]
```

**Setup:** Chord V2 Seventh output provides a single melodic voice tracking the upper register of the sequence. Hermod+ track 2 sends the same pitch CV data that drives Chord V2's root, so Aurora's Warp tracks the melody. With Warp centered and CV input active, the spectral field shifts up or down with each note change, harmonizing the reverb tail to the current pitch.

**Controls:** Time at 1 o'clock adds moderate amplitude blurring for reverb body without excessive tail length, keeping the shimmer tight enough to follow the sequence. A small amount of Blur at 9 to 10 o'clock adds frequency-domain shimmer to the high melodic content without moving into alien territory. Atmosphere slightly above center adds high-frequency content that reinforces the icy quality of the spectral shimmer. Reflect kept low avoids rhythmic artifacts at faster melodic rates. When the Hermod+ sequence changes pitch, Warp shifts the spectral field to match; the reverb tail follows the melody rather than decaying at a fixed pitch from the previous note.

**Result:** A pitch-tracking spectral shimmer on a melodic voice, where the reverb tail harmonizes with each note in the sequence via Warp CV. This demonstrates Aurora as a second harmonic voice rather than a static reverb effect.

---

### Patch 3: Drum Spectral Texture

vpme.de QD percussion into Aurora at FFT 1024 with Blur and Reflect for rhythmic spectral transformation, producing a textured percussive wash that retains the rhythmic structure of the input.

```
[QD Voice Out] ──────────────────────────▶ [Aurora Left In]
[Hermod+ Gate Out] ──────────────────────▶ [Aurora Freeze Gate]

                                            FFT Size: 1024 (cyan)
                                            Warp: 12 o'clock
                                            Time: 9-10 o'clock (minimal)
                                            Blur: 2 o'clock
                                            Reflect: 1-2 o'clock
                                            Mix: 12 o'clock
                                            Atmosphere: 11 o'clock (slightly down)

[Aurora Left Out] ───────────────────────▶ [MixUp CH3 L]
[Aurora Right Out] ──────────────────────▶ [MixUp CH3 R]
```

**Setup:** QD voice output provides a percussive transient-forward signal. FFT size 1024 introduces comb-like spectral timbres that complement percussive sources; at this FFT size, the module's transient response is faster and the frequency resolution is coarser, which produces a characteristic texture on drum voices that the larger FFT sizes do not. Hermod+ gate drives Freeze, which locks spectral snapshots at sequenced intervals to create rhythmic freeze events within the texture.

**Controls:** Time kept low preserves the rhythmic identity of the drum signal rather than blurring it into a continuous wash. Blur at 2 o'clock introduces heavy frequency smearing that transforms drum transients into pitched spectral artifacts. Reflect at 1 to 2 o'clock adds rhythmic multi-tap echoes that reinforce the percussion pattern with complementary delay offsets in the stereo field. Atmosphere slightly below center pulls down high frequencies, reducing harshness from the comb-like FFT character and shifting the spectral texture toward a denser, darker quality. Hermod+ gate to Freeze triggers spectral lock events: each gate captures a frozen moment of the drum transient's spectral character, which decays through Blur while the next hit enters the input.

**Result:** A rhythmic spectral texture from drum input, with comb-like FFT character at 1024, frequency blurring that transforms transients into pitched spectral artifacts, and gate-triggered Freeze events that layer frozen spectral snapshots against the live drum signal.

---

### Patch 4: Frozen Spectral Drone

Endorphin.es Furtrrrr Generator into Aurora with manual Freeze, then Warp CV transposing the frozen spectral content to build an evolving drone from a single captured moment.

```
[Furtrrrr Generator Out] ────────────────▶ [Aurora Left In]

                                            [Play source for 4-8 seconds]
                                            [Press Freeze to lock spectrum]
                                            [Disconnect source if desired]

[Hermod+ CV Out] ────────────────────────▶ [Aurora Warp CV]

                                            FFT Size: 4096 (blue)
                                            Warp: 12 o'clock (CV active)
                                            Time: 3 o'clock (full amplitude blur)
                                            Blur: 1-2 o'clock
                                            Reflect: 10 o'clock
                                            Mix: 3 o'clock (fully wet)
                                            Atmosphere: 12 o'clock

[Aurora Left Out] ───────────────────────▶ [MixUp CH3 L]
[Aurora Right Out] ──────────────────────▶ [MixUp CH3 R]
```

**Setup:** Furtrrrr Generator provides a dense, harmonically complex voice suitable for spectral capture. Allow the source to play for 4 to 8 seconds to build a stable spectral character in Aurora's processing chain before pressing Freeze. Once Freeze is engaged, the spectral snapshot is locked. The source can remain connected or be disconnected; Aurora holds the frozen content until Freeze is deactivated. Set Mix fully wet to hear only the frozen spectral content. Hermod+ CV into Warp drives pitch transposition of the frozen spectrum.

**Controls:** With Freeze active and Mix fully wet, Aurora outputs only the frozen spectral content. Time at fully CW blurs the amplitude of the frozen spectrum continuously, creating a sustained drone with soft, evolving amplitude movement. Blur at 1 to 2 o'clock adds frequency smearing to the frozen content, introducing slow spectral drift. Hermod+ CV into Warp shifts the pitch of the frozen spectrum in semitone or octave steps, which transposes the entire frozen drone without releasing the lock. A slow sequence driving Warp moves the frozen chord through pitch space in real time. To rebuild the drone from a new source moment, disengage Freeze, allow the source to play again for a few seconds, then re-engage Freeze. Changing FFT size while frozen requires a re-freeze.

**Result:** A sustained drone built from a single frozen spectral snapshot of the Furtrrrr Generator, transposable in real time via Warp CV, with slow amplitude and frequency blurring producing continuous evolution within the frozen content.

---

## Common Mistakes

**Treating Time and Blur as a single reverb size control.** Time and Blur operate on different components of the spectral signal. Time blurs amplitude; the result sounds like reverb decay. Blur smears frequency; the result sounds like spectral artifacts that often do not read as reverb at all. Raising both simultaneously produces a combined effect, but the individual behaviors are distinct enough that each deserves independent attention. Dial Time first to establish the reverb character, then add Blur carefully if spectral transformation is the goal.

**Ignoring FFT size.** The default 4096 is lush and appropriate for many sources, but staying there is leaving most of Aurora's character untouched. FFT 1024 on drum voices produces comb-like timbres that are genuinely different from anything the larger sizes produce. FFT 512 on a vocal or drum input creates alien spectral textures that have no equivalent elsewhere. Each FFT size suits different sources; the table in the manual gives starting points, but the only way to understand them is to cycle through all four on the current input.

**Misreading Atmosphere as a post-processing EQ.** Atmosphere shapes the spectral field within Aurora's processing chain, not after it. A high-pass character above center affects what frequencies the spectral processing operates on, not just the output. The whale-song territory below center emerges because spectral filtering interacts with the FFT-domain blurring, producing artifacts that no post-processing EQ would create. Treat Atmosphere as a timbral dimension of the reverb rather than a tone control on the output.

**Not adjusting input level.** Aurora's spectral response depends on the amplitude of the input signal. An undergained source produces a thin spectral field. The Shift+Mix input level control adjusts from -6dB to +12dB and is the correct way to match the source level to Aurora's internal framework. Default is 1x (blue LEDs). Sources that are quiet in the patch should have their input level raised before assuming Aurora cannot produce enough reverb density.

**Attempting Freeze without understanding what is being locked.** Freeze captures the current spectral characteristics of the input signal at the moment of engagement. What is frozen depends entirely on what was entering Aurora in the moments before Freeze is pressed. A momentary transient produces a thin spectral capture. A sustained, harmonically rich source produces a dense one. Allow the source to play through Aurora for several seconds before freezing to build a fuller spectral state worth capturing.

---

## Annotated Learning Path

**Entry point:** Patch any sustained voice (sine wave, pad, slow chord) into the left input and raise Time to 2 o'clock with Mix at 12 o'clock. Adjust Reflect while listening to how the tail changes character through its time zones. This establishes Aurora's core reverb behavior before any of the more complex controls are introduced.

**Step 2:** With a working reverb sound established, cycle through all four FFT sizes using Shift+Reverse. Listen to how the same knob settings produce entirely different sonic characters at each size. This is the most important orientation step because FFT size affects everything else.

**Step 3:** With Time and Mix set, introduce Blur slowly from fully CCW toward 12 o'clock. Stop at the point where the sound shifts from reverb to something else. Understanding where that transition occurs for the current source is essential to using Blur intentionally.

**Step 4:** Patch a 1V/Oct CV source into the Warp CV input and set a slow sequence. Listen to how the spectral field shifts with each note. This reframes Aurora from a reverb module into a pitch-responsive spectral instrument.

**Step 5:** Build a Freeze drone using the workflow in Patch 4. Capture a complex source, engage Freeze, then manipulate Time, Blur, and Atmosphere while the spectrum is locked. Add Warp CV to transpose the drone. This is Aurora's most distinctive capability and the one that separates it furthest from conventional reverb design.

**Step 6:** Route a percussive source through Aurora at FFT 1024 or 512 with Blur raised. This is the least reverb-like use of the module and requires accepting that the output will not be a recognizable version of the input. Aurora at FFT 512 on drums is a sound design tool, not a reverb.

---

## Patches Well With

- **Qu-Bit Chord V2** — Chord V2's Mix and Seventh outputs provide ideal input material for Aurora, with the Seventh voice tracking pitch sequences via Warp CV.
- **vpme.de QD** — Drum voices at FFT 1024 and 512 produce comb-like and alien spectral textures with rhythmic input, pushing Aurora into territory that sustained melodic sources cannot reach.
- **Gamechanger Audio Plasma Voice** — Plasma's metallic, harmonically dense character feeds Aurora's spectral engine with complex frequency content, producing reverb tails that preserve the industrial texture of the source.
- **Endorphin.es Furtrrrr Generator** — Dense, harmonically complex voice suitable for spectral capture and Freeze drones; Furtrrrr Generator's long sustain builds a stable spectral state worth locking.
