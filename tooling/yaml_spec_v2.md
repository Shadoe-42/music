# YAML Frontmatter Specification v2

**Status:** LOCKED v1 — all vocabularies defined. Expand use_cases seed list per domain as new gear categories are documented.  
**Supersedes:** v1 schema (title, manufacturer, primary_role, secondary_roles, hp only)  
**Migration:** Batch update of all existing guides required after spec is fully locked

---

## Purpose

This document defines the complete YAML frontmatter schema for all guides in this corpus.
The schema serves two purposes: human readability within guide files, and machine-readable
metadata for automated table generation, cross-domain search, and compliance auditing.

All fields with locked vocabularies must use only the defined terms. No free-form values
in controlled vocabulary fields. Consistency across the corpus is the entire point.

---

## Complete Schema

```yaml
---
title: STRING
manufacturer: STRING
primary_role: SEE ROLES
secondary_roles: [LIST]
form_factor: SEE FORM FACTORS
functions: [LIST, 1-3 items, locked vocabulary]
behavior_tags: [LIST, 3-8 items, locked vocabulary]
use_cases: [LIST, 1-4 items, intent language]
hp: NUMBER
memory: none | basic | full
transport: none | receive | full
screen: true | false
hybrid: true | false
cv: none | basic | full
---
```

**Field rules:**
- `secondary_roles` is always an array, even if empty: `[]`
- `hp` is omitted for non-modular form factors
- `memory`, `transport`, `screen`, `hybrid` are omitted only for form factors where
  they are structurally irrelevant (e.g., a blank panel, a speaker cabinet)
- `behavior_tags` and `use_cases` are required once the vocabulary is locked and
  migration is complete

---

## Primary Role Taxonomy

One primary role per guide. The role describes what the module fundamentally does
to signal in the majority of use cases.

| Role | Definition |
|------|------------|
| `SOURCE` | Generates signal: audio, CV, gates, or noise |
| `SHAPER` | Transforms signal character: timbre, spectrum, space, texture |
| `AMPLIFIER` | Controls signal level: gain staging, mixing, dynamics |
| `MODULATOR` | Generates time-varying control signals: envelopes, LFOs, random |
| `CONTROLLER` | Defines timing, sequencing, and performance structure |
| `ROUTER` | Distributes, combines, switches, or applies logic to signal paths |
| `ANALYZER` | Observes, measures, and displays signal behavior |
| `UTILITY` | Multi-function, hybrid, or cross-category modules |
| `EVENT_VOICE` | Trigger-dependent sound engine with internally managed amplitude envelope |

**EVENT_VOICE boundary rule:** A module qualifies as EVENT_VOICE when its amplitude
envelope is internally managed in response to a gate or trigger input and the user
does not need an external VCA to shape the note event. Test: if removing the external
VCA breaks the sound shape, it is SOURCE. If the module produces a discrete shaped
event without one, it is EVENT_VOICE.

---

## Form Factor

One value per guide. Describes the physical format of the instrument or device.

```
eurorack
semi-modular
standalone
pedal
rack
guitar
bass
amplifier
cabinet
monitor
headphones
blank-panel
```

**Notes:**
- `blank-panel` guides carry no functions, behavior_tags, or use_cases
- `cabinet` refers to guitar and bass speaker enclosures
- `monitor` refers to studio reference monitors and PA speakers
- `amplifier` refers to guitar, bass, and studio amplifier heads and combos

---

## Capability Flags

Five typed boolean or graduated fields describing system-level capabilities.
These scale across all form factors.

| Field | Values | Meaning |
|-------|--------|---------|
| `memory` | `none` / `basic` / `full` | Preset or patch storage capability |
| `transport` | `none` / `receive` / `full` | MIDI or clock send/receive capability |
| `screen` | `true` / `false` | Has a visual display |
| `hybrid` | `true` / `false` | Combines fundamentally different signal architectures (analog + digital, sampler + sequencer, valve + digital power stage) |
| `cv` | `none` / `basic` / `full` | CV integration capability: none = no CV, basic = pitch and gate only, full = CV over multiple parameters |

**Notes:**
- For Eurorack modules `cv: full` is the default and may be omitted if desired
- `cv: basic` covers synths with 1V/oct and gate inputs only
- `cv: none` covers most guitar pedals, passive devices, and standalone gear without CV jacks

---

## Functions Vocabulary

What the device physically does, independent of musical role.
Assign 1-3 items per guide. Use only terms from this list.

### Sources

| Term | Covers |
|------|--------|
| `oscillator` | Analog VCO, DCO |
| `complex-oscillator` | Oscillator with internal waveshaping or FM (analog or digital macro-oscillator) |
| `fm-oscillator` | Oscillator where FM or phase modulation is the primary synthesis architecture |
| `noise-source` | Noise and random signal generation |
| `drum-voice` | Single percussive synthesis engine |
| `sample-player` | Plays back recorded audio samples |
| `granular` | Granular synthesis or granular processing |
| `physical-model` | Physical modeling synthesis (Karplus-Strong, modal, etc.) |
| `string-instrument` | Guitar, bass, acoustic instrument |

### Shaping

| Term | Covers |
|------|--------|
| `filter` | Voltage-controlled filter, any topology (LP, BP, HP, notch, comb) |
| `wavefolder` | Harmonic folding and related waveshaping |
| `distortion` | Overdrive, fuzz, saturation, hard clipping |
| `resonator` | Resonant body or string simulation used as processor |
| `eq` | Frequency shaping without resonance as primary character |
| `dynamics` | Compressor, limiter, gate, expander |
| `fx-time` | Reverb, delay, echo |
| `fx-modulation` | Chorus, flanger, phaser, tremolo (as effect) |
| `fx-pitch` | Pitch shifter, harmonizer, vocoder |
| `fx-spectral` | Bitcrusher, sample rate reduction, spectral processing |

### Modulation

| Term | Covers |
|------|--------|
| `envelope-generator` | ADSR, AR, or similar discrete envelope |
| `lfo` | Low frequency oscillator |
| `function-generator` | Multi-mode device serving as envelope, LFO, slew, and related functions (Maths, Zadar, Stages) |
| `sample-hold` | Sample and hold circuit |
| `random-source` | Random or stochastic CV generation |
| `slew-limiter` | Portamento, lag processor, glide |
| `quantizer` | Pitch or CV quantization to scales or intervals |

### Sequencing and Timing

| Term | Covers |
|------|--------|
| `sequencer` | Step sequencer, melodic or rhythmic |
| `clock-source` | Master clock generation |
| `clock-divider` | Clock division |
| `clock-multiplier` | Clock multiplication |
| `euclidean-generator` | Euclidean or Bjorklund rhythm pattern generation |

### Routing and Utility

| Term | Covers |
|------|--------|
| `vca` | Voltage-controlled amplification |
| `mixer` | Signal summing |
| `attenuator` | Signal scaling, attenuation, attenuversion |
| `mult` | Signal splitting and distribution (buffered or passive) |
| `switch-router` | In-patch audio or CV signal switching (mutes, selectors, patch bays within a system) |
| `signal-router` | System-level signal routing infrastructure (MIDI routers, studio patch bays) |
| `logic-processor` | Boolean logic operations (AND, OR, XOR, etc.) |
| `cv-processor` | CV mathematics: scaling, offsetting, mixing, inverting control voltages |

### System

| Term | Covers |
|------|--------|
| `preamp` | Signal amplification before power stage |
| `power-amp` | Power amplification stage |
| `audio-interface` | Analog to digital and digital to analog conversion |
| `oscilloscope` | Visual signal display and measurement |
| `tuner` | Pitch display and measurement |
| `power-distribution` | Power conditioners, PDUs, power supplies, power strips |
| `transducer` | Converts electrical signal to physical air movement (monitors, headphones, speaker cabinets, PA speakers) |
| `microphone` | Converts acoustic energy to electrical signal (dynamic, condenser, ribbon, pickup) |

---

## behavior_tags Vocabulary

**Status:** Locked v1 — may be tuned as the corpus grows, but no additions without review.

A list of 3-8 tags per guide describing how the device sounds and behaves.
Use only terms from this list. Choose the most accurate and discriminating tags;
do not apply every tag that could technically fit.

### Stability

| Tag | Meaning |
|-----|---------|
| `stable` | Consistent, repeatable, same result every time |
| `unstable` | Prone to drift, variation, or tuning wander |
| `chaotic` | Sensitive to initial conditions, complex nonlinear behavior |

### Temporal Character

| Tag | Meaning |
|-----|---------|
| `percussive` | Attack-based, rhythmically oriented, short decay |
| `sustained` | Holds well, designed for long notes or drones |
| `evolving` | Naturally changes over time when left running |
| `static` | Does not change unless explicitly modulated |
| `free-running` | Operates continuously without external trigger |
| `gated` | Requires gate or trigger to produce output |

### Sonic Character

| Tag | Meaning |
|-----|---------|
| `clean` | Transparent, low distortion, accurate |
| `dirty` | Colored, adds harmonic saturation, character |
| `warm` | Analog roundness, soft transients |
| `harsh` | Aggressive, potentially fatiguing, sharp |
| `dark` | Frequency balance tilted low, filtered |
| `bright` | High frequency presence, open, extended |
| `metallic` | Bell-like, inharmonic overtones, ring character |
| `noisy` | Noise content is an intentional feature |
| `harmonic` | Overtone-rich, musically consonant partials |
| `inharmonic` | Overtones outside the harmonic series |

### Control Character

| Tag | Meaning |
|-----|---------|
| `linear` | Proportional, predictable response to control |
| `nonlinear` | Exponential, stepwise, or feedback-dependent response |
| `sensitive` | Small input changes produce large output changes |
| `reactive` | Fast tracking, responds quickly to CV or gate changes |
| `performance-oriented` | Rewards real-time hands-on interaction |

### Behavioral Flags

| Tag | Meaning |
|-----|---------|
| `self-modulating` | Designed or suited for feedback into itself |
| `generative` | Produces evolving output without continuous input |
| `stochastic` | Probability or randomness is a core design feature |

---

## use_cases Format and Seed List

**Status:** Format locked. Seed list covers modular corpus. Expand by domain as new
gear categories are documented.

**Format rules:**
- 1-4 items per guide
- 3-7 words each
- Intent language: what the musician is trying to achieve, not what the device does
- Written from the musician's perspective, not the technical spec
- Freeform within these rules — use seed phrases directly or write new ones that follow
  the same pattern

**How to apply:** Ask "what would a musician reach for this to do?" not "what can it do?"

---

### Seed List — Modular

**Voice and Tone**
```
lead voice
bass voice
drone foundation
harmonic pad
sub bass layer
chord voice
percussive voice
```

**Texture and Atmosphere**
```
evolving ambient texture
noise layer
granular texture bed
sustained pad
dark atmospheric layer
```

**Rhythmic**
```
rhythmic percussion layer
euclidean rhythm source
polyrhythmic pattern generator
clock source for full system
clock division utility
```

**Modulation and Control**
```
modulation source
random CV generator
stochastic modulation
gate and trigger source
pitch CV source
envelope shaping
```

**Generative and Experimental**
```
generative melodic sequence
self-evolving patch element
probability-based variation
chaotic texture source
feedback loop component
```

**Processing and Utility**
```
timbral movement and shaping
waveshaping and distortion
stereo signal processing
CV scaling and utility
audio mixing and routing
signal distribution
```

---

*Seed lists for other domains (pedals, standalone synths, rack gear, amplifiers, etc.)
to be added when documentation of those categories begins.*

---

## Blank Panel Rule

Blank panels carry `form_factor: blank-panel` and `hp: NUMBER` only. No functions,
behavior_tags, use_cases, or capability flags. They have no signal function.

---

## Migration Notes

- All 68 existing guides require updating from v1 to v2 schema
- Audit script (`tooling/audit_guides.py`) must be updated to validate v2 fields
  before any guide migration begins
- Update audit script first, migrate all guides in one batch, no partial states
- New guides written after migration use v2 schema from the start

---

*Last updated: 2026-04-15*
