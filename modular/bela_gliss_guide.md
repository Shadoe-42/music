---
title: Bela Gliss
manufacturer: Bela
primary_role: CONTROLLER
secondary_roles: [MODULATOR]
historical_context: true
form_factor: eurorack
functions: [sequencer, function-generator, cv-processor]
behavior_tags: [performance-oriented, reactive, sensitive, stable, gated, generative]
use_cases: [custom LFO and modulation source, gate and trigger source, pitch CV source, CV scaling and utility]
hp: 4
memory: basic
transport: receive
screen: false
hybrid: false
cv: full
---

# Bela Gliss

**A touch controller for modular synth**

![Bela Gliss](https://github.com/Shadoe-42/music/raw/main/modular/images/bela/gliss/front_panel.jpg)

## Historical Context

The idea that a musician's body should be in continuous, expressive contact with the instrument it controls is as old as music itself. When the first electronic instruments appeared in the early twentieth century, this relationship became a design problem rather than an assumed given. Leon Theremin's eponymous instrument, developed in the Soviet Union and patented in the United States in 1928, solved it by eliminating physical contact entirely: the player's hands move through space relative to two antennae, generating capacitance shifts that the circuit translates into pitch and volume. Clara Rockmore's virtuosic performances demonstrated that gestural control without tactile feedback could produce phrasing, vibrato, and dynamic shaping indistinguishable in expressiveness from acoustic bowed strings. Theremin's invention also established a design principle that would persist: that position and intensity are the two most musically relevant dimensions of a human gesture, and that capturing both simultaneously produces a controller of extraordinary musical utility.

The parallel lineage of ribbon controllers runs from Maurice Martenot's Ondes Martenot, introduced in France in 1928 in the same year as the Theremin's patent, through several decades of continuous development. Martenot's instrument included two playing modes: a keyboard for discrete pitches and a ribbon with a sliding ring that allowed continuous glissando between any frequencies the player could reach. The ribbon mode tracked finger position along its length and produced whatever pitch voltage the position corresponded to, a direct ancestor of the touch strip in every contemporary module that claims the term. Don Buchla arrived at a similar conclusion from a different direction in San Francisco in the early 1960s, refusing the piano keyboard entirely when designing the first Buchla Series 100 synthesizer around 1963 to 1964. Buchla's touch-sensitive plates used capacitance to detect both contact and pressure, producing two independent CV signals from a single gesture. His argument was that the keyboard was a latency-inducing translator between intention and sound, that removing it would allow the instrument to respond to musical thought rather than to practiced mechanics. His Music Easel of 1973 refined this to its most portable and teachable form and remains the clearest statement of what a gestural controller in a modular context can be.

The third contributing lineage is the category of CV processing utility. As modular synthesis matured through the 1970s and 1980s, a standard division of labor emerged: performance controllers generated pitch and gate information, and a parallel set of modules (LFOs, envelope generators, random sources, sample and hold circuits) generated the time-varying modulation that made synthesized sound interesting over its duration. These two categories rarely overlapped. A performer controlled the pitch; the modulation ran autonomously on its own schedule. The result was a structural separation between what the performer touched and what the synthesizer did in response, a separation Buchla had identified as a problem and which subsequent designers largely accepted as a given. The question of what a synthesizer would sound like if the modulation itself were gestural, if the LFO shape were drawn by hand in real time rather than derived from a fixed waveform, remained largely unexplored at the module level.

Bela, a UK-based hardware and software platform founded in 2016 for real-time audio and sensor interaction, developed the Trill family of capacitive touch sensors as part of their broader work on interactive instrument design. Trill sensors provide sub-millimeter position tracking and touch size measurement across a strip surface, the same two-dimensional gestural data that Theremin captured through antennas and Buchla captured through conductive plates. The Gliss, released in 2023, applies this sensor technology to a 4HP eurorack module organized around four performance modes, each of which exploits the position-plus-pressure data in a different musical direction. Its Record mode is the most significant departure from prior art: the performer draws a gesture on the touch strip and the module loops it as a custom modulation signal, making the LFO shape a performance parameter rather than a circuit constant. The gesture is the modulation. What Buchla proposed as a philosophy of instrument design, Gliss extends into the domain of synthesis automation itself.

---

## Quick Start

Bela Gliss is a capacitive touch controller with a large vertical Touch Strip and one button, offering four distinct performance modes: Control (real-time CV from touch position and pressure), Record (gesture recording and looped playback), Signal (CV and audio processing), and Notes (a tunable 5-note keyboard or step sequencer). The Touch Strip senses both finger position along its length with sub-millimeter accuracy and touch size (the area of fingertip contact, equivalent to pressure), producing two independent but related signals simultaneously from every gesture.

1. Power up Gliss. The module starts in Control mode.
2. Connect the Top Output to the V/Oct input of a VCO (Cs-L, Castor and Pollux II, or Swarm).
3. Connect the Bottom Output to a VCA CV input.
4. Slide one finger along the Touch Strip. The Top Output tracks position; the pitch of the VCO rises and falls with your finger.
5. Press harder on the strip. The Bottom Output tracks touch size; the VCA opens.
6. Lift your finger. By default both outputs drop to 0V (unlatched behavior).
7. To switch modes, hold the Button, tap the strip with two fingers, release the Button. Tap the green zone at the top of the strip to cycle through Control, Record, Signal, and Notes.
8. Press the Button to return to performance.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 4 HP |
| Depth | 27 mm |
| Power | 150 mA +12V / 30 mA -12V / 0 mA +5V |

The voltage range for all inputs and outputs is -5V to +10V. The default range is 0V to +10V and is configurable per mode through the voltage range menu.

---

## Essential Parameters

**Touch Strip: Position and Touch Size.** The Touch Strip is the primary interface. It tracks finger position along its full length with sub-millimeter accuracy, producing a voltage from the minimum to maximum of the configured output range as your finger moves from bottom to top. Simultaneously, it measures touch size — how much of your fingertip contacts the surface — as an independent signal. Pressing harder spreads more fingertip area across the capacitive pads and produces a higher touch size voltage; pressing lightly or grazing the surface produces a small or zero reading. In most modes, position is assigned to the Top Output and touch size to the Bottom Output, but in Dual Slider and Dual Touch configurations this relationship changes. The 23 LEDs visible through the faceplate display the current output state in real time; in Control mode a red indicator tracks your finger, and in Signal mode the same LEDs function as an oscilloscope or VU meter.

**The Button.** The illuminated button serves different functions in each mode: arming recordings, triggering gesture playback, navigating menus, and latching output values. In Control mode, pressing the Button while a finger is on the strip latches the current output voltage and holds it after your finger lifts, functioning as sample-and-hold for the gesture value. In Record mode, the Button arms recording, triggers one-shot playback, and erases gestures. Its color indicates mode state: green is standard operation, red indicates recording or clipping is active, and yellow signals a specific menu state.

**Voltage Range Selector.** Each of the four performance modes stores its own input and output voltage ranges independently, and these ranges persist through power cycles. The defaults are 0V to +10V for all three jacks. To customize: enter the menu, tap the blue/white zone at the bottom of the strip, then tap the zone for Input, Top Output, or Bottom Output individually. Cycle through presets (0V to +10V, -5V to +5V, 0V to +5V, -5V to +10V) or hold a zone for two seconds to set a custom range with two fingers. Setting the output range to -5V to +5V makes the Top Output suitable for bipolar modulation destinations; setting it to 0V to +5V matches standard V/Oct conventions for most oscillators.

**Control Mode: Latching.** Latching controls what happens when your finger leaves the strip. Unlatched means both outputs drop to 0V instantly. Latched holds the last position and touch size voltages until the next touch. Latch Position holds only the position voltage while touch size returns to 0V, which makes it possible to lock a pitch note while using the touch size signal as a retriggerable gate. On-the-fly latching is available in any latching mode by pressing the Button while a finger is on the strip; the output freezes at that moment when you lift, and pressing the Button again releases the latch.

**Record Mode: Playback Modes.** Record mode captures gestures up to 75 seconds in length and offers five playback behaviors. Loop plays the gesture continuously in a cycle; the speed matches the recorded duration and does not sync to external clock unless Clock mode is used. Trigger plays the gesture once per Button press or trigger signal, making recorded shapes behave as single-shot custom envelopes. Clock records gestures synchronized to a clock signal at the Input, snapping gesture lengths to the nearest clock tick for rhythmically locked loops. Wavetable plays the gesture at audio rate, with the Input accepting a 1V/oct pitch signal (0V = C2, 65.4 Hz); the recorded gesture becomes the waveform and the pitch CV determines the playback speed, turning Gliss into a voltage-controlled wavetable oscillator. Waveshaper maps the gesture length to the input voltage range, so the CV input scrubs through the recorded shape rather than looping it automatically — a smoothly rising envelope sweeps through the gesture from start to finish, and any other shape produces a corresponding transformation of the recorded content.

**Signal Mode.** Signal mode passes any incoming signal through the Touch Strip's LED display and makes it manipulable with two-finger touch. With two fingers on the strip in Active mode, the upper finger sets the maximum of a scaled output range and the lower finger sets the minimum; the input signal is rescaled to fill that window at the output. Pressing the Button activates clipping, which selects a portion of the incoming signal to pass through and rescales it to fill the output range — a performance-accessible form of compression for CV, or hard clipping distortion for audio. Signal mode accepts either DC-coupled CV signals (visualized as a moving dot, equivalent to a simple oscilloscope) or AC-coupled audio signals (visualized as a VU meter with level zones). The Bottom Output can carry the processed signal, its inverse, an envelope follower derived from the input, or the inverse of the envelope follower, depending on the Output Mode selector.

**Notes Mode.** Notes mode divides the Touch Strip into five tunable zones, each storing a user-defined voltage. In Keyboard configuration, touching a zone outputs its assigned voltage from the Top Output and touch size from the Bottom Output, with glissando available by sliding between zones and vibrato available by wiggling a finger on a held note. In Sequencer configuration, each zone becomes a step triggered by a clock at the Input; the Top Output sends the step voltage and the Bottom Output sends a trigger (+10V for step 1, +5V for subsequent steps). Each step is independently configurable as Active, Hold (sustain previous note), Mute (output 0V), or Skip (remove step from sequence). Notes can be tuned manually or by sending V/oct pitch CV into the Input and pressing the target zone — CV tuning is more reliable than manual sliding for achieving precise semitone values.

**Touch Sensitivity.** Global Settings (accessed by holding the Button and tapping the strip with three fingers) includes a Touch Sensitivity control that scales the gain applied to touch size readings. Increasing it makes pressure response more pronounced; decreasing it reduces sensitivity for situations where accidental pressure variations are causing unwanted output fluctuations. This is a global setting that applies across all modes.

---

## Why This Instrument Excels

The Touch Strip's simultaneous position and touch size measurement is architecturally different from anything that uses a single CV output for gestural control. A conventional ribbon controller or linear slider maps position to one voltage and provides nothing else. Gliss maps position to one output and touch size to a second output that moves orthogonally to the first, meaning that a finger held at a fixed position can still produce a continuously variable second signal by varying pressure. These two signals are not independent: they come from the same physical gesture, so there is an inherent relationship between where your finger is and how hard you are pressing that produces a particular kind of expressive simultaneity. Pitch and velocity, filter cutoff and resonance, LFO rate and depth — any two parameters that you want to adjust together in a gesture-linked way can be assigned to position and touch size respectively without any additional patching. The module is two performance controllers that share a single physical interaction.

Record mode's Loop playback is the deepest reason to own a Gliss even in a system that already has LFOs and function generators. The problem with fixed-waveform LFOs is that their shapes are determined by the circuit and their rates are set with a knob: you can approximate what you want, but you cannot draw it. Record mode inverts this completely. The modulation shape comes first, drawn by hand in one pass, and then loops at whatever rate it was drawn. A slow gesture produces a slow LFO; a fast one produces a fast one. The shape is exactly what was drawn: an asymmetric rise with a notch at the top, a gentle plateau with a quick drop, a series of irregular bumps separated by pauses. None of these shapes exist in a standard LFO module, and all of them can be drawn in a few seconds. More importantly, they can be redrawn at any time, so the modulation source itself becomes a live performance parameter rather than a background setting. This is what Buchla was gesturing toward: a synthesis environment where time-varying modulation is something a performer shapes with their body, not something a module generates autonomously.

Wavetable mode is a minority use case that rewards investigation because the resulting oscillator sounds like nothing else in the rack. The waveform is whatever shape the performer draws on the strip. A simple stroke from bottom to top and back produces a triangle-adjacent shape. A quick series of bumps produces dense harmonic content. Drawing a shape that starts and ends at the same strip position produces a looping waveform with minimal DC offset and a relatively smooth spectrum; drawing one that starts and ends at different positions produces a hard discontinuity at the loop point that adds sharp transients and odd-order harmonic character. The pitch is tracked by a V/oct input, so it integrates with a sequencer as cleanly as any other oscillator. The difference is that the waveform is not a fixed circuit property but a parameter the performer shapes by touch, updateable at any time by drawing a new gesture onto the strip. Two Gliss modules in Wavetable mode with independent drawn waveforms, both driven by the same pitch CV, produce two simultaneously detunable voices with sonically unrelated timbres derived from the same pitch relationship.

Signal mode extends Gliss's utility into the domain of CV and audio manipulation during performance without adding patch cables. The scale-and-offset operation that would ordinarily require an attenuverter, a DC offset source, and two or more cables to accomplish can be applied live with two fingers on the strip and adjusted fluidly without leaving the current patch state. Clipping a CV signal rescales the selected voltage window to fill the output range, which functions as a real-time compander for control voltages: narrowing the selected window increases effective CV gain, widening it reduces it. Clipping audio produces hard distortion in the selected amplitude window, independently adjustable for positive and negative halves of the signal — asymmetric clipping with continuously variable threshold, accessible by touch during performance. For visualizing signals in a small system without a dedicated oscilloscope, the Signal mode display gives enough information to distinguish a slowly moving CV from a fast one, to see whether an audio signal is clipping, and to verify that a modulation source is producing output before committing a cable to a destination.

---

## Patches

### Patch 1: Expressive One-Touch Voice

Gliss in Control mode as both pitch source and dynamic gate, using finger position for pitch and touch size for amplitude, turning the Touch Strip into a complete performance interface for a single voice.

```
[Gliss Top Output] ──────────[C]──────▶ [Cs-L V/Oct In]
[Gliss Bottom Output] ───────[C]──────▶ [VCA CV In]

[Cs-L Audio Out] ────────────[A]──────▶ [VCA Audio In]
[VCA Audio Out] ─────────────[A]──────▶ [MixUp CH1]

                                         Control Mode: Single Slider
                                         Latching: Latch Position
                                         Top Output range: 0V to +5V
                                         Bottom Output range: 0V to +5V
```

**Setup:** Set the Top Output voltage range to 0V to +5V to match standard V/Oct convention for two to three octaves of pitch travel across the strip's length. Set the Bottom Output range to 0V to +5V to drive the VCA cleanly. Configure Latching to Latch Position so that the Cs-L pitch holds when your finger leaves the strip, but the Bottom Output (and therefore the VCA) closes when pressure releases. This creates a natural gate: touch opens the voice, position controls pitch, and releasing your finger cuts the sound while holding the last pitch voltage.

**Controls:** Slide slowly for melodic movement and quickly for pitch jumps. The full length of the strip spans approximately two and a half octaves at the 0-5V range; adjust the Top Output maximum for narrower or wider pitch ranges. Touch size sensitivity is set in Global Settings; raise it if gentle pressure is not producing enough VCA opening. Pressing harder at a fixed position opens the VCA further without moving the pitch, which allows dynamic shaping by pressure alone. With Latch Position active, you can release and re-touch at the same point to retrigate the VCA without changing pitch, producing staccato articulation at a held note.

**Result:** A gesture-controlled monophonic voice where pitch is a positional parameter and note duration is a pressure parameter. No sequencer, no gate source, no separate CV controller: the touch strip plays all three roles simultaneously.

---

### Patch 2: Drawn Custom LFO

Gliss in Record mode with Loop playback, drawing a modulation shape by hand and looping it to Nautilus's Resolution CV input and Aurora's Warp CV simultaneously, creating a modulation source with an exact user-defined shape.

```
[Gliss Top Output] ──────────[C]──────▶ [Nautilus Resolution CV]
[Gliss Bottom Output] ───────[C]──────▶ [Aurora Warp CV]

                                         Record Mode: Single Slider
                                         Playback: Loop
                                         Top Output range: 0V to +5V
                                         Bottom Output range: 0V to +5V
```

**Setup:** Set both output ranges to 0V to +5V for useful modulation depth at both destinations. Touch the strip and draw a shape: a slow rise with a sudden drop, an irregular plateau, a short burst followed by a long quiet section. Lift your finger and Gliss immediately loops the recorded shape. The Top Output carries the position component of the gesture (the path your finger traced) and the Bottom Output carries the touch size component (how hard you pressed at each point), giving each destination a distinct but temporally related modulation signal from the same physical gesture.

**Controls:** The loop plays back at the same speed it was recorded. A gesture drawn over five seconds produces a five-second LFO; a gesture drawn over one second produces a one-second LFO. To change the shape, simply draw again: a new touch overwrites the previous recording. To change the rate, draw the same shape faster or slower. To return to the same shape at a different rate, you need to redraw; there is no playback speed control in Loop mode independent of recording speed. If you need tempo-synchronized loops, switch to Clock mode and feed the Input a clock from Hermod+. The Bottom Output's touch size dimension produces a shape correlated to but distinct from the position shape, because pressure and position are independent physical gestures — you can draw an arching position path while holding constant pressure, or trace a flat position while gradually increasing pressure.

**Result:** Two simultaneous custom modulation signals derived from a single drawn gesture, both looping at the same user-set period. Nautilus's delay timing and Aurora's spectral processing evolve together at a rate and in a shape that no fixed LFO waveform can replicate, because the shape was invented by the performer on the strip rather than selected from a menu.

---

### Patch 3: Gestural Wavetable Oscillator

Gliss in Record Wavetable mode as a voltage-controlled oscillator whose waveform is drawn by hand, driven by Hermod+'s pitch CV and mixed against Cs-L for timbral contrast.

```
[Hermod+ Pitch CV Out] ──────[C]──────▶ [Gliss Input]
[Hermod+ Pitch CV Out] ──────[C]──────▶ [Cs-L V/Oct In]

[Gliss Top Output] ──────────[A]──────▶ [MixUp CH1 L]
[Cs-L Audio Out] ────────────[A]──────▶ [MixUp CH2]

                                         Record Mode: Single Slider
                                         Playback: Wavetable
                                         Top and Bottom Output range: -5V to +5V
```

**Setup:** Set both output ranges to -5V to +5V so the outputs span a full bipolar audio range. The Input voltage range setting is ignored in Wavetable mode; it always interprets the input as a 1V/oct pitch signal. Draw a waveform onto the Touch Strip: touch the strip, trace a shape from one end to the other (or any path you choose), and lift. The drawn shape immediately becomes the waveform. For a relatively clean tone, start and end the gesture at approximately the same vertical position on the strip, so the waveform's start and end values match and the loop point does not produce a hard click. For a brighter, harmonically richer tone, start at the bottom and end at the top or vice versa: the loop discontinuity adds harmonic content equivalent to a wave with significant upper partial energy. Hermod+ pitch CV drives both Gliss's wavetable playback speed and the Cs-L's pitch simultaneously, keeping the two voices in tune.

**Controls:** Update the waveform at any time by drawing a new shape on the strip. The pitch CV changes the playback frequency in 1V/oct increments: 0V produces C2 (65.4 Hz), each volt above adds an octave. The drawn waveform's timbral character can be changed dramatically by redrawing: a single broad arc produces a waveform with low harmonic content; a jagged series of peaks produces dense and bright character. Set the MixUp channel faders to balance Gliss against the Cs-L, which provides a stable reference pitch for comparison. The two voices will have related pitch but unrelated timbre, producing a layered texture that changes timbral character every time a new waveform is drawn without disrupting the melodic sequence.

**Result:** A sequenced two-voice patch where one oscillator has a user-definable waveform, updateable by gesture at any point during performance. The Gliss voice is entirely unlike any fixed-waveform oscillator in the rack because its spectrum is shaped by whatever shape was last drawn.

---

### Patch 4: Five-Step Sequencer with Live Step Control

Gliss in Notes Sequencer mode as a five-step CV sequencer, with Hermod+ providing the clock and Zadar receiving per-step triggers, with live step muting and reordering during performance.

```
[Hermod+ Clock Out] ─────────[G]──────▶ [Gliss Input]

[Gliss Top Output] ──────────[C]──────▶ [Cs-L V/Oct In]
[Gliss Bottom Output] ───────[G]──────▶ [Zadar Trigger CH1]

[Zadar CH1 Env Out] ─────────[C]──────▶ [VCA CV In]
[Cs-L Audio Out] ────────────[A]──────▶ [VCA Audio In]
[VCA Audio Out] ─────────────[A]──────▶ [MixUp CH1]

                                         Notes Mode: Sequencer
                                         Quantisation: ON
                                         Variable (Selector 3): glide amount
                                         Tune notes via Hermod+ V/Oct to Input
```

**Setup:** Tune the five notes by entering tuning mode (press Button three times rapidly). Connect Hermod+'s pitch CV to the Gliss Input and press each of the five strip zones while sending the target pitch from Hermod+. Start with a pentatonic or modal set of five pitches within two octaves, tuning bottom to top in ascending order. After tuning, the Bottom Output sends a trigger at each active step: +10V for the first step in the sequence and +5V for subsequent steps. Both values trigger Zadar reliably. Zadar's envelope shapes the VCA for each note event.

**Controls:** While the sequence runs, tap any step on the strip to jump the sequence position to that step. The sequence continues looping from the tapped step, allowing real-time reordering without stopping. To configure step states, press the Button twice while in Active Mode: the steps pulse, and each tap cycles a step through Active, Hold, Mute, and Skip. Mute leaves the step in the sequence as a rhythmic rest (0V output, no trigger). Skip removes it entirely, reducing sequence length. Hold sustains the previous note through the step without triggering Zadar. The Selector 3 glide control in the Menu sets the slew between steps; increasing it smooths the pitch transitions into portamento. Retune any step live by pressing the Button three times during playback, touching the step to retune, and sliding to adjust.

**Result:** A five-step sequencer where every aspect of the sequence (step order, step states, step tuning, inter-step glide) is adjustable during performance by touch, without opening a menu. The Bottom Output's dual-voltage trigger (+10V on step 1, +5V otherwise) allows Zadar to use the sequence downbeat as a reset trigger if patched to the Zadar channel's CV input, creating envelope-length variation that marks phrase boundaries.

---

## Common Mistakes

### "The pitch output is jumping all over the place when I barely move my finger"

The default voltage range for the Top Output is 0V to +10V, which spans ten volts across the full length of the strip. This is too wide for pitch control in most applications: a few millimeters of finger movement covers a semitone at V/Oct scaling, making the strip extremely sensitive to small positional errors. The strip is physically accurate, but the range makes that accuracy difficult to use.

**Fix:** Reduce the Top Output voltage range for Control mode to 0V to +5V (two and a half to three octaves) or a custom narrow range if you want even finer pitch control. Enter the menu, tap the voltage range selector, tap the Top Output zone, and cycle to 0V to +5V. This doubles the physical distance per semitone and makes the strip significantly more playable for pitch.

---

### "I draw a gesture in Record mode but the loop plays too fast or too slow"

Record mode Loop playback plays the gesture at exactly the speed it was drawn. The loop duration is the elapsed time from when your finger touched the strip to when you lifted it. There is no playback rate control in Loop mode that is independent of the recorded gesture duration.

**Fix:** Redraw the gesture at the speed you want the loop to run. For a four-second LFO, draw for four seconds. For sync to external tempo, use Clock mode with a clock from Hermod+ at the Input. Clock mode snaps the recorded gesture length to the nearest clock tick count, so the loop length becomes a musical division of the clock rather than a freely drawn duration.

---

### "Wavetable mode sounds buzzy and harsh when I want a smooth tone"

When a drawn gesture starts and ends at different vertical positions on the strip, the waveform has a discontinuity at the loop point. Each time the wavetable cycles back to the beginning from the end, it jumps abruptly from the ending voltage to the starting voltage. This jump in the waveform is equivalent to a hard edge, which adds significant high-frequency harmonic content and produces the buzzy character.

**Fix:** Start and end your drawn gesture at approximately the same position on the strip. The loop point will then be a smooth continuation rather than a jump, and the resulting waveform will have significantly fewer high-frequency partials. If you want harmonic richness without the buzziness, draw a shape with internal curves and peaks but return to the starting position before lifting your finger.

---

### "Signal mode is not scaling my CV — the output is the same as the input"

Scaling and offsetting in Signal mode requires two fingers on the Touch Strip simultaneously in Active Mode (not in the Menu). Many users attempt to scale by touching with one finger, which in Signal mode simply observes the incoming signal without modifying it.

**Fix:** Ensure you are in Active Mode (press the Button to exit the Menu if necessary). Place two fingers on the strip simultaneously. A gold marker appears under the upper finger (representing the scaled maximum) and a gold marker under the lower finger (representing the scaled minimum). Spread or contract your fingers to set the scaling window. The signal visible between your fingertips is the input range that will be rescaled to fill the full output voltage range. Lift both fingers to store the scaling and return to normal display.

---

### "I cannot get the Notes mode keyboard tuned accurately by sliding my finger"

Manual tuning in Notes mode requires dragging a finger precisely to the target voltage, and Gliss responds to very small position changes. Achieving exact semitone precision by manual sliding alone is difficult enough that the manual explicitly warns about it and offers a workaround.

**Fix:** Use CV input tuning rather than manual sliding. Connect Hermod+'s pitch CV output to the Gliss Input. Set Hermod+ to output the desired pitch voltage for each note, enter Notes tuning mode (press the Button three times rapidly), then press the strip zone you want to tune to that voltage. The voltage from the Input is stored directly into that zone without any manual sliding ambiguity. Tune all five zones this way. If you must tune manually, enable Quantisation (Selector 2 in the Notes menu) to step the tuning to semitone intervals, which makes it significantly easier to land on the correct pitch.

---

### "The touch size output barely responds even when I press firmly"

Touch size response depends on skin capacitance, which varies considerably between people, environments, and skin moisture levels. The default sensitivity may produce insufficient touch size voltage for some users pressing what feels like a firm touch.

**Fix:** Open Global Settings (hold the Button, tap the strip with three fingers, release). The first selector is Touch Sensitivity. Tap it and a pointer appears on the strip. Slide upward to increase gain applied to the touch size signal. The Bottom Output previews the touch size voltage in real time while you adjust, so you can press the strip and watch the output change as you increase sensitivity until it responds appropriately to your touch.

---

## Advanced Learning Path

Begin in Control mode Single Slider with a VCO patched to the Top Output and a VCA to the Bottom Output. Work through all three latching settings — unlatched, latched, and latch position — and understand specifically what each one does to the gate behavior at the VCA and the held pitch at the VCO. The difference between latch position (pitch holds, gate closes) and latched (both hold) is subtle in the menu description but immediately audible in performance; building intuition about which you want for a given musical situation is the first competency Gliss rewards.

Spend time configuring voltage ranges for each mode independently before building complex patches. The range menu is the most commonly underconfigured aspect of the module, and the default 0V to +10V range is a reasonable starting point for very few applications. Set Control mode Top Output to 0V to +5V for pitch; set Record mode outputs to -5V to +5V for bipolar modulation destinations; set Notes mode Top Output to match the pitch range of whatever oscillator you are driving. Understanding that each mode stores its own ranges, and that changes to one mode's range do not affect others, prevents the confusion that results from switching modes and finding the voltage behavior unexpected.

In Record mode, work through the five playback modes in order: Loop first, then Trigger, then Clock, then Wavetable, then Waveshaper. Each one is a different answer to the question of how a recorded gesture should be reproduced, and they differ more than the menu labels suggest. Loop is a continuous autonomous cycle. Trigger is a one-shot event triggered externally. Clock is tempo-synchronized looping. Wavetable is audio-rate gesture synthesis. Waveshaper is voltage-scrubbed content access. Understanding when each mode is appropriate requires having experienced all five.

Explore the dual input types within Record mode. Single Slider gives you the full strip length for one gesture, with position on the Top Output and touch size on the Bottom Output. Dual Slider splits the strip into two halves, each recording independent position gestures with no touch size component. Dual Touch splits into two pressure-sensitive pads, recording touch size only with no position component. For LFO work, Single Slider usually produces the most musical results because it captures the full gesture as drawn. For two-envelope operation, Dual Slider in Trigger mode lets you draw different envelope shapes in each half and trigger both simultaneously.

Tune the Notes mode keyboard to a scale you do not normally use: a whole-tone scale, a diminished set, a quarter-tone series, a pentatonic built from unusual intervals. Notes mode's strength is that the five available pitches can be anything, and the glissando between them will slide through whatever voltage space lies between those notes. Playing a whole-tone keyboard with glissando active produces microtonal sliding between notes that are equidistant in frequency, a gesture impossible on a standard keyboard without pitch-bend hardware. Setting the output range narrowly (0V to +2V across the five notes) compresses all five pitches into a tight interval cluster for lead lines with minimal interval jumps.

Use Signal mode as a real-time CV scaling tool mid-performance. Patch a slowly moving LFO from another module into the Signal mode Input and scale it live with two fingers during a performance. Narrowing the two-finger window reduces the LFO's effective depth without changing its rate; widening it increases depth; shifting both fingers up or down offsets the LFO into a different voltage window. This replaces an attenuverter and DC offset module for situations where you want to modify a modulation source's effective range without stopping to repatch.

Try the Wavetable mode with the output range set to -5V to +5V and route both Top and Bottom Outputs to a stereo mixer with the VCA open. Record two very different waveform shapes for Single Slider (which puts position on Top and touch size on Bottom), then feed the same pitch CV from Hermod+ to drive playback rate. You now have two simultaneously audible waveforms with different timbral characters produced from the same pitch CV, without an additional oscillator module. The two timbres are related because they were drawn in the same gesture, but they are not identical, and the result has a richness that a single drawn waveform does not.

Combine Record Loop and Signal mode in the same patch by running the Gliss Top Output into the Signal mode Input of a second Gliss unit (or by patch-switching one Gliss between modes, which is less convenient). The first unit generates the looped gesture. The second unit scales and clips it in real time. This chain allows you to draw a fixed modulation shape and then perform its scaling and clipping envelope live without altering the recorded gesture, effectively separating the gesture creation from the gesture shaping into two interactive layers.

---

## Pairs Well With

**Instruo Cs-L** is the clearest pitch destination for Gliss's Control and Notes modes because its V/Oct tracking is linear and its audio quality means that whatever unusual pitch material Gliss produces is rendered faithfully. In Wavetable mode, Cs-L's audio makes an excellent comparison oscillator because its waveforms are fixed and clean: mixing the two voices directly reveals how much timbral difference a drawn waveform creates relative to a standard analog waveshape. The Cs-L's internal FM also responds to Gliss's Bottom Output in interesting ways when patch pressure is used to modulate timbre.

**Zadar** complements every mode in which Gliss produces gate or trigger output. In Notes Sequencer mode, Gliss's Bottom Output triggers Zadar with differentiated voltages (+10V on step one, +5V on subsequent steps), which Zadar can use to produce louder or more complex envelope responses on the downbeat without additional logic. In Record Trigger mode, Gliss's custom envelope can be cross-patched: Gliss draws the amplitude envelope, and Zadar handles a simultaneously triggered filter contour, allowing two distinct drawn shapes to fire on the same trigger.

**Qu-Bit Nautilus** receives Gliss's Record Loop output well at its Resolution CV input, because Resolution responds over a wide voltage range and the variation Gliss produces from an asymmetric drawn gesture creates timing irregularity that no standard LFO can replicate. The Sonar output from Nautilus in return makes an excellent candidate for Gliss's Signal mode Input, where the delay-state-derived CV can be observed on the strip, scaled, and clipped before being returned to another Nautilus CV input — a feedback loop where Gliss mediates the self-modulation depth.

**Qubit Aurora** pairs directly with Gliss in two configurations. Patching the Record Loop position output to Aurora's Warp CV produces spectral content that shifts according to the drawn gesture's path, so the spectral character of the reverb tail evolves according to whatever shape was drawn rather than following a sine wave or triangle. In Wavetable mode, passing the Gliss audio output through Aurora at high FFT sizes produces spectral blurring of the drawn waveform's harmonics, which is particularly effective with geometrically complex waveforms that have dense harmonic content the FFT processing can redistribute and sustain.

**Patching Panda Moon Phase** receives Gliss's Control mode Bottom Output as a filter cutoff CV source while position handles something else — pitch, or another parameter — using the pressure dimension of the touch gesture to control filter brightness. Pressing harder on the strip opens the filter; releasing pressure darkens the sound without changing pitch. Moon Phase's resonance responds cleanly to modest voltage excursions, so the 0V to +5V touch size range in Control mode is a good match for filter cutoff sweeps that remain musical rather than shrieking.

**Winterbloom Castor and Pollux II** provides a stable V/Oct pitch source in Gliss Notes mode tuning via CV input, which makes the tuning procedure straightforward: set Castor and Pollux II to output each target pitch in sequence, touch the corresponding strip zone in Gliss tuning mode, and the module stores the exact voltage. The Castor and Pollux II Thru output then passes the pitch downstream to a VCO while the Bottom Output from Gliss in Sequencer mode triggers envelopes for each step, allowing the two modules to divide the sequencing workload while sharing a pitch source.
