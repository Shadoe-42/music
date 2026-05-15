# Patch Format Specification

**Status:** Active  
**Applies to:** All module guides in `/modular/`  
**Version:** 1.0, May 2026

---

## Purpose

Patch examples in module guides serve one function: teach understanding, not demonstrate feature coverage. A patch that shows every possible connection is a manual. A patch that teaches one well-chosen concept is a guide.

This specification defines the structure, visual format, and writing standards for all patch examples. It exists because play testing revealed that inconsistent formats (varied signal ordering, no reasons for connections, audio introduced before CV and gate) made patches confusing to follow at the rack.

---

## Patch Structure

Every patch follows this sequence. Sections appear in this order, no exceptions.

### 1. Framing Sentence

One sentence. States what the patch teaches, not what it does.

> "This patch demonstrates how FM depth can be used as a real-time timbral control rather than a static setting."

Not:
> "This patch uses an LFO to modulate the FM depth input."

The framing sentence tells the reader why this patch is worth building.

---

### 2. First Voice

Every patch begins by establishing a working voice before introducing the specific lesson. This section is identical in structure across all guides. It uses generic role names, not specific module names, because it describes universal infrastructure.

**Always present. Never abbreviated. Never skipped.**

```
**First Voice**

Before adding anything specific to this module, establish a working voice:

  Sequencer CV out ──[C]──▶ [Module] 1V/OCT
  Sequencer gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  [Module] audio out ──[A]──▶ VCA audio in ──▶ Mixer

You should now have a pitched, gated voice. Verify pitch tracks correctly
before proceeding. If it does not, check the 1V/OCT calibration first.
```

Signal ordering within First Voice: CV first, gate second, audio third. This matches the logical dependency chain: pitch must be established before envelope, envelope before amplitude, amplitude before the signal reaches the mix.

#### First Voice Role Adaptations

The standard First Voice assumes a VCO role: the guide's module generates audio, an external EG shapes amplitude via an external VCA. Two module roles require a different First Voice structure. Add a brief note at the top of the Patch Examples section identifying which adaptation applies; do not bury this in the individual patches.

**EVENT_VOICE modules (e.g., Plasma Voice)**

EVENT_VOICE modules contain internal amplitude control: an onboard envelope, accent circuit, or internal VCA. External EG and VCA are not needed and should not appear in First Voice.

First Voice cabling adapts per patch type within the same guide:

- Percussion patches (trigger-driven): trigger to module, module audio to Mixer.
- Melodic patches (CV and trigger-driven): sequencer CV and trigger to module, module audio to Mixer.
- LOOP mode patches (continuous audio, no external trigger): audio to module, module audio to Mixer.

**SHAPER modules (e.g., Grand Terminal, Etna)**

SHAPER modules sit between oscillator and output; they process audio rather than generate it. External EG and VCA are required because the module provides no amplitude control of its own. The signal chain runs: external oscillator → module → external VCA → Mixer.

First Voice cabling:

```
  Sequencer CV out ──[C]──▶ VCO 1V/OCT
  Sequencer gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  VCO audio out ──[A]──▶ [Module] audio in
  [Module] audio out ──[A]──▶ VCA audio in ──▶ Mixer
```

The CV-before-gate-before-audio ordering holds. The module occupies the center of the audio chain rather than the source position.

---

### 3. Core Patch Section

The body of the patch. Teaches one concept per patch. Contains:

- A header naming what is being added ("Add the FM carrier")
- A box diagram
- Reasons for each connection (one sentence per cable)
- Optional: "Move the cable" section

#### Box Diagram Format

Diagrams run left to right. Sources appear on the left, the guide's module occupies the center box, destinations appear on the right.

```
                    ┌───────────────────────────────┐
Source ──[X]──▶     │ INPUT           OUTPUT        │──[X]──▶ Destination
Source ──[X]──▶     │ INPUT                         │
                    └───────────────────────────────┘
                             Module Name
```

**Signal type notation: always on the cable line, never on the module name:**

| Symbol | Signal Type |
|--------|-------------|
| `[A]`  | Audio       |
| `[C]`  | CV          |
| `[G]`  | Gate        |
| `[T]`  | Trigger     |

**LFO speed: always noted in parentheses on the cable line:**

| Label       | Cycle Time      |
|-------------|-----------------|
| slow        | 4s or longer    |
| medium      | 0.5s – 2s       |
| fast        | under 200ms     |
| audio rate  | 20Hz or faster  |

Example: `LFO out ──[C, slow]──▶ Filter cutoff in`

**Second row:** Use a second diagram row only when two external modules route to each other (not just both connecting to the guide's module). Keep rows flat; no nesting.

**Cable limit:** 5–7 connections is the target for a clear teaching patch. 10 is the absolute ceiling. If a patch requires more than 10 cables to explain, it is two patches. Drum modules with multiple discrete voices are the documented exception: the patch selects a subset of voices and notes that remaining outputs follow the same logic.

#### Module Naming

Use a specific module from the rack, followed by one alternative in parentheses.

> "A sequencer such as Hermod+ (or Pamela's Pro Workout)"  
> "A VCA such as Ceres (or Black VCA)"

The specific name grounds the patch. The alternative teaches rack portability. One alternative only; more than one consumes space without adding proportional value.

#### Reasons Per Connection

Every cable in the diagram gets one sentence explaining why it goes there, not what it does mechanically, but why that routing serves the lesson.

> `Sequencer CV ──[C]──▶ FM IN`: Using pitch CV to control FM depth means timbre and pitch follow the same sequence, locking harmonic motion to melodic movement.

No connection appears without a reason. If you cannot write a reason for a cable, the cable should not be in the patch.

---

### "Move the Cable" Section

**Include when:** The lesson is about signal destination. Where a cable goes changes what the patch teaches.
**Skip when:** The lesson is about source quality, processing depth, or layering. Not every patch has a move.

Format:
```
**Move the cable**

Unplug [cable] from [destination A] and plug it into [destination B].

[Updated diagram showing new routing]

What changed: [one sentence on the sonic or behavioral difference]
```

---

### 4. What to Listen For

Closes every patch. Two to four sentences describing the specific sonic result the reader should hear, and one sentence on what a wrong result indicates.

> "The carrier frequency should pull the fundamental pitch while the harmonic content shifts. If the pitch is wandering uncontrollably, FM depth is too high relative to the carrier level; back off the depth knob first."

---

## Complete Example

The following is Patch 3 from the New Godspeed guide, written to this spec.

---

**External FM Carrier**

Routing an external oscillator into the FM input creates a two-operator FM voice where the frequency relationship between carrier and modulator determines the harmonic series, not just the index depth.

**First Voice**

Before introducing the modulator, establish a working voice:

```
  Sequencer CV out ──[C]──▶ New Godspeed 1V/OCT
  Sequencer gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  New Godspeed SINE/FOLD out ──[A]──▶ VCA audio in ──▶ Mixer
```

Verify pitch tracks correctly. The carrier should be producing a clean pitched tone before the modulator is introduced.

**Add the FM modulator**

```
                         ┌──────────────────────────────────────┐
Sequencer ──[C]──▶       │ 1V/OCT              SINE/FOLD OUT    │──[A]──▶ VCA ──▶ Mixer
FM source ──[A]──▶       │ FM IN                                │
LFO ──[C, medium]──▶     │ INDEX CV                             │
                         └──────────────────────────────────────┘
                                       New Godspeed
```

Use a VCO such as Endorphin.es Local Parks (or Pittsburgh Modular Furthrrrr Generator) as the FM source. Set the FM source to a harmonic interval relative to New Godspeed: an octave above, a fifth above, or in unison as a starting point.

- `FM source ──[A]──▶ FM IN`: patching into FM IN breaks the internal sine normal; the external oscillator becomes the modulator, and its frequency relationship to New Godspeed determines the harmonic content of the output.
- `LFO ──[C, medium]──▶ INDEX CV`: a medium-rate LFO on depth sweeps FM complexity over time; the FM INDEX knob now attenuates this CV rather than acting as a direct depth control.

**Move the cable**

Unplug the sequencer CV from New Godspeed 1V/OCT and plug it into the FM source's 1V/OCT instead. Leave New Godspeed at a fixed pitch set by the PITCH knob.

```
                         ┌──────────────────────────────────────┐
PITCH knob (fixed) ──    │ 1V/OCT              SINE/FOLD OUT    │──[A]──▶ VCA ──▶ Mixer
FM source ──[A]──▶       │ FM IN                                │
LFO ──[C, medium]──▶     │ INDEX CV                             │
                         └──────────────────────────────────────┘
                                       New Godspeed
                  Sequencer ──[C]──▶ FM source 1V/OCT
```

What changed: the carrier pitch is now fixed while the modulator frequency follows the sequence. Each step changes the carrier-to-modulator ratio, producing a different FM harmonic series per note rather than a different fundamental pitch. The sequence becomes a timbre sequence, not a pitch sequence.

**What to listen for**

With the FM source at a harmonic ratio and moderate INDEX, the output should have a metallic quality that shifts with LFO movement. Non-harmonic ratios between carrier and modulator produce inharmonic, clangorous tones. If the pitch is unstable or drifting, FM depth is too high; reduce INDEX attenuation before adjusting the source interval.

---

## Checklist for New Patches

Before committing a patch to a guide:

- [ ] Framing sentence names the lesson, not the mechanism
- [ ] First Voice present and complete, CV before gate before audio
- [ ] Box diagram reads left to right with no exceptions
- [ ] Signal types labeled on cable lines, not module names
- [ ] LFO speed labeled with parenthetical on the cable line
- [ ] Every cable has a one-sentence reason
- [ ] Module names use rack-specific name plus one alternative
- [ ] "Move the cable" present only if destination is the lesson
- [ ] Cable count is 10 or fewer; 5–7 in most cases
- [ ] "What to listen for" closes the patch with a wrong-result indicator

---

## Applying This Spec to Existing Guides

When rewriting patches in an existing guide:

1. Rewrite all patches in a guide at once. Mixed formats within a single guide are worse than a consistent older format.
2. Do not add patches while rewriting. Patch count stays the same unless there is a specific gap.
3. Flag guides that have been rewritten in their YAML frontmatter with `patch_format: v1` so audit tooling can track coverage.

Guides converted to v1 format (as of May 2026): New Godspeed, Plasma Voice, Grand Terminal, Etna. No rewrites currently pending.
