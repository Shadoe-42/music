---
title: Percussion Interface + PI Expander
manufacturer: 4ms
primary_role: CONTROLLER
secondary_roles: [MODULATOR]
form_factor: eurorack
functions: [envelope-follower, gate-generator]
behavior_tags: [dynamic, performative, adaptive]
use_cases: [drum-to-gate conversion, velocity-sensitive envelope, sidechaining, acoustic-to-modular bridge]
hp: 8
depth: 29mm
memory: none
transport: none
screen: false
hybrid: false
cv: none
patch_format: v1
---

# 4ms Percussion Interface + PI Expander

**Audio-to-CV converter: generates gates and velocity-sensitive envelopes from any audio source**

![4ms Percussion Interface + PI Expander](https://github.com/Shadoe-42/music/raw/main/modular/images/4ms/percussion_interface/front_panel.jpg)
(https://github.com/Shadoe-42/music/raw/main/modular/images/4ms/percussion_interface/expander.jpg)

## Historical Context

The boundary between the acoustic world and the electronic control world is not natural. A drum being struck produces air pressure fluctuations. A Eurorack module waiting for a gate input expects a voltage transition from 0V to 8V. These are not the same thing, and bridging them requires a circuit that listens to one and speaks the other.

The envelope follower predates the modular synthesizer as a formal concept. Early voltage-controlled systems recognized that any time-varying signal could be used as a control source if it could be converted to a usable voltage range. The envelope follower detects the amplitude of an audio signal and outputs a voltage that tracks it: louder signal, higher voltage; quieter signal, lower voltage. That voltage, when routed to a filter cutoff or amplifier gain, produces the characteristic auto-wah effect that became a staple of 1970s funk production. The follower was also used to synchronize synthesizer events to live audio: when the bass guitar played a note above a certain threshold, a filter opened. When it stopped, the filter closed. The mechanism was the same as what the PI does, though the vocabulary of the time did not distinguish between envelope following and gate generation as cleanly as modular taxonomy now does.

In Eurorack, the practical problem the PI solves is this: a large portion of the world's rhythm is produced by instruments that do not speak CV. Acoustic drum kits, drum machines with audio outputs but no trigger outputs, samplers playing back grooves, a guitar being strummed percussively: all of these produce audio, not gates. The PI listens to that audio and translates it into the gate and envelope language the modular system understands. The acoustic snare can clock the sequencer. The velocity of the kick drum can open the filter. The beat already exists; the PI gives the modular rack access to it.

---

## Quick Start

The PI and PI Expander function as a single system. The PI handles input, gain, and mode selection; the Expander adds attenuation, a 1/4" input, audio output, and gain range switching. Both modules connect via an included 8-pin ribbon cable.

1. Connect the PI and PI Expander with the included ribbon cable. Red stripe orients toward the bottom of both modules.
2. Patch a drum machine audio output into the IN jack on the PI (or the 1/4" Input on the Expander if using an instrument cable; only one input is active at a time).
3. Set the L|M|H switch on the Expander to M (medium gain).
4. Set the Sensitivity knob to noon.
5. Play the drum machine. The LED above the Sensitivity knob should flash blue on each hit. If it flashes red, the signal is clipping; reduce Sensitivity or switch to L gain.
6. Patch the Gate Out jack to a module that accepts a trigger or gate input.
7. Verify the white Gate LED fires on each drum hit. Adjust Sensitivity until it fires cleanly on every intended hit without firing between hits.
8. Patch the + Env. Out jack to a filter cutoff CV input to hear the envelope modulating the filter on each drum hit.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width (PI + Expander) | 4 HP + 4 HP (8 HP total) |
| Depth (PI) | 25 mm |
| Depth (PI Expander) | 29 mm |
| Power (with Expander) | 104 mA +12V / 65 mA -12V |
| Power (PI only) | 69 mA +12V / 56 mA -12V |
| Gate output voltage | 8V |
| Gate pulse width | 6 ms to 0.5 s |
| Envelope output (+ Env) | 0V to 9V |
| Envelope output (- Env) | 9V resting, 0V at peak |
| Envelope attack | 15 ms |
| Envelope decay range | 70 ms to 6 s (exponential) |
| Gain range (L) | 0 to 2x |
| Gain range (M) | 0 to 20x |
| Gain range (H) | 0 to 500x |

The PI is sold with the PI Expander as a pair. The Expander draws power from the PI via the ribbon cable and does not require a separate power connection.

---

## What the PI Does

The PI converts an audio signal into three simultaneous outputs: a Gate, a positive envelope (+), and an inverted envelope (-). All three respond to the same input signal, governed by the same Sensitivity and gain settings, but they behave differently and serve different purposes.

The Gate fires when the input signal crosses a threshold (approximately 6.3Vpp post-gain). It goes high at 8V and stays high for a duration set by the Sustain knob (6ms to 0.5s). While the gate is high, it will not re-trigger, which prevents the drum's natural decay from generating unwanted additional gates. The Gate output clocks sequencers, triggers envelope generators, advances sample-and-hold circuits, and drives any module that expects a trigger or gate.

The + Env Out tracks the gain-boosted input signal's amplitude envelope and converts it to a 0V-to-9V control voltage. In Gen mode, this envelope has a fast attack, a sustain period matching the gate pulse width, and a decay controlled by the Env. Decay knob. The shape is consistent on every trigger regardless of how hard the drum was hit. In Follow mode, the envelope amplitude reflects the actual velocity of the hit: harder hits produce higher peak voltages; softer hits produce lower peak voltages. The shape is not fixed.

The - Env Out (inverted) rests at 9V and falls to 0V when the envelope is triggered, then returns to 9V as the decay completes. This is not a utility inversion; it is a purpose-built sidechain signal. A module with a VCA that normally responds to positive CV can receive the inverted envelope directly: when the kick drum fires, the 9V resting voltage drops, the VCA closes, and the audio ducks. No additional inversion circuitry is required.

---

## Gen Mode vs. Follow Mode

The Follow/Gen switch is the most consequential control on the module. It determines whether the envelope reflects what the module is told to produce (Gen) or what the audio source actually did (Follow).

**Gen mode** generates a fixed envelope shape on every trigger regardless of input velocity. The attack is fast (15ms), the sustain holds for the duration of the gate pulse, and the decay falls exponentially at the rate set by Env. Decay. The same envelope appears whether the drum was hit hard or barely tapped, as long as the hit exceeded the Sensitivity threshold. Gen mode is predictable. It is the right choice when consistent modulation is the goal: when the envelope should serve as a reliable, repeatable control signal that happens to be triggered by a drum, not as a reflection of how hard the drum was struck.

**Follow mode** allows the envelope amplitude to vary with the input signal's amplitude. Harder hits produce higher peak voltages; softer hits produce lower voltages. The envelope shape tracks the contour of the input signal more closely rather than following a fixed sustain-decay pattern. The gate and envelope outputs can fire at different times in Follow mode because the envelope responds to amplitude peaks in the signal rather than being synchronized to the gate. Follow mode is the right choice when velocity sensitivity is the goal: when the modulation should be louder, more aggressive, or more open when the playing is harder, and quieter, more restrained when the playing is softer.

The practical difference: in Gen mode, a snare hit and a ghost note both produce the same filter sweep, as long as both exceed the Sensitivity threshold. In Follow mode, the snare hit produces a wide filter opening and the ghost note produces a narrow one. The pattern breathing in and out of dynamics follows the performance.

---

## Setting Input Gain

Gain on the PI is set in two stages. The L|M|H switch on the Expander sets the gain range; the Sensitivity knob adjusts within that range. The appropriate range depends on the source.

L (Low Gain, 0-2x) is for modular-level signals and professional line-level sources. Modular outputs are already at high amplitude; feeding them through medium or high gain will clip immediately.

M (Medium Gain, 0-20x) is for instrument-level signals: drum machines with standard audio outputs, electric guitar pickups, line-level keyboards, low-impedance microphones.

H (High Gain, 0-500x) is for high-impedance microphones, piezo contact microphones, and any source with a very low output level.

The Sensitivity LED indicates gain status. Blue means signal is detected and below the clip threshold (2.5Vpp post-gain). As the signal approaches and exceeds the clip point, the LED transitions toward red. A red LED indicates clipping, which can generate misfires. If the LED is clipping on normal hits, reduce Sensitivity or switch to a lower L|M|H setting.

If using the PI without the Expander, the gain range is set via a jumper on the back of the PI module. The default with no jumper is medium gain.

---

## Preventing Misfires

Acoustic drums and drum machines with long decays can generate multiple gates from a single hit. The PI interprets the resonant decay of the drum as a second or third hit if Sensitivity is set too high relative to the decay amplitude. Misfires appear as extra gate pulses after the intended one.

The primary tool for misfire prevention is the Sustain knob. When the gate is high, the PI will not re-trigger. By setting Sustain long enough that the gate remains high for the entire decay period of the source, the PI becomes blind to the decay and fires only once per intended hit. Set Sustain long enough to cover the decay, but no longer; an excessively long Sustain will cause the PI to miss rapid sequential hits because it cannot re-trigger while the previous gate is still high. The trade-off is between misfire rejection and speed.

A second approach is reducing Sensitivity. Turning Sensitivity down raises the threshold the input must exceed to trigger a gate. If the initial transient is well above the threshold but the resonant decay is not, only the transient triggers. This works reliably for consistent sources (electronic drum machines) but risks missed triggers with variable sources (acoustic drums with varying strike force). Use Sustain for acoustic sources; use Sensitivity reduction for electronic ones.

The CAL LOCK-OUT trim pot on the back of the PI sets an absolute re-trigger minimum, defaulting to 100ms (10Hz). It operates independently from the Sustain knob and defines the fastest rate at which the PI can fire successive gates. In Gen mode, setting the trim pot appropriately allows Sustain to be adjusted freely for envelope shaping without affecting misfire rejection behavior.

---

## Patch Examples

### 1. Drum Machine Gate to Sequencer Clock (Gen Mode)

Feeding a drum machine audio output into the PI and routing the Gate Out to a sequencer clock input synchronizes the sequencer to the audio beat rather than to a dedicated clock module.

**Establish the Signal Path**

Before connecting the Gate Out to the sequencer, verify the PI is firing cleanly:

```
Drum machine audio out ──[A]──▶ PI IN
```

Set L|M|H to M. Set Sensitivity to noon. Play the drum machine. Confirm the Gate LED fires on every kick or snare hit and not between them. Adjust Sensitivity and Sustain as needed to eliminate misfires.

**Connect to Sequencer**

```
                    ┌────────────────────────────────────┐
                    │ Follow/Gen: Gen                     │
                    │ Sensitivity: set for clean gate     │
Drum machine ──[A]──▶│ IN               GATE OUT          │──[G]──▶ Sequencer clock in
                    └────────────────────────────────────┘
                              4ms Percussion Interface
                    Sustain: adjusted to cover drum decay
```

- `Drum machine ──[A]──▶ PI IN`: the PI listens to the audio output, not the trigger output of the drum machine. This works even for drum machines with no dedicated trigger or gate jacks.
- `Gate Out ──[G]──▶ Sequencer clock in`: each drum hit advances the sequencer by one step. The sequencer tempo is now defined by the rhythm of the drum machine audio, not by a separate clock source.

**Move the cable**

Unplug the Gate Out from the sequencer clock and plug it into the trigger input of an envelope generator instead. Leave the sequencer running freely from its own clock.

```
                    ┌────────────────────────────────────┐
Drum machine ──[A]──▶│ IN               GATE OUT          │──[G]──▶ EG trigger in
                    └────────────────────────────────────┘
```

What changed: the drum hit now triggers the envelope generator directly. Any module downstream of the EG responds on every drum hit. The drum machine becomes the performance trigger for a modular voice rather than a clock source for a sequencer.

**What to listen for**

The sequencer should advance in exact time with the drum machine's kick or snare, whichever output is connected. If the sequencer advances twice per hit, increase Sustain to extend the gate length and suppress the misfire. If the sequencer occasionally skips a step, Sensitivity is set slightly below threshold for the softest hits; nudge it up slightly. In the Move, the EG trigger should fire in strict rhythm with the drum machine. Any delay between the drum hit and the module's response indicates the Sensitivity threshold is too high; the PI is detecting the hit late in its decay rather than at its transient.

---

### 2. Velocity Envelope for Filter Modulation (Follow Mode)

In Follow mode, the PI generates envelopes whose peak voltage reflects the amplitude of each hit. Routing the + Env. Out to a filter cutoff creates a filter that opens wider on harder hits and narrower on softer hits, tracking the dynamics of the performance.

**Establish the Signal Path**

```
Drum machine audio out ──[A]──▶ PI IN
```

Switch to Follow mode. Set L|M|H to M. Set Sensitivity so that the gate fires on your softest intended hit but not on bleed from adjacent sources. Confirm the gate fires at maximum Sensitivity on hard hits and fires a noticeably smaller envelope on soft hits (Follow mode LED brightness will vary with hit strength).

**Connect the Envelope to Filter**

```
                    ┌────────────────────────────────────────────┐
                    │ Follow/Gen: Follow                          │
                    │ Sensitivity: lowest setting that            │
                    │   still triggers on softest hits            │
Drum machine ──[A]──▶│ IN             + ENV OUT                   │──[C]──▶ Filter cutoff CV
                    └────────────────────────────────────────────┘
                              4ms Percussion Interface
                    Env. Decay: set to taste (try noon)
```

Set filter cutoff at minimum. The PI envelope will push the filter open on each hit; cutoff knob position defines the floor, the envelope defines how far above it the filter travels on each hit.

- `+ Env. Out ──[C]──▶ Filter cutoff CV`: each drum hit opens the filter to a degree proportional to the velocity of that hit. A loud snare snap opens the filter fully; a ghost note barely cracks it.

**Move the cable**

Unplug the + Env. Out from the filter cutoff and plug it into the pitch CV input of an oscillator instead (treat as FM or coarse pitch modulation, not 1V/octave tracking).

```
                    ┌────────────────────────────────────────────┐
Drum machine ──[A]──▶│ IN             + ENV OUT                   │──[C]──▶ VCO FM in
                    └────────────────────────────────────────────┘
```

What changed: the envelope is now pitching the oscillator rather than opening a filter. Louder hits produce larger pitch jumps; softer hits produce smaller ones. This is a different musical result from the same CV source and the same drum pattern.

**What to listen for**

With the filter: harder hits should produce a noticeably more open, brighter sound. Softer hits should produce a darker, more filtered result. If all hits produce the same filter opening, Sensitivity is set too high; the input is clipping and all envelopes are hitting the same peak voltage. Reduce Sensitivity or L|M|H gain until the filter opening clearly varies between soft and hard hits. Adjust Env. Decay to control how quickly the filter closes after each hit; shorter decay produces a tight click-open-shut character; longer decay produces a slow breath.

---

### 3. Sidechaining: Duck a Synth Voice on Every Kick (Gen Mode)

The inverted envelope output rests at 9V and collapses to 0V when the PI triggers. Routing it to a VCA's CV input causes the VCA to close on every kick drum hit and recover as the envelope decays back to 9V.

**Establish the Baseline Voice**

Before connecting the PI to the sidechain, establish a continuous synth voice:

```
  Sequencer CV out ──[C]──▶ VCO 1V/OCT
  VCO audio out ──[A]──▶ VCA audio in ──▶ Mixer
  VCA CV in: set to receive external CV (no EG connected)
```

Set the VCA to open fully with 9V at its CV input (the Inv. Out resting voltage). Confirm the synth voice is audible and continuous.

**Connect the Kick Drum to the PI**

```
                    ┌────────────────────────────────────────────────┐
                    │ Follow/Gen: Gen                                 │
                    │ L|M|H: M. Sensitivity: clean gate on kick only  │
Kick drum ──[A]──▶  │ IN             - ENV OUT (Inv. Out, Expander)   │──[C]──▶ VCA CV in
                    └────────────────────────────────────────────────┘
                              4ms Percussion Interface + PI Expander
                    Sustain: minimum without misfires
                    Env. Decay: controls ducking recovery time
```

Use the Inv. Out on the PI Expander (with Inv. Level knob) rather than the - Env. Out on the main PI module. The Inv. Level knob controls the depth of the duck without affecting the Sensitivity threshold or gate behavior.

- `Kick drum ──[A]──▶ PI IN`: the PI listens only to the kick drum channel. A dedicated kick drum output from a drum machine, or a microphone positioned on the kick drum, works here.
- `Inv. Out ──[C]──▶ VCA CV in`: the 9V resting voltage keeps the VCA fully open. When the kick fires, the inverted envelope collapses to 0V and the VCA closes. As the Env. Decay rises, the 9V returns and the VCA re-opens.

**Move the cable**

Leave the sidechain connected. Adjust the Inv. Level knob on the Expander from maximum down to 50%.

What changed: the Inv. Out now rests at approximately 4.5V rather than 9V, and falls to 0V on each kick. The VCA no longer fully opens at rest; it sits at half gain between kicks. This produces a less dramatic duck; the synth voice is always audible but dips on each kick rather than being cut fully.

**What to listen for**

The synth voice should be clearly audible between kicks and clearly dimmer on each kick hit. The Env. Decay knob sets how quickly the voice recovers to full level; short decay produces a tight pump that opens immediately after the kick; long decay produces a slow swell back up. If the ducking depth is insufficient, verify the VCA is responding to the full 9V-to-0V swing; some VCAs have an attenuator on their CV input that limits the range. In the Move, the synth voice should never reach full level between kicks, sitting at a steady reduced volume that deepens on each kick hit.

---

## Essential Parameters

**Sensitivity knob.** Controls how much the input signal is amplified before threshold detection. Higher sensitivity means softer signals trigger gates. The LED shows blue when signal is present below clipping and transitions toward red as the signal clips. Clipping causes misfires; back off Sensitivity or switch L|M|H to a lower gain range.

**L|M|H switch (PI Expander).** Sets the gain range: L (0-2x) for modular and professional line level, M (0-20x) for instrument and standard line level, H (0-500x) for high-impedance mics and piezo contact mics. Sets the upper gain limit within which the Sensitivity knob operates. Without the Expander, this is set via a jumper on the back of the PI.

**Sustain knob.** Sets gate pulse width (6ms-0.5s) in both modes. In Gen mode, simultaneously sets the envelope sustain duration. While the gate is high, no additional gates fire; Sustain is the primary misfire prevention tool for sources with long decays. Longer Sustain = less susceptibility to misfires but slower maximum re-trigger rate.

**Env. Decay knob.** Sets the exponential decay time of the envelope (70ms to 6s). In Gen mode, determines how quickly the envelope falls from sustain to 0V after the gate closes. In Follow mode, determines how quickly the envelope falls when the input signal falls. Does not affect gate pulse width.

**Follow/Gen switch.** Gen: consistent envelope shape on every trigger, synchronized with gate. Follow: envelope amplitude tracks input velocity; louder hits produce higher envelopes; gate and envelope may fire at different times.

**Gate Out jack.** 8V gate/trigger output. Fires on every detected hit. Use to clock sequencers, trigger envelope generators, or advance any clock-dependent module. White LED indicates gate state.

**+ Env Out jack (PI main module).** 0-9V positive envelope. Blue LED tracks envelope voltage. Use for filter cutoff CV, VCA gain CV, or any destination where a positive push is the desired modulation.

**- Env Out jack (PI main module).** Inverted envelope. Rests at 9V; falls to 0V on trigger; returns to 9V as decay completes. Green LED dims when envelope is active. Use for sidechaining without additional inversion circuitry.

**Env. Out and Inv. Out jacks (PI Expander).** Attenuated versions of the + and - outputs from the main PI, controlled by Env. Level and Inv. Level knobs respectively. Preferred for sidechain depth control; use these knobs to set the modulation amount rather than adjusting Sensitivity, which changes the trigger threshold as well as the envelope level.

**Audio Out jack (PI Expander).** Buffered, amplified version of the input signal at modular level. Functions as a microphone preamp: a low-level mic signal can be routed through the PI for CV/gate extraction and simultaneously sent to a mixer or effects chain at usable amplitude.

**CAL LOCK-OUT trim pot (back of PI).** Sets the absolute minimum re-trigger period. Default: 100ms (10Hz). Turning counterclockwise allows faster re-triggers; turning clockwise increases the lockout period. Useful in Gen mode to set misfire rejection independently from envelope shaping.

---

## Why Percussion Interface + PI Expander Excels

The PI solves a specific problem that few modules address: getting the acoustic world into the modular vocabulary. Drum machines produce audio, not gates. Acoustic drums produce air pressure, not control voltage. The PI accepts both and generates something the modular system can use from either. That bridging function is genuinely rare. Most CONTROLLER modules assume the control signals already exist and need routing or processing. The PI creates them from scratch out of audio.

The two-mode architecture covers the two primary use cases without requiring separate modules for each. Gen mode handles deterministic applications: clock the sequencer on every kick hit, trigger the envelope generator on every snare, fire the sample on every hi-hat. The envelope is consistent, predictable, and independent of how hard each drum is struck. Follow mode handles expressive applications: let the velocity of each hit shape the filter sweep, control the oscillator pitch bend, or modulate reverb depth. One module, one switch position, two fundamentally different musical behaviors.

The inverted envelope as a purpose-built sidechain signal reflects a design decision worth appreciating. The module could have output only the positive envelope and left sidechain applications to an external inverter or attenuverter. Instead, the - Env Out rests at 9V and collapses to 0V on each trigger, precisely the behavior a VCA CV input expects when the goal is ducking. The Inv. Level knob on the Expander sets duck depth without touching Sensitivity or gate threshold. The sidechain is built in and requires no additional utility modules to implement.

At 8HP for the pair, the PI and Expander together occupy a modest panel footprint for the range of functions they cover: mic preamp, gate generator, envelope follower, velocity sensor, sidechain source, and audio output all from a single input.

---

## Advanced Learning Path

**Threshold-based event triggering with two PI modules.** Set two PI modules to different Sensitivity levels, both receiving the same audio source. The lower-sensitivity unit fires only on loud hits; the higher-sensitivity unit fires on all hits. Route each Gate Out to a different downstream module. The result: one event fires on every hit, a different event fires only on hard hits. This is a velocity-to-event routing system built entirely from gain staging.

**Envelope as FM modulation source in Follow mode.** Route the + Env. Out in Follow mode to the FM input of an oscillator rather than a filter. Each drum hit pitches the oscillator by an amount proportional to hit velocity. Combined with a short Env. Decay, this produces a pitched click on each hit; with a longer decay, it produces a slow pitch drop. Adjust Env. Decay to control the pitch envelope character per hit.

**Using Audio Out as a parallel processing tap.** The Expander's Audio Out provides the amplified input signal at modular level. This allows the PI to simultaneously generate CV/gate signals from the input and route the audio through the modular signal path for processing. A microphone routed through the PI generates gates for the modular and simultaneously feeds the microphone audio into a filter or effects chain for live processing.

**Self-reinforcing sidechain loop.** Route the Inv. Out to the CV input of a VCA that the drum machine audio is also passing through. The kick drum ducks its own audio signal at the VCA: the transient passes at full level (the envelope has not yet fired), the body of the kick is ducked, and the tail recovers as the envelope decays. This produces a transient-forward, body-reduced kick drum character from the modular processing chain.

**Velocity-controlled sample-and-hold.** Route the Gate Out to the trigger input of a sample-and-hold and the + Env. Out (in Follow mode) to the sample-and-hold's input. Each drum hit captures the current envelope voltage, which reflects that hit's velocity. The S&H output holds that voltage until the next hit. Route the S&H output to a filter cutoff or oscillator pitch: the filter or pitch ratchets to a new position on each hit, with the destination voltage determined by how hard the previous hit was. The pattern of dynamics becomes a pattern of stepped CV values.

---

## Pairs Well With

**Pamela's Pro Workout (ALM Busy Circuits).** The PI Gate Out synchronized to a kick drum and Pamela's clock running the rest of the system creates a hybrid timing architecture: the kick drum defines one rhythmic reference point and Pamela defines subdivisions and polyrhythms relative to its own internal clock. The two clocks will drift unless Pamela is also reset by the PI gate.

**Endorphin.es Grand Terminal.** The Grand Terminal's Airplane envelope inputs accept external CV to modulate the internal envelope's response time. Routing the PI + Env. Out (Follow mode) to an Airplane CV input means louder drum hits produce longer Airplane envelope times, changing filter response dynamically with performance velocity.

**Patching Panda Etna.** The Etna's three filter channels with independent frequency CV inputs provide multiple destinations for the PI's envelope output. Routing the + Env. Out to the FREQ ALL CV input opens all three filter channels simultaneously on each drum hit; routing it to a single channel's FREQ CV adds differential modulation to that channel relative to the others.

**Mutable Instruments Rings.** Routing the Gate Out to Rings' STRUM input triggers the resonator on each drum hit. In Follow mode, routing the + Env. Out to Rings' BRIGHTNESS or POSITION inputs makes the timbre of each resonator strike proportional to the velocity of the drum hit that triggered it.

**MISO (Tiptop Audio).** The PI's envelope outputs peak at 9V, which exceeds the expected range of some filter and VCA CV inputs (typically 0-5V or 0-8V). The MISO's attenuverter section scales the 9V output to the appropriate range for the destination without requiring a separate utility module.

**Endorphin.es New Godspeed.** Routing the PI Gate Out to the New Godspeed's external trigger input (if available) and the + Env. Out to the INDEX CV input creates a drum-triggered FM voice whose FM depth varies with the velocity of each hit. Harder hits produce denser, more complex FM sidebands; softer hits produce cleaner, more pure oscillator output.

---

## Common Mistakes

**Leaving L|M|H at H for electronic sources.** High gain (0-500x) is for contact mics and high-impedance microphones. A drum machine audio output at H gain will clip immediately and produce constant misfires. Start at M for electronic sources; move to L if still clipping.

**Adjusting Sensitivity to control envelope level in Follow mode.** Sensitivity changes the threshold at which the gate fires and changes the gain applied to the signal before envelope tracking. Turning it down to reduce the envelope output level will also reduce the velocity sensitivity range and raise the gate threshold, potentially causing missed triggers on soft hits. Use the Env. Level and Inv. Level knobs on the Expander to control output amplitude without affecting gate behavior.

**Expecting the inverted envelope to start at 0V.** The - Env. Out rests at 9V, not at 0V. A module receiving the inverted envelope that expects a 0V resting state will behave unexpectedly: a VCA connected to - Env. Out will be open at rest and close on each trigger, which is the correct behavior for ducking but may not be the intended behavior for other applications. Use the + Env. Out when a 0V resting state is required.

**Using Gen mode for velocity sensing.** In Gen mode, the envelope amplitude is fixed regardless of how hard the input is struck. A ghost note and a hard snare hit produce the same envelope as long as both exceed the Sensitivity threshold. Follow mode is required for velocity-sensitive behavior.

**Setting Sustain so long that fast patterns miss steps.** The gate will not re-trigger while it is high. A Sustain long enough to suppress misfires on a slow pattern may be too long for a fast one: if the gate from the first hit is still high when the second hit arrives, the second hit is ignored. Balance Sustain against the fastest expected tempo of the source.

**Ignoring the CAL LOCK-OUT trim pot.** The default lockout period of 100ms (10Hz) prevents re-triggers faster than 600BPM. At normal musical tempos this is sufficient. But very fast percussion sources or high-frequency audio inputs can produce valid signals faster than the lockout allows. If the PI is consistently firing at half the expected rate, the input signal is faster than the lockout period; adjust the trim pot counterclockwise to allow faster re-triggering.

---

## What's Next

The PI establishes a gateway between the acoustic world and the CV world. The gate output it generates is a clock signal: it carries timing information extracted from a live audio source. The guides for Pamela's Pro Workout and Hermod+ cover what to do with clock signals once they exist: how to subdivide them, multiply them, and distribute them across a patch.

The envelope output pairs directly with any module that accepts a CV input for parameter modulation. The Etna, Grand Terminal, and New Godspeed guides demonstrate how filter cutoff CV, FM depth CV, and envelope time CV respond to external modulation sources of the kind the PI generates.

The sidechaining application is a specific case of VCA CV control. The VCA section of the basics guides covers gain staging and how VCA CV inputs respond to different voltage ranges and resting states.

---

*Depth: 25mm (PI) / 29mm (PI Expander). Power: 104mA +12V / 65mA -12V (pair). Sold as a pair only.*
