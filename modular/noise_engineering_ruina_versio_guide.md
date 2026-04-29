---
title: Noise Engineering Ruina Versio
manufacturer: Noise Engineering
primary_role: SHAPER
secondary_roles: []
form_factor: eurorack
functions: [distortion]
behavior_tags: [dirty, harsh, nonlinear, performance-oriented, harmonic]
use_cases: [waveshaping and distortion, aggressive sound design, timbral movement and shaping]
hp: 10
historical_context: false
---

# Noise Engineering Ruina Versio

![Noise Engineering Ruina Versio](https://github.com/Shadoe-42/music/raw/main/modular/images/noise_engineering/ruina_versio/front_panel.jpg)
*Stereo destruction engine with wavefolding, multiband saturation, phase shifting, rectification, sub-octave generation, and the legendary SMOOSH button in 10HP*

**The Stereo Destruction Engine**

---

## Quick Start: Get Your First Destroyed Sound in 5 Minutes

**What is Ruina Versio?** Think of it as the ultimate stereo distortion laboratory containing multiple types of destruction in one module. It packs wavefolding, multiband saturation, phase shifting, full-wave rectification, sub-octave generation, and a notch filter into 10HP. Plus there's the legendary SMOOSH button that adds 128dB of gain instantly. It's part of the Versio platform, meaning you can swap firmwares for completely different effects using USB.

### Your First Gentle Destruction
1. **Connect audio source** → **L INPUT** (or both L & R for stereo)
2. **Connect Ruina Versio L & R OUTPUTS** → **your mixer**
3. **Set all knobs to 12 o'clock** except DOOM and FOLD (fully CCW), BLEND (fully CW)
4. **Set both switches** to leftmost positions (UND, OFF)
5. **Start with FOLD knob** - turn up slowly to add harmonic distortion
6. **Try DRIVE knob** for multiband saturation warmth

**Congratulations!** You've just experienced the "gentlest" side of Ruina Versio - it only gets more destructive from here!

---

## Essential Parameters (The Destruction Arsenal)

### **1. FOLD - The Infinifolder**
- **What it does:** Classic Noise Engineering wavefolder from BIA and Loquelic Iteritas
- **Character:** Adds harmonics through wavefolding - starts gentle, gets aggressive
- **Fully CCW:** No folding (cleanest setting)
- **12 o'clock:** Moderate harmonic addition
- **Fully CW:** Extreme folding and harmonic generation
- **CV controllable:** Essential for dynamic timbral changes
- **Pro tip:** One of the most "musical" distortions on the module

### **2. DRIVE + CENTER - Multiband Saturator**
- **DRIVE:** Controls emphasis of different frequency bands (inspired by Seca Ruina)
- **CCW:** Low frequencies emphasized
- **CW:** High frequencies emphasized  
- **CENTER:** Controls width and frequency of the center band
- **Interaction:** These work together to create complex frequency-dependent saturation
- **Modulate CENTER:** Creates filter-like sweeping effects
- **Four bands:** Low, low-mid, high-mid, high frequency processing

### **3. DOOM - The Sub-Octave Destroyer**
- **What it does:** Detuned sub-octave generator that gets progressively unstable
- **Fully CCW:** No sub-octave generation
- **Low settings:** Clean sub-octave for bass enhancement
- **Higher settings:** Detuning and pitch instability increases
- **Extreme settings:** Buzzy overtones and harmonic chaos
- **Character:** "Scary" version of traditional sub-octave effects
- **Perfect for:** Bass enhancement that goes very wrong in the best way

### **4. 8VIZE - Full-Wave Rectifier**
- **What it does:** Full-wave rectification - unlike any other clipping you've heard
- **Character:** Creates erratic, harsh, glistening harmonic content
- **Unpredictable:** Sometimes behaves in unexpected ways
- **Harmonic generation:** Adds both musical and inharmonic content
- **Extreme settings:** Can create complete sonic chaos
- **Unique:** Different from traditional clipping or wavefolding

### **5. PHASE - Stereo Width Creator**
- **What it does:** Phase shifting between left and right channels
- **12 o'clock:** No phase shifting
- **Turn either direction:** Creates stereo width and movement
- **Modulate:** Creates swirling stereo effects
- **Mono compatibility:** Be careful with extreme settings if mono summing
- **Essential:** For creating wide, immersive soundscapes

### **6. BLEND - Wet/Dry Mix**
- **Fully CCW:** Dry signal only (bypass)
- **12 o'clock:** Equal mix of dry and processed
- **Fully CW:** Fully processed signal
- **Essential for:** Controlling intensity of destruction
- **Parallel processing:** Allows blending clean and destroyed signals

---

## Advanced Controls (The Routing & Filtering System)

### **7. UND/X/OVR - Signal Routing Switch**
- **UND (Under):** Mildest routing path through the distortion algorithms
- **X (Cross):** Medium intensity, different internal signal flow
- **OVR (Over):** Most extreme routing - includes two wavefolding stages
- **Changes everything:** Same knob settings sound different in each mode
- **Experiment:** Try same patch in all three modes for variety

### **8. OFF/ON/TRK - Notch Filter Switch**
- **OFF:** Notch filter disabled
- **ON:** Fixed 1kHz notch filter (classic reese/bass technique)
- **TRK:** Variable notch filter frequency controlled by CENTER knob
- **TRK mode interaction:** CENTER now controls both multiband center AND notch frequency
- **Sound design use:** Traditional technique for certain bass and lead sounds

### **9. SMOOSH - The Nuclear Option**
- **Manual button:** Press for instant 128dB gain boost
- **Gate input:** External triggering of SMOOSH effect
- **128dB gain:** Extreme input overdrive while maintaining output level
- **Use sparingly:** This is intentionally over-the-top
- **Performance tool:** Great for dramatic effect moments

---

## Why Ruina Versio Excels

Ruina Versio is not a gentle processor. The name -- Latin for "ruin" and "version" -- is accurate: its primary design intent is controlled signal destruction, and it does this through a combination of distortion, multimode filter, and a compression/saturation circuit called SMOOSH. The module's particular value is that its destructions are musical rather than random.

**Three processors in a deliberate sequence.** Ruina Versio chains distortion (DRIVE), a multimode filter (FILTER with five modes), and SMOOSH in a fixed signal path. Each processor modifies what the next one receives. Heavy distortion before a low-pass filter produces a different sound than heavy distortion after it; Ruina's fixed ordering is an editorial choice about what combinations work musically. The ordering was chosen through extensive use, not by convention.

**SMOOSH is a unique effect.** Most distortion modules offer some version of soft or hard clipping. SMOOSH is a specific dynamic processing circuit that compresses the signal during peaks and saturates the transients, producing a thick, dense quality that pushes audio forward in a mix. It is not simply "more distortion"; it changes the dynamic envelope of the signal. Triggering SMOOSH externally via the gate input synchronizes this dynamic effect to rhythmic events, which is the most musically coherent way to use it.

**The multimode filter shapes the distorted signal.** Five filter modes (low-pass, high-pass, band-pass, notch, and all-pass) after the distortion stage let you carve the harmonic content that distortion generates. Distortion adds upper harmonics; a low-pass filter after distortion rolls those harmonics back off selectively. This is how "warm distortion" is achieved: not by using less distortion, but by distorting heavily and filtering the results. The filter cutoff and resonance controls let you choose exactly how much of the distortion's harmonic content survives to the output.

**The Versio platform means alternative firmware is available.** Ruina Versio runs on Noise Engineering's Versio hardware platform, which is shared by other modules (Imitor Versio, Melotus Versio, Desmodus Versio, and others). Alternative firmware images can be loaded via audio update, changing Ruina Versio into a reverb, delay, or granular processor. The hardware itself is neutral; the character is determined by firmware. Users who want multiple effect types from one module slot can reflash as needed.

---

## Patches

### Patch 1: Subtle Harmonic Enhancement

This patch demonstrates Ruina Versio used conservatively to add harmonic complexity without obvious distortion, establishing the module's operating range from the low end.

```
[Audio source] ──L INPUT──▶ RUINA VERSIO
                             L OUT ──▶ [Mixer]
                             R OUT ──▶ [Mixer]
```

**Setup:** Connect a mono audio source (oscillator, pad, or instrument) to the L INPUT. Route both L and R outputs to mixer channels. Set routing mode to UND. Set FOLD to about 9 o'clock, SMOOSH fully counterclockwise, and BLEND at about 8 o'clock (mostly dry).

**Controls:** Start playback and gradually increase FOLD. At low settings the algorithm adds upper harmonics to the input without obvious clipping or waveshaping. Bring BLEND slightly clockwise to mix more of the processed signal against the dry. Try the different algorithm positions using the routing button and listen to how each one colors the source differently at this low-intensity setting. The goal of this patch is to hear the module's character before adding any driving force; most useful timbral work with Ruina Versio happens at settings below obvious destruction.

**Result:** Subtle harmonic enrichment that adds texture and presence to a sound without changing its fundamental character. This is the working range for using Ruina Versio as an insert processor on melodic material or pads where the source needs enhancement rather than transformation.

---

### Patch 2: Bass Destruction

This patch uses Ruina Versio to apply heavy algorithm processing to a bass sequence with LFO-modulated parameter variation for evolving results.

```
[Bass sequence] ──L INPUT──▶ RUINA VERSIO
[Slow LFO] ──CV──▶ DOOM CV input
                   L OUT ──▶ [Mixer or VCA]
```

**Setup:** Route a bass sequence to L INPUT. Connect a slow LFO (0.1 to 0.5 Hz) to the DOOM CV input. Select X routing mode. Set DOOM to about noon and increase SMOOSH to about 2 o'clock.

**Controls:** With the bass sequence running, adjust SMOOSH upward from noon. The sub-harmonic and octave-down content increases as SMOOSH rises, adding mass and low-end density. The slow LFO on DOOM CV shifts the algorithm parameter continuously, making the character of the destruction move over time rather than staying static. Adjust the LFO rate to control how quickly the bass evolves. Bring BLEND toward dry if the processed signal loses too much note definition; the unprocessed bass underneath helps maintain pitch intelligibility against the distorted layer.

**Result:** A bass sound that morphs continuously from clean to heavily processed and back. The LFO-driven parameter movement means the same note sequence sounds different on each pass, adding variation to repetitive bass lines without changing the sequence itself.

---

### Patch 3: Stereo Drum Bus Processing

This patch routes a stereo drum mix through Ruina Versio and uses a kick-triggered gate event to apply periodic heavy processing.

```
[Drum mix L] ──L INPUT──▶ RUINA VERSIO
[Drum mix R] ──R INPUT──▶ RUINA VERSIO
[Kick gate] ──SMOOSH GATE──▶ RUINA VERSIO
              L OUT ──▶ [Master mixer L]
              R OUT ──▶ [Master mixer R]
```

**Setup:** Connect the stereo drum bus to L and R inputs. Route the kick drum's gate signal to the SMOOSH gate input. Select OVR routing mode. Set SMOOSH to about 2 o'clock and BLEND at noon. Set PHASE to about 9 o'clock for some stereo width modification.

**Controls:** The drum mix runs through the algorithm continuously at the current settings, and the kick gate triggers additional SMOOSH intensity on each kick hit, creating a momentary blast of processing synchronized to the kick. Adjust the base SMOOSH level to set the continuous processing character; the gate input adds to that level on each kick. Try different routing modes to change which algorithms are active in the stereo field. Raise BLEND toward wet to increase the drum bus transformation; pull it back toward dry to keep more of the original dynamics.

**Result:** A drum bus that periodically surges in processing intensity in rhythm with the kick, creating a pumping, explosive quality on hits while sustaining a continuous timbral transformation between them. The stereo routing maintains the left/right relationship of the original mix while applying the processing uniformly across both channels.

---

### Patch 4: Evolving Pad Destruction

This patch applies slow CV modulation to multiple Ruina Versio parameters simultaneously for continuous timbral evolution on sustained pad sounds.

```
[Pad or chord source] ──L INPUT──▶ RUINA VERSIO
[LFO 1 slow] ──CV──▶ CENTER CV (0.05-0.1 Hz)
[LFO 2 very slow] ──CV──▶ 8VIZE CV (0.03-0.08 Hz)
[LFO 3 medium] ──CV──▶ PHASE CV (0.2-0.5 Hz)
               L OUT ──▶ [Mixer or reverb]
               R OUT ──▶ [Mixer or reverb]
```

**Setup:** Connect a sustained pad or chord source to L INPUT. Assign three LFOs at different slow rates to CENTER, 8VIZE, and PHASE CV inputs. Select UND mode. Set FOLD at noon and BLEND at about 2 o'clock.

**Controls:** With LFO rates set so no two are synchronized, the algorithm parameters drift at different speeds, creating a slowly changing timbral landscape that never repeats a specific combination. Bring BLEND toward wet to increase the processed character of the output. Switch routing modes between UND and X to hear how the same modulation produces different destruction types. The three LFOs running at prime-number-ratio rates (for example, 7, 11, and 13 seconds per cycle) produce the longest time before any combination repeats, maximizing the sense of continuous evolution.

**Result:** A pad sound that continuously morphs through different harmonic textures without any manual intervention. The multi-parameter modulation ensures no single parameter dominates the evolution; the result is a complex, slowly shifting sound that rewards extended listening and works well as a textural background layer.

---

## Common Mistakes

### "I pressed SMOOSH and now my signal is completely destroyed and unusable"

SMOOSH applies 128dB of gain to the input signal, which instantly saturates everything in the signal path. Without proper gain staging upstream and attenuation or limiting downstream, this level of gain will push your audio interface, mixer, or speakers into hard clipping. SMOOSH is not a casual effect: it is a surgical tool for dramatic moments and requires the rest of your signal chain to be prepared for the output level it produces.

Use SMOOSH with a VCA downstream set to attenuate the output, and keep BLEND at a moderate setting to control how much of the processed signal reaches your output. When triggering SMOOSH via the gate input, ensure the rest of your chain is set up before the gate fires. SMOOSH used intentionally and rhythmically, triggered by a kick drum or a measure-length gate, produces powerful results; SMOOSH used casually destroys your gain structure.

### "I know what settings I used but the patch sounds completely different now"

Changing the UND/X/OVR routing switch changes the entire internal signal path. UND, X, and OVR route the audio through different combinations of the processing stages: OVR adds a second wavefolding stage that UND does not include. The same FOLD, DRIVE, DOOM, and 8VIZE knob positions produce genuinely different sounds in each routing mode because the signals encounter different processing orders and combinations.

Document routing mode alongside all other settings. When recreating a patch, confirm the routing switch position before touching any knobs. When exploring, move the routing switch deliberately through each position and listen to what changes before adjusting knobs. Treating the routing modes as different sonic characters rather than an intensity scale reveals three distinct distortion voices in one module.

### "I am turning CENTER but it is affecting something I did not expect"

CENTER has two behaviors depending on the notch filter switch position. In OFF or ON modes, CENTER controls the frequency emphasis of the multiband saturator: rotating it shifts which frequency band receives the most saturation. In TRK mode, CENTER simultaneously controls both the multiband center frequency and the notch filter cutoff frequency. A single knob now governs two separate aspects of the signal: the saturation character changes and a notch appears and moves at the same time.

If CENTER is producing unexpected filtering behavior, check the notch filter switch. If you are in TRK mode and only want the multiband effect, switch to OFF or ON. If you are in TRK mode and want the combined behavior, use CENTER as a unified timbral control understanding that both effects track together.

### "All the distortion algorithms at once just sounds like noise"

FOLD, DRIVE, DOOM, and 8VIZE are four independent distortion algorithms that interact. Heavy settings on multiple algorithms simultaneously produces compound distortion where each stage's harmonics become the next stage's input. The result is often a dense wall of upper-frequency harmonic content that loses any musical relationship to the original signal. This is not a flaw: it is the extreme limit of the module. The musical content lives in partial settings and specific combinations.

Start with a single algorithm at a time. FOLD alone is the most harmonic and predictable. DOOM alone adds sub-octave content. DRIVE adds multiband saturation. 8VIZE is the most unpredictable. Combine them incrementally: FOLD plus DOOM produces a specific relationship between harmonics and sub that is well-documented. Use BLEND to control the ratio of processed to dry signal throughout.

### "My signal sounds thin after passing through Ruina Versio"

Ruina Versio at conservative settings can thin a signal rather than enrich it if BLEND is set too low. Distortion adds harmonics, but it also changes the dynamic structure of the signal. A clean, rich pad run through Ruina at extreme settings with very low BLEND may arrive at the output sounding thinner than the dry signal, because the small amount of heavily processed signal adds harsh upper harmonics without the fullness of the original.

Use BLEND as the primary intensity control. Start fully clockwise (fully wet) and reduce blend toward 12 o'clock to find the point where the processed character adds something without replacing the fundamental character of the source. For gentle harmonic enhancement, low FOLD settings with BLEND around 25% is a reliable starting point.

---

## Advanced Learning Path

1. Work through each algorithm configuration in isolation using the same audio source and identical settings. Route a simple oscillator or a recording of a single instrument into L INPUT, set all knobs to noon, and select each routing mode in turn. With UND, X, and OVR modes, note how the signal path and algorithm combination changes the fundamental character of the processing. Take notes or make recordings at each. This baseline survey is necessary before adding CV modulation, because modulation changes are only meaningful if you know what state you are modulating from and to.

2. Understand SMOOSH as a gain staging control rather than purely a destruction knob. At very low settings, SMOOSH functions as an input level control; as it increases, the input stage begins saturating before any algorithmic processing occurs, adding harmonic content from the saturation itself. At high settings the input is heavily compressed before reaching the algorithms. This means the optimal SMOOSH setting depends on the input signal level and the desired character: a hot synth output needs less SMOOSH to achieve the same saturation a quiet source would need at maximum. Always calibrate SMOOSH to the input level, not to a fixed setting.

3. Investigate the CENTER TRK dual function thoroughly. With no patch cable in the CENTER TRK input, the parameter responds to the CENTER TRK knob directly. With a patch cable inserted, the knob becomes an attenuator for the incoming CV signal and the center frequency tracks the CV rather than the knob position. This behavior is not obvious from the panel markings and is easy to miss. Knowing the dual function opens up CENTER TRK as a performance control when unpatched and as a precision CV destination when patched, which are meaningfully different use cases.

4. Explore the BLEND knob as a mix between dry and wet rather than as a severity control. At fully counterclockwise you hear only the unprocessed input. At fully clockwise you hear only the algorithm output. The midpoint gives equal parts of both. Many useful applications of Ruina Versio involve BLEND at 25 to 50 percent wet, where the processed layer adds character and texture to the dry signal without replacing its fundamental identity. This is especially true for melodic and harmonic sources where pitch intelligibility matters alongside the processing.

5. Route audio to both L INPUT and R INPUT simultaneously for true stereo processing. In UND mode, the algorithms run independently on left and right. In X mode, the two channels cross-feed. In OVR mode, the effect is applied to the sum. Each routing mode produces a different relationship between the left and right channels, which changes the stereo image of the output in addition to the timbral processing. Processing a stereo drum bus through X mode, for example, narrows the image differently than processing it through UND mode, even with identical knob positions.

6. Use PHASE CV to manage stereo width of the output independently of the processing intensity. At noon the phase relationship between L and R outputs is neutral. Modulating PHASE with a slow LFO produces a slow movement in the stereo image that is distinct from any timbral processing, and when combined with other CV modulation creates a three-dimensional evolution where both timbre and space are changing simultaneously.

---

## Pairs Well With

**Noise Engineering Loquelic Iteritas** provides the spectral complexity that makes Ruina Versio processing most audible. Loquelic Iteritas generates dense, harmonically rich waveforms with CPU and wavefold content that the Versio algorithms can act on across a wide frequency range. Running Loquelic Iteritas directly into Ruina Versio L INPUT with moderate FOLD and SMOOSH settings produces a continuously evolving sound that neither module could achieve alone. The NE-to-NE combination also makes physical sense in a rack: both modules are Noise Engineering hardware with design philosophies that assume the other exists.

**DivKid Ochd** is the primary modulation source for sustained pad and drone work through Ruina Versio. Routing multiple Ochd LFOs at different rates to CENTER, 8VIZE, and PHASE CV inputs creates a slowly evolving multi-parameter modulation state that never repeats on short timescales. Because Ochd LFOs are always running at fixed rates without attack or decay envelopes, the modulation is continuous and smooth, which matches the long decay character of pad material better than envelope-triggered modulation would.

**Make Noise Wogglebug** supplies the chaotic gate signal that makes SMOOSH gate triggering rhythmically unpredictable. With Wogglebug Burst driving the SMOOSH gate input, destruction events happen at Wogglebug-defined timing rather than on regular clock pulses. This is particularly effective on drum buses where periodic but non-metronomic processing adds energy without the predictability of a straight beat-triggered gate.

**Erica Synths Black Quad VCA2** provides gain staging before and after Ruina Versio in a clean, precise package. Because SMOOSH is sensitive to input level, having a VCA upstream allows deliberate input level adjustment as part of the patch design rather than relying on the source module's output level alone. A VCA downstream handles the wide range of output levels that aggressive settings can produce. The Quad VCA2 covers both needs in a single module with individual CV control per channel.

---

*Ruina Versio manual and firmware: [Noise Engineering](https://noiseengineering.us)*
