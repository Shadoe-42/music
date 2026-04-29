---
title: Squarp Hermod+
manufacturer: Squarp
primary_role: CONTROLLER
secondary_roles: [ROUTER]
form_factor: eurorack
functions: [sequencer, signal-router]
behavior_tags: [stable, performance-oriented, reactive, linear]
use_cases: [generative melodic sequence, clock source for full system, MIDI and CV integration hub]
hp: 26
memory: full
transport: full
screen: true
historical_context: false
---

# Squarp Hermod+

**The Modular System Brain**

![Squarp Hermod+](https://github.com/Shadoe-42/music/raw/main/modular/images/squarp/hermod_plus/front_panel.jpg)

---

## Quick Start: Get Your First Sequence in 5 Minutes

**What is Hermod+?** Think of it as the central nervous system for your entire studio - modular and beyond. It's a 16-track sequencer (8 CV/Gate + 8 MIDI) that bridges the gap between your Eurorack system, MIDI gear, and computer. With high-resolution recording, real-time effects, and an intuitive workflow, it's like having a powerful DAW in 26HP.

### Your First Basic Sequence
1. **Connect CV/Gate outputs** → **Track 1 CV to oscillator V/OCT**, **Track 1 Gate to envelope**
2. **Press STEP button** to enter Step Mode (LED lights up)
3. **Press Track 1 button** to select it (LED lights up)
4. **Use grid buttons** to enter notes - press and hold while turning encoder
5. **Press PLAY** and watch your sequence come alive!
6. **Press TRACKS button** to mute/unmute and control levels

**Congratulations!** You've just programmed your first sequence in the brain of your modular system!

---

## Essential Parameters (The Four Modes System)

### **1. STEP Mode - Note Programming Central**
- **What it does:** Piano roll editor where you program notes, gates, and modulation
- **Grid buttons:** Each represents a step in time - press to select/edit
- **Main encoder:** Adjusts note pitch when step is selected
- **Zoom function:** Get ultra-precise with up to x8 magnification
- **Row edit:** Program chords and drum patterns quickly
- **Pro tip:** This is where the magic happens - spend most of your time here!

### **2. EFFECTS Mode - Real-Time Processing**
- **What it does:** Apply up to 8 MIDI effects per track in real-time
- **Available effects:** Quantize, Arpeggiator, Ratchet, Swing, Random, Euclidean, LFO, Delay
- **Stack effects:** Chain multiple effects for complex transformations
- **Live control:** Adjust effect parameters while sequence plays
- **Musical result:** Transform simple sequences into complex, evolving patterns

### **3. TRACKS Mode - Mix and Performance Control**
- **What it does:** Global track management - mutes, levels, and performance
- **Track muting:** Quickly mute/unmute tracks for live performance
- **Track selection:** Choose which track you're editing
- **Level control:** Adjust track volumes and CV amounts
- **Pattern switching:** Jump between different patterns per track (16 patterns each!)

### **4. SEQ Mode - Song Structure and Organization**
- **What it does:** Manage sequences, patterns, and song arrangements
- **64 sequence chains:** Build complete songs with verse/chorus structure
- **Pattern management:** Each track has 16 independent patterns
- **Project system:** Unlimited projects for different songs/patches
- **Live switching:** Change sequences seamlessly during performance

### **5. Recording Resolution - 96PPQ Precision**
- **What it does:** Captures your performance with incredible timing accuracy
- **96 pulses per quarter:** No more timing drift or note shifting
- **Real-time recording:** Play live and capture every nuance
- **Up to 16 bars:** Long pattern support for complex compositions

### **6. Dual Architecture - CV/Gate + MIDI**
- **8 CV/Gate tracks:** Direct control of Eurorack modules
- **8 MIDI tracks:** Control external gear, software, and computers
- **Voice flexibility:** Mono, poly, velocity, aftertouch - configure as needed
- **MIDI effects on CV:** Apply MIDI effects to CV tracks for hybrid processing


---

## Why This Excels

Hermod+ solves the integration problem that becomes urgent as a modular system grows beyond a few voices. A larger system produces more CV signals, more gate streams, more MIDI devices, and more timing relationships than any single brain can coordinate through manual patching alone. Hermod+ is designed specifically for this coordination role: it holds 16 independent tracks, handles both CV and MIDI on the same timeline, records at 96 pulses per quarter note, and provides an effects chain that processes recorded content in real time. Each of these capabilities addresses a specific coordination failure mode in a mature patch.

The 96PPQ recording resolution matters because it is finer than any grid that would be set by hand in a step sequencer. When a performer plays notes in real time, the subtle timing offsets that make a phrase feel human rather than mechanical are captured rather than quantized away. Most hardware sequencers record at 24 or 48PPQ, which snaps rhythmic gestures to coarser subdivisions. At 96PPQ, Hermod+ records the actual timing of each note event and plays it back with the same precision. Quantizing after recording is always available; capturing the performance at full resolution and deciding later how much grid correction to apply is qualitatively different from being forced to quantize at the moment of recording.

The four-mode architecture distributes different tasks across different interfaces. STEP mode is for note programming on a grid. TRACKS mode is for managing multiple tracks and their relationships simultaneously. EFFECTS mode is for applying real-time transformation to recorded content. SEQ mode is for chaining patterns into song-level arrangements. Navigating between these modes cleanly during a live performance is a learnable skill, and when it is mastered, Hermod+ becomes a complete performance instrument rather than just a sequencer.

The MIDI track capability removes the boundary between Eurorack and external hardware synthesizers. A sequencer that handles only CV cannot sequence a keyboard synthesizer or a drum machine; a MIDI-only sequencer cannot drive Eurorack voices. Hermod+ operates across both domains from a single timeline, which means a studio setup with both modular and external MIDI gear can be coordinated from a single module with a single transport control, a single clock source, and a single arrangement structure.

---

## Patches

### Patch 1: Basic Eurorack Sequence

This patch uses Hermod+ as the primary sequencer in a standard synthesizer voice configuration, establishing the core STEP mode workflow.

```
HERMOD+ Track 1 CV ──▶ [Oscillator V/OCT]
HERMOD+ Track 1 GATE ──▶ [Envelope GATE In]
[Envelope Out] ──▶ [VCA CV In]
[Oscillator Out] ──▶ [VCA Audio In]
[VCA Out] ──▶ [Mixer]
```

**Setup:** Enter STEP mode by pressing the mode button until the STEP LED is lit. Use the 16 grid buttons to enter notes for Track 1. The encoder selects pitch for each step; the grid buttons select which steps are active. Program an 8 to 16 step sequence. Connect Track 1 CV to an oscillator's V/OCT input and Track 1 GATE to an envelope generator.

**Controls:** Press the play button to start the sequence. The current step illuminates on the grid as the sequence advances. Switch to TRACKS mode to see all tracks simultaneously; Track 1 shows its progress as a moving indicator across the LED row. Adjust individual step pitches by returning to STEP mode and pressing the step to edit. Try different track lengths by setting the endpoint step; a 12-step sequence against a 16-step pattern elsewhere creates polyrhythmic relationships.

**Result:** A precisely sequenced synthesizer voice with full control over every step's pitch and gate state. Hermod+ stores the sequence in memory, so it survives power cycling and can be recalled reliably in live performance. The LED grid gives a visual representation of both the sequence content and the current playback position.

---

### Patch 2: Polyrhythmic Multi-Track

This patch uses three tracks at different lengths to create interlocking polyrhythmic relationships between bass, lead, and percussion voices.

```
HERMOD+ Track 1 CV+GATE ──▶ [Bass Oscillator + Envelope]  (16 steps)
HERMOD+ Track 2 CV+GATE ──▶ [Lead Oscillator + Envelope]  (12 steps)
HERMOD+ Track 3 GATE ──────▶ [Drum Module Trigger]        (8 steps)
[External Clock] ──────────▶ HERMOD+ Clock Input
```

**Setup:** In STEP mode, program Track 1 as a 16-step bass line and Track 2 as a 12-step melody. Program Track 3 as an 8-step gate pattern for percussion. Connect an external clock to the Clock input for stable synchronization with other modules.

**Controls:** With all three tracks running at their respective lengths, the sequences phase against each other in a 48-step cycle (the LCM of 8, 12, and 16) before all three realign simultaneously. Switch to TRACKS mode to monitor all three tracks at once; the independent LED rows show each track's current position against its sequence length. The moment all three tracks return to step 1 simultaneously is an anchor point for arrangement transitions. Adjust individual track lengths using the sequence length parameter to change the polyrhythmic cycle length.

**Result:** A multi-voice patch where rhythmic complexity emerges from different sequence lengths rather than from programming each rhythmic relationship explicitly. The arrangement structure is defined by the mathematical relationship between the three lengths, and it evolves continuously across the full cycle without any live intervention.

---

### Patch 3: MIDI and CV Hybrid

This patch runs an external MIDI synthesizer and Eurorack voices simultaneously from Hermod+, demonstrating its function as a unified performance brain across two signal domains.

```
HERMOD+ Track 9 MIDI Out ──▶ [External MIDI Synthesizer]
HERMOD+ Track 1 CV+GATE ──▶ [Eurorack Voice 1]
HERMOD+ Track 2 CV+GATE ──▶ [Eurorack Voice 2]
[USB] ──────────────────────▶ [Computer/DAW] (sync and MIDI out)
```

**Setup:** In STEP mode, program Track 9 as a MIDI track; this track outputs MIDI note data on Channel 1 by default, assignable via the menu. Program Track 1 and Track 2 as CV tracks for Eurorack voices. Connect the MIDI output to an external synthesizer's MIDI input and USB to a computer if DAW sync is desired.

**Controls:** All tracks play simultaneously from a single play command. The MIDI track sends note and gate information to the external synthesizer with the same step precision as the CV tracks; pitch resolution over MIDI is 127 semitones across the keyboard range. Use TRACKS mode to monitor all tracks at once. The USB connection allows the computer DAW to receive MIDI clock from Hermod+ or supply it to Hermod+; set the clock direction in the system menu based on which device is the master.

**Result:** A unified performance environment where external MIDI gear and Eurorack voices are sequenced and time-synchronized from a single module. Song arrangements that use both a hardware synthesizer and a modular system can be built, stored, and performed from Hermod+ without switching between a separate MIDI sequencer and a modular sequencer.

---

### Patch 4: Effects Processing Showcase

This patch applies Hermod+'s onboard effects to a simple base sequence, demonstrating how the effects chain transforms static programming into dynamic, varied output.

```
HERMOD+ Track 1 CV+GATE ──▶ [Oscillator + Envelope + VCA]
[Effects: Ratchet + Swing + Random active on Track 1]
```

**Setup:** Program a simple 4-note repeating sequence on Track 1. Enter EFFECTS mode and add the following to Track 1 in order: Quantize, then Ratchet at a low probability setting, then Swing at about 25 percent. Connect Track 1 CV and GATE to a complete synthesizer voice.

**Controls:** Listen to the base sequence first with all effects bypassed, then enable them one at a time. Quantize snaps any pitch CVs recorded with imprecision to the nearest semitone. Ratchet adds subdivided trigger bursts at the set probability, turning single steps into rolls and fills at random. Swing delays every other step by the set percentage, moving from metronomic to shuffled feel. The effects chain processes in order from top to bottom; changing the chain order produces different results from the same settings. Add a Random Pitch effect after Quantize to introduce occasional note variations that stay in the quantized key.

**Result:** A simple 4-note sequence that sounds complex and alive because the effects layer transforms it differently on each pass. The same programming produces different results each cycle, removing the static quality of a fixed sequence while keeping the pitch and rhythmic structure as the frame.

---

## Common Mistakes

### "I can see the step I want to edit but turning the encoder is not doing anything"

Hermod+ has four operating modes, each controlled by dedicated buttons: STEP, EFFECTS, TRACKS, and SEQ. The encoder does a different thing in each mode. In STEP mode, the encoder adjusts the pitch of the selected step. In TRACKS mode, it adjusts track-level parameters. In EFFECTS mode, it adjusts the focused effect's parameters. In SEQ mode, it navigates and manages sequence chains. If you are turning the encoder and nothing is responding as expected, you are in the wrong mode for the operation you are trying to perform.

Confirm the lit mode button before adjusting anything. Programming notes requires STEP mode. The mode buttons are the primary navigation system; fluency with mode switching is the foundational skill for working efficiently with Hermod+.

### "I recorded a performance but the timing sounds shifted or off"

Hermod+ records at 96 pulses per quarter note, which is high resolution, but the recording requires an accurate external clock. If your clock source has jitter, instability, or irregular pulse widths, the recorded timing will reflect that instability at high resolution. Clock issues that are inaudible during playback become visible and sometimes audible when examined in the step editor.

Use a stable clock source: either from Hermod+ itself when it functions as clock master, or from a clock module with a clean output. If using a DAW or MIDI clock source, verify that the USB or MIDI connection is not introducing latency. Once a stable clock relationship is established, 96PPQ recording captures performances accurately.

### "Track 9 does not have any CV outputs even though I programmed it"

Hermod+ provides eight CV/Gate output pairs on tracks 1 through 8. Tracks 9 through 16 are MIDI tracks: they transmit data over the MIDI output and USB, and have no corresponding CV jacks on the module's physical outputs. Programming a melody on Track 9 and expecting to find a voltage at a physical output will produce nothing: the information exists and is transmitting, but only over MIDI.

If you need more than eight CV/Gate tracks, the Squarp xp32 expander adds additional CV outputs. For hybrid Eurorack and MIDI setups, keep synthesis voices that need CV on tracks 1 through 8 and route MIDI instruments to tracks 9 through 16.

### "I cannot figure out why there are two different sections called patterns and sequences"

Hermod+ uses a three-level hierarchy for musical organization. A track is one voice or instrument. A pattern is one variation of what that voice plays, and each track stores up to 16 independent patterns. A sequence is a snapshot of which pattern is active on each track simultaneously: it represents a complete system state, like a verse or a chorus. Sequences can be chained together in up to 64 steps to define a complete song structure.

The relationship that clarifies this: patterns are the raw material stored per track, and sequences are the director that chooses which patterns play at the same time across all tracks. When you switch sequences during a performance, every track jumps to the pattern assigned to that sequence simultaneously.

### "I added a ratchet effect but now all my other tracks sound wrong"

Effects in Hermod+ are per-track: each track has an independent effects chain of up to eight slots. An effect applied to Track 1 does not affect Track 2. The confusion arises when effects are added to a track and the interaction between multiple stacked effects on the same track produces unexpected results. Ratchet before an arpeggiator produces a different result than arpeggiator before ratchet, because the signal processed by the second effect is different depending on what the first did.

Add one effect at a time and listen to the result before adding a second. Confirm which track is selected before entering the effects view: it is easy to add an effect to the wrong track when navigating quickly. The effects chain order within a single track is adjustable; if stacking multiple effects, experiment with the ordering to find the combination that produces the intended result.

---

## Advanced Learning Path

1. Work through each of the four modes in dedicated sessions before combining them in performance patches. Spend time only in STEP mode building sequences of different lengths and programming note data; then spend time only in TRACKS mode managing multiple tracks and understanding the relationship between track LEDs and sequence content; then explore EFFECTS mode in isolation, adding and reordering individual effects on a simple test sequence; then investigate SEQ mode for pattern and song arrangement. Understanding what each mode does without the distraction of the others prevents confusion later when switching modes quickly during live performance.

2. Explore all track configuration types available per track. A track can operate as mono CV, poly CV, velocity, modulation, or MIDI depending on configuration. Set up Track 1 as mono and listen to it, then reconfigure it as a velocity track and connect velocity to a VCA alongside a CV track. Connect Track 3 as a MIDI track and listen to it driving an external synth. Understanding which track type to assign based on the destination signal is the core skill for building hybrid Eurorack/MIDI patches, and it requires hands-on time with each type rather than reading about them abstractly.

3. Investigate the effects chain order systematically. Hermod+ processes effects in the order they appear in the chain, top to bottom. A Quantize effect placed before a Transpose effect quantizes the raw sequence and then transposes the quantized result. Placed after Transpose, it quantizes the already-transposed material. Program the same two effects in both orders on the same sequence and listen to the difference. This principle extends to any pair of effects in the chain; the chain order is the composition of the individual effect functions, and reordering produces genuinely different musical results.

4. Understand the Pattern, Sequence, and Track hierarchy through deliberate structure building. Tracks contain individual sequences of notes and gates. Patterns are groups of tracks playing simultaneously. Sequences (in SEQ mode) chain patterns in order for song arrangement. Build a two-pattern arrangement with Pattern A as an intro section and Pattern B as the main theme. Program SEQ mode to play A once then loop B. This workflow is the basis of any arranged live performance from Hermod+; mastering the hierarchy removes the ceiling on set complexity.

5. Explore the 96 PPQ recording resolution for capturing live performances. Set Hermod+ to record mode on a track and play notes in real time from a keyboard or CV keyboard while the clock runs. Hermod+ captures the timing of note events at 96 pulses per quarter note, which is finer timing resolution than most MIDI sequencers. After recording, play back the track and listen to how closely it matches the original performance feel. This is qualitatively different from step programming: the performance nuances of timing variation are preserved rather than quantized to the grid. Understand when quantizing after recording improves the result and when it removes something important.

6. Build a complete patch that uses MIDI out and CV out simultaneously and perform with it live. Connect a keyboard to Hermod+ via MIDI in, connect Track 9 MIDI out to an external synthesizer, and connect Track 1 and Track 2 CV/GATE to Eurorack voices. Record a live performance from the keyboard on Track 1, then use the recorded CV to drive Track 9 as MIDI simultaneously. The experience of performing into the module and hearing the result across multiple signal domains simultaneously is the fastest path to understanding Hermod+ as a complete studio brain rather than just a sequencer.

---

## Pairs Well With

**DivKid Ochd** provides continuously running LFOs for modulating Hermod+ effects parameters and Track CV inputs. Slow Ochd LFOs connected to Hermod+ CV inputs (for mod wheel or velocity tracks) create organic variation on recorded performances without requiring re-programming. Faster Ochd rates on effects parameters such as Swing amount or Ratchet probability produce evolving groove character across the performance. Because Ochd runs independently of Hermod+'s clock domain, the LFO phase relationship to the sequence changes gradually over time, creating long-period modulation cycles that add life to looped arrangements.

**Make Noise Maths** supplies envelope shapes for dynamic control of voices triggered by Hermod+ gates. A Maths end-of-rise output connected back to Hermod+'s clock or reset input can create self-advancing behavior for specific patches. More practically, Maths function outputs driving VCA CV inputs alongside Hermod+ gate signals give each voice an independently shaped amplitude envelope, replacing a dedicated envelope module for simple voices. Maths' ability to operate as both an envelope and a simple LFO makes it flexible enough to handle multiple Hermod+ voices simultaneously.

**Endorphin.es Ground Control** belongs to the same Endorphin.es ecosystem context and provides physical performance control over Hermod+-driven patches. Ground Control's trigger pads and CV outputs can feed into Hermod+ for live recording, manual pattern advance, or direct triggering of effects. In a performance context where Hermod+ holds the arrangement and Ground Control provides the expressive interface, the two modules together cover both the compositional and the performance-gesture dimensions of a complete live set.

**Mutable Instruments Marbles** feeds generative CV and gate material into Hermod+ recording inputs, allowing the module to capture probabilistic sequences and then play them back deterministically. Record a Marbles t1 gate stream and X1 CV stream into Hermod+ at 96PPQ; the result is a fixed sequence that sounds generative because its source was genuinely random. Adjust Marbles' DEJA VU during recording to control how much repetition the captured sequence contains, then use Hermod+ to loop, transpose, and arrange the recorded material as a composed piece.

---

*Hermod+ manual: [Squarp Instruments](https://squarp.net)*
