---
title: 4ms Company Listen IO
manufacturer: 4ms Company
primary_role: UTILITY
secondary_roles: [ROUTER]
form_factor: eurorack
functions: [audio-interface]
behavior_tags: [clean, stable, linear, reactive]
use_cases: [stereo output to external mixer, headphone monitoring in patch, recording Eurorack audio]
hp: 6
memory: none
transport: none
screen: false
hybrid: false
cv: none
historical_context: false
---

# 4ms Company Listen IO

**Bidirectional Audio Interface for Modular Systems**

![4ms Company Listen IO](https://github.com/Shadoe-42/music/raw/main/modular/images/4ms/listen_io/front_panel.jpg)   
*4ms Company Listen IO - Dual-section audio interface showing Line In/Mod Out (top) and Mod In/Line Out (bottom)*

---

## Quick Start

**What is 4ms Company Listen IO?** A 6HP bidirectional audio interface with two independent conversion stages: the top section amplifies external signals up to modular levels (up to 30x gain), and the bottom section attenuates modular signals down to line and headphone levels. Dual LED bar graphs monitor both stages simultaneously.

**Key Specifications:**

| Spec | Value |
|------|-------|
| Width | 6HP |
| Depth | ⚠️ Verify against official documentation |
| Power | ⚠️ Verify against official documentation |
| Input gain range | Up to +30dB (~30x voltage gain) |
| Mod Out level | Up to 22Vpp |
| Level control | -∞ to 0dB (attenuation only, no boost) |
| Headphone outputs | Dual (left = normal stereo, right = swapped stereo) |

### Your First External Connection
1. Connect external source to the top Line In jack (left jack for mono sources)
2. Adjust the Gain knob while watching the top LED bar graph for optimal level
3. Patch the top Mod Out jack to a modular destination (VCA, filter, effects module)
4. Patch your modular output to the bottom Mod In jack
5. Connect headphones to the bottom Line Out jack
6. Adjust the Level knob to a comfortable monitoring volume

**Watch the LEDs:** Top LEDs show input signal after gain is applied; aim for 4-6 active on louder passages without the red clipping light. Bottom LEDs show output level after attenuation; no red indicator here, as the output stage cannot clip.

---

## Essential Parameters

### Line to Modular Section (Top Half)

**Line In Jacks**

The two Line In jacks accept external signals ranging from instrument-level sources (electric guitars, basses, most dynamic microphones) through line-level equipment (keyboards, synthesizers, audio interfaces, effects processors, portable recorders, phones). Both jacks are mono; use the left jack for mono sources or the left channel of stereo sources. Phantom-powered condensers and electret microphones are not compatible, as the jacks provide no phantom power. The INS header on the rear of the panel exposes the same inputs in a different physical format for adaptor modules; signals from both the jacks and the header sum when both are connected simultaneously.

**Gain**

The Gain knob controls amplification from silence to approximately 30x voltage gain at maximum, acting on both channels simultaneously. This is the only active amplification stage in the module: it brings weak external signals up to modular-compatible operating levels. The correct setting depends entirely on the source. A hot keyboard synthesizer may need Gain below 9 o'clock; a passive guitar pickup with low output may need it near maximum. The LED bar graph is the calibration tool; set Gain by what the LEDs show, not by feel or expectation.

**LED Bar Graphs (Input Section)**

Two LED columns display signal level after Gain is applied, one column per channel. More LEDs lit means stronger signal; the top LED illuminates red when the signal clips. Clipping means the circuit has run out of headroom and the peak of the waveform is being hard-limited, creating harmonic distortion that cannot be removed by any downstream processing. The target is strong signal (typically 4-6 LEDs active during louder passages) without the red LED illuminating. Intentional input saturation is a deliberate sound design choice; accidental clipping from poor gain staging is not.

**Mod Out Jacks**

The two black Mod Out jacks output the amplified signals at modular levels, up to 22 volts peak-to-peak. Left input routes to left output; right input routes to right output. These outputs can drive multiple modular destinations simultaneously through passive multiples or active distributors without significant level degradation.

**INS Header**

A 3-pin expansion header exposing the same Line In signals in a different physical format for adaptor modules such as the 4ms Listen Up. Left channel is on the bottom pin, right channel on the top pin, ground at center. Signals from both the 3.5mm jacks and the header sum when both carry signals simultaneously.

### Modular to Line Section (Bottom Half)

**Mod In Jacks**

The bottom section accepts modular-level signals for conversion downward to line and headphone levels. Patch your final modular mix, individual voices, or any modular signal destined for external equipment or headphone monitoring here. Left and right jacks are independent; a signal present only in the left jack appears only on the left output channel.

**Level**

The Level knob controls attenuation only, from silence to unity gain (0dB) at maximum. It provides no amplification. This is intentional: modular signals are already at high voltage, and the Level stage's function is reducing them to appropriate levels for external equipment and headphones. Starting with Level at minimum and raising it to the desired monitoring volume is the correct workflow. The bottom section cannot clip regardless of how hot the modular input is, because attenuation can only reduce signal.

**LED Bar Graphs (Output Section)**

Two LED columns in the bottom section display the attenuated output level after the Level knob is applied. The display behavior is identical to the input bar graphs with one critical difference: no red clipping LED. The output stage can only reduce signal, so clipping cannot occur here. The bar graphs confirm signal presence and help calibrate output levels for connected equipment.

**Line/Headphones Out Jacks**

The two black Line/Headphones Out jacks serve a dual function: they output line-level signals to external equipment and drive headphones directly from the same jacks. The left jack outputs normal stereo; the right jack outputs swapped stereo, where the left channel signal appears in the right ear and vice versa. Both jacks can be used simultaneously for two-person monitoring sessions.

**OUTS Header**

A 3-pin expansion header providing the same line-level signals as the Line Out jacks, without headphone driving capability. Both the jacks and the header can be used simultaneously, allowing the module to feed multiple output destinations at once.

---

## Why This Excels

Listen IO's value comes from a specific architectural insight: professional modular synthesis does not exist in isolation. It exists in a studio containing instruments, effects processors, mixing consoles, monitoring systems, and recording infrastructure. Everything in that studio operates at different signal levels: instrument level for guitars and basses (around 100mV), line level for keyboards and interfaces (around 1V), and modular level for Eurorack signals (around 10V). Each level standard exists for engineering reasons related to headroom, noise floor, and circuit design. None is interchangeable with the others without active conversion.

Listen IO addresses this directly through two independent conversion stages in a single 6HP module. The top stage converts external signals upward to modular levels through active amplification. The bottom stage converts modular signals downward to line levels through passive attenuation. These stages are asymmetric by design: amplification and attenuation serve different purposes and require different circuit approaches. Understanding why one stage boosts and the other only reduces is one of the core lessons the module teaches through regular use.

The dual LED bar graphs make this normally invisible process visible. Gain staging — managing signal levels through every stage of a signal path to maximize headroom and minimize noise — is abstract as a concept and immediate as a practice when you can see what the Gain knob does to signal level in real time. The absence of a red LED on the output section communicates something important about the asymmetry between the two stages: you can only clip on the way in, not on the way out, because the stages do fundamentally different things.

The expansion headers extend this infrastructure thinking further. The INS and OUTS headers expose the same signals as the panel jacks in a format that accepts adaptor modules with different physical connector types. This separates the core function (signal conversion, level management, monitoring) from the physical connectivity format. A studio with quarter-inch equipment, a live rig with XLR, and an educational setup with banana jacks all connect to the same conversion infrastructure through different adaptor modules. The core module does not change; the interface to different environments does.

The dual headphone outputs with different stereo orientations address a practical reality of collaborative modular work. Two people monitoring the same system benefit from a module that provides the same audio in a form that serves each person differently. The swapped-channel right output is not a limitation; it is a deliberate provision for teaching, collaborative production, and diagnostic monitoring within a single 6HP module.

---

## Patch Examples

### **Patch 1: Basic - External Instrument Integration**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ External        │    │ 4ms Company     │    │ Modular         │    │ Monitoring      │
│ Instruments     │    │ Listen IO       │    │ Processing      │    │                 │
│                 │    │                 │    │                 │    │                 │
│ Electric        │    │ Line to Mod:    │    │ VCA Module      │    │                 │
│ Guitar ○────────┼────┼─ Line In L ◀    │    │                 │    │                 │
│                 │    │                 │    │ Audio In ◀──────┼────┼─ Mod Out L ○    │
│ Keyboard ○──────┼────┼─ Line In R ◀    │    │                 │    │                 │
│ (Stereo out)    │    │                 │    │ CV In ◀─────────┼────┼─ Envelope       │
└─────────────────┘    │ Gain: Adjust    │    │                 │    │                 │
                       │ for proper      │    │ Audio Out ○─────┼────┼─ Mod In L ◀     │
┌─────────────────┐    │ levels using    │    │                 │    │                 │
│ Visual          │    │ LED bar graphs  │    │ Filter Module   │    │ Mod to Line:    │
│ Monitoring      │    │                 │    │                 │    │ Process guitar  │
│                 │    │ LED Feedback:   │    │ Audio In ◀──────┼────┼─ Mod Out R ○    │
│ Top LEDs show   │    │ L/R bars show   │    │ (Keyboard)      │    │ (keyboard)      │
│ input levels    │    │ signal strength │    │                 │    │                 │
│ Bottom LEDs     │    │ Red = clipping  │    │ Audio Out ○─────┼────┼─ Mod In R ◀     │
│ show output     │    │ (adjust gain    │    │                 │    │                 │
│ levels          │    │ to avoid)       │    │                 │    │ Level: Set for  │
└─────────────────┘    │                 │    │                 │    │ comfortable     │
                       │                 │    │                 │    │ headphone level │
                       │                 │    │                 │    │                 │
                       │                 │    │                 │    │ Headphones ◀───┼────┼─ Line Out L ○   │
                       │                 │    │                 │    │                 │
                       │                 │    │                 │    │ Recording ◀─────┼────┼─ Line Out R ○   │
                       │                 │    │                 │    │ Interface       │
                       └─────────────────┘    └─────────────────┘    └─────────────────┘

External Instrument Integration Workflow:
1. Connect external instruments to Line In jacks (mono sources to left, stereo to both)
2. Adjust Gain knob while monitoring LED bar graphs for optimal levels without clipping
3. Route converted signals to modular processing (VCAs, filters, effects)
4. Return processed signals to Mod In jacks for monitoring and output
5. Use Level knob to set comfortable headphone monitoring levels
6. Connect Line Out jacks to external recording interface or amplification
```

**Setup:** Understanding conversion between external and modular signal levels
**Controls:** Gain staging with LED monitoring, level matching for external equipment
**Result:** Successful integration of external instruments into modular workflow
**Technical Focus:** Signal level conversion, visual monitoring, and proper gain staging
**Learning Objective:** Master essential I/O interface operations for external instrument integration

**What You're Learning:**
- **Signal level conversion:** Understanding the difference between instrument level (~100mV), line level (~1V), and modular level (~10V) - these aren't arbitrary standards, they're optimized for different circuit requirements and headroom needs
- **Gain staging through visual feedback:** The LED bar graphs teach you to recognize optimal signal levels by sight - more lights = higher level, red = clipping. This skill transfers to every mixing console and interface you'll ever use
- **Bidirectional signal flow:** Audio enters modular, gets processed, and exits to monitoring/recording - professional workflow requires managing both conversions with equal care
- **Complete signal path thinking:** Visual monitoring shows one stage is working, but complete signal flow requires patching every connection point from source to destination

**Enhanced Alternatives:**

**Main Example:** Electric guitar through Listen IO into a VCA for basic external instrument integration

**Alternative Options:**
- **Budget:** Use a passive DI box before Listen IO for better impedance matching on guitar; route the converted signal to Erica Synths Pico VCA2 as a minimal processing destination
- **Different character:** Add the Intellijel Stomp between guitar and Listen IO for proper high-impedance buffering — the Stomp and Listen IO together form the complete guitar-to-modular solution
- **Premium:** Route the converted signal through Tiptop Audio MISO for precision attenuversion and signal distribution before further modular processing

**Experimentation Ideas:**

1. **Feedback loop creation:** Patch Line Out back to Line In through external effects (reverb, delay, distortion). Adjust Level and Gain to control feedback intensity. Creates self-generating textures from simple sources.

2. **Dual-source stereo processing:** Guitar in left input, keyboard in right input. Process each channel differently in modular (different filters, envelopes, effects) before recombining for true stereo separation based on source.

3. **External CV generation:** Use Mod Out to trigger envelope generators or clock dividers from external drum machines. External rhythm becomes modular CV source, linking external timing to modular processing.

4. **Dynamic gain automation:** Patch modular LFO or envelope to a VCA controlling the Mod Out signal level. Creates rhythmic volume changes or tremolo effects on external sources within modular.

5. **Parallel processing technique:** Split external source after Listen IO - send one path through heavy processing (distortion, filtering), keep one path clean, blend with modular mixer. Professional studio technique in modular context.

### **Patch 2: Advanced - Dual Recording and Monitoring Setup**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Modular         │    │ 4ms Company     │    │ External        │    │ Multi-User      │
│ Sources         │    │ Listen IO       │    │ Processing      │    │ Monitoring      │
│                 │    │                 │    │                 │    │                 │
│ Final Mix L ○───┼────┼─ Mod In L ◀     │    │ Audio Interface │    │                 │
│                 │    │                 │    │                 │    │ Primary         │
│ Final Mix R ○───┼────┼─ Mod In R ◀     │    │ Input L ◀───────┼────┼─ Line Out L ○   │
│                 │    │                 │    │                 │    │ Headphones     │
│ (From mixer     │    │ Level: Set to   │    │ Input R ◀───────┼────┼─ Line Out R ○   │
│ or final VCA)   │    │ avoid clipping  │    │                 │    │ (Normal stereo) │
└─────────────────┘    │ external input  │    │ Output L ○──────┼────┼─ Line In L ◀    │
                       │                 │    │ (Processed)     │    │                 │
┌─────────────────┐    │ Mod to Line:    │    │ Output R ○──────┼────┼─ Line In R ◀    │
│ External        │    │ Convert modular │    │                 │    │ Secondary       │
│ Effects         │    │ to line level   │    │ External        │    │ Headphones     │
│                 │    │                 │    │ Effects Unit    │    │ (Swapped        │
│ Reverb/Delay ○──┼────┼─ Effects Send   │    │                 │    │ channels)       │
│ Returns         │    │ via OUTS header │    │ Input ◀─────────┼────┼─ OUTS Header    │
│                 │    │                 │    │                 │    │                 │
│ Processed ○─────┼────┼─ Line In via    │    │ Output ○────────┼────┼─ INS Header     │
│ Signal Return   │    │ INS header      │    │                 │    │                 │
└─────────────────┘    │                 │    │                 │    │                 │
                       │ Line to Mod:    │    │                 │    │                 │
                       │ Convert         │    │                 │    │                 │
                       │ processed       │    │                 │    │ Gain: Adjust    │
                       │ effects back    │    │                 │    │ for external    │
                       │ to modular      │    │                 │    │ effects return  │
                       │ levels          │    │                 │    │ levels          │
                       └─────────────────┘    └─────────────────┘    └─────────────────┘

Advanced I/O Configuration:
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ Signal Flow Management:                                                              │
│ • Modular signals converted to line level for external recording                    │
│ • Simultaneous sends to external effects via expansion headers                      │
│ • External effects returns converted back to modular levels                        │
│ • Multiple monitoring outputs for collaborative sessions                           │
│                                                                                      │
│ Professional Features:                                                               │
│ • Dual headphone outputs with different channel configurations                     │
│ • Expansion headers enable custom I/O configurations                               │
│ • LED monitoring prevents clipping in both directions                              │
│ • Professional signal levels for studio integration                                │
│                                                                                      │
│ Workflow Benefits:                                                                   │
│ • Single module handles complete I/O requirements                                  │
│ • Visual monitoring aids in maintaining signal integrity                           │
│ • Flexible routing options through headers and jacks                              │
│ • Simultaneous recording and monitoring capabilities                               │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

**Module Integration:**
| Integration Type | Signal Path | Professional Application | Technical Benefit |
|-----------------|-------------|------------------------|------------------|
| **Recording Interface** | Modular → Line Out → Recording | **Studio-quality capture** | **Professional signal levels** |
| **External Effects** | Line Out → Effects → Line In | **Hardware effects integration** | **Bidirectional conversion** |
| **Monitoring System** | Multiple headphone outputs | **Collaborative sessions** | **Independent monitoring configs** |
| **Custom I/O** | Expansion headers | **Flexible connectivity** | **Adaptor module compatibility** |

**Advanced Techniques:**
- **Dual monitoring:** Two users can monitor with different channel configurations
- **Effects integration:** Send/return loops through external hardware effects
- **Professional I/O:** Studio-quality recording and monitoring capabilities
- **Flexible routing:** Headers and jacks can be used simultaneously for complex routing

**Learning Objectives:**
- **Professional I/O:** Understanding studio-quality signal conversion and monitoring
- **Complex routing:** Using all I/O options simultaneously for advanced configurations
- **Signal integrity:** Maintaining quality through multiple conversion stages
- **System integration:** Listen IO as central hub for modular/external equipment interface

**What You're Learning:**
- **Bidirectional workflow architecture:** Professional studios route audio in loops - out to processing, back for more processing, out again. Listen IO makes this explicit through its dual-section design, teaching you that I/O isn't one-way traffic
- **Expansion header functionality:** The INS/OUTS headers aren't auxiliary features - they're infrastructure design. Same signals, different physical formats. This teaches modular thinking about connectivity: separate core function from physical implementation
- **Collaborative monitoring systems:** Dual headphone outputs with channel swapping enable different listening perspectives simultaneously. This teaches that monitoring is about reference and perspective, not absolute "correctness"
- **Signal integrity across conversions:** Each conversion stage (modular → line → external processor → line → modular) requires proper gain staging. Understanding cumulative conversion teaches you to maintain signal quality through complex professional signal chains

**Enhanced Alternatives:**

**Main Example:** Modular final mix through Listen IO to recording interface while monitoring on headphones with external effects loop

**Alternative Options:**
- **Budget:** Behringer UMC22 audio interface in place of a premium interface; remove the external effects loop and work with modular effects only to reduce conversion stages
- **Different character:** Use the 4ms MetaModule as the external processor — route modular signal into the MetaModule for plugin-quality processing, return it to the patch, then out through Listen IO
- **Premium:** Expert Sleepers ES-8 for multi-channel DC-coupled I/O alongside Listen IO; ES-8 handles DAW integration while Listen IO handles headphone monitoring and instrument inputs simultaneously

**Experimentation Ideas:**

1. **Ping-pong processing:** Send modular → external reverb → back to modular → different filter → back out → different external effect. Create impossible-in-one-system processing chains by bouncing between domains.

2. **Dual-user collaborative patching:** Two people with headphones, one monitoring normal stereo (working on rhythm), one monitoring swapped stereo (working on melody). Both hear full mix but focus on different spatial elements.

3. **External effects as modulation source:** Send modular audio to external effects, return the wet signal, use envelope follower on wet signal to create CV. External processing characteristics become modular control voltages.

4. **Multi-format I/O matrix:** Use both jacks and headers simultaneously - main monitors on jacks, recording interface on headers, headphones on second jack. One module becomes complete studio I/O infrastructure.

5. **Live performance FOH split:** Main mix to FOH via headers, personal monitor mix via jacks, recording split via interface. Single module handles all live sound I/O requirements with independent level control.

### **Patch 3: Expert - Complete Studio Integration Hub**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Multiple        │    │ 4ms Company     │    │ Studio          │    │ Distribution    │
│ External        │    │ Listen IO       │    │ Equipment       │    │ System          │
│ Sources         │    │                 │    │                 │    │                 │
│                 │    │ Line to Mod:    │    │ Audio Interface │    │                 │
│ Drum Machine ○──┼────┼─ Line In L ◀    │    │                 │    │ Main Monitor ◀──┼────┼─ Line Out L ○   │
│                 │    │                 │    │ Line In 1 ◀─────┼────┼─ OUTS Header L  │    │ Speakers        │
│ Groovebox ○─────┼────┼─ Line In R ◀    │    │                 │    │                 │
│                 │    │                 │    │ Line In 2 ◀─────┼────┼─ OUTS Header R  │    │ Studio Heads ◀──┼────┼─ Line Out R ○   │
│ Microphone ○────┼────┼─ INS Header     │    │                 │    │                 │    │ (Normal)        │
│ (via preamp)    │    │ (Custom input)  │    │ DAW Monitor ○───┼────┼─ Line In L ◀    │    │                 │
└─────────────────┘    │                 │    │ (Playback)      │    │ (Summed with    │    │ Performer ◀─────┼────┼─ Additional     │
                       │ Gain: Optimize  │    │                 │    │ external)       │    │ Headphones      │    │ headphone jack  │
┌─────────────────┐    │ for multiple    │    │ Line Out 1 ○────┼────┼─ External       │    │ (Swapped)       │    │ on case         │
│ Modular         │    │ source levels   │    │                 │    │ Processor       │    │                 │
│ System          │    │                 │    │ Line Out 2 ○────┼────┼─ Mod In L ◀     │    │                 │
│                 │    │ LED Monitoring: │    │                 │    │ (DAW return)    │    │                 │
│ Complex Patch ○─┼────┼─ Mod In R ◀     │    │                 │    │                 │    │                 │
│ Final Output    │    │ Visual feedback │    │ External        │    │ Mod In R ◀──────┼────┼─ Mod Out L ○    │
│                 │    │ for all signal  │    │ Hardware        │    │ (External       │    │ (Multiple       │
│ Send Effects ○──┼────┼─ Mod Out L ○    │    │ Processor       │    │ sources mixed   │    │ external        │
│ (Aux sends to   │    │ (To external    │    │                 │    │ in modular)     │    │ sources to      │
│ external gear)  │    │ processing)     │    │ Input ◀─────────┼────┼─ Line Out L     │    │ modular         │
└─────────────────┘    │                 │    │ (from modular)  │    │ (via header)    │    │ processing)     │
                       │ System Hub:     │    │                 │    │                 │    │                 │
                       │ Central point   │    │ Output ○────────┼────┼─ INS Header     │    │ Mod Out R ○─────┼────┼─ Additional     │
                       │ for all audio   │    │ (processed)     │    │ (External       │    │ processing      │
                       │ I/O in studio   │    │                 │    │ processor       │    │ chain           │
                       │                 │    │                 │    │ return)         │    │                 │
                       └─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘

Professional Studio Integration:
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ Complete I/O Hub Functionality:                                                     │
│ • Listen IO serves as central interface between modular and studio equipment       │
│ • Multiple external sources converted to modular levels for internal processing    │
│ • Modular outputs converted to professional levels for recording and monitoring    │
│ • Bidirectional signal flow enables complex studio routing architectures           │
│                                                                                      │
│ Professional Workflow Benefits:                                                      │
│ • Single module eliminates need for external interface in many applications        │
│ • LED monitoring ensures optimal signal levels throughout entire chain             │
│ • Expansion headers provide custom connectivity for any studio configuration       │
│ • Dual headphone outputs enable collaborative production sessions                  │
│                                                                                      │
│ System Architecture:                                                                 │
│ • Listen IO becomes the bridge between modular synthesis and traditional studio    │
│ • Enables modular to function as high-quality studio instrument and processor      │
│ • Provides professional monitoring and signal distribution capabilities            │
│ • Maintains signal integrity through high-quality conversion circuits              │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

**Expert Integration Techniques:**
| System Function | I/O Configuration | Professional Application | Workflow Benefit |
|----------------|------------------|------------------------|------------------|
| **Studio Hub** | All I/O utilized simultaneously | **Central audio routing** | **Single-module I/O solution** |
| **Signal Conversion** | Bidirectional level conversion | **Professional signal levels** | **Studio-quality integration** |
| **Monitoring System** | Multiple output configurations | **Collaborative sessions** | **Flexible monitoring options** |
| **Custom Connectivity** | Expansion headers active | **Adaptor module integration** | **Unlimited connectivity options** |

**Professional Applications:**
- **Studio integration:** Complete bridge between modular and traditional studio equipment
- **Live performance:** Professional I/O for modular in live sound environments
- **Collaborative production:** Multiple monitoring outputs for team-based sessions
- **Custom installations:** Expansion headers enable any conceivable I/O configuration

**Learning Objectives:**
- **System architecture:** Understanding Listen IO as central studio infrastructure
- **Professional workflow:** Integrating modular synthesis into professional production environments
- **Complex routing:** Simultaneous use of all I/O options for maximum flexibility
- **Signal integrity:** Maintaining quality through complex professional signal chains

**What You're Learning:**
- **Infrastructure thinking at scale:** When every piece of equipment in your studio connects through one 6HP module, you're learning system architecture principles that separate amateur collections from professional facilities. Listen IO teaches you to think about I/O as foundational infrastructure, not optional accessories
- **Simultaneous multi-domain routing:** External sources + modular processing + DAW integration + external effects + multiple monitoring systems all working together. This teaches you that professional workflows aren't linear - they're networks of interconnected signal paths
- **Adaptor module philosophy:** The expansion headers demonstrate that connectivity should be adaptable without redesigning core functionality. This teaches infrastructure design principles: stable core, flexible edges. Professional systems plan for unknowable future needs through modular expansion
- **Signal flow orchestration:** Managing gain staging across external sources, modular processing, external effects, DAW integration, and monitoring simultaneously. This teaches you signal flow isn't a single path - it's an orchestrated system where every stage affects every other stage

**Enhanced Alternatives:**

**Main Example:** Multiple external sources converted through Listen IO, processed through modular, returned to recording interface, with dual headphone monitoring

**Alternative Options:**
- **Budget:** Focusrite Scarlett 4i4 audio interface providing multiple input channels; consolidate external source mixing before Listen IO rather than after to simplify signal flow
- **Different character:** Replace the external effects loop with Erica Synths Pico DSP inside modular — this eliminates one conversion stage and keeps processing within the Eurorack domain
- **Premium:** Expert Sleepers ES-8 and ES-3 for complete multi-channel bidirectional I/O; Listen IO remains for headphone monitoring and instrument inputs while ES-8 handles DAW integration at full modular resolution

**Experimentation Ideas:**

1. **Complete hybrid production system:** External drum machine triggers modular percussion, modular output routes to DAW for arrangement, DAW stems return to modular for analog summing, final mix goes to external mastering chain. Every domain contributes its strength.

2. **Educational multi-station setup:** Four students with different external instruments, all entering through Listen IO, all processing through shared modular, multiple headphone monitoring points. One module enables complete educational I/O infrastructure.

3. **Live performance with backup redundancy:** Main PA connection via jacks, backup PA connection via headers, personal monitor via second headphone output, recording interface capture via additional header connection. Single module, complete redundant live sound system.

4. **Studio stem processing hub:** Each DAW track routes to separate modular processing chains (drums through one filter, bass through different filter, keys through effects), all return to DAW via Listen IO as processed stems. Modular becomes outboard processing rack.

5. **Cross-domain feedback networks:** Modular generates audio, exits to external delay, returns to modular filter, exits to different external reverb, returns to modular VCA, exits to DAW recording. Create processing chains impossible within any single domain by chaining across all domains.

**System Architecture Achievement:**

When you can successfully route external instruments + modular synthesis + DAW integration + external effects + multiple monitoring systems through a single 6HP module, you've mastered professional I/O thinking. This isn't about "getting sound in and out" - it's about understanding that professional music creation requires seamless integration across all your tools, and that infrastructure quality determines whether that integration enhances or limits your creativity.

---

## Common Mistakes

### **"My external instrument sounds distorted and harsh in modular"**

**Problem:** Input gain set too high, causing clipping at the Line to Mod conversion stage

**Why It Happens:** Coming from traditional recording, many users assume "more signal is better" and crank the Gain knob. But Listen IO can provide up to 30x gain - far more than most sources need. When you boost a line-level keyboard or phone output with maximum gain, you're multiplying an already strong signal by 30, pushing it well into clipping territory. The top LED flashing red isn't a "suggestion" - it's telling you the circuit is running out of headroom.

**The deeper principle:** Gain staging is about **optimization, not maximization**. In professional audio, you want the strongest clean signal, not the loudest possible signal. Clipping creates harsh harmonics that can't be removed later - it's permanent distortion of your source material. The LED bar graph is teaching you to recognize optimal gain visually: strong signal (most LEDs lit) without clipping (red LED off).

**Solution:**
- Start with Gain at minimum (fully counterclockwise)
- Play your external source at normal performance volume
- Slowly increase Gain while watching the LED bar graph
- Stop increasing when you see 4-6 LEDs consistently lit during loud passages
- If red LED flashes even occasionally, reduce gain slightly
- Remember: You can always add more gain in your modular processing chain

**Alternative approach:** If you need distortion, get it from modular waveshapers or distortion modules where you can control the character. Input clipping is the wrong place for creative distortion - it happens before any processing can shape it musically.

---

### **"I can barely hear my guitar through the modular system"**

**Problem:** Insufficient gain for instrument-level sources, or gain set correctly but modular processing reduces signal

**Why It Happens:** Electric guitars output very low voltage compared to line-level equipment - typically 100mV or less. This is **instrument level**, about 10x quieter than line level (~1V) and 100x quieter than modular level (~10V). Listen IO needs to amplify this tiny signal by 20-30x to reach modular levels. If Gain is set conservatively, or if subsequent modular processing includes VCAs that reduce level, the guitar disappears.

**The deeper principle:** **Understanding signal levels is fundamental to all audio work**. Instrument level (guitars, basses, dynamic microphones) requires significant amplification. Line level (keyboards, audio interfaces, effects processors) requires moderate amplification. Modular level is the highest operating level, providing headroom for processing. When sources are quieter than expected, it's usually a level mismatch, not a quality problem with the source.

**Solution:**
- For guitars/basses, expect to use Gain knob at 2-3 o'clock positions
- Watch LED bar graph - you should see at least 3-4 LEDs during strumming/picking
- If signal is still weak after maximum gain, your pickup output may be very low
- Consider a guitar preamp or boost pedal before Listen IO for very low-output pickups
- When patching to VCAs, keep VCA levels high initially - don't assume low VCA = subtle
- Remember: Modular expects hot signals, so don't be afraid of strong gain

**Alternative approach:** Use the guitar's volume knob as a performance control rather than trying to maintain constant level. Set Listen IO gain for maximum guitar volume, then use the guitar's own volume for dynamics.

---

### **"The LED bar graphs show signal but I hear nothing"**

**Problem:** Wrong section being monitored - LEDs show input signal but output isn't patched, or vice versa

**Why It Happens:** Listen IO has two completely independent sections with separate LED monitoring. The top LEDs monitor Line to Mod conversion (after Gain is applied), while bottom LEDs monitor Mod to Line conversion (after Level attenuation). New users often watch the wrong LED section for their signal path, seeing activity but hearing silence because the signal isn't actually reaching their destination.

**The deeper principle:** **Signal flow requires complete paths**. Audio doesn't "leak" between sections - you must explicitly patch both input AND output. Visual monitoring only shows that stage is working; it doesn't guarantee your signal reaches its destination. This is the same principle in mixing consoles, patch bays, and all professional audio routing: seeing signal at one point doesn't mean it's reaching another point.

**Solution:**
- **For external sources:** Check top LEDs (Line to Mod), but remember to patch Mod Out to a modular destination
- **For modular output:** Check bottom LEDs (Mod to Line), but remember to patch Mod In from your modular source
- Trace complete signal path: Source → Line In → Gain → Mod Out → [Modular processing] → Mod In → Level → Line Out → Destination
- If LEDs show activity but no sound, the break is after that LED stage
- If no LED activity, the break is before or at that stage

**Troubleshooting sequence:**
1. Confirm source is playing/generating signal
2. Check appropriate LED section for that signal path
3. Verify patch cables are fully inserted (3.5mm jacks can be finicky)
4. Test with headphones at Line Out to isolate monitoring from source issues

---

### **"My modular output sounds quiet even with Level knob maxed"**

**Problem:** Modular source isn't strong enough, or expecting amplification when Level only attenuates

**Why It Happens:** The Mod to Line section (bottom half) only provides **attenuation**, never amplification. Maximum Level knob position is unity gain (0dB) - the modular signal passes through unchanged. If your modular source is already quiet (low-output oscillators, heavily filtered signals, multiple attenuation stages), Listen IO can't boost it. This catches users who expect Level to work like Gain - but they're fundamentally different functions.

**The deeper principle:** **Gain vs. attenuation serve different purposes**. Gain (top section) amplifies weak signals up to modular levels - it needs to boost because external sources are too quiet for modular. Attenuation (bottom section) reduces strong modular signals down to safe line levels - it needs to reduce because modular is too hot for external equipment. Understanding this asymmetry is essential: you build up signals that are too weak, and reduce signals that are too strong. Listen IO's design reflects this reality through separate gain and attenuation stages.

**Solution:**
- Before Listen IO, boost your modular signal using VCAs, mixers, or amplifier modules
- Check your modular signal path for excessive attenuation (multiple passive mults, long cable runs)
- Use active modules (VCAs with gain makeup, active mixers) rather than passive utilities
- Consider a dedicated output amplifier module if your patches consistently run quiet
- Remember: Listen IO assumes modular sources are already at proper modular levels (~10Vpp)

**Signal chain optimization:**
- Keep VCAs in your modular chain at 70-80% open for healthy levels
- Use mixer channels near unity gain, not heavily attenuated
- Route oscillators and sound sources with minimal attenuation before final output
- Save dynamic control for performance (VCA expression), not fixed signal reduction

---

### **"Headphones sound different from my monitors"**

**Problem:** Level mismatch between headphone volume and monitor volume, or acoustic environment differences

**Why It Happens:** Line Out jacks serve double duty - they're both line outputs for studio monitors/interfaces AND headphone outputs. But headphones and monitors have vastly different impedance and sensitivity characteristics. What sounds "correct" on headphones at a given Level knob position may be too quiet or too loud through monitors. Additionally, acoustic environment dramatically affects perception - headphones eliminate room acoustics, while monitors include room reflections, bass buildup, and spatial information.

**The deeper principle:** **Monitoring is about reference, not absolute volume**. Professional engineers use multiple monitoring systems (main monitors, near-fields, headphones, car stereos) specifically because each reveals different aspects of a mix. Headphones show detail and stereo image without room interference. Monitors show how the mix works in three-dimensional space with realistic bass response. Neither is "correct" - they're different perspectives on the same audio. Listen IO's dual output capability lets you use both perspectives simultaneously.

**Solution:**
- Set Level knob separately for headphone vs. monitor sessions
- Mark your "headphone position" and "monitor position" on the panel with tape if you switch frequently
- Use headphones for detail work (precise panning, subtle modulation, high-frequency content)
- Use monitors for overall balance (bass levels, spatial width, room translation)
- Remember: They should sound different - that's information, not a problem

**Professional workflow:**
- Start patches on monitors to understand overall character and bass response
- Switch to headphones to fine-tune modulation depth and stereo movement
- Return to monitors for final level decisions and complete mix context
- Both perspectives reveal truth, just different aspects of it

---

### **"The red LED keeps flashing on the input section"**

**Problem:** Input clipping from excessive gain, but user isn't sure how much to reduce

**Why It Happens:** The red LED indicates clipping - the circuit has run out of voltage headroom and is "hard limiting" the signal peaks. But new users often don't understand how sensitive this threshold is. Even brief red LED flashes mean distortion is occurring on those peaks. Some users think "a little red is okay" because in traditional recording, meters often have "yellow zone" (approaching limits) and "red zone" (over limits). Listen IO's LED has no yellow zone - red means you're clipping.

**The deeper principle:** **Headroom is your safety margin against distortion**. Professional signal flow maintains headroom at every stage - recording, processing, mixing. When you're "hitting red," you've eliminated all headroom at that stage. Any louder peak will distort. Any additional gain in the chain will amplify the distortion. Digital systems can sometimes recover from brief clipping through look-ahead limiting, but analog systems like Listen IO clip immediately and permanently. Understanding headroom means understanding that optimal signal level is NOT "as hot as possible" - it's "as hot as sustainable with margin for dynamics."

**Solution:**
- Red LED should never illuminate, even on the loudest peaks
- Reduce Gain until red LED only flashes on absolutely maximum transients
- Then reduce Gain slightly more to create headroom for unexpected loud moments
- Aim for 4-6 LEDs lit on normal loud passages, with headroom for peaks
- Remember: You can always add gain later in modular processing without clipping artifacts

**When to break the rule:**
- If you want intentional input distortion for creative effect, watch for harshness
- Some sources (especially drum machines) benefit from slight clipping for aggression
- But make this a conscious creative choice, not an accident from improper gain staging
- Even creative clipping should be occasional and on peaks, not constant

---

### **"I can't hear my DAW playback through modular processing"**

**Problem:** DAW return level doesn't match modular processing expectations, or monitoring is set up incorrectly

**Why It Happens:** When routing DAW audio back into modular for processing, users often send it at line level from their audio interface. But even with Listen IO converting it to modular level, the gain staging might not match the rest of their modular setup. If they've been working with hot VCO signals and then patch in a conservatively-gained DAW return, it seems to vanish in the mix. The source is present (LEDs confirm), but it's not competing level-wise with existing modular signals.

**The deeper principle:** **Gain staging affects all sources equally, but perceived level differs based on content**. A sine wave at -10dBu and a drum loop at -10dBu measure identically but sound different in terms of loudness because of different peak-to-RMS ratios. Complex program material (like DAW tracks) often has lower peak levels than simple modular tones, making level matching tricky. Professional engineers understand this and adjust for perceived loudness, not just measured level.

**Solution:**
- Increase DAW output level before sending to audio interface (boost in DAW mixer)
- Use Listen IO's Gain control more aggressively for DAW returns than for instruments
- If processing DAW audio through modular, include a VCA with gain makeup in the chain
- Consider that modular VCOs run very hot - DAW returns don't need to match that level exactly
- Use Listen IO's bottom section to monitor the mix including DAW returns

**Workflow optimization:**
- Create a dedicated DAW return track with +6dB gain as a starting point
- Route DAW to audio interface at healthy levels (not conservative line level)
- Treat DAW returns as you would any external instrument - gain stage appropriately
- Remember: Listen IO bridges two different signal level worlds, but you control both sides

---

### **"I get noise when nothing is plugged into Line In"**

**Problem:** Gain knob creates noise floor amplification when turned up with no source connected

**Why It Happens:** All gain circuits amplify both signal AND noise. When there's no signal plugged into Line In, the Gain circuit is amplifying only its own noise floor - thermal noise from resistors, op-amp noise, power supply noise. At low gain settings this is inaudible. At high gain settings (necessary for guitars and low-output sources), this noise becomes audible. This isn't a defect - it's physics. Every preamp and gain stage exhibits this behavior.

**The deeper principle:** **Noise floor exists in all analog circuits**. The trick is keeping it below audibility relative to your signal. This is why professional recording emphasizes strong source levels - the louder your source relative to the circuit's inherent noise, the better your signal-to-noise ratio. Listen IO's high gain range (30x) is necessary for quiet sources, but it necessarily amplifies more noise floor when those sources are very quiet or absent.

**Solution:**
- Keep Gain at minimum when Line In is unused
- Only increase Gain when source is connected and playing
- Use Mod Out with a switch/gate to mute the signal path when no external source is active
- Consider the noise floor part of analog character if it's minimal - perfectionism about silence isn't necessary
- If noise is excessive (loud hiss), check power supply and cable routing for interference

**Professional perspective:**
- Some noise floor is normal and acceptable in modular systems
- Signal-to-noise ratio matters more than absolute silence
- Strong source signals + appropriate gain = acceptable noise floor
- Modular systems are inherently noisier than digital systems - embrace this as character

---

### **"External effects returns sound different than the dry signal"**n
**Problem:** Level mismatch or processing in external effects changes perceived loudness and tone

**Why It Happens:** When creating effects loops (modular → Line Out → external processor → Line In → modular), the signal goes through multiple conversion stages and the external processor itself. Even if both Listen IO sections are set optimally, the external processor adds its own gain staging, frequency response changes, and level adjustments. A reverb might output 10dB quieter than its input. A compressor might output louder. These level changes affect how the return integrates with your dry signal.

**The deeper principle:** **Parallel processing requires level matching**. In professional mixing, when you create a send/return loop, you level-match the return so it integrates properly. Too quiet, and the effect seems weak. Too loud, and it overwhelms. This level matching is separate from the effect itself - it's infrastructure management. Listen IO provides the infrastructure (conversion both ways), but you manage the levels on both sides plus the external processor's own levels.

**Solution:**
- Set external processor output to its "unity gain" or "0dB" position initially
- Adjust Listen IO's Gain (for return) to match the dry signal level
- Use modular VCA or mixer to blend dry and wet signals at matched levels
- If external processor has mix control, keep it 100% wet for parallel processing control
- Level-match first, then adjust wet/dry balance musically

**Effects loop optimization:**
- Document gain/level settings for each external processor
- Mark "return gain" positions on Listen IO panel for different effects
- Use consistent signal levels out of modular to external processors
- Consider that some effects (reverb, delay) intentionally sound quieter - this is correct

---

### **"Dual headphone outputs sound identical - what's the point?"**

**Problem:** Not understanding the channel swapping feature and its applications

**Why It Happens:** The left Line Out jack provides normal stereo (left signal to left ear, right signal to right ear). The right Line Out jack provides swapped stereo (right signal to left ear, left signal to right ear). On casual listening, these might sound "basically the same" because the content is identical - just swapped. But for certain applications (collaboration, stem monitoring, diagnostic work), this swapping is extremely useful.

**The deeper principle:** **Flexible monitoring enables different workflows**. Sometimes you need to isolate one channel, sometimes you need to hear the "opposite perspective" of a stereo field, sometimes you need two people monitoring different aspects simultaneously. Professional systems provide this flexibility because different listening tasks require different monitoring approaches. Listen IO's implementation is elegant - same outputs, different configurations through jack choice.

**Solution:**
- Use left jack for primary monitoring (normal stereo)
- Use right jack for second person's monitoring (they hear swapped channels)
- Use both simultaneously when teaching - instructor hears normal, student hears swapped
- Use swapped monitoring to check stereo field from opposite perspective
- In mono setups, use right jack to check right channel specifically

**Professional applications:**
- Collaborative production: Two producers with different listening perspectives
- Teaching: Instructor maintains normal reference while showing student alternate view
- Diagnostic: Swap channels to isolate issues with stereo field
- Performance: Performer gets swapped mix while engineer monitors normal mix

---

### **"I don't understand when to use the expansion headers"**

**Problem:** Unclear about INS/OUTS header functionality and applications versus standard jacks

**Why It Happens:** The expansion headers duplicate the functionality of the standard 3.5mm jacks but in a different physical format (3-pin headers). Users don't realize these are for adaptor modules (like Listen Up) that provide alternative connector types. Without an adaptor module, the headers seem purposeless. But the design intent is infrastructure flexibility - the same signals available in multiple physical formats through adaptors.

**The deeper principle:** **Infrastructure design separates core functionality from physical connectivity**. Professional systems make signals available at intermediate points, allowing for connection method flexibility without redesigning the core module. This is the same principle used in patch bays, where the same signals appear on multiple connector types. Listen IO's headers aren't an afterthought - they're recognition that different studios, live rigs, and educational environments need different physical connectivity.

**Solution:**
- Use standard 3.5mm jacks for normal modular patching
- Use expansion headers when you need different connector types (1/4", banana, etc.)
- Obtain Listen Up or similar adaptor modules to use headers with standard studio equipment
- Headers and jacks work simultaneously - you can use both at once
- Consider headers for permanent installation routing (studio wiring, case mounting)

**Applications for expansion headers:**
- Educational settings: Banana jacks for safety and ease of use
- Studio integration: 1/4" TRS for professional studio equipment
- Live performance: Different connectors for FOH systems
- Custom installations: Non-standard connectivity requirements
- Future expansion: Adaptor modules for protocols that don't exist yet

---

### **Pattern Recognition: Understanding the Root Causes**

**Four fundamental misunderstandings cause 90% of Listen IO issues:**

**1. Expecting Signal Level Standards to Match Between Domains**

Instrument level (~100mV), line level (~1V), and modular level (~10V) are different standards for good technical reasons. Each domain operates at the level that makes sense for its circuitry and headroom requirements. Listen IO bridges these domains through conversion, but users must understand that "line level" in their studio and "modular level" in their rack are intentionally different. The module doesn't make them the same - it translates between them. Issues with "too quiet" or "too loud" almost always trace to not understanding which signal level standard applies to which equipment.

**2. Treating Gain and Attenuation as Identical Functions**

Gain (top section) amplifies weak signals up. Attenuation (bottom section) reduces strong signals down. They're not mirror images - they serve different purposes in signal flow. Gain is active (adds voltage), attenuation is passive (removes voltage). This asymmetry confuses users who expect Level to "boost" like Gain does, or who don't understand why they can't make a modular signal louder with Level. Understanding gain vs. attenuation reveals a fundamental principle: signal flow requires building up weak sources and reducing strong sources. You can't reverse these operations.

**3. Assuming Visual Monitoring Guarantees Complete Signal Path**

LED bar graphs show signal at that stage - after Gain (top) or after Level (bottom). But seeing LEDs doesn't mean your signal reaches its final destination. Complete signal flow requires patching both input AND output, plus everything in between. This is the same principle in mixing consoles and patch bays: metering shows that stage is working, but doesn't confirm downstream connections. Users who see LED activity but hear nothing have a break in the signal path after the LED stage.

**4. Missing the Bidirectional Infrastructure Concept**

Listen IO isn't two separate modules crammed together. It's one bidirectional infrastructure module that treats "external to modular" and "modular to external" as equally important conversions. Users who think of it as "input module with bonus output" miss half its capability. Both directions are primary functions, both require quality conversion, both need proper gain staging. Understanding bidirectional thinking reveals that professional I/O isn't about getting signals in or getting signals out - it's about seamless integration between systems where signals flow both directions.

**The Deeper Pattern:**

Listen IO teaches professional signal flow principles through practical application: understanding signal levels, managing gain staging, monitoring signal health visually, and thinking about I/O as bidirectional infrastructure. Issues with Listen IO almost always reveal gaps in understanding these principles - which is exactly what makes it a teaching module. When you master Listen IO, you've mastered professional I/O concepts that apply to every mixing console, audio interface, and recording situation you'll ever encounter.

The LED bar graphs, the separate gain and attenuation stages, the dual independent sections - these aren't just features. They're visible representations of how professional signal flow works. Understanding why things go wrong with Listen IO teaches you how to prevent problems across all audio systems.

---

## Pairs Well With

**Intellijel Stomp** — Handles the high-impedance buffering that Listen IO's general-purpose inputs don't specifically provide for electric guitar. Together they form a complete guitar-to-modular integration: Stomp handles the pickup impedance, Listen IO handles the level conversion and monitoring.

**Any envelope follower (Maths works as one in a pinch)** — Route an external instrument through Listen IO's top section, then tap the Mod Out into an envelope follower. External dynamics from a guitar performance or drum machine become real-time CV, coupling a live player's expression directly to modular behavior.

**Frap Tools 411 or Intellijel Mixup** — A pre-conversion stereo mixer for combining multiple external sources into a clean stereo pair before Listen IO's inputs. Handles the mixing in the line-level domain, where the source signals actually live, rather than asking the Gain stage to reconcile mismatched levels.

**Erica Synths Pico DSP or any onboard effects module** — Route Listen IO's Mod Out into modular effects processing before returning the signal to the output stage. The combination produces sonic territory that neither domain reaches alone: a guitar through a Eurorack reverb or granular processor, monitored and recorded at line level through the same module.

**4ms MetaModule** — Plugin-quality processing inside the Eurorack case. Listen IO provides the I/O infrastructure framing the workflow: instrument in, MetaModule processes with DAW-quality algorithms, output monitored and recorded through the bottom section.

---

## What This Unlocks

The input section accepts virtually any external audio source that operates without phantom power: electric guitars, bass guitars, keyboards, synthesizers, drum machines, grooveboxes, portable recorders, phones, and most dynamic microphones. The scope covers the overwhelming majority of instruments and devices found in production and performance environments. The meaningful exclusion is phantom-powered condenser microphones, which require a dedicated preamp with 48V supply. For everything else, the Gain knob and LED bar graph provide the tools to bring those sources into the modular domain at appropriate operating levels.

The output section converts modular signals downward to levels appropriate for studio monitors, audio interfaces, mixing consoles, and headphones — simultaneously if needed. The dual headphone outputs mean two people can monitor the same system for collaborative work, teaching, or diagnostic checking from different stereo orientations. The OUTS expansion header feeds the same signals to additional destinations without affecting the panel jacks, enabling a recording interface and a monitor amplifier to receive the modular mix concurrently without any additional routing.

The bottom section's send and return capability creates a functional outboard gear loop in 6HP. A hardware compressor, vintage EQ, or rack reverb can sit between modular output and the return path, processing the signal before it reaches monitoring or recording destinations. Paired with the Intellijel Stomp upstream for high-impedance guitar buffering, Listen IO handles the complete guitar-to-modular workflow: instrument level in, modular level out for processing, effects loop available, stereo headphone monitoring included.

---

## Advanced Learning Path

Start with a single external source and headphone monitoring as the entire patch. The goal is to develop gain staging instincts through the LED bar graphs before adding any complexity. Work with different sources — a keyboard, a phone playing a reference track, a guitar — and notice how different sources require different Gain positions to reach the same target range on the LEDs.

Once gain staging is reliable, focus deliberately on the output stage. Understand through use that Level is attenuation only, that maximum position is unity gain, and that quiet modular signals must be fixed upstream. Build the habit of constructing patches where the signal arriving at Listen IO is already at a healthy level, with Level used for monitoring preference rather than signal recovery.

When both sections feel natural, begin using them simultaneously in the same patch. Route external material through the top section, process it in modular, return the processed result through the bottom section while the original source also feeds through. The module reveals its architectural character when both directions are active — it is infrastructure, not an instrument, and infrastructure is most clearly understood when it is load-bearing.

The 4ms Listen Up adaptor module, when available, is worth exploring at this stage. The header-based signal access it provides demonstrates the infrastructure thinking that runs through the module's design: the same conversion and monitoring functions, available through different physical formats without modifying the core module. This is the principle that separates systems built to grow from collections built around single configurations.
