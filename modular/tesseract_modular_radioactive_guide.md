---
title: Radioactive
manufacturer: Tesseract Modular
primary_role: SOURCE
secondary_roles: [EVENT_VOICE]
historical_context: true
form_factor: eurorack
functions: [oscillator, envelope-generator, wavefolder]
behavior_tags: [lo-fi, dirty, chiptune, chaotic, noisy]
use_cases: [lo-fi voice, chiptune lead, self-contained synth voice, poly voice, experimental lead]
hp: 6
depth: 25mm
memory: basic
transport: none
screen: false
hybrid: true
cv: full
---

# Radioactive

**14-bit wavetable oscillator with built-in envelope, glide, and five-mode voltage-controlled shaper: lo-fi, wild, and deliberately untamed**

![Tesseract Modular Radioactive](https://github.com/Shadoe-42/music/raw/main/modular/images/tesseract_modular/radioactive/front_panel.jpg)

## Historical Context

The history of wavetable synthesis runs from analog experiments at the edges of instrument design through digital hardware built to maximize expression within strict limits. Buchla's Complex Waveform Generator in the early 1970s stored and scanned analog waveforms under voltage control. Wolfgang Palm formalized the concept as a digital technique and built the PPG Wave 2.2 in 1982: a synthesizer that organized single-cycle digital waveforms into tables and allowed scanning through them in sequence or under CV, producing evolving timbres that analog oscillators could not replicate. The PPG became a defining sound of the early 1980s for composers including Peter Gabriel and Thomas Dolby, not because it sounded like acoustic instruments but because it sounded like nothing else. Wavetable synthesis developed from that point as a discipline of organizing waveform geometry into navigable space.

The chiptune tradition arrived at a related aesthetic from a different direction. The game audio chips of the early 1980s (the MOS 6581 SID chip designed by Bob Yannes for the Commodore 64, the Ricoh 2A03 in the Nintendo NES) were engineering constraints, not instruments. Three voices per chip, fixed waveform sets, limited envelope control, minimal memory. The composers who worked within those constraints, including Rob Hubbard and Martin Galway on the SID and Tim Follin on the 2A03, did not treat the hardware's limitations as obstacles to overcome but as the medium itself. Aliasing on high frequencies, the particular texture of low-bit-depth waveforms, the behavior of oscillators being pushed past their rated range: all of these became expressive resources rather than deficiencies. When Tesseract Modular's Sinisa Kekez and Mangu Díaz designed the Radioactive in Seville in 2019, they built a 14-bit wavetable oscillator on an 8-bit microcontroller and pushed it toward its ceiling deliberately. The aliasing on high notes, the buzzing and popping at extreme shaper settings, the Lo-Fi character throughout: these are not errors in the design. They are the design.

The nine waveforms across three sets carry the lineage visibly. Set 1 covers the canonical analog palette: sine, triangle, square. Set 2 offers distorted variants: semi-sine, semi-triangle, and Basso, a waveform whose name signals its low-frequency character. Set 3 reaches further: saw, pulse, and Ondes. That last name is a direct reference to the Ondes Martenot, the French electronic instrument designed by Maurice Martenot in 1928 and written for by Messiaen in the Turangalîla-Symphonie, by Varèse, by Honegger. The Ondes Martenot produced its characteristic tone through a heterodyne circuit, two high-frequency oscillators beating against each other with the audible difference frequency shaped by the instrument's resonating bodies. The waveform was not a simple sine or saw; it had a complex harmonic content from the beating process. Naming a waveform after it in a chiptune-inspired module is a specific historical gesture, reaching ninety years backward from a Seville workshop to a Paris concert hall.

---

## Quick Start

The Radioactive is a self-contained synth voice in 6HP: oscillator, envelope, glide, and shaper in one module. No external VCA is required for basic use. Start here in the default configuration before exploring modes and setup options.

1. Patch OUT to a mixer or filter input. Patch your gate or trigger source into the TRIG/GATE jack.
2. In default state (Mode A, Gate mode, Set 1, Shaper 1), the three LEDs will indicate which waveform is active. Short press the button to advance through waveforms.
3. Send a pitch CV into the PITCH jack. The pitch pot becomes an attenuator for that CV.
4. With nothing in the PITCH jack, the pitch pot controls the oscillator frequency directly (0V to 5V range).
5. Open and close a gate signal: the envelope opens on gate high and closes on gate low. Pots 2 and 3 set Attack and Release times directly.
6. Turn pot 4 (Shaper offset) slowly clockwise and hear the waveform character change. This is Shaper Mode 1 (micro-detune) by default.
7. Hold the button for one second to enter Shift mode, then turn pot 4 to change Shaper Mode. Listen to how Modes 1 through 5 differ on the same waveform.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 6 HP |
| Depth | 25 mm |
| Power | 42 mA avg / 65 mA max +12V / 10 mA -12V / 0 mA +5V |

The +12V draw is specified at two values: 42mA average and 65mA peak maximum. Power budget planning against the average figure may leave insufficient headroom at transient peaks. Use the 65mA maximum figure when calculating rack capacity. The -12V draw is minimal at 10mA.

---

## Architecture Overview: Three Configuration Layers

The Radioactive's front panel carries three distinct layers of labeling, each corresponding to a different operational context. Understanding which layer is active at any moment makes every control decision clear.

**Layer 1: Runtime controls (black square labels).** The four black-square labels on the panel (PITCH, ATTACK/GLIDE, RELEASE, SHAPER) are the active runtime parameters. Each has a corresponding knob (pots 1-4) and a CV input jack (jacks 5-8). When nothing is patched into a CV jack, the knob sets the parameter directly. When a CV is patched, the knob becomes an offset/attenuator for that CV, allowing the incoming voltage range to be scaled and shifted. These parameters are available at all times during normal operation.

**Layer 2: Setup parameters (copper text labels).** The copper-colored panel labels between each knob and jack (SET, ABC, GTP, MODE) indicate parameters that are configured in Setup mode only. Setup mode is entered by holding the button while powering on. In Setup, the same four knobs (pots 1-4) select the wave set, operating mode, envelope trigger mode, and shaper mode respectively. These selections are saved to EEPROM and recalled at every power-on.

**Layer 3: Shift layer (white text labels).** The white labels below pots 2, 3, and 4 (OCTAVE, SUSTAIN, MODE) indicate parameters available when the Shift button is held for one second or more. Shift functions are only accessible when no CV cable is patched into the corresponding jack. Shift+pot 2 sets octave range; Shift+pot 3 sets sustain duration or phase shift (mode dependent); Shift+pot 4 changes shaper mode at runtime without entering Setup.

These three layers share four physical knobs. The active layer determines what each knob does.

---

## Setup Mode: Configured Parameters

To enter Setup, hold the button while turning on the power. All three green LEDs will light and flash to confirm Setup mode is active. Turn pots 1-4 to set the four configured parameters. Press the button to save and exit.

**Wave Set (pot 1 in setup).** Selects one of three waveform sets. The selected set is available at runtime; waveforms from other sets are not accessible without re-entering Setup.

| Wave Set | Waveform 1 | Waveform 2 | Waveform 3 |
|----------|-----------|-----------|-----------|
| Set 1 | Sine | Triangle | Square |
| Set 2 | Semi-sine | Semi-triangle | Basso |
| Set 3 | Ondes | Saw | Pulse |

**Operating Mode (pot 2 in setup).** Selects one of three operating modes that determine the function of pot 2 and jack 6 at runtime.

| Mode | Character | Pot 2 / Jack 6 Function |
|------|-----------|------------------------|
| A | Free range oscillator, Attack and Release envelope | Attack offset / Attack CV |
| B | Free range oscillator, Release envelope with Glide | Glide offset / Glide CV |
| C | Quantized oscillator (semitones), Release envelope with Glide | Glide offset / Glide CV |

**Envelope Trigger Mode (pot 3 in setup).** Selects Gate, Trigger, or Poly behavior. See the Envelope Modes section below for full descriptions.

**Shaper Mode (pot 4 in setup).** Sets the starting shaper mode (1-5). This can also be changed at runtime via Shift+pot 4 without entering Setup, but the runtime change is not saved to EEPROM; only the Setup selection persists across power cycles.

---

## Operating Modes: A, B, and C

**Mode A: Free range oscillator with Attack and Release.** The full AR envelope is available. Pot 2 sets the Attack time (0ms to 1000ms) when no cable is patched into jack 6. Pot 3 sets the Release time. Pitch tracks the PITCH jack in the standard 1V/Oct range. Mode A is the most complete voice mode: attack, sustain (in gate mode), and release are all controlled from the front panel.

**Mode B: Free range oscillator with Release and Glide.** Attack is removed. Pot 2 sets Glide (glissando, pitch slew) from 0ms to 250ms when no cable is patched into jack 6. Glide is the time the oscillator takes to slide from one pitch to the next when the pitch CV changes. Release remains on pot 3. Mode B is suited for melodic patches where smooth pitch transitions matter more than attack shaping, and for classic VCO mode (see below).

**Mode C: Quantized oscillator with Release and Glide.** Identical to Mode B in control structure, but the oscillator's pitch is quantized to semitones. Incoming pitch CV is rounded to the nearest semitone before the oscillator responds. Glide is still active and slides between quantized semitone positions. Mode C is useful when the pitch CV source is not perfectly calibrated or when chromatic quantization is desired without an external quantizer module.

---

## Envelope Modes: G, T, and P

**G (Gate mode, monophonic).** The envelope Attack phase begins when the gate signal goes high. The Sustain phase holds for as long as the gate remains high. The Release phase begins when the gate goes low. Pitch CV changes are tracked in real time during the entire envelope cycle; pitch updates as the pitch CV changes, including during Sustain. In Gate mode, the Shift+Release (Shift+pot 3) function provides an experimental Phase Shift parameter rather than Sustain duration.

**T (Trigger mode, monophonic).** The envelope Attack phase begins on a trigger pulse. The Sustain phase holds for a fixed duration set by Shift+Release (Shift+pot 3, range 80ms to 1000ms), without requiring the trigger signal to stay high. The Release phase begins when the Sustain duration expires. Pitch CV changes after the Sustain phase ends are not tracked until the next trigger. This produces a sample-and-hold behavior for pitch: the module plays the pitch that was present at the moment the trigger fired and holds it for the duration of the envelope cycle. Mode T is suited for step-sequenced patterns where each trigger should capture one specific pitch.

**P (Poly mode, 3-voice polyphonic).** Three separate oscillator voices each with their own envelope cycle, advanced in sequence on each incoming trigger. The first trigger fires voice 1; the second fires voice 2; the third fires voice 3; the fourth fires voice 1 again, regardless of whether voices 2 and 3 have completed their release. Each voice runs its full Attack, Sustain, Release cycle independently. At fast trigger rates with short release times, the three overlapping voices produce a smeared, reverb-like texture. At slower rates with longer release times, the three voices produce a plucked-string character. Poly mode is the Radioactive's most distinctive envelope behavior and rewards patient exploration. Its relationship to pitch CV follows the Trigger mode model: each voice captures the pitch present at the moment of its trigger.

---

## Waveforms and Combinations

Within the selected wave set, the three waveforms can be used individually or combined. The button advances through all available selections in sequence; the Wave input jack advances on each rising trigger. The three green LEDs indicate the current selection: one LED lit is a single waveform; two or three LEDs lit indicates a combination.

Seven possible selections exist per set:
- Waveform 1 only
- Waveform 2 only
- Waveform 3 only
- Waveforms 1+2 combined
- Waveforms 2+3 combined
- Waveforms 1+3 combined
- Waveforms 1+2+3 combined

Combined waveforms are mixed before reaching the Shaper. The combined result is different from any single waveform and provides the Shaper with richer material to process. Set 2's Basso waveform has a complex, noise-rich character that responds dramatically to combination with Set 2's other waveforms and to shaper processing. Set 3's Ondes waveform, when combined with Saw or Pulse, produces complex beating interactions from their heterodyne-adjacent harmonic relationships.

The Wave trigger input (jack 9) accepts any rising edge signal: clock divisions, LFO pulses, gate sequences, random triggers. Using a clock-divided trigger to advance waveforms in rhythm with the patch creates timbral sequencing: the oscillator's waveform character changes on musical time divisions while the pitch and envelope remain under separate control.

---

## The Shaper

The Shaper is a voltage-controlled waveform processor positioned after the oscillator's wavetable output. Pot 4 sets the shaper amount (offset) when no cable is patched into jack 8; with a CV patched, pot 4 becomes an offset/attenuator for the incoming CV. Shaper amount runs from minimum to maximum with no labeled intermediate values; the result is always heard rather than measured.

Five shaper modes are available. The active mode is set in Setup (pot 4) and can be changed at runtime via Shift+pot 4 without entering Setup, though runtime changes are not saved to EEPROM.

**Mode 1: Active micro-detune.** The three internal oscillators (which run as one in standard operation) are spread slightly in frequency from each other, creating a chorus-like thickening effect. At low shaper amounts the detuning is subtle and adds warmth. As shaper amount increases the spread widens, moving from gentle chorus into deliberate beating between the three voices. Mode 1 is the most musically predictable of the five modes and the safest starting point.

**Modes 2, 3, 4:** Each mode applies progressively more complex waveform processing to the oscillator output. The specific character of each mode responds differently to different waveforms; behavior that works musically with Set 1 waveforms may produce very different results with Set 3. Exploring each mode across different waveform selections and different shaper amounts is how the Radioactive's approximately 30,000 possible waveform shapes become accessible. The manual declines to describe modes 2-4 precisely, and that restraint is accurate to the experience.

**Mode 5: Resonant waveform-altering distortion.** The most extreme mode. At moderate amounts it adds resonant character to the waveform, introducing strong harmonic peaks. At maximum, Mode 5 can drive the output to ±8V or approximately 16 volts peak-to-peak, well above the standard Eurorack audio level. This will clip anything downstream that is not prepared for it. Mode 5 on maximum is not a subtle effect; it is a structural change to the signal. Use with caution into sensitive inputs and confirm downstream module headroom before pushing to maximum.

---

## Essential Runtime Controls

**Pitch (pot 1 / jack 5).** The pitch pot is normalled to 5V internally; with nothing patched into jack 5, the pot controls oscillator pitch across the 32.70Hz (0V, C1) to 1046.50Hz (5V, C6) range in Modes A and B. In Mode C, the range is C1 to C6 in quantized semitone steps. When a CV is patched into jack 5, the pot becomes a pitch attenuator scaling the incoming 1V/Oct signal. Pitch does not respond to the Shift button function and remains stable while other Shift parameters are being adjusted.

**Octave Shift (Shift+pot 2, no cable in jack 6).** Holding Shift and turning pot 2 shifts the entire oscillator range by octave: position -1 covers C0-C5, position 0 covers C1-C6 (default), position +1 covers C2-C7, position +2 covers C3-C8. This gives access to the full C0 to C8 range. The Octave Shift setting is not saved to EEPROM and resets to default (0) on power-on.

**Attack/Glide (pot 2 / jack 6).** In Mode A, pot 2 sets Attack time from 0ms to 1000ms. In Modes B and C, pot 2 sets Glide time from 0ms to 250ms. When a CV is patched into jack 6, pot 2 becomes an offset/attenuator for that CV, allowing any voltage range (0-10V, ±5V, ±10V partial range) to be scaled to the parameter's control range.

**Release (pot 3 / jack 7).** Sets Release envelope time from 0ms to 2000ms across most of the pot's range. Turned fully clockwise, Release extends to 60 seconds: useful for sustained pads or for the classic VCO mode described below. When a CV is patched into jack 7, pot 3 becomes an offset/attenuator. With no CV patched, Shift+pot 3 sets Sustain phase duration in Trigger mode (80ms to 1000ms) or an experimental Phase Shift in Gate mode.

**Shaper Amount (pot 4 / jack 8).** Sets the amount of Shaper processing applied to the oscillator output, from minimum to maximum for the active Shaper Mode. When a CV is patched into jack 8, pot 4 becomes an offset/attenuator. With no CV patched, Shift+pot 4 changes the Shaper Mode (1-5) at runtime; the mode change is immediate and audible but not saved to EEPROM.

---

## Classic VCO Mode

To use the Radioactive as a pure oscillator without its internal envelope, bypassing the need for a gate or trigger input: select Mode B in Setup and turn pot 3 (Release) to its full clockwise maximum position. This holds the envelope gate permanently high, sustaining the output at full level without any external trigger signal. The Release envelope is not applied; the oscillator outputs continuously at the current pitch.

In this configuration the Radioactive behaves as a standard VCO: pitch CV controls frequency, an external VCA and envelope generator shape the amplitude as needed. Glide (pot 2 / jack 6) is still active in Mode B, adding pitch slew between CV steps if desired. The Wave input can still be used to advance waveforms externally. The Shaper remains fully functional.

A second application of the maximum-Release setting in Mode B: patching a brief trigger into jack 7 (the Release CV input) while in this state mimics Sample and Hold behavior; each trigger temporarily interrupts the sustained gate and re-triggers the release cycle from the current level. The pot's Release offset setting determines how long that release event lasts.

---

## Signal Flow

### Basic gated voice (Mode A, Gate mode)

```
[Sequencer Pitch CV] ──[C]──▶ [Jack 5 PITCH]
[Sequencer Gate] ──[G]──▶ [Jack 15 TRIG/GATE]
                                               │
[Envelope CV] ──[C]──▶ [Jack 6 ATTACK]        │
[Envelope CV] ──[C]──▶ [Jack 7 RELEASE]        │
                                               │
                          [Internal: 3-osc wavetable → Envelope → Shaper]
                                               │
                                      [Jack 16 OUT] ──[A]──▶ [Filter or Mixer]
```

### Waveform sequencing via Wave input

```
[Pamela Clock Div] ──[G]──▶ [Jack 9 WAVE]
(Advances waveform/combination on each rising edge,
in sync with patch clock; timbral rhythm independent of pitch rhythm)
```

### Classic VCO mode (Mode B, Release at maximum)

```
[Sequencer Pitch CV] ──[C]──▶ [Jack 5 PITCH]
Release: fully clockwise (gate held high permanently)

[Jack 16 OUT] ──[A]──▶ [External Filter] ──[A]──▶ [External VCA] ──[A]──▶ [Mixer]
[External Envelope] ──[C]──▶ [External VCA CV]
```

---

## Advanced Listening and Performance

**Shaper CV for timbral envelope shaping.** Patching an envelope into jack 8 (Shaper amount CV) makes the shaper respond to each triggered event with its own contour. With Mode 5 active and a fast-attack, slow-release envelope driving jack 8, each note begins at maximum shaper distortion and decays back to the clean waveform over the release time. This is a timbral envelope operating in parallel with the amplitude envelope: the note starts harsh and becomes cleaner, or the reverse if the envelope is inverted through an attenuverter before reaching jack 8.

**Wave input as timbral LFO.** Patching a square LFO into jack 9 (Wave trigger) advances the waveform on each rising edge. With an LFO running at a slow rhythmic rate, the oscillator's waveform character toggles in musical time. With a fast LFO approaching audio rate, waveform changes happen so rapidly that the ear hears them as a new composite character rather than discrete switches. The behavior at audio rate is unpredictable and module-dependent; on the Radioactive, fast Wave toggling at audio rate produces complex waveform interactions worth exploring.

**Glide in Mode C for chromatic portamento.** With Mode C selected (quantized) and Glide active, pitch slides between semitone positions rather than jumping. This produces a chromatic portamento: notes arrive at exact semitone positions but approach them from below or above depending on the direction of pitch change. The glide time (0ms to 250ms) determines whether the slide is a subtle slur or a prominent effect.

**Shaper Mode scanning via CV.** Shaper mode is normally set by Shift+pot 4 and not voltage controllable; it is a discrete five-position setting, not a continuous CV parameter. However, systematically moving through modes at runtime while a sequencer plays creates a timbral performance gesture. Holding Shift and slowly turning pot 4 through modes 1 to 5 during a live patch is an expressive choice; do it while listening to how each mode interacts with the current waveform and pitch register.

**Set 2's Basso in Poly mode.** The Basso waveform combined with Poly mode and a medium Release time produces a distinctive dense texture where three voices of the complex waveform overlap and interfere. With fast trigger inputs from a Euclidean generator, Poly mode with Basso reads as a thickened, glitchy rhythmic texture rather than three distinct melodic voices. The shaper at moderate Mode 1 settings adds further thickness.

---

## Pairs Well With

**Hermod+ (Squarp Instruments).** Hermod+ provides simultaneous pitch CV, gate, and multiple CV outputs from a single sequencer. Individual CV tracks can address Shaper amount (jack 8) and Attack/Glide (jack 6) simultaneously with pitch and gate, allowing full per-step timbral control of the Radioactive from a single sequencing hub.

**Pamela's Pro Workout (ALM Busy Circuits).** Clock divisions from Pamela into jack 9 (Wave) create rhythmically timed waveform advances in sync with the patch tempo. Multiple Pamela outputs can simultaneously drive Wave advances and gate the envelope at different subdivisions.

**Any analog filter.** The Radioactive's deliberately Lo-Fi, aliased output character responds dramatically to filtering. A low-pass filter rolling off the high-frequency aliasing content smooths the character significantly; a band-pass filter at resonance on the most active harmonic range of a given waveform creates a pitched, tonal focus from otherwise complex material.

**MISO (Tiptop Audio).** The four CV inputs (Pitch, Attack/Glide, Release, Shaper) can all be addressed simultaneously from different sources with MISO providing attenuation and offset conditioning for any CV that does not match the Radioactive's input range expectations.

**Etna (Patching Panda).** The Radioactive's output through the Etna's triple filter with snapshot morphing creates an evolving processing environment for the Radioactive's timbral changes. When Etna's CV FREQ3 output feeds back to the Radioactive's Shaper CV input, the two modules enter a coupled modulation relationship where filter state influences shaper behavior.

---

## Common Mistakes

**Budgeting power against the average draw.** The Radioactive draws 42mA on average but up to 65mA at peak. Planning rack power against the 42mA figure may leave insufficient headroom at transient load peaks. Use 65mA as the planning figure.

**Not entering Setup before first use.** The default configuration (Mode A, Gate, Set 1, Shaper 1) may not match the intended application. Wave Set, operating mode, and envelope trigger mode are all set in Setup and saved to EEPROM. Take five minutes to configure these before building any patch around the module.

**Expecting the Shaper to behave consistently across all waveforms.** Different waveforms respond very differently to the same Shaper mode at the same amount. A Shaper setting that sounds musical with Sine may produce noise with Square or produce silence with certain Set 2 waveforms at specific mode/amount combinations. The Shaper is a contextual effect; test it with the specific waveform and mode combination in use.

**Mode 5 at maximum into sensitive inputs.** Shaper Mode 5 at maximum produces output that can reach ±8V or 16Vpp. Most Eurorack filter and VCA inputs are not designed to handle signals at this level cleanly. The downstream module will clip, potentially audibly and potentially in ways that damage signal integrity in the chain. Use an attenuator before any sensitive input when Mode 5 is active near maximum.

**Forgetting that Shift+pot changes are not saved.** Octave Shift (Shift+pot 2) and Shaper Mode (Shift+pot 4) changes made at runtime are not written to EEPROM. On the next power cycle, Octave Shift returns to default (0) and Shaper Mode returns to the Setup-saved value. If a Shift-layer setting is part of a patch that needs to be recreated, either save it in Setup or note it separately.

**Treating Mode C quantization as a substitute for a calibrated oscillator.** Mode C quantizes incoming pitch CV to semitones, which corrects imprecise CV sources to the nearest note. It does not improve absolute pitch accuracy if the oscillator itself is not calibrated to the V/Oct standard. Offset calibration (described in the manual's Chapter 7) is required for reliable absolute pitch tracking in any mode.

---

## What's Next

The Radioactive provides a complete self-contained voice in 6HP: oscillator, envelope, glide, and shaper without any external modules. Its Lo-Fi, experimental character is most productive when treated as a source requiring timbral shaping downstream rather than a precise, clean oscillator. The next practical focus is filter interaction: how analog filtering changes the relationship between the Radioactive's aliased digital waveforms and the patch context, and how the Shaper and filter interact when both are processing the same source.

The signal chain literacy guide (modular/basics/06_signal_chain.md) covers the three-path voice model. Because the Radioactive contains its own envelope, the pitch path and gate path converge inside the module rather than at an external VCA, simplifying the external patch while increasing the complexity of internal configuration.

---

*Depth: 25mm. Power: 42mA avg / 65mA max +12V / 10mA -12V / 0mA +5V.*
