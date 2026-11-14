---
title: MIDI and Clock
type: detail
publish: private
updated: 2026-11-14
---

# MIDI and Clock

How MIDI notes and clock move through the studio. The MRCC is the hub. Device facts (what the MRCC is and how it works) live in `../infrastructure/conductive_labs_mrcc_guide.md`; this document holds how this studio uses it. The cables are recorded in `data/connections.csv`, and the tables below are views of it. When they disagree, the CSV is right.

**Status:** no MIDI link is recorded as wired yet. Every row below is `planned`.

## 1. The MRCC here

Facts checked on 2026-11-14 against the Conductive Labs user manual (v1.1.071) and the front-panel photo:

- Every MIDI and USB jack is on the **front panel**. Power (USB-C, 5 V, 3 A), the power switch, the analog clock out, the Remote jack and the firmware button are on the side. Cables leave the front of the rack.
- The unit is mounted on the rack today. Rack ears are on order, so the front cabling needs to be planned around the final position.
- **Inputs 1 to 6.** DIN on 1 to 5. TRS Type A and B jacks share input 1 with its DIN jack, and input 6 is TRS only.
- **Outputs 1 to 12.** DIN on 1 to 10. Outputs 11 and 12 are TRS, each with a separate Type A and Type B jack usable at the same time. The Type is chosen by the jack, not by a setting.
- **USB.** Four host ports (A to D), USB type A, and one PC port, USB type B.

Port names used in the data: `in-1` to `in-5`, `in-6-trs-a`, `out-1` to `out-10`, `out-11-trs-a`, `out-12-trs-a`, `host-a` to `host-d`, `pc`.

## 2. Port plan

The numbers force one choice: six MIDI sources and only five DIN inputs. Input 6 goes to a TRS source, and Hermod+ already speaks TRS Type A, so it needs no converter.

| Input | Device | Link | Cable |
|---|---|---|---|
| `in-1` | Hydrasynth | M-001 | 5-pin DIN |
| `in-2` | Take 5 | M-003 | 5-pin DIN |
| `in-3` | Ground Control | M-005 | TRS Type A to DIN |
| `in-4` | Pam's Pro Workout (clock only) | M-007 | TRS Type A to DIN |
| `in-5` | MPC X | M-008 | 5-pin DIN |
| `in-6-trs-a` | Hermod+ | M-010 | straight TRS Type A |

| Output | Device | Link | Cable |
|---|---|---|---|
| `out-1` | Hydrasynth | M-002 | 5-pin DIN |
| `out-2` | Take 5 | M-004 | 5-pin DIN |
| `out-3` | Ground Control (optional return) | M-006 | DIN to TRS Type A adapter |
| `out-4` | MPC X (optional return) | M-009 | 5-pin DIN |
| `out-5` | Pulsar-23 | M-012 | 5-pin DIN |
| `out-11-trs-a` | SP-404 MKII | M-015 | straight TRS Type A |
| `out-12-trs-a` | Hermod+ (optional return) | M-011 | straight TRS Type A |
| `host-a` | MicroFreak | M-013 | USB |
| `host-b` | EP-1320 Medieval | M-014 | USB |

Output assignments are proposals, apart from the SP-404 on a TRS Type A jack, which follows from the plan you approved. Adjust them freely; a planned row can be corrected in place.

## 3. Channel allocation

Carried from the first draft, not yet tested.

| Channel | Device |
|---|---|
| 1 | Hydrasynth |
| 2 | Take 5 |
| 3 | MicroFreak |
| 4 | Pulsar-23 (bass drum, bass, snare, hi-hat through MIDI learn) |
| 5 | SP-404 MKII, banks A to E |
| 6 | SP-404 MKII, banks F to J |
| 7 | EP-1320 Medieval |
| 8 | open |
| 9 to 16 | Eurorack voices |

Open question: the Eurorack voices are driven from Hermod+ and Ground Control over CV and gate, so it is unclear what MIDI on channels 9 to 16 carries through the MRCC. Decide before the presets are built.

## 4. Clock

One clock source is active at a time. Candidates:

- Hermod+, Ground Control, Pam's Pro Workout or the MPC X, each through the MRCC.
- The MRCC's own clock, adjustable from 10 to 240 BPM.

The MRCC filters clock per routing, per input port or per output port, so each preset can pass clock from one source and block it from the rest. Its manual warns that merging several inputs onto one output can delay or lose traffic, clock above all. This is why the single-source rule exists.

The MRCC also has an **analog clock out**: a 1/8 inch mono TS jack at 1, 2, 4 or 24 pulses per quarter note, at 5 V or 12 V. It could feed the Eurorack directly, bypassing Hermod+. Whether to use it is open and not yet in the data.

## 5. Presets

The MRCC stores one factory preset (number 0, read-only) and 127 user presets on its microSD card. A preset holds routings, modifiers, extras and label assignments, and not global settings. Planned set, from the first draft, none built yet:

| Preset | Purpose |
|---|---|
| HOME | Hermod+ is the clock for every clock-capable synth; Hydrasynth plays channels 1 to 7 |
| GNDCTL CLK | As HOME, with Ground Control as the clock |
| PAMS CLK | As HOME, with Pam's as the clock, for free-jamming standalone sequencers |
| MPCX MASTER | MPC X is the clock and sequencer across channels 1 to 16 |
| HYDRA to T5 | Hydrasynth plays the Take 5 only, without changing the keyboard's transmit channel |

⚠ Preset naming: sources disagree on whether names can be edited. Check on the unit.

## 6. MIDI hygiene

1. **One clock source** per preset, with clock filtered from every other input.
2. **Local Control off** on a synth whose MIDI out is routed through a sequencer and back into itself, to avoid doubled notes. ⚠ Check the setting on the Hydrasynth and the Take 5.
3. **TRS polarity.** Type A has tip on DIN pin 5, ring on pin 4, sleeve on pin 2. Type B swaps tip and ring, and a swapping adapter converts between them. The MRCC provides both types as separate jacks.
4. **Ground paths.** The MicroFreak and the Medieval will sit on USB host ports while their audio goes to the Yamaha. That is the pattern that can cause USB hum. Listen for it when they are wired, and keep DIN across the bridge.

## 7. Open items

- **SysEx.** The manual says SysEx passes through all ports; a retailer lists outputs 1 to 6 only. ⚠ Test with a device that needs it.
- **Channels 9 to 16**, as in section 3.
- **Return paths** M-006, M-009 and M-011: are they needed, or is the Hydrasynth the only controller?
- **MacBook.** The first draft routes a laptop into the MRCC PC port. No row yet.
- **Lyra-8 and Solar 50 clocking.** The first draft's claim is unsupported and is not recorded.
- **Eurorack case zones**, which decide which MIDI cables cross the bridge.
