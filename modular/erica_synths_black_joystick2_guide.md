---
title: Black Joystick2
manufacturer: Erica Synths
series: Black Series
primary_role: CONTROLLER
secondary_roles: [MODULATOR]
functions: [joystick, motion-recorder, lfo, noise-oscillator]
hp: 12
depth: 30mm
current_draw:
  plus12: 71mA
  minus12: 20mA
voices: 1
inputs: []
outputs: [X1, X2, X3, X4, Y1, Y2, Y3, Y4, GATE3, GATE4]
patch_format: v1
---

# Erica Synths Black Joystick2

## Historical Context

The joystick as a musical controller has a longer history than most modular users realize. Don Buchla incorporated joystick interfaces into his systems in the 1960s, treating two-dimensional physical gesture as a legitimate compositional input rather than a performance gimmick. The X/Y controller represents something the standard knob cannot: the ability to move two parameters simultaneously, along a continuous path, in proportions determined by hand rather than preset. A knob encodes a single value at a time. A joystick encodes a relationship between values in real time.

What the Black Joystick2 adds to that lineage is memory. The module can record up to eight seconds of joystick motion per channel and loop that recording indefinitely, turning a live gesture into a persistent modulation source. This collapses the distinction between performance and automation: you play something once, and it plays back until you decide to change it. More precisely, it continues playing back while you override it with your hand, then fades back to the recording when you release. The recorded gesture and the live gesture coexist, and the transition between them is smooth.

That behavior is unusual enough to deserve attention before anything else.

---

## How the Joystick2 Thinks

The module has four independent channels. Each channel has two outputs: an X output and a Y output. The four X outputs are labeled X1 through X4 and the four Y outputs are labeled Y1 through Y4, giving eight simultaneous CV outputs total. Each channel can be configured to one of four operating modes, and all four channels can run in different modes simultaneously.

**Mode selection** works by holding the MODE button and pressing a channel button. The selected mode blinks on that channel's button. Available modes per channel:

- **JOYSTICK**: X and Y outputs follow the joystick position directly. Range is -5V to +5V on both axes.
- **SINE**: X output carries a sinewave LFO. Y output carries the same sinewave shifted 90 degrees. Joystick X position controls frequency (0.1Hz to 32Hz), joystick Y position controls amplitude. Holding MODE + channel button for two seconds switches the channel to Drone Oscillator mode (32Hz to 1kHz audio range).
- **RND**: X and Y outputs carry stepped random voltages. Joystick X position controls the rate of change, joystick Y position controls amplitude. Same two-second hold access for Noise Oscillator mode.
- **SNEW**: Four-quadrant panning mode. See the SNEW section below.

**Gate outputs** exist only on channels 3 and 4 (GATE3 and GATE4). In JOYSTICK and SNEW modes, a gate fires at +5V during joystick movement. In SINE and RND modes, the gate goes high whenever the CV is above 0V, producing rhythmic gate patterns that follow the LFO zero-crossing. In Drone and Noise Oscillator modes, the gate output carries a squarewave audio signal.

**Motion recording** is available in all modes. Hold REC while moving the joystick; release to begin looping the recording automatically. Maximum recording time is eight seconds per channel. A half-dimmed channel LED indicates an active recording is playing back. Switching a channel to a different mode clears any recorded motion on that channel immediately.

**Live override during playback**: if a recording is looping and you move the joystick, the recording is temporarily overridden by your live movement. When you release the joystick, the output smoothly fades back to the recorded motion and playback continues. This is not a punch-in replacement; it is a momentary intervention.

**Two configuration options** are accessible at power-on (hold MODE while powering the case on): joystick position save across channel switches, and recall of the last active channel on power-up. These are set once and persist.

---

## Why Black Joystick2 Excels

Most modulation sources in a modular rack operate independently of the performer once patched. The joystick2 does not. Every parameter the module controls (LFO rate, LFO depth, gesture shape) is mediated by physical position, and the motion recorder extends that physical authorship across time. A gesture you performed eight seconds ago continues to shape the patch while you do something else.

The four-channel architecture multiplies this capability. Channel 1 can be recording a slow filter sweep in SINE mode while channel 2 runs a live JOYSTICK control of resonance, channel 3 runs a random LFO into a wavefolder, and channel 4 sits idle. Each channel is its own independent modulation voice with its own mode, its own recording state, and its own outputs. This is a modulation composition environment built around a single physical interface.

The override-and-fade behavior is what makes the module genuinely interactive rather than simply automated. A static looping LFO eventually recedes into the background of a patch. The Joystick2 invites intervention: you can reach in at any moment, reshape the gesture, and step back out. The patch responds to you rather than running past you.

---

## Patch Examples

Because each channel operates independently and the module's behavior depends on which modes are active and whether motion is recorded, each patch begins by specifying the channel layout in use.

The CONTROLLER First Voice for the Black Joystick2 establishes the downstream voice the controller will modulate before the controller's outputs are connected. Verify the voice is working cleanly before proceeding to the main patch.

---

### Patch 1: Recorded Gesture as Looping Modulation

Recording an eight-second joystick path in JOYSTICK mode turns a single physical gesture into a looping modulation source with the natural variation and continuity that programmed LFOs cannot replicate.

**Channel layout for this patch:** CH1 in JOYSTICK mode.

**First Voice**

Before connecting the Joystick2, establish a voice the gesture will modulate:

```
  Sequencer CV out ──[C]──▶ VCO 1V/OCT
  Sequencer gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  VCO audio out ──[A]──▶ VCF audio in ──▶ VCA audio in ──▶ Mixer
  [Black Joystick2] CH1 in JOYSTICK mode: X1 and Y1 outputs available
```

Verify the voice produces a clean pitched sequence before connecting the Joystick2.

**Add the gesture**

```
                    ┌──────────────────────────────────────┐
Joystick (live) ──  │ CH1 JOYSTICK    X1 OUT               │──[C]──▶ VCF cutoff CV in
                    │                 Y1 OUT               │──[C]──▶ VCF resonance CV in
                    └──────────────────────────────────────┘
                              Black Joystick2
```

Use a VCF such as Erica Synths Black Hole DSP2 (or Doepfer A-106-5) as the filter.

- `X1 OUT ──[C]──▶ VCF cutoff CV in`: the horizontal axis controls filter brightness; moving right opens the filter, left closes it, giving the gesture a natural brightness contour.
- `Y1 OUT ──[C]──▶ VCF resonance CV in`: the vertical axis controls resonance simultaneously; the diagonal path of the joystick determines how brightness and resonance interact over the gesture's arc.

With both cables patched, move the joystick slowly through a path that produces a filter sweep you find useful. Hold REC and repeat that path. Release REC. The loop begins immediately.

**Move the cable**

Unplug Y1 from resonance and plug it into VCO FM or wavefolder amount instead.

```
                    ┌──────────────────────────────────────┐
Joystick (live) ──  │ CH1 JOYSTICK    X1 OUT               │──[C]──▶ VCF cutoff CV in
                    │                 Y1 OUT               │──[C]──▶ VCO FM in
                    └──────────────────────────────────────┘
                              Black Joystick2
```

What changed: the gesture now draws a relationship between filter position and FM depth rather than filter position and resonance. The same recorded arc produces a different timbral story because the two axes map to different processes. This is also the test for override: while the loop plays, grab the joystick and move it to a different position, then release. Observe the smooth fade back to the recorded path.

**What to listen for**

The loop should produce a continuously varying filter contour with no hard edges or repeating rhythmic pulses. If you hear a click at the loop point, the recorded start and end positions were too far apart; re-record with a path that returns closer to its starting point. During override, the transition back to the loop should be smooth. If it snaps, the joystick position save configuration option may be off; this does not affect the fade behavior itself, but confirms the configuration state.

---

### Patch 2: LFO with Recorded Rate and Depth Automation

In SINE mode, recording a joystick path captures the evolution of the LFO's rate and depth over time, turning what would be a fixed modulation rate into a scripted performance of the LFO's character.

**Channel layout for this patch:** CH1 in SINE mode. CH2 in JOYSTICK mode (optional, for a second simultaneous gesture).

**First Voice**

```
  Sequencer CV out ──[C]──▶ VCO 1V/OCT
  Sequencer gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  VCO audio out ──[A]──▶ VCF audio in ──▶ VCA audio in ──▶ Mixer
  [Black Joystick2] CH1 in SINE mode: joystick center position, X1 LFO active
```

Set the joystick to center before selecting SINE mode. Verify an LFO signal is present on X1 before proceeding.

**Add the LFO and record automation**

```
                         ┌──────────────────────────────────────┐
Joystick (live) ──       │ CH1 SINE        X1 OUT (LFO)         │──[C]──▶ VCF cutoff CV in
                         │                 Y1 OUT (90° shifted)  │──[C]──▶ VCO PWM or FM in
                         └──────────────────────────────────────┘
                                     Black Joystick2
```

Use a sequencer such as Hermod+ (or Ornament and Crime) to provide the pitch sequence. Use a VCF such as Erica Synths Black VCF (or Doepfer A-124) as the filter destination.

- `X1 OUT ──[C]──▶ VCF cutoff CV in`: the primary sinewave LFO sweeps the filter. Joystick X position sets rate; move right for faster sweeps. The LFO range is 0.1Hz to 32Hz, covering slow evolving motion through fast tremolo.
- `Y1 OUT ──[C]──▶ VCO PWM or FM in`: the 90-degree phase-shifted output drives a different destination simultaneously. Because it is offset in phase, the two targets never peak or trough at the same moment, creating a continuous rolling modulation rather than a synchronized surge.

To record automation: position the joystick where you want to begin. Hold REC. Over eight seconds, move the joystick through a path that brings the LFO from slow and shallow (center) to fast and deep (upper right corner) and back. Release REC. The LFO will now cycle through that rate and depth arc on loop, with the two outputs always maintaining their 90-degree phase relationship throughout the automation.

**What to listen for**

The filter sweep should accelerate and deepen gradually, then pull back, following the arc of the recorded gesture. The PWM or FM destination should respond simultaneously but with an offset that prevents the two modulations from stacking in phase. If the LFO sounds static, the joystick may not have covered enough range during recording; re-record with a wider path. If the two outputs feel synchronized rather than offset, confirm X1 is routed to one destination and Y1 to a different one.

---

## SNEW Mode

SNEW (South-North-East-West) is a four-quadrant CV panning mode. When a channel is set to SNEW, its X and Y outputs each carry unipolar 0V to +5V signals that respond to joystick direction rather than position. Moving the joystick east (right from center) raises X output toward +5V while the other outputs remain near 0V. Moving north raises Y output. Moving west raises X output of the paired channel. Moving south raises Y output of the paired channel.

SNEW requires two channels configured together: channels 1 and 2 form one SNEW pair, channels 3 and 4 form another. The mode is most immediately useful for controlling four VCAs in a quadraphonic or surround routing setup, where joystick direction corresponds to speaker position. It also works as a multi-channel crossfader or as simultaneous control of four different filter or VCA destinations with a single hand.

A dedicated patch is not included here. The routing requires four VCAs at minimum before any teaching can happen, and the pedagogical point (joystick direction controls four destinations simultaneously) is contained entirely in the description above. If spatial audio routing or quadraphonic performance is part of the workflow, SNEW is worth an extended session at the rack with the manual open.

---

## Controls Reference

**Joystick.** In JOYSTICK mode: X axis and Y axis generate CV. In SINE/RND modes: X position sets frequency, Y position sets amplitude. In Drone/Noise Oscillator modes: same X/Y mapping as their LFO counterparts.

**CH1 / CH2 / CH3 / CH4 (CHANNEL/MODE buttons).** Press one or more to select active channel(s). Multiple channels can be selected simultaneously for parallel control. Hold MODE and press a channel button to set that channel's mode; the selected mode button blinks.

**MODE button.** Hold MODE and press a channel button to change mode. Hold MODE and press REC to clear recorded motion on the selected channel.

**REC button.** Hold to record joystick motion. Release to begin looping automatically. Maximum eight seconds per channel.

**CLEAR.** Clears recorded motion. Equivalent to MODE + REC.

**X1-X4 outputs.** Primary CV outputs. In JOYSTICK mode: follows joystick X axis, -5V to +5V. In SINE mode: sinewave LFO primary phase. In RND mode: stepped random voltage primary. In SNEW mode: east/west panning CV, 0V to +5V.

**Y1-Y4 outputs.** Secondary CV outputs. In JOYSTICK mode: follows joystick Y axis, -5V to +5V. In SINE mode: sinewave LFO 90-degree phase shifted. In RND mode: stepped random voltage secondary. In SNEW mode: north/south panning CV, 0V to +5V.

**GATE3 / GATE4 outputs.** Gate outputs on channels 3 and 4 only. In JOYSTICK/SNEW: +5V during joystick movement. In SINE/RND LFO: +5V when CV is above 0V. In Drone/Noise Oscillator: squarewave audio output.

**Bicolor LEDs.** Green indicates positive CV on the output. Yellow indicates negative CV. Half-dimmed channel LED indicates an active motion recording is looping on that channel.

---

## Key Specs

| Parameter | Value |
|-----------|-------|
| HP | 12 |
| Depth | 30mm |
| +12V | 71mA |
| -12V | 20mA |
| CV output range | -5V to +5V |
| LFO range | 0.1Hz to 32Hz |
| Drone oscillator range | 32Hz to 1kHz |
| Max record time | 8 seconds per channel |
| Gate voltage | +5V |
| Outputs | 8 CV (X1-X4, Y1-Y4) + 2 gate (CH3/CH4 only) |

---

## Common Errors

**Assuming gates are available on all four channels.** Gate outputs exist only on channels 3 and 4. If you need gate output from a SINE or JOYSTICK gesture on channel 1 or 2, patch that channel to channel 3 or 4 and use those gates, or route the CV output into a comparator.

**Switching modes mid-session and losing recordings.** Changing the mode on a channel clears its recorded motion immediately and without warning. If a recording is in use in a live context, do not touch the MODE button for that channel.

**Expecting the sine oscillator to function as a clean audio source.** The internal sampling rate is 20kHz. The sine oscillator in Drone mode is intended for FM modulation at audio rates, not as a primary audio voice. At moderate FM index values it works well as a modulator; as a standalone sound source through a mixer it may produce aliasing artifacts at higher frequencies.

**Confusing joystick position with joystick movement for gate generation.** In JOYSTICK mode, the gate fires during movement, not while the joystick is held in a fixed position. A held joystick produces no gate. This matters for recorded gate patterns: the gate in a looping JOYSTICK recording reflects the motion of the original gesture, including any pauses.

**Forgetting joystick position save behavior.** If joystick position save is off (default configuration), switching from one channel to another immediately reflects the current joystick position on the new channel. If you had a carefully set rate/amplitude balance in SINE mode on CH1, switching to CH2 and back will change that balance unless you return the joystick to the original position. Enable joystick position save at power-on configuration if you need to preserve LFO rate/depth settings across channel switches.

---

## Notes

Erica Synths recommends the Black Joystick2 primarily as an interactive performance and modulation composition tool rather than a set-and-forget LFO source. The design rewards regular physical engagement: rate, depth, and gesture shape are all physical rather than knob-set, which means the module responds to how you use your body at the rack rather than how you dialed in a setting.

The module has no CV inputs for external modulation of any parameter. Rate, depth, and all gesture data are sourced entirely from the joystick. This is a deliberate constraint: the human body is the only modulation source the module accepts.

Full documentation is available at [ericasynths.lv](https://www.ericasynths.lv).
