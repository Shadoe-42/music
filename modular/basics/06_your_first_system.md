# Your First System

**What it actually looks like, connected and ready to make sound.**

The previous guides covered voltage, signal types, patching concepts, and voice architecture. This guide brings it into the physical world. Here is a minimal functional system — a case, a few modules, power flowing in, audio flowing out — described as real hardware so you can see the whole picture in one place.

This is the proof of concept. Not the final system. The system that proves the concepts work.

---

## Power: From the Wall to the Module

Power in a Eurorack system travels through four stages. Each stage matters.

```
[Wall Socket]
     │
     │  mains AC
     ▼
[Power Brick]
     │
     │  DC voltage (usually 12V or 16V depending on case)
     ▼
[Case / Internal PSU]
     │
     │  regulated +12V / -12V / +5V rails
     ▼
[Bus Board]
     │
     │  ribbon cable per module
     ▼
[Module Power Header]
```

**Wall socket to power brick:** The brick (wall adapter) converts mains AC to DC. Most compact cases ship with their own brick matched to the PSU. Use the one that came with the case. Substituting a random adapter with the same connector but different voltage will damage your PSU or modules.

**Power brick to case:** The brick's output feeds the case's internal power supply unit (PSU), which regulates the voltage into the three Eurorack rails: +12V, -12V, and +5V. Some cases (like the Intellijel NiftyCase) have the PSU fully integrated — the brick plugs directly into the case and that's the entire external power chain. Others have an internal module PSU that you still cable to a brick.

**Case PSU to bus board:** Inside the case, the PSU connects to a bus board — a PCB running the full width of the case with a row of power headers (sockets). Each header provides all three voltage rails. Modules connect to these headers via ribbon cables.

**Bus board to module:** Each module ships with a ribbon cable. One end plugs into the bus board header; the other end plugs into the module's power header on the back of the PCB.

---

### The Red Stripe Rule

Ribbon cables have a red stripe running down one edge. That stripe marks the **-12V rail**. The module's power header has a notch (key) that aligns the connector so the red stripe faces the correct pin.

**Always orient the ribbon so the red stripe aligns with the -12V pin on the module's header.** The PCB silk screen usually labels the -12V side. When in doubt, check the module's manual before powering on — a reversed ribbon can damage the module, the PSU, or both.

Most modern power headers are keyed (physically notched) so the connector only inserts one way. But some modules use unkeyed headers. On those, the keying doesn't protect you. Check the stripe orientation manually every time on unkeyed connectors.

**Note on multi-colored cables:** Some manufacturers — endorphin.es among them — ship modules with multi-colored ribbon cables rather than the standard gray-with-red-stripe. On these cables, a red or brown wire marks the -12V side. Same rule, different visual. If your cable looks different, identify the -12V wire before connecting.

---

## The Modules

A minimal functional voice needs these building blocks. The specific modules don't matter — any reasonably featured module in each category works. These are representative examples, not prescriptions.

```
┌─────────────────────────────────────────────────────────────────┐
│  Case (e.g., Intellijel NiftyCase or similar compact case)      │
│                                                                  │
│  ┌──────┐ ┌──────┐ ┌────────┐ ┌──────┐ ┌────┐ ┌──────┐ ┌────┐ │
│  │  SEQ │ │ VCO  │ │ FILTER │ │ VCA  │ │ EG │ │  FX  │ │OUT │ │
│  └──────┘ └──────┘ └────────┘ └──────┘ └────┘ └──────┘ └────┘ │
│                                                                  │
│  ═══════════════════ Bus Board ══════════════════════════════   │
└─────────────────────────────────────────────────────────────────┘
```

**Sequencer (SEQ):** Generates the musical pattern. Outputs pitch CV (1V/octave) and gate signals on each step. The pitch CV tells the oscillator what note to play; the gate triggers the envelope. Example: any basic step sequencer, Keystep Pro, or even a MIDI keyboard with a CV interface.

**Oscillator (VCO):** Generates audio voltage at the pitch set by the incoming V/Oct CV. This is the sound source. A sawtooth or square wave gives you harmonic content for the filter to work with. Example: Doepfer A-110-1, Mutable Instruments Plaits, any VCO with V/Oct and audio output.

**Filter (VCF):** Processes the oscillator's audio voltage, shaping its tonal character. Takes audio in, audio out, and a CV input for cutoff modulation. The envelope drives the filter to create that classic opening-brightness effect. Example: Doepfer A-120, any lowpass or multimode filter.

**VCA:** Gates the audio signal using the envelope's control voltage. Without the VCA, the oscillator is heard at full volume constantly. With it, notes have discrete beginnings and endings shaped by the envelope. Example: Doepfer A-130-2, Intellijel Quad VCA, any VCA with CV input.

**Envelope Generator (EG):** Fires a time-based voltage contour when triggered by the sequencer's gate. That contour simultaneously controls the VCA (amplitude shape) and the filter cutoff (timbral shape). One EG can serve both destinations through a passive mult — or use two EGs for independent amplitude and timbral envelopes. Example: Doepfer A-140, Mutable Instruments Stages, any ADSR or AR envelope.

**Effects (FX):** Optional at this stage, but even a simple reverb turns a dry voice into something that exists in a space. Sits after the VCA, before the output. Example: Erica Synths Pico DSP, any small reverb or delay module.

**Output Module (OUT):** Brings modular-level voltage down to line level for external equipment. Non-negotiable — plugging Eurorack directly into a mixer or interface input at full level can damage equipment. Example: Intellijel Outs, ALM Busy Circuits S.B.G., 4ms Listen IO.

---

## The Patch

With the modules in the case and power connected, this is how audio and control voltage flow:

```
[SEQ]
  │
  ├─[G]─ Gate ──────────────────────────────▶ [EG] Trigger In
  │                                               │
  └─[C]─ Pitch CV ──────────────────────────▶ [VCO] V/Oct
                                                  │
                                    [A] Audio Out │
                                                  ▼
                                              [FILTER] Audio In
                                                  │
                               [EG] ──[C]────▶ Filter CV In
                                                  │
                                    [A] Audio Out │
                                                  ▼
                                               [VCA] Audio In
                                                  │
                               [EG] ──[C]────▶ VCA CV In
                                                  │
                                    [A] Audio Out │
                                                  ▼
                                               [FX] In
                                                  │
                                    [A] Audio Out │
                                                  ▼
                                               [OUT] Modular In
                                                  │
                             Line Level Out ───────┘
```

**What each connection does:**

The sequencer's gate output fires the envelope each time a step plays. The sequencer's pitch CV tells the oscillator what note to play. The oscillator produces audio voltage at that pitch. That audio passes through the filter, which shapes the tonal character — brighter when the envelope pushes the cutoff higher, darker as the envelope falls. The filtered audio then passes through the VCA, which opens and closes with the same envelope contour, giving each note a defined attack and release. The output module brings the resulting signal to line level.

The envelope does double duty here — driving both the filter and the VCA from one source. For a more expressive patch, use two separate envelopes with different attack and decay settings: a fast one for the VCA (tight amplitude shape) and a slower one for the filter (longer, more languid brightness movement).

---

## Audio Out: Getting Sound to Your Monitors

The output module produces a line-level signal. From there, two paths:

**Into an audio interface:** Connect the output module's line out to an input on your audio interface (USB interface connected to a laptop works fine). Set the interface input gain to a moderate level, monitor through your DAW or interface's direct monitoring, and listen on headphones or monitors connected to the interface's output. This is the most common setup for recording and production work.

**Into a mixer:** Connect the output module's line out to a channel on your mixer. Set channel gain appropriately (modular is hot — start with gain lower than you think). Route the mixer output to your monitors or powered speakers. This is common for live work or if you already have a mixing workflow.

**Headphones direct:** Some output modules (including the 4ms Listen IO) include headphone outputs with appropriate level attenuation. Useful for quiet practice, checking patches before going to monitors, or mobile work.

---

## What You've Built

This system — sequencer, VCO, filter, VCA, envelope, optional FX, output — is a complete, functional synthesizer voice. It plays melodic patterns, shapes them over time, and sends audio to your monitoring and recording setup. Every concept from the previous guides is present in physical form: voltage sources, voltage processors, voltage routers, timing signals, control signals, audio signals.

From here, the system grows by adding voices, modulation sources, utilities, and effects. But the architecture you just built — sound source, timbral shaper, amplitude control, modulation source, output — never stops being the foundation. Everything else is additional layers on top of this same structure.

---

*This guide is part of a progressive series building foundational modular understanding. Previous guide: 05_signal_types_and_mults.md*
