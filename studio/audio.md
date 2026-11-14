---
title: Audio and Monitoring
type: detail
publish: private
updated: 2026-11-14
---

# Audio and Monitoring

How audio moves from the sources to the monitors. The cables are recorded in `data/connections.csv` (the `A-` rows), and the tables below are views of it. When they disagree, the CSV is right. MIDI and clock are in `midi_and_clock.md`.

## 1. The path at a glance

```text
Cockpit2   ──► Mackie ch 3 (hard left) and ch 4 (hard right)
Listen I/O ──► Mackie ch 28 (stereo)
Mixup      ──► Mackie ch 29 (stereo)
Yamaha     ──► Mackie, two channels in the low 20s, hard left and right   [planned]

Mackie main L/R ──XLR──► T10S sub ──XLR (high-passed outputs)──► T8V left, T8V right
```

Everything in the first four lines and the monitor chain is as built. The Yamaha is not connected yet.

## 2. Mackie channel map

| Channel | Source | Link | Mode | Status |
|---|---|---|---|---|
| 3 | Cockpit2, left | A-001 | mono, panned hard left | wired |
| 4 | Cockpit2, right | A-002 | mono, panned hard right | wired |
| 28 | Listen I/O | A-003 | stereo channel | wired |
| 29 | Mixup | A-004 | stereo channel | wired |
| low 20s, left | Yamaha main out L | A-009 | mono, panned hard left | planned |
| low 20s, right | Yamaha main out R | A-010 | mono, panned hard right | planned |

No other Mackie channel is recorded yet. The Yamaha channels are not chosen, and the owner noted that the Yamaha goes on a mono pair, because the two stereo channels at 28 and 29 are already taken.

## 3. Monitor chain

The Mackie main outputs feed the T10S subwoofer over XLR, and the T10S feeds the two T8V monitors over XLR (A-005 to A-008). The sub sits first in the chain on purpose. It has balanced XLR and unbalanced RCA inputs and outputs, and its outputs are high-pass filtered so the monitors receive only the part of the signal above the crossover, with the crossover set to 80 Hz, 120 Hz or bypass (Adam Audio product page; Sound On Sound review, June 2020). Adam also designs the T10S to match the T5V, T7V and T8V monitors.

Settings to record once someone is at the back panel:

- Crossover: 80 Hz, 120 Hz or bypass ⚠
- Phase: 0 or 180 degrees ⚠
- Input sensitivity: +4 dBu or -10 dBV ⚠
- Whether the footswitch bypass input is used. Bypass removes the sub and its high-pass filter, so the monitors play full range ⚠

Power note for the power doc: the T10S has a two-pin IEC inlet and no power switch of its own (Sound On Sound), so its power is switched at the conditioner or the outlet.

## 4. Eurorack mixers

The Cockpit2, Listen I/O and Mixup are the points where the modular's audio leaves the cases. Their makers, output connectors, balanced or unbalanced outputs and level are not yet recorded, so the signal and connector fields on A-001 to A-004 are blank. Fill them in when each run is traced.

## 5. Yamaha submixer, planned

From the first draft, none of it tested:

- The on-stage synths sum into the Yamaha. Its main outputs go to the Mackie.
- Its monitor outputs reach the SP-404 MKII line inputs, so any synth turned up on the monitor bus can be sampled without repatching.
- While sampling, the SP-404's return channel on the Yamaha stays muted, or its external monitoring is off, so the sampler does not resample itself.

⚠ The Yamaha model is not recorded, and the monitor bus behavior depends on it. The first draft also routes these links through the patch bay, which this document does not yet confirm. The planned Mackie inputs follow the owner's later statement, not the draft.

## 6. Patch bay

The first draft describes a half-normalled 1/4 inch patch bay in the on-stage rack, with the Yamaha main and monitor outputs patched through it. No point list exists. Record, for each jack pair, what is normalled to what, and whether the normalling is full, half or none.

## 7. Gain staging

Not yet documented. The first draft says only that the Yamaha master sits at unity and the Mackie channel is flat. Once the runs are in, record at each hop the source output level, the input trim and the fader position, starting with the Eurorack mixers, which will vary most.

## 8. Grounding

See the ground path note in `midi_and_clock.md`, section 6. The long run across the bridge should be balanced, and the monitor runs are already XLR.

## 9. Open items

- Makers, outputs and levels of the Cockpit2, Listen I/O and Mixup.
- Mackie model and which channels carry what beyond the five recorded.
- How audio gets from the Mackie to the computer and the DAW. Nothing is recorded yet.
- T10S settings, as in section 3.
- Yamaha model, its channels on the Mackie, and the patch bay point list.
- Where the headphone connections go. Some 3.5 mm TRS runs exist and are not recorded.
