---
title: Studio Overview
type: master
publish: private
updated: 2026-11-14
---

# Studio Overview

The as-built record of this studio, and the entry point to every other document about it. It describes what is going on and links to the documents that hold the detail. The rules for all of them are in `standards.md`, and the controlled terms are in `vocab.md`. The first-draft wiring document, `studio_wiring_signal_flow_reference.md`, is superseded by the documents listed here and still contains known errors, so do not rely on it.

Snapshot date: 2026-11-14. The studio is being wired now, so statuses change often.

## 1. The studio in brief

Two physical zones are joined by a floor run (the bridge):

- **Jaspers rack** (`jaspers-rack`): master control and the main mix. It holds the Mackie console, the MPC X and a Black Lion power conditioner.
- **On-stage** (`on-stage`): a 3-tier instrument stand and a 19 inch server rack holding the synth and drum fleet, the MRCC MIDI router, the patch bay, the Yamaha submixer and a second power conditioner.
- **Eurorack**: six cases (Mantis, Go_0 to Go_3, NiftyCase), all filled, powered and mounted. Which zone each case belongs to is not yet recorded.

## 2. Signal flow at a glance

```text
AUDIO   (as built, except the Yamaha)
  Cockpit 2 (Go_2) ─┐
  Listen IO (Go_3) ──┼─► Mackie ──XLR──► T10S sub ──XLR──► T8V left, T8V right
  Mixup (Go_1) ──────┘        ▲
  Yamaha submixer [planned] ──┘

MIDI AND CLOCK   (all planned)
  Hydrasynth, Take 5, MPC X, Hermod+, Ground Control, Pamela's PRO Workout ──► MRCC
  MRCC ──► Hydrasynth, Take 5, Pulsar-23, SP-404 MKII, MPC X (returns), and over USB host
           ports ◄──► MicroFreak, EP-1320 Medieval

POWER
  Wall ──► Black Lion conditioners (one per rack, to confirm) ──► the racks
  Plus separate DC supplies: Go cases and Take 5 (barrel), MRCC (USB-C), JU-08A (mini-USB)
```

## 3. Gear by zone

**Jaspers rack**

| Device | Maker | Role |
|---|---|---|
| Mackie 30-channel console | Mackie | main mixer |
| MPC X | Akai | sampler, sequencer, MIDI hub |
| Power conditioner | Black Lion Audio | power conditioner for the Jaspers rack |

**On-stage**

| Device | Maker | Role |
|---|---|---|
| MRCC | Conductive Labs | MIDI router |
| 1/4 inch patch bay | to confirm | audio patch bay, half-normalled per first draft |
| Yamaha submixer | Yamaha | stereo submixer and monitor bus |
| Hydrasynth | ASM | synthesizer and keybed |
| Take 5 | Sequential | synthesizer |
| MicroFreak | Arturia | synthesizer |
| Pulsar-23 | SOMA | drum synthesizer |
| Lyra-8 | SOMA | drone synthesizer |
| EP-1320 Medieval | Teenage Engineering | synthesizer |
| Solar 50 | Elta Music | synthesizer |
| SP-404 MKII | Roland | sampler |
| Power conditioner | Black Lion Audio | power conditioner for the on-stage rack |

**Monitors** (zone not yet recorded)

| Device | Maker | Role |
|---|---|---|
| T10S | Adam Audio | subwoofer, first in the monitor chain |
| T8V (left) | Adam Audio | studio monitor |
| T8V (right) | Adam Audio | studio monitor |

**Eurorack cases** (zone not yet recorded)

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
| `audio.md` | Audio paths, Mackie channels, monitor chain, Yamaha plan | private |
| `midi_and_clock.md` | MRCC port plan, channels, clock, presets | private |
| `power.md` | AC and DC power, supplies, grounding | private |
| `physical.md` | Racks, the bridge, cabling | private |
| `data/devices.csv`, `data/connections.csv` | The source of truth for devices and cables | private |
| `../infrastructure/` | Guides for infrastructure devices, such as the MRCC | public |
| `../modular/` | The modular system and its module guides | public |

The Eurorack power maps and the rack and case plan are kept outside this repository, in `~/claude/`, and are named where they are used.

## 5. Status snapshot

Connections recorded in `data/connections.csv`, as of the snapshot date:

| Type | Planned | Wired | Tested |
|---|---|---|---|
| Audio | 2 | 8 | 0 |
| MIDI and clock | 15 | 0 | 0 |
| Power | 1 | 7 | 0 |

Nothing is `tested` yet. The CSV is the live record; this table goes stale.

## 6. Open issues

1. **Eurorack case zones.** Unrecorded, and they decide which cables cross the bridge. See `physical.md`.
2. **MIDI channels 9 to 16.** What they carry through the MRCC is unclear. See `midi_and_clock.md`.
3. **Mackie to computer.** How audio reaches the DAW is not recorded. See `audio.md`.
4. **Patch bay point list and gain staging.** Neither exists yet. See `audio.md`.
5. **Power maps.** Conditioner models, counts and outlet assignments are not recorded. See `power.md`.
6. **Possible USB hum.** Two USB-connected synths feed audio into the Yamaha. Listen for it when they are wired. See `midi_and_clock.md`.
7. **T10S phase and sensitivity.** Not recorded. See `audio.md`.
8. **Cable labels.** The IDs in the data are meant to match physical labels, and no label scheme has been chosen.
9. **The first-draft wiring document** should be retired once nothing depends on it.
