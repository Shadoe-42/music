---
title: Power and Grounding
type: detail
publish: private
updated: 2026-11-15
---

# Power and Grounding

How AC and DC power reach the studio's gear. The links are recorded in `data/connections.csv` (the `P-` rows), and this document is a view of them. When they disagree, the CSV is right. Power inside the Eurorack cases is its own subject: see the modular documentation, and the power maps `power_distro_sections_1026.md` and the rack and case plan in `~/claude/`.

Outlet maps below were read off the hardware on 2026-11-15 (basis `observed`). The outlet counts and the front-versus-rear switching come from retailer listings and reviews, not the makers' pages ⚠.

## 1. The chain

```text
Wall ──► Radial Power-1 (Jaspers rack)   ──► 6 loads   (P-009, P-012 to P-017)
Wall ──► Black Lion PG-X (Jaspers rack)  ──► 5 loads   (P-010, P-018 to P-022)
Wall ──► Radial Power-1 (on-stage rack)  ──► 8 loads   (P-011, P-023 to P-030)
```

Three power conditioners serve the studio. The first two are in a 19 inch server rack on the floor under the Jaspers rack's bottom row, with the patch bay above them, and the on-stage server rack holds only the third. Each unit has its own independent wall outlet (owner, 2026-11-15). Whether any of the three outlets share a circuit or breaker is not recorded.

Each unit distributes and conditions, so the role is `power conditioner` (see `vocab.md`). Both Radials have 8 rear outlets that sit behind the unit's power switch and 3 front outlets that stay live when it is off. The PG-X has 8 rear outlets and 1 front outlet.

## 2. Outlet maps

**Radial Power-1, Jaspers rack** (`radial-power-1-1`)

| Outlet | Load | Link |
|---|---|---|
| rear 1 | Adam T10S sub | P-012 |
| rear 2 | Magnatone Baby M-80 head | P-013 |
| rear 3 | Mackie | P-014 |
| rear 4 | open | |
| rear 5 | MPC X | P-015 |
| rear 6 | Mantis case | P-016 |
| rear 7 | Go_2 case | P-017 |
| rear 8 | open | |
| front 1 to 3 | open | |

**Black Lion PG-X, Jaspers rack** (`black-lion-pg-x-1`)

| Outlet | Load | Link |
|---|---|---|
| rear 1 | right T8V | P-018 |
| rear 2 | Go_1 case | P-019 |
| rear 3 | Go_3 case | P-020 |
| rear 4 to 6 | open | |
| rear 7 | Go_0 case | P-021 |
| rear 8 | left T8V | P-022 |
| front 1 | open | |

**Radial Power-1, on-stage rack** (`radial-power-1-2`)

| Outlet | Load | Link |
|---|---|---|
| front 1 | Yamaha PA-10B adaptor (for the MG10XU) | P-023 |
| front 2 and 3 | to confirm | |
| rear 1 | Take 5 supply | P-024 |
| rear 2 | MicroFreak | P-025 |
| rear 3 | Solar 50 | P-026 |
| rear 4 | open | |
| rear 5 | Hydrasynth | P-027 |
| rear 6 | Lyra-8 | P-028 |
| rear 7 | Pulsar-23 | P-029 |
| rear 8 | SP-404 MKII | P-030 |

## 3. Supplies between the outlet and the device

| Device | Supply | Connector | Link |
|---|---|---|---|
| Go_0 to Go_3 | external supply, model not recorded | barrel DC | P-017, P-019 to P-021 |
| Take 5 | external supply, model not recorded | barrel DC | P-024 |
| MG10XU | Yamaha PA-10B, 18.5 V AC x2, 0.62 A | three-contact locking, AC | P-031 |
| MRCC | included 5 V, 3 A USB-PD supply | USB-C | P-008, not powered yet |
| JU-06A | not recorded; listings say 4 AA batteries or USB bus power, with a micro-B port ⚠ | micro-B | not yet in the data |
| SH-4d | not recorded; listings say a USB-C phone charger or AA batteries ⚠ | USB-C | not yet in the data |
| T10S subwoofer | mains | two-pin IEC, no power switch | P-012 |

The PA-10B label (read 2026-11-15) gives an input of 120 V, 60 Hz, 300 mA and an output marked AC, GND, AC. **That output is alternating current, not DC.** It must never be swapped with a DC supply, and no DC supply must ever go into the MG10XU.

For most of the on-stage synths the device-side supply type is not recorded, so their rows only say what leaves the outlet.

## 4. Rules

- **Eurorack: no hot swapping, ever.** The power sections were not designed for it, and the manufacturers' manuals say the same (owner's rule, from the rack and case plan).
- **The T10S has no power switch.** It sits on a rear outlet of the Jaspers Radial, so the Radial's power switch is its switch.
- **The Yamaha adaptor sits on an unswitched front outlet,** so it stays energized when the on-stage Radial is switched off. The MG10XU has its own switch ⚠ not confirmed.
- **MRCC supply.** The manual says the MRCC may not run correctly below about 4.5 V at its host ports, so a substitute USB-C supply must be at least 5 V and 3 A.
- **Three-contact AC supplies are not interchangeable with any DC supply.** Several look alike on the shelf.

## 5. What the layout means

- **One strip carries the on-stage instruments.** Every synth, drum machine and sampler there hangs off a single Radial. If it trips or is switched off, the whole bench goes dark at once, apart from the Yamaha adaptor on the unswitched front outlet.
- **The Eurorack cases are split across two units.** Go_2 and the Mantis are on the Jaspers Radial, and Go_0, Go_1 and Go_3 are on the PG-X. A dropped unit takes out a pattern of cases, which matters for clocking, since Hermod+, Ground Control and Pamela's are all in Go_0.
- **The monitors are split too.** The sub is on the Radial, the right T8V is on the PG-X at rear 1, and the left T8V is on the PG-X at rear 8.
- **The two Jaspers units share a rack but not an outlet,** so one tripped strip leaves the other running. A shared breaker behind the outlets would still take them together, and that is not recorded.

## 6. Grounding

- The T10S inlet is two-pin and ungrounded, so its ground reference comes through its balanced XLR cables.
- USB-connected synths whose audio goes into a grounded mixer are the usual source of a hum or whine. The planned case is the MicroFreak and the EP-1320 Medieval on the MRCC host ports while their audio goes to the Yamaha. See `midi_and_clock.md`, section 6.
- When a hum appears, the outlet maps in section 2 are how to trace it.

## 7. Spare capacity

- Jaspers Radial: rear 4 and 8, front 1 to 3.
- PG-X: rear 4 to 6, front 1.
- On-stage Radial: rear 4, and front 2 and 3 if they are empty.

## 8. What to record next

- The circuit or breaker behind each of the three wall outlets, and the total load on each. Each unit is listed at 15 A ⚠ retailer listings.
- Every wall supply, its model, and its outlet, starting with the barrel supplies for the Go cases and the Take 5.
- How each on-stage synth takes its power, IEC or supply, and the same for the Mackie, the MPC X, the Mantis and the T8Vs.
- Power for the JU-06A and the SH-4d, which are on no outlet. The earlier note about a JU-08A with mini-USB power is probably this JU-06A, whose listed port is micro-B. Confirm.
- The NiftyCase is on a separate table, off the racks, and is not part of this record.
- Where the MRCC will be powered from, since it is not powered yet.
- The other Black Lion and Furman units the owner thinks exist. They are not in either rack and are not recorded.
