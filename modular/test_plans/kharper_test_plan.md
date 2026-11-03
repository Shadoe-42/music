# Error Instruments Kharper: Test Plan

Discovery plan for the future Kharper guide. Format: `tooling/test_plan_template.md`. There is no manual, so each row is a question and the result becomes the source for the guide. When the guide is drafted, the answers become predictions and this file converts to a verification plan; unanswered rows stay as discovery rows. Not a guide: no YAML, not in the README, not audited.

| Field | Value |
|---|---|
| Module | Error Instruments Kharper |
| Guide | none yet |
| Plan type | Discovery |
| Firmware | Not yet read (F2) |
| Unit | Revision and batch or serial: not yet read. Printed marks, board silkscreen and packaging to be photographed. Purchased from: not recorded. Date received: not recorded |
| Tested on | 2026-11-02 (section A only so far) |
| Sources | Retailer pages, Synth Anatomy, Paul Tas demo transcript, the user's recollection of a video |
| Status | In progress |

**Measurement block:** section A is this plan's measurement block. M1 is A1, M2 is A2, M3 is A3, M4 is A5, and M5 is F2. Unit identity (the Unit row in the header table) is recorded alongside the measurement block, because with so few units in circulation a later difference between two units has to be traceable to a revision or batch and not read as a mistake.

**Status (2026-11-02):** Module in hand. Physical measurements and the power checks are recorded below (section A and the Known table); everything else is still untested. No manual, no TINRS or GitHub material found. The only other sources are retailer pages and news coverage.

**Sources:** retailer pages (Signal Sounds, ModularGrid, Noisebug), Synth Anatomy, the user's recollection of a video, and the transcript of Paul Tas's pre-release demo video for Error Instruments (auto-captioned; captions read as Kharper, Grids, Stijn, Karplus-Strong, KoiKarp).

**Tools:** Mordax Data (scope, spectrum), tape measure, multimeter, tuner, a sequencer with a 1V/octave output, a MIDI keyboard or source, a stereo mixer.

**Marking:** Items under "Known so far" are not yet verified on the hardware. Verified items get a date and a result when tested.

---

## Known so far

| Fact | Source | Verified |
|---|---|---|
| Collaboration between This Is Not Rocket Science (TINRS) and Error Instruments, both Dutch | Synth Anatomy | |
| Announced at Superbooth 2025; available July 2025 in limited quantity at 350 € incl. VAT | Synth Anatomy | |
| 18 HP | ModularGrid, Signal Sounds | |
| Duo is the module in a case; Error Instruments sells a case, or a file is available to print one | User, from a video | |
| Power from ribbon cable or USB; both work | User, from a video | 2026-11-02: USB alone powers the module without the ribbon; the ribbon (power connector) also works. USB is not recommended in a traditional Eurorack case |
| Four strings, each one voice; two touch strips with an LED bar between them | Retailer pages | |
| Karplus-Strong physical model | Retailer pages | |
| Nine engines: two three-position switches, family (Herring, KoiKarp, Dolphin) and variation (Pond, River, Ocean) | User, from a video; Noisebug | |
| Touch position along the string sets pitch, higher as you move up | User, from a video | |
| Jacks under each string are V/OCT and gate/trigger | User, from a video | 2026-11-02: panel labeling confirmed as V/OCT and gate inputs. Tracking accuracy still open (B1) |
| Tone knob changes both pitch and timbre | User, from a video (uncertain) | |
| MIDI in plays strings at standard note pitch and holds while the key is held | User, from a video (uncertain) | |
| STRUM gate input plucks all four strings | Retailer pages | |
| Outputs: Control Gate, Control CV, audio L and R | Retailer pages | |
| Global Tone and Decay, each with knob and CV input | Retailer pages | |
| USB port allows firmware and engine uploads | Noisebug | |
| Demo is pre-release ("going to be released soon"); the control voltage, MIDI and audio parts were described as done | Paul Tas demo transcript | |
| Demo was played with Mutable Instruments Grids triggers; the speaker notes the touch interface is the main way to play | Paul Tas demo transcript | |
| Worked on with Stijn (TINRS) | Paul Tas demo transcript; Synth Anatomy | |
| Nine algorithms; some include a reverb and "more different functions" | Paul Tas demo transcript | |
| KoiKarp family is the more percussive one; its first variation is described as a "tublap" and its last as able to sound like a piano | Paul Tas demo transcript; Noisebug | |
| One engine is the classic Karplus-Strong sound "from Rings and Elements" (the speaker's words; engine not identified) | Paul Tas demo transcript | |
| Herring with Ocean gives a low sub sound | Paul Tas demo transcript | |

**Known tension:** the product page states that the standard firmware does not track 1V/octave, while the per-string jacks are described as tone CV by retailers and as V/OCT by the video. The panel labeling is now confirmed as V/OCT (2026-11-02); whether the jack actually tracks 1V/octave is still settled by B1.

---

## A. Physical specifications

| # | Question | How to find out | Result |
|---|---|---|---|
| A1 | Depth, panel back to furthest point, with the ribbon cable fitted | Tape measure | 2026-11-02: 32 mm, measured with the power connector fitted |
| A2 | Current draw on +12V, -12V, +5V | Multimeter in the supply line, or ask the makers | 2026-11-02: +12V 140 mA, measured via the power connector. +5V: none, the module has no 5V rail. -12V: not yet measured |
| A3 | Power connector type and polarity marking | Visual | 2026-11-02: ribbon power connector, red stripe down with the module held in its normal orientation. Board marking not yet photographed |
| A4 | Does USB power work with the module in a case, and does it conflict with the ribbon cable | Try USB alone, ribbon alone, then both | 2026-11-02: USB alone powers it; the ribbon works. Not tested together. USB power is not recommended in a traditional Eurorack case |
| A5 | Panel and control layout, including jack labels exactly as printed | Photograph; compare with the annotated panel image in the repo | |

## B. Pitch (settles the YAML role and Patch 1)

| # | Question | How to find out | Prediction (source) | Result |
|---|---|---|---|---|
| B1 | Does the per-string jack track 1V/octave? | Send a sequencer through 0, 1, 2, 3 V; read the spectrum peak in Data against the tuner; note error in cents per octave | Panel says V/OCT; product page says the standard firmware does not track 1V/octave (sources conflict) | |
| B2 | Is the jack labeled V/OCT or CV on the panel? | Read the panel |  | 2026-11-02: V/OCT and gate inputs, as expected |
| B3 | Is touch pitch continuous or stepped? | Slide a finger up a strip with the spectrum running; watch for steps | Pitch rises as the finger moves up the strip (user, video) | |
| B4 | Pitch range per string, lowest to highest | Touch the bottom and top of each strip; read the spectrum |  | |
| B5 | Are all four strings tuned the same, or offset? | Touch the same position on each string; compare peaks |  | |
| B6 | How do touch position and V/OCT combine: added, or does one override the other? | Hold a touch position and change the V/OCT; then the reverse |  | |
| B7 | What does the tone knob change: pitch, brightness, or both, and how much? | Hold a note; sweep Tone; watch the spectrum peak and harmonic content | Tone changes both pitch and timbre (user, video, uncertain) | |
| B8 | Do MIDI notes set pitch with the same accuracy as the video suggests? | Send notes across several octaves; compare with a tuner | MIDI plays strings at standard note pitch and holds while the key is held (user, video, uncertain) | |
| B9 | MIDI behavior: channel, note-off, velocity response, pitch bend | Test each with a keyboard |  | |
| B10 | Any scale or quantize option? | Check the firmware and panel |  | |

## C. Playing the strings

| # | Question | How to find out | Prediction (source) | Result |
|---|---|---|---|---|
| C1 | What does each of the two touch strips do? | Touch one strip, then the other, then both |  | |
| C2 | What does the LED bar show? | Play and watch; note states |  | |
| C3 | Touch response: position only, or also pressure, speed, area | Vary each with a steady finger; watch the scope |  | |
| C4 | Gate input: trigger or gate, does length matter, any velocity | Send short and long gates; compare the decay |  | |
| C5 | STRUM: order, timing offset, pitches played | Send a gate to STRUM; read the scope for onset times of the four strings | STRUM gate plucks all four strings (retailer pages) | |
| C6 | Behavior with all four strings ringing; re-pluck of a ringing string | Play while decaying; watch for cutoff or clipping |  | |
| C7 | Does touch interact with gate-triggered plucks | Pluck by gate, then touch the same string |  | |

## D. Engines and global controls

| # | Question | How to find out | Prediction (source) | Result |
|---|---|---|---|---|
| D1 | Character of each of the nine engines | Same string, same position, all nine; record waveform and spectrum | Nine engines: three families by three variations (user, video, Noisebug) | |
| D2 | Do the two switches change engine at once, or at the next pluck | Change a switch while a string rings |  | |
| D3 | Global Tone and Decay: range and effect on each family | Sweep each on three engines | Global Tone and Decay each have a knob and a CV input (retailer pages) | |
| D4 | CV ranges for Tone, Decay, and the per-string inputs | Sweep an LFO or slider; find where the response starts and stops |  | |
| D5 | How per-string tone knobs interact with global Tone | Move one, then the other |  | |
| D6 | Which engines include a reverb, and what do the "more different functions" the demo mentions control | Play each of the nine; listen for a tail beyond the string decay; check whether Tone or Decay changes it | Some engines include a reverb (Paul Tas demo) | |
| D7 | Which engine is the classic Karplus-Strong string, and how does it compare with Mutable Instruments Rings (the only comparison available; Elements is not in the rack) | Play all nine; compare the spectrum of each with Rings in its string mode and with a plain Karplus-Strong decay | One engine is the classic Karplus-Strong sound (Paul Tas demo) | |
| D8 | Does Herring with Ocean give the low sub sound described | Select it; read the spectrum | Herring with Ocean gives a low sub sound (Paul Tas demo) | |
| D9 | Does the last KoiKarp variation sound like a piano; what is the first variation's "tublap" character | Select each; record waveform and spectrum | KoiKarp is the percussive family; its last variation can sound like a piano and its first is a "tublap" (demo, Noisebug) | |
| D10 | Does the shipping unit match the pre-release demo, in firmware and in sound | Compare firmware version (F2) and the demo recording | Control voltage, MIDI and audio parts were described as done in the demo | |

## E. Outputs

| # | Question | How to find out | Prediction (source) | Result |
|---|---|---|---|---|
| E1 | What the Control Gate sends when a strip is touched | Scope on the output |  | |
| E2 | What the Control CV sends: position, pressure, a fixed value | Scope on the output; slide a finger |  | |
| E3 | Voltage range of both control outputs | Scope; check the lowest and highest touch |  | |
| E4 | Audio output level and stereo image of the four strings | Scope both outputs; touch one string at a time |  | |
| E5 | Is the left output normalled to the right | Patch left only; check right |  | |

## F. State, firmware, USB

| # | Question | How to find out | Result |
|---|---|---|---|
| F1 | What survives a power cycle: engine switches, knobs, anything else | Set, power off, power on | |
| F2 | Firmware version shipped and how to check it | Boot indication or USB; ask the makers | |
| F3 | Update procedure over USB | Documentation or the makers | |
| F4 | Does USB also carry MIDI | Connect to a computer and look for a MIDI device | |

## G. For the guide itself

| # | Question | How to find out | Result |
|---|---|---|---|
| G1 | First-hour surprises (these become Common Mistakes) | Keep notes while learning it | |
| G2 | Behavior at extremes: maximum decay, strong CV on tone, all strings struck together | Push each while watching the scope | |
| G3 | Sensitivity of the touch strips: dry or wet fingers, noise from nearby modules | Test with and without other modules powered | |
| G4 | Best YAML role: SOURCE, EVENT_VOICE, or both; do `harp` or `pluck` terms exist in the controlled vocabulary | Compare against `yaml_spec_v2.md` after the behavior is known | |
| G5 | Which patch conventions apply: the sustained-SOURCE First Voice, or an EVENT_VOICE one | Decide after B1 and C4 | |
| G6 | Pairings that work in practice | Try with Marbles, a sequencer, an envelope and VCA, and an effects module | |

---

## Notes for Historical Context

- Collaboration of Error Instruments and TINRS, both Dutch, who had already built modules together; Stijn and Priscilla are named at TINRS (Synth Anatomy), and Paul Tas presents it for Error Instruments.
- Announced at Superbooth 2025 and sold from July 2025 in limited quantity.
- The maker compares one engine to the Karplus-Strong sound of Mutable Instruments Rings and Elements. In the guide this stays the maker's claim, attributed to the demo: Elements is not in the rack, so that half cannot be verified, and only the Rings comparison (D7) can be tested. The Rings guide in this corpus mentions Karplus-Strong; there is no Elements guide and no Grids guide, so any cross-reference stays within what the Rings guide contains.
- The demo triggered the strings with Mutable Instruments Grids, which is not in the rack. For our tests use a sequencer, Marbles t outputs, or Pamela's PRO Workout; the pluck inputs only need gates.
- Karplus-Strong string synthesis itself needs a sourced paragraph (Wikipedia and an original source) before the guide is written; do not write it from memory.

---

## Order of testing

Section A is the measurement block and runs first.

1. A1 to A5 (nothing else depends on them).
2. B1, B2, B3, B4, B7 (pitch decides everything else).
3. E1 to E3 (the control outputs).
4. C and D (playing and engines, including D6 to D10).
5. F and G (state, firmware, and guide framing).

## What to bring back to the guide

- Key Specifications table: A1 to A3.
- YAML role, functions and behavior tags: B1, G4, G5.
- Quick Start and Patch 1: B1, B3, C4.
- Essential Parameters: B7, D3, D4.
- Common Mistakes: G1 to G3.
- Historical Context: the TINRS and Error Instruments facts under "Known so far", plus anything from the makers.

## Failure handling

Follow the template. The "Known so far" table holds claims that are not yet verified; a result that contradicts a claim there replaces it, with the date, and the source row is marked as contradicted. In particular B1 settles the standing conflict between the product page and the panel labeling.

## Closing steps

- [ ] Draft the guide from the results above, as a draft with its own status block, listing every row still open.
- [ ] Convert answered rows into predictions in a verification plan; keep unanswered rows as discovery rows.
- [ ] Mark this plan "Complete" with the date once every row has a result, or note the rows deliberately left open.
