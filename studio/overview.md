---
title: Studio Overview
type: master
publish: private
updated: 2026-11-15
---

# Studio Overview

The as-built record of this studio, and the entry point to every other document about it. It describes what is going on and links to the documents that hold the detail. The rules for all of them are in `standards.md`, and the controlled terms are in `vocab.md`. The first-draft wiring document, `studio_wiring_signal_flow_reference.md`, is superseded by the documents listed here and still contains known errors, so do not rely on it.

Snapshot date: 2026-11-15. The studio is being wired now, so statuses change often.

## 1. The studio in brief

Two physical zones are meant to be joined by a floor run (the bridge, not built yet; the cord cover is on order):

- **Jaspers rack** (`jaspers-rack`): master control and the main mix. It holds the Mackie console and the MPC X, with a rack stack of a 96-port 1U patch bay, a Radial Power-1 and a Black Lion PG-X. A Magnatone Baby M-80 head and a Marshall cabinet stand beside it, standalone.
- **On-stage** (`on-stage`): a 3-tier instrument stand holding the synth and drum fleet, the MRCC MIDI router and the Yamaha MG10XU, and a 19 inch server rack holding only a Radial Power-1 power conditioner.
- **Eurorack**: six cases, all filled, powered and mounted. The Mantis and Go_0 to Go_3 are on the Jaspers rack arms. The NiftyCase is on a separate table used by the family and is not wired into the racks.

## 2. Signal flow at a glance

```text
AUDIO   (as built, except the Yamaha)
  Cockpit 2 (Go_2) ─┐
  Listen IO (Go_3) ──┼─► Mackie ──XLR──► T10S sub ──XLR──► T8V left, T8V right
  Mixup (Go_1) ──────┘        ▲
  Yamaha MG10XU [planned link] ──┘      (the Hydrasynth feeds the Yamaha, ch 9 and 10, wired)

MIDI AND CLOCK   (all planned)
  Hydrasynth, Take 5, MPC X, Hermod+, Ground Control, Pamela's PRO Workout ──► MRCC
  MRCC ──► Hydrasynth, Take 5, Pulsar-23, SP-404 MKII, MPC X (returns), and over USB host
           ports ◄──► MicroFreak, EP-1320 Medieval

POWER
  Wall ──► Radial Power-1 and Black Lion PG-X (Jaspers rack) ──► Mackie, MPC X, sub, T8Vs, Mantis, Go cases, M80
  Wall ──► Radial Power-1 (on-stage) ──► the synth and drum fleet, the Yamaha adaptor
  Plus separate supplies: Go cases and Take 5 (barrel DC), MG10XU (PA-10B, AC), MRCC (USB-C, not powered yet), JU-06A and SH-4d (power not recorded)
```

## 3. Gear by zone

**Jaspers rack**

| Device | Maker | Role |
|---|---|---|
| Mackie 30-channel console | Mackie | main mixer |
| MPC X | Akai | sampler, sequencer, MIDI hub |
| JU-06A | Roland | Boutique synthesizer module |
| SH-4d | Roland | desktop synthesizer |
| 96-port 1U patch bay | to confirm | audio patch bay |
| Power-1 | Radial Engineering | power conditioner |
| PG-X | Black Lion Audio | power conditioner |
| Baby M-80 head, Chrome Grape | Magnatone | guitar amplifier head, standalone |
| Studio JTM 2x12 angled cabinet | Marshall | guitar speaker cabinet |

**On-stage**

| Device | Maker | Role |
|---|---|---|
| MRCC | Conductive Labs | MIDI router |
| MG10XU | Yamaha | small mixer, stereo submixer |
| PA-10B | Yamaha | AC power adaptor for the MG10XU |
| Hydrasynth | ASM | synthesizer and keybed |
| Take 5 | Sequential | synthesizer |
| MicroFreak | Arturia | synthesizer |
| Pulsar-23 | SOMA | drum synthesizer |
| Lyra-8 | SOMA | drone synthesizer |
| EP-1320 Medieval | Teenage Engineering | synthesizer |
| Solar 50 | Elta Music | synthesizer |
| SP-404 MKII | Roland | sampler |
| Power-1 | Radial Engineering | power conditioner |

**Monitors** (all in the Jaspers zone)

| Device | Maker | Role |
|---|---|---|
| T10S | Adam Audio | subwoofer, first in the monitor chain |
| T8V (left) | Adam Audio | studio monitor |
| T8V (right) | Adam Audio | studio monitor |

**Eurorack cases** (the NiftyCase is off the racks; the rest are in the Jaspers zone)

| Device | Maker | Role |
|---|---|---|
| Mantis | to confirm | Eurorack case |
| Go_0 | to confirm | Eurorack case |
| Go_1 | to confirm | Eurorack case |
| Go_2 | to confirm | Eurorack case |
| Go_3 | to confirm | Eurorack case |
| NiftyCase | to confirm | Eurorack case |

**Eurorack modules tracked here.** Each is installed in a case; the case is in the device record.

| Device | Maker | Role |
|---|---|---|
| Hermod+ | Squarp Instruments | Eurorack sequencer and master clock |
| Ground Control | Endorphin.es | Eurorack sequencer and master clock |
| Pamela's PRO Workout | ALM Busy Circuits | Eurorack clock source |
| Cockpit 2 | Endorphin.es | Eurorack mixer |
| Listen IO | 4ms Company | Eurorack external audio I/O module |
| Mixup | Intellijel | Eurorack mixer |

## 4. Documents

| Document | Holds | Publish |
|---|---|---|
| `standards.md` | The rules for these documents | public |
| `vocab.md` | Controlled terms | public |
| `audio.md` | Audio paths, Mackie channels, monitor chain, Yamaha MG10XU | private |
| `midi_and_clock.md` | MRCC port plan, channels, clock, presets | private |
| `power.md` | Outlet maps, supplies, grounding | private |
| `physical.md` | Racks, the bridge, cabling | private |
| `data/devices.csv`, `data/connections.csv` | The source of truth for devices and cables | private |
| `../infrastructure/` | Guides for infrastructure devices, such as the MRCC | public |
| `../modular/` | The modular system and its module guides | public |

The Eurorack power maps and the rack and case plan are kept outside this repository, in `~/claude/`, and are named where they are used.

## 5. Status snapshot

Connections recorded in `data/connections.csv`, as of the snapshot date:

| Type | Planned | Wired | Tested | Retired |
|---|---|---|---|---|
| Audio | 2 | 10 | 0 | 0 |
| MIDI and clock | 15 | 0 | 0 | 0 |
| Power | 1 | 23 | 0 | 7 |

Nothing is `tested` yet. The CSV is the live record; this table goes stale.

## 6. Open issues

1. **The bridge is not built.** The floor cord cover is on order, so every cross-zone cable is planned. The Hermod+, Ground Control and Pamela's links to the MRCC will cross it. See `physical.md`.
2. **MIDI channels 9 to 16.** What they carry through the MRCC is unclear. See `midi_and_clock.md`.
3. **Mackie to computer.** How audio reaches the DAW is not recorded. See `audio.md`.
4. **Patch bay point list and gain staging.** Neither exists yet, and the patch bay's jack type needs checking, since 96 points in 1U usually means bantam jacks ⚠. See `audio.md`.
5. **Power sources.** The outlet maps and wall feeds are recorded, one independent wall outlet per unit. The circuits behind them, the wall supplies for the Go cases and the Take 5, and how each synth takes its power are not. See `power.md`.
6. **Possible USB hum.** Two USB-connected synths feed audio into the Yamaha. Listen for it when they are wired. See `midi_and_clock.md`.
7. **T10S phase and sensitivity.** Not recorded. See `audio.md`.
8. **Cable labels.** The IDs in the data are meant to match physical labels, and no label scheme has been chosen.
9. **The first-draft wiring document** should be retired once nothing depends on it.
10. **Magnatone and cabinet.** Standalone and connected to each other, with the speaker cable and the cabinet impedance unrecorded. See `audio.md`.
11. **Unpowered synths.** The JU-06A and SH-4d are on no outlet and their power is not recorded. See `power.md`.
12. **Spare power units.** The owner thinks there are more Black Lion and Furman units than the three in the racks. They are not recorded.
