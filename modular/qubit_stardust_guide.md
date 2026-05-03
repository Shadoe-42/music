---
title: Qu-Bit Stardust
manufacturer: Qu-Bit Electronix
primary_role: PROCESSOR
secondary_roles: [GENERATOR]
form_factor: eurorack
functions: [looper, tape-emulation, sampler, effects]
behavior_tags: [looping, layering, tape-character, cv-friendly, stereo, performance-oriented]
use_cases: [live looping, overdub layering, tape-style loop manipulation, sample import, loop rearrangement]
hp: 18
depth: 22
historical_context: true
---

# Qu-Bit Stardust

![Qu-Bit Stardust](https://github.com/Shadoe-42/music/raw/main/modular/images/qubit/stardust/front_panel.jpg)

*Stereo tape looper with four loop modes including Frippertronics, Slice and Skip rearrangement, four effect pairs, Varispeed with 1V/oct tracking, and a configurable Nova CV/Gate output in 18HP*

## Historical Context

Pierre Schaeffer was working at French national radio in Paris in the late 1940s when he began composing music from recorded sound. His 1948 Études de bruits (studies in noise) were assembled from recordings of trains, spinning tops, canal boats, and other acoustic sources, manipulated by changing playback speed, reversing direction, and forming physical loops by cutting disc grooves into closed circles that repeated indefinitely. He called this practice musique concrète: concrete music, built from recorded real-world material rather than from abstract notation written for acoustic instruments. The foundational insight was that a recording was not documentation of sound but raw material for composition in its own right.

Tape replaced disc as the physical medium through the 1950s and allowed more precise manipulation. Magnetic tape could be cut with scissors, spliced, looped by joining the end to the beginning, and layered by recording multiple passes onto the same spool. Composers including Karlheinz Stockhausen, John Cage, and Edgard Varèse built major works from tape splicing and looping techniques during this period. The loop was now a compositional unit: a fixed duration of audio that repeated indefinitely, available for overdubbing, speed manipulation, and layering.

Robert Fripp and Brian Eno formalized tape looping as a live performance architecture. Their collaborative records No Pussyfooting (1973) and Evening Star (1975) were constructed using two Revox A77 reel-to-reel tape machines arranged so that the output of one machine's record head fed the input of the other after a delay determined by the length of tape running between them. Fripp played guitar into this system. The signal was recorded, passed through the delay, and returned to the input, where it was recorded again over the existing content. Each pass through the record head slightly reduced the amplitude of older material as new material was added. Older layers faded gradually into silence while fresh layers accumulated above them. The result was an ever-changing acoustic environment built from accumulated, decaying passes of a single instrument.

Fripp refined this into a solo performance practice he called Frippertronics, documented on Let The Power Fall (1981). The technique treated the tape loop system as the instrument: Fripp played into it, the layers accumulated and decayed, and the loop itself became the composition as it evolved through the performance. The machine was not a recorder of music but a participant in making it.

Stardust is a direct descendant of this lineage. Its Frippertronics loop mode implements the layer-decay behavior of the original tape technique in digital hardware, complete with configurable decay rate. The Slice and Skip controls extend the tape manipulation vocabulary into territory that physical tape could only approximate through literal cutting and rearranging. The tape saturation, wow and flutter, and hiss effects reference the sonic character of the machines that made the original technique possible.

## Quick Start: Get Sound in 5 Minutes

Stardust is a looper. The fundamental workflow is: record audio into a buffer, then play that buffer back as a loop.

1. Patch any audio source into the Left input
2. Patch Left and Right outputs to a stereo mixer
3. Set In Level to 12 o'clock (full amplitude)
4. Set Mix to 12 o'clock (50/50 dry and wet)
5. Set Start fully counter-clockwise (loop start at beginning of buffer)
6. Set Size fully clockwise (full buffer available for playback)
7. Press Record; the LED turns red and recording begins
8. Play several bars of source material
9. Press Play/Pause to set the loop point and begin looped playback
10. Listen to the loop repeat, then press Record again to begin an overdub
11. Press Undo to remove the last overdub layer if needed

That is the core workflow. Record, Play/Pause, and Undo are the three controls to learn before anything else.

## Key Specs

| Spec | Value |
|------|-------|
| HP | 18 |
| Depth | 22mm |
| +12V | 175mA |
| -12V | 8mA |
| 5V | 0mA |
| Sample Rate | 48kHz |
| Bit Depth | 32-bit internal, 24-bit conversion |
| Noise Floor | -94dB |
| Loop Modes | 4 |
| Effect Modes | 4 |

## Essential Parameters

**Record button and gate input** start and stop recording audio into the buffer. The first recording establishes the maximum buffer length and sets the loop duration. Subsequent recordings are overdubs made within that established loop. If a recording passes the loop end point, it continues from the loop start, allowing seamless circular overdubbing. The record state changes on button release or on the rising edge of a gate input. Three Punch-In modes are available via Shift+Record: manual (default), Immediate Full (recording ends automatically at the loop point), and Queued Full (recording queues to begin at the next loop start).

**Play/Pause button and gate input** start and stop loop playback. Pressing Play/Pause after an initial recording sets the loop point. Pressing it again pauses playback and leaves the tape head at its current position, which becomes the resume point on the next press. Ending an initial recording with Play/Pause rather than Record continues recording audio tails into the buffer past the loop point without cutting them off abruptly.

**Erase and Undo** manage the buffer content. Erase deletes the entire buffer and stages Stardust for a new recording; holding the button for more than two seconds cancels the erase. Undo removes only the most recent recording layer, preserving all previous overdubs. A second press of Undo after undoing reintroduces the removed layer (Redo). Undo is the primary safety net for overdub sessions where a single pass needs to be removed without starting over.

**Varispeed encoder and 1V/Oct input** control loop playback speed and pitch together. Because Stardust is a tape-style device, speed and pitch are inseparable: faster playback raises pitch, slower playback lowers it. The range spans from one-quarter speed (minus two octaves) to eight times speed (plus three octaves), with a click of the encoder returning to one-times speed. The 1V/Oct input allows a pitch sequencer to transpose the loop in real time while the recording remains unchanged. Four Varispeed range modes are available via Shift+Varispeed Click: Semitones, Unquantized, Octaves and Fifths, and Octaves Only.

**Inertia** controls the lag between a Varispeed change and the resulting change in playback speed, producing a tape stop effect. Fully counter-clockwise applies no lag. Turning clockwise increases the lag from short vinyl stop effects up to a two-second motor failure simulation. The Inertial Slope (Shift+Inertia) adjusts whether the lag applies to speed decreases only, increases only, or both.

**Start and Size** define the playback window within the recorded buffer. Start sets the loop start point from the beginning of the buffer (fully counter-clockwise) to the end (fully clockwise). Size sets the loop length relative to that start point, from 5ms at fully counter-clockwise to the full buffer length at fully clockwise. If the Size window extends past the end of the recorded buffer, the loop wraps around and continues from the beginning of the buffer. Both controls have CV inputs, which makes the playback window a patchable, animatable parameter. Slow CV on both simultaneously produces continuously shifting loop content from a fixed recording.

**Slice and Skip** are the rearrangement controls. Slice divides the active loop into evenly distributed splice points, with the number of slices increasing by multiples as the knob turns clockwise (2, 4, 8, 16, up to a minimum slice length of 62ms). Skip controls the probability that a splice transformation will occur at each slice point. Six transformation zones are stacked as Skip increases: start position offset, random reversal of a slice, micro pitch changes, octave jumps, random semitone jumps, and finally tape lag applied to the random semitone jumps. With Slice set and Skip at zero, the loop plays normally but the splice structure is active and available for Skip to act on. With both raised, the loop is actively rearranged on each slice point according to the Skip probability zones reached.

**Loop Mode button** selects the macro recording behavior. Sound on Sound (default) adds new recordings to existing content without affecting older material. Replace deletes audio at the current record position as new audio is recorded over it. Frippertronics decreases the amplitude of existing loop content each time a new recording is made, so older layers progressively fade while new layers accumulate above them, mirroring the original tape technique. Resample records a new buffer from the current mangled loop output, including all Varispeed, Reverse, Slice, Skip, and effect processing, baking the current state into a new source recording.

**Effect Mode button** cycles through four effect modes, each assigning a different pair of effects to the Flutter and Hiss knobs. In Analog Tape Emulation (blue), Flutter controls wow and flutter amount and Hiss controls tape hiss amount. In Digital Audio Artifacts (green), Flutter controls downsampling amount and Hiss controls bitcrush amount. In Reverberation (gold), Flutter controls reverb amount and Hiss controls reverb time. In Highpass/Lowpass Filtering (purple), Flutter controls a highpass filter (dry to 12kHz cutoff) and Hiss controls a lowpass filter (dry to 25Hz cutoff). All four effect modes run simultaneously; the Effect Mode button selects which pair Flutter and Hiss currently control. Effects can be applied to the wet signal only (default) or to the dry signal as well via Shift+Effect Mode.

**Reverse button and gate input** toggle loop playback direction. Forward is the default (LED white); reversed playback is indicated by a blue LED. The reversed speed matches the forward speed set by Varispeed. Reverse can be clocked in Clock Mode for rhythmically timed direction changes.

**Freeze button and gate input** lock and repeat a small portion of the loop, approximately 1 percent of the loop length with a minimum of 62ms. Freeze produces a stutter effect from the current loop position without affecting the underlying buffer.

**Nova output** generates a configurable CV or gate signal derived from Stardust's internal state. In the default Nova mode it outputs a gate at the end of each loop and at the end of each slice point, making it a clock source that reflects the loop and slice structure. Flare mode outputs end-of-loop gates only. Spark mode outputs end-of-slice gates only. Orbital mode outputs a CV representing the playback position within the loop (0V to +5V across the loop length), which can be used to modulate other modules in synchrony with the loop playback.

## Why This Excels

The four Loop Modes are four fundamentally different instruments sharing the same hardware. Sound on Sound builds density continuously, accumulating layers until the buffer is full of overlapping content. Replace is a traditional looper: one layer at a time, with each new recording erasing what was there before. Frippertronics is a compositional mode: the loop evolves continuously as older material decays and new material takes its place, producing output that changes over time without ever being the same twice. Resample collapses all processing into a new source recording, which can then be treated as raw material for another cycle of manipulation. Switching Loop Modes mid-session changes the behavior of every subsequent recording without disturbing existing content.

The Slice and Skip controls transform a linear loop into a probability engine. A loop recorded once becomes source material that Stardust can rearrange, reverse, pitch-shift, and reorder on each pass through the splice points. Skip's six stacked transformation zones mean the rearrangement complexity scales with the knob: low Skip introduces subtle offset and occasional reversal, while high Skip introduces octave jumps, random semitone variation, and tape lag on the rearranged slices. The result is that a single recorded phrase can produce dozens of distinct rhythmic and melodic variations without any new source material being introduced.

Start and Size as CV destinations make the playback window a patchable dimension of the loop. A slow envelope on Start CV gradually moves the loop start point through the buffer while Size holds the window length constant, producing a loop that scrolls through its own recorded content over time. Independent slow CV on both Start and Size simultaneously creates a window that shifts position and changes length, visiting different sections of the buffer at different durations. An hour of source material can be navigated continuously from a single patch point.

The Nova output closes the loop between Stardust and the rest of the patch. In Orbital mode, Nova outputs a CV proportional to the playback position within the loop, which can be routed to Varispeed CV (pitch rises and falls with loop position), to a filter cutoff, or to a VCA CV. In Spark mode, each slice point generates a gate that can clock a sequencer or trigger an envelope, synchronizing external modules to Stardust's internal slice structure. Stardust becomes both a looper and a clock and modulation source for the modules around it.

## Patches

### Patch 1: First Loop and Overdub

Basic loop recording and overdub workflow with Varispeed transposition and tape emulation effects.

```
[Cs-L Sine Out] ─────────────────────────▶ [Stardust Left In]
[Hermod+ CV Out] ────────────────────────▶ [Stardust V/Oct]

                                            In Level: 12 o'clock
                                            Mix: 12 o'clock
                                            Loop Mode: Sound on Sound (default)
                                            Effect Mode: Tape Emulation (blue)
                                            Flutter: 9-10 o'clock (subtle wow)
                                            Hiss: 9 o'clock (minimal hiss)
                                            Start: fully CCW
                                            Size: fully CW

                    [Record] → play 4-8 bars → [Play/Pause to set loop]
                    [Record again] → play a second phrase → [Play/Pause]
                    [Undo if the overdub is wrong]

[Stardust Left Out] ─────────────────────▶ [MixUp CH1 L]
[Stardust Right Out] ────────────────────▶ [MixUp CH1 R]
```

**Setup:** Cs-L provides a sustained melodic source. Hermod+ pitch CV into V/Oct allows the loop to be transposed after recording. Effect Mode is set to Tape Emulation with subtle Flutter and Hiss settings to add warmth without obscuring the source material.

**Controls:** Record the first phrase and set the loop with Play/Pause. Listen to the loop repeat for a few passes to understand its character, then press Record to begin a second overdub layer. The second recording adds to the first in Sound on Sound mode. Use Undo if a layer is wrong. Once two or three layers are accumulated, use Varispeed (via Hermod+ pitch CV into V/Oct) to transpose the entire loop, listening to how pitch and speed change together. Try Reverse to hear the loop backward, then return forward.

**Result:** A layered melodic loop with tape warmth, built from two or three overdub passes, transposable in real time via pitch CV. This is the foundational Stardust workflow from which all other patches extend.

---

### Patch 2: Frippertronics Layer Decay

Frippertronics loop mode with continuous overdubbing, producing a compositional loop that evolves as older layers decay and new layers accumulate.

```
[Cs-L Sine Out] ─────────────────────────▶ [Stardust Left In]
[Hermod+ CV Out] ────────────────────────▶ [Stardust V/Oct]
[Hermod+ Gate Out] ──────────────────────▶ [Stardust Record Gate]

                                            Loop Mode: Frippertronics
                                            In Level: 12 o'clock
                                            Mix: 2 o'clock (mostly wet)
                                            Effect Mode: Tape Emulation (blue)
                                            Flutter: 10 o'clock
                                            Hiss: 9-10 o'clock
                                            Shift+Start: 12 o'clock (moderate decay rate)

[Stardust Left Out] ─────────────────────▶ [MixUp CH1 L]
[Stardust Right Out] ────────────────────▶ [MixUp CH1 R]
```

**Setup:** Cs-L provides melodic material. Hermod+ pitch CV drives loop transposition via V/Oct. Hermod+ gate output automates Record start and stop, triggering new recording passes at musically timed intervals. Loop Mode is set to Frippertronics. Shift+Start controls the decay rate for older layers.

**Controls:** Begin with an initial recording to set the loop length. Each subsequent Record pass adds new material while reducing the amplitude of existing content. The first overdub begins to quiet the original recording; after three or four passes, the original phrase has faded significantly while recent layers remain prominent. The loop is never the same twice because what decays and what accumulates changes with each recording. Adjust the Shift+Start decay rate to change how quickly older material disappears: slow decay allows many generations of material to coexist, fast decay produces a loop that forgets its history quickly. Change the Hermod+ pitch CV to shift V/Oct and transpose the loop between recording passes.

**Result:** A continuously evolving loop that accumulates new melodic content while earlier content fades, implementing the original Frippertronics technique with CV-automated recording transitions and real-time pitch transposition.

---

### Patch 3: Slice and Skip Rearrangement

Recorded phrase divided into slices with Skip introducing transformations, Nova output clocking external modules to the slice structure.

```
[Chord V2 Mix Out] ──────────────────────▶ [Stardust Left In]
[Hermod+ Clock Out] ─────────────────────▶ [Stardust Clock In]

                                            [Record one 4-bar phrase]
                                            [Play/Pause to set loop]

                                            Loop Mode: Sound on Sound
                                            Slice: 11 o'clock (8-16 slices)
                                            Skip: 10 o'clock (zones 1-3 active)
                                            Effect Mode: Tape Emulation (blue)
                                            Flutter: 10 o'clock

[Stardust Nova Out] ─────────────────────▶ [Hermod+ Clock In]

                                            Nova mode: Spark (end-of-slice gates)

[Stardust Left Out] ─────────────────────▶ [MixUp CH2 L]
[Stardust Right Out] ────────────────────▶ [MixUp CH2 R]
```

**Setup:** Chord V2 provides a harmonic source phrase. Hermod+ clock syncs Stardust's Clock Mode for quantized slice behavior. Record a single 4-bar phrase with Chord V2 as the source. After setting the loop, engage Slice and Skip.

**Controls:** Slice at 11 o'clock divides the loop into 8 to 16 evenly spaced splice points. Skip at 10 o'clock activates the first three transformation zones: start position offset, random reversal of slices, and micro pitch changes per slice point. The recorded phrase plays back as a rearranged version of itself, with some slices reversed, some offset, and some with subtle pitch variation. Nova set to Spark outputs a gate on each slice transition, which feeds back into Hermod+ as a clock input, syncing Hermod+ to Stardust's slice rate. Raise Skip further to introduce octave jumps (zone 4) and random semitone changes (zone 5). Lower Slice to reduce the number of splice points and hear the rearrangement become coarser.

**Result:** A recorded phrase rearranged continuously by Stardust's slice and skip engine, with Nova output synchronizing Hermod+ to the slice structure so the rest of the patch follows Stardust's internal rhythm.

---

### Patch 4: CV-Animated Playback Window

Start and Size CV modulated independently by Zadar, creating a loop that continuously navigates different regions of a recorded buffer.

```
[Cs-L Sine Out] ─────────────────────────▶ [Stardust Left In]

                    [Record 16-32 bars of slowly evolving material]
                    [Play/Pause to set loop]

[Zadar CH1] ─────────────────────────────▶ [Stardust Start CV]
(slow envelope, 20-40 seconds, infinite repeat)

[Zadar CH2] ─────────────────────────────▶ [Stardust Size CV]
(different shape, 12-25 seconds, infinite repeat)

[Hermod+ CV Out] ────────────────────────▶ [Stardust V/Oct]

                                            Loop Mode: Sound on Sound
                                            Start: 12 o'clock (base)
                                            Size: 2-3 o'clock (moderate base)
                                            Mix: 2 o'clock (mostly wet)
                                            Effect Mode: Tape Emulation (blue)
                                            Flutter: 10 o'clock

[Stardust Nova Out] ─────────────────────▶ [External module CV]
(Nova mode: Orbital, playback position CV)

[Stardust Left Out] ─────────────────────▶ [MixUp CH3 L]
[Stardust Right Out] ────────────────────▶ [MixUp CH3 R]
```

**Setup:** Record a long, slowly evolving phrase from Cs-L; 16 to 32 bars of material provides enough buffer content for meaningful navigation. Zadar CH1 in infinite-repeat mode slowly modulates the Start CV, moving the loop start point through the buffer. Zadar CH2 independently modulates the Size CV, changing the loop window length. Both channels run at different rates so the two parameters evolve asynchronously.

**Controls:** Once the buffer is recorded and the Zadar modulation is running, Stardust plays back different regions of the recording at changing window sizes, continuously. The combination of shifting Start position and changing Size length means the playback window visits different sections of the buffer at different durations with no repeating pattern. Hermod+ pitch CV into V/Oct adds transposition to the already-navigating window. Nova set to Orbital outputs a CV proportional to the current playback position within the loop, which can be routed to a filter cutoff or VCA CV to create loop-position-driven modulation on external modules.

**Result:** A long recorded buffer explored continuously by two independently modulated window parameters, producing a loop that sounds different on every pass without any new source material, with Nova Orbital CV available for synchronizing external modulation to the playback position.

---

## Common Mistakes

### "The loop ends abruptly at the wrong point."

The loop end point is determined by how long recording continued before Play/Pause or a second Record press was used to set it. If the loop is shorter or longer than intended, there is no way to adjust the end point after the fact without re-recording.

**Fix:** Use Play/Pause to end the initial recording rather than pressing Record a second time. Play/Pause sets the loop point precisely at the moment of the button press, and also continues recording audio tails past the loop point if the source has a natural decay. Re-record the initial phrase if the loop point is wrong, using Erase to clear the buffer and start fresh.

---

### "Overdubs are accumulating and I cannot remove a specific middle layer."

Undo removes only the most recent recording layer, not a specific earlier layer. There is no way to target a layer in the middle of an overdub stack for removal.

**Fix:** Use Undo immediately after a recording pass that does not work. If an earlier pass needs to be removed, Undo must be used before any subsequent recording is made on top of it. Plan overdub sessions by committing each layer before adding the next, using Undo as a single-step safety valve rather than a multi-layer undo history.

---

### "Frippertronics mode is not decaying older content."

Frippertronics decay only occurs when new recordings are actively made into the buffer. With Loop Mode set to Frippertronics but no new recording passes being made, the existing loop plays back without any decay.

**Fix:** Frippertronics requires active recording passes to trigger the decay. Set up a gate source into the Record gate input (or use the Record button manually) to trigger regular recording passes while playing new material into the input. Adjust the decay rate via Shift+Start to control how quickly older layers fade between each recording pass.

---

### "Slice is dividing the loop but playback sounds identical to no slices."

Slice sets the splice point structure, but it does not produce audible rearrangement on its own. Skip must be raised to introduce actual transformations at the splice points. With Skip at zero, the splice structure exists but no transformations are applied.

**Fix:** After setting Slice, raise Skip to activate transformation zones. Start with Skip at 9 o'clock to introduce subtle start position offset and occasional slice reversal. Increase Skip further to add pitch changes and octave jumps. The rearrangement becomes audible once Skip has reached zone 2 or zone 3.

---

## Advanced Learning Path

1. Learn the four transport controls (Record, Play/Pause, Reset, Reverse) and the Undo button in isolation before adding any effects, Slice, or CV control. Record, set a loop, overdub, and undo until the core workflow is second nature. Stardust has many layers of capability, but all of them require the loop to be established and managed correctly first.

2. Explore each Loop Mode with the same recorded content. Record a phrase, then switch through Sound on Sound, Replace, Frippertronics, and Resample while making additional recordings, and listen to how each mode handles the relationship between the new recording and the existing buffer. These four modes produce fundamentally different results from identical source material and overdub actions.

3. Learn Varispeed range modes via Shift+Varispeed Click. Semitones, Unquantized, Octaves and Fifths, and Octaves Only each produce a different relationship between encoder position and pitch. Octaves and Fifths is particularly useful for transposing loops through harmonically related intervals without leaving key.

4. Explore Start and Size as a manually controlled playback window before adding CV. Set a long initial recording (16 or more bars), then experiment with Start and Size knobs to navigate different regions of the buffer at different lengths. This direct experience with what the window parameters do makes CV modulation of those parameters meaningful rather than opaque.

5. Use Nova in Orbital mode routed to a filter cutoff or VCA CV and listen to the relationship between loop playback position and the modulated parameter. Nova Orbital produces a ramp that rises and falls with the loop, which means modulated parameters track the loop's internal time position. Switching Nova to Spark and routing it to a clock input shows how Stardust can become a rhythmic master clock for the rest of the patch.

6. Explore Slice and Skip systematically by starting with a high Slice value and Skip at zero, then slowly raising Skip through each transformation zone. Listen to each zone individually before adding the next. The Skip transformation zones stack, so understanding each zone before layering them allows deliberate use of rearrangement complexity rather than undifferentiated randomness.

7. Use the Resample loop mode after a complex session of Slice, Skip, Varispeed, and effect processing. Resample bakes the current mangled state into a new source recording, which then becomes the starting point for another cycle of manipulation. The original source material can be transformed several generations deep by repeating this process, each Resample becoming the new raw material.

## Pairs Well With

**Squarp Instruments Hermod+** provides transport automation and pitch control for Stardust simultaneously. Gate outputs from Hermod+ sequences can trigger Record starts, Resets, and Freeze gates at musically precise intervals, removing the need to manually press transport buttons during a live patch. The 1V/oct pitch CV output into Stardust's V/Oct input transposes the entire loop in real time through diatonic or chromatic pitch sequences. Running Hermod+ clock output into Stardust's Clock input syncs Slice, Skip, and Record behaviors to the patch tempo, keeping Stardust's internal rearrangements in rhythmic relationship with everything else.

**Xaoc Devices Zadar** provides the independently paced, non-repeating modulation that Start and Size respond best to. Two Zadar channels in infinite-repeat mode, each with a different envelope shape and rate, move the playback window through the buffer asynchronously: Start shifts the loop start position on one timescale while Size changes the window length on another. A third Zadar channel into V/Oct changes the loop pitch on a third timescale. Three Zadar channels animating three Stardust parameters simultaneously produce continuous playback variation from a single fixed recording without any new source material.

**Instruo Cs-L** is a strong source instrument for Stardust because its complex oscillator output has enough harmonic richness and textural variation across a phrase to make long buffer recordings meaningful to navigate. Cs-L's multiple waveform outputs (sine, saw, sub, fold) can be recorded on separate passes in Sound on Sound or Frippertronics mode to build a harmonically layered loop from a single oscillator. With Hermod+ providing pitch CV to both Cs-L and Stardust's V/Oct simultaneously, pitch sequences drive both the source material and the transposition of the loop in parallel.

**Instruo Arbhar** relates to Stardust as a complementary tool in the same temporal domain. Arbhar granularizes incoming audio in real time; Stardust loops and layers recorded audio over time. Routing Stardust's loop output into Arbhar's input applies granular deconstruction to the layered loop content, breaking the loop into grain clouds that retain the harmonic character of the recorded material while losing its linear structure. The reverse direction, recording Arbhar's granular output into Stardust, builds a loop from granularized source material that Stardust then layers, transposes, and rearranges. Either direction produces meaningfully different results.
