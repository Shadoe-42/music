---
title: Qu-Bit Prism
manufacturer: Qu-Bit Electronix
primary_role: PROCESSOR
secondary_roles: []
form_factor: eurorack
functions: [filter, delay, comb-filter, decimator, freeze]
behavior_tags: [textural, lo-fi, cv-friendly, stereo, subtle, metallic]
use_cases: [delay textures, comb filtering, bit crushing, spectral processing, freeze effects, beat repeat]
hp: 12
depth: 22
historical_context: false
---

# Qu-Bit Prism

![Qu-Bit Prism](https://github.com/Shadoe-42/music/raw/main/modular/images/qubit/prism/front_panel.jpg)

*Stereo multidimensional signal processor combining a delay line, comb filter, decimator, and state variable filter with pre/post routing and Freeze control in 12HP*

## Quick Start: Get Sound in 5 Minutes

Prism has no dry/wet control. Its outputs carry the fully processed signal. Blend the dry source separately in a downstream mixer.

1. Patch any audio source into In 1 (normalled internally to In 2 for stereo processing)
2. Patch Out 1 and Out 2 to a stereo mixer
3. Set Comb fully counter-clockwise (no comb effect)
4. Set Decimate fully counter-clockwise (no bit reduction)
5. Press Filter Type until the LED is blue (LPF active)
6. Set Cutoff to 2 o'clock, Resonance to 9 o'clock
7. Set Mode to green (filter post)
8. Send audio and confirm the lowpass-filtered signal is present at the outputs
9. Slowly raise Comb while listening for the comb filter character to appear
10. Adjust Time to change the pitch and density of the comb resonance

That is Prism at its most immediate: a filtered comb processor. Each of its three processing dimensions (delay/comb, decimation, and filter) can be used alone or in combination, but all three together at high amounts produces an undifferentiated wash. Use restraint.

## Key Specs

| Spec | Value |
|------|-------|
| HP | 12 |
| Depth | 22mm |
| +12V | 90mA |
| -12V | 10mA |
| 5V | 0mA |
| Delay Range | 0.5ms to 1.5 seconds |
| Filter Types | LPF, HPF, BPF |
| Stereo I/O | Yes |

## Essential Parameters

**Time** controls the size of the audio buffer in the delay line. This buffer is the shared foundation for the comb filter, the Freeze control, and the delay effect. At short Time settings the buffer produces comb filtering and slapback echo; at longer settings it produces distinct delay repeats up to 1.5 seconds. Time has a CV input. In Clocked Delay Times mode (activated via Mode+Filter Type, see Edit Functions), Time becomes a clock division and multiplication control that sets the delay length relative to an external clock rate rather than as an absolute buffer size.

**Comb** controls the amount of comb filtering and delay feedback applied to the signal. With Comb at minimum there is no delay or feedback; the dry signal passes through the buffer and the Time setting has no audible effect. As Comb increases, the delay feedback builds and the comb filter resonances become more pronounced. At high settings with short Time, Comb produces pitched, vocoder-adjacent timbres from the comb filter resonances. At high settings with longer Time, it produces regenerating delay with increasing feedback. Comb has a CV input. The effective character of Comb changes dramatically with Time position, and the two controls should be explored together rather than independently.

**Decimate** controls the audio fidelity of the buffer by reducing both the sample rate and bit depth of the output simultaneously. At minimum, the signal passes through at full fidelity. As Decimate increases, the output acquires digital grit and lo-fi character from the combined downsampling and bit reduction. At high settings, signal definition degrades significantly. Small amounts of Decimate add texture and presence to complex sources; large amounts destroy detail. Decimate has a CV input.

**Cutoff Frequency** sets the cutoff of the state variable filter. The attenuverter to the right of the Cutoff knob scales and inverts the Cutoff CV input: fully counter-clockwise inverts the CV at full scale, center disables the CV, and fully clockwise passes the CV at full scale. This same attenuverter also controls the audio input level when the Mode button is held (see Edit Functions). The Cutoff CV range is -8V to +8V, wider than most filter CV inputs on the module.

**Resonance** sets the resonance of the state variable filter. High Resonance narrows the filter response and adds emphasis at the cutoff frequency. Resonance has a CV input.

**Filter Type** button cycles through the four filter states: LPF (blue LED), HPF (green LED), BPF (red LED), and Disabled (LED off). The selected filter type is stored between power cycles, so the module returns to the same filter configuration on the next power-on. The Filter Type CV input can be used to sweep between filter types under CV control, or reconfigured as a clock input for Clocked Delay Times mode.

**Mode** button determines whether the state variable filter is placed at the beginning of the signal chain (blue LED, filter pre) or at the end (green LED, filter post). In filter-pre position, the input signal is filtered before entering the delay buffer; the delayed and comb-processed content reflects the filtered source. In filter-post position, the delay and comb processing act on the full-bandwidth input, and the filter shapes the combined output. The difference between these two positions is most audible when Comb is raised and the Cutoff is in the midrange. Mode state is stored between power cycles.

**Freeze** button and gate input lock the current contents of the delay buffer. While frozen, the signal repeats indefinitely from the locked buffer and the input signal is ignored. The frozen buffer length is determined by the Time setting at the moment of Freeze activation. Freeze has two behaviors configurable via Mode+Freeze: latching (LED white when active), where each press or gate toggles the freeze on and off; and momentary (LED blue when active), where Freeze is engaged only while the button is held or the gate input is high. In Clocked Delay Times mode, Freeze syncs to the external clock rate, producing rhythmically aligned beat repeat effects.

**Edit Functions** provide three additional behaviors accessed via button combinations. Latching/Momentary Freeze behavior is toggled by pressing Freeze while holding Mode. Clocked Delay Times is toggled by pressing Filter Type while holding Mode; this reconfigures the Filter Type CV input as a clock input and makes Time control clock divisions and multiplications rather than absolute buffer size. Input Level Adjustment is accessed by holding Mode while turning the Cutoff attenuverter; all LEDs illuminate blue and display amplitude as brightness, allowing adjustment from modular level down to line level for sources that would otherwise overdrive the input.

## Why This Excels

Prism combines three processing dimensions that each produce useful results independently and compound into more complex textures when used together at moderate amounts. Delay and comb filtering from Time and Comb, spectral degradation from Decimate, and state variable filter shaping from Cutoff and Filter Type are all present simultaneously, and the Mode switch determines the order in which the filter and delay chain interact. A short delay with light comb and a low-resonance lowpass filter in post position produces a shimmer effect that sounds like a single unified processor rather than three separate effects stacked. The module rewards treating its parameters as a single instrument rather than individual effect modules chained together.

The Mode switch is more consequential than a simple routing toggle. With the filter in pre position and Comb raised, the delay buffer records filtered content, and the regenerating repeats carry the filter character into each recirculation. Raising Resonance in this configuration causes the resonant peak to accumulate in the feedback, building toward a pitched sustain derived from the comb resonance and filter interaction. With the filter in post position, the delay buffer records the full-bandwidth source, and the filter shapes the combined direct and delayed signal at the output. The same Cutoff and Comb settings produce audibly different results in each Mode, and both are musically valid.

Prism responds best to sources with harmonic complexity or inharmonic content. Clean sine waves and simple waveforms give the comb filter less spectral material to emphasize, producing subtle effects. Complex oscillator outputs, plasma-based sources, and metallic percussion tones have the dense spectral content that makes comb resonances and filter interaction audible and distinct. The module is not a general-purpose filter or delay; it is a texture processor that draws out spectral details in sources that have them.

The Freeze control with Clocked Delay Times active produces rhythmically structured beat repeat effects that standard delay feedback cannot replicate. With Time set to a clock division and Freeze gated from an external source, Prism locks the delay buffer at a specific rhythmic position and holds it until the gate releases, creating repeating slices that are phase-locked to the patch clock. The slice length changes with the Time/division setting, and the frozen content retains whatever Comb, Decimate, and filter character was active at the moment of the freeze.

## Patches

### Patch 1: Metallic Shimmer Delay

Complex oscillator source into Prism with light comb and lowpass filtering, producing a shimmer delay texture routed to MixUp alongside the dry source.

```
[Cs-L Fold Out] ─────────────────────────▶ [Prism In 1]

                                            Filter Type: LPF (blue)
                                            Mode: post (green)
                                            Time: short (comb/slapback range)
                                            Comb: 9-10 o'clock (light feedback)
                                            Decimate: fully CCW (none)
                                            Cutoff: 1-2 o'clock
                                            Resonance: 9 o'clock

[Cs-L Sine Out] ─────────────────────────▶ [MixUp CH1]
[Prism Out 1] ───────────────────────────▶ [MixUp CH2 L]
[Prism Out 2] ───────────────────────────▶ [MixUp CH2 R]
```

**Setup:** Cs-L fold output provides harmonically complex content into Prism. The sine output from the same oscillator goes directly to MixUp CH1 as the dry reference, allowing Prism's wet output to be blended against a clean signal. Filter Type is LPF in post position: the delay and comb act on the full-spectrum fold output, and the lowpass filter shapes the combined result at the output.

**Controls:** Time in the short range produces comb resonances that track the harmonic content of the Cs-L output. Light Comb at 9 to 10 o'clock adds subtle feedback without building toward uncontrolled regeneration. Cutoff at 1 to 2 o'clock rolls off the upper frequencies of the combined processed signal, producing a warm shimmer layer that sits behind the clean Cs-L sine in MixUp. Raise Comb slightly to increase the shimmer density; bring it back when the feedback becomes too prominent. Keep Decimate at zero throughout this patch to preserve the filter clarity.

**Result:** A shimmer delay layer processed through light comb feedback and lowpass filtering, blended against the dry oscillator signal in MixUp. The wet layer adds depth and spectral movement to the dry source without obscuring it.

---

### Patch 2: Plasma Comb and Bit Crush

Plasma Voice metallic source into Prism using comb filtering and moderate Decimate for lo-fi grit, routed to Cockpit 2.

```
[Plasma Voice Out] ──────────────────────▶ [Prism In 1]

                                            Filter Type: Disabled (LED off)
                                            Time: short (comb range)
                                            Comb: 10-11 o'clock (moderate feedback)
                                            Decimate: 10 o'clock (moderate grit)

[Prism Out 1] ───────────────────────────▶ [Cockpit 2 CH L]
[Prism Out 2] ───────────────────────────▶ [Cockpit 2 CH R]
```

**Setup:** Plasma Voice provides inharmonic, metallic content with a dense spectral character. Filter Type is disabled; this patch uses only the comb and decimation processing. Time is set short enough for comb resonances to appear in the metallic texture.

**Controls:** Comb at 10 to 11 o'clock applies moderate feedback to the short delay buffer, producing comb resonances that interact with the inharmonic content of the Plasma Voice. The comb effect on a metallic, plasma-based source sounds different from comb filtering on a tonal oscillator: the inharmonic spectrum produces irregular, shifting resonances rather than clean pitched artifacts. Decimate at 10 o'clock adds digital grit to the already textured plasma source without flattening its spectral detail. The combination of comb-filtered plasma content with moderate decimation produces a degraded metallic texture that retains the plasma character while adding electronic roughness. Bring Comb back if the feedback accumulates too much; bring Decimate back if the signal loses definition.

**Result:** Plasma Voice source processed through comb filtering and moderate bit crushing, producing a lo-fi metallic texture with irregular comb resonances. Routed to Cockpit 2 for mixing.

---

### Patch 3: Clocked Beat Repeat

Hermod+ clock syncing Prism's delay to patch tempo, with Freeze gate creating rhythmically locked buffer repeats.

```
[Cs-L Sine Out] ─────────────────────────▶ [Prism In 1]
[Hermod+ Clock Out] ─────────────────────▶ [Prism Filter Type CV]

                    [Enable Clocked Delay Times: hold Mode, press Filter Type]
                    [Enable Latching Freeze: hold Mode, press Freeze (LED white)]

[Hermod+ Gate Out] ──────────────────────▶ [Prism Freeze Gate]

                                            Filter Type: LPF (blue, pre-clock config)
                                            Mode: post (green)
                                            Time: 12 o'clock (clock division position)
                                            Comb: 10 o'clock
                                            Cutoff: 2 o'clock
                                            Resonance: 9 o'clock

[Prism Out 1] ───────────────────────────▶ [MixUp CH3 L]
[Prism Out 2] ───────────────────────────▶ [MixUp CH3 R]
```

**Setup:** Enable Clocked Delay Times by holding Mode and pressing Filter Type. This reconfigures the Filter Type CV input as a clock input. Patch Hermod+ clock output into the Filter Type CV jack. Hermod+ gate output into the Freeze gate input enables rhythmic buffer locking. Enable Latching Freeze mode by holding Mode and pressing Freeze until the LED turns white.

**Controls:** With Clocked Delay Times active, Time controls clock divisions and multiplications rather than absolute buffer length. The central Prism LEDs blink white each time the division changes as Time is adjusted. Set Time to a division that produces a rhythmically useful repeat length relative to the patch clock. When a Hermod+ gate arrives at the Freeze input, Prism locks the current buffer contents and holds them for the gate duration in latching mode. Each Freeze activation captures a different moment of the Cs-L output and repeats it until the next Freeze gate releases it. Adjust Time between Freeze events to change the locked slice length.

**Result:** A rhythmically synchronized beat repeat effect with delay length locked to the patch clock and Freeze events gated from Hermod+, producing structured slice repeats that stay in time with the rest of the patch.

---

### Patch 4: Modulated Delay Texture

Zadar modulating Time and Decimate at independent rates, with Cs-L as source and filter in pre position for a continuously shifting texture.

```
[Cs-L Fold Out] ─────────────────────────▶ [Prism In 1]

[Zadar CH1] ─────────────────────────────▶ [Prism Time CV]
(slow envelope, 8-15 seconds, infinite repeat)

[Zadar CH2] ─────────────────────────────▶ [Prism Decimate CV]
(different shape, 12-20 seconds, infinite repeat)

                                            Filter Type: BPF (red)
                                            Mode: pre (blue)
                                            Time: 10 o'clock (short-medium base)
                                            Comb: 9-10 o'clock
                                            Cutoff: 12 o'clock
                                            Resonance: 10 o'clock

[Prism Out 1] ───────────────────────────▶ [MixUp CH2 L]
[Prism Out 2] ───────────────────────────▶ [MixUp CH2 R]
```

**Setup:** Cs-L fold output enters Prism with the filter in pre position (Mode blue). Bandpass filter shapes the signal before it enters the delay buffer. Zadar CH1 in infinite-repeat mode slowly modulates Time CV, shifting the delay buffer size and comb resonance pitch over 8 to 15 seconds. Zadar CH2 in infinite-repeat mode modulates Decimate CV at a different rate, cycling through fidelity levels over 12 to 20 seconds.

**Controls:** With the BPF filter in pre position, only the bandpass-filtered content of the Cs-L fold output enters the delay buffer. The delay and comb processing act on this already-filtered material, and the buffer repeats carry the bandpass character. Zadar slowly moves Time, which shifts the pitch of the comb resonances as the buffer size changes. Zadar independently cycles Decimate, periodically adding and removing digital grit from the output. The two modulation rates are asynchronous, so the combination of comb pitch change and fidelity change produces a texture that evolves on two timescales without a repeating pattern. Keep both Zadar depths modest enough that neither parameter reaches its extreme; Decimate fully raised and Time fully extended simultaneously produces the wash-and-smear result to avoid.

**Result:** A bandpass-filtered complex oscillator source processed through slowly shifting comb resonances and intermittent decimation, producing a continuously evolving textural layer with two independent modulation timescales.

---

## Common Mistakes

### "Every source I run through Prism sounds like the same indistinct wash."

Comb, Time, and Decimate are all raised simultaneously to high values. Each parameter at high amounts removes signal definition: high Comb builds regenerating feedback, long Time produces long delay accumulation, and high Decimate destroys spectral detail. Together they compound into an undifferentiated texture regardless of the source.

**Fix:** Use each parameter at modest amounts. Set Comb to 9 to 10 o'clock rather than fully clockwise. Set Decimate to 9 to 10 o'clock rather than fully clockwise. Set Time to the range appropriate for the effect (short for comb, medium for slapback), not to its maximum. Prism produces its most useful results when each parameter contributes a small amount of character to a source that retains its identity through the processing.

---

### "The filter is not doing anything."

Filter Type is set to Disabled (LED off). In the disabled state, the state variable filter is not active and Cutoff and Resonance have no effect on the signal.

**Fix:** Press the Filter Type button to cycle to LPF (blue), HPF (green), or BPF (red). The filter becomes active immediately. If the filter effect seems subtle, confirm the Cutoff is not set to maximum (fully clockwise, all frequencies pass through a lowpass at full cutoff) or minimum (no frequencies pass through a highpass at zero cutoff).

---

### "Mode does not seem to change the sound."

The audible difference between filter-pre and filter-post is minimal when Comb is at zero or when Cutoff is at an extreme position. Without comb feedback recirculating the filtered content back into the buffer, and without a midrange Cutoff where the filter is actively shaping the spectrum, the two Mode positions produce nearly identical output.

**Fix:** Set Comb to 10 o'clock, Cutoff to 12 o'clock, and Resonance to 11 o'clock. Toggle Mode between blue and green and listen to the difference. In this configuration, filter-pre sends the shaped signal into the comb feedback loop, accumulating the filter character with each pass. Filter-post applies the filter to the combined comb output at the end of the chain. The difference is audible and significant with these settings.

---

### "Freeze is not staying engaged after I release the button."

Prism is in momentary Freeze mode (LED turns blue when active). In momentary mode, Freeze is only active while the button is held or the gate input is above 1V. Releasing the button ends the Freeze.

**Fix:** Hold the Mode button and press Freeze to toggle to latching mode. The LED will be white when Freeze is active in latching mode. In latching mode, each button press or gate rising edge toggles the Freeze state, so Freeze stays engaged after releasing the button.

---

## Advanced Learning Path

1. Learn Time and Comb together as a single system before adding filter or decimation. Set Decimate to zero and Filter Type to Disabled. Explore the full Time range with Comb at 10 o'clock and listen to how buffer size changes comb resonance pitch and delay character. This relationship between Time and Comb is the core of what Prism does.

2. Explore all three Filter Types in both Mode positions with Comb at a moderate setting. That is six distinct signal chain configurations from the same source. LPF-pre, LPF-post, HPF-pre, HPF-post, BPF-pre, and BPF-post each produce a different relationship between the filtered content and the comb feedback. Work through them deliberately with the same patch rather than discovering them by accident.

3. Learn Decimate at low amounts before raising it. Set Decimate to 9 o'clock and listen for the subtle fidelity change before increasing. The useful range for most textures is 9 to 11 o'clock; above that, signal definition degrades faster than it adds character.

4. Activate Clocked Delay Times and use an external clock before exploring the Freeze control in depth. With clock-synced Time, the Freeze buffer locks to a rhythmically meaningful duration rather than an arbitrary buffer position. Freeze in a clocked context produces beat repeat effects with consistent musical relationship to the patch tempo.

5. Explore the Cutoff CV attenuverter as an inversion control, not just an attenuation control. With the attenuverter fully counter-clockwise, the Cutoff CV is inverted: a rising CV closes the filter rather than opening it. This produces a filter that tracks inverse of the modulation source, which is a different musical behavior from the standard tracking direction.

6. Patch CV into Time while Comb is raised and listen for pitch effects. Moving the delay buffer size with feedback active causes the comb resonance pitch to shift with the Time CV. A slow envelope on Time CV produces a filter sweep effect from the shifting comb resonances that is distinct from the state variable filter behavior. At short Time settings, this produces pitched artifacts; at longer settings, it produces modulated echo character.

7. Experiment with Mode before and after raising Resonance significantly. High Resonance in filter-pre mode sends the resonant peak into the comb feedback loop, where it recirculates and builds with each pass. High Resonance in filter-post mode applies the resonant emphasis at the output without it entering the feedback path. The filter-pre configuration can sustain pitched resonances from the feedback accumulation; the filter-post configuration produces sharper, more controlled resonant emphasis.

## Pairs Well With

**Instruo Cs-L** provides the complex oscillator content that Prism processes most effectively. Cs-L's wavefolded output has dense harmonic content that gives Prism's comb filter resonances specific pitches and spectral material to interact with. The fold output into Prism with light Comb and LPF post produces a shimmer layer that retains the fold's harmonic character in a washed, delayed form. Running the Cs-L sine output directly to a mixer while its fold output goes through Prism gives a clean reference signal alongside the processed texture, allowing precise blending between dry and wet.

**Gamechanger Audio Plasma Voice** feeds Prism with inharmonic and metallic spectral content that produces different comb filter behavior than tonal oscillator sources. The irregular, plasma-generated spectrum interacts with Prism's comb resonances to produce shifting, unpitched artifacts rather than clean harmonic series. Moderate Comb and Decimate on Plasma Voice content creates a lo-fi metallic texture that degrades the plasma character in a musically controlled direction. Plasma Voice into Prism is primarily a timbre transformation chain rather than a spatial or delay effect.

**Squarp Instruments Hermod+** provides two distinct functions with Prism. In Clocked Delay Times mode, Hermod+ clock output into the Filter Type CV jack syncs Prism's delay buffer to the patch tempo, making Time a rhythmic division control rather than an absolute size control. Hermod+ gate outputs into the Freeze gate input then produce rhythmically aligned beat repeat effects with the locked buffer length tracking the clock division. Running both simultaneously gives full rhythmic control over the freeze and delay behavior from a single sequencer.

**Xaoc Devices Zadar** provides independent, asynchronous modulation for Prism's CV inputs. Time CV and Decimate CV modulated by separate Zadar channels at different rates produce two simultaneous layers of textural evolution: comb resonance pitch shifting on one timescale and fidelity change on another. A third Zadar channel into Cutoff CV adds filter movement on a third timescale. With all three Zadar channels running at different rates into Prism, the processed output changes continuously without a repeating modulation pattern.
