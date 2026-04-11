# ALM Busy Circuits Pamela's PRO Workout Guide

**Module:** ALM034 Pamela's PRO Workout  
**Manufacturer:** ALM Busy Circuits  
**Format:** Eurorack  
**HP:** 8HP | **Depth:** 32mm  
**Power:** +12V 60mA / -12V 10mA  
**Firmware:** 130 (March 2026)

![ALM Busy Circuits Pamela's PRO Workout](https://github.com/Shadoe-42/music/raw/main/modular/images/alm_busy_circuits/pamelas_pro_workout/front_panel.jpg)  
*8HP clock and modulation hub — 8 independently configurable outputs, Euclidean patterns, FLEX micro-timing, 4 CV inputs. Firmware 130.*

---

## Quick Reference

| Spec | Value |
|------|-------|
| Outputs | 8, independently configurable |
| Output voltage | 0–5V buffered, 12-bit resolution |
| Max output rate | 3.8kHz |
| CV inputs | 4 panel (CV1–CV4); CLK and RUN reassignable as CV5/CV6 |
| CV input range | 0–5V |
| Internal BPM range | 10–330 BPM, 0.5 BPM increments |
| Waveform types | 11 |
| FLEX micro-timing modes | 7 |
| Cross operations | 17 |
| Save banks | 64 |

---

## What Is a Clock Module?

In a modular system, timing does not happen automatically. Something has to generate the rhythmic pulse that everything else follows. That is what a clock module does.

A clock outputs a steady, repeating signal — typically a square wave gate — at a set tempo measured in BPM. Other modules receive that pulse and use it to trigger envelopes, advance sequencer steps, sync LFOs, reset patterns, and drive percussion. Without a clock, nothing knows when to happen.

Pamela's PRO Workout extends this idea considerably. Rather than outputting a single clock pulse, it generates up to 8 independent outputs — each running at its own speed, shape, and pattern, all derived from the same master tempo. A single BPM setting of 120 can simultaneously produce a quarter-note gate for a kick, a 16th-note pulse for a hi-hat, a slow triangle LFO sweeping a filter, and a 3-of-8 Euclidean pattern for a percussion accent. All locked together. All from one module.

---

## The Navigation Model

This is the most important section in the guide. Pamela's has no dedicated knob per function — every parameter is accessed through a single encoder and a display. Understanding how to move around the module is the foundational skill.

**Mental model:** Pamela's has 8 independent output lanes. Each lane has its own complete set of parameters — wave type, speed, shape, timing, modulation. The display is a window into one lane at a time. You select a lane, configure it, then move to the next.

**How navigation works:**

- Turn the Program knob to change the value of the currently selected parameter
- Press the Program knob briefly to move between parameter pages within the current output
- Hold the Program knob to access the output selection screen, then turn to choose a different output
- The 8 output LEDs show activity on all outputs in real time, regardless of which one is currently being edited
- The Start/Stop button starts and stops the master clock

**The muscle memory:** Select output → navigate to parameter → edit value → move to next output. Every session on Pamela's is some variation of this sequence.

**The common failure mode:** You configure OUT 1, navigate to check OUT 3, make a small adjustment, and continue editing — not realizing you are now working in OUT 3. The display always shows which output is active. Check it before turning the knob.

---

## Clock Setup

### What a Clock Module Does in Practice

When the clock runs, it generates a pulse stream at the master BPM. Every output on Pamela's derives its timing from this stream through division or multiplication. An output set to /4 fires once every four beats. An output set to x4 fires four times per beat. All eight outputs are always locked to the same source tempo, so they stay in rhythmic relationship with each other no matter how complex the individual patterns get.

### Internal BPM

Press Start/Stop to start the clock. The BPM screen shows the current tempo. Hold the Program knob and navigate to the BPM parameter to adjust. Range is 10–330 BPM in 0.5 BPM increments.

### External Clock Sync

Pamela's can follow an external clock source patched into the CLK input — a sequencer, drum machine, DAW MIDI interface, or another module. For reliable lock:

- **Use a 24 PPQN clock signal.** Pamela's needs to subdivide the incoming clock internally, so high resolution is critical. 24 pulses per quarter note (Din Sync standard) is the recommended minimum. Lower PPQN values will sync but with less accuracy.
- **Use a Run signal.** Patch a gate into the RUN input — high when the external clock is playing, low when stopped. Without a Run signal, Pamela's has to infer when the clock stopped and started, which introduces uncertainty at downbeats.
- **Match the PPQN setting.** In Pamela's settings, set the PPQN value to match the clock source. A mismatch causes the displayed BPM to read incorrectly and patterns to run at the wrong tempo relative to external gear. Set to 24 unless the source specifies otherwise.

Two Pamela's units can be synced together by patching one unit's x24 output into the second unit's CLK input, and a GATE output set to 'On' into the second unit's RUN input.

---

## Per-Output Parameters

Each of the 8 outputs can be independently configured with the following parameters.

### Wave Types (11)

| Wave | Signal | Behavior |
|------|--------|----------|
| SIN | [C] | Sine — smooth, continuous oscillation |
| TRI | [C] | Triangle — linear rise and fall |
| SAW | [C] | Sawtooth — slow rise, instant drop |
| RSAW | [C] | Reverse saw — instant rise, slow drop |
| SQR | [G] | Square — equal on/off gate |
| PULSE | [G] | Short trigger pulse — for percussion triggers |
| RATCHET | [G] | Multiple rapid triggers per division |
| S&H | [C] | Sample and hold — random stepped values |
| SLEW | [C] | Slewed random — S&H with smooth transitions |
| LOG | [C] | Logarithmic envelope shape |
| TRAPEZOID | [C] | Attack, hold, decay shape |

All outputs are 0–5V. CV-type waveforms oscillate within that range. Gate outputs go to 5V high and 0V low.

### Division and Multiplication

Sets the output rate relative to master BPM. Divisions slow the output; multipliers speed it up.

| Setting | Result at 120 BPM |
|---------|-------------------|
| /64 | One cycle every 64 beats — very slow LFO or long shape |
| /4 | One cycle per bar (4/4) |
| /1 | One cycle per beat (quarter note) |
| x2 | Twice per beat (8th notes) |
| x4 | Four per beat (16th notes) |
| x192 | Maximum multiplier — approaches audio rate |

### Phase

Offsets the start point of the waveform within its cycle. Useful for staggering two outputs that share a division, or aligning a trigger to fire slightly before or after a beat.

### Amplitude

Scales the output level from 0–100%. Reduces the peak output voltage proportionally.

### Offset

Shifts the output voltage up or down within the 0–5V range. Useful for biasing a CV output toward a specific voltage range to match the target module's expectations.

### Euclidean Patterns

Euclidean rhythm distributes a set number of hits as evenly as possible across a set number of steps. The result is patterns that feel musical and organic rather than mechanical, because the spacing between hits is as equal as the math allows.

- **Steps:** Total number of steps in the pattern (the loop length)
- **Hits:** Number of active triggers distributed within those steps
- **Rotation:** Shifts the pattern start point around the step circle — same hits, different downbeat
- **Padding:** Adds empty steps after each active hit, creating breathing room

A classic example: 5 hits over 8 steps produces a pattern found across West African drumming, Cuban clave, and most of electronic music's recurring grooves. Rotating it by 2 shifts where the phrase lands relative to the bar.

Euclidean mode applies to gate and trigger wave types. The output fires only on the active steps of the pattern.

### Probability

Sets the percentage chance that any given trigger fires. At 100%, every hit fires. At 50%, roughly half fire at random. At lower values, the output becomes sparse and unpredictable.

Probability applies per step — each active step rolls independently. A 5-of-8 Euclidean pattern at 70% probability produces a groove that shifts slightly on every loop without losing its fundamental rhythmic character.

### Loop / Nap / Wake

**Loop** sets a finite number of cycles before the output stops. **Nap** defines how many beats the output stays dormant after completing its loop. **Wake** defines how many beats before it restarts. Together these allow outputs to phase in and out on long timescales without manual intervention — useful for evolving arrangements and generative structures.

### Invert

Flips the output polarity. A gate that is normally high becomes a gate that is low, and vice versa. Useful for creating complementary patterns or driving modules that respond to falling edges rather than rising ones.

---

## FLEX Micro-Timing

FLEX operations apply small timing deviations to an output's triggers or waveform transitions. All FLEX modes affect *when* events fire within a beat, not the overall tempo. The master clock is unchanged.

| FLEX Mode | Behavior |
|-----------|----------|
| HUMAN | Random micro-timing variation — slight unpredictable push and pull on each event |
| SWING | Classic swing — alternates between early and late placement of subdivisions |
| RAMP UP | Gradually accelerates timing of events over the loop — builds energy toward the end |
| RAMP DOWN | Gradually decelerates timing of events — releases tension across the loop |
| HUMP | Events cluster toward the middle of the loop — energy centered around the midpoint |
| DELAY | Consistent offset — all events shifted by a fixed amount after the beat |
| PWR2 | Power-of-2 timing — produces a bouncing ball deceleration effect |

FLEX is additive. It sits on top of existing division and Euclidean settings. A 4-of-8 Euclidean pattern with SWING produces a swinging Euclidean groove. A straight quarter-note output with HUMAN loses its metronomic rigidity and starts to breathe.

---

## CV Modulation

Pamela's has four CV inputs on the panel (CV1–CV4). Each can be assigned to control any parameter on any output. The CLK and RUN inputs can also be reassigned as additional CV inputs (CV5/CV6) when external clock sync is not in use, for a total of six possible CV sources.

For each CV assignment:
- **Attenuation:** Scales how much the incoming CV affects the target parameter (0–100%)
- **Offset:** Shifts the CV center point before it reaches the parameter (-100% to +100%)

CV assignments are per-output and per-parameter. One CV input can simultaneously modulate the division on OUT 2 and the probability on OUT 6. The system is flexible but intentional — nothing is pre-routed. To assign a CV, navigate to the parameter to be modulated, access its CV assignment page, and select which input to use.

---

## Cross Operations

Cross operations allow one output's current value to influence another output's value in real time. Rather than running completely independently, two outputs can be placed in a defined relationship.

There are 17 cross operation types, including logic operations (AND, OR, XOR) and arithmetic operations (ADD, MULTIPLY). A logic AND between OUT 1 and OUT 2, for example, produces a high output only when both are simultaneously high — a rhythm that fires only on the overlap between two patterns.

Cross operations are powerful and interconnected enough to warrant their own dedicated document. For now: treat them as a tool for creating rhythmic interdependence between outputs — patterns that respond to each other rather than running in isolation. Explore them once individual output configuration is comfortable.

---

## Banks

A bank stores the complete state of all 8 outputs plus the current BPM. 64 banks are available.

- **Save Bank:** Hold Program knob → navigate to Save Bank → select a slot (1–64) → confirm
- **Load Bank:** Hold Program knob → navigate to Load Bank → select slot → confirm

Current output settings are saved automatically across power cycles, so Pamela's returns to its last state on startup. Banks are for intentional snapshots — complete configurations worth recalling reliably, especially in a live performance context.

**USB-C Backup:** Connect Pamela's to a computer via USB-C while unpowered. It mounts as a removable drive. Copy `PPWDATA.BAK` to your computer to back up all 64 banks. Copy it back to restore. On macOS Ventura, use Terminal with `rsync` rather than Finder if copy errors occur.

**Factory Reset:** Hold the Program knob during power-up until the bar fills. This clears all saved data back to factory state.

---

## Scope Display

Pamela's includes a built-in oscilloscope view that displays the current waveform for the selected output. Useful for visually confirming a shape, checking amplitude and offset settings, and diagnosing unexpected output behavior. Access it from the display menu. It is a diagnostic and configuration tool, not a performance feature.

---

## Expanders

Four expander modules are available as separate purchases. All connect to the rear of the module — the PPEXP expanders and the AXON expanders use different connectors on different parts of the PCB. Read the manual carefully before connecting.

- **PPEXXP1 / PPEXXP2:** Add Din Sync and MIDI Clock outputs plus fixed-factor pulse outputs (x1, x2, x4, /4, /16, stop trigger). Connect to the MIDI-EX 5-pin connector at the top right of the PCB rear.
- **AXON-1:** Adds 4 extra CV inputs. Connects to the EXPAND 6-pin connector at the bottom left of the PCB rear.
- **AXON-2:** Adds 4 extra CV inputs plus 2 assignable buttons with configurable functions (tap tempo, bank navigation, mute, and more). Connects to the EXPAND header. Requires firmware v120 or later.

---

## Patch Examples

### Patch 1: Polyrhythmic Gate Network

Four gate outputs driving independent percussion triggers. Each output runs at a different division with different pattern density.

```
┌──────────────────────────────────────────┐
│         Pamela's PRO Workout             │
│                                          │
│  OUT 1 ○──[G]──────────────────────────▶ Kick ENV trigger
│  OUT 2 ○──[G]──────────────────────────▶ Snare ENV trigger
│  OUT 3 ○──[G]──────────────────────────▶ Hi-Hat trigger
│  OUT 4 ○──[G]──────────────────────────▶ Percussion trigger
└──────────────────────────────────────────┘
```

| Output | Wave | Division | Euclidean | Notes |
|--------|------|----------|-----------|-------|
| OUT 1 | SQR | /4 | Off | Straight quarter-note kick |
| OUT 2 | SQR | /8 | 4-of-8 | Snare on beats 2 and 4 area |
| OUT 3 | SQR | x2 | Off | Steady 16th-note hi-hat |
| OUT 4 | SQR | /8 | 3-of-8, Rotation 2 | Rotating percussion accent |

**Try:** Add Probability 70% to OUT 4. The underlying 3-of-8 pattern holds its shape but the groove evolves on every loop without manual changes.

---

### Patch 2: Gates and Modulation Combined

Mixing gate outputs for rhythm with CV outputs for modulation — all from the same master clock, all locked to the same tempo.

```
┌──────────────────────────────────────────┐
│         Pamela's PRO Workout             │
│                                          │
│  OUT 1 ○──[G]──────────────────────────▶ Envelope trigger
│  OUT 3 ○──[C]──────────────────────────▶ VCF cutoff CV in
│  OUT 5 ○──[C]──────────────────────────▶ VCO FM or PWM in
└──────────────────────────────────────────┘
```

| Output | Wave | Division | Notes |
|--------|------|----------|-------|
| OUT 1 | SQR | /4 | Gate fires once per beat |
| OUT 3 | SIN | /1 | One full filter sweep per bar |
| OUT 5 | TRI | x4 | Fast triangle — 16th-note LFO rate |

**Note:** OUT 3 and OUT 5 are CV outputs (continuous 0–5V oscillation), not gates. Patch them into CV inputs on oscillators and filters. If they are accidentally patched into trigger inputs, the results will be unpredictable.

---

### Patch 3: Euclidean Pattern with FLEX Swing

A direct comparison between a swung Euclidean output and a straight reference pulse. The contrast is the lesson.

```
┌──────────────────────────────────────────┐
│         Pamela's PRO Workout             │
│                                          │
│  OUT 1 ○──[G]──────────────────────────▶ Drum trigger (swung)
│  OUT 2 ○──[G]──────────────────────────▶ Drum trigger (straight reference)
└──────────────────────────────────────────┘
```

| Output | Wave | Division | Euclidean | FLEX | Notes |
|--------|------|----------|-----------|------|-------|
| OUT 1 | SQR | /8 | 5-of-8 | SWING 60% | Swung Euclidean groove |
| OUT 2 | SQR | /4 | Off | None | Straight quarter-note reference |

OUT 2 provides a metronomic quarter-note pulse. OUT 1 provides a 5-of-8 Euclidean pattern whose 8th-note subdivisions are swung at 60%. The combination sounds like a drummer who knows exactly where the beat is but is deliberately pushing and pulling against it. Once that relationship is audible, adjust the SWING percentage and listen to how the groove character shifts.

---

## Common Mistakes

**Editing the wrong output.** After navigating away from an output to check something, it is easy to continue editing the new output without noticing the switch. The display always shows which output is active. Check it before turning the knob.

**Wrong PPQN with external clock.** A mismatch between Pamela's PPQN setting and the clock source's actual PPQN causes the displayed BPM to read incorrectly and patterns to run at the wrong tempo relative to external gear. When in doubt, use 24.

**No Run signal with external clock.** Without a Run signal, Pamela's infers clock state from whether pulses are arriving. It can misread stops and starts, causing patterns to phase at downbeats. Always use the RUN input when syncing externally.

**Confusing division and multiplication direction.** x4 means four times faster — 16th notes at a quarter-note BPM. /4 means four times slower — one cycle every four beats. When a pattern sounds wrong, this is the first thing to check.

**Patching a CV output into a trigger input.** An output set to SIN or TRI produces a continuously oscillating voltage. Patched into a trigger input expecting a discrete gate, the behavior is unpredictable. If a gate is needed, use SQR or PULSE.

**Not saving to a bank.** The current state persists across power cycles, but a bank snapshot is the safety net. Save before exploring new territory. Factory Reset clears everything — banks are the recovery path.

---

## Pairs Well With

**Envelope generators** — Pamela's gate outputs are the natural trigger source for any envelope module in the system. Multiple outputs can drive multiple envelopes simultaneously at different rhythmic densities.

**Drum and percussion modules** — Most drum modules expose individual trigger inputs per voice. Pamela's can drive a full percussion setup from a single module.

**Sequencers** — Patch a Pamela's output into a sequencer's clock input to advance steps, and a slower output into the reset input to control phrase length externally.

**VCOs** — Slow CV outputs from Pamela's serve as tempo-locked LFOs for pitch modulation, PWM, and FM. Fast outputs approach audio rate for lo-fi timbral effects.

**VCFs** — A sine or triangle at /1 or /2 produces a one- or two-bar filter sweep that is locked to the track tempo. Automated movement without a dedicated LFO module.

**Mixing and utility modules** — Pamela's 0–5V outputs can be scaled and offset downstream to reach any target CV range required by other modules in the system.

---

## Advanced Learning Path

**Euclidean rhythm theory** — Understand why even distribution of hits across steps produces musical patterns. The same mathematics appears in West African drumming, Cuban son clave, and the foundational grooves of electronic music. Knowing the theory helps with intentional pattern design rather than trial and error.

**FLEX micro-timing by ear** — Start with SWING and compare a swung output to its straight version side by side. Then try HUMAN on a gate output and listen for the looseness over several bars. These differences are subtle but accumulate into feel.

**Cross operations** — Once individual output configuration is comfortable, begin with AND and OR logic between two gate outputs. These two operations open a significant space of rhythmic possibility before any of the other 15 operations need to be explored.

**Bank management for performance** — Build 8–10 complete rhythmic configurations and save each to a numbered bank. Practice loading between them while the clock runs. This is a viable live performance workflow.

**CV modulation of Euclidean parameters** — Assign an external CV to the Hits parameter of a Euclidean output. As the CV changes, the pattern density changes in real time. A single slow LFO can evolve a rhythm from sparse to dense over bars or entire sections.

**AXON expander** — If an AXON-1 or AXON-2 is added to the system, four additional CV inputs become available. This significantly expands simultaneous modulation routing and is worth revisiting once base operation is natural.

---

*Guide reflects Pamela's PRO Workout firmware 130, March 2026. Features may vary on earlier firmware versions.*
