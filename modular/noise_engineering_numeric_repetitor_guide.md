---
title: Noise Engineering Numeric Repetitor
manufacturer: Noise Engineering
primary_role: CONTROLLER
secondary_roles: [MODULATOR]
form_factor: eurorack
functions: [sequencer, euclidean-generator]
behavior_tags: [stable, percussive, generative, stochastic, performance-oriented]
use_cases: [rhythmic pattern generator, euclidean rhythm source, polyrhythmic gate patterns]
hp: 8
historical_context: false
---

# Noise Engineering Numeric Repetitor

![Noise Engineering Numeric Repetitor](https://github.com/Shadoe-42/music/raw/main/modular/images/noise_engineering/numeric_repetitor/front_panel.jpg)
*Mathematical rhythm generator using prime number theory and binary arithmetic to create complex polyrhythmic patterns from 32 curated rhythms*

**The Mathematical Rhythm Generator**

---

## Quick Start: Get Your First Prime Rhythm in 5 Minutes

**What is Numeric Repetitor?** Think of it as a rhythm generator that uses mathematics rather than traditional step sequencing. It creates gate patterns based on binary arithmetic and prime number theory - but don't worry, you don't need to understand the math to use it! It contains 32 carefully curated "prime rhythms" that sound good, and generates variations by multiplying these patterns as binary numbers. It's perfect for creating complex polyrhythms with simple controls.

### Your First Mathematical Beat
1. **Connect your master clock** → **BEAT input**
2. **Connect PRIME output** → **kick drum or main percussion**
3. **Turn PRIME knob** slowly and listen to different rhythmic patterns
4. **Try the X/Y switch** to access the second set of 16 patterns
5. **Connect PRODUCT 1 output** → **second percussion voice**
6. **Turn PRODUCT 1 knob** to create rhythmic variations

**Congratulations!** You've just created polyrhythmic patterns using mathematical principles!

---

## Essential Parameters (The Mathematical Controls)

### **1. PRIME Pattern Selection**
- **PRIME knob:** Selects one of 16 core rhythmic patterns
- **X/Y switch:** Toggles between two sets of 16 patterns (32 total)
- **Prime rhythms:** Mathematically derived patterns that sound good
- **PRIME output:** The core rhythm - your foundational pattern
- **CV controllable:** Sequence through different prime patterns
- **16 per side:** X and Y each contain 16 different prime rhythms

### **2. PRODUCT Outputs - The Variations**
- **Three PRODUCT outputs:** Mathematically generated variations of the prime pattern
- **PRODUCT 1, 2, 3 knobs:** Control "factor offset" - how much variation from prime
- **Binary multiplication:** Prime pattern multiplied by factor creates variations
- **Time offset:** Product knobs control timing offset relative to prime
- **Related rhythms:** All products are mathematically related to the prime
- **CV controllable:** Each product can be modulated independently

### **3. Beat and Timing Controls**
- **BEAT input:** Master clock input - drives the entire system
- **MEASURE input:** Reset to beginning of measure for sync with other modules
- **RST button:** Manual reset and pause - hold to pause, release to reset
- **Clock-driven:** Requires external clock source to function
- **Rising edge:** Advances time on clock rising edge
- **Falling edge:** Returns gates to zero on clock falling edge

### **4. The Mathematical Engine**
- **Binary representation:** Rhythms stored as binary numbers
- **Prime number theory:** 32 patterns chosen using mathematical principles  
- **Heuristic filtering:** "Bad" rhythms removed through listening tests
- **Multiplication algorithm:** Prime × Factor = Product rhythm
- **Time offset calculation:** Mathematical delay creates polyrhythmic effects
- **You don't need to understand:** The math works behind the scenes

### **5. Visual Feedback System**
- **LEDs for each output:** Show when gates are active
- **Real-time visualization:** See the rhythmic relationships
- **Prime LED:** Shows the core pattern timing
- **Product LEDs:** Show variation timings relative to prime
- **Pattern recognition:** Visual aids help understand mathematical relationships

### **6. CV Integration**
- **Prime CV input:** Sequence through different core patterns
- **Product CV inputs:** Modulate the variation amounts/timing
- **7V CV range:** Full voltage range for complete pattern access
- **Real-time control:** Change patterns and variations during performance
- **Modulation friendly:** All parameters respond well to slow CV changes

---

## Why the Numeric Repetitor Excels

Most rhythm generators ask you to program patterns -- set which steps are active across a 16- or 32-step grid. The Numeric Repetitor takes a different approach: it generates rhythmic patterns from prime number mathematics, producing outputs that have specific, predictable mathematical relationships to each other. The result is polyrhythm that feels structured rather than arbitrary.

**Prime number division produces natural-sounding polyrhythm.** When you select a PRIME value, the module divides your clock by that prime number and generates output patterns based on its products. Because prime numbers share no common factors, patterns derived from different primes never synchronize at intermediate points -- they only align at the greatest common multiple, which for large primes can be extremely distant in time. This means Numeric Repetitor polyrhythms cycle slowly and feel continuously evolving rather than repetitive at short intervals.

**PRODUCT outputs generate variations on the same prime without additional programming.** The multiple PRODUCT outputs each apply different arithmetic relationships to the primary PRIME pattern, producing simultaneous related rhythms from one parameter selection. Changing the PRIME knob updates all outputs simultaneously, maintaining the mathematical relationships while shifting the entire rhythmic vocabulary. This makes pattern exploration extremely fast: one parameter change transforms everything coherently rather than requiring per-track reprogramming.

**CV control of PRIME enables live pattern morphing.** Applying CV to the PRIME input shifts the active prime number in real time. Because the module calculates patterns mathematically rather than from a stored sequence, the transition between prime values produces new rhythmic relationships immediately. Assigning a slow LFO, a stepped random source, or a manual CV to PRIME creates rhythmic evolution that is neither random nor mechanically repetitive -- it follows mathematical logic that produces musical results.

**X/Y switch doubles the available pattern vocabulary.** The X/Y switch toggles between two complete sets of patterns derived from the current PRIME setting. Each set has different arithmetic relationships applied. Adding this toggle to a live performance effectively gives two distinct groove settings accessible from a single switch press, with no parameter adjustment required.

---

## Patches

### Patch 1: Basic Polyrhythmic Drums

This patch establishes the fundamental Numeric Repetitor function: a clock enters, and four mathematically related trigger streams emerge.

```
[Master Clock] ──BEAT──▶ NUMERIC REPETITOR
                          PRIME Out ──▶ [Kick Drum]
                          PRODUCT 1 Out ──▶ [Snare]
                          PRODUCT 2 Out ──▶ [Hi-Hat]
                          PRODUCT 3 Out ──▶ [Perc]
```

**Setup:** Connect a master clock to BEAT. Route PRIME Out to a kick drum, PRODUCT 1 to a snare, PRODUCT 2 to a hi-hat, and PRODUCT 3 to a secondary percussion voice. Select prime pattern X1 from the display. Leave all Product knobs at noon initially.

**Controls:** Listen to all four outputs together. Slowly rotate PRODUCT 1 clockwise while the pattern plays and observe how the offset relationship between the snare trigger and the kick trigger changes. Return to noon and repeat with PRODUCT 2 and PRODUCT 3. Then switch to pattern X2 and listen to how the entire rhythmic structure shifts while the Product offsets maintain their relative behavior. Work through several X patterns to begin building familiarity with the pattern library.

**Result:** Four percussion voices with mathematically derived timing relationships. The PRIME output provides the stable rhythmic foundation; PRODUCT outputs derive from it with controllable offset and variation. Changing the prime pattern instantly reshapes the whole drum figure while preserving the internal logic between the voices.

---

### Patch 2: Sequenced Pattern Changes

This patch uses slow CV at the PRIME input to cycle through patterns automatically, producing rhythm evolution without manual intervention.

```
[Slow Sequencer] ──CV──▶ PRIME CV Input
[Master Clock] ──BEAT──▶ NUMERIC REPETITOR
                          All outputs ──▶ [Percussion voices]
```

**Setup:** Connect a 4-step or 8-step sequencer to the PRIME CV input. Set the sequencer speed to roughly 1/16 or 1/32 of the master clock so pattern changes occur every two to four bars rather than every beat. Run all four outputs to percussion modules.

**Controls:** Set the sequencer to advance through 4 to 6 different voltage levels and let the patch run. The prime pattern selection shifts automatically at each sequencer step, transforming the drum figure at regular musical intervals. The Product knob offsets remain constant throughout, so each new pattern inherits the same rhythmic character you dialed in with the knobs. Try setting the sequencer to random step order for a less predictable version of the same idea.

**Result:** Self-evolving drum patterns that change on a musical schedule. The pattern shifts feel composed because the Product offsets give every new prime pattern a consistent internal voice, even as the pattern itself changes.

---

### Patch 3: Techno Groove with MEASURE Sync

This patch configures Numeric Repetitor as a tight 16th-note groove source with bar-level reset to keep the pattern locked to song structure under live use.

```
[16th Clock] ──BEAT──▶ NUMERIC REPETITOR
[1-bar Clock] ──MEASURE──▶ NUMERIC REPETITOR
               PRIME Out ──▶ [Kick]
               PRODUCT 1 Out ──▶ [Closed Hi-Hat]
               PRODUCT 2 Out ──▶ [Open Hi-Hat]
               PRODUCT 3 Out ──▶ [Snare]
```

**Setup:** Run a 16th-note clock to BEAT and a 1-bar pulse to MEASURE. Connect the four outputs to kick, closed hi-hat, open hi-hat, and snare respectively. Select a pattern from the X bank.

**Controls:** With everything running, adjust PRODUCT 1 slightly clockwise for an off-beat hi-hat feel. Move PRODUCT 3 to find the snare position that creates the groove you want. The MEASURE input resets the pattern count on each bar, so anything you adjust with the Product knobs or pattern selector locks immediately back into bar-level alignment. During breaks, pull a Product knob fully counterclockwise to silence that voice; reintroduce it by returning the knob to the previous position.

**Result:** A locked, adjustable groove pattern that survives live performance interaction without drifting out of phase with the arrangement. The MEASURE input is the discipline mechanism; without it, any CV modulation or knob adjustment can compound into phase drift across bars.

---

### Patch 4: Generative Rhythm with Wogglebug

This patch uses Make Noise Wogglebug to supply semi-random CV to PRIME selection and a PRODUCT input, producing a drum pattern that never fully repeats while remaining internally coherent.

```
[Wogglebug STEPPED] ──CV──▶ PRIME CV Input
[Wogglebug WOGGLE] ──via attenuator──▶ PRODUCT 2 CV
[Master Clock] ──BEAT──▶ NUMERIC REPETITOR
[1-bar Clock] ──MEASURE──▶ NUMERIC REPETITOR
               All outputs ──▶ [Percussion voices]
```

**Setup:** Connect Wogglebug's Stepped output to PRIME CV and its Woggle output through an attenuator (set low initially) to PRODUCT 2 CV. Bring a steady 16th clock to BEAT and a 1-bar pulse to MEASURE.

**Controls:** Set the Wogglebug Rate to a slow position so prime pattern changes occur at a musical rate rather than erratically. The stepped random CV advances through different prime patterns, each one a coherent groove in itself. The Woggle CV on PRODUCT 2 adds a secondary layer of slight offset variation on the open hi-hat voice. Increase the attenuator level to widen the variation range on that voice; reduce it to keep the Woggle influence subtle. The MEASURE sync keeps everything anchored to bar boundaries even as the pattern content shifts.

**Result:** A drum pattern that never fully repeats but maintains mathematical internal consistency between all four voices. Each prime pattern the Wogglebug selects is a complete, logical groove; the randomness operates at the pattern selection level rather than the individual trigger level, which preserves musical coherence across the variation.

---

## Common Mistakes

### "My drum patterns keep drifting out of time with the rest of my system"

Numeric Repetitor calculates gate patterns from the prime rhythms and outputs them relative to the incoming clock, but it has no awareness of where it stands in the larger rhythmic cycle unless you tell it. Without a signal on the MEASURE input, the module starts its pattern from wherever it powered on or last reset, which may not align with your bar structure. In a live set or a complex patch, this drift becomes audible as patterns that are rhythmically correct but metrically displaced.

Connect a reset pulse to the MEASURE input at the start of each measure or bar. Most clock modules and sequencers output a dedicated end-of-cycle or bar-start signal: patch that to MEASURE and Numeric Repetitor will lock its internal pattern counter to your system's metric grid.

### "I turned the Product knob but the pattern barely changed"

The PRODUCT knobs control time offset, not pattern selection. Each PRODUCT output is a mathematically related variation of the current PRIME pattern, and the knob shifts when that variation occurs relative to the prime, not which variation plays. Small knob movements produce subtle polyrhythmic displacement; extreme movements shift the product further out of phase with the prime. The result is always a variation of the same prime: you cannot use a PRODUCT knob to access one of the other 31 prime patterns.

If you want a genuinely different pattern, change the PRIME knob or flip the X/Y switch. If you want variation on the current prime, the PRODUCT knobs are doing exactly what they are designed to do.

### "The CV input is jumping unpredictably between completely different patterns"

The PRIME CV input spans 0 to 7 volts to access all 16 patterns in the active bank. Because pattern selection is quantized (each pattern occupies a discrete voltage step), CV that changes faster than the ear can track produces rapid-fire pattern switching rather than smooth modulation. A 1Hz LFO swinging full range will cycle through multiple patterns per second.

Use slow CV: a long-period LFO, a manually adjusted sequencer, or attenuated random voltage. The most musical results come from CV that selects a new pattern every few bars rather than every few beats.

### "I explored everything in the first five minutes and it sounded repetitive"

Numeric Repetitor contains 32 prime patterns: 16 on the X bank and 16 on the Y bank. A common mistake is staying in one bank. The X/Y switch changes the entire rhythmic character of the module: X and Y banks have different mathematical relationships and produce patterns that feel distinct from each other. This effectively doubles the available vocabulary and is a primary performance tool.

Flip the X/Y switch while a pattern is running and listen to the difference. Then combine X-bank patterns with Y-bank patterns across different PRODUCT outputs by switching while noting the position you were in.

### "The pattern sounds boring when I listen to only the Prime output"

The Prime output alone is a single rhythmic pattern. The power of Numeric Repetitor is in the relationship between PRIME and multiple PRODUCT outputs heard simultaneously. Three Product outputs playing variations derived from the same prime create a polyrhythmic structure where the patterns are not independent: they share mathematical ancestry and therefore have natural resolution points.

Patch all four outputs (PRIME plus PRODUCTS 1, 2, and 3) to different percussion voices or sound sources simultaneously. Adjust the PRODUCT knobs to establish timing offsets that produce the rhythmic density you want. The full polyrhythmic texture is the point of the module, not the individual patterns in isolation.

---

## Advanced Learning Path

1. Spend dedicated time with every prime pattern in isolation. The X and Y banks each contain 16 patterns. Use a three-output drum kit and work through all 32 patterns at identical Product knob positions. Notice which patterns are sparse and which are dense, which are syncopated and which land on downbeats. Build a working internal map of the pattern library before adding any modulation. Pattern selection is only useful as a performance or compositional tool if you know what you are selecting between.

2. Understand Product knob behavior through systematic range sweeping. With one pattern playing and all four outputs routed to audible destinations, turn PRODUCT 1 slowly from fully counterclockwise to fully clockwise. Listen to the relationship between the PRIME output and PRODUCT 1 output across the full range. Repeat for PRODUCT 2 and PRODUCT 3. Each Product responds differently to the same knob position within any given prime pattern, because the offset is derived from the pattern mathematics, not independently of it. This dependency is the key to deliberate Product use rather than random knob turning.

3. Use the MEASURE input as a compositional discipline tool in every multi-module patch. Wire a 1-bar or 4-bar reset pulse to MEASURE whenever you are performing or recording. This keeps pattern counting locked to song structure even when CV modulation or live adjustments shift the pattern mid-bar. Generative patches without this anchor tend to drift out of phase with the arrangement, and that drift is only interesting if you chose it deliberately rather than discovered it by accident.

4. Explore cross-bank pattern pairing by building a patch where you can switch between an X pattern and a Y pattern in real time without adjusting any Product settings. Notice how the same Product offset values produce different rhythmic results with a different prime number underlying them. The X bank and Y bank have distinct mathematical characters that respond differently to the same knob positions, giving you two contrasting rhythmic personalities from a single set of offset settings.

5. Use individual PRODUCT outputs as real-time performance controls. In a live drum patch, assign one PRODUCT output to a secondary voice rather than the kick or snare. During a build or breakdown, pull that PRODUCT knob fully counterclockwise to silence that voice without stopping the pattern. Reintroduce it by returning the knob. This technique uses the offset mechanics as a mute control, allowing gradual drum builds and strip-downs using the module's native performance affordances rather than an external mixer.

6. Route a single PRIME output to multiple destinations simultaneously via a passive multiple or stackcable. Connect PRIME Out to both a kick drum trigger and an envelope generator that controls a filter cutoff. When the kick fires, the filter snaps open; the rhythmic relationship between the filter movement and the kick hit is mathematically locked because they share the same trigger source. This technique builds perceptual coherence across different synthesis layers from a single mathematical event, and it scales to any number of destinations.

---

## Pairs Well With

**DivKid Ochd** provides continuous, unquantized LFO signals into Numeric Repetitor's CV inputs, creating gradual pattern drift rather than abrupt jumps. A very slow Ochd LFO sweeping the PRIME CV input causes pattern changes to happen gradually as the voltage crosses pattern thresholds, producing a rhythm that evolves across several minutes rather than snapping between discrete states. Faster Ochd rates applied to PRODUCT CV inputs add subtle offset variation to individual voices without disrupting the overall prime pattern. With eight independent LFOs available, every CV input on the Numeric Repetitor can carry simultaneous unrelated modulation.

**Make Noise Wogglebug** is the most direct source of unpredictable-but-musical CV for prime pattern selection. The Stepped output produces quantized random voltages at clock-relative intervals; routing this to the PRIME CV input gives you pattern changes that happen rhythmically and land on different values each time. The Smooth output, applied to a PRODUCT CV input through an attenuator, adds continuous offset drift on one voice without erratic jumping. The Burst output can gate the MEASURE input for occasional forced resets, producing pattern-locking events at random intervals within an otherwise open arrangement.

**4ms RCD v2** turns a single clock into multiple clock divisions that can each serve as a BEAT input at different densities. Routing 8th notes to BEAT produces one rhythmic character; switching to 16ths doubles the density. With an RCD supplying selectable divisions, the same prime pattern produces distinctly different groove feels at different clock rates, and the switch between them is a single cable change or CV-controlled selection during performance.

**Mutable Instruments Marbles** applies pattern intelligence to prime selection. Marbles' X outputs produce musically coherent random voltages that follow internal harmonic relationships over time. When this drives the PRIME CV input, pattern selection follows a subtle musical logic rather than stepping randomly across the full range. Marbles' t outputs can supplement or replace the master clock with rhythmically varied timing pulses, adding a second layer of generative behavior to the already mathematical rhythm structure.

---

*Numeric Repetitor manual and algorithm documentation: [Noise Engineering](https://noiseengineering.us)*
