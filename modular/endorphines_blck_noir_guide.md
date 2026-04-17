---
title: Endorphin.es BLCK_NOIR
manufacturer: Endorphin.es
primary_role: SOURCE
secondary_roles: [SHAPER]
form_factor: eurorack
functions: [drum-voice]
behavior_tags: [percussive, gated, dirty, warm, harmonic, performance-oriented]
use_cases: [rhythmic percussion layer, analog drum voice set, full drum kit synthesis]
hp: 30
memory: basic
screen: true
hybrid: true
---

# Endorphin.es BLCK_NOIR Guide

**Analog Drum Synthesizer**  
**Manufacturer:** Endorphin.es  
**Format:** Eurorack  
**Width:** 30HP | **Depth:** <20mm | **Power:** +12V: 240mA / -12V: 75mA / +5V: not used  
**Firmware:** V.4 "Total Nightmare" (default as of this writing)

![Endorphin.es BLCK_NOIR](https://github.com/Shadoe-42/music/raw/main/modular/images/endorphines/blck_noir/front_panel.jpg)  
*30HP analog drum synthesizer with 7 voices across 5 channels, hybrid digital-noise-into-analog-circuit generation, THROTTLE isolator filter, and the Cabin Pressure effect processor. Voices are arranged in ascending frequency order from left to right.*

---

## What Is an Analog Drum Synthesizer?

A drum synthesizer generates percussive sounds from scratch using electronic circuits rather than recordings. There are no audio samples inside the BLCK_NOIR. Every kick, snare, and cymbal is created live by the module's circuits each time a trigger arrives.

The BLCK_NOIR uses a hybrid approach: it generates two varieties of electronic noise (white noise and metallic noise) using a high-quality digital process running at 90 kHz, then injects that noise into fully analog signal paths built around inductor coils rather than standard op-amp circuits. The inductors give the module its particular character, a dense quality associated with vintage drum machines that used similar construction.

This approach gives the BLCK_NOIR personality that differs from "accurate" digital drum sample playback. The sounds have physicality and respond to how you tune, modulate, and mix them. That character is the point. The manual describes the module as specifically tuned for darkwave and techno, though the voices cover enough ground to work in many styles.

---

## Historical Context

The BLCK_NOIR's circuit design traces directly to the Roland CR-78 CompuRhythm, released in 1978. The CR-78 was the first drum machine to offer full programmability by the user, a shift that changed how rhythm machines were understood and marketed. Its architecture combined a digital microcontroller for timing and pattern storage with discrete analog voice circuits, and those voice circuits used inductor coils as key filtering components. Inductors store and release electromagnetic energy differently than the resistor-capacitor circuits that dominate most analog designs, producing denser transients and a particular low-mid saturation that became the sonic signature of that generation of Roland hardware. The CR-78 fed directly into the TR-808 (1980), which carried forward similar design principles while expanding the voice count and programmability. The BLCK_NOIR's inductor-based noise circuits are a deliberate continuation of that electrical lineage rather than an approximation of its sound.

The gated reverb effect built into the DARKWAVES processor bank has its own history worth knowing. In 1980, engineer Hugh Padgham was working at Townhouse Studios in London on Peter Gabriel's third album alongside producer Steve Lillywhite. An SSL console's talkback circuit, left open during a session, was picking up the room ambience around Phil Collins's drum kit, then compressing and gating it through the console's dynamics processing. The result was a reverb tail that bloomed and then cut off abruptly rather than decaying naturally. Padgham and Lillywhite recognized what they were hearing and developed the technique deliberately; the track "Intruder" was the first recorded use. Collins then brought the same approach to his 1981 solo single "In the Air Tonight," where the technique became one of the most imitated drum sounds in popular music. The BLCK_NOIR's Gated Reverb effect in the DARKWAVES bank is a direct implementation of that sound: a reverb body gated by a threshold, with CABIN FEVER setting the decay and the secondary function setting the gate threshold.

---

## Architecture Overview

The BLCK_NOIR has 7 drum voices organized into 5 channels. Understanding which voices share a channel matters before patching, because shared channels cannot be fully separated.

**The 5 channels:**

Bass drum (bd) occupies its own channel. It is the only fully analog voice, generated from a tuned resonant circuit rather than noise injection.

Snare drum (sd) has its own channel. It uses two components: a body (analog resonant circuit, fixed decay) and a rattle layer (noise injection, adjustable decay via SD TAIL).

Tambourine (tb) has its own channel. Pure noise-based voice filling the frequency gap between snare and hi-hats.

Hi-hat (hh) is one channel shared by two voices: closed hi-hat (ch) and open hi-hat (oh). They share the same velocity input, volume fader, and individual output jack. They cannot be separated or routed independently.

Metallic (mb/cy) is one channel shared by two voices: metallic beat (mb) and cymbal (cy). Same shared channel structure as hi-hat. They cannot be separated.

**Frequency spectrum design:** The voices are arranged on the panel in ascending frequency order from left to right. Bass drum sits lowest (40-100 Hz), then snare (100-380 Hz plus higher harmonics), tambourine (around 5 kHz), closed and open hi-hats (around 8 kHz), then metallic beat and cymbal (around 9 kHz). This architecture ensures the voices occupy distinct spectral bands and do not mask each other in a mix, which is why even a minimal BLCK_NOIR patch tends to sound clear and usable without additional EQ.

---

## Triggering Your Drums

Each voice receives triggers through dedicated inputs at the bottom of the panel. The inputs accept standard V-trigger signals (0...+5V or 0...+10V pulses) with a 0.65V threshold. Minimum trigger length is 1ms, though 10ms is recommended for reliable triggering across all sequencers and sources.

**Velocity CV (pre-fader VCA):** Every voice channel has a velocity input above the trigger input. This input controls amplitude before the channel's manual volume fader, functioning as a VCA. The range is 0...+5V. At 0V the drum is silent. At +5V it plays at full amplitude. When nothing is patched into the velocity jack, that channel defaults to full volume automatically. Patching a CV source gives you dynamic control over each hit. The manual suggests thinking of this input as either a velocity control (for accent and dynamics) or an envelope input (for shaping how the level evolves within a hit). Any CV source in the 0...+5V range works: LFOs, S&H outputs, sequencer CV lanes, or envelopes.

**Drum launch buttons:** Each voice has a physical button on the panel. What these buttons do depends entirely on whether a cable is patched into the CLOCK IN ** jack. This is covered in its own section below. When no clock is patched, pressing a button fires a single shot of that voice. This is useful during patch setup for auditioning sounds without requiring a running sequence.

---

## Per-Voice Parameters

### Bass Drum (BD)

The bass drum is the deepest voice and the only one generated entirely from an analog resonant circuit without noise injection.

**BD TUNE** sets the pitch of the drum body. This is a manual-only control with no CV input. Turning CCW lowers the tuning toward 40 Hz; turning CW raises it toward 100 Hz. Think of this as the tension of the drum membrane.

**BD TAIL** sets the decay length of the drum. CCW gives the shortest decay; CW extends it up to approximately 1 second. A CV input (0...+5V) is available, with the manual knob acting as an attenuator when CV is present. Longer tail values produce more sustained, sub-bass kicks; shorter values produce punchy attacks with minimal sustain.

**Volume fader:** The BD channel fader has extra headroom behavior above approximately 2 o'clock. Past that point the bass drum output begins to saturate in the final mono and stereo outputs (not the individual output). This saturation adds density and harmonic content, making the kick cut harder at louder levels. Use this as a character control rather than just a volume control.

### Snare Drum (SD)

The snare consists of two independently behaving components: a body and a rattle (snares).

**SD TUNE** sets the pitch of the snare body. Manual only, no CV. CCW tunes the body toward 100 Hz; CW toward 380 Hz. The body decay is fixed and cannot be adjusted. When SD TAIL is at full CCW (snares completely decayed), the body alone is audible, and the drum sounds like a tom rather than a snare.

**SD TAIL** controls the decay of the rattle/noise component only, not the body. CCW gives the shortest rattle decay (body-only sound); CW extends the rattle up to approximately 1 second. CV input is 0...+5V with the knob as attenuator.

A practical starting point the manual suggests: SD TAIL at around 11-12 o'clock (moderate rattle decay) with SD TUNE at full CW gives a snappy, focused sound. Pushing THRUST (see next section) toward CW adds a metallic character reminiscent of anvil hits. Pushing SPOILER toward CW with SD TUNE at maximum produces a clap-like texture, particularly when mixed with tambourine.

### Tambourine (TB)

The tambourine is a pure noise-based voice with no dedicated tune control beyond the global THRUST and SPOILER knobs. Its role in the mix is to fill the frequency gap between the snare and hi-hats, adding rhythm and texture in the 5 kHz range. It can also function as a low-tuned open hi-hat or a shaker-type sound depending on THRUST position.

### Closed and Open Hi-Hats (CH/OH)

The hi-hats use a feature called hi-hat link: playing a closed hi-hat after an open hi-hat shuts off the open hi-hat, exactly as a real hi-hat pedal closes the cymbals. This behavior animates the hi-hat pattern and makes it sound more realistic when the two voices are interleaved in a sequence. The length of both voices is fixed (set during development to suit most musical styles).

Because CH and OH share the same velocity input, volume fader, and individual output jack, any dynamics applied to the hi-hat channel affects both simultaneously. They cannot be processed independently from within the module.

### Metallic Beat and Cymbal (MB/CY)

The metallic beat is a sharp accent sound derived from metallic noise injection. It functions well as a rimshot, a ride cymbal accent, or a supplementary hi-hat line. The cymbal is a longer-duration version of the same metallic character with a softer attack, suitable for china, crash, splash, or ride roles.

Like hi-hats, MB and CY share a velocity input, volume fader, and individual output. They cannot be separated.

---

## THRUST and SPOILER: The Global Noise Shapers

Six of the seven drum voices (everything except the bass drum) are generated using noise injection into analog circuits. The BLCK_NOIR contains two noise sources: white noise and metallic noise. THRUST and SPOILER are global controls that shape these noise sources for all six voices simultaneously.

**THRUST** controls the balance between white noise and metallic noise across the kit. This is the single most important tonal character control on the module.

At full CCW, the snare, tambourine, closed hi-hat, and open hi-hat receive white noise injection (clean, bright, flat-spectrum noise), while the metallic beat and cymbal receive metallic noise injection. This is the default frequency-appropriate assignment.

As THRUST moves toward CW, the balance shifts: the snare, tambourine, and hi-hats gradually receive more metallic noise, while the metallic beat and cymbal receive more white noise. At full CW, the character of the entire kit inverts from its default.

This means THRUST is not just a tone control for one voice. A small THRUST adjustment changes the character of six voices at once. Modulating THRUST with a slow LFO or a CV sequence gradually shifts the kit from clean and white to harsh and metallic over time, which is one of the most effective ways to add movement to a looping drum pattern without changing any triggers.

**SPOILER** reduces the sample rate of both noise sources. At full CCW the noise generators run at 90 kHz (clean, flat spectrum, no aliasing). Turning CW progressively lowers the sample rate, introducing digital artifacts and eventually reducing the noise to crackles and distortion. Both CV inputs (THRUST CV and SPOILER CV) accept 0...+5V signals, with the manual knobs functioning as attenuators when CV is present.

A useful distinction: THRUST changes the *character* of the noise (white versus metallic spectrum), while SPOILER changes the *quality* of the noise (clean versus degraded). Used together they give a wide range of drum textures from pristine to deliberately broken.

---

## Output Routing

**Individual outputs:** Five individual jacks at the top of the panel provide post-fader audio for bd, sd, tb, hh (ch+oh combined), and mb/cy (combined). Patching a cable into any individual output **disconnects that voice from the final mix**. This is the same behavior as the Queen of Pentacles and is intentional. The individual output is for external processing: running the kick through a dedicated compressor, sending the snare to an external reverb, routing voices into a separate mixer for individual EQ. Once a cable is inserted, that voice is no longer in the internal mix.

If you want a voice to go to both an external processor and the final mix, use the AUX IN input to return the processed signal to the mix path.

**AUX IN:** The small trim knob labeled AUX INPUT LEVEL adjusts the gain of the mono auxiliary input. At full CCW it accepts modular-level signals (approximately +/-5V). At full CW it accepts line-level signals (approximately 1Vpp). This input also feeds through the THROTTLE filter and exits at the main outputs, meaning anything patched into AUX IN is processed by THROTTLE and FLAPS along with the drum mix. The AUX IN jack is also the input for firmware updates delivered over audio.

**Final mix outputs:** The module provides two final mix outputs. MONO MIX outputs at approximately +/-5V (modular level). STEREO MIX outputs at approximately +/-1V (line level, suitable for mixers and audio interfaces). Both outputs are affected by THROTTLE and FLAPS.

**THROTTLE:** A bipolar DJ-isolator-style filter applied to both final outputs. With the knob centered, the output is clean and unfiltered. Turning CCW applies a low-pass filter, attenuating high frequencies. Turning CW applies a high-pass filter, attenuating low frequencies. A CV input (0...+5V) is available. This is a 12 dB/octave zero-delay state-variable filter with intentional character. Caution: turning THROTTLE fully CCW or fully CW cuts the relevant frequencies entirely, which can result in complete silence. Use gradual adjustment, especially in a live setting.

**FLAPS:** The resonance control for THROTTLE. At low settings, FLAPS adds presence and a gentle peak at the filter cutoff frequency. At high settings, FLAPS can produce self-oscillation and an extremely loud high-frequency whistle capable of damaging speakers and hearing. Treat FLAPS as a tone shaping tool rather than a swept parameter. CV input is 0...+5V.

---

## CLOCK IN ** : Fills, Rolls, and Sample-and-Hold

The CLOCK IN ** jack changes the behavior of the drum launch buttons when a cable is present. This dual-mode behavior is easy to miss and genuinely useful once understood.

**Without a clock patched:** Each drum launch button fires a single trigger of that voice (tap) and holds the trigger open while held (gate). This is useful for auditioning drum sounds during patch building, or as a manual performance tool for accent hits.

**With a clock patched:** The behavior changes entirely. The CLOCK IN ** jack accepts a standard clock signal (gate/trigger, 0...+5V). With a clock present, pressing a drum launch button activates fill/roll mode for that voice: each incoming clock pulse fires that drum automatically. As long as the button is held, the drum fires on every clock tick. Releasing the button stops the rolls and returns to normal sequencer-driven triggering for that voice. Holding a button longer provides a momentary mute: incoming triggers for that voice are suppressed.

This means CLOCK IN ** at a faster division than your main sequence creates fills of different densities. At 24 PPQN from a sequencer running standard divisions, the most useful clock inputs are:

- PPQN divided by 3: 1/32nd note fills
- PPQN divided by 6: 1/16th note fills  
- PPQN divided by 12: 1/8th note fills
- PPQN divided by 24: 1/4 note fills

**Sample and Hold CV output:** While a clock is patched into CLOCK IN **, the module generates a stepped random CV signal on every clock pulse in the range 0...+5V. This output is available from the clock section and can be used anywhere in your patch as a free random modulation source. Using this S&H output to animate velocity or THRUST CV turns a static clock connection into an additional modulation resource without any extra modules.

---

## Effect Processor (Cabin Pressure)

The BLCK_NOIR includes the same Cabin Pressure effect processor found in the Endorphin.es Queen of Pentacles and Grand Terminal. If you have any of those modules, the effect system works identically here.

The processor hosts 16 effects in two banks of 8. The default bank is DARKWAVES, which contains 8 effects optimized for percussive material. The alternate bank is AIRWAYS, which contains 8 ambient effects originally designed for the Grand Terminal. Both banks can be loaded via firmware update over audio.

**How the processor works:** Effects are applied to the final drum mix (and anything patched into AUX IN) before the main outputs. Each voice has a toggle switch on the panel labeled ENABLE TO FX. Voices with the switch in the right position are sent through the effect; voices with it in the left position bypass the effect and go directly to the output. Alternatively, holding the TYPE button for more than 1 second enables effects on all voices simultaneously regardless of toggle switch positions.

**Cabin Pressure knob:** Controls the dry/wet balance. Full CCW is completely dry. Full CW is 100% wet (fully processed). The corresponding CV input accepts bipolar -5V...+5V; inserting a CV plug causes the Cabin Pressure knob to function as an attenuator for the incoming CV rather than as a direct dry/wet control.

**Cabin Fever knob:** Controls a secondary effect parameter that varies by effect type (see tables below). A CV input (0...+5V for CV, 0...+5V for gate or clock) is available.

**TAP button:** Acts as a tap-tempo clock for time-based effects (delays). Short press sends a tap. Holding longer than 1 second enters secondary mode for the Cabin Fever knob. The LED blinks once to confirm entry; hold again for 1 second to return to primary mode.

**Effect selection:** Short press the TYPE button to cycle through effects 1-8. The HAL9000 LED blinks to indicate the selected effect: green blinks for effects 1-4 (one blink = effect 1, two = effect 2, three = effect 3, four = effect 4), red blinks for effects 5-8 (one red blink = effect 5, and so on up to four red blinks for effect 8).

### DARKWAVES Bank (Default: Drum-Oriented Effects)

| # | Effect | Cabin Pressure | Cabin Fever (Primary) | TAP Button |
|---|--------|---------------|----------------------|------------|
| 1 | Gated Reverb | Reverb dry/wet | Decay of the reverb | Long hold: enter secondary (noise gate threshold) |
| 2 | Spring Reverb | Reverb dry/wet | Decay of the reverb | Short press: pluck spring exciter. Long hold: enter secondary (spring excitement decay) |
| 3 | Reversed Reverb | Pre-delay time / dry-wet | Reverb decay/feedback | Long hold: enter secondary (damping/tail volume) |
| 4 | Flanger | Amount of delay | LFO range | Long hold: enter secondary (feedback amount, 100% default) |
| 5 | Ring Modulator | Modulation amount | Modulator frequency rate | Long hold: enter secondary (feedback amount, 50% default) |
| 6 | Overdrive | Drive amount | Tone control | Short press: bypass on/off (latch). CV accepts gate/trigger for bypass |
| 7 | Compressor | Threshold (-90dB to 0dB) | Ratio (1:1 to 25:1) | Long hold: enter secondary (compressor attack, 1-100ms) |
| 8 | Freezer/Looper | Playback speed | Granule size (bipolar) | Short/long press: enable audio freezing |

**On Gated Reverb:** This is the signature 1980s drum reverb sound (Phil Collins, Peter Gabriel). A reverb tail is applied and then cut off by a noise gate at a defined threshold. The result is a reverb that adds size without the long tail muddying the mix. CABIN PRESSURE sets the wet amount; CABIN FEVER sets the reverb decay (size of the reverb body). The secondary CABIN FEVER function sets the noise gate threshold, from 0 (gate always open, continuous reverb) to maximum (only the loudest peaks trigger the reverb opening). Default threshold is 20%.

**On Freezer/Looper:** TAP or a gate into the CABIN FEVER CV input triggers the freeze. CABIN PRESSURE controls playback speed (full CCW is 5x slower, center is normal speed, full CW is 5x faster). CABIN FEVER controls granule size: center is smallest grain, CW up to 2 seconds forward, CCW up to 2 seconds in reverse.

### AIRWAYS Bank (Alternate: Ambient Effects)

| # | Effect | Cabin Pressure | Cabin Fever (Primary) | TAP Button |
|---|--------|---------------|----------------------|------------|
| 1 | Hall Reverb | Decay / hall size | Hi-pass filter at reverb input (50% default) | Long hold: enter secondary |
| 2 | Shimmer Reverb | Decay of the reverb | Pitch-shifter vs reverb mix (40/60 default) | Long hold: enter secondary |
| 3 | Room Reverb | Decay / room size | Stereo spread (maximum default) | Long hold: enter secondary |
| 4 | Plate Reverb | Decay of the reverb | Pre-delay amount (maximum default) | Long hold: enter secondary |
| 5 | Spring Reverb | Decay of the reverb | Spring excitement decay (maximum default) | Short press: spring excitement. Long hold: enter secondary |
| 6 | Ping-Pong Delay | Delay feedback amount | Clock divider for delay frequency (1/1 default) | Short press: tap tempo. Long hold: enter secondary |
| 7 | Tape Echo | Tape speed | Clock divider for delay frequency (1/1 default) | Short press: tap for feedback. Long hold: enter secondary |
| 8 | Chorus | Feedback amount | Modulation depth (100% default) | Long hold: enter secondary |

---

## Why the BLCK_NOIR Excels

The BLCK_NOIR occupies a specific position in the eurorack drum landscape: fully analog voice generation, 7 voices in 30HP, with deliberate frequency spectrum engineering and a global noise architecture that most drum modules do not attempt.

**Inductor-coil circuit design.** Standard analog drum circuits use op-amps throughout. The BLCK_NOIR uses inductor coils in the signal paths for the noise-based voices. Inductors store energy and release it differently than resistor-capacitor circuits, producing a denser transient character associated with vintage drum machines (specifically the CR-78 era of Roland hardware). This is not a sample of that sound; it is the same electrical behavior reproduced in circuit form. There is no software approximation involved.

**Frequency spectrum design across voices.** The five channels are tuned to complement each other: bass drum in the 40-100 Hz range, snare in the 100-380 Hz range plus harmonics, tambourine at approximately 5 kHz, hi-hats at approximately 8 kHz, metallic beat and cymbal at approximately 9 kHz. A kit running all voices together does not require additional EQ to avoid masking because the designers built spectral separation into the voice architecture itself. That separation is why even minimal BLCK_NOIR patches sound clear and usable immediately.

**THRUST and SPOILER as global noise color control.** Most drum synthesizers treat noise as a fixed ingredient. The BLCK_NOIR exposes the noise character architecture directly: THRUST shapes the white noise component across all six noise-based voices simultaneously, and SPOILER shapes the metallic noise component. Moving both knobs changes the tonal character of the entire kit in a single gesture. This is particularly useful with CV modulation: a single envelope routed to THRUST will animate the attack character of every noise-based voice together, creating a cohesive kit response to musical dynamics.

**Shared Cabin Pressure with the Queen of Pentacles.** The effect processor is identical to the one in the Endorphin.es Queen of Pentacles. Users who add a Queen of Pentacles to their system inherit the same effect knowledge immediately. The effect applies to the entire kit from a single set of controls, which encourages thinking about the kit as a sound rather than a collection of individual sounds.

**CLOCK IN ** dual function.** The CLOCK IN input does two different jobs depending on whether a sequencer clock is patched into it. With clock: manual launch buttons become fill/roll triggers that fire at clock divisions, and the output becomes a sample-and-hold CV source. Without clock: the buttons become preview and mute controls. A single jack delivers two entirely different performance tools depending on patch configuration. This is the kind of context-sensitive design that characterizes the module's overall approach.

---

## Patch Examples

### Patch 1: Basic Beat with Velocity Dynamics

A minimal starting patch demonstrating trigger routing and velocity as accent control.

```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

Sequencer/Clock ──[G]──► BD TRIG IN
Sequencer/Clock ──[G]──► SD TRIG IN
Sequencer/Clock ──[G]──► CH TRIG IN

Accent CV from sequencer ──[C]──► BD VELOCITY IN
                                   (0V = silent, 5V = full, unpatched = full)

BD INDIVIDUAL OUT ──[A]──► (external compressor or mixer channel)
MONO MIX OUT ──[A]──► main mixer
```

Start with THROTTLE centered (no filtering), FLAPS at minimum. Set BD TUNE to taste and BD TAIL to about noon for a medium kick. SD TAIL at 11-12 o'clock. No effects engaged. This establishes the dry signal path before adding complexity.

The key insight here is the velocity input behavior: unpatch the BD VELOCITY to hear the difference between full-volume-by-default and actively controlled dynamics. Then patch the accent CV and notice how even a modest 0-3V range versus 0-5V changes the perceived energy of the groove.

### Patch 2: THRUST Animation with S&H Modulation

Using CLOCK IN ** to generate free random CV that modulates THRUST, creating an evolving kit character without any additional modules.

```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

Main clock ──[G]──► CLOCK IN **
CLOCK IN ** S&H OUT ──[C]──► THRUST CV IN
                              (stepped random 0...+5V on each clock)

All drum triggers from sequencer ──[G]──► respective TRIG INs

STEREO MIX OUT ──[A]──► mixer stereo input
```

With a clock in CLOCK IN **, the S&H output generates a new random voltage on every clock pulse. Patching that directly to THRUST CV continuously and randomly shifts the noise color balance across all six noise-based voices. The kit subtly reshapes on every clock step without any pattern repetition.

Set THRUST knob to noon (attenuator position). The S&H output will sweep THRUST between 0 and +5V, covering the full CCW-to-CW range. Reduce the THRUST knob from noon to attenuate the modulation range if the variation is too extreme. Add slow SPOILER modulation from a separate LFO for additional texture degradation on top of the color shifting.

### Patch 3: Gated Reverb with Fill Mode

Combining the Cabin Pressure effect processor with CLOCK IN ** fill triggering for a classic production technique.

```
Signal types: [A]=Audio  [C]=CV  [G]=Gate

Sequencer clock ──[G]──► CLOCK IN **
                          (enables fill mode on drum launch buttons)

Main drum triggers ──[G]──► respective TRIG INs

THROTTLE CV IN ──[C]──► slow LFO (0...+5V)
                         (gradual high-pass sweep across the mix)

MONO MIX OUT ──[A]──► mixer
```

Select DARKWAVES effect 1 (Gated Reverb) using the TYPE button (one green blink). Set CABIN PRESSURE to about 2 o'clock (mostly dry with some reverb). Set CABIN FEVER to about 1 o'clock (medium reverb decay). Enable the SD toggle switch to send snare through the reverb; leave BD bypassed so the kick stays tight.

With a clock in CLOCK IN **, hold the SD drum launch button during a fill section. Every clock pulse fires the snare, creating a snare roll at the clock division rate. The gated reverb on each of those hits creates the characteristic 80s snare fill sound without washing out the overall mix. Releasing the button returns to normal sequencer-driven triggering instantly.

---

## Common Mistakes

**1. Patching triggers without a clock and expecting velocity dynamics.**
The VELOCITY inputs are sample-and-hold: they capture whatever CV is present at the moment a trigger arrives. With no clock in CLOCK IN **, the S&H output is static. With no external CV at the VELOCITY inputs, each voice fires at maximum volume. If all your drums hit at the same level, check that velocity sources are actually changing value and that the hold circuit is seeing those changes before the trigger arrives.

**2. Turning FLAPS past noon without watching the output level.**
FLAPS is resonance on the THROTTLE filter. Above about 2-3 o'clock, the filter approaches self-oscillation and can produce a loud high-frequency tone that exceeds eurorack levels. This is not a gentle rolloff situation; it crosses into damaging territory for monitors quickly. Set FLAPS slowly and watch your output metering. The manual explicitly warns about this.

**3. Patching an individual output and expecting to still hear that voice in the main mix.**
Plugging anything into an individual voice output (BD OUT, SD OUT, etc.) disconnects that voice from the main L/R and individual channel mix outputs. The behavior is intentional, identical to the Queen of Pentacles architecture, and completely silent until you understand it. If a voice disappears from your mix after patching its individual output, nothing is broken: route the individual output to your mixer or effect and bring it back that way.

**4. Leaving THRUST and SPOILER at noon and never exploring the noise architecture.**
Noon on both knobs is the balanced default, not the musically optimal position. The BLCK_NOIR's character lives in THRUST and SPOILER interaction. CCW on THRUST produces whiter, brighter noise; CW on SPOILER adds metallic edge. A full session exploring both knobs across the full range while listening to how the kit changes will reveal the actual design space of the module. Most users who describe the BLCK_NOIR as "not quite what they expected" have never moved these knobs significantly.

**5. Using CLOCK IN ** as a reset input.**
The CLOCK IN ** jack does not reset the sequencer or the module's internal state. It is a clock reference used for two things: setting the speed at which fill/roll buttons fire their triggers, and clocking the sample-and-hold output. Sending a reset pulse into it will be interpreted as a clock pulse, which may fire fills unexpectedly. Keep clock and reset functions on separate jacks; route your actual master clock here and your reset signals elsewhere.

---

## Pairs Well With

**Sequencers and pattern generators:** The BLCK_NOIR needs an external trigger source. Anything that outputs gates on multiple channels works: Winter Modular Eloquencer (the manual uses it in examples), Endorphin.es Shuttle Control (MIDI-to-CV/gate), or simpler options like the ALM Busy Circuits Pamela's PRO Workout for clock-derived rhythmic gates.

**The Endorphin.es Queen of Pentacles:** These two modules share the same effect processor, the same individual-output-disconnects-from-mix routing behavior, and the same Cabin Pressure / Cabin Fever / Cabin Fever CV control layout. The BLCK_NOIR is fully analog with noise synthesis; the Queen of Pentacles adds sample playback and different analog voice architectures. Together they form a complete percussion system with complementary character. Keep them as standalone patches since most users have one or the other; the shared knowledge transfers directly when you do have both.

**Attenuverters and offset modules:** THRUST and SPOILER CV inputs accept 0...+5V. If your modulation sources output bipolar signals (+/-5V), an attenuverter lets you shift and scale the range before it reaches THRUST or SPOILER. This expands what you can use as a modulation source without accidentally sweeping the parameter into extremes.

**External effects and mixers:** The individual outputs are post-fader and ready for external processing. A dedicated reverb on the snare, a compressor on the kick, or a separate delay on the hi-hats all become straightforward routing decisions once the individual outputs are understood.

---

## Advanced Learning Path

**Understand the noise architecture first.** Before pursuing complex patches, spend time with THRUST and SPOILER in isolation. Run only the hi-hats (CH/OH), remove all other triggers, and sweep both knobs across their full range while listening. Then do the same with just the snare. You are learning what "white noise dominant" and "metallic noise dominant" actually sound like on each voice. That understanding makes every subsequent patch decision more intentional.

**Learn the frequency spectrum by tuning each voice independently.** The TUNE controls on bass drum and snare affect pitch in ways that interact with the spectral design of the full kit. Finding the tuning range where each voice sits clearly in its intended band -- without bleeding into adjacent voices -- develops an ear for the module's design logic. This is also where the "physicality responds to tuning" character of inductor circuits becomes apparent versus sample playback.

**Build the Cabin Pressure vocabulary systematically.** The eight DARKWAVES effects and eight AIRWAYS effects each have distinct musical contexts. Rather than discovering them at random, work through them one session at a time: one effect at minimum, maximum, and medium CABIN PRESSURE on your working kit patch. Take notes on what CABIN FEVER adds to each one. By the end of sixteen sessions you will know which effects suit which musical situations rather than reaching for whatever sounds interesting.

**Introduce CLOCK IN ** as a performance tool.** Once the basic kit is stable, patch your sequencer clock into CLOCK IN **. Learn the exact behavior of each launch button with clock present: short press (fill at clock division), sustained hold (roll until released). Combine this with the S&H CV output: patch it to THRUST CV and watch how the THRUST parameter captures a new CV value with each fill trigger, then holds it until the next trigger arrives. This creates animated noise character during fills that returns to steady state between them.

**Route individual outputs through different effects chains.** Patch the BD OUT into a dedicated compressor. Patch the SD OUT into a separate reverb than the Cabin Pressure is providing. Listen to the difference between per-voice processing and the shared Cabin Pressure processor. The creative tension between individual control and global cohesion is where the BLCK_NOIR's system design becomes visible.

**Study alongside the Endorphin.es Queen of Pentacles documentation.** The two modules share architecture deliberately. Reading the Queen of Pentacles guide reveals additional perspective on why the Cabin Pressure processor is designed as it is, and gives context for the shared individual-output behavior. The vocabulary transfers directly.
