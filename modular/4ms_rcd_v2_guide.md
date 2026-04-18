---
title: 4ms Rotating Clock Divider v2
manufacturer: 4ms Company
primary_role: CONTROLLER
secondary_roles: [ROUTER]
form_factor: eurorack
functions: [clock-divider]
behavior_tags: [stable, percussive, linear, performance-oriented]
use_cases: [polyrhythmic clock division, rhythmic gate patterns, clock distribution]
hp: 8
transport: receive
historical_context: true
---

# 4ms Rotating Clock Divider v2

**The Polyrhythm Infrastructure Module**

![4ms Rotating Clock Divider v2](https://github.com/Shadoe-42/music/raw/main/modular/images/4ms/rcd_v2/front_panel.jpg)  
*4ms RCD v2 — Clock In, Rotate CV, Reset, and eight simultaneous division outputs*

---

## Historical Context

Binary clock division arrived in modular synthesis early and stayed there for a long time. The Doepfer A-160, one of Eurorack's founding utility modules, divided a master clock by 2, 4, 8, and 16: standard subdivisions aligned predictably to a shared downbeat. The Serge Timing Pulse Divider from the late 1970s followed similar logic. Both assumed Western meter — even subdivisions of a master pulse, all outputs locking to the same grid on beat one. The assumption was reasonable given the context, but it left prime number divisions entirely inaccessible in Eurorack: the divisions that create tension, that refuse to align neatly with a four-on-the-floor.

The rhythmic relationships those missing divisions describe have deep roots outside Western music. West African percussion traditions, Indian classical talas, and Cuban polyrhythm build from interlocking cycles of different lengths: a pattern of three against a pattern of four, a seven-beat phrase moving against an eight-beat one. Steve Reich began importing this structural logic into Western experimental music through tape-loop phase techniques in "It's Gonna Rain" (1965) and "Come Out" (1966), then through ensemble pieces including "Drumming" (1970-71) and "Music for 18 Musicians" (1976). Reich's work made non-binary rhythmic relationships visible and audible to a generation of Western composers and producers. The interest in polyrhythm existed well before the Eurorack infrastructure to produce it easily did.

Dann Green founded 4ms Company in Nashville, Tennessee around 2008-2009. The Rotating Clock Divider was among the company's first modules, and it addressed the binary gap directly. Eight simultaneous outputs covering divisions one through eight gave prime divisions (/3, /5, /7) equal standing with binary ones for the first time in a Eurorack clock module. The rotation feature — a CV input that shifts which division appears at which output — meant the assignment itself could be modulated in real time, turning a static utility into a dynamic performance instrument. The RCD Breakout expander moved the module's internal jumper settings (counting direction, gate versus trigger output, maximum division range, spread mode, and auto-reset interval) to front-panel toggle switches, making configuration changes that previously required opening the rack into immediate performance decisions.

---

## Quick Start: First Polyrhythm in 5 Minutes

1. **Patch your clock source** → RCD **Clock In**
2. **Leave Rotate CV unpatched** (start from default position)
3. **Patch Output 1** → kick drum trigger (divide by 1, same speed as clock)
4. **Patch Output 2** → snare trigger (divide by 2, half speed)
5. **Patch Output 3** → hi-hat or percussion (divide by 3, triplet feel)
6. **Start your sequence** — you now have a three-voice polyrhythmic pattern

**Add rotation:**

1. **Patch a slow LFO** → **Rotate CV**
2. **Listen as all three divisions shift simultaneously** — kick moves to /2, snare to /3, percussion to /4
3. The relationships between them transform, not just the individual speeds

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 8HP |
| Depth | ⚠️ ~24mm |
| Power | ⚠️ +50mA / 0mA |
| Inputs | Clock In, Rotate CV, Reset |
| Outputs | Out 1-8 (gate or trigger, selectable) |
| Division range | /1 to /8 default; /1 to /64 via jumper or Breakout |
| Expander | RCD Breakout (4HP, ribbon cable) |

---

## Essential Parameters

**Clock In** receives your master timing signal. Any gate or trigger source works: sequencer clock, LFO square wave, drum machine sync. The rate of the clock sets the base tempo for all eight outputs. Higher input clock rates give more rhythmic resolution across the outputs.

**Rotate CV** shifts the division assignment at every output simultaneously. At zero volts, Output 1 carries /1, Output 2 carries /2, and so on through /8. As voltage increases, each output steps to the next division in the sequence: /1 becomes /2, /2 becomes /3, /7 becomes /8, /8 wraps back to /1. The divisions themselves do not change — only which output carries which division. A slow LFO creates gradual rhythmic evolution. Stepped random voltage creates sudden gear changes between rhythmic states.

**Reset** forces all division counters back to their starting position simultaneously, regardless of where they are in their cycles. A Reset trigger at a regular musical boundary (every 4 or 8 bars) lets complex polyrhythms evolve freely between resets while remaining organized enough to follow. The input requires a 5V or higher trigger signal.

---

## Why This Instrument Excels

The RCD v2 is not a clock divider the way the Doepfer A-160 is a clock divider. Binary dividers give you /2, /4, /8, /16: subdivisions that align predictably because they share common factors with every standard meter. Every output hits beat one together. The RCD v2 gives you /1, /2, /3, /4, /5, /6, /7, /8 simultaneously — and /3, /5, /7 do not share those common factors. Divide-by-3 against divide-by-4 creates a 3:4 polyrhythm that takes 12 clock pulses to fully resolve. Divide-by-5 against divide-by-7 takes 35. These patterns reveal themselves over time rather than repeating every four beats, and that longer resolution cycle is where the rhythmic tension comes from. The module does not hide this mathematics behind user-friendly abstractions. It puts mathematical relationships directly in your hands as patch cables.

Rotation is what separates the RCD v2 from a simpler fixed-output clock divider. When Rotate CV shifts all outputs by one step, the patch cables stay connected to the same modules — kick drum still receives Output 1, snare still receives Output 2 — but the divisions those outputs carry have changed. Output 1 has moved from /1 to /2, Output 2 from /2 to /3. The rhythmic relationship between kick and snare has transformed from a simple 2:1 ratio to a 3:2 polyrhythm. Same modules, same patch, completely different groove. Modulating Rotate CV continuously produces patterns that evolve without repatching. Modulating it in stepped increments produces controlled transitions between distinct rhythmic states. The arrangement capability this creates — real-time structural variation without stopping — is the core musical reason the RCD v2 became standard timing infrastructure in complex Eurorack systems.

Reset exists to give polyrhythm a floor. Left running without intervention, complex odd-division patterns take dozens or hundreds of beats to complete their full cycle. That is musically interesting for ambient or experimental work but potentially disorienting for structured music. A Reset trigger at every eighth bar brings all divisions back to beat one simultaneously, providing the listener with a recognizable anchor point while allowing the pattern to evolve freely in between. The decision of how frequently to reset is an arrangement decision: frequent resets keep patterns comprehensible, infrequent resets maximize polyrhythmic complexity, no reset allows the pattern to run as a long-form mathematical structure.

The jumper settings — accessible via internal jumpers or the front-panel Breakout switches — extend the module's range and behavior significantly. The extended division range (/1 to /64 instead of /1 to /8) opens ambient and slow-evolving work where Output 8 might fire once every 30 seconds at normal tempo. Gate versus trigger mode determines whether outputs send sustained gates or short pulses, which matters for any module that responds to gate length. Spread mode controls whether divisions distribute evenly across the full range or cluster near the maximum. These are not edge cases — they determine whether the module is configured for dance music, ambient work, or live performance, and they should be set deliberately for each musical context.

---

## Understanding Division Outputs

**Default configuration (no rotation applied):**

| Output | Division | Relationship to clock |
|--------|----------|-----------------------|
| Out 1 | /1 | Same speed as input |
| Out 2 | /2 | Half speed |
| Out 3 | /3 | Triplet feel against /4 |
| Out 4 | /4 | Quarter speed |
| Out 5 | /5 | Complex 5-against-4 tension |
| Out 6 | /6 | Two triplet groups per cycle |
| Out 7 | /7 | Very long resolution cycle |
| Out 8 | /8 | Eighth speed |

**With rotation applied:** Each output steps to the next higher division. At maximum rotation, the sequence wraps and returns to the starting assignment.

**Key polyrhythmic resolution times:** /2 against /3 resolves every 6 pulses. /3 against /4 resolves every 12. /4 against /5 resolves every 20. /5 against /7 resolves every 35. This is the mathematical cycle time — how many clock pulses before both patterns land on the same pulse again. Longer resolution times mean longer tension before release.

---

## RCD Breakout Expander

![RCD Breakout Expander](https://github.com/Shadoe-42/music/raw/main/modular/images/4ms/rcd_v2/expander.jpg)  
*RCD Breakout — 4HP expander with panel-access switches for all internal jumper settings*

The RCD Breakout (4HP) connects to the RCD v2 via ribbon cable and surfaces all internal jumper settings as front-panel toggle switches. Changes that previously required removing the module from the rack and moving physical jumpers by hand become instant panel decisions during a session.

**Counting** (up or down): Up counting means rotation increases the division number at each output as voltage rises. Down counting reverses this. The default (up) is the most intuitive starting point; down counting produces different rotation behavior from the same CV source.

**Gate / Trig**: Gate mode holds each output high for half the division period (50% duty cycle). Trigger mode sends a short pulse regardless of division length. Percussion modules are typically indifferent to gate length and respond to either. Envelope generators respond very differently: gate mode gives sustained control over attack and sustain phases, trigger mode fires the envelope regardless of division tempo. Set this based on what the RCD outputs are connected to.

**Max Div** (8, 16, 32, 64): Sets the maximum division in the sequence. At 8, the eight outputs cover /1 through /8. At 16, they spread across the range to cover divisions up to /16. At 32 or 64, Output 8 fires very slowly — useful for ambient textures or slow clock inputs. Higher Max Div settings at standard tempos push Outputs 6, 7, and 8 toward very slow trigger rates.

**Spread** (on or off): Spread ON distributes outputs evenly across the full division range. Spread OFF clusters outputs near the maximum division, producing subtle variations between adjacent outputs rather than wide rhythmic contrast. Spread ON is the practical default for polyrhythmic work; Spread OFF suits situations where you want several outputs running at similar rates with minor differences.

**Auto-Reset** (16 pulses or off): Automatically resets the division sequence every 16 clock pulses. With Auto-Reset active, complex polyrhythms self-anchor to a downbeat periodically without requiring an external Reset source. Disable for maximum polyrhythmic freedom or when using an external Reset trigger.

---

## Progressive Patch Examples

### Patch 1: Beginner - Basic Polyrhythmic Drums

```
┌─────────────────┐    ┌──────────────────┐
│  Clock Source   │    │   4ms RCD v2     │
│                 │    │                  │
│ Clock Out ○─────┼────┼─▶ Clock In       │
│                 │    │                  │
│                 │    │ Out 1 ○──────────┼─── Kick (/1, same speed)
│                 │    │                  │
│                 │    │ Out 2 ○──────────┼─── Snare (/2, half speed)
│                 │    │                  │
│                 │    │ Out 3 ○──────────┼─── Percussion (/3, triplet)
│                 │    │                  │
│                 │    │ Out 5 ○──────────┼─── Hi-hat (/5, complex)
│                 │    │                  │
│ Slow LFO ○──────┼────┼─▶ Rotate CV      │
└─────────────────┘    └──────────────────┘
```

| Connection | Signal | Purpose |
|------------|--------|---------|
| Clock → Clock In | [G] | Master timing source |
| Out 1 → Kick | [G] | Division by 1 — same rate as clock |
| Out 2 → Snare | [G] | Division by 2 — standard backbeat |
| Out 3 → Percussion | [G] | Division by 3 — triplet feel against /4 |
| Out 5 → Hi-hat | [G] | Division by 5 — creates 5-against-4 tension |
| Slow LFO → Rotate CV | [C] | Gradual rhythmic evolution |

**Module settings:**
- Clock In: 16th-note clock at moderate tempo
- Rotate CV: very slow LFO (30-60 second cycle)
- Reset: leave unpatched for continuous operation
- Jumpers / Breakout: default settings (/1-/8, Spread ON, Trigger mode)

**Learning objectives:**
- Hear the difference between /2 (predictable backbeat) and /3 (triplet tension against the kick)
- Notice that /5 creates a longer resolution cycle than /3 or /4 — count the pulses before it aligns with the kick again
- Watch the LEDs: flash rate is a visible representation of division number
- With slow LFO on Rotate CV, identify the moment the groove character changes completely — that is the rotation passing through a new division assignment

**Enhancement:** Replace the slow LFO on Rotate CV with a stepped random source (Wogglebug Stepped, Marbles X). Instead of gradual evolution, the pattern snaps between distinct rhythmic states — a more effective arrangement tool for section transitions.

---

### Patch 2: Intermediate - Evolving Arpeggios with Reset Control

```
┌─────────────────┐    ┌──────────────────┐
│  Fast Clock     │    │   4ms RCD v2     │
│  (32nd notes)   │    │                  │
│ Clock Out ○─────┼────┼─▶ Clock In       │
│                 │    │                  │
│ Stepped         │    │ Out 2 ○──────────┼─── Arpeggiator 1 (16th notes)
│ Random ○────────┼────┼─▶ Rotate CV      │
│                 │    │                  │
│                 │    │ Out 4 ○──────────┼─── Arpeggiator 2 (8th notes)
│                 │    │                  │
│                 │    │ Out 6 ○──────────┼─── Bass sequencer (slow intervals)
│                 │    │                  │
│ Sequencer  ○────┼────┼─▶ Reset In       │
│ Downbeat        │    └──────────────────┘
└─────────────────┘
```

| Connection | Signal | Purpose |
|------------|--------|---------|
| Fast Clock → Clock In | [G] | 32nd-note resolution for detailed arpeggios |
| Out 2 → Arpeggiator 1 | [G] | 16th-note arpeggio clock |
| Out 4 → Arpeggiator 2 | [G] | 8th-note arpeggio clock, slower feel |
| Out 6 → Bass Sequencer | [G] | Long intervals for slow bass motion |
| Stepped Random → Rotate CV | [C] | Sudden rhythmic gear changes |
| Sequencer Downbeat → Reset | [G] | Structural anchor at measure boundaries |

**Module settings:**
- Clock In: 32nd-note clock for detailed timing resolution
- Rotate CV: stepped random voltage changing every 4-8 bars
- Reset: triggered on sequencer measure boundaries (every 4 or 8 bars)
- Jumpers / Breakout: consider Gate mode if using VCAs or envelope-sensitive modules on the outputs

**Learning objectives:**
- Understand why fast input clocks are useful: high resolution gives fine-grained divisions across all eight outputs
- Compare smooth LFO rotation (Patch 1) against stepped random rotation — one evolves, one transitions
- Feel the effect of Reset: complex polyrhythms between two arpeggiators snap back to rhythmic alignment at every downbeat, providing phrase structure
- Recognize that three separate musical voices are derived from one clock and one module

---

### Patch 3: Expert - Probabilistic Polyrhythm with Chaos Processing

Marbles provides the RCD's clock source from its t1 output — probabilistic gate events at musically weighted intervals rather than metronomic ones. Marbles X2 (stepped random CV) drives Rotate CV, shifting division assignments in patterns that repeat but not predictably. Marbles t2 provides periodic Reset. The RCD's outputs then feed Wogglebug: Out 2 drives Wogglebug's Disturb input, injecting polyrhythmic trigger events into Wogglebug's stepped output timing; Out 3 clocks Wogglebug's internal cycle. Wogglebug's Smooth and Stepped outputs feed Function Junction for further processing. RCD Out 5 gates Function Junction for envelope-shaped outputs.

```
┌─────────────────────┐         ┌──────────────────────┐
│   Mutable Marbles   │         │   4ms RCD v2         │
│                     │         │                      │
│ t1 Out ○────────────┼─────────┼─▶ Clock In           │
│                     │         │                      │
│ X2 Out ○────────────┼─────────┼─▶ Rotate CV          │
│                     │         │                      │
│ t2 Out ○────────────┼─────────┼─▶ Reset              │
└─────────────────────┘         │                      │
                                │ Out 2 ○──────────────┼─── Wogglebug Disturb
                                │                      │
                                │ Out 3 ○──────────────┼─── Wogglebug Clock
                                │                      │
                                │ Out 5 ○──────────────┼─── Function Junction Gate
                                └──────────────────────┘

┌─────────────────────┐    ┌────────────────────────────┐
│   Make Noise        │    │ Cre8audio Function Junc.   │
│   Wogglebug         │    │                            │
│                     │    │                            │
│ Smooth ○────────────┼────┼─▶ Ch1 Input               │
│                     │    │                            │
│ Stepped ○───────────┼────┼─▶ Ch2 Input               │
│                     │    │                            │
│ (Disturb ◀ RCD Out 2)    │ ADSR Gate ◀ RCD Out 5     │
│ (Clock  ◀ RCD Out 3)     │                            │
└─────────────────────┘    │ MIX Out ○──────────────────┼─── Modulation output
                           │                            │
                           │ ADSR Out ○─────────────────┼─── Envelope output
                           └────────────────────────────┘
```

| Connection | Signal | Result |
|------------|--------|--------|
| Marbles t1 → RCD Clock | [G] | Probabilistic pulse stream drives division engine |
| Marbles X2 → Rotate CV | [C] | Stepped random shifts division assignments |
| Marbles t2 → Reset | [G] | Periodic gate anchors the pattern |
| RCD Out 2 → Wogglebug Disturb | [G] | Polyrhythmic trigger disrupts Wogglebug output timing |
| RCD Out 3 → Wogglebug Clock | [G] | Division clocks Wogglebug's internal cycle |
| Wogglebug Smooth → Function Junction | [A] | Chaos output processed through mixing and offset |
| RCD Out 5 → Function Junction Gate | [G] | Polyrhythmic gating of envelope output |

**Module settings:**
- Marbles: STEPS at 10 o'clock, DEJA VU at 11 o'clock, t1 providing weighted gate timing
- RCD: Trigger mode, default division range (/1-/8)
- Wogglebug: Disturb and Clock actively patched — run without further intervention

**Learning objectives:**
- A probabilistic clock input means the division engine receives gates at weighted random intervals — the polyrhythmic relationships remain mathematically consistent but trigger timing itself carries variation
- Wogglebug's outputs change character depending on which division is clocking it — Out 3 (/3) produces a different stepped output pattern than Out 2 (/2) from the same Wogglebug
- Function Junction processes Wogglebug's analog outputs into modulation — the result carries both the rhythmic structure of RCD's divisions and the chaotic character of Wogglebug's outputs
- This patch is not fully predictable and is also not random — polyrhythmic structure constrains the chaos

---

### Patch 4: Guided Breakout Exploration

This patch is specifically structured for learning what each Breakout switch does through direct comparison. Use a simple base patch and change one switch at a time, listening to the specific effect of each change before moving to the next.

**Base patch:**

```
┌─────────────────┐    ┌──────────────────────────┐
│  Clock Source   │    │   4ms RCD v2             │
│                 │    │   + RCD Breakout         │
│ Clock Out ○─────┼────┼─▶ Clock In               │
│                 │    │                          │
│                 │    │ Out 1 ○──────────────────┼─── Percussion voice 1
│                 │    │                          │
│                 │    │ Out 3 ○──────────────────┼─── Percussion voice 2
│                 │    │                          │
│                 │    │ Out 5 ○──────────────────┼─── Percussion voice 3
│                 │    │                          │
│                 │    │ Out 8 ○──────────────────┼─── Envelope generator
│                 │    │                          │
│ Slow LFO ○──────┼────┼─▶ Rotate CV              │
└─────────────────┘    └──────────────────────────┘
```

Start with all Breakout switches at their default positions: Counting up, Trig mode, Max Div at 8, Spread ON, Auto-Reset off. Let the patch run with slow rotation active throughout each step.

**Step 1 — Max Div switch:**
Listen to the current pattern, then flip Max Div from 8 to 32. Outputs 5 and 8 now carry much higher division numbers — Out 8 is dividing by 32 rather than 8. The envelope generator fires far less frequently; percussion voice 3 on Out 5 slows dramatically. Flip back to 8. The contrast is immediate. Max Div is the fastest way to change the rhythmic density of outputs in the upper range.

**Step 2 — Spread switch:**
With Max Div back at 8, flip Spread from ON to OFF. Outputs now cluster near the maximum division rather than distributing evenly. The three percussion voices should sound closer together in rhythmic character when Spread is OFF. Flip back to ON. Spread ON is the working default for most polyrhythmic patches; Spread OFF suits situations where you want subtle rhythmic variation between adjacent outputs rather than wide contrast.

**Step 3 — Auto-Reset:**
With rotation running, flip Auto-Reset to 16. Every 16 clock pulses, all divisions reset to their starting positions. Listen for the pattern periodically anchoring back to a recognizable state even while rotating. Flip it off. Without Auto-Reset and no external Reset patched, the pattern runs freely without periodic anchoring. Auto-Reset is useful for structured music; off allows longer-form development.

**Step 4 — Gate/Trig:**
Connect Out 8 specifically to an envelope generator with a moderate sustain setting. Set Gate/Trig to Gate. The envelope responds to gate length — the sound sustains for a longer portion of the division period. Flip to Trig. The envelope fires and decays on a short trigger regardless of division length. The rhythmic timing is the same; the sonic character changes because the envelope generator receives different duration information. This matters most for melodic or tonal voices; percussion modules are typically indifferent to gate length.

**Step 5 — Counting direction:**
Flip Counting from up to down. With a rising voltage on Rotate CV, division assignments now shift in the opposite direction — the same LFO source produces different rhythmic evolution. This is a performance option rather than a corrective setting: down counting is not better or worse than up counting, it produces a different feel from the same CV source.

**Learning objectives:**
- Each switch has one specific, audible effect — internalize what it does before combining switches
- Max Div and Spread affect which divisions are available; Gate/Trig and Counting affect how individual outputs behave
- Auto-Reset is a structural tool: it affects phrase organization, not individual output character
- After working through each switch individually, try combining two changes at once and listen for how the interactions feel different from either change alone

---

## Advanced Features Reference

The RCD v2's jumper settings — or Breakout panel switches if you have the expander — determine the module's operating character. Set these deliberately for each musical context rather than leaving them at factory default indefinitely.

**Division range:** /1 to /8 covers standard rhythmic work at normal tempos. /1 to /16 extends the upper range usefully for melodic sequencing. /1 to /32 or /64 pushes Outputs 6-8 into very slow territory — useful at slow clock rates or for ambient work where minutes-long trigger intervals make musical sense. At 120 BPM with a 16th-note clock, /64 fires Output 8 approximately once every 32 seconds.

**Spread ON** distributes all eight outputs evenly across the division range. Spread OFF clusters outputs near the maximum division, producing subtle differences between adjacent outputs. Spread ON is the practical default for polyrhythmic work; Spread OFF suits situations where you want several voices running at similar but not identical rates.

**Gate mode** holds outputs high for 50% of each division period. Trigger mode sends a short pulse at the start of each division. Use Gate for envelope generators, VCAs, and filter gates; use Trigger for percussion modules, sequencer clocks, and modules that ignore gate length.

**Auto-Reset** fires an internal reset every 16 clock pulses. Keeps complex polyrhythms from drifting too far from a recognizable anchor point. Useful for dance or structured music; disable for maximum polyrhythmic freedom.

---

## Common Use Cases

**Polyrhythmic drum programming:** Four or more drum voices clocked by different RCD outputs produce polyrhythmic patterns without step programming. Choose outputs that share no common factors (/2, /3, /5) for maximum complexity, or mix binary and prime (/2, /4, /3) for structured polyrhythm.

**Timing infrastructure for sequencer networks:** Multiple sequencers clocked at different divisions from a single RCD input run at mathematically related but independent rates. One master clock drives the entire system; each sequencer advances at its own tempo relationship to the master.

**Modulation rate control:** RCD outputs used as LFO or envelope clocks create different modulation rates from a single source. Outputs 6, 7, 8 at extended division ranges produce very slow modulation events useful for ambient or evolving textures.

**Live performance arrangement:** A slow Rotate CV voltage from a performance controller transforms the rhythmic character of the entire system without stopping. Reset triggered manually at section boundaries brings everything back to beat one.

**Polyrhythmic modulation layering:** Patch RCD outputs to envelope retriggering for different modulation voices. Each envelope fires at its own division rate, creating layered amplitude and filter movement at mathematically related but independent rates.

---

## Common Mistakes

### "My polyrhythms sound random and chaotic, not musical"

Odd divisions (/3, /5, /7) create polyrhythmic cycles that take many beats to resolve. Divide-by-3 against divide-by-4 takes 12 clock pulses to fully align. Divide-by-5 against divide-by-7 takes 35. Without understanding how long these cycles are, the patterns sound chaotic because you are hearing the middle of a long mathematical structure rather than recognizing its shape.

Polyrhythms are long-form patterns. The resolution point — when two divisions land on the same pulse — is the moment of musical release, the equivalent of a harmonic cadence. Without reset or auto-reset, complex polyrhythms can take minutes to complete their full cycle at moderate tempos.

Use Reset input on regular musical boundaries (every 4 or 8 bars). Enable Auto-Reset via jumper or Breakout. Start with simpler division pairs (/2 and /3, then /3 and /4) before adding /5 and /7. Give the patterns time — at least 30-60 seconds to hear the full structure emerge.

---

### "I don't hear any difference when I change Rotate CV"

Rotation response depends on the rate relationship between Rotate CV movement and the clock speed. A very slow LFO on a fast clock produces rotation that seems invisible because the change happens over minutes. A very fast LFO produces rotation so rapid that the outputs blur together into apparent randomness.

Start by manually sweeping an offset into Rotate CV by hand. Turn a knob slowly and listen for the shift in groove character. Once you can hear it manually, set an LFO to approximately that rate. At 16th-note clock speeds, Rotate CV should change on a 20-60 second cycle for audible evolution.

Stepped random voltage on Rotate CV often makes the effect more obvious than smooth LFO: the pattern snaps to a new rhythmic state rather than drifting, and the before-and-after contrast is easier to perceive.

---

### "Output 3 and Output 4 keep triggering at almost the same time"

This is the mathematics working correctly. Divide-by-3 and divide-by-4 share an alignment point every 12 clock pulses. Between those alignments they create the polyrhythmic tension; at those alignments they create the resolution. The alignment is not a flaw — it is the cadence that makes the polyrhythm comprehensible rather than just noisy.

For longer cycles between alignments, use divisions with larger least common multiples: /5 against /7 (35 pulses), /3 against /8 (24 pulses). For shorter, more frequent alignment points, use /2 against /4 (4 pulses) or /3 against /6 (6 pulses).

---

### "My clock is too fast or too slow for the divisions to feel musical"

The RCD v2 scales mathematically with its input. At 120 BPM, a quarter-note clock (2Hz) makes Output 8 (/8) fire every 4 seconds — too slow for percussion, useful for slow modulation. A 16th-note clock (8Hz) makes Output 8 fire every second, workable for percussion. A 32nd-note clock (16Hz) makes Output 1 (/1) fire 16 times per second — useful for melodic sequencing, too fast for kick drums.

Choose the input clock rate based on what Output 8 should do, then work backward. For drums at 120 BPM, a 16th-note clock input (8Hz) puts Output 8 at roughly one trigger per two beats — a reasonable starting point. For modulation purposes, faster clocks give finer resolution across all outputs. Pair with the 4ms SCM Plus to generate multiple clock rates from one source when the system needs different rate inputs for different purposes.

---

### "I changed Breakout switches (or jumpers) but nothing sounds different"

Switch effects are context-specific. Division range changes only affect Outputs 5-8 noticeably at standard tempo. Gate versus Trigger mode is only audible on modules that respond to gate length — a percussion module will not reflect the difference. Spread mode requires listening to all eight outputs simultaneously to hear the distribution change. Auto-Reset requires waiting enough bars for a reset cycle to complete.

Change one switch at a time, then specifically listen to the outputs it affects. Test Gate/Trig mode on an envelope generator, not a percussion module. Test Max Div by listening to Output 8 specifically before and after the change. Test Spread by patching all eight outputs and comparing their rhythmic density.

---

### "Reset doesn't seem to do anything"

Reset requires 5V or higher trigger signal. LFOs, audio, and CV signals that do not reach 5V will not reliably trigger it. Use a gate from a sequencer, a trigger from a clock, or a gate source that reaches the threshold.

More commonly: reset is happening at a rhythmically awkward moment. Reset triggered at every single beat rather than every 4 or 8 bars interrupts patterns rather than organizing them. Reset should happen at musically significant structural points — phrase boundaries, section changes, bar downbeats. Visual confirmation: watch all output LEDs flash simultaneously when reset fires.

---

### "Rotation makes everything sound the same, just shifted"

The shift is the point — but understanding what is shifting makes the difference between hearing it as movement and hearing it as transformation. When Output 1 rotates from /1 to /2, it is not just "the kick is now slower." The mathematical relationship between Output 1 and Output 2 has changed from 2:1 (simple subdivision) to 3:2 (polyrhythm). Every module connected to an RCD output now operates in a different rhythmic relationship to every other module, even though nothing was repatched.

Patch at least four outputs to contrasting sounds to make this audible. Listen for how the relationship between kick and snare changes, not just how the kick changes in isolation. The transformation of the ratio between voices is where the musical interest is.

---

### "The outputs drift out of alignment"

They are supposed to. Desynchronization is the core function of a polyrhythm module. Binary clock dividers (Doepfer A-160, 4ms QCD) keep all divisions aligned to shared downbeats — that is a deliberate design choice appropriate for subdivisions, not a universal clock behavior. The RCD v2 lets each division maintain its own cycle, which creates the tension of polyrhythm. When divisions align (LEDs flash together), that is the resolution point. Between alignment points is the tension.

If you want synchronized divisions that all share a downbeat, use a binary clock divider. Use the RCD v2 when you want polyrhythmic independence with mathematical structure.

---

### "My patterns sound boring — RCD is not adding interest like I expected"

Clock division provides infrastructure; musical interest comes from how you use it. Patching /1 to kick and /2 to snare creates a standard backbeat — mathematically correct but rhythmically uninteresting. The interest comes from sound selection (contrasting timbres on different outputs make polyrhythms audible), from rotation timing (slow evolution versus sudden transitions), from reset structure (letting patterns develop between anchors), and from what the divisions are triggering (not just percussion, but sequencer steps, envelope rates, modulation events).

Use outputs at non-adjacent divisions for percussion (/1, /3, /5 rather than /1, /2, /3). Layer at least three contrasting timbres. Route some outputs to envelope generators or sequencer clocks rather than only to percussion. Make rotation serve arrangement goals rather than running continuously at a fixed rate.

---

## Advanced Learning Path

1. **Start without Rotate CV.** Run all eight outputs into different destinations and listen to how each division relates to the master clock. Polyrhythm comprehension begins here. Rotation adds transformation on top of this foundation and makes no sense before the foundation is internalized.

2. **Add Rotate CV from a slow LFO and watch the output assignments shift.** The key insight is that the divisions themselves do not change — only which output carries which division. Understanding this makes rotation predictable rather than mysterious.

3. **Study the prime divisions (/3, /5, /7) independently.** Run divide-by-3 alone against a kick drum on the master clock and count how many pulses before they align again. Repeat with /5 and /7. This builds intuitive understanding of resolution cycle lengths, which is the foundation of working with polyrhythm compositionally rather than accidentally.

4. **Use Reset to bring controlled order back.** After building a complex rotating patch, add a Reset trigger at a predictable musical boundary (every 8 bars). This is the essential live performance skill — it lets patterns evolve freely between resets and return to a known state on demand.

5. **Pair with the SCM Plus to compare division philosophies.** RCD v2 distributes multiple divisions from one clock in parallel; SCM Plus applies one division scheme to a clock and outputs related variations. Understanding both deepens clock manipulation vocabulary significantly.

6. **Work through the Breakout switches using Patch 4 as a guide.** Each switch changes one specific aspect of module behavior — learn what each does in isolation before combining them. Max Div and Spread affect rhythmic density and distribution; Gate/Trig and Counting affect how individual outputs behave for connected modules.

7. **Explore extended division range (/1-/64) at slow clock rates.** Extended range divisions are meaningful only at slow tempos or for modulation purposes. A 32nd-note clock at 120 BPM produces Output 8 at /64 firing approximately once every 32 seconds — useful for very slow texture evolution, not percussion.

---

## Pairs Well With

**Clock multiplication:** The 4ms SCM Plus is the natural companion — it multiplies clocks where RCD v2 divides them. A master clock into both modules gives you a complete timing network: fast multiplied clocks for melodic resolution and slow divided clocks for polyrhythmic structure.

**Rotation control sources:** Ochd provides continuous organic LFO motion for gradual rotation evolution. Wogglebug Stepped output produces the gear-change rotation behavior that works well for section transitions. Marbles X outputs deliver rotation changes that repeat in patterns rather than drifting freely, which produces more musically coherent results than pure random voltage.

**Chaos sources:** Wogglebug's Disturb input responds to triggers from RCD outputs, creating a feedback relationship between the division engine and the chaos source. Maths or Function Junction can generate trigger events for the same purpose with more control over timing.

**Percussion modules:** Any trigger-responding percussion module benefits from polyrhythmic clock inputs. Use Gate mode (via jumper or Breakout) for modules that respond to gate length; Trigger mode for standard percussion.

**Sequencers as polyrhythmic layers:** Clock a second sequencer from RCD Output 5 (/5) while your main sequencer runs from Output 4 (/4). Both sequencers advance at different rates from the same master, creating melodic polyrhythm that evolves over 20-beat cycles without programming.

**Logic modules:** Combining RCD outputs through AND/OR logic gates produces division combinations not directly available as single outputs. AND of Out 2 and Out 3 fires only when both are high simultaneously — a rhythmic pattern derived from the 3:2 relationship. This extends the rhythmic vocabulary beyond the eight direct outputs.

---

*Visit [4mscompany.com](https://4mscompany.com) for firmware updates, jumper documentation, and the complete RCD v2 manual*
