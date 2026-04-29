---
title: Qubit Bloom v1
manufacturer: Qubit
primary_role: CONTROLLER
secondary_roles: []
form_factor: eurorack
functions: [sequencer]
behavior_tags: [stable, generative, stochastic, evolving, performance-oriented]
use_cases: [generative melodic sequence, self-evolving patch element, probability-based variation]
hp: 16
memory: full
transport: receive
screen: true
historical_context: false
---

# Qu-Bit Bloom V1

**The Fractal Sequencing Garden**

![Qu-Bit Bloom V1](https://github.com/Shadoe-42/music/raw/main/modular/images/qubit/bloom_v1/front_panel.jpg)

---

## Quick Start: Get Your First Evolving Sequence in 5 Minutes

**What is Bloom?** Think of it as a sequencer that grows like a living tree. You plant a simple "trunk" sequence, and Bloom uses fractal algorithms to grow infinite "branches" - variations that are related but never quite the same. It's like having a composer that improvises endlessly on your musical ideas.

### Your First Growing Sequence
1. **Connect clock** → **CLOCK input** (or use internal tempo with RATE knob)
2. **Connect Channel A outputs** → **CV to oscillator V/OCT**, **GATE to envelope**
3. **Press CHANNEL button** until the Channel A LED lights up
4. **Turn LENGTH encoder** to set 8 steps
5. **Enter some notes** by turning NOTE encoder while pressing step buttons
6. **Turn BRANCH knob slowly** and watch your sequence evolve!

**Congratulations!** You've just planted your first musical tree and watched it grow branches!

---

## Essential Parameters (The Tree Growing Kit)

### **1. TRUNK Controls - Your Root Sequence**
- **LENGTH:** Sets how many steps in your base sequence (1-32 steps)
- **NOTE Encoder:** Programs the pitch for each step when editing
- **GATE Button:** Sets gate on/off for each step
- **Root Sequence:** Your fundamental musical idea that everything grows from

### **2. BRANCH Knob - The Magic Growth Control**
- **What it does:** Creates variations of your trunk sequence using fractal algorithms
- **Musical result:** Each branch position generates a complete new variation
- **Range:** Infinite positions = infinite sequence variations
- **Visual feedback:** RGB LEDs show which branch you're exploring

### **3. PATH Knob - Navigation Through the Tree**
- **What it does:** Determines how you move through all the generated branch sequences
- **Musical result:** Different paths create different ways of combining variations
- **Think of it as:** Choosing which route you take through the musical tree
- **Interaction:** Works with Branch to create complex sequence evolution

### **4. MUTATION Control - Controlled Chaos**
- **What it does:** Adds random variation to notes in the current sequence
- **0% (CCW):** Plays original notes exactly
- **100% (CW):** Complete random note selection
- **Musical result:** Introduces controlled randomness while maintaining structure
- **Pro tip:** Sweet spot around 25-40% for musical surprise without chaos

### **5. RATE Knob - Internal Tempo**
- **What it does:** Sets internal clock speed (5 seconds to 10ms per step)
- **Special feature:** At fully CCW position, automatically uses external clock
- **Musical result:** Complete tempo control from glacial to frantic
- **Performance tip:** Great for live tempo manipulation and smooth clock switching

### **6. PATTERN System - Memory Bank**
- **8 pattern slots:** Store and recall complete sequences
- **SHIFT + encoder:** Select pattern slot
- **SHIFT + click:** Load pattern
- **SHIFT + hold:** Save current sequence (3 seconds)
- **Visual:** LED pairs show selected pattern

---

## Why Bloom Excels

Most sequencers ask you to program notes explicitly -- place a pitch on step 1, another on step 2, and so on until you have a sequence you want to repeat. Bloom generates sequences by growing them from seed patterns using a tree algorithm, which means sequences evolve organically over time without requiring ongoing manual programming.

**The tree algorithm produces natural-sounding evolution.** Bloom's central metaphor is a growing tree: a seed pattern branches into variations according to mathematical rules, and playback traverses these branches according to the BRANCHES setting. The resulting sequences feel like they are developing and changing while maintaining a relationship to their origin. This is categorically different from manual step sequencing, random note generators, or simple transposition; it is generative progression with internal logic.

**BRANCHES controls how far from the seed the sequence wanders.** At low BRANCHES values, playback stays close to the seed pattern, producing a recognizable repeating sequence with small variations. At high values, playback reaches distant branches that are more loosely related to the original. This single parameter moves a sequence from "stable with subtle variation" to "continuously evolving" without changing any notes directly. Assigning CV to BRANCHES while a sequence is playing produces sequences that tighten and loosen their relationship to the seed in real time.

**Multiple channels share the same tree from independent branch positions.** Bloom's channels can each be set to a different branch position on the same tree, producing sequences that are related to each other but not identical. Channel A might play close-in branches while Channel B explores further out simultaneously. Because both derive from the same seed, the sequences complement each other harmonically even as they evolve independently.

**Sequences can be grown without stopping playback.** New nodes can be added to the tree while the sequence is running, and the growth integrates immediately into the evolving pattern. This means Bloom can be used as a live composition tool: grow the sequence forward in performance, not just before it.

---

## Patches

### Patch 1: Simple Evolving Melody

This patch uses Bloom's single-channel output to generate a melodic sequence that evolves continuously through the module's branching algorithm.

```
[Clock] ──CLOCK──▶ BLOOM V1
[Sequencer 8 steps] ──V/OCT──▶ [Oscillator V/OCT]
BLOOM CH A CV ──────────────▶ [Oscillator V/OCT]
BLOOM CH A GATE ────────────▶ [Envelope GATE]
```

**Setup:** Program an 8-note sequence into Bloom using the onboard encoder. Connect CH A CV output to an oscillator's V/OCT input and CH A GATE to an envelope generator. Connect the envelope output to a VCA. Set BRANCH at noon and PATH at noon.

**Controls:** Start the clock and listen to the base sequence. Slowly turn BRANCH clockwise from noon. As the branch value increases, the algorithm begins introducing variations on the sequence: some notes shift to adjacent positions within the fractal tree, while others remain anchored. At moderate BRANCH settings the melody remains recognizable with occasional departures; at high settings the departures become the norm and the original sequence is more of a seed than a literal content. Adjust PATH to change how the algorithm navigates through variation space; different PATH positions emphasize different types of departures from the base pattern.

**Result:** A single-voice melody that retains the harmonic logic of the original sequence while continuously evolving away from and returning to it. The algorithm produces variation that feels composed rather than random because it derives from the branch structure of the original sequence.

---

### Patch 2: Dual Channel Polyrhythm

This patch uses both Bloom channels at different sequence lengths to create evolving polyrhythmic counterpoint between two voices.

```
[Clock] ──CLOCK──▶ BLOOM V1
BLOOM CH A CV ──▶ [Oscillator 1 V/OCT]   (8-step sequence)
BLOOM CH A GATE ──▶ [Envelope 1 GATE]
BLOOM CH B CV ──▶ [Oscillator 2 V/OCT]   (5-step sequence)
BLOOM CH B GATE ──▶ [Envelope 2 GATE]
```

**Setup:** Program an 8-step sequence on CH A and a 5-step sequence on CH B. Tune the two oscillators a perfect fourth or fifth apart for harmonic relationship. Set both channels to the same BRANCH position initially; adjust PATH slightly differently per channel if available.

**Controls:** Run the clock and listen to the polyrhythmic interaction between the 8-step and 5-step sequences phasing in and out of alignment. The two channels run from the same clock but their different lengths create beat cycle lengths of 40 steps (8 × 5) before both realign. Increase BRANCH on both channels equally to introduce synchronized variation across the two voices. Try programming the two sequences to share a common root note or key center so their harmonic relationship remains coherent even as the variations diverge.

**Result:** A two-voice polyrhythmic texture where both voices evolve simultaneously through related variations. The shared clock and BRANCH setting keeps the two voices evolving in a coordinated manner, while the different lengths ensure they are always at different points in their respective sequences.

---

### Patch 3: Gate-Only Drum Pattern Evolution

This patch uses only the GATE outputs of both channels for percussive triggering with a slow LFO on the BRANCH input to produce drum patterns that evolve automatically.

```
[Clock] ──CLOCK──▶ BLOOM V1
[Slow LFO] ──CV──▶ BRANCH CV Input
BLOOM CH A GATE ──▶ [Kick / Primary Drum]
BLOOM CH B GATE ──▶ [Snare / Secondary Drum]
```

**Setup:** Set CH A to an 8-step pattern with kick-appropriate gate placement. Set CH B to a 5-step or 7-step pattern for the secondary percussion voice. Connect a slow LFO (one cycle per 8 to 16 bars) to the BRANCH CV input. Ignore the CV outputs of both channels for this patch.

**Controls:** As the LFO slowly sweeps the BRANCH value, the gate patterns evolve: some triggers appear, others disappear, and the rhythmic relationship between the two channels shifts. The LFO rate determines how quickly the pattern transforms; slower rates create the impression of a composed arrangement that changes gradually, while faster rates produce a pattern that seems to be exploring its own variation space. Try switching the LFO from a sine wave to a random stepped signal for less predictable pattern evolution.

**Result:** A self-evolving two-voice drum pattern that changes continuously without any manual intervention. The underlying branch structure ensures that even as the patterns change, they retain an internal logic, as variations are derived from the seed sequence rather than generated randomly.

---

### Patch 4: Generative Melodic Voice with Marbles

This patch uses Mutable Instruments Marbles to provide both timing and branch selection input to Bloom, creating a generative system where two modules share probabilistic control.

```
MARBLES t1 ──────────────▶ BLOOM CLOCK
MARBLES X1 ──via attenuator──▶ BLOOM BRANCH CV
BLOOM CH A CV ──────────▶ [Oscillator V/OCT]
BLOOM CH A GATE ────────▶ [Envelope GATE]
```

**Setup:** Connect Marbles t1 to Bloom's CLOCK input. Connect Marbles X1 through an attenuator (set to modest level) to the BRANCH CV input. Route CH A CV and GATE to an oscillator and envelope respectively. Set Bloom's BRANCH at noon and MUTATION at a low setting.

**Controls:** Marbles t1 provides rhythmically varied timing pulses rather than a steady metronome clock, which means Bloom's sequence timing is irregular in a musical way. The X1 voltage simultaneously varies the branch selection, so the pattern variation correlates with the timing variation. Adjust Marbles' DEJA VU toward repetition to anchor the melodic material to recognizable phrases; move it toward exploration to increase both timing and pitch variety. Adjust the attenuator on the BRANCH CV to control how much of the Marbles voltage range translates into branch variation.

**Result:** A melodic voice that changes in both timing and content according to Marbles' internal probability model. Because Marbles produces musically coherent variation rather than pure randomness, the result feels guided rather than stochastic, as though a musician is making deliberate choices about when and how to vary the phrase.

---

## Common Mistakes

### "I changed the BRANCH knob and everything paused for a second"

Bloom uses a fractal tree algorithm to generate sequence variations. When you move the BRANCH knob, the module recalculates the entire tree: all potential variations are computed before playback continues. This calculation takes a brief but audible moment, particularly with longer sequences or higher complexity settings. The pause and LED flicker are not a malfunction; they are the module doing the mathematical work that makes the fractal approach possible.

If this pause is disruptive in a performance context, treat BRANCH changes as compositional choices rather than real-time expressive controls. For live variation, assign CV to the BRANCH input and automate it: slow CV changes cause the tree to recalculate gradually rather than jumping to a distant branch position in one movement. Alternatively, use PATH for variation while leaving BRANCH stable; PATH changes how playback traverses the existing tree without triggering a full recalculation.

### "My branches wander too far from the original sequence"

BRANCHES controls how far from the trunk the playback position reaches: high values access distant branches that share less musical relationship with the seed. A common pattern is to program a sequence, turn BRANCHES toward maximum, and find the resulting variations unrecognizable. The fractal algorithm's distant branches are related by mathematics but may not be obviously related by ear.

Keep BRANCHES in the lower portion of its range until you understand the specific seed sequence you have programmed. Values in the first third of the range produce variations that are clearly recognizable as relatives of the trunk. Increase BRANCHES gradually from there and identify where the sweet spot is between variation and coherence for that particular sequence.

### "I changed the scale but my existing notes did not transpose"

Scale selection in Bloom V1 affects note quantization during entry and during MUTATION, not the pitches already stored in the sequence. Notes entered under one scale retain their stored values when you change scales: there is no retroactive transposition. This is particularly noticeable when MUTATION is involved: mutated notes will conform to the new scale while unmutated stored notes may not.

If you want to change the musical key or scale of an existing sequence, re-enter the notes under the new scale setting. Consider the scale as a constraint on new note generation rather than a property of the stored sequence.

### "Channel B is playing the same sequence as Channel A"

Bloom has two independent channels, each with its own sequence stored in memory. A common workflow issue is programming a sequence on Channel A, switching to Channel B to program a second sequence, and discovering that Channel B has its own separate trunk requiring independent programming. Alternatively, players sometimes program what they intend as Channel B content but forget to switch channels before entering notes, writing over Channel A instead.

Confirm the active channel before entering any notes by checking which channel LED is lit. Channel A and Channel B share the same fractal tree architecture, which means setting them to different BRANCH values produces two simultaneously evolving but harmonically related sequences.

### "MUTATION is adding notes that are not in the scale I selected"

MUTATION introduces controlled random variation into the sequence. In V1, the quantization behavior is not perfectly consistent across all MUTATION amounts: at higher values, notes can land outside the intended scale depending on how the random selection resolves against the available voltage steps.

Keep MUTATION below 50% for most applications. At 25 to 40%, you get recognizable variation without the boundary behaviors that appear at extreme settings. A downstream quantizer module will enforce scale compliance on anything that Bloom outputs, which is the most reliable solution to this behavior in V1.

---

## Advanced Learning Path

1. Work through the full BRANCH range methodically on a single programmed sequence before adding any modulation. Start with BRANCH fully counterclockwise and listen to the base sequence unmodified. Advance BRANCH slowly in small increments, pausing at each position to hear what the current branch selection sounds like. Note where the sequence first begins to vary, which notes are most stable, and which positions in the sequence are most affected by branching. Building this knowledge of your specific sequence's branch behavior is necessary before using BRANCH as a performance or modulation target.

2. Investigate the BRANCH and PATH interaction. BRANCH determines how far along the fractal tree the algorithm reaches; PATH determines the direction of travel through that tree. With BRANCH set to a moderate fixed value, sweep PATH from fully counterclockwise to fully clockwise slowly and listen to how the variations change character. Different PATH positions emphasize different types of melodic departures from the seed. This two-dimensional space is the core of Bloom's expressivity and repays extended exploration on every new sequence you program.

3. Understand how scale locking affects BRANCH behavior. When a scale is active, note variations are constrained to the selected scale degrees. With scale locking off, branch departures can land on chromatic notes outside the seed sequence's key. Program the same sequence with scale locking on and off, set BRANCH to the same moderate position, and compare the character of the variations. Scale locking produces variations that feel harmonically related to the original; without it, chromatic departures create more dissonant, adventurous departures. Neither is always correct; the choice depends on the harmonic context of the patch.

4. Explore the channel A and channel B relationship when running the same sequence on both channels at different BRANCH settings. With both channels playing the same 8-step sequence but CH A at BRANCH 3 o'clock and CH B at BRANCH 9 o'clock, you hear two different degrees of variation on the same underlying material simultaneously. The more heavily varied channel provides a countermelody to the less varied one. Adjusting BRANCH on one channel while the other holds steady produces the perceptual effect of one voice becoming more or less exploratory relative to its partner.

5. Program sequences that exploit the fractal branching rather than fighting it. Long, stepwise sequences with many adjacent semitones provide many closely related branches and produce smooth, continuously varying melodies. Sequences with large interval leaps produce more dramatic branch variations because adjacent branch positions are farther apart harmonically. Neither approach is better; the choice determines whether Bloom produces gentle evolution or more abrupt transformation. Understanding this relationship allows you to choose sequence design based on the kind of variation you want rather than accepting whatever the algorithm produces.

6. Use the BRANCH CV input with an envelope rather than only with a slow LFO. Triggering a short envelope into BRANCH CV on each note gate produces a rhythmically synchronized branch push: at the moment of each note, the branch value momentarily jumps before returning to the base setting. If the envelope is fast, the variation event is brief and the sequence snaps back to the base branch after each note. If the envelope is slow with a long release, successive notes accumulate branch distance before decaying back. This per-note branch envelope technique produces variation that is rhythmically coherent because it is triggered by the sequence's own gate output.

---

## Pairs Well With

**Mutable Instruments Marbles** addresses Bloom's two primary CV inputs from a single module: the t outputs supply clock and timing variation while the X outputs supply BRANCH and PATH modulation. Because Marbles produces internally correlated outputs rather than independent random voltages, the timing and variation control fed to Bloom share an underlying probabilistic relationship. The combined system produces generative material that feels guided by musical intention rather than statistical noise. Marbles' DEJA VU parameter offers global control over how repetitive or exploratory the shared output is, which translates directly into how much Bloom varies from its seed sequence.

**4ms RCD v2** provides multiple clock divisions from a single master clock, which allows Bloom's CLOCK input to be fed different rates during a performance. At a 16th-note clock rate, the sequence advances quickly and sounds melodic; at an 8th-note or quarter-note rate, the same sequence becomes slower and more legato, with BRANCH variations unfolding over longer timeframes. Switching Bloom's clock input between RCD divisions is a direct timbre-and-feel change that requires no reprogramming of the sequence.

**Make Noise Maths** supplies function generation for BRANCH CV modulation with precise control over attack and decay shapes. A Maths channel configured as a fast attack, long decay envelope triggered by Bloom's own gate output creates a self-modulating system: each note event pushes BRANCH momentarily toward higher variation and then returns to the base setting at the rate of the decay. Longer Maths decay times accumulate variation across multiple notes; shorter times produce per-note branch excursions that reset quickly. The logarithmic and linear curve options in Maths change the feel of the branch push and return.

**Noise Engineering Numeric Repetitor** creates a rhythmically related trigger layer that complements Bloom's melodic output. With Bloom providing the melodic sequence and Numeric Repetitor providing mathematically derived percussion triggers from the same master clock, both modules are operating from shared timing sources with different generative logic. Patching one of Numeric Repetitor's PRODUCT outputs into Bloom's BRANCH CV input creates a cross-module feedback where drum hits influence melodic variation, linking rhythmic and harmonic evolution into a single system.

---

*Bloom manual: [Qu-Bit Electronix](https://www.qubitelectronix.com)*
