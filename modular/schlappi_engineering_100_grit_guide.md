---
title: 100 Grit
manufacturer: Schlappi Engineering
primary_role: SHAPER
secondary_roles: [FILTER]
historical_context: true
form_factor: eurorack
functions: [distortion, filter, vca]
behavior_tags: [dirty, harsh, nonlinear, warm, noisy, reactive]
use_cases: [signal destruction, timbral movement and shaping, noise layer, percussive voice processing]
hp: 14
memory: none
transport: none
screen: false
hybrid: false
cv: full
---

# 100 Grit

**Transistor ladder filter, VCA, and dual-path distortion with eight brass touch points and full self-feedback normalization**

![Schlappi Engineering 100 Grit](https://github.com/Shadoe-42/music/raw/main/modular/images/schlappi_engineering/100_grit/front_panel.jpg)

## Historical Context

The transistor ladder filter that sits at the core of the 100 Grit is one of the most documented circuits in electronic music history. Robert Moog designed the four-pole ladder topology in 1964, building on his collaborations with composer Herbert Deutsch and his encounter with Harald Bode's work at the Audio Engineering Society convention the previous year. The filter works by cascading four transistor stages, each contributing a 6dB per octave rolloff, to produce a 24dB per octave slope. What distinguishes the ladder from other filter topologies of the same period is a physical property of the transistors themselves: at high input levels, the transistors begin to saturate, producing a soft-clipping behavior that adds harmonic content to the signal passing through. This saturation is not an error in the design; it is the design. The warmth associated with the ladder filter is the audible signature of transistors being asked to do more than their linear operating range accommodates. The 100 Grit provides significant gain ahead of the filter, which means saturation is available without special patching and is part of the module's default character at any setting above minimal gain.

Electronic distortion as a deliberate aesthetic rather than a circuit defect has a longer history than synthesis. Guitar amplifiers driven beyond their headroom in the early 1950s produced tube saturation that performers noticed as an expressive resource rather than a failure mode; by the early 1960s, guitarists were deliberately blowing out speakers and cutting slits in cones to achieve sustained, harmonically saturated tones. The synthesis community was initially less interested in distortion as a tool — instruments like the Moog modular were designed to minimize noise and nonlinearity in the signal path. The two outputs on the Schlappi Engineering 100 Grit reflect the accommodation of both positions simultaneously: OUT provides the filtered, gain-staged signal that a conventional synthesis architecture expects, and DIST provides the output of a second distortion amplifier that the manual describes as capable of "total sonic obliteration." Both outputs are available at the same time. The design does not require a choice between the two approaches; it offers them as simultaneous perspectives on the same signal.

Circuit bending as a named practice was developed by Reed Ghazala, who discovered in the late 1960s that shorting contacts on battery-powered circuits with his fingers or conductive objects produced tonal changes, instabilities, and sounds that the circuit was never designed to make. Ghazala formalized the practice over decades and published "Circuit Bending: Build Your Own Alien Instruments" in 2005, but the underlying intuition predates him. David Tudor, the American experimental composer and Cage collaborator, was modifying and misusing electronic equipment in performance settings beginning in the 1950s; his Rainforest series used electronic circuits in ways that had no relationship to their intended function. The eight brass touch points on the 100 Grit are a designed implementation of this tradition. Each point connects directly to a sensitive node in the circuit with a current-limiting resistor in series; connecting two points simultaneously with a finger, a cable tip, or a conductive object creates a resistive connection between those nodes whose resistance value is determined by contact pressure, skin conductivity, and contact area. The manual notes that the touch points are positioned so that an output is always adjacent to an input, making any neighboring pair a functional resistive patch connection. The resistance value is never fully repeatable, which is the point.

Eric Schlappi's design logic for the 100 Grit is visible in one feature that distinguishes it from every conventional filter or distortion module: all inputs, when nothing is patched into them, carry an active feedback signal from elsewhere in the circuit. IN 1 receives the DIST 2 comparator output. IN 2 receives the DIST output. FM 1 receives the DIST output into the filter's frequency control. GAIN CV receives POLE 2, the filter's 12dB output node. RES CV receives the DIST output into the resonance control. The default state — the module with no cables — is maximum internal complexity, where every parameter is being modulated by the circuit's own output. Patching a cable into any of these inputs removes that feedback connection and replaces it with whatever signal is on the cable. The module simplifies as patching increases, rather than gaining function. This inversion of the conventional modular assumption, where an empty input is neutral and a patched one is active, is the entire design philosophy of the 100 Grit in a single architectural decision.

---

## Quick Start

The Schlappi Engineering 100 Grit is a transistor ladder filter with an OTA VCA and two distortion amplifier stages, with eight brass touch points connected directly to circuit nodes and a full feedback normalization system on every input. It requires GAIN to produce any output — with GAIN at zero, no signal passes regardless of any other setting.

1. Patch audio into IN 1.
2. Patch the DIST output into a mixer channel.
3. Set IN 1 to 75%, FREQUENCY to 75%, GAIN to 75%, all other knobs fully counterclockwise.
4. You should hear your source signal with significant distortion character.
5. Increase RES slowly and hear the filter resonance build; at higher settings it will screech and howl.
6. Increase GAIN further and hear distortion increase. At 100%, clip and fragmentation dominate.
7. Flip the x100 switch to ON for extreme gain and maximum distortion density.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 14 HP |
| Depth | 25 mm |
| Power | 55 mA +12V / 70 mA -12V / 0 mA +5V |

The -12V draw exceeds the +12V draw, which is unusual and worth accounting for in rack power planning. The OTA VCA circuit draws more from the negative rail than the positive. Confirm available headroom on the -12V bus before installing.

---

## Essential Parameters

The 100 Grit's inputs behave differently from any other module in this rack: when no cable is patched into an input, that input is not silent — it carries a feedback signal from elsewhere in the circuit. These normalizations are indicated on the panel with parentheses and described in detail below. Any normalization you do not want contributing to the sound must be turned fully counterclockwise on its associated knob; there is no silent default.

**Frequency.** The large central knob controls the cutoff frequency of the four-pole transistor ladder low-pass filter. Fully counterclockwise, the filter cuts off all audio passing through it; turning clockwise raises the cutoff and allows more of the spectrum through. The filter is 24dB per octave and has a characteristic warmth from transistor saturation in the signal path. FREQUENCY interacts with RES: at high resonance settings, the filter's response becomes very peaked at the cutoff frequency, and the exact FREQUENCY position determines the pitch of the resonant peak and any self-oscillation. FM 1 and FM 2 CV inputs both sum with the FREQUENCY knob position to modulate cutoff.

**IN 1.** The primary audio input. The IN 1 attenuator knob controls the level of this signal entering the filter. Above 75%, the input begins to overdrive the filter input stage, adding saturation before the filter has processed the signal. When no cable is inserted, IN 1 receives DIST 2: the output of a second internal distortion circuit that compares the VCA output with the DIST output and produces an extreme square-wave comparator signal. This normalization creates maximum internal complexity when IN 1 is unpatched — a chaotic, aliased signal driven into the filter at whatever level the IN 1 knob sets. Patching an audio source into IN 1 breaks this normalization entirely.

**IN 2.** The second audio input. IN 2 and IN 1 are summed together before the filter, making the 100 Grit a two-input mixing stage into a single filter and distortion chain. At the summing point, both signals interact in the filter's nonlinear saturation behavior: two signals summed into a saturating circuit produce intermodulation products — sum and difference frequencies — that neither signal contains individually. This is qualitatively different from mixing two signals cleanly and then distorting; the saturation acts on the combined material and generates new frequency content from the relationship between the two inputs. When no cable is inserted, IN 2 receives the DIST output back into the filter — a distorted resonance path that the manual describes as working "in opposition to the one offered by RES." Patching any audio source into IN 2 removes this self-feedback and replaces it with the new source.

**FM 1.** Linear voltage control over the filter cutoff frequency. FM 1 and FM 2 sum together at the filter's frequency control point. When no cable is inserted, FM 1 receives the DIST output as dynamic frequency modulation: the distortion content of the current output modulates the filter frequency in real time, creating a feedback loop where the more distorted the signal is, the more the filter frequency shifts, which changes the distortion, which changes the FM. The FM 1 knob controls the depth of this normalization; with FM 1 fully counterclockwise, the normalization is attenuated to silence. With FM 1 up and no cable patched, the self-FM normalization is the most immediately audible feedback behavior on the module: it adds laser-like pitch sweeps to percussive material and can reduce bass content due to the filter sweeping its cutoff above the fundamental.

**FM 2.** Exponential voltage control over filter cutoff frequency, roughly scaled to volts per octave. FM 2 will not track accurately in tune — the manual is explicit that it is "roughly scaled" and will not follow a V/oct sequence precisely. It is useful for approximate pitch tracking that keeps the filter generally following the harmonic register of a sequenced source without precision tuning. FM 2 has no normalization: when unpatched it is silent and does not affect the circuit. Patching a V/oct source here keeps the filter's resonant peak near the pitch of the incoming sequence across register changes.

**GAIN.** Controls the gain of the OTA VCA and therefore how hard the signal is driven into the distortion amplifier. The GAIN knob must have some clockwise position for any audio to pass; without GAIN, both OUT and DIST are silent regardless of all other settings. Above approximately 75%, GAIN itself begins to add distortion independent of the x100 switch. The GAIN CV input accepts 5V for unity gain; above 5V it provides additional gain. When no cable is patched into GAIN CV and the CV attenuator knob below GAIN is turned up, POLE 2 (the 12dB output node of the filter) is used to modulate the VCA — a relatively subtle harmonic content shift that the manual describes as "a relatively subtle form of distortion." Patching any CV source into GAIN CV breaks this normalization and allows envelope, LFO, or gate control of the VCA amplitude directly. This is the standard configuration for VCA use.

**RES.** Controls the resonance of the transistor ladder filter. The RES knob sets the baseline resonance level. An internal resonance amplitude trim (RV3) on the PCB sets the point at which maximum RES reaches self-oscillation; from the factory, this is calibrated so the filter self-oscillates at or near the maximum RES position. When no cable is patched into RES CV and the CV attenuator knob under RES is turned up, the DIST output is routed as audio-rate modulation into the resonance control — the manual notes this creates "laser sounds and screeches riding on top of the RES." This normalization works in opposition to the IN 2 normalization; both are distorted resonance paths but from different points in the circuit. With RES CV patched by an external source, external CV controls resonance and the normalization is removed.

**x100 Switch.** A three-position switch that multiplies the gain by 100 before the distortion amplifier. OFF is the default position. ON locks x100 active continuously. The third position, labeled (ON) on the panel, is momentary: it engages x100 only while the switch is held, returning to OFF when released. The momentary position is a performance control — held for a hit, a phrase, or a single accent, then released. At x100, the distortion output self-limits to approximately 12Vpp and the waveform is fully squared and harmonically dense regardless of the input level. For continuous maximum distortion density, flip to ON. For percussive x100 bursts during a patch that otherwise runs at lower distortion, use the momentary position.

**OUT.** By default, OUT is the VCA output: the filter output after the GAIN stage, before the distortion amplifier. This is the cleaner of the two outputs, though at high GAIN settings it will still distort significantly. The output source can be changed via the J10 header on the rear PCB to take from the filter directly, bypassing the VCA and GAIN knob entirely — in this configuration OUT is affected only by FREQUENCY and RES.

**DIST.** The output of the distortion amplifier following the VCA. This is the primary output for heavy distortion applications. GAIN controls how hard the signal is driven into the distortion stage; at high GAIN and with x100 on, DIST produces a fully saturated, harmonically dense signal that self-limits at approximately 12Vpp. The DIST output is also the source for several feedback normalizations, meaning what DIST produces feeds back into FM 1, IN 2, and RES CV simultaneously when those inputs are unpatched. This self-referential architecture means the distortion character is always partially feeding back into the process that generates it.

**Touch Points.** Eight brass balls arranged in two groups of four on the upper portion of the panel, connected to sensitive circuit nodes through current-limiting resistors. Connecting two touch points simultaneously creates a resistive path between those nodes. The left group (counterclockwise from top left): DIST 2 OUT, GAIN CV, DIST 2 AMP PIN, RES CV IN. The right group (counterclockwise from top left): DIST 1 AMP PIN, FREQ CV, DIST 1 OUT, GAIN CV. The AMP PINs are bidirectional and can produce effects from capacitive loading alone — touching a finger to the DIST 1 AMP PIN without touching any other point changes the distortion amplifier's behavior from the circuit's perspective. The DIST 1 AMP PIN is also the touch point most likely to pick up radio frequencies; this is location-dependent and more common when touching only one point rather than bridging two.

---

## Why This Instrument Excels

The dual-input summing architecture is what separates the 100 Grit from single-input distortion modules. Two different audio sources patched into IN 1 and IN 2 are summed at the filter's input stage, where the combined signal is processed by the filter's nonlinear transistor ladder together. When the combined signal drives the ladder into saturation, the distortion acts on the mathematical relationship between the two signals rather than on either signal independently. The frequency content of the intermodulation products depends on the spectral difference between the two inputs: two related pitches produce difference tones in the lower register, two unrelated sources produce a complex and inharmonic intermodulation spectrum, and a slow LFO and a fast audio signal produce amplitude modulation sidebands. None of these intermodulation products exist in either source; they are created by the nonlinear mixing at the filter input. Driving this combined and intermodulated signal further into the DIST output adds a second stage of harmonic generation that compounds the complexity.

The FM 1 normalization is the feature most directly responsible for the laser-pitched sweep character that the module produces during percussive processing. When FM 1 is unpatched, the DIST output feeds back into the filter's frequency control at whatever depth the FM 1 knob sets. A percussive transient arriving at the input drives the GAIN stage, produces a DIST output, and that DIST output simultaneously frequency-modulates the filter: the attack of the sound pushes the filter frequency up or shifts it dynamically, adding a pitch sweep to the distortion tail that is derived from the distortion itself rather than from an external envelope. The sweep is not programmable or predictable in the conventional sense; it responds to the amplitude and spectral content of whatever is being processed at that moment. This is why the module's character changes depending on the source material: a kick drum produces a different FM sweep than a sustained bass note, because the two have different distortion profiles and therefore different FM signals feeding back into the frequency control.

The normalization system as a design principle means the 100 Grit is always processing itself, even before any external signal arrives. The default state — with no cables in any input — has all five feedback normalizations active simultaneously: DIST 2 into IN 1, DIST into IN 2, DIST into FM 1, POLE 2 into GAIN CV, DIST into RES CV. The total behavior of this unpatched state, with x100 on and touch points engaged, is the noise box: a self-sustaining oscillator-like system whose sound character is entirely determined by the GAIN, RES, FREQUENCY, and knob positions of each normalization's attenuator. This is not a mode that requires special configuration; it is the default state of the circuit with no inputs. Most modules are silent without audio sources. The 100 Grit is complex without them.

The touch points make the physical act of playing the module different from any knob-and-cable interaction. Skin resistance varies continuously with contact pressure, body position, hydration, and skin surface condition; the resistive value of a finger bridge between two touch points at one moment is not the same as the same bridge a moment later. This makes touch point control genuinely non-repeatable in a way that knobs, which return to the same position, are not. Two thumbs placed across the full set of eight points creates eight simultaneous connections with continuously varying resistance values, which is a control density far beyond what eight CV inputs would provide — not in precision but in simultaneous influence. The manual suggests connecting touch points with cables or alligator clips for more stable connections; this converts them from gestural performance elements into fixed resistive patch points and retains the circuit-node access while removing the continuous variation of skin contact.

---

## Patches

### Patch 1: Dual Input Intermodulation Distortion

Schlappi Engineering 100 Grit receiving two different audio sources into IN 1 and IN 2, summed and driven hard into the DIST output, demonstrating intermodulation between the two sources.

```
[BIA Out] ────────────────────[A]──────▶ [100 Grit IN 1]
[MIA Out] ────────────────────[A]──────▶ [100 Grit IN 2]

[100 Grit DIST] ─────────────[A]──────▶ [MixUp CH3]

                                          IN 1: 60% CW
                                          IN 2: 50% CW
                                          FREQUENCY: 70% CW
                                          RES: 20% CW
                                          GAIN: 75% CW
                                          FM 1: fully CCW (disable normalization)
                                          RES CV: fully CCW (disable normalization)
                                          GAIN CV: fully CCW (disable normalization)
                                          x100: OFF
```

**Setup:** Patch BIA Out into IN 1 and MIA Out into IN 2. Both are now patched, which removes the DIST feedback normalizations from those inputs. Set FM 1, RES CV, and GAIN CV knobs fully counterclockwise to disable their normalizations, isolating the two-source summing behavior from the self-FM feedback. Set x100 to OFF to stay in the controllable distortion range rather than maximum obliteration.

**Controls:** The two sources sum at the filter input and are processed together. Adjust IN 1 and IN 2 levels to balance their contributions to the mix; with IN 1 higher, the BIA's character dominates the distortion. With IN 2 higher, the MIA's sawtooth-heavy spectrum leads. When both are set at similar levels, neither source dominates and the intermodulation between them becomes audible as frequency content that neither module produces independently — low-register difference tones and upper-register aliasing that reflects the mathematical relationship between the two sources. Raise GAIN to drive the VCA harder into the distortion amp; the intermodulation products become more prominent as the signal clips. Increase FREQUENCY slowly and hear the filter open onto more of the spectrum; at low FREQUENCY with high GAIN, the distortion is low-passed into a thick, dark grind. At high FREQUENCY, the full spectrum including upper harmonics and intermodulation content comes through. Raise RES slightly to add a resonant peak that emphasizes one frequency in the distortion spectrum.

**Result:** A single-output distortion voice combining two drum synthesizer sources with intermodulation-generated frequency content that neither source produces alone. The balance of IN 1 and IN 2 determines whether the BIA or MIA character leads, and the intermodulation content shifts as the patch parameters change.

---

### Patch 2: Self-FM Distortion on Percussive Material

100 Grit with audio on IN 1 only, FM 1 normalization active (DIST feeding back into filter frequency), demonstrating how the self-FM normalization creates dynamic pitch sweeps from percussive transients.

```
[Hermod+ Gate Out] ───────────[G]──────▶ [BIA Trig In]
[BIA Out] ────────────────────[A]──────▶ [100 Grit IN 1]

[100 Grit DIST] ─────────────[A]──────▶ [MixUp CH3]

                                          IN 1: 70% CW
                                          IN 2: fully CCW (disables DIST FB normalization)
                                          FM 1: 30% CW (DIST normalization active at this depth)
                                          FM 2: fully CCW
                                          FREQUENCY: 65% CW
                                          RES: 15% CW
                                          GAIN: 70% CW
                                          GAIN CV: fully CCW
                                          RES CV: fully CCW
                                          x100: OFF
```

**Setup:** Patch BIA Liquid Bass mode into IN 1 only. Leave FM 1 unpatched and set its knob to 30% CW; this allows the DIST output to feed back into FM 1 at moderate depth without maxing out the feedback intensity. Set IN 2 fully counterclockwise to disable its DIST normalization, isolating the FM 1 normalization as the only active feedback path. Set x100 OFF for a controllable distortion range.

**Controls:** With each BIA trigger, the attack of the kick drives the GAIN stage, producing DIST output. That DIST output simultaneously feeds into FM 1, sweeping the filter frequency by a dynamic amount proportional to the current distortion level: the louder and more distorted the attack, the more the filter frequency sweeps. The result is a kick drum that has a self-generated pitch sweep on the attack and return as the envelope decays. This sweep is not a fixed envelope shape — it tracks the distortion profile of the BIA's own output in real time. Adjust FM 1 depth counterclockwise to reduce the sweep amount and produce a subtler pitch movement; clockwise to exaggerate the sweep into an extreme FM scream. Adjust FREQUENCY to set where the filter sits when the FM normalization is not active (between transients); lower FREQUENCY settings produce a darker resting tone with bright FM sweeps, higher settings produce a more open sound where the FM sweep is less dramatic relative to the full spectrum already passing through. Listen specifically to the tail of each kick after the attack: the FM sweep follows the decay shape of the BIA's DIST output all the way to silence, producing a characteristic descending filter sweep that is driven by the distortion decay rather than by any external envelope.

**Result:** A kick drum voice with a self-derived filter frequency sweep on each transient, produced by the DIST-to-FM 1 normalization routing the distortion output back into the filter's frequency control. The sweep character changes with BIA Decay and GAIN settings without any additional CV routing.

---

### Patch 3: Two Inputs Plus Active Self-FM Normalization

100 Grit with both inputs patched for intermodulation and FM 1 patched from an external source for precise filter frequency modulation, combining the dual-source character from Patch 1 with controllable FM.

```
[BIA Out] ────────────────────[A]──────▶ [100 Grit IN 1]
[MIA Out] ────────────────────[A]──────▶ [100 Grit IN 2]
[Pons Asinorum Out 1] ────────[C]──────▶ [100 Grit FM 1]
[Hermod+ Pitch CV Out] ───────[C]──────▶ [100 Grit FM 2]
[Zadar CH1 Env Out] ──────────[C]──────▶ [100 Grit GAIN CV]
[Hermod+ Gate Out] ───────────[G]──────▶ [BIA Trig In]
[Hermod+ Gate Out] ───────────[G]──────▶ [MIA Trig In]
[Hermod+ Gate Out] ───────────[G]──────▶ [Zadar Trigger CH1]

[100 Grit DIST] ─────────────[A]──────▶ [Qu-Bit Aurora In L]
[Aurora Out L] ───────────────[A]──────▶ [MixUp CH3 L]
[Aurora Out R] ───────────────[A]──────▶ [MixUp CH3 R]

                                          IN 1: 55% CW
                                          IN 2: 45% CW
                                          FM 1: 40% CW (PA LFO depth)
                                          FM 2: 30% CW (pitch CV depth)
                                          FREQUENCY: 60% CW
                                          RES: 25% CW
                                          GAIN knob: 65% CW
                                          GAIN CV: 50% CW (Zadar attenuated)
                                          RES CV: fully CCW
                                          x100: OFF
                                          PA CH1: LFO, up/down, 6 seconds
                                          Zadar CH1: sharp attack, medium decay
```

**Setup:** Patch BIA and MIA into IN 1 and IN 2. Patch Pons Asinorum Ch1 in slow LFO mode into FM 1 to provide slow, repetitive filter frequency modulation — this replaces the self-FM normalization with a controllable periodic sweep. Patch Hermod+ pitch CV into FM 2 at moderate depth so the filter roughly follows the pitch register of the sequence. Patch Zadar's first channel into GAIN CV so each trigger opens and closes the VCA amplitude with a shaped envelope. Route DIST through Aurora at moderate reverb for spatial depth.

**Controls:** With both inputs patched and FM 1 providing external LFO modulation, the self-FM normalization on FM 1 is removed; the PA LFO sweeps the filter frequency on its own 6-second cycle. The Zadar envelope on GAIN CV opens the VCA with each trigger and closes it when the envelope decays, so the distortion character is fullest at the attack moment and trails off as GAIN drops. Raise the GAIN knob to set the peak distortion level at the Zadar envelope's maximum. Adjust the GAIN CV attenuator knob to set how much the Zadar envelope closes down the VCA between triggers; at 100% CV, the VCA closes fully between hits; at 50%, it stays partially open, producing a sustained low-level distortion between transients. Use FM 2 depth (the FM 2 knob) to set how much pitch register changes in the Hermod+ sequence shift the filter; low depth gives a hint of tracking, high depth produces dramatic filter sweeps between sequence steps. Aurora's reverb blurs the DIST output's sharp transients into a sustain tail; adjust Aurora's Warp to change how the distortion spectrum is treated in the reverb.

**Result:** A dual-source distortion processing patch with external FM control, per-note GAIN envelope shaping, and rough pitch tracking, using the 100 Grit as the primary distortion and timbral processing point for two simultaneous drum synthesizer voices.

---

### Patch 4: Noise Box

100 Grit with no audio inputs, x100 on, all feedback normalizations active, touch points as the primary performance interface.

```
(No audio inputs patched)

[100 Grit DIST] ─────────────[A]──────▶ [MixUp CH3]

                                          IN 1: 25% CW
                                          IN 2: 25% CW
                                          FM 1: 15% CW
                                          FM 2: fully CCW
                                          FREQUENCY: 50% CW
                                          RES: 20% CW
                                          GAIN: 60% CW
                                          GAIN CV: 50% CW
                                          RES CV: 25% CW
                                          x100: ON
                                          Touch points: explore
```

**Setup:** Patch nothing into any audio or CV input. Route DIST to the mixer. Set IN 1 and IN 2 knobs to 25% CW — these attenuate the DIST 2 and DIST normalizations respectively, controlling how much of the internal feedback is active. Set GAIN CV attenuator to 50% CW, allowing POLE 2 to modulate the VCA at moderate depth. Set RES CV to 25% CW, allowing DIST to modulate resonance at low depth. Set x100 to ON. The module is now generating sound from its own internal feedback through all five normalization paths simultaneously.

**Controls:** The FREQUENCY knob is the most dramatic real-time control in this configuration: it changes the fundamental character of the oscillation the feedback system is sustaining and can sweep from dense low-frequency grumble to high-frequency screech across its range. RES controls the pitched character of the resonance feedback; with RES higher, the feedback sustains more at a specific pitched frequency and the noise character becomes more tonal. GAIN at 60% and x100 on produces maximum distortion density; reducing GAIN to around 40% with x100 still on changes the character toward something slightly more structured. The touch points are the performance interface in this mode: place one thumb from each hand on each group of four balls and rotate each thumb to make contact with different adjacent pairs. Each pair bridges an output to a nearby input with skin resistance as the path. The left group's DIST 2 OUT adjacent to GAIN CV is particularly effective; bridging them adds the DIST 2 comparator output directly to the VCA gain, creating amplitude modulation from the internal comparator. The right group's DIST 1 OUT adjacent to GAIN CV (right side) is the same connection from a different access point. Touch FREQ CV with a free finger while moving the FREQUENCY knob with the other hand for the most chaotic simultaneous control.

**Result:** A self-sustaining noise and oscillation instrument requiring no external signal, controlled by knob positions and touch point gestures. The noise box mode is not a demonstration of a secondary capability — it is the architecture's natural state when every feedback normalization is active simultaneously.

---

## Common Mistakes

### "No sound is coming out of either output"

GAIN must be turned up or GAIN CV must provide sufficient voltage for any audio to pass. The 100 Grit's VCA is in the signal path before both OUT and DIST; without any gain, the VCA closes completely and the filter output does not reach either output jack. This is the most frequent initial setup error and the first thing to check.

**Fix:** Turn the GAIN knob clockwise to at least 50%. If GAIN CV is patched, confirm the CV attenuator knob below GAIN is also turned up and that the CV source is providing voltage. With GAIN at 0% and no CV, the module is silent by design regardless of all other settings.

---

### "The module is making noise even though I have not patched anything"

The normalizations are active. Every input on the 100 Grit carries an internal feedback signal when unpatched; with IN 1, IN 2, FM 1, GAIN CV, and RES CV all unpatched and their associated knobs turned up, all five feedback paths are simultaneously active. This is the module's default behavior, not a malfunction.

**Fix:** If you want a quiet, controlled baseline, turn the knobs associated with any unused input fully counterclockwise. IN 1 knob at CCW disables the DIST 2 normalization. IN 2 knob at CCW disables the DIST normalization. FM 1 knob at CCW disables the DIST→FM 1 normalization. GAIN CV attenuator at CCW disables the POLE 2 normalization. RES CV attenuator at CCW disables the DIST→RES normalization. With all five at CCW, the module is quiet until an external signal is patched.

---

### "Patching a cable into IN 2 made the module quieter or less interesting"

Patching into IN 2 removes the DIST normalization that was feeding back into that input. If the patch before insertion was relying on that feedback for character — as a distorted resonance path contributing to the overall sound — removing it by patching reduces complexity rather than adding it. This is the normalization inversion: adding a cable removes a feedback path.

**Fix:** If you want to add IN 2 as an audio input while preserving the DIST feedback character of the normalization, try using a mult or stackable cable to send both the new audio source and the DIST output into IN 2 simultaneously through an external mixer before the IN 2 input. Alternatively, accept that patching IN 2 changes the character of the sound and compensate by adjusting other parameters.

---

### "The RES CV normalization is too wild — the resonance is screeching uncontrollably"

The RES CV normalization feeds DIST into the resonance control at whatever depth the RES CV attenuator allows. The resonance amplitude trim (RV3) on the PCB sets where the filter begins to self-oscillate; if RV3 is calibrated aggressively and the RES CV normalization is running DIST into resonance, the combination can push the filter well into self-oscillation territory without warning.

**Fix:** Turn RES CV attenuator fully counterclockwise to disable the DIST normalization entirely and return to manual RES control only. Then build up from there: turn RES CV attenuator clockwise slowly and listen to the resonance character change as small amounts of DIST modulate the resonance control. The useful range for most applications is a small fraction of the full attenuator travel.

---

### "The FM 1 normalization is eating my bass frequencies"

The DIST→FM 1 normalization applies the distortion output as dynamic frequency modulation to the filter. Because DIST contains significant high-frequency energy, the FM sweeps the filter cutoff upward during transients, which can pull the filter above the bass register at the moment of attack. This is the design behavior but may not be desired for every application.

**Fix:** Reduce FM 1 depth (turn the FM 1 knob toward counterclockwise) until the bass content is preserved at an acceptable level while retaining some FM character. For applications where bass preservation is critical, patch an external LFO or CV source into FM 1 to replace the normalization with a controlled sweep that does not track the distortion amplitude directly.

---

### "The DIST and OUT outputs sound similar — I expected DIST to be more distorted"

With x100 off and GAIN below approximately 75%, the distortion amplifier following the VCA may not be adding substantial additional character beyond what the VCA and filter are already contributing. The OUT and DIST outputs diverge significantly only when the distortion amplifier is driven beyond its linear range, which requires higher GAIN settings or x100.

**Fix:** Increase GAIN past 75% and listen for DIST to begin clipping noticeably above OUT's level. Alternatively, flip x100 to ON for immediate maximum distortion density — with x100, DIST is always dramatically different from OUT regardless of GAIN position. The intended use case for monitoring both outputs simultaneously is comparing the filtered/gained version (OUT) with the distorted version (DIST) as two different takes on the same signal, which only becomes meaningful when DIST is pushed significantly harder.

---

## Advanced Learning Path

Map each normalization in isolation before working with combinations. Start with all input attenuator knobs fully counterclockwise (all normalizations disabled, module quiet). Turn IN 1 knob slowly to 25% CW and listen: the DIST 2 normalization is now active, feeding the internal comparator signal into the filter at low level. Note the character. Return IN 1 to CCW. Turn FM 1 knob slowly to 25% CW: the DIST→FM 1 normalization is now active, but without any audio passing (GAIN at 0), there is nothing to distort and therefore no FM. Turn GAIN up to 50% and a self-oscillating FM loop begins. Return both to CCW. Work through each normalization this way individually before combining them.

Learn the two distortion outputs as simultaneously usable rather than as an either-or choice. Patch both OUT and DIST to separate mixer channels and set different levels for each in the mix. OUT provides the filtered, gain-staged version; DIST provides the additional distortion stage. In a mix context, blending a low level of OUT under a high level of DIST provides a clean low-frequency foundation below the saturated high-frequency content of the DIST output. This parallel processing of the same signal at two distortion depths is only possible because both outputs are simultaneously available.

Practice the noise box mode with systematic exploration rather than random touching. Begin with all five normalizations at low attenuator settings (approximately 20% CW each), x100 on, FREQUENCY at center, GAIN at 60%. Touch one pair of adjacent touch points and hold them for several seconds before releasing. Note the specific effect of that pair. Move to the next adjacent pair and repeat. Work clockwise through all adjacent pairs on both sets before touching non-adjacent pairs or bridging the two sets. This systematic approach builds a mental map of which touch point connections produce which effects in the current state; the same connections will produce different effects when the knob positions change.

Explore the Output Source header (J10) on the rear PCB. By default, OUT taps the VCA output. With the header moved to the filter direct position, OUT takes the filter output before the VCA and GAIN knob; the GAIN knob no longer affects OUT, which passes signal at a fixed level determined only by FREQUENCY and RES. In this configuration, OUT becomes a pure VCF output and DIST remains the VCA-driven distortion output, producing two genuinely different stages of processing from separate tap points. This is useful when you want a clean filtered reference signal alongside a distorted version from the same source.

Practice the x100 momentary position as a performance gesture independent of any patch configuration. With a patch running at a moderate distortion level, hold the switch in the (ON) position for a full phrase and release. The transition in and out of x100 is abrupt rather than gradual — it is a switch, not a knob — which means it functions as a hard cut to maximum obliteration and back. Find the phrase boundaries in your sequence where this transition lands musically. Then try holding it for a single beat, or for a bar, or only at the downbeat of every fourth bar. The momentary position is a manual performance control that has no CV equivalent; it is the one parameter on this module that requires a hand on the hardware to use.

Use the 100 Grit as a final stage for a complete percussion voice by routing both BIA and MIA outputs into IN 1 and IN 2 simultaneously and adjusting the balance between them. With BIA in Liquid mode and MIA in Skin mode at similar pitch registers, the two sources interact in the filter and produce a combined distortion character that is specific to their relationship at that moment. Changing BIA's Spread or MIA's Smash setting changes the spectral content of both sources independently, which changes the intermodulation at the 100 Grit's filter input and therefore the DIST output's character without any changes to the 100 Grit's own parameters. The 100 Grit becomes responsive to upstream changes automatically.

For CV-controlled distortion intensity, use a Zadar envelope patched into GAIN CV as a per-note distortion shaper: a short Zadar attack and decay produces a distortion burst at each trigger that rises and falls with the envelope, making the distortion amount itself rhythmically shaped rather than static. With GAIN knob at a baseline that keeps some distortion always present and the Zadar envelope adding additional GAIN CV on each trigger, the hits are noticeably more distorted than the spaces between them. Adjust the GAIN CV attenuator to set how much additional drive the Zadar envelope contributes beyond the knob's baseline.

---

## Pairs Well With

**Noise Engineering Basimilus Iteritas Alter** is a natural primary source for the 100 Grit, particularly in Metal or Liquid modes where the BIA's output already contains dense harmonic and inharmonic content before it reaches the 100 Grit's filter. The BIA's variable sample rate creates aliasing content that aligns with harmonic multiples; running this through the 100 Grit's ladder filter and distortion stage reinforces that harmonic alignment in the saturation character and produces a distortion that is musically coherent rather than uniformly harsh. In Liquid mode, the BIA's internal pitch sweep interacts with the 100 Grit's FM 1 normalization: the varying distortion content of the pitch sweep produces a time-varying FM signal that tracks the BIA's own pitch envelope through the 100 Grit's filter, creating an additional layer of pitch-tracking frequency response that neither module provides alone.

**Noise Engineering Manis Iteritas Alia** feeds the 100 Grit with material that is already heavily processed at the source — sawtooth oscillators through Smash modulus destruction and Profundity sample-rate chorus. Routing the MIA's DIST output into IN 1 of the 100 Grit and adding a secondary source into IN 2 creates a three-stage processing chain: MIA source generation, MIA Smash destruction, and 100 Grit filter plus distortion amp. The combined distortion of two analog and digital processing stages produces frequency content that is genuinely difficult to generate by any other means. With MIA's Bash knob controlling per-note MIA distortion amount and 100 Grit's GAIN controlling the second distortion stage, two independent drives operate in series, each contributing its own harmonic character.

**Noise Engineering Pons Asinorum** provides the modulation bus for the 100 Grit's FM, GAIN CV, and RES CV inputs from a single 6HP module. The PA's four channels in LFO mode at different cycle lengths can simultaneously sweep FREQUENCY via FM 1 (replacing the self-FM normalization with a controlled periodic sweep), modulate GAIN CV for slow amplitude and drive variation, and apply a slow RES CV sweep for evolving resonance character. Using PA in envelope mode on GAIN CV, triggered by the same gate as the audio source, makes the 100 Grit function as a VCA with envelope shaping controlled by the PA's attack and decay settings rather than the 100 Grit's own gain knob alone.

**Zadar** provides per-note GAIN CV shaping when the 100 Grit is processing sequenced material. Patching Zadar into GAIN CV and triggering it from the same gate as the audio source makes the distortion amount follow Zadar's envelope shape: short Zadar envelopes produce distortion bursts on each trigger with clean(er) spaces between; long Zadar envelopes sustain the distortion drive through the full note duration. Zadar's independently programmable envelope shapes per channel allow different distortion drive curves for different sequence steps if multiple Zadar channels are combined at the GAIN CV input through a mixer before patching, though this requires additional modules.

**Qu-Bit Aurora** receives the 100 Grit's DIST output well because Aurora's FFT-based spectral processing operates on frequency content, and the 100 Grit's DIST output is spectrally dense across a wide range. Aurora's spectral reverb blurs the 100 Grit's sharp transient edges into sustained tails while preserving the frequency character of the distortion; high Warp settings transform the distortion into a shimmering spectral cloud. The combination is particularly effective for industrial ambient applications where the 100 Grit provides the harsh attack character and Aurora extends it into a sustaining texture that outlasts each transient by several seconds.

**Hermod+** provides gate signals for any envelope controlling GAIN CV or RES CV, and V/oct sequences into FM 2 for rough filter pitch tracking. FM 2 does not track accurately in tune — the manual is explicit that it is "roughly scaled" to V/oct — but it tracks register changes well enough that the filter's resonant peak generally follows the pitch range of the sequence. For applications where the 100 Grit is functioning as a distortion voice rather than a filter, FM 2 pitch tracking adds a pitch-related tonal quality to the distortion output that makes sequenced material more coherent tonally even at extreme distortion settings.
