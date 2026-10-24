---
title: Joranalogue Fold 6
manufacturer: Joranalogue
primary_role: SHAPER
secondary_roles: []
historical_context: true
form_factor: eurorack
functions: [wavefolder, distortion]
behavior_tags: [harmonic, bright, nonlinear, sensitive, reactive, self-modulating]
use_cases: [west coast timbre shaping, harmonic enrichment of a sine wave, feedback wavefolding texture, waveshaping and distortion]
hp: 4
memory: none
transport: none
screen: false
hybrid: false
cv: full
patch_format: v1
---

# Joranalogue Fold 6

**Multi-topology wavefolder: six-stage hybrid series and parallel diode folding, voltage-controlled overdrive, and two simultaneous outputs in 4 HP**

![Joranalogue Fold 6](https://github.com/Shadoe-42/music/raw/main/modular/images/joranalogue/fold_6/front_panel.jpg)
*Joranalogue Fold 6: FOLD, SHAPE, and SYMMETRY knobs; two signal inputs; FOLD and SHAPE CV inputs; MAIN and ALT outputs*

> **Draft status (2026-10-24):** Written from the official Joranalogue manual (revision D, version 2023-06-26) before the module was in hand. Every specification and control description comes from that manual. All four patches are untested on hardware and are marked ⚠️. Open items to clear on hardware: (1) Depth is 40 mm per ModularGrid (manufacturer approved), while the manual lists 35 mm including the power cable and 52 mm outer depth; (2) all patch settings and every "What to listen for" result; (3) whether the FOLD and SHAPE knobs sum with incoming CV or scale it, which the manual does not state. Remove this block when the items are cleared.

---

## Historical Context

Wavefolding began in the Buchla 200 series, in the Model 259 Complex Waveform Generator. Its Timbre control sets the amplitude of a sine wave from the principal oscillator before that sine passes through a series of nonlinear stages whose outputs are summed. As the amplitude rises, the curves fold over on themselves, and each additional stage that engages makes the waveshape more complex; the 259's internal modulation oscillator can also sweep Timbre with a saw, square, or triangle wave. The musical argument ran opposite to subtractive synthesis. Instead of starting with a harmonically rich waveform and removing partials with a filter, the 259 started from the simplest waveform there is and added harmonics by shaping, with timbre treated as a continuous control rather than a menu of waveform choices.

Two circuit families carried folding out of Buchla's instruments and into the wider modular world. The middle section of the Serge wave multiplier, designed by Serge Tcherepnin in 1977, uses six identical folding stages in series, each an op-amp with a diode pair in its feedback path, with an input amplifier setting how many stages fold the signal. The other family descends from a 1973 circuit by R. Lockhart Jr., designed as a general-purpose frequency tripler and published in Bernie Hutchins's Electronotes newsletter; Ken Stone later repurposed it as a wavefolder by adding an input attenuator and an inverting output amplifier. It uses an NPN and a PNP transistor in place of diodes, folds more sharply, sounds brighter, and became ubiquitous in DIY builds. Academic analysis of analog folding circuits notes that series cascades of two to six stages are the norm.

Joranalogue's argument, made in the Fold 6 manual, is that diode wavefolders come in only two variants, series and parallel, and that choosing one confines a module to the sounds of that topology. Fold 6, introduced in November 2020, runs a six-stage hybrid series and parallel topology and exposes both through separate MAIN (series) and ALT (parallel) outputs in 4 HP. Around that core it places a voltage-controlled input stage that sets how many fold stages engage, and an overdrive circuit with a symmetrical soft clipper that holds the output to roughly 10 Vpp. The manual's revision history lists revision C as the initial release and revision D as having no functional changes.

Joranalogue Audio Design is the Belgian company of electronics engineer Joran van Gremberghe, who has said that he "started designing modules before I had even touched a module myself" and who later repaired vintage synths as a student. In a Perfect Circuit interview about the Collide 4 collaboration with Hainbach, he described the house approach: a minimal set of parameters and functions with voltage control over everything, no menu diving or mode switching, inspiration from test gear, and designs rolled from op amps and VCAs instead of dedicated oscillator or filter chips. At that point the catalog stood at more than twenty modules. The Fold 6 manual's closing credits thank a group that includes Ben "DivKid" Wilson, Gregory Delabelle, and Quincas "Synth DiY Guy" Moreira, and its tagline reads "21st Century Analogue Synthesis, Made in Belgium."

---

## Quick Start: First Fold in 5 Minutes

Fold 6 takes any audio or CV signal, multiplies it by an internal voltage-controlled amplifier, and folds the result back on itself through six diode stages. The harder the signal is driven, the more stages engage and the more harmonics appear. A sine or triangle wave is the clearest source for hearing this happen. ⚠️ Untested on hardware.

1. **Patch a sine or triangle into either IN jack.** Use a VCO such as Endorphin.es New Godspeed (SINE/FOLD output with TIMBRE at minimum gives a clean sine). The two IN jacks are identical and mixed together.
2. **Patch MAIN to a mixer channel** with the channel level low. The output reaches about 10 Vpp, which is a full Eurorack signal.
3. **Set SHAPE fully counterclockwise and SYMMETRY at center.** SHAPE at minimum disables the overdrive stage, and SYMMETRY at center applies no DC offset.
4. **Raise FOLD slowly from minimum.** At minimum the input is fully attenuated, so the output is silent. As FOLD rises, the plain sine appears first, then folds begin and overtones accumulate.
5. **Raise SHAPE.** The folded waveform is driven into the soft clipper and moves toward pulse-like shapes with a harsher character.
6. **Move SYMMETRY away from center.** Folding becomes asymmetric: either the positive or the negative half of the wave folds more than the other.
7. **Move the cable from MAIN to ALT.** The manual describes ALT as a more mellow sound for most input signals.

---

## Key Specifications

| Spec | Value |
|------|-------|
| Width | 4 HP |
| Depth | 40 mm ⚠️ |
| Power | 40 mA +12V / 40 mA -12V / 0 mA +5V |
| Controls | FOLD, SHAPE, SYMMETRY |
| Inputs | 2 signal IN (mixed, DC-coupled), FOLD CV, SHAPE CV |
| Outputs | MAIN (series), ALT (parallel) |
| Impedance | Inputs 100 kΩ; outputs 0 Ω (compensated) |
| Output level | Constrained to about -5 V to +5 V (about 10 Vpp) |
| Protection | Reverse polarity (MOSFET) |

The Depth value of 40 mm comes from the ModularGrid listing, which carries the manufacturer approved mark. The manual gives two other figures: 35 mm in its module format line (including the power cable) and 52 mm in its outer dimensions line (128.5 x 20 x 52 mm for the module itself). Treat the flag as open until the module is measured in the rack. The manual lists no +5V rail.

---

## Signal Path: One Folder, Two Voices

The manual's block diagram runs in a single line: IN, then an input VCA, then the six-stage hybrid wavefolder, then the overdrive circuit, then MAIN and ALT. Both outputs leave through the overdrive stage, so SHAPE affects both. The input VCA is controlled by FOLD, which is the key to the whole module: FOLD is not a threshold knob inside the folder, it is a level control in front of it. A larger signal reaches more fold stages, so FOLD sets how many folds occur.

MAIN is the series output, the classic wavefolding action found in earlier series-topology designs. ALT carries waveforms like those from parallel wavefolders, where fold levels and directions differ between the stages. Per the manual the result is more mellow for most inputs. Both outputs are always live, so the module is two timbres from one input at no extra cost.

The entire path is DC-coupled. Control voltages fold the same way audio does, and DC added to an audio signal shifts where the folds occur. This is what SYMMETRY exploits, and it is also why a small DC offset on an incoming signal changes the sound.

---

## Essential Parameters

**FOLD** controls the linear VCA that sits ahead of the wavefolder. As the signal amplitude entering the folder increases, more fold stages engage, which produces more folds and more harmonics. At minimum the input is fully attenuated and nothing reaches the output. The knob range is limited to +5 V for optimal control, but external voltage at the FOLD CV input can drive the folder harder than the knob can. FOLD CV is linear, so a sequencer step, an envelope, or an LFO moves the harmonic density in direct proportion to voltage. ⚠️ The manual does not say whether the knob and an incoming CV sum, or whether the knob scales the CV; confirm on hardware.

**SHAPE** controls the overdrive circuit after the wavefolder. At minimum the overdrive is essentially disabled and the result is classic wavefolder tone. As SHAPE rises, the folded signal is driven harder into the soft clipper, and continuous waveforms such as sine and triangle are gradually shaped into pulses with a harsher sound. At the SHAPE CV input, 0 V gives no drive and +5 V gives maximum drive with the knob at minimum. Negative voltages attenuate the output, which means SHAPE CV doubles as an output amplitude control, and it also means a bipolar LFO on this input will pull the level down on its negative half.

**SYMMETRY** adds a manually variable DC offset to the signal inputs, from -5 V to +5 V. Turned away from center, it makes the folding asymmetric: the positive or negative part of the waveform folds more than the other. It also works in the opposite direction: if the incoming signal already carries a DC offset, SYMMETRY can re-center the folder. There is no CV input for SYMMETRY, but because both IN jacks are DC-coupled, a CV mixed into either one acts as a modulated symmetry offset.

**IN (two jacks)** accept the signals to be folded. The jacks are identical and are mixed together inside the module, which often removes the need for a separate mixer. Because the path is DC-coupled, audio, CV, and combinations of the two are all valid inputs.

**MAIN** is the series output. The overdrive circuit holds its waveform to roughly -5 V to +5 V, so levels stay near the nominal Eurorack amplitude even at extreme fold settings, and clipping becomes symmetric once the final fold stage has been engaged. The manual warns that high-gain circuitry means some noise and DC offset are to be expected, especially at high FOLD and SHAPE levels.

**ALT** is the alternate (parallel) output, available at the same time as MAIN. It responds to the same FOLD, SHAPE, and SYMMETRY settings but with different fold levels and directions between stages, which the manual describes as a more mellow sound for most input signals.

---

## Why This Instrument Excels

The central distinction is that Fold 6 does not ask the player to choose a topology. Series and parallel diode folders have separate sonic personalities, and most wavefolder modules commit to one. Here both are present in the same six stages and both are available at the same time through MAIN and ALT, which means a single patch can use one output as the lead timbre and the other as a layered voice, or pick whichever suits the source on a given day without reaching for a different module. In 4 HP that is an unusual amount of choice.

The second distinction is the separation of two timbral axes. FOLD decides how many harmonics exist by deciding how many stages engage; SHAPE decides how aggressively the folded result is clipped toward a pulse. Because the clipper is symmetrical and limits the output to about 10 Vpp, high fold ratios stay usable instead of overloading the next module, and the character can be moved from smooth bell-like complexity to buzzy pulse-like edge with a single control. Both axes carry their own CV input, so they can be modulated independently or by the same source for correlated movement.

The third distinction is the DC-coupled, two-input design. The module mixes its inputs, accepts CV as readily as audio, and offers a symmetry offset that works in both directions, either creating asymmetric folds or correcting an unwanted offset in the source. The manual points toward feedback patching, CV folding, and frequency multiplication as natural uses; each depends on the path being fully DC-coupled and unfiltered, which is a design decision rather than a default.

The fourth distinction is how the module fits into a rack. At 4 HP and 40 mA on each rail, it costs very little space and very little power, so it can sit behind every oscillator that needs enrichment, rather than being treated as a rare centerpiece. The controls are few and the parameters are all voltage-controllable, which matches Joranalogue's stated approach of a minimal set of parameters with voltage control over everything: it is quick to understand and deep in how it responds to modulation.

---
## Patch Examples

Fold 6 is a SHAPER, so every patch needs an external oscillator ahead of it and an external envelope and VCA behind it. The First Voice below uses the SHAPER cabling: the module sits in the middle of the audio chain. Before inserting Fold 6 for the first time, patch the oscillator straight into the VCA and confirm that pitch and envelope behave, then place Fold 6 between them.

All four patches below are drafts written from the manual and are untested on hardware ⚠️. Knob positions describe intent, and every "What to listen for" result is a prediction until the module has been patched.

---

### Patch 1: FOLD as a Harmonic Density Control ⚠️

This patch demonstrates that FOLD is a level control feeding a folder: the same sine at the same pitch gains overtones as more fold stages engage.

**First Voice**

Before introducing anything specific to Fold 6, establish a working voice:

```
  Squarp Hermod+ CV out ──[C]──▶ New Godspeed 1V/OCT
  Squarp Hermod+ gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  New Godspeed SINE/FOLD out ──[A]──▶ Fold 6 IN
  Fold 6 MAIN ──[A]──▶ VCA audio in ──▶ Mixer
```

Use a sequencer such as Squarp Hermod+ (or Mutable Instruments Marbles, with X1 for pitch and t2 for gate), an oscillator such as Endorphin.es New Godspeed (or Endorphin.es Furthrrrr Generator with its waveshaper knobs fully counterclockwise), an envelope generator such as Blue Lantern BLM Looping Simple ADSR (or Make Noise Maths), and a VCA such as Vostok Instruments Ceres (or Erica Synths Pico VCA2). Set the sequencer to repeat a single note and verify that the VCA opens and closes with each gate.

**Add the folder**

```
                          ┌──────────────────────────────────┐
New Godspeed ──[A]──▶     │ IN                          MAIN │──[A]──▶ VCA ──▶ Mixer
                          │ FOLD  SHAPE  SYMMETRY            │
                          └──────────────────────────────────┘
                                   Joranalogue Fold 6
```

- `New Godspeed SINE/FOLD ──[A]──▶ IN`: a clean sine is the simplest possible source, so every overtone you hear afterwards was created by the folder and not by the oscillator.
- `MAIN ──[A]──▶ VCA`: MAIN is the series output and the most classic wavefolder behavior, which makes it the baseline for every later comparison.

Set SHAPE fully counterclockwise and SYMMETRY at center. Starting from minimum, turn FOLD up by hand over about thirty seconds while the sequencer repeats the note.

**What to listen for**

At minimum FOLD the output should be silent, because the input is fully attenuated. As FOLD rises, the plain sine should appear first, then take on added overtones in stages as more fold stages engage, ending in a dense, bright spectrum. If the sound is buzzy and harsh from the start, SHAPE is not at minimum; if nothing ever appears, check FOLD and the envelope before suspecting the module.

---

### Patch 2: SHAPE as a Second Axis, and MAIN versus ALT ⚠️

This patch demonstrates that fold density and clipping are separate timbral controls, and that the two outputs are two different voicings of the same fold.

**First Voice**

Use the same voice as Patch 1, with Fold 6 in the chain and MAIN feeding the VCA.

**Add the SHAPE sweep**

```
                          ┌──────────────────────────────────┐
New Godspeed ──[A]──▶     │ IN                          MAIN │──[A]──▶ VCA ──▶ Mixer
                          │ FOLD (fixed)  SHAPE (swept)      │
                          └──────────────────────────────────┘
                                   Joranalogue Fold 6
```

- `New Godspeed SINE/FOLD ──[A]──▶ IN`: the same clean source as Patch 1 keeps the comparison honest.
- `MAIN ──[A]──▶ VCA`: the series output is the reference sound before the cable moves.

Set FOLD at a fixed, moderately high position that produces a clearly folded tone. Turn SHAPE up from minimum by hand. The overdrive stage sits after the folder, so SHAPE should change the edge of the sound rather than the number of overtones.

**Move the cable**

Unplug the cable from MAIN and plug it into ALT. Leave every knob where it is.

```
                          ┌──────────────────────────────────┐
New Godspeed ──[A]──▶     │ IN                           ALT │──[A]──▶ VCA ──▶ Mixer
                          │ FOLD (fixed)  SHAPE (swept)      │
                          └──────────────────────────────────┘
                                   Joranalogue Fold 6
```

What changed: the series output is replaced by the parallel output, which the manual describes as a more mellow sound for most input signals, with different fold levels and directions between stages.

**What to listen for**

With SHAPE rising on MAIN, the tone should move from folded and bell-like toward pulse-like and harsher. On ALT the same settings should sound softer. If MAIN and ALT sound identical, raise FOLD and compare again at matched listening level before drawing a conclusion.

---

### Patch 3: Feedback Through the Second Input ⚠️

This patch demonstrates that Fold 6 can feed itself: the second IN jack turns MAIN into a source for its own input, and a modulated FOLD keeps the loop moving.

**First Voice**

Use the same voice as Patch 1, but leave Fold 6 MAIN free for the feedback cable and take the VCA feed from ALT instead.

**Add the feedback loop**

```
                           ┌──────────────────────────────────┐
New Godspeed ──[A]──▶      │ IN 1                         ALT │──[A]──▶ VCA ──▶ Mixer
Fold 6 MAIN ──[A]──▶       │ IN 2                        MAIN │──[A]──▶ (patched back to IN 2)
Ochd LFO 1 ──[C, medium]──▶│ FOLD CV                          │
                           └──────────────────────────────────┘
                                    Joranalogue Fold 6
```

- `New Godspeed SINE/FOLD ──[A]──▶ IN 1`: the oscillator provides the pitched seed that the loop will reshape.
- `MAIN ──[A]──▶ IN 2`: the second input is mixed with the first, so MAIN returns to the folder and the signal folds against itself.
- `ALT ──[A]──▶ VCA`: listening to the parallel output while MAIN drives the loop separates what feeds the loop from what reaches the mixer.
- `DivKid Ochd LFO 1 ──[C, medium]──▶ FOLD CV`: a medium-speed LFO keeps the fold depth moving so the loop does not settle into one state. Check the polarity of the LFO output first; FOLD is a linear input that expects a positive voltage to open it further.

Use an LFO such as DivKid Ochd (or 2hp LFO v2). Start with the mixer channel low. The module limits its output to about 10 Vpp, but a feedback loop can still be loud and abrupt.

**Move the cable**

Unplug the feedback cable from MAIN and plug it into ALT, then take the VCA feed from MAIN.

What changed: the parallel output now drives the loop and the series output is what you hear. The loop gain and character differ because ALT carries different fold levels between stages.

**What to listen for**

Expect a range from a tone that thickens and shimmers to one that becomes unstable, noisy, or locks to a fixed level, because the path is DC-coupled and a loop can latch. ⚠️ Which of these occurs at which setting is unverified. If the loop sticks, lower FOLD or move SYMMETRY to re-center the offset; if it is simply too loud, back off FOLD before changing anything else.

---

### Patch 4: Random Fold Depth Per Note in a Complete Voice ⚠️

This patch demonstrates Fold 6 as one stage in a larger voice: a probability generator chooses pitch and fold depth together, a filter tames the result, and both outputs reach the mix.

**First Voice**

The voice is built in full inside this patch; the sequencer role is filled by Mutable Instruments Marbles (or Squarp Hermod+).

**The complete voice**

```
                          ┌──────────────────────────────────┐
New Godspeed ──[A]──▶     │ IN                          MAIN │──[A]──▶ Black Polyvoks VCF IN
Marbles X2 ──[C]──▶       │ FOLD CV                      ALT │──[A]──▶ MixUp CH2 IN
                          └──────────────────────────────────┘
                                   Joranalogue Fold 6

  Marbles X1 ──[C]──▶ New Godspeed 1V/OCT
  Marbles t2 ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  Black Polyvoks VCF OUT ──[A]──▶ VCA audio in ──▶ MixUp CH1 IN
```

- `Marbles X1 ──[C]──▶ New Godspeed 1V/OCT`: the quantized random pitch from the X section sets the melody.
- `Marbles t2 ──[G]──▶ EG gate in`: the t section sets the timing, and each gate triggers the envelope.
- `EG out ──[C]──▶ VCA CV in`: the envelope shapes each note's loudness after the filter.
- `New Godspeed ──[A]──▶ Fold 6 IN`: the oscillator is the sine source the folder will enrich.
- `Marbles X2 ──[C]──▶ Fold 6 FOLD CV`: a second output from the same probability system sets the fold depth, so every note gets its own harmonic density, correlated with the melody but not identical to it.
- `Fold 6 MAIN ──[A]──▶ Black Polyvoks VCF IN`: the filter removes or shapes the upper harmonics that the folder created, joining a Buchla-lineage fold to a subtractive stage.
- `Black Polyvoks VCF OUT ──[A]──▶ VCA audio in`: the filtered signal reaches the VCA and the mix as the main voice.
- `VCA out ──[A]──▶ MixUp CH1 IN`: the filtered, enveloped voice reaches the mix on its own channel so its level can be balanced against the layer below.
- `Fold 6 ALT ──[A]──▶ MixUp CH2 IN`: the unfiltered parallel output sits beside the filtered main voice as a second layer, so one folded source gives two timbres.

Use a mixer such as Intellijel MixUp (channels 1 and 2 are mono inputs with level knobs and mute switches). Set Marbles STEPS around 2 o'clock and DEJA VU around 11 o'clock (see the Marbles guide, Patch 1). Set the filter cutoff near the middle and resonance low. This patch uses nine cables, below the ten-cable ceiling. ⚠️ The voltage span of Marbles X2 relative to the FOLD CV range has not been verified; if the fold depth is too extreme, scale X2 with an attenuator before it reaches FOLD CV.

**What to listen for**

Each note should arrive with its own harmonic density: some bell-like and open, some dense and bright, all following a pitch sequence that loosely repeats as DEJA VU recycles values. The ALT layer should sound softer and less filtered than the main voice. If every note has the same timbre, check that X2 is patched to FOLD CV and not X1; if the sound is uniformly harsh, lower FOLD CV depth or SHAPE before touching the filter.

---

## Common Mistakes

### "I turned FOLD all the way down and the output is silent"

FOLD controls the linear VCA that sits in front of the wavefolder, so at its minimum position the input is fully attenuated, not passed through unfolded. The module is not broken; no signal reaches the folder at all. Raise FOLD slightly and the plain waveform appears; keep raising it to bring in folds. If you want a nearly clean signal, use a low but non-zero FOLD with SHAPE at minimum.

### "There is noise and DC offset on the output when I push it hard"

The manual states that, because of Fold 6's high-gain circuitry, some noise and DC offset are to be expected in the outputs, especially at high FOLD and SHAPE levels. This is a property of a high-gain DC-coupled folder, not a fault. If the offset causes trouble downstream, route the output through a high-pass filter or an AC-coupled input, and reduce SHAPE first since it adds drive after the fold. If the offset is arriving with the source signal, use SYMMETRY to re-center the folder.

### "My LFO on SHAPE makes the level pump instead of changing the tone"

SHAPE CV is a unipolar control: 0 V gives no drive and +5 V gives maximum drive with the knob at minimum. Negative voltages attenuate the output, so a bipolar LFO swings between more drive and less level, and the negative half sounds like a volume dip. The fix is to feed SHAPE a positive-only source, or offset a bipolar LFO to stay above zero. If level modulation is what you wanted, the behavior is a feature, since SHAPE CV doubles as an output amplitude control.

### "MAIN and ALT sound the same"

MAIN and ALT come from the same six stages and the same input, so with little folding the two can be hard to tell apart. The manual describes ALT as a more mellow sound for most input signals, with fold levels and directions varying between the stages. Raise FOLD with a sine input, match the listening level of the two outputs, and compare again. ⚠️ How much the outputs differ at different fold amounts is unverified.

### "Two oscillators into the inputs does not give me ring modulation"

The two IN jacks are summed, not multiplied. Two audio signals patched in are mixed and then folded together, which produces intermodulation shaped by the folder rather than the sum and difference sidebands of a ring modulator. For amplitude-style interaction, patch one oscillator into IN and the other into FOLD CV, where it controls the input VCA directly. Keep the combined level in mind: two inputs together raise the signal entering the folder, so they also raise the number of folds.

---

## Advanced Learning Path

1. **Learn to hear fold count.** Run a sine through MAIN with SHAPE at minimum and sweep FOLD slowly, listening for each new layer of overtones. Repeat with a triangle and then with a sawtooth, and notice how the input shape changes where the folds land. This is the vocabulary for everything that follows.

2. **Look at what you hear.** Connect MAIN and ALT to two inputs of Mordax Data in SCOPE mode and watch the two waveforms at the same time while you sweep FOLD, SHAPE, and SYMMETRY. Switch to the spectrum program and watch harmonics appear as fold stages engage. Seeing the structure turns a vague impression of mellow and bright into specific differences you can predict.

3. **Put an envelope on FOLD CV.** Patch an envelope into FOLD CV so that each note starts folded and relaxes toward a plain tone, or the reverse. Compare linear and exponential envelope shapes, since the harmonic motion tracks the curve of the voltage. This is the classic pluck and bongo gesture of folded timbre.

4. **Use SYMMETRY and DC deliberately.** Move SYMMETRY away from center and compare even and odd harmonic balance. Then patch a static or slowly moving CV into the second IN jack so that an offset modulates symmetry continuously. Because both inputs are DC-coupled, any CV you mix into the audio becomes a symmetry offset.

5. **Fold a control voltage.** Patch a slow LFO into IN instead of audio and send MAIN to a modulation destination. The folder turns a simple LFO into a complex multi-peaked control voltage, which is a form of CV folding and frequency multiplication of the control signal. Use SYMMETRY to move where the folds occur.

6. **Drive FOLD at audio rate.** Patch a second oscillator into FOLD CV and listen as the input VCA is modulated at audio rate. The result is an amplitude interaction before the fold, with the character depending on the frequency relationship between the two oscillators. Compare it with patching the same second oscillator into IN.

7. **Build a stereo fold.** Send MAIN to the left channel and ALT to the right channel of a stereo mixer input, such as Intellijel MixUp channel 3, with a slowly modulated FOLD. The two voicings of the same fold become a stereo image, and any CV on FOLD or SHAPE moves both channels together while their different topologies keep them distinct.

---

## Pairs Well With

**Endorphin.es New Godspeed:** A stable sine source is the best input for hearing what a folder does, and the SINE/FOLD output of Endorphin.es New Godspeed provides one when TIMBRE is at minimum. Its digital autotune keeps the pitch locked while Fold 6 moves the timbre, so changes in sound come from the folder and not from oscillator drift. Feeding its own folded output into Fold 6 puts one wavefolder in front of another, a combination to explore with care. ⚠️

**Make Noise Maths:** Make Noise Maths used as an envelope source into FOLD CV gives each triggered note its own fold sweep with adjustable rise and fall shapes. Its function-generator design lets one channel drive FOLD and another drive SHAPE with a different timing, so the two timbral axes can move independently. Channel outputs that exceed the knob's +5 V range can push the folder harder than the panel can.

**Mutable Instruments Marbles:** Marbles X1 and X2 give pitch and fold depth from the same probability system, so each note's timbre is correlated with its pitch without being identical to it. DEJA VU locked on the X section makes the pitch and fold pattern repeat; unlocked, both drift together. The t outputs supply gates for the envelope, completing a self-contained generative voice around a single folder.

**Erica Synths Black Polyvoks VCF:** Placing Erica Synths Black Polyvoks VCF after the folder joins a Buchla-lineage fold to a subtractive stage. Fold 6 adds harmonics, and the filter removes or emphasizes parts of that spectrum in a way that moves with its own cutoff modulation. The combination turns a bell-like sine into a sculpted voice with a movable spectral envelope.

**Mordax Data:** Mordax Data connects oscilloscope and spectrum views to Fold 6's two outputs at once, showing how MAIN and ALT differ in waveform and in harmonic content. Each input gets its own color on screen, so a side-by-side comparison of series and parallel behavior is immediate. It makes the difference between FOLD and SHAPE visible, which is the quickest route to controlling both on purpose.

**DivKid Ochd:** DivKid Ochd supplies eight free-running LFOs at related but drifting rates, ideal for moving FOLD CV and, with attention to polarity, SHAPE CV. Because the rates drift against each other, the fold depth and the drive evolve out of step, producing timbral changes that do not repeat on a short cycle. SHAPE CV treats negative voltage as attenuation, so check the LFO polarity before patching.

---

*Visit [joranalogue.com](https://joranalogue.com/collections/eurorack/products/fold-6) for the official manual and product information*
