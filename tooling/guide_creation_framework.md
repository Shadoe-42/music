# Guide Creation Framework

**The specification for every guide in this project.**

This document defines what a completed guide is: its structure, section requirements, language rules, and quality standards. It does not preserve historical decisions or document the evolution of standards; see `tooling/archive/guide_creation_framework_archived_2026-04.md` for that record.

For triage criteria (what makes a guide Tier 1, 2, or 3), see `triage_rubric.md`.

---

## YAML Frontmatter

Every guide begins with a YAML frontmatter block. This is the machine-readable metadata that drives automated table generation, compliance auditing, and the README generator. The complete controlled vocabulary lists live in `yaml_spec_v2.md`.

### Complete Schema

```yaml
---
title: STRING                        # Full manufacturer + module name
manufacturer: STRING                 # Manufacturer name exactly as used in guides
primary_role: SEE ROLE TAXONOMY     # One value; see taxonomy below
secondary_roles: [LIST]             # Array; use [] if none
historical_context: true | false    # true if HC section is present; false if suppressed
form_factor: eurorack | desktop | keyboard-synth | rack-unit | pedal | semi-modular | software | bundle | other
functions: [LIST, 1-3 items]        # Structural capability; locked vocabulary in yaml_spec_v2.md
behavior_tags: [LIST, 3-8 items]    # Tonal/temporal/sonic character; locked vocabulary in yaml_spec_v2.md
use_cases: [LIST, 1-4 items]        # Musical intent phrases; natural language
hp: NUMBER                          # Eurorack only; omit for other form factors
memory: none | basic | full
transport: none | receive | full    # transport uses receive, not basic
screen: true | false
hybrid: true | false
cv: none | basic | full
---
```

### Role Taxonomy

One primary role per guide. Secondary roles are the additional functions the module serves when patched differently.

| Role | Definition |
|------|------------|
| `SOURCE` | Generates signal: audio, CV, gates, or noise |
| `SHAPER` | Transforms signal character: timbre, spectrum, space, texture |
| `AMPLIFIER` | Controls signal level: gain staging, mixing, dynamics |
| `MODULATOR` | Generates time-varying control signals: envelopes, LFOs, random |
| `CONTROLLER` | Defines timing, sequencing, and performance structure |
| `ROUTER` | Distributes, combines, switches, or applies logic to signal paths |
| `ANALYZER` | Observes, measures, and displays signal behavior |
| `EVENT_VOICE` | Trigger-dependent sound engine with internally managed amplitude envelope |
| `UTILITY` | Multi-function, hybrid, or cross-category modules |

**EVENT_VOICE boundary rule:** Remove the external VCA. If the sound shape breaks, the module is SOURCE. If it still produces a complete shaped note event, it is EVENT_VOICE.

### Key Field Rules

`secondary_roles` is always an array, even if empty: `[]`.

`functions` describes structural capability: what the module physically does. 1-3 items from locked vocabulary. Not sound character, not use case. "filter" is a function; "warm" is not.

`behavior_tags` describes tonal, temporal, and sonic character. 3-8 items. Answers "what does this sound or behave like?" Use these to distinguish a warm analog filter from an aggressive digital one even though both carry `functions: [filter]`.

`use_cases` is natural musical intent language. 1-4 phrases. "harmonic pad", "clock subdivision", "send/return effects loop". These power intent-based lookup so someone searching for "ambient texture" finds modules tagged accordingly without knowing the category.

`transport` uses its own three-value vocabulary: `none | receive | full`. This is distinct from `memory` and `cv`, which use `none | basic | full`. Do not use `basic` for transport.

Capability flags (`memory`, `transport`, `screen`, `hybrid`, `cv`) are omitted only for form factors where they are structurally irrelevant (passive modules, blank panels). For eurorack modules, all flags are required.

`historical_context: false` suppresses the HC section and the audit warning for it. Use only when the module genuinely has no meaningful lineage. It is not a shortcut to avoid research.

---

## Canonical Section Order

The following nine anchor sections appear in every guide, in this sequence. Intervening non-anchor content (reference tables, output glossaries, architecture overviews) is permitted between anchors but does not replace them.

1. **Historical Context** (or YAML flag if suppressed)
2. **Quick Start**
3. **Key Specifications**
4. **Essential Parameters**
5. **Why This Instrument Excels**
6. **Patches** (4 patches)
7. **Common Mistakes**
8. **Advanced Learning Path**
9. **Pairs Well With**

Architectural complexity adds sections between anchors. It does not remove anchors.

---

## Section Requirements

### Historical Context

**YAML:** Set `historical_context: true`. If the module has no meaningful lineage, set `historical_context: false` and omit the section.

**Format:** 3-4 prose paragraphs. No sub-headings inside the section.

**Research standard:** Name the lineage. Name specific people, specific years, specific instruments that came before. Do not write vague sentences about "pioneering work in generative synthesis." A reader should finish the HC section knowing exactly where the module comes from and whose thinking shaped it.

**When to suppress:** Contemporary designs with no meaningful lineage — modules built on modern DSP platforms without historical antecedents, new utility designs with no prior art. If the module is a clone, revival, or derivative of an influential instrument, it has HC. If it is a wholly original contemporary tool, it likely does not. Err toward research.

---

### Quick Start

**Format:** Brief module overview (2-3 sentences), followed by a numbered step sequence to first sound or first useful patch. Steps should be completable in under 10 minutes.

The Quick Start is not a tutorial. It is an orientation: get the reader to a state where the module is doing something audible or useful, so the rest of the guide has a foundation to build from.

---

### Key Specifications

**Format:** Dedicated section with a `| Spec | Value |` table. Not buried inside Quick Start.

**Required rows:**

| Spec | Value |
|------|-------|
| Width | [X] HP |
| Depth | [X] mm |
| Power | [X] mA +12V / [X] mA -12V / [X] mA +5V |

Always show all three power rails even if one is 0 mA. Width in HP, depth in mm, no exceptions.

**Unverified specification flags:** Append ⚠️ after any Depth or Power value that has not been verified against hardware or an official manufacturer source. See the Unverified Specification Flags section below for full rules.

---

### Essential Parameters

**Format:** One paragraph per major parameter or parameter group. Include CV destinations for each parameter where applicable.

The goal is to teach what each control actually does in musical terms, not to restate the front-panel label. "RATE controls the speed of the LFOs" is not useful. "RATE sets the cycle time of all eight outputs simultaneously, spanning several minutes of slow drift to audio-rate modulation; a CV input at RATE shifts the entire bank up or down together" is useful.

---

### Why This Instrument Excels

**Format:** Exactly 4 prose paragraphs. No sub-headings inside the section.

Each paragraph addresses a different dimension of the module's distinction. Not marketing language. This section argues for what the module does that others cannot or do differently. A reader finishing this section should understand not just what the module does but why it occupies a position in the rack that another module cannot easily replace.

---

### Patches

**Count:** 4 patches per guide.

**Progression logic:**

Patch 1 is basic and intentional. Single voice or single destination. Establishes fundamental operation. A reader with no prior experience of the module can complete it in under 10 minutes.

Patch 2 introduces a key secondary feature or parameter. Builds directly on Patch 1. First encounter with the module's characteristic behavior beyond its most obvious function.

Patch 3 pushes toward edge or feedback behavior. The module's unusual or extreme capabilities. May introduce external CV modulating the module itself.

Patch 4 is integrative. Brings in other modules from the rack. Shows the module as part of a larger system rather than in isolation.

**Each patch includes:**

- ASCII signal flow diagram using signal coding: `[A]` = Audio, `[C]` = CV, `[G]` = Gate
- **Setup:** what to connect before turning anything on
- **Controls:** what to adjust once the patch is running
- **Result:** what the patch produces and why it matters

---

### Common Mistakes

**Count:** 4-6 mistakes. Not fewer than 4; not more than 6 unless a seventh mistake genuinely exists and teaches something that the others do not.

**Format per mistake:**

```
### "[The complaint written as the user would voice it]"

[Prose explanation of why it happens.]

[Explicit fix.]
```

The heading is always the complaint in the user's own words, in quotes, as an H3. No sub-headings inside the explanation. The fix is direct: what to do, not what to consider doing.

---

### Advanced Learning Path

**Format:** Numbered prose list. 6-8 steps. No sub-headings, no bullet points inside the steps.

The ALP is a progression from intermediate competency toward mastery. Step 1 should be reachable by someone who has worked through all four patches. Step 8 should require either deep module knowledge or integration with several other modules. The steps are not a list of features; they are a trajectory.

---

### Pairs Well With

**Format:** Bold module name as paragraph opener, one paragraph per pairing. No sub-headings, no bullet lists. 4-6 pairings.

Include the manufacturer name on first reference for each module. Subsequent mentions within the same paragraph may use the module name alone.

Each pairing explains specifically why the two modules work well together and what musical result emerges from the combination. Generic statements ("adds modulation possibilities") do not meet the standard.

---

## Language Rules

### Em Dashes

Em dashes are prohibited in all guide prose. The em dash has become a reliable signal of AI-generated text. Regardless of grammatical correctness, the perception problem undermines the credibility of this work.

Alternatives, by context:

- **Colon** for introducing an explanation, definition, or list: "RATE governs the entire bank simultaneously: all eight outputs shift together."
- **Semicolon** for two closely related independent clauses: "Velocity defaults to full when nothing is patched; insert a cable to enable dynamic control."
- **Parentheses** for asides and clarifications: "The decay control (labeled TAIL on the panel) affects only the noise component."
- **Comma** for mild parentheticals where the thought flows naturally.
- **Sentence restructure** when none of the above feel right. Two shorter sentences are almost always cleaner than one long one held together with an em dash.

### Contractions

Contractions are prohibited. Write "do not" not "don't". Write "it is" not "it's". Write "cannot" not "can't". This applies to all drafted content in guides, section headings, and inline prose.

### Manufacturer Naming

Use full manufacturer name plus module name on first reference within each section. Subsequent references within the same section may use the module name alone.

Correct: "Make Noise Wogglebug", "Mutable Instruments Marbles", "DivKid Ochd"  
Incorrect: "Wogglebug", "Marbles", "Ochd" (on first reference within a section)

This applies to all module references in the guide, including alternatives mentioned in patches and Pairs Well With pairings.

### Circuit-Based Descriptions

No AI or intelligence references in guide prose. The modules are circuits. Describe what they do in terms of signal behavior, not cognition. "The algorithm selects" is acceptable. "The module decides" or "the module thinks" is not.

No "Phase 2" terminology anywhere. Use "advanced" where a stage descriptor is needed.

---

## Unverified Specification Flags

**Purpose:** Mark specs in the Key Specifications table that have not been verified against hardware or an official source, so readers know the difference between confirmed and unconfirmed values.

**Trigger:** Any Depth or Power value that comes from an unconfirmed source (memory, third-party listing, guide carried forward without verification). Width (HP) is generally reliable from multiple sources and does not require flagging.

**Format:** Append ⚠️ after the value in the table cell:

```
| Depth | 25 mm ⚠️ |
| Power | 120 mA +12V ⚠️ / 5 mA -12V ⚠️ / 0 mA +5V |
```

**Clearance:** Remove the flag only after personal hardware verification or confirmation against the official manufacturer manual or Modular Grid. Document the verification source in the commit message.

**Do not clear flags by inference or cross-referencing other guides.** Hardware verification or official source only.

---

## Compliance

Run `python3 tooling/audit_guides.py` from the Music directory to verify YAML compliance. All controlled vocabulary fields must use only the defined terms from `yaml_spec_v2.md`.

The audit script checks YAML field presence and vocabulary validity. It does not check prose quality, section content, or patch count. Structural compliance is a necessary condition for a guide to be considered complete; it is not sufficient.

---

*Cross-reference: `triage_rubric.md` for tier definitions and repair criteria. `yaml_spec_v2.md` for complete controlled vocabulary.*
