---
title: AtoVproject lx-euclid
manufacturer: AtoVproject
primary_role: CONTROLLER
secondary_roles: []
form_factor: eurorack
functions: [euclidean-generator, sequencer]
behavior_tags: [stable, percussive, linear, generative]
use_cases: [euclidean rhythm source, polyrhythmic pattern generator, rhythmic gate patterns]
hp: 16
screen: true
---

# AtoVproject lx-euclid Guide

**4-Channel Euclidean Trigger Sequencer**  
**Manufacturer:** AtoVproject  
**Format:** Eurorack  
**Width:** 16HP | **Power:** +12V: 120mA / -12V: 7mA / +5V: not used  
**CV Input Range:** -5V to +5V | **Gate Output:** 0-10V

![AtoVproject lx-euclid](https://github.com/Shadoe-42/music/raw/main/modular/images/atovproject/lx_euclid/front_panel.jpg)  
*4-channel Euclidean trigger sequencer with touch ring interface, circular display, four distribution algorithms, per-channel clock dividers, CV-assignable parameters, burst mode, and macro-mapped performance controls.*

---

## What Is a Euclidean Rhythm?

In 2004, computer scientist Godfried Toussaint observed that a large number of traditional rhythmic patterns from around the world can be described by a single mathematical principle: distribute a given number of beats as evenly as possible across a given number of steps.

The algorithm that does this is called the Euclidean algorithm, originally developed by the ancient Greek mathematician Euclid for calculating the greatest common divisor of two numbers. Applied to rhythm, it produces something remarkable: when you ask it to place 3 beats across 8 steps, for example, it generates the pattern used in Cuban son and tresillo. Five beats in 8 steps produces the bell pattern fundamental to West African and Afro-Cuban music. Three beats in 4 steps produces the basic clave. The algorithm independently arrived at the same solutions human cultures developed over centuries.

The practical result is that Euclidean rhythms feel natural and musical even when generated mathematically. They have a quality of even spacing that the ear registers as groove rather than arithmetic. Because the beats are distributed as evenly as the numbers allow, polyrhythmic combinations of multiple Euclidean patterns tend to interlock rather than clash.

The lx-euclid applies this principle to four independent channels simultaneously, with controls for length (total steps), beats (how many of those steps fire a trigger), rotation (where in the cycle the pattern begins), and probability (how often each beat actually fires). These four parameters give you access to a very large space of rhythmic possibilities through a compact and fast interface.

---

## Architecture Overview

The lx-euclid is a 4-channel trigger sequencer. Each channel produces a gate signal at its output whenever the current step is a beat in that channel's Euclidean pattern. The four channels run simultaneously from the same clock, with per-channel clock division available for independent subdivisions.

**Key specifications:**
- 4 independent Euclidean rhythm channels
- Touch ring interface: inner ring and outer ring, both tap and scroll
- Circular graphical display showing all 4 rhythms simultaneously
- 4 assignable CV inputs (-5V to +5V)
- 4 gate outputs (0V inactive, 10V active)
- 8 preset slots with 4 recall modes
- Automatic state save on power-down

**On boot:** The lx-euclid performs a touch sensor calibration routine every time it powers up. Do not touch the rings during this process. Wait until the display is fully active before interacting with the module.

---

## Interface: Touch Rings and Controls

**Inner ring and Outer ring:** Two concentric capacitive touch rings surround the circular display. Both rings can be tapped and scrolled. The motion is similar to the original iPod click wheel: run a finger along the ring surface to scroll through values, or tap to confirm. The inner ring and outer ring are assigned different functions depending on which edit page is active. Their default main-page functions can be reassigned via the Macro system.

**Tap button:** On the main page with the internal clock source selected, tapping this button sets the tempo by rhythm. Press it multiple times and the lx-euclid averages the intervals to calculate BPM. Holding the Tap button and releasing it resets all channels to their first step simultaneously. When a preset is armed in "internal reset" recall mode, releasing the Tap button also triggers the preset recall.

**Channel selection buttons (4):** Four buttons below the display, color-coded left to right: Channel 1 (Yellow), Channel 2 (Red), Channel 3 (Blue), Channel 4 (Turquoise). Pressing a channel button enters that channel's edit page. These buttons are also the primary navigation tool for moving between channels while in edit mode.

**Config button:** From the main page, pressing Config enters the module configuration menu (presets, macros, clock source, touch sensitivity). While editing a channel, pressing Config enters that channel's configuration page (algorithm, clock divider, gate time, CV assignments, burst division). Since firmware V1.14.1, a long press on Config from the main page jumps directly to the preset page.

**Jacks:**

**A (Reset input):** A rising edge on this input resets all channels to their first step. Useful for synchronizing the lx-euclid to a phrase boundary in your system. Notably, the manual suggests self-patching: connecting one of the lx-euclid's own gate outputs to the reset input, so an internal channel can trigger phrase resets automatically.

**B (CV inputs, x4):** Four CV inputs freely assignable to any channel parameter. Each input accepts -5V to +5V. One CV input can be simultaneously assigned to multiple parameters across multiple channels. Assignments are configured per-channel in the channel config page.

**C (Clock input):** Accepts external clock when the module is set to external clock mode. Each rising edge advances all channels by one step. Per-channel clock dividers allow individual channels to run at slower subdivisions of the incoming clock.

**D (Gate outputs, x4):** One output per channel, color-matched to the channel buttons. Outputs are 0V when inactive and 10V when active. Gate length is configurable per channel in milliseconds and can optionally be randomized.

---

## Editing a Rhythm

Pressing a channel button enters that channel's edit pages. The lx-euclid uses a two-page edit structure per channel, plus a separate configuration page.

**Edit page 1 (first press of channel button):**
- Outer ring: sets the rhythm **Length** (total number of steps in the cycle)
- Inner ring: sets the number of **Beats** (how many steps in the cycle fire a trigger)

**Edit page 2 (second press of the same channel button):**
- Outer ring: sets **Probability** (how often each beat actually fires, from always to rarely)
- Inner ring: sets **Rotation** (shifts the entire pattern forward or backward through the cycle, changing where the first beat falls)

**Returning to main page:** A third press of the channel button returns to the main page. Pressing the Tap button also exits the edit page at any time.

**Switching channels:** While in any edit page, pressing a different channel button immediately jumps to that channel's edit pages without returning to the main page first.

**Channel configuration page:** Pressing the Config button while on any edit page opens additional parameters for that channel, selected using the inner ring. These include algorithm selection, clock divider, gate time, gate time randomization, CV assignments, and burst division. All channel parameters are saved to module memory and survive power cycles.

---

## The Four Algorithms

The lx-euclid offers four variations on the Euclidean distribution algorithm. The standard algorithm distributes beats as evenly as possible across the cycle. The three alternative algorithms modify how evenly that distribution is spaced, which shifts the perceived groove and accent placement of the pattern.

| Algorithm | How beats are distributed | Character |
|-----------|--------------------------|-----------|
| **Linear Euclidean** | As evenly as possible across the full cycle | Balanced, symmetrical feel; the classic Euclidean sound |
| **Exponential Euclidean** | Beats accumulate toward the beginning of the cycle | Front-heavy; accents land early, trailing off toward the end |
| **Inverse Exponential** | Beats accumulate toward the end of the cycle | Back-heavy; anticipation builds, resolves at the end of the phrase |
| **Symmetric Euclidean** | First half Exponential, second half Inverse Exponential | Mirrored; accents cluster at the center of each half, creating a rocking feel |

For a deeper exploration of how algorithm choice interacts with polyrhythmic layering across multiple channels, see the sequencing guide (forthcoming).

---

## CV Assignments

Each of the four CV inputs can be assigned to any of the following parameters for any channel. One CV input can serve multiple destinations simultaneously, which lets a single modulation source affect several channels at once.

| Target | Behavior |
|--------|----------|
| **Reset** | Rising edge resets that channel to its first step |
| **Length** | CV shifts the number of steps in the cycle |
| **Beats** | CV shifts the number of active beats |
| **Rotation** | CV shifts the pattern offset position |
| **Probability** | CV shifts the probability value |
| **Fill** | Voltage above 1V forces every step to fire (all beats on) |
| **Mute** | Voltage above 1V silences the channel completely (no triggers output) |
| **Burst** | Voltage above 1V triggers burst mode; channel stays in burst until CV drops below 1V |

Fill and Mute have binary behavior: below 1V they have no effect, above 1V they switch the channel state entirely. This makes them well suited to gate signals and trigger pulses as much as continuous CV. Burst via CV is identical in behavior to burst triggered through the macro system.

Assigning CV to Length and Beats simultaneously, driven by the same source, creates patterns that expand and contract together as the CV changes. Assigning a slow LFO to Rotation creates a pattern that gradually shifts its phase relationship to everything else in your patch.

---

## Burst Mode

Burst mode temporarily accelerates a channel's clock rate until the multiplied rhythm and the original rhythm naturally re-align on the same step. Understanding what that means makes burst far more useful than it first appears.

When burst is triggered on a channel, that channel begins firing its pattern at a multiplied tempo: 2x, 3x, 4x, 6x, or 8x the incoming clock rate (set in the channel config under Burst Div). The channel continues running at that multiplied rate, playing through its full Euclidean pattern faster, until a step arrives where both the fast version and the normal version would land on step 1 simultaneously. At that point, burst ends and the channel returns to normal clock rate, back in phase with the rest of the system.

This phase-locking behavior means burst does not create timing chaos. The channel accelerates, runs for however many cycles it takes to realign, and snaps back cleanly. Shorter patterns with smaller multipliers realign quickly. Longer patterns with larger multipliers can run in burst for several full cycles before locking back.

Burst can be triggered three ways: through the macro system (touch the ring while macro is set to Burst), through CV assignment (voltage above 1V on the assigned CV input), or through the channel configuration page for testing.

The Burst Div options (2, 3, 4, 6, 8) are multipliers of the incoming clock. At 24 PPQN with the clock divider set to /6 (for 16th note triggering), a burst multiplier of 4 produces 64th note fills for the duration of the burst.

---

## The Macro System

The Macro system is where the lx-euclid becomes a live performance instrument rather than just a sequencer you program and leave running. It lets you assign functions to the inner ring and outer ring as they appear on the main page, so a single ring gesture can affect the rhythm in real time without entering any edit page.

**Setting up a macro:** Enter the Config menu from the main page, then select Macro. Choose whether to assign the macro to the Inner Ring or the Outer Ring. Select the function to assign to that ring. Then select which channels the macro affects (one or more).

**Standard macro functions:** None, Reset, Length, Beats, Rotation, Probability, Fill, Mute. When one of these is assigned to a ring, scrolling the ring on the main page adjusts that parameter on all selected channels simultaneously. This allows real-time control of beat density, pattern length, probability, or phase offset across multiple channels with a single finger movement.

**Special performance functions (Reset, Fill, Mute, Burst):** These four functions work differently from the others when assigned as macros. Rather than scrolling a value, they respond to where on the ring you touch. The ring is divided into four positions corresponding to the four channels:

- Touch at the top (12 o'clock): affects Channel 1
- Touch at the right (3 o'clock): affects Channel 2
- Touch at the bottom (6 o'clock): affects Channel 3
- Touch at the left (9 o'clock): affects Channel 4

This means with Fill assigned to a ring, touching the top of the ring instantly fills Channel 1, touching the right fills Channel 2, and so on. The same applies to Mute: instant per-channel muting from the main page without entering any menu. Reset fires an immediate channel reset at the touched position.

Burst via macro is triggered by touching the ring at the channel's position. The number of burst cycles triggered corresponds to how many times you touch that position on the ring.

A practical performance setup: assign Fill to the outer ring (quick all-steps-on for any channel) and Mute to the inner ring (instant silence per channel). From the main page you can then mute any channel, fill any channel, or both, all with ring touches while the sequence plays.

---

## Presets

The lx-euclid stores 8 preset slots. Each preset captures the following per-channel parameters: Length, Beat count, Rotation, Probability, Clock divider, Gate time, Gate time randomization, and Algorithm. All other settings (clock source, macro assignments, touch sensitivity) are saved as global state and recalled automatically on every power-up.

**Accessing presets:** From the main page, press Config to enter the config menu, then select Presets. A long press on Config since firmware V1.14.1 jumps directly to the preset page. The inner ring selects which preset slot to load.

**Saving a preset:** On the preset page, press Config again. Use the inner ring to select the destination slot. The current state saves to that slot.

**Preset recall modes:** The lx-euclid offers four modes for how presets are recalled, selectable from the preset page by pressing Config a third time:

**Direct with reset:** The preset loads immediately when you touch the ring next to it. All internal counters reset and every rhythm restarts from its first step. Use this when you want a clean, synchronized transition.

**Direct without reset:** The preset loads immediately but all rhythms continue running from their current positions. The pattern changes, but the phase does not. Use this for smooth transitions where sudden restarts would be disruptive.

**On external reset:** Touching the ring next to a preset arms it for recall. The preset loads when the lx-euclid receives a pulse on the Reset input jack. This allows you to time the transition precisely from elsewhere in your patch, for example from a clock divider output that fires at the start of every 8-bar phrase.

**On internal reset:** Touching the ring next to a preset arms it for recall. The preset loads when the Tap button is held and then released. This keeps the transition entirely on the module without requiring any additional patching.

---

## Clock Source and Touch Sensitivity

**Clock source** is set in the Config menu under More.

**Internal:** The lx-euclid generates its own clock. Tap tempo sets the BPM on the main page. Since firmware V1.14.1, BPM can also be set numerically: the inner ring provides fine BPM adjustment and the outer ring provides coarse adjustment while on the main page in internal clock mode.

**External:** Each rising edge on the Clock input jack advances all channels by one step. The tempo is entirely determined by whatever is driving the clock input. This opens the possibility of non-linear clocking: if your clock source is not perfectly steady (a shuffled or swung clock, an irregular gate sequence), the lx-euclid follows it step by step.

**Clock division and PPQN:** The lx-euclid advances one step per clock pulse. Many common clock sources (Pamela's PRO Workout, OXI One) run at 24 PPQN by default. At 24 PPQN, you need to divide by 6 in the per-channel clock divider to get 16th note triggering. Available dividers are /1 (no division), /2, /3, /4, /6, /8, and /16.

**Touch sensitivity** is adjustable in the Config menu under More. Three settings are available: High, Mid, and Low. If the rings are responding to unintended touches, lower the sensitivity. If they require firm pressure to register, increase it.

---

## Why the lx-euclid Excels

The lx-euclid does something unusual: it takes a mathematically rigorous concept (Euclidean rhythm distribution) and makes it tactile and immediate through an interface that most modules do not attempt.

**The touch ring interface changes what rhythm editing feels like.** Step sequencers require iterating through buttons. The lx-euclid lets you set a length by running a finger around the outer ring once, set beats by running a finger around the inner ring once, and land on a working pattern immediately. For musicians who think in terms of groove and density rather than numbered steps, this is not a cosmetic difference; it is a fundamentally different relationship with the sequencer. Editing happens in seconds by feel rather than in seconds by counting.

**Four algorithms, not one.** Most Euclidean sequencers offer one distribution: the Linear algorithm, which spreads beats as evenly as mathematics allows. The lx-euclid offers three additional algorithms that alter where beats cluster while keeping the total beat count identical. Exponential accumulates beats at the beginning of the pattern. Inverse Exponential accumulates them at the end. Symmetric alternates between the two halves. The same "three beats in eight steps" produces four rhythmically distinct patterns across the four algorithms. This turns the algorithm parameter into a groove character control, not just a mathematical property.

**Burst mode as phase-locked clock multiplication.** Standard burst modes in other modules fire a set number of triggers and stop. The lx-euclid's Burst mode runs the affected channel at a multiplied clock rate -- 2x, 3x, 4x, 6x, or 8x -- until the accelerated rhythm and the original rhythm complete a full cycle and align on the same step simultaneously. The burst ends at a musically coherent point, not at an arbitrary trigger count. This phase-locking behavior means that Burst adds energy and acceleration to a rhythm without ever introducing timing chaos.

**The Macro system scales live performance.** Touch gestures on the outer ring during performance map to per-channel Fill, Mute, Reset, and Burst simultaneously based on which compass position you touch. Four channels can be controlled with a single ring gesture. Combined with preset recall tied to internal or external reset, the lx-euclid supports live set structures where full rhythm changes happen at phrase boundaries without requiring manual parameter editing during performance.

**Probability as an organic variation tool.** Setting a channel to less than 100% probability does not randomly drop beats in an unpatterned way. Because the beat positions are Euclidean, the remaining beats when some drop out still tend to fall in musically coherent positions. The randomness adds variation without completely destroying the rhythmic feel. Combined with touch sensitivity (which introduces micro-variations), the lx-euclid can generate patterns that resist the machine-rigid quality of strictly deterministic sequencers.

---

## Patch Examples

### Patch 1: Four-Channel Drum Pattern with Independent Subdivisions

A foundational patch demonstrating Euclidean rhythm generation across a complete drum kit, with clock division creating multiple simultaneous time feels.

```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

Pamela's PRO Workout ──[G] 24 PPQN──► lx-euclid CLOCK IN

lx-euclid CH1 OUT ──[G]──► Kick trigger in     (CH1: /6 divider, 5 beats / 16 steps)
lx-euclid CH2 OUT ──[G]──► Snare trigger in    (CH2: /6 divider, 3 beats / 16 steps)
lx-euclid CH3 OUT ──[G]──► Hi-hat trigger in   (CH3: /3 divider, 7 beats / 16 steps)
lx-euclid CH4 OUT ──[G]──► Percussion trigger  (CH4: /12 divider, 2 beats / 8 steps)
```

Set all four channels to external clock. CH1 and CH2 run at /6 (16th note resolution). CH3 runs at /3 (32nd note resolution) for a denser hi-hat pattern. CH4 runs at /12 (8th note resolution) for a slower accent voice.

Each channel's beat count determines the Euclidean density. Start with the numbers above, then experiment with algorithm selection per channel: Linear on the kick for symmetry, Exponential on the snare to front-load the accents, Inverse Exponential on the hi-hat for a pattern that builds toward the downbeat.

Adjust rotation on CH2 and CH4 to phase-shift them relative to CH1. Even a one or two-step rotation creates dramatically different groove relationships between the voices.

### Patch 2: Self-Patching: Sequence the Sequencer

Using one channel's output to modulate another channel's beat count, creating automatic rhythmic evolution without any external modulation source.

```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

External clock ──[G]──► lx-euclid CLOCK IN

lx-euclid CH1 OUT ──[G]──► lx-euclid CV INPUT 1
                            (CV1 assigned to CH2 Beats)

lx-euclid CH2 OUT ──[G]──► Drum voice trigger
lx-euclid CH3 OUT ──[G]──► Drum voice trigger
lx-euclid CH4 OUT ──[G]──► Drum voice trigger
```

Assign CV Input 1 to the Beats parameter of Channel 2. Set Channel 1 to a slow clock divider (/8 or /16) with a short pattern (4 or 8 steps) and extend the gate time so adjacent gates merge into a long continuous high signal. As Channel 1 fires and holds its gate, Channel 2's beat count is raised. When Channel 1 is between beats, Channel 2 returns to its base beat count.

The result is a Channel 2 pattern that automatically becomes denser during certain points in Channel 1's cycle and sparser during others. Channel 1 is effectively conducting Channel 2's density without any external module. Add a slow LFO into CV Input 2 assigned to Channel 3's Rotation for a pattern that simultaneously shifts phase while CH2 shifts density.

### Patch 3: Macro-Driven Live Performance

Building a performance setup where the touch rings control fill and mute states in real time, with timed preset recall synchronized to phrase boundaries.

```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

External clock ──[G]──► lx-euclid CLOCK IN
Clock divider (phrase output) ──[G]──► lx-euclid RESET IN
                                        (fires at start of every 8 or 16 bars)

lx-euclid CH1-4 OUT ──[G]──► drum voices / sequencer triggers
```

Configure macros: assign Fill to the Outer Ring (affects all 4 channels), assign Mute to the Inner Ring (affects all 4 channels). On the main page, the outer ring now fills any individual channel by touching at its compass position (top=CH1, right=CH2, bottom=CH3, left=CH4). The inner ring mutes any channel the same way.

Set the preset recall mode to "On external reset." Arm a different preset by touching the ring next to it. The transition will fire precisely when the clock divider sends a reset pulse at the phrase boundary, so the new pattern locks in at the top of the next phrase rather than mid-pattern.

During performance: build tension by muting CH1 (kick) with a ring touch, fill CH3 (hi-hat) to increase density, then let the preset recall snap to a new rhythm configuration at the phrase change. The entire structural shift happens with two ring touches and a preset arm, all from the main page while the sequence plays.

---

## Common Mistakes

**1. Not connecting an external clock and expecting the module to sequence.**
The lx-euclid requires a clock signal to advance its channels. In external clock mode, nothing moves until a signal is patched into the Clock jack. In internal mode, the module generates its own clock, but this mode must be selected in Config. Many users patch outputs but forget the clock input entirely. If no pattern is advancing, check clock mode and clock presence before anything else.

**2. Confusing inner and outer ring functions on the two edit pages.**
Edit page 1 and edit page 2 assign the rings differently, and new users frequently work on the wrong page. On page 1: the outer ring sets the pattern length (number of steps) and the inner ring sets the number of beats. On page 2: the outer ring sets probability and the inner ring sets rotation (phase offset). Getting rotation when you want beats -- or length when you want probability -- means you are on the wrong page. Long-press the channel button to switch pages; the display shows which page is active.

**3. Missing the two-page edit system entirely and editing only page 1.**
Some users discover that the outer ring changes length and the inner ring changes beats, and stop there. The probability and rotation controls on page 2 are not prominently labeled on the panel and the manual buries them in the interface description. Page 2 is where much of the lx-euclid's variation capability lives: rotation shifts the phase of the pattern without changing its density, and probability introduces the organic variation that distinguishes lx-euclid patterns from strictly deterministic output. A guide that only uses page 1 is using half the module.

**4. Treating all four algorithms as minor variations of the same sound.**
Linear Euclidean is the algorithm most people discover first, and it sounds good immediately. The other three (Exponential, Inverse Exponential, Symmetric) sound clearly different and alter the groove character of the same beat and length values in ways that feel like different rhythmic traditions. If you have been running Linear exclusively, spend a session setting identical Beat and Length values across all four channels with one algorithm per channel. The contrast is substantial and immediately musical.

**5. Setting Burst without understanding when it ends.**
Burst mode does not end after a fixed number of triggers. It ends when the accelerated version of the pattern and the original pattern complete a full cycle and realign on the same beat. For some Burst division and pattern length combinations, this means Burst runs for several bars before ending. If your Burst seems to go on far longer than expected, this is the phase-locking logic working as designed. To keep Bursts short, choose Burst divisions that divide cleanly into your pattern length.

---

## Pairs Well With

**Clock sources with PPQN output:** The Pamela's PRO Workout (explicitly referenced in the lx-euclid manual) outputs 24 PPQN, which pairs directly with the per-channel clock dividers. Set the lx-euclid's channel dividers to /6 for 16th notes, /3 for 32nd notes, or /12 for 8th notes from the same master clock.

**CV sequencers and random sources:** With four freely assignable CV inputs covering Length, Beats, Rotation, Probability, Fill, Mute, and Burst, almost any CV source becomes a rhythmic modulation tool. A slow LFO into Rotation creates phase drift. A stepped random into Beats creates evolving density. A Turing machine into Probability creates patterns that vary from performance to performance without ever fully changing.

**Drum voices with individual trigger inputs:** The lx-euclid outputs 10V gates, which are compatible with virtually all Eurorack drum modules. The BLCK_NOIR and Queen of Pentacles both accept the lx-euclid's outputs directly. With four channels covering kick, snare, hi-hat, and metallic voices, the lx-euclid covers the complete rhythmic structure of either drum module.

**Matrix mixers and attenuverters:** When using CV to modulate multiple channels simultaneously, a matrix mixer (the AtoVproject MMx2, also in the manual's patch ideas) lets you route one CV source to multiple destinations at different amounts. An attenuverter before any CV input lets you scale -5V to +5V sources into the positive-only ranges that parameters like Length and Beats respond to most musically.

---

## Advanced Learning Path

**Master one channel before expanding to four.** Set up a single Euclidean pattern on CH1 with an external clock, a drum module, and nothing else. Work through: length variations from 8 to 32 steps, beat density from 1 to length-1, all four algorithms at the same beat/length settings, rotation offsets on page 2, and probability below 100%. Understand each parameter's effect in isolation before combining them across channels. This single-channel study will be the most educational session you spend with the module.

**Build a four-algorithm comparison patch.** Set all four channels to identical beat and length values (try 3 beats in 8 steps), then assign one algorithm per channel. Route all four to different drum voices. Listen to how the same mathematical distribution produces four rhythmically distinct grooves. This comparison makes the algorithm parameter's musical function viscerally clear in a way that no description can match.

**Study Euclidean rhythm theory alongside the module.** Godfried Toussaint's 2004 paper "The Euclidean Algorithm Generates Traditional Musical Rhythms" is freely available and readable without a mathematics background. Understanding why the algorithm produces the patterns it does -- and why those patterns correspond to musical traditions around the world -- deepens the intentionality of every patch decision. The lx-euclid is not just a sequencer; it is an implementation of a specific theory of what makes rhythm feel natural.

**Build the Macro system before a live performance.** Map compass positions to the actions you need: typically North for fill on all channels, South for mute on all channels, East/West for channel-specific burst or reset. Rehearse the gestures until they are reflexive. The Macro system has the most performance value when it is muscle memory, not a feature you are consciously recalling during a set.

**Combine with preset recall for live set structure.** Store eight distinct groove variations (different algorithms, densities, or lengths per channel) in the eight preset slots. Configure preset recall to trigger on phrase boundaries using an external reset signal. This creates a live sequencing architecture where groove changes happen at musically coherent points -- the end of a 32-step phrase, the beginning of a new section -- driven by the music itself rather than manual preset recall.

**Cross-reference with the Pamela's PRO Workout guide.** The manual explicitly uses Pamela's as the reference clock source. Reading the PRO Workout guide alongside this one explains the 24 PPQN clock division relationship in depth and gives additional context for how clock multiplication and division interact across both modules simultaneously. The two together form a strong rhythmic foundation for systems of any complexity.
