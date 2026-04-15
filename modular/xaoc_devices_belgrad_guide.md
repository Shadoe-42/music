---
title: Xaoc Devices Belgrad
manufacturer: Xaoc Devices
primary_role: SHAPER
secondary_roles: [SOURCE]
form_factor: eurorack
functions: [filter, wavefolder]
behavior_tags: [warm, harmonic, nonlinear, evolving, performance-oriented]
use_cases: [timbral movement and shaping, complex filter character, self-evolving patch element]
hp: 14
---

# Xaoc Devices Belgrad Guide

**Dual-Core State Variable Filter**  
**Manufacturer:** Xaoc Devices  
**Format:** Eurorack  
**Width:** 14HP | **Depth:** 31mm | **Power:** +45mA / -42mA  
**Manual revision:** 1976/1.5

![Xaoc Devices Belgrad](https://github.com/Shadoe-42/music/raw/main/modular/images/xaoc/belgrad/front_panel.jpg)  
*14HP dual-core state variable filter with two independently tunable resonant peaks, ten routing modes, and the TITO nonlinear cross-modulation switch. One instrument built from two filters.*

---

## Quick Start

**What you need:** An audio source, a CV or LFO source, and a basic patch cable set.

**Minimum viable patch:**
1. Patch your audio source into the IN jack
2. Take the OUT jack to your mixer or next module
3. Set MODE to LL (leftmost position)
4. Set RESO to 4-5
5. Set SPAN to 12 o'clock
6. Turn FREQ slowly left and right; you will hear a dual-resonance lowpass sweep
7. Now turn SPAN and notice how the two peaks separate as a pair

**Key Specifications:**

| Spec | Value |
|------|-------|
| Width | 14HP |
| Depth | 31mm |
| Power | +45mA / -42mA |
| Input level | 0-20Vpp (10Vpp recommended) |
| FREQ V/OCT range | -10V to +10V |
| FM input range | -10V to +10V |
| RESO CV range | 0V to +8V |
| BALANCE CV range | -5V to +5V |
| SPAN CV range | -10V to +10V |
| Tuning range | ~4Hz to ~28kHz |
| V/OCT tracking | ~5 octaves at RESO ≥ 5 |
| Self-oscillation threshold | RESO ~8 |

---

## The Architecture: Two Filters, One Instrument

Most filters in a modular system have a single resonant peak. You control its frequency, you control how sharp it is, and you choose whether signal passes below it (lowpass), above it (highpass), at it (bandpass), or around it (notch). That single-peak model is the foundation of subtractive synthesis and it works extremely well.

Belgrad starts in a different place. It contains two independent state variable filter cores, each capable of its own resonant peak. Those two cores share a single FREQ control: they track the same center frequency. But SPAN sets the distance between them. At SPAN zero, both peaks overlap and Belgrad behaves like a conventional high-quality single-resonance filter. As you increase SPAN, the peaks separate symmetrically above and below the center frequency, and you now have two simultaneous resonant peaks in a single filter.

This is the central concept: **SPAN sets a musical interval between two filter voices.** The two peaks are not an artifact or an artifact to be managed. They are the instrument.

BALANCE then determines which peak is louder. At center, both peaks are equal. Turned left, the lower peak dominates. Turned right, the upper peak dominates. This gives you formant-like control: you are choosing which region of the dual-peak system is emphasized.

The MODE switch selects how the outputs of the two cores are combined. Each filter core can produce lowpass (L), highpass (H), bandpass (B), or notch (N) outputs. The ten positions on the rotary switch route different output combinations, creating ten distinct frequency response shapes, all derived from the same two-core architecture. The label on each mode names the output types of Core 1 and Core 2 respectively: LL is both cores in lowpass, HL is Core 1 highpass and Core 2 lowpass, HB is Core 1 highpass and Core 2 bandpass, and so on.

TITO adds a third dimension. The switch stands for Time Invariant Transfer Oscillator (the module's affectionate internal name for its nonlinear feedback path). In the center position, the cores run independently. In the self-modulation (SM) position, each core feeds back into itself, thickening the resonance with harmonic content. In the cross-modulation (XM) position, the cores modulate each other at audio rate. The result at high RESO in XM mode is not subtle: it produces FM-like timbral chaos that is nearly impossible to replicate any other way. The Belgrad was designed to reward exploration at the edges of its parameter space, and TITO is where most of those edges are.

---

## Essential Parameters

### FREQ

Center frequency for both filter cores simultaneously. This is the anchor point around which SPAN separates the two peaks. The control sweeps from approximately 4Hz to 28kHz. At extreme counterclockwise settings, the filter dips into sub-audio frequency, which has useful CV processing applications even if the audio effect is limited. FREQ accepts V/OCT tracking voltage in the labeled jack; tracking is reliable across approximately five octaves when RESO is at 5 or higher.

### SPAN

The separation between the two resonant peaks. At minimum, both peaks are at FREQ. As SPAN increases, Core 1 shifts downward and Core 2 shifts upward symmetrically, reaching approximately eight octaves of separation at maximum. Think of SPAN as an interval selector. Set SPAN to the position that produces a fifth, an octave, a minor third, and notice that the tonal character changes in musically meaningful ways. This is not a fine-tuning knob; it is a harmonic relationship control. SPAN accepts CV (-10V to +10V) and this is one of the most musically productive CV targets on the module.

### BALANCE

Amplitude weighting between the two peaks. At center, both peaks contribute equally. Turned counterclockwise, the lower peak (Core 1) gains dominance. Turned clockwise, the upper peak (Core 2) gains dominance. The effect is most audible in modes where both peaks are clearly defined, particularly HB (double bandpass) and HL (cascaded bandpass). In these modes, sweeping BALANCE with SPAN set to a wide interval produces formant morphing: the timbral equivalent of an "ah" to "ee" vowel shift. BALANCE accepts CV (-5V to +5V), which opens real-time formant animation.

### RESO

Resonance (Q) for both cores simultaneously. The behavior at different settings:

- **RESO 1-4:** Mild emphasis, both peaks visible but gentle. Good starting point for tonal filtering.
- **RESO 5-6:** Pronounced peaks. V/OCT tracking becomes reliable here. Good for percussion and tonal processing.
- **RESO 7:** Strong resonance. Self-oscillation begins approaching.
- **RESO ~8:** Self-oscillation threshold. Both cores begin producing audio even without an input signal. This is the entry point to using Belgrad as a dual-VCO sound source.
- **RESO above 8:** Full self-oscillation. Both oscillators are now active and tracking V/OCT. SPAN sets their interval.

Note: Notch modes (NN, NL, HN) behave counterintuitively with RESO. The notches become narrower and less audible as resonance increases. The manual specifically addresses this: notch effects are most prominent at low-to-moderate RESO settings.

### TITO (Switch)

Three-position switch: center = neutral, left = SM (self-modulation), right = XM (cross-modulation).

**Neutral:** Both cores run independently. Clean dual-resonance behavior.

**SM (self-modulation):** Each core feeds back into itself via a nonlinear path. The effect at moderate RESO is a slight harmonic thickening. At high RESO it produces significantly more complex resonant overtones than standard feedback would. The peaks become richer and slightly less predictable.

**XM (cross-modulation):** Core 1 modulates Core 2 and vice versa at audio rate. This is FM synthesis between two filter cores. At moderate RESO the effect is audible but controllable. At high RESO in modes like BH and HH, XM produces FM ratios that depend on the SPAN setting, creating inharmonic sidebands or musical FM relationships depending on how SPAN is tuned. The most radical sounds Belgrad is capable of come from XM at maximum RESO with SPAN carefully tuned to a musical interval.

TITO is intentionally not a CV-controllable parameter. Switching it mid-patch by hand while patched is a performance gesture; the abrupt timbral shift is part of its character.

### LEVEL

Input amplitude control. This is not a simple volume knob. At lower settings it attenuates the incoming signal, which is useful when your source is hot and you want to avoid overdriving the filter. At higher settings it amplifies the input, driving the filter cores harder. Filter saturation at high LEVEL settings produces harmonic distortion that interacts with RESO in complex ways, particularly at high resonance settings where the cores are already near self-oscillation. Moderate input drive (LEVEL at 12 o'clock with a standard modular level source) is a good starting point; intentional overdrive is a sound design tool.

### FM and FM Attenuator

The FM jack accepts bipolar modulation voltage (-10V to +10V) for frequency modulation of the center frequency. The illuminated slider above the jack is an attenuator with a visual indicator: it glows brighter as FM modulation depth increases. The slider goes from zero (fully left) to full FM depth (fully right). Negative FM requires inverting the source before it reaches the jack, as the slider is unipolar. FM into FREQ produces frequency modulation of the entire dual-peak system simultaneously: both peaks shift with the FM input.

### V/OCT

Dedicated one-volt-per-octave tracking input. Reliable across approximately five octaves at RESO 5 and above. At lower RESO the filter tracking is audible but imprecise; the V/OCT input becomes musically accurate as resonance approaches and enters self-oscillation territory. When Belgrad self-oscillates, patching your pitch CV into V/OCT turns it into a dual-sine oscillator with SPAN setting the interval.

---

## The 10 Modes

The MODE rotary switch selects from ten frequency response configurations. Each label names the output type of Core 1 followed by Core 2 (L = lowpass, H = highpass, B = bandpass, N = notch).

**LL: Double Slope Lowpass**  
Both cores in lowpass. At SPAN zero, this is effectively a 4-pole lowpass with -24dB/octave above the cutoff. As SPAN increases, a -12dB shelf appears between the two peaks, with -24dB above the upper peak. The classic Belgrad starting point for rich lowpass filtering.

**LB: Lowpass + Bandpass**  
Core 1 lowpass, Core 2 bandpass. A 2-pole lowpass slope with a formant bump in the upper midrange from the bandpass component. The -6dB/octave slope above the higher peak gives this mode an open, present character compared to the steeper LL. Good for instrument-like timbres where you want the filter to enhance rather than heavily cut.

**NL: Lowpass with Notch in Passband**  
Core 1 notch, Core 2 lowpass. A -12dB lowpass with a notch placed below the corner frequency. The notch position is set by SPAN. Keep RESO low to hear the notch clearly; high RESO narrows it out of audibility.

**NN: Double Notch**  
Both cores in notch. Two cascaded notches separated by SPAN. This produces a comb-like response when SPAN is set wide. Most useful as a static tone-shaping tool or as a filter for signals where you want to remove two specific frequency regions simultaneously.

**LH: Lowpass + Highpass (Band Rejection)**  
Core 1 lowpass, Core 2 highpass. This is a band-rejection filter: the region between the two cutoffs (set by SPAN) is attenuated, while content below Core 1 and above Core 2 passes. Both cores have resonant peaks at their respective cutoff edges, so you get two resonant crests flanking a notch band. The width of the rejected band is directly controlled by SPAN.

**HB: Double Bandpass**  
Core 1 highpass, Core 2 bandpass. Two bandpass-like peaks with a combined two-formant response. This mode produces vocal and bowed-string character most readily. SPAN sets the formant interval, BALANCE sets which formant is emphasized, and RESO sharpens both. The manual specifically recommends this mode alongside LL and LB for vocal timbres, with RESO at 6-7 and SPAN set to 2-4 intervals.

**HL: Bandpass (Cascaded HP + LP)**  
Core 1 highpass into Core 2 lowpass in series: a bandpass filter with two distinct resonant peaks at the band edges. At wide SPAN the passband between the peaks becomes flat, producing an unusually wide bandpass with sharp resonant walls. This mode is particularly good for percussion processing: it preserves midrange transient content while emphasizing the resonant edges of the band.

**HN: Highpass with Notch in Passband**  
Core 1 highpass, Core 2 notch. A 12dB highpass with a notch placed above the cutoff frequency. Counterpart to NL: use it for situations where you want to cut a specific region within an already-highpassed signal. Same RESO behavior applies: notch is most audible at low-to-moderate resonance.

**BH: Bandpass + Highpass**  
Core 1 bandpass, Core 2 highpass. A 2-pole highpass with a bandpass formant below. The slope below the lower peak is +6dB/octave. TITO cross-modulation with high RESO in this mode is specifically mentioned in the manual as one of the most radical TITO combinations available.

**HH: Double Slope Highpass**  
Both cores in highpass. The mirror image of LL: +12dB between the two peaks, +24dB below. At SPAN zero, a conventional 4-pole highpass. As SPAN increases, the double-slope character emerges. TITO cross-modulation at high RESO in HH mode is the other mode specifically recommended for extreme TITO effects.

---

## Historical Context

Xaoc Devices operates from Warsaw, Poland, with the stated identity "Working Class Electronics, Made in the EU." The phrase communicates something deliberate: the aesthetic position of Eastern European industrial production applied to boutique synthesis hardware. This is not a neutral branding choice.

Belgrad is named for Belgrade, the capital of what was Yugoslavia. The module's panel carries the notation "Model of 1976," a reference to the era of Yugoslav electronics development under communist-era industrial production. The TITO switch is almost certainly a reference to Josip Broz Tito, the Yugoslav leader from 1944 until his death in 1980. The manual's cover photograph depicts what appears to be a Soviet-era computer demonstration, in period-accurate monochrome. These choices are consistent across the module: the naming, the aesthetic, and the cultural references all locate the Belgrad within a specific historical moment in Eastern European technological history.

The technical lineage is state variable filter design, which has roots in analog computing and active filter theory from the 1960s and 1970s. The state variable topology allows simultaneous lowpass, highpass, and bandpass outputs from a single filter structure because it computes filter state variables (hence the name) using integration rather than passive RC networks. Xaoc takes the standard state variable approach and doubles it, then adds the TITO cross-modulation path as a distinctly nonlinear extension of that architecture.

The result sits in a specific filter lineage among the project's guides. The Wasp SE uses CMOS digital-logic gates as filter stages, producing its distinctive gritty and broken character from the nonlinearity of those components. The Forbidden Planet uses the Steiner-Parker topology with its three-input architecture for direct timbre blending. The Black Polyvoks derives its character from the Soviet Polyvoks synthesizer's original filter chip. Belgrad stands apart from all three: it is not a single-peak topology with character derived from unusual component choices, but an architecture designed from the ground up to produce and manipulate two simultaneous resonant peaks. The musical consequence is that it addresses formant synthesis and dual-oscillator applications that the other filters in the system cannot.

---

## Why This Excels

Belgrad's primary advantage over single-resonance filters is its ability to produce multi-peak frequency responses without stacking multiple filter modules. Formant synthesis (producing vowel-like and instrument-body-like resonances) requires at least two resonant peaks at defined intervals. Belgrad does this natively in a single 14HP module. For electronic producers working with bowed strings, vocals, or any timbre where body resonance matters, Belgrad is the correct tool where other filters in the system would fall short.

The MODE switch's ten positions give genuinely different filter topologies without requiring additional modules or complex routing. Moving from LL to HB to HL is not the same as switching a single filter type: each mode is a different combination of the two cores' output paths, producing frequency responses that have distinct musical applications and distinct character. Most filters offer one or two modes (often LP/BP/HP/notch on a single selector). Belgrad offers ten configurations of a dual-core system.

SPAN as a modulation target is underused by first-time owners and highly productive once engaged. A slow LFO on SPAN animates the interval between the two peaks continuously. Because the peaks maintain their harmonic relationship to each other while both tracking FREQ, the modulation sounds more like a formant animation than a standard filter sweep. The result is movement that resembles vocal or orchestral instrument character in a way that a single-peak filter sweep cannot produce.

Self-oscillation at SPAN tuned to a musical interval turns Belgrad into a dual-sine-wave source with defined pitch relationships. This is the SOURCE secondary role in the taxonomy: at sufficient RESO, Belgrad generates audio without an input signal, and V/OCT turns it into a playable dual-oscillator. TITO in XM mode at self-oscillation produces FM synthesis between the two cores at a ratio set by SPAN. This application is entirely different from filtering and represents a genuine second instrument mode built into the same architecture.

The TITO switch is not a novelty. It is a discrete three-position gesture that changes the fundamental behavior of the filter at a level that cannot be smoothly CV'd. This makes it a performance control: switching TITO mid-patch with your hand while controlling RESO with the other is the kind of live gesture the module was designed for.

---

## Patch Examples

### Patch 1: Dual-Peak Lowpass Sweep (Foundational)

**Goal:** Hear the difference between single-peak and dual-peak filtering in a direct comparison.

**Setup:**
```
Oscillator OUT        ---[A]---> Belgrad IN
LFO OUT (slow, tri)   ---[C]---> FREQ CV
Belgrad OUT           ---[A]---> VCA IN
ENV OUT               ---[C]---> VCA CV
```

**Procedure:**
1. Set MODE to LL
2. Set RESO to 5
3. Set SPAN to minimum (fully counterclockwise)
4. LFO sweeps the FREQ; notice the single resonant peak characteristic of a standard lowpass sweep
5. Now slowly increase SPAN to 12 o'clock
6. The same sweep now moves two peaks simultaneously, and the resonant character doubles
7. Continue to maximum SPAN and notice the peaks separate wide enough to produce a distinct double-crest in the midrange

**What to listen for:** At SPAN zero, Belgrad sounds like any quality 4-pole lowpass. As SPAN increases, the resonant peak splits and thickens. The same sweep sounds fatter, less like a single tonal emphasis and more like two instruments being swept together. This is the architectural difference in its most audible form.

**Extend it:** Once you can hear the dual-peak character clearly, try different MODE positions while keeping RESO, SPAN, and the LFO sweep constant. LL, HB, and HL will give you the most distinct differences with this simple setup.

---

### Patch 2: Formant Synthesis (Vocal/Bowed)

**Goal:** Produce a vowel-like formant response using SPAN as interval control and BALANCE as morphing.

**Setup:**
```
Oscillator (saw/sq) OUT   ---[A]---> Belgrad IN
Slow random CV or S&H     ---[C]---> SPAN CV
LFO (slow, triangle)      ---[C]---> BALANCE CV
Belgrad OUT               ---[A]---> Mixer
```

**Procedure:**
1. Set MODE to HB (double bandpass)
2. Set RESO to 6-7 (just below self-oscillation)
3. Set SPAN manually to approximately 10 o'clock (moderate separation)
4. Patch the oscillator and listen without modulation; notice the two bandpass peaks giving the signal a resonant, vocal-like body
5. Now engage the LFO on BALANCE: the emphasis shifts between the lower and upper formant regions, producing a slow vowel-morph
6. Add the random CV to SPAN: as the formant interval changes, the vowel character shifts more dramatically

**What to listen for:** The combination of RESO at 6-7, HB mode, and SPAN in the 2-4 interval range is the sweet spot the manual identifies for vocal character. BALANCE modulation produces movement that resembles "ah" shifting toward "ee" shifting toward "oh." This is not an approximation of formant synthesis; it is a basic implementation of it, using Belgrad's architecture directly.

**Extend it:** Replace the oscillator with a bowed-string sample or a drone from another module. The formant emphasis from Belgrad will add body resonance that transforms a flat sustained tone into something that breathes. Try LB mode as a more open-sounding alternative to HB in this patch.

---

### Patch 3: Resonant Bandpass Percussion (Advanced)

**Goal:** Use Belgrad in HL mode to add resonant body to percussive transients, producing tuned metallic percussion.

**Setup:**
```
Drum or noise source OUT      ---[A]---> Belgrad IN
Percussive envelope OUT       ---[C]---> FREQ CV
Gate or trigger               ---[G]---> Envelope GATE
Belgrad OUT                   ---[A]---> Mixer
```

**Procedure:**
1. Set MODE to HL (cascaded highpass + lowpass = bandpass with dual resonant edges)
2. Set RESO to 7 (high, close to self-oscillation)
3. Set SPAN to 12 o'clock
4. Set FREQ to a midrange position
5. Patch the envelope into FREQ CV; the envelope pitch-shifts the filter center on each hit
6. Trigger the envelope and hear the filter peak as a resonant snap on the transient

**What to listen for:** HL mode produces a bandpass with distinct resonant walls at the edges of the passband. At RESO 7 with a fast envelope, each trigger produces a pitched resonant body sound. SPAN controls whether the resonant response sounds like a single tuned peak or two separate frequency components being energized simultaneously. Higher SPAN produces a more metallic, inharmonic body character; lower SPAN tightens toward a single resonant pitch.

**Extend it:** Set RESO above 8 so that the filter self-oscillates. The envelope on FREQ CV now pitches the self-oscillating dual-core: each trigger produces a pitched sine-wave ping. Tune FREQ and SPAN so that the self-oscillating interval matches a harmonic of your kick or bass. This is tuned physical modeling behavior from a filter.

---

### Patch 4: Dual Oscillator FM via TITO Cross-Modulation (Expert)

**Goal:** Use Belgrad as a dual-sine oscillator with FM synthesis between the two cores via TITO XM.

**Setup:**
```
Pitch CV (seq/kbd)            ---[C]---> V/OCT
Envelope or gate              ---[C]---> RESO CV  (optional)
Belgrad OUT                   ---[A]---> VCA IN
ENV OUT                       ---[C]---> VCA CV
(no audio input required)
```

**Procedure:**
1. Set MODE to HH or BH (both recommended for TITO XM in the manual)
2. Set RESO above 8; Belgrad self-oscillates
3. Set TITO to XM
4. Set SPAN to 0 (both cores at the same pitch)
5. Play pitch CV and confirm Belgrad tracks the note
6. Begin increasing SPAN slowly
7. At low SPAN, the two cores produce a chorus-like beating effect
8. At wider SPAN (set to a fifth or octave), the cross-modulation between two harmonically related oscillators produces FM sidebands
9. Continue to wider intervals: the FM behavior becomes increasingly inharmonic

**What to listen for:** This is FM synthesis generated entirely within the Belgrad's own cross-modulation path. The carrier-to-modulator ratio is set by SPAN. Musical intervals in SPAN (fifth, octave, minor third) produce FM spectra with harmonic sidebands. Non-musical intervals produce inharmonic FM spectra. TITO XM at high RESO is deliberately designed to be chaotic, but SPAN gives you a way to approach that chaos from a tuned starting point. Try adjusting LEVEL to overdrive the self-oscillating cores: the saturation changes the FM character significantly.

**Note on V/OCT tracking:** In self-oscillation, both cores track V/OCT. SPAN sets their interval relative to each other, not relative to absolute pitch. As you play a sequence, both oscillators move together while maintaining the SPAN interval. This is musically coherent in a way that two independent oscillators detuned by semitones would not be.

---

## Common Mistakes

**Treating SPAN as a fine-tune control**  
SPAN is a musical interval selector, not a detune knob. At low values it produces beating and chorus character, which is useful, but that application represents a small fraction of what SPAN does. The productive territory is setting SPAN to specific intervals (a fifth, an octave, a minor third) and listening to how that harmonic relationship shapes the filter character. Players who only use SPAN in the 7-10 o'clock range are leaving most of its musical value untouched. Set it wide. Tune the interval deliberately.

**Engaging TITO at low RESO and hearing nothing interesting**  
TITO's effects are highly RESO-dependent. At RESO 3-4, even XM mode produces subtle results: slight harmonic thickening that is difficult to distinguish from bypass. The transformative TITO behavior happens above RESO 6 in SM mode and above RESO 7-8 in XM mode. If TITO is not doing what you expect, raise RESO first, then evaluate. The manual specifically identifies BH and HH modes at high RESO as the most extreme TITO combinations.

**Raising RESO to hear the notch better**  
Notch modes (NN, NL, HN) behave opposite to intuition: the notches become narrower and less audible as resonance increases. At high RESO, the resonant peaks dominate and the notches become nearly inaudible frequency cuts. To hear notch modes clearly, keep RESO at 2-4. The notch width and audibility are inversely related to resonance. This is acoustically correct behavior for a high-Q filter, but it surprises most users who expect more RESO to mean more of everything.

**Using LEVEL as a post-filter volume control**  
LEVEL is an input attenuator/amplifier that affects the signal going into the filter cores, not the output level. Raising LEVEL drives the filter input harder, which at high RESO settings creates input saturation that interacts with the resonance in complex ways. If you want to control output level, use your VCA or mixer after Belgrad. Adjusting LEVEL changes the drive and saturation character of the filtering; it is a timbre control with level implications, not a simple level control with no other effect.

**Ignoring V/OCT in non-self-oscillating applications**  
V/OCT is most obviously useful when Belgrad self-oscillates as a dual oscillator. But V/OCT tracking is also valuable for filter-as-instrument applications at RESO 5-6, where the filter resonance follows pitch sequences without self-oscillating. This produces a filter that seems to resonate "with" the note being played: the peak emphasis tracks the melody, giving filtered melodic content a more coherent relationship to the source pitch. Patching pitch CV to both your oscillator and Belgrad's V/OCT simultaneously is a foundational technique for melodic patch work.

---

## Pairs Well With

**Zadar (Xaoc Devices):** Zadar's 270 envelope shapes, particularly the multi-stage and organic forms from the later banks, are unusually good CV sources for Belgrad's SPAN and BALANCE inputs. Standard ADSR envelopes produce linear formant movement; Zadar's vector shapes produce organic, instrument-body-like formant contours. The pairing reflects both being Xaoc products in the same system.

**Batumi or any quad LFO:** Belgrad has multiple CV inputs (FREQ, SPAN, BALANCE, RESO, FM) that benefit from simultaneous, phase-offset modulation. A quad LFO sending different phases to FREQ and SPAN simultaneously produces animated dual-peak movement that is difficult to achieve with a single LFO source. The more modulation sources available to Belgrad, the more the dual-core architecture reveals its range.

**Rings (Mutable Instruments) or resonator modules:** Belgrad in HL mode processing the output of a physical model or resonator creates a two-stage resonant processing chain. The resonator defines the body; Belgrad adds a second spectral layer. The combination can produce orchestral instrument character from relatively simple input material.

**Ground Control (Endorphin.es):** A pattern generator sending stepped CV to Belgrad's SPAN input produces rhythmically timed formant changes synchronized to the pattern. Because SPAN changes alter the harmonic character of the filter response rather than simply the cutoff frequency, the rhythmic modulation produces timbral variation that reads as phrasing rather than just filter movement.

**Noise source into NN or HL mode:** White or colored noise processed through double-notch (NN) or bandpass (HL) mode at high RESO with SPAN-defined intervals produces resonant comb-filtered noise: windchime, metallic breath, or cave-resonance textures depending on SPAN and RESO settings. Any noise-capable module (VCO with noise output, dedicated noise source, even a sample player in loop) works.

---

## Advanced Learning Path

**Step 1: Master the mode matrix**  
Spend a session working through all ten modes with a simple oscillator source, fixed RESO at 5, and SPAN at 12 o'clock. Take notes on which modes produce the most distinct tonal differences. The goal is building a mental map of the mode grid before adding modulation complexity.

**Step 2: Modulate SPAN deliberately**  
Replace manual SPAN adjustment with a slow LFO or sequenced CV. Set a specific musical interval as the LFO center (tune SPAN so the static sound is a fifth, then let the LFO move above and below that point). This reveals SPAN as an animated harmonic interval rather than a static setting.

**Step 3: Explore BALANCE in formant modes**  
In HB and LB modes at RESO 6-7, use an LFO or envelope to animate BALANCE continuously. Listen for the vowel-like formant shift as BALANCE moves. This builds the muscle memory for when to reach for BALANCE CV in practical patches.

**Step 4: Approach TITO systematically**  
Start with SM at RESO 6. Note the harmonic thickening. Increase RESO to 7-8 and note the increase in SM character. Switch to XM. Then increase RESO above 8 into self-oscillation with XM engaged. Work through BH and HH modes specifically at maximum RESO and XM. This is the designed parameter space for TITO's most extreme behavior; going there methodically rather than randomly produces more usable sounds.

**Step 5: Self-oscillation as instrument**  
Remove your audio input. Turn RESO above 8. Patch V/OCT from a sequencer or keyboard. Play notes. Then increase SPAN to a fifth and play the same notes. Then to an octave. Then to a tritone. Listen to how the FM character changes as the interval changes. Then engage TITO XM. This entire exercise requires no external audio source and treats Belgrad as a primary synthesizer voice rather than a filter.

**Step 6: Study the other filters in the system**  
After working Belgrad in depth, return to the Wasp SE, Forbidden Planet, and Black Polyvoks with specific attention to where each one produces resonance and how the character differs. Belgrad is most informative in contrast: its dual-core formant capability is clearest when compared directly against single-peak alternatives on the same source material. This comparative listening is the foundational technique for filter literacy in the system.

**Filter design reading:** State variable filter theory is covered in Will Pirkle's *Designing Audio Effect Plugins in C++* (Chapter 12) and in Bob Moog's and Don Buchla's published circuit notes from the late 1960s. The academic context is not required to play Belgrad, but understanding why the state variable topology produces simultaneous LP/HP/BP/N outputs deepens appreciation for what Xaoc did by doubling the architecture.
