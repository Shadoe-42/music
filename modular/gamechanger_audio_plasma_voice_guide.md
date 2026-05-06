---
title: "Gamechanger Audio Plasma Voice"
manufacturer: "Gamechanger Audio"
primary_role: EVENT_VOICE
secondary_roles: [SOURCE]
historical_context: true
form_factor: eurorack
functions: [plasma-oscillator, sound-engine, digital-bank, cv-processor, filter, drive, midi]
behavior_tags: [triggered, loopable, oscillator-capable, preset-based, cv-controlled, midi-capable, hybrid, high-voltage]
use_cases:
  - "Percussive and tonal sound design using 49 factory preset plasma sounds across 7 banks"
  - "Melodic sequencing with 1V/octave pitch tracking across the xenon tube's usable range"
  - "Continuous drone and texture work using OSCILLATE or LOOP trigger modes"
  - "Live performance with CLUTCH buffering parameter changes until the moment of release"
  - "Accent and dynamics control using ACCENT modes with separate trigger and accent inputs"
hp: 16
depth: 35mm
memory: none
transport: midi
screen: false
hybrid: true
cv: full
---

![Gamechanger Audio Plasma Voice front panel](../images/gamechanger_audio/plasma_voice/front_panel.jpg)

## Historical Context

Sound has always come from the movement of air. Instruments move air with membranes, strings, reeds, or lips. Loudspeakers move air with cones driven by electromagnets. For most of the history of sound reproduction, the cone was treated as an immovable constraint: the transducer converts electrical signal to mechanical motion, mechanical motion moves air. The chain was non-negotiable.

Electrical arc discharge offers a different path. When a high-voltage spark jumps between two electrodes, it heats the surrounding air rapidly enough to produce a pressure wave without any mechanical intermediate. The air itself is the moving element, and the arc that drives it has no mass, no resonance, no cone breakup, and no distortion from physical deformation. In principle, it is a more direct conversion from electricity to sound than anything involving a moving part.

William Duddell understood this in 1899. Working with carbon arc street lamps in London, he noticed that the electrical discharge that sustained the lamp's light could be made to oscillate at audio frequencies by connecting a capacitor and inductor in parallel with the arc. The result was an audible tone. Duddell built on this to create what he called the "singing arc," an instrument he could play by connecting a keyboard to switch between different tuned LC circuits, each producing a different pitch from the same electrical discharge. It was among the first demonstrations that electricity alone, without strings, membranes, or air columns, could produce musical tones.

Nikola Tesla extended the high-voltage arc into experimental territory throughout the 1890s and early 1900s. His high-frequency resonance experiments produced luminous discharges and audible harmonic series as byproducts of resonant coil systems. Tesla was not building musical instruments, but his work established the physical basis for sustained high-frequency discharge at levels and frequencies relevant to audio.

The plasma speaker arrived in the mid-twentieth century as a practical application of this lineage. The Ionovac, developed in the early 1950s by Alan Hill and later commercialized by DuKane, used a high-voltage plasma flame sustained in a tube of ionized gas as a massless tweeter. Because the plasma flame has no mass, it can follow electrical signals at frequencies far above the range of any cone tweeter. The Ionovac produced exceptional high-frequency reproduction precisely because the transducing element was not a physical object. It was a maintained discharge in a controlled environment.

Gamechanger Audio, founded in Riga, Latvia, approached plasma discharge from the synthesizer side rather than the loudspeaker side. Their 2018 Plasma Pedal guitar effects unit applied high-voltage xenon tube discharge to signal processing: an input signal drives a high-voltage converter, the converted current drives a xenon tube, and an electromagnetic rectifier circuit reads the resulting discharge as audio. The plasma tube is both the processing element and the sound source simultaneously. The Plasma Voice brings this architecture into Eurorack, adds a digital sound engine driving the plasma system, and organizes the result into 49 preset sounds across 7 banks with comprehensive CV, attenuverter, and MIDI integration.

Gamechanger Audio is based in Riga and has produced a small, distinctive catalog of instruments that take physical phenomena not normally used in musical instruments and turn them into studio and performance tools. The Plasma Voice carries the company's characteristic approach: an unusual physical sound source, carefully engineered for musical utility.

## Quick Start

1. Patch a gate or trigger signal into the TRIGGER input. On receiving a gate, the module sounds using whatever BANK and SOUND are currently selected. Set BANK 4 and SOUND 1 for a basic kick-like plasma percussion sound.
2. Set the TIME slider to center. This is the nominal envelope time for the selected sound. Move the slider upward to stretch the envelope longer; move it downward to compress it shorter.
3. Patch a 1V/octave pitch source into the V/OCT input (or use the MULTICV input set to 1V/oct in settings). The PITCH slider at center is the reference pitch; move it upward or downward to offset the pitch up or down by up to an octave.
4. Use the HARM slider to adjust harmonic content within the selected sound. FLUX adds controlled artifact and chaos character. FILTER adjusts cutoff. DRIVE on the right side adds soft saturation to the output.
5. Press and hold ALT, then use the encoder to access octave selection (top encoder row) and master CV attenuation (bottom encoder row).
6. To hold parameters for a beat before switching: hold the CLUTCH button, make any control adjustments, then release CLUTCH to apply all changes simultaneously.

## Key Specifications

| Specification | Value |
|---|---|
| Width | 16 HP |
| Depth | 35 mm |
| +12V Current | 220 mA |
| -12V Current | 35 mA |
| +5V Current | 0 mA |
| Sound Banks | 7 (1BASS, 2LEAD, 3PLUCK, 4DRUM, 5METAL, 6STATIC, 7SPARK) |
| Sounds per Bank | 7 |
| Total Preset Sounds | 49 |
| Sliders | 6 (TIME, MOD, HARM, FLUX, FILTER, PITCH) |
| CV Inputs | 6 (one per slider) plus MULTICV, TRIGGER, ACCENT, V/OCT |
| Trigger Modes | 5 |
| Accent Modes | 7 |
| Output Level | ±8V maximum |
| Xenon Tube Rated Life | ~10,000 hours |
| Price | $499 |

**Power note:** At 220 mA on the +12V rail, the Plasma Voice draws more current than any other module documented in this guide series. The high-voltage conversion circuit that drives the xenon tube accounts for this draw. Plan rack power accordingly. Many standard 6U Eurorack cases supply 1A or less on the +12V rail; a fully populated rack with this module installed should be audited for total current before power is applied. Exceeding the rail limit causes instability in all modules on the affected rail, not just the overloaded one.

**Safety note:** The module contains high-voltage internal circuitry. Operate indoors only. Never expose to moisture or rain. Do not open the module.

## The Physical Layer

The Plasma Voice is a hybrid instrument: a physical xenon gas tube driven by a digital control engine. Understanding both layers matters because the xenon tube is not a passive element that responds transparently to the digital signal. It has its own physical character that the digital engine exploits and works with.

Xenon is an inert noble gas that ionizes readily under high voltage. When sufficient voltage is applied across the electrodes, the gas ionizes and a discharge arc forms. That discharge superheats a column of gas in microseconds, creating a pressure wave. The electromagnetic rectifier circuit surrounding the tube reads the changes in discharge intensity as an electrical signal, which becomes the audio output. There is no cone, no membrane, no moving part between the discharge and the output signal.

The xenon tube's physical behavior shapes the sound of every preset in the bank. The discharge has characteristic transient intensity, a decay curve governed by the tube's ionization and de-ionization time, and a tendency toward certain harmonic relationships based on the geometry of the discharge and the tube dimensions. The digital engine does not synthesize sound independently and route it through the tube for coloration. The digital engine controls the high-voltage driver that sustains the discharge, and the discharge itself is the sound source.

The tube is rated for approximately 10,000 hours of use. At eight hours of use per day, this is roughly three and a half years of daily use before the tube approaches end of life. Tube replacement should be treated as a maintenance item in the same category as replacing a lamp in a projector.

## Sound Navigation: BANKs and SOUNDs

The 49 sounds are organized into 7 BANKs of 7 SOUNDs each. The banks are not arbitrary groupings; each represents a different sonic character of the plasma discharge as shaped by the digital engine.

**BANK 1 (1BASS):** Low-frequency plasma sounds with extended bass character. Useful for sub-bass reinforcement and kick-adjacent texture.

**BANK 2 (2LEAD):** Tonal, pitched plasma sounds with lead instrument character. These track pitch input most predictably and work well for melodic sequences.

**BANK 3 (3PLUCK):** Fast-attack, decaying plasma sounds with plucked transient character. The TIME slider has pronounced effect on sustain length in this bank.

**BANK 4 (4DRUM):** Percussive sounds with drum-adjacent character. SOUND 1 is a kick-like fundamental; other sounds in the bank cover snare and tom-adjacent textures. This bank benefits most from ACCENT mode use for velocity-like dynamics.

**BANK 5 (5METAL):** Metallic, inharmonic plasma textures. The harmonic structure of xenon discharge in this bank produces the natural beating and roughness of struck metal. HARM and FLUX have strong character-shaping effect here.

**BANK 6 (6STATIC):** Noise and static textures. The discharge runs in a less controlled regime in these sounds, producing broadband energy with varying spectral tilt. FILTER is particularly useful here.

**BANK 7 (7SPARK):** Chaotic, artifact-rich plasma sounds. These are the least pitched and most event-like in the set, treating each trigger as a discrete electrical event with unpredictable high-frequency content.

**Navigation:** The encoder has two modes accessed by pushing the encoder button. Top mode selects BANK (1-7) by turning; the seven top LEDs indicate the current bank. Bottom mode selects SOUND (1-7) by turning; the seven bottom LEDs indicate the current sound. A second push switches back to the other row. Holding ALT while using the top encoder row selects the pitch octave. Holding ALT while using the bottom encoder row adjusts master CV attenuation for all CV inputs simultaneously.

## The Six Sliders and Their CV Inputs

Each of the six sliders controls a different dimension of the plasma sound, and each has a dedicated CV input jack with a corresponding attenuverter knob.

The CV inputs accept bipolar signals (±5V from center). The attenuverter knobs scale the CV contribution. At center, the attenuverter contributes zero CV influence regardless of what is patched; the slider position alone determines the parameter value. Turning the attenuverter clockwise from center opens up positive CV tracking: the parameter follows the CV signal in the positive direction. Turning counterclockwise from center opens up inverted CV tracking: the CV signal modulates the parameter in the opposite direction from what the CV source is doing.

**TIME** controls the envelope time stretch for the current sound. Center position is the nominal designed duration for the selected sound. Moving the slider above center stretches the envelope longer; moving below center compresses it shorter. This does not simply fade the sound earlier; it adjusts the shape of the amplitude and timbral envelope that the digital engine applies to the plasma driver. A sound designed as a tight percussive event at center can become a sustained texture when TIME is moved high, or a click-like artifact when moved low.

**MOD** controls a pitch modulation effect similar in character to vibrato depth. It affects the degree to which a pitch-mod-type modulation is applied within the sound. At minimum, the sound plays at the base pitch without modulation; as MOD increases, the modulation deepens. The specific character of the modulation varies by BANK and SOUND.

**HARM** controls the harmonic content depth of the selected sound. The plasma discharge has a natural harmonic series; HARM adjusts how prominently the upper harmonics are expressed in the output. Higher HARM values add brightness and complexity; lower values reduce the harmonic density toward a more fundamental-focused sound.

**FLUX** introduces controlled chaos and artifact character into the discharge. The plasma tube naturally has a tendency toward chaotic variation at certain drive levels; FLUX deliberately takes the discharge into or near this regime. At low FLUX values the sound is well-controlled; at higher values, the discharge introduces pitch instability, dropout artifacts, and irregular distortion that varies from trigger to trigger. FLUX is not random in the algorithmic sense; it is physical variability from the discharge itself, which means it sounds different from purely software-generated noise or randomization.

**FILTER** controls a post-discharge filter applied to the output signal. At center position, the filter is fully open and passes the full spectrum of the plasma output. Moving the slider in either direction from center closes the filter: one direction toward low-pass, the other direction toward high-pass. The filter has a dedicated tilt-EQ companion in the DRIVE section (BASS and TREB knobs) and four operational modes accessible in settings: LP only, HP only, LP/HP (DJ-style with center fully open), and per-SOUND default (each BANK/SOUND combination determines which filter mode is active). The CV input for FILTER allows real-time cutoff modulation.

**PITCH** controls the base pitch of the plasma sound within a ±1 octave range from center. This is a coarse pitch offset, not a 1V/octave tracking input. For 1V/octave melodic control, use the V/OCT input or assign MULTICV to 1V/oct (Settings 3:1). The PITCH slider sets where in the xenon tube's usable pitch range the sound begins; the PITCH CV input and attenuverter allow pitch modulation without changing the PITCH slider's base position.

## Trigger Modes

The trigger mode determines how the Plasma Voice responds to the TRIGGER input. Five modes are available, accessed in settings (Settings 1:1 through 1:5).

**TRIGGER (1:1):** The module sounds on each rising edge of the TRIGGER input. The envelope plays from start to finish regardless of gate length. A second trigger during a sound's decay restarts the envelope from the beginning. This is the default percussive behavior.

**GATE (1:2):** The module sounds and sustains for the duration of the gate signal. Envelope character is shaped by gate length as well as by the TIME slider. The sound holds while the gate is high and releases when the gate falls. This allows legato-style playing where longer gates produce longer, different-shaped sounds.

**LOOP (1:3):** The module triggers continuously at an internally defined rate without requiring an external trigger signal. The TIME slider adjusts the loop rate. This mode turns the Plasma Voice into a self-cycling sound source. The TRIGGER input in LOOP mode can reset or sync the loop to an external clock; the exact interaction depends on the relative timing.

**OSCILLATE (1:4):** The plasma discharge runs continuously as a free oscillator without requiring a trigger. The TRIGGER input gates the output rather than initiating discrete events. This is the mode most similar to a conventional oscillator: the plasma tube is always running, and the TRIGGER input controls whether the output passes. PITCH, V/OCT, and MULTICV (assigned to 1V/oct) control pitch in this mode. This is the secondary SOURCE role of the module: a continuously running plasma oscillator that plays melodic lines.

**ON/OFF (1:5):** A single trigger alternates the module between active and inactive states. One trigger turns the sound on and it sustains indefinitely; the next trigger turns it off. This creates a toggle behavior suitable for performance contexts where the sound should run until it is explicitly stopped.

## Accent Modes

Accent modes change the fundamental behavior of both the TRIGGER input and the ACCENT input, and in most cases reassign some of the ALT+slider functions. Seven modes are available in Settings 2:1 through 2:7.

**ACCENT (2:1):** The TRIGGER input fires the sound at normal level. The ACCENT input fires the sound at an accented level, with increased amplitude and potentially brighter timbre. This is a direct velocity-layer implementation: routes with gates can send to either input for two distinct dynamic levels. Drum sequencers that provide separate accent outputs integrate naturally here.

**DUCK (2:2):** When a signal arrives at the ACCENT input, the Plasma Voice output level is reduced. This is a sidechain ducking mode: the ACCENT input controls attenuation rather than accent. Route a kick output to ACCENT and the Plasma Voice will duck under every kick, creating the sidechain compression effect through direct level control rather than a dynamics processor.

**STARVE (2:3):** The ACCENT input reduces the high-voltage supply to the plasma tube, starving the discharge. This produces voltage-starvation artifacts: sputtering, pitch drop, and partial discharge failure. The effect is similar to running a battery-powered analog circuit near the end of battery life. At moderate STARVE input levels, the sound degrades in a musically useful way; at high levels, the discharge fails and the output drops out.

**CVFREEZE (2:4):** When the ACCENT input is active, all CV inputs are frozen at their last sampled values. CV modulation continues until a gate appears at ACCENT, at which point the CV state is locked. Releasing the ACCENT gate unfreezes CV tracking. This allows a performer to lock in a particular CV-modulated state during a performance moment and hold it regardless of what the CV sources are doing.

**JUMP (2:5):** On receiving a signal at the ACCENT input, the module immediately jumps to a random SOUND within the current BANK. The TRIGGER input continues to fire sounds normally, but the ACCENT input randomizes which sound from the bank is selected each time it fires. This introduces controlled variation without leaving the tonal character of the current bank.

**REVERSE (2:6):** The ACCENT input plays the current sound in reverse. Forward and reverse versions of the same preset produce different transient and spectral shapes from the same source material.

**BURST (2:7):** A single trigger at the TRIGGER input fires a rapid burst of retriggered sounds. The burst rate and count are adjustable via the ALT+slider assignments specific to BURST mode. This turns the Plasma Voice from a single-event module into a rapid-fire texture generator on demand.

## CLUTCH: The Performance Buffer

CLUTCH is a dedicated performance feature with no equivalent in most Eurorack modules. It solves a practical live performance problem: when the sound is running and the performer wants to change banks, sounds, or parameter settings, any adjustment takes effect immediately, potentially producing unwanted transitions during a performance moment.

Holding the CLUTCH button suspends all parameter updates. The plasma tube continues playing the current state. Any changes made to sliders, the encoder, or other controls while CLUTCH is held are recorded but not applied to the output. Releasing CLUTCH applies all queued changes simultaneously at the moment of release.

This is not a quantized or tempo-synced hold; it is performer-controlled. The performer holds CLUTCH through a busy moment in the music, makes the next sound or bank selection while holding, and releases at the transition point they choose. In practice, CLUTCH functions as a "prepare the next sound while the current sound plays, then commit on the downbeat" mechanism.

CLUTCH works across BANK selection, SOUND selection, and slider positions. It does not buffer CV input signals; those continue updating through the hold period and apply normally at release.

## MULTICV: The Assignable Input

The MULTICV jack is a single CV input that can be assigned to seven different internal targets. The assignment is made in Settings 3:1 through 3:7.

**1V/OCT (3:1):** Standard 1V/octave pitch tracking. This is the primary assignment for melodic use. The MULTICV attenuverter (accessed via ALT) scales the pitch CV before it reaches the oscillator, allowing non-standard V/oct relationships or compressed pitch ranges.

**TIME CV (3:2):** MULTICV controls the TIME parameter, adding a second CV source for envelope time in addition to the TIME slider's own CV input.

**MOD CV (3:3):** MULTICV controls the MOD depth parameter.

**HARM CV (3:4):** MULTICV controls the harmonic content depth.

**FLUX CV (3:5):** MULTICV controls the chaos/artifact depth.

**FILTER CV (3:6):** MULTICV controls the filter cutoff.

**BANK and SOUND (3:7):** MULTICV selects BANK and SOUND based on input voltage. The selection is quantized to a major scale relationship: each volt selects a different bank, and subdivision within the volt selects the sound within that bank. This allows a sequencer or keyboard to step through preset sounds in a musically predictable pattern. The scale quantization means adjacent steps on a keyboard select adjacent sounds in a way that follows the major scale interval pattern rather than linear voltage division.

## Drive and EQ

The right side of the Plasma Voice provides post-discharge signal shaping that is independent of the plasma engine itself.

**DRIVE** applies soft-clipping saturation to the output signal. This is not digital clipping or digital distortion; it is an analog soft-clipping circuit that introduces warm saturation as the drive level increases. At low settings, DRIVE is transparent. As the level increases, the output begins to saturate at peaks, adding harmonic density and perceived loudness. Heavy DRIVE settings compress the dynamic range and produce a pushed, dense texture. DRIVE comes after the plasma output stage and before the BASS/TREB controls.

**BASS** is a low-frequency tilt control. Turning it clockwise boosts bass; counterclockwise reduces bass. This is a shelving-style EQ rather than a peaking band.

**TREB** is a high-frequency tilt control with the same behavior in the opposite frequency range. BASS and TREB together form a simple tilt EQ that adjusts the spectral balance of the plasma output without affecting the plasma drive behavior.

**FILTER modes:** The FILTER slider operates in one of four modes depending on the setting in the filter mode settings page. LP mode applies a low-pass filter as the slider moves from center. HP mode applies a high-pass filter. LP/HP mode applies low-pass on one side of center and high-pass on the other, with center position being fully open (the "DJ filter" behavior). Per-SOUND mode uses whichever filter behavior is baked into the current SOUND's preset definition. Switching filter modes changes the character of what the FILTER slider does without affecting any other parameters.

## MIDI

The Plasma Voice accepts MIDI over a standard 3.5mm TRS jack (adapter required for 5-pin DIN). MIDI implementation covers notes, velocity, continuous controllers, program change, and SysEx for deeper parameter access.

Notes received on any MIDI channel trigger the module and control pitch. Channel 10 uses the General MIDI percussion key map: each MIDI note on channel 10 triggers a different sound from the Plasma Voice's bank as mapped to the GM percussion standard. A drum machine or DAW sending to channel 10 with standard kick/snare/hi-hat notes fires corresponding Plasma Voice sounds without additional mapping setup.

Velocity received via MIDI controls accent level, equivalent to the ACCENT input level in the active accent mode. MIDI continuous controllers map to the six slider parameters. Program change steps through SOUND selections. The full CC and SysEx map is in the Gamechanger Audio Plasma Voice manual.

## Why the Plasma Voice Excels

The Plasma Voice is the only Eurorack module in this guide series where the sound source is a physical discharge phenomenon that the player can hear and, in some cases, see. This is not a metaphor for the synthesis behavior; the xenon tube is producing light and pressure waves simultaneously from the same discharge. The acoustic character of that discharge is fundamentally unlike anything a digital oscillator, analog VCO, or sampled waveform produces, because it does not involve a waveform in the conventional sense. The discharge is a chaotic high-energy event that the digital engine shapes but does not fully domesticate. FLUX at higher settings makes this explicit: the variation from trigger to trigger is physical, not algorithmic. No two plasma events are exactly alike.

This has a specific practical value. In dense mix contexts, sounds that have some internal physical variability sit differently from sounds that are perfectly reproducible. The slight timbral variation from event to event creates a perceptual texture that many producers associate with live acoustic sources. The Plasma Voice provides this without sampling, without randomization algorithms, and without the playback-quality limitations of sample-based modules.

The CLUTCH button addresses a real problem in modular live performance. Most Eurorack modules have no mechanism for queuing changes; what you touch happens immediately. CLUTCH provides a way to work ahead of the music: prepare the next state while the current state plays, commit at a chosen moment. This is a workflow affordance borrowed from DJ performance culture, where cueing the next track before the audience hears it is standard practice. Applied to synthesis, it changes the cognitive relationship between the performer and the instrument during a live set.

The ACCENT mode system provides a depth of expressivity that goes beyond simple velocity control. DUCK, STARVE, and BURST are not variations on accent; they are fundamentally different relationships between two trigger inputs and the module's output. A system built around these modes -- routing different rhythmic sources to TRIGGER and ACCENT -- can produce behaviors that no parameter adjustment of a single-trigger module could replicate.

## Patch Examples

### Patch 1: Plasma Percussion with Clock and Accent

**What this demonstrates:** Basic triggered sound using the drum bank, with accent for velocity-like dynamics.

Set BANK 4 (4DRUM), SOUND 1. Set Accent mode to ACCENT (Settings 2:1). Set FILTER mode to LP/HP (fully open at center).

```
Clock or gate source → TRIGGER [G]
Accent gate (fires on beat 1 and 3) → ACCENT [G]
TRIGGER output → VCA or direct to mixer [A]
```

TIME slider at center. HARM at 9 o'clock. FLUX at minimum. DRIVE at 9 o'clock.

The clock triggers the sound on every beat. The accent gate arriving at ACCENT on beats 1 and 3 fires the same sound at higher amplitude and slightly brighter timbre. This creates a two-layer dynamics structure from a single module without a VCA dedicated to velocity.

Vary SOUND selection within BANK 4 while the pattern runs. Use CLUTCH to prepare the SOUND change while the clock continues, then release CLUTCH at the start of the next measure.

### Patch 2: Pitched Plasma Melody in OSCILLATE Mode

**What this demonstrates:** Using the Plasma Voice as a free-running melodic oscillator with sequenced pitch.

Set Trigger mode to OSCILLATE (Settings 1:4). Set MULTICV to 1V/OCT (Settings 3:1). Set BANK 2 (2LEAD), SOUND 3.

```
Sequencer 1V/oct output → MULTICV [C]
Sequencer gate output → TRIGGER [G] (gates output in OSCILLATE mode)
Plasma Voice output → Filter module input [A]
```

PITCH slider at center. TIME slider has no effect in OSCILLATE mode (the discharge runs continuously). MOD slider at 8 o'clock for a small amount of pitch modulation. HARM at 10 o'clock. DRIVE at 9 o'clock.

The plasma tube runs continuously. The TRIGGER gates the output: when the gate is high, the sound is audible; when the gate is low, it is not. The pitch follows the sequencer via MULTICV. Because the discharge is continuous, the attack is determined by the gate transition rather than by a triggered envelope, producing a different envelope character than TRIGGER mode.

Patching the plasma output through an external filter after the module's own filter adds independent timbral control. The Plasma Voice's FILTER slider then acts as a pre-filter to the external module, giving two filter stages in series.

### Patch 3: CLUTCH-Based Sound Switching in a Live Set

**What this demonstrates:** Using CLUTCH to queue sound changes without audible glitching during a continuous performance.

Set BANK 4 (4DRUM), SOUND 1. Set Trigger mode to LOOP (Settings 1:3). TIME slider controls loop rate.

```
Plasma Voice output → Mixer channel [A]
```

No external trigger required in LOOP mode. The module fires continuously at the loop rate set by TIME.

With the sound looping: hold the CLUTCH button. While holding, turn the encoder to select BANK 7 (7SPARK), SOUND 4. Adjust HARM and FLUX sliders to new positions. Release CLUTCH on the downbeat of the next four-bar phrase.

All queued changes apply simultaneously at the moment of release. The transition is committed at the performer's chosen moment rather than when the knobs were moved. Repeat this workflow throughout the performance to move between sounds without the intermediate states being audible.

Vary the TIME slider (not buffered by CLUTCH in all configurations; test before the performance) to adjust the loop rate between holds.

### Patch 4: STARVE Mode Voltage Degradation

**What this demonstrates:** Using STARVE accent mode to produce physical discharge degradation as a musical effect.

Set BANK 5 (5METAL), SOUND 2. Set Accent mode to STARVE (Settings 2:3). Set FILTER to LP mode.

```
Gate source (regular rhythm) → TRIGGER [G]
Slow rising ramp or envelope (4-8 second rise) → ACCENT [C]
LFO (slow, triangle) → FILTER CV input [C]
Plasma Voice output → Mixer [A]
```

FLUX at minimum initially. HARM at 12 o'clock. DRIVE at 10 o'clock.

The gate triggers the plasma sound normally at first. As the slow ramp arriving at ACCENT rises over 4-8 seconds, the high-voltage supply is progressively starved. The sound begins to degrade: pitch drops slightly, the discharge becomes inconsistent, and the characteristic crackle and sputter of a voltage-starved discharge appears. The LFO on the FILTER CV adds filter motion during this degradation.

As the ramp reaches maximum, the discharge may fail partially, producing clicks and dropouts alongside the intended metal texture. This is not a malfunction; it is the physical behavior of a xenon tube discharge under reduced drive voltage used deliberately as a timbral evolution tool.

Reset the ramp and the sound returns to its normal character on the next cycle.

## Common Mistakes

**"Nothing happens when I patch the gate."** Check that the power draw has not pushed the rack's +12V rail into overload. At 220 mA, this module draws heavily. A rail at or near its limit produces intermittent operation in all modules on that rail. Verify with a power audit before diagnosing the Plasma Voice itself. If power is adequate, confirm the gate signal is reaching the module by checking the trigger LED if present, or by substituting a manual button or keyboard gate.

**"The pitch is wrong when I use 1V/oct."** The primary pitch CV input labeled V/OCT is for 1V/octave tracking. The MULTICV input requires assignment to 1V/OCT (Settings 3:1) before it tracks pitch. If both are patched, they add together. Using only one or the other is the standard workflow; combining them requires careful planning to avoid doubled pitch offsets.

**"The sound is changing while I adjust knobs in a live set."** This is expected behavior. CLUTCH exists precisely to prevent this. Hold CLUTCH before making any changes during a live performance, adjust while holding, and release at the chosen moment. Building CLUTCH into the performance workflow from the beginning is preferable to retrofitting it as a workaround.

**"The FILTER sounds different from what I expect."** The FILTER slider behavior depends on the active filter mode. In LP/HP mode, center is fully open and movement in either direction closes the filter. In LP or HP mode, the slider sweeps in one direction only. In per-SOUND mode, the behavior is determined by the preset. Verify which filter mode is active in settings before assuming the slider or CV input is not working.

**"The FLUX sounds like a malfunction."** At higher FLUX settings, the plasma discharge intentionally enters a less controlled regime. Pitch instability, irregular amplitude variation, and discharge artifacts are the designed output of high FLUX values, not symptoms of a damaged tube or faulty module. If the behavior is unwanted, reduce FLUX to minimum, which returns the discharge to its most controlled state. Reserve high FLUX for sounds and contexts where physical unpredictability is the goal.

**"The xenon tube dimmed or stopped glowing."** Tube life is rated at approximately 10,000 hours. If the tube is near end of life, discharge intensity drops and the sound changes character. This is a consumable component, not a warranty-covered defect. Contact Gamechanger Audio for tube replacement options. Do not attempt to source a replacement tube without verifying the exact voltage and geometry specifications with the manufacturer.
