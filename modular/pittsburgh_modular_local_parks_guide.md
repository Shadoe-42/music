---
title: Local Parks
manufacturer: Pittsburgh Modular
primary_role: SOURCE
secondary_roles: []
historical_context: true
form_factor: eurorack
functions: [oscillator, wavefolder]
behavior_tags: [nonlinear, evolving, harmonic, percussive]
use_cases: [textural oscillator, dual-waveform layering, experimental lead, blade morphing]
hp: 14
depth: 25mm
memory: none
transport: none
screen: false
hybrid: false
cv: full
---

# Local Parks

**Experimental analog oscillator with next-generation waveshaping: blade morphing, dual-dimension pulse, and built-in self-patching modulation LFO**

![Pittsburgh Modular Local Parks](https://github.com/Shadoe-42/music/raw/main/modular/images/pittsburgh_modular/local_parks/front_panel.jpg)

## Historical Context

The waveform palette of the analog voltage controlled oscillator has been effectively fixed since the early 1970s. Sine, triangle, sawtooth, square: four waveform geometries derived from the physics of oscillating circuits, each with a characteristic harmonic content that synthesis practice has spent five decades combining, filtering, and modulating. The Minimoog had all four. The ARP 2600 had them. The Moog modular had them. The Buchla 200 series approached waveforms differently: Don Buchla's Complex Oscillator paired two oscillators in a waveshaping relationship that produced waveforms outside the basic four, but the underlying geometry of the individual waveforms remained the same sine, triangle, and sawtooth shapes.

Pulse Width Modulation became the primary tool for adding movement to the square wave within this fixed palette. Varying the duty cycle of a square wave (the ratio of time the wave spends high versus low in each cycle) changes its harmonic content continuously, producing the chorusing, thickening effect associated with synthesizers like the Roland Juno-106 and Jupiter-8. The Juno's DCO (digitally controlled oscillator) with its chorus effect and simultaneous PWM became one of the defining sounds of early 1980s synthesis precisely because PWM was one of the few mechanisms available for creating movement within the fixed waveform vocabulary. The palette was not expanded; instead, one of its members was given a single degree of freedom.

Pittsburgh Modular was founded by Richard Nicol in Pittsburgh, Pennsylvania, and the company's oscillator development runs from the Voltage Lab through the SV-1 semi-modular and the Primary Oscillator. Each iteration refined the same core circuit. The Local Parks is their departure from that refinement process: it retains the Pittsburgh oscillator core and its four standard outputs, then adds three waveforms that do not exist in the canonical analog palette. The Blade wave is a morph between a sawtooth running one octave above the core frequency and a square-adjacent shape at the core frequency, a waveform that changes both pitch relationship and harmonic content simultaneously as a single continuous knob gesture. The Pulse wave retains standard Width control but adds Pulse Shift, which inserts a flat step of adjustable height into the waveform cycle, creating a geometry outside what duty-cycle control alone can produce. Pittsburgh calls this "next generation waveshaping" in the module description, and the specific claim is defensible: the Blade and the shifted Pulse are waveform geometries the analog tradition did not have a name for before this instrument.

---

## Quick Start

The Local Parks is an analog oscillator with seven simultaneous outputs and an internal modulation LFO that self-patches to FM, blade shape, and pulse width when those inputs are unpatched. Start here with the blade output before exploring the rest.

1. Patch the Pitch output of a sequencer or keyboard CV into the Pitch input. Patch the Blade output into a filter or mixer.
2. Set the Coarse knob to a comfortable pitch register. Set the Blade knob to fully counterclockwise (minimum).
3. You should hear a sawtooth tone pitched one octave above where the Coarse knob suggests; this is the blade wave at its pure octave-up state.
4. Slowly turn the Blade knob clockwise. The wave morphs: pitch drops toward the core frequency and the harmonic character shifts toward a square-adjacent shape.
5. At maximum Blade, the wave is at the core frequency with a rounder harmonic content.
6. Now patch the Pulse (PW) output alongside the Blade output into separate mixer channels. Set P.Width to 12 o'clock and P.Shift to minimum.
7. Slowly increase P.Shift and hear the step appearing within the pulse waveform; a new harmonic texture not achievable with width alone.
8. With nothing patched into the FM, Blade CV, or Pulse Width CV inputs, the internal LFO is already modulating all three simultaneously. Set Mod Rate to 9 o'clock and listen to the combined animation at a slow rate.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 14 HP |
| Depth | 25 mm |
| Power | 85 mA +12V / 80 mA -12V / 0 mA +5V |

The +12V and -12V draws are nearly balanced at 85mA and 80mA respectively. Both rails are meaningfully loaded; confirm headroom on each bus independently before installing.

---

## The Oscillator Core and Standard Outputs

The Local Parks builds on Pittsburgh Modular's established analog oscillator core, developed through the Voltage Lab, SV-1, and Primary Oscillator. This core produces four simultaneous standard waveform outputs:

**Sine.** A pure sinusoidal waveform with no harmonic content above the fundamental. The sine output is clean and useful as a source through a filter (the filter adds harmonic content as resonance increases), as a sub-bass layer under a fuller waveform, or as the carrier in FM synthesis patches where harmonic cleanliness at the carrier matters.

**½ Sine (Half Sine).** A half-rectified sine wave: the positive half-cycle passes, the negative half-cycle is clipped to zero. The result adds harmonics that the full sine does not contain, producing a tone Pittsburgh describes as sounding "nice through a filter." The half sine is fuller than a pure sine but less harmonically dense than a triangle; it occupies a useful middle register for filter-based processing.

**Triangle.** A triangle wave has odd harmonics that fall off quickly (at the square of harmonic number), producing a hollow, flute-adjacent tone. Softer than saw or square. Useful as a starting point for subtractive synthesis when the saw's brightness is too much.

**Saw.** The sawtooth wave contains all harmonics, both odd and even, making it the most harmonically complete of the standard waveforms and the default choice for classic subtractive synthesis. Bright, cutting, and responsive to filtering. The saw output is the same core pitch as the Coarse and Fine knobs indicate.

These four outputs are always active and always available simultaneously. No switching is required.

**Coarse and Fine tuning.** The Coarse knob sets the primary pitch register. The Fine knob trims within a semitone range. The Octave Switch shifts the entire oscillator (all outputs including blade and pulse) one octave up or down from the Coarse position, giving a three-octave range without touching the Coarse knob.

**Pitch input.** The standard one volt per octave CV input. The pitch input tracks the standard 1V/Oct relationship: one volt of CV change shifts pitch by one octave.

**Hard Sync.** A gate input that resets the oscillator's waveform cycle to its starting point on each positive edge. Hard sync against a second oscillator running at a different frequency produces the characteristic hard sync sound: a complex waveform determined by the ratio between the two oscillators' frequencies, with a nasal, aggressive harmonic content. The synced oscillator's frequency determines the timbre; the master oscillator's frequency can be swept via CV for classic sync sweeps.

---

## The Blade Wave

The Blade wave is the Local Parks' most distinctive contribution to the oscillator's timbral palette. It is not a fixed waveform; it is a continuous morph between two states.

At minimum Blade knob position, the Blade output produces a sawtooth wave pitched exactly one octave above the core frequency set by the Coarse knob. If the Coarse knob is tuned to C3, the Blade output at minimum is a saw at C4. The octave relationship is fixed at this position.

As the Blade knob advances clockwise, two things happen simultaneously: the pitch descends from the octave-up position back toward the core frequency, and the waveform shape transitions from sawtooth toward a more square-adjacent character. At maximum Blade knob position, the output is at the core frequency with a harmonic content that has moved away from the pure saw brightness. The Blade output at maximum is not a standard square wave; it is the result of the morphing process, and its character sits between the saw and square regions of the waveform spectrum.

This simultaneous pitch and timbre relationship is what makes the Blade output unusual. Turning the knob is not just a timbre adjustment; it is also a pitch adjustment. A sequence driving both the Pitch input and a slow LFO into the Blade CV input produces melodic lines where the harmonic character and octave relationship of the blade output shift in sync with the LFO's movement, without any change to the pitch of the other outputs.

**Blade CV input and attenuator.** An external CV source into the Blade CV input modulates the blade knob position under voltage control. The attenuator sets the depth of this modulation. When no cable is patched into the Blade CV input, it receives the internal modulation LFO signal; the blade wave is already self-modulating at the LFO's current rate and depth (set by the Blade CV attenuator knob).

---

## The Pulse Wave: Width and Shift

The Pulse output gives the standard square/pulse waveform two independent dimensions of shape control rather than the single duty-cycle control found on conventional oscillators.

**Pulse Width (P.Width).** Standard duty-cycle control. At 12 o'clock, the pulse wave is a square wave with equal high and low times per cycle. Counterclockwise narrows the high time; clockwise widens it. All the standard PWM behavior applies here: narrow width produces a thin, nasal tone; wide width approaches a full square; moderate width with a slow LFO on the width CV produces the classic thickening PWM effect.

**Pulse Shift (P.Shift).** This control is specific to the Local Parks and has no direct equivalent on conventional analog oscillators. Pulse Shift inserts a flat step, a plateau of adjustable height, into the waveform cycle. The P.Shift knob sets the height of this step. At minimum, the step is absent and the waveform behaves as a standard pulse. As P.Shift increases, the step appears and grows, creating a waveform that has three distinct voltage levels in a single cycle rather than the standard two (high and low). This three-level structure produces harmonic content that Pulse Width alone cannot generate.

The interaction between Width and Shift is multiplicative: a narrow width with a high shift produces a different waveform geometry than a wide width with the same shift. Both dimensions are independently modulatable.

**Pulse Core Switch.** Selects the internal waveform used as the basis for generating the pulse wave. Up selects saw; down selects sine. The difference is subtle but audible at moderate width and shift settings: saw core adds brightness and a slight edge to the pulse; sine core produces a softer, rounder pulse character. Neither is standard; both are flavors.

**Pulse Width CV input and attenuator.** External CV modulates pulse width. When unpatched, this input receives the internal LFO; pulse width is self-modulating at the LFO rate. The attenuator sets the modulation depth.

---

## The Binary Logic Output

The Binary Logic waveform is the Local Parks' most experimental output. Pittsburgh Modular's documentation identifies it as a "Binary Logic waveform" without specifying the circuit topology, and the sonic character of this output is best understood through direct experimentation rather than technical description.

**Binary Switch.** A three-position switch that determines what appears at the Binary output jack. Up mixes the Binary Logic waveform with the Blade wave. Center outputs only the Binary Logic waveform. Down sums the Binary Logic with the Pulse wave. The switch makes the Binary output a combination point rather than a fixed waveform output.

**Binary CV input.** CV modulation of the Binary Logic waveform. When unpatched, this input receives the internal LFO.

The Binary output rewards patient experimentation. It is not the primary sonic character of the Local Parks.

---

## The Internal Modulation LFO

The Local Parks contains a built-in voltage controlled LFO (low frequency oscillator, a slow oscillator whose output is used to modulate other parameters rather than produce audible pitch) with a normalization system that self-patches its output to four inputs when no external CV is present.

**Mod Rate knob.** Controls the LFO frequency. The Mod Switch sets the active range: Up selects the high range (faster modulation); Down selects the low range (slower modulation).

**Modulation CV input and attenuator.** The Mod CV input accepts exponential frequency modulation of the LFO rate itself; the LFO's speed can be voltage controlled. The Mod CV attenuator scales the depth of this rate modulation.

**What the LFO normalizes to:**

- **FM input:** When no cable is patched into FM, the LFO drives linear frequency modulation of the oscillator. The FM CV attenuator controls the depth. With FM CV attenuator up and nothing patched, the oscillator's pitch warbles at the LFO rate. This is the strongest of the normalizations; with the attenuator high, the pitch deviation can be musically significant rather than subtle.

- **Blade CV input:** When no cable is patched into Blade CV, the LFO modulates the blade wave's morph position. The blade wave breathes through its octave and shape range at the LFO rate.

- **Binary CV input:** When no cable is patched into Binary CV, the LFO modulates the Binary Logic waveform.

- **Pulse Width CV input:** When no cable is patched into PW CV, the LFO modulates pulse width. The pulse wave breathes through its duty cycle at the LFO rate.

With all four inputs unpatched and the attenuators set to moderate depth, the Local Parks animates itself: the pitch warbles, the blade wave morphs, and the pulse width breathes, all at the same LFO rate but potentially at different depths. Setting the LFO to a musical rate (synced to patch tempo via external CV into Mod CV) and using it as the animation engine for a simple patch is a valid starting point before introducing any external modulation sources.

Patching any external CV into a normaled input breaks the LFO normalization for that input only. The remaining normaled inputs continue to receive the LFO.

---

## Signal Flow

```
[Hermod+ Pitch CV] ──[C]──▶ [Pitch In]
                                        ├──[A]──▶ [Sine Out] ──▶ [Mixer]
                                        ├──[A]──▶ [½Sine Out]
                                        ├──[A]──▶ [Triangle Out]
                                        ├──[A]──▶ [Saw Out]
[Hermod+ CV] ──[C]──▶ [Blade CV In]   ├──[A]──▶ [Blade Out] ──▶ [Filter] ──▶ [Mixer]
[Envelope] ──[C]──▶ [PW CV In]        └──[A]──▶ [Pulse Out] ──▶ [VCA] ──▶ [Mixer]
```

With Blade CV and PW CV patched from external sources, those two inputs are removed from LFO normalization. FM and Binary CV remain self-modulated by the internal LFO.

---

## Essential Parameters Summary

| Parameter | Function | Normalization |
|-----------|----------|--------------|
| Coarse | Primary pitch | none |
| Fine | Pitch trim | none |
| Blade | Blade wave morph (pitch and shape) | none |
| Mod Rate | Internal LFO frequency | none |
| P.Shift | Pulse step height | none |
| P.Width | Pulse duty cycle | none |
| Octave Switch | ±1 octave range | none |
| Binary Switch | Binary output mix | none |
| Mod Switch | LFO range (high/low) | none |
| Pulse Core Switch | Pulse basis (saw/sine) | none |
| FM CV Att | FM depth | LFO normaled |
| Blade CV Att | Blade CV depth | LFO normaled |
| Mod CV Att | LFO rate CV depth | none |
| P.Width CV Att | Pulse width CV depth | LFO normaled |

---

## Why Local Parks Excels

The Local Parks provides seven simultaneous outputs from a single oscillator core, which makes it one of the densest signal sources in the corpus relative to its panel space. A single pitch CV into the Pitch input produces blade, sine, triangle, sawtooth, pulse, sub, and binary logic signals simultaneously. In a patch with limited voices, this output density makes Local Parks function as a multi-timbral source: different outputs can feed different downstream processors, with each receiving a different waveform character from the same fundamental pitch. The result is harmonic layering without additional oscillators.

The blade wave is the module's most distinctive tonal contribution. Rather than a simple sawtooth or triangle, the blade wave morphs between an octave-up variation and the core frequency as the Blade knob advances, producing a continuous shift in both pitch register and harmonic character that is not achievable through standard waveshaping. The P.Shift control adds a second dimension to the pulse output by introducing a step discontinuity within the waveform cycle, generating harmonic content that differs from simple pulse width variation. These two controls give Local Parks a tonal identity distinct from a conventional analog oscillator.

The internal modulation LFO removes the dependency on an external modulation source for basic animation. When FM, Blade CV, and Pulse Width CV inputs are unpatched, the LFO automatically routes to all three simultaneously. A newly powered, minimally patched Local Parks is already in motion: FM depth, blade position, and pulse width all vary continuously at whatever rate the Mod Rate knob sets. For a patch in early assembly where a dedicated LFO has not yet been added, Local Parks provides a naturally animated output from the first cable placed.

## Advanced Learning Path

**Blade as a transposing voice in a chord patch.** With a chord source or multiple oscillators providing the root pitch, the Blade output adds a voice that sits one octave above when the Blade knob is at minimum and returns to the root register as the knob advances. In a chord context, this produces an octave doubling at one extreme and a unison voice with different timbre at the other. A slow LFO or envelope into Blade CV sweeps the blade voice between those two states during a sustained chord, creating movement within a held harmonic structure.

**Pulse Shift as timbral contrast between outputs.** Run the Pulse output and any of the standard outputs (saw or triangle) into separate filter channels. Set P.Width to 12 o'clock and advance P.Shift while listening to both. The pulse output's harmonic content changes in ways that the saw output does not track. The two channels of the filter will respond differently to the same Q and cutoff sweep because the source material has different harmonic distribution. Mixing the filtered results produces a texture that neither output generates alone.

**Hard sync with Blade CV swept.** Patch a second oscillator as the sync master into the Sync input. Set the Local Parks (slave) to a different coarse pitch. Hard sync produces a complex waveform at the master's pitch with a timbre determined by the frequency ratio. Now route a slow LFO into the Blade CV input (patching this breaks the LFO normalization for Blade CV). The blade wave's morph contributes additional timbral variation on top of the sync relationship, producing a slowly evolving harmonic texture that changes with both the sync ratio and the blade position.

**LFO normalization as a starting patch.** Before patching any external CV into the normaled inputs, set all four attenuators (FM CV, Blade CV, Binary CV, P.Width CV) to about 9 o'clock. Set Mod Rate to a slow position and Mod Switch to low range. With Blade and Pulse outputs into a mixer, the module will self-animate at a pace slow enough to hear each dimension of modulation separately. Raising the FM CV attenuator further introduces pitch warble; lowering it and raising the Blade CV attenuator shifts the animation to the blade morph only. This is a productive way to understand what each normalization contributes before replacing it with external control.

**FM CV for subtle vibrato versus wide pitch deviation.** The FM input is linear frequency modulation, which means the pitch deviation it produces is proportional to the modulation voltage rather than exponential. At low attenuator settings with the LFO normaled in, it adds subtle vibrato. At high attenuator settings with a faster LFO rate, it produces wide pitch deviation that can function as a limited form of FM synthesis when the deviation depth moves through audio rate. The Mod Switch high-range setting can push the LFO fast enough to approach audio-rate modulation of the FM input, blurring the boundary between LFO modulation and FM timbre shaping.

---

## Pairs Well With

**Hermod+ (Squarp Instruments).** Pitch CV, gate, and multiple modulation outputs from a single sequencer allow full simultaneous control of pitch, blade morph, pulse width, and LFO rate from one module. The Hermod+ CV outs can address each of the four normaled inputs independently, replacing all LFO self-modulation with sequenced parameter changes.

**MISO (Tiptop Audio).** The Local Parks' standard outputs are well-matched to MISO's mixing and attenuation capabilities. Blending saw and blade at adjustable ratios, or mixing triangle and half-sine before a filter, produces layered textures that the individual outputs alone do not provide.

**Qu-Bit Chord V2.** Chord V2 produces polyphonic pitch CV outputs. Patching different Chord V2 outputs to the Pitch and Blade CV inputs independently creates a patch where blade morph position tracks a different voice of the chord than the oscillator's base pitch; the blade waveform harmonically relates to one chord voice while the core pitch tracks another.

**Any analog filter.** The Local Parks' range of simultaneous outputs is most useful when different outputs go to separate filter instances with different settings. Saw through a low-pass and blade through a band-pass, mixed at the output stage, produces a layered harmonic texture that changes when either filter's cutoff moves. The half-sine output is particularly productive through filters because its harmonic content is minimal enough that the filter's own resonance behavior dominates the character.

**Pamela's Pro Workout (ALM Busy Circuits).** Clock-derived CV from Pamela addresses the Mod CV input (LFO rate), keeping the internal LFO synchronized to patch tempo. Euclidean gate outputs from Pamela into the Hard Sync input produce rhythmic sync reset patterns, resetting the oscillator waveform on rhythmically interesting subdivisions rather than at a steady rate.

**DivKid Ochd.** The Ochd's slow LFO outputs replace the internal LFO normalization on individual inputs with independent, phase-unrelated slow modulation sources. Blade CV from one Ochd output, PW CV from another, FM CV from a third: three independent slow movements at different rates producing layered animation that the single internal LFO cannot replicate.

---

## Common Mistakes

**Forgetting the blade wave changes pitch as well as timbre.** The Blade knob is not just a tone control. At minimum, the blade output is one octave above the core pitch. Patching blade into a pitch-dependent effect or alongside a tuned voice without accounting for this octave relationship produces a harmonic mismatch that sounds like a tuning error. Either tune the core pitch one octave up when using blade at minimum, or keep the Blade knob advanced toward the core pitch position for pitched ensemble work.

**Not accounting for LFO normalization depth.** With the FM CV attenuator turned up and nothing patched into the FM input, the internal LFO is driving pitch deviation. In a tuned patch where pitch stability matters, this normalization must either be patched out (any cable into FM breaks it) or the FM CV attenuator must be fully counterclockwise. A pitch that seems unstable or wandering with no obvious cause is usually the FM normalization active at a depth higher than intended.

**Treating Pulse Width and Pulse Shift as interchangeable.** They are independent shape dimensions that produce different results at the same knob position. At 12 o'clock, Width produces a square wave; Shift at 12 o'clock produces a specific step height that changes the waveform geometry independently. Rotating both simultaneously with the same modulation source is different from modulating each separately. Experiment with each in isolation before combining them.

**Expecting hard sync to produce subtle results.** Hard sync is not a gentle effect. Forcing the slave oscillator to reset its cycle at the master's frequency produces harsh, nasal waveforms that change dramatically with small frequency ratio changes. If a hard-synced patch sounds unexpectedly aggressive, this is the expected behavior. Use the Coarse and Fine knobs to find frequency ratios where the sync character matches the patch context; certain ratios produce more musical results than others.

**Underusing simultaneous outputs.** The Local Parks provides seven outputs simultaneously. A common initial approach is to use one output at a time, replacing the previous cable when trying a different waveform. This misses the module's strength entirely: sine and blade and pulse into three separate filter channels, each processed differently, produces a composite voice far richer than any single output processed alone.

---

## What's Next

The Local Parks covers oscillator fundamentals through standard outputs while adding blade morphing and dual-dimension pulse shaping as its primary expressive tools. With the standard and extended waveforms in hand, the productive next focus is filter behavior across different source waveforms: how the half-sine and blade wave respond to identical filter settings compared to saw and triangle, and how the blade's simultaneous pitch and timbre shift interacts with a resonant filter tracking pitch via V/Oct CV.

The signal chain literacy guide (modular/basics/06_signal_chain.md) covers the three-path model that underlies every voice built around the Local Parks. The filter guides in this corpus, particularly those covering multimode filters, apply directly to the multiple simultaneous outputs the Local Parks provides.

---

*Depth: 25mm. Power: 85mA +12V / 80mA -12V / 0mA +5V.*
