---
title: Frap Tools 411
manufacturer: Frap Tools
primary_role: AMPLIFIER
secondary_roles: [ROUTER]
form_factor: eurorack
functions: [vca, mixer]
behavior_tags: [clean, stable, linear, reactive]
use_cases: [audio mixing and routing, CV-controlled mixing, signal distribution]
hp: 6
---

# Frap Tools 411 Guide

**Quadruple Linear VCA, Mixer, and Multiple**  
**Manufacturer:** Frap Tools  
**Format:** Eurorack  
**Width:** 6HP | **Depth:** 38mm | **Power:** +35mA / -25mA  

![Frap Tools 411](https://github.com/Shadoe-42/music/raw/main/modular/images/frap_tools/411/front_panel.jpg)  
*6HP quad linear VCA with semi-normalled signal and CV inputs, -6dB CV switches, ALL output, and UNPATCHED output. Four channels that adapt to what you patch.*

---

## Quick Start

**What you need:** An audio source, an envelope, and a destination.

**Minimum viable patch:**
1. Patch your oscillator OUT ---[A]---> 411 ch1 IN
2. Patch your envelope OUT ---[C]---> 411 ch1 CV
3. Patch 411 ALL OUT ---[A]---> your mixer
4. Trigger the envelope; the VCA opens and closes

**Key Specifications:**

| Spec | Value |
|------|-------|
| Width | 6HP |
| Depth | 38mm |
| Power | +35mA / -25mA |
| Channels | 4 (semi-normalled) |
| Response | Linear only |
| DC coupling | Yes (audio and CV both supported) |
| Default state | Open (signal passes without CV) |
| -6dB switch | Per channel; halves the CV input |
| ALL output | Sum of all four channels |
| UNPATCHED output | Sum of channels with no cable in OUT |

---

## The Architecture: Semi-Normalled Inputs and Two Outputs

The 411 has two architectural features that distinguish it from a basic quad VCA.

**Semi-normalled signal and CV inputs:** Both the signal inputs and the CV inputs are cascaded through the four channels. Patching a signal into ch1 IN sends that signal to ch2, ch3, and ch4 as well, unless a cable is patched into those inputs to break the normal. The same normalling applies to CV: a single envelope patched into ch1 CV automatically controls all four channels unless individual CV inputs are broken by patching. This is different from modules that normal only the signal; the 411 normals both, independently.

The practical result: two cables (one audio source into ch1 IN, one envelope into ch1 CV) create a four-channel, simultaneously gated amplitude system. All four channels receive the source and all four respond to the same envelope. Breaking the normal at any point (for signal or CV independently) creates mixed configurations where some channels share the source and others have their own, while some channels share the CV and others have their own.

**Two output types:** The ALL output sums all four channels regardless of whether individual channel OUTs are patched. The UNPATCHED output sums only the channels whose individual OUT jacks have no cable. This mirrors the behavior in the Frap Tools 321, a related utility module.

The UNPATCHED output is the less obvious but more useful of the two for live work. Any channel you route to a specific destination with a patch cable disappears from the UNPATCHED mix and remains in it when you unplug. The mix adjusts automatically. If you are routing three channels to specific places and one channel is unpatched, the UNPATCHED output carries only that remaining channel. If you unplug one of the three, it rejoins the UNPATCHED mix automatically.

**Open by default:** With no CV patched, the 411's VCAs pass signal at full level. This is opposite to a closed-by-default VCA, where no CV means no output. The 411's open default means it functions as a passive mult or attenuator without any CV: patch audio in, audio comes out at full level from the appropriate output. A gate or envelope then closes it down from full open: a different modulation model than the more common closed-by-default VCAs.

---

## Essential Parameters

### IN (Signal Input)

Audio or CV signal input. Semi-normalled from the previous channel: if nothing is patched here, this channel receives whatever was patched into ch1 IN (or the most recent channel with a cable). Patching a cable breaks the normal at this point; only this channel and subsequent unplugged channels receive the new source.

### CV

Control voltage input. Semi-normalled from ch1: patching into ch1 CV sends that CV to all four channels unless broken. Patching into ch2 CV applies that CV only to ch2 forward (and backward normalling is broken at ch2). Because both signal and CV are semi-normalled independently, any combination of shared/independent signal and shared/independent CV is achievable by selective patching.

### -6dB Switch

Per channel. Halves the CV input voltage before it reaches the VCA circuit. This compensates for the difference between 0-5V and 0-10V CV ranges.

Without the switch: a 0-10V envelope would reach full gain (open) at approximately 5V (halfway through the attack) and stay fully open for the remainder of the attack and sustain. The top half of the envelope shape is lost.

With the switch engaged: the 0-10V envelope is halved to 0-5V before the VCA sees it. Full gain is reached at the envelope peak, and the entire shape is preserved.

Use the -6dB switch when driving the 411 with 0-10V sources. Leave it off for 0-5V sources. The exact threshold depends on the 411's unity gain CV level, which varies slightly per unit.

### OUT (Individual Channel Output)

The output for this channel. Patching a cable here routes this channel independently. When patched, this channel is absent from the UNPATCHED output mix; it remains in the ALL output.

### ALL Output

Sums all four channels continuously. All channels appear here regardless of whether individual OUTs are patched.

### UNPATCHED Output

Sums only the channels with no cable in their individual OUT jack. This is the "remainder" mix: whatever is not explicitly routed somewhere else. The mix updates automatically as cables are patched and unpatched during a performance.

---

## Historical Context

Frap Tools is an Italian manufacturer whose design language centers on the interaction between modules in a system rather than isolated module features. The 411 is a direct counterpart to the 321 (triple attenuverter, offset, and mixer), sharing the ALL and UNPATCHED output concept. The numbering system reflects the channel count: 3 channels in the 321, 4 in the 411. Both modules assume that the user will be routing signals between multiple destinations and that the routing behavior itself should be part of the module's design rather than an external patching concern.

The semi-normalled dual-input architecture of the 411 reflects a different design philosophy than the Doepfer approach to VCAs. Where Doepfer provides clean, minimal channels with no implicit routing, Frap Tools builds routing assumptions directly into the module: the defaults expect the user to be working with one or two sources through multiple CV shapes, or multiple CVs applied to a shared source, and to be routing results to multiple destinations simultaneously. The UNPATCHED output specifically anticipates live performance patching, where the "what's not routed elsewhere" category is a useful bus to have available without planning ahead.

DC coupling across all inputs means the 411 handles audio and CV identically, reflecting the Eurorack principle that the distinction between signal types is a patching decision, not a hardware constraint.

---

## Why This Excels

The UNPATCHED output solves a real live-patching problem without requiring any additional modules or decisions. In a typical performance patch, some channels go to specific destinations and the remainder should ideally feed a main mix. With a standard quad VCA, this requires manually patching the "remainder" channels into a mixer. The 411 does this automatically: the UNPATCHED output is always the running sum of channels you have not explicitly sent elsewhere. Plugging a channel OUT into a specific destination removes it from UNPATCHED; unplugging it returns it. The mix maintains itself.

The dual semi-normalling (both signal and CV) combined with the open default behavior creates a module that adapts to the patch rather than requiring the patch to adapt to it. Two cables into ch1 establishes four-channel amplitude control; progressive patching into individual inputs and CVs builds complexity from that default. This is additive patching logic, where the initial state is functional and additional cables increase specificity rather than beginning with nothing.

The -6dB switches are a practical quality-of-life feature. Managing 0-5V versus 0-10V CV compatibility manually (by adding attenuators upstream) is a common friction point in dense patches. Per-channel switches that handle the conversion at the VCA itself reduce that friction without consuming additional module space.

---

## Patch Examples

### Patch 1: Default Four-Channel Gate Control

**Goal:** Understand the open-by-default behavior and semi-normalling from two cables.

**Setup:**
```
Oscillator OUT        ---[A]---> 411 ch1 IN
Envelope OUT          ---[C]---> 411 ch1 CV
411 ALL OUT           ---[A]---> Mixer
```

**Procedure:**
1. Before triggering anything, notice that the oscillator passes through to ALL OUT at full level (open by default)
2. Trigger the envelope; the signal closes on the envelope's attack and opens on the release; the VCA starts open and the envelope closes it, or starts open and the envelope represents gain target
3. Set ch1 CV attenuator or LEVEL to explore the effect

**Note on open by default:** The 411's default open state means the envelope controls the level from full open downward if the envelope is used as a gain ceiling, or the envelope controls the level upward from zero if the CV is a trigger-driven gate. Confirm your envelope polarity and starting point for the behavior you expect.

**What to listen for:** All four channels receive the oscillator (semi-normalled through ch1 IN) and all four receive the envelope (semi-normalled through ch1 CV). All four contribute to ALL OUT. Four-channel VCA operation from two cables.

---

### Patch 2: Mixed CV Application (Shared Source, Independent CVs)

**Goal:** Send one source through all four channels with different CV shapes, observe results at ALL and UNPATCHED.

**Setup:**
```
Oscillator OUT        ---[A]---> 411 ch1 IN  (normals to all channels)
Envelope OUT          ---[C]---> 411 ch1 CV
LFO OUT               ---[C]---> 411 ch2 CV  (breaks CV normal at ch2)
411 ch3 OUT           ---[A]---> Filter IN
411 ALL OUT           ---[A]---> Main mix
411 UNPATCHED OUT     ---[A]---> Secondary mix
```

**What this creates:**
- Ch1: envelope-controlled amplitude
- Ch2: LFO-controlled amplitude  
- Ch3: LFO-controlled (same LFO as ch2, normalled from ch2 CV unless you break it), routed independently to the filter
- Ch4: LFO-controlled (same as ch3 via normal), contributing to UNPATCHED output

ALL output contains all four channels summed. UNPATCHED output contains only ch1, ch2, and ch4 (ch3 is extracted via its OUT jack).

**What to listen for:** The ALL output combines the envelope-shaped and LFO-shaped versions of the same source. The UNPATCHED output updates automatically when you patch and unplug ch3 OUT.

---

### Patch 3: CV Processing (DC Coupled Application)

**Goal:** Use the 411 to control the depth of modulation sources, not audio.

**Setup:**
```
LFO 1 OUT             ---[C]---> 411 ch1 IN
LFO 2 OUT             ---[C]---> 411 ch2 IN  (breaks signal normal at ch2)
Envelope 1 OUT        ---[C]---> 411 ch1 CV
Envelope 2 OUT        ---[C]---> 411 ch2 CV  (breaks CV normal at ch2)
411 ch1 OUT           ---[C]---> VCO FM input
411 ch2 OUT           ---[C]---> Filter FM input
```

**Procedure:**
1. Engage -6dB switch if envelopes are 0-10V
2. Each envelope controls how deeply its paired LFO modulates the target
3. The LFO depth grows and shrinks with the envelope shape on each channel

**What to listen for:** LFO modulation depth that breathes with the note shape. The 411's DC coupling treats modulation signals identically to audio signals, so the same amplitude-shaping logic applies to CVs.

---

## Common Mistakes

**Expecting closed-by-default behavior**  
The 411 starts open. With no CV patched, signal passes at full level. If you patch audio in and hear it immediately without triggering anything, the module is working correctly. If you want the VCA to be silent until triggered, you need to actively close it with CV, not rely on a closed default state. This is the opposite of most VCAs in the system and requires recalibrating expectations when working with the 411.

**Not using the -6dB switch with 0-10V envelopes**  
A 0-10V envelope into the 411 without the -6dB switch engaged saturates the CV input before the envelope peaks. The VCA reaches full gain midway through the attack and the rest of the envelope shape is invisible to the circuit. Engage the -6dB switch whenever using 0-10V CV sources; leave it off for 0-5V sources.

**Confusing ALL and UNPATCHED output behavior**  
ALL always has all four channels. UNPATCHED has only those with nothing plugged into their OUT. If you patch a cable into ch2 OUT, ch2 appears in ALL and disappears from UNPATCHED. If you then unplug that cable, ch2 returns to UNPATCHED. The two outputs are complementary, not alternatives: use ALL when you want a complete sum, UNPATCHED when you want to dynamically manage what goes into your main mix.

**Forgetting CV normalling when adding individual CVs**  
Patching into ch1 CV sends that CV to ch2, ch3, and ch4 via normalling. If you then patch a separate CV into ch2 CV, ch2 receives its own CV but ch3 and ch4 still receive ch1's CV (normalled through ch2). To give ch3 its own CV, patch into ch3 CV directly. Each new CV patch breaks the normal only from that point forward. Drawing out the normalling state before patching complex configurations prevents confusion.

---

## Pairs Well With

**321 (Frap Tools):** The 321 is the direct companion module, sharing the ALL and UNPATCHED output architecture in a three-channel attenuverter format. The two modules share design language and both appear frequently in Frap Tools-centric systems. Using both together gives seven controllable signal channels (3 + 4) with complementary output behaviors across 9HP.

**Sequencers with multiple CV outputs:** The semi-normalled CV inputs make the 411 well-suited to sequencer-driven patches. A sequencer with four CV outputs drives each 411 channel independently, with the same audio source through all channels, producing rhythmically varied amplitude patterns collected at ALL.

**Ochd (Divkid) or multi-output LFO:** Multiple unrelated LFO shapes into four 411 channels, one audio source through ch1 IN, ALL output to a mixer: this is the 411's compositional mode. The composite amplitude pattern from four different LFO rates and shapes produces continuously evolving dynamics from a static pitch source.

**A-130-2 (Doepfer):** The two modules are complementary in system design. The 411's open-by-default, semi-normalled, dual-output architecture suits live performance routing. The A-130-2's lin/exp switch and DC-coupled precise CV processing suits studio patch work where response type and exact gain control matter more than default routing behavior.

---

## Advanced Learning Path

**Step 1: Map the normalling system deliberately**  
Before patching any session with the 411, sketch the intended normalling state: which channels share a signal source, which share a CV source, which are independent. The semi-normalled architecture rewards planning; random patching without understanding the normals produces unexpected signal routing.

**Step 2: Practice with UNPATCHED as a performance bus**  
In a live patch, route two channels to specific destinations and leave two in the UNPATCHED bus. During the performance, practice patching and unpatching individual OUT jacks. The UNPATCHED mix adjusts in real time; the goal is becoming fluent with the dynamic mix behavior as a performance gesture.

**Step 3: Explore the open-by-default state creatively**  
Design patches that use the open default intentionally: the 411 as a starting-point-at-full that CVs pull down from, rather than a closed gate that CVs push open. Inverted envelopes, negative offsets, and falling CVs all become musical tools in this model.

**Step 4: Compare 411, Ceres, and A-130-2 side by side**  
These three modules address the same core function from three different design philosophies: Doepfer's minimal precision dual-channel with response switching, Vostok's six-channel chain-and-mix system with LED feedback, and Frap Tools' four-channel open-default routing module with dual output types. Understanding what each one does well and where each one is the wrong tool is more useful than any single guide can convey. Patching the same signal through all three in sequence and comparing the results teaches system design thinking directly.
