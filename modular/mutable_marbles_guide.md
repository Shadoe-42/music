---
title: Mutable Instruments Marbles
manufacturer: Mutable Instruments
primary_role: MODULATOR
secondary_roles: [SOURCE, CONTROLLER]
form_factor: eurorack
functions: [random-source, sequencer]
behavior_tags: [stochastic, evolving, generative, free-running, performance-oriented]
use_cases: [generative melodic sequence, stochastic modulation, random CV generator, self-evolving patch element]
hp: 18
transport: receive
historical_context: true
---

# Mutable Instruments Marbles

**The Stochastic Pattern Generator**

![Mutable Instruments Marbles](https://github.com/Shadoe-42/music/raw/main/modular/images/mutable_instruments/marbles/front_panel.jpg)
*Mutable Instruments Marbles: Rate, DEJA VU, Steps, Spread, Bias controls; three t gate outputs; three X CV outputs; Y CV output*

---

## Historical Context

Iannis Xenakis coined the term "stochastic music" in the 1950s, drawing on the Greek word for "aimed-at." Where John Cage used chance operations to remove the composer's intentions from the work, Xenakis used probability distributions to model processes that have natural structure: the way individual particles in a gas behave randomly but produce predictable aggregate behavior, the way rain sounds irregular in detail but consistent in character. The distinction matters. Pure randomness produces sequences that feel arbitrary; probability-weighted randomness produces sequences that feel like they belong to a world with internal rules. Xenakis was arguing that mathematics could formalize the second kind and use it compositionally.

The problem that followed composers into modular synthesis was practical. Random voltage generators produced values that were too statistically flat to be musically useful without significant patching overhead. Earlier modules had addressed part of this by giving performers control over probability distributions, but the question of repetition remained open. Human performers, even when improvising freely, naturally produce local repetition: a phrase slightly varied, a rhythm returned to, a pitch revisited. Pure random generators produce none of this unless explicitly patched to store and recall values, which typically required external sequencers and logic.

Émilie Gillet founded Mutable Instruments in 2011, building a catalog of modules whose designs engaged compositional and philosophical questions as directly as technical ones. The open-source publication of all circuit schematics and firmware was not incidental; it reflected a conviction that instruments should be understood by the people who use them. Marbles, released in 2018, was Gillet's direct answer to the repetition problem. Its DEJA VU system works by maintaining a buffer of recently generated values and, at each decision point, probabilistically choosing between drawing a new value from the hardware random source or recycling a value from the buffer. The result is not a memorized pattern; it is a probability-weighted tendency toward recent material. At one extreme the output is genuinely random; at the other it is a locked loop; across the middle range it produces the kind of evolving-but-familiar sequences that human performers generate through habit and musical preference.

Mutable Instruments closed in 2022. Gillet open-sourced all remaining designs before the company ended, and Marbles has since been cloned, ported to VCV Rack, and incorporated into other instruments. The DEJA VU architecture is now a reference point for how to make randomness compositionally useful rather than merely statistically present.

---

## Quick Start: First Random Sequence in 5 Minutes

1. **Patch X1** → oscillator 1V/Oct input
2. **Patch t2** → envelope generator trigger input
3. **Set RATE** to 12 o'clock
4. **Set STEPS** to 2 o'clock (quantized range, musical intervals)
5. **Let it run:** a random melody appears with rhythmic gating

**Add DEJA VU:**

1. **Turn DEJA VU to 11 o'clock:** patterns begin repeating but continue to evolve slowly
2. **Turn DEJA VU to 12 o'clock exactly:** the current phrase locks into a perfect loop
3. **Turn DEJA VU past 12 o'clock:** the locked phrase shuffles its note order without losing the pitches

**Add a second voice:**

1. **Patch X2** → a second oscillator 1V/Oct
2. **Patch t1** → that oscillator's envelope trigger
3. **X1 and X2 are different outputs from the same probability system:** they diverge over time

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 18HP |
| Depth | ⚠️ ~25mm |
| Power | ⚠️ +120mA / -5mA |
| Gate outputs | t1, t2, t3 |
| CV outputs | X1, X2, X3 (quantizable), Y (smooth random) |
| Clock | Internal (RATE knob) or external (CLOCK input) |
| Algorithm modes | Green (conservative) / Orange (moderate) / Red (complex) |

---

## Essential Parameters

**RATE** sets the master clock tempo when running in internal clock mode. At 12 o'clock the clock runs at approximately 120 BPM. The RATE has a V/Oct CV input, which means tempo can be sequenced: patching a sequencer's CV output to the RATE CV input shifts the tempo in musically tuned intervals as the sequence advances. Patching an external clock to the CLOCK input overrides the internal RATE entirely and locks the module to external timing.

**DEJA VU** is the memory control. The underlying mechanism maintains a buffer of recently generated values. When DEJA VU is below 12 o'clock, the module draws freely from the random source with the buffer having diminishing influence as the knob moves left. At 12 o'clock the module locks into a repeating loop of whatever has recently accumulated in the buffer. Above 12 o'clock the module enters a shuffle mode: the same values from the buffer recombine in different orders rather than repeating exactly. The t button and X button next to DEJA VU select which sections (timing/gates or voltage/pitch) are subject to the memory system; either, both, or neither can be engaged.

**STEPS** controls the shape and quantization of the X voltage outputs. Turned left of center, the X outputs produce smooth, slowly wandering voltage curves suited to continuous modulation use. At center they produce classic stepped random voltages. Turned right of center, the values are progressively quantized toward musical intervals: first chromatic quantization, then diatonic, then only root notes and octaves at the far right. The practical effect is that the same module can produce free-form modulation CV or pitch-quantized melodic sequences from the same output by changing one knob.

**SPREAD** controls the probability distribution of the X output values: how clustered or spread out they are across the available voltage range. Fully left produces a constant voltage (no randomness). At 12 o'clock the distribution forms a bell curve, with most values near the center of the range. At 2 o'clock the distribution is approximately uniform across the full range. Fully right produces only extreme values, minimum and maximum, which turns the X outputs into random gates rather than pitch CVs.

**BIAS** shifts the probability distribution toward high or low voltage values. Turned left, the distribution favors lower voltages; applied to pitch, this means lower notes appear more frequently. Turned right, higher voltages dominate. Bias and Spread interact: Bias shifts where the center of the distribution sits, while Spread determines how wide it is. Both have CV inputs for external modulation.

**Algorithm mode** (green, orange, red, selected by holding the t button) controls the rhythmic complexity of the t gate outputs. Green mode produces simpler, more conservative timing patterns. Orange adds more syncopation and variation. Red produces complex polyrhythmic relationships between t1, t2, and t3. The algorithm mode does not affect the X voltage outputs.

---

## Why This Instrument Excels

The DEJA VU system's specific contribution is solving the musical repetition problem in a way that feels performative rather than programmed. A step sequencer solves the problem by having the performer record a fixed phrase, which then repeats identically. Marbles' buffer system solves it without recording: the current contents of the buffer represent a probability-weighted tendency toward recent material, not a stored pattern. Locking DEJA VU at 12 o'clock produces a loop, but that loop emerged from the live random process rather than being deliberately composed. Unlocking it allows the pattern to start drifting again from where it is. This means DEJA VU is a real-time performance control rather than a programming step: turning it during a performance locks patterns or releases them on demand, and the transition between states is immediate and musical.

The module's two-section architecture separates timing from pitch at the panel level in a way that makes independent control natural. The t section generates gate and trigger patterns; the X section generates CV voltages. Both sections have their own DEJA VU engagement, their own probability controls, and their own outputs. This means rhythmic patterns can lock while pitch continues to evolve, or pitch patterns can lock while rhythm changes, or both can be independently varied. No dedicated sequencer achieves this because sequencers record the combination of timing and pitch together; here they are generated by distinct but related probability systems.

STEPS covers a range from free-form modulation source to pitch-quantized melodic sequencer without changing any patch cables. A CV output that is producing smooth wandering modulation suitable for filter cutoff can be shifted by the STEPS knob into a source of diatonic melody in key, and back again. This single-control range means the module serves double duty as both modulation source and pitch sequencer depending on STEPS position, which is valuable in patches where HP is constrained or where the musical context demands shifting between the two uses.

The Y output provides a fourth CV channel that follows different probability rules from the X outputs and does not participate in DEJA VU quantization in the same way. It produces a smooth, slowly wandering random voltage with its own character, useful as an independent modulation source when X1-X3 are committed to pitch duties. Patching Y back into the DEJA VU CV input creates a self-modulating feedback loop: the module's own output biases its own memory system, producing evolving behavior driven by the current output state rather than by external control. This patch requires no additional modules and produces results that change over time without intervention.

---

## Progressive Patch Examples

### Patch 1: Beginner - Random Melody with Gate Control

```
┌─────────────────────┐    ┌──────────────────┐
│ Mutable Instruments │    │   Oscillator     │
│ Marbles             │    │                  │
│                     │    │                  │
│ X1 ○────────────────┼────┼─▶ 1V/Oct         │
│                     │    │                  │
│                     │    │ Audio Out ○──────┼─── Filter In
│                     │    └──────────────────┘
│ t2 ○────────────────┼─── Envelope Trigger
│                     │
│ [Envelope Out] ─────┼─── VCA CV
└─────────────────────┘
```

| Connection | Signal | Purpose |
|------------|--------|---------|
| X1 → Oscillator 1V/Oct | [C] | Random pitch; STEPS controls quantization amount |
| t2 → Envelope Generator Trigger | [G] | Gate timing for each pitch change |
| Envelope Out → VCA CV | [C] | Shapes each note's amplitude |

**Module settings:**
- RATE: 12 o'clock
- STEPS: 2 o'clock (quantized toward musical intervals)
- DEJA VU: 11 o'clock (slow evolution, not yet locked)
- SPREAD: 12 o'clock (bell-curve distribution)
- BIAS: 12 o'clock (no preference)
- Algorithm mode: green or orange

**Learning objectives:**
- Turn STEPS from left to right and listen to the X1 output transform from smooth modulation through stepped random through quantized pitch. The output is from the same probability system across the entire range; only the shape and quantization of values changes
- Engage DEJA VU at 11 o'clock and listen over several minutes: patterns begin returning without locking completely. Advance DEJA VU to 12 o'clock and identify the moment a phrase locks. Then turn back to 11 o'clock and listen to the locked pattern begin drifting again
- With DEJA VU locked, change SPREAD and listen to how the loop's pitch range changes: narrower Spread pulls all pitches toward center, wider Spread extends the range. The locked phrase adapts to the new distribution
- Patch X2 to a second destination simultaneously with X1. X1 and X2 are different outputs from the same system; they produce correlated but not identical values and diverge over time

---

### Patch 2: Intermediate - Parameter-Modulated Marbles

Ochd LFOs applied to Marbles' RATE, SPREAD, and BIAS CV inputs create a slowly drifting pattern character. The quantization and memory behavior change continuously as the LFOs move through their ranges.

```
┌─────────────────┐    ┌──────────────────────┐    ┌─────────────────┐
│  DivKid Ochd    │    │ Mutable Instruments  │    │   Oscillator    │
│                 │    │ Marbles              │    │                 │
│ LFO 1 ○─────────┼────┼─▶ RATE CV            │    │                 │
│                 │    │                      │    │                 │
│ LFO 3 ○─────────┼────┼─▶ SPREAD CV          │    │                 │
│                 │    │                      │    │                 │
│ LFO 7 ○─────────┼────┼─▶ BIAS CV            │    │                 │
│                 │    │                      │    │                 │
│                 │    │ X1 ○─────────────────┼────┼─▶ 1V/Oct        │
│                 │    │                      │    │                 │
│                 │    │ X2 ○─────────────────┼────┼─▶ FM Input      │
│                 │    │                      │    │                 │
│ LFO 2 ○─────────┼────┼─▶ Filter Cutoff ─────┼────┼─                │
│                 │    │                      │    │ Audio Out ○─────┼─── Output
└─────────────────┘    │ t1 ○─────────────────┼────┼─▶ Envelope Gate │
                       │                      │    └─────────────────┘
                       │ Y ○──────────────────┼────── Reverb Send
                       └──────────────────────┘
```

| Connection | Signal | Purpose |
|------------|--------|---------|
| Ochd LFO 1 → Marbles RATE CV | [C] | Organic tempo drift; rate breathes over long cycles |
| Ochd LFO 3 → Marbles SPREAD CV | [C] | Distribution width evolves; pitch range narrows and widens |
| Ochd LFO 7 → Marbles BIAS CV | [C] | High/low preference shifts slowly; melodic register drifts |
| Ochd LFO 2 → Filter Cutoff | [C] | Independent filter sweep at medium LFO rate |
| Marbles X1 → Oscillator 1V/Oct | [C] | Quantized random pitch from the pattern system |
| Marbles X2 → Oscillator FM | [C] | Second X output for timbral modulation |
| Marbles t1 → Envelope Gate | [G] | Gate timing from Marbles' rhythmic section |
| Marbles Y → Reverb Send | [C] | Slow independent random for evolving reverb mix |

**Module settings:**
- Ochd Rate: 9 o'clock (slow LFO cycles for gradual drift)
- Marbles STEPS: 2 o'clock (melodic quantization)
- Marbles DEJA VU: 10-11 o'clock (slow evolution with memory tendency)
- Marbles Algorithm: orange

**Learning objectives:**
- Ochd LFO 1 on RATE CV shifts tempo continuously; the pattern speeds and slows with the LFO. Notice that very slow Ochd LFO 1 produces changes that feel like gradual tempo acceleration and deceleration rather than sudden shifts
- Ochd LFO 7 on BIAS shifts the melodic register: the same probability system produces higher or lower pitches as the bias moves. Over a slow LFO cycle, the melody drifts from bass register to upper register and back without any manual intervention
- The Y output on reverb send operates independently from X1 and X2; it evolves on its own slow random trajectory regardless of what the rest of Marbles is doing
- Three Ochd LFOs each control a different Marbles parameter at slightly different rates. Because the LFOs drift relative to each other, the combination of RATE, SPREAD, and BIAS effects produces a constantly shifting pattern character

---

### Patch 3: Expert - Polyrhythmic Percussion with Self-Modulation

Marbles generates three independent gate streams from its t outputs in Red algorithm mode. The Y output patches back into the DEJA VU CV input, creating a self-modulating system where the current output state affects the module's own memory behavior.

```
┌─────────────────────┐
│ Mutable Instruments │
│ Marbles             │
│ [Red algorithm]     │
│                     │
│ Clock In ◀──────────┼─── Master Clock
│                     │
│ t1 ○────────────────┼─── Kick drum trigger
│                     │
│ t2 ○────────────────┼─── Snare drum trigger
│                     │
│ t3 ○────────────────┼─── Hi-hat trigger
│                     │
│ X1 ○────────────────┼─── Kick pitch CV (if tunable)
│                     │
│ X2 ○────────────────┼─── Melodic voice 1V/Oct
│                     │
│ Y ○─────────────────┼─▶ DEJA VU CV In
└─────────────────────┘
         ║ [Y feeds back into DEJA VU CV]
```

| Connection | Signal | Purpose |
|------------|--------|---------|
| Master Clock → Clock In | [G] | External timing locks Marbles to song tempo |
| t1 → Kick trigger | [G] | Primary rhythmic pulse in Red algorithm |
| t2 → Snare trigger | [G] | Secondary cross-rhythm pattern |
| t3 → Hi-hat trigger | [G] | Tertiary rhythmic layer; most complex in Red mode |
| X1 → Kick pitch CV | [C] | Random pitch variation on tunable percussion |
| X2 → Melodic 1V/Oct | [C] | Pitch sequence simultaneous with percussion |
| Y → DEJA VU CV | [C] | Self-modulation: Y output biases its own memory |

**Module settings:**
- Algorithm mode: Red (held t button; complex polyrhythmic relationships between t1, t2, t3)
- BIAS: 2 o'clock (denser rhythmic activity in t outputs)
- JITTER: 10 o'clock (subtle timing humanization if available on firmware)
- DEJA VU: 11 o'clock as baseline; Y output will push and pull this
- External clock: patched; RATE knob inactive

**Learning objectives:**
- Red algorithm mode produces significantly different rhythmic relationships between t1, t2, and t3 than green or orange. Listen in isolation: t1 fires more often than t2, t2 more often than t3, but not in simple integer ratios. The relationships shift as BIAS changes
- The Y → DEJA VU feedback path means the current Y voltage is continuously pushing the DEJA VU control toward more or less memory engagement. As Y drifts, the t outputs shift between evolving patterns and locked loops without manual intervention
- Using an external clock locks the timing to the master tempo while all probability parameters remain free. The rhythmic patterns produced by Marbles in Red mode feel humanized but tempo-synchronized
- X2 producing melodic pitch while t1-t3 produce drum triggers demonstrates that both sections are running simultaneously from the same module: one source provides both rhythm and melody

---

### Patch 4: Advanced - Full Output Matrix as Complete Voice

All seven Marbles outputs patch to different destinations: X1-X3 carry pitch CVs for three independent melodic voices, t1-t3 carry their individual gates, and Y provides slow modulation to a shared processing parameter. DEJA VU at different settings on t and X independently creates rhythmic loops while melody continues evolving, or locked melodies while rhythm continues shifting.

```
┌─────────────────────┐    Three voices from Marbles:
│ Mutable Instruments │
│ Marbles             │    Voice 1:
│                     │    X1 ○────── Oscillator 1 1V/Oct
│ [DEJA VU: X only]   │    t1 ○────── Oscillator 1 envelope gate
│                     │
│                     │    Voice 2:
│                     │    X2 ○────── Oscillator 2 1V/Oct
│                     │    t2 ○────── Oscillator 2 envelope gate
│                     │
│                     │    Voice 3:
│                     │    X3 ○────── Oscillator 3 1V/Oct
│                     │    t3 ○────── Oscillator 3 envelope gate
│                     │
│                     │    Shared modulation:
│                     │    Y ○─────── Filter cutoff (all three voices)
└─────────────────────┘
```

| Connection | Signal | Purpose |
|------------|--------|---------|
| X1 → Oscillator 1 1V/Oct | [C] | Voice 1 pitch from Marbles X section |
| t1 → Oscillator 1 envelope gate | [G] | Voice 1 timing; t1 fires most densely |
| X2 → Oscillator 2 1V/Oct | [C] | Voice 2 pitch; correlated with X1 but distinct |
| t2 → Oscillator 2 envelope gate | [G] | Voice 2 timing; t2 fires at different rate from t1 |
| X3 → Oscillator 3 1V/Oct | [C] | Voice 3 pitch; third independent but correlated output |
| t3 → Oscillator 3 envelope gate | [G] | Voice 3 timing; t3 fires least densely |
| Y → Shared filter cutoff | [C] | Slow independent random modulation across all voices |

**Module settings:**
- STEPS: 2 o'clock (quantized pitch for melodic voices)
- SPREAD: 12-1 o'clock (moderate range gives workable pitch distribution)
- BIAS: 12 o'clock (neutral; adjust to shift melodic register of all three voices)
- DEJA VU: engage X button only, not t button. Lock X DEJA VU at 12 o'clock: all three X outputs repeat the same phrase while t outputs continue evolving
- Algorithm mode: orange or red

**Learning objectives:**
- X1, X2, and X3 are correlated but not identical; they share probability parameters but produce different values. When X DEJA VU locks, all three voices lock into a repeating chord pattern: the same phrase heard simultaneously across three oscillators
- With X locked and t free, rhythmic timing continues to evolve while pitch stays consistent. This is the practical value of independent DEJA VU control: phrase-loop the melody while the rhythm continues to breathe
- Y is not subject to DEJA VU and continues its slow random drift regardless of what X and t are doing. The filter cutoff moves independently of the pitch and timing structure, adding a continuously evolving spectral character to the locked phrase
- With three voices running, change STEPS from 2 o'clock to 3 o'clock: the X outputs quantize more strictly and the chord voicings simplify. Move STEPS toward far right: only root notes appear and all three voices converge toward unison or octave relationships

---

## Common Use Cases

**Generative melodic sequences:** X1 into a 1V/Oct input with STEPS at 2 o'clock and DEJA VU at 11 o'clock produces melodies that stay roughly in a musical range, occasionally repeat phrases, and gradually evolve without manual intervention. This is the foundational Marbles application.

**Polyrhythmic gate generation:** The three t outputs in Red algorithm mode produce independent but related gate streams for driving multiple envelope generators or percussion voices. Gate density and polyrhythmic complexity are controlled by BIAS and the algorithm mode.

**Self-evolving ambient patch:** Y output into DEJA VU CV creates a patch that shifts between more and less repetitive behavior based on its own output, requiring no external control after initial setup.

**Humanized sequencer timing:** Marbles accepts external clock and applies its JITTER control to that timing, producing slightly humanized versions of a rigid clock source. The t outputs then carry this humanized timing to other modules.

**Multi-voice chord generator:** X1, X2, and X3 simultaneously into three oscillators with DEJA VU X locked produces repeating chord patterns drawn from the current probability distribution. BIAS and SPREAD control the register and spread of the voicing.

**Smooth modulation source:** STEPS fully left turns X outputs into smooth random CV curves useful for filter cutoff, reverb amount, or any continuous parameter. Y output always provides a slow independent random CV regardless of STEPS position.

---

## Common Mistakes

### "DEJA VU at 12 o'clock locked a phrase I do not want"

When DEJA VU reaches 12 o'clock, Marbles locks whatever values are currently in the buffer into a repeating loop. If the locked phrase is not useful, turn DEJA VU away from 12 o'clock toward 11 o'clock and let the pattern evolve for several measures. New values enter the buffer over time. Then advance DEJA VU back to 12 o'clock when the phrase has drifted to something more useful.

The locked phrase content depends on what was playing immediately before the lock. To curate the locked phrase, dial DEJA VU to around 10-11 o'clock and wait until the output is producing something worth keeping, then lock it.

---

### "My X outputs are not making musical pitches"

STEPS controls how quantized the X outputs are. At left of center, X outputs produce smooth continuous curves useful for modulation but not for pitch. Moving STEPS right of center introduces quantization toward musical intervals. At far right, outputs only produce root notes and octaves.

If the X outputs sound atonal or chromatic rather than melodic, advance STEPS further right to increase quantization. The specific scale is determined by the STEPS position: center-right gives chromatic quantization, further right gives diatonic, far right gives root-octave only.

---

### "Nothing changes after I turn DEJA VU"

DEJA VU works on the buffer of recently generated values. If the module has just started running, the buffer may be sparsely populated. Patterns do not become obviously repetitive until the buffer has enough material in it, which takes several complete cycles at the current tempo.

Let Marbles run for at least 30-60 seconds at the current Rate before evaluating DEJA VU behavior. At slow tempos this takes longer; at fast tempos the buffer fills more quickly. Also verify whether the t button and X button next to DEJA VU are engaged: if neither is lit, DEJA VU has no active targets and produces no effect.

---

### "t1 and t2 and t3 all fire at the same time"

Algorithm mode controls the rhythmic relationship between the three t outputs. In green mode the outputs are relatively synchronous; in red mode they are maximally differentiated with complex polyrhythmic relationships. If all three seem to fire together, try switching to orange or red mode (hold the t button).

Also check SPREAD: at very low Spread settings the t outputs all tend toward the same density. Increase SPREAD for more varied rhythmic activity between the three outputs.

---

### "External clock is patched but RATE knob still seems to affect timing"

When an external clock is patched to the CLOCK input, the internal RATE is bypassed for timing purposes. The RATE knob then has no effect on tempo. If timing seems to be drifting, the issue is more likely that the external clock itself is unstable, or that the JITTER knob is set high enough to produce noticeable timing variation.

JITTER humanizes the timing by adding small random variations. At high JITTER settings these can be audible as a loose, swinging quality in the t outputs. Reduce JITTER if tighter timing is needed.

---

### "The Y output seems random but unrelated to X and t"

Y is generated by a different random process from the X and t sections and is not subject to DEJA VU in the same way. This independence is intentional: Y provides a bonus slow-random CV that evolves on its own trajectory regardless of the memory and pattern states of X and t.

If a correlated relationship between Y and the X outputs is needed, patch Y into the DEJA VU CV input. This creates a feedback relationship where Y's current value influences how much memory the X section uses, producing a loose correlation between Y and the pattern repetition state.

---

## Advanced Learning Path

1. **Start with X1 and t2 as a complete voice.** X1 to 1V/Oct, t2 to an envelope trigger, STEPS at 2 o'clock, DEJA VU at 11 o'clock. Spend time understanding these two controls before introducing others. The foundational Marbles skill is understanding how STEPS shapes the pitch output and how DEJA VU creates the tension between novelty and repetition.

2. **Work through the DEJA VU range in sequence.** From fully left (pure random) through 11 o'clock (evolving with memory tendency) through 12 o'clock (locked loop) to past 12 o'clock (shuffled). Listen to each position for at least a minute. Understand what "locked" means versus what "evolving" means, and hear the shuffle mode as distinct from both.

3. **Engage the t and X buttons independently.** Lock X DEJA VU while leaving t free. Listen to the result: melody repeats, rhythm continues evolving. Then reverse: free X, locked t. Rhythm repeats, melody continues evolving. This demonstrates the practical value of independent memory control over the two sections.

4. **Add BIAS and SPREAD as performance controls.** With a patch running and DEJA VU at 11 o'clock, adjust BIAS during playback and listen to the melodic register shift. Then adjust SPREAD and hear the pitch range contract and expand. Both controls are effective real-time performance gestures that change the character of the output without losing the pattern continuity.

5. **Try the Y → DEJA VU CV feedback patch.** Patch Y directly into the DEJA VU CV input with no other DEJA VU control active. Let the patch run for several minutes without intervention. The Y output will drift, pushing DEJA VU toward and away from the lock point, producing a pattern that cycles between evolving behavior and brief locked loops without manual control.

6. **Switch algorithm modes during a running patch.** Move from green to orange to red while listening to the t outputs. Green mode produces simpler, more metronomic gate patterns; red produces complex polyrhythmic relationships. The X outputs do not change with algorithm mode; only the t section is affected. This makes algorithm mode a pure rhythmic texture control that can be changed without affecting the pitch output.

7. **Use all three X outputs for a three-voice patch.** X1, X2, X3 each to a different oscillator's 1V/Oct, with t1, t2, t3 each to the corresponding envelope trigger. Listen to how the three X outputs are correlated but distinct: same probability parameters, different values. Then lock DEJA VU on X only and hear the three voices settle into a repeating chord pattern while timing continues to evolve.

---

## Pairs Well With

**DivKid Ochd:** Ochd LFOs patched to Marbles' RATE, SPREAD, and BIAS CV inputs create continuously drifting pattern character. The three parameters respond to independent LFO rates, producing complex evolution driven by Ochd's organic drift. Ochd trigger outputs can also provide an external clock source for Marbles.

**Make Noise Wogglebug:** Wogglebug Stepped output patched to Marbles BIAS CV shifts the melodic register from Wogglebug's own random process. Wogglebug Clock Out can provide external clock timing for Marbles. Running both simultaneously with shared timing but independent random sources produces two interacting but distinct probability streams.

**4ms RCD v2:** RCD division outputs used to clock Marbles' CLOCK input synchronize Marbles to a specific subdivision of the master tempo. RCD Out 3 (/3) produces a triplet-feel clock; Out 5 (/5) produces a complex relationship to the master. Marbles then generates its patterns at that subdivision rate.

**Quantizers:** When STEPS is at left-of-center positions, X outputs produce unquantized random CV. Patching through an external quantizer before reaching a pitch destination allows scale selection independent of STEPS position, which can be useful when STEPS is needed in a smooth position for a specific patch character but pitch quantization to a particular scale is still required.

**Cre8audio Function Junction:** Marbles t outputs used to gate Function Junction channels produce envelopes with random timing. Marbles X outputs into Function Junction CV inputs apply random voltage to modulation shaping. The combination creates rhythmically unpredictable envelopes with pitch-correlated modulation depths.

**Percussion modules:** The three t outputs driving three separate percussion voices in Red algorithm mode is a direct and effective use case. Marbles provides polyrhythmic gate timing without requiring a clock divider or logic module; the relationships between t1, t2, and t3 in Red mode are already complex.

---

*Visit [mutable-instruments.net](https://mutable-instruments.net/modules/marbles/) for complete documentation and open-source firmware*
