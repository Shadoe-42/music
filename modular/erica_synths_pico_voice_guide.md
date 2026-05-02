---
title: Erica Synths Pico Voice
manufacturer: Erica Synths
primary_role: SOURCE
secondary_roles: [SHAPER, AMPLIFIER]
form_factor: eurorack
functions: [oscillator, filter, envelope-generator, wavetable, karplus-strong]
behavior_tags: [warm, stable, gated, performative]
use_cases: [complete voice in small system, lead voice, bass voice, melodic sequencing]
hp: 3
memory: basic
historical_context: true
---

# Erica Synths Pico Voice
**8-Algorithm Synthesis Voice | 3HP**

![Erica Synths Pico Voice](https://github.com/Shadoe-42/music/raw/main/modular/images/erica_synths/pico_voice/front_panel.jpg)

## Historical Context

Erica Synths, founded in Riga, Latvia, built a reputation within Eurorack for engineering discipline: affordable modules that do specific things well without unnecessary complexity. The Pico series extended that philosophy to an extreme constraint, fitting complete synthesis functionality into 3HP per module. Designing at that width means every component earns its place; there is no room for redundancy or unused surface area.

The Pico Voice's eight synthesis algorithms span several decades of electronic instrument development. Karplus-Strong physical modeling was formalized by Kevin Karplus and Alex Strong in 1983 and became one of the first computationally practical methods for synthesizing plucked-string timbres without recording them. The TB-303 Bassline algorithm references the Roland TB-303 of 1981, a sequencer-synth that became the foundational instrument of acid house after musicians discovered its resonant filter could produce sounds Roland never anticipated. Wavetable synthesis, associated with Wolfgang Palm's PPG Wave instruments of the late 1970s and early 1980s, introduced the idea of storing complex waveforms in memory and morphing between them, producing timbral movement that static oscillators could not achieve.

Collecting these approaches in a single 3HP module is not a gimmick. Each algorithm produces a genuinely distinct timbral family, and having them accessible via a single button press means a small system can cover territory that would otherwise require multiple dedicated voice modules.

---

## Quick Start

```
[Sequencer] 1V/Oct Out ──▶ [Pico Voice] 1V/Oct In
[Sequencer] Gate Out   ──▶ [Pico Voice] Trig In
                           [Pico Voice] Out ──▶ [Mixer]
```

1. Patch a sequencer's 1V/oct output to the 1V/Oct input and its gate output to the Trig input
2. Route the audio output to a mixer
3. Set Tune to noon
4. Press the button until the LED shows yellow (Chords algorithm)
5. Turn PAR1 to select a chord type and PAR2 to set release time
6. Start your sequencer and listen

---

## Key Specs

| Parameter | Value |
|-----------|-------|
| Width | 3HP |
| Depth | 35mm |
| Power | 30mA +12V / 20mA -12V / 0mA 5V |
| Algorithms | 8 |
| Memory | Per-algorithm settings retained |
| **Role** | **SOURCE (SHAPER, AMPLIFIER)** |

---

## Essential Parameters

The button cycles through eight synthesis algorithms, each indicated by a distinct LED color. Short presses advance through the sequence; a one-second hold enters configuration mode, where the LED blinks. The module retains PAR1, PAR2, and configuration settings for each algorithm independently, so switching from Bassline to Wavetable and back returns to the Bassline settings as last set.

The Tune knob sets the base pitch. The module tracks 1V/octave over the C1 to C8 range (1V to 8V). Below or above that range, tracking becomes unreliable. The external 1V/oct input adds to the Tune knob position, so setting Tune to C4 and sending a sequence centered around 0V produces output centered at C4.

PAR1 controls the primary synthesis parameter for the active algorithm. PAR2 controls a secondary parameter and in most algorithms also sets the envelope release time. Turning PAR2 fully clockwise removes the gate dependency for sustained sound: the voice outputs continuously regardless of the trigger input, which is useful for pad textures and drone patches where an external gate is not available or not wanted.

The CV input accepts bipolar voltage and modulates whichever parameter is assigned in configuration mode. Assignment is set by holding the button until the LED blinks, then pressing to cycle through three states: blinking red assigns CV to Tune, blinking green assigns CV to PAR1, blinking blue assigns CV to PAR2. Turning PAR2 in configuration mode accesses algorithm-specific settings such as waveform selection, chord voicing type, and note mode. Each algorithm has its own configuration settings stored independently.

The Trig input requires a gate or trigger signal to generate sound. Without a trigger, most algorithms produce no output regardless of other settings. The Karplus-Strong algorithm is entirely dependent on the trigger: each trigger event fires a short noise burst that the algorithm converts into a decaying resonant tone. The gate length influences sustain behavior for other algorithms when PAR2 is not at maximum.

The eight algorithms by LED color, with PAR1 and PAR2 functions:

| LED | Algorithm | PAR1 | PAR2 |
|-----|-----------|------|------|
| Red | Karplus-Strong | Distortion | Noise burst character |
| Yellow | Chords | Chord type | Release time |
| Green | Wavetable | Wave position (morph) | Release time |
| Blue | Bassline (TB-303) | Filter resonance | Release time |
| Purple | PWM | Pulse width | Release time |
| Orange | Supersaw | Detune spread | Release time |
| Cyan | Wavefold | Fold amount | Release time |
| Lime | Harmonic | Harmonic content | Release time |

---

## Why Pico Voice Excels

The 3HP width is the defining constraint and the defining achievement. A complete synthesis voice in three panel units means Pico Voice fits in any system that has three free HP, including small skiffs and performance cases where larger voice modules are not practical. The footprint does not limit the output: each of the eight algorithms is a complete synthesis approach with its own timbral character, not a simplified version of something more capable. The constraint shaped the design toward essential controls rather than toward compromise.

The algorithm range covers the primary timbral families that electronic music production draws on. The Karplus-Strong and Harmonic algorithms produce pitched resonance and additive overtone content respectively, covering the organic and tonal end of the spectrum. The Bassline and PWM algorithms cover subtractive synthesis territory familiar from analog instruments. Wavetable and Wavefold move into digital morphing and harmonic distortion territory. Chords and Supersaw provide harmonic stacking for pad and lead contexts. Moving between these with a button press allows a single module to serve as the voice core in a small system without requiring the user to repatch or swap modules.

The CV assignment system is a practical solution to the constraint of a single CV input. Rather than hardwiring CV to one parameter, configuration mode allows the assignment to change per algorithm. A patch that sends an envelope to CV can assign that envelope to resonance when Bassline is active and to wave position when Wavetable is active, with those assignments stored independently. This makes one CV input behave differently across algorithms without any patch changes, which is a meaningful capability gain in a small system where cable count is a real concern.

The PAR2 fully clockwise behavior decouples the module from gate requirements for sustained operation. This is a practical feature for situations where a trigger source is not available, a drone context is wanted, or the module is being used with a modulation source that does not produce gates. Combined with CV assignment for PAR1, a Pico Voice running in continuous mode with a slow LFO on PAR1 operates as a self-sufficient evolving texture source from a minimal patch.

---

## Patches

### Sequenced Lead Voice

Drive Pico Voice as a full melodic instrument from Hermod+, with Function Junction shaping the timbral envelope via the CV input.

```
[Hermod+] CV Out            ──▶ [Pico Voice] 1V/Oct In
[Hermod+] Gate Out          ──▶ [Pico Voice] Trig In
[Function Junction] ADSR Out ──▶ [Pico Voice] CV In
                                 [Pico Voice] Out ──▶ [MixUp] Ch1
```

**Setup:** Set the algorithm to Purple (PWM). Assign CV to PAR1 in configuration mode (blinking green). Set PAR1 to noon and PAR2 to 1 o'clock for moderate release. Program Hermod+ with a melodic sequence. Set Function Junction to ADSR mode with a short attack, moderate decay, low sustain, and medium release. Gate the Function Junction from the same Hermod+ gate output.

**Controls:** The Function Junction envelope opens PAR1 (pulse width) on each gate event, so each triggered note has a pulse width sweep from narrow to wide over the decay stage. Adjust Function Junction decay to taste: short decay produces a sharp timbral snap on each note, longer decay creates a slow sweep that outlasts the note. Advance PAR2 clockwise to extend the audio release and hear the pulse width continue to evolve after the gate closes. Swap algorithms mid-sequence using the button to compare PWM character against Bassline or Supersaw with the same patch.

**Result:** A melodic sequence where each note has its own timbral arc driven by the envelope, rather than a static tone at each pitch. The CV assignment to PAR1 makes the timbral movement tied to the gate timing rather than to a free-running LFO.

---

### Acid Bassline

Run the Bassline algorithm with CV-controlled resonance sweeps against a rhythmic Hermod+ sequence.

```
[Hermod+] CV Out   ──▶ [Pico Voice] 1V/Oct In
[Hermod+] Gate Out ──▶ [Pico Voice] Trig In
[Zadar] Ch1 Out    ──▶ [Pico Voice] CV In
                       [Pico Voice] Out ──▶ [MixUp] Ch2
```

**Setup:** Set the algorithm to Blue (Bassline). Assign CV to PAR1 in configuration mode (blinking green). Set PAR1 to 2 o'clock as the base resonance position. Set PAR2 to 10 o'clock for a short release that keeps notes separated. Program Hermod+ with a low-register bass sequence. Set Zadar channel 1 to a fast attack and medium decay envelope, triggered by the same gate source as Pico Voice.

**Controls:** Each gate event triggers both Pico Voice and a Zadar envelope that sweeps resonance upward on the attack and decays back toward the PAR1 knob position. Set PAR1 lower (9 o'clock) and Zadar envelope depth high for dramatic sweeps; set PAR1 higher (2 o'clock) and Zadar amplitude lower for a consistently filtered but still moving character. In configuration mode, toggle between saw and pulse waveform (PAR2 in config) to change the base harmonic content going into the filter.

**Result:** A rhythmic bass line with per-note resonance sweeps from the Zadar envelope. The Bassline algorithm's filter character combined with the CV-driven resonance produces the classic acid synthesis behavior: each triggered note has a distinct timbral arc tied to its gate event.

---

### Karplus-Strong Plucked Voice

Use the Karplus-Strong algorithm with Hermod+ for pitched melodic plucked string tones triggered by a rhythmic gate pattern.

```
[Hermod+] CV Out   ──▶ [Pico Voice] 1V/Oct In
[Hermod+] Gate Out ──▶ [Pico Voice] Trig In
                       [Pico Voice] Out ──▶ [MixUp] Ch3
```

**Setup:** Set the algorithm to Red (Karplus-Strong). Set PAR1 to noon (moderate distortion on the resonator). Set PAR2 to 9 o'clock for a fast decay that produces a defined pluck character. Program Hermod+ with a melodic sequence and a rhythmic gate pattern that includes rests.

**Controls:** Each gate trigger fires a noise burst that the algorithm sustains as a decaying pitched resonance at the frequency set by 1V/oct and Tune. Adjust PAR1 clockwise to add distortion to the resonator, which darkens and thickens the pluck character. Adjust PAR2 to control decay length: counterclockwise gives a very short pluck; clockwise gives a longer sustain before the resonance fades. Rests in the gate pattern are important; without silence between notes the pluck character accumulates and loses definition. Bring PAR2 fully clockwise only if a drone-like sustained resonance is wanted rather than a pluck texture.

**Result:** A sequenced melodic line of plucked-string tones with natural decay, generated from Pico Voice alone without any additional oscillator or filter modules. The algorithm handles pitch tracking, resonance, and decay within 3HP.

---

### Sustained Wavetable Pad

Run the Wavetable algorithm in gate-free sustained mode with slow envelope modulation on the wave position for a continuously evolving pad texture.

```
[Hermod+] CV Out  ──▶ [Pico Voice] 1V/Oct In
[Zadar] Ch2 Out   ──▶ [Pico Voice] CV In
                      [Pico Voice] Out ──▶ [Ghost] In
                                          [Ghost] Out ──▶ [MixUp] Ch4
```

**Setup:** Set the algorithm to Green (Wavetable). Assign CV to PAR1 in configuration mode (blinking green). Turn PAR2 fully clockwise for sustained output without gate dependency. Set PAR1 to noon as the center wave position. Program Zadar channel 2 as a slow cycling envelope at a 20 to 40 second period. Patch no gate signal to the Trig input; the module runs continuously from the 1V/oct pitch alone.

**Controls:** The Zadar envelope sweeps PAR1 slowly through the wavetable, producing gradual timbral movement over time. Adjust PAR1 manually to shift the center of the sweep. Bring PAR2 slightly counterclockwise from maximum to reintroduce gate sensitivity for slower-attack textures when a gate is eventually added. In configuration mode, toggle between 1 and 2 note operation (PAR2 in config) to add a second detuned voice layer for a thicker pad character. Ghost's FX-first routing adds reverb and light saturation downstream.

**Result:** A continuous, slowly morphing pad texture that evolves over long time periods without requiring a clock or gate source. The Wavetable algorithm's wave position modulation combined with Ghost's spatial processing produces sustained ambient material from a minimal patch.

---

## Common Mistakes

### "No sound is coming out"

Pico Voice requires a gate or trigger signal at the Trig input to produce audio. Without a trigger, most algorithms generate no output regardless of the 1V/oct pitch or PAR settings. The exception is PAR2 fully clockwise, which enables sustained output without gate dependency. If there is no gate source available, turn PAR2 fully clockwise as a temporary measure to confirm the audio path is working before troubleshooting the trigger connection. **Fix:** Patch a gate or trigger source to the Trig input, or turn PAR2 fully clockwise for gate-free sustained operation.

---

### "Pitch tracking is inconsistent in the low register"

The module's 1V/octave tracking is reliable from C1 to C8, corresponding to 1V to 8V input. Sequences or CV sources that send values below 1V place the pitch below the reliable tracking range. Many sequencers default to 0V as the lowest step, which falls outside the Pico Voice tracking window. **Fix:** Transpose the sequence up so the lowest note corresponds to at least 1V (C1), or adjust the Tune knob to shift the base pitch into the reliable range.

---

### "My CV modulation is not affecting anything"

The CV input assignment is set per algorithm in configuration mode. If no assignment has been made since the algorithm was selected, or if the assignment was made for a different algorithm, the CV input may be assigned to a parameter that has no audible effect at current settings. Each algorithm stores its own CV assignment independently, so switching algorithms resets to whatever was previously saved for that algorithm. **Fix:** Enter configuration mode (hold button one second until LED blinks), press to cycle through blinking color states (red for Tune, green for PAR1, blue for PAR2), and confirm the assignment is set to the intended target for the active algorithm.

---

### "Karplus-Strong sounds like a sustained tone rather than a pluck"

PAR2 controls the decay length of the Karplus-Strong resonance. At or near fully clockwise, the resonance sustains for a long time, producing a bowed or organ-like texture rather than a pluck. Turning PAR2 counterclockwise shortens the decay. At 9 o'clock the resonance decays quickly enough to produce a defined pluck character. **Fix:** Turn PAR2 counterclockwise to shorten the decay. For clearly defined plucks, PAR2 between 9 and 11 o'clock is the usable range.

---

## Advanced Learning Path

1. Learn one algorithm per session before working with the full set. Start with Bassline or PWM since those are the most immediately familiar to anyone with a subtractive synthesis background. Understand how PAR1 and PAR2 behave for that algorithm, then explore the configuration mode settings for waveform selection. Moving to the next algorithm after mastering one produces clearer results than sampling all eight in a single session.

2. Master configuration mode early. The CV assignment and per-algorithm parameter settings (waveform, note mode, phase lock) are not surface-level options; they define the fundamental behavior of each algorithm. PAR1 on the Supersaw algorithm is detune spread, but whether phase lock is on or off determines whether the detuned voices are stable or drift independently. These settings should be explored deliberately for each algorithm.

3. Learn the PAR2 fully clockwise behavior before building gate-dependent patches. The distinction between gated and sustained operation changes how the module fits into a patch. Sustained mode allows Pico Voice to function as a drone or pad source without gate infrastructure; gated mode ties the voice to the rhythmic structure of whatever gate source is used. Knowing which mode is active prevents confusion when a patch produces continuous output when silence was expected, or silence when continuous output was expected.

4. Experiment with CV assignment to Tune for vibrato and pitch modulation before assigning to PAR1 or PAR2. Assigning a slow LFO to Tune produces pitch variation on whatever algorithm is active, which demonstrates how the 1V/oct input and Tune knob interact with the CV input. Once that relationship is clear, the behavior of PAR1 and PAR2 CV assignments is easier to predict.

5. Use algorithm switching mid-sequence as a performance technique. Pressing the button while a sequence plays changes the synthesis approach without interrupting the pitch or gate signals. The transition between Wavetable and Wavefold, or between Chords and Supersaw, produces an immediate timbral shift that works as a compositional event. The per-algorithm memory means switching back returns to the previous settings.

6. Use Pico Voice as the synthesis core in patches where all other modules handle modulation, timing, and effects. The module handles pitch tracking, voice generation, and internal envelope in 3HP; adding Function Junction for envelope-to-CV modulation, Hermod+ for sequencing and gate generation, and Ghost for output processing produces a complete performance voice with clear functional separation between components.

---

## Pairs Well With

**Squarp Hermod+** is the most complete sequencing partner for Pico Voice. Hermod+ sends simultaneous CV and gate outputs from the same sequence, satisfying both the 1V/oct and Trig inputs from a single programming source. Additional CV outputs from Hermod+ can be routed to the Pico Voice CV input for parameter automation that stays synchronized to the sequence tempo without requiring a separate modulation source.

**Cre8audio Function Junction** provides envelope and function generator outputs that pair directly with the Pico Voice CV input. An ADSR output assigned to PAR1 via configuration mode gives each triggered note a timbral arc tied to the gate event, transforming the module from a static voice into one that responds expressively to each trigger. The Function Junction LFO output on the same CV input produces slow parameter evolution when PAR2 is fully clockwise for sustained operation.

**Endorphin.es Ghost** is the natural effects processor for Pico Voice output. Ghost's FX-first routing adds reverb and delay texture before light saturation, which complements the Pico Voice's relatively clean algorithm outputs. The Bassline and Karplus-Strong algorithms both benefit from Ghost's filter as an additional tonal shaping stage after the internal voice processing. The Sidechain Trigger input on Ghost can share the same gate source as Pico Voice, so the effects processing ducks rhythmically with each triggered note.

**Intellijel MixUp** brings the Pico Voice output into the broader system. Using two Pico Voice modules on different algorithms and blending them through MixUp at different levels produces hybrid synthesis textures that neither algorithm achieves alone: Wavetable plus Harmonic creates complex evolving timbres with additive overtone content layered over wavetable morphing. MixUp's per-channel mute controls allow algorithm combinations to be brought in and out without level adjustments.
