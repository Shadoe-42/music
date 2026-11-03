---
title: Make Noise GTE
manufacturer: Make Noise
primary_role: CONTROLLER
secondary_roles: []
historical_context: true
form_factor: eurorack
functions: [gate-generator]
behavior_tags: [reactive, sensitive, free-running, performance-oriented]
use_cases: [rhythm from modulation motion, gestures that trigger drums, self-playing rhythmic patterns]
hp: 8
depth: 29mm
current_draw:
  plus12: 25mA
  minus12: 2mA
memory: none
transport: none
screen: false
hybrid: false
cv: full
inputs: [SPAN, SPACE, TRIGGER]
outputs: [CHANNEL 1-8, PULSE STREAM, EVEN, ODD]
patch_format: v1
---

# Make Noise GTE

**Gestural Time Extractor: turns the motion of any control voltage into eight channel gates, a pulse stream, and odd and even gates, with no clock required, in 8 HP**

![Make Noise GTE](https://github.com/Shadoe-42/music/raw/main/modular/images/make_noise/gte/front_panel.jpg)
*Make Noise GTE: SPAN control, attenuverter, and CV input; SPACE control and CV input; TRIGGER input; eight channel outputs with LEDs; and the PULSE STREAM, EVEN, and ODD outputs*

> **Draft status (2026-11-02):** Written from the official Make Noise GTE manual (8 pages, by Tony Rolando and Walker Farrell) and announcement coverage from April 2026, before the module was in hand. Every description of how the module behaves comes from that manual, which gives no voltage numbers. All four patches are untested on hardware and are marked ⚠️. Open items to clear on hardware: (1) the voltage range at SPAN needed to travel across all eight channels at several SPACE settings; (2) the level of the gate outputs and the width of the pulse stream's pulses; (3) whether the SPAN attenuverter and the SPAN panel control add or scale, and how they behave at center; (4) behavior above and below the full range, where no channel is active; (5) the printed panel label of the pulse stream output (the manual's text calls it the GTE output); (6) channel LED behavior; (7) depth, which comes from Sound On Sound and includes the power cable; (8) the Historical Context is short because no source gives a design history beyond the maker's own announcement; (9) the front panel image link below points to the location for the photograph taken in the test plan, and shows nothing until that photograph is added. The Channel Index Translation described in the manual needs a N.U.S.S. module that sends a Channel Index signal, which is not in this rack, so no patch uses it. Remove this block when the items are cleared.

---

## Historical Context

Make Noise was founded in 2008 in Asheville, North Carolina, by Tony Rolando, a self-taught instrument designer who builds electronics for artists and has worked for Moog Music. Its best-known module is Maths, a function generator that this corpus documents in its own guide, and the maker has built a family of modules around the idea of a universal system. Perfect Circuit's review of PoliMATHS refers to the New Universal Synthesizer System, or N.U.S.S., as a proposed system that includes PoliMATHS, QXG, MultiMod, and Jumbler, with a MultiWAVE sound source expected. The GTE was announced on April 7, 2026 at 179 US dollars, and Synthtopia describes it as the latest module in the N.U.S.S.

The idea that makes the GTE possible is in PoliMATHS. Perfect Circuit explains that PoliMATHS has a Span input that works like an address: the voltage at Span targets one of the channels of its function generator. With nothing patched to its Activate input the targeted channel triggers as soon as Span reaches it, and with a signal patched there it fires only when a trigger, called an Activation, arrives; Channel Index is one of the three Span modes. The GTE reads a voltage in the same way, with the voltage at SPAN selecting one of eight channels, and then reports the position as eight gates, as an odd and even pair, and as a short pulse every time the position changes. The manual calls it an analog pulse extractor and a Channel Index Translator, because with the right settings it also converts a Channel Index signal from PoliMATHS or another N.U.S.S. module into eight gates.

The manual is credited to Tony Rolando and Walker Farrell, with illustration and layout by Lewis Dahm. No source consulted names a designer for the GTE or describes how it was conceived, so this guide does not claim a design intent beyond what the manual states. Sound On Sound lists the module as 8 HP, 29 millimeters deep including the power cable, and drawing 25 milliamps from the +12 V rail and 2 milliamps from the -12 V rail, which matches the manual's current figures.

---

## Quick Start: First Rhythm from a Voltage in 5 Minutes

The GTE watches a control voltage and reports where it is. Eight channel outputs go high one at a time as the voltage at SPAN rises, a pulse fires every time the active channel changes, and nothing needs a clock. This quick start uses a slow LFO as the moving voltage and the panel LEDs as the first readout. ⚠️ Untested on hardware.

1. **Power the module with the red stripe toward -12 V.** On a Make Noise busboard the manual says the -12 V line is the white stripe, so check the case maker's specification.
2. **Patch a slow triangle LFO into SPAN.** The CV input at SPAN takes the voltage whose motion you want to read.
3. **Raise the SPAN attenuverter and turn the SPAN panel control.** Together they set how much of the voltage reaches the channel selector.
4. **Watch the eight channel LEDs.** One is lit at a time, and the lit channel moves up as the voltage rises. If none is lit, the voltage is above or below the full range.
5. **Turn SPACE.** SPACE sets how large a voltage range is needed to travel across all eight channels. Lower values make small changes cover more channels.
6. **Patch any channel output to a trigger input.** The channel gate fires each time the voltage enters that channel's band.
7. **Patch PULSE STREAM to a second trigger input.** It fires a short pulse every time a new channel is selected, up or down.
8. **Leave TRIGGER empty at first.** With nothing patched, the module follows the voltage. Patching a clock there makes the channel change only when a trigger or gate arrives.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 8 HP |
| Depth | 29 mm ⚠️ |
| Power | 25 mA +12V / 2 mA -12V / 0 mA +5V |
| Inputs | SPAN CV (with panel control and attenuverter), SPACE CV (with panel control), TRIGGER |
| Outputs | Eight channel gates with LEDs, PULSE STREAM, EVEN, ODD |
| Price | 179 US dollars at announcement |
| Warranty | One year from purchase |

The depth of 29 mm comes from Sound On Sound and includes the power cable; the manual does not give a depth. The current draw is the manual's. The manual lists no +5 V rail.

---

## Essential Parameters

**SPAN.** SPAN is the input where a moving voltage is read. As the voltage rises, so does the selected channel. A panel control, an attenuverter, and a CV input work together to set how much of the signal reaches the selector, so SPAN is the place for any gesture: an LFO, an envelope, a random voltage, or a touch plate. ⚠️ The manual does not say whether the panel control and the attenuverter add or scale, and it gives no voltage range for the full travel.

**SPACE.** SPACE sets the range of input voltage that SPAN needs to reach all eight channels. As SPACE decreases, smaller changes at SPAN produce larger jumps between channels, so the outputs are denser and more reactive; at the minimum, the total voltage range becomes very small. SPACE also has a CV input, so the sensitivity can move with a second source. The same SPAN signal can read as a slow, sparse rhythm at one SPACE setting and a dense one at another.

**Channel outputs 1 to 8.** The eight channel outputs are gates for the eight possible values of SPAN. At any moment one is high, unless SPAN goes above or below the full range set by SPACE, in which case none is high. Each output has an LED. A channel gate rises when the voltage enters its band and falls when the voltage leaves it.

**ODD and EVEN.** ODD is high when the active channel is 1, 3, 5, or 7, and EVEN is high when it is 2, 4, 6, or 8. If any channel is active, exactly one of the two is high. Because adjacent channels alternate parity, a voltage that moves one channel at a time flips between the two outputs at every step. ⚠️ A voltage that jumps over a channel keeps the same output high, and the output would not produce a new rising edge; this follows from the manual's description and is unverified.

**PULSE STREAM.** The manual calls this output the GTE output. It fires a short pulse any time a new channel is selected via SPAN, and the manual describes the stream as representing the speed of motion of the input signal. A faster-moving voltage crosses more channel boundaries per second, so the pulses come more often. ⚠️ The panel label and the pulse width are unverified.

**TRIGGER.** TRIGGER is optional. With nothing patched, the output channel follows SPAN continuously. With a trigger or gate patched, the output channel changes only on the rising edge, so the channel changes line up with other events in the system. The module can be free-running or locked to a clock without changing anything else.

**Channel Index Translation.** With the module set to its starter positions for this task, a Channel Index signal from PoliMATHS or another N.U.S.S. module at SPAN produces eight gates that coincide with channel activity at the source. When several channels are activated at once, each channel's index is delivered in a rapid series of 5 millisecond triggers, ending with the last channel staying high, which the manual calls Flam Data Delivery (FDD). The result is a quick downward flam of gates at the channel outputs. ⚠️ This feature is described from the manual and is not covered by a patch in this guide; the exact knob positions for this mode, which the manual words as a combination of SPAN fully counterclockwise and the attenuverter and SPACE fully clockwise, are unverified.

---

## Time Without a Clock

Most rhythm tools start from a clock and ask where to put events on it. The GTE starts from a movement and asks when the movement crosses a line. Eight thresholds are laid across a range of voltage; whenever the signal crosses one, a channel changes, a pulse fires, and the odd and even outputs may flip. The spacing of the events in time is the spacing of the crossings in time, so the rhythm is the shape and speed of the signal.

Three consequences follow from the manual. A slow triangle crosses the thresholds in order on the way up and in reverse order on the way down, so the rhythm is a palindrome whose spacing is set by the slope. A faster signal makes denser pulses, because the pulse stream represents the speed of motion. And a narrow SPACE brings the thresholds closer together, so the same signal crosses more of them and fires more events in the same time.

The TRIGGER input is the one place a clock can enter. When it is patched, the channel change waits for the rising edge, so the rhythm that came from motion is snapped to a grid. Unpatched, the module has no beat of its own; patched, it has exactly the beat that was patched.

---

## Why This Instrument Excels

The GTE gets its timing from the motion of a voltage. A slow envelope gives a slow rhythm, a random voltage gives an irregular one, and a hand moving over a touch plate gives a rhythm that follows the hand. Because the gate pattern comes from movement and not from a clock, the module is a tool for performances that should not sit on a grid, and for patches where one slow source should drive several rhythmic voices together.

Three readings of the same signal are available at once. The eight channel gates say where the voltage is, the odd and even pair says which kind of position it is in and flips at nearly every step, and the pulse stream says that something changed. A single source can therefore drive a kick on one channel, a snare on ODD, a hat on the pulse stream, and a melodic trigger on another channel, all in time with each other because they come from the same motion.

SPACE is a single sensitivity control that changes the density of everything at once. The same LFO or random voltage becomes sparse or dense by moving one knob, or by patching a second source into SPACE CV, and the thresholds scale with it. The optional TRIGGER input adds a second behavior without changing the module: free-running and continuous, or quantized to a clock.

At 8 HP and 25 milliamps, the module is cheap in space and power, and it puts the channel gates, the odd and even gates, and the pulse stream on one panel. It is also the translator for N.U.S.S. Channel Index signals, which gives it a role in a system built around that family. The cost is that the manual gives no voltage figures, so the first job with any new source is to find out how SPACE and SPAN line up with it.

---
## Patch Examples

The GTE is a CONTROLLER that sits in the control path and drives other modules, so each patch needs a moving voltage in and voices behind it. The First Voice below follows the clock-and-sequencer pattern from the patch format spec: it establishes the voice the GTE will drive and confirms that it sounds before the GTE is connected. The voices are Endorphin.es BLCK_NOIR in Patches 1 to 3 and a pitched voice with Erica Synths Pico DRUM2 in Patch 4.

All four patches are drafts written from the manual and are untested on hardware ⚠️. Knob positions describe intent, and every "What to listen for" result is a prediction until the module has been patched. The manual gives no voltage figures, so each patch tells you how to set SPACE by watching the channel LEDs. Because adjacent channels alternate between ODD and EVEN, a voltage that moves one channel at a time flips between the two outputs at every step.

---

### Patch 1: A Rhythm Read from a Slow Triangle ⚠️

This patch demonstrates that a rhythm can be read from the shape of a slow voltage: a triangle crosses the channel boundaries in order on the way up and in reverse on the way down, so the pattern is a palindrome.

**First Voice**

Before introducing anything specific to the GTE, establish the voices it will drive:

```
  Endorphin.es BLCK_NOIR MONO MIX OUT ──[A]──▶ Mixer
```

With nothing patched into the BLCK_NOIR CLOCK IN, press the BD, SD, and CH launch buttons and confirm that each fires a single hit. The module is an EVENT_VOICE, so no external envelope or VCA is needed.

**Add the slow triangle**

```
                           ┌──────────────────────────────────┐
2hp LFO v2 ──[C, slow]──▶  │ SPAN                    CHANNEL 1│──[G]──▶ BLCK_NOIR BD TRIG IN
                           │ SPACE                   CHANNEL 4│──[G]──▶ BLCK_NOIR SD TRIG IN
                           │                         CHANNEL 7│──[G]──▶ BLCK_NOIR CH TRIG IN
                           └──────────────────────────────────┘
                                      Make Noise GTE
```

- `2hp LFO v2 ──[C, slow]──▶ SPAN`: a slow, steady voltage moves through the eight channels at an even speed, so the spacing of the hits is easy to hear.
- `CHANNEL 1 ──[G]──▶ BD TRIG IN`: the lowest channel is the first band the triangle enters, so the kick lands at the bottom of each sweep.
- `CHANNEL 4 ──[G]──▶ SD TRIG IN`: the middle channel puts the snare halfway up the slope.
- `CHANNEL 7 ──[G]──▶ CH TRIG IN`: a high channel puts the hat near the top of the cycle.

Use a slow modulation source such as 2hp LFO v2 (or Make Noise Maths in cycle mode), a drum module such as Endorphin.es BLCK_NOIR (or Erica Synths Pico DRUM2 for a single voice), and a mixer. Set the 2hp LFO v2 RANGE toggle to the left, the WAVE knob to the triangle position, and the RATE to a cycle of about six seconds, and take the primary output. Raise the SPAN attenuverter, then turn SPACE until the eight channel LEDs sweep from 1 to 8 as the triangle rises. This patch uses five cables.

**Move the cable**

Unplug the cable from CHANNEL 4 and plug the ODD output into the BLCK_NOIR SD TRIG IN.

```
                           ┌──────────────────────────────────┐
2hp LFO v2 ──[C, slow]──▶  │ SPAN                    CHANNEL 1│──[G]──▶ BLCK_NOIR BD TRIG IN
                           │ SPACE                        ODD │──[G]──▶ BLCK_NOIR SD TRIG IN
                           │                         CHANNEL 7│──[G]──▶ BLCK_NOIR CH TRIG IN
                           └──────────────────────────────────┘
                                      Make Noise GTE
```

What changed: the snare now fires every time the voltage enters an odd channel (1, 3, 5, or 7), so there are four snare hits on each slope instead of one, with the first and last landing at the same moment as the kick and the hat.

**What to listen for**

Each rising slope should give a kick, then a snare, then a hat at even intervals, and the falling slope should repeat them in reverse order, so the pattern reads kick, snare, hat, hat, snare, kick. A longer LFO cycle should stretch the spacing without changing the order. With the ODD cable, the snare should fire on the odd steps and double up with the kick and the hat. If only some of the voices sound, the triangle does not travel across all eight channels; turn SPACE so the LEDs sweep through every position. ⚠️ The voltage range of the LFO at SPAN, and the way the output channels behave when the voltage returns to the same band, are unverified.

---

### Patch 2: A Hand as the Clock ⚠️

This patch demonstrates that the pulse stream follows the speed of motion: the faster the hand moves over a touch plate, the more often the hat fires.

**First Voice**

Use the same voices as Patch 1. Patch BLCK_NOIR MONO MIX OUT to the mixer and confirm each voice with its launch button.

**Add the touch plates**

```
                           ┌──────────────────────────────────┐
Pressure Points ──[C]──▶   │ SPAN                PULSE STREAM │──[T]──▶ BLCK_NOIR CH TRIG IN
(Common Pressure)          │ SPACE                            │
                           └──────────────────────────────────┘
                                      Make Noise GTE

  Pressure Points Common Gate ──[G]──▶ BLCK_NOIR BD TRIG IN
```

- `Pressure Points Common Pressure ──[C]──▶ SPAN`: the pressure of a finger becomes the voltage that moves the channel selector, so the hand is the signal.
- `PULSE STREAM ──[T]──▶ CH TRIG IN`: the pulses fire when the channel changes, so the hat follows how fast the pressure changes and not how hard it is.
- `Pressure Points Common Gate ──[G]──▶ BD TRIG IN`: touching a plate fires the kick, so every gesture has a start.

Use a touch controller such as Make Noise Pressure Points (or Make Noise Wogglebug, Smooth output, for a version that plays itself) and a drum module such as Endorphin.es BLCK_NOIR. Set SPACE so that moderate pressure on a plate moves the LEDs through several channels. This patch uses four cables.

**What to listen for**

Touching a plate should fire the kick, and pressing and releasing, or sliding a finger along the plate, should fire hats at a rate that follows the motion: a quick rub gives a burst and a slow press gives a few hits. Holding still should give silence, since no new channel is selected. If hats keep firing with the hand at rest, the voltage is hovering at a boundary; turn SPACE up or move the SPAN attenuverter down to leave some room. ⚠️ The voltage range of the pressure output is not given in this corpus, and the sensitivity of SPAN to it is unverified.

---

### Patch 3: Odd and Even as Kick and Snare, with an Optional Grid ⚠️

This patch demonstrates that the odd and even outputs alternate with every step, and that the TRIGGER input snaps a rhythm that came from motion onto a clock.

**First Voice**

Use the same voices as Patch 1.

**Add the random voltage**

```
                           ┌──────────────────────────────────┐
Marbles X1 ──[C]──▶        │ SPAN                         ODD │──[G]──▶ BLCK_NOIR BD TRIG IN
                           │ SPACE                       EVEN │──[G]──▶ BLCK_NOIR SD TRIG IN
                           │ TRIGGER           PULSE STREAM   │──[T]──▶ BLCK_NOIR CH TRIG IN
                           └──────────────────────────────────┘
                                      Make Noise GTE
```

- `Marbles X1 ──[C]──▶ SPAN`: a stepped random voltage lands on a different channel at each step, so the pattern is irregular.
- `ODD ──[G]──▶ BD TRIG IN`: the kick fires when the voltage lands on an odd channel.
- `EVEN ──[G]──▶ SD TRIG IN`: the snare fires when it lands on an even one, so a step to a neighboring channel flips between the two.
- `PULSE STREAM ──[T]──▶ CH TRIG IN`: the hat fires on every change, whether or not the kick or snare did.

Use a probability source such as Mutable Instruments Marbles (or Make Noise Wogglebug, Stepped output). Set Marbles SPREAD wide enough that X1 covers a large part of its range, and turn SPACE so the LEDs visit many channels. Marbles runs on its own clock for the first part. This patch uses six cables.

**Move the cable**

Patch a steady clock into TRIGGER, using a clock source such as ALM Busy Circuits Pamela's PRO Workout (or Squarp Hermod+), with OUT 1 set to a square wave at a steady division.

```
                           ┌──────────────────────────────────┐
Marbles X1 ──[C]──▶        │ SPAN                         ODD │──[G]──▶ BLCK_NOIR BD TRIG IN
Pamela's OUT 1 ──[T]──▶    │ TRIGGER                     EVEN │──[G]──▶ BLCK_NOIR SD TRIG IN
                           │ SPACE             PULSE STREAM   │──[T]──▶ BLCK_NOIR CH TRIG IN
                           └──────────────────────────────────┘
                                      Make Noise GTE
```

What changed: the channel now changes only on the rising edge of the clock, so the hits no longer land wherever Marbles steps and instead fall on the clock grid. Unpatching the cable returns to the free-running behavior.

**What to listen for**

Without the clock, hits should fall wherever X1 steps. With the clock, they should line up with the beat and some steps should be silent: when X1 jumps over a channel and lands on the same parity as before, ODD or EVEN stays high and does not fire again, while the hat still fires on every change. Lowering SPACE should make X1 cross more channels and give busier hits. If nothing happens after patching a cable into TRIGGER, check that the clock is actually running, since the channel only changes when a trigger arrives. ⚠️ The voltage span of Marbles X1 against the SPAN range, and the behavior of ODD and EVEN across a jump of more than one channel, are unverified.

---

### Patch 4: A Self-Playing Pair of Voices ⚠️

This patch demonstrates that two slow cycling voltages can run a whole piece: one moves through the channels, a second changes how much range SPAN needs, and the odd and even gates play two different voices.

**First Voice**

Establish the two voices with a temporary gate:

```
  Squarp Hermod+ gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  New Godspeed SINE/FOLD out ──[A]──▶ VCA audio in ──▶ Mixer
  Squarp Hermod+ gate out ──[G]──▶ Pico DRUM2 TRIGG
  Pico DRUM2 OUT ──[A]──▶ Mixer
```

Use a sequencer such as Squarp Hermod+ (or Mutable Instruments Marbles, with t2 for the gate), an oscillator such as Endorphin.es New Godspeed (or Endorphin.es Furthrrrr Generator), an envelope generator such as Blue Lantern BLM Looping Simple ADSR (or Make Noise Maths), a VCA such as Vostok Instruments Ceres (or Erica Synths Pico VCA2), and Erica Synths Pico DRUM2 for the second voice. Set the oscillator to a fixed pitch with its pitch knob. Confirm that each gate fires a pitched note and a drum hit, then remove the sequencer gate.

**Add the cycling voltages**

```
                                ┌────────────────────────────┐
Maths Ch1 Unity ──[C, slow]──▶  │ SPAN                   ODD │──[G]──▶ EG gate in
Maths Ch4 Variable ──[C, slow]─▶│ SPACE CV              EVEN │──[G]──▶ Pico DRUM2 TRIGG
                                └────────────────────────────┘
                                      Make Noise GTE
```

- `Maths Ch1 Unity ──[C, slow]──▶ SPAN`: a cycling channel sweeps the channels at the pace of its rise and fall times, so the pattern needs no sequencer.
- `Maths Ch4 Variable ──[C, slow]──▶ SPACE CV`: a second, slower cycle changes how much range SPAN needs, so the density of the pattern rises and falls over time.
- `ODD ──[G]──▶ EG gate in`: the pitched voice plays on the odd steps.
- `EVEN ──[G]──▶ Pico DRUM2 TRIGG`: the drum plays on the even steps, so the two voices alternate with each step.

Press the Cycle button on Maths channels 1 and 4. Set channel 1 Rise and Fall to about three seconds each, and channel 4 to about thirty seconds, then scale channel 4 with its attenuverter so the density changes by a modest amount. Use the SPAN attenuverter to bring the Maths output into the range of SPAN. The patch uses eight cables, below the ten-cable ceiling.

**What to listen for**

The two voices should alternate as the first cycle sweeps the channels, with the pitched voice on the odd steps and the drum on the even ones, and the whole pattern should speed up and thin out slowly as the second cycle moves SPACE. Speeding up the first cycle should speed up the pattern. If the pitched voice plays almost nothing, the voltage skips channels and stays on the same parity; reduce SPACE or the Maths amplitude. ⚠️ The output range of Maths against the ranges of SPAN and SPACE CV is unverified, and the knob positions above are a starting point to be adjusted by watching the LEDs.

---

## Common Mistakes

### "Nothing fires and every channel LED is dark"

SPAN has gone above or below the full range set by SPACE, so no channel is active and neither ODD nor EVEN is high. The module is not broken. Raise the SPAN attenuverter or the SPAN control until one LED lights, and widen SPACE if the voltage is larger than the range allows.

### "I only get two or three channels from my LFO"

SPACE sets how much voltage is needed to reach all eight channels, and a source that moves less than that range reaches only some of them. A 5 V triangle at a wide SPACE visits only the lower channels. Turn SPACE down until the LEDs sweep through all eight, or raise the SPAN attenuverter so more of the source reaches the selector.

### "I get twice as many hits as I expected"

The module selects a new channel on the way down as well as on the way up, so a triangle fires the same channels in reverse on every falling slope. The pulse stream fires on both. This is expected. To thin the pattern, patch fewer channels to voices, raise SPACE so that the triangle crosses fewer boundaries, or patch a clock into TRIGGER so that channel changes can only happen on the clock.

### "The module froze after I patched TRIGGER"

With a cable in TRIGGER the channel changes only when a trigger or gate arrives, so a missing or stopped clock holds the last channel. Check that the clock is running and that its level is high enough to register. Remove the cable to return to the free-running behavior.

### "ODD or EVEN did not fire when I expected"

ODD and EVEN are gates, and a gate that stays high has no new rising edge. Adjacent channels alternate between the two outputs, so a voltage that moves one channel at a time fires them in turn, but a jump of two channels leaves the same output high and the drum receives nothing new. Use the pulse stream, which fires on every change, or reduce the size of the jumps with SPACE and the source amplitude. ⚠️

---

## Advanced Learning Path

1. Find how much voltage your slowest LFO needs to sweep all eight channels, by lowering SPACE until the LEDs travel from one end to the other, and write the SPACE position down for that source.
2. Replace the triangle in Patch 1 with a saw, a square, and a stepped waveform, and listen to how the shape of the wave changes the order and spacing of the hits.
3. Patch a second modulation source into SPACE CV and listen to the density change while the first source sweeps SPAN.
4. Patch a clock into TRIGGER and move from free-running to a grid, then change the clock speed while leaving the source untouched, and notice that the rhythm of the channel changes follows the clock but the order follows the source.
5. Use the pulse stream as the clock for another module, such as a sample and hold or a random source, so that the speed of one voltage becomes the clock of a second.
6. Use ODD and EVEN together as a pair that cross-fades two voices, with one controlling a VCA and the other controlling a second VCA.
7. Map the module: with a known ramp and Mordax Data, record the voltage at which each channel starts and stops for three SPACE settings, and keep the table with your patches.
8. If a N.U.S.S. module with a Channel Index output joins the rack, use the Channel Index Translation and compare the flam of gates against the manual's description.

---

## Pairs Well With

**Make Noise Maths:** The manual lists Maths among the modules that work well with the GTE, and in cycle mode its channels make the slow, steady voltages the GTE reads most clearly. Make Noise Maths can also supply the shaped ramps that set how the channel changes are spaced, with long rises for stretched patterns and short falls for sharp restarts. ⚠️

**Make Noise Pressure Points:** Make Noise Pressure Points turns a finger into a voltage, and the GTE turns that voltage into timing, so a hand on a touch plate plays a rhythm without any clock. The individual gate and pressure outputs of each plate can also be used with the common outputs for more complex gestures. ⚠️

**Make Noise Wogglebug:** The Smooth output of Make Noise Wogglebug is a lagged random voltage that drifts across the channels, and the Stepped output jumps between them, so the same module gives a flowing pattern or a jumpy one depending on the jack. Its random behavior needs no clock, which suits the free-running mode of the GTE. ⚠️

**Mutable Instruments Marbles:** Mutable Instruments Marbles produces stepped random voltages whose spread and memory can be set, so it gives the GTE a source with a controlled amount of variation. A locked DEJA VU makes the channel pattern repeat, and the SPREAD control sets how many channels the voltage reaches. ⚠️

**ALM Busy Circuits Pamela's PRO Workout:** A clock from ALM Busy Circuits Pamela's PRO Workout at the TRIGGER input snaps the channel changes to a grid, so the rhythm that came from motion lines up with the rest of the system. Changing its division changes how often the GTE is allowed to move without touching the source. ⚠️

**Endorphin.es BLCK_NOIR:** Endorphin.es BLCK_NOIR has a trigger input for each of its drum channels, and a single moving voltage through the GTE can fire the kick, the snare, and the hat together. Its velocity inputs accept a CV from the same source for accents that follow the same gesture. ⚠️
