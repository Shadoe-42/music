# Current Work Roadmap

**Last Updated:** November 21, 2025
**Status:** Active planning phase
**Mission:** Educate for generations. Anyone with an interest should be able to use guides independently.

---

## Phase 1: Tooling Cleanup & Clarification

**Priority:** High | **Timeline:** Next 2-4 weeks | **Status:** IN PROGRESS

### Core Framework (Keep - In Active Use)
- [x] `guide_creation_framework.md` - Retain, up to date
- [x] `guide_enhancement_pattern.md` - Retain, proven through Mordax Data
- [x] `workflow_checklist.md` - Retain, essential operational discipline
- [x] `onboarding.md` - Retain, user-facing for Future Claude
- [x] `project_philosophy.md` - Retain, explains the WHY behind everything
- [x] `session_continuity_guide.md` - Retain, important for cross-session understanding
- [x] `verification_strategy.md` - Retain, useful in waves for major updates (SCHEDULED FOR REWRITE)

### Historical/Maintenance (Archived)
- [x] `accountability_tracking.md` - Archived (was effective during process refinement, no longer needed)
- [x] `failure_patterns.md` - Archived (learnings should be baked into guides, not separated)
- [x] `efficiency_tracker.md` - Archived (token tracking, specific to session management)
- [x] `quality_system.md` - Archived (internalized by creator, uncertain Future Claude need)
- [x] All `myths_*.md` files (8 files) - Archived (gear myths, can revisit post-Perfect Circuit feedback)
- [x] `ms20_common_mistakes_section.md` - Archived (MS-20 guide is fine where it is in update cycle)
- [x] `ms20_mini_completion_checklist.md` - Archived (MS-20 guide is fine where it is in update cycle)
- [x] `music_theory_framework.md` - Archived (stays available, not deleted)

### Action Items (Consolidation & Improvement)
- [ ] `visual_communication_standards.md` - CONSOLIDATE into `guide_creation_framework.md` or `guide_enhancement_pattern.md` (verify which is proper home) - file stays active for now, consolidation is future task

**Outcome:** Archive directory created. 12 files moved to archive with full git history preserved. Core framework remains clean and focused. Consolidation actions flagged for future phases.

---

## Phase 2: Guide Compliance Audit

**Priority:** High | **Timeline:** 4-6 hours of focused work

### Create Audit Spreadsheet
Column structure:
- Module name
- Framework compliance (✅ / 🟡 / ❌)
- Completeness (✅ / 🟡 / ❌)
- Real-world tested (Y/N + feedback notes)
- Next action (none / cosmetic / Phase A / Phase B / Phase C)

### Tier 1: Framework Compliance Check (Quick Scan)
- [ ] Official section ordering present? (Quick Start → Essential → Philosophy → Patches → Mistakes → Pairs Well With → Advanced Path)
- [ ] Key Specifications included?
- [ ] Common Mistakes: proper structure (misunderstanding → why → solution → learning moment)?
- [ ] Interconnection teaching present (WHY, not just WHAT)?

### Tier 2: Completeness Check (Medium Effort)
- [ ] All required patches present for module classification?
- [ ] Enhanced alternatives in all patches?
- [ ] Technical accuracy verified (voltage ranges, specs, jack names flagged where uncertain)?
- [ ] Learning objectives explicit?
- [ ] WHY explanations throughout?

### Tier 3: Real-World Use (Feedback Integration)
- [ ] Which guides have been tested by external users?
- [ ] What feedback did they give?
- [ ] Are common user questions addressed?
- [ ] Document: guide name → feedback received → changes made

**Outcome:** Clear visibility into which guides are ready, which need work, which have validation

---

## Phase 3: Feedback Documentation System

**Priority:** Medium | **Timeline:** Set up framework during audit, populate ongoing

### Create Feedback Registry
- [ ] Add to appropriate guide or central tracking: User feedback log
- [ ] Format: Date | Guide Name | Feedback Type | What User Found Confusing | Change Made
- [ ] Link this to commit messages (when feedback drives a change, reference the feedback)

### Document Perfect Circuit Feedback
- [ ] After holiday conversation: Capture what they say
- [ ] Mark which guides they tested
- [ ] Note specific criticisms/suggestions
- [ ] Prioritize changes based on their expertise
- [ ] Document what changed and why

**Outcome:** Visible feedback loop showing how real users shape guide improvement

---

## Phase 4: Ongoing Execution (After Cleanup & Audit)

**Priority:** Continuous

### Maintenance Cadence
- [ ] Weekly: Review feedback from forum distributions + external users
- [ ] Bi-weekly: Enhance 2-3 guides per cycle (following enhancement pattern)
- [ ] Monthly: Check framework compliance against completed work
- [ ] Quarterly: Audit progress, update roadmap

### Content Prioritization (Current Strategy)
- Current approach: Alphabetical + completion percentage
- Keep guides at 75% completion (MetaModule and other complex modules get sustained work)
- As guides reach Phase B completion, move to maintenance mode

### Theory & Problem-Solving Directories
- [ ] Keep in planning stage (not core to mission, but valuable context)
- [ ] These are "work in progress" by design
- [ ] Don't force completion; let them evolve with user need

---

## Phase 4.5: Active Guide Development

**Started:** 24 Dec 2025
**Mission:** Fill teaching gaps identified through inventory-to-guides analysis. Foundational concepts first, then module-specific guides in priority order.

### Foundational Guides (Priority: HIGH)
- [ ] **Signal Types & Mult Selection Guide**
  - Teaching objective: Decision matrix for choosing mult type (passive vs. buffered) based on signal type, cable distance, and destination count
  - Scope: Establish interconnection thinking about infrastructure choices
  - Status: Planned
  - Why: Beginners conflate all mults as generic splitters; this teaches the decision tree that makes infrastructure choices coherent
  - Difficulty: Easy to moderate (no complex synthesis theory, high conceptual clarity)

### Module Guides (Priority Ranked)

**Tier 1: Core Drum Voice Teaching (HIGH IMPACT)**
- [ ] **Endorphin.es Queen of Pentacles** (909-inspired analog drum)
  - Why: Ground Control guide exists but teaching lacks the drum voice itself. Core analog drum philosophy.
  - Difficulty: Moderate (comprehensive but self-contained)
  
- [ ] **Endorphin.es BLCK_Noir** (CR-78 inspired digital drum)
  - Why: Teaches analog vs. digital drum philosophy as direct comparison with Queen of Pentacles
  - Difficulty: Moderate (digital concepts add complexity but teaching value high)

**Tier 2: Sequencing Evolution (MODERATE IMPACT, HIGH EASE)**
- [ ] **AtoVproject lx-euclid** (Euclidian sequencer)
  - Why: Euclidian Circles guide exists; lx-euclid teaches dedicated drum sequencing progression
  - Difficulty: Easy to moderate (builds on existing Euclidian teaching)
  - Teaching pair: Euclidian Circles v2 + lx-euclid show sequencing specialization

**Tier 3: Filter Design Comparison (MODERATE IMPACT)**
- [ ] **Xaoc Belgrad** (state variable multimode filter)
  - Why: System has Wasp, Forbidden Planet, Moon Phase; Belgrad completes filter design comparison teaching
  - Difficulty: Moderate (builds on filter theory but introduces state variable architecture)
  
- [ ] **Patching Panda Etna** (morphing filter)
  - Why: Flagged for system expansion; morphing design is unique teaching moment
  - Difficulty: Moderate to challenging (morphing mechanics need clear explanation)

**Tier 4: Foundational Concepts (LOWER IMPACT BUT CLEAN)**
- [ ] **Erica Synths Pico Quant** (microtonal quantizer)
  - Why: Beginners need scale/tuning concept; natural teaching moment after pitch sequencing
  - Difficulty: Easy to moderate (self-contained, clear application)

---

## Batch 1: Infrastructure & Self-Contained Modules

**Priority:** HIGH | **Scope Definition:** VCAs/Mixers + Clock/Timing modules
**Rationale:** Self-contained teaching scope, infrastructure roles clear, easier to explain than complex synthesis modules
**Started:** 24 Dec 2025

### VCAs & Mixers (5 modules - alphabetical order)

- [ ] **After Later Audio - Cloaks** ← STARTING POINT
  - Classification: VCA
  - Type: Mutable Instruments Veils 2020 replica
  - Teaching scope: Linear VCA with routing
  - Why: Commonly found, clear VCA teaching moment
  
- [ ] **After Later Audio - Mingles**
  - Classification: VCA
  - Type: Dual 3 Channel Mixer/VC Autopanner
  - Teaching scope: Mixer + panning combo
  - Why: Introduces autopanning as CV modulation concept
  
- [ ] **Doepfer - A-130-2**
  - Classification: VCA
  - Type: Dual linear/exponential VCA (Slim Line Series)
  - Teaching scope: Linear vs. exponential VCA behavior
  - Why: Slim format infrastructure; dual function comparison
  
- [ ] **Frap Tools - 411**
  - Classification: VCA
  - Type: Quadruple Linear VCA for Audio and CV
  - Teaching scope: Quad linear amplification; infrastructure role
  - Why: Contrasts with Black Quad VCA2; different design philosophy
  
- [ ] **Vostok Instruments - Ceres**
  - Classification: VCA
  - Type: Linear VCA and Mixer
  - Teaching scope: Simple linear VCA foundation + mixing
  - Why: Minimal VCA clarity; infrastructure teaching

### Clock/Timing (4 modules - alphabetical order)

- [ ] **4ms Company - RCD Breakout**
  - Classification: Clock
  - Type: Breakout module for Rotating Clock Divider
  - Teaching scope: RCD functionality expansion
  - Why: Ecosystem teaching; expands division possibilities
  
- [ ] **4ms Company - Rotating Clock Divider V2**
  - Classification: Clock
  - Type: Divides clock input with rotation concept
  - Teaching scope: Clock division + creative rotation
  - Why: Clock manipulation fundamental; rotation adds creative dimension beyond division
  
- [ ] **4ms Company - Shuffling Clock Multiplier Plus**
  - Classification: Clock
  - Type: Clock Multiplication & Breakout
  - Teaching scope: Clock multiplication + rhythm shuffling
  - Why: Rhythm variation teaching through clock manipulation
  
- [ ] **ALM Busy Circuits - Pamela's Pro Workout**
  - Classification: Clock
  - Type: Clock Modulator
  - Teaching scope: Advanced clock control with modulation
  - Why: Extended clock possibilities; different approach from simple dividers

**Note:** Turing Machine ecosystem (Pulses, Volts, Turing Machine LPG Expander) covered in existing `turing_machine_ecosystem_guide.md`

---

## Framework Issues: Active

### Signal Type Emoji: Portability Conflict

**Identified:** April 2026
**Priority:** HIGH; affects every guide in the project

The visual_communication_standards.md uses emoji color coding (🔴 Audio, 🔵 CV, 🟡 Gate) as the core signal differentiation system. This directly conflicts with the project's stated portability and durability principle. Emoji rendering depends on unicode support in the viewing environment. A file opened in a terminal, plain text editor, or future system without proper unicode rendering will display question marks or boxes instead of colored circles. The framework's own opening states diagrams must work in 2075; emoji-dependent diagrams do not meet that standard.

**Resolution:** Replace emoji legend and inline emoji with plain text signal type labels.

**New standard:**
```
Signal types: [A]=Audio  [C]=CV  [G]=Gate
```

Inline on diagram connections:
```
OSC OUT ---[A]---> Filter IN
ENV OUT ---[C]---> Filter CV
Seq OUT ---[G]---> VCA Gate
```

**Scope:** visual_communication_standards.md requires update. All existing guides require systematic audit and correction. New guides (starting with Cloaks) use the new standard.

**Status:** visual_communication_standards.md updated April 2026. Cloaks guide written to new standard. Existing guide audit is a future phase.

---

## Known Constraints & Context

**Module Guide Inventory:**
- 56 total module guides
- ~75% updated to current standards
- ~25-30% actively used by external users with integrated feedback
- MetaModule and similar complex modules require extensive sustained testing (on roadmap, not blocking)

**Current Distribution:**
- GitHub-hosted, easy to access and maintain
- Organic forum distribution (users link to specific guides when answering questions)
- No monetization plan
- No central website (not needed, mission is "independent use")

**Validation In Progress:**
- 25-30% guides with real external user feedback
- Perfect Circuit testing/feedback incoming (post-holiday)
- Feedback source documentation needs formalization (not yet captured systematically)

**Core Mission:**
- Educate for generations
- Anyone with an interest should be able to use independently
- Knowledge should survive without creator maintenance
- Interconnection teaching (not just procedures)

---

## Notes & Decisions

**Gear Myths Document:**
- Keep if: Serves educational mission (corrects misconceptions about synthesis principles)
- Cut if: Just opinion/editorializing without pedagogical value
- Decision: Revisit after review

**Theory Documentation:**
- Started as personal learning (music theory not creator's strength)
- Now available for anyone who needs it
- Not required for any guides (standalone context)
- Will continue to evolve, no forced completion needed

**Process Discipline:**
- Granular commits are strategic (token management, preventing session overwrites)
- Not excessive; this is smart operational practice
- Continue as-is

---

## Last Review

**Date:** November 21, 2025
**Reviewer:** Shadoe + Claude collaboration session
**Key Insight:** Project is further along than "problem diagnosis" suggests. Real validation happening, appropriate timeline, clear mission alignment. Cleanup is refinement, not crisis response.

**Next Review:** After Perfect Circuit feedback (post-holiday)

---

## Teaching Rack: Separate System

**Updated:** April 2026

The following modules have guides but do NOT appear in the main rack CSV (mg_data_sheet_rack3069924.csv). These are installed in a dedicated teaching rack and their guides serve that specific educational purpose. Do NOT flag as orphaned.

- Noise Engineering Ruina Versio
- Qu-Bit Bloom v1
- Tiptop Audio Forbidden Planet
- Intellijel Stomp
- Cre8audio Function Junction
- Erica Synths Pico LFO/SH
- Erica Synths Pico Voice

---

## Module Gap Analysis: Main Rack

**Updated:** April 2026
**Source:** Modular Grid export mg_data_sheet_rack3069924.csv (February 2026, ~95% accurate)
**Total modules in main rack:** 125
**Guides existing:** ~58 (including teaching rack guides above)
**Guides needed:** ~60+ modules

### Expanders: Covered by Parent Guides (No Separate Guide Needed)
- Instruō arbhar USB Expander; covered by arbhar guide
- Instruō arbhar expander; covered by arbhar guide
- Winterbloom Castor & Pollux II expander; covered by C&P II guide
- Xaoc Devices Nin; covered by Zadar guide (when created)
- Xaoc Devices Poti II; covered by Batumi II guide (when created)
- 4ms RCD Breakout v1.1; covered by RCD V2 guide
- 4ms MetaModule Wi-Fi Expander; covered by MetaModule guide
- 4ms MetaAIO; covered by MetaModule guide
- 4ms MetaButtons; covered by MetaModule guide
- Music Thing Modular Volts; covered by Turing Machine ecosystem guide
- Music Thing Modular Pulses Mk II; covered by Turing Machine ecosystem guide
- WORNG Electronics Turing Machine LPG Expander; covered by Turing Machine ecosystem guide
- Xaoc Devices Zadar Nin expander; covered by Zadar guide (when created)

### Blank Panels & Passive Utilities (No Guide Needed)
- Other/unknown Attenuate! Blank Panel 6HP
- Other/unknown MentalNoise (x2)
- 2hp Mult (x3)
- Intellijel Buff Mult
- Intellijel Mult

### Guides Needed: Prioritized

**Tier 1: High Impact / Complex Modules**
- Endorphin.es Queen of Pentacles: 909-inspired analog drum voice
- Endorphin.es Blck_Noir: CR-78 inspired digital drum voice
- Endorphin.es Furthrrrr Generator; dual oscillator, complex voice
- Endorphin.es Grand Terminal; complex filter/effects
- Endorphin.es NEW GODSPEED: (assess scope)
- Endorphin.es Cockpit 2; performance mixer/controller
- Xaoc Devices Belgrad; state variable multimode filter
- Xaoc Devices Batumi II; quad LFO (include Poti II expander)
- Xaoc Devices Zadar; complex envelope generator (include Nin expander)
- Noise Engineering Basimilus Iteritas Alter; percussion oscillator
- Noise Engineering Manis Iteritas Alia; distorted voice
- Noise Engineering Pons Asinorum: (assess scope)
- Befaco Oneiroi; complex oscillator/effects
- Gamechanger Audio PLASMA Voice; ionized gas oscillator
- Qu-Bit Aurora; reverb/spectral processor
- Qu-Bit Prism; multiband processor
- Qu-Bit Mojave; granular oscillator
- Qu-Bit Stardust; sample player
- Qu-Bit Nautilus; delay/looper
- Qu-Bit Chord v2; polyphonic oscillator
- Instruō Selam; complex oscillator (Tesseract Modular)
- dsp.coffee YYS: (assess scope)
- dsp.coffee 22 Deaf Chinchillas: (assess scope)
- Schlappi Engineering 100 Grit; distortion/waveshaper
- Steady State Fate SSG Stereo Field; stereo processor
- Patching Panda ETNA; morphing filter

**Tier 2: Moderate Impact**
- After Later Audio Cloaks: Veils clone, VCA
- After Later Audio Mingles; dual mixer/autopanner
- After Later Audio Scenes: (assess scope)
- After Later Audio Bartender V2: (assess scope)
- After Later Audio Light Rail: (assess scope)
- Frap Tools 411; quad linear VCA
- Frap Tools 333; mixer/utility
- Vostok Instruments Ceres; linear VCA/mixer
- AtoVproject lx-euclid: Euclidean sequencer
- ALM Busy Circuits Pamela's PRO Workout; clock modulator
- Erica Synths Black Joystick2; performance controller
- Erica Synths Pico Quant; quantizer
- Bela Gliss: (assess scope)
- Tesseract Modular Radioactive: (assess scope)
- Altered State Machines Eris: (assess scope)
- CalSynth uO_C; utility/multi-function
- Blue Lantern Subharmonic Generator: (assess scope)

**Tier 3: Smaller Scope**
- 4ms Percussion Interface + Expander
- Pittsburgh Modular The Toad; filter
- 2hp LFO v2
- 2hp Verb
- 2hp Swarm
- Qu-Bit Lunar Orbiter: (assess scope)
- Error Instruments Eraserhead Theremin: (assess scope)

---

## Last Review

**Date:** November 21, 2025
**Reviewer:** Shadoe + Claude collaboration session
**Key Insight:** Project is further along than "problem diagnosis" suggests. Real validation happening, appropriate timeline, clear mission alignment. Cleanup is refinement, not crisis response.

**Next Review:** After Perfect Circuit feedback (post-holiday)

---

*This roadmap documents current priorities and decisions. Update as phases complete or priorities shift.*
