---
title: Make Noise Pressure Points
manufacturer: Make Noise
primary_role: CONTROLLER
secondary_roles: [SOURCE]
historical_context: true
form_factor: eurorack
functions: [sequencer]
behavior_tags: [stable, performance-oriented, reactive, sensitive, gated]
use_cases: [performance touch control, pitch CV source, gate and trigger source]
hp: 24
memory: none
transport: none
screen: false
hybrid: false
cv: full
---

# Make Noise Pressure Points

![Make Noise Pressure Points](https://github.com/Shadoe-42/music/raw/main/modular/images/make_noise/pressure_points/front_panel.jpg)

*Four-stage touch plate controller with three preset voltage rows per stage and individual gate/pressure outputs: analog preset storage through physical potentiometer positions, selected by direct skin contact*

---

## Historical Context

The piano keyboard became the default interface for electronic music instruments not because it was optimal for synthesis but because it was familiar. When the first commercially viable synthesizers appeared in the 1960s, keyboard players were the target market, and manufacturers gave them the interface they already knew. The keyboard maps one key to one pitch and reads velocity at the moment of key strike; it provides no information about what the performer's hand is doing after the note begins. For an acoustic piano, that is acceptable because the hammer mechanism handles the rest. For a voltage-controlled synthesizer, where any parameter can be a continuous variable for the entire duration of a sound, the keyboard offers a single data point where the instrument could accept continuous expression. This limitation was recognized immediately by the engineers who thought most carefully about what electronic music instruments could be.

Don Buchla was commissioned by Morton Subotnick and Ramon Sender at the San Francisco Tape Music Center in 1962 to build a voltage-controlled instrument from the ground up. Buchla designed the Series 100 without a keyboard intentionally and without apology: in a system where voltage controls pitch, the assignment of voltage to key position is arbitrary, and a copper touch plate can provide pressure, contact area, and position as simultaneous variables rather than the single velocity value of a piano key. The Buchla 112 Touch Controlled Voltage Source, part of the original Series 100 system, presented four copper plates that produced voltage proportional to applied pressure, with no fixed pitch assignment. The performer could map any voltage to any synthesis parameter. This was not a workaround for an absent keyboard; it was a statement that the keyboard was the wrong tool for the instrument. The idea of constructing synthesis interfaces around the physical properties of human touch rather than the mechanics of a nineteenth-century concert instrument is the philosophical root of every touch controller that followed.

Through the 1970s and 1980s, pressure-sensitive performance interfaces developed in parallel to traditional keyboard controllers. The Serge synthesizer used touch-plate triggers as a primary interface. Breath controllers emerged for wind players. The specific limitation that persisted across this era was preset storage: a touch plate could capture gesture beautifully, but it could not remember what voltage it was supposed to output in a given musical context. Reprogram a performance from one piece to another and the performer had to repatch the entire system. The gesture was captured; the musical context around it was not. This remains the central unsolved problem in touch controller design until a module explicitly addresses it.

Make Noise was founded by Tony Rolando in Asheville, North Carolina, around 2010. The Pressure Points design directly addresses the preset storage gap: three rows of potentiometers (X, Y, Z) each store one voltage value per stage, so each of the four touch plates accesses three completely independent preset voltages simultaneously. The preset is encoded in the physical knob positions, readable at a glance without menus or displays, and survives power cycles because it is stored in the potentiometer, not in memory. One touch gesture simultaneously outputs a gate, an analog pressure CV, and three preset voltages, each independently patched to wherever they are useful. A Make Noise Brains expander adds logic and sequencing capability to the touch plate outputs; Shadoe does not own the Brains, and the practical details of how it integrates into a system are outside the scope of this guide.

---

## Quick Start

Pressure Points stores three independent voltage values per stage across four stages, accessed by touching copper plates with bare fingers. Touching a plate selects that stage and outputs its preset voltages on X, Y, Z common outputs, while also generating a gate signal and a pressure CV proportional to how hard you press. The module requires clean, bare hands: skin conductivity is what completes the circuit.

1. Wash and dry your hands. Oils, lotions, and gloves prevent the plates from sensing contact.
2. Connect Pressure Points Tuned Voltage Y common output to a VCO V/OCT input.
3. Connect Pressure Points Common Gate to an envelope generator trigger input.
4. Connect the envelope generator output to a VCA control input, and VCO output through the VCA to your mixer.
5. Touch plate 1. You should hear a note. Touch plate 2. Different note, or the same if you have not tuned the Y row yet.
6. Turn the four Y row potentiometers to four different pitch positions. Touch each plate to hear its pitch.
7. If plates do not respond reliably, locate the Digit Trimmer on the circuit board (right side) and turn it clockwise slightly with the power off, then power back on.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 24 HP |
| Depth | 25 mm ⚠️ |
| Power | 30 mA +12V ⚠️ / 20 mA -12V ⚠️ / 0 mA +5V |

---

## Essential Parameters

The four copper touch plates are the primary interface. Each plate is a printed copper circuit surface that responds to skin conductivity when touched with a bare finger. A light touch activates the gate output for that stage and selects its preset voltages on the common X, Y, Z outputs. Pressing harder generates a proportional voltage on the pressure output, ranging from zero at no contact to a variable maximum determined by applied force and contact area. Using more of the finger pad rather than just the fingertip produces a more consistent pressure CV response because the contact area is larger. The module responds to the biology of the performer: skin moisture, temperature, and finger size all affect the character of the response.

The Digit Trimmer is a small trimmer potentiometer on the circuit board, accessible from the panel with a small screwdriver. It adjusts the overall touch sensitivity threshold to accommodate different skin types and playing conditions. The factory default position works for most players; players with dry skin, smaller fingers, or modules mounted at unusual angles may need to increase sensitivity by turning it clockwise. Adjustments should be made with the module powered off. The correct setting is the minimum sensitivity that produces reliable response to light touch: too high a sensitivity setting causes false triggering from proximity or heat.

Tuned Voltage Row X spans 0 to 8V and is the general-purpose voltage row. Because its maximum matches or exceeds gate voltage levels, turning an X row potentiometer fully clockwise outputs a persistent high voltage and fully counterclockwise outputs zero, which can function as a manual gate or a static CV offset. Row X is well-suited to controlling parameters that benefit from a full 8V range: oscillator FM depth, envelope times, LFO rates.

Tuned Voltage Row Y spans 0 to approximately 5.5V and covers roughly 5.5 octaves of 1V/octave pitch range. It is the primary pitch row. Tuning the four Y potentiometers to musical intervals creates a four-note touch keyboard; tuning them to specific harmonic relationships creates a chordal or modal fingering system. The limited four-stage architecture is a constraint that encourages deliberate pitch selection rather than chromatic coverage.

Tuned Voltage Row Z spans the same 0 to 5.5V range as Row Y and is typically used for a second independent parameter that changes with each stage alongside the pitch from Y. Filter cutoff, LFO rate, reverb send level, or oscillator waveform selection are all reasonable Z row applications. The value of Z is that it allows each stage to define a complete timbre context rather than only a pitch: stage 1 might be a bright high note, stage 2 a dark low note, with the filter state encoded in Z rather than manually adjusted between touch events.

The individual outputs provide a separate gate and separate pressure CV for each of the four stages independently. These are distinct from the common outputs. With individual gates patched to four different envelope generators, each touch plate can trigger a different voice or a different synthesis process simultaneously. With individual pressure CVs patched to four different parameter targets, the pressure from each plate can affect something unique to that stage. Most players begin with the common outputs, which provide a single gate and single pressure CV from whichever stage is active, before exploring the additional routing possibilities of the individual outputs.

---

## Why This Instrument Excels

The preset architecture is genuinely novel among Eurorack controllers. Twelve voltage values (three rows times four stages) are stored in the physical positions of twelve potentiometers. There is no digital memory, no patch storage, no recall sequence. The preset is the knob position: it is visible, it survives power loss, it can be read at a glance from across the room, and it can be adjusted in performance by physically turning a knob. Most modular preset systems involve either saving to firmware memory (requiring a recall gesture) or writing down settings (requiring attention away from performance). Pressure Points stores presets the way a mechanical instrument stores tuning: in the physical state of the instrument itself.

A single touch event simultaneously generates five or more independent signals: a gate, a pressure CV, and three preset voltages from X, Y, and Z. Each of those signals travels to wherever it is patched, affecting whatever parameter is connected at that destination. The gate triggers an envelope. The pressure CV modulates filter cutoff. Y controls oscillator pitch. X controls FM depth. Z controls reverb send. One finger touch produces a coordinated, multi-dimensional change across the entire synthesis chain at once. This is not something a MIDI controller can replicate without significant mapping overhead, and it is not something a sequencer can replicate without step programming. The touch event is atomic: it all happens simultaneously, because it is all one analog signal path per output.

The copper plate interface removes the intermediary between the performer and the circuit. There is no sensor, no ADC, no digital processing between finger and voltage: the skin closes an analog circuit, and the resulting conductivity variation generates the pressure CV directly. This means the response characteristics of the interface are tied to the biology of the performer in ways that no digital system can fully simulate. Skin moisture changes across a performance. Body temperature changes. The angle of contact changes. These variations produce subtle changes in the pressure CV output that are not programmed or controlled: they emerge from the physical reality of the performer's state. This is not a limitation; it is the quality that makes Pressure Points distinctly expressive rather than merely responsive.

Four stages is a severe constraint by sequencer standards, but it is the correct constraint for a touch performance interface. A 16-step sequencer requires either a single-step mental model (advance through the sequence) or a complex addressing scheme to jump non-linearly. Four plates can be addressed instantly by any four fingers on one hand, and the relationships between the stages can be internalized spatially with a few minutes of practice. The performer knows where each pitch is without looking. The limitation forces musical discipline in the preset design: with only four stages, each stage must earn its position in the system. Players who find four stages insufficient can chain multiple Pressure Points units together, expanding the touch surface in multiples of four while retaining the same analog simplicity per unit.

---

## Patches

### Patch 1: Touch Keyboard

This patch establishes Pressure Points as a four-note touch keyboard with gate-triggered envelopes and pitch from the Y row.

```
PRESS. POINTS Tuned Y ──[C]──▶ VCO V/OCT
PRESS. POINTS Common Gate──[G]──▶ [Envelope Gen] GATE IN
[Envelope Gen] OUT ──────[C]──▶ VCA CV IN
VCO OUT ─────────────────[A]──▶ VCA IN
                               VCA OUT ──[A]──▶ [Mixer]
```

**Setup:** Connect Tuned Voltage Y to a VCO V/OCT input. Connect Common Gate to an envelope generator gate input. Connect the envelope generator output to a VCA control input and VCO output through the VCA to a mixer.

**Controls:** Turn the four Y row potentiometers to four different pitch positions: roughly 0V, 1V, 2V, and 3V gives a three-octave spread in one-octave steps. Set the envelope generator for a medium attack and medium release. Touch each plate and listen. Refine Y row tuning until the four pitches form a musical relationship: a minor third, a major chord, a tritone, or whatever interval serves the piece. Try sliding between plates for legato transitions and lifting cleanly between them for staccato.

**Result:** A four-note touch keyboard with gate-driven amplitude. The four notes are immediately accessible spatially: left hand pinky through index covers all four stages in one natural hand position. The patch requires no sequencer and no clock; the performer is the sequencer.

---

### Patch 2: Pressure-Expressive Voice

This patch extends Patch 1 by routing the pressure CV to a secondary parameter, adding continuous expression to the touch keyboard.

```
PRESS. POINTS Tuned Y ──[C]──▶ VCO V/OCT
PRESS. POINTS Common Gate──[G]──▶ [Envelope Gen] GATE IN
PRESS. POINTS Common Press──[C]──▶ VCF CUTOFF CV
[Envelope Gen] OUT ──────[C]──▶ VCA CV IN
VCO OUT ──────────────── [A]──▶ VCF IN
VCF OUT ─────────────────[A]──▶ VCA IN
                               VCA OUT ──[A]──▶ [Mixer]
```

**Setup:** Add a filter between the VCO and VCA from Patch 1. Connect Common Pressure to the filter cutoff CV input. Set the filter cutoff to a closed position and add enough CV depth from the attenuverter that pressing firmly opens the filter noticeably.

**Controls:** Touch a plate lightly: note triggers with a closed, dark tone. Press harder: the filter opens and the note brightens in proportion to the applied force. Release pressure while holding the gate: filter closes. The gate and pressure are independent signals. A sustained note can shift from dark to bright and back while the gate remains open, all controlled by how hard you press.

**Result:** A touch keyboard with pressure-sensitive timbre. Notes are not only pitched but timbral: a soft touch produces a closed, dark tone and a firm press opens into brightness. This is the quality that distinguishes Pressure Points from a keyboard: a keyboard cannot modulate timbre continuously during the sustain of a note. The finger can.

---

### Patch 3: Four Independent Voices via Individual Outputs

This patch routes the four individual gate outputs to four different envelope generators, making each plate trigger a distinct synthesis voice.

```
PRESS. POINTS Gate 1 ──[G]──▶ [ENV 1] GATE IN → VCA 1 → Voice 1 ──[A]──▶ [Mixer Ch 1]
PRESS. POINTS Gate 2 ──[G]──▶ [ENV 2] GATE IN → VCA 2 → Voice 2 ──[A]──▶ [Mixer Ch 2]
PRESS. POINTS Gate 3 ──[G]──▶ [ENV 3] GATE IN → VCA 3 → Voice 3 ──[A]──▶ [Mixer Ch 3]
PRESS. POINTS Gate 4 ──[G]──▶ [ENV 4] GATE IN → VCA 4 → Voice 4 ──[A]──▶ [Mixer Ch 4]
PRESS. POINTS Tuned Y ──[C]──▶ VCO V/OCT (shared pitch, or per-voice)
```

**Setup:** Connect each individual gate output (Gate 1, Gate 2, Gate 3, Gate 4) to a separate envelope generator input. Route each envelope through a VCA to a separate voice or to separate mixer channels from the same voice. This requires four envelope generators; Make Noise Maths can supply two channels, and a second utility module can supply the other two.

**Controls:** Set each envelope to a different shape: Gate 1 short percussive, Gate 2 slow swell, Gate 3 plucked, Gate 4 long pad. Touch plate 1: only envelope 1 fires. Touch plate 2: only envelope 2 fires. Hold plates 1 and 3 simultaneously: envelopes 1 and 3 fire at the same time. The X and Z rows on each stage now control parameters specific to whatever synthesis process that stage is connected to.

**Result:** Four stages with genuinely different synthesis behaviors, all accessible through touch. The common output approach treats all four stages as variations on one voice; the individual output approach treats each stage as a separate instrument under the performer's hands. Holding multiple plates simultaneously produces chords or layered textures that a common-output-only approach cannot.

---

### Patch 4: Slewed Pressure with Rings as Resonator

This patch combines pressure expression with slew limiting to produce smooth, continuous timbral modulation driving a Mutable Instruments Rings resonator.

```
PRESS. POINTS Tuned Y ──[C]──▶ RINGS V/OCT
PRESS. POINTS Common Gate──[G]──▶ RINGS STRUM
PRESS. POINTS Common Press──[C]──▶ [Maths Ch 1] IN (slew/portamento)
[Maths Ch 1] OUT ───────────[C]──▶ RINGS BRIGHTNESS CV (via attenuverter)
[Maths Ch 3] OUT (slow LFO)─[C]──▶ RINGS STRUCTURE CV (via attenuverter)
                                   RINGS ODD ──[A]──▶ [Mixer Left]
                                   RINGS EVEN──[A]──▶ [Mixer Right]
```

**Setup:** Connect Tuned Voltage Y to Rings V/OCT and Common Gate to Rings STRUM. Patch Common Pressure into Make Noise Maths channel 1 in portamento/slew mode: set the rise and fall times to smooth the pressure CV response. Connect Maths channel 1 output to Rings BRIGHTNESS CV through the attenuverter. Set Maths channel 3 as a slow free-running LFO into Rings STRUCTURE CV.

**Controls:** Select the Rings modal algorithm (green LED). Set DAMPING for a long decay. Touch plates and vary pressure during sustained notes. The slew from Maths smooths the pressure CV so that the BRIGHTNESS response follows the pressure gesture with a slight lag, producing a bowing or swelling quality rather than an immediate step. The LFO on STRUCTURE slowly evolves the resonant character of each note independently of the touch gesture. Tune the Y row to pitches that complement Rings' modal decay behavior: longer intervals work well because the sustain gives the modulation time to develop.

**Result:** A touch-controlled resonator voice where pressure shapes the timbral evolution of each note and an independent modulation source shapes the resonator's character over longer timescales. The slew processing on the pressure signal transforms finger dynamics from control events into something closer to bowing pressure on a string instrument.

---

## Common Mistakes

### "The plates are not responding at all"

The copper plates sense skin conductivity, not physical pressure. Oils, lotions, and residue on the fingers reduce conductivity below the activation threshold. Gloves prevent contact entirely. The fix is clean, bare hands: wash with soap, rinse, and dry completely before playing. If plates still do not respond after cleaning, the Digit Trimmer sensitivity setting may be too low for the current skin conditions or environmental temperature. Increase it by turning clockwise with the module powered off.

### "All four stages play the same pitch"

The Y row potentiometers are set to the same position. Each stage has its own potentiometer for each row: four knobs in the Y row, four in the X row, four in the Z row. If all four Y knobs are at noon, all four stages output the same voltage. Turn each Y potentiometer to a distinct position and verify that touching each plate produces a different pitch. This also applies to X and Z: if the preset voltages are not varied across stages, the module behaves as a switch to a single preset rather than a four-stage performance controller.

### "The pressure CV jumps or pops at the start of each touch"

The initial touch event produces a small transient as the circuit registers contact before building pressure CV proportionally. This is more noticeable when pressure CV is patched to fast-responding parameters like oscillator FM depth or a filter cutoff with no CV slewing. The fix: add a slew limiter or a short attack envelope in the path between pressure output and the destination parameter. Make Noise Maths in portamento mode between Common Pressure and the target smooths the onset without affecting the sustained pressure response. Setting a short attack on the envelope generator triggered by the gate also helps by delaying the parameter change slightly relative to the note attack.

### "I am only using the Common outputs and the individual outputs are doing nothing"

The individual gate and pressure outputs for each stage are separate jacks that require separate cables. They are not alternatives to the common outputs; they provide per-stage signals in addition to the combined common signals. Patching Gate 1, Gate 2, Gate 3, and Gate 4 to four different envelope generators is one of the most musically distinctive capabilities of the module. Without exploring the individual outputs, Pressure Points is used as a single-voice touch keyboard, which is useful but represents roughly half the available architecture.

### "The Digit Trimmer adjustment is making things worse, not better"

Two common errors occur during sensitivity adjustment: adjusting with the module powered on (the trimmer is a high-voltage circuit element that should only be adjusted with power off), and adjusting in large steps past the optimal range. The correct approach is small increments: adjust slightly, power on, test, power off, adjust again. The target is the minimum sensitivity that produces reliable response to a light touch, not the maximum sensitivity. Setting sensitivity too high causes false triggers from proximity, body heat, or vibration. When in doubt, return to the factory position (approximately 40% clockwise) and work from there.

---

## Advanced Learning Path

1. Master the four stages as a fully tuned four-note melodic instrument. Tune the Y row to a specific chord or scale fragment that is useful in your musical context: a minor third, a dominant seventh voicing, a pentatonic cluster. Practice touching each plate without looking, building spatial memory of which pitch is where. The goal is to touch without looking the way a pianist knows where middle C is: the hand goes to the right position without conscious direction.

2. Add the Z row as a simultaneous timbral control. For every Y row tuning decision, make a corresponding Z row decision: what filter cutoff, LFO rate, or synthesis parameter should accompany this pitch? Stage 1 might be a bright high note with a fast filter; stage 4 a dark low note with a slow filter. Program Z row values to form a coherent relationship with Y row values so that each stage presents a complete timbral context, not just a pitch.

3. Use the X row gate trick for rhythmic patterns without an external sequencer. Turn one or two X row potentiometers fully clockwise (gate high) and the others fully counterclockwise (gate low). Patch X common output to an envelope trigger or to a gate destination. Now touching different plates opens or closes that X row gate independently of whether the note gate fires. This creates the ability to trigger a secondary synthesis event on some but not all stage selections.

4. Patch individual stage gate outputs to separate destinations. Use Gate 1 through Gate 4 to trigger four different envelope generators with four different shapes. Each plate now produces not only its preset voltages but its own unique amplitude envelope. Touching plates in succession produces four voices with four distinct articulation characters. Holding multiple plates simultaneously produces layered events.

5. Introduce slew limiting on the pressure output. The raw pressure CV tracks finger movement at audio speeds and can produce sudden jumps that sound mechanical rather than expressive. Running the pressure CV through Make Noise Maths in portamento mode, or through a dedicated slew limiter, transforms the response from a step-like control signal to a smooth, gesture-following curve. This is particularly valuable when pressure CV controls reverb send, filter resonance, or other parameters where smooth transitions are musically preferred.

6. Program stages for non-sequential musical relationships rather than scalar progressions. Nothing requires stage 1 through stage 4 to represent ascending pitches. Stage 1 and stage 3 could be the tonic; stage 2 the dominant; stage 4 an octave displacement. Design the stage relationships for the music that will be performed, not for the convenience of numbering. Four stages can represent a complete harmonic field rather than four points on a line.

7. Combine Pressure Points with a clock source and envelope generators to create hybrid performance/automation structures. Use Pressure Points to select which synthesis preset is active and to inject pressure expression, while a clock or sequencer handles rhythmic articulation. The two systems operate independently: the performer controls pitch and timbre through touch; the clock controls timing. This separation frees the performer from rhythmic precision while retaining complete harmonic and timbral control.

---

## Pairs Well With

**Make Noise Maths** is the most natural processing partner for Pressure Points' outputs. Maths channels handle pressure CV slewing for smooth gesture response, envelope generation from gate triggers, and end-of-cycle pulse generation for derived events. The common pressure output slewed through Maths produces a bowing or breath-like quality that raw pressure CV does not have. Maths' two channels plus the Pressure Points outputs constitute a complete expressive voice controller without requiring any additional modules.

**Make Noise Optomix** responds to CV control in a way that reflects the organic character of touch control particularly well. The Low Pass Gate architecture of Optomix means that the CTRL input simultaneously controls amplitude and filter frequency: a single pressure CV opening the gate produces both louder and brighter output, exactly as a struck physical instrument does. Common Pressure patched to an Optomix CTRL input produces amplitude and filter dynamics that track finger pressure in a physically intuitive way.

**Mutable Instruments Rings** serves as the ideal sound source for extended pressure-expressive patching. Rings' BRIGHTNESS and DAMPING inputs accept pressure CV with musically meaningful results: pressure into BRIGHTNESS produces the timbral arc of a struck resonating body, and pressure into STRUM combined with pitch from Y row creates a touch-controlled physical modeling voice. The dual ODD/EVEN outputs from Rings add stereo width to the result without additional processing.

**Any voltage-controlled filter** benefits from the simultaneous gate-and-pressure architecture. The gate triggers the envelope that opens the VCA; the pressure CV, patched separately to the filter cutoff, provides a continuous timbral control during the sustained portion of the note that the envelope alone cannot produce. A simple filter with a single CV input accepts pressure directly. A filter with multiple CV inputs accepts both an envelope for the attack sweep and continuous pressure for the sustained timbral character independently.

**Mutable Instruments Marbles** provides a contrasting but complementary approach to the same pitch and gate destinations. Where Pressure Points gives direct human control over pitch selection and timing, Marbles generates probabilistic pitch and timing from a clock source. Patching both to a VCO V/OCT through a switch or A/B module creates a performance where the musician can alternate between programmed generative sequences and direct touch control: Marbles when stepping back, Pressure Points when stepping forward. The shared voltage architecture means both sources speak the same language at the destination.

---

*Official documentation: [Make Noise Pressure Points](https://www.makenoisemusic.com/modules/pressure-points)*
