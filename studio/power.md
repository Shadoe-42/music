---
title: Power and Grounding
type: detail
publish: private
updated: 2026-11-14
---

# Power and Grounding

How AC and DC power reach the studio's gear. The links are recorded in `data/connections.csv` (the `P-` rows), and this document is a view of them. When they disagree, the CSV is right. Power inside the Eurorack cases is its own subject: see the modular documentation, and the power maps `power_distro_sections_1026.md` and the rack and case plan in `~/claude/`.

## 1. The chain

```text
Wall outlets ──► Black Lion conditioner, Jaspers rack   ──► the Jaspers rack
Wall outlets ──► Black Lion conditioner, on-stage rack  ──► the on-stage rack
```

Power runs to both racks and is in place (P-001, P-002). The conditioner models and counts are not recorded, and neither is which outlet feeds which device.

## 2. Devices with their own supply

| Device | Supply | Connector | Link |
|---|---|---|---|
| Go_0 to Go_3 | external supply | barrel DC | P-003 to P-006 |
| Take 5 | external supply | barrel DC | P-007 |
| MRCC | included 5 V, 3 A USB-PD supply | USB-C | P-008 |
| JU-08A | to confirm | mini-USB | not yet in the data |
| T10S subwoofer | mains | two-pin IEC, no power switch | not yet in the data |

Other devices that use mini-USB power are not yet identified. Each supply that exists should become a row once its source outlet is known.

## 3. Rules

- **Eurorack: no hot swapping, ever.** The power sections were not designed for it, and the manufacturers' manuals say the same (owner's rule, from the rack and case plan).
- **The T10S has no power switch**, so it is switched at the conditioner or the outlet.
- **MRCC supply.** The manual says the MRCC may not run correctly below about 4.5 V at its host ports, so a substitute USB-C supply must be at least 5 V and 3 A.

## 4. Grounding

- The T10S inlet is two-pin and ungrounded, so its ground reference comes through its balanced XLR cables.
- USB-connected synths whose audio goes into a grounded mixer are the usual source of a hum or whine. The planned case is the MicroFreak and the EP-1320 Medieval on the MRCC host ports while their audio goes to the Yamaha. See `midi_and_clock.md`, section 6.
- When a hum appears, the outlet map in section 5 is how to trace it, so it is worth recording.

## 5. What to record next

- Conditioner models and counts, per rack.
- Which device sits on which outlet, as `P-` rows with the outlet as the source port.
- The circuit or breaker behind each conditioner, and the total load on it.
- Every wall supply and its source outlet, especially the barrel supplies for the Go cases and the Take 5.
- Whether the Mackie, the Yamaha, the MPC X and the other mains devices are on the conditioners.
- Which devices take mini-USB power, beyond the JU-08A.
- The first draft puts wall supplies at the bottom of the on-stage rack, away from unbalanced cables. ⚠ Confirm against the rack as built.
