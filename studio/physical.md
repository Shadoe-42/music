---
title: Physical Layout and Cabling
type: detail
publish: private
updated: 2026-11-15
---

# Physical Layout and Cabling

How the racks are laid out and how cables cross the room. Connection details are in `data/connections.csv`, and the tables below are views of it. When they disagree, the CSV is right.

## 1. Jaspers rack

A 4-tier rack of rows, with arms holding the Eurorack cases and the synths. As placed (owner, 2026-11-15, basis `observed`), top to bottom:

```text
Top row     JU-06A   │ Mantis case │ SH-4d
Row 2       Go_2     │ Go_3
Row 3       Go_0     │ Go_1
Bottom row  MPC X    │ Mackie 30-channel mixer      (about 28 inches off the floor)
```

A 19 inch server rack stands on the floor under the bottom row, in the middle of the floor space. Top to bottom it holds the 96-port 1U patch bay, the Radial Power-1 and the Black Lion PG-X. The T10S subwoofer sits on the floor to the right of that server rack, under the bottom row, and the two T8V monitors are on stands at about standing head height, just outside the left and right vertical supports of the synth rack.

The Magnatone Baby M-80 head and its Marshall Studio JTM 2x12 cabinet stand just to the right of the Jaspers rack, nearly touching it. The head is powered from the Radial and is wired only to its cabinet.

The NiftyCase is on a separate table, used by the family, and is not part of these racks.

A photo of the Jaspers rack from the front, 2026-11-15, is kept outside the repository at `~/claude/studio_photos/jaspers_rack_2026-11-15.jpg`. It is not published.

## 2. On-stage

A 3-tier instrument stand and a 19 inch server rack.

**Server rack.** It holds only the Radial Power-1 power conditioner (owner, 2026-11-15, basis `observed`). The first draft's order, with the patch bay, a 1U gap and a Black Lion unit, does not match the rack as built. The patch bay is in the Jaspers rack.

**Rack mounting.** The patch bay and the power conditioners are rack mounted, the Jaspers ones in the floor server rack. The MRCC sits loose on the on-stage rack today and is not powered yet; its ears are on order. The MRCC is 15.25 inches wide, 3.5 inches high and 1.5 inches deep, and all its MIDI and USB jacks are on the front panel, so cables leave the front of the rack. The first draft assumed rear jacks, so its access notes no longer apply. Plan the cable exit and a front strain relief before the ears go on.

**Stand instruments:** Hydrasynth, Take 5, MicroFreak, Pulsar-23, Lyra-8, EP-1320 Medieval, Solar 50, SP-404 MKII and the Yamaha MG10XU.

## 3. The bridge

**The bridge does not exist yet.** The floor cord cover is on order and due within days (owner, 2026-11-15), so every cross-zone cable in the data is planned. The run is meant to be a low-profile rubber cord cover of about 4 to 6 feet, with beveled edges and separate channels.

- MIDI and analog audio run in separate channels, so digital chatter stays out of the audio.
- Leave a relaxed 3 to 4 inch loop under each stand before the cover, so a bump never stresses a jack.
- Bundle with reusable Velcro and leave 4 to 6 inch loops at connectors.

Two things in the first draft contradict each other and need a decision:

- It says AC power trunks run in "suspended bundles" beside the cover, but the cover is on the floor and no AC cable is in its manifest. Decide whether AC crosses at all. If it does, keep it out of the audio channel.
- Three lengths appear: about 1 meter of gap, a 4 to 6 foot cover and 10 foot cables. The loops explain the difference, but the document never says so.

### Cables that will cross the bridge

All are planned, and none exist yet. The Hermod+, Ground Control and Pamela's are in Go_0, which is in the Jaspers rack, so their MIDI links cross.

| Link | From | To | Signal | Status |
|---|---|---|---|---|
| A-009 | yamaha-mg10xu.main-out-l | mackie.ch- | to confirm | planned |
| A-010 | yamaha-mg10xu.main-out-r | mackie.ch- | to confirm | planned |
| M-005 | ground-control.midi-out | mrcc.in-3 | midi-trs-a | planned |
| M-006 | mrcc.out-3 | ground-control.midi-in | midi-din | planned |
| M-007 | pams.midi-out | mrcc.in-4 | midi-trs-a | planned |
| M-008 | mpcx.midi-out-a | mrcc.in-5 | midi-din | planned |
| M-009 | mrcc.out-4 | mpcx.midi-in | midi-din | planned |
| M-010 | hermod.midi-out | mrcc.in-6-trs-a | midi-trs-a | planned |
| M-011 | mrcc.out-12-trs-a | hermod.midi-in | midi-trs-a | planned |

## 4. Cable stock

Rough, from the owner's memory: about 300 3.5 mm TS patch cables for the modular, many TRS Type A to Type B adapters, and 5-pin MIDI cables. Monitor runs are XLR. The owner is wiring with the cables on hand, so planned output ports in the data may change with the lengths available.

## 5. Open items

- Whether AC crosses the bridge.
- The label scheme. The IDs in the data are meant to match physical labels on both ends of each cable.
- The final MRCC position, and its front cable exit.
- The power and USB arrangements for the JU-06A and the SH-4d, which are on no outlet.
- The jack type and normalling of the 96-port patch bay.
