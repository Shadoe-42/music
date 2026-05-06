---
title: "Endorphin.es New Godspeed"
manufacturer: "Endorphin.es"
primary_role: SOURCE
secondary_roles: [SHAPER]
historical_context: "Triangle core VCO lineage; thermal drift and the tempco problem; thru-zero FM from the Buchla tradition; wavefolder synthesis and west-coast timbre generation; Roland SH-101 single-oscillator plus sub architecture"
form_factor: eurorack
functions:
  - triangle-core-vco
  - thru-zero-linear-fm
  - wavefolder
  - harmonic-waveshaping
  - sub-oscillator
  - trs-midi
behavior_tags:
  - pitched
  - harmonic-shaping
  - fm-capable
  - self-contained-fm
  - chromatic-autotune
  - dual-output-character
use_cases:
  - melodic-voice
  - two-operator-fm
  - west-coast-waveshaping
  - dual-timbre-voice
  - sub-bass
  - noise-plus-tone-textures
hp: 6
depth: 30
memory: true
transport: midi
screen: false
hybrid: true
cv: full
---

# Endorphin.es New Godspeed

**A hybrid triangle-core VCO with instant chromatic autotune, thru-zero FM, a wavefolder, a harmonic waveshaper, and a sub oscillator. Two outputs with distinct tonal characters. Six HP.**

---

## Historical Context

Every analog oscillator drifts. The triangle core at the heart of the New Godspeed is a classic topology dating to the earliest synthesizer designs: a comparator and an integrator exchange control to produce a triangle waveform, which is then processed into other shapes. The triangle itself is internally clean but the analog components that generate it are temperature-sensitive. As the circuit heats up from a cold start, component values shift, and the pitch moves with them. This phenomenon, called thermal drift, was the central engineering problem of early voltage-controlled oscillators.

The traditional engineering solution was the temperature compensation resistor, a specialized component whose resistance changes with temperature in a way that counteracts the drift of the oscillator core. Getting these resistors right required careful selection and matching. Even with proper compensation, analog VCOs benefit from a warmup period and may require tuning adjustments over the course of a session. This is not a defect but a physical property of the analog circuitry, and it shaped how synthesis was practiced: players routinely tuned oscillators at the start of a set and sometimes between songs.

Digital oscillators solved the drift problem by moving pitch generation into a domain where temperature has no effect on frequency. But the digital approach trades thermal stability for a different quality: the sound. Analog triangle cores have a character shaped by the imperfections of the circuit, the slight asymmetry of the waveform, the nonlinearity of the comparator behavior at the switching points. This character is difficult to replicate digitally.

The New Godspeed is a hybrid instrument: an analog triangle core for sound generation paired with digital control for pitch accuracy. The digital side handles the autotune system, pitch quantization, and MIDI integration. The analog side handles the waveforms that come out. The result is an oscillator that does not drift and does not require manual tuning, while retaining the tonal character of an analog core.

The thru-zero FM capability connects the New Godspeed to a different lineage. Linear frequency modulation, in the form developed by Don Buchla in the late 1960s and early 1970s, operates by adding an audio-rate signal directly to the frequency of a carrier oscillator. When the modulator signal drives the carrier frequency toward zero and then through it, the carrier phase reverses rather than stopping. This thru-zero behavior produces FM textures that are clean and metallic at moderate depths and increasingly complex at higher depths, without the timbral artifacts that appear when non-thru-zero FM approaches zero frequency and stalls. The New Godspeed carries an internal virtual sine wave as a normalled FM modulator, making it a self-contained two-operator FM voice with no additional modules required.

The wavefolder tradition in the New Godspeed's SINE/FOLD output traces to the Buchla 259 complex oscillator and related west-coast synthesis instruments. A wavefolder takes a waveform and reflects it back on itself when it exceeds a threshold, creating additional zero-crossings and harmonic content that does not exist in the original signal. Applied to a sine wave, folding produces bell-like and bongo-like tones at low depths and harmonically dense textures as depth increases. This is a different approach to harmonic generation than the subtractive method common in east-coast synthesis: instead of starting with a harmonically rich waveform and filtering it, the wavefolder starts with a harmonically simple signal and adds complexity through shaping.

The EVEN/ODD output's tonal reference is the Roland SH-101, released in 1982. The SH-101 was a single-oscillator monophonic synthesizer with a suboscillator, designed to produce full, thick mono bass and lead tones from one voice. The sub oscillator added a square wave one octave below the main oscillator, reinforcing the low end and filling out the sound. The New Godspeed's EVEN/ODD output, with its sub normalled in and its continuous shift from warm even harmonics toward hollow odd harmonics, occupies similar tonal territory: present, mono, thick.

Endorphin.es is a Barcelona-based manufacturer (Furth Barcelona S.L.) that produces the New Godspeed and its sibling modules at the intersection of analog audio character and digital control precision.

---

## Quick Start

Patch a pitch CV source into the 1V/OCT jack [C] and a cable to either output. The SINE/FOLD output [A] produces a sine wave shaped by the TIMBRE knob. The EVEN/ODD output [A] produces a harmonically warmer signal with the sub oscillator mixed in.

Press the TUNE button once to snap the current pitch to the nearest C, G, or A. The LED blinks briefly and returns to steady on. The oscillator is now in tune.

Turn the FM INDEX knob clockwise with nothing patched into the FM IN jack to increase self-FM depth. The internal sine wave modulates the carrier through zero, producing FM textures without an external modulator.

Turn the TIMBRE knob clockwise to add wavefolder character to the SINE/FOLD output or to shift the EVEN/ODD output toward odd harmonics.

---

## Key Specifications

| Parameter | Value |
|---|---|
| Format | Eurorack |
| Width | 6 HP |
| Depth | 30 mm |
| Current Draw | 65 mA +12V / 40 mA -12V / 0 mA 5V |
| Price | $209 |
| Core | Analog triangle, digital pitch control |
| Outputs | SINE/FOLD, EVEN/ODD, SUB |
| FM Type | Thru-zero linear FM |
| MIDI | TRS MIDI IN (A or B standard) + THRU |
| Memory | Yes (LOCK state, autotune target, sub octave, MIDI channel) |

---

## The Tuning System

The New Godspeed's most immediately practical feature is its autotune system. Analog VCOs drift as they warm up. The New Godspeed eliminates the tuning problem by embedding a tuning reference and calibration routine directly into the module.

### TUNE Button

A single press of the TUNE button triggers an instant calibration: the module detects the current pitch of the oscillator core and adjusts the digital control to snap to the nearest reference note. The snap is immediate, not gradual. The LED blinks briefly during the operation and returns to steady on when complete.

The reference note is selectable. By default the module snaps to the nearest C. A long press of five seconds cycles through the three available targets. One blink after release sets C (default). Two blinks sets G. Three blinks sets A. The chosen target persists across power cycles.

C is the most universally useful reference for Western pitched music. G and A are provided for players who work in contexts where tuning to a drone or reference pitch is more natural than tuning to C. For standard chromatic work, C is the correct choice and does not need to be changed.

### LOCK

A double-click of the TUNE button locks the PITCH knob. The LED remains on steady without blinking as long as LOCK is active. In LOCK mode, the PITCH knob no longer controls pitch. The oscillator receives pitch only from the 1V/OCT jack and from MIDI. This allows confident use of the PITCH knob's secondary functions (sub octave selection, MIDI channel setting) without accidentally shifting the pitch during a performance or patch.

LOCK state persists across power cycles.

### PITCH Knob

The PITCH knob provides pitch offset in a range of approximately two octaves above and two octaves below center. Unlike a traditional continuous-sweep pitch knob, the PITCH knob moves in discrete chromatic semitone steps. There is no position between C and C-sharp: the knob clicks through individual semitones.

This design makes the PITCH knob useful as a transpose control rather than a fine-tuning tool. Shifting the oscillator up a fifth, down an octave, or to a specific interval relative to center is a deliberate operation that lands on a note, not a frequency somewhere between notes.

Fine tuning within a semitone is not available through the PITCH knob. The autotune system handles absolute pitch accuracy. If fine adjustment is needed after autotune, use the 1V/OCT input and a precise offset source.

### OCTAVE Switch

A three-position toggle switch transposes the oscillator by one octave up, center (no transpose), or one octave down. This is independent of the PITCH knob and operates in addition to whatever the PITCH knob is set to.

---

## Pitch CV and FM Input

### 1V/OCT Jack [C]

Standard exponential pitch CV input. The jack is unattenuated and DC-coupled. The input range is -5V to +5V, covering ten octaves. Sequences, keyboards, MIDI-to-CV converters, and other pitch sources connect here in the usual way.

### FM IN Jack [C]

Thru-zero linear FM input. The jack is AC-coupled, which means slowly moving voltages and DC offsets do not pass through. The input responds to audio-rate signals, which is the correct modulator range for FM synthesis. The input is not exponential: it is linear, meaning equal voltage changes produce equal frequency shifts rather than equal interval shifts. This linear response is what enables thru-zero behavior.

When nothing is patched into the FM IN jack, the module normalls its own internal virtual sine wave to the input. The oscillator self-modulates. The FM INDEX knob controls the depth of this self-modulation. With INDEX at minimum, the output is the unmodulated waveform. As INDEX increases, the internal sine drives the carrier into FM territory. At high INDEX values the carrier and modulator are the same fundamental frequency, producing classic two-operator FM timbres: metallic, bell-like, or harmonically complex depending on the exact tuning relationship.

Patching an external signal into the FM IN jack breaks the internal normal. The external signal becomes the modulator. The FM INDEX knob then controls the depth of external modulation.

---

## FM INDEX

The FM INDEX knob has two behaviors depending on whether a cable is present at the INDEX CV jack.

With nothing patched into INDEX CV, the INDEX CV input is normalled to +5V. The FM INDEX knob acts as a direct depth control: turned fully counterclockwise, no FM; turned clockwise, increasing FM depth. The knob is the primary control of FM character.

With a cable patched into the INDEX CV jack, the incoming CV signal drives FM depth and the FM INDEX knob becomes an attenuator for that CV. At minimum, the CV has no effect. At maximum, the CV has full effect. The knob sets how much of the incoming CV range is applied to FM depth.

This normalled-to-+5V design is important to understand: when no CV is patched, the knob is a direct depth control. When CV is patched, the knob is an attenuator. The same physical control has different roles depending on what is connected.

### Secondary Function: Sub Octave Selection

Holding the TUNE button and turning the FM INDEX knob sets the sub oscillator octave. Three positions are available: sub at one octave below the main oscillator, sub at two octaves below, or sub at three octaves below. The selection is stored in memory and persists across power cycles.

---

## The Two Outputs

The New Godspeed produces two simultaneous, independent outputs with distinct tonal characters. Both are available at all times and can be used simultaneously for two different sounds from one oscillator.

### SINE/FOLD Output [A]

This output begins as a pure sine wave derived from the triangle core. The TIMBRE knob controls a wavefolder applied to this sine wave.

At TIMBRE minimum, the output is a clean sine: the smoothest, most harmonically simple waveform the oscillator produces. No overtones beyond the fundamental.

As TIMBRE increases, the wavefolder reflects the sine wave back on itself at progressively lower amplitude thresholds. The first fold adds a second harmonic peak above the fundamental. Further folding adds more harmonic content. At high TIMBRE settings the waveform crosses zero multiple times per cycle, producing a dense harmonic spectrum with bell-like or hollow resonant qualities. These are timbres associated with west-coast percussion synthesis: the bongo tones, the metallic bell strikes, the hollow woody sounds that Buchla-lineage instruments are known for.

The wavefolder responds to TIMBRE CV in the same normalled-to-+5V manner as INDEX CV: with nothing patched, TIMBRE is a direct depth control; with CV patched, TIMBRE becomes an attenuator for the incoming signal.

### EVEN/ODD Output [A]

This output uses the triangle core differently. The TIMBRE knob controls a continuous waveshaping sweep from even harmonics to odd harmonics.

At TIMBRE minimum, the output emphasizes even harmonics. Even harmonics are octave-related to the fundamental: the second harmonic is one octave up, the fourth harmonic is two octaves up. Even harmonic content sounds warm, full, and sawtooth-adjacent. The even harmonic extreme of this output has body and density without harshness.

At TIMBRE maximum, the output emphasizes odd harmonics. Odd harmonics are non-octave-related to the fundamental: the third harmonic is an octave and a fifth above, the fifth harmonic is two octaves and a major third above. Odd harmonic content sounds hollow, reedy, and square-wave-adjacent. The odd harmonic extreme has a nasal, clarinet-like quality.

The sub oscillator is normalled into the EVEN/ODD output. By default, the sub signal adds to this output at whatever sub octave has been selected. The sub is a square wave. Its presence reinforces the low end and gives the EVEN/ODD output a fullness comparable to a single-oscillator synth with a sub added, which is precisely the SH-101 tonal reference. The sub can be removed from the EVEN/ODD mix by patching a cable into the SUB output jack, which breaks the internal normal.

White noise can be added to the EVEN/ODD output via a secondary function. Holding the TUNE button and turning the TIMBRE knob sets the level of white noise mixed into EVEN/ODD. At minimum there is no noise. At maximum there is a significant noise contribution. This allows the EVEN/ODD output to carry a noise-plus-tone texture without an external noise source or mixer.

---

## Sub Oscillator

The SUB jack outputs a square wave at the sub octave set by the FM INDEX secondary function: one, two, or three octaves below the main oscillator.

When nothing is patched into the SUB jack, the sub signal normalls into the EVEN/ODD output mix. Patching a cable into the SUB jack removes the sub from the EVEN/ODD mix and sends it to the patched destination as a standalone output.

The sub can be used simultaneously with the main oscillator outputs by patching it to a mixer and combining it externally with either or both outputs.

---

## MIDI

### TRS MIDI IN

The New Godspeed accepts TRS MIDI via a 3.5mm jack on the front panel. MIDI A and MIDI B standards are both supported. The standard is selected independently per jack via a small switch on the rear of the module. The two most common TRS MIDI standards differ in which ring-tip-sleeve connections carry which MIDI signals. Check the output standard of the sending device (controller, sequencer, MIDI interface) and set the rear switch to match.

MIDI NOTE messages control pitch. MIDI VELOCITY is not used by the oscillator itself, but passes through to MIDI THRU. MIDI PITCH BEND affects pitch.

The MIDI channel is set via a secondary function: hold the TUNE button and turn the PITCH knob. Fully counterclockwise is OMNI mode (the module responds to all channels). Turning clockwise steps through channels 1 through 16. The setting persists in memory.

### MIDI THRU

A second TRS jack mirrors all incoming MIDI to a THRU output without modification. Daisy-chaining MIDI to additional modules does not require a MIDI splitter. Whatever arrives at MIDI IN exits at MIDI THRU intact.

---

## Why It Excels

The New Godspeed's strength is consolidation without compromise. A full melodic voice typically requires a VCO, a sub oscillator, an FM source, and a waveshaper across multiple modules and significant HP. The New Godspeed delivers all of these simultaneously in six HP.

The autotune system removes the friction of analog oscillator ownership. The thermal drift problem simply does not exist from a workflow perspective. A single TUNE button press at the start of a session and the oscillator is in pitch. This matters most in live contexts where pausing to tune is disruptive, but it improves studio work as well: the oscillator can be trusted without verification.

The two simultaneous outputs with distinct tonal characters allow one VCO to serve two roles in a patch. SINE/FOLD sent to a west-coast style envelope-plus-filter chain and EVEN/ODD sent to a subtractive voice produces two different timbral results from one pitch source. They track identically because they are the same oscillator.

The self-FM capability makes the module a two-operator FM synthesizer with nothing else connected. The internal sine normalled as modulator and the INDEX knob controlling depth is a complete FM instrument in six HP. Adding an external modulator expands the FM range further.

The discrete semitone pitch knob turns the pitch offset function into a musical tool. Interval relationships, transpositions, and chord doublings are dialed in by feel rather than by careful frequency estimation. Combined with LOCK, the PITCH knob becomes a reliable performance transpose tool.

---

## Patch Examples

### 1. Self-FM Bell Voice

```
[New Godspeed]

No patch to FM IN (internal sine normalled as modulator)
FM INDEX: 9 o'clock to noon (moderate depth)
TIMBRE: 10 o'clock on SINE/FOLD

SINE/FOLD [A] → [VCA signal input]
[Envelope GATE output] [G] → [VCA CV input]

[Sequencer pitch] [C] → [New Godspeed 1V/OCT]
[Sequencer gate] [G] → [Envelope gate input]
```

No external FM modulator needed. The internal sine self-modulates the triangle core. The SINE/FOLD output with moderate TIMBRE adds bell-like wavefolder character on top of the FM texture. The result is a percussive pitched voice with metallic overtones: piano-adjacent at low INDEX, more clanging and complex at higher settings. Adjust FM INDEX to taste. Longer envelope release times reveal the full decay of the FM spectrum.

---

### 2. Dual Timbre Chord Voice

```
[New Godspeed]

TIMBRE: 7 o'clock (minimum, SINE/FOLD = pure sine)
EVEN/ODD TIMBRE: inherits same TIMBRE knob

SINE/FOLD [A] → [Filter 1 input]
EVEN/ODD [A] → [Filter 2 input]

[Sequencer pitch] [C] → [New Godspeed 1V/OCT]
```

Both outputs carry the same pitch. SINE/FOLD with TIMBRE at minimum is a clean sine: good for a sub-heavy root voice, for a high harmonic partial in a stack, or for feeding into a pitch-shifted effect. EVEN/ODD with the sub normalled in is warm and full: good for a mid-range mono voice. Running them through separate filters or effects processes creates two distinct timbres from one oscillator and one patch cable from the sequencer.

---

### 3. External FM Carrier

```
[LFO or second VCO audio output] [A] → [New Godspeed FM IN]
FM INDEX: to taste (with CV patched, FM INDEX is now an attenuator)
INDEX CV: unpatched (module ignores INDEX CV when FM IN is patched externally)

SINE/FOLD [A] → [VCA signal input]

[Sequencer pitch] [C] → [New Godspeed 1V/OCT]
```

Patching an external audio-rate signal into FM IN breaks the internal sine normal. The external source becomes the modulator. A second VCO tuned to a harmonic ratio relative to the New Godspeed produces classic two-operator FM textures. A non-harmonic ratio produces inharmonic, bell or metallic tones. The FM INDEX knob attenuates the incoming INDEX CV if one is patched, or serves as the direct depth control if only FM IN is patched.

Note: the INDEX CV jack remains independent of the FM IN jack. Patching FM IN does not affect how INDEX CV behaves.

---

### 4. Sub-Forward Bass Voice with Noise

```
[New Godspeed]

Sub octave: 2 octaves below (set via TUNE + FM INDEX secondary)
White noise in EVEN/ODD: low level (set via TUNE + TIMBRE secondary)
TIMBRE: 10 o'clock (slight odd harmonic shift)
OCTAVE switch: -1 (down one octave)

EVEN/ODD [A] → [VCA signal input]
SUB [A] → left unpatched (sub remains normalled into EVEN/ODD mix)

[Sequencer pitch] [C] → [New Godspeed 1V/OCT]
[Sequencer gate] [G] → [Envelope gate input]
[Envelope output] [C] → [VCA CV input]
```

The EVEN/ODD output with sub normalled in, set two octaves below and OCTAVE switch down one, produces a very low fundamental with square-wave sub reinforcement. A touch of odd harmonic shift from TIMBRE gives the tone some nasal character to cut through a mix without relying purely on volume. A small amount of white noise mixed in adds a slight breath or texture to the attack, useful for distinguishing articulations in a bass line. The VCA shapes the amplitude. A single oscillator, one patch destination, producing a full mono bass voice.

---

## Common Mistakes

**Expecting the PITCH knob to provide continuous fine tuning.** The PITCH knob steps through discrete semitone intervals. There is no position between adjacent semitones. Fine tuning within a semitone is not possible through this knob. If the oscillator needs precise intonation adjustment beyond what autotune provides, use a small CV offset at the 1V/OCT input. The autotune system handles the gross calibration; precise intonation relative to other instruments in a context is a 1V/OCT task.

**Misreading FM INDEX and TIMBRE as direct controls when CV is patched.** Both knobs become attenuators when a CV is present at their respective inputs (INDEX CV and TIMBRE CV). Turning the knob fully counterclockwise when CV is patched results in no effect from the CV at all. The knob does not add to the CV; it scales it. If the expected FM or waveshaping effect disappears after patching a CV, check the knob position.

**Missing the normalled-to-+5V behavior when no CV is patched.** INDEX CV and TIMBRE CV are normalled to +5V internally when nothing is connected. This means the knobs act as full-range direct controls when unpatched. The module is not misbehaving when TIMBRE at maximum produces maximum wavefolder effect without any CV present. This is the intended behavior.

**Patching the SUB jack and expecting the sub to still appear in EVEN/ODD.** The sub oscillator normalling into EVEN/ODD breaks the moment a cable is inserted into the SUB jack. At that point the sub is routed only to the SUB output. If the goal is to use the SUB output externally AND to keep the sub in the EVEN/ODD mix, a mult is required: split the SUB output to both the external destination and back into a mixer with the EVEN/ODD signal.

**Selecting the wrong TRS MIDI standard on the rear switch.** MIDI A and MIDI B differ in their electrical connections. A device set to one standard will not communicate correctly with a module set to the other. The error typically manifests as no MIDI response at all, or as garbled note data. The rear switch is small and easy to overlook. If MIDI is connected and the module does not respond, verify that the rear switch matches the output standard of the sending device before looking elsewhere.

**Forgetting to LOCK before using PITCH knob secondary functions.** Setting the sub octave (TUNE + FM INDEX) and setting the MIDI channel (TUNE + PITCH) both require holding TUNE while turning a knob. The PITCH knob secondary function shifts the MIDI channel but does not shift the pitch directly. However, if the PITCH knob is not LOCKED and the player inadvertently turns it while navigating secondary functions, the pitch offset will change. Engaging LOCK before accessing secondary functions prevents accidental pitch shifts.

**Assuming autotune replaces 1V/OCT tracking calibration.** Autotune snaps the oscillator's current pitch to a reference note. It does not calibrate the 1V/OCT tracking response across the full range. If the 1V/OCT input tracks correctly at the bottom of its range but drifts out of tune at higher octaves (or vice versa), the module may need 1V/OCT tracking calibration, which is a separate procedure described in the Endorphin.es documentation. Autotune and tracking calibration solve different problems.
