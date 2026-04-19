---
title: DivKid Ochd + Expander
manufacturer: DivKid
primary_role: MODULATOR
secondary_roles: []
form_factor: eurorack
functions: [lfo]
behavior_tags: [free-running, evolving, stable, generative]
use_cases: [modulation source, evolving ambient texture, stochastic modulation]
hp: 8
transport: receive
historical_context: true
---

# DivKid Ochd + Expander

**The Organic Drift Modulation Source**

![DivKid Ochd](https://github.com/Shadoe-42/music/raw/main/modular/images/divkid/ochd/front_panel.jpg)
*DivKid Ochd: Rate knob, CV input with attenuverter, eight triangle LFO outputs from fastest (top) to slowest (bottom)*

![DivKid Ochd Expander](https://github.com/Shadoe-42/music/raw/main/modular/images/divkid/ochd/exp_panel.jpg)
*DivKid Ochd Expander: Full Wave Rectifiers, Min/Max Logic, Cascading Triggers, 4-Bit DACs*

---

## Historical Context

Ben Wilson runs the DivKid YouTube channel from the UK, producing tutorial and review content for the Eurorack community. His output is educational and practical: he walks through module functions with a focus on how things actually get used in patches rather than on technical specifications. Around 2017-2018 he began developing his own modules in collaboration with Instruo, a small synthesizer manufacturer based in Glasgow, Scotland. Instruo was founded by George Hearn with a product line focused on analog hardware and a design sensibility shaped in part by the Scottish and Irish experimental music traditions. The company name and several product names draw from Scottish Gaelic: ochd is Scottish Gaelic for eight, and the name directly references the module's eight LFOs while acknowledging the geographic and cultural context of the manufacturing partner.

The ochd's design premise came from a practical observation Wilson had made during years of modular use: rigidly synchronized modulation tends to feel mechanical and predictable. When multiple LFOs lock to the same tempo, their phase relationships repeat exactly every cycle. Listeners habituate to repetitive patterns quickly, and modulation that never surprises loses its sense of movement. Free-running LFOs at slightly different rates drift gradually in and out of phase with each other, producing relationships that evolve over time and never repeat in exactly the same way. This is not a new idea; West Coast synthesis in the Buchla tradition embraced non-synchronized timing elements for similar reasons, and composers like Brian Eno and Harold Budd had built entire practices around slowly shifting, non-repeating modulation sources in their tape and synthesizer work. But it had not been implemented in this form for Eurorack: eight free-running triangle LFOs in 4HP, covering a useful musical range from vibrato speed at the top to very-long-term drift at the bottom, with a single Rate knob that scales all eight simultaneously while preserving the ratios between them.

The frequency range spans from roughly audio rate at the fastest setting down to 25-minute cycles at the slowest. At 12 o'clock on the Rate knob, the top LFO runs at approximately 3-7Hz, a vibrato rate, while the bottom LFO runs at cycle times measured in tens of seconds. The expander, added later, extended the module from 8 triangle wave outputs to 24 total outputs by applying four different processing operations to the existing LFO signals rather than generating new ones. Full Wave Rectification converts the bipolar triangle waves to unipolar 0-5V signals at double frequency. Min/Max Logic outputs the minimum and maximum voltage of specific LFO pairs, producing complex curves from two simple sources. Cascading Triggers generates gate outputs synchronized to LFO zero crossings. 4-Bit DAC conversion samples the LFO levels and converts them to stepped voltages, producing a sample-and-hold-like effect. The Expander uses only 5mA on each power rail because it is transforming signals that already exist rather than generating new ones.

---

## Quick Start: First Modulation in 5 Minutes

1. **Set Rate knob** to 12 o'clock
2. **Patch LFO 1 (top output)** → filter cutoff CV input
3. **Patch LFO 8 (bottom output)** → VCA CV input
4. **Play a sustained note:** the filter sweeps fast while the volume changes slowly
5. **Turn Rate clockwise:** both LFOs speed up together, maintaining their ratio

**Add a middle output:**

1. **Patch LFO 4** → oscillator pitch (through an attenuator reduced to about 20%)
2. **Listen:** three parameters now move at three different rates from one module

**If you have the Expander:**

1. **Connect the ribbon cable** (red stripe down on the expander side)
2. **Patch Full Wave Rect 1** → a parameter expecting unipolar CV (0-5V)
3. **Patch DAC A** → another parameter; notice it changes in discrete steps rather than smoothly

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width (Ochd) | 4HP |
| Width (Expander) | 4HP |
| Depth (both) | 32mm |
| Power (Ochd) | +80mA / -80mA |
| Power (Expander) | +5mA / -5mA |
| LFO outputs | 8 bipolar triangle waves, ±5V (10Vpp) |
| Full Wave Rect outputs | 4 unipolar, 0-5V, double frequency |
| DAC outputs | 4 stepped, 0-5V |
| Trigger outputs | 4 cascading gates |
| Logic outputs | 2 Min + 2 Max |
| Frequency range | ~audio rate (fast) to 25-minute cycle (slow) |

---

## Essential Parameters

**Rate** scales all eight LFOs simultaneously while preserving the ratios between them. At 12 o'clock, the fastest LFO runs at approximately 3-7Hz, a useful vibrato speed. Turned counterclockwise, all LFOs slow proportionally; the slowest can reach cycle times of 25 minutes. Turned fully clockwise, the fastest LFO approaches audio rate. The musical consequence of this unified control is that the LFOs always maintain their relative speed relationships to each other regardless of the Rate setting. What changes is the density of modulation activity, not the proportional character of the eight outputs.

**CV input and attenuverter** allow external control of Rate from a voltage source. Positive voltage increases the Rate, speeding up all LFOs; negative voltage decreases it, which at strong negative values can stall or freeze the LFOs at their current position. The attenuverter scales the incoming CV before it reaches the rate circuit. Patching one of the LFO outputs back into the CV input while adjusting the attenuverter creates a self-modulation effect that reshapes the triangle waves into more complex curves: exponential shapes, squared shapes, or stepped waveforms depending on the feedback amount. This feedback works because the LFO output is affecting the rate of its own oscillation, producing non-linear distortion of the waveform.

**Output position** determines the LFO speed. The eight outputs are arranged from fastest at the top (LFO 1) to slowest at the bottom (LFO 8). The speed ratios between adjacent outputs are not perfectly integer-spaced: the spacing is tuned for musical usefulness rather than mathematical precision, and the analog components introduce a small amount of individual variation that changes slightly with temperature and over time. This variation is the source of the organic drift behavior. Two units will not run at identical rates even at the same Rate setting, and the same unit will drift slightly between sessions.

---

## Why This Instrument Excels

The design decision to not synchronize the LFOs is the entire product. A synchronized LFO module with eight outputs would produce phase relationships that repeat exactly every cycle: predictable, useful, but not alive in the same way. The ochd's free-running LFOs drift gradually in and out of phase with each other, which means the modulation relationships change over time without any patch changes or performance intervention. A filter cutoff being modulated by LFO 3 and a VCA being modulated by LFO 6 start in one phase relationship and slowly arrive at another, then another, cycling through combinations over time that never exactly repeat. This is musically similar to what happens when two acoustic players play the same phrase at very slightly different tempos: the resulting phase shift between them creates rhythmic relationships that feel alive in a way that perfectly locked playing does not.

Eight outputs simultaneously available at a range of speeds means a single module can handle most of a patch's modulation needs without requiring multiple separate LFO modules taking up HP and mixing complexity. The Rate knob's unified control means all eight speeds can be adjusted for the current musical context in one gesture (slower for ambient drift, faster for rhythmic movement) while the proportional relationship between them stays intact. Most patches need modulation at several different timescales simultaneously: vibrato at a few Hz, filter sweep in the range of seconds, slow parameter drift in the range of minutes. The ochd addresses all three with one module.

The Expander's value is specifically in the signal processing operations it applies rather than in adding more LFOs. Full Wave Rectification doubles the frequency of the selected LFOs while making them unipolar (0-5V). Many synthesis parameters respond only to positive voltages, or respond in a way that is easier to predict when the modulation source only moves in one direction. A filter cutoff modulated by a bipolar LFO closes below its resting position as well as opening above it; modulated by a Full Wave Rectified version of the same LFO, it only opens. For pitch modulation, this means the pitch only rises, never drops. DAC conversion samples LFO voltages and quantizes them to stepped levels, producing a slow sample-and-hold effect from a source that is already at a musical rate and already drifting. The four cascading trigger outputs fire gates on each LFO zero crossing, providing rhythmic trigger sources at organic rates without requiring a separate clock source.

One single Rate knob affects 24 outputs simultaneously when the Expander is connected: eight triangle waves, four Full Wave Rectified versions, four stepped DAC outputs, four cascading triggers, and two pairs of Min/Max logic outputs. The musical consequence is that the entire modulation structure of a patch can be shifted from slow ambient drift to faster rhythmic activity in one gesture. This also means that one Rate CV input can modulate all 24 outputs simultaneously, which makes ochd unusually responsive to tempo-based or performance-based rate control compared to a collection of individual LFO modules where each rate would need its own CV.

---

## Progressive Patch Examples

### Patch 1: Beginner - Basic Organic Movement

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  DivKid Ochd    │    │   Oscillator     │    │   Filter        │
│                 │    │                  │    │                 │
│ LFO 1 ○─────────┼────┼─▶ FM Input       │    │                 │
│                 │    │                  │    │                 │
│ LFO 4 ○─────────┼────┼──────────────────┼────┼─▶ Cutoff CV     │
│                 │    │                  │    │                 │
│                 │    │ Audio Out ○──────┼────┼─▶ Audio In      │
│                 │    │                  │    │                 │
│ LFO 8 ○─────────┼────┼──────────────────┼────┼─────────────────┼─── VCA CV
└─────────────────┘    └──────────────────┘    │ Audio Out ○─────┼─── VCA In
                                               └─────────────────┘
```

| Connection | Signal | Purpose |
|------------|--------|---------|
| LFO 1 → Oscillator FM | [C] | Fast frequency modulation; attenuate to taste |
| LFO 4 → Filter Cutoff | [C] | Medium-speed filter sweep |
| LFO 8 → VCA CV | [C] | Slow amplitude drift |

**Module settings:**
- Rate: 12 o'clock
- FM input attenuator on oscillator: 8-9 o'clock (LFO 1 output is 10Vpp; attenuate before use on pitch)
- Leave CV input unpatched on Ochd

**Learning objectives:**
- LFO 1 at the top is the fastest output; LFO 8 at the bottom is the slowest. Listen to how these three outputs move at different rates simultaneously while remaining proportionally related to each other
- Turn Rate slowly clockwise and counterclockwise: all three modulation speeds change together. The ratio between them stays the same; only the overall density shifts
- After a few minutes, listen for how the phase relationship between the three LFOs shifts: LFO 1 and LFO 4 start at some phase relationship, drift apart, and meet again at a different point. This drift is the source of the organic quality
- Patch LFO 1 output back into the Rate CV input, with the attenuverter at about 10 o'clock: the LFO begins to reshape its own waveform through feedback, producing more complex curves than a pure triangle

---

### Patch 2: Intermediate - Expander Unipolar Modulation

The Expander's Full Wave Rectifiers convert bipolar triangle waves to unipolar 0-5V signals at double frequency. This patch uses them for pitch and filter modulation where unipolar behavior is musically cleaner: pitch only rises, filter only opens.

```
┌─────────────────────┐         ┌──────────────────────┐
│  DivKid Ochd        │         │  Oscillator          │
│  + Expander         │         │                      │
│                     │         │                      │
│ FWR 1 ○─────────────┼─────────┼─▶ 1V/Oct             │
│                     │         │                      │
│ FWR 3 ○─────────────┼─────────┼──────────────────────┼─── Filter Cutoff
│                     │         │                      │
│ DAC A ○─────────────┼─────────┼──────────────────────┼─── LFO Rate (external)
│                     │         │                      │
│ Min (2+3) ○─────────┼─────────┼──────────────────────┼─── VCA CV
│                     │         │                      │
│ Trigger 1 ○─────────┼─────────┼──────────────────────┼─── Envelope Gate
└─────────────────────┘         └──────────────────────┘
```

| Connection | Signal | Purpose |
|------------|--------|---------|
| FWR 1 → 1V/Oct | [C] | Unipolar pitch modulation: pitch only rises |
| FWR 3 → Filter Cutoff | [C] | Unipolar filter sweep: filter only opens |
| DAC A → LFO Rate input (external) | [C] | Stepped random rate control on another LFO module |
| Min (2+3) → VCA CV | [C] | Complex amplitude curve from two combined LFOs |
| Trigger 1 → Envelope Gate | [G] | Organic gate timing from LFO zero crossings |

**Module settings:**
- Rate: 12 o'clock
- FWR outputs are 0-5V; attenuate before pitch to reduce sweep range

**Learning objectives:**
- Compare the original LFO 1 (bipolar, ±5V) with its FWR 1 output (unipolar, 0-5V at double frequency): same source, different behavior. The pitch modulation from FWR only goes up; from the raw LFO it goes both up and down
- DAC A steps through discrete voltage levels rather than sweeping smoothly: the output changes at intervals rather than continuously. Listen to how this stepped behavior sounds different from the smooth LFO when applied to rate control
- The Min output of LFOs 2 and 3 follows whichever of the two is at the lower voltage at each moment. Because the two LFOs run at different rates and drift in phase, the Min output creates a complex curve that neither LFO produces on its own
- The Trigger 1 output fires a gate each time LFO 1 crosses zero. Because LFO 1 drifts relative to external timing, these gates are organic rather than locked to a tempo

---

### Patch 3: Expert - Ochd as Multi-Destination Modulation Hub

This patch uses the full set of Ochd outputs to simultaneously modulate different parameters across multiple modules. The goal is to demonstrate how one Rate knob can control the modulation density of an entire patch.

```
┌─────────────────────┐
│  DivKid Ochd        │
│  + Expander         │
│                     │
│ LFO 1 ○─────────────┼─── Wogglebug Ego Input (fast chaos character)
│                     │
│ LFO 3 ○─────────────┼─── Oscillator FM (medium vibrato)
│                     │
│ LFO 5 ○─────────────┼─── Filter Cutoff (slow sweep)
│                     │
│ LFO 8 ○─────────────┼─── VCA CV (very slow volume drift)
│                     │
│ FWR 1 ○─────────────┼─── Second Oscillator 1V/Oct (unipolar pitch drift)
│                     │
│ DAC B ○─────────────┼─── Wogglebug Speed/Chaos (stepped rate changes)
│                     │
│ Trigger 2 ○─────────┼─── Wogglebug Disturb (organic forced samples)
│                     │
│ Max (6+7) ○─────────┼─── Reverb Mix CV (slow evolving send amount)
└─────────────────────┘
```

| Connection | Signal | Purpose |
|------------|--------|---------|
| LFO 1 → Wogglebug Ego | [C] | Fast Ochd LFO modulates Wogglebug probability distribution |
| LFO 3 → Oscillator FM | [C] | Medium vibrato; attenuate before patching |
| LFO 5 → Filter Cutoff | [C] | Slow organic filter sweep |
| LFO 8 → VCA CV | [C] | Very slow amplitude drift |
| FWR 1 → 2nd Oscillator 1V/Oct | [C] | Unipolar pitch drift; only rises |
| DAC B → Wogglebug Speed/Chaos | [C] | Stepped rate changes for Wogglebug |
| Trigger 2 → Wogglebug Disturb | [G] | Organic gate timing forces Wogglebug samples |
| Max (6+7) → Reverb Mix | [C] | Long slow drift of reverb send |

**Module settings:**
- Rate: 11 o'clock (slightly slower for ambient density)
- Attenuate LFO 3 → FM heavily (10-20% of full range for pitch modulation)
- Wogglebug Speed/Chaos: 10 o'clock; DAC B will shift this in steps

**Learning objectives:**
- One Rate knob now controls eight separate modulation destinations across two or three modules simultaneously. Turn Rate slowly from 9 o'clock to 2 o'clock and listen to how the entire modulation density of the patch shifts
- Trigger 2 fires at an organic rate derived from LFO 2's zero crossings; this is not a clock but it is rhythmically related to the Ochd rate. When Rate changes, the Disturb timing changes proportionally
- The Wogglebug Ego input receiving LFO 1 means the fastest Ochd LFO is continuously shifting Wogglebug's probability distribution. The Wogglebug's random character drifts between clustered and spread as LFO 1 rises and falls
- Multiple parameters at different timescales create a sense of ongoing motion at several levels simultaneously: fast vibrato, medium filter movement, slow volume drift, very slow reverb shift

---

### Patch 4: Advanced - Rate CV Feedback and Expander Integration

Patching one of Ochd's own outputs back into the Rate CV input creates a self-modulating system where the LFO rate varies with the LFO's own output. The shape of the triangle wave distorts depending on how much feedback is applied via the attenuverter.

```
┌─────────────────────┐         ┌──────────────────────┐
│  DivKid Ochd        │         │  Cre8audio           │
│  + Expander         │         │  Function Junction   │
│                     │         │                      │
│ LFO 2 ○─────────────┼────┐    │                      │
│                     │    │    │                      │
│ [attenuverter]      │    └────┼─▶ Rate CV Input       │
│ Rate CV In ◀────────┼────┘    │  (attenuverter: slow)│
│                     │         │                      │
│ LFO 4 ○─────────────┼─────────┼─▶ Ch1 CV In          │
│                     │         │                      │
│ FWR 3 ○─────────────┼─────────┼─▶ Ch2 CV In          │
│                     │         │                      │
│ DAC C ○─────────────┼─────────┼─▶ Gate/Trigger timing │
│                     │         │                      │
│ LFO 6 ○─────────────┼─────────┼─▶ Mix mod input      │
│                     │         │                      │
│ LFO 8 ○─────────────┼─────────┼──────────────────────┼─── Downstream VCA
└─────────────────────┘         └──────────────────────┘
```

| Connection | Signal | Purpose |
|------------|--------|---------|
| LFO 2 → Rate CV In (via attenuverter) | [C] | Self-modulation: LFO 2 shapes its own waveform |
| LFO 4 → Function Junction Ch1 | [C] | Medium LFO into envelope processing |
| FWR 3 → Function Junction Ch2 | [C] | Unipolar version of LFO 3; always positive |
| DAC C → Function Junction Gate input | [G] | Stepped values used as gate-height control |
| LFO 6 → Function Junction Mix | [C] | Slow LFO modulates mix between channels |
| LFO 8 → Downstream VCA | [C] | Very slow amplitude shaping |

**Module settings:**
- Attenuverter for Rate CV feedback: start at 9 o'clock, move slowly clockwise while listening
- Rate: 12 o'clock as starting point; the feedback will modify the effective rate
- Function Junction: process Ch1 and Ch2 inputs into shaped outputs for filter, VCA, or other destinations

**Learning objectives:**
- Start with the attenuverter at minimum (no feedback) and listen to pure triangle waves. Move the attenuverter slowly clockwise while monitoring LFO 2 at audio rate or watching an oscilloscope if available: the waveform begins to bend. At low feedback amounts the result is slightly asymmetric; at moderate amounts it becomes an exponential curve or squared shape; at high amounts it becomes unstable
- The attenuverter sweet spot for musical feedback waveshaping is typically between 10 and 30 percent of full clockwise rotation. Beyond this the system becomes increasingly chaotic
- Function Junction receiving both a smooth LFO and its Full Wave Rectified counterpart demonstrates how signal processing can create useful relationships between two sources: LFO 4 is bipolar, FWR 3 is its unipolar counterpart. Processing them together produces output shapes that neither produces alone
- One Rate knob still controls all outputs simultaneously, including the feedback-distorted LFO 2. Adjusting Rate while feedback is active changes both the rate and the feedback amount simultaneously, since the attenuverter scales the LFO output that feeds into Rate

---

## Common Use Cases

**Ambient texture:** Slow LFOs (6, 7, 8) into filter cutoff, reverb send, and oscillator detune produce slowly evolving textures that shift continuously without repeating. Set Rate below 12 o'clock for cycle times measured in minutes rather than seconds.

**Vibrato and tremolo:** LFO 1 or 2 into oscillator pitch (heavily attenuated) and LFO 3 or 4 into VCA CV produce simultaneous vibrato and tremolo at slightly different rates. The rates drift apart over time, producing a subtle phasing effect between the pitch and amplitude modulation.

**Organic gate timing:** Expander trigger outputs fire at rates derived from specific LFO zero crossings. Patching these to envelope generators produces notes at organic intervals. Since the triggers are proportional to the Rate setting, turning Rate up produces denser events while preserving the timing relationships between the four trigger outputs.

**Filter sweep automation:** LFO 5 or 6 into filter cutoff with Rate around 11 o'clock produces a 10-30 second sweep cycle. Turning Rate slowly during performance shifts the sweep density, covering a wide range of filter motion speeds from one patch.

**Stepped modulation without sample-and-hold:** DAC outputs step through discrete levels at LFO rates. Applied to delay time, reverb size, or a second LFO rate input, the stepped behavior creates discrete rather than continuous changes, similar to sample-and-hold but with the advantage of being synchronized to the overall Rate scaling.

**Unipolar pitch drift:** Full Wave Rectifier outputs applied to oscillator 1V/Oct create a pitch drift that only goes upward from the resting pitch. Slow rates produce gradual rising inflections; fast rates create tremolo-like pitch oscillation that does not go below the original pitch.

---

## Common Mistakes

### "My modulation does not sync with the sequencer"

Ochd's LFOs are designed to not synchronize to an external clock. They run freely and drift relative to any external timing. This is intentional. Modulation that repeats exactly in time with a sequencer feels predictable and mechanical; modulation that drifts relative to the sequence creates continuously changing relationships.

If strict synchronization is required, patch a clock source to the Rate CV input with the attenuverter set so that the incoming clock voltage speeds and slows the LFOs to follow the external tempo. This is not how the module is primarily intended to work, but it is possible. For most uses, the drift is the feature, not a limitation to correct.

---

### "The filter barely responds to the LFO"

The LFO outputs are bipolar (±5V). If the filter's cutoff CV input only responds to positive voltages, negative portions of the LFO waveform will push the cutoff below its minimum and produce no audible change. The result sounds like weak or sluggish modulation because only half the LFO's range is doing anything.

Use the Expander's Full Wave Rectifier outputs for unipolar (0-5V) filter modulation. Without the Expander, mix the LFO with a DC offset to shift the entire waveform into positive territory, or use an attenuverter module that can add a positive offset. Another approach: patch the LFO through a precision rectifier utility module before it reaches the filter.

---

### "Everything is modulating too dramatically"

The LFO outputs are 10Vpp, which is a large voltage swing for many synthesis parameters. Pitch modulation typically requires only a fraction of this range: 1V of FM produces a full octave of pitch deviation. A full 10Vpp LFO into an unattenuated FM input produces 10 octaves of deviation, which is not useful.

Attenuate every LFO output before patching to sensitive parameters, especially pitch. Start with the attenuator at its minimum and increase slowly until the modulation depth matches what is musically useful. A 10-20% attenuator position often works for pitch; 40-70% may work for filter cutoff depending on the filter's CV sensitivity.

---

### "All 8 LFOs seem to move at the same speed"

The Rate knob scales all eight LFOs simultaneously. Moved quickly, the change happens faster than the ear can distinguish the speeds from each other. Let the Rate knob settle in one position for several seconds and listen to specific outputs in isolation: LFO 1 is clearly faster than LFO 4, which is clearly faster than LFO 8. The variety is in the ratios, not in independent speed controls.

Patch LFO 1 and LFO 8 to two different visual indicators or listen to them through separate VCA outputs at the same volume. The speed difference is obvious when comparing specific outputs directly rather than listening to the whole patch at once.

---

### "The feedback waveshaping is just producing noise"

Feedback through the Rate CV input is very sensitive to attenuverter position. Too much feedback sends the LFOs into instability; too little produces no audible change. The effective range for musical waveshaping is typically narrow: 10-30% of the attenuverter's clockwise range.

Start with the attenuverter at minimum and rotate very slowly clockwise while listening. The waveform change is subtle at first, a slight asymmetry in the triangle wave, and becomes more pronounced as feedback increases. If the result sounds unstable or noise-like, back the attenuverter off toward minimum. The effect is most predictable when feeding a slow LFO (5, 6, or 7) rather than the fastest ones.

---

### "The Expander trigger outputs fire unpredictably"

The trigger outputs fire each time a specific LFO crosses zero. Because the LFOs are free-running and not synchronized to an external clock, the triggers are organic rather than metronomic. This is the same drift behavior that all Ochd outputs share, applied to gate timing.

Patch each trigger output independently to see what it does in isolation before combining them. The outputs are normalled to cascade (an unpatched trigger input receives the signal from the trigger above it), which can produce unexpected behavior if not all jacks are deliberately patched. If the behavior feels too chaotic, patch each output explicitly rather than relying on the cascade.

---

## Advanced Learning Path

1. **Start with three LFO outputs at different positions and spend time at a fixed Rate setting.** The goal is to hear how LFO 1, LFO 4, and LFO 8 behave differently at the same Rate, and how their phase relationship drifts over time. This is the foundational Ochd experience; everything else builds on this.

2. **Practice using the Rate knob as a real-time control.** While a patch is running, slowly turn Rate from its slowest useful position to its fastest and back. This single knob is the primary performance control for the module. Understanding the full range of the Rate knob as a performance gesture is more useful than any other technique the module offers.

3. **Add the Expander and compare FWR outputs to their source LFOs.** Patch LFO 1 and FWR 1 to two identical modulation destinations (two copies of the same parameter, or two channels of a mixer) and compare. The FWR version runs at double frequency and stays positive. Understanding this relationship concretely makes the full set of Expander outputs interpretable.

4. **Explore the DAC outputs applied to a second LFO module's Rate input.** The stepped voltages from DAC outputs change the second LFO's rate in discrete increments rather than smoothly. This produces rate changes that feel quantized, a different character from a smooth LFO modulating rate. Compare the sound of DAC-controlled rate changes against smooth LFO-controlled rate changes on the same destination.

5. **Practice the Rate CV feedback technique through the attenuverter.** Start at minimum and move slowly. Find the point where the triangle wave begins to distort and learn where the boundary between useful waveshaping and instability sits on your specific unit. The sweet spot varies slightly between units due to component tolerances.

6. **Integrate Ochd with a module that has multiple CV inputs** (a complex oscillator, a multi-parameter effects module, or an advanced filter) and patch several Ochd outputs to different CV inputs on that module simultaneously. Adjust Rate and hear how shifting the overall Ochd density affects multiple parameters of the target module at once. This demonstrates Ochd's value as a unified modulation source for HP-efficient multi-parameter control.

7. **Explore the trigger outputs in a percussion or gate-driven context.** Patch the four trigger outputs to four envelope generators driving different voices and listen to how the organic trigger timing affects the rhythmic feel. Adjust Rate to shift the density of events. This use of Ochd as a timing source rather than a modulation source opens a different set of musical possibilities from the CV outputs.

---

## Pairs Well With

**Make Noise Wogglebug:** Ochd's trigger outputs patched to Wogglebug's Disturb input provide organic trigger timing for forced random values. Ochd LFOs patched to Wogglebug's Ego input gradually shift the random distribution over time. The two modules represent complementary chaos sources: Ochd provides structured drift, Wogglebug provides genuine randomness, and the combination of both produces a modulation environment that is neither predictably periodic nor uniformly random.

**Mutable Instruments Marbles:** Ochd DAC outputs patched to Marbles' Spread or DEJA VU CV inputs shift Marbles' behavior in stepped increments from the same Rate-controlled source that drives the rest of the patch. Ochd trigger outputs can provide an external clock for Marbles, keeping gate timing organically related to the Rate setting.

**4ms RCD v2:** Ochd trigger outputs into RCD's Clock In provide organic clock timing for polyrhythmic division. The RCD's divided outputs are then at rhythmically structured fractions of Ochd's organic timing, producing polyrhythmic patterns with a non-metronomic feel. Adjusting Ochd's Rate changes the entire rhythmic density of the RCD network proportionally.

**VCAs and attenuverters:** Any Ochd output benefits from an attenuator before it reaches sensitive parameters. Quad VCA modules (Veils, Intellijel Quad VCA) are useful for scaling multiple Ochd outputs independently before they reach their destinations. An attenuverter that can invert polarity is useful for creating opposing motion from two related Ochd outputs.

**Quantizers:** LFO outputs passed through a quantizer before reaching oscillator pitch produce stepwise pitch movement in a musical scale rather than smooth FM. This converts Ochd's continuous output into discrete pitch values, which is useful for melodic applications where pitch modulation should stay in key.

**Filters with extensive CV:** Ochd benefits from being paired with filters that have multiple CV inputs, since it can simultaneously modulate cutoff, resonance, and any additional filter parameters from different LFO outputs at different rates. Filters with fewer CV inputs limit Ochd's multi-parameter value.

---

*Visit [divkidvideo.com](https://divkidvideo.com) and [instruomodular.com](https://www.instruomodular.com) for full documentation*
