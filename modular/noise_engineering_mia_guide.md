---
title: Manis Iteritas Alia
manufacturer: Noise Engineering
primary_role: EVENT_VOICE
secondary_roles: [SOURCE]
historical_context: true
form_factor: eurorack
functions: [drum-voice, fm-oscillator, distortion]
behavior_tags: [percussive, harsh, dirty, dark, noisy, gated, nonlinear]
use_cases: [percussive voice, bass voice, lead voice, noise layer]
hp: 10
memory: none
transport: none
screen: false
hybrid: false
cv: full
---

# Manis Iteritas Alia

**Six-oscillator sawtooth drum synthesizer with modulus wave destruction, pitch-tracking LPF, and sample-rate chorus**

![Noise Engineering Manis Iteritas Alia](https://github.com/Shadoe-42/music/raw/main/modular/images/noise_engineering/manis_iteritas_alia/front_panel.jpg)

## Historical Context

The sawtooth wave holds a specific position in synthesis history that distinguishes it from every other basic waveform. It is the most harmonically dense waveform a single oscillator can produce without additional processing: every harmonic in the overtone series is present simultaneously, with amplitudes falling as the inverse of harmonic number. A sawtooth wave is, in a sense, already a complete spectrum. The Moog modular synthesizer of 1964 was built around this principle: the subtractive synthesis model assumes you begin with a source rich in harmonic content and carve away what you do not want. Oscillators produce sawtooth, square, or pulse waves full of harmonics; filters remove them selectively; amplifiers control level and time. This is the opposite of additive synthesis, which begins with silence and adds harmonic components one at a time. The Basimilus Iteritas approaches percussion from the additive direction: sine waves built up into drum sounds by layering modes. The Manis Iteritas approaches it from the subtractive direction: sawtooth waves in their full harmonic density, reshaped by destruction. The design decision to restrict the oscillators to sawtooth is not a limitation; it is a statement about where the synthesis should begin.

The industrial and aggressive electronic music tradition that the Manis Iteritas inhabits was not built from acoustic instruments or conventional synthesis chains. Throbbing Gristle, operating from 1975 to 1981, constructed sound from circuit-bent consumer electronics, industrial machinery recordings, and purpose-built noise generators, with no interest in the Moog-descended tradition of musical synthesis and explicit interest in what happened when electronic equipment was made to misbehave. SPK, the Australian industrial group, used oscillators and filters in ways that treated the gear as raw material for sonic confrontation rather than a tool for musical production. Einstürzende Neubauten used demolition equipment and metal percussion as primary instruments. What these projects share is the aesthetic premise that sounds which are difficult, harsh, or alien to the ear are not failures of synthesis but the intended result: that the right synthesis architecture is one that generates maximum density and maximum confrontation from whatever signal material is available. A sawtooth wave run through a wavefolder is already doing something in this tradition; a sawtooth wave run through a modulus function that shreds its waveform into discontinuous fragments is doing something further along the same path. The Manis Iteritas was designed from within this tradition rather than as an attempt to reach it from somewhere else.

The instrument exists because of two producers: Matt Lange, a film score composer and modular synthesis practitioner, and Anthony Baldino, who sent Kris Kaiser at Noise Engineering a firmware sketch suggesting what would happen if the Basimilus Iteritas oscillators were restricted to sawtooth waves and the wavefolder was replaced with something harsher. The suggestion became a firmware alternative for the BIA hardware, which Kaiser implemented and which Lange and Baldino helped develop into a complete instrument. The Smash parameter is the core of the departure from the BIA: where the BIA uses an infinifold wavefolder that adds harmonic stages through a continuous and musically smooth process, Smash applies a modulus function that divides the waveform into repeating fragments. A modulus operation on an audio signal does not fold it; it resets it. The character is harsher, less predictable, and less controllable than folding, which is exactly why it was chosen. Baldino also suggested the pitch-tracking low-pass filter that would become the LPF parameter, keeping the filter tonally anchored to the oscillator pitch as pitch changes during envelope sweeps. Profundity, the sample-rate chorus that adds out-of-phase oscillators modulated by a random sample rate offset, came from the same design session. Patrik Andersson later suggested the free-running envelope mode, which allows the oscillators to sustain indefinitely until a trigger resets the phase, converting the module from a trigger-dependent percussion synthesizer into a sustained drone source within the same parameter space.

The Manis Iteritas ran for several years on its original hardware platform before that processor was discontinued. Noise Engineering's response was the Alia platform: a new hardware foundation designed to host the full library of NE digital modules as interchangeable firmware. The Alia version of the Manis Iteritas, which is the current instrument, is functionally identical to the original with one addition: Env Out, a dedicated envelope output that makes the instrument's internal AD envelope available as a CV source for external modules. The Alia platform also adds firmware swapping via micro USB, so the hardware that runs Manis Iteritas can be reflashed to run any other Alia-compatible instrument without physical modification. Autocalibration runs on each power-up when nothing is patched into the Pitch CV input; the module tunes its internal pitch reference to the power supply, which accounts for minor rail voltage variations between cases and ensures consistent pitch tracking. Noise Engineering has also partnered with Save Pangolins, the conservation organization, in connection with the module: the word *manis* is the genus name for the pangolin, and the module name carries the connection.

---

## Quick Start

The Noise Engineering Manis Iteritas Alia is a six-oscillator sawtooth-based drum synthesizer with three modes and a set of wave-destruction parameters designed to produce industrial, aggressive, and confrontational percussion and bass voices. All synthesis begins with sawtooth oscillators; the parameters shape, destroy, and filter that harmonic density into a wide range of percussive and tonal sounds. Like the BIA, the MIA requires a trigger to produce sound in its default state; the envelope must be enabled by turning it clockwise from fully left.

1. Patch a trigger from Hermod+ or a clock into the Trig input.
2. Patch the Out jack into a mixer channel.
3. Set the Skin/Liquid/Metal switch to Skin.
4. Set the Bass/Alto/Treble switch to Bass.
5. Set all knobs to center, except: set Env (Decay) to 10 o'clock and LPF fully clockwise (disabled).
6. Send a trigger. You should hear a short, punchy, sawtooth-based kick-like sound.
7. Press the Hit button to trigger manually at any time.
8. Turn Smash slowly clockwise and listen to the waveform fragment into harsher, more harmonically chaotic territory.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 10 HP |
| Depth | 25 mm ⚠️ |
| Power | 100 mA +12V ⚠️ / 15 mA -12V ⚠️ / 0 mA +5V |

The manufacturer manual states a depth of 1.5 inches (~38 mm). The user-measured value of 25 mm differs from this; both are flagged until hardware verification resolves the discrepancy. The power values provided above differ slightly from the manual (105 mA +12V / 10 mA -12V); both sets of values are flagged pending verification.

---

## Essential Parameters

**Pitch.** Adjusts the fundamental oscillator frequency with 1V/octave tracking. The pitch encoder operates in fine mode by default, advancing in sub-perceptible steps; pressing the encoder while turning switches to coarse mode, advancing in semitone steps. This dual-mode behavior is useful for precise tuning in melodic applications and for broad register changes in performance. The Pitch CV input accepts -2V to +5V on the Alia platform; patching nothing into this input during power-up allows the autocalibration routine to complete successfully, which should be the default startup practice.

**Saw Mod.** Applies the formula Frac((2*s+1)*x) to the oscillator waveform, where s is the Saw Mod amount and x is the oscillator output. The result resembles pulse-width modulation or sync modulation in its audible character without being either: the modulus operation on the formula produces a waveform that narrows and shifts its effective duty cycle as Saw Mod increases, adding buzzing and aliasing character to the sawtooth base. Fully counterclockwise, Saw Mod has no effect and the oscillators produce pure sawtooth. Clockwise, the waveform becomes progressively narrower and more complex. In Metal mode, Saw Mod modulates the oscillator phase relationships rather than the waveform directly, producing a different character. CV input spans 0V to +5V; the knob offsets the CV.

**LPF.** A pitch-tracking low-pass filter consisting of two cascaded non-resonant 2-pole stages. Fully counterclockwise produces maximum low-pass attenuation: a very dark, heavily filtered tone. Fully clockwise disables the filter entirely, letting the full sawtooth spectrum through. The filter tracks the oscillator pitch, so as pitch changes (including during Liquid mode's internal pitch envelope sweep), the filter cutoff moves proportionally, maintaining a consistent spectral character relative to the fundamental regardless of the note played. The filter does not self-oscillate and does not have a resonance control; it is a tonal shaping tool rather than a featured filter voice. CV input into LPF accepts 0V to +5V and offsets the knob position.

**Env / Decay.** Controls the Manis Iteritas Alia's internal AD envelope, which governs oscillator amplitude. Fully counterclockwise produces the shortest possible envelope: an extremely short pop. Turning clockwise extends the decay time progressively; the attack stage begins to lengthen at approximately 2 o'clock. Fully clockwise, the envelope enters free-running mode: the oscillators sustain indefinitely, cycling through their waveforms without decaying. In free-running mode, a trigger input hard-resets the oscillator phase to the beginning of the waveform without triggering a new envelope; the oscillators continue sounding until something external gates the output, making the MIA behave as a continuous drone source with phase-resettable pitch. The Env Out jack on the Alia outputs 0V to +5V following the envelope shape, available as a CV source to external modules for the duration of each note event.

**Profundity.** Applies a chorus effect by adding additional oscillators offset in phase and modulated by a randomized sample rate variation. This produces a detuned, out-of-phase oscillator layer that thickens the fundamental and adds the instability characteristic of chorus or ensemble effects. Fully counterclockwise, Profundity is absent. Clockwise, the chorus depth and the number of additional oscillators increases, widening the sound from a single coherent sawtooth cluster into a diffuse, wavering mass. At extreme settings, Profundity contributes to the noise floor in a way that blurs pitch definition. The CV input for Profundity is labeled "Deep" on the front panel; there is no jack labeled "Profundity." The Deep jack accepts 0V to +5V and offsets the knob position.

**Smash.** Applies a modulus function to the waveform after the oscillators and Saw Mod stage. A modulus operation divides the waveform value by a threshold and takes the remainder: when the waveform exceeds the Smash threshold, it resets to zero and climbs again. This is not wave folding, which mirrors a waveform at its threshold; it is wave destruction, which truncates the waveform and restarts it. The sonic result is harsher, more aliased, and less predictable than folding. Low Smash settings add a gritty harmonic edge; high Smash settings fragment the waveform into rapidly resetting segments that produce dense noise content and metallic brightness. The CV input for Smash accepts 0V to +5V and offsets the knob position. The Bash parameter routes the internal envelope to Smash, Profundity, and LPF simultaneously, so Smash is also modulated by Bash when Bash is turned from center.

**Bash.** An attenuverter that routes the internal AD envelope to three destinations simultaneously: Smash, Profundity, and LPF. At 12 o'clock, Bash is off and has no effect on any of the three. Turning clockwise applies positive envelope modulation: each trigger pushes Smash, Profundity, and LPF in the positive direction for the duration of the envelope, which means each trigger simultaneously increases wave destruction, increases chorus depth, and opens the filter. Turning counterclockwise applies negative modulation: each trigger reduces Smash, Profundity, and opens the filter less, or the inverse of those relationships depending on starting positions. Bash is the primary per-note dynamics control in the MIA's architecture; without Bash, Smash and Profundity are static timbral settings, and with Bash they become the transient character of each note event.

**Skin / Liquid / Metal Switch.** Selects the synthesis mode. Skin places all six sawtooth oscillators in an additive arrangement where each oscillator decays independently: a percussion voice with no internal pitch movement. Liquid adds the internal pitch envelope from the BIA's Liquid mode, sweeping the fundamental downward during the decay for a kick-drum pitch-drop character, now applied to sawtooth oscillators rather than the BIA's waveform-variable oscillators. Metal reconfigures the six oscillators into two sets of three, each set with sequential phase modulation between the oscillators; the two resulting signals sum together to produce a waveform that blends between sawtooth and square depending on Saw Mod and phase settings. Metal mode on the MIA is a phase modulation architecture distinct from the BIA's FM Metal mode. The switch position can be CV-controlled via the S/L/M input.

**Bass / Alto / Treble Switch.** Sets the pitch range. Bass places the fundamental in the low percussion register. Alto raises it two octaves. Treble raises it four octaves from Bass, bringing the MIA into melodic territory with usable 1V/oct pitch tracking. The switch position can be CV-controlled via the B/A/T input.

**Trigger and Hit.** The Trig input fires the drum voice on a rising edge; the MIA's trigger threshold is approximately 1.8V, which is lower than most modules' standard 3-5V gate output. This means any gate or trigger signal in the rack will reliably fire the MIA. The Hit button fires the voice manually. In free-running mode, Trig resets the oscillator phase rather than triggering a new envelope cycle. Env Out follows the internal envelope shape at 0V to +5V; the audio output can reach approximately 14V peak-to-peak at high amplitude settings.

---

## Why This Instrument Excels

The sawtooth restriction is the fundamental reason the Manis Iteritas Alia occupies a different tonal territory than the Basimilus Iteritas despite sharing the same three-mode architecture and the same trigger-dependent synthesis model. Starting from the densest harmonic content a simple waveform provides and then subjecting that content to modulus destruction, Saw Mod phase shaping, and sample-rate chorus produces sounds that exist at the outer edge of recognizable percussion synthesis. A low Smash setting in Skin mode produces a plausible industrial kick, gritty and dense; a high Smash setting in Metal mode with maximum Bash and Profundity produces something that sounds closer to an electrical failure than a drum hit. Both exist within the same parameter space, and the path between them is continuous. No other module in the rack covers this specific tonal territory with this specific approach: the BIA's folding is musical, the MIA's Smash is confrontational, and that distinction is the MIA's reason for existing.

Bash is the most architecturally distinctive parameter in the MIA's design, and it is the one that most clearly reflects the industrial synthesis tradition the module comes from. Rather than providing separate CV inputs for Smash, Profundity, and LPF and leaving the player to build their own modulation routing, Bash assumes that all three of these parameters belong together as the transient character of a note event: the wave destruction, the chorus depth, and the filter opening are all part of the same attack gesture. When Bash is turned clockwise, each trigger produces a sound that is harsher, thicker, and brighter at the moment of attack than the sustained tail; when Bash is turned counterclockwise, the attack is cleaner and the tail is more aggressively treated. This built-in transient shaping produces the kind of percussive articulation that usually requires an envelope generator, an attenuverter, and multiple patch cables, collapsed into a single knob. The musical consequence is that the MIA can sound like a complete percussion voice with pronounced attack character without any external modulation whatsoever.

The free-running envelope mode, accessible at the fully clockwise position of the Env knob, converts the MIA into a sustained sound source without changing any other parameter. In free-running mode the oscillators do not decay and the module produces continuous audio output; patching a trigger or gate into Trig resets the oscillator phase without re-triggering the envelope, which allows rhythm to be imposed on a continuous sound through phase resets rather than amplitude gates. This behavior is distinct from anything a conventional VCO offers: the oscillators do not start and stop, they cycle continuously, and the trigger defines the moment of phase coherence rather than the moment of amplitude onset. Running the free-running MIA through the SSF SSG Stereo Field's EXCITE input then creates a two-stage system where the SSG's LPG controls amplitude while the MIA provides the sustained raw material, separating synthesis from dynamics in a way that is not possible when the envelope is internal to both modules.

Profundity occupies an unusual position in a drum synthesizer. Chorus is typically associated with sustained melodic synthesis, where the slight detuning and phase offset of the chorus oscillators produces spatial width and warmth. Applied to a sawtooth-based percussion synthesizer with a short envelope, Profundity adds a roughness and instability to the attack transient that has no clean analog in acoustic percussion: the oscillators are slightly out of phase and slightly detuned from the moment of attack, which diffuses the initial transient into something wider and less focused than a single coherent oscillator cluster would produce. At low Profundity settings this adds a subtle texture to the attack; at high settings it pushes the sound toward a cloud of related frequencies rather than a single pitched hit. In free-running mode with high Profundity, the MIA sounds more like a cluster of slightly detuned drone oscillators than a drum synthesizer, which is a different instrument role entirely and one that is available without any module changes or additional patching.

---

## Patches

### Patch 1: Industrial Kick in Skin Mode

Noise Engineering Manis Iteritas Alia in Skin mode, Bass range, configured as a harsh sawtooth kick with moderate Smash and Bash shaping the transient.

```
[Hermod+ Gate Out] ──────────[G]──────▶ [MIA Trig In]

[MIA Out] ───────────────────[A]──────▶ [MixUp CH1]

                                         Mode: Skin
                                         Range: Bass
                                         Pitch: 9 o'clock (low)
                                         Saw Mod: fully CCW (off)
                                         LPF: 3 o'clock (slight cut)
                                         Env: 10 o'clock (short decay)
                                         Profundity: 8 o'clock (subtle)
                                         Smash: 9 o'clock (light)
                                         Bash: 2 o'clock (positive, moderate)
```

**Setup:** Patch Hermod+'s gate into Trig and MIA Out into a mixer. Set Skin mode and Bass range. Saw Mod fully counterclockwise leaves the oscillators as pure sawtooth. LPF slightly counterclockwise from full clockwise (which would disable it) adds a mild high-frequency cut. Bash at 2 o'clock routes the envelope positively to Smash, Profundity, and LPF, meaning each trigger pushes wave destruction and chorus depth upward at the attack moment and allows them to settle as the envelope decays.

**Controls:** Adjust Pitch to set the fundamental; small movements at the low end of Bass range produce large perceived pitch changes. Turn Smash slowly clockwise and hear the sawtooth waveform fragment: each increment adds more harmonic irregularity to the body of the sound. The key relationship is between Smash and Bash: Smash sets the resting amount of wave destruction, and Bash determines how much more destruction is added at the attack. With Smash at 9 o'clock and Bash at 2 o'clock, the attack is harder and more aggressive than the tail. Move Bash counterclockwise toward 12 o'clock and the transient character flattens; move it further counterclockwise and the tail becomes harsher than the attack, which is a less typical but usable dynamic inversion. Extend the Env decay to lengthen the tail; the Bash routing extends proportionally.

**Result:** A short industrial kick with a defined, Smash-aggravated attack and a decaying tail, producing a harsher and more abrasive character than conventional analog or additive drum synthesis. The Bash transient shaping is the primary voice of the instrument at this setting.

---

### Patch 2: Bash Envelope as Timbral Gate

MIA in Skin mode, Bass range, with Bash set negative so each trigger briefly cleans the sound before letting it return to a heavily Smashed resting state — inverting the typical transient-bright, tail-dark dynamic.

```
[Hermod+ Gate Out] ──────────[G]──────▶ [MIA Trig In]
[MIA Env Out] ───────────────[C]──────▶ [SSF SSG Stereo Field EXCITE]

[MIA Out] ───────────────────[A]──────▶ [SSF SSG Stereo Field IN-L]
[SSG Stereo Field OUT-L] ────[A]──────▶ [MixUp CH1]

                                         Mode: Skin
                                         Range: Bass
                                         Pitch: 8 o'clock
                                         Saw Mod: 11 o'clock
                                         LPF: fully CW (disabled)
                                         Env: 11 o'clock
                                         Profundity: 2 o'clock (strong)
                                         Smash: 3 o'clock (heavy)
                                         Bash: 10 o'clock (negative)
                                         SSG FREQ: 10 o'clock
```

**Setup:** Set Smash heavy (3 o'clock) so the resting state is a strongly wave-destroyed, harmonically dense sawtooth. Set Profundity high (2 o'clock) for a thick, chorused resting state. Set Bash to 10 o'clock: the negative envelope routing means each trigger reduces Smash and Profundity temporarily, pulling the sound toward a cleaner, more coherent sawtooth for the duration of the envelope before the parameters return to their heavily-treated resting positions. Route MIA Env Out into the SSF SSG Stereo Field EXCITE input and pass MIA Out through SSG IN-L, with SSG Out-L to the mixer; the SSG acts as an LPG, providing amplitude shaping from the MIA's own envelope signal.

**Controls:** The sound in this patch is continuously active at full Smash and high Profundity, meaning a dense, fragmented, diffuse audio output. Each trigger briefly snaps the sound toward a cleaner sawtooth and simultaneously opens the SSG LPG amplitude, producing a moment of relative clarity at the attack point before the resting treatment returns as the envelope decays. Adjust SSG FREQ to set how much of the MIA's spectrum the LPG opens during each trigger; lower FREQ values allow only the low frequencies through, higher values allow more brightness. Adjust Bash counterclockwise further toward 9 o'clock to make the cleaning effect more extreme, or back toward 12 o'clock to reduce it. Extend Env to lengthen both the LPG's open window and the duration of the Bash-modulated parameter reduction.

**Result:** A percussion voice whose attack is its cleanest moment and whose tail returns to a heavy, treated resting state; the opposite of a conventional percussive synthesis architecture. The MIA's Env Out drives the SSG's LPG from the same envelope, so both the timbral behavior and the amplitude shaping are synchronized to each trigger without additional patching.

---

### Patch 3: Free-Running Drone with Phase-Reset Rhythm

MIA in Metal mode, Alto range, with Env fully clockwise for free-running oscillators. Pons Asinorum modulates Smash and Profundity; Hermod+ gate resets phase rhythmically without re-triggering an envelope.

```
[Hermod+ Gate Out] ──────────[G]──────▶ [MIA Trig In]
[Pons Asinorum Out 1] ───────[C]──────▶ [MIA Smash CV In]
[Pons Asinorum Out 2] ───────[C]──────▶ [MIA Deep (Profundity) CV In]
[Pons Asinorum Out 3] ───────[C]──────▶ [MIA Saw Mod CV In]
[MIA Env Out] ───────────────[C]──────▶ [Pons Asinorum Trigger CH1]

[MIA Out] ───────────────────[A]──────▶ [Qu-Bit Aurora In L]
[Aurora Out L] ──────────────[A]──────▶ [MixUp CH1 L]
[Aurora Out R] ──────────────[A]──────▶ [MixUp CH1 R]

                                         Mode: Metal
                                         Range: Alto
                                         Pitch: center
                                         Saw Mod knob: center (PA offsets)
                                         LPF: fully CW (disabled)
                                         Env: fully CW (free-running)
                                         Profundity knob: center
                                         Smash knob: 10 o'clock
                                         Bash: 12 o'clock (off)
                                         PA CH1: LFO, up/down, 9 seconds
                                         PA CH2: LFO, up/down, 13 seconds
                                         PA CH3: LFO, ramp up, 7 seconds
                                         Aurora: moderate reverb, high Warp
```

**Setup:** Set Env fully clockwise to engage free-running mode; the MIA now oscillates continuously without triggering. Metal mode in free-running produces a continuous phase-modulated sawtooth cluster. Hermod+ gate signals no longer produce a new envelope onset; they reset the oscillator phase to the beginning of the waveform cycle. Set three Pons Asinorum channels to LFO mode at coprime cycle lengths and route them to Smash, Deep (Profundity), and Saw Mod CV inputs respectively. Route MIA Env Out into the PA trigger input for Ch1; in free-running mode the Env Out is a constant high CV signal rather than an envelope, which holds the PA in a triggered state and keeps its first channel cycling.

**Controls:** The Hermod+ gate rhythm determines when the oscillator phase resets, which produces a rhythmic artifact in the continuous output as each reset creates a momentary phase discontinuity: a small click or transient at the phase-reset point. At high Hermod+ clock rates, these phase resets create rhythm within the drone. At low rates, they produce widely spaced timbral interruptions. The three PA LFOs rotate Smash, Profundity, and Saw Mod through their ranges at different speeds; because their cycle lengths are coprime, the three-way modulation pattern does not repeat in any practical musical timeframe. Aurora's reverb captures each moment of the MIA's shifting timbral state and extends it into a long tail; the high Warp setting adds spectral processing that transforms the MIA's harshness into a more diffuse ambience. Returning Env slightly counterclockwise from fully clockwise exits free-running and allows the envelope to decay; this restores the percussive character while all other patch elements remain active.

**Result:** A continuous metallic drone whose spectral character evolves through Smash and Profundity modulation while rhythmic phase resets impose structure on the continuity. The patch demonstrates the MIA's capacity as a sustained drone source, a capability that does not require any additional modules, only a different Env position.

---

### Patch 4: Industrial Bass Voice with Pitch Sequence

MIA in Liquid mode, Bass range, receiving V/oct pitch from Hermod+ for a sequenced industrial bass line; Zadar provides per-note Bash CV for per-note transient character variation; SSF SSG Stereo Field provides LPG amplitude shaping.

```
[Hermod+ Gate Out] ──────────[G]──────▶ [MIA Trig In]
[Hermod+ Pitch CV Out] ──────[C]──────▶ [MIA Pitch CV In]
[Zadar CH1 Env Out] ─────────[C]──────▶ [MIA Bash CV In]
[Hermod+ Gate Out] ──────────[G]──────▶ [Zadar Trigger CH1]
[MIA Env Out] ───────────────[C]──────▶ [SSF SSG Stereo Field EXCITE]
[Pons Asinorum Out 1] ───────[C]──────▶ [MIA LPF CV In]

[MIA Out] ───────────────────[A]──────▶ [SSF SSG Stereo Field IN-L]
[SSG Stereo Field OUT-L] ────[A]──────▶ [MixUp CH2]

                                         Mode: Liquid
                                         Range: Bass
                                         Pitch knob: center
                                         Saw Mod: 10 o'clock
                                         LPF knob: 2 o'clock (PA modulates)
                                         Env: 11 o'clock
                                         Profundity: 9 o'clock (light)
                                         Smash: 10 o'clock
                                         Bash knob: 12 o'clock (Zadar drives it)
                                         SSG FREQ: 11 o'clock
                                         PA CH1: LFO, up/down, 15 seconds
                                         Zadar CH1: sharp attack, medium decay
```

**Setup:** Set Liquid mode and Bass range. Patch Hermod+'s pitch CV and gate to MIA Pitch CV and Trig for a bassline sequence. Bash knob at 12 o'clock disables the direct envelope routing; Zadar's envelope into Bash CV drives it externally, allowing per-note Bash intensity from the Zadar envelope shape. Route MIA Env Out to the SSF SSG Stereo Field EXCITE for LPG amplitude control, then pass MIA audio through SSG IN-L and take SSG Out-L to the mixer. The SSG provides the amplitude envelope from MIA's own envelope signal. Pons Asinorum's first channel in slow LFO mode modulates LPF over a 15-second cycle, slowly varying filter character across the phrase.

**Controls:** The Hermod+ sequence determines pitch; in Liquid mode, each note begins at the sequenced pitch and sweeps downward during the decay, so lower notes in the sequence produce heavier pitch drops and higher notes produce tighter, more tonal ones. Zadar's envelope controls how much positive Bash intensity arrives at each trigger: a short Zadar decay means the Bash modulation peaks quickly and releases fast, producing a sharp transient crunch from Smash and Profundity; a longer Zadar decay sustains the Bash modulation through more of the note event, which keeps the Smash character elevated for the full note duration. Adjust the Zadar envelope shape to control this balance. The Pons Asinorum LPF modulation slowly opens and closes the filter over 15 seconds, shifting the bass voice from darker to brighter and back across multiple phrase repetitions without any manual intervention. Adjust SSG FREQ to set the overall tonal balance of the voice in the mix.

**Result:** A sequenced industrial bass voice with per-note transient intensity from Zadar's Bash CV, Liquid mode pitch sweep for each note, LPF variation from Pons Asinorum for slow tonal drift, and SSG LPG amplitude shaping from MIA's own envelope signal. The combination produces a bass voice with the harmonic aggression of the MIA and the dynamics shaping of an LPG without the MIA requiring any additional amplitude envelope generators.

---

## Common Mistakes

### "Smash sounds broken — it clicks and stutters at random"

The modulus function that Smash applies resets the waveform to zero when it exceeds the Smash threshold; this produces discontinuities in the waveform at the reset points, which are audible as clicks, crackle, and aliasing artifacts. This is not a malfunction. The discontinuity is the intended mechanism: the MIA is designed for this territory. Smash is not a wavefolder. Wavefolders mirror the signal at the threshold, which is a continuous operation; Smash applies modulus, which truncates it, which produces discontinuities by design.

**Fix:** If the discontinuity character is not desired, reduce Smash toward counterclockwise or leave it fully counterclockwise. If the character is present but excessive, lower the Env decay time so less of the Smash-treated signal is audible. Smash is a harmonic destruction tool; use it if the goal is harsh, fragmented sound, and avoid it if the goal is a clean, predictable waveform.

---

### "The 'Deep' jack is not doing anything — I expected Profundity CV"

The Profundity CV input is labeled "Deep" on the front panel. The word "Profundity" does not appear on the panel itself; it appears only in the manual and in the parameter name. Patching into a jack labeled anything else while expecting Profundity CV modulation will have no effect.

**Fix:** Route Profundity CV into the jack labeled "Deep" on the panel. It is in the CV row, positioned according to its layout in the Alia's jack assignment. After patching, turn the Profundity knob to center and use the incoming CV to modulate above and below that center position.

---

### "Bash seems to have no effect even though I have it turned up"

Bash routes the internal AD envelope to Smash, Profundity, and LPF. If the Env knob is fully clockwise (free-running mode), the envelope is not triggered by incoming gates; the oscillators sustain continuously without envelope activity. Bash depends on the envelope cycling to produce modulation. In free-running mode, there is no envelope event for Bash to route, so Bash produces no change per trigger.

**Fix:** To use Bash as a per-note transient shaping tool, Env must be in a position that produces an envelope cycle (any position counterclockwise of fully clockwise). Set Env to produce a decay of the desired length and confirm that each trigger produces a clear amplitude onset before adjusting Bash. Alternatively, an external CV source patched into Bash CV (the attenuverter CV input) can drive Bash externally regardless of the Env position.

---

### "Free-running mode is confusing — the module just drones without stopping"

In free-running mode (Env fully clockwise), the oscillators do not decay and there is no internal amplitude control. The MIA produces audio at a constant amplitude determined by the synthesis parameters. Patching a trigger or gate into Trig resets the oscillator phase but does not reduce amplitude; the output continues at the same level before and after the trigger. This is not a malfunction. Free-running mode is intentionally a drone architecture.

**Fix:** To control amplitude in free-running mode, route MIA Out through an external VCA or LPG (such as the SSF SSG Stereo Field) and provide an external envelope or gate to control the amplitude stage. Alternatively, use MIA Env Out (which outputs a constant high voltage in free-running mode) to hold another module in a sustained state. If the intent is a triggered decay rather than a drone, return Env counterclockwise until the decay behavior is audible.

---

### "In Metal mode, the MIA sounds nothing like the BIA's Metal mode"

The MIA's Metal mode uses phase modulation between two sets of three oscillators. The BIA's Metal mode uses frequency modulation where each operator modulates the next in a chain. These are different synthesis architectures that produce different results despite both being labeled "Metal." The MIA's Metal mode is not interchangeable with the BIA's, and expecting identical tonal territory leads to confusion when the results differ.

**Fix:** Treat the MIA Metal mode as its own synthesis architecture rather than a variant of the BIA Metal mode. The MIA Metal mode produces phase-modulated sawtooth clusters; the BIA Metal mode produces FM inharmonic spectra. Both produce metallic and complex tones but by different mechanisms. The MIA Metal mode responds strongly to Saw Mod and Smash; the BIA Metal mode responds strongly to Spread. Explore the MIA Metal mode on its own terms and map its parameter responses independently.

---

### "The MIA triggers unexpectedly from other signals in the patch"

The MIA's trigger threshold is approximately 1.8V, which is lower than most modules' standard threshold of 3-5V. In a dense patch, audio-rate or CV signals that cross 1.8V on a rising edge can trigger the MIA unintentionally. This includes slow LFO peaks, CV buses with common ground, or signals that are not intended as triggers but whose voltage reaches the threshold.

**Fix:** Check all cables feeding into the Trig input and ensure only the intended trigger signal is patched there. If unintended triggering persists, examine adjacent patch cables for capacitive coupling. Using a dedicated trigger or gate signal from Hermod+ rather than derived trigger signals from other modules is the most reliable way to ensure intentional-only triggering.

---

## Advanced Learning Path

Begin by learning the Smash parameter's three distinct tonal zones through slow exploration from fully counterclockwise to fully clockwise. In Skin mode, Bass range, with a steady trigger and everything else at center, move Smash in small increments and pause at each position to listen. At low settings the sawtooth character dominates with a mild edge. Through the midrange the fragmentation begins, with clicks and harmonic irregularities entering. At high settings the waveform is so frequently reset that the output approaches noise. Map where each zone begins and ends by ear; these three zones are the MIA's primary tonal vocabulary and knowing their exact positions enables intentional parameter choices rather than searching.

Explore Bash in both directions from center across its full range, with Smash, Profundity, and LPF all set to different mid-range positions. Turn Bash fully clockwise and listen: each trigger produces maximum Smash, Profundity, and filter opening at the attack and decays toward the resting knob positions. Then turn Bash fully counterclockwise: each trigger produces minimum of all three, meaning the resting state is more aggressively treated than the attack. The two extreme Bash directions produce opposite transient characters; the midpoint of each produces a different balance. Understanding this full bidirectional range is essential for using Bash as a deliberate transient shaping tool rather than an enhancement knob.

Practice the free-running mode transition without stopping playback. With a trigger sequence running and the MIA in Skin mode with a normal Env decay, slowly turn Env clockwise toward the free-running threshold. Before fully clockwise, the decay becomes very long; at fully clockwise, the decay disappears and the oscillators sustain. Return counterclockwise to restore the decay. The transition between percussive and drone is a continuous parameter sweep, not a mode switch, and using it in performance requires knowing precisely where the free-running threshold sits on your specific unit. Locate that threshold point and practice controlling it smoothly.

Patch the MIA Env Out to a destination that exposes the envelope shape directly: into a Pons Asinorum trigger input, or into an SSF SSG Stereo Field EXCITE input, or into a VCA CV input. Listen to how the envelope's duration tracks the Env knob and how the shape changes across its range. The Alia addition of Env Out makes the MIA a two-output module: audio from Out and CV from Env Out. Developing fluency with Env Out as a patch component, rather than treating the MIA as a single-output module, expands the module's utility significantly without additional patching complexity.

Configure the autocalibration routine deliberately. Power down the case. Disconnect any cable from the MIA Pitch CV input. Power up and wait for the module to complete its startup sequence. Reconnect the Pitch CV source. Then play a two-octave scale from a Hermod+ sequence and verify that the MIA tracks pitch accurately across the range. Compare this to the same sequence after a session where the Pitch CV was connected at power-up. If the pitch tracking has drifted, the autocalibration was incomplete; unplugging and repowering with nothing in Pitch CV corrects it. Making this part of the session startup routine eliminates pitch tracking drift as a variable.

Route all three Smash, Profundity, and LPF CV inputs simultaneously from different Pons Asinorum channels and map how the three parameters interact. Smash adds harmonic density; Profundity adds spatial diffusion and out-of-phase oscillator thickening; LPF removes upper harmonic content. With all three moving at different rates, the interaction produces a continuously evolving tonal character where the wave destruction, the chorus width, and the filter position are never simultaneously at the same relative position. This three-dimensional modulation space is the MIA's equivalent of the BIA's Spread/Fold/Morph CV space; both define the range of timbral variation available without changing the synthesis mode or the pitch sequence.

Use Liquid mode in Alto or Treble range as a melodic instrument with pitch-drop articulation on every note. Set a chromatic sequence on Hermod+ spanning a fourth or fifth in the mid-register. In Liquid mode, each note in the sequence begins at the sequenced pitch and sweeps downward; higher notes in the sequence produce a steeper perceived drop because the starting pitch is higher. Use Smash at a moderate setting and LPF at 2 o'clock for a controlled but aggressive tonal character. This application turns the MIA into a melodic lead voice with a built-in descending pitch articulation on every note event, producing an industrial lead tone that requires no additional CV routing to generate its characteristic motion.

For a complete two-module system with the Pons Asinorum, assign all four PA channels as an envelope/LFO bus for the MIA: CH1 envelope into Bash CV for per-trigger intensity, CH2 LFO into Smash CV for slow wave destruction evolution, CH3 LFO into Deep (Profundity) CV for chorus sweep, and CH4 LFO into LPF CV for filter movement. Set the PA trigger from the same gate as the MIA Trig input so CH1's envelope fires in sync with each trigger. The result is a self-contained percussion voice where every primary timbral parameter is modulated from a single 6HP companion module, producing variation across pitch, harmonic content, chorus, filter, and transient character without any additional modules.

---

## Pairs Well With

**Noise Engineering Pons Asinorum** is the natural modulation partner for the MIA within the rack, sharing the same manufacturer's control philosophy (knobs offset CV rather than attenuate it) and a trigger threshold close enough for direct connection. The PA's four channels handle the MIA's primary CV-able parameters without redundancy: Bash CV for per-note transient intensity, Smash CV for wave destruction sweep, Deep (Profundity) CV for chorus depth evolution, and LPF CV for tonal brightness shift. Because the PA can run channels in either envelope or LFO mode, the same four-output module can provide triggered transient shaping for Bash while simultaneously providing slow LFO motion on Smash and Profundity, creating a modulation bus that varies both per-note and across longer time scales from a single 6HP module.

**SSF SSG Stereo Field** addresses the one thing the MIA does not provide internally when used in non-free-running mode: a second amplitude shaping stage. Routing MIA Out through the SSG's low-pass gate and driving EXCITE with MIA Env Out creates a two-stage dynamics chain where the MIA's internal envelope shapes the voice and the SSG's LPG adds the coupled filter-amplitude bloom of vactrol response on top of it. This is particularly useful in Liquid mode, where the internal pitch sweep already provides descent character and the SSG's LPG adds a physical warmth to the amplitude decay that softens the MIA's digital harshness. The combination is appropriate for contexts where the MIA needs to sit in a mix rather than dominate it, adding organic dynamics without sacrificing the instrument's core tonal character.

**Bela Gliss** in Notes Sequencer mode provides pitch and gate sequences to the MIA in Liquid or Skin mode for melodic applications. The Gliss's differentiated trigger voltage (+10V on the first step of a phrase, standard voltage on subsequent steps) sent to both Trig and Bash CV produces a louder, more aggressively Smashed first note in each phrase; the phrase accent is built into the trigger voltage rather than requiring a separate accent signal, which reduces patching complexity. The Gliss's real-time step muting and step-order manipulation then allows the MIA's pitch and rhythmic content to change during playback without stopping the patch, providing live arrangement capability for the bass or percussion voice without manual knob adjustment on the MIA itself.

**Qu-Bit Nautilus** receives MIA well as a source for reverb processing, particularly in Liquid Bass mode where the pitch-drop of each kick note produces a melodically specific frequency content. Routing MIA through Nautilus at low Resolution settings produces a reverb tail that emphasizes the fundamental of each kick drop and sustains it as a pitched resonance after the MIA's own decay is complete. The combination creates a kick voice with a naturally decaying reverb component that is tuned to the same pitch as the kick drop itself, producing a room-like resonance behavior that is melodically coherent rather than a neutral wash of reverb energy.

**Zadar** extends the MIA's per-note variation by providing independent envelope curves to multiple CV inputs simultaneously. In a patch where Hermod+ provides gate and pitch, Zadar's four channels can drive Bash CV, Smash CV, Profundity CV, and LPF CV each with their own attack and decay shapes. Because Zadar's envelope shapes are configurable independently per channel, the character of each MIA parameter can evolve differently through each note event: Bash might peak immediately and decay fast, while LPF peaks slowly and sustains longer, producing a note event where the transient character and the tonal brightness follow different curves through the same gate window. This per-parameter envelope shaping is the most musically expressive application of the MIA's full CV capability.

**Qu-Bit Aurora** handles the MIA's harsh output well when the goal is to place that harshness in a spatial and spectral context rather than letting it sit dry in the mix. Aurora's FFT-based spectral processing captures the MIA's dense sawtooth content and redistributes it into sustained tails with configurable frequency character. At high Warp settings, Aurora transforms the MIA's industrial kicks into textural events that sustain for several seconds and retain the frequency character of the original hit without the sharp transient. This is effective for industrial ambient music where percussion is meant to blur into texture rather than articulate rhythm, and it is also a practical tool for reducing the perceived harshness of the MIA in a full mix without reducing its Smash setting.
