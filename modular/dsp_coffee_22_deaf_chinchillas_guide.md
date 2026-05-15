---
title: 22 Deaf Chinchillas
manufacturer: dsp.coffee
primary_role: EVENT_VOICE
secondary_roles: [SOURCE]
functions: [vco, vca, vcf, voice]
hp: 12
depth: 30mm
current_draw:
  plus12: 90mA
  minus12: 73mA
price_eur: 299
inputs: [1v/o, lin fm, exp fm, pwm, s. sync, h. sync, vca l1, vca l2, vca in, vca in 2, cutoff, rez]
outputs: [sin, tri, saw, pulse, 2144]
patch_format: v1
edition: hand-numbered, run of 10
---

# dsp.coffee 22 Deaf Chinchillas

![dsp.coffee 22 Deaf Chinchillas](https://github.com/Shadoe-42/music/raw/main/modular/images/dsp_coffee/22_deaf_chinchillas/front_panel.jpg)

## Historical Context

Three integrated circuits define the sound of a significant portion of the analog synthesizers built between 1977 and 1985. The CEM3340 voltage-controlled oscillator, designed by Doug Curtis at CEM, appeared in the Sequential Circuits Prophet-5, the Moog Source, the Roland SH-101 and SH-2, and the Oberheim OB-Xa. Its combination of stable exponential pitch tracking, multiple simultaneous waveform outputs, and hard and soft sync made it the oscillator chip of the era. The SSM2044 four-pole lowpass filter, from Solid State Micro Technology, appeared in the Korg Polysix, the Korg Mono/Poly, and the early E-mu Emulator; its steep rolloff and tendency toward smooth, musical self-oscillation gave those instruments a distinctive warmth. The SSM2164 quad VCA provided the amplitude control infrastructure for countless designs of the same period.

None of these chips are in production in their original form. What exists today are high-fidelity clones: the AS3340 from Alpha & Omega Semiconductor, the SSI2144 from Sound Semiconductor (a direct successor company to SSM), and the AS2164 from Alpha & Omega. Electrosmith built these three chips onto individual analog submodules as part of their Analog Signal Processing platform. A single builder at dsp.coffee wired those three submodules together in 12HP, added jacks for every meaningful breakpoint in the signal chain, and produced ten units. The 22 Deaf Chinchillas is hand-numbered.

There is no official documentation. This guide is compiled from the developer's own description in a Discord conversation, inspection of the panel, and direct experience with the module.

---

## How the 22 Deaf Chinchillas Is Wired

Understanding the internal signal flow is essential before any patch makes sense, and since no documentation exists elsewhere, it is reproduced here in full.

**The default internal chain:**

```
AS3340 VCO
  │
  ├── saw ──[normalled]──▶ AS2164 VCA channel 1 (level: vca l1)
  │                                    │
  └── pulse ──[normalled]──▶ AS2164 VCA channel 2 (level: vca l2)
                                        │
                             SSI2144 dual filter
                                        │
                                   2144 output
```

The VCO saw output is normalled to VCA channel 1. The VCO pulse output is normalled to VCA channel 2. Both VCA outputs feed the SSI2144 filter, which sums to the single 2144 output jack. This is the default audio path: saw and pulse blended through dual VCA into dual filter, out at 2144.

**Breaking the normals:**

Patching to `vca in` breaks the saw-to-VCA-channel-1 normal. Whatever you patch there replaces the saw as the input to VCA channel 1. Patching to `vca in 2` breaks the pulse-to-VCA-channel-2 normal. The VCA and filter remain in the chain; only the source changes. This is how the module's VCA and VCF become available for processing external audio.

**The direct VCO outputs:**

All four VCO waveforms are available as direct outputs at the bottom of the panel regardless of VCA state: `sin`, `tri`, `saw`, and `pulse`. These outputs bypass the VCA and filter entirely. They produce audio continuously whenever the module is powered, at whatever frequency is set by the tuning knobs and 1V/oct input.

**VCA behavior:**

The 2144 output depends on the VCAs being open. The AS2164 chip defaults closed with no control voltage: `vca l1` and `vca l2` require CV input to produce audio at the 2144 output. The direct VCO outputs are not affected by VCA state and drone freely.

⚠️ The exact default behavior of the VCAs with nothing patched has not been exhaustively confirmed. The above reflects expected AS2164 behavior and reported experience. Play-test with the Mordax Data to confirm during setup.

---

## Why 22 Deaf Chinchillas Excels

The 22 Deaf Chinchillas is the most structurally flexible voice in the rack, not because it has the most features, but because every meaningful breakpoint in its signal chain is exposed. You can use it as a conventional pitched voice with external envelope shaping. You can use the VCA and filter as a standalone processor by breaking both normals and injecting external audio. You can use all four direct VCO outputs simultaneously as independent sources in different parts of a patch. You can slow the VCO to LFO speeds with a negative control voltage and harvest four simultaneous modulation waveforms. You can patch one of those waveforms back into an FM input and let the oscillator destabilize itself.

The chip pedigree matters because these are not generic analog building blocks. The AS3340 has hard sync and soft sync inputs that produce musically specific timbral changes. The SSI2144 self-oscillates at high resonance and tracks 1V/oct with reasonable accuracy, making it a secondary pitched voice independent of the VCO. The dual VCA configuration means saw and pulse can be balanced against each other before hitting the filter, creating a simple internal mixer whose character changes depending on VCA CV routing.

Ten of these exist. The guide you are reading was compiled from a Discord message and panel inspection. Any additional documentation this corpus can provide is documentation that did not otherwise exist.

---

## Patch Examples

The 22 Deaf Chinchillas is an EVENT_VOICE requiring external amplitude CV for the 2144 output. The direct VCO outputs are always active and do not require external CV.

A note before the patches: the module does not have an internal envelope generator. Amplitude shaping at the 2144 output requires patching an external EG to `vca l1`, `vca l2`, or both. The direct VCO outputs bypass this requirement entirely.

---

### Patch 1: Basic Gated Voice

Patching the default chain with an external envelope establishes the full VCO-through-VCA-through-filter signal path and demonstrates how the saw and pulse normals interact through the dual VCA at the filter input.

**First Voice**

```
  Sequencer CV out ──[C]──▶ 22 Deaf Chinchillas 1v/o
  Sequencer gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ 22 Deaf Chinchillas vca l1
  22 Deaf Chinchillas 2144 out ──[A]──▶ Mixer
```

With this patch and nothing else: the saw waveform passes through VCA channel 1 (opened by the envelope), through the filter, and out at 2144. The pulse channel is present in the filter but VCA channel 2 (vca l2) has no CV, so it contributes little or nothing to the output. Verify the voice produces a clean pitched tone tracking the sequencer before proceeding.

**Expand the voice**

```
                    ┌─────────────────────────────────────────────────┐
Sequencer ──[C]──▶  │ 1v/o          sin  tri  saw  pulse  2144        │
EG ──[C]──▶         │ vca l1                                          │──[A]──▶ Mixer
EG ──[C]──▶         │ vca l2                                          │
LFO ──[C]──▶        │ cutoff                                          │
                    └─────────────────────────────────────────────────┘
                              22 Deaf Chinchillas
```

Use a sequencer such as Hermod+ (or Ornament and Crime) for pitch and gate. Use an EG such as the Cre8audio Function Junction (or Behringer 1003) for the envelope. Use an LFO such as 2hp LFO v2 (or Batumi) for filter modulation.

- `EG out ──[C]──▶ vca l1`: opens VCA channel 1 on each gate, letting saw through to the filter. The envelope shape determines the amplitude contour of the output.
- `EG out ──[C]──▶ vca l2`: opens VCA channel 2 simultaneously, adding pulse to the filter input alongside saw. The balance between saw and pulse character is determined by the relative VCA levels: if both receive identical CV, they mix equally into the filter. Attenuating one EG signal before patching to vca l2 sets a fixed ratio.
- `LFO ──[C]──▶ cutoff`: sweeps filter brightness over time independent of the amplitude envelope. Set the LFO rate slower than the note rate for a gradual timbral evolution, or faster for tremolo-like filter movement.

**Move the cable**

Unplug the EG from `vca l2` and leave it unpatched. Now patch one of the direct outputs to a separate mixer channel:

```
  22 Deaf Chinchillas sin out ──[A]──▶ Mixer channel 2
```

What changed: the 2144 output carries saw only through the gated VCA. The sin output runs continuously to the mixer, unaffected by the envelope. The result is a gated saw voice with a continuous sine underneath it: two layers from one module, one shaped, one free.

**What to listen for**

The 2144 output should track pitch cleanly and respond to the envelope shape. If the output is silent, confirm the EG is reaching sufficient voltage to open the AS2164 VCA; it may require a CV level above 1V to produce audible output. If the pulse and saw are both present but unbalanced in an unintended way, check whether anything is patched to `vca l2`; unpatched, it may contribute a residual level or remain silent depending on the module's exact default state. The sin output at the mixer should be a continuous pitched tone at the same frequency as the VCO; if it sounds like a square or saw, confirm the jack is `sin` and not one of the other direct outputs.

---

### Patch 2: Quad LFO Mode

Patching a negative control voltage to the `1v/o` input drives the VCO below audio rate, turning all four direct outputs into simultaneous LFOs with distinct waveform characters. The module becomes a four-output modulation source from a single CV.

**First Voice**

Before making the 22 Deaf Chinchillas the modulation source, establish a voice it will modulate:

```
  Sequencer CV out ──[C]──▶ VCO 1V/OCT
  Sequencer gate out ──[G]──▶ EG gate in
  EG out ──[C]──▶ VCA CV in
  VCO audio out ──[A]──▶ VCF audio in ──▶ VCA audio in ──▶ Mixer
  [22 Deaf Chinchillas] running: negative CV into 1v/o, direct outputs available
```

Verify the downstream voice is working before connecting the Chinchillas' modulation outputs.

**Set up the quad LFO**

```
                    ┌─────────────────────────────────────────────────────┐
Negative CV ──[C]──▶│ 1v/o    sin ──[C]──▶ VCF cutoff CV in              │
                    │         tri ──[C]──▶ VCO FM in                      │
                    │         saw ──[C]──▶ VCA CV in (secondary modulation)│
                    │         pulse ──[C]──▶ (leave or route elsewhere)   │
                    └─────────────────────────────────────────────────────┘
                              22 Deaf Chinchillas (LFO mode)
```

Use a module capable of producing negative CV such as Maths (or any bipolar CV source) to drive `1v/o` below 0V. The further negative, the slower the LFO rate. Start around -2V and adjust to taste.

- `sin ──[C]──▶ VCF cutoff CV in`: the sine output produces a smooth, symmetric filter sweep with no sharp edges.
- `tri ──[C]──▶ VCO FM in`: triangle wave FM produces a symmetrical pitch oscillation. At slow rates this creates vibrato; at medium rates it creates a siren-like effect.
- `saw ──[C]──▶ VCA CV in`: the sawtooth rises slowly and resets sharply, producing a rhythmically regular amplitude swell with an abrupt cutoff. This creates a different envelope shape than an EG would.
- `pulse ──[C]──▶` any destination: the square wave output gates between two levels, useful as a rhythmic trigger or hard-switching modulation source.

All four run simultaneously at the same rate (set by the negative CV into `1v/o`) but with different waveform shapes. Routing them to different destinations creates a coordinated but varied modulation texture from a single rate control.

**What to listen for**

All four outputs should be modulating their respective destinations simultaneously. If the rate feels too fast to be useful as LFO, push the `1v/o` CV further negative. If the outputs are not producing visible modulation effect, check that the destinations have CV inputs with enough sensitivity; some inputs need attenuators to respond to low-amplitude modulation. The sine and triangle should produce smooth variation; the saw should produce a rhythmic sweep-and-reset; the pulse should produce an abrupt switching effect.

---

### Patch 3: Self-Patching FM Feedback

Routing one of the direct VCO outputs back into an FM input of the same VCO creates a feedback loop. The oscillator modulates its own frequency, producing instability, harmonic complexity, and controlled chaos that changes character depending on modulation depth and initial tuning.

**First Voice**

```
  Sequencer CV out ──[C]──▶ 22 Deaf Chinchillas 1v/o
  EG out ──[C]──▶ 22 Deaf Chinchillas vca l1
  22 Deaf Chinchillas 2144 out ──[A]──▶ Mixer
```

Establish a clean pitched tone at the 2144 output before introducing the feedback path.

**Add the feedback**

```
                    ┌──────────────────────────────────────────┐
Sequencer ──[C]──▶  │ 1v/o          sin                        │
EG ──[C]──▶         │ vca l1        tri                        │
                    │               saw ──╮                    │
                    │ lin fm ◀────────────╯  pulse    2144     │──[A]──▶ Mixer
                    └──────────────────────────────────────────┘
                              22 Deaf Chinchillas
```

Patch the `saw` direct output to `lin fm` input. The sawtooth wave of the VCO now modulates the VCO's own linear FM input. Start with the lin fm knob at minimum and slowly increase.

- `saw ──[C]──▶ lin fm`: at low modulation depth, the feedback introduces mild harmonic enrichment and a slight instability in the pitch. At medium depth, the waveform begins to fold back on itself, adding subharmonic content and upper partials. At high depth, the oscillator enters chaotic territory: the output becomes unpredictable, rich, and loud.

**Move the cable**

Unplug `saw` from `lin fm` and repatch to `exp fm` instead. Alternatively try `sin` or `tri` as the feedback source rather than `saw`.

What changed: exponential FM produces a different instability character than linear FM. Linear FM at audio rates tends toward sidebands that grow symmetrically; exponential FM produces asymmetric pitch deviation that sounds more extreme at the same knob setting. Different source waveforms create different feedback textures: sine produces a smoother, more organic chaos; triangle tends toward a buzzing, edged instability; saw produces the most aggressive and asymmetric result.

**What to listen for**

At low feedback depth, the tone should sound richer and slightly unstable compared to the clean voice from Patch 1: a pleasant roughness. As depth increases, watch for a transition from complex-but-pitched to chaotic-and-noisy: this threshold is the most musically interesting territory. If the output immediately clips or distorts before any musical chaos is audible, reduce the lin fm or exp fm knob and increase it more gradually. If nothing audible changes with feedback depth, confirm the `saw` output is patched to the FM input and not to another jack.

---

## Controls Reference

**1v/o.** Exponential pitch tracking CV input. Standard 1V/oct. Negative voltages slow the VCO below audio rate for LFO use.

**lin fm.** Linear frequency modulation CV input. Modulation depth set by the lin fm knob. Linear FM produces symmetrical sidebands and is preferred for audio-rate FM applications.

**exp fm.** Exponential frequency modulation CV input. Depth set by the exp fm knob. Produces asymmetric pitch deviation; at high depth sounds more extreme than equivalent linear FM.

**pwm.** Pulse width modulation CV input. Controls the duty cycle of the pulse output. Depth set by the pwm knob.

**s. sync.** Soft sync input. Resets the VCO cycle in a phase-aware way that allows the slave oscillator to produce complex waveforms while maintaining a harmonic relationship to the master.

**h. sync.** Hard sync input. Forces VCO cycle reset on each incoming trigger regardless of phase. Produces classic hard-sync timbres; the interval between master and slave determines the harmonic content.

**vca l1.** CV input for VCA channel 1. Controls the level of the signal passing through VCA channel 1 to the filter. With the default normal in place, this controls the saw level reaching the SSI2144.

**vca l2.** CV input for VCA channel 2. Controls the level of the signal through VCA channel 2. With the default normal in place, this controls the pulse level reaching the SSI2144.

**vca in.** Breaks the internal saw-to-VCA-channel-1 normal. Patch external audio here to use VCA channel 1 and the SSI2144 as a standalone processor.

**vca in 2.** Breaks the internal pulse-to-VCA-channel-2 normal. Patch external audio here to use VCA channel 2 as a standalone processor alongside channel 1.

**cutoff.** CV input for SSI2144 filter cutoff frequency. Positive CV opens the filter; negative CV closes it.

**rez.** CV input for SSI2144 filter resonance. At high resonance the filter self-oscillates, producing a sine wave at the cutoff frequency trackable by pitch CV.

**sin.** Direct VCO sine wave output. Bypasses VCA and filter. Always active.

**tri.** Direct VCO triangle wave output. Bypasses VCA and filter. Always active.

**saw.** Direct VCO sawtooth output. Bypasses VCA and filter. Also normalled internally to VCA channel 1 unless `vca in` is patched.

**pulse.** Direct VCO pulse output. Bypasses VCA and filter. Also normalled internally to VCA channel 2 unless `vca in 2` is patched. Width controlled by pwm input.

**2144.** SSI2144 filter output. Main processed audio output. Requires VCA channels to be open (CV patched to `vca l1` and/or `vca l2`) to produce audio. Self-oscillates at high resonance.

---

## Key Specs

| Parameter | Value |
|-----------|-------|
| HP | 12 |
| Depth | 30mm |
| +12V | 90mA |
| -12V | 73mA |
| VCO chip | AS3340 (CEM3340 clone) |
| VCA chip | AS2164 (SSM2164 clone) |
| VCF chip | SSI2144 (SSM2044 clone) |
| Edition | Hand-numbered, run of 10 |
| Price | €299 |

---

## Common Errors

**Expecting audio at the 2144 output with no CV on vca l1 or vca l2.** The AS2164 defaults closed. The 2144 output requires CV to open the VCA. Use the direct outputs (sin, tri, saw, pulse) if you need audio without external CV.

**Confusing the direct outputs with the processed output.** The bottom four jacks (sin, tri, saw, pulse) come directly from the VCO and bypass the VCA and filter entirely. The 2144 jack is the only output that reflects filter and VCA processing. Patching the wrong output to a destination produces unexpected results in either direction: unfiltered/unenveloped audio from the direct outputs, or no audio from 2144 without VCA CV.

**Patching to `vca in` expecting an additional input rather than a replacement.** Patching to `vca in` breaks the saw normal. The saw no longer feeds VCA channel 1; your patched signal does instead. If you want to add an external signal alongside saw, you need a mixer before the `vca in` jack.

**Running feedback depth too high immediately.** Self-patching FM feedback transitions from musical to chaotic at a threshold that changes depending on tuning and modulation source. Approach the threshold slowly, starting with the FM knob at minimum and increasing gradually.

**⚠️ VCA default state: confirm at the rack.** The AS2164 is expected to default closed, but the exact behavior of this particular circuit with no CV patched has not been exhaustively verified. If the 2144 output produces audio without any CV on `vca l1` or `vca l2`, the VCA may be biased open at a fixed level by the circuit design. Verify and update this note after play-testing.

---

## Notes

No official documentation exists for this module. The signal flow description in "How the 22 Deaf Chinchillas Is Wired" is drawn from a single Discord message by the module's creator and from panel inspection. The chip identifications are drawn from the ModularGrid listing and the creator's description. The behavioral details of the VCA default state and certain edge-case routing behaviors are flagged for play-test verification throughout this guide.

The module's name is a My Bloody Valentine reference. Kevin Shields at one point reportedly owned 22 chinchillas; someone corrected the story to 22 deaf ones. The font used on the panel is the same font MBV used on the album artwork, sourced by the builder specifically for this module. Shields is famously protective of his hearing to the point of near-obsession, which gives "deaf chinchillas" a particular edge as a name for a synthesizer module. It is a good name.

This is guide number 100 in this corpus. It documents a module with a production run of ten units built by one person without a manual, using three chips that defined the sound of an entire era of analog synthesis. That is the right thing for the hundredth entry to be about.

Full information, when and if published by the creator, is available at [dsp.coffee](https://dsp.coffee/products/22-deaf-chinchillas).
