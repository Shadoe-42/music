---
title: Patching Panda Moon Phase
manufacturer: Patching Panda
primary_role: SHAPER
secondary_roles: []
form_factor: eurorack
functions: [filter, stereo_imaging]
behavior_tags: [stereo, nonlinear, performance-oriented, cv-friendly, dark]
use_cases: [stereo signal processing, mono to stereo conversion, timbral movement, texture creation]
hp: 14
historical_context: false
---

# Patching Panda Moon Phase

![Patching Panda Moon Phase](https://github.com/Shadoe-42/music/raw/main/modular/images/patching_panda/moon_phase/front_panel.jpg)
*Stereo multimode filter with 8 filter mode combinations, stereo imager, and independent frequency offset controls in 14HP*

## Quick Start: Get Sound in 5 Minutes

Moon Phase is a stereo multimode filter. It applies independent filter types to left and right channels simultaneously and then shapes the stereo relationship between them with the ST IMAGER and SPAN controls. Any mono signal patched into IN L appears at both outputs with stereo character added.

1. Patch any mono source into IN L
2. Connect OUT L and OUT R to a stereo mixer
3. Press MODE until you reach mode 6 (LP + LP), the closest to a traditional stereo lowpass
4. Set ST f to 12 o'clock
5. Leave SPAN and ST IMAGER at 12 o'clock to start
6. Sweep ST f slowly and listen to the basic lowpass response
7. Turn SPAN slightly clockwise and listen to the right channel open up relative to the left
8. Now turn ST IMAGER clockwise and listen to how the stereo width and resonance character change

That eight-step sequence covers the core interaction. Every patch extends from that foundation.

## Key Specs

| Spec | Value |
|------|-------|
| HP | 14 |
| Depth | ⚠️ unverified |
| +12V | 82mA |
| -12V | 63mA |
| 5V | 0mA |
| Filter modes | 8 |
| Self-oscillation | No |

## Essential Parameters

**Mode button** cycles through eight filter combination modes, one press per step. The left and right channels receive different filter algorithms in most modes, which creates genuine tonal contrast between sides rather than simple stereo width. The eight modes, with left channel listed first: LP+NOTCH, BP+HP, LP+BP, BP+BP, HP+HP, LP+LP, LP+HP, NOTCH+BP. Modes that apply the same type to both channels (LP+LP, BP+BP, HP+HP) produce symmetric stereo filtering. Modes that apply different types per channel produce spectral contrast, where each ear hears a different portion of the frequency content. Mode selection is the first decision in any patch. Changing mode during a patch is a valid performance technique.

**ST f** is the master cutoff control. It sets the center frequency for both filter channels simultaneously. This is the primary performance sweep control. The actual cutoff frequency on each channel depends on both ST f and SPAN together. ST f has a CV input. At audio rate, CV modulation of ST f creates complex harmonic FM-style interactions well beyond a standard sweep.

**SPAN** offsets the left and right filter cutoffs away from each other. At 12 o'clock both channels track ST f identically and the filtering is symmetric. Turning counterclockwise opens the left channel relative to the right; turning clockwise opens the right relative to the left. Small SPAN amounts add stereo movement without an obvious split. Large SPAN settings create audible frequency crossover effects where one side passes content the other removes. SPAN has a CV input and responds well to slow or irregular modulation.

**ST IMAGER** controls the stereo character of the combined output. It applies mid/side processing and phase shifting between the two channels. At 12 o'clock the stereo field is at its narrowest. Turning clockwise widens the image and shifts the phase relationship between channels. The critical interaction: ST IMAGER changes how Q resonance behaves. High Q combined with a wide ST IMAGER setting produces distortion artifacts that do not occur when ST IMAGER is centered. This is intentional design behavior, not a flaw. Modulating ST IMAGER at audio rate produces metallic, ring-modulator-adjacent effects. ST IMAGER has a CV input.

**Q** controls resonance. Moon Phase does not self-oscillate. Increasing Q emphasizes frequencies around the cutoff and adds character, but at high settings produces distortion rather than the pitched sine tone you might expect from other filters. The quality and intensity of that distortion depends on the current ST IMAGER position. Q has a CV input.

All four CV inputs accept audio rate signals, giving Moon Phase a range of extreme sound design possibilities beyond standard filter modulation.

## Why This Excels

Moon Phase is built stereo at the circuit level. The left and right filter paths are fully independent and can apply different algorithms simultaneously. This makes frequency splitting a core function rather than a creative workaround. In LP+HP mode with SPAN spread wide, the left channel performs lowpass filtering while the right channel performs highpass filtering, with ST f setting both cutoff points simultaneously. One source, sent through one module, arrives at the mixer with the low frequencies on one side and the high frequencies on the other. No routing gymnastics required.

The ST IMAGER is what separates Moon Phase from other stereo filters. Most stereo filter designs widen the image by adding a fixed delay or pitch offset to one channel. ST IMAGER actively controls the mid/side relationship between channels and modifies the behavior of resonance as it moves. The same Q setting produces different harmonic effects at different ST IMAGER positions. This means the module has effectively more than five independent parameters, because the interaction between Q and ST IMAGER is its own dimension of sound design.

The choice to eliminate self-oscillation is deliberate and worth understanding. At high Q, Moon Phase produces saturation and distortion rather than a pitched tone. This keeps the module in the domain of signal shaping rather than signal generation. The distortion adds character without requiring a separate saturation stage downstream, and it does not lock the filter into tracking pitch. Patches that depend on self-oscillation as a sound source need a different filter. Patches that need a stereo shaper with controllable harmonic distortion are exactly what Moon Phase is built for.

Eight modes accessed with a single button means mode changes happen at performance speed with no menu navigation. The transition is instant. Using mode switching as a structural element in a performance, moving from LP+LP for a section to LP+HP for the next, changes the character of everything running through the filter simultaneously. That kind of instant reconfiguration is difficult to achieve with most other filter designs.

## Patches

### Patch 1: First Stereo Spread

A clean introductory patch to hear how SPAN and ST IMAGER interact using a single mono source.

```
[Cs-L OUT] ──────────────────────────────▶ [Moon Phase IN L]

                                           Mode: LP+LP
                                           ST f: 10-12 o'clock
                                           SPAN: 1-3 o'clock
                                           ST IMAGER: 1-2 o'clock
                                           Q: 9 o'clock

                             [Moon Phase OUT L] ──▶ [MixUp CH3 L]
                             [Moon Phase OUT R] ──▶ [MixUp CH3 R]
```

**Setup:** Patch Cs-L audio output into Moon Phase IN L only. Connect both Moon Phase outputs to MixUp channel 3 as a stereo pair. Set mode to LP+LP.

**Controls:** Start with SPAN and ST IMAGER both at 12 o'clock. Sweep ST f and note the symmetric lowpass response. Now move SPAN clockwise to around 2 o'clock. The right channel opens up above the left. Now add ST IMAGER to 1 or 2 o'clock. The stereo field widens and the resonance character shifts. Try increasing Q to 10 or 11 o'clock and notice how the distortion behavior changes as you move ST IMAGER.

**Result:** A mono oscillator spread into a stereo image with frequency separation between channels. The patch sounds different each time ST IMAGER moves, which makes it immediately expressive with minimal patch complexity.

---

### Patch 2: Zadar Infinite-Loop Modulation

Zadar channels set to infinite repeat mode become irregular, shape-driven LFOs. This patch uses two of them to continuously modulate SPAN and ST IMAGER at different rates and shapes, creating slow unpredictable stereo movement.

```
[Arbhar OUT L] ───────────────────────────▶ [Moon Phase IN L]
[Arbhar OUT R] ───────────────────────────▶ [Moon Phase IN R]

[Zadar CH1] ──────────────────────────────▶ [Moon Phase SPAN CV]
(envelope shape, infinite repeat on)

[Zadar CH2] ──────────────────────────────▶ [Moon Phase ST IMAGER CV]
(different shape and time, infinite repeat on)

                                            Mode: LP+BP
                                            ST f: 11 o'clock
                                            Q: 9 o'clock
                                            SPAN: 12 o'clock (offset by Zadar)
                                            ST IMAGER: 12 o'clock (offset by Zadar)

                             [Moon Phase OUT L] ──▶ [MixUp CH3 L]
                             [Moon Phase OUT R] ──▶ [MixUp CH3 R]
```

**Setup:** Patch Arbhar stereo outputs into Moon Phase IN L and IN R. Set Zadar CH1 to any envelope shape with a long duration (8 to 30 seconds works well) and enable infinite repeat. Patch CH1 into SPAN CV. Set Zadar CH2 to a different shape and a different time, also infinite repeat, and patch into ST IMAGER CV. Set Moon Phase to LP+BP mode.

**Controls:** The Zadar channels cycle through their envelope shapes continuously, acting as complex LFOs with the shape character of an envelope. Because the two channels run at different times and with different shapes, they fall in and out of phase with each other, creating modulation relationships that do not repeat in any obvious cycle. Adjust the SPAN CV attenuverter (if present) or the starting SPAN knob position to control how wide the frequency split swings. Adjust ST f manually to move the overall filter region while the modulation handles the stereo character.

**Result:** Arbhar granular output filtered through continuously evolving stereo movement driven by Zadar's irregular envelope shapes. The stereo image shifts width and frequency balance without any LFO feeling repetitive or metronomic.

---

### Patch 3: Effects-Into-Filter

Ghost's processed stereo output fed into Moon Phase as the source material. The filter operates on an already-processed signal, shaping the frequency content of the effect rather than the dry source.

```
[Cs-L OUT] ────────────────────────────────▶ [Ghost IN]

                                             Ghost: FX chain order of choice
                                             Reverb active, Delay moderate

              [Ghost OUT L] ───────────────▶ [Moon Phase IN L]
              [Ghost OUT R] ───────────────▶ [Moon Phase IN R]

                                             Mode: LP+HP
                                             ST f: 10 o'clock
                                             SPAN: 2 o'clock
                                             ST IMAGER: 1-2 o'clock
                                             Q: 9-10 o'clock

                              [Moon Phase OUT L] ──▶ [MixUp CH3 L]
                              [Moon Phase OUT R] ──▶ [MixUp CH3 R]
```

**Setup:** Run Cs-L into Ghost. Set Ghost to a reverb-forward routing with moderate delay blend. Patch Ghost stereo outs into Moon Phase IN L and IN R. Set Moon Phase to LP+HP mode.

**Controls:** The filter now acts on Ghost's full wet signal. LP+HP mode with SPAN at 2 o'clock creates a complementary split: reverb tail low frequencies appear on the left, high frequency shimmer and transients pass through the right. Sweep ST f to move both cutoffs simultaneously, changing where the frequency boundary sits. Try switching to NOTCH+BP mode and listen to how the filter hollows out different parts of the reverb tail. Increase Q slightly to add saturation to the reverb content at the cutoff region rather than to the dry source.

**Result:** A filtered stereo reverb where the filter character interacts with the wet signal directly. Mode and SPAN changes create dramatic reconfigurations of which frequencies reach each output, giving the effect chain a second stage of expressive control.

---

### Patch 4: Rhythmic Filter Sweep

Zadar in normal envelope mode triggered by Hermod+ to create rhythmic filter opening events on ST f, with a second Zadar channel shaping SPAN for each event.

```
[Hermod+] ── Gate out ──────────────────────▶ [Zadar TRIG IN]
          └─ CV out (1V/oct) ───────────────▶ [Arbhar 1V/OCT]

[Arbhar OUT L] ─────────────────────────────▶ [Moon Phase IN L]

[Zadar CH1] ────────────────────────────────▶ [Moon Phase ST f CV]
(fast attack, slow decay, triggered)

[Zadar CH2] ────────────────────────────────▶ [Moon Phase SPAN CV]
(slower attack, different decay, triggered)

                                              Mode: BP+BP
                                              ST f: 9 o'clock (base)
                                              SPAN: 12 o'clock (base)
                                              Q: 10 o'clock

                               [Moon Phase OUT L] ──▶ [MixUp CH3 L]
                               [Moon Phase OUT R] ──▶ [MixUp CH3 R]
```

**Setup:** Hermod+ sends gate outputs to Zadar trigger input and CV to Arbhar pitch input. Zadar CH1 is set to a fast attack and moderate decay envelope shape, patched into ST f CV. Zadar CH2 is set to a slower attack and longer decay, patched into SPAN CV. Set Moon Phase to BP+BP mode with ST f at 9 o'clock as the closed base position.

**Controls:** Each Hermod+ gate event opens the filter via ST f (CH1 envelope) and simultaneously spreads the stereo frequency separation via SPAN (CH2 envelope). Because the attack times differ, the SPAN spread arrives slightly after the filter opens, creating a motion where the filter opens and then the stereo image widens across the decay. Try adjusting Zadar CH1 attack for snappier or softer filter onset. Try BP+HP mode for a version where the rhythmic events produce a brighter right channel than left.

**Result:** Rhythmically triggered filter sweeps that carry stereo separation as part of each event rather than as a static setting. The filter and the stereo image move together in response to the sequence.

---

## Common Mistakes

### "I patched it in and I only hear mono."

Moon Phase requires both outputs to be connected to hear stereo processing. Patching only OUT L into a mono mixer input will produce a mono signal. The stereo character, including all the SPAN and ST IMAGER behavior, only exists as a difference between the two outputs.

**Fix:** Connect OUT L and OUT R to a stereo mixer channel or a dedicated stereo input pair.

---

### "The resonance sounds distorted and broken at high settings."

Moon Phase does not self-oscillate. At high Q settings the resonance produces saturation and harmonic distortion rather than the clean pitched sine tone produced by filters that do self-oscillate. This is intentional behavior. The distortion quality is part of the module's character, not an indication of a patching problem.

**Fix:** Treat high Q as a saturation and character control rather than a self-oscillation threshold. Adjust ST IMAGER position to change the texture of the distortion. Lower Q to 9 or 10 o'clock for clean resonance emphasis without saturation.

---

### "SPAN does not seem to do anything interesting."

SPAN creates a frequency difference between the two channels, but that difference is only audible as a stereo effect when both outputs reach separate speakers or headphone channels. If only one output is monitored, SPAN changes the cutoff of that channel relative to the other, which can sound like subtle frequency shifts without an obvious stereo counterpart.

**Fix:** Confirm both outputs are connected and audible in separate channels of a stereo mix. Once both outputs are heard simultaneously, SPAN at even moderate positions (11 or 1 o'clock) produces a clear frequency separation between sides. Larger SPAN settings create more dramatic splits.

---

### "All eight modes sound the same to me."

With SPAN centered and ST IMAGER at 12 o'clock, modes that apply different filter types to each channel will sound more similar than they should, because the two channels are running at the same frequency and the stereo field is narrow. The differentiation between modes requires SPAN and ST IMAGER to be engaged.

**Fix:** Set SPAN to 2 or 3 o'clock and ST IMAGER to 1 or 2 o'clock before cycling through modes. With frequency separation and some stereo width active, each mode produces a distinctly different relationship between the two outputs.

---

## Advanced Learning Path

1. Start with one mode and learn its character fully before exploring the others. LP+LP at mode 6 is the most familiar starting point. Spend time sweeping ST f, pushing Q to different levels, and moving ST IMAGER through its range in that single mode before pressing MODE. Understanding how Q and ST IMAGER interact in one mode makes the behavior in every other mode immediately more legible.

2. Learn SPAN as a performance control rather than a set-and-forget knob. Move it slowly while a sound plays and listen to how the frequency balance shifts between channels. At small amounts it adds movement. At extreme amounts it creates dramatic splits. The optimal position depends on the mode, the source material, and how much frequency content lives in the region near the cutoff.

3. Explore the complementary modes as tools for signal splitting. LP+HP is the clearest example: one ear hears below the cutoff, the other hears above it. With SPAN spread and a different envelope or LFO modulating ST f, this mode creates evolving crossover effects where low and high content trade dominance between channels. NOTCH+BP creates a more subtle version of the same concept.

4. Use Zadar in infinite-repeat mode as a substitute for a dedicated LFO on any of the four CV inputs. Set each channel to a different envelope shape and a different total duration. The result is a continuously changing modulation source that never settles into a recognizable repeating cycle. Patching two Zadar channels into SPAN CV and ST IMAGER CV simultaneously, as in Patch 2 above, creates stereo movement that feels generative rather than mechanical.

5. Try audio rate modulation of ST f once you are comfortable with standard sweep ranges. Patching a second oscillator or Arbhar output into ST f CV at full audio frequency creates FM-style harmonic interactions, turning the filter into an audio rate modulator. The results depend heavily on the interval relationship between the source pitch and the modulating signal, so this technique rewards experimentation with precise pitch sources from Hermod+.

6. Use mode switching as a structural tool in longer patches rather than a setup decision. Pressing MODE during a performance changes the frequency character of everything downstream simultaneously. A patch running LP+LP for a low and wide texture becomes LP+HP instantly, splitting the frequency content into complementary sides. Practicing deliberate mode changes at musically relevant moments, phrase boundaries or rhythmic accents, makes Moon Phase an active performance instrument rather than a configured signal processor.

7. Process Ghost output into Moon Phase rather than always using Moon Phase first in the chain. The reverb and delay content from Ghost contains a specific frequency distribution. Running that processed signal through Moon Phase and setting high Q creates saturation of the reverb tail at the filter cutoff frequency, a different effect than saturating the dry source before reverb. Experiment with the signal order between Ghost and Moon Phase as a compositional variable.

## Pairs Well With

**Instruo Arbhar** is a natural source for Moon Phase because Arbhar produces stereo granular output with its own internal spatial character. Feeding Arbhar's L and R outputs into Moon Phase IN L and IN R applies filter shaping to an already-stereo signal, and the different filter modes treat the granular texture with frequency tools rather than spatial ones. Arbhar's Spray and Pitch controls combined with Moon Phase's SPAN and ST f create a patch with multiple independent axes of stereo movement.

**Xaoc Zadar** has two roles in a Moon Phase patch depending on its configuration. In standard envelope mode with a trigger source, Zadar shapes rhythmic filter events on ST f or Q. In infinite-repeat mode with no trigger, Zadar acts as a complex LFO whose shape character comes from the envelope curve rather than a sine or triangle waveform. The latter use is particularly effective on SPAN and ST IMAGER simultaneously, where two channels cycling at different rates and shapes create continuously shifting stereo behavior without any periodicity.

**Endorphin.es Ghost** works well both upstream and downstream of Moon Phase. Upstream, Ghost processes the source before it reaches the filter, and Moon Phase then shapes the frequency content of the effect chain. Downstream, Ghost applies reverb or delay to Moon Phase's already-filtered stereo output, extending the spatial width of the filtered result into a larger field. The routing order is a compositional decision with audible consequences, and both orderings are musically valid.

**Intellijel MixUp** is the natural endpoint for Moon Phase's stereo output. Moon Phase's OUT L and OUT R connect directly to a MixUp stereo channel, with the stereo imaging character preserved through MixUp's unity-gain stereo handling. MixUp's mute and level controls make it straightforward to blend Moon Phase's contribution against other sources in the mix.
