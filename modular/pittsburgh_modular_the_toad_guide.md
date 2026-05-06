---
title: The Toad
manufacturer: Pittsburgh Modular
primary_role: SHAPER
secondary_roles: []
historical_context: true
form_factor: eurorack
functions: [fx-modulation, lfo]
behavior_tags: [warm, evolving, harmonic, dark]
use_cases: [analog phase sweeping, spatial processing, self-oscillation as pitched voice, dual-output stereo processing]
hp: 8
depth: 35mm
memory: none
transport: none
screen: false
hybrid: false
cv: basic
---

# The Toad

**12-stage all-analog phase shifter with dual tapped outputs, bi-polar feedback, and attenuverting CV: deep, gummy, and self-oscillation capable**

![Pittsburgh Modular The Toad](https://github.com/Shadoe-42/music/raw/main/modular/images/pittsburgh_modular/the_toad/front_panel.jpg)

## Historical Context

The phase shifter occupies an unusual position in the history of audio effects. Unlike distortion, which produces new harmonic content by clipping or saturating a signal, or reverb, which simulates acoustic space through reflections, a phase shifter does not change what frequencies are present in a signal or add any new ones. It changes when they arrive. The circuit at the core of every analog phase shifter is the all-pass filter: a network that passes all frequencies at equal amplitude but introduces a phase shift that varies with frequency. The phase-shifted signal, mixed back with the original, produces cancellation at frequencies where the two are out of phase and reinforcement where they are in phase. The result is a notch filter, a comb of peaks and troughs in the frequency spectrum, whose character is determined by the degree of phase shift and the number of filter stages chained together.

The first widely heard application of phase shifting in popular music was not a phaser in the technical sense. The Uni-Vibe, designed by Fumio Miida and manufactured by Shin-ei in Japan in 1968, was built to simulate the rotating speaker effect of a Leslie cabinet. It used photocells rather than all-pass filter stages to create its phase relationships and was technically closer to a four-stage chorus-vibrato effect. Jimi Hendrix used it extensively in performance, most notably at Woodstock in 1969 on "Machine Gun," and the association between that sound and Hendrix made phase shifting a recognized sonic category before the circuit that would define it commercially had been designed.

The MXR Phase 90, released in 1974, established the all-pass filter chain as the standard phase shifter architecture. Four stages in series, each contributing 90 degrees of phase shift, producing two notch/peak pairs across the frequency spectrum. The Phase 90 became a fixture in rock guitar, famously used by Eddie Van Halen on the debut Van Halen album in 1978 in a context where its sweeping character defined a generation of players' relationship to the effect. MXR followed it with the Phase 100 in 1975, extending the chain to ten stages and five notch/peak pairs, producing a denser, more complex sweep with correspondingly more prominent peak and notch density.

The Pittsburgh Modular The Toad is a direct descendant of Pittsburgh's earlier Phase Shifter module, extending the all-pass chain to twelve stages. Six notch/peak pairs. The difference in density between a four-stage and a twelve-stage phaser is not incremental; it is qualitative. A four-stage phaser produces a relatively open, transparent sweep with two notches moving through the spectrum. A twelve-stage phaser at high feedback produces the characteristic Pittsburgh description: gummy. The spectrum is more thoroughly shaped, the peaks are more prominent, and the interaction between the feedback and the notch structure creates a resonant quality that approaches filter-like behavior without any actual frequency-selective attenuation. In modular context, the addition of attenuverting CV input, bi-polar feedback, and two simultaneously accessible tapped outputs turns the phase shifter from a sweep effect into a precision spectral sculpting tool with self-oscillation capability in either feedback direction.

---

## Quick Start

The Toad is a 12-stage analog phase shifter with an internal triangle LFO for modulation, bi-polar feedback, and two simultaneous outputs tapped at stages 7 and 12. Start here for the classic sweeping effect before exploring feedback and dual-output use.

1. Patch audio into the IN jack. Patch the Stage 12 output into a mixer or the next module in the chain. Set the Stage 12 Mix Switch to up (positive dry blend).
2. Set Input Level to 12 o'clock, Feedback to 12 o'clock (center, no feedback), Manual Shift to 12 o'clock, Mod Depth to full left (off).
3. Set Modulator to 9 o'clock (slow LFO rate). Now increase Mod Depth slowly clockwise.
4. You should hear the classic phaser sweep beginning as the internal LFO modulates the center frequency of all twelve stages simultaneously.
5. Advance Mod Depth further and hear the sweep deepen. Adjust Modulator rate to find a speed that works with the source material.
6. Now slowly bring the Feedback attenuverter clockwise from center. The resonance of the phaser increases and the peaks in the spectrum become more prominent.
7. At full clockwise Feedback, the Toad will self-oscillate. Manual Shift sets the pitch of self-oscillation at that point.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 8 HP |
| Depth | 35 mm |
| Power | 110 mA +12V / 100 mA -12V / 0 mA +5V |

The power draw requires attention before installing. At 110mA on +12V and 100mA on -12V, The Toad draws more current than many oscillators and filters, in 8HP of panel space. Both rails carry significant load; verify available headroom on each bus independently. The 35mm depth is also notable and may conflict with components on adjacent module PCBs in shallower cases.

---

## How Phase Shifting Works

Understanding what The Toad does to a signal makes every control decision clearer. The explanation below covers the physics once and applies it throughout the rest of the guide.

**The all-pass filter.** An all-pass filter (APF) passes every frequency at equal amplitude; nothing is cut or boosted. What changes is the phase relationship between frequencies: some frequencies are delayed relative to others. The amount of delay depends on the filter's center frequency setting. One all-pass filter stage produces 90 degrees of phase shift at its center frequency.

**Chaining stages.** Connecting twelve all-pass filter stages in series multiplies the total phase shift. At the center frequency of the chain, the signal accumulates phase shift across all twelve stages. The combined shift creates a richer, more complex phase relationship between different frequencies than any single stage could produce.

**The notch filter effect.** On its own, a phase-shifted signal sounds identical to the dry signal; amplitude is unchanged. The effect only appears when the phase-shifted signal is mixed with the dry, unshifted signal. At frequencies where the two signals are 180 degrees out of phase, they cancel, producing a notch. At frequencies where they reinforce, a peak appears. Every two stages of phase shift (180 degrees) creates one notch/peak pair. The Toad's twelve stages produce six notch/peak pairs simultaneously.

**Why stage count matters.** A four-stage phaser (Phase 90) produces two notches. Ten stages produce five notches. The Toad's twelve stages produce six notches. More notches mean the sweep is denser, the cancellation pattern is more complex, and the tonal character of the effect is more pronounced. At low modulation depth and center settings, a twelve-stage phaser has a measurably richer tonal character than a four-stage phaser applied to the same source at the same settings.

**Modulation.** The character of a static notch filter is interesting but limited. The signature sweeping sound emerges when the center frequency of all twelve stages is modulated simultaneously, moving the notch/peak comb up and down the frequency spectrum in real time. The Toad's internal triangle LFO does this at a rate set by the Modulator knob and a depth set by the Mod Depth knob. External CV into the Shift CV jack replaces or supplements the LFO modulation with any voltage source.

---

## Essential Parameters

**Input Level.** The audio input attenuator controls how much of the incoming signal enters the phase shifter circuit. At 12 o'clock, the input is at unity gain. Reducing Input Level below unity lowers the signal level entering the all-pass chain; increasing it above unity drives the input harder, which at extreme settings begins to add subtle saturation character from the analog circuit. For most applications, 12 o'clock is the correct starting position.

**Feedback.** An attenuverter controlling how much of the stage 12 output is fed back into the input of the all-pass chain. At 12 o'clock (center), feedback is zero and the Toad is in its cleanest, most open state. Turning clockwise adds positive feedback: the resonant character of the notch peaks increases, the effect becomes more pronounced, and at full clockwise the Toad self-oscillates, sustaining a pitched tone at the frequency determined by the Manual Shift setting and the current modulation position. Turning counterclockwise from center adds inverted (negative) feedback: the same resonant buildup occurs but with the polarity of the feedback signal reversed, producing a different tonal character at high settings and self-oscillation at full counterclockwise. Negative feedback self-oscillation has a slightly different pitch and harmonic character than positive feedback self-oscillation; both are valid and both are extreme. The range between center and the self-oscillation threshold in either direction is where most musical phaser tones live.

**Manual Shift.** An attenuverter that sets the center frequency of the entire all-pass chain. At 12 o'clock, the center frequency is positioned so the internal LFO and any external CV have equal positive and negative sweep range available; the modulation can move the notch comb equally far above and below the center position. Turning counterclockwise moves the center frequency down; turning clockwise moves it up. The position of Manual Shift relative to the modulation source determines which part of the frequency spectrum the notch filter sweeps through. A low Manual Shift setting with deep modulation sweeps through the low-mid range; a high setting with deep modulation sweeps through the upper midrange and beyond.

**Modulator.** Controls the rate of the internal triangle LFO. The triangle LFO produces a smooth, symmetrical modulation waveform that moves the notch comb up and down at the set rate. Counterclockwise is slowest; clockwise increases rate toward audio-rate territory at extreme settings. At very slow rates the sweep is a gradual, almost imperceptible drift. At medium rates it produces the classic rhythmic phaser sweep. At fast rates approaching audio rate, the LFO begins to contribute to the harmonic character of the effect rather than producing a perceptible sweep.

**Mod Depth.** Sets the amount of LFO modulation applied to the phase shifter center frequency. Full left is off; the LFO is running but has no effect on the circuit. Increasing Mod Depth clockwise widens the sweep. At maximum Mod Depth, the notch comb sweeps through the widest possible range of the frequency spectrum with each LFO cycle. Mod Depth and Modulator interact directly: a fast LFO with low depth produces subtle shimmer; a slow LFO with high depth produces a wide, dramatic sweep; a fast LFO with high depth produces dense spectral movement where individual sweep cycles are too close together to distinguish.

**Shift CV Attenuverter.** A bi-polar CV input that supplements or replaces the internal LFO for phase shifter center frequency modulation. Turning the attenuverter counterclockwise from center inverts the incoming CV; turning clockwise adds it in positive polarity. The Shift CV input and the internal LFO both contribute to the center frequency simultaneously; patching an external CV does not disable the LFO. To use only external CV, set Mod Depth to full left (LFO off) and use Shift CV exclusively. The Shift CV input accepts any CV source: envelopes, LFOs, sequencer outputs, random voltages, audio-rate signals for extreme frequency modulation effects.

---

## The Two Outputs

The Toad's twelve-stage signal path has two points where the processed signal is tapped and sent to an output jack: after stage 7 and after stage 12. Both outputs are available simultaneously. Each output has its own mix switch that determines the polarity of the dry signal blended with the phased signal at that tap point.

**Stage 7 output.** Taps the signal after six notch/peak pairs, half the full phaser depth. The stage 7 output has a lighter, more open phaser character than stage 12. The notch structure is present but less dense. In a dual-output patch, stage 7 provides the lighter of the two voices.

**Stage 12 output.** The full twelve-stage output: maximum notch density, maximum resonance from the feedback circuit, the complete gummy character Pittsburgh describes. Stage 12 is where the Toad is most fully itself.

**Mix Switch polarity.** Each output has a three-position switch: up for positive dry blend, down for negative (inverted) dry blend. In the up position, the dry signal and the phased signal are mixed with the same polarity: cancellation occurs where they are out of phase, reinforcement where they are in phase, producing the standard notch filter character. In the down position, the dry signal's polarity is inverted before mixing. This swaps the cancellation and reinforcement points: frequencies that were notched become peaks and vice versa. The tonal character with negative dry mixing has a brighter, slightly more aggressive quality compared to positive mixing on the same phased signal. The negative mix position is worth trying on any patch; positive is the default working position for most applications.

**Using both outputs simultaneously.** Routing stage 7 and stage 12 to separate destinations is where The Toad opens up spatially. Both outputs carry the same twelve-stage phaser chain, but stage 7 is tapped partway through; it hears a lighter version of what stage 12 hears. With stage 7 into one channel of a stereo panner or matrix mixer and stage 12 into another, the two phased signals diverge in their spectral character. Because their notch positions are related but not identical (stage 12 continues processing where stage 7 stopped), they interact with downstream stereo effects differently. Into a stereo reverb or a panning matrix like the After Later Audio Mingles, the two outputs create a spatial image that moves differently from what either output alone would produce: the depth of the twelve-stage version and the openness of the seven-stage version in the same stereo field.

Setting the two mix switches to opposite polarities (stage 7 to positive, stage 12 to negative) creates maximum divergence between the two outputs: not only are they tapped at different points in the chain, they have inverted dry blends, placing their cancellation/reinforcement patterns at opposite frequency positions. Used as a stereo pair this creates a wide, enveloping spectral image that moves in opposing directions.

---

## Feedback and Self-Oscillation

The Feedback attenuverter sets the amount of stage 12's output that is fed back into the beginning of the all-pass chain. Feedback in a phase shifter behaves analogously to resonance in a filter: as feedback increases, the peaks in the notch filter response become sharper and more prominent, and the effect becomes increasingly resonant and colored.

At moderate positive feedback settings (Feedback clockwise from center, not yet at maximum), the Toad takes on a singing, resonant character where the peaks ring audibly against the source material. This is the most musically useful feedback zone for most applications: present enough to add character, controlled enough to remain tonal rather than destabilizing.

At maximum positive feedback (full clockwise), the Toad self-oscillates: it sustains a pitched tone independently of the input signal. The pitch of that tone is determined by the Manual Shift position and the current modulation state. With Mod Depth at zero and Manual Shift at a fixed position, self-oscillation produces a stable pitched tone. With Mod Depth increased, that tone sweeps in pitch at the LFO rate, producing a voltage-controlled sinewave-adjacent oscillator. External CV into Shift CV at this state gives direct pitch control over the self-oscillating tone.

Negative feedback (Feedback counterclockwise from center) produces inverted resonance behavior: the feedback signal re-enters the chain with opposite polarity. The effect is different in character from positive feedback resonance; the notch structure responds differently to the inverted signal, and the tonal quality of moderate negative feedback has a slightly different color than equivalent positive feedback. Full counterclockwise also reaches self-oscillation, with a pitch and harmonic character distinguishable from positive feedback self-oscillation at the same Manual Shift position. Both are worth exploring as distinct tools rather than treating negative feedback as a lesser version of positive feedback.

A practical note: the transition from resonant but controlled to self-oscillation is fast near the extremes of the Feedback knob. In a live patch, be aware of the threshold; it is easy to pass through controlled resonance into self-oscillation unintentionally if sweeping the Feedback knob at speed.

---

## Signal Flow

### Basic: single output phasing

```
[Source] ──[A]──▶ [IN]
                    │
              [12-stage APF chain]
                    │
              [Stage 7 tap] ──[A]──▶ [Stage 7 Out] (available but not patched)
                    │
              [Stage 12 tap] ──[A]──▶ [Stage 12 Out] ──▶ [Mixer/next module]
                    │
              [Feedback loop back to input]

[LFO internal] ──────────────────▶ [APF center freq]
```

### Dual output: stereo spatial processing

```
[Source] ──[A]──▶ [IN]
                    │
              [12-stage APF chain]
                    ├──▶ [Stage 7 Out] ──[A]──▶ [Mingles Ch1] ──▶ [Left]
                    └──▶ [Stage 12 Out] ──[A]──▶ [Mingles Ch2] ──▶ [Right]

[Envelope] ──[C]──▶ [Shift CV] (LFO Mod Depth at zero, CV drives sweep)
```

### Self-oscillation as pitched source

```
[Nothing or quiet signal] ──▶ [IN]
Feedback: full clockwise
Manual Shift: set to desired pitch register
Mod Depth: low-to-medium (sweeps oscillation pitch at LFO rate)

[Stage 12 Out] ──[A]──▶ [Filter or VCA]
[Shift CV] ──[C]──▶ [External V/Oct or slow LFO for pitch control]
```

---

## Why The Toad Excels

The Toad's dual-output architecture is its primary practical advantage. Most phase shifters provide a single processed output; the Toad taps the phase shift network at stage 7 and stage 12 simultaneously, producing two outputs at different points in the phase rotation. These two outputs are not identical: stage 7 carries less accumulated phase shift than stage 12, so the two signals have different spectral relationships to the dry blend at any given Manual Shift or LFO position. Routing the two outputs to separate mixer channels or to separate downstream processors produces a natural stereo image from a mono source without additional modules, and patching them to different CV destinations or effects chains produces two distinct timbral perspectives on the same input simultaneously.

The feedback path determines how much of the Toad's character shows at any given setting. With the Feedback attenuverter at center, the phasing is clean and subtle: the classic swept comb filtering effect at a moderate depth. Advancing the attenuverter clockwise increases resonance at the notch frequencies until the filters self-oscillate and the module produces a pitched sine tone independent of any input signal. The same knob motion traverses the full range from transparent effect to self-contained pitched source, which means the Toad can shift roles within a patch without rewiring. Manual Shift sets the pitch of self-oscillation, making it possible to tune the self-oscillating Toad to a specific interval within the patch.

The twelve-stage design produces a denser, more complex phase relationship than four- or eight-stage alternatives. More stages means more notches in the frequency spectrum and a deeper, richer sweep at equivalent Mod Depth settings. The result is a phasing character that reads as more substantial and spatially immersive on sustained material, particularly when the LFO rate is slow enough for individual filter positions to be heard rather than blurred together.

## Advanced Learning Path

**Envelope as sweep source.** With Mod Depth at zero (LFO off) and an envelope generator patched into Shift CV, the Toad's notch comb sweeps through the frequency spectrum once per triggered event rather than continuously. The envelope shape determines the sweep contour: a fast attack pushes the notches upward quickly; a slow decay pulls them back down. Each note trigger creates a phased sweep event rather than a continuous cycle. This is a fundamentally different use of the phaser from LFO modulation and produces a more rhythmically intentional effect.

**Sequencer CV for stepped phasing.** A stepped sequencer output into Shift CV produces a phaser that snaps between specific notch positions on each clock step. With Manual Shift at 12 o'clock and the sequencer outputting a four-step pattern, the notch comb moves through four distinct spectral positions in rhythm with the sequence. The steps are audible as discrete tonal shifts rather than continuous sweeps. Combining this with a slow LFO at low Mod Depth adds gentle motion within each stepped position.

**Dual-output spatial processing into Mingles.** Route stage 7 into one Mingles channel and stage 12 into another. Set the Mingles channels to different pan positions. With stage 7 at positive dry mix and stage 12 at negative dry mix, the two outputs have opposing cancellation patterns and pan to opposite sides of the stereo field. A slow LFO sweeping the phaser moves both outputs' notch combs simultaneously, but because they started at different positions in the chain and have opposite dry polarities, the stereo image breathes and rotates rather than moving uniformly. Adding a stereo reverb after the Mingles extends the spatial movement into a wider acoustic environment.

**Feedback swept by CV.** Patching an envelope or LFO into the Shift CV while simultaneously adjusting the Feedback knob by hand creates a two-dimensional performance gesture: the CV controls where in the frequency spectrum the resonant peaks sit, and the hand control determines how sharp and prominent those peaks are. Pushing feedback toward self-oscillation and then pulling back with the LFO sweeping creates a sound that periodically approaches and retreats from self-oscillation in a rhythmic cycle.

**Audio-rate Shift CV.** Patching an audio-rate signal into Shift CV with the Shift CV attenuverter set to a low level produces a form of frequency modulation of the phase shifter's center frequency. The notch comb moves at audio rate, adding sidebands and harmonic content to the processed signal that goes beyond conventional phaser sweeping. This is an extreme effect that works best on rhythmically sparse or harmonically simple sources where the added complexity can be heard distinctly.

---

## Pairs Well With

**After Later Audio Mingles.** The Toad's two simultaneous outputs pair directly with Mingles' stereo panning capability. Stage 7 and stage 12 at different pan positions, with independent mix switch settings, produce a moving stereo image that changes as the phaser sweeps. Mingles' per-channel level control also allows the balance between the lighter seven-stage and fuller twelve-stage outputs to be adjusted in real time.

**Hermod+ (Squarp Instruments).** The Hermod+ provides sequenced CV output for the Shift CV input, enabling stepped or programmed phaser position sequences synchronized to the patch clock. Gate outputs from Hermod+ can trigger envelope generators whose outputs drive the Shift CV for rhythmically synchronized sweep events.

**Envelopes (any).** Envelope generators patched to Shift CV convert the phaser from a continuous sweep effect into a triggered one. Each note or clock event produces one sweep arc through the frequency spectrum. The envelope's shape directly determines the sweep contour.

**DivKid Ochd.** The Ochd's multiple slow LFO outputs at different rates give the option to replace the internal LFO (Mod Depth at zero) with an external LFO running at a tempo-unrelated rate, or to simultaneously modulate Shift CV at one rate while manually adjusting other parameters at a different tempo relationship.

**Qu-Bit Chord V2.** Polyphonic chord material through the Toad, especially through stage 12 with high feedback, produces a richly phased harmonic structure where the notch comb interacts differently with each component frequency of the chord. The resulting spectral movement is more complex than a phaser applied to a single-frequency source.

**Any stereo reverb or spatial processor.** The Toad's two outputs are an ideal front end for stereo effects that accept dual mono inputs. The spectral divergence between stage 7 and stage 12 gives the reverb or spatial processor two meaningfully different input characters to work with simultaneously, producing a stereo image with more depth and internal variation than a single mono source could provide.

---

## Common Mistakes

**Starting with Mod Depth at zero and wondering why nothing is happening.** Mod Depth at full left is off. The internal LFO is running but has no effect on the circuit. Increase Mod Depth before evaluating the Toad's character.

**Ignoring Manual Shift.** Manual Shift sets the center frequency around which modulation sweeps. With Manual Shift at an extreme position, the LFO modulation may sweep entirely outside the range where the phasing effect is most audible on a given source. Starting at 12 o'clock and adjusting from there ensures the modulation has symmetric sweep range in both directions.

**Pushing Feedback past the self-oscillation threshold accidentally.** The Feedback knob's transition from resonant to self-oscillating is not gradual near the extremes. In a performing or recording context, approach the extreme positions slowly and be prepared for self-oscillation to appear quickly. This is not a malfunction; it is the intended behavior of the circuit.

**Not accounting for the power draw.** At 110mA +12V and 100mA -12V, The Toad is a significant power consumer for its panel width. Both rails are loaded. Confirm available headroom on each bus before assuming the case can accommodate it alongside other power-hungry modules.

**Using only stage 12.** Stage 7 provides a meaningfully different output, not merely a quieter or simpler version of stage 12. Patching both outputs to separate destinations, even just two channels of a mixer, gives access to the Toad's full range of simultaneous spectral characters. Using only stage 12 leaves half the module's expressive output unplugged.

**Setting both mix switches identically without trying the opposing configuration.** The tonal difference between stage 7 positive/stage 12 positive and stage 7 positive/stage 12 negative is significant. The opposing configuration produces a wider spectral divergence between the two outputs and is worth a deliberate comparison before settling on the matched-polarity setup.

---

## What's Next

The Toad shapes audio spectrally through phase relationships rather than through frequency-selective attenuation. With phase shifting in the signal chain, the productive next focus is how the Toad's output interacts with filters and further effects: patching stage 12 into a voltage controlled filter and using the same modulation source to sweep both simultaneously produces a coupled spectral movement where phase and amplitude shaping change in lockstep.

The signal chain literacy guide (modular/basics/06_signal_chain.md) covers how effects modules like The Toad fit into the three-path voice model. The Mingles guide covers the specific panning and mixing capabilities that make dual-output use of The Toad most effective.

---

*Depth: 35mm. Power: 110mA +12V / 100mA -12V / 0mA +5V.*
