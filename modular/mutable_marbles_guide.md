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
---

# Mutable Instruments Marbles - Beginner's Guide

![Mutable Instruments Marbles](https://github.com/Shadoe-42/music/raw/main/modular/images/mutable_instruments/marbles/front_panel.jpg)  
*Intelligent chaos generator with musical memory: algorithmic pattern generation using probability distributions, DEJA VU memory system, and sophisticated randomness for musical sequences*


## Quick Start: Get Your First Random Sequence in 5 Minutes

**What is Marbles?** Think of it as a sophisticated pattern generator that creates musical randomness with memory. It generates random rhythms and melodies, but with algorithmic intelligence - it can repeat patterns you like, avoid repeating patterns too much, and gradually evolve based on probability distributions. It's controlled randomness with musical sophistication.

### Your First Random Pattern
1. **Connect Marbles X1 output** → **Oscillator 1V/OCT input**
2. **Connect Marbles t2 output** → **Envelope generator TRIGGER input**
3. **Set RATE knob** to around 12 o'clock (120 BPM)
4. **Turn STEPS knob** clockwise to 2 o'clock (quantized to scales)
5. **Play with DEJA VU knob** - turn right to create repeating loops

**Congratulations!** You've just created an evolving random melody that can lock into memorable patterns!

---

## Essential Parameters (The Big 6)

### **1. RATE Knob (Master Clock)**
- **What it does:** Sets the master tempo for everything (internal clock)
- **Musical result:** 120 BPM at 12 o'clock - your main pulse
- **Range:** Super slow to very fast - covers all musical tempos
- **Pro tip:** Has V/Oct input - you can sequence the tempo changes!

### **2. DEJA VU Knob (The Memory)**
- **What it does:** Controls how much the module remembers and repeats
- **Left (7-12 o'clock):** Random to perfect loops  
- **Right (12-5 o'clock):** Perfect loops to shuffled variations
- **Sweet spot:** 11 o'clock for slowly evolving patterns
- **Magic moment:** At 12 o'clock exactly = perfect locked loop

### **3. STEPS Knob (Musical Shape)**
- **What it does:** Controls how "musical" the random voltages sound
- **Left of center:** Smooth, flowing random curves (great for modulation)
- **Center:** Traditional stepped random voltages
- **Right of center:** Progressively quantized to musical scales
- **Far right:** Only root notes and octaves (very musical)

### **4. SPREAD Knob (Voltage Distribution)**
- **What it does:** Controls how the random voltages are distributed
- **Far left:** Constant voltage (no randomness)
- **12 o'clock:** Bell curve distribution (most notes near center)
- **2 o'clock:** Equal probability across full range
- **Far right:** Only minimum and maximum values (random gates!)

### **5. BIAS Knob (High/Low Preference)**
- **What it does:** Skews random voltages toward high or low values
- **Left:** Prefers low voltages (bass notes if controlling pitch)
- **Center:** No preference (balanced)
- **Right:** Prefers high voltages (treble notes if controlling pitch)

### **6. t/X Section Buttons (DEJA VU targets)**
- **What they do:** Choose which parts are affected by DEJA VU memory
- **t button:** Rhythm memory (timing patterns repeat/evolve)
- **X button:** Voltage memory (melodies repeat/evolve)
- **Both/neither:** Different combinations create different behaviors


---

## Why Mutable Instruments Marbles Excels

### **The Philosophy:**
Marbles represents a revolutionary approach to musical randomness - **sophisticated algorithms applied to music creation**. Unlike pure random generators, Marbles uses probability distributions and memory systems to create patterns that sound musical, but **you are still the creative director**. The module responds to your input and settings to create the musical results you guide it toward.

### **Perfect For:**
- **Electronic producers** seeking intelligent, evolving sequences that never get boring
- **Ambient musicians** creating long-form generative compositions with slow development
- **Live performers** who want an AI collaborator that responds to musical context
- **Experimental composers** exploring machine learning in musical composition
- **Advanced system builders** creating multi-module pattern generation ecosystems

### **The Learning Experience:**
Using Marbles teaches you about your own musical preferences by showing you patterns in new ways. As you adjust the DEJA VU and other parameters, you discover which probability distributions and pattern repetitions appeal to you musically. **You guide the system** - it doesn't learn independently, but responds to your creative direction. It's a sophisticated tool for musical exploration.


---

## Historical Context

Iannis Xenakis coined the term "stochastic music" in the 1950s, drawing on the Greek word for "aimed-at." Where John Cage used chance operations to remove the composer's intentions from the work, Xenakis used probability distributions to model processes that have natural structure: the way individual particles in a gas behave randomly but produce predictable aggregate behavior, the way rain sounds irregular in detail but consistent in character. The distinction matters. Pure randomness produces sequences that feel arbitrary; probability-weighted randomness produces sequences that feel like they belong to a world with internal rules. Xenakis was arguing that mathematics could formalize the second kind and use it compositionally.

The problem that followed composers into modular synthesis was practical. Random voltage generators produced values that were too statistically flat to be musically useful without significant patching overhead. Earlier modules had addressed part of this by giving performers control over probability distributions, but the question of repetition remained open. Human performers, even when improvising freely, naturally produce local repetition: a phrase slightly varied, a rhythm returned to, a pitch revisited. Pure random generators produce none of this unless explicitly patched to store and recall values, which typically required external sequencers and logic.

Émilie Gillet founded Mutable Instruments in 2011, building a catalog of modules whose designs engaged compositional and philosophical questions as directly as technical ones. The open-source publication of all circuit schematics and firmware was not incidental; it reflected a conviction that instruments should be understood by the people who use them. Marbles, released in 2018, was Gillet's direct answer to the repetition problem. Its DEJA VU system works by maintaining a buffer of recently generated values and, at each decision point, probabilistically choosing between drawing a new value from the hardware random source or recycling a value from the buffer. The result is not a memorized pattern; it is a probability-weighted tendency toward recent material. At one extreme the output is genuinely random; at the other it is a locked loop; across the middle range it produces the kind of evolving-but-familiar sequences that human performers generate through habit and musical preference.

Mutable Instruments closed in 2022. Gillet open-sourced all remaining designs before the company ended, and Marbles has since been cloned, ported to VCV Rack, and incorporated into other instruments. The DEJA VU architecture is now a reference point for how to make randomness compositionally useful rather than merely statistically present.

---

## Progressive Patch Examples

### **Patch 1: First Steps - Musical Random Melodies**
```
                    ┌─────────────────────┐
                    │    Mutable Marbles  │
                    │                     │
     Master Clock──▶│ RATE    ┌─────────┐ │
                    │  ●      │ DEJA VU │ │
                    │         │   ●     │ │
                    │ STEPS   │ SPREAD  │ │
                    │   ●     │   ●     │ │
                    │         └─────────┘ │
                    │                     │
                    │ X1 ○────────────────┼─── [C]
                    │    ║                │     ║
                    │ t2 ○────────────────┼─── [G]
                    │    ║                │     ║
                    └────║────────────────┘     ▼
                         ▼                ┌──────────────┐
                    ┌─────────────┐       │  Oscillator  │
                    │  Envelope   │       │              │
                    │ Generator   │       │ 1V/Oct    ◀─┼─── From X1
                    │             │       │              │
                    │ Trigger  ◀──┼───────┼─ Audio Out ○ │
                    │             │       │              │
                    │ Output   ○  │       └────┬─────────┘
                    └────┬────────┘            ║ [A]
                         ║ [C]           ▼
                         ▼                ┌─────────────┐
                    ┌─────────────┐       │     VCA     │
                    │     VCA     │       │             │
                    │             │       │ Audio In ◀──┼─── From Oscillator
                    │ CV Input ◀──┼───────┼─             │
                    │             │       │ Audio Out○──┼─── Final Output
                    │ Audio Out○──┼───────┼─             │
                    └─────────────┘       └─────────────┘
```

| Connection | Cable Type | Purpose | Learning Objective |
|------------|------------|---------|-------------------|
| Marbles X1 → Oscillator 1V/Oct | [C] | **Random pitch control** | **Creates evolving melodies** |
| Marbles t2 → Envelope Trigger | [G] | **Rhythmic triggering** | **Main beat with variations** |
| Oscillator Audio → VCA Audio | [A] | **Signal path** | **Complete voice chain** |
| Envelope Out → VCA CV | [C] | **Amplitude shaping** | **Musical note envelopes** |

**Module Settings:**
- **Marbles RATE:** 12 o'clock (120 BPM)
- **Marbles STEPS:** 2 o'clock (musical quantization)
- **Marbles DEJA VU:** 11 o'clock (slow evolution)
- **Marbles SPREAD:** 12 o'clock (balanced distribution)

**Learning Objectives:**
- Experience sophisticated algorithmic randomness vs. pure chaos
- Understand DEJA VU memory and pattern repetition system
- Learn musical quantization with STEPS
- Discover how patterns evolve through probability manipulation

**Visual Feedback:**
- **t2 LED:** Flashes with main rhythmic pulse
- **X1 voltage display:** Shows pitch changes in real-time
- **DEJA VU influence:** Watch patterns slowly lock and evolve
- **Result:** Musical sequences that find memorable phrases and develop them

**Alternative Options:**
- **Instead of Marbles:** Try **Make Noise Wogglebug** for different chaos generation, or **Intellijel Metropolix** for structured sequence generation
- **Different randomness:** **Ornament & Crime** Turing Machine for binary pattern evolution, or **Music Thing Turing Machine** for classic shift register patterns
- **Budget approach:** **2HP Arp + Rnd** for basic random sequence generation

**Enhanced Alternative Options:**
- **Budget:** 2HP Arp + 2HP Rnd + Doepfer A-111-4 Quad VCO for basic random sequence generation
- **Different character:** Make Noise Wogglebug + Intellijel Metropolix for chaos + structured pattern combination
- **Premium:** Multiple Marbles + Ornament & Crime + comprehensive algorithmic pattern ecosystem

### **Patch 2: Intermediate - Advanced Integration with Ochd**
```
   ┌─────────────────────┐      ┌─────────────────────┐
   │   DivKid Ochd      │      │    Mutable Marbles  │
   │   (Advanced)       │      │    (Advanced)       │
   │                    │      │                     │
   │ LFO 1 ○────────────┼──────┼─▶ RATE CV           │
   │       ║            │      │                     │
   │ LFO 3 ○────────────┼──────┼─▶ SPREAD CV         │
   │       ║            │      │                     │
   │ LFO 7 ○────────────┼──────┼─▶ BIAS CV           │
   │       ║            │      │                     │
   │       ║            │      │ X1 ○────────────────┼─── [C]
   │       ║            │      │ X2 ○────────────────┼─── [C]
   │       ║            │      │ t1 ○────────────────┼─── [G]
   │       ║            │      │ Y  ○────────────────┼─── [C]
   └───────║────────────┘      └─────────────────────┘
           ║                           ║      ║    ║    ║
   [C]║                   [C]║      ║    ║    ║
           ▼                           ║      ║    ║    ║
   ┌─────────────┐                    ▼      ▼    ▼    ▼
   │   Filter    │           ┌──────────────────────────┐
   │             │           │    Complex Oscillator    │
   │ Cutoff CV◀──┼───────────┼─ 1V/Oct    ◀─ X1 Output │
   │             │           │ FM Index   ◀─ X2 Output │
   │ Audio In ◀──┼───────────┼─ Sync       ◀─ t1 Output│
   │             │           │ Timbre     ◀─ Y Output  │
   │ Audio Out○──┼───────────┼─                        │
   └─────────────┘           │ Audio Out ○─────────────┼─── Final Output
                             └──────────────────────────┘
```

| Module | Parameter | Source | Purpose | Phase 2 Integration |
|--------|-----------|--------|---------|-------------------|
| **Marbles** | Rate CV | Ochd LFO 1 | **Organic tempo variations** | **Breathing algorithmic rhythm** |
| **Marbles** | Spread CV | Ochd LFO 3 | **Evolving voltage distribution** | **Organic pattern character** |
| **Marbles** | Bias CV | Ochd LFO 7 | **Shifting high/low preference** | **Organic tonal movement** |
| **Oscillator** | 1V/Oct | Marbles X1 | **Algorithmically-controlled pitch** | **Musical pattern generation** |
| **Filter** | Cutoff CV | Ochd LFO 1 | **Organic filter movement** | **Breathing spectral evolution** |

**Module Settings:**
- **Ochd:** All LFOs at different rates for complex organic modulation
- **Marbles STEPS:** 2 o'clock (musical quantization for harmonic content)
- **Marbles DEJA VU:** 10 o'clock (slow learning with organic influences)

**Learning Objectives:**
- **Advanced module integration:** Ochd and Marbles working together
- **Organic AI music:** Combining breathing modulation with learning intelligence
- **Multi-parameter modulation:** Multiple CV sources controlling different aspects
- **System-level thinking:** How modules enhance each other's capabilities

**Alternative Options:**
- **Instead of Ochd:** Try **Batumi** for geometric LFO modulation, or **Quadrax** for discrete envelope control of Marbles parameters
- **Different modulation:** **Make Noise Maths** for mathematical functions affecting pattern generation, or **Befaco Rampage** for dual modulation sources
- **Budget approach:** **2HP LFO x3** for basic multi-parameter modulation of Marbles

**Enhanced Alternative Options:**
- **Budget:** 2HP LFO x3 + basic oscillator + envelope for simple modulated pattern generation
- **Different character:** Batumi + Quadrax + Make Noise DPO for geometric modulation + discrete pattern control
- **Premium:** Multiple Marbles + comprehensive LFO ecosystem + advanced pattern modulation workstation

### **Patch 3: Advanced - Polyrhythmic Percussion Network**
```
                    ┌─────────────────────┐
                    │    Mutable Marbles  │
                    │                     │
     Clock Source──▶│ RATE    ┌─────────┐ │
                    │  ●      │ BIAS ●  │ │
                    │         │ JITTER ●│ │
                    │ STEPS   │ SPREAD  │ │
                    │   ●     │   ●     │ │
                    │         └─────────┘ │
                    │ Algorithm: Red      │
                    │                     │
                    │ t1 ○─────────────────┼─── [G]
                    │ t2 ○─────────────────┼─── [G]
                    │ t3 ○─────────────────┼─── [G]
                    │ Y  ○─────────────────┼─── [C]
                    │    ╚══════════════╗  │      ║
                    │        DEJA VU CV◀┼──┼──────╚═══ Self-Modulation
                    └─────────────────────┘
                             ║      ║      ║
                   Gate       ▼      ▼      ▼    
                (Yellow) ┌─────────┐ ┌─────┐ ┌─────────┐ 
                        │  Kick   │ │Snare│ │ Hi-hat  │
                        │  Drum   │ │Drum │ │  Drum   │
                        │         │ │     │ │         │
                        │Trig  ◀──┼─│Trig◀┼─│Trig  ◀─ │
                        │         │ │     │ │         │
                        │Audio ○  │ │Audio│ │Audio ○  │
                        └────┬────┘ └──┬──┘ └────┬────┘
                             ║         ║         ║
                        Audio║    Audio║    Audio║
                        (Red)║   (Red) ║   (Red) ║
                             ▼         ▼         ▼
                            ┌───────────────────────┐
                            │       Mixer           │
                            │ Ch1 ◀─────────────────┼─── Kick
                            │ Ch2 ◀─────────────────┼─── Snare
                            │ Ch3 ◀─────────────────┼─── Hi-hat
                            │ Mix Out ○─────────────┼─── Final Drum Mix
                            └───────────────────────┘
```

| Connection | Cable Type | Purpose | Musical Function |
|------------|------------|---------|-----------------|
| Marbles t1 → Kick Trigger | [G] | **Main beat generator** | **Foundational rhythm** |
| Marbles t2 → Snare Trigger | [G] | **Secondary rhythm** | **Syncopated patterns** |
| Marbles t3 → Hihat Trigger | [G] | **Tertiary rhythm** | **Complex polyrhythms** |
| Marbles Y → Marbles DEJA VU CV | [C] | **Self-modulation** | **Evolving memory patterns** |

**Module Settings:**
- **Marbles Algorithm:** Red mode (complex polyrhythms)
- **Marbles BIAS:** 2 o'clock (denser rhythms)
- **Marbles JITTER:** 10 o'clock (subtle humanization)
- **Marbles DEJA VU:** Controlled by Y output (self-evolving)

**Learning Objectives:**
- Master multiple trigger outputs simultaneously
- Understand rhythm algorithm modes
- Experience polyrhythmic relationships
- Learn self-modulation techniques

**Alternative Options:**
- **Instead of Marbles:** Try **4ms RCD v2** for mathematical polyrhythmic division, or **Pamela's NEW Workout** for comprehensive pattern generation
- **Different drums:** **Erica Synths Drum modules** for analog percussion, or **sample-based drum modules** for different sonic character
- **Budget approach:** **Doepfer A-160-2** Clock Divider + basic drum triggers for simple polyrhythmic patterns

**Enhanced Alternative Options:**
- **Budget:** Doepfer A-160-2 + basic drum triggers + simple mixer for polyrhythmic percussion system
- **Different character:** 4ms RCD v2 + Erica Synths Drums + comprehensive percussion ecosystem
- **Premium:** Multiple Marbles + Pamela's NEW Workout + professional drum module collection for complete rhythmic workstation

---

## Common Use Cases

**🎲 **Intelligent Sequencing:** Random melodies that learn and repeat good ideas**
**🥁 **Polyrhythmic Drums:** Complex percussion patterns with multiple outputs**  
**🌊 **Organic Modulation:** Smooth random modulation that evolves over time**
**🔄 **Sequence Processing:** Transform existing sequences into variations**
**⏰ **Humanized Timing:** Add natural feel to rigid clock sources**
**🎵 **Generative Composition:** Create self-evolving musical structures**
**🎛️ **Performance Tool:** Real-time control over randomness and repetition**
**🎹 **Algorithmic Music Partner:** Sophisticated pattern generator that responds to your creativity**

---

## Advanced Cross-Reference Learning Path

### **Essential Advanced Progressions:**
1. **Start here** with basic intelligent randomness and DEJA VU concepts
2. **Add organic breathing** with DivKid ochd for natural rhythm variations (see ochd guide)
3. **Introduce controlled chaos** with Make Noise Wogglebug for unpredictable elements (see Wogglebug guide)
4. **Add mathematical structure** with 4ms RCD v2 for polyrhythmic precision (see RCD guide)
5. **Process everything** with Cre8audio Function Junction for refined modulation (see Function Junction guide)
6. **Build complete algorithmic systems** using feedback and cross-module pattern networks

### **Advanced Integration Strategies:**

**With DivKid ochd:**
- **Organic algorithmic patterns:** ochd's breathing rhythms provide natural timing for Marbles
- **Rate modulation:** LFO 1 → Marbles Rate CV for organic tempo breathing
- **Character evolution:** LFO 3/7 → Spread/Bias for evolving pattern character

**With Make Noise Wogglebug:**
- **Controlled chaos:** Wogglebug randomness + Marbles probability control = musical chaos
- **Stepped sequences:** Wogglebug Stepped + Marbles quantization = evolving melodies  
- **Chaos processing:** Marbles can make Wogglebug output more musical through probability shaping

**With 4ms RCD v2:**
- **Polyrhythmic patterns:** RCD divisions trigger Marbles at mathematical ratios
- **Precise timing:** RCD clocks provide structured timing for Marbles to respond to
- **Mathematical pattern evolution:** Marbles creates musical relationships within mathematical structures

**With Cre8audio Function Junction:**
- **Modulation processing:** Function Junction shapes Marbles outputs into musical envelopes
- **Pattern feedback:** Function Junction triggers provide rhythmic structure to Marbles
- **Multi-stage processing:** Marbles generates, Function Junction refines and processes

---

## Beginner "Gotchas" 

### **Two Separate Sections**
- **Left side (t) = Rhythms/Timing** - outputs t1, t2, t3 are gates/triggers
- **Right side (X) = Voltages/Melodies** - outputs X1, X2, X3 are CV voltages
- **They work together but can be controlled independently**
- **Y output is bonus smooth random CV** - great for slow modulation

### **DEJA VU is the Secret Sauce**
- **12 o'clock = Perfect Loop** - module gets stuck repeating same pattern
- **11 o'clock = Slow Evolution** - patterns gradually change and develop
- **1 o'clock = Shuffle Mode** - same notes/rhythms in different orders
- **t/X buttons choose which sections are affected** by DEJA VU memory

### **STEPS Knob is Bi-Directional**
- **Left of center = Smooth** (for modulation, not melodies)
- **Right of center = Quantized** (for musical sequences)  
- **The further right, the more "musical"** it becomes
- **Far right = Only root notes** - very consonant but potentially boring


---

**Bottom Line:** Marbles isn't just a random generator - it's a **sophisticated algorithmic pattern generator** that creates musically satisfying randomness. It transforms chaotic randomness into musical patterns through clever programming and probability control, **responding to your creative input and guidance**. You remain the composer - Marbles is your sophisticated tool for exploring musical possibilities.

---

*Visit [Mutable Instruments](https://mutable-instruments.net/modules/marbles/) for complete documentation, firmware updates, and the open-source code that makes the magic possible.*
