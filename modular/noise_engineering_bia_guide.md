---
title: Basimilus Iteritas Alter
manufacturer: Noise Engineering
primary_role: EVENT_VOICE
secondary_roles: []
historical_context: true
form_factor: eurorack
functions: [drum-voice, fm-oscillator, wavefolder]
behavior_tags: [percussive, harmonic, inharmonic, gated, nonlinear, dirty, noisy]
use_cases: [percussive voice, lead voice, noise layer, timbral movement and shaping]
hp: 10
memory: none
transport: none
screen: false
hybrid: false
cv: full
---

# Basimilus Iteritas Alter

**Six-oscillator parameterized drum synthesizer with additive, pitch-envelope, and FM modes**

![Noise Engineering Basimilus Iteritas Alter](https://github.com/Shadoe-42/music/raw/main/modular/images/noise_engineering/basimilus_iteritas_alter/front_panel.jpg)

## Historical Context

The acoustic percussion family generates sound through the physical vibration of membranes, plates, and shells: each physical structure has characteristic resonant modes, each mode has its own frequency, decay time, and amplitude, and the sum of all active modes at a given moment is what the ear hears as the instrument's voice. Electronic percussion synthesis has always been an attempt to approximate this modal structure with available circuits. The Roland TR-808, released in 1980, used a bridge-T resonator circuit for its kick drum: a tuned filter and an exponentially decaying pitch envelope that swept the fundamental frequency downward over a short window, producing the characteristic descending thud that has defined electronic kick bass for over four decades. The 808's architecture modeled one mode. The percussion instruments it approximated had dozens of interacting modes. The gap between the two was always audible, and for most producers it was the gap that made the 808 sound better than the real thing for its intended context rather than a limitation to be apologized for. The Roland TR-909 followed in 1981 with analog synthesis for some elements and PCM samples for others; the resulting hybrid palette set the dominant template for what synthesized percussion sounded like until digital polyphonic synthesis gave designers the oscillator count to attempt something more thorough.

The academic framework for simulation-based percussion synthesis arrived in Stefan Bilbao's *Numerical Sound Synthesis*, published in 2009. Bilbao, working at the University of Edinburgh, documented methods for simulating physical acoustic systems as numerical differential equations, which in principle allowed a computer to simulate the exact behavior of a membrane or plate from first principles. The appeal for percussion synthesis is obvious: a numerical model of a drum head with adjustable tension, radius, and striking position would produce every possible drum sound from a single parametric space. The difficulty is equally obvious from the engineer's perspective: the numerical methods that produce physically accurate results at low frequencies become computationally expensive, poorly behaved, or both at audio rates, and the parameter space that a physically accurate model demands bears little resemblance to the musical terms a performer wants to adjust. Kris Kaiser read Bilbao's book and spent a few hours prototyping a numerical oscillator based drum synthesizer before deciding that the approach was impractical for a real-time hardware instrument. The question that ended that prototype: what would analog do?: became the design question that produced the Basimilus Iteritas.

The alternative Kaiser settled on was additive wavetable synthesis: six oscillators, each representing one resonant mode of a virtual drum, each with its own pitch, decay, and amplitude, summed to produce the full instrument voice. This is structurally similar to what the numerical approach would have produced, but evaluated analytically rather than numerically, which is computationally tractable at audio rates and parameterizable in musical terms. The SPREAD control adjusts the frequency intervals between the six oscillators from the harmonic series (integer multiples of the fundamental, producing the tonal character of skin-headed drums) to the prime series (2, 3, 5, 7, 11 times the fundamental, producing the inharmonic character of metal), which maps directly to the physical distinction between instruments whose modes are mathematically related and those whose modes are not. John Chowning's FM synthesis, developed at Stanford in 1967 and published in the Journal of the Acoustical Society of America in 1973, provides the third mode: Metal reconfigures the six oscillators so that each modulates the next, producing the dense inharmonic spectra characteristic of metallic percussion and bell-like sounds. The 1983 Yamaha DX7, which brought Chowning's work to mass commercial production, had already demonstrated that FM synthesis was the most efficient known method for generating metallic and bell timbres with digital technology. The BIA's Metal mode is a deliberate echo of that lineage.

The Alter revision emerged two years after the original Basimilus Iteritas shipped, driven by a combination of hardware necessity and a single outside influence. The CPU board used in the original required replacement for engineering reasons, and Kaiser used the opportunity for a more thorough redesign: 2HP narrower, CV over the mode and range switches, and the change from attenuating to offsetting behavior for the knob and CV relationship. The most significant addition was Liquid mode, which the manual credits directly to Chris Randall of Audio Damage, who sent Kaiser an Audio Damage Neuron to play with. The Neuron's pitch envelope behavior demonstrated how much expressive range an internal pitch sweep added to a percussion synthesizer without requiring external patching, and Liquid mode was prototyped within a few hours of Kaiser's first session with it. The infinifold wavefolder, a digital implementation that dynamically adds fold stages to maximize harmonic output at any given threshold, completes the signal chain after the summed oscillators and restores the dynamics lost during folding through a final amplitude envelope derived from the six individual oscillator envelopes.

---

## Quick Start

The Noise Engineering Basimilus Iteritas Alter is a six-oscillator digital drum synthesizer with three synthesis modes and full CV over every parameter. At its core it is an additive synthesizer with adjustable waveform, harmonic spread, and independently decaying modes, summed and run through an infinifold wavefolder. It always requires a trigger to produce sound; there is no free-running mode.

1. Patch a trigger from Hermod+ or a clock into the Trig input.
2. Patch the Out jack into a mixer channel.
3. Set the Skin/Liquid/Metal switch to Skin.
4. Set the Bass/Alto/Treble switch to Bass.
5. Set Pitch to center, Spread fully counterclockwise, Morph to the left quarter, Attack to center, Decay to center, Harmonic fully left, Fold to center.
6. Send a trigger. You should hear a short tonal kick-like sound.
7. Press the Hit button to trigger manually at any time.
8. Slowly increase Harmonic clockwise and listen to additional modes blend in and sustain longer.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 10 HP |
| Depth | 38 mm ⚠️ |
| Power | 80 mA +12V / 5 mA -12V / 90 mA +5V |

The manual states a depth of 1.5 inches (~38 mm). The flag remains pending physical hardware verification.

Power draw depends on voltage supply configuration. The values above reflect the +5V rail configuration (processor running on the 5V bus). Without the +5V rail, power draw is 150 mA +12V / 5 mA -12V / 0 mA +5V. The voltage supply switch on the rear PCB selects between configurations; using the 5V rail reduces load on the 12V bus and lowers noise.

---

## Essential Parameters

**Pitch.** Adjusts the fundamental oscillator frequency. This is a 1V/octave standard input; the pitch knob sums with the CV input, offsetting rather than attenuating it. A knob at center position with no CV produces the default pitch; turning it clockwise raises the fundamental and counterclockwise lowers it. In Bass mode, the fundamental sits in the kick drum register. Pitch CV from a sequencer tracks 1V/oct across the knob's range in Skin and Liquid modes; in Metal mode, pitch sets the frequency of the carrier oscillators in the FM network, with audible pitch tracking available but less precise due to the FM cross-modulation.

**Spread.** Controls the frequency spacing between the six oscillators. Fully counterclockwise sets the oscillators to harmonic integer intervals relative to the fundamental, modeling instruments whose modes align with the overtone series (drums, tonal percussion). Turning Spread clockwise shifts the intervals progressively toward the prime series, making the overtone structure inharmonic and more metallic or alien in character. In Metal mode, Spread also affects the FM operator frequency ratios. The knob offsets the CV input; the full Spread range is accessible from CV alone with the knob at center.

**Morph.** Controls the waveform of all six oscillators simultaneously, blending continuously through sine, triangle, saw, and square. At the leftmost position all oscillators run as sine waves, producing the cleanest and most fundamental-heavy tone. Moving clockwise adds harmonic content progressively through triangle, then saw, then square. The knob offsets the CV input, making real-time waveform sweep available from any CV source; a slow LFO into Morph CV produces timbral movement that all six oscillators track together.

**Attack.** Controls the attack stage for all oscillators and the noise component behavior. Left of center adds noise to the attack transient; the further left the knob goes, the more prominent the noise component becomes. At dead center, Attack produces a classic analog-style pop: a sharp transient derived from the oscillators' initial phase relationships without added noise. Right of center, Attack slows the onset, producing a softer swell into the main body of the sound. The noise oscillator's envelope is also controlled by the Attack knob. The knob offsets the CV input; positive CV with the knob left of center increases noise content, negative CV with the knob right of center shortens the attack.

**Decay.** Controls the decay time for all six oscillators simultaneously. Shorter settings produce tight, punchy sounds that release quickly; longer settings produce sustained tones with a long ringing decay. Decay interacts with Harmonic: at low Harmonic settings only one oscillator is active and Decay controls its single decay time; at high Harmonic settings multiple oscillators are active with their own individual decay times, but the Decay knob still globally offsets all of them. The knob offsets the CV input.

**Harmonic.** Controls the harmonic complexity of the sound by adjusting which oscillators are active and how long they sustain. Fully left, only one oscillator is audible: a single tonal mode, which simulates the simple character of single-oscillator analog bass drums. Through the first quarter of travel, a second tone fades in. Beyond the first quarter, the remaining turning extends first the decay times and then the amplitudes of the other four harmonics. The result at maximum Harmonic is a dense multi-oscillator sound with all six modes contributing at full amplitude for their full decay duration. The knob offsets the CV input; Harmonic CV produces one of the most musically useful real-time timbral variations the module offers, sweeping from a pure fundamental tone to a complex modal structure.

**Fold.** Controls the infinifold wavefolder section. For the first three quarters of travel, Fold sets the threshold of the folder: a lower threshold means the signal reaches the fold point sooner, producing more folding stages and denser harmonic output. The folder dynamically adds stages to maximize the number of folds based on the threshold and signal amplitude, so the relationship between Fold position and harmonic content is nonlinear and depends on the current output amplitude from the oscillators. In the top quarter of travel, a pulse train derived from the signal is mixed in at the local minima and maxima of the waveform, adding an extreme buzzing harmonic density. The knob offsets the CV input. A final amplitude envelope is applied after the folder to restore dynamics that folding would otherwise compress away, keeping the output punchy even at maximum Fold settings.

**Skin / Liquid / Metal Switch (S/L/M).** Selects the synthesis mode. Skin is a six-operator additive synthesizer modeling instruments whose modes do not interact: each oscillator decays independently without coupling to the others. Liquid is the same architecture as Skin with the addition of a pitch envelope applied to all oscillators: the fundamental descends from a higher starting pitch over the course of the decay, adding the characteristic kick-drum pitch drop without requiring an external pitch envelope or CV source. Metal is a six-operator FM synthesizer where the oscillators modulate each other, modeling instruments with significant modal interaction: the resulting spectra are dense, inharmonic, and often noisy. The switch position can be controlled by CV into the S/L/M jack, enabling real-time mode switching during performance.

**Bass / Alto / Treble Switch (B/A/T).** Sets the pitch range of the module. Bass is the default register for kick and low drum sounds. Alto shifts the pitch two octaves up. Treble shifts four octaves up from Bass. At Treble with a high Pitch setting, the BIA operates in melodic and tonal territory far from its percussion roots. The switch position can be controlled by CV into the B/A/T jack.

**Trigger and Hit.** The Trig input fires the drum voice on a rising edge of approximately 3V. The Hit button fires the voice manually for testing and performance. No CV or gate signal produces output without a trigger.

---

## Why This Instrument Excels

The oscillator-per-mode architecture gives the BIA a physical coherence that single-oscillator drum synthesizers cannot replicate. A real snare drum's character comes from the interaction of the head's modes decaying at different rates: the fundamental decays slowly, the upper partials decay quickly, and the relative energy in each mode changes continuously during the decay. Harmonic and Decay control exactly this relationship in the BIA: Harmonic determines which modes are active and how long each sustains relative to the others, while Decay controls the global offset of all decay times. Moving these two knobs together allows exploration of a large territory of tonal character that no fixed analog circuit provides: from a tightly focused single-mode click at low Harmonic to a long-decaying multi-modal resonance at maximum Harmonic, with every point between being a musically valid drum sound.

Liquid mode's internal pitch envelope resolves a patching problem that every modular kick drum patch faces eventually. To get a pitch sweep on a kick voice built from a VCO, a separate envelope generator, an attenuator, and specific patching are required; the sweep shape depends on the envelope's curve and timing in ways that require tuning to the specific VCO response. Liquid mode builds this pitch sweep into the synthesis engine, where it is calibrated to the oscillator frequency and decay time already set on the module. The sweep is inherent to the sound rather than bolted on, which means it tracks correctly regardless of the Pitch and Decay settings without additional calibration. For a kick drum voice that simply needs to sound like a kick drum without additional patching overhead, Liquid mode is the fastest path to a convincing result. For a more electronic bass-pitched percussion sound, Liquid's parameter space is equally useful: the pitch drop can be made subtle (short, narrow) or extreme (long, wide) by adjusting the interaction of Pitch, Decay, and Harmonic in ways that suggest a much more complex patch than the single module represents.

Metal mode is the most distinctly non-analog sound the BIA produces, and the manual is candid about its character: the FM implementation is described as "classic 80s 'who cares about aliasing?' frequency modulation in all of its noisy glory." This framing is accurate. Metal mode does not attempt to produce clean FM bell tones or precisely tuned metallic spectra; it produces dense, noisy, harmonically unpredictable tones that exist in the territory between recognizable percussion and pure noise. With Spread and Fold both pushed high, Metal mode generates sounds that are more texture than percussion, which makes the module dual-purpose in a patch: a trigger sequence that produces clearly shaped kick and snare sounds at one Spread and Fold setting produces ambient noise texture when those parameters shift, without changing any patching. This transition from percussion to texture is available as a single parameter sweep, making the BIA a practical noise source in addition to a drum voice.

The variable sample rate is a design decision with audible consequences that distinguish the BIA from conventional digital drum synthesizers. Most digital synthesis uses a fixed sample rate; the relationship between the sample rate and the oscillator frequency determines the aliasing content, which sits at frequencies unrelated to the fundamental and adds a characteristic digital grit. The BIA's sample rate is a multiple of the fundamental oscillator frequency, which maps alias content to harmonic multiples of the fundamental: the aliasing still exists but it now aligns with the overtone series of the sound, blending into the harmonic structure rather than competing with it. At Spread settings that produce strong harmonic structure, this produces a particularly clean result where the digital nature of the synthesis is audibly suppressed. At inharmonic Spread settings, the aliasing alignment breaks down and introduces unique textural character. This variability is part of the instrument's sonic range rather than a defect to be corrected.

---

## Patches

### Patch 1: Analog-Style Kick Drum

Noise Engineering Basimilus Iteritas Alter in Skin mode, Bass range, configured to produce a tonal bass drum with adjustable pitch, decay, and single-mode harmonic character.

```
[Hermod+ Gate Out] ──────────[G]──────▶ [BIA Trig In]

[BIA Out] ───────────────────[A]──────▶ [MixUp CH1]

                                         Mode: Skin
                                         Range: Bass
                                         Pitch: 9 o'clock (low)
                                         Spread: fully CCW
                                         Morph: 8 o'clock (sine-adjacent)
                                         Attack: center
                                         Decay: 2 o'clock
                                         Harmonic: 7 o'clock (nearly fully left)
                                         Fold: 10 o'clock
```

**Setup:** Patch Hermod+'s gate into Trig and BIA Out into a mixer. Set Skin mode and Bass range. Spread fully counterclockwise places all oscillators at harmonic intervals relative to the fundamental. Harmonic nearly fully left means only one oscillator is active, which simulates the single-mode character of simple analog bass drums. Morph in the sine-adjacent position keeps the wave clean and round.

**Controls:** Adjust Pitch to set the fundamental. Each octave of the Pitch knob spans a significant tonal range in Bass mode; small knob movements at low settings produce large perceived pitch changes. Move Decay clockwise to extend the sound's sustain. Increase Harmonic slowly and listen: at the first quarter of travel a second mode fades in and the sound gains body; beyond that, additional modes extend the decay and increase complexity. Increase Fold gradually and hear harmonic content multiply; the infinifold adds richness without sacrificing the percussive punch because the output envelope compensates for amplitude loss. Switch from Skin to Liquid and hear the pitch envelope drop in immediately, adding the characteristic kick sweep without any additional patching.

**Result:** A tunable single-voice bass drum covering the range from minimal one-mode click to multi-modal resonant thud, with tonal character controlled entirely by Harmonic and Decay. Liquid mode is accessible by a switch flip at any point.

---

### Patch 2: Pitched Kick Sequence in Liquid Mode

BIA in Liquid mode, Bass range, receiving V/oct pitch CV from Hermod+ for a melodically sequenced kick bass line where each trigger produces a different pitched drop.

```
[Hermod+ Gate Out] ──────────[G]──────▶ [BIA Trig In]
[Hermod+ Pitch CV Out] ──────[C]──────▶ [BIA Pitch CV In]
[Zadar CH1 Env Out] ─────────[C]──────▶ [BIA Decay CV In]
[Hermod+ Gate Out] ──────────[G]──────▶ [Zadar Trigger CH1]

[BIA Out] ───────────────────[A]──────▶ [SSF SSG Stereo Field IN-L]
[SSG Stereo Field OUT-L] ────[A]──────▶ [MixUp CH1]

                                         Mode: Liquid
                                         Range: Bass
                                         Pitch knob: center (sequence determines pitch)
                                         Spread: fully CCW
                                         Morph: 8 o'clock
                                         Attack: slightly right of center
                                         Decay: center
                                         Harmonic: first quarter
                                         Fold: 9 o'clock
```

**Setup:** Patch Hermod+'s pitch CV and gate into BIA Pitch CV and Trig respectively. Set a bassline sequence on Hermod+ spanning four to six semitones in the low register. Patch Zadar's first channel envelope into Decay CV, with Zadar triggered by the same Hermod+ gate. Route BIA Out through the SSF SSG Stereo Field in Skin mode as a light low-pass gate for tonal shaping before the mixer.

**Controls:** Each step of the Hermod+ sequence sets a different pitch for the fundamental at the moment of the trigger. In Liquid mode, the pitch envelope sweeps downward from this set pitch over the decay, so each kick step has a different starting frequency and therefore a different perceived pitch and weight. Low notes produce heavy drops; higher notes produce brighter, tighter kicks. Zadar controls the Decay length per step: a short Zadar envelope tightens the kick for rhythmically active steps; a longer one extends the sustain for accented beats. Adjust the Pitch knob clockwise to shift the entire sequence up; this raises the starting point of every Liquid pitch drop, changing the overall register of the bassline. The SSG Stereo Field's FREQ control can trim the top end of the BIA if the attack is too bright for the mix context.

**Result:** A sequenced kick bass with per-note pitch variation from the Hermod+ sequence and per-note decay variation from Zadar, producing a rhythmically and tonally expressive bass voice from a drum synthesizer.

---

### Patch 3: Metal Texture with CV-Controlled Spread and Fold

BIA in Metal mode, Alto range, with Spread and Fold modulated by Pons Asinorum LFO channels for continuously evolving metallic texture that transitions between pitched FM percussion and pure noise.

```
[Hermod+ Clock Out] ─────────[G]──────▶ [BIA Trig In]
[Pons Asinorum Out 1] ───────[C]──────▶ [BIA Spread CV In]
[Pons Asinorum Out 2] ───────[C]──────▶ [BIA Fold CV In]
[Pons Asinorum Out 3] ───────[C]──────▶ [BIA Morph CV In]

[BIA Out] ───────────────────[A]──────▶ [Qu-Bit Aurora In L]
[Aurora Out L] ──────────────[A]──────▶ [MixUp CH1 L]
[Aurora Out R] ──────────────[A]──────▶ [MixUp CH1 R]

                                         Mode: Metal
                                         Range: Alto
                                         Pitch: center
                                         Spread knob: center (PA modulates full range)
                                         Morph knob: center
                                         Attack: left of center (some noise)
                                         Decay: 2 o'clock
                                         Harmonic: 3 o'clock (multiple modes active)
                                         Fold knob: center
                                         PA CH1: LFO mode, up/down, 8 seconds
                                         PA CH2: LFO mode, up/down, 11 seconds
                                         PA CH3: LFO mode, ramp up, 5 seconds
```

**Setup:** Set Hermod+ to a regular clock at the desired tempo and patch it to Trig. Set three Pons Asinorum channels to LFO mode at coprime cycle lengths (8, 11, and 5 seconds, or similar non-related values) and route them to Spread, Fold, and Morph CV respectively. Route BIA's output into Qu-Bit Aurora at a moderate reverb setting for spatial depth. Metal mode and Alto range place the synthesis in the midrange metallic zone.

**Controls:** With the three LFOs sweeping Spread, Fold, and Morph at different rates, the BIA's timbral character rotates through a large space without repeating in a predictable cycle. When all three LFOs align near their maxima, the sound becomes densely inharmonic and folded; when they align near their minima, it pulls back toward a cleaner, more pitched FM bell character. Because the LFO cycle lengths are coprime, the three-way alignment point returns only rarely, producing variation that sustains interest over long durations. Attack left of center adds noise to each hit; increasing it further increases the noise transient character. Aurora's reverb blurs the metallic transients into a longer tail; adjust Aurora's Warp CV from an additional PA channel for spectral movement in the reverb itself.

**Result:** A self-evolving metallic texture source driven by a clock, whose spectral character continuously transforms from FM percussion to dense noise and back without any manual intervention. The periodicity of the Pons Asinorum LFOs ensures the variation is structured rather than random.

---

### Patch 4: Melodic Voice in Treble Range

BIA in Skin mode, Treble range, operated as a pitched melodic voice with V/oct tracking, Morph CV from Pons Asinorum for timbral movement, and Harmonic CV from Zadar for per-note complexity variation.

```
[Hermod+ Gate Out] ──────────[G]──────▶ [BIA Trig In]
[Hermod+ Pitch CV Out] ──────[C]──────▶ [BIA Pitch CV In]
[Pons Asinorum Out 1] ───────[C]──────▶ [BIA Morph CV In]
[Zadar CH1 Env Out] ─────────[C]──────▶ [BIA Harmonic CV In]
[Hermod+ Gate Out] ──────────[G]──────▶ [Zadar Trigger CH1]

[BIA Out] ───────────────────[A]──────▶ [SSF SSG Stereo Field IN-L]
[SSG Stereo Field OUT-L] ────[A]──────▶ [MixUp CH2]

                                         Mode: Skin
                                         Range: Treble
                                         Pitch knob: center
                                         Spread: 10 o'clock (slightly inharmonic)
                                         Morph knob: center (PA offsets)
                                         Attack: right of center (slow, clean)
                                         Decay: 3 o'clock (longer sustain)
                                         Harmonic: 9 o'clock (baseline, Zadar sweeps up)
                                         Fold: 9 o'clock (light)
                                         PA CH1: LFO mode, up/down, 7 seconds
                                         Zadar CH1: slow rise, medium hold, quick decay
```

**Setup:** Set Treble range to shift the BIA four octaves above Bass. In Treble range, the Pitch CV 1V/oct tracking is active and the module produces clearly pitched tones in the melodic register. Skin mode keeps the oscillators from pitch-dropping as Liquid would, producing stable pitched notes that sustain at constant pitch. Set a melodic sequence on Hermod+ in a scale appropriate for the patch. Pons Asinorum LFO modulates Morph slowly; Zadar adds Harmonic complexity on each note and decays back, so notes begin with a specified harmonic density that decreases through the note's duration.

**Controls:** Tune the Spread knob to a slight clockwise position for subtle inharmonicity that keeps the tones interesting without sounding like pure noise. Increase Decay to hold notes through long sequence steps. The Zadar envelope adds Harmonic complexity at the note's beginning and pulls back to the baseline level during the note's body, creating an attack-forward brightness that fades into a simpler sustain. The Pons Asinorum LFO sweeps Morph continuously, gradually shifting all six oscillators' waveforms between sine and triangle and back, producing timbral drift that is slower than any individual note and changes the quality of the melodic sequence phrase by phrase. Route through the SSG Stereo Field in Skin mode with a moderate FREQ to roll off the upper harmonic content from Fold for a warmer final tone.

**Result:** A pitched six-mode melodic voice with internally generated timbral movement, operating in the register of a conventional synthesizer voice without any added VCA, envelope, or filter required. The internally managed amplitude envelope of the BIA produces a shaped note event from each trigger, fulfilling the EVENT_VOICE role in a melodic rather than percussive context.

---

## Common Mistakes

### "The output is way too loud and clips everything downstream"

The BIA's output level varies significantly with parameter settings, and the amplitude compensation built into the infinifold is designed to preserve punch at high Fold settings rather than to maintain a consistent output level across all settings. High Fold values and dense Harmonic settings can produce output levels that are much louder than the same module at minimal settings.

**Fix:** Place an attenuator between BIA Out and the destination. The output is described as low-impedance, meaning it drives most inputs cleanly, but the level itself requires management in the patch. Fold is the primary driver of output variation; lowering Fold brings the level down more than any other single control. In a full patch, set Fold last after the other parameters are dialed in and the level relationship to other voices is established.

---

### "The Pitch knob doesn't seem to do much, or the CV isn't tracking correctly"

The knobs on the BIA offset the CV input rather than attenuating it. If a CV signal with significant voltage is patched into a CV input, the knob shifts the center point of the CV's range. A Pitch CV running 0-5V with the knob at minimum will track 0-5V starting from the knob's minimum offset; the same CV with the knob at maximum will track 0-5V from a much higher starting pitch. If the knob appears to do nothing, the CV voltage may be so high that the knob's offset range is entirely within the CV's operating window.

**Fix:** Set the knob to center position as a baseline for any CV-controlled parameter. With the knob at center, the CV input operates in a range where the knob has meaningful offset effect in both directions. For Pitch CV specifically, tune the sequence to the register you want with the knob at center and use the knob to transpose up or down from there.

---

### "Spread at maximum sounds similar to Spread at minimum: I expected more inharmonic content at one extreme"

The variable sample rate system aligns aliasing with harmonic multiples, which works best at settings with strong harmonic structure. At both extremes of Spread (fully harmonic and fully prime-series intervals), the sample rate optimization produces a cleaner result; intermediate settings produce more aliasing character. This can make the two extremes sound more similar than expected while intermediate Spread positions sound noticeably different.

**Fix:** Listen through the full Spread range slowly rather than comparing only the extremes. The most inharmonic character often occurs in the mid-to-upper range of Spread rather than at the maximum. In Metal mode, Spread's effect on FM operator ratios interacts differently than in Skin or Liquid, and the same knob position produces different results across the three modes.

---

### "Attack fully left adds a lot of noise but I want a noisy attack without the noise dominating the tone"

Attack left of center adds noise to the attack transient, and the further left the knob goes, the more the noise component dominates. At extreme left positions the noise can overwhelm the tonal content from the oscillators, particularly at low Harmonic settings where only one oscillator is contributing.

**Fix:** Increase Harmonic to bring more tonal oscillators into the mix, which balances the noise against the tonal content. Alternatively, keep Attack only slightly left of center for a subtle noise transient rather than a dominant one. The interaction between Attack (noise amount) and Harmonic (tonal density) is the primary mix control for the transient character; both need to move together to maintain the intended balance.

---

### "Metal mode doesn't sound like drums at all: it just sounds like noise"

Metal mode is a six-operator FM synthesizer designed to produce "noisy and alien sounds," as the manual describes it. It is not intended to produce recognizable acoustic drum characters. At high Spread and Fold settings, Metal mode produces pure noise texture rather than shaped percussion.

**Fix:** Reduce Spread toward center or fully counterclockwise to bring more pitch coherence to the FM network. Reduce Fold to lower the harmonic density. Set Harmonic to the lower half to reduce the number of active FM operators. In Metal mode, lower parameter settings produce more tonal FM character while higher settings produce noise; the usable percussion territory exists in the lower half of the parameter range for most players. High Metal mode settings are more useful as noise texture or experimental sound design than as conventional percussion.

---

### "Switching modes or ranges mid-patch causes a large jump in pitch or level"

The Bass/Alto/Treble switch offsets pitch by two or four octaves; switching while a sequence is playing produces immediate pitch transposition. The Skin/Liquid/Metal switch changes the synthesis architecture, which can also produce level differences because the three modes generate different amounts of oscillator energy at the same parameter settings.

**Fix:** If mode switching is intended as a performance gesture, manage the output level with an attenuator and tune the sequence to account for the register change before switching. The S/L/M and B/A/T CV inputs allow automated and gradual control of the switch positions, which is smoother than manual switching. A short gate into S/L/M CV at precise timing can switch modes at the start of a phrase rather than mid-phrase, which produces cleaner results in context.

---

## Advanced Learning Path

Begin with Skin mode in Bass range and work through the Harmonic parameter's four distinct zones in sequence. Start fully counterclockwise: one oscillator, one mode, simple tone. Move slowly through the first quarter and listen to the second mode fade in; adjust Decay to hear how the two modes' relative decay times differ. Continue through the middle range and hear the remaining four modes extend their decays one by one. At maximum Harmonic all six modes are active at full amplitude and maximum decay. Return slowly and map exactly where each mode's contribution begins and ends. This mapping is the foundation for using the BIA's most distinctive parameter intelligently.

Compare the three Attack zones with the same sound. Set Decay and Harmonic to a fixed mid-range position. Move Attack from fully left (maximum noise transient) to center (analog pop) to fully right (slow attack, clean). The three zones produce three distinct transient characters that serve different musical functions: left of center for snare-like noise attack, center for crisp kick transient, right of center for tonal swell without percussive impact. None of these is better than the others; all three occupy different positions in a mix and require different treatment downstream.

Work through the Fold parameter's two behavioral zones. Set everything else fixed and move Fold from fully counterclockwise to three-quarters: this is the threshold zone, where the folder adds harmonic stages as the threshold drops and signal amplitude crosses it. Note how the amount of folding depends on both the Fold position and the current amplitude; louder oscillator settings fold more than quieter ones at the same Fold position. Then continue into the top quarter: a pulse train mixes in and the character changes from folded waveshaping to a buzzing, aggressive density. This top quarter is a distinct sound, not a continuation of the first three quarters, and is useful for very specific applications rather than as the default maximum fold position.

Explore Liquid mode as a melodic bass instrument rather than a percussion synthesizer. Patch a V/oct sequence from Hermod+ into Pitch CV, set Range to Bass, and build a bassline using Liquid's internal pitch envelope as the only pitch modulation. Each note begins at the sequenced pitch and drops; the depth and duration of the drop depend on Pitch and Decay settings. By adjusting these two parameters together, the same sequence produces a range of bass voices from a gentle pitched bass guitar simulation to an extreme electronic bass drop, all from the same trigger-per-note sequence.

Investigate the S/L/M and B/A/T CV inputs for real-time mode and range switching. The CV inputs respond to voltage to select between the switch positions, which allows automated transitions between modes and ranges that are impossible to perform manually in time. Patching a stepped CV sequence from Hermod+ into S/L/M switches synthesis modes per step; the same drum pattern in Skin, Liquid, and Metal modes produces three different sounds that can rotate through a sequence automatically. Combine this with a second stepped CV into B/A/T to change both mode and range per step, producing a drum pattern that cycles through six different sonic territories automatically.

Build a self-patching configuration using BIA Out through an attenuator into Fold CV. The BIA's own audio output modulates its own fold threshold: louder hits fold more heavily and quieter hits fold less, creating a dynamic relationship between signal level and harmonic content that is different from both fixed Fold settings and external CV modulation. Set the attenuator so the self-modulation adds subtle variation rather than extreme feedback; the effect is a perceived loudness compression with simultaneous spectral expansion, where the loudest hits are the brightest rather than the most compressed.

Use BIA in Treble range as a primary melodic voice in a patch where no conventional VCO is present. Route the output through the SSF SSG Stereo Field as a low-pass gate for amplitude shaping, feeding Trig into both the BIA and the SSG Stereo Field's EXCITE input. This gives the BIA a second amplitude envelope stage from the SSG, which shapes the note event with a physical LPG decay on top of the BIA's internal amplitude control. The combination of BIA's internal envelope and the SSG's coupled filter-amplitude response produces a voice with a two-stage dynamics and spectral character that neither module generates alone.

For a complete percussion system from two modules, assign BIA in Liquid Bass mode for kick and configure the Pons Asinorum in quadrature ring mode to generate four modulation signals. Patch the four PA outputs to BIA Spread, Fold, Decay, and Morph CV inputs. The quadrature ring produces four phase-offset modulations that slowly rotate the BIA's spectral character through the kick's duration; the same kick pattern sounds different on each cycle as the quadrature phases evolve. Retrigger the PA ring with the Hit button at phrase boundaries to reset the phase relationships and reintroduce controlled variation into the kick's evolving character.

---

## Pairs Well With

**Noise Engineering Pons Asinorum** is the BIA's natural modulation partner within the NE ecosystem, and the two modules share a trigger threshold (~3V) that makes direct connection without buffering straightforward. The PA's four envelope and LFO channels can simultaneously modulate BIA's Spread, Fold, Morph, and Harmonic CV inputs, providing a complete modulation bus from one 6HP module. Because the PA's knobs offset CV rather than attenuate it, both modules share an identical control philosophy: the knob sets the baseline, CV provides the movement, and the interaction is additive rather than multiplicative. Using PA in quadrature ring mode against the BIA produces a slowly rotating four-dimensional spectral space that takes significant time to complete a full cycle, making the combination suitable for long-form generative sessions.

**SSF SSG Stereo Field** provides the amplitude and timbral shaping stage that the BIA's outputs benefit from before reaching the mix. Routing BIA Out into SSG IN-L and triggering the SSG EXCITE input from the same clock creates a two-stage dynamic: BIA handles all spectral content generation, and the SSG provides a second low-pass gate response that adds the coupled filter-amplitude bloom of LPG processing to the BIA's already shaped output. The combination produces a percussion voice with the spectral density of the BIA and the organic resonance decay of an LPG simultaneously, which is sonically distinct from either module alone and fills the kick or melodic percussion role in a larger patch without additional modules.

**Qu-Bit Nautilus** receives BIA well as an audio source because Nautilus's reverb algorithms operate on spectral content, and the BIA in Metal mode produces dense, harmonically varied content that the reverb's internal processing redistributes into long sustaining tails. Routing BIA Liquid mode kick through Nautilus at a low Resolution setting produces a tuned reverb tail that follows the kick's pitch drop, sustaining the descent as a pitched resonance after the kick itself has decayed. ENV OUT from a companion SSG Stereo Field patched to Nautilus Resolution CV connects the reverb character to the dynamics of the BIA's trigger rhythm.

**Qu-Bit Aurora** serves BIA well in Metal mode, where Aurora's FFT-based spectral processing operates on the dense inharmonic content that Metal mode generates. Setting Aurora to high FFT sizes and long spectral decay blurs the metal transients into a sustained shimmer that outlasts the gate by several seconds, converting a percussive impact into an ambient texture while preserving the frequency character of each hit. Warp CV from Pons Asinorum sweeping the spectral transformation produces a sound that shifts between recognizable metallic percussion and pure granular blur on each phrase boundary, without changing the BIA's parameters.

**Bela Gliss** in Notes Sequencer mode provides a five-note pitched sequence for BIA in Treble range, with the Bottom Output's differentiated trigger voltage (+10V on step one, +5V on subsequent steps) producing a louder or more complex response from the BIA's Fold and Harmonic parameters when both voltages are simultaneously routed to those CV inputs via a mult or stackable cables. The first step of each phrase produces a brighter, more complex hit; subsequent steps produce a slightly different character. Gliss's live step muting and step-order changing during playback also provides real-time pattern variation for the BIA sequence without stopping playback or disconnecting the trigger chain.

**Zadar** pairs with BIA as a per-note Harmonic and Decay CV source in melodic applications. In Liquid Bass mode with a pitched sequence from Hermod+, Zadar's four channels can provide per-note shaping of Decay (note length), Harmonic (tonal complexity), Fold (spectral density), and Spread (inharmonic character) simultaneously, all synchronized to the same gate. Each note in the sequence triggers Zadar, which fires its four channel envelopes into the BIA's four CV inputs, producing a note event where all spectral parameters are shaped by Zadar's envelope curves rather than by fixed knob positions. The result is a melodic bass voice with a different timbral contour on every note, without changing the sequence or the patch routing.
