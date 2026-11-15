---
title: Studio Documentation Standards
type: standards
publish: public
updated: 2026-11-15
---

# Studio Documentation Standards

These rules govern every document in `studio/`. They exist so the record stays accurate as gear moves, and so any document can be trusted, checked and, where appropriate, published. Terms used in tables come from `vocab.md`.

## 1. What lives where

| Folder | Holds | Question it answers |
|---|---|---|
| `studio/` | The as-built record of this studio: master doc, detail docs, data | How is everything actually wired? |
| `infrastructure/` | Guides for infrastructure devices: routers, mixers, patch bays, power, monitors | What is this device and how does it work? |
| `modular/` | The modular system and its module guides | What is in the Eurorack, and what does each module do? |

A fact lives in exactly one place. Every other document links to it and never restates it.

## 2. Document types

| Type | Purpose | Rule |
|---|---|---|
| `master` | Describes the whole studio at a glance and indexes everything else | Short enough to read in one sitting; no deep detail |
| `detail` | One domain in depth (MIDI and clock, audio, power, physical, modular interface) | Links back to the master; owns its domain's facts |
| `data` | Connection and device records (CSV) | The source of truth for every cable and device |
| `vocab` | Controlled terms | A term is added here before it is used anywhere else |
| `standards` | This document | Updated in the same session that a refinement is discovered |

Every markdown document carries frontmatter with at least `title`, `type`, `publish` and `updated`.

## 3. Identity

Identity never encodes location, because gear moves.

- **Devices** have a short, stable, lowercase slug, such as `mrcc` or `mackie`. A slug is never reused for a different device.
- A device may carry an `aka`, the owner's shorthand for it. An `aka` is never used as an identifier, because a nickname often names a role and not a model.
- **Ports** are written `device.port`, for example `mrcc.din-out-3`.
- **Connections** have an ID made of a type prefix and a three-digit number: `A-014`, `M-007`, `V-022`, `P-003`, `D-005`. Prefixes are defined in `vocab.md`.
- **IDs are never renumbered and never reused.** A connection that goes away is marked `retired`, and its row stays.
- Zone is a column on the record, not part of the ID.
- A `planned` row that turns out to be wrong may be corrected in place, because nothing physical depends on it yet. Once a row is `wired` or `tested`, changing an endpoint means retiring the row and adding a new ID.

## 4. The connection record

Every cable or link has one row in `data/connections.csv` with these fields:

| Field | Meaning |
|---|---|
| `id` | Per section 3 |
| `from`, `to` | `device.port` at each end |
| `signal` | Term from `vocab.md` |
| `connector_from`, `connector_to` | Terms from `vocab.md` |
| `zone_from`, `zone_to` | Terms from `vocab.md`; a cable that crosses zones shows both |
| `status` | `planned`, `wired`, `tested` or `retired` |
| `verified` | Date of the last check; required when status is `tested` |
| `basis` | How the row is known: `observed`, `manual`, `stated` or `inferred` |
| `note` | Anything a future reader needs |

## 5. Status and provenance

Status and basis answer different questions, so they are kept apart.

- **Status** describes the connection. `wired` means physically connected with the signal not yet checked. `tested` means the signal was confirmed, on the date in `verified`, with the method in `note`. Moving or replacing a cable resets its status to `wired`.
- **Basis** describes how the fact is known. `observed` means someone checked it at the equipment or by measurement. `manual` means the manufacturer's documentation states it, and `note` names the document. `stated` means the owner said it. `inferred` means it was derived and has not been checked.
- A technical specification (a voltage, a level, a polarity, a firmware behavior) whose basis is `stated` or `inferred` is marked with ⚠ wherever it appears.
- **Observed beats remembered.** A model name, a count, a port assignment or a connector is recorded from the hardware, with basis `observed`. A value taken from memory stays `stated` and is treated as provisional until someone checks it. Counts and port assignments are never written down from memory alone. A nickname such as "the Yamaha" is not a model until the badge has been read.

## 6. Data and views

The CSV files in `data/` are the source of truth. Markdown tables are views of them. When a table and the CSV disagree, the CSV is right. Until a generator exists, a change is made in the CSV first and the view is updated by hand in the same commit. IDs are checked for duplicates before every commit.

## 7. Publishing

Every document declares `publish: private` or `publish: public`.

- **Private by default:** anything specific to this studio, such as the as-built record, the connection data, layout, inventory and power topology.
- **Public:** standards, vocabulary, device guides, and lessons extracted from the as-built record with the studio specifics removed.
- Only `public` documents sync to GitHub. A public document never contains physical location details, serial numbers or a complete inventory.

## 8. Writing

- No contractions and no em dashes.
- Define a technical term in plain language before its precise name, on first use.
- Verify a manufacturer name before writing it.
- Flag uncertain specifications with ⚠ per section 5.

## 9. Physical conventions

- **Stereo cable color:** red is right and black is left, always (owner's rule). A pair that breaks the rule is a labeling fault to fix, not a variation to record.

## 10. Changing these standards

When practice shows a rule needs refining, update this document in the same session, as its own change with its own commit.
