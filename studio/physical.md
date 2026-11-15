---
title: Physical Layout and Cabling
type: detail
publish: private
updated: 2026-11-15
---

# Physical Layout and Cabling

How the racks are laid out and how cables cross the room. Connection details are in `data/connections.csv`, and the tables below are views of it. When they disagree, the CSV is right.

## 1. Jaspers rack

A 4-tier rack holding the Mackie console and the MPC X, with a rack-mounted power and patching stack.

**Rack-mounted stack, top to bottom** (owner, 2026-11-15, basis `observed`):

1. 96-port 1U patch bay.
2. Radial Power-1 power conditioner.
3. Black Lion PG-X power conditioner.

The Magnatone Baby M-80 head and its Marshall Studio JTM 2x12 cabinet stand just to the right of the rack as you face it, nearly touching. The head is powered from the Radial above and is wired only to its cabinet.

The first draft also places a Eurorack case here, holding the master sequencing and clock modules. ⚠ Not confirmed.

## 2. On-stage

A 3-tier instrument stand and a 19 inch server rack.

**Server rack.** It holds only the Radial Power-1 power conditioner (owner, 2026-11-15, basis `observed`). The first draft's order, with the patch bay, a 1U gap and a Black Lion unit, does not match the rack as built. The patch bay is in the Jaspers rack.

**Rack mounting.** The patch bay and the power conditioners are rack mounted. The MRCC sits loose on the on-stage rack today and is not powered yet; its ears are on order. The MRCC is 15.25 inches wide, 3.5 inches high and 1.5 inches deep, and all its MIDI and USB jacks are on the front panel, so cables leave the front of the rack. The first draft assumed rear jacks, so its access notes no longer apply. Plan the cable exit and a front strain relief before the ears go on.

**Stand instruments:** Hydrasynth, Take 5, MicroFreak, Pulsar-23, Lyra-8, EP-1320 Medieval, Solar 50, SP-404 MKII and the Yamaha MG10XU.

## 3. The bridge

The floor run joining the two zones is a low-profile rubber cord cover of about 4 to 6 feet, with beveled edges and separate channels.

- MIDI and analog audio run in separate channels, so digital chatter stays out of the audio.
- Leave a relaxed 3 to 4 inch loop under each stand before the cover, so a bump never stresses a jack.
- Bundle with reusable Velcro and leave 4 to 6 inch loops at connectors.

Two things in the first draft contradict each other and need a decision:

- It says AC power trunks run in "suspended bundles" beside the cover, but the cover is on the floor and no AC cable is in its manifest. Decide whether AC crosses at all. If it does, keep it out of the audio channel.
- Three lengths appear: about 1 meter of gap, a 4 to 6 foot cover and 10 foot cables. The loops explain the difference, but the document never says so.

### Cables that cross the bridge

| Link | From | To | Signal | Status |
|---|---|---|---|---|
| A-009 | yamaha-mg10xu.main-out-l | mackie.ch- | to confirm | planned |
| A-010 | yamaha-mg10xu.main-out-r | mackie.ch- | to confirm | planned |
| M-008 | mpcx.midi-out-a | mrcc.in-5 | midi-din | planned |
| M-009 | mrcc.out-4 | mpcx.midi-in | midi-din | planned |

### Cables that may cross

These touch the Hermod+, Ground Control or Pamela's PRO Workout, which are in case Go_0. Whether that case is on the Jaspers side is not yet recorded.

| Link | From | To | Signal | Status |
|---|---|---|---|---|
| M-005 | ground-control.midi-out | mrcc.in-3 | midi-trs-a | planned |
| M-006 | mrcc.out-3 | ground-control.midi-in | midi-din | planned |
| M-007 | pams.midi-out | mrcc.in-4 | midi-trs-a | planned |
| M-010 | hermod.midi-out | mrcc.in-6-trs-a | midi-trs-a | planned |
| M-011 | mrcc.out-12-trs-a | hermod.midi-in | midi-trs-a | planned |

## 4. Cable stock

Rough, from the owner's memory: about 300 3.5 mm TS patch cables for the modular, many TRS Type A to Type B adapters, and 5-pin MIDI cables. Monitor runs are XLR. The owner is wiring with the cables on hand, so planned output ports in the data may change with the lengths available.

## 5. Open items

- Which zone each Eurorack case belongs to.
- Whether AC crosses the bridge.
- The label scheme. The IDs in the data are meant to match physical labels on both ends of each cable.
- The final MRCC position, and its front cable exit.
- Where the Eurorack cases physically stand: the Go cases and Mantis take power from the Jaspers rack, so a long supply run may exist if they are on-stage.
- The jack type and normalling of the 96-port patch bay.
