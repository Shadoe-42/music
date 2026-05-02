---
title: Endorphin.es Ghost
manufacturer: Endorphin.es
primary_role: SHAPER
secondary_roles: [ROUTER]
form_factor: eurorack
functions: [reverb, delay, filter, distortion, compressor]
behavior_tags: [evolving, nonlinear, performative, dark]
use_cases: [stereo signal processing, atmospheric texture, rhythmic processing, Karplus-Strong synthesis]
hp: 16
historical_context: true
---

# Endorphin.es Ghost
**Multi-Dimensional Effects Chain | 16HP | Firmware V4**

![Ghost Module](https://github.com/Shadoe-42/music/raw/main/modular/images/endorphines/ghost/front_panel.jpg)

## Historical Context

Recording engineers working in the analog studio developed strong intuitions about signal chain order. Running audio through reverb before compression produced a different character than compressing first and then adding reverb. Distortion before equalization had a different result than equalization before distortion. These relationships were not simply aesthetic preferences; they followed from how each processor transformed the signal that entered it and what the next stage in the chain consequently received. The conventions around gain staging, tonal shaping, dynamics control, and spatial processing reflected decades of practical knowledge about what order worked for what purposes.

Digital audio workstations changed the underlying assumption. Plugin chains can be reordered without rewiring, and the question of whether reverb precedes or follows distortion became a design choice rather than a constraint. Producers who worked across hardware and software began to understand routing order as a creative variable rather than a fixed architectural fact.

Endorphin.es, a Barcelona-based company, designed the Ghost module in collaboration with producer Andrew Huang. The central design decision was to build routing reorderability into the hardware itself: three processing blocks, three available signal flow orders, one button to cycle between them without repatching. Ghost treats routing order as a performance parameter in the same way that filter cutoff or reverb tail time are performance parameters, something to change during a session rather than a commitment made before one begins.

---

## Quick Start

```
[Any Source] Audio Out ──▶ [Ghost] In
                           [Ghost] Out ──▶ [Mixer or Interface]
```

1. Patch any audio source into Ghost's input and route Ghost's output to a mixer
2. Set all knobs to noon
3. Set the Routing button to LED off (FX then DIST then VCF order)
4. Slowly advance the Distortion knob clockwise and listen to the character shift
5. Sweep the Frequency knob counterclockwise toward 9 o'clock to hear low-pass filtering
6. Bring Reverb Dry/Wet clockwise past noon to add space
7. Press the Routing button once to shift signal flow order and compare the result with the same knob settings

---

## Key Specs

| Parameter | Value |
|-----------|-------|
| Width | 16HP |
| Depth | 25mm |
| Power | 135mA +12V / 35mA -12V / 0mA 5V |
| Processing | ARM Cortex-M7 / 96kHz / 32-bit |
| Firmware | V4 |
| **Role** | **SHAPER (ROUTER)** |

---

## Essential Parameters

The Routing button is the defining control on Ghost. One press cycles through three signal flow orders: FX then DIST then VCF (LED off), DIST then VCF then FX (LED half-lit), and VCF then FX then DIST (LED fully lit). Each order sends audio through the same three processing blocks in a different sequence, producing fundamentally different character from identical knob positions. The routing order should be the first decision in any patch, because it determines what each downstream block receives as input and therefore how it behaves.

The FX block contains delay and reverb. Delay Time sets repeat interval from audio-rate frequencies at minimum (used for Karplus-Strong synthesis) up to 2.5 seconds at maximum. Delay Repeats controls feedback amount. Delay Dry/Wet sets the balance of delayed and dry signal. Reverb Tail controls decay length and Reverb Dry/Wet sets the spatial mix. Pre-delay, accessible by holding the Routing button while turning the Tail knob, separates the direct signal from the reverb onset and preserves transient definition when reverb levels are high. An external clock input and clock divider allow delay time to sync to an incoming gate signal, and the delay accepts 1V/octave control of delay time for pitched Karplus-Strong synthesis.

The DIST block contains the Distortion knob, which moves from clean at minimum to heavy saturation at maximum, and a Gain control accessible via the Routing hold. A bit-crusher depth parameter, also shift-accessible, reduces the sample word length independently of the analog saturation stage. The DIST block operates on whatever the routing order places before it: in DIST-first routing that is the clean input signal; in the other two routings it receives material already shaped by one or two prior stages.

The VCF block is a zero-delay feedback state-variable filter with a bipolar Frequency control. Counterclockwise removes high frequencies (low-pass behavior); clockwise removes low frequencies (high-pass behavior); noon is flat. The Resonance knob adds emphasis at the cutoff frequency and at extreme settings produces self-oscillation at the filter frequency. A button toggles the filter between its default bipolar LP/HP mode, band-pass mode, and comb resonator mode accessible via shift. The VCF CV input has its own attenuverter so modulation depth and polarity can be set without additional modules.

The dynamics section sits at the end of the signal chain regardless of routing order. The Compressor knob controls compression amount. The Sidechain Trigger input accepts gate or trigger signals; when a trigger arrives the output ducks and then recovers over a time set by the Sidechain knob. Sidechain depth (the amount of attenuation per trigger) is set via the Routing hold. The PRE-VCA CV input controls input level before any processing occurs, which affects the entire downstream chain simultaneously. The POST-VCA CV input and Volume/Drive knob control the output level; the drive stage activates past approximately 1 o'clock on the Volume knob. Global Dry/Wet, accessible via the Routing hold on the Volume knob, sets the balance between the fully processed and unprocessed signal.

---

## Why Ghost Excels

The routing architecture is the central argument for Ghost. Most effects processors apply their blocks in a fixed sequence, so what the distortion or filter receives as input is determined by the module's design rather than by the user's intent at a given moment. Ghost removes that constraint by making routing order a panel control. The character difference between running reverb into distortion versus running distortion into reverb is not subtle; it is the difference between atmospheric saturation and aggressive presence. Pressing the Routing button mid-session while audio plays demonstrates the principle more directly than any explanation.

The three routing orders cover distinct sonic territories rather than being arbitrary permutations of the same tools. FX then DIST then VCF places spatial complexity before saturation; the distortion colors already-diffused material rather than clean input, producing atmospheric heaviness. DIST then VCF then FX places definition before space; distortion establishes character and the filter sculpts it before reverb adds spatial dimension, which keeps transient clarity through the processing. VCF then FX then DIST sends distortion to the end of the chain where it colors a signal that has already been frequency-shaped and spatially processed; the manual describes this as producing the heaviest tones because saturation is applied to complex material rather than to a simple input. Each order has a natural application domain and the single-button switch makes comparison fast enough to function as a creative tool.

The Karplus-Strong synthesis capability represents a distinct mode of use. At minimum delay time the delay operates at audio frequencies, and at high feedback the delay feedback loop sustains a resonant tone at the frequency corresponding to the delay time. The 1V/octave delay time input allows this tone to be played melodically from a CV sequence. The result is a plucked-string physical model voice generated entirely from Ghost's delay feedback without any external oscillator input. Ghost in this configuration is not processing audio; it is generating it, which expands its role from processor to voice.

The Sidechain Trigger input makes Ghost responsive to external events rather than only to manual control or gradual modulation. A gate signal from a sequencer or drum trigger causes the output level to duck and recover, with depth and release time both adjustable. Using a rhythmic gate source against sustained or evolving audio creates dynamic contrast that manual adjustments cannot replicate: the effect reacts to tempo rather than being tempo-agnostic. Pairing the sidechain with routing choices and VCF CV modulation gives Ghost three independent real-time control axes, which is the combination that makes it function as a performance instrument rather than a static effects unit.

---

## Patches

### Atmospheric Texture Layer

Route a complex oscillator through Ghost in FX-first order to build a sustained atmospheric pad texture from a single audio source.

```
[Cs-L] Audio Out ──▶ [Ghost] In
[Zadar] Ch1 Out  ──▶ [Ghost] VCF CV
                     [Ghost] Out ──▶ [MixUp] Ch1
```

**Setup:** Set the Routing button to LED off (FX then DIST then VCF). Set Reverb Dry/Wet to 2 o'clock and Tail to 2 o'clock for a long, wet reverb. Set Delay Dry/Wet to noon and Repeats to 1 o'clock for dense feedback. Set Distortion to 11 o'clock for mild saturation. Set Frequency to noon and Resonance to 11 o'clock. Program Zadar channel 1 with a very slow falling envelope cycling at 20 to 40 second intervals.

**Controls:** The Zadar envelope slowly closes the VCF over its cycle, then resets and opens again, producing long arcs of tonal movement underneath the reverb processing. Adjust the Frequency noon position to shift the center of the sweep. Advance Distortion to 1 o'clock and listen to how the saturation colors the reverb tail rather than the dry signal; this is the defining character of FX-first routing. Bring Reverb Dry/Wet toward 3 o'clock to push further into wet reverb saturation.

**Result:** A sustained, slowly evolving atmospheric texture that changes character over long time periods. The reverb and delay establish spatial complexity and the distortion saturates that complexity rather than the source directly, producing diffuse heaviness that shifts in tonal character as the Zadar envelope moves the VCF.

---

### Sidechain Rhythmic Processor

Use Ghost's Sidechain Trigger input to create rhythmically pulsing effects processing that ducks and resurfaces with a gate sequence.

```
[Cs-L] Audio Out     ──▶ [Ghost] In
[Hermod+] Gate Out   ──▶ [Ghost] Sidechain Trig In
[Hermod+] CV Out     ──▶ [Ghost] VCF CV
                         [Ghost] Out ──▶ [MixUp] Ch2
```

**Setup:** Set the Routing button to LED half-lit (DIST then VCF then FX). Set Distortion to 2 o'clock and Frequency to 10 o'clock for a warm, saturated character. Set Reverb Tail to noon and Dry/Wet to 1 o'clock so the reverb is audible in the spaces between trigger events. Program Hermod+ to send a rhythmic gate pattern and a complementary CV sequence. Hold the Routing button and turn the Sidechain knob clockwise to set sidechain depth to approximately 60 to 70 percent.

**Controls:** As each gate fires, Ghost's output ducks briefly and resurfaces over the release time set by the Sidechain knob turned without holding the Routing button. Adjust the release time to control whether the recovery feels snappy or gradual. The Hermod+ CV sequence modulates the VCF, so the filter position shifts between trigger events. The DIST-first routing keeps saturation character present and defined even during ducking; the reverb in third position adds space without softening the distortion character.

**Result:** Processed audio that pulses rhythmically with the gate pattern, the reverb tail filling the space between duck events. The VCF modulation from Hermod+ adds a second layer of independent change layered over the sidechain timing.

---

### Distorted Lead with Routing Contrast

Process a melodic line through DIST-first routing to demonstrate how distortion before filtering and reverb produces defined, present tones rather than atmospheric texture.

```
[Cs-L] Audio Out  ──▶ [Ghost] In
[Hermod+] CV Out  ──▶ [Ghost] VCF CV
                      [Ghost] Out ──▶ [MixUp] Ch3
```

**Setup:** Set the Routing button to LED half-lit (DIST then VCF then FX). Set Distortion to 1 o'clock. Set Frequency to 10 o'clock for a warm low-pass character and Resonance to 1 o'clock for a presence peak. Set Reverb Dry/Wet to 10 o'clock (minimal) and Delay Dry/Wet to noon. Program Hermod+ to send a melodic CV sequence to the VCF CV input. Set the VCF CV attenuverter to 2 o'clock.

**Controls:** The Hermod+ CV sequence opens and closes the filter as the melody plays, so each note has a different tonal character depending on the CV value at that step. Press the Routing button once to switch to FX-first order (LED off) while audio is playing and compare the result: the same settings now produce diffuse atmospheric character instead of defined presence. Press again to return to DIST-first. This comparison demonstrates the routing architecture's effect directly without changing any other setting. Advance Resonance toward 2 o'clock to hear the filter emphasis compounding the distorted signal.

**Result:** A melodic voice with defined, present character that cuts through a mix. The distortion establishes the saturation, the filter sculpts it, and the minimal reverb adds just enough spatial dimension without softening the distorted foundation.

---

### Karplus-Strong Voice

Use Ghost's audio-rate delay feedback to generate a plucked-string physical model voice without any external oscillator, triggered by gate events from a pitch sequence.

```
[Hermod+] Gate Out ──▶ [Ghost] Sidechain Trig In
[Hermod+] CV Out   ──▶ [Ghost] VCF CV (1V/oct delay time)
                       [Ghost] Out ──▶ [MixUp] Ch4
```

**Setup:** Set the Routing button to LED half-lit (DIST then VCF then FX). Patch no audio source into Ghost's input. Turn Delay Time fully counterclockwise to minimum. Advance Delay Repeats to 3 o'clock (high feedback, approaching self-oscillation). Set Delay Dry/Wet to 3 o'clock (fully wet). Set Reverb Dry/Wet to 9 o'clock (minimal, to preserve pluck transient definition). Set Distortion to 11 o'clock. Set the VCF CV attenuverter to noon so the Hermod+ CV controls delay time at 1V/octave scale. Program Hermod+ with a melodic CV sequence and a gate pattern to trigger pluck events.

**Controls:** Each gate trigger creates a brief excitation that the high-feedback delay sustains as a resonant tone at the pitch corresponding to the current CV value. The Delay Time minimum position places the delay in audio frequency range so the feedback loop produces pitched resonance rather than discrete echoes. Adjust Delay Repeats: below approximately 2 o'clock the resonance decays quickly (short sustain); above 3 o'clock it sustains longer and approaches infinite feedback. The Distortion knob at low settings adds warmth to the resonance character. Bring Reverb Dry/Wet up to noon to add space around each plucked event.

**Result:** A sequenced melodic line of plucked-string tones generated entirely from Ghost's delay feedback with no oscillator in the signal path. The technique represents Ghost operating as a sound generator rather than a signal processor, which is a fundamentally different mode than any of the other patches.

---

## Common Mistakes

### "All three routing orders sound the same to me"

The routing order difference is most audible when at least one processing block is pushed to a meaningful depth. With all three blocks near neutral, distortion at noon, reverb and delay at low wet values, and filter at noon, the routing difference is subtle. The blocks need to be active before the sequence in which they process the signal becomes audible. **Fix:** Set Distortion to 2 o'clock, Reverb Dry/Wet to 2 o'clock, and Frequency to 10 o'clock before switching routing orders and comparing.

---

### "I am using Ghost as a reverb module and nothing else"

The FX block is the most obvious entry point but using it in isolation leaves the DIST and VCF blocks at neutral, which means Ghost produces results similar to any other reverb module in the system. The character that distinguishes Ghost comes from the interaction between all three blocks and from the routing order that determines what each block receives as input. Using reverb alone also leaves the Routing button without a meaningful effect, since switching order is only audible when multiple blocks are active. **Fix:** Set Distortion to 1 o'clock and Frequency to 10 o'clock before adding reverb, then compare the three routing orders with all three blocks contributing.

---

### "I have not patched CV into anything and the patch feels static"

Ghost has three CV-accessible parameters: VCF CV with attenuverter, PRE-VCA CV for input level, and POST-VCA CV for output level, plus the Sidechain Trigger input for dynamics. Treating Ghost as a fixed-knob processor uses only a fraction of its range. Patching a single slow modulation source to VCF CV and setting the attenuverter to noon is the minimum step that gives Ghost character that changes over time. The PRE-VCA CV input is particularly useful because it modulates the entire processing chain simultaneously rather than a single block. **Fix:** Patch at least one CV source to VCF CV and one gate source to the Sidechain Trigger input before treating a Ghost patch as complete.

---

### "The Karplus-Strong patch sounds like a wet delay, not a pitched tone"

The delay time is not short enough. Karplus-Strong synthesis requires the delay feedback loop to operate at audio frequencies, which means the delay time must be in the sub-millisecond range: Delay Time at or very near minimum. At longer delay times the feedback produces discrete echoes rather than a resonant tone. The distinction is clear once heard: an echo repeats; a resonance sustains as a continuous pitched sound. **Fix:** Turn Delay Time fully counterclockwise, advance Repeats above 2 o'clock, set Delay Dry/Wet to fully wet, and confirm a 1V/octave CV source is connected to the VCF CV input before triggering.

---

## Advanced Learning Path

1. Spend dedicated time on each routing order in isolation before working with all three. Begin with FX then DIST then VCF (LED off): set meaningful reverb and delay levels, then adjust the Distortion knob and listen to how the saturation behaves on already-spatial material. Do the same with DIST-first and VCF-first separately. The routing architecture becomes intuitive after experiencing each order as its own processing philosophy rather than as a configuration option.

2. Learn the Delay Tone control (hold Routing, turn Repeats knob) before building dense delay patches. Tone adjusts the brightness of the delay repeats, which determines what character the next processing block receives. Dull repeats feeding into distortion produce different saturation than bright repeats feeding into the same Distortion knob setting. This shift control has more impact on overall character than it appears at first.

3. Use PRE-VCA CV before adding multiple simultaneous modulation sources. PRE-VCA controls how much signal enters the entire processing chain, which affects saturation density and reverb loading simultaneously. An envelope or slow LFO at PRE-VCA creates a consistent dynamic shape across the whole chain rather than modulating individual blocks independently. Understanding this global control first makes the effects of per-block modulation easier to interpret and balance.

4. Practice the Sidechain Trigger as a timing and dynamics tool before using it for texture. Patch a steady clock pulse into the Sidechain Trig input and set depth to 50 percent. Adjust the release time until the recovery aligns with the clock rate. Once that timing relationship is clear, move to an irregular gate source such as a probabilistic trigger output. The sidechain is most effective when the relationship between trigger timing and release time is intentional rather than coincidental.

5. Explore the comb filter mode (BPF/Comb button held with Routing) as a resonator rather than as a filter. In comb mode, Resonance adds harmonic emphasis at a series of related frequencies above the fundamental rather than at a single cutoff peak. At high resonance in comb mode with VCF in first position (VCF-first routing), the resonance character compounds through the delay and distortion stages. This combination produces dense, harmonically complex textures not available from the standard LP/HP or band-pass modes.

6. Build a patch in which Ghost receives audio from Arbhar as an input source. Arbhar's granular output provides temporally scattered, grain-level material: when Ghost processes it through FX-first routing, the reverb and delay add spatial dimension to material already transformed from its source, and the distortion saturates layers that contain granular variation. The combination produces textures at a level of complexity that neither module reaches alone.

---

## Pairs Well With

**Instruo Cs-L** provides the richest source material for Ghost to process. The Cs-L is a complex dual oscillator with wavefolding, cross-modulation, and sub-oscillator outputs; its harmonic complexity interacts differently with each Ghost routing order and with the DIST block at different saturation levels. Patching the Cs-L main output into Ghost and comparing how the three routing orders transform the same complex waveform demonstrates the routing architecture's range more clearly than a simple sine or sawtooth would.

**Squarp Hermod+** handles both the pitch sequencing and gate generation that Ghost's CV inputs and Sidechain Trigger need for full performance use. The Hermod+ provides simultaneous CV and gate outputs from the same sequence, so the melodic line and the sidechain timing derive from the same musical source rather than from independent generators. The Hermod+ clock output also serves as a sync source for the delay clock input, which makes delay timing tempo-related rather than arbitrary.

**Instruo Arbhar** upstream of Ghost creates a layered processing path where granular transformation precedes multi-FX processing. Arbhar scatters, stretches, and repositions audio across its six-layer granular engine; Ghost then applies routing-order-dependent processing to the granulated result. The Arbhar output feeding Ghost's FX-first routing produces textures at a level of complexity that neither module reaches on its own: granular time-domain manipulation followed by reverb-then-saturation spatial and tonal shaping.

**Intellijel MixUp** is the natural downstream endpoint for Ghost's stereo output. Ghost is a stereo processor throughout its signal chain; MixUp provides the multi-channel mixing needed to blend Ghost's output with dry or parallel-processed signal paths. The per-channel mute controls on MixUp allow Ghost's output to be dropped in and out during a session without manual level adjustment, which is useful for comparing processed and unprocessed versions of the same source.
