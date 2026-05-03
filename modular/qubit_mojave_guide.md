---
title: Qu-Bit Mojave
manufacturer: Qu-Bit Electronix
primary_role: PROCESSOR
secondary_roles: [GENERATOR]
form_factor: eurorack
functions: [granular, live-processing, reverb, feedback, cv-source]
behavior_tags: [granular, textural, atmospheric, cv-friendly, stereo, performance-oriented, rhythmic]
use_cases: [live granular processing, textural pads, melodic grain generation, feedback drones, granular looping]
hp: 14
depth: 22
historical_context: false
---

# Qu-Bit Mojave

![Qu-Bit Mojave](https://github.com/Shadoe-42/music/raw/main/modular/images/qubit/mojave/front_panel.jpg)

*Live granular processor with four Sky Mode pitch quantizations, three grain generation modes, and an algorithmic Dune CV output in 14HP*

## Quick Start: Get Sound in 5 Minutes

Mojave captures a continuously updating audio buffer and generates grains from that buffer in real time. It does not work from pre-recorded samples; it granularizes whatever audio is entering the module at that moment.

1. Patch any audio source into the Left input
2. Patch Left and Right outputs to a stereo mixer
3. Set Mix to 12 o'clock
4. Set Rate to 10 o'clock (moderate grain density)
5. Set Size just right of center (short forward grains)
6. Set Zone fully counter-clockwise (real-time grains)
7. Set Gust to center (no feedback or reverb)
8. Confirm Gen Mode LED is blue (Erode, the default)
9. Send audio and listen to the granular layer appearing over the dry signal
10. Press Sky Mode to cycle to Dawn (blue LEDs), then slowly raise Structure

Rate, Size, and Structure are the three controls to understand before adding anything else.

## Key Specs

| Spec | Value |
|------|-------|
| HP | 14 |
| Depth | 22mm |
| +12V | 167mA |
| -12V | 13mA |
| 5V | 0mA |
| Sample Rate | 48kHz |
| Bit Depth | 32-bit internal, 24-bit conversion |
| Sky Modes | 4 (scales configurable via Narwhal) |
| Gen Modes | 3 |

## Essential Parameters

**Rate** controls how frequently grains are triggered. In the default Free Clock Mode, Rate spans from a slow, sparse grain rate fully counter-clockwise to audio rate triggering fully clockwise. In Quantized Clock Mode, Rate becomes a division and multiplication control for an internal or external clock, with steps from /8 through x8. Rate has a CV input. The relationship between Rate and Size is important: the maximum grain length is always capped at ten times the current grain interval, so fast Rate settings prevent long grains.

**Gen button and Gen Gate input** trigger a single grain independent of the clock rate. The Gen Mode button cycles through three generation modes. In Erode (blue, default), Mojave generates grains from both the clock rate and the Gen input simultaneously. In Shear (green), Mojave monitors the incoming audio level and generates grains when the signal crosses a threshold, making rhythmic content in the input drive grain density directly. In Chisel (gold), grains are generated only from the Gen button or gate input; all other generation sources are ignored. Chisel pairs with a gate sequencer for precise rhythmic grain triggering when clock-driven generation is not wanted.

**Sky Mode** button cycles through four pitch quantization modes that affect Structure and Speed simultaneously. Dawn (blue LEDs) quantizes to a major scale. Day (green LEDs) quantizes to a minor scale. Dusk (gold LEDs) quantizes to a chromatic scale. Twilight (purple LEDs) removes all pitch and rhythm quantization. Sky Mode does not change the input audio; it changes the pitch intervals available to Structure and Speed when they produce grain pitch variation. Each mode's scale is reconfigurable via the Narwhal web app.

**Structure** controls random grain pitch variation. At zero, all grains play at the original pitch. Turning clockwise introduces semitone pitch shifts per grain, then adds octave jumps, then narrows to octave-only shifts, then opens to all pitches within the current Sky Mode scale, and finally introduces melodic events including arpeggios and trills as the knob reaches fully clockwise. The Speed knob position acts as the root offset that Structure randomizes around. Structure has a CV input, which makes pitch complexity a patchable, continuously variable parameter.

**Size** controls both the length and playback direction of each grain from a single knob. The center position produces the shortest grain, approximately 20ms. Turning right of center extends grain length forward in time, up to 4 seconds. Turning left of center extends grain length in reverse, and also flips the Window envelope shape to emphasize the reversed playback character. Maximum grain length is tied to Rate and cannot exceed ten times the current grain interval. Size has a CV input.

**Zone** determines where in the audio buffer grains are generated. Fully counter-clockwise produces grains from real-time incoming audio. Turning clockwise moves the grain read position further back into the buffer, reaching up to the full buffer length into the past. Zone has a CV input. When Lock is active, Zone becomes a scrub control over the frozen buffer rather than a live position selector.

**Lock** button and gate input freeze the audio buffer in place, capturing a snapshot of the incoming audio at that moment. Once locked, the buffer content stays fixed while Mojave continues generating and modifying grains from it. Zone then functions as a buffer scrub. With Rate set high and Size large enough for grains to overlap, the Lock and Zone combination produces pseudo-time-stretching effects on the frozen audio.

**Gust** is an end-of-chain effect control. Center position produces no effect. Turning left of center increases feedback, recirculating the granular output back into the processing chain. Turning right of center increases reverb amount. Both the feedback and reverb characters are configurable in finer detail via the Narwhal web app. Gust has a CV input.

**Dune output** generates an algorithmically determined CV or gate signal that responds to Mojave's internal state. In the default configuration, it outputs a morphing voltage whose behavior is shaped by three controls: Distribute controls the amount of stepped modulation, Drift controls modulation direction (ascending or descending ramp), and Whirl controls the speed. Via Narwhal, Dune can be reconfigured to output grain gates or a clock passthrough. Dune is a direct window into what Mojave is doing internally, and self-patching Dune to Zone CV creates a continuously evolving granular loop driven by the module's own state.

**Speed** applies vari-speed pitch shifting to each grain, spanning minus two octaves to plus two octaves with original pitch at center. Speed tracks 1V per octave and has a CV input. Speed acts as the root position that Structure's pitch randomization uses as an offset, so changing Speed while Structure is active shifts the entire range of melodic grain variation simultaneously.

**Distribute** adds rhythmic variation to grain triggering. In Free Clock Mode it increases the probability that grains deviate from the grain rate, ranging from predictable to fully random. In Quantized Clock Mode it introduces quantized rhythmic variations including rests, ratchets, and pulsing patterns. **Whirl** adds random stereo panning per grain, from the original stereo position to fully random placement. Both controls have CV inputs and both affect the behavior of the Dune output.

**Window** selects the envelope shape applied to each grain, crossfading between five shapes from left to right: Hamming, Up Ramp, Triangle, Exponential Down Ramp, and Square. Each shape produces a different attack and release character on individual grains, and the current Window is indicated by a unique LED color on the Dune indicators. Window has a CV input.

## Why This Excels

Mojave processes incoming audio from a live, continuously updating buffer rather than a recorded sample, which means the granular output at any moment reflects what is entering the module right now. A cymbal hit that decays naturally produces different grain material at different points in its decay curve, and all of that material is available for Zone to address. A slowly evolving chord from another oscillator produces grain material that shifts as the chord shifts. This live-buffer architecture is the fundamental difference between Mojave and a granular sampler; Mojave granularizes performance as it happens, not recordings.

The combination of Sky Mode and Structure transforms Mojave from a texture tool into a melodic generator. With a Sky Mode scale selected and Structure turned up, any incoming audio becomes a source of harmonically coherent grain clouds that remain in key regardless of the original pitch content of the source. A monophonic drone fed into Mojave with Dawn selected and Structure at three-quarters produces a major-scale granular arpeggio from a single sustained pitch. Routing a 1V/oct CV sequence into the Speed input then transposes the entire cloud diatonically, making the sequencer drive both the grain pitch center and the melodic range of the granular output simultaneously.

Lock and Zone together form an underused workflow. With the audio buffer frozen via Lock and Zone receiving CV, Mojave becomes a buffer scrubber with granular playback. High Rate and overlapping grain sizes produce time-stretching effects on the captured audio. Patching the Dune output to the Zone CV input creates a self-patching granular looper: Mojave generates its own buffer position modulation from its own internal state, producing a continuously cycling loop that evolves as Distribute, Drift, and Whirl change the character of the Dune signal. The loop is never identical twice because the modulation source is the module itself.

The feedback range of Gust is a distinct sound design space that has no equivalent in the reverb range. With Gust turned left of center and a short transient fed into the input, the granular engine recirculates its own output, building and sustaining feedback textures from a single impulse. Speed set one semitone above center causes the feedback to accumulate in an ascending harmonic series as it recycles through the granular engine. Drift turned up converts the stable feedback into an echo chamber of granular events spread across the buffer. This is a patch that rewards slow, deliberate control changes over time rather than immediate parameter sweeps, because the granular recirculation takes time to build into something coherent.

## Patches

### Patch 1: Metallic Granular Texture

Cymbal or metallic percussion source into Mojave with Whirl adding per-grain stereo scatter, routed through Mingles for a second layer of autopanning.

```
[QoP] ── Voice out ──────────────────────▶ [Mojave Left In]

                                            Gen Mode: Erode (blue)
                                            Sky Mode: Twilight (purple)
                                            Rate: 10 o'clock
                                            Size: 1 o'clock (short forward)
                                            Drift: 9 o'clock (slight)
                                            Whirl: 2 o'clock
                                            Gust: 1-2 o'clock (light reverb)
                                            Mix: 12 o'clock

[Mojave Left Out] ───────────────────────▶ [Mingles Ch1 Input A]
[Mojave Right Out] ──────────────────────▶ [Mingles Ch1 Input B]

                                            Mingles LFO: 10 o'clock
                                            Mingles Pan: 12 o'clock

                          [Mingles Mix Out L] ──▶ [MixUp CH3 L]
                          [Mingles Mix Out R] ──▶ [MixUp CH3 R]
```

**Setup:** QoP cymbal or metallic voice feeds Mojave's left input, which is normalled internally to both channels. Mojave's stereo output feeds Mingles Channel 1. Sky Mode is set to Twilight to remove pitch quantization; metallic and cymbal sounds have inharmonic spectral content that does not benefit from scale-based grain pitch restriction.

**Controls:** Rate at 10 o'clock produces a grain density that preserves the attack and decay character of the cymbal hit while adding a granular cloud around it. Drift at 9 o'clock introduces slight buffer position randomization, loosening the tight real-time tracking without fully dispersing the grains. Gust right of center adds a short reverb tail to the granular output. Whirl at 2 o'clock randomly repositions each grain in the stereo field before the signal reaches Mingles. Mingles' built-in LFO then adds a slower autopanning sweep over the already spatially scattered output, building stereo movement on two different timescales simultaneously.

**Result:** A metallic percussion sound dispersed into a granular stereo texture with per-grain random panning from Whirl and slower rhythmic autopanning from Mingles, producing a stereo field that moves continuously at two rates.

---

### Patch 2: Melodic Structure Clouds

Sustained chord source into Mojave with Sky Mode and Structure generating melodic grain clouds, with Kali delay building echo depth.

```
[Chord V2 Mix Out] ──────────────────────▶ [Mojave Left In]

[Zadar CH1] ─────────────────────────────▶ [Mojave Structure CV]
(slow envelope, 15-25 seconds, infinite repeat)

                                            Gen Mode: Erode (blue)
                                            Sky Mode: Day (green, minor)
                                            Rate: 9 o'clock (sparse grains)
                                            Size: 2-3 o'clock (long forward)
                                            Structure: 3 o'clock (base)
                                            Speed: 12 o'clock (original pitch)
                                            Gust: 2 o'clock (light reverb)
                                            Mix: 2 o'clock (mostly wet)

[Mojave Left Out] ───────────────────────▶ [Kali Audio In L]
[Mojave Right Out] ──────────────────────▶ [Kali Audio In R]

                                            Kali: ping-pong delay
                                            Kali delay time: clocked or moderate manual

                         [Kali Out L] ──▶ [MixUp CH3 L]
                         [Kali Out R] ──▶ [MixUp CH3 R]
```

**Setup:** Chord V2 Mix output provides sustained harmonic content into Mojave's left input. Sky Mode is set to Day (minor scale) to match minor chord material from Chord V2. Zadar CH1 in infinite-repeat mode slowly modulates the Structure CV input over 15 to 25 seconds, sweeping Structure from its set base position up through the melodic range and back.

**Controls:** Slow Rate and long Size produce overlapping grains that accumulate into a sustained pad. With Sky Mode Day active and Structure at 3 o'clock, grains are pitched to minor scale intervals, spreading the chord input into a harmonically expanding cloud. Zadar's slow Structure modulation drives the cloud from simple pitch variation into melodic arpeggios at the top of the sweep, then pulls it back to simpler texture as the envelope descends. Kali's ping-pong delay catches each grain cluster and repeats it in alternating stereo positions, building echo trails that extend the sustain of the cloud between Mojave's grain events.

**Result:** A sustained harmonic cloud from a chord input, with grain pitch following the minor scale and slowly evolving from texture toward melodic content as Zadar modulates Structure, with Kali extending each granular event into stereo delay trails.

---

### Patch 3: Lock and Zone Granular Looper

Buffer-freezing workflow with Dune self-patched to Zone CV, producing a continuously cycling granular loop driven by Mojave's own internal state.

```
[Cs-L Sine Out] ─────────────────────────▶ [Mojave Left In]
[Hermod+ CV Out] ────────────────────────▶ [Mojave Speed CV]

                        [Allow 2-4 bars of audio to fill the buffer]
                        [Then engage Lock: Left Dune LED turns white]

[Mojave Dune Out] ───────────────────────▶ [Mojave Zone CV]

                                            Lock: active
                                            Rate: 1-2 o'clock (fast, overlapping)
                                            Size: 2-3 o'clock (long grains)
                                            Drift: 10 o'clock (moderate)
                                            Whirl: 1 o'clock
                                            Gust: 1 o'clock (light reverb)
                                            Mix: 2 o'clock (mostly wet)

[Mojave Left Out] ───────────────────────▶ [Mingles Ch1 Input A]
[Mojave Right Out] ──────────────────────▶ [Mingles Ch1 Input B]

                          [Mingles Mix Out L] ──▶ [MixUp CH3 L]
                          [Mingles Mix Out R] ──▶ [MixUp CH3 R]
```

**Setup:** Cs-L provides a sustained tonal source to build a buffer worth capturing. Hermod+ pitch CV into Speed sets the playback pitch center of the granular output. Allow 2 to 4 bars of audio to enter before engaging Lock; the buffer captures that window of material. Then patch the Dune output to the Zone CV input. Dune's default ascending ramp behavior moves Zone continuously through the frozen buffer.

**Controls:** With Lock engaged, Zone is a scrub control over the fixed buffer. Dune drives Zone from the most recent captured audio toward the oldest, cycling the loop forward through the frozen material. Rate at 1 to 2 o'clock and Size large enough for grains to overlap produces smooth granular time-stretching from the cycling buffer. Drift at moderate levels adds controlled randomness to the Dune-driven Zone position, creating variation in the loop without breaking its forward motion. Adjusting Distribute, Drift, and Whirl changes the Dune output character, which changes the loop behavior. To unlock and recapture new material, disengage Lock and allow the buffer to refill.

**Result:** A granular loop built from a captured audio buffer, cycling continuously via Dune driving Zone, with time-stretching grain overlap and Drift adding controlled position randomness to the loop.

---

### Patch 4: Feedback Drone

Short transient into Mojave with Gust in full feedback, building a self-sustaining granular texture with ascending harmonic character from Speed.

```
[QoP] ── Gate out ───────────────────────▶ [Mojave Gen Gate In]
                                            Gen Mode: Chisel (gold)

[QoP] ── Voice out (short transient) ────▶ [Mojave Left In]

                                            Rate: 2 o'clock (fast)
                                            Size: 3 o'clock (maximum forward)
                                            Gust: 8 o'clock (full feedback)
                                            Speed: 12 o'clock +1 semitone
                                            Drift: 9-10 o'clock (moderate)
                                            Mix: 3 o'clock (fully wet)
                                            Zone: fully CCW

[Mojave Left Out] ───────────────────────▶ [Kali Audio In L]
[Mojave Right Out] ──────────────────────▶ [Kali Audio In R]

                                            Kali: basic delay, moderate time
                                            Kali feedback: 9-10 o'clock

                         [Kali Out L] ──▶ [MixUp CH3 L]
                         [Kali Out R] ──▶ [MixUp CH3 R]
```

**Setup:** QoP sends a single gate into Mojave's Gen input with Gen Mode set to Chisel, so grains are triggered only by the gate and not the internal clock. A short transient voice output from QoP enters the left audio input as the grain source material. Gust turned fully left engages full feedback, recirculating the granular output back into the processing chain.

**Controls:** A single gate trigger seeds the feedback with one grain event. With Gust at full feedback, Mojave recirculates that event and builds it into a sustaining texture. Speed set one semitone above center causes the feedback to accumulate pitch upward through a harmonic series with each recirculation. Drift at moderate levels introduces random buffer position variation, spreading the tight feedback into a wider granular echo chamber. Changes to Rate and Size while the feedback sustains reshape the texture without stopping it. To end the drone, bring Mix down or return Gust to center. Kali's basic delay adds echo depth and stereo width behind the granular feedback texture.

**Result:** A self-sustaining granular feedback drone seeded by a single transient, with ascending harmonic drift from Speed and spreading delay depth from Kali. The drone persists and evolves until Gust or Mix is reduced.

---

## Common Mistakes

### "The granular effect sounds like a chorus or comb filter, not a cloud of grains."

Rate is likely too high relative to Size, driving grain generation into audio frequencies where grains overlap into pitch and comb effects rather than distinct granular texture. This is accurate granular physics at audio rate, but it is not the cloud-like result most users expect initially.

**Fix:** Bring Rate below 12 o'clock to slow grain triggering to a distinguishable density, and set Size just right of center for short forward grains. Turn up Mix to blend the granular layer over the dry signal. Once distinct grains are audible, Rate and Size can be explored from that foundation.

---

### "Structure is producing random pitches with no musical relationship."

Sky Mode is likely set to Twilight (purple LEDs), which removes all pitch quantization. In Twilight, Structure randomizes grain pitch without scale constraints, producing chromatic or microtonal scattering.

**Fix:** Press Sky Mode to select Dawn (blue, major), Day (green, minor), or Dusk (gold, chromatic). Structure's pitch randomization will then be constrained to the selected scale, producing harmonically coherent grain pitch variation from the same control position.

---

### "Lock is active but there is no time-stretching effect."

Lock freezes the audio buffer and makes Zone a scrub control, but the time-stretching effect requires Rate to be high and Size to be large enough for grains to overlap continuously. Sparse or short grains with Lock active produce discrete events from the frozen buffer, not a smooth stretched texture.

**Fix:** With Lock active, bring Rate up to 1 to 2 o'clock and Size to 2 to 3 o'clock so grains overlap. Then move Zone manually or via CV to hear the buffer scrub. The smooth granular time-stretch emerges from grain density, not from Lock alone.

---

### "The Dune output appears to be a slow, featureless LFO."

Dune's behavior is shaped by Distribute, Drift, and Whirl. With all three at zero or center, Dune outputs minimal movement and appears almost static.

**Fix:** Raise Whirl to increase Dune's speed, raise Distribute to introduce stepped modulation character, and use Drift to set the ramp direction. Self-patch Dune to Zone CV for the looper workflow in Patch 3, or route it to an external module's CV input to hear its character before using it internally. Dune responds to Mojave's own state; changing other controls changes the Dune output.

---

## Advanced Learning Path

1. Learn Rate and Mix in isolation before adding any other controls. Understand what different grain densities sound like from the same audio source across the full Rate range: the difference between 8 o'clock, 12 o'clock, and 3 o'clock Rate positions is fundamental to understanding what Mojave is doing. Only once the grain density relationship is clear should Size and Zone be added to the learning process.

2. Work through all four Sky Modes with Structure raised to the same position in each. Dawn, Day, Dusk, and Twilight produce fundamentally different pitch relationships from identical control positions. Use the same audio source and the same Structure position across all four modes to hear what quantization is doing to the grain pitch distribution in isolation.

3. Learn Size as a two-dimensional control rather than a single-axis adjustment. Center is not a neutral or bypass position; it is the shortest grain. Left of center is a distinct reversal domain with its own set of grain characters, not simply a quieter or subtler version of the right side. Explore the full left range of Size as its own territory.

4. Explore Gen Mode before adding CV control. Switching from Erode to Shear and back while audio is running reveals the difference between clock-driven and audio-threshold-driven grain generation. Shear makes rhythmic content in the input signal become the grain trigger source, which produces fundamentally different results from Erode with identical audio.

5. Use the Dune output as a modulation source for external modules before self-patching it to Zone. Patch Dune to a filter cutoff or VCA CV first to hear what it is doing under different Distribute, Drift, and Whirl settings. Once its voltage character is understood, the self-patching looper in Patch 3 becomes a controlled choice rather than an opaque outcome.

6. Explore the full feedback range of Gust as a distinct sound design domain. Full feedback with a short transient input produces results with no analog in the reverb range of the same knob. The feedback range rewards slow, deliberate control changes over time because the granular recirculation takes time to build and stabilize.

7. Use Speed CV with 1V/oct tracking from a sequencer while Structure is active. Because Speed acts as the root offset for Structure's pitch randomization, changing Speed via a pitch sequence transposes the entire cloud of granular pitch variation diatonically within the selected Sky Mode. A two-track sequencer, one driving Speed CV and one driving an audio source into Mojave, produces a melodic granular arrangement with pitch information coming from two simultaneous sources.

## Pairs Well With

**After Later Audio Mingles** receives Mojave's stereo output and adds a second layer of spatial movement to an already spatially active signal. Mojave's Whirl control randomizes stereo panning per grain; Mingles' built-in LFO then applies a slower, rhythmic autopanning sweep over the entire stereo image. Channel 1 of Mingles receives the standard LFO phase and Channel 2 receives an inverted phase, which creates a crisscross panning motion when both stereo outputs are used. For textural and rhythmic Mojave patches, the combination of per-grain Whirl and Mingles autopanning builds a stereo field that moves on two different timescales from a single downstream connection.

**dsp.coffee Kali** receives Mojave's stereo output and extends the granular content with delay and modulation. In ping-pong delay mode, Kali catches each grain cluster and repeats it in alternating stereo positions, building echo trails independent of Mojave's own Gust reverb. Kali's granular delay modes interact productively with already-granularized content, adding a second layer of grain-based time domain processing to the signal. Kali also generates its own modulation CV outputs, which can be routed back to Mojave's Rate or Structure CV inputs to create a clock-synced feedback loop between the two modules.

**Squarp Instruments Hermod+** serves two distinct functions with Mojave. In Chisel Gen Mode, Hermod+ gate outputs trigger individual grain events with precise rhythmic timing, making grain density a sequenced parameter rather than a continuous rate. In any Gen Mode, Hermod+ 1V/oct outputs into the Speed CV input control the base pitch of granular playback, with diatonic pitch changes driving the harmonic center of Structure's melodic variation. Running two Hermod+ CV tracks simultaneously, one into Speed and one into Structure CV, provides direct melodic and harmonic control over what the granular engine produces from any incoming audio source.

**Xaoc Devices Zadar** provides the slow, independently paced modulation that Mojave's CV inputs respond best to. Structure CV modulated by a slow Zadar envelope in infinite-repeat mode sweeps Mojave through its pitch complexity range over 15 to 30 seconds, moving the granular output from simple texture to full melodic content and back on a timescale independent of the patch tempo. Zone CV from a separate Zadar channel moves the grain read position through the audio buffer at a different rate. Rate CV from a third channel changes grain density independently of both. Three Zadar channels into three Mojave CV inputs at different rates produce granular evolution that changes on multiple simultaneous timescales with no repeating pattern.
