---
title: Qu-Bit Chord V2
manufacturer: Qu-Bit Electronix
primary_role: GENERATOR
secondary_roles: [MODULATOR]
form_factor: eurorack
functions: [oscillator, wavetable, polyphonic]
behavior_tags: [harmonic, polyphonic, cv-friendly, clean, stable, performance-oriented]
use_cases: [chord generation, polyphonic voice, harmonic source, melodic lead over chords]
hp: 14
depth: 23
historical_context: false
---

# Qu-Bit Chord V2

![Qu-Bit Chord V2](https://github.com/Shadoe-42/music/raw/main/modular/images/qubit/chord_v2/front_panel.jpg)  
*Four-voice wavetable oscillator with individual interval outputs, seven chord types, seventeen voicings, and four polyphony modes in 14HP*

## Quick Start: Get Sound in 5 Minutes

Chord V2 is a four-voice wavetable oscillator that generates complete chords from a single pitch CV. Each voice in the chord has its own dedicated output (Root, Third, Fifth, Seventh), plus a Mix output that combines all four. You can process every voice independently or use the Mix as a single combined source.

1. Patch Hermod+ CV output (1V/oct) into the V/Oct input
2. Patch Hermod+ gate output into a VCA or Punch V3 trigger
3. Patch the Mix output to your mixer or effects chain
4. Set Quality to 12 o'clock (major chord)
5. Set Voicing to 12 o'clock (root position)
6. Set Wave to 9 o'clock (basic waveform)
7. Send a note from Hermod+ and listen to the four-voice chord
8. Turn Quality clockwise and counterclockwise to hear different chord types
9. Turn Voicing to hear the same chord in different inversions

That is the core architecture. The four individual outputs are where the real patching begins.

## Key Specs

| Spec | Value |
|------|-------|
| HP | 14 |
| Depth | 23mm |
| +12V | 122mA |
| -12V | 25mA |
| 5V | 0mA |
| Voices | 4 |
| Chord types | 7 (factory) |
| Voicing stages | 17 |
| Wavetable banks | 8 |

## Essential Parameters

**Quality** selects the chord type. The seven factory types are: major, minor, dominant 7th, diminished, augmented, sus4 with major 7th, and sus2 with minor 7th. Quality has a CV input, which makes chord type changes a patchable, sequenceable parameter rather than a manual decision. An LFO or step sequencer into Quality CV produces harmonic movement without changing the root pitch.

**Voicing** determines how the four voices are arranged across the register. At its simplest, it selects chord inversion, moving the root note up an octave so the third becomes the lowest voice, or the fifth, and so on. The 17 voicing stages include standard inversions and spread voicings that place the chord tones further apart from each other. Voicing has a CV input. Slow modulation of Voicing produces harmonic motion that is different from pitch change or chord type change: the same notes rearranging themselves in space.

**Wave** controls the position within the current wavetable bank. All four voices use the same wavetable simultaneously. The eight factory banks cover traditional oscillator shapes, vocal formant-style waveforms, organ emulation, and chiptune timbres. Transitions between waveforms as Wave moves are smoothed, which makes Wave a natural target for slow LFO modulation to produce gradual timbral evolution. Wave has a CV input.

**Mode button** cycles through four operating modes, indicated by LED color. In standard Chord mode (LED off) the 1V/oct input controls all four voices as a complete chord. In Melody mode (LED blue) the Seventh output becomes an independent voice controlled by the Lead input, while the remaining three voices form a triad controlled by 1V/oct; press the Triad button to limit the Mix output to those three voices, leaving the Seventh free for a separate lead line. In Free Poly mode (LED green) all four voices are fully independent, each with its own V/Oct input. In Unison Poly mode (LED teal) all four voices are tuned together in unison but can be spread and detuned individually.

**V/Oct input** sets the root pitch of the chord in standard Chord mode. The four voices are generated at the correct intervals above this pitch according to the selected chord type and voicing. Coarse and Fine knobs provide manual pitch adjustment.

**FM input** accepts linear frequency modulation with an onboard attenuator. This allows external audio rate modulation of the oscillator pitch, adding harmonic sidebands and timbral complexity to the wavetable output.

**Individual outputs (Root, Third, Fifth, Seventh)** carry each voice of the chord as a separate audio signal. These outputs are the primary sound design resource of the module. Each voice can be routed to its own VCA, filter, effects chain, and mixer channel independently, treating the four-voice chord as four separate monophonic signals that happen to be harmonically related.

**Mix output** carries all four voices summed together. It is the most immediate output for basic use, but it removes the ability to process voices independently.

## Why This Excels

The individual voice outputs are what distinguish Chord V2 from a simple chord generator. Most polyphonic sources in Eurorack sum their voices internally and offer a single output. Chord V2 offers five outputs simultaneously (four individual and one combined), which means a four-voice chord becomes four independent signal paths. The Root output can go through a long-decay VCA and a lowpass filter to become the harmonic foundation. The Seventh output can go through a shorter envelope and a different filter to become the melodic edge of the same chord. The Mix output can go to a reverb or lo-fi delay as a unified texture. All of this happens simultaneously from a single pitch CV input.

Voicing as a CV-controllable parameter separates Chord V2 from a static chord lookup table. The 17 voicing stages mean the same chord type, played from the same root pitch, can move through fundamentally different harmonic arrangements without changing any note in the chord. Sequencing or modulating the Voicing CV while a chord sustains produces a kind of harmonic animation: the notes shift register relationship with each other while staying harmonically correct.

Melody mode addresses a practical limitation of chord generators: what happens when you want a melodic line over the underlying harmony. By freeing the Seventh output from the chord voicing and making it independently pitchable via the Lead input, Chord V2 provides a dedicated slot for a lead voice that remains tonally related to the chord below it. The three remaining voices continue to track the main 1V/oct input. This is a two-hand or two-sequencer architecture without requiring additional oscillators.

The eight factory wavetable banks, combined with the Wave CV input, give Chord V2 a significant timbral range beyond what fixed-waveform oscillators offer. The smoothed transitions between waveforms mean Wave modulation is usable as a musical parameter rather than a switching artifact. An LFO on Wave at a rate slow enough to complete one cycle over several bars produces timbral evolution that tracks the length of a musical phrase.

## Patches

### Patch 1: Four-Voice Chord with Envelope Shaping

Basic four-voice chord in standard mode with Punch V3 shaping the Root and Seventh outputs independently before the mix.

```
[Hermod+] ── CV (1V/oct) ────────────────▶ [Chord V2 V/Oct]
          └─ Gate out ────────────────────▶ [Punch V3 CH1 TRIG|CV]
          └─ Gate out ────────────────────▶ [Punch V3 CH2 TRIG|CV]

[Chord V2 Root OUT] ─────────────────────▶ [Punch V3 CH1 IN]
[Chord V2 Seventh OUT] ──────────────────▶ [Punch V3 CH2 IN]
[Chord V2 Mix OUT] ──────────────────────▶ [MixUp CH1]

                                            Punch CH1: Vintage, DECAY 1 o'clock, CURVE 10 o'clock
                                            Punch CH2: CV, DECAY 9 o'clock, CURVE 12 o'clock

                             [Punch V3 CH1 OUT] ──▶ [MixUp CH2]
                             [Punch V3 CH2 OUT] ──▶ [MixUp CH3]
```

**Setup:** Hermod+ sends pitch CV to Chord V2 and gate to both Punch V3 channels. Chord V2 Root output feeds Punch CH1; Seventh output feeds Punch CH2. Mix output goes directly to MixUp CH1.

**Controls:** Punch CH1 shapes the Root with a longer, softer decay; the harmonic foundation sustains. Punch CH2 shapes the Seventh with a shorter, snappier envelope; the highest voice attacks and releases before the foundation. MixUp balances the unshaped Mix against the two independently shaped voices. Adjust Quality on Chord V2 to change chord type and listen to how the same envelope relationships sound across major, minor, and diminished. Try changing Voicing while the patch runs to hear the same notes rearranging in register.

**Result:** A four-voice chord where different voices have different envelope characters simultaneously: the root sustains while the seventh snaps, with the full mix available as a separate blend point.

---

### Patch 2: Melody Mode, Lead Over Triad

Melody mode with Hermod+ providing the chord root and a second sequencer track driving the Seventh as an independent lead voice.

```
[Hermod+] ── CV track 1 (1V/oct) ────────▶ [Chord V2 V/Oct]
          └─ CV track 2 (1V/oct) ────────▶ [Chord V2 Lead IN]
          └─ Gate out ────────────────────▶ [Punch V3 CH1 TRIG|CV]

                                            Mode: Melody (LED blue)
                                            Triad button: active
                                            Quality: minor
                                            Voicing: 12 o'clock

[Chord V2 Mix OUT] ──────────────────────▶ [Punch V3 CH1 IN]
[Chord V2 Seventh OUT] ──────────────────▶ [Moon Phase IN L]

                                            Moon Phase mode: LP+BP
                                            Moon Phase ST f: 11 o'clock
                                            Moon Phase SPAN: 1 o'clock

                             [Punch V3 CH1 OUT] ──▶ [MixUp CH1]
                             [Moon Phase OUT L] ──▶ [MixUp CH3 L]
                             [Moon Phase OUT R] ──▶ [MixUp CH3 R]
```

**Setup:** Hermod+ track 1 drives the chord root via V/Oct. Track 2 drives the Seventh independently via the Lead input. Set Mode to Melody (LED blue) and press Triad to limit Mix to three voices. Chord V2 Mix (three-voice triad) goes through Punch V3 for envelope shaping. Seventh output goes through Moon Phase for filtered stereo widening.

**Controls:** The triad tracks track 1, forming the harmonic backdrop. The Seventh tracks track 2 independently, creating a lead melody that is always in a harmonically sensible relationship to the chord below it. Moon Phase's LP+BP mode filters and widens the Seventh voice into stereo before it reaches the mix. Adjust Moon Phase ST f to change how bright the lead voice sounds. Try different Quality settings to change the chord type while the lead line continues.

**Result:** A two-layer patch from one module: a three-voice chordal foundation and an independent melodic voice, with the lead filtered and widened by Moon Phase while the triad is shaped by Punch V3.

---

### Patch 3: Voicing CV Modulation

Standard chord mode with Zadar slowly modulating the Voicing CV input, creating continuous harmonic rearrangement of the same chord over time.

```
[Hermod+] ── CV (1V/oct) ────────────────▶ [Chord V2 V/Oct]

[Zadar CH1] ─────────────────────────────▶ [Chord V2 Voicing CV]
(slow envelope, 12-20 seconds, infinite repeat)

[Zadar CH2] ─────────────────────────────▶ [Chord V2 Wave CV]
(different shape, 8-15 seconds, infinite repeat)

                                            Mode: Chord (LED off)
                                            Quality: major
                                            Voicing: 9 o'clock (base)
                                            Wave: 10 o'clock (base)

[Chord V2 Mix OUT] ──────────────────────▶ [Lyra-8 FX Audio In]

                                            Lyra-8 FX: Stage 1 self-mod
                                            Lyra-8 FX Feedback: 11 o'clock

                         [Lyra-8 FX Main Out] ──▶ [MixUp CH1]
```

**Setup:** Hermod+ holds a sustained chord root via V/Oct. Zadar CH1 in infinite-repeat mode modulates Voicing CV, cycling through the 17 voicing stages over 12 to 20 seconds. Zadar CH2 in infinite-repeat mode modulates Wave CV, slowly shifting the wavetable position over 8 to 15 seconds. Chord V2 Mix goes into Lyra-8 FX for lo-fi delay processing.

**Controls:** The chord root stays fixed. The Zadar channels slowly move the chord through different inversions and voicings (Voicing CV) while the timbre shifts across the wavetable (Wave CV). The result is a sustained chord that changes its internal register arrangement and tonal character without ever changing its fundamental pitch or type. Lyra-8 FX adds lo-fi delay degradation to the combined texture. Adjust the Zadar rates to speed up or slow down the harmonic movement.

**Result:** A slowly evolving harmonic texture where the same chord continuously rearranges itself in register and timbre without changing its root or type: the chord version of granular time-domain transformation.

---

### Patch 4: Split Output Processing

Root and Mix outputs routed to completely different processing chains simultaneously, treating one voice as a foundation and the combined chord as a texture.

```
[Hermod+] ── CV (1V/oct) ────────────────▶ [Chord V2 V/Oct]
          └─ Gate out ────────────────────▶ [Punch V3 CH1 TRIG|CV]

[Chord V2 Root OUT] ─────────────────────▶ [Punch V3 CH1 IN]
[Chord V2 Mix OUT] ──────────────────────▶ [Lyra-8 FX Audio In]

                                            Punch CH1: Vintage
                                            DECAY: 1-2 o'clock
                                            CURVE: 11 o'clock

                                            Lyra-8 FX: Stage 1 self-mod
                                            Stage 2: external (no CV)
                                            Feedback: 10 o'clock
                                            Distortion drive: 10 o'clock

[Punch V3 CH1 OUT] ──────────────────────▶ [Moon Phase IN L]
                                            Moon Phase mode: LP+LP
                                            Moon Phase ST f: 10 o'clock

                         [Moon Phase OUT L] ──▶ [MixUp CH3 L]
                         [Moon Phase OUT R] ──▶ [MixUp CH3 R]
                         [Lyra-8 FX Main Out] ──▶ [MixUp CH1]
```

**Setup:** Root output goes through Punch V3 CH1 (envelope shaping) and then into Moon Phase (lowpass filtering into stereo). Mix output goes to Lyra-8 FX directly for lo-fi delay processing. Both chains reach MixUp independently.

**Controls:** The Root voice receives precise envelope shaping from Punch V3 and then stereo filter treatment from Moon Phase, producing a clean, controlled version of the chord's foundation. The Mix output goes into Lyra-8 FX unprocessed, receiving lo-fi delay and self-modulation degradation as a combined texture. Blend the two chains in MixUp: the filtered root and the degraded full chord can coexist or be weighted toward either character. Adjust Moon Phase ST f to control the brightness of the root voice. Adjust Lyra-8 FX Feedback to control how much the mix texture sustains.

**Result:** The same chord simultaneously as a clean filtered foundation (Root through Punch + Moon Phase) and a lo-fi degraded texture (Mix through Lyra-8 FX), blended in MixUp for a layered harmonic sound with two distinct tonal characters.

---

## Common Mistakes

### "All four outputs sound the same."

In standard Chord mode all four voices are generated from the same wavetable at harmonically related pitches. The tonal difference between outputs is pitch, not timbre, unless each output is processed differently downstream. Patching all four into the same mixer channel at the same level produces a full chord, not four distinct sounds.

**Fix:** Route different outputs to different processing chains. A lowpass filter on the Root and a bandpass on the Seventh produces immediately audible timbral contrast between voices. The individual outputs are the starting point for differentiation, not the end point.

---

### "I changed Quality but the chord type did not change."

Quality CV works additively with the Quality knob position. If the knob is already at one extreme and CV is pushing in the same direction, there is no range left to move through. Similarly, in some modes the Quality parameter behavior changes.

**Fix:** Set the Quality knob to 12 o'clock before patching Quality CV, which leaves the full range available in both directions. Confirm the current Mode, as in Free Poly and Unison Poly modes the voice relationships change.

---

### "Melody mode is not working: the Seventh output is not responding to my Lead input."

Melody mode requires the Lead input to be patched with a CV signal. Without a signal at Lead, the Seventh voice has no pitch reference and may produce unexpected results. Also confirm the Mode LED is blue, not green or teal.

**Fix:** Confirm Mode is set to Melody (LED blue) and patch a 1V/oct CV source into the Lead input. The Triad button limits the Mix output to three voices; press it to hear the triad without the Seventh in the main mix while the Seventh runs separately.

---

### "The Mix output sounds thin compared to the individual outputs combined."

The Mix output sums all four voices at unity. If individual outputs are being amplified or driven by downstream VCAs at higher levels before reaching the mixer, the combined individual chain will be louder than the direct Mix output.

**Fix:** Use the Mix output as a reference level and match downstream processing gain accordingly. Alternatively, treat Mix and individual outputs as two separate signal paths rather than two versions of the same thing: each serves a different role in the patch.

---

## Advanced Learning Path

1. Learn the module in standard Chord mode with Quality and Voicing at fixed positions before adding any CV modulation. Understand what each of the seven chord types sounds like across several octaves of the V/Oct range. Understand what the 17 voicing stages do to the register arrangement of the same chord. These two parameters interact in ways that require familiarity before modulation makes them useful rather than random.

2. Explore the individual outputs before the Mix output becomes your default. Patch Root only into your mixer and listen to a single voice. Patch Fifth only. Patch Seventh only. Understanding what each voice contributes individually clarifies what the Mix is combining and why splitting the outputs for independent processing produces meaningfully different results.

3. Use Voicing CV as a harmonic sequencing tool. A step sequencer with four different voltage levels into Voicing CV produces a four-stage harmonic sequence from a single sustained chord: the notes stay the same but their register relationships change on each step. This is a form of harmonic rhythm that does not require changing the root pitch or the chord type.

4. Explore Melody mode with two independent sequencer tracks. Track 1 sets the chord root and controls the triad. Track 2 controls the Seventh lead voice via the Lead input. The two tracks do not need to move in lockstep. A slowly moving chord sequence on track 1 with a more active melodic line on track 2 produces a complete harmonic and melodic arrangement from a single module driven by two CV sources.

5. Treat Wave CV as a timbral envelope. A slow attack envelope from Zadar or Punch V3 ENV output patched into Wave CV causes the chord to open from a basic waveform shape into a richer, more complex timbre over the sustain of each note. This adds movement to long chord tones without requiring additional modulation of pitch or voicing.

6. Route Root and Mix to completely different effects chains and blend the results in MixUp. The Root output through a precise filter and envelope shaping becomes a clean, controlled foundation. The Mix output through Lyra-8 FX becomes a lo-fi degraded texture. Both versions of the same chord coexist in the final mix with fundamentally different characters.

7. Use Quality CV from a quantized or stepped source to create chord type sequences. A four-step sequence cycling between voltages that land on major, minor, dominant 7th, and diminished positions produces a repeating chord progression from a single fixed root pitch. Combined with Voicing CV on a different rate, the harmonic content of the patch changes on multiple timescales simultaneously.

## Pairs Well With

**Squarp Instruments Hermod+** is the natural sequencing infrastructure for Chord V2. Hermod+ provides 1V/oct pitch CV for the root, gate outputs for downstream VCAs and Punch V3 triggering, and a second CV track for the Lead input in Melody mode. The ability to run multiple CV tracks simultaneously from one sequencer makes Hermod+ the cleanest way to drive Chord V2's multi-input architecture without requiring additional modules.

**Patching Panda Punch V3** handles envelope shaping for the individual voice outputs. Each Punch V3 channel receives one voice output from Chord V2 and shapes it with an independent decay envelope. The Root output through Punch CH1 with a long Vintage decay becomes a sustaining harmonic foundation. The Seventh through Punch CH2 with a short CV-mode envelope becomes a responsive melodic edge. The two channels operate simultaneously, giving the chord's voices different dynamic characters from a single module.

**Patching Panda Moon Phase** processes individual Chord V2 voice outputs through stereo filter shaping. Routing the Seventh output through Moon Phase in LP+BP mode filters and widens the highest voice of the chord into a stereo image, while the lower voices continue through separate chains. In Melody mode, the independent Seventh voice through Moon Phase creates a stereo lead presence over a mono or differently processed triad.

**Soma Lyra-8 FX** receives Chord V2 Mix output and applies lo-fi PT2399 delay degradation to the combined chord texture. The clean wavetable chord content from Chord V2 passes through Lyra-8 FX's self-modulating delay stages and emerges with the characteristic PT2399 warmth and instability. Used alongside a clean processing chain on the Root output, Lyra-8 FX creates a parallel lo-fi version of the full chord that can be blended against the processed foundation in MixUp.
