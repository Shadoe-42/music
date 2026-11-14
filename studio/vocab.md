---
title: Studio Vocabulary
type: vocab
publish: public
updated: 2026-11-14
---

# Studio Vocabulary

Controlled terms for every table and data file in `studio/`. A term is added here before it is used anywhere else. This list is capped at terms that exist in the studio today; it grows only when a real record needs a new term. Gear names and makers are not kept here: they live in `data/devices.csv`, where each maker is verified.

Entries marked ⚠ are carried over from the first-draft wiring document and have not been checked against a primary source.

## Zones

| Term | Meaning |
|---|---|
| `jaspers-rack` | The Jaspers 4-tier rack: master control and main mix |
| `on-stage` | The on-stage stand and 19-inch server rack: the synth and drum fleet |
| `bridge` | The floor run between the two zones |

Which zone each Eurorack case belongs to is not yet recorded.

## Signal types

| Term | Plain meaning |
|---|---|
| `audio-line-balanced` | Line-level audio on a three-conductor cable that cancels picked-up noise |
| `audio-line-unbalanced` | Line-level audio on a two-conductor cable, more prone to hum over distance |
| `midi-din` | MIDI note and clock messages over a five-pin DIN cable |
| `midi-trs-a` | MIDI over a 3.5 mm stereo cable, wired as Type A ⚠ |
| `midi-trs-b` | MIDI over a 3.5 mm stereo cable, wired as Type B ⚠ |
| `midi-usb` | MIDI messages over USB |
| `clock-analog` | A pulse signal that carries tempo to gear without MIDI |
| `cv` | Control voltage: a changing voltage that controls pitch or a parameter |
| `gate` | A voltage that is high while a note is held and low otherwise |
| `power-ac` | Mains power |
| `power-dc` | Low-voltage direct-current power to a device |
| `usb-data` | USB used for data other than MIDI |

MIDI TRS polarity, as carried from the draft ⚠: Type A has the tip on DIN pin 5 (current sink) and the ring on pin 4 (current source). Type B swaps them. Verify against the MIDI Association specification before relying on it.

## Connectors

| Term | Meaning |
|---|---|
| `ts-quarter` | 1/4 inch two-conductor jack, unbalanced |
| `trs-quarter` | 1/4 inch three-conductor jack, balanced or stereo |
| `trs-3.5mm` | 3.5 mm three-conductor jack, used here for MIDI |
| `din-5` | Five-pin DIN, the original MIDI connector |
| `xlr-3` | Three-pin XLR, balanced |
| `usb-b` | USB type B |
| `usb-c` | USB type C |
| `iec` | Standard mains inlet or cord |
| `barrel-dc` | Barrel-type low-voltage DC connector, as on wall supplies |

## Connection ID prefixes

| Prefix | Carries |
|---|---|
| `A` | Audio |
| `M` | MIDI and analog clock |
| `V` | CV and gate |
| `P` | Power, AC and DC |
| `D` | USB and other data |

## Status

| Term | Meaning |
|---|---|
| `planned` | Intended, not yet connected |
| `wired` | Physically connected, signal not yet checked |
| `tested` | Signal confirmed on the `verified` date |
| `retired` | No longer in place; the row stays and the ID is never reused |

## Basis

| Term | Meaning |
|---|---|
| `observed` | Checked at the equipment or by measurement |
| `manual` | Stated in manufacturer documentation, named in the note |
| `stated` | Said by the owner |
| `inferred` | Derived, not checked |

## Document fields

| Field | Values |
|---|---|
| `type` | `master`, `detail`, `data`, `vocab`, `standards` |
| `publish` | `private`, `public` |
