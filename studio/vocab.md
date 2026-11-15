---
title: Studio Vocabulary
type: vocab
publish: public
updated: 2026-11-15
---

# Studio Vocabulary

Controlled terms for every table and data file in `studio/`. A term is added here before it is used anywhere else. This list is capped at terms that exist in the studio today; it grows only when a real record needs a new term. Gear names and makers are not kept here: they live in `data/devices.csv`, where each maker is verified.

Entries marked ⚠ have not been checked against a primary source.

## Zones

| Term | Meaning |
|---|---|
| `jaspers-rack` | The Jaspers 4-tier rack: master control and main mix |
| `on-stage` | The on-stage stand and 19-inch server rack: the synth and drum fleet |
| `bridge` | The floor run between the two zones |

## Signal types

| Term | Plain meaning |
|---|---|
| `audio-line-balanced` | Line-level audio on a three-conductor cable that cancels picked-up noise |
| `audio-line-unbalanced` | Line-level audio on a two-conductor cable, more prone to hum over distance |
| `midi-din` | MIDI note and clock messages over a five-pin DIN cable |
| `midi-trs-a` | MIDI over a 3.5 mm stereo cable, wired as Type A, the MIDI Association standard |
| `midi-trs-b` | MIDI over a 3.5 mm stereo cable, wired as Type B, an older maker-specific variant |
| `midi-usb` | MIDI messages over USB |
| `clock-analog` | A pulse signal that carries tempo to gear without MIDI |
| `cv` | Control voltage: a changing voltage that controls pitch or a parameter |
| `gate` | A voltage that is high while a note is held and low otherwise |
| `power-ac` | Mains power |
| `power-dc` | Low-voltage direct-current power to a device |
| `power-ac-lv` | Low-voltage alternating-current power, as from the Yamaha PA-10B adaptor; never interchangeable with `power-dc` |
| `usb-data` | USB used for data other than MIDI |

MIDI TRS polarity: Type A has the tip on DIN pin 5, the ring on pin 4 and the sleeve on pin 2. Type B swaps tip and ring. Source: Conductive Labs MRCC 880 user manual, which describes the Type A standard and the swap. An adapter that swaps tip and ring converts between the two.

## Connectors

| Term | Meaning |
|---|---|
| `ts-quarter` | 1/4 inch two-conductor jack, unbalanced |
| `trs-quarter` | 1/4 inch three-conductor jack, balanced or stereo |
| `ts-3.5mm` | 3.5 mm two-conductor jack, the Eurorack patch cable |
| `trs-3.5mm` | 3.5 mm three-conductor jack, used for MIDI and for headphones |
| `din-5` | Five-pin DIN, the original MIDI connector |
| `xlr-3` | Three-pin XLR, balanced |
| `usb-a` | USB type A, the host-side jack on a computer or router |
| `usb-b` | USB type B |
| `usb-c` | USB type C |
| `usb-mini` | Mini-USB, used for power on some devices; which ones to confirm |
| `iec` | Standard mains inlet or cord |
| `barrel-dc` | Barrel-type low-voltage DC connector, as on wall supplies |
| `ac-3pin-locking` | Three-contact locking low-voltage AC plug, as on the Yamaha PA-10B; not a DC connector |

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

## Device roles

Roles in `data/devices.csv` are free text, with these conventions.

| Term | Meaning |
|---|---|
| `power conditioner` | A unit that distributes mains power to several outlets and also filters and surge-protects it. Most units in this studio do both, so this is the single role used for them |

## Device fields

| Field | Meaning |
|---|---|
| `aka` | The owner's shorthand names for a device, separated by semicolons. A nickname often names a role ("small mixer") and not a model, so an `aka` is a trail to the real unit and never an identifier |

## Document fields

| Field | Values |
|---|---|
| `type` | `master`, `detail`, `data`, `vocab`, `standards` |
| `publish` | `private`, `public` |
