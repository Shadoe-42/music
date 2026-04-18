# Guide Triage Rubric

**Purpose:** Consistent criteria for grading existing guides against current standards. Used during the generational triage pass to assign every flagged guide a tier and identify required work before repair or rebuild sessions begin.

**Established:** 2026-04-17

---

## Required Anchor Sections

Every guide must contain the following sections in this order:

1. Quick Start
2. Why This Instrument Excels
3. Historical Context (or `historical_context: false` in YAML frontmatter)
4. Essential Parameters
5. Patches
6. Common Mistakes
7. Advanced Learning Path
8. Pairs Well With

**Present:** Heading exists and contains substantive content.
**In position:** Appears in the sequence above relative to other anchor sections. Intervening non-anchor content is acceptable.

---

## Tier 1 — Surface Fixes (Batchable)

All of the following are true:
- All 8 anchor sections present and in correct order
- Patch content is functional and not dominated by "Phase 2 ecosystem" framing
- Why Excels content is substantive, not generic marketing language
- ALP is a numbered progression (may have sub-sections, but the core numbered path is present and usable)

Issues present are cosmetic only, drawn from this list:
- "Beginner's Guide" in title, or " - Guide" suffix
- "The Big 6" in Essential Parameters heading
- "Beginner Patch Ideas" or equivalent old patch section naming
- "Beginner Gotchas & Pro Tips" heading (with or without emoji)
- "Why [Full Manufacturer + Module Name] Excels" instead of "Why This Instrument Excels"
- "Bottom Line:" closing paragraph
- Emoji in any heading
- Key Specs in bullet format instead of `| Spec | Value |` table
- Contractions throughout

Tier 1 guides are fixed programmatically via batch scripts with light human review. No content needs to be written or rewritten.

---

## Tier 2 — Structural Cleanup (One Dedicated Session)

One or more of the following is true, and the guide does not meet Tier 3 criteria:
- One or two anchor sections missing or significantly out of position
- Patch content is functional but wrapped in "Phase 2 ecosystem" framing that needs stripping — the underlying patch is valid, the language around it is not. "Phase 2 framing" in one patch only is Tier 1; pervasive framing across multiple patches is Tier 2.
- Why Excels has sub-sections (### headers inside it) but content is accurate and salvageable with editing
- ALP is structured as a study progression with sub-sections ("Cross-Module Learning Opportunities", "Skill Development Milestones") but the core numbered path is present and usable
- Pairs Well With has sub-headers ("Phase 1 Integration", "Advanced Synergies", etc.) but the module pairings themselves are accurate
- Common Mistakes or Pairs Well With missing, but all other anchor sections are sound

Tier 2 guides need a human pass: strip framing, consolidate sub-sections, add missing sections. Core content does not need to be rewritten from scratch.

---

## Tier 3 — Full Rebuild (Dedicated Session)

Any one of the following is true:
- "Phase 2 ecosystem" framing is pervasive throughout patches, Why Excels, and ALP — not just present in places but the organizing logic of the whole guide
- Patch tables contain "Advanced Synergy", "Advanced Concept", "Phase 2 Integration", "Phase 2 Synergy", "Algorithmic Synergy", "Mathematical Synergy", or "Organic Result" columns that reframe patches in terms of the old ecosystem model
- ALP has no usable numbered progression — it is entirely sub-sections with no recoverable numbered path
- Why Excels is generic marketing language with no substantive content about the module's technical or historical significance
- Patch numbering is broken (duplicates, gaps, misnumbering)
- Multiple anchor sections missing

Tier 3 guides are faster to rebuild from scratch than to repair. Before rebuilding, review existing content for salvageable material (a solid Quick Start, a well-written ALP, accurate Essential Parameters) and carry it forward.

**Confirmed Tier 3 (pre-triage):** Mob of Emus, Rings, Plaits, Pressure Points.

**Final triage count (2026-04-17):** 27 Tier 3, 34 Tier 2, 3 Tier 1, 4 Clean. Full list in `tooling/guide_triage_2026.md`.

---

## Edge Cases

**Good content, one missing anchor section:** Tier 2, not Tier 1. Missing sections require writing, not reformatting.

**"Phase 2 framing" isolated to one patch, otherwise clean:** Tier 1. Flag the patch for manual review; treat the rest of the guide as batchable.

**Confirmed Tier 3 guides:** Do not re-triage. Mark as confirmed and proceed to rebuild scheduling.

---

## Output Format

Each triaged guide is recorded in `tooling/guide_triage_2026.md` with:
- Guide filename
- Tier (1, 2, or 3)
- Specific issues detected
- Anchor sections missing or out of position (if any)
- Notes on salvageable content (Tier 3 only)
- HC status (needed / written / historical_context: false)

---

*Applied during triage pass beginning 2026-04-17. Run audit script first (`python3 tooling/audit_guides.py`) to establish structural baseline before reading guides for content grading.*
