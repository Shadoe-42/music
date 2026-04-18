---
title: Tiptop Audio Forbidden Planet
manufacturer: Tiptop Audio
primary_role: SHAPER
secondary_roles: [SOURCE]
form_factor: eurorack
functions: [filter]
behavior_tags: [warm, clean, stable, nonlinear, reactive]
use_cases: [timbral movement and shaping, filter as primary voice character, lead voice when self-oscillating]
hp: 8
---

# Tiptop Audio Forbidden Planet

**The Steiner-Parker Synthacon Filter Reborn**

---

## Quick Start: Get Your First Sound in 5 Minutes

**What is Forbidden Planet?** An analog multimode filter inspired by the legendary 1975 Steiner-Parker Synthacon, featuring three separate inputs (HP, BP, LP) instead of typical mode switching. It's famous for its crisp high-pass filtering, unique resonance behavior, and sci-fi self-oscillation capabilities.

### Your First Classic Lowpass Sweep
1. **Turn RESO** all the way down (counterclockwise)
2. **Patch sawtooth wave** → **LP IN** (lowpass input)
3. **Set VOLUME** to around 3 o'clock
4. **Connect output** → your mixer/amp
5. **Slowly turn FREQUENCY** knob full scale - hear the classic filter sweep
6. **Gradually increase RESO** - listen as it goes from smooth to self-oscillating madness!

### Discover the Signature High-Pass
1. **Unplug from LP IN** and **patch same signal** → **HP IN**
2. **Set FREQUENCY to minimum** (9 o'clock)
3. **Slowly turn FREQUENCY up** - notice how highs cut through with "no residue"
4. **Try on kick drums** - removes rumble while keeping punch!

---

## Essential Parameters (The Big 5)

### **1. Three Input Jacks (HP, BP, LP)**
- **HP IN:** High-pass input - "signature sound" with crisp, sharp cuts
- **BP IN:** Band-pass input - isolates "pie-slice" frequency ranges  
- **LP IN:** Low-pass input - classic "airy" 12dB/octave slope
- **Unique feature:** Can use all three simultaneously for complex filtering
- **Key difference:** Inputs, not outputs - each processes signal differently

### **2. FREQUENCY Control**
- **What it does:** Sets cutoff frequency for all active filter modes
- **Range:** Wide frequency sweep from bass to treble
- **Behavior:** Works in "reverse direction" for HP compared to LP
- **Performance control:** Primary real-time filter manipulation

### **3. RESO (Resonance)**
- **What it does:** Internal feedback path emphasizing cutoff frequencies
- **Low settings:** Smooth harmonic emphasis
- **Medium settings:** Self-oscillation begins (filter becomes sine oscillator)
- **Maximum settings:** "Aggressive and scattered" - chaotic, grainy sci-fi tones
- **Unique trait:** Volume doesn't drop when resonance increases (unlike many filters)

### **4. CV Inputs (Attenuated + Full)**
- **Attenuated CV:** Has dedicated attenuator knob for precise control
- **Full CV:** Direct CV input with no attenuation
- **Use both:** Combine envelope + LFO modulation simultaneously
- **Creative tip:** Manual suggests trying audio signals in CV inputs!

### **5. VOLUME Control**
- **What it does:** Master output level control
- **Necessity:** No input level controls, so output volume is your gain staging
- **Range:** Controls final output from filter circuit
- **Performance use:** Quick level adjustments during play

---

## Understanding the Steiner-Parker Heritage

### **What Made the Original Special:**
- **1975 Steiner-Parker Synthacon** - rare analog synthesizer with unique filter design
- **Opposite polarity** compared to Moog/ARP filters of the era
- **Volume retention** when resonance increases (most filters get quieter)
- **Aggressive self-oscillation** with complex harmonic content
- **Three separate inputs** for innovative signal routing

### **Forbidden Planet's Modern Adaptation:**
- **Same core circuit** adapted for Eurorack
- **Improved stability** while retaining character
- **Compact 8HP format** vs. original large format
- **CV control** added for modular integration
- **Affordable** access to legendary filter sound

### **The Sci-Fi Connection:**
- **Named after 1956 film** "Forbidden Planet" with 100% electronic soundtrack
- **"Electronic tonalities"** - what the Musician's Union called it (refusing to call it music!)
- **Aggressive resonance** perfect for laser zaps and sci-fi effects
- **Self-oscillation chaos** creates otherworldly textures

---

## Why This Instrument Excels

**The Heritage:**
Forbidden Planet brings the legendary Steiner-Parker Synthacon filter - one of the most distinctive filters in synthesizer history - into the affordable Eurorack format. This isn't just another filter; it's a piece of analog synthesis history.

**The Unique Approach:**
- **Three inputs instead of mode switching** - completely different workflow
- **Volume-retaining resonance** - unusual behavior that sounds musical
- **Aggressive self-oscillation** - perfect for sound design and sci-fi effects
- **HP signature sound** - crisp, clean high-pass filtering unlike anything else

**The Practical Benefits:**
- **Compact 8HP** - legendary filter sound in minimal space
- **Low power consumption** - 10mA on both rails
- **Affordable** - access to rare Synthacon character without vintage prices
- **Multiple uses** - filter, oscillator, processor, effect

**Perfect For:**
- **Electronic musicians:** Seeking classic analog character with modern convenience
- **Sound designers:** Unique resonance and self-oscillation for sci-fi effects
- **Mix engineers:** Excellent high-pass filtering for cleaning up mixes
- **Vintage synth fans:** Experience legendary Synthacon sound in modular format
- **Anyone wanting distinctive filtering:** Sounds unlike Moog, ARP, or other common filters

---

## Historical Context

Nyle Steiner was born in 1945 in American Fork, Utah, and came to synthesis from the performer's side of the room. A classically trained trumpet player who had worked with the Utah Symphony, he spent the early 1970s designing electronic instruments that could give wind players the same expressive vocabulary over synthesizer voices that a brass player already had over pitch, dynamics, and articulation; that work eventually became the EVI, Electronic Valve Instrument. That starting point matters: Steiner understood a filter not as a circuit specification but as something a musician would hold and move in real time. When he formed Steiner-Parker with electrical engineer Dick Parker and launched the Synthacon in 1975 as an affordable competitor to the Minimoog and ARP Odyssey, that performing musician's perspective ran through every decision.

The filter Steiner designed for the Synthacon was built on a Sallen-Key topology, a circuit architecture published in 1955 by R.P. Sallen and E.L. Key at the MIT Lincoln Laboratory. The topology gave Steiner an efficient two-pole 12dB per octave slope, but what he did with it structurally had no precedent in production synthesizers. Every other multimode filter of the era routed a single input signal through the circuit and selected low-pass, high-pass, or bandpass at the output. Steiner inverted this logic: three separate inputs, one for each filter mode, feeding into a single output. You selected the response by choosing which input to send signal into, not which output to read from. Multiple signals could enter different inputs simultaneously and the filter would process all of them internally, each path interacting with the others before reaching the output. The three inputs were not a convenience feature; they were a fundamentally different model of what a filter is for.

The filter also behaved differently from the transistor-ladder designs that Moog and ARP had made standard. In a ladder filter, the internal feedback path that builds resonance pulls energy away from the main signal, so increasing resonance drops output volume. Players learned to compensate by pushing level as they pushed resonance, until the two adjustments became a single learned habit. Steiner's positive feedback approach kept output volume stable through the full resonance range. Resonance could be used as a purely tonal decision, not a gain management problem. At maximum settings the filter self-oscillated aggressively, producing complex harmonic content rather than the relatively clean sine that most filters generated, and the volume held steady all the way to chaos.

The Synthacon was manufactured between 1975 and 1979, and the filter circuit largely disappeared from production instruments for the following decades. It survived in DIY documentation and a small community of builders who recognized the distinctive behavior of the three-input design. Tiptop Audio brought it into the Eurorack format as Forbidden Planet, named after the 1956 science fiction film, which was the first major Hollywood production to use a fully electronic score. Louis and Bebe Barron built custom ring modulators and manipulated tape to produce sounds the Musician's Union refused to classify as music. The name connects the module to that moment: a piece of technology that arrived before the mainstream had a framework for it, doing something structurally unlike what came before it, named for the place where that kind of sound was expected to originate.

---

## Patches

### **Patch 1: Classic Analog Bass**
- **Sawtooth oscillator** → **LP IN**
- **Bass sequence** controls oscillator pitch
- **Envelope generator** → **Full CV Input**
- **FREQUENCY at 9 o'clock**, **RESO at 1 o'clock**
- **Result:** Classic analog bass with Synthacon character

### **Patch 2: Drum Processing Magic**
- **Kick drum** → **HP IN** (removes rumble, keeps punch)
- **Snare drum** → **BP IN** (isolates snare frequencies)
- **Hi-hats** → **LP IN** (smooths harsh highs)
- **Mix all three inputs** for complete drum processing
- **Result:** Multi-band drum processing in one module

### **Patch 3: Sci-Fi Sound Design**
- **Any oscillator** → **BP IN**
- **RESO at maximum** (chaotic self-oscillation)
- **LFO** → **Attenuated CV** (frequency sweeps)
- **Manual FREQUENCY tweaks** for alien textures
- **Result:** Perfect Forbidden Planet soundtrack sounds!

### **Patch 4: Expert - Three-Input Simultaneous Processing**

This patch uses all three inputs at once, the defining capability of the Steiner-Parker architecture. Most patches route a single source through one input. This configuration sends three different audio sources into HP, BP, and LP simultaneously while two independent modulation sources drive both filter parameters at different rates.

```
[Plaits Main Out]    ---> [HP Input]
[Plaits Aux Out]     ---> [BP Input]
[HP + BP mix]        ---> [LP Input]

[Ochd LFO 2]         ---> [FREQUENCY CV]
[Wogglebug Stepped]  ---> [ATTENUATED CV]  (attenuator at 9 o'clock)
[Ochd LFO 6]         ---> [FULL CV]

[RCD Div 2]          ---> clock reference
[RCD Div 4]          ---> polyrhythmic subdivision

[MAIN OUTPUT]        ---> VCA -> out
```

**Setup:**
1. Patch Plaits Main Out -> HP Input
2. Patch Plaits Aux Out -> BP Input
3. Use a mult or mixer to combine both Plaits outputs -> LP Input, or route any other audio source into LP
4. Ochd LFO 2 -> Frequency CV Input
5. Wogglebug Stepped Out -> Attenuated CV Input; set attenuator to 9 o'clock
6. Ochd LFO 6 -> Full CV Input
7. Start with FREQUENCY at 12 o'clock, RESO at 10 o'clock
8. Raise RESO slowly until tonal emphasis appears; stop before self-oscillation unless that is the goal

**What to listen for:** HP and BP process the two Plaits outputs differently before the LP stage handles the combined material. All three paths respond to FREQUENCY together, so sweeping the knob moves everything simultaneously. Ochd LFO 2 on FREQUENCY creates a slow organic sweep; Wogglebug Stepped on the attenuated input adds irregular lurches at unpredictable intervals on top of that motion. Because LFO 2 and LFO 6 run at unrelated rates, frequency and resonance evolve independently and drift in and out of phase with each other over time.

The attenuator controls how far the filter moves on each Wogglebug step. At low settings the steps add subtle tonal emphasis; at higher settings they become dramatic filter jumps layered over the organic sweep.

---

## Advanced Learning Path

**Multiple Input Usage:**
- **Send same signal** to multiple inputs for parallel processing
- **Different signals** to each input for complex mixing
- **Crossfade between inputs** by varying their source levels
- **Creative routing:** Use inputs as a primitive mixer with filtering

**Resonance Exploration:**
- **Self-oscillation mode:** Remove audio input, crank RESO, use as sine oscillator
- **Frequency tracking:** Use 1V/Oct into CV input for musical self-oscillation
- **Chaos mode:** Maximum RESO for grainy, unstable tones
- **Performance resonance:** Real-time RESO sweeps for dramatic effects

**CV Modulation Strategies:**
- **Envelope + LFO:** Use both CV inputs for complex modulation
- **Audio rate CV:** Try audio signals in CV inputs for FM-like effects
- **Inverted envelopes:** Reverse filter movement for unusual effects
- **Random CV:** Create unpredictable filter movement

---

## Common Use Cases

1. **🎵 Analog Bass Synthesis:** LP input for classic bass lines with Synthacon character
2. **🥁 Drum Processing:** HP input removes unwanted low frequencies while keeping punch
3. **🎸 Lead Synthesis:** BP input for focused, cutting leads and vocal textures
4. **🎭 Sound Design:** Unique resonance for sci-fi and experimental textures
5. **🎚️ Mix Processing:** Clean up muddy mixes with surgical frequency control
6. **🎛️ Creative Effects:** Resonance sweeps for build-ups and breakdowns
7. **🎤 Live Performance:** Real-time filtering with immediate hands-on control

---

## Pairs Well With

**Modulation Sources:**
- **DivKid Ochd & Expander:** Eight independent LFOs allow simultaneous modulation of FREQUENCY CV, attenuated CV, and Full CV at different rates. Routing different LFOs to different parameters creates complex multi-rate filter motion without additional modules.
- **Make Noise Wogglebug:** Stepped output through the attenuated CV input gives the filter irregular, unpredictable lurches; Smooth output provides continuous wandering sweeps. The combination of Wogglebug and Ochd into both CV inputs simultaneously creates layered modulation with very different characters on the same sweep.
- **Make Noise Maths:** Maths-generated envelopes applied to Full CV create precise attack and decay filter shapes. Using Maths as a function generator with manual triggering allows live, performance-oriented filter control.

**Synthesis Sources:**
- **Mutable Instruments Plaits:** Plaits Main and Aux outputs carry different synthesis material from the same voice. Routing them into HP and BP simultaneously uses the two-signal capability of the three-input design directly.
- **Mutable Instruments Rings:** Forbidden Planet HP input reshapes Rings acoustic modeling and removes the low-frequency resonances that can dominate modal synthesis. Running Rings into HP and a separate oscillator into LP creates a patch where two sources share one filter with different spectral characters.
- **Expert Sleepers Disting mk4:** Disting running a quantizer algorithm provides pitch-tracked CV for self-oscillation sequences. The filter tracks V/Oct through the CV input for musical self-oscillation across the keyboard.

**Rhythm and Timing:**
- **4ms RCD v2:** Gate outputs from multiple RCD divisions trigger envelopes patched to the CV inputs, creating rhythmic filter sweeps that move at polyrhythmic rates relative to the main clock.

**Processing:**
- **VCAs and Mixers:** A mixer before the LP input allows blending multiple audio sources into a single path while HP and BP handle individual sources. Parallel processing, mixing Forbidden Planet output with dry signal, preserves low-frequency body that aggressive HP filtering removes.
- **Reverb and Delay:** Self-oscillation and resonance feed into time-based effects in interesting ways. The aggressive resonance character of the Steiner-Parker topology creates sustained spatial textures in reverb that other filters rarely achieve.

**Multiple Forbidden Planets:**
- Running two in series, one for high-frequency shaping and one for low, uses the three-input architecture in each to build a flexible multi-band processing chain from two identical modules.

---

## Common Mistakes

### **Common Mistakes:**

**"The high-pass works backwards!"**
- HP frequency control is inverted compared to LP - this is normal
- **Solution:** For HP, low FREQUENCY = more highs, high FREQUENCY = less highs

**"I can't get the resonance to self-oscillate!"**
- Need to find the right frequency range for self-oscillation
- **Solution:** Try different FREQUENCY positions while increasing RESO

**"The filter doesn't have enough low-end when self-oscillating!"**
- Known limitation - self-oscillation cuts out below ~150Hz
- **Solution:** Use other filters for low-frequency self-oscillation, or layer with sub-oscillators

### **Pro Tips:**

**Input Selection Strategy:**
- **LP IN:** For traditional filter sweeps, bass synthesis, warm sounds
- **HP IN:** For crisp cuts, drum processing, removing mud
- **BP IN:** For focused leads, vocal textures, frequency isolation

**Resonance Sweet Spots:**
- **9-11 o'clock:** Subtle harmonic emphasis
- **12-2 o'clock:** Musical resonance without self-oscillation  
- **3-4 o'clock:** Self-oscillation begins - filter becomes oscillator
- **5 o'clock:** Maximum chaos - grainy, aggressive sci-fi tones

**CV Modulation Tips:**
- **Use both CV inputs:** Envelope for dynamics, LFO for movement
- **Attenuated CV:** Start with small amounts, increase gradually
- **Audio rate modulation:** Try audio signals in CV inputs for complex interactions
- **1V/Oct tracking:** When self-oscillating, filter tracks musically

**Performance Techniques:**
- **Resonance sweeps:** Classic build-up and breakdown technique
- **Input hopping:** Move signals between inputs for instant timbre changes
- **Self-oscillation mode:** Remove input, use filter as sound source
- **Multiple inputs:** Process different elements of your mix simultaneously



---


---

*Visit [Tiptop Audio](http://tiptopaudio.com/) for complete documentation and more innovative Eurorack modules*