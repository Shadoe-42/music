# Studio Wiring, MIDI & Signal Flow Reference

> **Purpose:** A practical, real-world infrastructure blueprint covering physical rack architecture, multi-zone cable bridging, MIDI routing/filtering, gain-staged submixing, and DAW-to-hardware integration. Designed as both a living studio reference and a shareable template for multi-synth hardware setups.

---

## 1. Studio Zone Architecture

The studio is divided into two primary physical zones connected via a protected ~1-meter (3–4 ft) floor umbilical trunk:

### Zone A: Jaspers 4-Tier Rack (Master Control & Main Mix)
* **Eurorack Case:** Master clock and hardware sequencing brains (`Squarp Hermod+`, `Endorphin.es Ground Control`, `ALM Pam's Pro Workout`).
* **Akai MPC X:** Hardware sampler/sequencer and secondary MIDI/CV hub.
* **Mackie 30-Channel Console:** Main studio mixer receiving discrete stereo submixes and direct tracks.

### Zone B: On-Stage 3-Tier Stand + 19" Server Rack (Synth & Drum Fleet)
* **Server Rack (Top-to-Bottom Layout):**
  1. **Top (2U):** Conductive Labs MRCC (MIDI Router Control Center) — placed at eye/hand level with rear DIN access clear.
  2. **Middle (1U–2U):** 1/4" TRS/TS Audio Patch Bay (Half-Normalled).
  3. **Air Gap (1U):** Open/vented space for thermal airflow and electromagnetic isolation between analog audio and AC power.
  4. **Bottom (1U–2U):** Power Distribution / Conditioner — anchors heavy AC power trunks and wall-wart pigtails at the base of the rack.
* **On-Stage Stand Instruments:**
  * ASM Hydrasynth
  * Sequential Take 5
  * Arturia MicroFreak
  * SOMA Pulsar-23
  * SOMA Lyra-8
  * Teenage Engineering EP-1320 Medieval
  * Elta Music Solar 50
  * Roland SP-404 MKII
  * Yamaha Submixer (Stereo summing + Monitor Out sampling bus)

---

## 2. The 1-Meter Floor Bridge (Umbilical Trunk)

A **low-profile, multi-channel rubber floor cord cover** (4–6 ft length, beveled edges, bottom-slit channels) bridges the gap between Zone A and Zone B to prevent trip hazards and chair-caster damage.

* **Channel Separation:** Outbound MIDI data lines and return analog audio lines run in separate channels inside the rubber cover to prevent digital clock/data chatter from bleeding into audio.
* **Service Loops:** A 3–4 inch relaxed S-curve is left under each stand before entering the cord cover so accidental bumps never put shear stress on rear panel jacks.
* **Cable Management:** AC power trunks, analog 1/4" snakes, and MIDI cables are routed in separate suspended bundles using reusable Velcro wraps with 4–6 inch service loops at all connectors.

### Bridge Trunk Cable Manifest (10 ft / 3m Recommended)

| Direction | Signal Type | Cable Spec | Source → Destination |
| :--- | :--- | :--- | :--- |
| **Zone A → Zone B** | Eurorack Master Clock / Seq | **3x** 3.5mm TRS Type A → 5-Pin DIN | Hermod+, Ground Control, Pam's → MRCC Rear DIN Ins 3, 4, 5 |
| **Zone A → Zone B** | MPC X Sequence / Clock | **1x** 5-Pin DIN | MPC X MIDI Out A → MRCC Rear DIN In 6 |
| **Zone B → Zone A** | Keybed / Controller Return | **2–3x** 5-Pin DIN *(Optional)* | MRCC Rear DIN Outs 3, 4, 6 → Hermod+, Ground Control, MPC X |
| **Zone B → Zone A** | Yamaha Stereo Submix | **2x** Balanced 1/4" TRS | Yamaha Main Out L/R (via Patch Bay) → Mackie Discrete Stereo Ch |

---

## 3. Conductive Labs MRCC Port & MIDI Channel Map

### Physical Port Assignments

| MRCC Port | Port Label | Connected Gear | Connection Standard | Assigned MIDI Ch | Role & Routing Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DIN In/Out 1** *(Rear)* | `HYDRA` | ASM Hydrasynth | 5-Pin DIN (In + Out) | **Ch 1** | Primary keybed / poly-AT controller |
| **DIN In/Out 2** *(Rear)* | `TAKE5` | Sequential Take 5 | 5-Pin DIN (In + Out) | **Ch 2** | Receives Clock + Transport for arp/seq |
| **DIN In/Out 3** *(Rear)* | `HERMOD` | Squarp Hermod+ | 3.5mm TRS Type A → DIN | **Ch 9–16** | Master Clock Option 1; multi-track seq |
| **DIN In/Out 4** *(Rear)* | `GNDCTL` | Endorphin.es Ground Control | 3.5mm TRS Type A → DIN | **Ch 9–16** | Master Clock Option 2; multi-track seq |
| **DIN In 5** *(Rear)* | `PAMS` | ALM Pam's Pro Workout | 3.5mm TRS Type A → DIN *(In)* | **Clock Only** | Master Clock Option 3; also clocks CV gear |
| **DIN Out 5** *(Rear)* | `PULSAR` | SOMA Pulsar-23 | 5-Pin DIN *(Out only)* | **Ch 4** | Receives Clock + MIDI-learned drum triggers |
| **DIN In/Out 6** *(Rear)* | `MPCX` | Akai MPC X | 5-Pin DIN (In + Out) | **All / Omni** | Master Clock Option 4 / external sequencer |
| **DIN Out 7–8** *(Rear)* | `OPEN` | *Reserved* | 5-Pin DIN | — | Future expansion / MRCC CV24 expander |
| **USB Host 1** *(Front)* | `MFREAK` | Arturia MicroFreak | Standard USB-B | **Ch 3** | Bi-directional MIDI + clock over USB |
| **USB Host 2** *(Front)* | `MEDV` | TE EP-1320 Medieval | Standard USB-C | **Ch 7** | Bi-directional MIDI + clock over USB |
| **TRS Out A** *(Front)* | `SP404` | Roland SP-404 MKII | 3.5mm TRS *(Set to Type A)* | **Ch 5–6** | Banks A–E (Ch 5) & Banks F–J (Ch 6) |

### Master Channel Allocation Table
* **Ch 1:** ASM Hydrasynth
* **Ch 2:** Sequential Take 5
* **Ch 3:** Arturia MicroFreak
* **Ch 4:** SOMA Pulsar-23 *(BD, Bass, SD, HHT via MIDI Learn)*
* **Ch 5:** Roland SP-404 MKII *(Sample Banks A–E)*
* **Ch 6:** Roland SP-404 MKII *(Sample Banks F–J)*
* **Ch 7:** TE EP-1320 Medieval
* **Ch 8:** *Open (Future Desktop Synth)*
* **Ch 9–16:** Eurorack Modular Voices *(Hermod+ / Ground Control)*
* **Analog CV/Gate:** SOMA Lyra-8 & Elta Solar 50 *(clocked/modulated directly via Pam's Pro Workout or Pulsar-23 converters)*

---

## 4. MRCC Preset Templates & MIDI Hygiene

### Recommended Core Presets
* **`01 HOME` (Default Studio Broadcast):** `HERMOD` sends Clock/Transport to all clock-capable synths (`TAKE5`, `MFREAK`, `SP404`, `MEDV`, `PULSAR`). `HYDRA` routes to all synths across Channels 1–7.
* **`02 GNDCTL CLK`:** Duplicates `01 HOME`, switching Clock/Transport source exclusively to `GNDCTL`.
* **`03 PAMS CLK`:** Duplicates `01 HOME`, switching Clock/Transport source exclusively to `PAMS` for free-jamming across standalone sequencers.
* **`04 MPCX MASTER`:** Sets `MPCX` as master clock and sequencer across Channels 1–16.
* **`05 HYDRA->T5`:** Dedicated performance preset remapping `HYDRA` output directly to `TAKE5` Ch 2 without changing transmit channels on the keyboard.

### Essential MIDI Rules
1. **Single Clock Source:** Enable MIDI Clock/Start/Stop from **only one** active master per preset. Filter out incoming MIDI Clock from all other synths to prevent tempo jitter and double-clocking.
2. **Local Control:** Turn **Local Control = OFF** on the Hydrasynth and Take 5 whenever routing their MIDI out through a sequencer and back into themselves to avoid double-triggered notes and voice stealing.
3. **TRS MIDI Polarity Reference:**
   * **Type A (Tip = Sink/Ch 5, Ring = Source/Ch 4):** SP-404 MKII, EP-1320 Medieval, Hermod+, Ground Control, Pam's MIDI Expander.
   * **Type B (Tip = Source/Ch 4, Ring = Sink/Ch 5):** Arturia MicroFreak *(bypassed cleanly here via MRCC USB Host port)*.

---

## 5. Audio Submixing & Feedback-Free SP-404 Sampling

```text
[On-Stage Synths] ──► [Yamaha Submixer]
                           │
                           ├──► Main Stereo Out L/R ──► [Patch Bay] ──► [Mackie Discrete Stereo Ch]
                           │
                           └──► Monitor Out L/R ──────► [Patch Bay (Half-Normalled)] ──► [SP-404 MKII Line In]
                                                                                                │
                     ┌─────────────────────── (MUTE channel during sampling!) ◄──────────────────┘
                     ▼
             [Yamaha Stereo Ch] ◄── [SP-404 MKII Line Out]
```

* **Discrete Mix Path:** Yamaha Main Outs feed a dedicated stereo channel on the 30-channel Mackie across the floor bridge (`0 dB` unity master fader on the Yamaha, flat EQ on the Mackie channel).
* **Instant Sampling Path:** Yamaha Monitor Outs are **half-normalled** through the 1/4" patch bay directly into the SP-404 MKII `Line In L/R`. Any synth turned up in the Monitor bus can be sampled immediately without repatching.
* **Preventing Resampling Feedback Loops:** Keep the SP-404 MKII's return channel **muted** on the Yamaha submixer while recording into the 404 (or disable `EXT SOURCE` monitoring on the 404), then unmute for playback.

---

## 6. Practical "Missing Manual" Quick-Start Notes

### Making a MacBook Play a MIDI File on Hardware Synths
1. **Connection:** Connect the MacBook via USB to the MRCC's PC USB port (or a USB-MIDI interface routed into MRCC DIN In 6).
2. **macOS Audio MIDI Setup:** Open **Audio MIDI Setup → Window → Show MIDI Studio** to verify the MRCC appears online.
3. **DAW Track Setup:** Create an External MIDI track in your DAW, set the MIDI Output port to the MRCC, and set the **MIDI Channel** to match the target instrument (e.g., **Ch 3** for MicroFreak, **Ch 4** for Pulsar-23).
4. **Instrument-Specific Prep:**
   * **Arturia MicroFreak:** Set *Utility → MIDI → Input Channel* to `3` (or `All`), and *Clock Source* to `USB` or `Auto`.
   * **SOMA Pulsar-23:** Press and hold the **`LRN` (Learn)** button next to the desired drum module (e.g., `BD`), send the target MIDI note from your MacBook/controller, and release `LRN` to bind that pitch/channel permanently.

### Eliminating Ground Loops & USB Noise
* **USB Ground Hum:** Connecting a computer or USB bus-powered device to a synth while its 1/4" audio outs are plugged into a grounded mixer often creates a high-pitched digital whine or 60Hz hum.
* **Fixes:**
  1. Prefer **5-pin DIN MIDI** across zones (DIN is optically isolated by specification and breaks ground paths).
  2. Use **balanced 1/4" TRS cables** for long mixer-to-mixer runs (Yamaha Main Out → Mackie).
  3. Keep wall-wart switching supplies at the bottom of the rack separated from unbalanced TS instrument cables.