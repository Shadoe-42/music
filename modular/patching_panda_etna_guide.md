---
title: Etna
manufacturer: Patching Panda
primary_role: SHAPER
secondary_roles: [MODULATOR]
historical_context: true
form_factor: eurorack
functions: [filter, sequencer]
behavior_tags: [clean, evolving, harmonic]
use_cases: [morphing filter voice, evolving texture, rhythmic filtering, parallel voice filtering]
hp: 20
depth: 30mm
memory: basic
transport: receive
screen: false
hybrid: true
cv: full
---

# Etna

**Triple multimode analog filter with eight-stage snapshot morphing sequencer**

![Patching Panda Etna](https://github.com/Shadoe-42/music/raw/main/modular/images/patching_panda/etna/front_panel.jpg)

## Historical Context

The history of voltage controlled filters in synthesis is, in large part, a running argument about whether a filter should do one thing extremely well or several things on demand. Robert Moog's four-pole transistor ladder filter resolved a specific design problem in 1964: low-pass filtering with a steep 24dB per octave rolloff and a saturation characteristic in the transistors that gave the filtered signal a warmth that purely linear circuits could not match. The ladder was a fixed architectural choice. It had one output mode, one response curve, and one set of sonic consequences. Those consequences were beautiful, which is why the ladder is still reproduced and referenced in new designs sixty years later.

The state variable filter, which appeared in instruments like the Oberheim SEM in 1974, was a different answer to the same question. A state variable topology produces low-pass, band-pass, and high-pass outputs simultaneously from the same circuit node, with the signal available at each output at the same time. The designer or player could choose which output to use, or combine them in varying ratios, and the filter's character changed accordingly. This was not a better filter than the ladder; it was a different argument about what a filter should offer. Where the ladder said "one mode, executed perfectly," the state variable said "multiple modes, available simultaneously, player decides."

The Patching Panda Etna is a further extension of that argument. Three complete analog filter circuits, each independently switchable between low-pass (24dB per octave, four-pole), band-pass, and high-pass (12dB per octave, two-pole) operation, with individual frequency and amplitude controls, individual audio inputs with daisy-chain normalization, and individual outputs as well as a mixed output. The three filters are built around the SSI2164 voltage controlled amplifier chip, a modern design by David Rossum, co-founder of E-mu Systems, whose Emulator sampler and SP-1200 drum machine used the original SSM2164 chip in circuits where noise accumulation in cascaded stages was a critical concern. The SSI2164 is specified for extremely low noise and wide dynamic range; in the Etna, these properties mean that three parallel filters can process audio simultaneously without the accumulated noise floor that would result from chaining three independent filter modules in series.

The Q compensation circuit addresses a behavior that appears in most resonant filter designs: as resonance increases, the filter removes increasing amounts of energy from the signal, and the output grows quieter at high Q settings. The Etna's compensation circuit counteracts this by increasing the filter's output level proportionally as resonance rises, so the perceived loudness remains consistent across the full resonance range. This is not universal in filter design; it is a deliberate choice that prioritizes usability over strict circuit transparency.

The snapshot system is where the Etna diverges from every conventional multimode filter in the corpus. A snapshot is a stored record of the module's slider positions at a given moment: the three filter frequencies, the three amplitude levels, the resonance setting, and the glide time between snapshots. The Etna stores up to eight snapshots and plays them back in sequence, driven by a clock input. The filter morphs between stored states over a programmable glide time, producing continuous analog transitions between completely different filter configurations. The concept of morphing between stored parameter states exists in digital synthesis: DX7 operator scaling, D-50 partial morphing, later vector synthesis architectures. The Etna implements the same concept through analog circuitry driven by digital memory. The filter transitions are smooth, voltage-driven, and fully analog; only the storage and sequencing of target positions is digital. Patching Panda, based in Barcelona, describes this architecture as allowing the filter to become "a morphing filter sequencer" in addition to its conventional role as a static multimode filter. Both descriptions are accurate, and both are worth using depending on what the patch demands.

---

## Quick Start

The Etna is a triple multimode analog filter with a built-in snapshot sequencer. The three filter sections (F1, F2, F3) can process audio independently or share a single source through daisy-chain normalization. Start here to hear it as a conventional filter before introducing the snapshot system.

1. Patch audio into IN1.
2. Patch OUT1 or MIX into your mixer.
3. Set the FRQ1 knob to 12 o'clock. Set FRQ1 slider to center. Set Q slider to minimum.
4. Confirm the F1 switch is set to LP.
5. You should hear your source filtered at the low-pass cutoff position set by knob and slider together.
6. Sweep the FRQ1 knob to hear the cutoff move. Raise the Q slider slowly to introduce resonance.
7. Switch F1 from LP to BP and hear the character shift: band-pass output is narrower and has a different peak character than low-pass.
8. Switch to HP and hear high-frequency content pass while low frequencies are attenuated.
9. To hear all three filters on the same source: confirm IN2 and IN3 are unpatched (they receive IN1 by daisy-chain normalization). Patch OUT1, OUT2, and OUT3 each to a separate mixer channel. Set each filter section to a different mode and different FRQ position. You now have three simultaneous filtered versions of one source.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 20 HP |
| Depth | 30 mm |
| Power | 165 mA +12V / 88 mA -12V / 0 mA +5V |

The +12V draw of 165mA is significant for a single module. Confirm available headroom on the +12V bus before installing, particularly in smaller cases with multiple processing modules.

---

## The Analog Core: Three Filters in Parallel

The Etna contains three independent analog filter circuits, designated F1, F2, and F3. Each filter is the same circuit: a four-pole topology capable of 24dB per octave low-pass response, selectable to band-pass or high-pass operation via a panel switch. The output topology changes depending on the selected mode: in low-pass configuration, the output is taken from the fourth filter pole; in high-pass configuration, the output is taken from an earlier tap in the circuit, which produces a shallower 12dB per octave rolloff. Band-pass is a middle position whose center frequency and width are determined by the Q setting.

Each filter section has its own set of controls: a hardware knob for frequency (FRQ1, FRQ2, FRQ3), a digital slider for frequency (also labeled FRQ1, FRQ2, FRQ3), a CV input with an attenuverter (a control that scales CV and can invert it; turning it counterclockwise attenuates and eventually inverts the incoming signal) for individual frequency modulation, and an amplitude slider (AM1, AM2, AM3). The hardware knob and digital slider both control cutoff frequency; their positions are summed together at the filter's frequency control point. This means that the slider and knob together determine the total cutoff position, and modulation via CV is added on top of their combined position.

**Q compensation.** The single Q slider controls resonance for all three filters simultaneously; there is no per-filter resonance control. As the Q slider rises, resonance increases across all three filters equally. The Q compensation circuit maintains consistent output level as resonance increases, so the signal does not thin or disappear at high Q settings. At maximum Q, all three filters self-oscillate, producing pitched sine tones at their respective cutoff frequencies. With three filters set to different frequencies and all in self-oscillation, the Etna becomes a three-voice sine tone generator; patching CV to the individual frequency inputs at that point produces independent pitch control per voice.

**Audio inputs and daisy-chain normalization.** The three audio inputs (IN1, IN2, IN3) are connected through normalization: when IN2 is unpatched, it receives the signal from IN1. When IN3 is unpatched, it receives the signal from IN2 (or IN1 if IN2 is also unpatched). This means a single audio source patched into IN1 feeds all three filters without any additional cables. Patching a signal directly into IN2 or IN3 breaks the normalization for that input and below, providing that filter with its own independent source. A three-voice patch (three separate audio signals, each processed by its own filter) requires three cables, one into each input.

**Individual and mixed outputs.** OUT1, OUT2, and OUT3 each carry their respective filter's output at approximately 10Vpp under normal conditions (up to 18Vpp at high resonance settings). The MIX output carries all three filters summed together, with the AM sliders (AM1, AM2, AM3) controlling each filter's contribution to the mix independently. The AM sliders are part of the snapshot memory system: stored snapshots can specify different amplitude balances between the three filters, allowing the mix character to change as the sequencer advances.

**FREQ ALL.** A global frequency CV input and hardware knob that offsets all three filter cutoff frequencies simultaneously by the same amount. FREQ ALL does not override the individual FRQ controls; it adds its offset on top of whatever each filter's individual knob, slider, and CV are already doing. Sweeping FREQ ALL sweeps all three filters together while preserving their relative offsets.

**FM input.** A single FM input with a dedicated attenuator drives all three filter frequencies simultaneously with audio-rate or control-rate modulation. Patching an oscillator into FM and turning up the attenuator produces frequency modulation of all three filter cutoffs at audio rate, creating complex harmonic content that changes as the FM source's pitch and the filter frequencies interact. At low FM attenuator settings, the effect is a subtle harmonic shimmer; at high settings, it becomes dense and inharmonic.

---

## The Digital Layer: Snapshots

A snapshot is a stored record of all slider positions at one moment in time. Specifically, each snapshot stores: FRQ1, FRQ2, FRQ3 (individual filter frequency slider positions), AM1, AM2, AM3 (individual filter amplitude slider positions), Q (resonance setting), and GLIDE (the time to transition from the previous snapshot to this one). The Etna stores up to eight snapshots.

When the snapshot sequencer advances from one snapshot to the next, the module does not jump instantly to the new settings. Instead, it glides from the current slider positions to the stored positions over the GLIDE time specified in the destination snapshot. GLIDE is a linear slope with a range of 0 to 500ms; at zero, transitions are instantaneous steps; at maximum, transitions take half a second of continuous analog movement. Each snapshot specifies its own GLIDE time, so the sequencer can alternate between slow morphs and instant snaps within a single sequence.

The hardware knobs (FRQ1, FRQ2, FRQ3) and incoming CV are not stored in snapshots. Snapshots capture slider positions only. This means the hardware knobs and CV inputs remain live and summed at all times, independent of whatever the snapshot sequencer is doing. You can record a sequence of slider states and then sweep the FRQ1 knob to transpose all three snapshots' filter positions upward simultaneously.

**Encoder modes.** The encoder, the rotary control at the center of the module, operates in three modes indicated by LED color:

- **EDIT mode (green LED):** Turning the encoder selects which snapshot is currently active for editing. The sliders control that snapshot's stored values. Moving a slider in EDIT mode immediately writes the new position to the selected snapshot and also applies it to the analog filter in real time, so you hear the change as you make it.

- **POSITION mode (orange LED):** Turning the encoder manually steps through snapshots in real time, overriding the clock-driven sequencer. Useful for live performance or for auditioning snapshots in sequence without a clock patched.

- **LENGTH mode (red LED):** Turning the encoder sets the number of snapshots the sequencer cycles through, from 1 to 8. A length of 2 cycles between snapshots 1 and 2; a length of 6 cycles through 1 to 6. The LENGTH setting determines the sequence without deleting any stored snapshots beyond the length boundary.

Press the encoder to step through EDIT, POSITION, and LENGTH modes in order.

**EDIT ALL.** A dedicated button that, when held during slider adjustment in EDIT mode, writes the moved slider's new position to all snapshots simultaneously. This is a global trim: adjusting AM1 while holding EDIT ALL sets every snapshot's AM1 level to the new value, erasing the per-snapshot variation for that parameter. Useful for resetting a parameter across the whole sequence or for globally raising or lowering Q across all snapshots without changing their relative frequency differences.

---

## The Snapshot Sequencer

With a clock patched into the CLOCK input, the sequencer advances one step per clock pulse. Each clock edge moves the sequencer forward one snapshot and begins the glide transition to the new stored settings over the GLIDE time embedded in the destination snapshot. The sequencer does not wait for the glide to complete before accepting the next clock; if a clock pulse arrives before the previous glide finishes, the module begins transitioning toward the new snapshot from wherever the glide currently is, which can produce overlapping or interrupted morphs at fast clock rates.

**RESET input.** A gate or trigger at RESET returns the sequencer to snapshot 1 immediately. RESET overrides the playback mode and is available regardless of whether a clock is patched.

**POS CV input.** A voltage from 0 to 10V that selects the current playback position directly, bypassing clock-driven stepping. 0V selects snapshot 1; 10V selects the snapshot at the current LENGTH boundary. Patching a step sequencer's CV output here allows direct positional control of which snapshot is active.

**LEN CV input.** A voltage from 0 to 10V that sets the sequence length directly, overriding the encoder LENGTH setting. 0V sets length to 1; 10V sets length to 8. LEN CV allows the sequence length to change under voltage control mid-performance.

**Playback modes.** Three sequencer playback behaviors are available, set by holding EDIT ALL and pressing PLAY during EDIT ALL mode:

- **FORWARD:** Snapshots advance in order from 1 to the LENGTH boundary, then loop back to 1.
- **PENDULUM:** Snapshots advance forward to the LENGTH boundary, then reverse back to 1, then forward again, producing a back-and-forth sweep.
- **RANDOM:** Each clock pulse selects a random snapshot within the LENGTH boundary. With high GLIDE times, RANDOM mode produces continuously shifting, unpredictable analog filter morphing.

**CV FREQ3 output.** The Etna outputs a CV signal from 0 to 9V that represents the current position of the F3 frequency, including all slider, knob, CV, and snapshot contributions summed together. This output allows the snapshot sequencer to drive other modules in the rack: patch CV FREQ3 to an oscillator's V/Oct input, a second filter's frequency CV, or any CV destination to send the Etna's morphing filter position outward as a modulation source. The snapshot sequence then becomes a modulation sequence for the entire patch, not just the Etna's own filters.

**Clock divider.** Holding the encoder for three seconds enters clock division mode. The encoder then sets the division ratio between the incoming clock and the sequencer's advance rate. The DIV indicator LED illuminates while division is active. This allows a master clock running at patch tempo to drive the Etna sequencer at a slower rate without an external clock divider module.

---

## Signal Flow and Patch Diagrams

### Basic: One source, three filters in parallel (unified voice)

```
[Source] ──[A]──▶ [IN1]
                    │
                    ├── [F1 LP 24dB] ──[A]──▶ [OUT1] ──▶ [Mixer Ch1]
                    │
                    ├── [F2 BP] ──[A]──▶ [OUT2] ──▶ [Mixer Ch2]
                    │
                    └── [F3 HP 12dB] ──[A]──▶ [OUT3] ──▶ [Mixer Ch3]
                         (IN2, IN3 unpatched: daisy-chain normalization)
```

Three simultaneous filtered versions of one source, each mode independent. Blend at the mixer to combine their characters.

### Intermediate: Three sources, three independent voices

```
[Voice 1 VCO] ──[A]──▶ [IN1] → [F1] ──[A]──▶ [OUT1] ──▶ [VCA 1] ──▶ [Mixer Ch1]
[Voice 2 VCO] ──[A]──▶ [IN2] → [F2] ──[A]──▶ [OUT2] ──▶ [VCA 2] ──▶ [Mixer Ch2]
[Voice 3 VCO] ──[A]──▶ [IN3] → [F3] ──[A]──▶ [OUT3] ──▶ [VCA 3] ──▶ [Mixer Ch3]
```

Each filter processing its own voice independently. Individual FRQ1/2/3 CVs allow per-voice brightness control. Q affects all three simultaneously.

### Advanced: Snapshot-driven morphing with CV FREQ3 as modulation output

```
[Clock] ──[G]──▶ [CLOCK IN]
[Envelope] ──[C]──▶ [FREQ ALL CV]
                                        [CV FREQ3] ──[C]──▶ [VCO FM In]
[Source] ──[A]──▶ [IN1] → [F1/F2/F3] ──[A]──▶ [MIX] ──▶ [Mixer]
```

The snapshot sequencer advances on each clock, morphing all three filter states according to stored snapshots. The envelope sweeps all three filters together via FREQ ALL. CV FREQ3 exports F3's current position to the VCO, coupling the filter's morphing sequence to the oscillator's timbre.

---

## Essential Parameters

**FRQ1, FRQ2, FRQ3 (knobs).** Hardware frequency controls for each filter section, active at all times and summed with the corresponding FRQ sliders. These are always live; they are not stored in snapshots. Use the knobs to set a baseline frequency position and the sliders to program the range of positions the snapshot sequence will traverse above or below that baseline.

**FRQ1, FRQ2, FRQ3 (sliders).** The digital sliders that are stored in each snapshot. These represent the snapshot-programmable component of each filter's cutoff frequency. When the snapshot sequencer morphs between states, it is these values that transition; the hardware knobs remain fixed at their current positions throughout.

**AM1, AM2, AM3 (sliders).** Per-filter amplitude controls that set each filter's contribution to the MIX output. These are stored in snapshots, which means the mix balance between the three filters can change with each step of the sequence. A sequence that alternates between high AM1/low AM3 and low AM1/high AM3 will shift the character of the MIX output between filter voices even if the frequencies do not change.

**Q (slider).** Global resonance control for all three filters. Stored in snapshots. At minimum, the filters have no resonance peak. At maximum, all three self-oscillate at their respective frequencies. Because Q affects all three simultaneously, varying Q across snapshots changes the resonance character of the entire filter bank together; there is no per-filter resonance control.

**FQ ALL (slider).** A global frequency offset stored in snapshots that adds to all three individual filter frequencies simultaneously. This is the slider equivalent of the FREQ ALL hardware knob and CV input. FQ ALL in snapshots allows the sequencer to program global frequency shifts across the entire filter bank as part of the morphing sequence, separate from per-filter programming.

**GLIDE (slider).** Sets the transition time from the previous snapshot to the current one, 0 to 500ms. Stored per snapshot. A snapshot with GLIDE at minimum produces an instant transition to its stored values; a snapshot with GLIDE at maximum takes 500ms to fully arrive. Varying GLIDE across snapshots creates rhythmic contrast between morphing and stepping behavior within a single sequence.

**CV FRQ1, CV FRQ2, CV FRQ3 (inputs with attenuverters).** Individual frequency CV inputs per filter. The attenuverter knob for each controls the depth and polarity of the incoming CV. These are live analog inputs; their contribution to filter frequency is not stored in snapshots and is always summed with the knob and slider positions.

**FREQ ALL CV (input).** A CV input that offsets all three filter frequencies simultaneously, summed with the individual CVs and the FQ ALL slider. Patching an envelope here sweeps all three filters together, tightening or opening the filter bank as a unified gesture.

**FM (input with attenuator).** An audio-rate or control-rate signal that modulates all three filter frequencies simultaneously. The FM attenuator scales the depth of this modulation from zero to maximum. At low attenuator settings and a slow source (LFO), FM adds slow drift to all three cutoffs together. At high attenuator settings and an audio-rate source (oscillator), FM produces complex harmonic multiplication across all three filter outputs simultaneously.

**POS CV (input).** A 0 to 10V input that directly sets the sequencer's playback position. 0V points to snapshot 1; 10V points to the snapshot at the current LENGTH boundary. POS CV overrides clock-driven stepping when a voltage is present.

**LEN CV (input).** A 0 to 10V input that sets the sequence length. 0V equals length 1; 10V equals length 8. LEN CV allows dynamic sequence length changes under voltage control.

**CV FREQ3 (output).** An output that carries the current F3 frequency position as a CV signal from 0 to 9V. This is a read of F3's actual analog state, summing all contributions: knob, slider, snapshot, and incoming CV. Using this output allows the Etna's snapshot sequencer to drive other modules' parameters in sync with its own filter morphing.

---

## Advanced Learning Path

**EDIT ALL as a live performance tool.** While the sequencer is running, holding EDIT ALL and moving a slider writes that slider's new position to every snapshot simultaneously. This allows mid-performance global adjustment: raising Q across all snapshots, pulling back a filter's overall frequency range, or lowering one voice's amplitude in the mix without disrupting the relative differences between snapshots. It is a way to reshape the entire sequence's character without stopping playback.

**Exploiting CV FREQ3 as a modulation source.** The CV FREQ3 output converts the Etna's snapshot morphing into a modulation sequence for the rest of the rack. Patch it to an oscillator's linear FM input and the oscillator's timbre tracks the Etna's F3 filter position. Patch it through an attenuverter to another filter's frequency CV and the second filter follows F3's movement at a scaled depth. The Etna then drives not just its own internal character but the broader patch's behavior over time.

**Clock division and polyrhythmic filtering.** With the clock divider active (encoder held three seconds to set the division), the Etna advances its snapshot sequence at a slower rate than the master clock. A four-to-one division means the filter morphs every four clock steps while the rest of the patch moves at full tempo. At two-to-one, the filter morphs every other beat, creating an alternating texture. Combined with PENDULUM mode, clock division produces slow oscillation of the filter bank against the faster rhythm of the patch.

**Independent voices with a shared Q sweep.** With three separate oscillators patched into IN1, IN2, and IN3, the three filters act as independent voice processors. Because Q is global, a single Q slider movement applies resonance equally to all three voices. This is a limitation and a feature simultaneously: the resonance character is always consistent across the voices, which prevents timbral conflict between them at the cost of independent per-voice control.

**Self-oscillation as a voice.** At maximum Q, all three filters self-oscillate and produce sine tones at their respective cutoff frequencies. Patch individual CVs into CV FRQ1, CV FRQ2, and CV FRQ3 to pitch-control each self-oscillating filter independently. The three oscillating filters share a single Q setting, which means all three are simultaneously at or near self-oscillation. This is a three-voice analog sine oscillator with independent frequency CV per voice; the snapshot system allows the three base frequencies to morph over time without external CV.

**Snapshot programming strategy: anchor and vary.** A productive approach for snapshot programming is to establish a reference state in snapshot 1 (the "anchor") and then vary individual parameters in subsequent snapshots. Snapshot 2 might change only FRQ1. Snapshot 3 might change FRQ1 and AM2. Snapshot 4 might return to the anchor settings. The sequence then produces clearly audible, purposeful movement because each departure from the anchor is identifiable. Random distribution of slider positions across all eight snapshots tends to produce complex motion without a clear reference point, which can be appropriate for texture work but loses the sense of forward movement that a purposeful sequence provides.

**Using POS CV for direct snapshot control.** Patching a step sequencer's CV output into POS CV and removing the clock input puts the Etna into fully external positional control. Each step of the external sequencer selects a specific Etna snapshot, with GLIDE still applied on each transition. The Etna's sequence then follows the external sequencer's rhythm and order precisely, which allows non-linear snapshot playback: snapshot 3, then 1, then 5, then 2, in whatever order the external sequence specifies.

---

## Pairs Well With

**Hermod+ (Squarp Instruments).** The Hermod+ provides clock and CV outputs for driving the Etna's CLOCK, RESET, POS, and LEN inputs simultaneously from a single multitrack sequencer. Individual CV tracks can address each filter's frequency CV input, allowing per-filter pitch sequencing alongside the snapshot morphing.

**MISO (Tiptop Audio).** The MISO's attenuverter and offset capabilities are well-matched to conditioning the CV FREQ3 output before it reaches another module's CV input. Scaling and offsetting the 0 to 9V range allows precise mapping to a destination module's expected input range.

**Multiple VCOs.** Three oscillators patched into IN1, IN2, IN3 turns the Etna into a parallel filter bank for a three-voice chord. Each voice has independent frequency control; the shared Q and the snapshot system shape all three voices as a coherent ensemble rather than three separate filter settings.

**Qu-Bit Chord V2.** Chord V2 outputs polyphonic chords as a single summed signal or individual voice outputs. The individual voice outputs paired with the Etna's three independent inputs allows per-voice filter processing of a chord, with the snapshot sequencer morphing the filter character over chord progression changes.

**Pamela's Pro Workout (ALM Busy Circuits).** Pamela provides clock with division and multiplication, making it a straightforward source for the Etna's CLOCK input at any subdivision of the master tempo. Multiple outputs from Pamela can drive CLOCK and RESET simultaneously for rhythmically structured snapshot resets.

**DivKid Ochd.** The Ochd's eight slow LFO outputs are an efficient source for FM, FREQ ALL CV, and individual frequency CVs simultaneously. Patching four or five Ochd outputs into the Etna's CV inputs while the snapshot sequencer runs creates layered movement where slow analog drift combines with programmed snapshot morphing.

---

## Common Mistakes

**Ignoring the slider-knob sum.** The hardware FRQ knobs and the FRQ sliders both contribute to each filter's cutoff frequency. A common mistake is to program snapshots with slider positions that assume the knobs are at zero. With a knob at 12 o'clock and a slider also at center, the actual cutoff is significantly higher than either control alone suggests. Either set the knobs to minimum before programming snapshots, or account for the knob contribution explicitly.

**Fast clock with long GLIDE.** If the GLIDE time in a snapshot is longer than the clock interval, the sequencer will advance to the next snapshot before the previous glide completes. The result is a chain of interrupted transitions that never fully arrives anywhere. This can be intentional (producing smooth, continuous movement) or it can be an accidental state where the filter never settles. Confirm that GLIDE time is shorter than the clock interval unless the interrupted morph effect is the goal.

**Treating Q as a per-filter control.** There is one Q slider for all three filters. Patching audio into IN1 and expecting to set resonance independently for F1, F2, and F3 is not possible. If per-voice resonance control is needed, the Etna is not the right tool; pair it with individual filter modules for independent Q per voice.

**Forgetting that AM sliders control MIX, not individual outputs.** The AM1, AM2, AM3 sliders set each filter's contribution to the MIX output. The individual OUT1, OUT2, OUT3 outputs are not affected by the AM sliders; they output their respective filter at full level regardless of AM position. If a filter is silent in the MIX output but audible at its individual output, the AM slider is the cause.

**Self-oscillation frequency drift.** At maximum Q, all three filters self-oscillate. The self-oscillation pitch tracks the FRQ knob, slider, CV, and snapshot values, so any drift in these inputs will drift the oscillation pitch. Without pitch-stable CV patched into the frequency inputs, self-oscillating filters will drift with temperature and power supply variation. Use the individual FRQ CV inputs with a stable V/Oct source to hold the oscillation pitch reliably.

---

## What's Next

The Etna processes audio through analog filters while programming their behavior over time through snapshot memory. With the filter established as a morphing voice, the next useful concept is how to coordinate multiple morphing processes in a patch: the Etna's CV FREQ3 output driving a second module, the snapshot clock synced to a master sequencer, and GLIDE times coordinated with the overall tempo.

The guides for the 4ms Pamela's Pro Workout and Hermod+ cover clock routing and multi-output CV coordination that applies directly to driving the Etna's CV inputs from a single sequencing hub.

---

*Depth: 30mm. Power: 165mA +12V / 88mA -12V / 0mA +5V.*
