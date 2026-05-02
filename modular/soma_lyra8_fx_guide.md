---
title: Soma Lyra-8 FX
manufacturer: Soma Laboratory
primary_role: SHAPER
secondary_roles: []
form_factor: eurorack
functions: [delay, distortion, fx-modulation]
behavior_tags: [dirty, warm, chaotic, nonlinear, lo-fi, self-modulating]
use_cases: [lo-fi atmospheric processing, drone generation, textural destruction, dark delay]
hp: 20
depth: 40
historical_context: true
---

# Soma Lyra-8 FX

![Soma Lyra-8 FX](https://github.com/Shadoe-42/music/raw/main/modular/images/soma/lyra8_fx/front_panel.jpg)
*Dual lo-fi delay with self-modulation, cross-feedback, and parallel distortion extracted from the Lyra-8 instrument in 20HP*

## Historical Context

Vlad Kreimer grew up in Donetsk, Ukraine, trained as a radio engineer and working as a musician. The first serious instrument he built was an 8-bit sampler, constructed in the years immediately after the Soviet collapse, at a moment when electronic components were becoming accessible in ways they previously had not been but the commercial infrastructure around synthesizer manufacturing was entirely absent. Kreimer built instruments for himself and his own music, making experimental synthesizers outside any established industry context. That origin is not incidental to what SOMA instruments became. It is the condition under which a different set of assumptions about what an electronic instrument should do had room to develop.

The Lyra-8 was not designed to be a product. Kreimer built it for his own use and posted a demonstration online; the response was large enough that he founded SOMA Laboratory in 2016 to manufacture it. The instrument's defining characteristic is what Kreimer calls "organismic" design, a term he uses to describe synthesis architectures where internal modules relate to each other in nonhierarchical, feedback-capable ways, resembling the structural relationships of biological systems rather than a linear signal chain. The Lyra-8's eight voices are triggered not by keyboard or MIDI but by metal touch sensors that read the player's body capacitance directly. There is no pitch quantization, no fixed tuning reference, and no parameter that behaves identically across all playing conditions. The nonlinearity that most instrument design works to eliminate is here a design goal.

The effects section uses PT2399 delay chips, inexpensive integrated circuits originally manufactured for consumer karaoke echo units, operating at sample rates low enough that the lo-fi character is a structural property of the circuit rather than an added aesthetic. Kreimer configured them in a double-modulated delay with cross-feedback between the two stages, and added a self-modulation path in which the delay output signal modulates its own sample rate. The result is a feedback system rather than a discrete effects chain: the behavior of the delays depends on what is already passing through them, and the relationship changes continuously. The Lyra-8 FX module extracts this specific circuit for Eurorack, adding CV control inputs while leaving the underlying circuit unchanged.

Kreimer describes SOMA's approach as "romantic engineering," by which he means instruments built from a philosophical position rather than a market specification. The Lyra-8 was designed without MIDI because he considered the requirement to quantize pitch and time to a grid a constraint on musical thinking rather than a neutral convenience. The choice to use through-hole components and avoid surface-mount construction was about tactility and repairability. These positions came from a tradition of instrument-making oriented toward building what you needed rather than choosing from what was available, a tradition shaped by the specific conditions of working as an engineer and musician in post-Soviet eastern Ukraine. The Lyra-8 FX carries that origin into the Eurorack format without adapting to its conventions.

## Quick Start: Get Sound in 5 Minutes

Lyra-8 FX is a dual lo-fi delay with self-modulation and parallel distortion. It accepts any audio source and degrades it through cross-feeding PT2399 delay stages that can modulate their own sample rate. The result is never fully predictable and never fully clean. Both are design properties.

1. Patch any audio source into Audio In
2. Set IN volume to 12 o'clock
3. Set Stage 1 and Stage 2 delay times to different positions: Stage 1 at 10 o'clock, Stage 2 at 2 o'clock
4. Set both mod source switches to external CV (no signal needed yet)
5. Set Feedback to 11 o'clock
6. Set Delay mix to 2 o'clock
7. Listen to the cross-feeding delays producing complex repeating patterns
8. Now flip Stage 1 mod source switch to self-modulation and turn Stage 1 mod depth to 1 o'clock
9. Listen to the delay begin to degrade and destabilize as it modulates its own sample rate

The character shift in step 9 is the central behavior. Everything else extends from there.

## Key Specs

| Spec | Value |
|------|-------|
| HP | 20 |
| Depth | 40mm |
| +12V | 90mA |
| -12V | 20mA |
| 5V | 0mA |
| Delay chips | PT2399 ×2 |
| Self-oscillation | Yes (via feedback) |

## Essential Parameters

**Stage 1 and Stage 2 delay time knobs** set the delay length for each of the two PT2399 stages independently. The two stages feed into each other via cross-feedback, so their relative timing determines the rhythmic relationship between the repeating echoes. Matched times produce reinforcement and resonance. Different times produce polyrhythmic delay interactions. Very short times produce comb filtering and chorus-adjacent textures. Very long times produce distinct rhythmic echoes.

**Mod source switches (one per stage)** select whether each stage is modulated by an external CV signal at the mod CV input or by the self-modulation path. In self-modulation mode the stage's own output feeds back to modulate the PT2399 sample rate clock, causing the delay time to vary with the content of the signal currently passing through it. The character of self-modulation depends entirely on what is in the delay: a dense signal produces rapid, complex modulation; a sparse signal produces slower, more isolated warping. External CV mode disconnects this feedback path and accepts a control voltage instead.

**Mod depth controls (one per stage)** set how much the selected modulation source affects the delay sample rate. Low depth produces subtle pitch wobble and instability. High depth produces dramatic sample rate reduction, glitching, and time-stretching artifacts. With self-modulation active and depth high, the stage can become fully unstable. Each stage has its own independent depth control, so one stage can run subtle and the other extreme.

**Feedback** controls how much of the combined delay output recirculates into the input. Below a certain threshold the delays decay normally. As feedback increases, repeating cycles build and sustain into metallic drone tones. Above the self-oscillation threshold the module generates continuous pitched tones without any audio input. Feedback has a CV input for dynamic control of the recirculation amount during performance.

**Distortion** sits in parallel with the delay path and processes the delayed signal. Drive sets the amount of gain and saturation applied. Unlike guitar-pedal distortion circuits designed around guitar frequency content, this circuit processes the full frequency range equally. The distortion mix control blends the distorted signal against the clean delay output. Drive also has a CV input. At audio rate, CV modulation of Drive creates pitched harmonic artifacts unrelated to the delay processing.

**IN volume** controls the input level entering the processing chain. This is the primary level management control and affects how hard the delays are being driven. Pushing IN volume high overdrives the input stage and adds its own saturation before the delay processing begins.

**Main out** carries the full mixed output of delay and distortion. **Delay Only out** carries the delay signal before the distortion stage and after the IN volume and feedback path. Patching both outputs simultaneously into separate mixer channels gives independent control over the delay character and the distorted character.

## Why This Excels

Self-modulation is not an effect applied to the delay. It is a feedback path within the delay circuit itself, meaning the signal currently passing through the PT2399 changes how that same chip will process the next moment of audio. The behavior cannot be fully predicted from the input signal alone because the modulation is generated by the interaction between the input and the existing state of the delay. This makes Lyra-8 FX a feedback system rather than a signal processor with predictable transfer characteristics. What comes out depends on what went in combined with what is already there.

The PT2399 chip's lo-fi character is structural, not cosmetic. The chip operates at a sample rate that imposes audible quantization artifacts as part of its basic function, and Kreimer's circuit does not filter or compensate for these artifacts. Self-modulation lowers the effective sample rate further, dynamically, based on signal content. The degraded quality of the output at high modulation depths is the circuit behaving as designed: it is not simulating the sound of damaged equipment, it is the sound of this specific analog signal path under specific electrical conditions.

The Delay Only output is frequently overlooked and consistently underused. The distortion circuit in parallel with the delay path is useful precisely because it processes a signal that has already been through the PT2399 degradation. Patching Main out and Delay Only out to separate mixer channels, or routing Delay Only to additional downstream processing, gives access to the clean delay character independently of the distorted version. This also means the module can serve as two distinct signal sources in the same patch: lo-fi delay at one output, lo-fi delay plus full-range saturation at the other.

With no audio input and feedback above the self-oscillation threshold, Lyra-8 FX generates pitched drone tones from the recirculating delay feedback alone. The pitch of these tones is influenced by the Stage delay time settings and the feedback level. CV control of the Feedback input during no-input operation creates rising and falling drone events without any audio source. The module functions as a generator in this configuration, not only as a processor.

## Patches

### Patch 1: Granular Through Lo-Fi Delay

Arbhar granular output fed into Lyra-8 FX with one stage in self-modulation and one stage receiving Zadar CV. The two delay stages apply different characters to the same granular source simultaneously.

```
[Arbhar OUT L] ────────────────────────────▶ [Lyra-8 FX Audio In]

[Zadar CH1] ───────────────────────────────▶ [Lyra-8 FX Stage 2 Mod CV]
(slow envelope, 8-15 second duration)

                                              Stage 1: self-modulation
                                              Stage 1 time: 11 o'clock
                                              Stage 1 mod depth: 1-2 o'clock

                                              Stage 2: external CV
                                              Stage 2 time: 2 o'clock
                                              Stage 2 mod depth: 12 o'clock

                                              Feedback: 11 o'clock
                                              IN volume: 12 o'clock
                                              Delay mix: 2 o'clock
                                              Distortion drive: 9-10 o'clock

                         [Lyra-8 FX Main Out] ──▶ [MixUp CH1]
```

**Setup:** Patch Arbhar left output into Lyra-8 FX Audio In. Patch Zadar CH1 (set to a slow envelope shape, 8 to 15 seconds, no trigger needed for ambient use) into Stage 2 Mod CV. Set Stage 1 mod source switch to self-modulation. Set Stage 2 mod source switch to external CV.

**Controls:** Stage 1 self-modulates based on the Arbhar granular content passing through it, producing unstable warping that changes with the grain density and pitch. Stage 2 receives slow Zadar envelope CV, shifting its sample rate periodically as the envelope moves. The two delay stages apply different modulation characters to the same source simultaneously. Adjust Stage 1 mod depth to control how extreme the self-modulation becomes. Push Feedback toward 12-1 o'clock to sustain more of the granular content and build denser textures.

**Result:** Arbhar's granular output processed through two independently modulated lo-fi delay stages: one self-modulating from its own content, one shifting slowly under Zadar's control. The combination produces textures that neither module generates alone.

---

### Patch 2: Feedback Drone with CV Sweep

No-input feedback oscillation with Zadar controlling the Feedback CV input, creating rising and falling drone events timed by the envelope.

```
(no audio input)

[Zadar CH1] ───────────────────────────────▶ [Lyra-8 FX Feedback CV]
(medium duration envelope, looping or triggered)

                                              Both stages: self-modulation
                                              Stage 1 time: 12 o'clock
                                              Stage 2 time: 1 o'clock
                                              Both mod depths: 1 o'clock
                                              Feedback: 2 o'clock (base)
                                              IN volume: 11 o'clock
                                              Delay mix: 3 o'clock

                         [Lyra-8 FX Main Out] ──▶ [MixUp CH1]
                         [Lyra-8 FX Delay Only] ──▶ [MixUp CH2]
```

**Setup:** Patch nothing into Audio In. Set both stages to self-modulation with moderate mod depth. Set base Feedback to 2 o'clock. Patch Zadar CH1 into Feedback CV with a medium-duration envelope (4 to 8 seconds). Use MixUp CH1 for Main out and CH2 for Delay Only so both outputs are audible in the mix.

**Controls:** As the Zadar envelope rises it pushes Feedback above the self-oscillation threshold, causing the module to begin generating drone tones from the recirculating delay. As the envelope falls Feedback drops below the threshold and the drones decay. Stage 1 and 2 time settings determine the pitch content of the oscillation: adjust them to find pitches that complement the surrounding patch. Main out and Delay Only out carry different tonal characters, which MixUp allows you to balance against each other.

**Result:** A no-input generator producing periodic drone events timed by Zadar's envelope, with the pitch determined by the PT2399 delay time settings and the two outputs giving access to different saturation characters simultaneously.

---

### Patch 3: Lo-Fi Delay into Stereo Filter

Lyra-8 FX Main out into Moon Phase IN L, routing the processed delay output through stereo filter shaping before the mix.

```
[Cs-L OUT] ────────────────────────────────▶ [Lyra-8 FX Audio In]
[Hermod+] ── CV (1V/oct) ──────────────────▶ [Cs-L 1V/OCT]

                                              Stage 1: self-modulation
                                              Stage 2: external CV (no CV patched)
                                              Stage 1 time: 11 o'clock
                                              Stage 2 time: 1 o'clock
                                              Stage 1 mod depth: 1 o'clock
                                              Feedback: 10 o'clock
                                              Distortion drive: 10 o'clock

[Lyra-8 FX Main Out] ──────────────────────▶ [Moon Phase IN L]

                                              Moon Phase mode: LP+BP
                                              Moon Phase ST f: 11 o'clock
                                              Moon Phase SPAN: 1 o'clock
                                              Moon Phase ST IMAGER: 1-2 o'clock

                              [Moon Phase OUT L] ──▶ [MixUp CH3 L]
                              [Moon Phase OUT R] ──▶ [MixUp CH3 R]
```

**Setup:** Cs-L audio feeds Lyra-8 FX Audio In, with Hermod+ providing pitch CV to Cs-L. Lyra-8 FX Main out routes into Moon Phase IN L. Moon Phase spreads the processed signal into stereo at its outputs.

**Controls:** Lyra-8 FX handles the lo-fi delay degradation of the Cs-L voice; Moon Phase then applies stereo filter shaping to the degraded output. Adjust Moon Phase ST f to determine how much of the lo-fi delay content passes. Low ST f keeps the filtered texture dark; high ST f opens the full degraded character into the mix. Try Moon Phase LP+HP mode to route the low-frequency delay content left and high-frequency content right, creating a frequency-split version of the lo-fi processing. Adjust Lyra-8 FX Feedback and Distortion to change the character of the signal before it reaches Moon Phase.

**Result:** A signal chain where Cs-L is processed through lo-fi self-modulating delay and then filtered stereo by Moon Phase. The tonal content that Moon Phase shapes has already been through the PT2399 degradation, so the filter is working on transformed source material rather than the original oscillator sound.

---

### Patch 4: Percussive Source Destruction

Drum or percussive audio source patched into Lyra-8 FX with short delay times and high self-modulation depth on both stages, treating the module as a destructive processor for rhythmic material.

```
[Drum or percussive source] ───────────────▶ [Lyra-8 FX Audio In]

[Zadar CH1] ───────────────────────────────▶ [Lyra-8 FX Feedback CV]
(triggered by drum gate, fast attack, medium decay)

                                              Both stages: self-modulation
                                              Stage 1 time: 9-10 o'clock (short)
                                              Stage 2 time: 10-11 o'clock (short)
                                              Both mod depths: 2-3 o'clock (high)
                                              Feedback: 10 o'clock (base)
                                              IN volume: 1-2 o'clock
                                              Distortion drive: 12 o'clock
                                              Distortion mix: 1-2 o'clock

                         [Lyra-8 FX Main Out] ──▶ [MixUp CH1]
                         [Lyra-8 FX Delay Only] ──▶ [MixUp CH2]
```

**Setup:** Patch any drum channel, percussion source, or noise burst into Audio In. Patch Zadar CH1 (fast attack, medium decay, triggered by a drum gate) into Feedback CV. Set both stages to short delay times and high self-modulation depth.

**Controls:** Short delay times turn the PT2399 stages into comb filters and chorus-range processors rather than audible echoes. High self-modulation depth at these short times creates rapid glitching, sample rate reduction artifacts, and timbral degradation of the percussive transients. Zadar's triggered envelope pushes Feedback on each hit, briefly increasing the recirculation and building residual tones before decaying. Blend Main out (with distortion) and Delay Only (without) in MixUp to balance the saturated and unsaturated versions of the destroyed percussion.

**Result:** Percussive source material processed through short comb-range lo-fi delays with high self-modulation, creating glitched, degraded transients with feedback-driven tail events timed to each hit.

---

## Common Mistakes

### "It sounds broken and unstable, something must be wrong."

Instability is the intended behavior. PT2399 delay chips operating at reduced sample rates with self-modulation feeding back into the sample rate clock will produce pitch warping, glitching, and degradation under normal operating conditions. A Lyra-8 FX patch that sounds clean and transparent is not working at the settings this module is designed for.

**Fix:** Engage self-modulation on at least one stage, increase mod depth, and push Feedback above 11 o'clock. The character of the module becomes apparent at these settings. If you need transparent delay processing, this is not the right tool.

---

### "The delays do not sync to my sequencer tempo."

PT2399-based delays do not have a clock sync input and do not quantize delay time to a tempo grid. The delay time knobs set a delay length in milliseconds, not a rhythmic subdivision. No CV input changes this; the Mod CV inputs affect sample rate modulation, not tempo synchronization.

**Fix:** Set delay times by ear relative to your sequence tempo, or use the Feedback CV input to create rhythmic feedback swells that complement the tempo without locking to it. For strict tempo-synced delay, use a different module.

---

### "No-input mode produces nothing."

With no audio input and Feedback below the self-oscillation threshold, the module is silent. Self-oscillation in feedback delay circuits requires a recirculating signal above a certain gain level to sustain. Below that threshold there is nothing to recirculate.

**Fix:** Turn Feedback to 2-3 o'clock or higher, and confirm IN volume is at least at 11 o'clock. If silence persists, try tapping the Audio In jack briefly to introduce a transient that the feedback can then sustain. The exact self-oscillation threshold shifts with Stage time settings and mod depth.

---

### "I only use the Main out and ignore the Delay Only output."

Main out includes the parallel distortion stage, which adds saturation and harmonic content to the delay signal. Delay Only out carries the delay without distortion. Using only Main out means making one decision about the distortion character and committing to it for the whole patch.

**Fix:** Patch both outputs to separate mixer channels. Balancing Main out and Delay Only out independently gives access to both the saturated and unsaturated delay characters simultaneously, and allows the distortion contribution to be adjusted during the patch without changing the delay settings.

---

## Advanced Learning Path

1. Learn the module in external CV mode on both stages before engaging self-modulation. Set a slow LFO or Zadar envelope into one stage mod CV input and hear what sample rate modulation sounds like as a controlled, predictable parameter. This establishes a reference for normal modulated behavior before self-modulation makes the relationship between input and output non-deterministic.

2. Understand what self-modulation actually does before relying on it as a sound design tool. The delay output signal is routed back to modulate the PT2399 sample rate clock on the same stage. Sparse input with low self-modulation depth produces slow, subtle warping. Dense input with high depth produces rapid glitching because more signal energy is feeding back into the modulation path. The self-modulation character is a function of what is in the delay, not only of the knob settings.

3. Use the Delay Only output as a separate processing send rather than a monitoring option. Routing Delay Only into a separate effects chain and Main out into another creates two different versions of the processed signal available simultaneously. The Delay Only signal can go to Moon Phase, a reverb, or a second distortion with different character. Mixing these downstream paths gives more control over the final sound than working with Main out alone.

4. Explore no-input feedback oscillation at different Stage time combinations. Each combination of Stage 1 and Stage 2 delay times produces a different pitch content in the self-oscillating feedback. Moving one Stage knob while in oscillation changes the pitch in ways that are not musically quantized but are repeatable: once you find a useful drone pitch, note the Stage positions. Using Feedback CV from Zadar or an envelope to move in and out of the self-oscillation threshold turns this into a performable event rather than a static setting.

5. Use Lyra-8 FX early in the signal chain before other processing rather than as a final send. The degraded, lo-fi character it applies becomes the source material for everything downstream. Sending Lyra-8 FX output to Moon Phase means Moon Phase is filtering a signal that has already been through PT2399 degradation, self-modulation, and cross-feedback. The filter shapes a transformed source, not the original. Sending to Ghost after Lyra-8 FX adds reverb and delay on top of an already complex degraded signal. These chain orders produce fundamentally different results from using the module as a final effect.

6. Treat Feedback CV as a dynamic range control during performance. A sequence of triggered envelopes from Zadar or Punch V3 ENV output into Feedback CV creates rhythmic feedback swells timed to events elsewhere in the patch. Each event briefly pushes Feedback higher, increasing the recirculation and building tonal content, then releasing. This introduces rhythmic structure into what would otherwise be a static effects setting without requiring tempo synchronization.

## Pairs Well With

**Instruo Arbhar** is among the most productive sources for Lyra-8 FX. Arbhar's granular output already contains complex temporal relationships from its grain cloud processing; Lyra-8 FX then applies a second layer of time-domain transformation via the PT2399 stages. Self-modulation behavior changes with grain density, so Arbhar parameters that affect grain layer count and spray directly influence how the self-modulation responds. The combination produces textures where neither module's contribution is clearly separable from the other.

**Xaoc Zadar** provides the ideal CV source for Lyra-8 FX's modulation inputs because its envelope shapes produce non-repeating, contoured movements rather than the constant cycling of a standard LFO. Patching Zadar channels into the Feedback CV and one Stage mod CV input, with different shapes and durations on each, creates slowly shifting modulation relationships that never settle into a predictable pattern. In infinite-repeat mode Zadar becomes a slow irregular LFO; triggered mode creates modulation events timed to the patch's rhythmic structure.

**Patching Panda Moon Phase** downstream of Lyra-8 FX adds stereo filter shaping to an already-degraded signal. The different Moon Phase filter modes respond very differently to lo-fi PT2399 content versus clean oscillator content. LP+BP mode filters out extreme degradation artifacts in the highs while preserving the warmed lo-mid delay character. LP+HP mode splits the degraded frequency content between channels, creating stereo contrast from a mono Lyra-8 FX output. The filter is shaping something that has already been transformed, which produces results unavailable from either module alone.

**Intellijel MixUp** handles both Lyra-8 FX outputs in the same patch by accepting Main out and Delay Only out on separate channels. This allows the balance between the saturated and unsaturated delay versions to be adjusted during the performance, and allows either output to be muted independently. MixUp's architecture is well suited to patches where Lyra-8 FX is one of several processing chains feeding a common mix point.
