# Make Noise GTE: Test Plan

Verification plan for `modular/make_noise_gte_guide.md`. Format: `tooling/test_plan_template.md`. Clears the draft status block and every ⚠️ in the guide.

| Field | Value |
|---|---|
| Module | Make Noise GTE |
| Guide | `modular/make_noise_gte_guide.md` (draft, 2026-11-02) |
| Plan type | Verification |
| Firmware | Not applicable (analog) |
| Tested on | Not yet tested; the module ships the week of 2026-11-02 |
| Sources | Make Noise GTE manual, 8 pages; Sound On Sound and Synthtopia announcement coverage |
| Status | Not started |

## Tools

Mordax Data (scope and voltmeter-style readout), multimeter, tape measure, a precise ramp or stepped CV source (Squarp Hermod+ CV lanes or Make Noise Maths in cycle mode), 2hp LFO v2, Make Noise Pressure Points, Marbles, Pamela's PRO Workout, Endorphin.es BLCK_NOIR, Erica Synths Pico DRUM2, a gate-to-LED check (the channel LEDs), a stereo mixer.

## Measurement block (run first)

| ID | Item | How | Result |
|---|---|---|---|
| M1 | Depth with the power cable fitted (guide: 29 mm, from Sound On Sound) | Tape measure | |
| M2 | Current on +12V and -12V (guide: 25 mA and 2 mA, from the manual) | Multimeter in the supply line, with all eight channels cycling | |
| M3 | Power connector polarity marking | Photograph the header; the manual says red stripe to -12 V | |
| M4 | Front-panel photograph | Square on, even light, no hands, no cables. Save as `modular/images/make_noise/gte/front_panel.jpg` and record the source in `images/SOURCES.md`. Read and record the exact printed label of the pulse stream output | |
| M5 | Not applicable | | |

## Test order

M block, then T1 to T8 (the SPAN and SPACE map, which every patch depends on), then T9 to T16 (outputs), then T17 to T19 (TRIGGER), then T20 to T25 (patches). The voltage map first because the manual gives no numbers.

## Tests

| ID | Setup | Prediction (guide) | Pass criterion | Result | Clears |
|---|---|---|---|---|---|
| T1 | Known ramp 0 V to 10 V into SPAN (attenuverter and panel control at their maximum), SPACE at several positions (minimum, noon, maximum), channel LEDs and scope on all eight outputs | One channel is high at a time; as the voltage rises, so does the selected channel | For each SPACE position, record the voltage at which each channel starts and stops | | Draft block item 1; Essential Parameters, SPAN and SPACE |
| T2 | Same ramp, SPACE swept slowly | As SPACE decreases, smaller changes at SPAN produce greater channel spans; at minimum the total span is very small | Total voltage for eight channels against SPACE; minimum value | | Essential Parameters, SPACE |
| T3 | SPAN panel control and attenuverter: ramp in, control at several positions, attenuverter left, center and right | The manual does not say whether they add or scale | Compare the channel map at each combination; record add, scale, or other and the behavior at center | | Draft block item 3; Essential Parameters, SPAN |
| T4 | Voltage above and below the range set by SPACE | Beyond the range, no channel is high | Record which outputs go low above and below, and the ODD and EVEN states | | Draft block item 4; Common Mistakes |
| T5 | SPACE CV with a stepped source at 0 V, 2.5 V, 5 V; ramp at SPAN | SPACE has a CV input that moves the sensitivity | Channel map shifts with the CV; direction and amount; whether the panel control and CV add | | Essential Parameters, SPACE; Patch 4 |
| T6 | Channel outputs 1 to 8: level of the gates with the scope | Eight gates, one high at a time | High level in volts, low level; the rising edge is clean | | Draft block item 2; Key Specifications |
| T7 | Channel LEDs against the outputs | Each output has an LED | LED lit exactly when its output is high; any dimming or partial states recorded | | Draft block item 6 |
| T8 | Overlap: slow ramp through a boundary, scope on two adjacent channels | Only one is high at a time | No overlap and no gap at a boundary (a gap is expected only outside the range) | | Essential Parameters |
| T9 | ODD and EVEN against the channels | ODD is high for channels 1, 3, 5, 7 and EVEN for 2, 4, 6, 8; exactly one is high whenever any channel is active | Confirmed for all eight; both low when none is active | | Essential Parameters, ODD and EVEN |
| T10 | A stepped source that moves by one channel, then by two channels (for example 0 V, 1 V, 3 V of the channel width) | One-channel steps flip ODD and EVEN; two-channel jumps leave the same output high with no new rising edge | Edge behavior at each | | Essential Parameters, ODD and EVEN; Common Mistakes |
| T11 | PULSE STREAM on the scope while a ramp passes through channels | A short pulse every time a new channel is selected, up or down | One pulse per boundary crossing on both slopes; pulse width in milliseconds and level in volts | | Draft block items 2 and 5; Essential Parameters |
| T12 | Speed of the pulse stream: sine LFO at three speeds into SPAN | The stream represents the speed of motion | Pulse count per second proportional to the LFO frequency at a fixed SPACE | | Time Without a Clock |
| T13 | Printed label of the pulse stream jack | The manual's text calls it the GTE output | Record the printed label exactly and update the guide | | Draft block item 5 |
| T14 | Triangle into SPAN, SPACE so that eight channels are used | Hits in order on the rising slope and in reverse on the falling slope | Channel order on both slopes from the LEDs | | Time Without a Clock; Patch 1 |
| T15 | Trigger input at 0.5 V, 2 V and 5 V gates with a ramp at SPAN | Channel changes only on the rising edge of a trigger or gate | Threshold between 0.5 V and 2 V; output updates only on the edge | | Essential Parameters, TRIGGER |
| T16 | TRIGGER cable present, clock stopped | The last channel is held | Output frozen; resumes when the clock restarts | | Common Mistakes |
| T17 | TRIGGER with the pulse stream: ramp through several channels between two clock edges | With a trigger the channel change waits for the edge | Pulse stream fires on the clock edge, not at the boundary crossing; multiple crossings between edges collapse to one change | | Essential Parameters, TRIGGER; Patch 3 |
| T18 | Patch 1 full: 2hp LFO v2 (RANGE left, triangle, about six seconds) into SPAN, channels 1, 4 and 7 into BLCK_NOIR BD, SD and CH TRIG IN | Kick, snare, hat at even intervals on the rise, reverse on the fall | Pattern kick, snare, hat, hat, snare, kick; even spacing; five cables | | Patch 1 |
| T19 | Patch 1 move: ODD into SD TRIG IN | Snare on every odd channel entry, four per slope | Four snare hits per slope; coincidence with kick and hat | | Patch 1 Move the cable |
| T20 | Patch 2 full: Pressure Points Common Pressure into SPAN, PULSE STREAM to CH TRIG IN, Common Gate to BD TRIG IN | Touching fires the kick; pressing, releasing or sliding fires hats at a rate that follows the motion; holding still is silent | Hat rate against rubbing speed; silence at rest; the Pressure Points voltage range at SPAN recorded; four cables | | Patch 2 |
| T21 | Patch 3 full: Marbles X1 into SPAN, ODD to BD, EVEN to SD, PULSE STREAM to CH; free-running | Hits fall wherever X1 steps; some steps are silent when parity repeats | Hit timing follows X1; silent steps match same-parity jumps; X1 span against SPAN recorded; six cables | | Patch 3 |
| T22 | Patch 3 move: Pamela's OUT 1 into TRIGGER | Hits fall on the clock grid | Hits aligned to the clock; unpatching returns to free-running | | Patch 3 Move the cable |
| T23 | Patch 3 SPACE lowered | X1 crosses more channels and gives busier hits | Hit density against SPACE | | Patch 3 |
| T24 | Patch 4 full: Maths Ch1 (cycle, about three seconds each rise and fall) into SPAN, Ch4 (cycle, about thirty seconds) into SPACE CV, ODD to an EG gate on the New Godspeed voice, EVEN to Pico DRUM2 TRIGG | Two voices alternate; density breathes with the second cycle | Alternation heard; density follows Ch4; Maths range against SPAN and SPACE CV recorded; eight cables | | Patch 4 |
| T25 | Maths amplitude and SPAN attenuverter in Patch 4: find the setting where the cycle covers eight channels | The SPAN attenuverter brings Maths into range | Attenuverter position and SPACE position that give full travel | | Patch 4; Draft block item 1 |
| T26 | Channel Index Translation: not testable without a N.U.S.S. module | Described in the manual; wording of the knob positions is ambiguous | Not tested; if a module with a Channel Index output joins the rack, add rows here | | Essential Parameters, Channel Index Translation |

## Failure handling

Follow the template. T1 to T3 are expected to add numbers to the guide that it currently lacks; record them in Key Specifications and Essential Parameters, marked as measurements.

## Closing steps

- [ ] Remove the draft status block from the guide.
- [ ] Remove the ⚠️ markers the results above cleared, and only those.
- [ ] Resolve Depth in Key Specifications to the measured value (M1).
- [ ] Confirm that the front panel image link in the guide points to the photograph from M4, and update the pulse stream label from T13.
- [ ] Commit the guide changes separately from the results in this file.
- [ ] Mark this plan "Complete" with the date.
