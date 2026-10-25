---
title: Erica Synths Pico QUANT
manufacturer: Erica Synths
series: Pico
primary_role: UTILITY
secondary_roles: []
historical_context: true
form_factor: eurorack
functions: [quantizer, cv-processor]
behavior_tags: [stable, nonlinear, reactive, clean]
use_cases: [turning random voltage into melody, playing microtonal and non-western scales, rhythm that follows pitch changes, making melodies restless or settled]
hp: 3
depth: 35mm
current_draw:
  plus12: 25mA
  minus12: 6mA
price_eur: 120
memory: basic
transport: none
screen: false
hybrid: false
cv: basic
inputs: [CLK IN, CV IN]
outputs: [CV OUT, CLK OUT]
patch_format: v1
---

# Erica Synths Pico QUANT

**CV quantizer with a tolerance control, quarter-tone accuracy, glide, a clocked mode, and web-designed scales in 3 HP**

![Erica Synths Pico QUANT](https://github.com/Shadoe-42/music/raw/main/modular/images/erica_synths/pico_quant/front_panel.jpg)
*Erica Synths Pico QUANT: TOLERANCE and GLIDE knobs, SCALE button with RGB LED, CLK IN, CLK OUT, CV IN, and CV OUT*

> **Draft status (2026-10-24):** Rebuilt from the official Pico QUANT manual (English, listed on the Erica Synths product page as dated April 23, 2018), the product page, and the live scale design page, before the module was patched for this guide. Specifications and control descriptions come from the manual. All four patches are untested and are marked ⚠️. Open items to clear on hardware: (1) every patch setting and every "What to listen for" result; (2) CLK OUT behavior when CLK IN is patched, which the manual does not describe; (3) whether the scale slots survive a power cycle; (4) the voltage range of Marbles X1 and the root note of the scales (Patch 4); (5) the layout of the live scale design page, which differs from the manual's description (see Scale Upload); (6) the CV OUT range, which the manual gives as 0 V to +8 V while the product page text is garbled. Remove this block when the items are cleared.

---

## Historical Context

A quantizer rounds an incoming control voltage to the nearest level in a set scale, the way a rounding step turns 2.75 into 3. The reason one is needed comes from the pitch standard. Moog popularized the one volt per octave standard in the 1960s, and under it a semitone is about 0.0833 V, so any source that makes arbitrary voltages makes arbitrary pitches. Perfect Circuit's quantizer primer describes the early answers: the EML 400 sequencer, which it calls one of the earliest modular quantizers and which offered scales of 5 to 60 steps per octave but could not quantize external voltages; the ARP 1601 sequencer of the 1970s, whose onboard quantizer snapped voltages to the nearest semitone and accepted external CV; and a Serge quantizer developed at the end of the 1970s, which the primer says the Doepfer A-156 appears to descend from. In each case the job was the same: put a source that was never meant to play notes in tune with a scale.

The other direction is the scale itself. Twelve equal steps is a convention, and the 1V/oct standard does not enforce it: a quarter tone is about 0.0417 V. Quarter-tone music has a long record on acoustic instruments. Ivan Wyschnegradsky became convinced that equal temperament was inadequate and made his early microtonal work on two pianos tuned a quarter tone apart. He moved to Paris in 1920, in part to develop instruments for microtones, and in 1921 Pleyel built a quarter-tone piano for him using its Pleyela player-piano system. Alois Hába and August Förster completed a quarter-tone keyboard in 1928, a Förster upright reached Wyschnegradsky's Paris apartment in 1929, and he published a manual of quarter-tone harmony in 1932. A quantizer that holds quarter-tone accuracy extends that work to a voltage-controlled rack.

Erica Synths is a Riga company built by Ģirts Ozoliņš, who grew up in the late Soviet era teaching himself amateur radio from a library book, later worked as a physics teacher, built an electronic kit for his son, and began making synthesizer modules at home, which grew into the company. The Pico series was a deliberate constraint. The manual opens with the challenge in the company's own words: "Can we make any superior functionality synth module 3HP wide and affordable? Yes, we can." The series page lists Pico QUANT alongside Pico Voice, Pico MScale, and Pico Mixer, at 120 euros before VAT for the quantizer, and Ozoliņš is credited with writing the user manual.

Pico QUANT extends the quantizer in three ways. A tolerance control sets how far the incoming voltage must travel before the output advances, a glide control smooths the steps, and a web-based tool uploads new scales to the module as audio, into eight slots, with quarter-tone resolution. It also runs with or without a clock, and it sends a trigger from CLK OUT each time the output changes. Together these turn a utility into a performance control: the same source and the same scale produce a restless line or a settled one depending on one knob.

---

## Quick Start: First Quantized Line in 5 Minutes

Pico QUANT takes a control voltage at CV IN and returns the nearest note of the selected scale at CV OUT. Feed it anything that moves, and the oscillator that receives CV OUT plays in key. ⚠️ Untested on hardware.

1. **Patch a slowly moving voltage into CV IN.** A slow LFO or a random source works. The input ignores negative voltages, so use a source that stays above 0 V.
2. **Patch CV OUT to the 1V/OCT input of an oscillator.** CV OUT runs from 0 V to +8 V.
3. **Leave the SCALE LED at black.** That is the Diatonic scale. Press the SCALE button once for the next scale, and note the LED color.
4. **Turn TOLERANCE fully counterclockwise.** The output steps to the next note about halfway between notes, so it follows the source closely.
5. **Turn TOLERANCE clockwise.** The output holds each note longer and steps only when the source is very close to the next note.
6. **Add GLIDE.** A small amount of clockwise turn slides between the notes. At fast sequences, the manual describes GLIDE as acting like a wet and dry control between quantized and unquantized.
7. **Patch a clock into CLK IN.** The manual describes this as clocked quantization.
8. **Patch CLK OUT to an envelope gate with CLK IN left empty.** The output fires a trigger each time the quantized note changes.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 3 HP |
| Depth | 35 mm |
| Power | 25 mA +12V / 6 mA -12V / 0 mA +5V |
| Controls | TOLERANCE, GLIDE, SCALE button |
| Inputs | CV IN, CLK IN |
| Outputs | CV OUT, CLK OUT |
| CV IN range | -10 V to +10 V (negative voltages are ignored) |
| CV OUT range | 0 V to +8 V |
| Glide time | 0 to 1 second |
| Minimum accuracy | 1/4 tone |
| Preset scales | 8, selected by the SCALE button |
| User scale slots | 8, filled by upload from the web tool |

The manual lists no +5V rail. The product page text for CV OUT amplitude and glide is garbled, so the table follows the manual. The manual's tolerance figure shows the output stepping at about the midpoint between notes at 50 percent and only near the next note at 10 percent.

---

## Essential Parameters

**TOLERANCE** sets how far the incoming voltage must travel before the output advances to the next note. The manual describes it as a CV range around a note in which the module advances to the next stage. Fully counterclockwise gives 50 percent tolerance: the output advances about halfway between two scale notes. Fully clockwise gives 10 percent: the output advances only when the incoming voltage is very close to the next note. The direction runs against the label. Clockwise means a smaller window and a more reluctant output, and counterclockwise means a larger window and a more eager one. As shorthand, think of counterclockwise as eager and clockwise as stubborn. The manual notes that the control is particularly useful when a random voltage or noise goes into CV IN, where it sets how busy the result sounds.

**GLIDE** sets the glide time between notes from 0 to 1 second. At slow settings it is portamento between quantized steps. For quick sequences, the manual describes it as working like a wet and dry control: counterclockwise is quantized, clockwise is not quantized.

**SCALE** is a button with an RGB LED. A short press steps through the eight scales, and the LED color shows which is active (see Preset Scales). Holding the button for two seconds enters scale upload mode, and the LED blinks red.

**CV IN** takes the unquantized voltage. The range is -10 V to +10 V, and negative voltages are ignored. A bipolar LFO therefore changes the output only during its positive half. **CV OUT** gives the quantized voltage from 0 V to +8 V, so the module covers roughly eight octaves at one volt per octave.

**CLK IN** is for clocked quantization. Patch a clock here and the module works as a clocked quantizer. The manual does not say more about the mechanism, so the guide treats the sample-on-clock behavior as the intended reading and marks it for confirmation. **CLK OUT** is a trigger output. The manual states that if nothing is patched to CLK IN, the output trigger appears on each CV step change. Its LED blinks on each CV change. The manual does not describe what CLK OUT does when CLK IN is patched. ⚠️

---

## Preset Scales

| LED color | Scale |
|-----------|-------|
| Black | Diatonic |
| Red | Double Harmonic Major (Arabian) |
| Yellow | Harmonic Minor |
| Green | Blues |
| Cyan | Diminished |
| Dark blue | Pentatonic |
| Magenta | Whole-tone |
| White | Chromatic |

The manual spells the cyan scale "Diminish." The eight slots hold the presets at delivery. Uploading a scale to a slot replaces what is there.

---

## Why Pico QUANT Excels

The module is best at domesticating unstable control voltage. Give it a random source, a noise signal, or a slow modulation voltage from a module that was never meant to play notes, and it returns something with melodic coherence while keeping the energy of the source. Nothing about the patch sounds composed. It sounds like a rack that plays in key without anyone choosing the notes. That is a different job from a sequencer, which stores notes. Here the source supplies the movement and the scale supplies the vocabulary.

The tolerance control is what makes the module a performance instrument and not just a filter. The same source, the same scale, and the same patch give a restless line when the knob is counterclockwise and a settled one when it is clockwise. The manual's own figure shows why: the output steps at the midpoint between notes at one end and only near the next note at the other. Turning the knob during a performance changes how the line behaves without changing a note in the scale, a gesture that few quantizers expose.

CLK OUT adds a second axis. With no clock patched, it fires a trigger each time the quantized note changes, which ties rhythm to pitch movement. Active pitch movement gives many triggers and quiet movement gives few, and a repeated note gives none. Patched to an envelope or a drum voice, it produces a voice whose hits follow the melody, and TOLERANCE then controls both melodic and rhythmic density at once. The manual mentions the output only briefly, but it changes what the module can do in a patch.

The scales are the last advantage, and they are open. The web tool uploads scales with quarter-tone accuracy into eight slots, which brings non-Western and experimental tunings into a module that fits in 3 HP and costs 120 euros before VAT. Most quantizers ship a fixed set of scales. Here the scale set is a thing the player writes, saves on a laptop, and swaps between sessions.

---

## Scale Upload

The module takes new scales as audio. The tool lives at [ericasynths.lv/quant](https://www.ericasynths.lv/quant/), and the page was reachable on 2026-10-24. Nothing needs to be installed, and no USB or MIDI connection is used.

**Procedure from the manual**

1. Open the web tool on a laptop or smartphone.
2. Connect the headphone output of the laptop or smartphone to CLK IN on the module. Remove any clock cable first.
3. Design a scale or choose a ready one from the dropdown.
4. Click SEMI/QUARTER to choose regular semitone scales or microtonal quarter-note scales.
5. To select a preset, use the SCALES dropdown. The notes appear as dots on the keyboard. To design your own, click the keys. Black or white dots mark the active notes.
6. Press and hold the SCALE button on the module for two seconds. The LED blinks red, which is upload mode. Use the dropdown next to UPLOAD to choose one of the eight slots, which correspond to the LED colors, and click UPLOAD. The upload takes about a second, and the LED blinks green once on success.
7. Design the next scale and upload it to another slot. A slot that already holds a scale is overwritten.
8. Scales can be saved on the laptop and loaded again with the SAVE and LOAD buttons.

**What the live page looked like on 2026-10-24.** The page is titled "Pico Quantizer V1.0." It shows SEMI and QUATER labels, slots 1 through 8, two SCALES dropdowns, and CLEAR and UPLOAD buttons. The scale lists include modes such as Major (Ionian), Dorian, and Phrygian, pentatonic and blues scales, world scales including Hirajoshi, Pelog, and Raga Bhairavi, Messiaen's modes, and chord sets. The layout differs from the manual's description, and the manual says the tool offers sixteen predefined scales. Treat the live page as the current tool and the manual as the procedure. ⚠️ Confirm the layout and the upload steps on hardware.

Whether scales persist after power-off is not stated in the manual. ⚠️

---

## Patch Examples

Pico QUANT is a UTILITY that sits in the control path, so every patch needs an oscillator receiving its CV OUT and an envelope and VCA behind it. The First Voice below uses the same voice each time, with the quantizer placed between a voltage source and the oscillator. Before adding the quantizer to a patch, play the voice with the oscillator on its own tuning and confirm that the envelope and VCA behave.

All four patches are drafts written from the manual and are untested on hardware ⚠️. Knob positions describe intent, and every "What to listen for" result is a prediction until the module has been patched. Use a source that stays above 0 V, since negative voltages at CV IN are ignored.

---

### Patch 1: Clocked and Unclocked Quantization ⚠️

This patch demonstrates that the clock input changes when the quantizer reads its source: unclocked, the pitch follows the source as it crosses each tolerance threshold, and clocked, the manual describes the result as clocked quantization.

**First Voice**

Before introducing anything specific to Pico QUANT, establish a working voice:

```
  ALM Busy Circuits Pamela's PRO Workout OUT 1 (SQR, /1) ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  New Godspeed SINE/FOLD out ──[A]──▶ VCA audio in ──▶ Mixer
  Pico QUANT CV OUT ──[C]──▶ New Godspeed 1V/OCT
```

Use a clock and modulation source such as ALM Busy Circuits Pamela's PRO Workout (or Squarp Hermod+ for the gate), an oscillator such as Endorphin.es New Godspeed (or Endorphin.es Furthrrrr Generator with its waveshaper knobs fully counterclockwise), an envelope generator such as Blue Lantern BLM Looping Simple ADSR (or Make Noise Maths), and a VCA such as Vostok Instruments Ceres (or Erica Synths Pico VCA2). Set SCALE to black (Diatonic). With nothing patched to CV IN, the output is a fixed note, so the voice plays one repeating pitch.

**Add the voltage source, unclocked**

```
                                 ┌──────────────────────────────┐
Pamela's OUT 3 ──[C, slow]──▶    │ CV IN                CV OUT  │──[C]──▶ New Godspeed 1V/OCT
                                 │ CLK IN               CLK OUT │
                                 └──────────────────────────────┘
                                      Erica Synths Pico QUANT
```

- `Pamela's OUT 3 ──[C, slow]──▶ CV IN`: a slow triangle sweeps the voltage up and down through the scale, so the quantizer steps through the notes as the voltage crosses each threshold. Set the wave type to a triangle at a slow division such as /16, with the amplitude near 40 percent. At 0 V to 5 V the sweep covers five octaves, and a reduced amplitude narrows it to about two. (A 2hp LFO v2 works as the source; its outputs are unipolar, 0 V to 5 V, and would need an attenuator for a narrower sweep.)
- `Pico QUANT CV OUT ──[C]──▶ New Godspeed 1V/OCT`: the quantized voltage replaces a raw sequencer voltage, so the oscillator plays only notes of the scale.

Set TOLERANCE fully counterclockwise. The pitch should climb and fall through the scale, stepping about halfway between notes.

**Move the cable**

Patch Pamela's OUT 2 (SQR, x2) into CLK IN. Leave every knob where it is.

```
                                 ┌──────────────────────────────┐
Pamela's OUT 3 ──[C, slow]──▶    │ CV IN                CV OUT  │──[C]──▶ New Godspeed 1V/OCT
Pamela's OUT 2 ──[T]──▶          │ CLK IN               CLK OUT │
                                 └──────────────────────────────┘
                                      Erica Synths Pico QUANT
```

What changed: the module is now in clocked mode. The manual describes this as clocked quantization, and the working assumption in this guide is that pitch changes now line up with the clock pulses and not with the moment the source crosses a threshold. The source still sets the note, and the clock sets when the change takes effect.

**What to listen for**

Unclocked, the pitch should step the moment the source crosses a threshold, so changes land wherever the sweep happens to be. Clocked, the changes should land on the beat. If the pitch never changes, the source is probably below 0 V or the amplitude is too low to cross a threshold. If the clocked and unclocked results sound the same, check that the clock cable is in CLK IN and not CV IN. ⚠️ The manual does not describe the clocked mechanism in detail; confirm that pitch changes align to the clock.

---

### Patch 2: A Random Line That Triggers Itself ⚠️

This patch demonstrates that CLK OUT fires when the quantized pitch changes, so the rhythm of the melody is a product of how busy the pitch is.

**First Voice**

Use the same voice as Patch 1, with the gate from Pamela's OUT 1 (SQR, /1) and the oscillator on CV OUT. Verify that the envelope and VCA behave before adding the source.

**Add the random source**

```
                                 ┌──────────────────────────────┐
Turing Machine Volts 1 ──[C]──▶  │ CV IN                CV OUT  │──[C]──▶ New Godspeed 1V/OCT
                                 │ CLK IN               CLK OUT │
                                 └──────────────────────────────┘
                                      Erica Synths Pico QUANT
                                      (CLK IN left empty)
Pamela's OUT 2 ──[T]──▶ Turing Machine clock in
```

- `Music Thing Modular Turing Machine Volts 1 ──[C]──▶ CV IN`: the Volts expander makes a stream of random voltages from the shift register, with outputs up to 5 V. Set the Volts quantize control to off so the voltage arrives unquantized and Pico QUANT does the work. Lock the pattern by turning the Turing Machine knob fully counterclockwise, so the sequence repeats. (A Mutable Instruments Marbles X1 also works here.)
- `Pamela's OUT 2 ──[T]──▶ Turing Machine clock in`: the shift register advances on each pulse, so the clock rate sets how often a new voltage arrives.

Leave CLK IN empty. Start with TOLERANCE fully counterclockwise.

**Move the cable**

Move the envelope gate cable from Pamela's OUT 1 to CLK OUT.

What changed: the envelope no longer fires on every beat. It fires only when the quantized pitch changes, so a note that repeats gives no trigger and the melody gains rests.

**What to listen for**

At TOLERANCE counterclockwise, the output should change often, and the envelope should fire often. Turn TOLERANCE clockwise and the output should hold each note longer, with fewer triggers and more silence. If the voice is silent, check that CLK IN is empty and that the Turing Machine is receiving a clock. If the pitch is stuck on one note, the random source may be below 0 V or outside the range where it crosses thresholds. The five-octave range is wide; if it is too wide, use an attenuator between the source and CV IN. ⚠️ CLK OUT behavior when CLK IN is patched is not described in the manual and is not used here.

---

### Patch 3: Tolerance as a Performance Control ⚠️

This patch demonstrates that TOLERANCE changes how readily the output advances to the next note, so one knob moves the character of the line from busy to settled with the source and scale unchanged.

**First Voice**

Use the same voice as Patch 1, with a steady gate from Pamela's OUT 1 (SQR, /1), so a note sounds on every beat whether or not the pitch changes.

**Add a slowly evolving source**

```
                                 ┌──────────────────────────────┐
Pamela's OUT 4 ──[C, slow]──▶    │ CV IN                CV OUT  │──[C]──▶ New Godspeed 1V/OCT
                                 │ TOLERANCE            GLIDE   │
                                 └──────────────────────────────┘
                                      Erica Synths Pico QUANT
```

- `Pamela's OUT 4 ──[C, slow]──▶ CV IN`: set the wave type to a slewed random, which the Pamela's guide describes as sample and hold with smooth transitions, at a slow division such as /8, with the amplitude near 60 percent. The output wanders slowly through a range of voltage, staying positive. (Make Noise Maths in cycle mode is an alternative, with its rise and fall times set long.)
- `Pico QUANT CV OUT ──[C]──▶ New Godspeed 1V/OCT`: the quantized wander drives the oscillator.

Press SCALE until the LED shows dark blue for Pentatonic, or green for Blues, so that every note of the scale sounds musical against the others.

Start with TOLERANCE fully counterclockwise and listen for a minute. Turn it slowly clockwise. Return it and turn it again at a different pace, as a gesture. Then add a small amount of GLIDE and repeat.

**What to listen for**

At counterclockwise, the pitch should follow the wander closely and change often. At clockwise, the pitch should hold each note longer and change only when the source approaches the next one, so the line sounds slower and more deliberate. GLIDE should turn the steps into slides, most clearly at the slower tolerance setting. If the pitch never changes at any setting, the source is not moving enough: try a larger amplitude or a faster division.

---

### Patch 4: Marbles Into a Custom Scale ⚠️

This patch demonstrates the scale upload: a locked random loop from Marbles stays fixed while the scale underneath it changes, so the same sequence of voltages produces different melodies.

**Prepare the scales**

Before patching, follow the Scale Upload section to load two scales: a seven-note scale of your own, and a quarter-tone scale built with the SEMI/QUARTER setting. Put them in two of the eight slots. CLK IN must be empty, so remove any clock cable first.

**First Voice**

```
  Mutable Instruments Marbles t2 ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  New Godspeed SINE/FOLD out ──[A]──▶ VCA audio in ──▶ Mixer
  Pico QUANT CV OUT ──[C]──▶ New Godspeed 1V/OCT
```

Marbles supplies the gate, so the patch needs no other clock. Verify that the voice sounds before adding the voltage source.

**Add Marbles to the quantizer**

```
                                 ┌──────────────────────────────┐
Marbles X1 ──[C]──▶              │ CV IN                CV OUT  │──[C]──▶ New Godspeed 1V/OCT
                                 │ CLK IN               CLK OUT │
                                 └──────────────────────────────┘
                                      Erica Synths Pico QUANT
```

- `Marbles X1 ──[C]──▶ CV IN`: X1 supplies a random stepped voltage, and Pico QUANT turns it into notes of the chosen scale.
- `Marbles t2 ──[G]──▶ EG gate in`: each new random value comes with a gate, so every note is articulated.

Set the Marbles STEPS knob to center, where the X outputs produce classic stepped random voltages, so that Marbles does not quantize first and Pico QUANT supplies all of the scale. Set SPREAD near 12 o'clock for a bell-curve spread of pitches. Set DEJA VU to 12 o'clock, which the Marbles guide describes as locking into a perfect loop, and let a phrase settle. Then press SCALE to move through the presets and then through your uploaded slots.

**What to listen for**

With DEJA VU locked, the rhythm and the order of the voltages should repeat exactly, and only the scale should change when SCALE is pressed. The Diatonic preset should sound conventional, the uploaded seven-note scale should sound like the scale you designed, and the quarter-tone scale should sound in between the keys of a conventional tuning. If the pitches sit in a narrow band, widen SPREAD. If nothing sounds, check that X1 is positive. ⚠️ The voltage range of Marbles X1 and the root note of the scales are unverified: if Marbles offers a range choice, select a positive range, and expect the scales to be built from C, as on the web tool's keyboard, until confirmed on hardware.

---

## Common Mistakes

### "I patched my LFO in and only half of it makes notes"

Pico QUANT ignores negative voltages at CV IN. A bipolar LFO swinging from -5 V to +5 V changes the output only during its positive half. Use a unipolar output, such as the outputs of 2hp LFO v2 or a Pamela's PRO Workout CV wave, or add a DC offset to lift the whole swing above 0 V. A source that sits just above 0 V will also sound narrow, since only the voltage that crosses a threshold changes the note.

### "TOLERANCE is backwards"

The label and the behavior run in opposite directions. Fully counterclockwise is 50 percent tolerance, where the output advances about halfway between notes, so it follows the source closely. Fully clockwise is 10 percent, where the output advances only when the source is very close to the next note, so it holds longer. Clockwise is tighter, not looser. The shorthand of eager for counterclockwise and stubborn for clockwise helps until it becomes habit, and it is worth practicing before a performance.

### "CLK OUT does not follow my clock"

With nothing patched to CLK IN, CLK OUT fires a trigger each time the quantized note changes. It does not keep time. A repeated note gives no trigger, and a source that moves a lot gives many. The manual does not describe what CLK OUT does when CLK IN is patched, so do not rely on it as a clock thru until that is confirmed on the hardware. ⚠️

### "My upload did nothing, or it replaced a scale I wanted"

The headphone cable goes into CLK IN, so remove any clock cable first. Hold the SCALE button for two seconds until the LED blinks red before clicking UPLOAD, and watch for the single green blink at the end. A slot that already holds a scale is overwritten without warning, including a preset, so save scales you care about on the laptop with the SAVE button, and note which scale lives in which slot. The live web page can look different from the manual's description, so work from the slot and UPLOAD controls on the page you see.

### "My melody is stuck on the same high note"

CV OUT stops at +8 V. A source that exceeds that voltage quantizes to the highest note available and stays there. Check the source with a scope such as Mordax Data, or reduce its amplitude with an attenuator, a Pamela's amplitude setting, or the source's own range control.

### "Everything is in the wrong key"

The scales are fixed patterns, and the manual gives no root note setting. The web tool's keyboard starts at C, so scales are most likely built from C at 0 V. The quantizer cannot transpose, so the key of the result depends on the tuning of the receiving oscillator. To change key, tune the oscillator or add an offset to the CV before or after the quantizer. ⚠️ The root note is not stated in the manual and needs confirmation on hardware.

---

## Advanced Learning Path

1. **See the staircase.** Patch the source into one input of Mordax Data and CV OUT into another, and run the scope. Watch the smooth input and the stepped output at once, then turn TOLERANCE and see where the steps move. The manual's own figure shows the same thing, and watching it live turns the diagram into a feel for the control.

2. **Play every scale on one source.** Hold a slow, wide source constant and press SCALE through all eight presets, listening to the same movement in each. Note which scales leave large gaps, such as Pentatonic and Whole-tone, and which are dense, such as Chromatic. This builds a vocabulary for choosing a scale by character.

3. **Clock it slower than the source.** Patch a clock into CLK IN at several rates, including a rate slower than the source's movement. Compare a clock that matches the source's rate with one far slower. The note choice follows the source, and the timing follows the clock, which is the difference between a lead line and a held bass.

4. **Make the rhythm from the pitch.** Leave CLK IN empty and use CLK OUT to trigger an envelope or a drum voice. Change the source's rate and range, and listen to the rhythm change. Then change TOLERANCE and notice that it moves both melody and rhythm at once.

5. **Use glide as a wet and dry control.** At fast sequence rates, turn GLIDE from counterclockwise to clockwise and listen to the line move from fully quantized to unquantized. Find the point where the slide makes the steps sound like a single gesture.

6. **Write a scale of your own.** Build a five-note scale on the web tool, upload it to a slot, and play it. Then build the same scale in quarter-tone mode with one or two notes moved by a quarter tone, and compare the two. Save both on the laptop.

7. **Try other tunings.** Choose scales from the web tool's lists, such as Hirajoshi, Pelog, Raga Bhairavi, or a Messiaen mode, and upload them to separate slots. Play the same locked sequence through each. This is where the module stops being a quantizer for a chosen key and becomes a way to hear what a tuning does.

---

## Pairs Well With

**Mutable Instruments Marbles:** Marbles supplies X1 as a stepped random voltage and t2 as the gate, so one module makes a complete source for the quantizer. With STEPS at center, Marbles leaves the scale entirely to Pico QUANT. With DEJA VU locked at 12 o'clock, the sequence repeats, which makes a clean test bed for comparing scales on identical material. ⚠️

**Music Thing Modular Turing Machine:** The Turing Machine with a Volts expander makes a repeating or drifting stream of voltages up to 5 V, and a quantizer is the module that turns that stream into a tune. Locked loops give a repeating sequence, and unlocked, the pattern changes over time. With Pico QUANT's CLK OUT, the melody triggers its own envelope, and a repeated step becomes a rest.

**ALM Busy Circuits Pamela's PRO Workout:** Pamela's outputs run from 0 V to 5 V, which fits CV IN, and its slew and sample-and-hold wave types give slowly evolving random voltages. Its amplitude and offset settings narrow a source to the range the quantizer should see, and its clock outputs supply CLK IN. One module can provide the voltage, the clock, and the gate.

**2hp LFO v2:** The 2hp LFO v2 outputs are unipolar, 0 V to 5 V, so they meet the quantizer's requirement that negative voltage is ignored without any offset. Slow triangle or saw waves become scale-wide arpeggios, and a faster rate produces trills. The range is five octaves, so an attenuator or a reduced oscillator range may help.

**Make Noise Maths:** Maths in cycle mode makes a slowly rising and falling voltage with rise and fall times up to 25 minutes, according to the Maths guide. Used as a source for CV IN, it gives very slow melodic motion across a scale. Check the output range before patching, since negative voltages are ignored.

**Mordax Data:** Mordax Data in scope mode shows the input and output of the quantizer together, so the staircase and the effect of TOLERANCE become visible. It also makes the +8 V ceiling and the effect of an attenuator easy to check. Using it once makes the module's behavior concrete in a way no description can.

---

*Visit [ericasynths.lv](https://www.ericasynths.lv/pico-quant-3/) for the official manual and product information*
