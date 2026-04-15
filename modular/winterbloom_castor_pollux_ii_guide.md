---
title: Winterbloom Castor & Pollux II
manufacturer: Winterbloom
primary_role: SOURCE
secondary_roles: []
form_factor: eurorack
functions: [oscillator, fx-modulation]
behavior_tags: [warm, stable, harmonic, bright, evolving]
use_cases: [lead voice, chord voice, lush stereo oscillator, bass voice]
hp: 18
memory: full
hybrid: true
---

# Winterbloom Castor & Pollux II - Beginner's Guide

**The Modern Juno Twins**

---

## Quick Start: Get Your First Juno-Style Sound in 5 Minutes

**What is Castor & Pollux II?** Think of it as two Roland Juno-106 oscillators reimagined for the modern age. It contains two digitally-controlled analog oscillators (DCOs) that faithfully recreate the legendary 80s Juno sound, but with modern improvements like hard sync, built-in chorus, and USB connectivity. Named after the mythological twins, these oscillators can work independently or together to create everything from classic 80s pads to complex evolving textures.

### Your First Juno Lead Sound
1. **Connect Castor OUT** → **your filter or audio output**
2. **Turn up Castor's RAMP mix knob** (small knob, fully clockwise)
3. **Connect keyboard/sequencer CV** → **Castor PITCH CV input**
4. **Play some notes** - you should hear that classic Juno sawtooth!
5. **Try the MODE button** - tap to cycle through Chorus/LFO FM/Hard Sync modes
6. **Adjust CROSSFADE knob** to blend in Pollux for thickness

**Congratulations!** You've just experienced the legendary Juno sound in Eurorack format!

---

## Essential Parameters (The Twin System)

### **1. The Twin Oscillators - Castor & Pollux**
- **Two identical DCOs:** Each with independent pitch control and waveform mixing
- **Castor (left):** The primary oscillator, typically your main voice
- **Pollux (right):** The secondary oscillator, often used for detuning and effects
- **Independent operation:** Each can work as separate mono oscillators
- **Coupled operation:** Use together for thick, complex sounds
- **Juno-authentic:** Faithfully recreates the original Juno 106 oscillator behavior

### **2. Pitch Control System - Smart Tuning**
- **Large pitch knobs:** Coarse frequency control for each oscillator
- **PITCH CV inputs:** 1V/octave for musical control
- **Non-linear response:** "Virtual notch" makes tuning easier around musical pitches
- **Tweak mode:** Hold MODE button + turn pitch knob for fine tuning (±2.5 semitones)
- **Follow vs Free modes:** Pitch knob can track 1V/oct or run free (configurable via web)
- **Pro tip:** The non-linear response makes it easier to hit exact musical intervals

### **3. Waveform System - Three Shapes Each**
- **RAMP:** Classic sawtooth waveform (bright, buzzy, perfect for leads)
- **PULSE:** Square/rectangular wave with PWM capability
- **SUB:** Sub-oscillator at -1 octave (adds bass foundation)
- **Individual mix controls:** Small knobs control how much of each wave in the mixed output
- **Mixed outputs:** Each oscillator combines its three waves into one output
- **Expander access:** 2HP expander provides individual waveform outputs

### **4. Three Operational Modes - The Magic Button**
- **MODE button:** Tap to cycle between three distinct behaviors
- **Chorus mode (blue LED):** Default mode with built-in chorus on Pollux
- **LFO FM mode (green LED):** Internal LFO modulates both oscillators' pitch
- **Hard Sync mode (pink LED):** Pollux syncs to Castor for metallic tones
- **Tweak overlay:** Hold MODE button for additional parameters in each mode
- **Visual feedback:** LED color and animations show current mode

### **5. Crossfade System - Blending the Twins**
- **CROSSFADE knob:** Blends between Castor and Pollux mixed outputs
- **CROSSFADE output:** Main output combining both oscillators
- **Full CCW:** Only Castor audible
- **12 o'clock:** Equal blend of both oscillators  
- **Full CW:** Only Pollux audible
- **Performance control:** Perfect for live morphing between sounds

### **6. Web Editor Integration - Modern Convenience**
- **USB connection:** Connect via micro USB for advanced configuration
- **Browser-based editor:** No software installation required
- **Deep customization:** LED brightness, pitch behavior, LFO settings, and more
- **Calibration:** Fine-tune oscillator accuracy and tracking
- **Open source:** All firmware and hardware designs available on GitHub


---

## Why Winterbloom Castor & Pollux II Excels

### **The Philosophy:**
Castor & Pollux II represents the **perfect bridge between vintage and modern** - authentic Juno-106 character with contemporary convenience. Unlike simple oscillator recreations, this module captures the complete DCO experience including the quirks, characteristics, and musical behavior that made the Juno legendary. **The web editor integration means you get vintage soul with modern flexibility.**

### **Perfect For:**
- **80s music enthusiasts** seeking authentic Juno character in modular format
- **Modern producers** wanting vintage sounds with contemporary modular integration
- **Space-conscious builders** needing multiple oscillator functions in reasonable HP
- **Performance musicians** requiring reliable vintage sounds with modern stability
- **Phase 2 system builders** adding vintage character to intelligent modular ecosystems

### **The Vintage-Modern Experience:**
Using Castor & Pollux II teaches you about both **vintage synthesis philosophy and modern modular integration**. The authentic DCO behavior shows you why the Juno became legendary, while the web editor and CV control reveal how vintage concepts translate to contemporary modular workflow. **You experience music history through modern tools.**


---

---

## Progressive Patch Examples

### **Patch 1: First Steps - Classic Juno Lead**
```
                    ┌─────────────────────────────────┐
                    │  Winterbloom Castor & Pollux   │
                    │                                │
     1V/Oct CV ─────┼─▶ Castor PITCH CV              │
                    │                                │
                    │ MODE: Chorus (Blue LED)        │
                    │ Castor RAMP: Full CW           │
                    │ Castor PULSE: 25%              │
                    │ CROSSFADE: 9 o'clock           │
                    │                                │
                    │ Castor OUT ○───────────────────┼─── Audio (Red)
                    │                                │
                    │ Status: Classic Juno Voice     │
                    └─────────────────────────────────┘
                             ║
                        Audio║
                        (Red)║
                             ▼
                    ┌─────────────────────┐
                    │      Filter         │
                    │                     │
                    │ Audio In        ◀───┼─── Classic Juno Lead
                    │                     │
                    │ Audio Out ○─────────┼─── Final Output
                    └─────────────────────┘
```

| Connection | Cable Type | Notes |
|------------|------------|-------|
| 1V/Oct CV → Castor PITCH | CV (Blue) | Keyboard or sequencer pitch control |
| Castor OUT → Filter | Audio (Red) | Classic Juno sawtooth tone |

**Module Settings:**
- **Mode:** Chorus (default blue LED)
- **Castor RAMP mix:** Full clockwise (main sawtooth)
- **Castor PULSE mix:** 25% for slight square wave blend
- **CROSSFADE:** 9 o'clock (mostly Castor with hint of chorus)

**Learning Objectives:**
- Experience authentic Juno-106 oscillator character
- Understand waveform mixing with small trim knobs
- Learn MODE button operation and visual feedback
- Master basic dual-oscillator relationship

**Visual Feedback:**
- **Blue LED:** Chorus mode active
- **Waveform response:** Hear classic Juno brightness and movement
- **Result:** Authentic 80s lead sound with built-in character

### **Patch 2: Intermediate - Phase 2 Organic Juno Evolution**
```
   ┌─────────────────────┐      ┌─────────────────────────────────┐
   │   DivKid Ochd      │      │  Winterbloom Castor & Pollux   │
   │    (Phase 2)       │      │                                │
   │                    │      │ Audio Source             ◀─────┼─── [External Audio]
   │ LFO 3 ○────────────┼──────┼─▶ Castor PITCH CV              │
   │       ║            │      │                                │
   │ LFO 6 ○────────────┼──────┼─▶ Pollux PITCH CV              │
   │       ║            │      │                                │
   │ LFO 1 ○────────────┼──────┼─▶ CROSSFADE CV (via web editor)│
   │       ║            │      │                                │
   │ Trigger 2○─────────┼──────┼─▶ MODE Trigger (via web editor)│
   │       ║            │      │                                │
   │ Rate: 12 o'clock   │      │ MODE: All modes cycling        │
   │ (Organic timing)   │      │ Detuning: Slight Pollux offset │
   │                    │      │                                │
   └───────║────────────┘      │ CROSSFADE OUT ○────────────────┼─── Organic
           ║                   │                                │    Juno
   CV (Blue)║                   └─────────────────────────────────┘    Evolution
           ▼                            ║
   ┌─────────────────┐                 Audio║
   │   Effects       │                 (Red)║
   │ Processing      │                      ▼
   │                 │             ┌─────────────────────┐
   │ Modulation  ◀───┼─────────────┼─ Chorus/Reverb      │
   │ CV Input        │             │                     │
   │                 │             │ Audio In        ◀───┼─── Organic Juno
   │ Audio Out   ○───┼─────────────┼─                     │
   └─────────────────┘             │ Spatial Out ○───────┼─── Complete
                                   └─────────────────────┘    Organic
                                                              Experience
```

| Module Integration | Signal Flow | Purpose | Phase 2 Synergy |
|-------------------|-------------|---------|------------------|
| **Ochd LFO 3 → Castor Pitch** | Organic frequency drift | **Breathing pitch evolution** | **Natural Juno character drift** |
| **Ochd LFO 6 → Pollux Pitch** | Organic detuning | **Breathing thickness control** | **Natural beating evolution** |
| **Ochd LFO 1 → Crossfade** | Organic blending | **Breathing oscillator balance** | **Natural voice morphing** |
| **Ochd Trigger 2 → Mode** | Organic mode switching | **Character evolution** | **Natural Juno mode changes** |

**Module Settings:**
- **Ochd Rate:** 12 o'clock for musical organic timing
- **Web Editor:** Enable CV control of crossfade and mode switching
- **Pollux detuning:** Slight pitch offset for natural beating
- **All modes active:** Organic switching between chorus/FM/sync modes

**Learning Objectives:**
- **Organic Juno processing:** Natural breathing applied to vintage character
- **Web editor integration:** Advanced CV control setup
- **Multi-mode evolution:** Organic switching between Juno characteristics
- **Phase 2 + vintage integration:** Modern modulation with classic sound

### **Patch 3: Advanced - Phase 2 Algorithmic Juno Intelligence**
```
┌─────────────────────┐    ┌─────────────────────────────────┐
│   Mutable Marbles   │    │ Make Noise Maths               │
│     (Phase 2)       │    │   (Phase 1)                    │
│                     │    │                                │
│ X1 Out ○────────────┼────┼─▶ Ch1 Signal Input             │
│                     │    │                                │
│ X2 Out ○────────────┼────┼─▶ Ch4 Signal Input             │
│                     │    │                                │
│ t1 Out ○────────────┼────┼─▶ Ch1 Trigger                  │
│                     │    │                                │
│ Y Out  ○────────────┼────┼─▶ Attenuverter 3               │
│                     │    │                                │
│ User-Guided         │    │ Ch1 Unity ○────────────────────┼─── To C&P Castor Pitch
│ Pattern Control     │    │                                │
│                     │    │ Ch4 Variable ○─────────────────┼─── To C&P Pollux Pitch
│ STEPS: 2 o'clock    │    │                                │
│ (Musical patterns)  │    │ SUM Out ○──────────────────────┼─── To C&P Crossfade
│                     │    │                                │
│ DEJA VU: 11 o'clock │    │ OR Out ○───────────────────────┼─── To C&P Mode Control
│ (Slow evolution)    │    │                                │
└─────────────────────┘    └─────────────────────────────────┘
                                    ║      ║    ║    ║
                            CV (Blue)║      ║    ║    ║
                                    ▼      ▼    ▼    ▼
                           ┌─────────────────────────────────┐
                           │  Winterbloom Castor & Pollux   │
                           │    (Intelligent Juno Brain)    │
                           │                                │
                           │ Castor Pitch  ◀─ Algorithmic   │
                           │ Pollux Pitch  ◀─ Pattern       │
                           │ Crossfade     ◀─ Control       │
                           │ Mode Switch   ◀─ User-Guided   │
                           │                                │
                           │ Intelligent Juno Processing   │
                           │                                │
                           │ CROSSFADE OUT ○────────────────┼─── Sophisticated
                           └─────────────────────────────────┘    Juno Music
```

| Algorithmic + Mathematical Chain | Function | Purpose | Advanced Integration |
|--------------------------------|----------|---------|---------------------|
| **Marbles X1,X2 → Maths Ch1,Ch4** | Algorithmic voltage processing | **Intelligent Juno control** | **User-guided pattern processing** |
| **Marbles t1 → Ch1 Trigger** | Algorithmic timing | **Musical envelope generation** | **Pattern-based Juno triggering** |
| **Maths processing** | Mathematical shaping | **Musical Juno modulation** | **Processed algorithmic control** |
| **All CVs → C&P parameters** | Complete control | **Every aspect modulated** | **Sophisticated Juno intelligence** |

**Module Settings:**
- **Marbles:** User-controlled sophisticated pattern generation
- **Maths:** Processes algorithmic patterns into musical Juno control
- **Castor & Pollux:** All parameters under intelligent modulation control
- **Web Editor:** Advanced CV mapping for complete parameter access

**Learning Objectives:**
- **Algorithmic Juno processing:** Sophisticated pattern generation controls vintage character
- **Complete parameter control:** Every aspect of Juno synthesis under intelligent modulation
- **User-guided complexity:** You direct sophisticated systems toward Juno musical goals
- **Advanced system design:** Multi-module ecosystems creating intelligent vintage music

### **Patch 4: Expert - Complete Phase 2 Juno Ecosystem**
```
┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│   DivKid    │ │ Make Noise  │ │ 4ms RCD v2  │ │ Mutable     │
│    Ochd     │ │ Wogglebug   │ │ (Phase 2)   │ │ Marbles     │
│ (Organic)   │ │ (Chaos)     │ │             │ │ (Algorithms)│
│             │ │             │ │ Out 2 ○─────┼─┼─t1 Clock   │
│ LFO 4 ○─────┼─┼─Stepped ○   │ │             │ │             │
│       ║     │ │        ║    │ │ Out 6 ○─────┼─┼─X1 Reset   │
│ Trigger 1○──┼─┼─Disturb     │ │             │ │             │
│             │ │             │ │ Clock In◀───┼─┼─t2 Output  │
└───────║─────┘ └────────║────┘ │             │ │             │
        ║                ║      └─────────────┘ └───────║─────┘
        ▼                ▼                              ║
┌──────────────────────────────────────────────────────║─────┐
│            Winterbloom Castor & Pollux II           ║     │
│              (Juno Command Center)                  ║     │
│                                                      ▼     │
│ Castor Pitch  ◀─ Organic + Chaos + Mathematical + Algorithmic │
│ Pollux Pitch  ◀─ Multi-Intelligence Juno Control            │
│ Crossfade     ◀─ Sophisticated Pattern Processing           │
│ Mode Control  ◀─ Polyrhythmic Character Evolution           │
│ Waveform Mix  ◀─ Intelligent Harmonic Control              │
│                                                            │
│ All Phase 2 Intelligence Types Control Juno Synthesis:    │
│ • Authentic DCO Character with Modern Intelligence         │
│ • 3 Operational Modes under AI Control                    │
│ • Dual Oscillator Relationships                           │
│                                                            │
│ CROSSFADE OUT ○────────────────────────────────────────────┼─── Complete
└────────────────────────────────────────────────────────────┘   Phase 2
                              ║                                 Juno
                         Audio║                              Intelligence
                         (Red)║
                              ▼
                    ┌─────────────────────┐
                    │   Complete Musical  │
                    │     Intelligence    │
                    │                     │
                    │ Organic + Chaos +   │
                    │ Mathematical +      │
                    │ Algorithmic =       │
                    │ Juno Evolution      │
                    │                     │
                    │ System Output ○─────┼─── Evolving Juno
                    └─────────────────────┘       Intelligence
```

**Complete Phase 2 Juno Integration:**

| Intelligence Layer | Function | C&P Control | Musical Evolution |
|-------------------|----------|-------------|-------------------|
| **Organic (Ochd)** | Natural breathing | **Pitch/Crossfade timing** | **Breathing Juno character** |
| **Chaos (Wogglebug)** | Controlled uncertainty | **Mode/Waveform chaos** | **Chaotic Juno evolution** |
| **Mathematical (RCD)** | Precise timing relationships | **Polyrhythmic triggering** | **Mathematical Juno timing** |
| **Algorithmic (Marbles)** | Sophisticated pattern generation | **Intelligent parameter control** | **Intelligent Juno evolution** |
| **Juno (Castor & Pollux)** | Vintage synthesis | **All parameters controlled** | **Complete vintage expression** |

**Expert System Design:**
- **Castor & Pollux as Juno brain:** All Phase 2 intelligence types control every vintage aspect
- **Multi-mode vintage evolution:** 3 different Juno modes respond to 4 intelligence types
- **User-guided vintage sophistication:** You direct sophisticated systems toward Juno musical goals
- **Emergent vintage complexity:** Simple modular interactions create sophisticated vintage music
- **Complete Juno ecosystem:** Every aspect of vintage synthesis controlled by every intelligence type

---

## Common Use Cases

**🎹 **Classic 80s Sounds:** Authentic Juno pads, leads, and bass sounds**
**🌊 **Thick Textures:** Detuned dual oscillators for lush, beating sounds**
**⚡ **Hard Sync Leads:** Metallic, aggressive sounds via oscillator sync**
**🎭 **Performance Instrument:** Live mode switching and crossfading**
**🔄 **Built-in Effects:** Chorus and FM without external modules**
**🎵 **Dual Voice:** Two independent oscillators in one module**
**📱 **Modern Workflow:** USB connectivity for deep customization**
**🏠 **Space Efficient:** Multiple oscillator functionality in compact format**

---

## Beginner "Gotchas"

### **Mode Button Behavior**
- **Tap to change modes:** Quick press cycles through the three modes
- **Hold for tweak overlay:** Long press accesses additional parameters
- **LED feedback:** Color shows mode, animations show state changes
- **Mode affects everything:** Each mode completely changes how the oscillators interact
- **Don't forget tweak mode:** Hold MODE + turn knobs for fine adjustments

### **Waveform Mix Controls Are Tiny**
- **Small trimpots:** Individual waveform levels use small knobs, not large ones
- **Easy to miss:** Beginners often overlook these crucial mixing controls
- **Full CCW = off:** Each waveform mix starts at zero
- **Combined output:** Mixed output is sum of all three waveforms
- **Start simple:** Begin with just RAMP mix up, add PULSE and SUB gradually

### **Expander Separation (Version II)**
- **Main module simplified:** Individual waveform outputs moved to separate expander
- **Expander included:** 2HP module comes with Castor & Pollux II
- **Ribbon cable connection:** Small cable connects main module to expander
- **Optional use:** You don't need the expander for basic operation
- **V1 vs V2:** Version I had all outputs on main panel, Version II uses expander

### **Web Editor Necessity**
- **Advanced features require web editor:** Some functions only accessible via browser
- **USB cable needed:** Micro USB connection to computer required
- **No mobile app:** Browser-based editor works on computers, not phones
- **Calibration important:** Factory calibration may need adjustment for your system
- **Open source advantage:** Community contributions add features over time

### **Non-Linear Pitch Response**
- **Virtual notch:** Pitch knobs are less sensitive in middle range
- **Helps tuning:** Easier to hit musical intervals like octaves and fifths
- **Can confuse:** Knob sensitivity changes across range
- **Follow mode only:** Non-linear response only when tracking CV input
- **Configurable:** Can be adjusted via web editor if desired

---

## Next Steps

1. **Master each mode individually** - spend time with Chorus, LFO FM, and Hard Sync modes
2. **Explore waveform mixing** - understand how RAMP, PULSE, and SUB combine
3. **Practice crossfading** - learn to blend the oscillators expressively
4. **Connect the web editor** - unlock advanced features and customization
5. **Try the expander** - explore individual waveform outputs for complex patches
6. **Experiment with detuning** - use slight pitch differences for thick sounds

**Remember:** Castor & Pollux II is both faithfully vintage and thoroughly modern - embrace both aspects!

---

## Pairs Well With

### **Phase 2 Module Synergies (Modulation & CV Sources):**
- **DivKid Ochd & Expander:** Ochd LFOs → Castor/Pollux parameters for organic Juno evolution
- **Make Noise Wogglebug:** Wogglebug chaos CVs → Mode switching for controlled vintage uncertainty
- **Mutable Marbles:** Marbles X/t outputs → Castor/Pollux for sophisticated algorithmic Juno control
- **4ms RCD v2:** RCD divisions → Mode control for polyrhythmic vintage character switching
- **Cre8audio Function Junction:** Function Junction outputs → C&P for processed vintage modulation
- **Cross-Phase 2 Integration:** All Phase 2 modules can control every aspect of vintage synthesis

### **Phase 1 Module Integration (Core Synthesis):**
- **Make Noise Maths:** Maths envelopes perfect for Castor & Pollux parameter control
- **Juno-style Filters:** Complete the authentic vintage sound chain with appropriate filtering
- **Classic VCAs:** Control dynamics and create expressive vintage patches
- **Traditional Effects:** Reverb/delay processors enhance the vintage character
- **Complete Phase 1 systems:** Castor & Pollux as central vintage voice in classic synthesis chains

### **Essential Vintage Partners:**
- **SEM/MMF Filters:** Complete the authentic Juno sound chain with vintage-style filtering
- **Chorus/Ensemble Processors:** Add external chorus for even lusher vintage sounds
- **Analog Delay/Reverb:** Castor & Pollux loves spacious effects for 80s atmosphere
- **Performance Controllers:** Real-time control over crossfade and mode switching

### **Advanced Vintage Integration:**
- **Multiple Castor & Pollux units:** Layer different vintage processes for complex polyphonic textures
- **Modern Granular Processing:** Contemporary processing on vintage-inspired sounds (Arbhar)
- **Quantized Control:** Ensure musical intervals when using hard sync and algorithmic control
- **Web Editor Integration:** Deep customization for personalized vintage character

---

## Advanced Learning Path

### **Recommended Study Progression:**
1. **Start with Castor & Pollux fundamentals:** Master vintage DCO synthesis, web editor, and mode switching
2. **Add organic vintage breathing:** Integrate DivKid Ochd for natural Juno character evolution (see Ochd guide)
3. **Include chaotic vintage textures:** Use Make Noise Wogglebug for controlled uncertainty in vintage synthesis (see Wogglebug guide)
4. **Add algorithmic vintage intelligence:** Apply Mutable Marbles for sophisticated pattern-based vintage control (see Marbles guide)
5. **Include polyrhythmic vintage timing:** Use 4ms RCD v2 for mathematical vintage character switching (see RCD guide)
6. **Complete the vintage ecosystem:** Add Cre8audio Function Junction for processed vintage modulation (see Function Junction guide)

### **Cross-Module Learning Opportunities:**
- **Castor & Pollux + Ochd:** Learn organic vintage evolution through breathing Juno parameters
- **Castor & Pollux + Wogglebug:** Master chaotic vintage textures with controlled uncertainty
- **Castor & Pollux + Marbles:** Understand sophisticated algorithmic control of vintage synthesis
- **Castor & Pollux + RCD:** Explore polyrhythmic vintage character switching with mathematical precision
- **All Phase 2 + Castor & Pollux:** Build complete vintage ecosystems under intelligent guidance

### **Skill Development Milestones:**
- **Beginner:** Master basic Juno synthesis, web editor, and mode switching
- **Intermediate:** Understand multi-mode vintage systems and CV modulation
- **Advanced:** Create Phase 2 integration patches with sophisticated vintage processing
- **Expert:** Design vintage ecosystems where you guide intelligent vintage systems

### **Advanced Vintage Concepts:**
- **Vintage Character Preservation:** Understand how authentic DCO behavior creates musical character
- **Multi-Parameter Vintage Modulation:** Use multiple intelligence types to control different vintage aspects
- **Organic Vintage Control:** Apply natural breathing to vintage parameter evolution
- **System-Level Vintage Design:** Create patches where multiple modules enhance vintage character together

### **Performance Applications:**
- **Live Vintage Performance:** Real-time vintage character manipulation for live vintage expression
- **Generative Vintage Systems:** Foundation for self-evolving vintage compositions
- **Hybrid Vintage Processing:** Bridge between organic, chaotic, algorithmic, and mathematical vintage control
- **Creative Vintage Direction:** Guide sophisticated systems toward vintage musical expression


---

**Bottom Line:** Castor & Pollux II isn't just a Juno clone - it's a **faithful tribute that enhances the original concept**. It preserves everything that made the Juno-106 special while adding modern features that expand creative possibilities. **You get vintage authenticity with modern reliability and contemporary modular integration.**

---

*Visit [Winterbloom](https://winterbloom.com/store/winterbloom-castor-and-pollux) for complete documentation, web editor access, and open-source hardware/firmware designs. Special thanks to the Winterbloom team for preserving vintage character while embracing modern convenience.*