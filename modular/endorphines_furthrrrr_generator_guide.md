---
title: Endorphin.es Furthrrrr Generator
manufacturer: Endorphin.es
primary_role: SOURCE
secondary_roles: [SHAPER]
historical_context: true
form_factor: eurorack
functions: [complex-oscillator, wavefolder]
behavior_tags: [harmonic, metallic, harsh, evolving, inharmonic, nonlinear, self-modulating]
use_cases: [west coast synthesis, FM sound design, harmonic exploration, complex timbres]
hp: 30
memory: none
transport: none
screen: false
hybrid: false
cv: full
---

# Endorphin.es Furthrrrr Generator

![Endorphin.es Furthrrrr Generator](https://github.com/Shadoe-42/music/raw/main/modular/images/endorphines/furthrrrr_generator/front_panel.jpg)

*Dual analog complex oscillator with through-zero FM capability, three-dimensional waveshaping, and a unified Mood Index modulation bus, built on West Coast synthesis principles.*

---

## Historical Context

In 1963, Don Buchla began developing electronic instruments in San Francisco at the request of dancers and composers working at the San Francisco Tape Music Center. His 100 Series modular synthesizer appeared at almost exactly the same moment as Robert Moog's instruments on the East Coast, but from a fundamentally different design philosophy. Where Moog centered his approach on voltage-controlled subtractive synthesis (rich waveforms filtered down to sculpted timbres), Buchla refused this premise. His instruments generated complex waveforms through waveshaping and additive-adjacent techniques, treating the oscillator itself as the primary timbral sculptor rather than a raw material for filtering. Buchla also rejected the keyboard as a primary controller. His was an instrument for composers working in new territory, not for translating existing instrumental gestures into new sounds.

The Buchla 259 Programmable Complex Waveform Generator, introduced as part of the 200 Series in the early 1970s, crystallized the West Coast complex oscillator concept. It paired two oscillators: a programming oscillator (the modulator) and a principal oscillator (the carrier), with the modulator capable of frequency-modulating the carrier and feeding into a dedicated waveshaping circuit. The companion Buchla 258 Waveshaper gave the carrier three-dimensional control over harmonic content: a sine wave entering the circuit could be transformed across a space defined by even harmonics, odd harmonics, and the degree of wavefolder saturation. This three-axis harmonic architecture remains the direct ancestor of the Furthrrrr Generator's own symmetry, order, and furthrrrr controls.

John Chowning at Stanford University formally described frequency modulation synthesis in 1967, demonstrating that modulating one oscillator's frequency with another at audio rates produces harmonic sidebands whose density and character depend on the frequency ratio and modulation depth. Yamaha licensed his findings and the DX7 in 1983 brought FM synthesis to a mass audience in digital form. Analog FM introduced a complication: standard analog oscillators slow and stop as the modulation signal crosses zero, creating an asymmetry in the sideband structure and restricting the timbral palette. Through-zero FM addresses this by allowing the carrier oscillator to continue through the zero crossing with a phase reversal, producing symmetric sidebands and deeper metallic timbres. The Strong Zero VCO Core, an optional replacement chip for the Furthrrrr Generator, implements true TZFM in analog hardware, extending the module's timbral range into territory that standard oscillator cores cannot reach.

Endorphin.es was founded in 2013 in Barcelona, Spain, as Furth Barcelona S.L., developing performance-focused Eurorack modules with a distinctive character: aggressive timbral range, precise engineering, and circuits pushed toward unusual territory. The Furthrrrr Generator is their complex oscillator, designed from scratch using modern components rather than cloning the 259 circuit directly. The manual is explicit on this point: the module is inspired by and based upon the Buchla 259's routing logic, but all circuit parts were developed independently with modern tolerances and without vactrols. The result preserves the architectural logic of the West Coast tradition while adding contemporary capabilities: audio-frequency modulation across all parameters, a unified Mood Index modulation bus, and multi-turn potentiometers with integrated LED tuners. The manual's instruction to forget about the waveforms is the clearest possible restatement of the Buchla philosophy: the output is defined by harmonic relationships, not waveform shapes.

---

## Quick Start

The Endorphin.es Furthrrrr Generator is a dual analog complex oscillator in which a Modulator oscillator and a Carrier oscillator are connected through a unified modulation bus called the Mood Index. The Carrier's output passes through a three-stage waveshaping section before reaching the final outputs. The Modulator can simultaneously frequency-modulate, ring-modulate, amplitude-modulate, and waveshaper-modulate the Carrier, in any combination, at any depth.

1. Patch the Carrier final output (the jack marked with a triangle icon, lower right of the module) to your audio path or VCA input.
2. Patch a V/oct source into the Carrier key in jack.
3. Turn the large Carrier frequency knob until both Looney Tuner LEDs light simultaneously: both lit indicates a perfect A note.
4. Keep symmetry, order, and furthrrrr fully counterclockwise. You will hear a pure sine wave from the Carrier.
5. Slowly rotate furthrrrr clockwise. The sine wave folds progressively, adding harmonic content. This is the waveshaper in action.
6. With furthrrrr at noon, introduce symmetry: counterclockwise pushes toward even harmonics; clockwise pushes toward odd harmonics and a narrower pulse character.
7. Add order at a low setting to bring forward higher harmonics. Adjust all three together to explore the harmonic space.
8. Enable the Frequency destination toggle on the Mood Index section and raise the Mood Index knob to 9 o'clock. The Modulator now frequency-modulates the Carrier.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 30 HP |
| Depth | 25 mm |
| Power | 180 mA +12V / 215 mA -12V / 0 mA +5V |

---

## Essential Parameters

**Carrier Frequency and Modulator Frequency.** Each oscillator uses a multi-turn potentiometer requiring approximately ten full rotations to sweep all ten octaves of the module's range, with each revolution covering roughly one octave. Precise tuning is achievable without trimmer adjustments mid-performance. The Looney Tuners (two LEDs flanking each frequency knob, labeled Ab and A#) provide a continuous pitch reference: the left LED lit indicates the oscillator is below the nearest A note, the right LED lit indicates above, and both lit simultaneously indicates a perfect A. The oscillators span from approximately 10 Hz to 10 kHz; the Modulator can drop into LFO range (down to ~0.22 Hz per cycle) by engaging the low-range switch at the top-left of the Modulator section. Each oscillator accepts exponential CV at the cv in jack (with a black attenuverter for bipolar control), a direct 1V/oct input at key in, and linear FM at the fm in jack (with a red attenuator).

**Furthrrrr.** The furthrrrr knob is the primary waveshaping control on the Carrier's harmonic section. With all three waveshaper knobs fully counterclockwise, the Carrier produces a pure sine wave at its final outputs. Rotating furthrrrr clockwise increases the drive level into the wavefolder, progressively adding harmonic content as the sine folds over on itself. The output does not behave like a traditional waveform selector: the waveshaper sculpts a continuous distribution of harmonics, and the furthrrrr knob determines how deeply that sculpting proceeds. A waveshaper CV input allows external voltage to control fold depth in real time.

**Symmetry.** The symmetry knob controls the balance between even and odd harmonics in the waveshaped output. Rotating clockwise attenuates even harmonics and emphasizes odd harmonics; rotating counterclockwise does the inverse. At maximum clockwise, only odd harmonics are present and the Carrier square output reaches a 50% duty cycle. Moving symmetry counterclockwise introduces even harmonics and narrows the square pulse width toward a thin spike wave. When the order knob is at maximum, symmetry additionally defines the transition between saw-like and square-like character, recreating the behavior of the Buchla Model 258 waveshaper in that configuration.

**Order.** The order knob saturates the presence of higher harmonics in the waveshaped output. At minimum counterclockwise, the fundamental harmonic dominates. As order increases clockwise, progressively higher-order harmonics are brought forward, adding upper-register brightness and complexity. Order interacts with furthrrrr and symmetry simultaneously: the combination of all three knobs defines a three-dimensional harmonic space rather than a linear spectrum. A practical approach is to establish the overall character with furthrrrr and symmetry first, then use order to adjust harmonic brightness.

**Mood Index Knob and Destination Switches.** The Mood Index is the central modulation bus. It routes the Modulator to four distinct destinations on the Carrier, each activated by its own toggle switch: amplitude (Modulator controls Carrier output level; sub-audio rate produces tremolo, audio rate produces ring-mod-like artifacts), balanced (ring modulation: Modulator multiplies Carrier signal, producing sum and difference frequencies plus intermodulation sidebands), frequency (Modulator FM-modulates Carrier pitch; switchable between linear and exponential via a jumper on the PCB back), and furthrrrr (Modulator modulates the waveshaper's furthrrrr control, producing dynamic harmonic variation). The Mood Index knob acts as a unified wet/dry control across all active destinations: fully counterclockwise bypasses all Mood Index modulation regardless of which destination toggles are engaged. A CV input at the mood index jack allows external voltage to control modulation depth in real time. All four destinations can be active simultaneously.

**Mood Wave Selector.** The mood wave selector button (top-left of the module) cycles through the waveform used as the Mood Index modulation source. Options include Modulator sine, saw, square, flat noise, a sample-and-hold output clocked at Modulator frequency, and external input. Selecting external input activates the ext. in jack, which accepts any patched signal as the Mood Index source, replacing the Modulator for that function. The red LED lighting on the selector indicates external input mode is active.

**Lock Switch.** The three-position lock toggle pre-routes Modulator sync to the Carrier without requiring a patch cable. Left position enables soft sync from the Modulator: rather than resetting the Carrier's cycle, soft sync inverts the waveform direction at the half-cycle, producing complex harmonic saturation. Right position enables hard sync: the Carrier fully restarts its cycle each time the Modulator resets, enriching all outputs with even and odd harmonics and producing a tearing, ripping character. Center disconnects sync entirely. Individual external sync input jacks on each oscillator allow independent sync routing from external sources, bypassing the lock switch pre-routing.

---

## Why This Instrument Excels

The Furthrrrr Generator's most significant quality is that FM synthesis and waveshaping are not two functions coexisting in a single panel: they are architecturally integrated through the Mood Index bus. In a conventional patch using separate oscillators and a wavefolder, FM affects pitch and the wavefolder responds to whatever waveform arrives at its input independently. In the Furthrrrr Generator, the Modulator can simultaneously frequency-modulate the Carrier, ring-modulate it, amplitude-modulate it, and modulate the waveshaper's furthrrrr control, all governed by a single depth knob, all affecting the same signal as it moves through the Carrier's circuit path. The timbral behavior this produces cannot be replicated by combining separate modules, because the modulations interact within the signal path rather than acting on it from outside.

The Mood Index bus fundamentally changes what it means to perform with a complex oscillator. Instead of managing individual cables from a Modulator output to FM inputs, amplitude inputs, and waveshaper CVs separately, the Mood Index collapses all four destinations into a single depth control with four on/off switches. A single knob movement simultaneously deepens or withdraws all active modulations together. The modulation source can be swapped between Modulator waveforms and external signals without interrupting audio. During a performance, the combination of Mood Index depth, destination switch selection, and mood wave source creates a timbral control surface that responds continuously to a single hand gesture, not a multi-parameter adjustment procedure.

Every design decision in the Furthrrrr Generator reflects a performance-first philosophy, and the Looney Tuner LED system exemplifies this. Traditional VCO tuning requires a utility tuner module, a reference tone through headphones, or careful monitoring while adjusting. The Furthrrrr Generator's LED tuners continuously scan each oscillator's frequency and indicate proximity to the nearest A note: one LED for sharp, one for flat, both lit for exact. A musician can retune both oscillators to a known harmonic relationship in seconds without interrupting a performance and without additional modules. Combined with multi-turn frequency knobs that prevent accidental detune from minor physical contact, factory trimming to stable 1V/oct tracking, and 10-minute thermal stabilization for drift-free tuning, the module is designed to stay in tune and under control across extended performances in ways that standard VCOs often are not.

Standard analog FM synthesis is limited by the behavior of the oscillator core as the modulation signal approaches zero: the carrier slows and stops, producing an asymmetry in the sideband structure that restricts the timbral palette to one side of the FM spectrum. Through-zero FM, implemented via the Strong Zero VCO Core chip, allows the carrier to pass through zero frequency with a phase reversal, maintaining oscillation through the entire modulation cycle. The practical result is access to a class of metallic, bell-like, and deeply inharmonic timbres unavailable from standard FM, particularly at high modulation indices where a standard core would simply halt. Combined with the Furthrrrr Generator's waveshaping section, which already operates in harmonic territory beyond standard waveform synthesis, TZFM extends the timbral range further: from near-pure sine tones through dense harmonic complexity to asymmetric inharmonic metallic sounds that belong to no standard synthesis category.

---

## Mood Index Destinations Reference

| Destination | What it modulates | Sub-audio rate character | Audio rate character |
|-------------|------------------|--------------------------|----------------------|
| Amplitude | Carrier final output level | Tremolo | Ring modulation artifacts |
| Balanced | Carrier signal (ring mod) | Mild intermodulation sidebands | Full ring modulation, carrier suppression |
| Frequency | Carrier pitch (FM) | Vibrato; pitch inflection | FM sidebands; timbral density |
| Furthrrrr | Carrier waveshaper fold depth | Slow harmonic sweep | Rapid timbral animation |

---

## Patches

### Patch 1: Carrier Waveshaper Exploration

```
[V/oct source]---[C]---> Carrier key in
                                |
                        CARRIER VCO (sine core)
                                |
                  [furthrrrr] [symmetry] [order]
                                |
                        Carrier final out
                                |
[A]-----------------------------+-----> audio output / VCA
```

**Setup:** Patch a V/oct source to Carrier key in. Patch the Carrier final output (triangle icon jack) to your audio chain. Set symmetry, order, and furthrrrr fully counterclockwise. Leave the Mood Index destinations all off.

**Controls:** Play a note and confirm pitch tracking using the Looney Tuner LEDs (both lit = A note; use this to set a known reference pitch). With the oscillator confirmed in tune, slowly rotate furthrrrr clockwise. The pure sine begins to fold, adding harmonic content. At approximately noon, introduce symmetry counterclockwise (even harmonics, broader sound) and clockwise (odd harmonics, narrower pulse-like character). With furthrrrr at maximum, bring order in gradually to add upper harmonic brightness. Map the corners of the three-knob space systematically.

**Result:** A single analog oscillator producing continuously variable harmonic content from pure sine to complex waveshaped timbres. This establishes the Furthrrrr Generator's foundational character: the waveshaper is not a waveform selector but a three-dimensional harmonic sculpting tool, and all subsequent patches build on this foundation.

---

### Patch 2: Locked Sync with Mood Index FM

```
[V/oct]---[C]---> Carrier key in      [V/oct]---[C]---> Modulator key in
                        |                                       |
                CARRIER VCO                            MODULATOR VCO
                        |                                       |
         Lock switch: LEFT (soft sync) <----- pre-routed ------+
                        |
                Carrier final out
                        |
[A]---------------------> audio output
```

**Setup:** Patch a V/oct source to both Carrier and Modulator key in jacks. Set the lock switch to the left position (soft sync from Modulator to Carrier). Enable the Frequency destination toggle on the Mood Index section. Set the Mood Index knob to 9 o'clock.

**Controls:** Use the Looney Tuners to set the Modulator one octave above the Carrier. At this frequency ratio, FM via Mood Index produces odd harmonics in the Carrier output. Raise the Mood Index knob slowly to deepen the FM effect: the Carrier's timbre becomes denser without the pitch becoming unstable at moderate depth. Now the lock switch is already engaged (left position): the Carrier's waveform direction inverts on each Modulator half-cycle, adding complex harmonic saturation on top of the FM. Try moving the Modulator frequency knob through different ratios relative to the Carrier: integer ratios (2:1, 3:1) produce harmonic sidebands, non-integer ratios produce inharmonic metallic content.

**Result:** The combination of soft sync and Mood Index FM produces timbres unavailable from either technique in isolation. This is the Furthrrrr Generator's characteristic identity: FM synthesis and oscillator synchronization working on the same signal simultaneously, each shaping the other's effect.

---

### Patch 3: Furthrrrr Modulation and Internal Cross-FM

```
Carrier final out --[pre-routed internal]--> Modulator lin fm in
                                                      |
[V/oct]---[C]---> Carrier key in          MODULATOR VCO
                        |                  [low-range switch ON]
                CARRIER VCO                           |
         [furthrrrr][symmetry][order]      Mood Index bus:
                        |                  [Frequency dest: ON]
                Carrier final out [A]      [Furthrrrr dest: ON]
                        |
[A]---------------------> audio output
```

**Setup:** No additional cables are needed for internal cross-modulation: the Carrier final output is pre-routed internally to the Modulator's linear FM input when no cable is inserted into the Modulator fm in jack. Enable the Modulator low-range switch to drop the Modulator into LFO range. Enable both the Frequency and Furthrrrr destinations on the Mood Index section. Set the Mood Index knob to 10 o'clock.

**Controls:** With the Modulator cycling slowly in LFO range and both Frequency and Furthrrrr Mood Index destinations active, the Carrier's pitch and harmonic content shift together in slow cycles governed by the Modulator's rate. Raise the Mood Index knob to deepen both modulations simultaneously. Patch external CV to the Mood Index jack to make modulation depth respond to an envelope or external LFO. Engage the Modulator's hard sync input from an external clock to snap the modulation cycles to a rhythmic grid.

**Result:** The internal cross-FM feedback path combined with simultaneous Mood Index destinations creates self-modulating timbral behavior that evolves continuously from a minimal patch: one oscillator in LFO mode slowly modulating the other's pitch and harmonic content simultaneously. This demonstrates the Furthrrrr Generator's generative capacity without additional modules.

---

### Patch 4: Full Voice with External Modulation

```
[Mutable Instruments Marbles]
  X1 out --[C]---> Carrier key in
  X2 out --[C]---> Modulator key in
  t1 out --[G]---> envelope trigger
  Y out  --[C]---> Mood Index cv in (attenuated)

[DivKid Ochd]
  LFO 1 --[C]---> Carrier furthrrrr cv
  LFO 2 --[C]---> Carrier symmetry cv (attenuated)
  LFO 3 --[C]---> Modulator cv in (attenuverter at 9 o'clock)

[Endorphin.es Furthrrrr Generator]
  Carrier final out --[A]---> VCA audio in
  Mood Index: Frequency + Furthrrrr destinations ON

[Envelope + VCA]
  Envelope --[C]---> VCA cv in
  VCA out  --[A]---> audio output
```

**Setup:** Patch Mutable Instruments Marbles X1 to Carrier key in and X2 to Modulator key in so both oscillators track Marbles' probabilistic pitch output. Patch Marbles Y (attenuated) to the Mood Index CV input. Patch three DivKid Ochd outputs to the Carrier's waveshaper CVs and the Modulator's cv in. Enable Frequency and Furthrrrr Mood Index destinations. Route the Carrier final output through a VCA triggered by Marbles t1.

**Controls:** Set Marbles DEJA VU to approximately noon so the pitch sequence repeats with moderate probability rather than fully randomizing. Adjust Ochd's rate so waveshaper modulation moves slower than the note rate. Set the Mood Index knob to noon. Let the patch run: Ochd provides continuous waveshaper animation across notes, Marbles Y introduces slow variation in FM and furthrrrr modulation depth, and the harmonic relationship between the two oscillators shifts as Marbles moves them through different pitch relationships. Adjust Mood Index depth to taste.

**Result:** The Furthrrrr Generator becomes a complex generative voice in which pitch, timbre, and modulation depth all vary semi-independently. Marbles controls harmonic relationships between the oscillators; Ochd animates the waveshaper on a long drift cycle; the Mood Index connects both to timbral depth variation. This demonstrates the module's full integration capability and shows why dedicated external modulation sources multiply its timbral range beyond what manual control alone can produce.

---

## Common Mistakes

### "I turned up the Mood Index but nothing is modulating"

All four Mood Index destinations are governed by individual toggle switches, and all are bypassed when no destination is switched on. The Mood Index knob controls depth across all active destinations simultaneously, but if no destination toggle is enabled, the knob has no effect regardless of its position. Check that at least one of the four destination toggles (amplitude, balanced, frequency, furthrrrr) is in the active position before adjusting the Mood Index knob.

### "The pitch shifts wildly when I raise the Mood Index"

The Frequency destination routes the Modulator into the Carrier's FM circuit, and at high Mood Index values this produces substantial pitch variation, especially with exponential frequency modulation mode active (the PCB jumper default). If timbral FM color is the goal rather than pitch instability, reduce the Mood Index knob significantly (start at or below 9 o'clock), or switch the Frequency modulation type to linear via the jumper on the PCB back. Linear FM at high modulation depth keeps the perceived pitch more stable while still producing audible sideband content. Alternatively, use the Furthrrrr destination alone: timbral variation from waveshaper modulation with no pitch movement at all.

### "The waveshaper sounds thin and buzzy, not rich and harmonic"

This typically means the order knob is too high relative to furthrrrr. Order emphasizes higher harmonics, but without sufficient waveshaper drive from the furthrrrr knob, those high harmonics appear without the lower and mid-range harmonic content that gives the waveshaper its characteristic density. Start with furthrrrr to establish the fundamental fold; use order conservatively afterward to add upper harmonic brightness. Bringing order to maximum before establishing furthrrrr level produces a buzzy, thin character rather than the full harmonic texture the waveshaper is capable of producing.

### "My oscillators drift out of tune during a session"

The manual specifies that frequency stabilization takes approximately 10 minutes after power-up. Both oscillators require a warmup period before their tracking becomes thermally stable. Avoid critical tuning in the first 10 minutes after powering the rack. If drift continues after warmup, the V/oct scale trimmers on the PCB back may need adjustment; the manual describes the trimming procedure using the Looney Tuners as a reference. The tuning process is calibrated using an infinite looping sequence of the same note across multiple octaves, comparing the Looney Tuner LED responses at each octave.

### "Soft sync and hard sync sound the same to me"

The audible distinction between soft and hard sync depends significantly on the frequency relationship between the two oscillators. Hard sync fully restarts the Carrier's cycle on each Modulator reset; soft sync inverts the waveform direction at the half-cycle instead. When both oscillators are close to unison, the effect of either sync type is subtle. The distinction becomes clear when the Modulator runs at a higher frequency than the Carrier (3:1 ratio or greater): hard sync produces a brighter, more aggressive tearing quality akin to classic sync leads; soft sync produces a denser, more complex harmonic saturation with a less regular waveform shape. Set the Modulator two to three octaves above the Carrier and compare the two lock switch positions directly.

---

## Advanced Learning Path

1. Spend a full session with the Carrier waveshaper alone before introducing the Modulator. Set furthrrrr, symmetry, and order all fully counterclockwise (pure sine), then methodically explore each axis: furthrrrr alone, symmetry alone, order alone, then pairs, then all three together. Map the corners and edges of the harmonic space by ear before adding Mood Index complexity. The waveshaper's three-dimensional behavior becomes intuitive only through this kind of systematic exploration, and that intuition is the foundation for all subsequent work with the module.

2. Study each Mood Index destination individually. Enable one destination toggle at a time and sweep the Mood Index knob from minimum to maximum with the Modulator running at a slow sub-audio rate. Listen carefully to what amplitude modulation does to the Carrier output versus balanced modulation, frequency modulation, and furthrrrr modulation. Each destination has a distinct sonic identity; understanding them separately makes combining them intentional rather than cumulative noise.

3. Develop a vocabulary of FM frequency ratios. The harmonic character of FM synthesis changes dramatically based on the ratio between Modulator and Carrier frequency. Integer ratios (1:1, 1:2, 2:3, 3:4) produce harmonic sidebands with musical pitch relationships; non-integer ratios produce inharmonic metallic content. With the Frequency Mood Index destination active, use the Looney Tuners to set each oscillator to known pitches and listen to the timbral result of each ratio. Map the ratios that produce musically useful timbres for your own work.

4. Use the lock switch as a timbral tool, not a convenience. Soft and hard sync produce different harmonic results and interact differently with the active waveshaper settings. With sync and Mood Index both engaged, slowly sweep the Modulator frequency while maintaining a consistent Carrier pitch. The timbral landscape changes continuously as the sync relationship passes through integer and non-integer ratios. This sweep becomes a performance gesture available without patching any additional cables.

5. Make Mood Index depth an articulated parameter rather than a set-and-forget control. Patch an envelope to the Mood Index CV input and set the Mood Index knob to a low base value. The envelope now controls how deeply the Carrier is modulated on each note: at the envelope attack, modulation depth increases and the timbre opens; at release, it closes. This creates a dynamic timbral envelope entirely independent of amplitude and pitch shaping, adding a dimension of expression not available through standard envelope-to-VCA patching.

6. Explore the external input option on the mood wave selector. Any signal patched to the ext. in jack becomes the Mood Index modulation source, replacing the Modulator for Mood Index purposes. Patch a random CV source (such as a Make Noise Wogglebug stepped output) to ext. in and select external input mode via the mood wave selector. The Carrier's timbre now responds to unpredictable external control while the Modulator remains free for sync, independent audio output, or clock duties. This separation of the Modulator's audio role from its Mood Index role is a significant structural flexibility that rewards exploration.

7. Install the Strong Zero VCO Core chip if through-zero FM timbres are central to your work. The standard triangle core oscillators produce excellent results for most West Coast synthesis applications, but the TZFM capability of the Strong Zero core opens a class of metallic and inharmonic timbres that is simply unavailable from the standard circuit. The core is pin-compatible and the installation procedure is covered in the separate Strong Zero manual. With TZFM enabled, use the linear FM Mood Index destination at high modulation indices to access timbres that require the carrier to pass through zero frequency cleanly.

8. Use the Furthrrrr Generator as the voice in a long-form generative patch with slowly varying pitch and modulation sources. Connect pitch and gate material that evolves slowly (Mutable Instruments Marbles with high DEJA VU, or a slow quantized random source), route organic modulation to the waveshaper CVs (DivKid Ochd or similar), and let the patch run for an extended period. The interaction between the oscillators' internal harmonic structure and slowly varying external control produces behavior that changes on a timescale beyond active performance gesture. This is the module's most direct connection to the West Coast tradition that shaped it: synthesis as a process that unfolds over time, not only a sound design tool operated in real time.

---

## Pairs Well With

**Mutable Instruments Marbles** provides probabilistic V/oct pitch and gate outputs across multiple channels simultaneously, making it an ideal control source for the Furthrrrr Generator's dual-oscillator architecture. Patching Marbles X1 to Carrier key in and X2 to Modulator key in allows the harmonic ratio between the two oscillators to vary with the sequence, so that the FM character of the output shifts across notes rather than remaining fixed. Marbles Y output, attenuated through the Mood Index CV input, introduces slow semi-random variation in overall modulation depth, giving timbral expression a probabilistic dimension that evolves alongside pitch.

**DivKid Ochd** provides eight independent free-running LFOs at organic, non-synchronized drift rates that suit the Furthrrrr Generator's extensive CV input set well. The three waveshaper CV inputs (furthrrrr, symmetry, order) benefit from slow modulation that changes harmonic content on a timescale longer than individual notes. Ochd's Expander unit provides unipolar versions of each LFO output, which are useful for waveshaper inputs that respond well to one-directional sweeps rather than bipolar modulation. Three Ochd outputs routed to the Furthrrrr Generator's waveshaper CVs and Modulator CV input create continuous timbral evolution without any further programming or sequencing.

**Endorphin.es Terminal or Grand Terminal** transforms the Furthrrrr Generator into a two-operator modular FM synthesizer. The Furthrrrr Generator manual explicitly names this combination: Terminal or Grand Terminal provides the filtering, envelope generation, and voice management that complete the FM voice. Terminal's filter section processes the Carrier output while its envelope generators provide amplitude shaping, creating a full performance-ready voice from two Endorphin.es modules built with shared design principles. Together with Terminal's sequencing capabilities and the Furthrrrr Generator's timbral depth, the combination represents the intended performance system context for both modules.

**Make Noise Wogglebug** provides the kind of chaotic, analog-random CV character that connects most directly to the Furthrrrr Generator's West Coast lineage. The Wogglebug's stepped and smooth random outputs, both derived from the same noise source and therefore correlated, give two differently shaped random voltages useful for the Carrier and Modulator CV inputs simultaneously. Patching Wogglebug's Woggle CV output to the Mood Index CV input and its Clock Out to the Modulator hard sync input creates rhythmically punctuated timbral events governed by an organic, irregular clock source, producing unpredictable but coherent harmonic behavior that neither module generates alone.

**A dedicated envelope generator and VCA** complete the Furthrrrr Generator as a discrete voice. The module produces continuous audio from both oscillators whenever the rack is powered and has no internal amplitude envelope. Pairing it with a module that provides attack-decay-sustain-release shaping (Xaoc Devices Zadar, Mutable Instruments Stages, or a simple ADSR) and a VCA gives the voice the articulation needed to serve a musical phrase. The timbral complexity the Furthrrrr Generator generates is most effective when shaped by an amplitude envelope that gives each note a defined start and end, rather than sustaining indefinitely as a continuous drone.
