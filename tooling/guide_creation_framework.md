# Guide Creation Framework

**Essential requirements for systematic guide creation**

---

## **Integration with Project Philosophy**

This framework implements the interconnectedness principle from `project_philosophy.md` - teaching how modules connect within systems, not just isolated features.

**For philosophical foundation:** See `project_philosophy.md` for WHY systematic documentation matters (generational teaching, ~500 instruments, interconnection principle).

**For operational discipline:** See `framework_overview.md` for WHY systematic standards maintain system integrity (teaching obligation, mise en place, consequence model).

**For applying these standards:** See `guide_enhancement_pattern.md` for systematic enhancement approach (transforming guides from procedural to understanding-focused).

**For visual presentation:** See `visual_communication_standards.md` for diagram and image integration standards.

**For verification:** See `quality_system.md` and `verification_strategy.md` for ensuring accuracy and reliability.

---

## **Module Classifications & Requirements**

### **Utility Modules (2-3 Patches):**
- **What:** Signal routing, level control, interface modules (Mixers, VCAs, Clocks)
- **Structure:** Basic → Advanced (→ Expert for complex utilities)
- **Focus:** Technical operation, system integration

### **Creative Modules (4-5 Patches):**
- **What:** Sound generation, musical control modules (Oscillators, Filters, Effects, Drums)
- **Structure:** Basic → Intermediate → Advanced → Expert
- **Focus:** Musical exploration, sound design, performance

### **Multi-Function Modules (4-5 Patches):**
- **What:** Platform modules with 10+ modes (Disting mk4, MetaModule, Hermod+)
- **Structure:** Basic → Intermediate → Advanced → Expert
- **Focus:** Demonstrate functional breadth with practical guidance

### **Complete Synthesizers (4-5 Patches):**
- **What:** Self-contained instruments (Desktop synths, keyboard synths, grooveboxes)
- **Structure:** Basic → Intermediate → Advanced → Expert
- **Focus:** Studio integration, performance techniques, sound design mastery

### **Studio Equipment (3-4 Patches):**
- **What:** Recording/production gear (Interfaces, processors, controllers)
- **Structure:** Basic → Intermediate → Advanced (→ Expert for complex gear)
- **Focus:** Workflow integration, professional techniques

**Classification Decision:** Primary function + creative potential + parameter complexity

---

## **Synthesizer-Specific Framework Enhancements**

### **Content Structure for Complete Synthesizers**

**Required Sections (Adapted from Modular Standards):**
1. **Quick Start** - First sound in 5 minutes with preset recommendation
2. **Essential Parameters** - Core synthesis sections with signal flow diagram
3. **What This Unlocks From Your Existing Gear** - Studio/performance integration focus
4. **Patch Examples** - 4-5 programming tutorials with similar synthesizer alternatives
5. **Advanced Techniques** - Instrument-specific features (modulation matrix, alternative tunings, etc.)
6. **Common Use Cases** - Studio, live, sound design, learning applications
7. **Historical Context** - When educationally valuable (vintage reissues, influential designs)
8. **Troubleshooting** - Synthesizer-specific issues (calibration, MIDI, performance)
9. **Pairs Well With** - Studio gear, controllers, processing equipment

### **Synthesizer Alternative Format**

**Enhanced Format for Complete Synthesizers:**
```
**Main Example:** Take 5 hard sync lead technique
**Similar Synthesizer Options:**
- **Budget:** Behringer DeepMind 6, Korg Minilogue XD
- **Different character:** Moog Subsequent 37 (Moog filter), Novation Peak (digital algorithms)
- **Premium:** Sequential Prophet Rev2, Moog One
```

**Selection Criteria:**
- **Budget tier:** Under $800, accessible alternatives with similar capabilities
- **Different character:** Different synthesis approach (analog vs digital, different filter types)
- **Premium tier:** $1500+, flagship instruments with enhanced features

### **Studio Integration Focus**

**"What This Unlocks" for Synthesizers:**
- **MIDI Controllers:** Transform basic controllers into professional workstations
- **Audio Interfaces:** Add analog character to digital workflows
- **Expression Pedals:** Real-time performance control and filter sweeps
- **Hardware Sequencers:** Clock sync and bidirectional MIDI communication
- **Studio Effects:** External processing integration and auxiliary sends
- **Performance Setups:** Transform practice into professional performance rigs

### **Synthesizer-Specific Visual Standards**

**Internal Signal Flow Diagrams:**
```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

┌─OSCILLATORS─┐    ┌─FILTER──┐    ┌─AMPLIFIER─┐    ┌─EFFECTS─┐
│ OSC 1    ○──┼────┼─▶Cutoff │    │          │    │         │
│ OSC 2    ○──┼────┼─ Reso   ├────┼─▶VCA ○───┼────┼─▶Out ○──┼──[A]
│ Sub/Noise○──┼────┼─ Drive  │    │     ↑    │    │  ↑  ↑   │
└─────────────┘    └─────────┘    └─────┼────┘    └──┼──┼───┘
                                        │            │  │
                   ┌─MODULATION─────────┼────────────┘  │
                   │ LFO/ENV ○──────────┘               │
                   │ Mod Matrix ○───────────────────────┘ [C]
                   └─────────────────────────────────────────┘
```

**Performance Control Integration:**
```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

┌─PERFORMANCE CONTROLS─┐    ┌─SYNTHESIZER─┐
│ Mod Wheel     ∼──────┼────┼─▶LFO Amount │  ∼ = Real-time control [C]
│ Aftertouch    ∼──────┼────┼─▶Filter Cut │  
│ Expression    ∼──────┼────┼─▶Reverb Mix │  Performance expression [C]
│ Sustain Pedal ∼──────┼────┼─▶Arp Hold   │
└──────────────────────┘    └─────────────┘
```

### **Synthesizer Programming Techniques**

**Essential Programming Skills:**
- **Two-oscillator fundamentals:** Detuning, sync, FM techniques
- **Filter envelope shaping:** Attack/decay/sustain/release relationships
- **Modulation matrix usage:** Advanced routing beyond front-panel controls
- **Performance integration:** Real-time expression techniques
- **Studio workflow:** MIDI integration, recording techniques

**Advanced Synthesizer Features:**
- **Alternative tunings:** Microtonal and historical temperaments
- **Unison/chord memory:** Monophonic stacking and chord triggering
- **Multi-timbral programming:** When applicable to specific instruments
- **External processing integration:** Auxiliary sends, effects loops

### **Educational Progression for Synthesizers**

**Basic Level:** Single-oscillator patches, basic filter sweeps, preset exploration
**Intermediate Level:** Multi-oscillator programming, envelope coordination, effects integration
**Advanced Level:** Modulation matrix, performance techniques, alternative tunings
**Expert Level:** Complex sound design, studio integration, advanced performance techniques

---

## **YAML Frontmatter**

Every guide begins with a YAML frontmatter block. This is the machine-readable metadata that drives automated table generation, compliance auditing, and the README generator. The complete vocabulary lists live in `tooling/yaml_spec_v2.md`.

### **Complete Schema**

```yaml
---
title: STRING                        # Full manufacturer + module name
manufacturer: STRING                 # Manufacturer name exactly as used in guides
primary_role: SEE ROLE TAXONOMY     # One value; see taxonomy below
secondary_roles: [LIST]             # Array; use [] if none
form_factor: eurorack | desktop | keyboard-synth | rack-unit | pedal | semi-modular | software | bundle | other
functions: [LIST, 1-3 items]        # Structural capability; locked vocabulary in yaml_spec_v2.md
behavior_tags: [LIST, 3-8 items]    # Tonal/temporal/sonic character; locked vocabulary in yaml_spec_v2.md
use_cases: [LIST, 1-4 items]        # Musical intent phrases; natural language
hp: NUMBER                          # Eurorack only; omit for other form factors
memory: none | basic | full
transport: none | receive | full    # Note: transport uses receive, not basic
screen: true | false
hybrid: true | false
cv: none | basic | full
---
```

### **Role Taxonomy**

One primary role per guide. Secondary roles are the additional functions the module serves when patched differently.

| Role | Definition |
|------|------------|
| `SOURCE` | Generates signal — audio, CV, gates, or noise |
| `SHAPER` | Transforms signal character — timbre, spectrum, space, texture |
| `AMPLIFIER` | Controls signal level — gain staging, mixing, dynamics |
| `MODULATOR` | Generates time-varying control signals — envelopes, LFOs, random |
| `CONTROLLER` | Defines timing, sequencing, and performance structure |
| `ROUTER` | Distributes, combines, switches, or applies logic to signal paths |
| `ANALYZER` | Observes, measures, and displays signal behavior |
| `EVENT_VOICE` | Trigger-dependent sound engine with internally managed amplitude envelope |
| `UTILITY` | Multi-function, hybrid, or cross-category modules |

**EVENT_VOICE boundary rule:** Remove the external VCA. If the sound shape breaks, the module is SOURCE. If it still produces a complete shaped note event, it is EVENT_VOICE.

### **Key Field Rules**

`secondary_roles` is always an array, even if empty: `[]`.

`functions` describes structural capability — what the module physically does. 1-3 items from the locked vocabulary. Not sound character; not use case. "filter" is a function. "warm" is not.

`behavior_tags` describes tonal, temporal, and sonic character. 3-8 items. Answers "what does this sound or behave like?" Use these to distinguish a warm analog filter from an aggressive digital one even though both have `functions: [filter]`.

`use_cases` is natural musical intent language. 1-4 phrases. "harmonic pad", "clock subdivision", "send/return effects loop". These power intent-based lookup: someone searching for "ambient texture" finds modules tagged accordingly without knowing the category.

`transport` uses its own three-value vocabulary: `none | receive | full`. This is distinct from `memory` and `cv`, which use `none | basic | full`. Do not use `basic` for transport.

Capability flags (`memory`, `transport`, `screen`, `hybrid`, `cv`) are omitted only for form factors where they are structurally irrelevant (a passive module, a blank panel). For eurorack modules, all flags are required.

### **Example**

```yaml
---
title: Mutable Instruments Rings
manufacturer: Mutable Instruments
primary_role: SOURCE
secondary_roles: [SHAPER]
form_factor: eurorack
functions: [resonator, physical-model]
behavior_tags: [harmonic, sustained, metallic, evolving, performance-oriented]
use_cases: [harmonic pad, evolving ambient texture, chord voice, drone foundation]
hp: 14
memory: none
transport: none
screen: false
hybrid: false
cv: full
---
```

### **Compliance**

Every guide must have complete YAML frontmatter. Run `python3 tooling/audit_guides.py` from the Music directory to verify. All controlled vocabulary fields must use only the defined terms from `yaml_spec_v2.md`. The audit script checks every field and reports violations as errors or warnings.

---

## **Content Structure & Quality**

### **Required Sections:**
1. **Quick Start** - 5-minute success path
2. **Essential Parameters** - Core controls with CV information
3. **Patch Examples** - Count per module classification above
4. **Common Use Cases** - Real-world applications
5. **Troubleshooting** - Common issues
6. **Pairs Well With** - Integration suggestions with alternatives
7. **What This Unlocks From Your Existing Gear** (Optional but Strongly Encouraged) - Include when module creates genuine new possibilities with commonly-owned equipment

### **Official Section Ordering (Updated 2025-11-18)**

**Authoritative sequence for all guides:**

1. **Quick Start** - First sound in 5 minutes, builds confidence immediately
2. **Essential Parameters** - Learn the controls before understanding philosophy
3. **Historical Context** - Ground understanding in module's place in synthesis/music history (when educationally valuable)
4. **Algorithm Reference / Key Specifications** - Provide reference material for the sections that follow (where applicable)
5. **Why This Instrument Excels** - Set philosophical and architectural context before practical application
6. **Patch Examples** - Apply learning through hands-on patches; guides encounter common mistakes here
7. **Common Mistakes & Pattern Recognition** - Supportive troubleshooting after practice; reveals synthesis principles through problems encountered
8. **Pairs Well With** - Show integration possibilities after user has hands-on experience
9. **Advanced Learning Path** - Growth trajectory after mastery of basics

**Rationale for this ordering:**

- **Sections 1-4 (Foundation):** Build technical competency and historical context before abstract philosophy
- **Section 5 (Philosophy):** Inspire with design understanding after establishing foundation
- **Sections 6-7 (Application & Learning):** Patches come first so users encounter mistakes naturally; troubleshooting becomes supportive, not cautionary
- **Sections 8-9 (Integration & Growth):** Advanced content after core mastery

**Why this sequence matters:**
- Quick Start builds immediate success (user confidence)
- Essential Parameters + Historical Context establish competency (user understanding)
- Why This Excels sets vision (user inspiration) AFTER understanding controls
- Patches let user discover real-world problems (user experience)
- Common Mistakes provides supportive guidance AFTER user has tried (user learning)
- Advanced content comes last (user growth trajectory)

**Pattern Discovery Note:** This ordering emerged from Erica Synths Pico DRUM2 enhancement (November 2025), where placing Common Mistakes before Patch Examples created tonal dissonance (excitement → caution), while moving it after patches created natural flow (vision → practice → learning from experience → growth). This sequence now applies to all guides.

### **Non-Negotiable Anchor Sections**

The following sections must appear in every guide regardless of module complexity. Technical depth increases the content between anchors; it never removes the anchors themselves.

A guide that documents every jack and parameter on a complex module but omits these sections is a reference manual, not a teaching guide. The pedagogical obligation requires all six anchors.

**Required anchors, in sequence:**

1. **Key Specifications** -- near the top, within Quick Start or Quick Reference
2. **Why This Instrument Excels** -- immediately before Patch Examples
3. **Patch Examples**
4. **Common Mistakes** (4-5 core mistakes) -- immediately after Patch Examples
5. **Pairs Well With**
6. **Advanced Learning Path**

**"Why This Excels" must precede patches.** Placing it after patches (as seen in some older guides) inverts the pedagogical sequence. The correct order is: orient the user toward the instrument's design intent, then have them practice. Not the other way around.

**On "Quick Start" vs. "Quick Reference":** A 5-minute first-sound Quick Start works well for simple and single-voice modules. Complex multi-voice instruments (multi-voice drum synthesizers, multi-output clocks) may substitute a "Quick Reference" table instead. Both serve the same orienting function. Key Specifications must appear in whichever format is used.

**Architectural complexity adds sections between anchors. It does not remove anchors.** Clock modules need a Navigation Model section. Multi-voice drums need Architecture Overview and per-voice parameters. Euclidean sequencers need algorithm tables and interface documentation. All of this interior content belongs between Key Specifications and "Why This Excels." The anchors before and after that interior are fixed.

---

### **Key Specifications Placement (Critical for Evaluation)**

**Location:** Within Quick Start section, immediately after "What is [Module]?" description, before "Your First [Experience]"

**Mandatory Format:**
```
**Key Specifications:**

| Spec | Value |
|------|-------|
| Width | [X] HP |
| Depth | [X] mm |
| Power | [X] mA +12V / [X] mA -12V / [X] mA +5V |
```

**Why This Placement:**
- Users read: Concept → Evaluate if fits system → Try it
- Specs are decision-making information, not learning material
- Before "Your First [Experience]" because users need to know fit before investing time
- Natural evaluation flow: "Is this for me?" (specs) → "Can I use it?" (first patch)

**Mandatory for all module guides:** No exceptions. Hardware constraints are deal-breakers.

**Format Rules:**
- **Width:** Always in HP (eurorack standard)
- **Depth:** Always in mm (case compatibility check)
- **Power:** Always show all three rails (+12V, -12V, +5V) even if one is 0 mA
- **Accuracy:** Verify against official documentation or Modular Grid

**Additional Module-Specific Details (Optional):**
If applicable, add module-specific technical specs:
- **Oscillators:** Frequency range, waveforms, modulation types
- **Filters:** Filter type, slope, frequency range
- **Sequencers:** Steps, tracks, clock options
- **Effects:** Sample rate, algorithm count, I/O types

**Example (Pico DRUM2):**
```
**Key Specifications:**

| Spec | Value |
|------|-------|
| Width | 3 HP |
| Depth | 35 mm |
| Power | 28 mA +12V / 5 mA -12V / 0 mA +5V |
```

**Compliance Requirement:** Every guide must include Key Specifications in Quick Start. This is non-negotiable; users cannot evaluate module fit without this information.

### **"Existing Gear Integration" Section Guidelines:
**Include this section when:**
- Module genuinely opens up integration possibilities with common existing gear
- There are specific, practical examples that would excite users about new workflows
- The connections aren't already obvious from the patch examples
- The integration actually enhances the module's utility (not random gear mentions)

**Examples of good fits:**
- Interface modules (Stomp, audio interfaces, MIDI converters) - unlock pedals, studio gear, controllers
- Utility modules with unique capabilities - clock dividers (unlock drum machines), sample & holds (unlock field recorders)
- Modules that bridge different signal types - envelope followers (unlock dynamic mics, instruments)

**Skip this section when:**
- Module function is self-contained (basic VCAs, simple LFOs)
- Integration possibilities are already covered in patch examples
- Would require forced content rather than genuine discovery

**Quality test:** Does this section make someone think "I never realized I could do that with equipment I already have!" If not, skip it.

### **Mandatory Framework Compliance Requirements:**
**Based on systematic testing findings (2025-09-22) - these gaps appeared in 100% of tested guides**

1. **GitHub Image Integration (MANDATORY):**
   - **Format:** `![Module Name](https://github.com/Shadoe-42/music/raw/main/modular/images/[module_name]/front_panel.jpg)`
   - **Caption:** Descriptive text about module interface and key elements
   - **Placement:** Immediately after title + tagline, before all content sections (provides immediate visual context)
   - **Non-negotiable:** Every guide must include proper GitHub image integration

2. **Enhanced Format Alternatives (MANDATORY - ALL PATCHES):**
   - **Required for EVERY patch:** Budget/Different character/Premium options with specific module names
   - **Cannot be skipped:** Testing revealed systematic omission when not explicitly required
   - **See Patch Section Palette** for full format, additional optional blocks, and sequencing rules

### **Quality Requirements:**
- **Interface accuracy** - Verify jack names against `comprehensive_interface_database.md`
- **No fabricated terminology** - Use actual module language
- **Educational progression** - Clear learning objectives
- **Module-specific language** - Honor manufacturer philosophy

---

## **Enhanced Format Standards**

### **Implementation Examples:**

**Modular Module Guide:**
```
**Main Example:** Maths Ch1 → filter cutoff (complex modulation)
**Alternative Options:**
- **Budget:** 2HP LFO, Doepfer A-143-3
- **Different character:** Batumi geometric patterns, Ochd organic breathing  
- **Premium:** Intellijel Quadrax complex envelopes
```

**Complete Synthesizer Guide:**
```
**Main Example:** Take 5 hard sync lead technique
**Similar Synthesizer Options:**
- **Budget:** Arturia MicroBrute, Korg MS-20 Mini
- **Different character:** Moog Matriarch (Moog sync), Novation Peak (digital sync)
- **Premium:** Sequential Prophet Rev2, Moog One
```

**Studio Equipment Guide:**
```
**Main Example:** Focusrite Scarlett 2i2 direct recording setup
**Alternative Options:**
- **Budget:** Behringer U-Phoria UM2, PreSonus AudioBox USB 96
- **Different character:** MOTU M2 (enhanced monitoring), Zoom PodTrak P4 (podcast focus)
- **Premium:** Universal Audio Apollo Twin, RME Babyface Pro FS
```

### **Visual Standards:**
- **Signal coding:** [A]=Audio  [C]=CV  [G]=Gate
- **ASCII symbols:** ○ = output, ◀ = input, ── = audio, ║ = CV
- **Module boxes:** Standard format (see `visual_communication_standards.md` for details)
- **GitHub images:** `![Module](https://github.com/Shadoe-42/music/raw/main/modular/images/[module]/front_panel.jpg)`

---

## **Patch Section Palette**

Each patch in a guide is built from a core structure (diagram, Setup, Controls, Result) plus optional blocks drawn from this palette. The palette exists because the guides document a modular ecosystem — the documentation itself should reflect that compositional flexibility. Use what serves the patch. Omit what does not. Never force a block to fill space.

### **Core Structure (required in every patch)**

- **ASCII signal flow diagram** — shows the actual patch connections
- **Setup** — what to connect before turning anything on
- **Controls** — what to adjust once running
- **Result** — what the patch produces and why it matters

### **Palette Blocks (use when they serve the patch)**

---

**Enhanced Alternatives** *(use in every patch — the only palette block that is effectively mandatory)*

Provides three concrete substitution options at different price/character points so the patch is not locked to one exact module configuration.

```
**Enhanced Alternatives:**
- **Budget:** [specific module] — [one-line rationale]
- **Different character:** [specific module] — [one-line rationale]
- **Premium:** [specific module] — [one-line rationale]
```

Use manufacturer + module name for every entry. Do not write generic descriptions ("any VCA") when a specific module name exists.

---

**Learning Objectives** *(use when the patch teaches a transferable principle)*

States what the musician learns from this specific patch — not what the module does, but what understanding they walk away with. Best when the principle applies beyond this module.

```
**Learning Objectives:**
- [Principle 1 — one sentence, written as a takeaway, not a feature description]
- [Principle 2]
- [Principle 3]
```

Two to four items. If there is nothing genuinely transferable, omit the block rather than generating placeholder content.

---

**Experimentation Ideas** *(use when the patch has natural room to grow)*

Numbered list of variations and extensions the musician can try from this starting point. Encourages divergence without scripting the outcome.

```
**Experimentation Ideas:**
1. [Variation or extension — starts with an action verb, one to two sentences]
2. ...
```

Three to five items. Framed as invitations, not instructions. If the patch is already at the edge of the module's range, omit rather than inventing artificial extensions.

---

### **Sequencing Within a Patch**

When multiple palette blocks appear in the same patch, maintain this order:

1. Core structure (diagram + Setup/Controls/Result)
2. Enhanced Alternatives
3. Learning Objectives
4. Experimentation Ideas

---

## **Language & Terminology Standards**

### **Punctuation Standards**

**Em dashes are prohibited in guide prose.**

The em dash has become a reliable signal of AI-generated text in the eyes of readers and critics. Regardless of grammatical correctness, the perception problem is real and undermines the credibility of this work. Avoid em dashes entirely. Use the following alternatives based on context:

- **Colon** when introducing an explanation, definition, or list: "THRUST shapes the noise color: CCW favors white noise, CW favors metallic."
- **Semicolon** when connecting two closely related independent clauses: "Velocity defaults to full when nothing is patched; insert a cable to enable dynamic control."
- **Parentheses** for asides and clarifications: "The decay control (labeled TAIL on the panel) affects only the noise component."
- **Comma** for mild parentheticals or light pauses where the thought flows naturally.
- **Sentence restructure** when none of the above feel right. Breaking one long sentence into two shorter ones is almost always the better solution anyway.

**Rationale:** These guides are intended as training data and human-readable references. The moment a reader flags the prose as artificial, the teaching fails. Clean punctuation serves the long-term mission.

**Audit requirement:** All existing guides should be reviewed and updated to remove em dashes. New guides must be written without them from the start.

---

### **Required Language:**
- **Circuit-based descriptions** - No AI/intelligence references
- **"Advanced"** not "Phase 2" throughout all guides
- **Exact manufacturer terminology** - Honor module-specific language
- **Manufacturer + Module naming** - Always use "Manufacturer Module" format for consistency and searchability

**Module Naming Standards:**
- ✅ **Correct:** "Intellijel Stomp", "4ms Listen IO", "Make Noise Maths", "Erica Synths Pico Voice"
- ❌ **Incorrect:** "Stomp", "Listen IO", "Maths", "Pico Voice" (manufacturer missing)
- **Rationale:** Searchability (users look under manufacturer sections), clarity (multiple manufacturers may have similar names), framework consistency

**Naming Guidelines:**
- **First reference:** Always include full manufacturer name
- **Cross-references:** Always use full manufacturer + module name for guide linking
- **Alternative suggestions:** Include manufacturer names in module alternatives

### **Progression Terminology:**
- **Patches:** Basic → Intermediate → Advanced → Expert
- **Integration:** "Advanced synergies" for multi-module coordination
- **System Design:** "Advanced integration" for complex networks

---

## **Historical Context (When Appropriate)**

### **Include Historical Context For:**
- **Historical significance** - Major synthesis milestones
- **Technical innovation** - Techniques that influenced the field
- **Cultural impact** - Widely adopted, influenced genres
- **Educational value** - Helps understand module importance

### **Examples:** Korg MS-20, Make Noise Maths, classic Moog modules, Buchla designs

### **Treatment:**
- **Factual information** about development/impact
- **2-3 paragraphs maximum**
- **Integrated into existing sections** not separate section
- **Educational focus** - module's place in synthesis history

### **When There Is No Historical Context**

Some modules are wholly original contemporary designs with no meaningful lineage — not clones, not revivals, not derivatives of influential instruments. Forcing a Historical Context section onto these produces filler that dishonors the standard.

For these guides, add `historical_context: false` to the YAML frontmatter. This records the decision explicitly in the file and suppresses the audit warning. Use it only when the module genuinely has nothing to say — not as a shortcut to skip research.

**Examples of modules with no meaningful historical context:** Contemporary DSP modules built on modern platforms (Daisy, etc.), new utility designs without lineage, purpose-built contemporary tools.

---

## **Workflow Integration**

### **Mandatory Process:**
1. **Complete workflow checklist** from `workflow_checklist.md` before ANY guide work
2. **Show checklist to user** and get explicit approval
3. **Follow efficiency standards:** 1-2 function calls maximum for most operations

### **Never:**
- Bypass workflow checklist
- Start operations without user approval  
- Exceed promised function call count
- Skip accountability documentation

---

## **Framework Application**

### **For New Guides:**
1. Determine module classification and write complete YAML frontmatter (all v2 fields)
2. Complete workflow checklist
3. Single comprehensive write with mandatory compliance elements
4. **Verify framework compliance** using systematic testing criteria
5. Document results

### **For Guide Updates:**
1. Read entire existing guide
2. Complete workflow checklist for specific changes
3. **Check for systematic gaps** (GitHub image + enhanced format alternatives)
4. Targeted edits for small changes OR comprehensive compliance update
5. Record efficiency

### **Framework Compliance Verification (Enhanced 2025-09-22):**
**Comprehensive verification checklist - systematic testing revealed tunnel vision failures when verification was incomplete**

**Mandatory Checklist (ALL Requirements):**
- [ ] **YAML frontmatter complete** — all v2 fields present with valid vocabulary values; verify with `python3 tooling/audit_guides.py`
- [ ] **GitHub image integration present** with proper URL format and descriptive caption
- [ ] **Enhanced format alternatives in ALL patches** (budget/premium/different character)
- [ ] **Terminology consistency** - "Advanced" not "Phase 2" throughout entire guide
- [ ] **Required sections complete** per module classification (Quick Start, Essential Parameters, etc.)
- [ ] **Interface accuracy verified** against official manuals
- [ ] **Language standards applied** - circuit-based descriptions, exact manufacturer terminology
- [ ] **Visual standards compliance** - signal coding, ASCII symbols, module boxes
- [ ] **Historical context appropriateness** - included when educationally valuable, properly integrated
- [ ] **Cross-references functional** - links to other guides work correctly
- [ ] **Educational progression clear** - learning objectives and skill development milestones

**Testing Evidence & Tunnel Vision Prevention:**
- **Instruo Arbhar guide:** Missing image + enhanced alternatives + terminology violations
- **Instruo Cs-L guide:** Missing image + enhanced alternatives + terminology violations  
- **Pattern:** Tunnel vision on specific gaps missed comprehensive framework verification
- **Solution:** Complete checklist prevents partial compliance claims
- **Critical understanding:** "Framework compliance" means ALL requirements, not just targeted fixes

### **Emergency Protocols:**
- **File operation failure:** Stop immediately, diagnose, ask for guidance
- **Efficiency targets missed:** Document actual performance, analyze causes
- **Quality issues:** Address using quality system protocols
- **Framework compliance gaps:** Use systematic testing criteria to identify and resolve

---

## **Pattern Refinement Notes (November 2025)**

### **Discovery: 4-5 Core Common Mistakes Standard**

**Session:** Erica Synths Pico DRUM2 enhancement

**Finding:** The original framework requirement of "8-12 common mistakes" was too rigid. Testing revealed:
- **Utility modules** rarely have 8-12 legitimate beginner issues (forcing to count requires edge cases)
- **Creative modules** better served by 4-5 core mistakes that teach foundational principles
- **Quality principle:** Four deeply explained mistakes teaching synthesis principles beats twelve padded issues
- **Teaching obligation:** Stretching to hit numbers dishonors the interconnection principle

**Decision:** Minimum 4-5 core common mistakes (not 8-12). Additional issues only if they genuinely exist and teach something new.

**Application:** This standard now applies to all guide enhancements going forward. Pico DRUM2 serves as reference implementation with 4 core mistakes that explain 90% of beginner problems.

### **Discovery: Official Section Ordering**

**Session:** Erica Synths Pico DRUM2 enhancement

**Finding:** Without prescribed section order, guides varied structurally, and content placement affected pedagogical flow. Specific problem:
- Placing "Common Mistakes" immediately after "Why This Excels" created tonal dissonance (excitement → caution)
- Moving "Common Mistakes" after "Patch Examples" created natural pedagogical flow (inspire → practice → learn from experience)

**Decision:** Adopted authoritative section ordering (documented above) that sequences content by learning stage: foundation → philosophy → application → learning → integration → growth.

**Impact:** This ordering aligns with user experience lifecycle and teaching obligation principle (guides become pedagogically sound, not just reference materials).

**Application:** All new guides and significant enhancements must follow this section ordering. Existing guides should be updated when feasible.

### **Cross-Documen Implications**

These refinements affect:
- `guide_creation_workflow.md` - Update section ordering references
- `guide_enhancement_pattern.md` - Update mistake count expectations
- All future guide enhancements - Follow 4-5 mistake standard and prescribed section ordering

---

**This framework provides essential requirements for systematic guide creation while integrating with established accountability systems.**

---

*Integrates with: `workflow_checklist.md`, `quality_system.md`, `visual_communication_standards.md`, `comprehensive_interface_database.md`*