---
title: Winterbloom Castor & Pollux II
manufacturer: Winterbloom
primary_role: SOURCE
secondary_roles: []
form_factor: eurorack
functions: [oscillator, fx-modulation]
behavior_tags: [warm, stable, harmonic, bright, evolving]
use_cases: [lead voice, chord voice, lush stereo oscillator, bass voice]
hp: 18
memory: full
hybrid: true
---

# Winterbloom Castor & Pollux II

**The Modern Juno Twins**

![Winterbloom Castor & Pollux II](https://github.com/Shadoe-42/music/raw/main/modular/images/winterbloom/castor_pollux_ii/front_panel.jpg)

---

## Historical Context

The Roland Juno-106 arrived in 1984 as the third instrument in Roland's Juno series, following the Juno-6 and Juno-60. Its defining technical feature, shared across the entire Juno line, was the digitally controlled oscillator, or DCO. Conventional analog VCOs of the era were prone to pitch drift: temperature changes, component aging, and humidity caused them to wander from their set frequency in ways that required constant attention from players. Roland's solution was to drive the oscillator's frequency from a digital clock signal rather than a purely analog control voltage, giving the oscillator the pitch stability of digital control while keeping an analog signal path for the actual waveshaping and filtering. The Juno-106 extended its predecessors by adding MIDI capability at the moment the standard was becoming universal, and 128-patch memory. It sold in sufficient volume to define a generation of keyboard players' tonal vocabulary; the specific combination of stable DCO tone and the instrument's onboard bucket-brigade chorus became one of the most recognized sounds in 1980s recorded music.

Two specific hardware failures have become endemic to the Juno-106 over the decades since its manufacture. The first involves the 80017A voice chips: Roland coated these integrated circuits, each combining a filter and amplifier section on a single package, in an epoxy compound that gradually becomes electrically conductive as it ages. The coating degrades into a resistive fault across the chip's circuitry, causing individual voices to drop out, crackle on note attacks, or sustain indefinitely without releasing. Every unmodified Juno-106 remaining in circulation is at some stage of that process, and the failure rate increases with time. The second failure point is the MN3009 bucket-brigade delay chips in the chorus section, which age into noise and distortion as their substrates degrade. The chorus, a stereo two-mode BBD effect that became as sonically recognizable as the DCO tone itself, depends on chips that are no longer in production. Both failure modes shaped the context in which Thea Flowers approached the instrument.

Flowers is a software engineer and open-source advocate who came to hardware synthesis through technical curiosity rather than an instrument-making background. Before founding Winterbloom in April 2020 she worked in Developer Relations at Google, with expertise in open-source tooling, technical writing, and community engagement. She approached the Juno-106 not as a musician wanting to clone a beloved sound but as an engineer wanting to understand one specific circuit, the DCO design, well enough to implement it faithfully. She published a detailed technical analysis of the original oscillator architecture on her personal blog, working from the original Roland schematics to document exactly what the DCO did and why it behaved as it did. Castor & Pollux came directly out of that research: two DCOs implemented using a modernized version of the original Juno circuit, in Eurorack format, with all design files released publicly under an open-source license.

Winterbloom operated for five years. Flowers has been explicit that it was never intended to be permanent; she started it to demonstrate what open-source hardware development could look like when applied to musical instruments, and to show that well-documented, beginner-accessible hardware production was achievable from a one-person operation. When she wound the company down she moved to Opulo, continuing open-source hardware work in a different domain. The Castor & Pollux II designs remain fully public: schematics, firmware, and production files available for anyone to build, fork, or manufacture independently. The Juno-106 units that inspired the design continue failing one voice chip at a time in studios and instrument collections around the world. Castor & Pollux II is not a replacement for that instrument; it is a record of what made one specific part of it worth understanding.

---

## Quick Start

**What is Castor & Pollux II?** Two digitally controlled analog oscillators (DCOs) that faithfully recreate the Roland Juno-106 oscillator circuit in Eurorack format. Castor is the primary oscillator; Pollux is the secondary, typically detuned or configured differently. Both share waveform structure and pitch range. The CROSSFADE output blends between them. Three operational modes change the relationship between the pair: Chorus adds built-in BBD-style chorusing to Pollux; LFO FM applies an internal LFO to both oscillators' pitch; Hard Sync locks Pollux's cycle to Castor's for metallic, harmonically rich tones.

### First Sound

1. Connect a V/OCT source to the Castor PITCH CV input
2. Connect Castor OUT to a filter or directly to a mixer
3. Turn Castor's RAMP mix knob (small trim knob) fully clockwise
4. Play notes; you will hear the classic Juno sawtooth character
5. Press MODE once to reach Chorus mode (blue LED) and listen to the Pollux chorus layer
6. Adjust the CROSSFADE knob to blend in Pollux's output

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 18HP |
| Depth | ⚠️ Verify against official documentation |
| Power | ⚠️ Verify against official documentation |
| Oscillator type | Digitally controlled analog (DCO) |
| Waveforms per oscillator | Ramp, Pulse (with PWM), Sub (-1 octave) |
| Operating modes | Chorus, LFO FM, Hard Sync (LED color indicates active mode) |
| V/OCT tracking | 1V/octave, calibratable via web editor |
| Fine tune access | Hold MODE + turn pitch knob (±2.5 semitones) |
| Configuration | Browser-based web editor via micro USB |
| Expander | Optional 2HP expander for individual waveform outputs |

---

## Essential Parameters

**Castor and Pollux** are two identical DCO circuits that share the same fundamental oscillator architecture. Castor functions as the primary oscillator and is the one most often driven by the main V/OCT sequence. Pollux is the secondary oscillator, intended to be detuned, configured in a different mode, or blended in through CROSSFADE. Each oscillator has independent pitch control, independent waveform mix knobs, and independent output jacks. They can operate as two separate monophonic voices or as a coupled pair producing a combined output through the CROSSFADE jack.

**Pitch control** on each oscillator consists of a large coarse pitch knob and a 1V/octave CV input. The pitch knob response is non-linear around musical intervals, with a built-in "virtual notch" behavior that makes it easier to land on octaves and fifths by feel without visual reference. Tweak mode, accessed by holding the MODE button and turning a pitch knob, provides ±2.5 semitone fine adjustment without affecting the coarse setting. This is the correct way to set the Castor-to-Pollux interval precisely when detuning for thickness or programming a specific hard sync interval.

**Waveform mixing** on each oscillator uses three small trim knobs to set the relative level of RAMP (sawtooth), PULSE (square wave with PWM), and SUB (sub-oscillator at one octave below pitch). The combined output from all three waveforms exits from the oscillator's main output jack. The optional 2HP expander provides individual output jacks for each waveform if separate processing is needed. On the Juno-106, the mix of these three waveforms defined the tonal character; the same applies here. A Castor set predominantly to RAMP with a small PULSE contribution sounds close to the original Juno brass and pad character.

**The MODE button** cycles through three operational modes with a single tap. Chorus mode (blue LED) applies a built-in chorus effect to Pollux's oscillator, recreating the bucket-brigade chorus that defined the Juno-106's signature sound. LFO FM mode (green LED) routes an internal LFO to both oscillators' pitch inputs, producing vibrato, tremolo-pitch effects, or continuous pitch drift depending on rate and depth. Hard Sync mode (pink LED) locks Pollux's reset to Castor's cycle, creating the metallic, harmonically dense tones characteristic of hard-synced analog oscillators. Each mode has a Tweak overlay accessed by holding MODE, which exposes secondary parameters such as chorus depth, LFO rate, and sync interval that are not available from the main panel.

**CROSSFADE** is the primary output for combined operation. Fully counterclockwise, only Castor is audible. Fully clockwise, only Pollux is audible. At noon, both contribute equally. The CROSSFADE output also has a CV input that allows the blend to be modulated by envelope, LFO, or sequencer. Using CROSSFADE as a performance axis, sweeping the knob or modulating the CV during a phrase, morphs continuously between two different oscillator characters without a hard switch.

**The web editor** is a browser-based configuration tool accessible by connecting Castor & Pollux II via micro USB. It provides calibration controls for precise V/OCT tracking, LED brightness adjustment, default LFO rate and depth settings, and pitch behavior options including the Follow and Free modes for the coarse pitch knob. Calibration through the web editor is the correct way to ensure accurate 1V/octave tracking across the full keyboard range; panel knob tuning alone cannot achieve the same precision.

---

## Why This Excels

Castor & Pollux II is the only Eurorack module that provides an authenticated recreation of the Roland Juno-106's DCO circuit by someone who understood the circuit at the component level. Thea Flowers published a detailed technical analysis of the original Roland schematics before designing this module, which means the DCO implementation is not an approximation by ear or a generic analog oscillator with Juno-adjacent controls: it is the specific circuit, rebuilt with modern components, retaining the behaviors that made the original instrument's oscillator distinctive. This includes the non-linear tuning response, the specific waveform character of each shape, and the coupling between Castor and Pollux that produces the authentic Juno thickness when both oscillators are active.

The three-mode architecture removes the usual oscillator trade-off between simplicity and versatility. A chorus-capable oscillator, a pitch FM oscillator, and a hard sync oscillator would typically require three separate modules. Here they occupy 18HP, share calibration, and switch between modes instantly with a single button press. The CROSSFADE output adds a fourth dimension: live morphing between two differently configured oscillators within any mode. The available sound palette is genuinely large for the panel size.

The open-source design philosophy means that Castor & Pollux II will remain buildable, repairable, and forkable indefinitely. Winterbloom has wound down, but the schematics, firmware, and production files are public. The module is not dependent on continued manufacturer support. In a field where obsolescence is a constant concern, this design approach treats longevity as a feature rather than an afterthought.

---

## Patches

### Patch 1: Classic Juno Lead

This patch uses Castor alone in Chorus mode to produce the canonical Juno-106 lead sound.

```
[Sequencer] ──V/OCT──▶ Castor PITCH CV
             Castor OUT ──▶ [Filter] ──▶ [VCA] ──▶ [Mixer]
```

**Setup:** Connect a sequencer's V/OCT output to the Castor PITCH CV input. Connect Castor OUT to a VCF input, the VCF output to a VCA, and the VCA to a mixer. Set Castor's RAMP mix trim fully clockwise and PULSE mix at about 9 o'clock for a hint of square. Leave SUB mix fully counterclockwise. Press MODE until the blue LED lights (Chorus mode). Set CROSSFADE fully counterclockwise (Castor only).

**Controls:** Play the sequence and adjust the filter cutoff for the desired brightness. The RAMP-heavy waveform mix produces the characteristic Juno brightness without harshness. Try adding a small amount of PULSE content by bringing that trim knob slightly clockwise; the combination of sawtooth and narrow square at low mix is close to the original instrument's standard patch. Press and hold MODE to access the Tweak overlay for Chorus; adjust the secondary parameter to change chorus depth. Deeper chorus widens and thickens the sound; shallower settings keep it close to a straight DCO tone with subtle movement.

**Result:** An authentic Juno-106 lead voice with the DCO stability and chorus character that defined a generation of synthesizer recordings. The output is thick, stable, and immediately recognizable. Route it through a resonant low-pass filter swept by an envelope for the classic analog synth sound; the DCO character provides the brightness and the filter provides the tonal shaping.

---

### Patch 2: Detuned Dual Oscillator

This patch runs both Castor and Pollux, sets them to slightly different pitches, and blends them through CROSSFADE for classic analog thickness.

```
[Sequencer] ──V/OCT──▶ Castor PITCH CV
[Same Sequencer] ──V/OCT──▶ Pollux PITCH CV
                CROSSFADE Out ──▶ [Filter] ──▶ [Mixer]
```

**Setup:** Connect the same V/OCT source to both Castor and Pollux PITCH CV inputs. Connect CROSSFADE OUT to the signal chain. Set both oscillators to similar waveform mixes. Set CROSSFADE to noon. Press MODE until blue LED (Chorus mode). Use Tweak mode to detune Pollux slightly: hold MODE and turn the Pollux pitch knob a small amount clockwise until you hear the beating frequency between the two oscillators.

**Controls:** Set the detuning to a beat frequency of about 2 to 6 Hz. Faster beating sounds more intense and can feel harsh; slower beating sounds more subtle and adds width without obvious vibrato. Adjust CROSSFADE from noon toward Castor or Pollux to change the relative weight of each oscillator in the mix. Set Castor's waveform mix to favor RAMP and Pollux's to favor PULSE; the different waveform characters from each oscillator combine through CROSSFADE into a mixed timbre that neither produces alone.

**Result:** The thick, beating, wide oscillator sound that gives the Juno its characteristic presence. Both oscillators contribute to the output, and the slight frequency difference between them creates the natural chorus effect of two detuned analog oscillators. The Pollux chorus overlay (in Chorus mode) adds a third layer of motion on top of the natural detuning.

---

### Patch 3: Hard Sync Metallic Voice

This patch uses Hard Sync mode with Pollux's pitch swept to produce the bright, harmonically dense tones characteristic of hard-synced analog oscillators.

```
[Sequencer] ──V/OCT──▶ Castor PITCH CV
[Envelope or LFO] ──▶ Pollux PITCH CV (via attenuator)
             Pollux OUT ──▶ [Filter] ──▶ [Mixer]
```

**Setup:** Connect the V/OCT sequencer to Castor PITCH CV only. Connect an envelope or slow LFO to Pollux PITCH CV through an attenuator. Press MODE until the pink LED lights (Hard Sync mode). Connect Pollux OUT to the signal chain; in Hard Sync mode, Pollux produces the sync-modified output. Set Pollux's RAMP mix to noon.

**Controls:** In Hard Sync mode, Pollux's cycle is reset by Castor's cycle on each Castor period. Sweeping Pollux's pitch creates classic sync sweep tones: as the Pollux pitch rises relative to Castor, the harmonic content changes through a series of timbral positions that are determined by the ratio between the two frequencies. Connect an envelope to Pollux's PITCH CV input and listen to the timbre change across the envelope decay. Use the attenuator to control the pitch sweep range; wide range sweeps produce dramatic timbre changes while narrow range sweeps produce subtle formant movement.

**Result:** Metallic, harmonically rich tones with a pitch-controlled timbre sweep. Hard sync voices respond to pitch CV differently than normal oscillator voices: the same CV that would produce vibrato on a standard oscillator produces timbre change on a synced oscillator. This makes Pollux's PITCH CV input a timbre control rather than a pure pitch control in this mode.

---

### Patch 4: LFO FM Drift and Vibrato

This patch uses LFO FM mode to apply internal LFO pitch modulation to both oscillators, creating vibrato, organic pitch drift, or FM-like harmonic movement depending on rate and depth.

```
[Sequencer] ──V/OCT──▶ Castor PITCH CV
             CROSSFADE Out ──▶ [Filter] ──▶ [Mixer]
[MODE = LFO FM (green LED)]
```

**Setup:** Connect a V/OCT sequencer to Castor. Connect CROSSFADE OUT to the signal chain with CROSSFADE at noon. Press MODE until the green LED lights (LFO FM mode). Set both oscillators to complementary waveform mixes with the trims. Hold MODE to access the Tweak overlay and adjust the LFO rate and depth parameters.

**Controls:** At low LFO depth and moderate rate (around 5 to 7 Hz), LFO FM mode produces classical vibrato. Reduce the rate to below 1 Hz and the pitch drift becomes slow and organic, like a player pushing pitch on a string instrument. Increase depth with a fast rate (above 20 Hz) to enter FM territory: the two oscillators begin producing sidebands and the timbre becomes overtone-rich and metallic. Tune Pollux to a fixed interval above Castor using Tweak mode to change the harmonic relationship in the FM output; specific intervals produce characteristic FM timbral textures.

**Result:** A pitch-modulated dual-oscillator voice with wide tonal range from expressive vibrato to dense FM synthesis, all within the single module. The LFO FM mode makes Castor & Pollux II a credible FM voice source without any external modulation patching, and the sweep between vibrato and FM timbres is continuous rather than binary.

---

## Common Mistakes

### "I cannot hear any difference when I turn the waveform mix knobs"

Castor & Pollux II has two types of knobs: large performance knobs for pitch and crossfade, and small trimpot-style knobs for waveform mixing. The waveform mix knobs, which set the individual levels of RAMP, PULSE, and SUB for each oscillator, are small and physically easy to overlook. Each waveform mix starts at zero: if no waveform mix is turned up, the oscillator produces no output. A freshly patched Castor & Pollux with no waveform levels set will be completely silent despite working perfectly.

Turn up at least the RAMP mix knob on Castor before checking anything else. The small trimpots are labeled on the panel; once located, one or two careful turns will confirm they are working. After that, add PULSE and SUB incrementally to build the desired timbre.

### "I held down the MODE button and now things are behaving differently than I expected"

The MODE button has two distinct behaviors depending on how you press it. A quick tap cycles through the three main modes: Chorus (blue LED), LFO FM (green LED), and Hard Sync (pink LED). A long press activates the tweak overlay: a set of deeper parameters within the current mode, accessed by holding MODE while turning a knob. Accidental long presses change parameters that are not visible on the panel without the web editor, which can produce unexpected tuning or behavior changes that persist after you release the button.

If the module is behaving unexpectedly after a MODE press, open the web editor to check whether any tweak parameters were accidentally adjusted. For everyday operation, practice a deliberate quick tap rather than pressing and holding.

### "The oscillator is not tracking pitch accurately across the keyboard range"

Castor & Pollux II uses DCO technology with digital pitch control, but factory calibration may not be perfectly matched to a given system's voltage reference. Pitch tracking accuracy across multiple octaves depends on the calibration state of the module. An uncalibrated or slightly drifted module will track well in a narrow range around the calibration point and become increasingly inaccurate toward the extremes of the keyboard range.

Connect the module to a computer via micro-USB and open the web editor. Run the calibration procedure using a reference pitch from a tuner or the web editor's own calibration mode. Calibration takes approximately five minutes and significantly improves tracking accuracy across the full range. This is a normal part of setting up any precision oscillator, not a sign of hardware issues.

### "Hard Sync mode sounds like nothing is syncing"

Hard Sync mode requires Castor and Pollux to have a pitch relationship where the sync effect is audible. If both oscillators are tuned to the same pitch, sync produces minimal audible effect because the cycle boundaries are already aligned. The sync sound (the classic metallic overtone series) emerges when Pollux is tuned to a higher frequency than Castor: Castor's cycle resets Pollux mid-waveform, producing harmonic content determined by the interval between them.

In Hard Sync mode, tune Pollux up relative to Castor. The most immediate approach is to use the tweak overlay (hold MODE in Hard Sync mode) to fine-tune Pollux's pitch offset, or apply CV to the Pollux PITCH CV input while leaving Castor's pitch stable. The interval between the oscillators directly determines the character of the sync: small intervals produce subtle tonal shifts while large intervals produce the aggressive, classic sync sound.

### "The chorus effect is subtle but I expected something dramatic"

Chorus mode applies the built-in chorus to Pollux and then blends Pollux with Castor through the CROSSFADE output. The amount of chorus character in the final output depends on how much Pollux is present in the blend. With CROSSFADE fully counterclockwise (only Castor audible), the chorus has no effect on the output because Pollux is not present. With CROSSFADE at center, the chorus character is at half strength; with CROSSFADE fully clockwise, only the chorused Pollux is present.

Rotate CROSSFADE toward the center or further clockwise to bring in the chorused Pollux signal. Additionally, detuning Pollux slightly before engaging Chorus mode adds beating between the two oscillators that interacts with the chorus sweep, producing the thicker, more movement-rich character associated with the original Juno-106.

---

## Advanced Learning Path

1. Work through each MODE in dedicated sessions on the same simple patch. Set up Castor OUT to a mixer with no other processing. Play a steady single pitch or short two-note phrase in each mode (Chorus, LFO FM, Hard Sync) and listen to what changes between them. Then hold MODE in each setting to access the Tweak overlay and adjust the secondary parameter (chorus depth, LFO rate, or sync interval) while listening. Understanding what each mode does and what its secondary parameter controls is the foundation for all performance and sound design work with the module; it should not be rushed.

2. Practice the Tweak mode access until it is mechanical. Tweak mode requires holding the MODE button and turning a knob simultaneously. This is a two-hand operation that is easy to execute slowly but can be disruptive during live performance if it is not automatic. Spend time entering Tweak mode repeatedly until the action is comfortable and the LED response, which changes character to indicate Tweak is active, is immediately recognizable. The parameters accessible in Tweak mode are critical to voiced performance; anything that requires deliberate conscious thought to access becomes a liability during a set.

3. Explore the hard sync interval sweep methodically using a constant pitch input and a slowly sweeping Pollux pitch. Connect a fixed DC voltage (or a keyboard held at a single note) to Castor PITCH CV and leave Pollux's pitch controlled only by its own pitch knob. Enter Hard Sync mode. Slowly turn the Pollux pitch knob through its full range while listening to the harmonic content change. Map the positions at which you hear strong, clean harmonic tones versus harsh, unstable tones; those strong positions correspond to small integer ratios between Castor and Pollux frequencies (unison, octave, fifth, and similar). Note the Pollux pitch knob positions that produce the most musically useful timbres for future use.

4. Use CROSSFADE as a primary performance axis rather than as a set-and-forget blend control. In a patch where Castor and Pollux are in different modes or have different waveform mixes, CROSSFADE movement is a continuous timbre morph between two distinct voices. Automate this with a slow LFO at the CROSSFADE CV input to produce a voice that oscillates between two characters on a musical schedule. Faster LFO rates produce tremolo-like effects; very slow rates (one cycle per phrase or section) create gradual tonal evolution. The CROSSFADE CV input is one of the most musically productive modulation targets on the module.

5. Calibrate V/OCT tracking through the web editor before any recording session that requires accurate pitch. The web editor's calibration routine measures the oscillators' frequency response across the V/OCT range and compensates for any deviation from exact 1V/octave tracking. Without calibration, octave accuracy across the full pitch range is approximate; with calibration, it is precise. This distinction matters most on long melodic sequences where notes in different octaves need to be in tune with each other and with external instruments. Make calibration a standard part of setup before any session where pitch accuracy is critical.

6. Program patch pairs that deliberately contrast Castor and Pollux configurations so CROSSFADE becomes a sound design tool. Set Castor to full RAMP in Chorus mode and Pollux to full PULSE in LFO FM mode. The CROSSFADE output at noon is a blend of a chorusing sawtooth and a vibrating square, and sweeping CROSSFADE from end to end is a morph between two fundamentally different characters. Build a library of these contrasting configurations: one warm, one bright; one stable, one modulated; one with sub content, one without. The CROSSFADE axis between them is an expressive resource that most oscillators do not offer.

---

## Pairs Well With

**4ms Company Listen IO** handles monitoring and recording the stereo output that Castor & Pollux II is capable of producing. With CROSSFADE OUT routed to one channel of Listen IO and the individual Castor and Pollux outputs routed to another, the full stereo field of a dual-oscillator patch can be monitored through headphones and recorded through the line outputs simultaneously. The 30x gain range of Listen IO's input stage means it accommodates both the hot modular output level and the need for precise level control before the recording chain.

**A voltage controlled filter** is the direct companion of any DCO-based oscillator in the Juno tradition. The original Juno-106 pairing of DCO through Juno's own IR3109 filter was the defining signal chain of that instrument; the same principle applies here. A resonant low-pass filter with an envelope-controlled cutoff takes the bright, complex DCO output and shapes it into a note with attack and decay. Any VCF works; ones with lower-cost character and slight saturation at the input stage tend to complement the Juno brightness most naturally.

**Make Noise Maths** provides envelope generation for filter cutoff and amplitude control of voices driven by Castor & Pollux II. Maths' logarithmic decay curves produce the plucked and bowed attack shapes that physical instruments share; applied to a VCF cutoff driven by a Castor sawtooth output, the result is a synthesized string or brass note with physically plausible timbral arc. A single Maths channel generating both a gate and an envelope from the same trigger input eliminates the need for a separate envelope module in simple voice configurations.

**DivKid Ochd** supplies continuous pitch modulation for LFO FM mode without requiring any setup beyond a cable to Castor or Pollux PITCH CV. With one Ochd LFO sweeping Castor's pitch and a second slower LFO sweeping CROSSFADE, both the pitch and the blend between the two oscillators modulate simultaneously at different rates, producing a voice that drifts in character and timbre over time. Ochd's always-running design means the modulation starts immediately with no programming required.

**Intellijel Stomp** connects Castor & Pollux II to guitar amplifiers for physical speaker resonance and room acoustics. The DCO character of the module (stable pitch, complex waveform harmonic content) responds to amplifier saturation and speaker coloration in ways that reveal how close the Juno oscillator design is to the acoustic physics of string instruments. The combination of DCO output, amp character, and room microphone produces recordings where modular synthesis is genuinely indistinguishable from a recorded acoustic instrument.

---

*Castor & Pollux II schematics, firmware, and documentation: [Winterbloom on GitHub](https://github.com/wntrblm)*
