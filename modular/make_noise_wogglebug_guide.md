---
title: Make Noise Wogglebug
manufacturer: Make Noise
primary_role: MODULATOR
secondary_roles: [SOURCE]
form_factor: eurorack
functions: [random-source, noise-source]
behavior_tags: [stochastic, evolving, noisy, chaotic, generative]
use_cases: [stochastic modulation, random CV generator, chaotic texture source]
hp: 10
transport: receive
historical_context: true
---

# Make Noise Wogglebug

**The Controlled Uncertainty Source**

![Make Noise Wogglebug](https://github.com/Shadoe-42/music/raw/main/modular/images/make_noise/wogglebug/front_panel.jpg)  
*Make Noise Wogglebug: Speed/Chaos, Ego/Id, Woggle controls, Disturb button, three CV outputs, three audio outputs*

---

## Historical Context

The Wogglebug's direct ancestor is the Buchla 265 Source of Uncertainty, a random voltage module that appeared in the Series 200 Electric Music Box beginning around 1970-71. Don Buchla (1937-2016) had first built an instrument for the San Francisco Tape Music Center in 1963 at the request of composers Ramon Sender and Morton Subotnick, who wanted a voltage-controlled instrument suited to the experimental music they were making. That first instrument became the Buchla 100 Series. The 200 Series expanded on it with more sophisticated modules, and the 265 formalized Buchla's approach to randomness: three functional sections providing continuously fluctuating random voltages (smooth, with rate and spread control), quantized stored random voltages (stepped, sample-and-hold), and a noise source. The design was explicit that these were not error sources to minimize but compositional materials to cultivate. Random voltage in the Buchla system was routed, shaped, and calibrated like pitch or amplitude: an instrument, not an artifact.

The San Francisco Tape Music Center where Buchla worked was embedded in the experimental music milieu that John Cage had helped establish in the 1950s. Cage's chance operations, using I Ching hexagrams to determine pitches, durations, and dynamics in works like "Music of Changes" (1951), had already reframed indeterminacy as a valid compositional strategy rather than a failure of control. Subotnick and Oliveros, both associated with the Center, carried that thinking into live electronic performance and composition. Buchla's 265 translated the philosophical position into hardware: voltage randomness was a musical parameter with its own identity, not a problem to be solved.

Grant Richter founded Wiard Synthesizers in Milwaukee in 1999 with a product line deeply indebted to Buchla's West Coast designs. His Wogglebug was conceived as a "mutant variation" on the 265, with the core random voltage architecture preserved but altered in two significant ways. First, Richter introduced the Woggle CV outputs: stepped voltage transitions that do not jump cleanly between values but instead carry a decaying sinusoidal edge at each step, a brief oscillation as the voltage settles. This softens the stepped output's edges and adds a characteristic movement that pure sample-and-hold lacks. Second, Richter tapped the internal oscillators that drive the random circuit and brought them to the panel as audio outputs, then ring-modulated them together into a third output. These oscillators are not independent of the CV section; they run at rates determined by the same clock that governs the random voltages, which means the audio and CV outputs are aspects of the same underlying process rather than parallel but separate functions.

Make Noise, founded by Tony Rolando in Asheville, North Carolina, licensed the Wogglebug design from Richter and adapted it for the Eurorack format. The architecture that Richter had developed remained intact, including the analog chaos circuitry rather than a digital implementation of randomness. This was deliberate. Richter's original circuit does not reproduce exactly from session to session; the coupled oscillators drift, the transitions vary, and the outputs carry a behavioral character that comes from the underlying analog processes rather than from a random number algorithm. The module's full name on early Make Noise panels reads "Make Noise Richter Wogglebug," preserving the attribution through the format change. The resulting lineage, from Cage's chance operations to Buchla's voltage randomness to Richter's mutant variation to Rolando's Eurorack adaptation, spans sixty years and two continents, but each step maintains the same foundational premise: unpredictability as a musical instrument, not a technical failure.

---

## Quick Start: First Randomness in 5 Minutes

1. **Set Speed/Chaos** to 12 o'clock
2. **Set Ego/Id** to 3 o'clock (toward full randomness)
3. **Patch Stepped Output** → oscillator 1V/Oct input
4. **Patch Smooth Output** → filter cutoff CV input
5. **Let the internal clock run.** Watch the system clock LED blink
6. **Pitch and filter now move independently** from different random voltages

**Add the Disturb button:**

1. **Press Disturb once:** observe a new random value appearing immediately
2. **Hold Disturb down:** the random values freeze at the current position
3. **Tap Disturb rhythmically:** inject a human timing element into the random process

**Hear the audio outputs:**

1. **Patch Smooth VCO** → a mixer channel
2. **Patch Ring-Mod** → a second mixer channel
3. **Adjust Speed/Chaos:** watch how both the CV behavior and audio character change together

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 10HP |
| Depth | 24mm |
| Power | +50mA / -40mA / 0mA |
| CV outputs | Stepped, Smooth, Woggle (0-10V) |
| Audio outputs | Smooth VCO, Woggle VCO, Ring-Mod (10Vpp) |
| Additional outputs | Clock Out, Burst Out |
| Clock range | ~1 cycle/minute to ~40Hz internal; ~200Hz with +8V CV |

---

## Essential Parameters

**Speed/Chaos** controls two things simultaneously: the rate at which the internal clock runs and the character of the randomness it generates. Turned counterclockwise, the module runs slowly and produces smooth, wandering random values. Turned clockwise, it runs faster but also becomes more jittery and erratic, approaching audio rate at the extreme end. This is not a tempo knob with a separate character control; the two are coupled. The Speed/Chaos CV input is internally normalled to +8V, which extends the range to approximately 200Hz when a cable is inserted and another voltage source overrides that normalling.

**Ego/Id** controls the probability distribution of the random values: how clustered or spread out they are across the output range. Fully counterclockwise (maximum Ego), values cluster together and the randomness is relatively predictable, staying near a central tendency. Fully clockwise (maximum Id), values spread across the full 0-10V range with maximum unpredictability. The Ego CV input allows this distribution to be modulated externally. Subtle voltages work more effectively here than full-swing signals; the input shifts probability distribution, not simple amplitude.

**Woggle** controls the rate at which the Woggle CV output tracks changes in the underlying random voltage. The Woggle output does not jump cleanly between values like Stepped does, nor does it lag smoothly like Smooth does; instead it follows each new value with a decaying sinusoidal transition, briefly oscillating before settling. The Woggle knob controls how fast that oscillation decays: counterclockwise for a fast settling time, clockwise for a slow one that makes the sinusoidal character pronounced. The result is a stepped-but-organic CV that produces pitch slides and filter sweeps with a distinctive character that neither Stepped nor Smooth can replicate.

**Disturb** functions as both a panel button and a panel jack. Pressing the button manually triggers a new sample from the S&H circuit, forcing a new random value regardless of where the internal clock is in its cycle. Patching a gate or trigger source to the Disturb jack provides the same function under CV control. Holding the button down freezes the current random value until released. This makes Disturb a real-time intervention point: any gate source (a percussion trigger, a sequencer pulse, a logic output) can interrupt the internal random process and force a new value at a specific moment.

---

## Wogglebug Output Reference

| Output | Type | Range | Character |
|--------|------|-------|-----------|
| Stepped | CV | 0-10V | Discrete jumps; classic sample-and-hold behavior |
| Smooth | CV | 0-10V | Lagged version of Stepped; smooth curves between values |
| Woggle CV | CV | 0-10V | Stepped with sinusoidal decay at each transition |
| Smooth VCO | Audio | 10Vpp | Shark's-fin waveform; frequency tracks all CV circuits |
| Woggle VCO | Audio | 10Vpp | Square wave following Woggle CV |
| Ring-Mod | Audio | 10Vpp | Ring modulation of both VCOs plus Influence input |
| Clock Out | Gate | 0-10V | Square wave from internal clock; continues with external clock |
| Burst Out | Gate | 0-10V | Random gates synchronized to the internal clock |

---

## Why This Instrument Excels

The Wogglebug provides three fundamentally different CV shapes from one random process, and that distinction matters more than just having "more outputs." Stepped is classic sample-and-hold: discrete jumps to new values at each clock tick. Smooth is the same underlying process lagged through a filter: it curves between values instead of jumping. Woggle is neither; it follows each new target value with a decaying sinusoidal oscillation, briefly ringing before it settles. These three outputs represent three different mathematical approaches to describing change over time. Patch all three to different destinations and each one produces a distinct musical result from the same source: the pitch jumps, the filter sweeps, and a third parameter (perhaps the resonance or an LFO rate) oscillates briefly each time the value shifts.

Speed/Chaos couples rate and character in a way that most modulation sources keep separate. An LFO that runs faster does not change its waveform shape. The Wogglebug's random character does shift as the clock rate changes: slow settings produce smooth, wandering behavior, while fast settings introduce jitter and erratic qualities that are qualitatively different from the same randomness at a slower rate. The practical result is that one knob handles both timing and character simultaneously. Turned slowly for ambient work, it breathes. Turned to audio rate, it becomes a different kind of modulation source entirely.

The three audio outputs (Smooth VCO, Woggle VCO, and Ring-Mod) are not independent oscillators running alongside the random circuit. They run at rates determined by the same clock that governs the CV outputs, which means the audio and CV behavior are aspects of the same process. Patch the Ring-Mod output to an audio mixer and the Stepped CV to a filter simultaneously: the filter cutoff is jumping at the same rate as the audio character is changing, because they share a source. This coherence is what makes Wogglebug useful as a complete voice rather than a modulation source that happens to have audio outputs on the side.

Disturb and Ego turn the module into something that can be integrated into a broader patch rather than running autonomously. Disturb accepts gates and triggers from any source, making it possible for a sequencer downbeat, a percussion trigger, or a logic gate to force a new random value at a specific musical moment. Ego accepts CV to modulate the probability distribution of the randomness itself, so a slow LFO can gradually shift the Wogglebug from clustered, predictable behavior to full-spread chaos and back. Neither input changes what the module fundamentally is; both make it responsive to the rest of the patch rather than isolated from it.

---

## Progressive Patch Examples

### Patch 1: Beginner - Basic Random CV

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Make Noise      │    │   Oscillator     │    │   Filter        │
│ Wogglebug       │    │                  │    │                 │
│                 │    │                  │    │                 │
│ Stepped ○───────┼────┼─▶ 1V/Oct         │    │                 │
│                 │    │                  │    │                 │
│ Smooth ○────────┼────┼──────────────────┼────┼─▶ Cutoff CV     │
│                 │    │                  │    │                 │
│                 │    │ Audio Out ○──────┼────┼─▶ Audio In      │
│                 │    │                  │    │                 │
│                 │    │                  │    │ Audio Out ○─────┼─── Output
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

| Connection | Signal | Purpose |
|------------|--------|---------|
| Stepped → 1V/Oct | [C] | Random pitch: discrete jumps between voltages |
| Smooth → Filter Cutoff | [C] | Random filter sweep: smooth curves between values |
| Oscillator Audio → Filter In | [A] | Signal path through pitch-randomized oscillator |

**Module settings:**
- Speed/Chaos: 12 o'clock (moderate rate)
- Ego/Id: 3 o'clock (toward full spread)
- Woggle: leave unpatched for this patch
- Disturb: leave unpatched for now

**Learning objectives:**
- Hear the difference between Stepped and Smooth from the same source: the pitch jumps while the filter sweeps, and both are driven by the same random process at the same rate
- Press Disturb manually during the patch to hear how it forces an immediate new random value outside the internal clock rhythm
- Hold Disturb down to freeze both the pitch and filter position simultaneously
- Turn Ego/Id fully counterclockwise: the pitch and filter movement becomes more clustered and predictable. Turn it clockwise: the values spread across the full range

**Enhancement:** Patch Woggle CV to a second oscillator's 1V/Oct. Now you have two oscillators moving to random pitches, but one jumps cleanly (Stepped) and one oscillates briefly before settling at each new pitch (Woggle). The difference between them is audible as a pitch character difference even though both come from the same underlying random voltage.

---

### Patch 2: Intermediate - Clocked Chaos with Disturb Control

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  Sequencer      │    │ Make Noise       │    │   Quantizer     │
│                 │    │ Wogglebug        │    │                 │
│ Clock Out ○─────┼────┼─▶ External Clock │    │                 │
│                 │    │                  │    │                 │
│ Gate Out ○──────┼────┼─▶ Disturb        │    │                 │
│                 │    │                  │    │                 │
│                 │    │ Stepped ○────────┼────┼─▶ CV In         │
│                 │    │                  │    │                 │
│ Slow LFO ○──────┼────┼─▶ Ego Input      │    │ CV Out ○────────┼─── 1V/Oct
│                 │    │                  │    │                 │
│                 │    │ Clock Out ○──────┼────┼─── Side-chain   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

| Connection | Signal | Purpose |
|------------|--------|---------|
| Sequencer Clock → External Clock | [G] | Lock Wogglebug sample rate to sequencer tempo |
| Sequencer Gate → Disturb | [G] | Sequence-triggered forced random values |
| Stepped → Quantizer CV In | [C] | Quantized random pitch in musical scale |
| Slow LFO → Ego Input | [C] | Gradual drift between clustered and spread randomness |
| Quantizer CV Out → 1V/Oct | [C] | Pitch output constrained to musical intervals |

**Module settings:**
- Speed/Chaos: 12 o'clock (internal clock still runs; external clock overrides sample rate)
- Ego/Id: 12 o'clock (slow LFO will sweep this)
- Disturb: patched to sequencer gate; forces new values on sequencer beats
- External Clock: patched to sequencer clock output

**Learning objectives:**
- External Clock synchronizes the sample-and-hold rate to the sequencer without stopping the internal oscillators; Clock Out continues even with external clock patched
- The sequencer gate into Disturb creates a second random-value event on each beat, adding a forced change on top of the clock-divided timing
- The quantizer imposes musical order on the random voltage; the pitch output stays in key even as the underlying voltage changes unpredictably
- The slow LFO on Ego drifts the module between predictable (clustered) and unpredictable (spread) behavior over a longer timescale than the individual clock events

**Enhancement:** Add Smooth CV to filter cutoff simultaneously. Now pitch (via quantizer) and filter both respond to the random process, but pitch is constrained to musical intervals while the filter sweeps continuously. The quantizer organizes one dimension of the randomness while leaving another free.

---

### Patch 3: Expert - Chaos Audio Synthesis

The three audio outputs (Smooth VCO, Woggle VCO, and Ring-Mod) run at rates set by the same clock that drives the CV outputs. This patch uses all three as an audio voice, with the CV outputs modulating processing parameters so the audio character and the modulation character evolve together.

```
┌─────────────────────┐         ┌──────────────────────┐
│  Make Noise         │         │  Audio Mixer         │
│  Wogglebug          │         │                      │
│                     │         │                      │
│ Smooth VCO ○────────┼─────────┼─▶ Ch 1               │
│                     │         │                      │
│ Woggle VCO ○────────┼─────────┼─▶ Ch 2               │
│                     │         │                      │
│ Ring-Mod ○──────────┼─────────┼─▶ Ch 3               │
│                     │         │                      │
│ Stepped ○───────────┼─────────┼─▶ Ch 1 Level CV      │
│                     │         │                      │
│ Smooth ○────────────┼─────────┼──────────────────────┼─── Filter Cutoff
│                     │         │                      │
│ Burst ○─────────────┼─────────┼─▶ Gate Out           │
│                     │         │                      │
│                     │         │ Mix Out ○────────────┼─▶ Influence In
└─────────────────────┘         └──────────────────────┘
```

| Connection | Signal | Result |
|------------|--------|--------|
| Smooth VCO → Ch 1 | [A] | Shark's-fin chaos oscillator; rate locked to random clock |
| Woggle VCO → Ch 2 | [A] | Square-wave chaos oscillator following Woggle CV |
| Ring-Mod → Ch 3 | [A] | Ring modulation of both VCOs; the most complex of the three |
| Stepped → Ch 1 Level CV | [C] | Random amplitude variation on the Smooth VCO channel |
| Smooth → Filter Cutoff (downstream) | [C] | CV modulation tracks audio character |
| Burst → Gate | [G] | Random gates for envelope triggering at random intervals |
| Mix Out → Influence In | [A] | Feedback: processed mix remodulates Woggle VCO frequency |

**Module settings:**
- Speed/Chaos: 1 o'clock (moderately fast for audio-rate interest)
- Ego/Id: 2 o'clock (slight spread, not maximum chaos)
- Woggle: 11 o'clock (moderate sinusoidal decay speed)
- Influence: mixer output fed back creates a feedback loop through the ring modulator

**Learning objectives:**
- All three audio outputs come from the same internal process, but their waveforms differ: the Smooth VCO produces a curved shark's-fin shape, the Woggle VCO produces a square wave, and the Ring-Mod produces their ring-modulated product
- The Stepped CV modulating Ch 1 level creates amplitude variation that is rhythmically related to the pitch variation, since both come from the same clock
- Feeding the mixer output back into Influence creates a feedback relationship: the ring modulator output affects the Woggle VCO frequency, which changes the ring modulator output
- The Burst output provides unpredictable gate timing for any envelope in the downstream signal path

---

### Patch 4: Advanced - Multi-Module Chaos Source

Wogglebug serves as the primary random voltage source for a network of other modules. Marbles uses Wogglebug's Clock Out as its timing reference, so both modules operate from the same underlying clock. Wogglebug's Stepped and Smooth outputs feed Marbles' spread and DEJA VU inputs, feeding its probability engine from the same chaos source that generates the base CV. Function Junction receives Woggle CV for modulation shaping and Burst for gate timing.

```
┌─────────────────────┐         ┌──────────────────────┐
│  Make Noise         │         │  Mutable Instruments │
│  Wogglebug          │         │  Marbles             │
│                     │         │                      │
│ Clock Out ○─────────┼─────────┼─▶ External Clock     │
│                     │         │                      │
│ Stepped ○───────────┼─────────┼─▶ Spread CV          │
│                     │         │                      │
│ Smooth ○────────────┼─────────┼─▶ DEJA VU CV         │
│                     │         │                      │
│                     │         │ X Out ○──────────────┼─── 1V/Oct
│                     │         │                      │
│                     │         │ t1 Out ○─────────────┼─▶ Disturb In
└─────────────────────┘         └──────────────────────┘

┌─────────────────────┐
│ Cre8audio           │
│ Function Junction   │
│                     │
│ Ch1 In ◀────────────┼─── Woggle CV (from Wogglebug)
│                     │
│ Gate In ◀───────────┼─── Burst Out (from Wogglebug)
│                     │
│ Ch1 Out ○───────────┼─── Filter Cutoff or LFO Rate
└─────────────────────┘
```

| Connection | Signal | Result |
|------------|--------|--------|
| Wogglebug Clock → Marbles Ext Clock | [G] | Both modules share the same timing source |
| Stepped → Marbles Spread | [C] | Random voltage controls Marbles' pitch spread range |
| Smooth → Marbles DEJA VU | [C] | Random voltage shifts Marbles' repetition tendency |
| Marbles t1 → Wogglebug Disturb | [G] | Marbles probabilistic gates force new random values |
| Woggle CV → Function Junction Ch1 | [C] | Sinusoidal-decay CV fed into envelope processing |
| Burst → Function Junction Gate | [G] | Random gates trigger envelope shaping |

**Module settings:**
- Wogglebug Speed/Chaos: 11 o'clock (moderate speed, stable enough for Marbles to track)
- Ego/Id: 2 o'clock (some spread but not maximum)
- Marbles: STEPS at 10 o'clock, DEJA VU at 12 o'clock (Wogglebug Smooth will push this)
- Function Junction: process Woggle CV into modulation shapes for filter or rate control

**Learning objectives:**
- Wogglebug and Marbles share a clock, so their outputs have a rhythmic relationship even though the pitch and gate outputs are independently random
- Marbles t1 feeding Disturb creates a feedback path: Marbles' probabilistic gate timing forces new random values in Wogglebug, which then affects the spread and DEJA VU inputs that modulate Marbles' behavior
- The Woggle CV into Function Junction demonstrates how the sinusoidal-decay character passes through envelope processing differently than Stepped or Smooth would
- Three different downstream musical functions (pitch via Marbles, modulation via Function Junction, gate timing via Burst) all derive from one Wogglebug

---

## Common Use Cases

**Random pitch sequences:** Stepped output into a quantizer produces melodic phrases that stay in scale while moving unpredictably between intervals. The clock rate sets the sequence density; Ego/Id sets how wide the pitch range spreads.

**Organic filter modulation:** Smooth output into filter cutoff produces sweeps that feel alive without being mechanical. Because the Smooth output curves between values rather than jumping, it avoids the stepped quality that makes many random voltage sources feel unmusical when applied to filter cutoff.

**Chaos audio synthesis:** The three audio outputs used as a voice: Smooth VCO and Woggle VCO mixed for timbre, Ring-Mod added for harmonic complexity, all three changing character together as Speed/Chaos changes.

**Random gate timing:** Burst output into an envelope generator creates events at unpredictable intervals. The density of bursts tracks the internal clock rate: faster Speed/Chaos produces denser burst activity.

**Performance intervention:** The Disturb button as a real-time tool during performance: pressing it forces pattern changes at will, holding it freezes the current state. Patching Disturb to a foot controller or performance CV source extends this to hands-free control.

**Woggle as pitch glide:** Woggle CV into an oscillator's 1V/Oct produces pitch changes that briefly oscillate before settling. At slow Woggle settings with a slow internal clock, each new pitch arrives with an audible overshoot and decay, a distinctive character that cannot be replicated with a standard portamento or pitch glide.

---

## Common Mistakes

### "The randomness sounds chaotic and unmusical"

Random voltage without constraint produces unpredictable results that may not respect musical expectations. Ego/Id at full clockwise gives maximum spread: pitches jump across the entire output range with no tendency toward any center. This is accurate to what the control does, but it may be too much spread for melodic use.

Turn Ego/Id counterclockwise to cluster the values toward a center. Patch Smooth to filter rather than Stepped to pitch: the curved transitions of Smooth feel more organic and less abrupt than discrete jumps. Add a quantizer on Stepped to constrain pitch to a scale. Use the External Clock input to lock the sample rate to your master tempo; freerunning Wogglebug at a rate unrelated to the song tempo adds another layer of rhythmic conflict that can compound the chaos.

---

### "Nothing is changing at slow Speed/Chaos settings"

At very slow settings, changes can take tens of seconds to occur. The system clock LED gives visual confirmation of the actual rate; watch it rather than listening for change. At settings below 9 o'clock, the time between samples may be longer than your attention span while monitoring.

Start around 11 o'clock and adjust from there. If the rate seems right visually but the audio is not changing, verify that the Stepped or Smooth outputs are actually patched to a destination that responds to slow CV: a VCA rather than a filter, for instance, may need larger voltage swings than the Ego/Id setting is providing.

---

### "My Woggle CV sounds the same as the Smooth output"

At fast clock rates or when monitoring quickly, the sinusoidal decay that distinguishes Woggle from Smooth is easy to miss. The difference is most audible when patched to pitch at a slow clock rate: each new pitch arrives with a brief oscillation before settling, producing a stepped-but-gliding effect. At fast rates, the oscillation is too rapid to hear as a discrete event.

To hear the difference: slow Speed/Chaos to 9-10 o'clock, patch Stepped to one oscillator's 1V/Oct and Woggle to a second oscillator's 1V/Oct simultaneously, then listen to how the two pitches change. Stepped jumps cleanly; Woggle oscillates before settling. Adjust the Woggle knob to control how fast it settles. At extreme clockwise settings, the oscillation is slow enough to be clearly audible as a pitch wobble at each new value.

---

### "Patching the Ego Input produces almost no effect"

The Ego Input shifts the probability distribution of random values, not the amplitude range. This means the change it produces is statistical rather than immediately dramatic: the distribution of values shifts toward clustering or spreading over time, not instantly. A single new sample may not show any clear change; the effect accumulates over multiple samples.

Use attenuated signals for Ego: a slow LFO at 20-30% of its original amplitude is more effective than a full-swing signal. Full-swing input can push the distribution to an extreme and hold it there, removing the useful range of variation. A 0-2V signal sweeping into Ego produces a more musically useful drift between clustering and spreading than a 0-10V signal that moves through the entire control range rapidly. Patch Stepped into a quantizer to pitch while slowly sweeping Ego: the pitch range graduallywidening or narrowing as the distribution shifts is the clearest way to hear what Ego is doing.

---

### "The audio outputs are overloading my mixer"

The audio outputs are 10Vpp, roughly twice the amplitude of a typical Eurorack oscillator. They will clip any input that expects standard ±5V audio levels without attenuation. Use a mixer channel with attenuation, or patch through a VCA or attenuator before the mixer.

The high level is also deliberately useful for overdriving filters: feeding a Wogglebug audio output directly into a filter input at high levels produces saturation and harmonic content that is a feature, not a problem. Treat the output level as a parameter to set intentionally rather than a defect to correct.

---

### "The Disturb input does not seem to trigger"

The Disturb jack requires a gate or trigger signal that rises above approximately 2.5V. Low-level signals, audio, or CV below that threshold will not reliably trigger it. Use a gate or trigger from a sequencer, clock, or envelope output that reaches 5V or higher.

If patching Disturb to a trigger source that works at the correct voltage and still seeing no response, verify the connection is to the Disturb jack and not the Ego jack; the two are adjacent on the panel and easy to misidentify.

---

## Advanced Learning Path

1. **Begin with Stepped and Smooth into separate destinations.** Run the two CV outputs to pitch and filter simultaneously and spend time with Ego/Id across its full range. The foundational Wogglebug skill is understanding how these two outputs differ from each other and what Ego/Id does to both of them. Rotation around the clock rate and distribution controls, listening carefully at each position, builds the intuition that makes later patches work.

2. **Add Woggle CV to a third destination and learn what distinguishes it.** Pitch modulation at a slow clock rate is the clearest demonstration. Once the sinusoidal decay is audible at a slow rate, increase Speed/Chaos and listen for where the decay becomes too fast to hear as a discrete event. This calibrates the Speed/Chaos range where Woggle's character is most useful.

3. **Patch an external clock source and note the difference.** When the External Clock jack receives a signal, the sample rate locks to that clock, but the internal oscillators continue running. Clock Out remains active. Understanding this distinction, that external clock controls when samples are taken rather than stopping the internal process, clarifies what the module's different subsystems do independently.

4. **Explore Disturb as a performance tool before patching it.** Use the manual button during a simple pitch-plus-filter patch and develop a feel for how it interrupts the clock rhythm. Then patch a gate source to the Disturb jack and compare: the gate source forces new values at its own timing, overlaid on the internal clock's rhythm. Both the internal clock and the Disturb input are sampling the random circuit, producing two independent streams of random events from one source.

5. **Use the audio outputs as a voice and compare them to the CV behavior.** The audio and CV outputs come from the same process and change character together as Speed/Chaos changes. Hear this connection directly by monitoring audio while watching or patching the CV outputs. The coherence between the audio voice and the CV behavior is what makes Wogglebug useful as a unified chaos source rather than as a CV module that happens to have audio outputs.

6. **Integrate with a quantizer for melodic randomness.** Stepped into a quantizer into a pitch destination is the standard musical use of sample-and-hold randomness. After understanding the basic version, explore how Ego/Id affects the melodic output through the quantizer: at clustered settings, the melody stays near a central pitch; at spread settings, it ranges across the full scale. The quantizer constrains the randomness to a key without eliminating the variation.

7. **Route Burst to an envelope generator and listen to the rhythmic result.** Burst produces gates at the internal clock rate but not on every tick; the density varies with clock rate and internal state. Using Burst for envelope triggering produces events at unpredictable intervals, a complement to the CV randomness that extends uncertainty into timing rather than only into parameter values.

---

## Pairs Well With

**Quantizers:** A pitch quantizer on Stepped output is the standard tool for turning random voltage into melodic content that stays in scale. The quantizer imposes musical order on the chaos without eliminating the variation. This pairing appears throughout Eurorack and is the foundational application of sample-and-hold randomness.

**Mutable Instruments Marbles:** Marbles has its own random CV and gate generation, and it can take Wogglebug's Clock Out as an external timing reference. The two modules complement each other: Wogglebug generates raw chaos; Marbles applies probability weighting and DEJA VU repetition tendency to its own outputs using Wogglebug's CV as a modulation source. Running them from a shared clock lets both modules operate in rhythmic relationship.

**DivKid Ochd:** Ochd's eight LFO outputs provide slow, organic modulation sources for Ego and Speed. Patching a slow Ochd LFO to Ego gradually drifts the Wogglebug's distribution between clustered and spread behavior over timescales longer than the individual random events. Patching a second Ochd LFO to Speed/Chaos similarly shifts rate and character over time, so the module's overall behavior changes slowly while its short-term randomness continues.

**Cre8audio Function Junction:** Woggle CV and Burst output both benefit from Function Junction processing. Woggle CV fed into an envelope-follower or attenuator chain produces shaped modulation from the sinusoidal-decay character. Burst output triggering a Function Junction ADSR gate creates shaped envelopes at random timing intervals. Either use case extends the Wogglebug's CV outputs into processed modulation shapes.

**4ms RCD v2:** RCD divisions can clock the Wogglebug via External Clock or trigger Disturb from specific division outputs. Clocking Wogglebug from RCD Out 3 or Out 5 synchronizes sample timing to non-binary rhythmic divisions, creating random values that arrive at a rhythmically structured rather than free-running rate.

**Filters:** Smooth output into filter cutoff is the most common single-destination patch for Wogglebug. The curved transitions of Smooth feel natural on a filter and avoid the stepped quality that can make random CV sources sound mechanical. The audio outputs are also high enough in level to overdrive filter inputs intentionally, adding saturation and harmonic content as a separate use case.

---

*Visit [makenoisemusic.com](https://www.makenoisemusic.com/modules/wogglebug) for full documentation. Original Wiard Wogglebug design by Grant Richter.*
