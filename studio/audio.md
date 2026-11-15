---
title: Audio and Monitoring
type: detail
publish: private
updated: 2026-11-15
---

# Audio and Monitoring

How audio moves from the sources to the monitors. The cables are recorded in `data/connections.csv` (the `A-` rows), and the tables below are views of it. When they disagree, the CSV is right. MIDI and clock are in `midi_and_clock.md`.

## 1. The path at a glance

```text
Cockpit 2  ──► Mackie ch 3 (hard left) and ch 4 (hard right)
Listen IO  ──► Mackie ch 28 (stereo)
Mixup      ──► Mackie ch 29 (stereo)
Hydrasynth ──► Yamaha MG10XU ch 9 and 10   (A-011, A-012, wired)
Yamaha     ──► Mackie, two channels in the low 20s, hard left and right   [planned]

Mackie main L/R ──XLR──► T10S sub ──XLR (high-passed outputs)──► T8V left, T8V right
```

Everything above the Yamaha-to-Mackie line, and the monitor chain, is as built. The Hydrasynth is the only source connected to the Yamaha, and the Yamaha is not connected to the Mackie yet, so the Hydrasynth is not reaching the monitors.

## 2. Mackie channel map

| Channel | Source | Link | Mode | Status |
|---|---|---|---|---|
| 3 | Cockpit 2, left | A-001 | mono, panned hard left | wired |
| 4 | Cockpit 2, right | A-002 | mono, panned hard right | wired |
| 28 | Listen IO | A-003 | stereo channel | wired |
| 29 | Mixup | A-004 | stereo channel | wired |
| low 20s, left | Yamaha MG10XU main out L | A-009 | mono, panned hard left | planned |
| low 20s, right | Yamaha MG10XU main out R | A-010 | mono, panned hard right | planned |

No other Mackie channel is recorded yet. The Yamaha channels are not chosen, and the owner noted that the Yamaha goes on a mono pair, because the two stereo channels at 28 and 29 are already taken.

## 3. Monitor chain

The Mackie main outputs feed the T10S subwoofer over XLR, and the T10S feeds the two T8V monitors over XLR (A-005 to A-008). The sub sits first in the chain on purpose. It has balanced XLR and unbalanced RCA inputs and outputs, and its outputs are high-pass filtered so the monitors receive only the part of the signal above the crossover, with the crossover set to 80 Hz, 120 Hz or bypass (Adam Audio product page; Sound On Sound review, June 2020). Adam also designs the T10S to match the T5V, T7V and T8V monitors.

Settings to record once someone is at the back panel:

- Crossover: 80 Hz (stated by the owner, 2026-11-14)
- Phase, 0 or 180 degrees: not recorded ⚠
- Input sensitivity: the switch is in the vertical position; which level that is, +4 dBu or -10 dBV, is not recorded ⚠
- Footswitch bypass: not installed and never used. Bypass would remove the sub and its high-pass filter, so the monitors would play full range

Power note for the power doc: the T10S has a two-pin IEC inlet and no power switch of its own (Sound On Sound), so its power is switched at the conditioner or the outlet.

## 4. Eurorack mixers

The Cockpit 2 (Endorphin.es, in case Go_2), Listen IO (4ms, in Go_3) and Mixup (Intellijel, in Go_1) are the points where the modular's audio leaves the cases, so the three runs to the Mackie start in three different cases. Their output connectors, balanced or unbalanced outputs and level are not yet recorded, so the signal and connector fields on A-001 to A-004 are blank. Fill them in when each run is traced.

## 5. Yamaha MG10XU

The model was read off the unit on 2026-11-15 (basis `observed`). It sits in the on-stage zone and is powered by a Yamaha PA-10B adaptor, which gives alternating current and not DC (see `power.md`). The Hydrasynth main outputs are the only audio connected to it: left to channel 9 and right to channel 10, on 1/4 inch TRS cables, red for right and black for left (A-011, A-012). Whether the Hydrasynth outputs are balanced is not recorded ⚠. The MG10XU also has a USB audio interface ⚠ not checked against the manual, which would be a separate path from the Mackie feed if it is ever used.

The plan below is from the first draft, none of it tested:

- The on-stage synths sum into the Yamaha. Its main outputs go to the Mackie.
- Its monitor outputs reach the SP-404 MKII line inputs, so any synth turned up on the monitor bus can be sampled without repatching.
- While sampling, the SP-404's return channel on the Yamaha stays muted, or its external monitoring is off, so the sampler does not resample itself.

⚠ The monitor bus behavior depends on the MG10XU manual, which has not been checked. The first draft also routes these links through the patch bay, which this document does not yet confirm. The planned Mackie inputs follow the owner's later statement, not the draft.

## 6. Patch bay

The patch bay is a 96-port 1U unit at the top of the Jaspers rack stack (owner, 2026-11-15), not in the on-stage rack as the first draft says. ⚠ 96 points in 1U usually means bantam (TT) jacks, not 1/4 inch, so the jack type needs checking. The first draft describes half-normalling, with the Yamaha main and monitor outputs patched through it. No point list exists. Record, for each jack pair, what is normalled to what, and whether the normalling is full, half or none.

## 7. Gain staging

Not yet documented. The first draft says only that the Yamaha master sits at unity and the Mackie channel is flat. Once the runs are in, record at each hop the source output level, the input trim and the fader position, starting with the Eurorack mixers, which will vary most.

## 8. Grounding

See the ground path note in `midi_and_clock.md`, section 6. The long run across the bridge should be balanced, and the monitor runs are already XLR.

## 9. Open items

- Output connectors, balance and level of the Cockpit 2, Listen IO and Mixup.
- Mackie model and which channels carry what beyond the five recorded.
- How audio gets from the Mackie to the computer and the DAW. Nothing is recorded yet.
- T10S phase and sensitivity, as in section 3.
- The Yamaha channels on the Mackie, the patch bay model and jack type, and its point list.
- The Magnatone Baby M-80 head is connected to a Marshall Studio JTM 2x12 cabinet and is not integrated with the Mackie or the modular. The speaker cable type, the cabinet impedance and the head's impedance setting are not recorded.
- Where the headphone connections go. Some 3.5 mm TRS runs exist and are not recorded.
