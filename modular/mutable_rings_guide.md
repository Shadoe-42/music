# Mutable Instruments Rings - Beginner's Guide

![Mutable Instruments Rings](https://github.com/Shadoe-42/music/raw/main/modular/images/mutable_instruments/rings/front_panel.jpg)
*Physical modeling powerhouse with three acoustic resonator algorithms - Modal, Sympathetic, and String models for authentic instrument simulation*

**The Physical Modeling Powerhouse**

---

## Quick Start: Get Your First Resonant Sound in 5 Minutes

**What is Rings?** Think of it as a magic box that turns any sound (or even just a voltage) into beautiful, resonant tones - like striking a bell, plucking a string, or bowing a violin. It doesn't make sound by itself; instead, it takes whatever you feed it and makes it sing with the voice of real physical objects.

### Your First Plucked String
1. **Connect keyboard/sequencer** → **V/OCT input** (bottom)
2. **Connect Rings ODD output** → **your mixer/audio interface**
3. **Press left button** until you see 1 voice (single LED)
4. **Press right button** for green LED (modal resonator)
5. **Play some notes** - Rings creates its own "pluck" sounds automatically!

**Congratulations!** You've just played a virtual string instrument that responds to your melodies with beautiful, decaying resonances!

---

## Essential Parameters (The Big 6)

### **1. Resonator Type Button (Right) + LED Colors**
- **Green LED = Modal Resonator** - bells, chimes, metallic sounds, classic physical modeling
- **Orange LED = Sympathetic Strings** - sitar-like sympathetic resonances, rich harmonics
- **Red LED = String Model** - guitar/violin-like string sounds with nonlinearities
- **Musical impact:** Each mode sounds completely different - explore them all!

### **2. Polyphony Button (Left) + Voice Count**
- **1 Voice = Monophonic** - one note at a time, all 64 filters for maximum quality
- **2 Voices = Duophonic** - two overlapping notes, like fingerpicking
- **4 Voices = Quadraphonic** - chord strumming, multiple decaying notes
- **Trade-off:** More voices = less resolution per voice, but more musical complexity

### **3. FREQUENCY Knob**
- **What it does:** Sets the fundamental pitch/tuning of the resonator
- **Behavior:** Quantized to semitones when V/OCT input is patched
- **Range:** 5 full octaves of precise tuning
- **Sweet spot:** Tune to match your musical material

### **4. STRUCTURE Knob** 
- **What it does:** Changes the harmonic relationships - the "material" of the object
- **Modal mode:** Metal → wood → string materials by changing partial relationships
- **String modes:** Detuning, nonlinearity, and string intervals
- **Magic knob:** This transforms the entire character of the sound

### **5. BRIGHTNESS Knob**
- **What it does:** Controls spectral content from dark to bright
- **Left side:** Low-pass filtering, darker, warmer sounds
- **Right side:** Opens up harmonics, adds brilliance and edge
- **Musical use:** Like tone controls on a guitar amp

### **6. DAMPING Knob**
- **What it does:** Controls how long resonances last (decay time)
- **Range:** From 100ms (short plucks) to 10 seconds (infinite sustain)
- **Musical impact:** Short = percussive, Long = sustained drones
- **Key to character:** This knob defines whether sounds are attacks or sustains


---

## Why This Module Rocks

### **The Philosophy:**
Rings represents **acoustic reality through electronic means** - not just sound synthesis, but authentic simulation of real physical instruments. It bridges the gap between electronic music and acoustic instruments, proving that modular synthesis can create sounds indistinguishable from real bells, strings, and resonant objects.

### **The Innovation:**
- **Three distinct physical modeling algorithms** each simulating different acoustic phenomena
- **Polyphonic voice management** that mimics real instrument behavior
- **Dual outputs with harmonic separation** for spatial acoustic imaging
- **Audio processing mode** transforms any sound into acoustic instruments
- **Built-in decay envelopes** eliminate need for external envelope generators

### **The Practical Benefits:**
- **Space efficiency:** Three complete acoustic instruments in 14HP
- **Learning tool:** Experience acoustic instrument physics hands-on
- **Creative catalyst:** Transform electronic sounds into acoustic reality
- **Complete voice:** Built-in envelopes and polyphony eliminate external processing needs
- **Immediate results:** Every setting sounds musical and acoustic

### **Perfect For:**
- **Electronic producers** wanting to add acoustic realism to electronic music
- **Sound designers** needing authentic acoustic instrument simulation
- **Ambient musicians** creating realistic acoustic spaces and environments
- **Experimental artists** exploring the boundary between electronic and acoustic
- **Small system builders** needing maximum acoustic variety in minimal space
- **Acoustic instrument players** wanting electronic versions of familiar instruments

### **The Magic:**
Rings **democratizes acoustic instrument access** - you don't need to learn violin technique, bell casting, or guitar construction. Just turn knobs and **every acoustic instrument becomes immediately playable**. It's like having a complete acoustic instrument collection that responds to electronic control.

### **Advanced Integration Power:**
As the **acoustic reality engine of Advanced ecosystems**, Rings transforms organic breathing, controlled chaos, Advanced pattern generation, and mathematical processing into authentic acoustic instrument behavior. **You conduct electronic intelligence toward acoustic musical expression.**


---

---

## Progressive Patch Examples

### **Patch 1: First Steps - Basic Physical Modeling**
```
                    ┌─────────────────────┐
                    │   Mutable Rings     │
                    │                     │
     1V/Oct CV ─────┼─▶ V/OCT Input       │
                    │                     │
     Gate/Trig ─────┼─▶ STRUM Input       │
                    │                     │
                    │ FREQUENCY: 12 o'clk │
                    │ STRUCTURE: 12 o'clk │
                    │ BRIGHTNESS:2 o'clk  │
                    │ DAMPING:  10 o'clk  │
                    │ POSITION:  1 o'clk  │
                    │                     │
                    │ Resonator Mode:     │
                    │ Green LED (Modal)   │
                    │                     │
                    │ ODD Output ○───────┼─── Audio (Red)
                    │                     │
                    │ EVEN Output ○──────┼─── Audio (Red)
                    └─────────────────────┘
                             ║       ║
                        Audio║  Audio║
                        (Red)║ (Red) ║
                             ▼       ▼
                    ┌─────────────────────┐
                    │    Stereo Mixer     │
                    │                     │
                    │ Left Input      ◀──┼─── ODD Harmonics
                    │                     │
                    │ Right Input     ◀──┼─── EVEN Harmonics
                    │                     │
                    │ Stereo Output ○───┼─── Physical Modeling
                    └─────────────────────┘
```

| Connection | Cable Type | Purpose | Learning Objective |
|------------|------------|---------|-------------------|
| 1V/Oct CV → V/OCT Input | CV (Blue) | **Harmonic pitch tracking** | **Learn physical modeling fundamentals** |
| Gate/Trigger → STRUM Input | Gate (Yellow) | **Trigger resonant bursts** | **Experience acoustic triggering** |
| ODD Output → Left Mix | Audio (Red) | **Odd harmonics** | **Understand harmonic separation** |
| EVEN Output → Right Mix | Audio (Red) | **Even harmonics** | **Stereo harmonic imaging** |

**Module Settings:**
- **Rings Mode:** Green LED (Modal resonator)
- **Voices:** 1 voice for maximum resolution
- **DAMPING:** 10 o'clock (musical decay time)
- **BRIGHTNESS:** 2 o'clock (bright, present sound)

**Learning Objectives:**
- Understand physical modeling vs. traditional synthesis
- Experience acoustic instrument simulation
- Learn harmonic separation between ODD/EVEN outputs
- Discover natural decay envelopes in physical modeling

**Visual Feedback:**
- **Green LED:** Shows Modal resonator mode
- **Single voice LED:** Maximum quality physical modeling
- **Parameter LEDs:** Show real-time CV modulation
- **Result:** Beautiful bell-like tones with natural acoustic behavior
```
[Sequencer] ──1V/OCT──→ [Rings V/OCT]
[Rings ODD] ──→ [Reverb] ──→ [Audio Out]
```
**Setup:** Green LED (modal), 1 voice, DAMPING around 2 o'clock for musical decay
**Visual:** Single green LED shows modal mode, notes trigger automatically
**Controls:** STRUCTURE changes materials, BRIGHTNESS for tone, POSITION for character
**Sound:** Beautiful, bell-like melodic sequences with natural decay

### **Patch 2: Intermediate - Advanced Organic Evolution with Ochd**
```
   ┌─────────────────────┐      ┌─────────────────────┐
   │   DivKid Ochd      │      │   Mutable Rings     │
   │    (Advanced)      │      │                     │
   │                    │      │                     │
   │ LFO 2 ○────────────┼──────┼─▶ STRUCTURE CV      │
   │       ║            │      │                     │
   │ LFO 4 ○────────────┼──────┼─▶ BRIGHTNESS CV     │
   │       ║            │      │                     │
   │ LFO 6 ○────────────┼──────┼─▶ DAMPING CV        │
   │       ║            │      │                     │
   │ LFO 8 ○────────────┼──────┼─▶ POSITION CV       │
   │       ║            │      │                     │
   │       ║            │      │ Polyphonic Mode:    │
   │       ║            │      │ 4-voice chords      │
   │       ║            │      │                     │
   │       ║            │      │ ODD Output ○───────┼─── Audio (Red)
   │       ║            │      │                     │
   │       ║            │      │ EVEN Output ○──────┼─── Audio (Red)
   └───────║────────────┘      └─────────────────────┘
           ║                           ║       ║
   CV (Blue)║                      Audio║  Audio║
           ▼                      (Red)║ (Red) ║
   ┌─────────────┐                    ▼       ▼
   │ Sequencer/    │           ┌─────────────────────┐
   │ Clock Source  │           │   Spatial Effects   │
   │               │           │                     │
   │ STRUM Trigs○─┼──────────┼─ Left Input      ◀──┼─── ODD
   │               │           │                     │
   └─────────────┘           │ Right Input     ◀──┼─── EVEN
                               │                     │
                               │ Processed Out ○───┼─── Organic Physical
                               └─────────────────────┘     Modeling
```

| Advanced Integration | Rings Parameter | Purpose | Organic Result |
|-------------------|-----------------|---------|----------------|
| **Ochd LFO 2 → Structure CV** | Physical modeling structure | **Evolving resonator character** | **Breathing acoustic spaces** |
| **Ochd LFO 4 → Brightness CV** | Harmonic content | **Organic timbral evolution** | **Natural spectral movement** |
| **Ochd LFO 6 → Damping CV** | Resonance decay | **Living sustain behavior** | **Breathing resonance** |
| **Ochd LFO 8 → Position CV** | Excitation point | **Organic playing technique** | **Natural performance variation** |

**Module Settings:**
- **Rings:** Polyphonic mode for rich harmonic content
- **Ochd Rate:** 1 o'clock for slow, organic parameter evolution
- **All LFOs:** Different phases creating complex organic interactions
- **Spatial processing:** Separate ODD/EVEN outputs for stereo imaging

**Learning Objectives:**
- **Advanced organic integration:** Ochd's breathing modulation applied to physical modeling
- **Multi-parameter organic control:** Multiple aspects of physical modeling evolving together
- **Acoustic space simulation:** Physical modeling creating realistic acoustic environments
- **Stereo physical modeling:** Using dual outputs for spatial acoustic simulation

### **Patch 3: Advanced - Audio Processing Hub with Chaos**
```
   ┌─────────────────────┐      ┌─────────────────────┐
   │ Make Noise        │      │   Mutable Rings     │
   │ Wogglebug         │      │  (Audio Processor)  │
   │ (Chaos)           │      │                     │
   │                   │      │                     │
   │ Smooth VCO ○──────┼──────┼─▶ IN (Audio Input)   │
   │            ║      │      │                     │
   │ Stepped CV ○──────┼──────┼─▶ STRUCTURE CV       │
   │            ║      │      │                     │
   │ Smooth CV  ○──────┼──────┼─▶ BRIGHTNESS CV      │
   │            ║      │      │                     │
   │ Burst Gate ○──────┼──────┼─▶ STRUM Input        │
   │            ║      │      │                     │
   └───────────║──────┘      │ Resonator Mode:     │
          Audio║                 │ Red LED (String)    │
         (Red) ║                 │                     │
               ▼                 │ ODD Output ○──────┼─── Audio (Red)
       ┌─────────────┐         │                     │
       │ Audio Source  │         │ EVEN Output ○─────┼─── Audio (Red)
       │ (Drums, Voice,│         └─────────────────────┘
       │  Noise, etc.) │                      ║       ║
       │               │                 Audio║  Audio║
       │ Audio Out ○───┼────────────────────(Red)║ (Red)║
       └─────────────┘                           ▼       ▼
                                     ┌─────────────────────┐
                                     │   Spatial Effects   │
                                     │                     │
                                     │ Left Input      ◀──┼─── String Harmonics
                                     │                     │
                                     │ Right Input     ◀──┼─── Phase Shifted
                                     │                     │
                                     │ Processed Out ○─┼─── Chaotic Physical
                                     └─────────────────────┘     Modeling
```

| Chaos Processing | Rings Function | Purpose | Advanced Technique |
|------------------|----------------|---------|--------------------|
| **Wogglebug VCO → Audio Input** | Audio processing | **Chaos becomes resonant material** | **Pure chaos transformed into acoustic instruments** |
| **Stepped CV → Structure** | Physical modeling character | **Chaotic structural changes** | **Randomized acoustic materials** |
| **Smooth CV → Brightness** | Harmonic content | **Chaotic spectral evolution** | **Uncertain timbral movement** |
| **Burst → Strum** | Trigger excitation | **Random acoustic strikes** | **Unpredictable acoustic performance** |

**Module Settings:**
- **Rings:** Red LED (String model) for complex nonlinear behavior
- **Wogglebug:** Medium chaos rate for musical randomness
- **Audio processing mode:** Chaos audio becomes resonant string material
- **Dual output processing:** Separate harmonic components for spatial chaos

**Learning Objectives:**
- **Audio processing mastery:** Transform any sound into physical modeling material
- **Chaos as acoustic material:** Controlled uncertainty becomes instrument simulation
- **Complex resonator control:** Multiple chaos sources control acoustic behavior
- **Stereo acoustic processing:** Use harmonic separation for spatial audio design

**Advanced Techniques:**
- **Feedback routing:** Route Rings outputs back to Wogglebug for complex interactions
- **Dynamic acoustic materials:** Structure CV changes acoustic material in real-time
- **Chaotic performance:** Burst triggers simulate unpredictable playing techniques
- **Spatial acoustic modeling:** Dual outputs create stereo acoustic instrument simulation

### **Patch 4: Expert - Complete Advanced Physical Modeling Ecosystem**
```
┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│   DivKid    │ │ Make Noise  │ │ Mutable     │ │ 4ms RCD v2  │
│    Ochd     │ │ Wogglebug   │ │  Marbles    │ │ (Phase 2)   │
│ (Organic)   │ │ (Chaos)     │ │ (Patterns)  │ │             │
│             │ │             │ │             │ │ Div 1 ○─────┼─┼─Poly Clock  │
│ LFO 1 ○─────┼─┼─Smooth ○    │ │ X1 Out ○───┼─┼─             │
│       ║     │ │        ║    │ │       ║     │ │ Div 3 ○─────┼─┼─Mono Clock  │
│ LFO 3 ○─────┼─┼─Stepped ○   │ │ X2 Out ○───┼─┼─             │
│       ║     │ │        ║    │ │       ║     │ │ Div 5 ○─────┼─┼─Trigger     │
│ LFO 7 ○─────┼─┼─Woggle ○    │ │ t1 Out ○───┼─┼─             │
│       ║     │ │        ║    │ │       ║     │ │             │
└───────║─────┘ └────────║────┘ └───────║─────┘ └─────────────┘
        ║                ║              ║
        ▼                ▼              ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                              Mutable Rings                              │
│                        (Physical Modeling Hub)                        │
│                                                                        │
│ STRUCTURE CV     ◀─ Organic + Chaos + Pattern Material Control         │
│ BRIGHTNESS CV    ◀─ Spectral Evolution via Multi-Source Modulation      │
│ DAMPING CV       ◀─ Decay Time Control for Acoustic Realism             │
│ POSITION CV      ◀─ Playing Technique Simulation                         │
│ STRUM Input      ◀─ Polyrhythmic Triggering via Mathematical Timing      │
│ V/OCT Input      ◀─ Pattern-Based Harmonic Control                       │
│                                                                        │
│ Three Resonator Models Available:                                      │
│ • Modal (Green): Bell/chime simulation                                │
│ • Sympathetic (Orange): Sitar-like resonances                        │
│ • String (Red): Guitar/violin simulation                             │
│                                                                        │
│ Polyphonic Voices: 1/2/4 voice modes for complexity vs. quality       │
│                                                                        │
│ ODD Output ○─────────────────────────────────────────────────┼─── Complete
│                                                                        │
│ EVEN Output ○────────────────────────────────────────────────┼─── Phase 2
└──────────────────────────────────────────────────────────────────────────────┘   Physical
                              ║                                 Modeling
                         Acoustic║
                         Models║
                              ▼
                    ┌─────────────────────┐
                    │   Complete Musical  │
                    │     Ecosystem       │
                    │                     │
                    │ Organic + Chaos +   │
                    │ Patterns + Math =   │
                    │ Living Instruments  │
                    │                     │
                    │ System Output ○─────┼─── Acoustic Reality
                    └─────────────────────┘       from Electronics
```

**Complete Advanced Physical Modeling Integration:**

| Intelligence Layer | Function | Rings Control | Musical Result |
|-------------------|----------|---------------|----------------|
| **Organic (Ochd)** | Natural breathing | **Structure/Brightness modulation** | **Breathing acoustic instruments** |
| **Chaos (Wogglebug)** | Controlled uncertainty | **Position/Damping modulation** | **Unpredictable playing techniques** |
| **Pattern (Marbles)** | Sophisticated sequences | **V/OCT + trigger control** | **Musical phrase generation** |
| **Mathematical (RCD)** | Polyrhythmic timing | **STRUM polyrhythmic triggers** | **Complex acoustic rhythms** |
| **Physical (Rings)** | Acoustic simulation | **Complete instrument modeling** | **Realistic acoustic instruments** |

**Expert System Design:**
- **Rings as acoustic reality engine:** All Advanced pattern generation becomes realistic instruments
- **Multi-source acoustic control:** Every aspect of instrument behavior under sophisticated control
- **User-guided acoustic performance:** You direct sophisticated pattern generation toward acoustic realism
- **Emergent acoustic complexity:** Simple electronic sources become complex acoustic instruments
- **Complete acoustic ecosystem:** Every control type creates different aspects of acoustic reality

**Advanced Performance:**
1. **Organic foundation:** Ochd establishes natural breathing in acoustic behavior
2. **Mathematical structure:** RCD provides polyrhythmic acoustic triggering
3. **Pattern sophistication:** Marbles provides musical phrase control
4. **Chaos expression:** Wogglebug adds unpredictable playing technique variation
5. **Acoustic transcendence:** All electronic intelligence becomes acoustic instrument reality

```
**Result:** Complex self-modulating textures with stereo output

---

## Common Use Cases

1. **🎵 Melodic Resonator:** Transform sequences into bell-like, stringed, or metallic melodies
2. **🎸 String Simulator:** Polyphonic chord strumming and fingerpicked patterns
3. **🔊 Audio Processor:** Turn any sound into harmonic, resonant versions
4. **🏴 Drone Generator:** Create rich, evolving textures from simple inputs
5. **🥁 Percussion Processor:** Make drum hits ring with pitched resonances
6. **🎹 Complete Voice:** No need for external envelopes - built-in decay envelopes
7. **🎛️ Modulation Target:** All parameters respond beautifully to CV control
8. **🌌 Ambient Engine:** Physical modeling creates realistic acoustic spaces and environments

---

## Beginner "Gotchas" & Pro Tips

### **⚠️ Common Mistakes:**

**"It's Not An Oscillator"**
- **Rings doesn't generate sound** - it processes or responds to input
- **No input = internal exciter** - it creates its own "pluck" or "strike" when triggered
- **Think "instrument" not "oscillator"** - you're striking/plucking/bowing a virtual object
- **Different from traditional synthesis** - this is physical modeling, not subtractive

**"Three Completely Different Models"**
- **Green ≠ Orange ≠ Red** - each LED color is essentially a different instrument
- **Same knob, different function** - STRUCTURE means different things in each mode
- **Don't expect consistency** - embrace the unique character of each model
- **Modal (green) most versatile** - good starting point for beginners

**"Polyphony is About Overlapping Decay"**
- **Not traditional polyphony** - no multiple CV inputs or keyboard splitting
- **Voices overlap and decay together** - like real string instruments
- **4-voice = lower quality per voice** - trade resolution for complexity
- **STRUM input manages voice allocation** - controls which voice gets the new note

### **🎵 Pro Tips:**

**Two Outputs with Different Content:**
- **ODD and EVEN are not stereo** - they carry different harmonic components
- **Modal mode:** Odd/even numbered harmonics split between outputs
- **String modes:** Phase-shifted components create stereo-like effects
- **Mono operation:** Only plug ODD output for summed signal
- **Stereo magic:** Both outputs to separate channels creates width and movement

**External Audio Input Changes Everything:**
- **IN input transforms the module** - becomes an audio processor instead of instrument
- **Any audio works** - percussion, voice, noise, other instruments
- **Continuous vs percussive** - different input types create different behaviors
- **Volume matters** - modular levels expected (loud signals for best results)

**Model Exploration Strategy:**
- **Master one mode at a time** - start with Modal (green), learn its sweet spots
- **Experiment with external inputs** - try processing different audio sources
- **Explore polyphonic modes** - understand how voice overlap creates musical textures
- **Use both outputs** - stereo processing opens up spatial possibilities
- **Add CV modulation** - slow parameter changes create evolving, organic sounds

---

## Advanced Learning Path

### **Recommended Study Progression:**
1. **Start with Rings fundamentals:** Master all three resonator models and polyphonic voice management
2. **Add organic evolution:** Integrate DivKid Ochd for breathing acoustic parameter control (see Ochd guide)
3. **Include controlled chaos:** Use Make Noise Wogglebug for chaotic acoustic parameter evolution (see Wogglebug guide)
4. **Add pattern sophistication:** Apply Mutable Marbles for sophisticated acoustic pattern control (see Marbles guide)
5. **Include polyrhythmic triggering:** Use 4ms RCD v2 for mathematical acoustic timing (see RCD guide)
6. **Complete the ecosystem:** Add Cre8audio Function Junction for processed acoustic modulation (see Function Junction guide)

### **Cross-Module Learning Opportunities:**
- **Rings + Ochd:** Learn organic acoustic parameter control across all three physical modeling algorithms
- **Rings + Wogglebug:** Master chaotic modulation of acoustic parameters for controlled uncertainty
- **Rings + Marbles:** Master sophisticated pattern-based control of acoustic instruments
- **Rings + RCD:** Explore polyrhythmic acoustic triggering with mathematical precision
- **All Advanced + Rings:** Build complete acoustic ecosystems with multiple pattern generation types under your guidance

### **Skill Development Milestones:**
- **Beginner:** Master individual resonator models and basic acoustic parameter control
- **Intermediate:** Understand polyphonic voice management and CV control of acoustic parameters
- **Advanced:** Create Advanced integration patches with sophisticated acoustic pattern generation
- **Expert:** Design acoustic ecosystems where you guide sophisticated pattern generation toward realistic instruments

### **Advanced Physical Modeling Concepts:**
- **Multi-Modal Acoustic Simulation:** Understand how three different physical modeling algorithms respond to modulation
- **Pattern-Based Acoustic Control:** Use sophisticated pattern generation to guide acoustic instrument behavior
- **User-Directed Acoustic Evolution:** Guide sophisticated systems toward acoustic realism
- **System Integration:** Design patches where you control multiple pattern generation types for acoustic simulation

### **Performance Applications:**
- **Live Acoustic Control:** Real-time acoustic parameter control and model switching
- **Generative Acoustic Systems:** Foundation for self-evolving acoustic compositions under your creative guidance
- **Hybrid Acoustic Processing:** Bridge between electronic and acoustic music creation
- **Creative Acoustic Direction:** Guide sophisticated pattern generation systems toward acoustic musical expression


---

**Bottom Line:** Rings isn't just a resonator - it's an **acoustic instrument laboratory** that brings the sound and behavior of real physical instruments to modular synthesis. Every patch teaches you something new about acoustic instrument physics and musical expression. As the **acoustic reality engine of Advanced ecosystems**, it transforms electronic pattern generation into living, breathing acoustic instruments under your creative direction.**

---

## Pairs Well With

### **Advanced Module Synergies (Modulation & CV Sources):**
- **DivKid Ochd & Expander:** Ochd LFOs → Rings Structure/Brightness/Damping for organic acoustic evolution
- **Make Noise Wogglebug:** Wogglebug chaos CVs → Rings parameters for controlled uncertainty in acoustic simulation
- **Mutable Marbles:** Marbles X/t outputs → Rings V/OCT/STRUM for sophisticated pattern-based acoustic control
- **4ms RCD v2:** RCD divisions → Rings STRUM for polyrhythmic acoustic triggering
- **Cre8audio Function Junction:** Function Junction outputs → Rings Position/Damping for processed acoustic modulation
- **Cross-Advanced Integration:** All Advanced modules can control every aspect of physical modeling under your creative direction

### **Phase 1 Module Integration (Core Synthesis):**
- **Make Noise Maths:** Maths envelopes perfect for Rings Brightness/Damping control and acoustic dynamics
- **Mutable Plaits:** Plaits audio outputs → Rings IN for processed physical modeling synthesis
- **Mob of Emus:** Harmonic series pairs perfectly with Rings modal resonator models for mathematical acoustic harmony
- **Disting mk4:** Use as audio processor/analyzer for Rings outputs or complex CV generation
- **Complete Phase 1 systems:** Rings as acoustic reality engine for electronic synthesis networks

### **Essential Physical Modeling Partners:**
- **Audio Sources:** Any audio → Rings IN transforms sounds into acoustic instruments
- **Reverb/Delay Processors:** Physical modeling + spatial effects = complete acoustic environments
- **VCAs/Mixers:** Balance between ODD/EVEN outputs for stereo acoustic imaging
- **External Filters:** Parallel processing of Rings outputs for complex acoustic textures

### **Advanced Acoustic Integration:**
- **Multiple Rings:** Layer different resonator models for complex polyphonic acoustic textures
- **Contact Microphones:** Real acoustic excitation for authentic physical modeling
- **Performance Controllers:** Real-time acoustic parameter control and model switching
- **Analysis Tools:** Visualize resonator behavior and understand physical modeling mathematics

---

*Need the full technical manual? Find it at mutable-instruments.net/modules/rings*