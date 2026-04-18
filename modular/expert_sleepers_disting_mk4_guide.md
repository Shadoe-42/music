---
title: Expert Sleepers Disting MK4
manufacturer: Expert Sleepers
primary_role: UTILITY
secondary_roles: []
form_factor: eurorack
functions: [oscillator, fx-time, envelope-generator]
behavior_tags: [stable, linear, reactive, performance-oriented]
use_cases: [utility fill-in role, problem-solving in-patch, whatever is needed right now]
hp: 4
memory: none
screen: true
---

# Disting mk4
*The Swiss Army Knife of Eurorack*

---

## Quick Start: Get Your First Sound in 5 Minutes

![Expert Sleepers Disting mk4](https://github.com/Shadoe-42/music/raw/main/modular/images/expert_sleepers/disting_mk4/front_panel.jpg)
*Expert Sleepers Disting mk4 - Front panel showing algorithm display, dual inputs/outputs, and parameter controls*

**What is Disting mk4?** A **multi-algorithm utility module** that can function as 80+ different modules in one tiny 4HP package. Think of it as having an entire modular system that you can switch between instantly - oscillators, filters, delays, quantizers, LFOs, envelopes, and much more.

**Key Specifications:**

| Spec | Value |
|------|-------|
| Width | 4HP |
| Depth | 42mm |
| Power | +51mA / -19mA |
| Architecture | 80+ algorithm multi-function utility with SD card integration |

### Your First Algorithm - Precision Adder
1. **Power up** - watch the startup LED sequence (columns then rows)
2. **Press S knob once** to enter menu, **press again** to select "Algorithm"
3. **Turn S knob** to A-1 "Precision Adder", **press to confirm**
4. **Patch oscillator** → **X input** and **LFO** → **Y input** 
5. **Patch A output** → your next module's CV input
6. **Turn Z knob** - add/subtract voltage offset for transposition
7. **Display shows** voltage when Z changes

### Discover the Quantizer Magic
1. **Press S twice** to access algorithm menu
2. **Turn S to A-6** "Quantizer", **press to confirm**
3. **Patch oscillator CV** → **X input**
4. **Patch A output** → oscillator's 1V/Oct input  
5. **Turn Z knob** - cycle through musical scales (major, minor, triads, etc.)
6. **Listen** - your oscillator now plays only in-key notes!

---

## Essential Parameters (The Big 5)

### **1. Algorithm Selection (80+ Algorithms)**
- **What it does:** Completely changes the module's function
- **Access:** Press S twice, turn to select, press to confirm
- **Categories:** A-N series (A=CV utilities, B=modulation, C=audio processing, etc.)
- **Key concept:** Each algorithm is like swapping to a completely different module

### **2. Z Knob/CV Control**
- **What it does:** Main real-time parameter control (function depends on algorithm)
- **Examples:** Frequency, feedback, scale selection, resonance, mix
- **CV Input:** Dedicated Z CV input adds to knob position
- **Visual feedback:** Socket lights red (positive) or blue (negative) indicating voltage

### **3. S Knob & Parameters**
- **What it does:** Adjusts algorithm-specific parameters (up to 8 per algorithm)
- **Access:** Turn S knob to change current parameter
- **Parameter selection:** Press Z to cycle through parameters, or hold S + turn
- **Display:** Shows parameter values when changed

### **4. X & Y Inputs**
- **What they do:** Main CV/audio inputs (function varies by algorithm)
- **Examples:** Signal input + control CV, left + right audio, pitch + gate
- **Voltage range:** ±5V (higher voltages won't damage but will be clipped)
- **Socket lighting:** Visual indication of input voltage levels

### **5. A & B Outputs**
- **What they do:** Main outputs (function varies by algorithm)
- **Examples:** Processed signal, dry + wet, left + right, CV + gate
- **Voltage range:** ±10V maximum before clipping
- **Socket lighting:** Shows output voltage in real-time

---

## Historical Context

**The Algorithm Revolution:** The Expert Sleepers Disting mk4 represents a pivotal innovation in modular synthesis - the first module to successfully implement dozens of classic synthesis functions in a single 4HP package. Released when modular systems required separate modules for every function, Disting proved that sophisticated algorithm implementation could replace hardware specialization.

**Technical Innovation:** With 80+ algorithms covering every fundamental synthesis category, Disting mk4 democratized modular synthesis by making advanced functions accessible without requiring extensive module collections. Its SD card integration and continuous firmware updates established the template for software-enhanced hardware that many manufacturers now follow.

**Educational Impact:** Disting became the "modular synthesis textbook" - allowing users to explore quantizers, delays, filters, LFOs, and complex processing without investing in dozens of specialized modules. This educational accessibility helped grow the modular synthesis community significantly.

---

## Understanding the Algorithm Structure

### **The Philosophy:**
Instead of buying dozens of modules, Disting mk4 gives you **one module that can become any module you need**. Each algorithm is a complete reimplementation of a classic modular function, from simple utilities to complex effects.

### **Algorithm Categories:**
- **A Series (A1-A8):** CV utilities - mixers, quantizers, logic, arithmetic
- **B Series (B1-B8):** Modulation sources - LFOs, S&H, envelopes, VCOs  
- **C Series (C1-C8):** Audio processing - delays, filters, effects
- **D Series (D1-D8):** More filters and audio manipulation
- **E-F Series:** Envelopes, dynamics, format conversion
- **G Series:** References, clocks, MIDI/CV conversion
- **H-M Series:** Advanced processing, logic, sample playback
- **N Series:** Latest additions and specialized functions

### **SD Card Integration:**
- **Sample playback:** I & J series algorithms play WAV files
- **MIDI sequencing:** J series plays back MIDI files  
- **Wavetables:** K series loads custom wavetables
- **Scala support:** Microtonal scales from Scala software
- **Presets & help:** Store module presets and algorithm help on card

### **Menu System Navigation:**
- **Algorithm:** Select from 80+ functions
- **Save/Load:** 64 preset slots for storing complete module states
- **Settings:** Display brightness, MIDI channels, file behavior
- **Help:** Algorithm-specific information (loaded from SD card)
- **Calibrate:** Factory calibration (usually not needed)

---

## Why This Instrument Excels

**The Philosophy:**
Disting mk4 proves that **one excellent module** can be more valuable than dozens of mediocre ones. Instead of buying a separate quantizer, delay, LFO, filter, and sample player, you get all of them in 4HP - and they're all excellent implementations.

**The Innovation:**
- **80+ algorithms** covering every fundamental modular synthesis function
- **Consistent interface** means learning one algorithm helps with all others
- **SD card integration** extends functionality far beyond typical hardware limitations
- **Continuous development** with regular firmware updates adding new algorithms

**The Practical Benefits:**
- **Space efficiency:** Entire studio functionality in 4HP
- **Cost effectiveness:** One module replaces dozens of specialized modules
- **Learning tool:** Explore modular synthesis concepts without buying everything
- **Problem solver:** Always have the right tool for any synthesis challenge

**Perfect For:**
- **Beginners:** Learn modular synthesis without breaking the bank
- **Small system builders:** Maximum functionality in minimal space
- **Experimenters:** Try every type of synthesis and processing
- **Professionals:** Reliable, high-quality implementations of essential functions
- **Anyone needing:** That one specific function they don't have a module for

**The Magic:**
Disting mk4 **democratizes modular synthesis** by making every function accessible to everyone. Whether you need a simple mixer or complex granular processing, it's all there, waiting to be discovered.

---

## Patches
### **Patch 1: First Steps - Musical CV Quantizer**
```
                    ┌─────────────────────┐
                    │   Disting mk4       │
                    │                     │
     Random CV ─────┼─▶ X Input           │
     Generator       │                     │
                    │ Algorithm: A-6      │
                    │ (Quantizer)         │
                    │                     │
                    │ Z Knob: Scale       │
                    │ (Turn for Major,    │
                    │  Minor, etc.)       │
                    │                     │
                    │ A Output ○─────────┼─── [C]
                    │ (Quantized CV)      │
                    │                     │
                    │ B Output ○─────────┼─── [G]
                    │ (Note Change Trig)  │
                    └─────────────────────┘
                             ║       ║
                        CV   ║  Gate ║
                        (Blue)║(Yellow)║
                             ▼       ▼
                    ┌──────────────────────┐
                    │   Oscillator         │
                    │                      │
                    │ 1V/Oct    ◀─────────┼─── Quantized Pitch
                    │                      │
                    │ Audio Out ○──────────────── To Envelope/VCA
                    │                      │
                    └──────────────────────┘
                             ║
                        Audio║
                             ▼
                    ┌──────────────────────┐
                    │   Envelope Generator │
                    │                      │
                    │ Trigger   ◀─────────┼─── Note Change Trigger
                    │                      │
                    │ CV Out    ○────────────── To VCA
                    └──────────────────────┘
```
```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│ Random CV   │───▶│ Disting mk4  │───▶│ Oscillator  │
│ Generator   │    │ Algorithm:   │    │ 1V/OCT Input│
│ (or Slides) │    │ A-6 Quantizer│    └─────────────┘
└─────────────┘    │              │           │
                   │ X Input      │           ▼
                   │ A Output     │    ┌─────────────┐
                   │              │───▶│ Envelope    │
                   │ B Output     │    │ Generator   │
                   │ (Trigger)    │    │ Trigger In  │
                   │              │    └─────────────┘
                   │ Z Knob:      │
                   │ Scale Select │
                   │ [Display:    │
                   │  "Major"]    │
                   └──────────────┘
```

| Connection | Cable Type | Notes |
|------------|------------|-------|
| Random CV → Disting X Input | [C] | Unquantized pitch CV |
| Disting A Out → Oscillator V/OCT | [C] | Quantized to musical scale |
| Disting B Out → Envelope Trigger | [G] | Fires on note changes |

**Module Settings:**
- **Disting:** Algorithm A-6 Quantizer
- **Z Knob:** Turn to select scale (Major, Minor, Pentatonic, etc.)
- **Display shows:** Current scale name when Z changes
- **Parameters:** Default settings work well for most applications

**Visual Feedback:**
- **Socket LEDs:** X input shows incoming CV, A/B outputs show processed signals
- **Display:** Shows "Quantizer" and current scale name when Z changes
- **B Output LED:** Flashes when note changes trigger
- **Result:** Random CV becomes musical melodies in any scale

**Alternative Module Options:**
- **Instead of Random CV Generator:** Try **Make Noise Wogglebug** for stepped chaos, **Turing Machine** for binary sequences, or **2HP Rnd** for compact randomness
- **Budget alternatives:** **Doepfer A-118-2** provides noise/random sources, **AI Synthesis AI008** for DIY random CV
- **Different character:** **Mutable Marbles** for algorithmic randomness with musical bias, **Intellijel Quadrax** for complex envelope-based CV
- **Premium options:** **Malekko Varigate 8+** for pattern-based random sequences with visual feedback

### **Patch 2: Intermediate - Dual Function Hub**
```
   ┌─────────────────────┐      ┌─────────────────────┐
   │   Audio Source      │      │   Disting mk4       │
   │                     │      │                     │
   │ Audio Out ○────────┼──────┼─▶ X Input (Audio)     │
   │                     │      │                     │
   └─────────────────────┘      │ Algorithm: C-5      │
                                │ (Resonator)         │
   ┌─────────────────────┐      │                     │
   │   Clock/LFO        │      │ Y Input         ◀──┼────── Modulation CV
   │                     │      │ (Frequency CV)      │
   │ Clock Out ○────────┼──────┘      │                     │
   │                     │              │ Z Knob: Resonance   │
   └─────────────────────┘              │ (Real-time control) │
                                      │                     │
                                      │ A Output ○────────┼─── [A]
                                      │ (Resonant Audio)    │
                                      │                     │
                                      │ B Output ○────────┼─── [C]
                                      │ (Envelope Follower) │
                                      └─────────────────────┘
                                               ║       ║
                                          Audio║  CV   ║
                                          (Red)║ (Blue)║
                                               ▼       ▼
                                      ┌─────────────────────┐
                                      │   Effects Chain     │
                                      │                     │
                                      │ Audio In     ◀───┼─── Resonant Audio
                                      │                     │
                                      │ Mod CV       ◀───┼─── Envelope Follow
                                      │                     │
                                      │ Audio Out ○──────┼─── Final Processing
                                      └─────────────────────┘
```

| Connection | Cable Type | Purpose | Advanced Function |
|------------|------------|---------|------------------|
| Audio Source → X Input | [A] | **Signal to be processed** | **Resonant filtering** |
| Clock/LFO → Y Input | [C] | **Frequency modulation** | **Dynamic resonance control** |
| A Output → Effects Audio | [A] | **Processed signal** | **Resonant audio character** |
| B Output → Effects Mod | [C] | **Envelope follower CV** | **Audio-reactive modulation** |

**Module Settings:**
- **Disting Algorithm:** C-5 (Resonator)
- **Z Knob:** Resonance amount (start at 12 o'clock)
- **Y Input:** Modulation for frequency sweeping
- **Real-time control:** Z knob for performance

**Learning Objectives:**
- Master dual-output algorithms
- Understand audio processing with CV outputs
- Learn resonant filtering concepts
- Experience envelope following techniques

**Alternative Module Options:**
- **Instead of Audio Source:** Try **Make Noise STO** for clean oscillator tone, **Mutable Plaits** for varied synthesis models, or **2HP OSC** for budget oscillation
- **Budget alternatives:** **Doepfer A-111-3** provides basic VCO functionality, **AI Synthesis AI002** for DIY oscillator projects
- **Different character:** **Intellijel Rubicon** for complex waveform generation, **Make Noise DPO** for dual oscillator complex tones
- **For modulation:** **Batumi** for quad LFO, **2HP LFO** for compact modulation, **Maths** for complex function generation
### **Patch 3: Advanced - Phase 1 Integration Hub**
```
   ┌─────────────────────┐      ┌─────────────────────┐
   │   Mutable Plaits    │      │   Disting mk4       │
   │    (Phase 1)        │      │   (Utility Hub)     │
   │                     │      │                     │
   │ Model CV        ◀───┼──────┼─ A Output           │
   │                     │      │                     │
   │ Timbre CV       ◀───┼──────┼─ Algorithm: K-3     │
   │                     │      │ (LFO + Quantizer)   │
   │ Audio Out ○─────────┼──────┼─▶ X Input           │
   │                     │      │                     │
   └─────────────────────┘      │ B Output ○──────────┼─── [C]
                                │ (Quantized CV)      │
   ┌─────────────────────┐      │                     │
   │   Make Noise Maths  │      │ Z Knob: Scale       │
   │    (Phase 1)        │      │ S Knob: LFO Rate    │
   │                     │      │                     │
   │ Ch1 Unity Out ○─────┼──────────────┐     └─────────────────────┘
   │                     │              │     ║
   │ Ch4 Variable Out○───┼──────────────┼─────╬═══════════▶ Multiple
   │                     │              │     ║ [C]   Destinations
   │ SUM Output ○────────┼──────────────┘     ▼
   │                     │              ┌──────────────┐
   └─────────────────────┘              │   Synthesis  │
                                        │   Network    │
                                        │              │
                                        │ Multi-module │
                                        │ Integration  │
                                        │              │
                                        │ Audio Out ○──┼─── Complex Music
                                        └──────────────┘
```

| Module Chain | Integration Role | Purpose | Phase 1 Synergy |
|-------------|------------------|---------|------------------|
| **Plaits → Disting** | Audio analysis | **Model switching intelligence** | **Synthesis drives utility functions** |
| **Disting LFO/Quantizer** | Dual utility | **Modulation + pitch processing** | **Single module, multiple functions** |
| **Maths → Multi-destinations** | Complex modulation | **Mathematical processing** | **Analog computation** |
| **System Integration** | Complete voice | **All modules working together** | **Phase 1 ecosystem** |

**Module Settings:**
- **Disting:** Algorithm K-3 (LFO + Quantizer combo)
- **Plaits:** Responds to Disting's intelligent CV processing
- **Maths:** Provides complex envelopes and mathematical relationships
- **Integration:** All Phase 1 modules enhance each other

**Learning Objectives:**
- **Phase 1 module integration:** All core modules working as unified system
- **Utility hub concept:** Disting as central processing for other modules
- **Complex signal routing:** Multiple modules, multiple functions, musical results
- **System-level thinking:** Design patches as integrated ecosystems

### **Patch 4: Expert - Three-Algorithm Live Switching**

This patch uses Disting's preset recall system to switch between three different algorithm configurations during performance. Each preset serves a different role in a larger modulation system: quantizing organic LFO voltages into musical scale degrees, performing boolean logic on chaotic gate streams, and providing a reference LFO plus precision CV addition. The performance technique is switching presets by ear as the patch evolves.

```
[Ochd LFO 2]         ---> [Disting X Input]   (for Preset 1: Quantizer)
[Wogglebug Stepped]  ---> [Disting X Input]   (for Preset 2: Logic)
[Marbles T gates]    ---> [Disting Y Input]   (for Preset 2: Logic)
[RCD Div 2]          ---> clock reference

Preset 1: A-6 Quantizer
  X Input <-- Ochd LFO 2 (unquantized organic CV)
  Z Knob: scale selection (Major, Pentatonic, etc.)
  A Output --> oscillator 1V/Oct or other pitch destination
  B Output --> gate on note change

Preset 2: H-1 Logic Operations
  X Input <-- Wogglebug Stepped (logic input A)
  Y Input <-- Marbles T gates (logic input B)
  A Output --> complex trigger pattern
  B Output --> inverted trigger pattern

Preset 3: B-5 LFO + A-1 Precision Adder
  Internal LFO --> system reference or modulation
  Z Knob: LFO rate
  X Input <-- any CV for offset addition
  A Output --> offset/summed CV

[A Output]           ---> destination depends on active preset
[B Output]           ---> destination depends on active preset
```

**Setup:**
1. Save three Disting presets: Preset 1 = A-6 Quantizer, Preset 2 = H-1 Logic, Preset 3 = B-5 LFO
2. Route Ochd LFO 2 to X Input for Quantizer work
3. For Logic work, route Wogglebug Stepped to X Input and Marbles T output to Y Input
4. Patch A Output to a synthesis destination that benefits from the active algorithm
5. Use the preset recall system to switch algorithms during performance
6. Z Knob controls the most immediate parameter in each algorithm: scale for Quantizer, rate for LFO

**What to listen for:** Each preset change reconfigures what Disting is doing entirely. The Quantizer turns continuous organic LFO movement into stepwise musical intervals; the scale setting (Z Knob) determines which steps are available. The Logic operations combine the Wogglebug and Marbles gate streams using boolean AND, OR, or XOR depending on the algorithm parameter, creating trigger patterns that neither source could produce alone. The LFO preset turns Disting into an additional modulation source that can be tuned to complement or contrast with Ochd.

The practical skill this builds is learning to think of Disting as a reconfigurable tool rather than a fixed module, and developing the habit of saving useful configurations to preset slots before a performance.

**Alternative Module Options:**
- **For organic modulation sources:** **DivKid Ochd** for natural breathing LFOs, **Batumi** for quad LFO with phase relationships, **2HP LFO** for budget modulation
- **Budget alternatives:** **Doepfer A-143-3** for quad LFO, **AI Synthesis AI003** for DIY envelope generation
- **For chaos sources:** **Make Noise Wogglebug** for stepped random, **Turing Machine** for binary sequences, **2HP Rnd** for compact randomness
- **Advanced processing:** **Make Noise Maths** for complex mathematical operations, **Function Junction** for comprehensive CV processing
- **Different character:** **Pamela's New Workout** for algorithmic pattern generation, **Malekko Varigate 8+** for visual pattern sequencing

---

## Common Mistakes

### **Common Mistakes:**

**"I can't hear any difference when I turn the Z knob!"**
- Check that you're using the right algorithm for your signal type
- **Solution:** A-6 Quantizer needs pitch CV input, B-4 Delay needs audio input

**"The algorithm menu is confusing!"**
- 80+ algorithms can be overwhelming at first
- **Solution:** Start with A1-A8 and B1-B8, learn a few well before exploring

**"My samples won't play!"**
- SD card must be FAT32 formatted, 16-bit WAV files only
- **Solution:** Use SD Association formatting tool, convert files to 16-bit WAV

**"Settings keep reverting when I power cycle!"**
- Preset 0 loads at startup and auto-saves when switching algorithms
- **Solution:** Save your settings to Preset 0 if you want them at startup

### **Pro Tips:**

**Algorithm Learning Strategy:**
- **Master one series first** - try all A-series (CV utilities) before moving on
- **Learn the classics:** A-1 (adder), A-6 (quantizer), B-5 (LFO), B-4 (delay)
- **Use favorites system** to create your personal "greatest hits" menu

**Z Knob Mastery:**
- **Different per algorithm** - Z might be frequency, feedback, scale, or resonance
- **Watch the display** when changing Z - it shows the current value
- **CV input adds to knob** - set knob to center for bipolar CV control

**Parameter Navigation:**
- **Press Z to cycle** through parameters instead of holding S + turn
- **Parameter names displayed** briefly when you switch
- **Parameter values shown** when you change them with S knob

**SD Card Organization:**
- **Separate folders** for different sample sets (drums, melodies, textures)
- **Use playlists** to control file order and loop settings
- **Keep it simple** - don't put 1000s of files on card (slows down loading)

**Performance Techniques:**
- **Save complex setups** to numbered presets for instant recall
- **Use knob recorder** for repeated complex movements
- **Learn algorithm numbers** for quick navigation (A1, B5, etc.)
- **Chain algorithms** by saving partial setups and switching between them

---

## Advanced Learning Path

**Favorites System:**
- **Create custom menu** of your 16 most-used algorithms (O1-P8)
- **Text file on SD card** named 'favourites.txt' 
- **Quick access** to personalized algorithm collection
- **Example:** "b5 LFO", "a6 quantizer", "c5 resonator"

**Preset Management:**
- **64 preset slots** store complete algorithm states
- **Preset 0 special:** Loads at power-up, auto-saves on algorithm change
- **Save workflow:** Menu → Save → choose slot → confirm
- **Performance tip:** Use presets for complex algorithm configurations

**Knob Recorder Function:**
- **Available on many algorithms** where Z doesn't have another function
- **Hold Z while turning** to record knob movements (up to 14 seconds)
- **Release Z** to loop playback of recorded movements
- **Turn knob slightly** to regain manual control
- **Perfect for:** Complex filter sweeps, rhythmic parameter changes

**SD Card Advanced Features:**
- **Playlist files** control sample/MIDI file order and settings
- **Loop markers** in WAV files for complex sample playback
- **Scale files** for microtonal quantization using Scala format
- **Help files** can be customized or translated
- **Firmware updates** via audio file playback

**MIDI Integration:**
- **MIDI/CV algorithms** (G-7, G-8) for full MIDI integration
- **MIDI input** affects quantizers, triggers envelopes
- **MIDI output** from quantizers and step sequencers
- **MIDI clock** sync for delay and LFO algorithms

---

## Common Use Cases

1. **🔢 CV Processing & Logic:** Precision math on control voltages (add, multiply, compare), quantization to musical scales, logic operations
2. **🌊 Modulation Generation:** LFOs with Hz/V or clock sync, envelopes with various shapes, sample & hold, random CV generation
3. **🔊 Audio Processing:** Filters in every configuration, delays with tape simulation, effects including phaser/chorus/vocoder
4. **🎵 Sample Playback & Sequencing:** Audio playback with pitch control, MIDI file playback, wavetable synthesis, multi-sampling
5. **⏰ System Utilities:** Clock generation and division, tuning references, MIDI/CV conversion, signal mixing
6. **🎛️ Utility Hub:** Central processing and conversion for modulation, timing, and pitch
7. **🔧 Problem Solver:** Always have the exact utility function needed for any synthesis challenge
8. **📚 Learning Tool:** Explore every aspect of modular synthesis through 80+ algorithm implementations

---

## Pairs Well With

**Modulation & CV Source Integration:**
- **DivKid Ochd & Expander:** Use Disting quantizers to process Ochd organic LFOs into musical scales
- **Make Noise Wogglebug:** Disting logic/CV processing algorithms perfect for taming Wogglebug chaos
- **Mutable Marbles:** Use Disting as probability processor and pattern quantizer for Marbles algorithms
- **4ms RCD v2:** Clock processing and division algorithms complement RCD's polyrhythmic outputs
- **Cre8audio Function Junction:** Disting envelope and LFO algorithms provide additional modulation processing
- **Cross-System Integration:** Disting serves as utility hub processing all sophisticated modulation sources

**Core Synthesis Module Integration:**
- **Make Noise Maths:** Use Disting quantizers to process Maths CV outputs into musical sequences
- **Mutable Plaits:** Audio processing algorithms perfect for Plaits synthesis models
- **Mob of Emus:** Mathematical processing algorithms complement harmonic relationships
- **Complete synthesis systems:** Disting as central utility processor for synthesis networks

**Essential Utility Partners:**
- **SD Card (32GB SDHC recommended):** Unlocks sample playback, MIDI, wavetables, and custom scales
- **Clock Sources:** Essential for rhythm-synced delays, LFOs, and sequencer algorithms
- **CV Sources:** Multiple CV inputs benefit from having various modulation available
- **Audio Sources:** Brings life to the extensive audio processing and analysis algorithms

**Advanced System Integration:**
- **Small Systems:** Single module providing dozens of essential functions
- **Large Systems:** Fill gaps and provide specialized utility functions not available elsewhere
- **Performance Rigs:** Quick algorithm changes for live flexibility and real-time function switching
- **Studio Systems:** Recall-able setups via comprehensive preset system

---
