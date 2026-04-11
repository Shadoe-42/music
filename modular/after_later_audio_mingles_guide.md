# After Later Audio Mingles - Guide

**Dual 3-Channel VC Panning Mixer with Integrated LFO**

![After Later Audio Mingles](https://github.com/Shadoe-42/music/raw/main/modular/images/after_later_audio/mingles/front_panel.jpg)  
*12HP dual 3-channel panning mixer with equal loudness VC panning, linear VCAs, and a built-in LFO normalled to both channels in opposing phase*

---

## Quick Start: Get Moving Sound in 5 Minutes

**What is Mingles?** Two independent 3-channel mixers sharing a single panel. Each channel blends three audio sources, then pans the result across a stereo field using a built-in LFO. Channel 1 and Channel 2 pan in opposite directions simultaneously — when one moves right, the other moves left. Every channel has its own stereo output, and a combined MIX output sums everything together. Designed by Brian at Robots Are Red (RAR) and After Later Audio, Mingles also connects via pin headers into Barback or Bartender without consuming a mixer channel.

**Key Specifications:**
- **Width:** 12 HP
- **Depth:** 30 mm
- **Power:** 140 mA @ +12V / 120 mA @ -12V / 0 mA @ +5V

### Your First Autopanning Patch

1. **Patch three audio sources** into CH1 inputs: IN ▷, IN ×, IN Y
2. **Take output** from L CH1 OUT R to a stereo destination (use both L and R)
3. **Set all three CH1 input level knobs** to 12 o'clock
4. **Set CH1 PAN** to center
5. **Set CV AMT (CH1)** to 12 o'clock
6. **Set LFO RATE** to a slow speed
7. **Leave CH1 PAN jack unpatched** — the LFO is already normalled

Your three sources will blend together and the combined signal will sweep left and right automatically. CV AMT controls how wide the sweep is. CH1 PAN knob sets where the sweep is centered.

---

## Essential Parameters

### Input Level Knobs

Each channel has three input level knobs, each controlling one source in that channel's mix. CH1 uses symbols ▷, ×, and Y. CH2 uses □, ○, and ✦. These knobs set the relative blend of each source before the pan stage — they are pre-pan mix controls, not post-pan trims.

### CH1 PAN / CH2 PAN

The large center knobs set each channel's pan position. With no CV active (CV AMT at zero, or CH PAN jack unpatched and CV AMT at minimum), the knob directly positions the sound in the stereo field. With the LFO normalled and CV AMT turned up, the knob sets the center point around which the LFO sweeps. With external CV patched into CH PAN, the CV drives position and the knob's role as an offset is ⚠️ unverified — treat it as the center/offset point.

### CV AMT (CH1 and CH2)

The depth control for pan modulation. Attenuates whatever is driving the CH PAN input — the normalled LFO when nothing is patched, or external CV when a cable is present. At zero, no modulation reaches the pan circuit and the PAN knob sets a fixed static position. At maximum, the full LFO or CV swing applies to panning. Each channel has its own CV AMT, so CH1 and CH2 can have different sweep depths from the same LFO.

### LFO RATE

Controls the speed of the built-in LFO, which drives both channels simultaneously. The LFO OUT jack provides the LFO signal for use elsewhere in the patch regardless of whether it is currently driving any panning.

### Jacks

**CV inputs (top row, left to right):**
- **CH1 PAN** — Pan CV input for Channel 1. When unpatched, the LFO is normalled here. Patching a cable overrides the LFO.
- **CH1 VCA** — Amplitude CV input for Channel 1. Controls the overall level of the channel independently of panning.
- **LFO RATE** — CV input for voltage-controlling the LFO speed.
- **LFO OUT** — Tap the built-in LFO signal for use as a modulation source elsewhere.
- **CH2 VCA** — Amplitude CV input for Channel 2.
- **CH2 PAN** — Pan CV input for Channel 2. When unpatched, the inverted LFO is normalled here.

**Audio inputs:**
- **CH1:** IN ▷, IN ×, IN Y
- **CH2:** IN □, IN ○, IN ✦

**Audio outputs:**
- **L CH1 OUT R** — Stereo output of Channel 1 only
- **L MIX OUT R** — Stereo sum of both channels
- **L CH2 OUT R** — Stereo output of Channel 2 only

---

## Why Mingles Excels

Most mixers place a sound somewhere in the stereo field and leave it there. Mingles treats pan position as a live, continuously modulated parameter — the stereo field becomes part of the composition rather than a fixed staging decision.

The equal loudness panning design is the technical foundation for why this works. Simple linear panning reduces one channel's level while raising the other, which causes the perceived volume to dip when the source is centered. Equal loudness panning uses constant-power curves so the perceived level stays consistent across the entire sweep. When a source moves from left to right through Mingles, it sounds like it's traveling — not fading and reappearing. This is the professional standard for panning and it is what makes automated panning actually useful rather than distracting.

The inverted LFO normalling between CH1 and CH2 is a thoughtful design choice about complementary motion. Both channels share one LFO but receive it in opposing phases. When CH1 sweeps right, CH2 sweeps left. Run different sources through each channel and mix them at MIX OUT — the result is two signals orbiting opposite sides of the stereo field simultaneously. This creates a naturally wide, moving stereo image without any external modulation sources. It is the kind of behavior that would require careful patching elsewhere but arrives as the default state here.

The stereo per-channel outputs alongside the combined MIX output give you a routing decision that matters. MIX OUT is the convenient option. CH1 OUT and CH2 OUT are for when you want to process each panning layer independently before combining — separate reverbs, separate compression, different effect chains — then combine downstream. The architecture supports both workflows without requiring anything extra.

---

## Patch Examples

### **Patch 1: Three-Source Autopanning Mixer**

The foundation patch. Three sources blend in CH1, the LFO drives continuous stereo movement, CV AMT sets the sweep width.

```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

┌─ Source 1 ─────┐    ┌─ Mingles ──────────────────────────┐
│ Voice 1 OUT ○──┼────┼─▶ IN ▷ [A]                          │
└────────────────┘    │   level: 3/4 up                     │
                      │                                     │
┌─ Source 2 ─────┐    │                                     │
│ Voice 2 OUT ○──┼────┼─▶ IN × [A]                          │
└────────────────┘    │   level: 1/2 up                     │
                      │                                     │
┌─ Source 3 ─────┐    │                                     │
│ Voice 3 OUT ○──┼────┼─▶ IN Y [A]   L CH1 OUT R ○──────────┼──▶ Stereo In [A]
└────────────────┘    │   level: 1/2 up                     │
                      │                                     │
                      │   CH1 PAN: center                   │
                      │   CV AMT (CH1): 12 o'clock          │
                      │   LFO RATE: slow                    │
                      │   CH1 PAN jack: unpatched (LFO normalled)
                      └─────────────────────────────────────┘
```

The three sources mix at their respective knob levels before reaching the pan stage. The LFO sweeps the combined mix left and right at the rate set by LFO RATE. CV AMT determines how far the sweep travels from center — at low CV AMT the sweep is subtle, at high CV AMT the signal fully crosses from hard left to hard right. The CH1 PAN knob positions the sweep's center; moving it left biases the sweep toward the left half of the field.

**Main Example:** Three voice modules (Mutable Plaits, Noise Engineering Loquelic Iteritas, Mutable Rings) blended and autopanned as a single evolving layer  
**Alternative Options:**
- **Budget:** Any three oscillators with their levels balanced by ear — same result with simpler sources
- **Different character:** Replace one source with a noise or texture module (Wogglebug, Rings in noise mode) for a mix that has tonal sources plus moving texture
- **Premium:** Use Xaoc Devices Zadar envelopes into CH1 VCA to add amplitude shaping on top of the panning sweep

---

### **Patch 2: Opposing Stereo Field Movement**

Both channels run simultaneously with their opposing LFO phases. Sources on CH1 and CH2 orbit opposite sides of the stereo field.

```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

┌─ CH1 Sources ──┐    ┌─ Mingles ──────────────────────────────────────────┐
│ Lead OUT ○─────┼────┼─▶ IN ▷ [A]                                          │
│ Pad OUT ○──────┼────┼─▶ IN × [A]   L CH1 OUT R ○ (optional: separate FX) │
└────────────────┘    │                                                     │
                      │   CH1 PAN: center                                   │
                      │   CV AMT (CH1): 12 o'clock                          │
                      │   CH1 PAN jack: unpatched                           │
┌─ CH2 Sources ──┐    │                                                     │
│ Bass OUT ○─────┼────┼─▶ IN □ [A]                                          │
│ Drum OUT ○─────┼────┼─▶ IN ○ [A]   L CH2 OUT R ○ (optional: separate FX) │
└────────────────┘    │                                                     │
                      │   CH2 PAN: center                                   │
                      │   CV AMT (CH2): 12 o'clock                          │
                      │   CH2 PAN jack: unpatched                           │
                      │                                                     │
                      │   LFO RATE: moderate                                │
                      │               L MIX OUT R ○────────────────────────┼──▶ Stereo In [A]
                      └─────────────────────────────────────────────────────┘
```

Because CH2 receives the LFO phase-inverted, when CH1 moves right, CH2 moves left. The MIX OUT captures both in a single stereo output. Setting both CV AMT values to the same level creates symmetric orbiting motion — sources from each channel pass through opposite sides of the stereo field simultaneously. Try different CV AMT values for each channel: asymmetric sweeps create a less predictable stereo image that sounds more alive. The individual channel outputs (L CH1 OUT R, L CH2 OUT R) allow separate reverb or delay processing before summing, which preserves the spatial separation between channels.

**Main Example:** Melodic voices on CH1 (lead, pad) and rhythmic sources on CH2 (bass, drums) orbiting opposite halves of the stereo field via MIX OUT  
**Alternative Options:**
- **Budget:** Any two pairs of sources — the opposing LFO behavior works identically regardless of source complexity
- **Different character:** Route CH1 OUT and CH2 OUT to different reverb depths before combining — CH1 dry and close, CH2 wet and distant, to create depth alongside width
- **Premium:** Qu-Bit Aurora on CH1 OUT and Endorphin.es Ghost on CH2 OUT before a final sum creates two fully independent spatial environments orbiting each other

---

### **Patch 3: External CV Pan Control**

Patching a CV source into CH1 PAN overrides the LFO normalling for that channel. Pan position becomes voltage-controlled by the external source while CH2 continues receiving the inverted LFO. The freed LFO signal is available at LFO OUT.

```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

┌─ Sequencer ────┐    ┌─ Mingles ──────────────────────────────────────────┐
│ CV OUT ○───────┼────┼─▶ CH1 PAN [C] (LFO normalling broken)              │
└────────────────┘    │                                                     │
                      │   CV AMT (CH1): 3/4 up                              │
┌─ CH1 Sources ──┐    │                                                     │
│ Lead OUT ○─────┼────┼─▶ IN ▷ [A]   L CH1 OUT R ○────────────────────────┼──▶ Stereo In [A]
│ Pad OUT ○──────┼────┼─▶ IN × [A]                                          │
└────────────────┘    │   CH1 PAN knob: center                              │
                      │                                                     │
                      │   CH2 PAN jack: unpatched (inverted LFO active)     │
                      │   LFO RATE: moderate                                │
                      │                                                     │
                      │   LFO OUT ○────────────────────────────────────────┼──▶ Filter CV [C]
                      └─────────────────────────────────────────────────────┘
```

The sequencer steps the pan position in discrete voltage jumps rather than a continuous sweep — hard-left on one step, center on the next, hard-right on another. CV AMT scales how far each voltage step moves the pan position. CH2 still receives the inverted LFO, so its sources continue sweeping in opposition to wherever CH1 is currently positioned. Meanwhile LFO OUT now carries the unused LFO signal to a filter's CV input, modulating timbre at the same rate as CH2's panning. One LFO drives spatial movement on CH2 and timbral movement on the filter simultaneously.

**Main Example:** Sequenced CV driving discrete pan steps on CH1, inverted LFO still active on CH2, LFO OUT repurposed for filter modulation  
**Alternative Options:**
- **Budget:** Slow random CV from any sample-and-hold source into CH1 PAN for unpredictable but unhurried spatial repositioning
- **Different character:** Envelope from Make Noise Maths into CH1 PAN — each note attack triggers a pan sweep that decays back to center, creating a spatial envelope that mirrors the amplitude envelope
- **Premium:** Mutable Marbles X output into CH1 PAN for stepped random pan positions quantized to interesting rhythmic intervals, with t output into LFO RATE CV for rhythmically varying LFO speed on CH2

---

## Common Mistakes

### **1. CV AMT at zero with no panning movement**

CV AMT is the gate between the LFO (or any external CV) and the pan circuit. When it is fully counterclockwise, no modulation reaches the panner regardless of LFO rate, LFO amplitude, or what is patched into CH PAN. The PAN knob then sets a completely static position. This is useful when you want no movement, but it is easy to forget it is the control responsible for enabling modulation at all. If the autopanning stops working, check CV AMT before assuming something is wrong with the LFO.

### **2. Expecting the LFO to remain active after patching into CH PAN**

When a cable is plugged into CH1 PAN, the LFO normalling breaks entirely for that channel. The patched CV source takes complete control. There is no way to combine the LFO with external CV through the same jack. If you want to mix the LFO with another modulation source and send the result to CH PAN, that mixing needs to happen before the jack — through a utility mixer, Maths, or similar — before the combined signal enters CH PAN.

### **3. Patching only one side of a stereo output pair**

L CH1 OUT R, L MIX OUT R, and L CH2 OUT R are stereo output pairs. Patching only the L jack gives a mono signal — specifically whatever the current pan position sends to the left channel. When the panner moves right, that signal gets quieter. When it moves hard right, you hear nothing. For the full stereo image, both L and R need to connect to a stereo destination. Using a single output into a mono destination is valid when that is the intent, but it is rarely the intent.

### **4. Using MIX OUT when independent channel processing is the goal**

MIX OUT combines both channels into a single stereo sum. Once the signals are in the mix output, they cannot be separated. If you want different reverb depths on CH1 and CH2, or different compression, or different effect chains, that processing needs to happen on the individual channel outputs before the signals combine. The architecture gives you CH1 OUT and CH2 OUT for exactly this reason. MIX OUT is convenient; the separate outputs are intentional.

### **5. Missing LFO OUT as a free modulation source**

The internal LFO runs constantly and its output is always available at LFO OUT. Even while it is driving panning, that same signal can modulate a filter, a VCA, an oscillator's FM input, or anything else that accepts CV. When you patch external CV into both CH1 PAN and CH2 PAN, the LFO becomes completely free — no longer committed to any panning purpose — but it keeps running and LFO OUT keeps outputting. Treating LFO OUT as a free extra modulation source rather than an afterthought multiplies what Mingles contributes to a patch.

---

## Pairs Well With

**Stereo-capable effects:** Qu-Bit Aurora, Endorphin.es Ghost, and any reverb or delay with stereo inputs benefit directly from Mingles' stereo outputs. Feeding the output of a panning channel into a stereo reverb preserves the spatial position — a sound that has swept right enters the reverb from the right and its tail decays from there. The movement becomes part of the reverb's behavior rather than lost in it.

**Modulation sources for CH PAN override:** Make Noise Maths, Xaoc Devices Batumi II, and Mutable Marbles X outputs all provide CV for programmatic pan control when the built-in LFO is not the right tool. Different waveform shapes create different spatial movement — a Maths falling exponential creates a pan sweep that rushes and then slows, Batumi II sine waves create smooth sine-shaped movement at precise frequencies, Marbles stepped random creates unpredictable repositioning within musical timing.

**After Later Audio Barback / Bartender:** The native ecosystem connection. Mingles attaches via pin headers and contributes its mix to the Barback or Bartender without using a regular channel. This is a system-design choice — Mingles was built knowing it would live alongside After Later Audio mixer infrastructure, and the pin header connection is how that relationship works in practice.

**Envelope generators into CH VCA:** Erica Synths Black EG2, Behringer 1003, or Make Noise Maths into CH1 VCA or CH2 VCA adds amplitude envelope shaping on top of the panning. A slow decay envelope combined with autopanning produces a spatially moving fade — the sound not only moves across the field but also diminishes over time. The VCA and pan modulation are independent axes, so combining them produces behavior neither creates alone.

**Mordax Data:** Patching L and R of any output pair into Mordax Data visualizes the stereo level balance as a voltage relationship. This makes equal loudness panning's behavior visible — the levels shift but the perceived loudness stays consistent, which is easier to hear once you have seen it.

---

## Advanced Learning Path

1. **Single channel foundation** — Use CH1 only with all three inputs and the normalled LFO. Understand CV AMT as the depth control by sweeping it from zero to maximum while listening to the pan width change. Identify where the LFO center point sits and how the CH1 PAN knob moves it.

2. **Add CH2 through MIX OUT** — Bring sources into CH2 and monitor MIX OUT. Observe the opposing LFO phase — when CH1 moves right, CH2 moves left. Experiment with matching and mismatching CV AMT values between channels to see how symmetric vs. asymmetric sweeps change the stereo image character.

3. **Separate the outputs** — Route CH1 OUT and CH2 OUT into different effects before combining in a mixer. This demonstrates when the individual outputs matter and what you lose by going directly to MIX OUT.

4. **Override CH1 PAN with external CV** — Patch a slow triangle LFO from another module into CH1 PAN. Notice the LFO normalling breaks and the external source takes control. CH2 still receives the inverted internal LFO. Adjust LFO RATE and observe it affects only CH2's panning now.

5. **Use LFO OUT** — With CH2 PAN still normalled to the internal LFO, patch LFO OUT into a filter's CV input or a VCA. The same LFO now drives panning on CH2 and timbre or amplitude elsewhere. Adjust LFO RATE and notice all three behaviors change together.

6. **Barback/Bartender integration** — If your system includes Barback or Bartender, connect via pin headers and observe how Mingles feeds into the mixer ecosystem without consuming a channel. Compare the workflow difference between pin header integration and using the output jacks directly.

---

*After Later Audio Mingles is an original design by Brian (Robots Are Red) in collaboration with After Later Audio.*
