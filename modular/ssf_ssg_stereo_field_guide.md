---
title: SSG Stereo Field
manufacturer: Steady State Fate
primary_role: SHAPER
secondary_roles: [AMPLIFIER]
historical_context: true
form_factor: eurorack
functions: [filter, vca, wavefolder]
behavior_tags: [warm, harmonic, evolving, gated, reactive, nonlinear, dirty]
use_cases: [percussive voice, timbral movement and shaping, stereo signal processing, evolving ambient texture]
hp: 10
memory: none
transport: none
screen: false
hybrid: false
cv: full
---

# SSG Stereo Field

**A stereo low-pass gate with wavefolder, saturation, and psychoacoustic field control**

![Steady State Fate SSG Stereo Field](https://github.com/Shadoe-42/music/raw/main/modular/images/steady_state_fate/ssg_stereo_field/front_panel.jpg)

## Historical Context

Don Buchla designed the first low-pass gate as part of the Buchla Series 200 modular system in the early 1970s. The 292 Quad Dynamics Manager used vactrols: optocouplers pairing an LED with a cadmium sulfide light-dependent resistor: to control a low-pass filter's cutoff frequency and a signal's amplitude through the same physical component simultaneously. The LDR's inherent response characteristics, particularly the slow release of its resistive element after the LED extinguishes, produced a decay profile that tracked the natural physics of acoustic instruments more closely than any standard voltage-controlled amplifier circuit could. When a marimba bar or guitar string loses energy, its brightness and loudness diminish together in a coupled, material curve; the vactrol made an electronic equivalent of this coupling available to synthesis for the first time. Buchla's Music Easel of 1973, a portable performance system built around the 208 Stored Program Sound Source, brought this LPG architecture to its most concentrated form and demonstrated that the pluck and bloom character of coupled filter-amplitude gating was musically irreplaceable for percussion, analog string simulation, and organic melodic lines.

The sonic character of an LPG is inseparable from the physics of the coupling. In standard subtractive synthesis, an envelope generator opens and closes the filter and the VCA through two independent control voltage connections; the designer decides the contour of each separately. The LPG collapses this into a single gate input that opens both filter and amplitude together through one circuit element. The result is a characteristic pluck when a short trigger is applied: brightness and loudness peak simultaneously at the moment of contact and decay together at a rate partly determined by the LDR's material release time, which is a physical property rather than a purely electrical one. A short trigger lowers the intensity of this pluck rather than changing its shape, which produces a natural dynamic response to trigger level without requiring a separate velocity processing stage. This behavior is the origin of the term low-pass gate: the module is simultaneously a low-pass filter and an amplitude gate, and the distinction between those two functions disappears when they share the same control element.

The integration of wavefolder processing into LPG designs extends a timbral lineage Buchla himself established. The 259 Complex Waveform Generator, developed alongside the Series 200 system, included a symmetry section that folded waveforms back on themselves to generate additional harmonics from a simple source. When wavefolder processing is placed at the output stage of a low-pass gate, the two circuits interact in a musically useful way: the LPG's opening and closing cycle continuously sweeps the audio signal through different amplitude levels, and the wavefolder's harmonic output changes with signal level. As the gate opens and the signal rises above the fold threshold, new harmonics appear; as the gate closes and the signal falls, those harmonics collapse back into the fundamental. This produces an intrinsically evolving harmonic content at the output rather than a static spectral shape that simply rises and falls in amplitude, and it happens from the physical interaction of the two stages rather than from any additional modulation patching.

Steady State Fate extended the LPG concept in two directions not present in the Buchla lineage: a spatially aware stereo field processor and a stochastic resonance injection system called QAOS. The stereo field control draws on psychoacoustic research into how listeners perceive the position and distance of sound sources. A distant sound reaches the listener with high-frequency content attenuated by air absorption and with altered inter-aural relationships relative to a near source; the NEAR and FAR modes of the FIELD control model these perceptual differences, making the stereo position feel physically closer or further rather than simply adjusted in amplitude balance. QAOS, which appears across several SSF modules, injects controlled stochastic instability into the resonance control rather than deriving Q from a fixed feedback coefficient. The result is a filter resonance that varies slightly and unpredictably around its set point, preventing the characteristic static narrowness that self-resonant filters can develop and keeping the sound alive over long durations in ways that no fixed Q setting achieves.

---

## Quick Start

The Steady State Fate SSG Stereo Field is a stereo low-pass gate that couples dynamic filtering and amplitude control through a single gate or CV input, with three switchable timbre modes: wavefolder, saturator, and QAOS chaos injection: plus a voltage-controlled stereo field processor. It accepts mono or stereo sources and produces an envelope output for downstream CV use. Without any gate signal present, it operates as a static VCF with amplitude fully open.

1. Patch a mono audio source into IN-L. Patch OUT-L into a mixer or audio destination.
2. Patch a gate or trigger signal from a clock or sequencer into EXCITE.
3. Set the FREQ slider to approximately 75% of its travel.
4. Set the DECAY slider to the middle position.
5. Set the TIMBRE switch to SAT and the TIMBRE slider to the lower third of its travel.
6. Set the FIELD knob to the center M (mono) position. Set the NEAR/FAR switch to NEAR.
7. Send triggers. The SSG Stereo Field opens and closes with each trigger, producing a pluck or gate effect depending on DECAY and FREQ positions.
8. Move the FREQ slider downward. The filter ceiling drops and the pluck becomes darker. Move it upward to restore brightness.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 10 HP |
| Depth | 23 mm |
| Power | 120 mA +12V / 120 mA -12V / 0 mA +5V |

---

## Essential Parameters

**EXCITE and CV/GATE.** Two independent gate inputs open the low-pass gate through different mechanisms. EXCITE accepts any gate or trigger and conditions it internally into a short pluck: regardless of the incoming signal's duration, the module derives a compact attack transient from it. Very short triggers reduce the pluck intensity rather than the pluck shape, making EXCITE level-sensitive in a way that functions as a natural velocity input when driven from variable-level gates. CV/GATE passes the full duration of any signal presented to it: a gate of fixed length, an envelope from an external generator, or an LFO for continuous cycling. Both inputs are level-sensitive between approximately 0V and 5V; the exact relationship between incoming level and LPG opening depth depends on the FREQ slider position. When neither input has a cable patched, the SSG Stereo Field operates as a static VCF with amplitude fully open and the DECAY control inactive. Using both inputs simultaneously produces combined behavior where EXCITE provides the initial pluck attack and CV/GATE extends or shapes the sustained portion, enabling complex envelope dynamics from a single module.

**DECAY.** Controls the decay time of the LPG response and is active only when a signal is present at EXCITE and/or CV/GATE. The slider increases decay time as it moves upward: minimum settings produce sharp percussive plucks, maximum settings produce sustained gate responses that release slowly after the gate closes. DECAY time interacts with the selected filter type and the FREQ slider position; the same DECAY setting produces audibly different perceived lengths depending on whether BP, 1PLP, or 2PLP is selected, because each topology has a different relationship between cutoff frequency and perceived output loudness at a given slider position. The DECAY input accepts any CV signal type for real-time control of envelope length by LFOs, sequencers, or random sources.

**TIMBRE.** Selects the timbral enhancement mode and controls its depth. Three modes are available via the upper switch: FOLD applies a wavefolder that adds harmonics by folding the waveform back on itself above a threshold; SAT applies a soft saturator that rounds transients and adds gentle harmonic warmth; QAOS injects stochastic variation into the Q-FACTOR control independent of the FOLD/SAT selection. A second switch below Q-FACTOR can deactivate QAOS entirely across all TIMBRE modes, or QAOS can be active alongside either FOLD or SAT simultaneously. The TIMBRE slider controls the amount of the active effect. CV applied to the TIMBRE input modulates this depth in real time; however, sufficiently negative CV in FOLD or SAT mode ducks the output level below the bypassed signal level. Setting the TIMBRE slider to a mid position before applying a bipolar LFO to TIMBRE CV offsets this ducking, keeping the output audible throughout the full modulation cycle.

**FREQ.** Controls the base frequency of the selected filter topology. Three filter types are selected via a switch: BP is a 2-pole band-pass, 1PLP is a single-pole (-6dB/oct) low-pass, and 2PLP is a 2-pole (-12dB/oct) low-pass. Without a gate signal present, FREQ sets the static cutoff of the VCF and signal passes through continuously at that frequency. With a gate signal present, FREQ sets the maximum frequency the filter opens to during the gate event; the LPG opens up to this ceiling and then decays from it. The FREQ slider must be set to at least 75% of its travel to fully open the filter when a 5V gate signal is applied; settings below this point limit the filter's opening regardless of gate amplitude. FREQ accepts any signal type as CV for real-time frequency modulation.

**Q-FACTOR.** Controls the resonance quality factor of the filter. A sine wave symbol on the dial marks the calibration point at the boundary of self-oscillation; turning Q-FACTOR to this mark places the filter at the threshold where it begins to ring. Beyond this point the filter produces resonant ringing that may sustain when a signal is present; full continuous self-oscillation is not guaranteed. Activating QAOS via either the TIMBRE switch or the dedicated switch below Q-FACTOR injects stochastic variation into the resonance, producing a Q that wanders around the set point rather than remaining fixed. QAOS limits the effective range of Q-FACTOR but adds instability and life to the filter character; it produces asymmetric behavior across the two channels when processing stereo sources. Q-FACTOR accepts CV of any signal type.

**FIELD.** Controls the stereo field of the output. A NEAR/FAR switch determines the perceptual character of the field manipulation. In stereo operation with both IN-L and IN-R patched: the FIELD knob at the ST position produces normal stereo output with left and right channels in their original positions; at -ST it reverses the positions; at the center M position it sums the stereo signal to mono on both outputs. Turning FIELD beyond the ST or -ST positions widens the stereo image, extending the side elements and creating a broader perceived stage. In mono operation with a single source into IN-L and out of OUT-L: in NEAR mode FIELD operates as a high-frequency cut and boost control, with center position giving a flat response; in FAR mode, turning toward ST and beyond adds high boost with low cut, while turning toward -ST and beyond adds high-mid cut with an upper high boost, providing extended tone shaping. FIELD accepts CV of any signal type for real-time stereo position and tone control.

**ENV OUT.** Outputs an envelope signal derived from the LPG's amplitude response. This output rises when the gate opens and decays when it closes, following the DECAY and FREQ interaction. ENV OUT can trigger downstream modules, open additional VCAs, or modulate parameters in time with the gate activity, effectively turning the SSG Stereo Field's LPG response into a derived CV source without requiring a separate envelope generator.

---

## Why This Instrument Excels

The LPG's coupled filter-and-amplitude architecture solves a problem that subtractive synthesis creates and then requires additional patching to work around. When a filter and a VCA are separate modules, the patch establishes their amplitude relationship at build time, and changing that relationship requires repatching. An LPG collapses this into one control element that governs both simultaneously, which sounds like a simplification but is actually an expansion: the coupled behavior produces harmonic-amplitude interactions that no amount of careful dual-envelope programming replicates, because the filter and amplitude always track exactly the same curve rather than two approximated versions of it. The SSG Stereo Field's DECAY and FREQ sliders operate on this coupled response as a unit, meaning that every FREQ and DECAY setting combination produces a distinct sound character, not just a different duration of the same sound. The result is a processor that sounds different, not just longer or shorter, as its controls are adjusted.

The dual input architecture of EXCITE and CV/GATE is architecturally more flexible than a single gate input and rewards investigation beyond basic single-input operation. EXCITE's internal conditioning produces a consistent pluck attack from any gate length, which solves the common problem of a long gate from a sequencer producing a different attack shape than a short trigger from a clock. CV/GATE's direct pass-through then handles the sustain portion of the event using whatever envelope or modulation source is appropriate for the musical moment. Patching Zadar into CV/GATE while Hermod+'s gate drives EXCITE means the attack shape is always the pluck character of the LPG regardless of sequence timing, while the sustain is shaped by Zadar's envelope independently. This separation of attack and sustain into two independently patchable sources makes the SSG Stereo Field a more expressive and adaptable dynamics processor than a module with a single gate architecture, without requiring any additional envelope or VCA modules.

The stereo field processor is not a mixer or a panner in the conventional sense; it operates on the perceptual relationship between the two channels rather than simply adjusting their amplitude balance. Centering the FIELD knob in stereo operation produces a mono sum, but moving it toward ST or -ST does not simply increase the amplitude difference between channels as a standard pan control would. The NEAR/FAR distinction maps to the psychoacoustic difference between how sounds from close and distant sources reach the listener, with far sounds having different frequency characteristics than near ones. This means that the FIELD control changes the character of the stereo image qualitatively as well as positionally; a sound processed in FAR mode with FIELD turned past ST does not sound like the same sound panned hard left but rather like a sound that exists at a specific distance and position in acoustic space. For a modular system that spends most of its time producing sources and modulators without stereo awareness, the SSG Stereo Field provides a final stage that makes the output sound as if it occupies physical space.

QAOS addresses one of the practical limitations of high-resonance filter use in long-form or generative patches. A filter locked to a fixed Q value in a patch running for an hour develops an audible quality of mechanical repetition; the resonance produces the same narrow peak on every cycle, and the ear locks onto it as a static element rather than registering it as part of a living sound. QAOS injects stochastic variation into the Q-FACTOR control, which means the resonance is never quite the same twice even when the Q knob has not moved. The variation is light rather than chaotic; it does not destabilize the filter's pitch or produce random output, but it prevents the ear from locking onto a fixed resonant frequency over time. In stereo operation this effect becomes asymmetric between the two channels, introducing a subtle difference between left and right resonance behavior that further prevents the processed stereo image from sounding like two identical channels. For ambient and generative work where the patch runs without intervention, QAOS is the difference between a filter that stays alive over an hour and one that ceases to be interesting after twenty minutes.

---

## Patches

### Patch 1: Mono LPG Voice

Steady State Fate SSG Stereo Field as a basic low-pass gate for a single mono voice, establishing the fundamental coupled filter-amplitude behavior using only the EXCITE input.

```
[Hermod+ Gate Out] ──────────[G]──────▶ [SSG Stereo Field EXCITE]

[Cs-L Audio Out] ────────────[A]──────▶ [SSG Stereo Field IN-L]
[SSG Stereo Field OUT-L] ────[A]──────▶ [MixUp CH1]
[SSG Stereo Field ENV OUT] ──[C]──────▶ [Zadar Trigger CH1]

                                         FREQ: 75% travel
                                         DECAY: middle
                                         TIMBRE: SAT, slider lower third
                                         Filter: 2PLP
                                         FIELD: center M, NEAR
```

**Setup:** Patch the Instruo Cs-L into IN-L and OUT-L into a mixer channel. Connect Hermod+'s gate output to EXCITE. Set FREQ to 75%, DECAY to center, and select the 2PLP filter type. Route ENV OUT to Zadar's trigger input for a later step. FIELD should be at center M with NEAR selected, which keeps the mono signal tonally flat through the module.

**Controls:** Trigger Hermod+ and hear the LPG open and close. Adjust FREQ downward and notice the pluck darkens; the filter's ceiling drops, so the sound never fully opens to its original brightness. Move DECAY upward and the gate sustains longer before closing; the coupled filter-amplitude decay extends together. Switch the filter type from 2PLP to 1PLP and notice the decay sounds shorter even at the same DECAY slider position, because the single-pole topology has a different frequency-to-amplitude curve. Increase SAT amount on the TIMBRE slider and the sustained portion of the gate gains warmth and soft harmonic saturation. The ENV OUT jack is now producing an envelope that tracks this gate; check with a scope or patch it forward to Zadar to trigger a secondary envelope that follows the primary gate timing without requiring a separate trigger cable.

**Result:** A single mono voice where filter brightness and amplitude are coupled through one control, producing pluck and bloom behavior that changes character with every FREQ and DECAY combination rather than simply adjusting duration.

---

### Patch 2: Dual Input Dynamics

EXCITE and CV/GATE used simultaneously, with EXCITE providing the attack pluck and Zadar providing a separate envelope for the sustained portion, separating the attack and sustain shapes into two independently controlled dimensions.

```
[Hermod+ Gate Out] ──────────[G]──────▶ [SSG Stereo Field EXCITE]
[Zadar CH1 Env Out] ─────────[C]──────▶ [SSG Stereo Field CV/GATE]
[Hermod+ Gate Out] ──────────[G]──────▶ [Zadar Trigger CH1]

[Cs-L Audio Out] ────────────[A]──────▶ [SSG Stereo Field IN-L]
[SSG Stereo Field OUT-L] ────[A]──────▶ [MixUp CH1]

                                         FREQ: 80% travel
                                         DECAY: lower third
                                         TIMBRE: FOLD, slider middle
                                         Filter: 1PLP
                                         FIELD: center M, NEAR
```

**Setup:** Patch Hermod+'s gate to both EXCITE and to Zadar's trigger input. Patch Zadar's envelope output to CV/GATE. With EXCITE receiving the gate directly, the LPG gets the pluck conditioned attack; with Zadar's envelope going into CV/GATE, the sustain shape is determined by Zadar's attack-hold-decay curve rather than by the DECAY slider alone. Set DECAY to the lower third so it contributes a short natural release after Zadar's envelope closes. Set FREQ to 80% to allow full opening. Switch TIMBRE to FOLD and set the slider to middle.

**Controls:** Adjust Zadar's envelope shape. A long attack on Zadar makes the LPG swell open after the initial pluck rather than opening immediately; the pluck from EXCITE provides the transient, and Zadar's attack determines how long the filter and amplitude rise to their full state. A short sharp Zadar envelope gives full dynamic range in a short event with a distinct pluck at the beginning. Set Zadar to a longer hold and shorter decay for a sustained gate with a clear attack transient. The TIMBRE FOLD mode interacts with this dynamic: as Zadar's envelope rises and the signal amplitude increases, the wavefolder's threshold is crossed and harmonics appear, fading back as the envelope closes. This harmonic-amplitude coupling happens automatically from the combination without additional modulation patching.

**Result:** A voice with two independently shaped envelope dimensions: a pluck attack from EXCITE and a sustained shape from Zadar. The wavefolder's interaction with the signal amplitude adds harmonics that appear and disappear in time with the Zadar envelope, producing a naturally evolving timbre that no static filter setting produces.

---

### Patch 3: QAOS Filter Character with Modulated TIMBRE

SSG Stereo Field as a heavily processed VCF in static mode (no EXCITE or CV/GATE), with QAOS active, wavefolder modulated by Zadar, and FREQ modulated by the Bela Gliss Record Loop output, exploring the module's continuous filter behavior without gating.

```
[Zadar CH2 Env Out] ─────────[C]──────▶ [SSG Stereo Field TIMBRE CV]
[Gliss Top Out] ─────────────[C]──────▶ [SSG Stereo Field FREQ CV]

[Cs-L Audio Out] ────────────[A]──────▶ [SSG Stereo Field IN-L]
[SSG Stereo Field OUT-L] ────[A]──────▶ [MixUp CH1]

                                         EXCITE: nothing patched
                                         CV/GATE: nothing patched
                                         FREQ slider: 50% travel
                                         DECAY: inactive (no gate input)
                                         TIMBRE: FOLD, slider middle
                                         QAOS: active (both switches on)
                                         Filter: BP
                                         FIELD: center M, FAR
```

**Setup:** Leave EXCITE and CV/GATE unpatched; the SSG Stereo Field runs as a static VCF with amplitude fully open. Select the BP filter type to produce a band-pass response. Set FREQ to 50% travel. Activate QAOS using the switch in the TIMBRE section and confirm it is also active on the Q-FACTOR switch. Set TIMBRE to FOLD with the slider at middle. Patch Zadar's second channel envelope output to the TIMBRE CV input; Zadar will sweep the wavefolder depth. Patch the Bela Gliss Top Output, set to Record Loop mode with a drawn slow modulation gesture, to the FREQ CV input. Set FIELD to center M with FAR selected; in FAR mode at center position, FIELD provides extended tone shaping for the mono source.

**Controls:** The Bela Gliss loop moves the band-pass filter's center frequency through a user-drawn shape, producing frequency sweeps that follow whatever gesture was recorded rather than a sine or triangle wave. Zadar's envelope sweeps the wavefolder depth in and out, adding harmonics as the fold amount rises and reducing to the raw band-passed signal when the envelope falls. QAOS causes the filter resonance to wander; increase Q-FACTOR until the filter rings and then activate QAOS to hear the ringing become unstable and alive rather than fixed at one pitch. Adjust the FIELD control away from center while in FAR mode to add high-frequency shaping on top of the band-pass character; this is cumulative and can produce a complex tonal shape that the BP filter alone does not achieve.

**Result:** A continuously processing filter voice where frequency follows a hand-drawn gesture, timbre evolves with a Zadar envelope, and resonance wanders under QAOS control. No gate event required; the module runs continuously and changes with every movement of the modulation sources.

---

### Patch 4: Stereo Field Processing with Live FIELD CV

SSG Stereo Field receiving two mono sources into left and right inputs, using FIELD CV from Zadar to sweep the stereo image automatically, with EXCITE triggering from Hermod+ for rhythmic LPG gating of the full stereo bus.

```
[Hermod+ Gate Out] ──────────[G]──────▶ [SSG Stereo Field EXCITE]
[Zadar CH1 Env Out] ─────────[C]──────▶ [SSG Stereo Field FIELD CV]
[Hermod+ Gate Out] ──────────[G]──────▶ [Zadar Trigger CH1]

[Cs-L Audio Out] ────────────[A]──────▶ [SSG Stereo Field IN-L]
[2hp Swarm Audio Out] ───────[A]──────▶ [SSG Stereo Field IN-R]

[SSG Stereo Field OUT-L] ────[A]──────▶ [MixUp CH1 L]
[SSG Stereo Field OUT-R] ────[A]──────▶ [MixUp CH1 R]

                                         FREQ: 85% travel
                                         DECAY: middle
                                         TIMBRE: SAT, slider lower third
                                         Filter: 2PLP
                                         QAOS: off
                                         FIELD knob: center M
                                         NEAR/FAR: FAR
```

**Setup:** Patch the Instruo Cs-L into IN-L and 2hp Swarm into IN-R; these two mono sources become the left and right legs of a constructed stereo image. Patch both OUT-L and OUT-R into a stereo mixer. Set FIELD to center M as a starting position with FAR selected. Patch Zadar's first channel envelope to the FIELD CV input and Hermod+'s gate to both EXCITE and Zadar's trigger. FREQ to 85%, DECAY to middle, TIMBRE to SAT at low depth; the SAT keeps both sources slightly warm without adding obvious distortion.

**Controls:** With Hermod+ running, the LPG gates the entire stereo bus simultaneously; both channels open and close together on each trigger, which means the stereo image gates as a unit rather than as separate mono sources. Zadar sweeps the FIELD CV with its envelope, moving the stereo field position automatically in time with the gate rhythm. At center M, both channels sum. As FIELD moves toward ST in FAR mode, the Cs-L on the left and the Swarm on the right separate into a widened stereo image with FAR-mode tonal shaping applied. As it moves past ST, the image continues to widen and side content extends. Tune Zadar's attack to be longer than the initial pluck decay so the stereo field sweeps open as the gate sustains. Adjust the FIELD CV amount by attenuating Zadar's output or by adjusting the Zadar channel's level to control how far into the stereo field the sweep travels. Try switching NEAR/FAR during playback; the same FIELD CV position produces a different spatial character, with NEAR emphasizing close-field and NEAR/FAR transitions changing whether the field sweeps toward presence or distance.

**Result:** A stereo bus processor where rhythmic LPG gating and automated stereo field positioning are synchronized to the same gate rhythm, producing a combined dynamic-spatial movement that treats the stereo image as a live performance parameter rather than a fixed mix position.

---

## Common Mistakes

### "The module is not gating: audio passes through constantly even with nothing at the gate inputs"

The SSG Stereo Field operates as a static VCF with amplitude fully open when nothing is patched to EXCITE or CV/GATE. This is correct behavior, not a malfunction. Without a gate signal present, the module is designed to pass signal continuously so it can be used as a filter without gating.

**Fix:** Patch a gate, trigger, or CV signal into EXCITE or CV/GATE to activate the LPG behavior. EXCITE accepts any gate or trigger from a clock, sequencer, or keyboard. CV/GATE accepts envelopes and LFOs as well as gates. Either input activates the LPG and enables the DECAY control; without at least one patched, the gate stage does not operate.

---

### "The filter never fully opens, even with EXCITE receiving a strong gate signal"

The FREQ slider must be set to at least 75% of its travel to allow the filter to open completely when a 5V gate signal is applied. Below this threshold, the filter ceiling is set too low and the LPG never reaches full brightness regardless of gate amplitude or DECAY setting.

**Fix:** Move the FREQ slider to at least 75% travel when using EXCITE or CV/GATE to open the filter. If the filter still sounds closed or muffled, also verify that the incoming gate level is close to 5V; levels significantly below this interact with the FREQ ceiling in ways that reduce the maximum opening further. Once the filter opens fully, bring the FREQ slider back down to shape the timbre rather than limit the ceiling.

---

### "Long gates produce the same attack shape as short triggers: I cannot get a slow fade-in"

EXCITE internally conditions any incoming gate or trigger into a short pluck regardless of the incoming signal's duration. It does not pass the gate's length; it extracts an attack transient from it. Long gates and short triggers produce the same attack shape through EXCITE, which is the intended behavior for that input.

**Fix:** Use CV/GATE instead of EXCITE, or use both simultaneously. CV/GATE passes the full duration and shape of the incoming signal, so patching a slowly rising envelope from Zadar into CV/GATE produces a slow LPG fade-in that follows the envelope's attack. Patching both EXCITE and CV/GATE at the same time gives the initial pluck from EXCITE plus the sustained follow-through from CV/GATE, which provides a sharp attack with a shaped sustain.

---

### "The TIMBRE CV is causing the volume to drop, not just changing the timbre character"

Sufficiently negative CV applied to the TIMBRE input ducks the output level in FOLD and SAT modes. This is not a malfunction; negative polarity CV in those modes actively reduces amplitude as well as decreasing the effect amount.

**Fix:** Offset the TIMBRE slider to a higher position before applying a bipolar LFO or envelope to TIMBRE CV. The slider position sets the DC offset, so starting at middle travel means that the most negative CV brings the effective TIMBRE level to zero rather than going below zero and ducking the signal. If using a unipolar positive CV (0V to +5V) for TIMBRE modulation, this ducking does not occur and the slider can be set lower.

---

### "FIELD does not do anything audible when I turn it: the stereo image sounds the same"

FIELD's behavior depends on whether IN-L and IN-R are both patched, which input carries which signal, and which NEAR/FAR mode is selected. With only one input patched and only one output used for mono operation, FIELD functions as a tone control rather than a stereo field processor, and its effect may be subtle at center positions.

**Fix:** For stereo field operation, confirm that both IN-L and IN-R carry signals and that both OUT-L and OUT-R are patched to a stereo destination. Set the NEAR/FAR switch to FAR for the widest range of field behavior. Turn FIELD from center M toward ST or -ST and listen in the stereo output; the image should shift spatially. For mono tone shaping, switch to FAR mode and turn the knob past the ST or -ST markers to reach the extended tone shaping range described in the manual.

---

### "Increasing Q-FACTOR produces a whistling tone that makes the whole patch too bright and harsh"

Setting Q-FACTOR high enough to approach or cross the self-oscillation calibration point produces strong resonant ringing that dominates the filtered signal, particularly with narrowband filter types like BP. This is expected behavior at high Q settings.

**Fix:** Reduce Q-FACTOR below the sine wave calibration mark if the ringing is unwanted. Alternatively, activate QAOS, which limits the effective Q-FACTOR range and adds stochastic variation to the resonance rather than holding it at a sharp fixed peak. QAOS prevents the filter from locking into a single resonant pitch and produces a more organic, less strident high-Q character. If some resonance is wanted without the harshness, QAOS at moderate Q-FACTOR settings typically produces the best balance between filter character and musical usability.

---

## Advanced Learning Path

Begin with the EXCITE input only and work through all three filter types systematically: listen to the same gate and source through BP, 1PLP, and 2PLP at the same FREQ and DECAY settings, and notice how the perceived decay length and character differ even when the slider positions are identical. The 2PLP rolls off more steeply and produces a darker, longer-seeming decay; the 1PLP is more open and tracks more of the high-frequency content through the decay tail; the BP peaks in the midrange and produces the most obviously tonal gate character. Understanding these three behaviors before adding any additional complexity is the foundation for choosing the right filter type for a given source material.

Explore the EXCITE and CV/GATE combination systematically. Begin with only EXCITE patched and identify the pluck character it produces from your gate source. Then add a cable from the same gate into CV/GATE and notice that the gate's full duration now passes through in addition to the EXCITE pluck. Then replace the CV/GATE connection with a Zadar envelope and shape the sustain portion independently from the attack. Work through Zadar envelope shapes ranging from instant-attack short-decay (for a double-contour event with pluck then quick close) to slow-attack long-hold (for a swell that opens after the initial pluck). This parameter space defines what the SSG Stereo Field can do as a dynamics processor beyond what any single-input LPG achieves.

Spend dedicated time with TIMBRE FOLD mode and study how the wavefolder interacts with signal level. Set FREQ high enough that the filter is fully open, disable the gate inputs, and send a continuous tone through the module. Increase the TIMBRE slider slowly and listen to the wavefolder add harmonics. Then modulate the signal level with an external VCA while the TIMBRE slider is at a fixed position; notice that the harmonic content changes with amplitude even though the TIMBRE control did not move. This amplitude-to-timbre relationship is the core of why the LPG plus wavefolder combination sounds different from either alone; building intuition for it through direct experiment is more productive than any description.

Investigate QAOS behavior across all three TIMBRE modes. Activate QAOS in FOLD mode; note how the wavefolder interacts with the stochastic resonance. Switch to SAT with QAOS; note that the saturation character becomes less predictable. Switch to QAOS as the primary TIMBRE mode (not FOLD or SAT, just QAOS active on its own) and listen to what QAOS contributes without the fold or saturation coloring. Then turn the QAOS switch below Q-FACTOR to deactivate it completely across all modes and compare the filter behavior with and without stochastic resonance variation. This comparison makes clear exactly what QAOS adds to the module's character across its full parameter range.

Use ENV OUT as a derive-and-forward signal in larger patches. Patch ENV OUT to a second module's CV input, a VCA's control input, or an Aurora Warp CV input, and observe that the downstream module now responds to every gate event through the SSG Stereo Field without requiring a separate envelope generator or a mult. Build a patch where ENV OUT simultaneously feeds Zadar as a re-trigger source, an attenuator going to another module's frequency, and the DECAY CV of the SSG Stereo Field itself, creating a self-feedback loop where the module's own envelope duration modulates its future decay time.

For stereo operation, work through the psychoacoustic panning technique described in the manual: patch a single mono source into IN-R only, patch both OUT-L and OUT-R to a stereo mixer, set FIELD to FAR mode, and use the FIELD knob to position the mono source across the stereo field in a way that sounds like a position in physical space rather than a simple amplitude pan. Compare this to a standard pan position on the mixer at the same apparent location and notice the tonal difference between psychoacoustic positioning and amplitude-only panning. Then add FIELD CV from a slow LFO or a Bela Gliss Record Loop and automate this spatial position over time.

Construct the stereo signal design workflow described in the manual: patch two mono sources that differ in frequency and harmonic content into separate mixers, add a centered element (kick, bass, or low drone) to both mixers at the same level, then route both mixer outputs into IN-L and IN-R. In FAR mode, the centered element does not shift in the stereo field regardless of FIELD position, but the differing elements do. This technique produces a stereo image where the centered elements remain stable while the differing elements move with FIELD control, which is more controllable than a simple stereo mix and produces a more defined spatial stage.

For advanced modular integration, run the SSG Stereo Field's stereo output through Qu-Bit Nautilus set to a long reverb decay, and use the SSG Stereo Field ENV OUT as Nautilus's Resolution CV. Each gate event at the SSG Stereo Field advances Nautilus's internal state, coupling the reverb character to the gate rhythm rather than letting it run autonomously. Simultaneously modulate SSG Stereo Field's FREQ CV from Nautilus's Sonar output, creating a reciprocal relationship where the LPG's filter ceiling is modulated by the reverb state and the reverb's internal timing is modulated by the LPG's gate. This type of cross-modulation patch produces behavior neither module generates independently and rewards extended experimentation with gate timing, DECAY length, and Nautilus resolution settings.

---

## Pairs Well With

**Instruo Cs-L** is the natural primary voice source for the SSG Stereo Field because its sine and other waveform outputs are tonally stable sources that let the LPG's filter and wavefolder character be heard clearly without interference from a complex source waveform. The Cs-L's internal FM capability means that patching the SSG Stereo Field's ENV OUT to the Cs-L's FM index produces timbre-from-dynamics modulation where the LPG's opening and closing also shapes the source oscillator's spectrum in sync; the result is a voice where the harmonic content and amplitude derive from the same gate event through two different physical mechanisms.

**Zadar** provides the most direct complement to the SSG Stereo Field's dual input architecture. Patching Zadar into CV/GATE while a clock gate drives EXCITE separates attack and sustain into independently controlled stages, and Zadar's four-channel design means that up to three additional parameters on the SSG Stereo Field (TIMBRE CV, FREQ CV, FIELD CV) can receive independently shaped envelopes from the same trigger source, all synchronized without additional patching. When the SSG Stereo Field's ENV OUT feeds back to Zadar as a retrigger input, the two modules create a gate-envelope relationship where the envelope duration and the LPG behavior stay locked regardless of sequencer timing drift.

**Qu-Bit Nautilus** receives ENV OUT well as a Resolution CV input, coupling the reverb's internal state to the LPG's gate rhythm rather than letting both run on independent timescales. Nautilus's Sonar output, which derives stepped control voltage from the reverb's internal delay state, makes an effective FREQ CV source for the SSG Stereo Field: the filter ceiling changes with the reverb's own evolution, producing a self-referential patch where the LPG's brightness follows the reverb's history. This feedback topology produces emergent complexity from two modules that neither generates independently.

**2hp Swarm** as a second source into IN-R completes the stereo pair with a harmonically dense unison voice that contrasts with a single-oscillator source in IN-L. Swarm's detuned unison character occupies a wider frequency band than a single Cs-L oscillator, which means the two channels passing through the SSG Stereo Field have genuinely different spectral content; when FIELD processes them, the side content that expands with FIELD rotation carries the Swarm's detuned density rather than a matched copy of the same source. This difference in spectral character between left and right is what makes the stereo field processing musically interesting rather than just spatially wider.

**Bela Gliss** in Record Loop mode provides FIELD CV from a hand-drawn gesture rather than a fixed LFO waveform, which means the stereo field position follows an exact shape drawn by the performer. Patching the Gliss Top Output to FIELD CV and the Bottom Output to FREQ CV simultaneously drives both the spatial positioning and the filter ceiling from the same physical gesture, creating a linked stereo-and-timbre movement that feels gestural in a way that independent LFO modulation does not replicate. For live performance, this combination makes the SSG Stereo Field's stereo output a directly playable spatial instrument rather than an automated processor.

**Qu-Bit Aurora** receives the SSG Stereo Field's stereo output well, because Aurora's FFT-based spectral processing operates on the full frequency content of its input and the SSG Stereo Field's wavefolder adds overtones that Aurora can redistribute, blur, or spectrally freeze in ways that a simpler filtered source does not provide. Setting Aurora to high FFT sizes and long decay with the SSG Stereo Field's FOLD mode active produces spectral textures where the harmonics generated by the wavefolder are sustained independently by Aurora after the LPG gate closes, creating a sustained tail of harmonics that outlasts the gate event itself.
