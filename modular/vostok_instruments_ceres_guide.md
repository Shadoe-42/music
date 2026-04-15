---
title: Vostok Instruments Ceres
manufacturer: Vostok Instruments
primary_role: AMPLIFIER
secondary_roles: [ROUTER]
hp: 10
---

# Vostok Instruments Ceres Guide

**Six-Channel Linear VCA and Mixer**  
**Manufacturer:** Vostok Instruments  
**Format:** Eurorack  
**Width:** 10HP | **Depth:** 30mm | **Power:** +50mA / -50mA  

![Vostok Instruments Ceres](https://github.com/Shadoe-42/music/raw/main/modular/images/vostok_instruments/ceres/front_panel.jpg)  
*10HP six-channel linear VCA array with daisy-chained inputs, automatic mix output, LED level indicators per channel, and 3360 chip core. Six channels that function as one system.*

---

## Quick Start

**What you need:** An audio source, an envelope or LFO, and a mixer or destination.

**Minimum viable patch (single channel):**
1. Patch your audio source OUT ---[A]---> Ceres ch1 IN
2. Patch your envelope OUT ---[C]---> Ceres ch1 CV
3. Patch Ceres ch6 MIX OUT ---[A]---> your mixer
4. Set ch1 LEVEL fully clockwise
5. Trigger the envelope; ch1 opens, and the signal appears at the MIX output

**Key Specifications:**

| Spec | Value |
|------|-------|
| Width | 10HP |
| Depth | 30mm |
| Power | +50mA / -50mA |
| Channels | 6 (identical) |
| Response | Linear only |
| Unity gain CV | 5V |
| Max CV | Clipped at 5V |
| Input impedance | 100kΩ |
| Output impedance | 1kΩ |
| VCA chip | 3360 (OTA) |
| Input normalling | Daisy-chained ch1 → ch6 |
| Output mix | All channels sum to ch6 MIX |

---

## The Architecture: Chain and Mix

Ceres is not six separate VCAs. It is six VCAs wired into a system with two architectural decisions that define how it behaves.

**Daisy-chained inputs:** By default, the signal present at ch1 IN feeds forward to ch2 IN, ch3 IN, and so on down to ch6. If nothing is patched into ch2 IN, ch2 receives whatever is at ch1 IN. Breaking the chain at any point requires patching a cable into that channel's IN jack. This means a single audio source patched into ch1 automatically appears at all six channels without any additional cables.

**Automatic mix output:** By default, all six channels sum together at ch6 MIX OUT. If you patch a cable into a channel's OUT jack, that channel is extracted from the mix and routed independently; it no longer contributes to the ch6 MIX. Channels with nothing patched into their OUT remain in the mix.

These two behaviors together produce a system where the default state is: one source, six independent CV inputs, one summed output. Each channel receives the same audio but can be opened or closed by its own CV signal and LEVEL control. The mix output combines the results.

The practical consequence: applying six different CV shapes to one audio source and collecting the sum is a standard Ceres operation that requires only one audio source cable, six CV cables, and one output cable.

---

## Essential Parameters

### IN (Signal Input)

Audio or CV signal input. If no cable is patched here, this channel receives the signal from the previous channel (daisy-chain normalling). Patching a cable into IN breaks the chain at this point; this channel and all following channels now receive only what is explicitly patched into them.

### CV (Control Voltage Input)

Unipolar (positive) signal expected here. Unity gain at 5V. Signals above 5V are clipped to 5V. Ceres expects 0-5V envelopes; if your envelope outputs 0-10V, the LEVEL control can attenuate it. Negative CV voltages will close the VCA (below zero = no output).

### LEVEL

When CV is present: LEVEL attenuates the CV signal before it reaches the VCA circuit. Turning LEVEL down reduces how much CV opens the channel. At the fully counterclockwise position, no CV reaches the VCA regardless of the CV signal level.

When no CV is present: LEVEL acts as a manual volume control. The channel reaches unity gain at the fully clockwise position. This makes Ceres usable as a six-channel mixer without any CV patched.

### OUT

Signal output for this channel. If nothing is patched into OUT, this channel's output is included in the ch6 MIX. Patching a cable into OUT routes this channel independently and removes it from the mix.

### MIX (ch6 OUT/MIX)

The final output of the system. By default, all six channels contribute to this mix. Channels extracted via their individual OUT jacks are absent from the MIX. The mix is a simple sum; no level compensation for the number of active channels.

### LED Indicator

Shows the amplitude of the output signal for each channel in real time. Useful for verifying that a channel is receiving CV and opening correctly, and for visual monitoring of relative channel levels during a performance.

---

## Historical Context

The 3360 chip at Ceres's core is the SSI2164 (and its predecessor, the V2164), a quad VCA integrated circuit originally developed by Doug Curtis. The same chip or its direct ancestors have been used in the Roland JX-3P, Oberheim Matrix-12, Ensoniq ESQ-1, and many other instruments of the 1980s and beyond. Curtis's OTA (operational transconductance amplifier) designs became a standard for low-noise, low-distortion voltage-controlled amplification in professional audio and synthesis applications. Choosing the 3360 for Ceres reflects a design priority for audio quality: it is a proven, characterless VCA core that does not impose coloration on the signal.

Vostok Instruments is a small Spanish manufacturer whose design philosophy emphasizes functional clarity and careful construction. Ceres, as described in the manual, was designed to solve a specific problem the designer encountered repeatedly: running out of VCA channels. The response was not a minimal dual VCA but a six-channel system with deliberate architecture around the chain and mix behavior. The "you never have enough VCAs" maxim from the manual is accurate; six channels addressed the shortage while the daisy-chain and mix bus added creative utility beyond simple headcount.

---

## Why This Excels

Six VCA channels with daisy-chain normalling and a passive mix bus in 10HP addresses both the infrastructure shortage problem and the creative modulation problem simultaneously. As a pure channel count solution, Ceres gives more VCAs per HP than almost any alternative in the system. As a modulation tool, the chain-plus-mix architecture enables applications that individual VCAs cannot replicate without additional mixing modules.

The automatic mix output is particularly practical in performance. Extracting one or two channels for independent routing while letting the rest fall into the mix requires no additional patching decisions; it is the default behavior. Unpatching a channel OUT reintegrates it into the mix automatically. This makes live patching changes clean and predictable.

The LED indicators per channel are genuinely useful, not decorative. In a complex patch where six different CVs are driving six channels, the LEDs give immediate visual confirmation of which channels are active and at what approximate level. This feedback is absent on most simple VCA modules.

The 3360 chip means the signal path is quiet. Ceres is specifically described in the manual as designed for low noise and low CV bleeding, both common weaknesses in budget VCA designs. CV bleeding (audible artifacts from the control voltage leaking into the signal path) becomes audible in complex musical contexts; avoiding it is a quality indicator.

---

## Patch Examples

### Patch 1: Single Channel Amplitude Control

**Goal:** Basic VCA application, establishing the default behavior before exploring the architecture.

**Setup:**
- Oscillator OUT ---[A]---> Ceres ch1 IN
- Envelope OUT ---[C]---> Ceres ch1 CV
- Ceres ch6 MIX OUT ---[A]---> Mixer
- Gate ---[G]---> Envelope GATE

**Procedure:**
1. Set ch1 LEVEL to fully clockwise
2. Leave ch2 through ch6 LEVEL at fully counterclockwise (channels closed)
3. Trigger the envelope; the signal opens at ch1 and appears at the MIX out
4. The LED on ch1 responds to the envelope shape

**What to listen for:** This confirms the default chain behavior. The source at ch1 IN is available at all channels but only ch1 is open. The output arrives at MIX even though no cable is in ch1 OUT. This is the baseline before layering CVs.

---

### Patch 2: One Source, Multiple CV Shapes, Summed

**Goal:** Use the daisy-chain and mix bus to apply different CV shapes to one audio source and collect a composite waveform at the output.

**Setup:**
- Oscillator OUT ---[A]---> Ceres ch1 IN (daisy-chains through all channels automatically)
- Envelope OUT ---[C]---> ch1 CV
- LFO (triangle) OUT ---[C]---> ch2 CV
- LFO (square) OUT ---[C]---> ch3 CV
- Random CV ---[C]---> ch4 CV
- Ceres ch6 MIX OUT ---[A]---> Mixer

**Procedure:**
1. Set ch1 through ch4 LEVEL to 12 o'clock
2. Leave ch5 and ch6 LEVEL at fully counterclockwise
3. Play the envelope and listen to the mix output
4. The oscillator is being amplitude-shaped by four independent CVs simultaneously; the MIX output is the sum of all four

**What to listen for:** The mix output does not sound like the oscillator through a single envelope. It sounds like the oscillator whose amplitude is being shaped by all four CV sources simultaneously. If the envelope, triangle LFO, square LFO, and random CV are all running at different rates, the composite amplitude shape is complex and continuously varying. This is waveform synthesis via multiple simultaneous amplitude modulation, available from the default architecture.

**Extend it:** Set an LFO to audio rate on one channel and listen to how ring-modulation-like effects emerge when the "modulator" is running fast enough.

---

### Patch 3: Independent Routing from a Shared Source

**Goal:** Send the same source to multiple destinations with independent level control for each.

**Setup:**
- Oscillator OUT ---[A]---> Ceres ch1 IN
- Envelope OUT ---[C]---> ch1 CV (all channels receive this via normalling)
- Ceres ch1 OUT ---[A]---> Filter A IN
- Ceres ch2 OUT ---[A]---> Filter B IN
- Ceres ch3 OUT ---[A]---> Delay IN
- Ceres ch6 MIX OUT ---[A]---> Main mixer

**Procedure:**
1. Set ch1, ch2, ch3 LEVEL to different positions for different levels to each destination
2. Notice: patching cables into ch1, ch2, ch3 OUT removes them from the MIX
3. Ch4, ch5, ch6 (unplugged OUT) still contribute to MIX if their LEVEL is open

**What to listen for:** The same source reaches three different processing chains at independently controlled levels. The MIX output still collects the channels that were not individually extracted. This behavior (one source, multiple destinations at different levels, remainder mix) is achieved through Ceres's default architecture without any additional routing modules.

---

## Common Mistakes

**Patching all six inputs manually when daisy-chain does it**  
The most common first-session mistake: patching the same oscillator into all six IN jacks with a mult. This is unnecessary; patching only ch1 IN sends the source to all channels automatically. Patch ch1 IN and leave all other INs empty unless you want to break the chain and send a different source to that point.

**Forgetting that patching an OUT removes it from the MIX**  
When you patch a cable into ch3 OUT to send that channel somewhere specific, ch3 disappears from the ch6 MIX. This is by design but surprises users who expect the channel to appear in both places. If you need a channel to go to a specific destination AND remain in the mix, you need a mult or buffered mult after the ch3 OUT.

**Using 0-10V envelopes without adjusting LEVEL**  
Ceres clips CV above 5V. A 0-10V envelope will reach unity gain partway through its attack and stay clipped at unity for the rest of the attack and all of the sustain. The envelope shape from the midpoint upward is lost. Either use a 0-5V envelope source or use the LEVEL control to attenuate a 0-10V envelope to the correct range before it reaches the VCA circuit.

**Expecting the mix to compensate for channel count**  
The MIX output sums all active channels without level compensation. With six channels contributing at full LEVEL, the output will be louder than a single channel. Plan accordingly: either keep individual LEVEL controls lower when using many channels, or attenuate after the MIX output.

---

## Pairs Well With

**Zadar (Xaoc Devices):** Zadar's four independent envelope channels map directly onto four Ceres channels. Different vector shapes on each Zadar channel produce four distinct amplitude contours running simultaneously on one source. The ASGN input on Zadar adds another layer of per-channel CV control.

**Batumi or any multi-output LFO:** Multiple phase-offset LFO outputs into Ceres channels produce animated composite amplitude modulation that sounds organic and continuously evolving. A quadrature LFO (four outputs at 90-degree phase offsets) through four Ceres channels produces a smooth rotating amplitude effect.

**A-130-2 (Doepfer):** The two modules are complementary in the same system. Ceres handles multi-source mixing and multi-CV amplitude shaping. The A-130-2 handles lin/exp switched precision VCA work and CV processing with its DC-coupled linear/exponential options that Ceres lacks.

**Sequencer with multiple CV outputs:** Multiple sequencer channels driving Ceres channels individually, with the same audio source daisy-chained through, produces rhythmically shaped amplitude patterns where each step controls a different channel's gain. The MIX collects the result as a composite rhythmic amplitude pattern.

---

## Advanced Learning Path

**Step 1: Master the extract-from-mix behavior**  
Patch six sources (or one daisy-chained source), then systematically patch and unplug individual OUT jacks while listening to the MIX. Develop the reflex for when to extract a channel versus let it contribute to the mix. This decision is the core skill for using Ceres in complex patches.

**Step 2: Explore the waveform synthesis application**  
Patch one audio source into ch1 IN and run different LFOs at different rates into ch1 through ch4 CV. Listen to the MIX output and watch the LEDs. Experiment with LFO rates from slow (0.1Hz) through medium (5Hz) to audio-rate (above 20Hz). The composite amplitude modulation behavior changes fundamentally across this range.

**Step 3: Use Ceres as a performance mixer**  
Without any CV patched, Ceres is a six-channel manual mixer. The LEVEL controls become faders. The daisy-chain means one source can be sent to multiple channels at different levels simultaneously, or different sources can be broken into the chain at different points. This application uses none of the VCA functionality but demonstrates the architectural flexibility.

**Step 4: Combine Ceres with Belgrad (Xaoc Devices)**  
Run a Belgrad self-oscillating dual-sine output through Ceres with different CV shapes on different channels. The summed output combines the amplitude contours of the two Belgrad oscillators with the composite CV shapes from Ceres. This is generative sound design from two modules whose architectures interact productively.
