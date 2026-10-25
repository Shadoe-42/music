# Error Instruments Kharper: Hardware Questions and Test Protocol

Working checklist for the Kharper guide. Delete this file or fold its results into the guide once the guide is written. Not a guide: it carries no YAML and is not part of the README.

**Status (2026-10-24):** Module not in hand (expected in 3-5 days). No manual, no TINRS or GitHub material found. The only sources are retailer pages and news coverage.

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
| Power from ribbon cable or USB; both work | User, from a video | |
| Four strings, each one voice; two touch strips with an LED bar between them | Retailer pages | |
| Karplus-Strong physical model | Retailer pages | |
| Nine engines: two three-position switches, family (Herring, KoiKarp, Dolphin) and variation (Pond, River, Ocean) | User, from a video; Noisebug | |
| Touch position along the string sets pitch, higher as you move up | User, from a video | |
| Jacks under each string are V/OCT and gate/trigger | User, from a video | |
| Tone knob changes both pitch and timbre | User, from a video (uncertain) | |
| MIDI in plays strings at standard note pitch and holds while the key is held | User, from a video (uncertain) | |
| STRUM gate input plucks all four strings | Retailer pages | |
| Outputs: Control Gate, Control CV, audio L and R | Retailer pages | |
| Global Tone and Decay, each with knob and CV input | Retailer pages | |
| USB port allows firmware and engine uploads | Noisebug | |

**Known tension:** the product page states that the standard firmware does not track 1V/octave, while the per-string jacks are described as tone CV by retailers and as V/OCT by the video. Question B1 settles this first.

---

## A. Physical specifications

| # | Question | How to find out | Result |
|---|---|---|---|
| A1 | Depth, panel back to furthest point, with the ribbon cable fitted | Tape measure | |
| A2 | Current draw on +12V, -12V, +5V | Multimeter in the supply line, or ask the makers | |
| A3 | Power connector type and polarity marking | Visual | |
| A4 | Does USB power work with the module in a case, and does it conflict with the ribbon cable | Try USB alone, ribbon alone, then both | |
| A5 | Panel and control layout, including jack labels exactly as printed | Photograph; compare with the annotated panel image in the repo | |

## B. Pitch (settles the YAML role and Patch 1)

| # | Question | How to find out | Result |
|---|---|---|---|
| B1 | Does the per-string jack track 1V/octave? | Send a sequencer through 0, 1, 2, 3 V; read the spectrum peak in Data against the tuner; note error in cents per octave | |
| B2 | Is the jack labeled V/OCT or CV on the panel? | Read the panel | |
| B3 | Is touch pitch continuous or stepped? | Slide a finger up a strip with the spectrum running; watch for steps | |
| B4 | Pitch range per string, lowest to highest | Touch the bottom and top of each strip; read the spectrum | |
| B5 | Are all four strings tuned the same, or offset? | Touch the same position on each string; compare peaks | |
| B6 | How do touch position and V/OCT combine: added, or does one override the other? | Hold a touch position and change the V/OCT; then the reverse | |
| B7 | What does the tone knob change: pitch, brightness, or both, and how much? | Hold a note; sweep Tone; watch the spectrum peak and harmonic content | |
| B8 | Do MIDI notes set pitch with the same accuracy as the video suggests? | Send notes across several octaves; compare with a tuner | |
| B9 | MIDI behavior: channel, note-off, velocity response, pitch bend | Test each with a keyboard | |
| B10 | Any scale or quantize option? | Check the firmware and panel | |

## C. Playing the strings

| # | Question | How to find out | Result |
|---|---|---|---|
| C1 | What does each of the two touch strips do? | Touch one strip, then the other, then both | |
| C2 | What does the LED bar show? | Play and watch; note states | |
| C3 | Touch response: position only, or also pressure, speed, area | Vary each with a steady finger; watch the scope | |
| C4 | Gate input: trigger or gate, does length matter, any velocity | Send short and long gates; compare the decay | |
| C5 | STRUM: order, timing offset, pitches played | Send a gate to STRUM; read the scope for onset times of the four strings | |
| C6 | Behavior with all four strings ringing; re-pluck of a ringing string | Play while decaying; watch for cutoff or clipping | |
| C7 | Does touch interact with gate-triggered plucks | Pluck by gate, then touch the same string | |

## D. Engines and global controls

| # | Question | How to find out | Result |
|---|---|---|---|
| D1 | Character of each of the nine engines | Same string, same position, all nine; record waveform and spectrum | |
| D2 | Do the two switches change engine at once, or at the next pluck | Change a switch while a string rings | |
| D3 | Global Tone and Decay: range and effect on each family | Sweep each on three engines | |
| D4 | CV ranges for Tone, Decay, and the per-string inputs | Sweep an LFO or slider; find where the response starts and stops | |
| D5 | How per-string tone knobs interact with global Tone | Move one, then the other | |

## E. Outputs

| # | Question | How to find out | Result |
|---|---|---|---|
| E1 | What the Control Gate sends when a strip is touched | Scope on the output | |
| E2 | What the Control CV sends: position, pressure, a fixed value | Scope on the output; slide a finger | |
| E3 | Voltage range of both control outputs | Scope; check the lowest and highest touch | |
| E4 | Audio output level and stereo image of the four strings | Scope both outputs; touch one string at a time | |
| E5 | Is the left output normalled to the right | Patch left only; check right | |

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

## Order of testing

1. A1 to A5 (nothing else depends on them).
2. B1, B2, B3, B4, B7 (pitch decides everything else).
3. E1 to E3 (the control outputs).
4. C and D (playing and engines).
5. F and G (state, firmware, and guide framing).

## What to bring back to the guide

- Key Specifications table: A1 to A3.
- YAML role, functions and behavior tags: B1, G4, G5.
- Quick Start and Patch 1: B1, B3, C4.
- Essential Parameters: B7, D3, D4.
- Common Mistakes: G1 to G3.
- Historical Context: the TINRS and Error Instruments facts under "Known so far", plus anything from the makers.
