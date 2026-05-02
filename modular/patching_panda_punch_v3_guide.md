---
title: Patching Panda Punch V3
manufacturer: Patching Panda
primary_role: MODULATOR
secondary_roles: [AMPLIFIER]
form_factor: eurorack
functions: [vca, envelope-generator]
behavior_tags: [percussive, gated, reactive, warm, performance-oriented, cv-friendly]
use_cases: [voice shaping, percussive dynamics, envelope generation, sidechain effects]
hp: 9
historical_context: false
---

# Patching Panda Punch V3

![Patching Panda Punch V3](https://github.com/Shadoe-42/music/raw/main/modular/images/patching_panda/punch_v3/front_panel.jpg)
*Dual-channel VCA with voltage-controlled decay envelopes and two response modes in 9HP*

## Quick Start: Get Sound in 5 Minutes

Punch V3 is a dual-channel VCA with a built-in decay envelope generator on each channel. You patch an audio source in, a trigger in, and it shapes that audio with a decay contour. No separate envelope module required. Each channel also outputs its envelope as a CV signal, which you can send to any other module simultaneously.

1. Patch any audio source into CH1 IN
2. Patch a gate or trigger into CH1 TRIG|CV
3. Set mode switch to Vintage
4. Set DECAY to 12 o'clock
5. Set CURVE to 12 o'clock
6. Set AMOUNT to 2 o'clock
7. Trigger it and listen to the decay envelope shape the audio
8. Turn DECAY counterclockwise for a snappier result, clockwise for a longer tail

That is the core operation. Everything else extends from that foundation.

## Key Specs

| Spec | Value |
|------|-------|
| HP | 9 |
| Depth | ⚠️ unverified |
| +12V | 55mA |
| -12V | 52mA |
| 5V | 0mA |
| Channels | 2 (independent) |
| Self-oscillation | N/A |

## Essential Parameters

**Mode switch** selects between Vintage and CV behavior. In Vintage mode the module responds to triggers with a fixed, consistent envelope every time. The ACC|VEL input in this mode functions as an accent: a signal present at ACC|VEL when a trigger arrives adds extra intensity to that hit, mimicking the accent behavior of classic analog drum machines. In CV mode the entire response scales with the voltage at ACC|VEL. A higher voltage produces a louder, more open envelope; a lower voltage produces a quieter, more closed one. Vintage gives you reliable consistency. CV gives you dynamic expression tied to a sequenced or performed voltage.

**DECAY** sets how long the envelope takes to fall from its peak back to zero. Short DECAY times produce snappy transients. Long DECAY times let the audio breathe and sustain. DECAY has a CV input, so a sequencer or LFO can vary the decay time per step, producing rhythmic patterns with different lengths on each hit.

**CURVE** changes the shape of the decay contour. Counterclockwise settings produce a more linear fall, which sounds smoother and more modern. Clockwise settings produce a more aggressive exponential curve, which sounds snappier and more like a classic analog drum machine. CURVE is a timbre control as much as a timing control: the same DECAY time sounds dramatically different at opposite CURVE settings.

**AMOUNT** sets the gain of the VCA response. It controls the peak level the envelope reaches and how much of the input signal passes at the top of the envelope. At low AMOUNT settings even a fully open envelope is quiet. At high AMOUNT settings the module drives harder. Use AMOUNT to balance the output level against the rest of the patch and to control how much headroom the decay envelope uses.

**ACC|VEL input** functions differently depending on mode. In Vintage mode it is an accent input: a gate or trigger arriving here simultaneously with a TRIG|CV event produces a more intense hit. In CV mode it is a continuous scaling input: the voltage present here at the moment of each trigger determines the intensity of the response. Any CV source works, including sequencer velocity outputs, random sources, or even audio rate signals for AM effects.

**ENV output and invert switch** send the internal decay envelope as a CV signal to any destination. The envelope is generated whether or not any audio is patched into IN. Flipping the invert switch reverses the envelope polarity, producing a falling-to-rising shape instead of falling. This makes the ENV output useful for ducking, sidechain-style effects, and any parameter that needs to move in the opposite direction from the audio envelope.

## Why This Excels

Punch V3 is not a drum module with a narrow application. It is a dual-channel EG and VCA that happens to have excellent percussive character. The distinction matters. Any audio source that benefits from a decay contour belongs here: oscillator voices, granular output, noise bursts, pad layers, bass sequences. The module does not care what the source material is. It applies the same decay shaping regardless.

The two-mode design gives the module a split personality that is genuinely useful rather than redundant. Vintage mode produces the locked, consistent behavior that percussion programming requires. Every kick hit sounds the same, every accent sounds like an accent, and the pattern stays tight. Switching to CV mode opens the same physical controls to continuous dynamic expression, where the sequence or performer determines intensity on each event. Most patches benefit from choosing one mode and committing to it, but the option to switch during a performance creates instant character changes without any other modifications to the patch.

The ENV output is where Punch V3 becomes more than a VCA. One trigger event generates a decay envelope that simultaneously shapes the audio path through the VCA and sends a CV signal to any external destination. A filter cutoff, a second VCA, a pitch offset, a stereo imager input: all of these can track the envelope of the audio without any additional envelope generator in the patch. Each channel has its own independent ENV output, so both channels can modulate separate targets at different rates.

At 9HP for two independent channels, the HP-per-function ratio is efficient. A comparable patched setup, using separate VCAs and envelope generators for two channels, would require substantially more space and more cables. Punch V3 compresses that functionality into a form factor that works in systems of any size.

## Patches

### Patch 1: Percussive Voice Shape

A foundational patch demonstrating Vintage mode with a single channel. The focus is on learning how DECAY and CURVE interact to produce different transient characters from the same source.

```
[Hermod+] ── Gate out ───────────────────▶ [Punch V3 CH1 TRIG|CV]
[Cs-L OUT] ──────────────────────────────▶ [Punch V3 CH1 IN]

                                            Mode: Vintage
                                            DECAY: 11 o'clock
                                            CURVE: 2-3 o'clock
                                            AMOUNT: 2 o'clock

                             [Punch V3 CH1 OUT] ──▶ [MixUp CH1]
```

**Setup:** Patch Cs-L audio output into Punch V3 CH1 IN. Patch Hermod+ gate output into CH1 TRIG|CV. Set mode to Vintage, DECAY to 11 o'clock, CURVE to 2-3 o'clock, AMOUNT to 2 o'clock. Connect CH1 OUT to a MixUp channel.

**Controls:** Trigger Hermod+ and listen to the percussive decay shape. Turn CURVE counterclockwise toward 9 o'clock and listen to the envelope become smoother and longer-feeling at the same DECAY time. Turn CURVE clockwise toward 4 o'clock and listen to the decay become snappier with a sharper exponential bend. Now adjust DECAY to hear the range between short transient and extended tail. Try patching a second CV source into ACC|VEL and triggering with it simultaneously to hear the accent behavior.

**Result:** A shaped transient from the Cs-L voice, with CURVE and DECAY as independent handles on the character and length of the decay. The same patch produces entirely different results across the CURVE range without changing any other setting.

---

### Patch 2: Velocity-Responsive Sequence

CV mode with Hermod+ providing both gate and velocity outputs. The sequence programs note-to-note dynamic variation into the envelope response.

```
[Hermod+] ── Gate out ───────────────────▶ [Punch V3 CH1 TRIG|CV]
          └─ Velocity CV out ────────────▶ [Punch V3 CH1 ACC|VEL]
          └─ CV out (1V/oct) ────────────▶ [Cs-L 1V/OCT]

[Cs-L OUT] ──────────────────────────────▶ [Punch V3 CH1 IN]

                                            Mode: CV
                                            DECAY: 12 o'clock
                                            CURVE: 12 o'clock
                                            AMOUNT: 2 o'clock

                             [Punch V3 CH1 OUT] ──▶ [MixUp CH1]
```

**Setup:** Patch Hermod+ gate to CH1 TRIG|CV, Hermod+ velocity CV output to CH1 ACC|VEL, and Hermod+ pitch CV to Cs-L 1V/OCT. Set mode to CV. Program a sequence in Hermod+ with velocity variation between steps: some steps at full velocity, others at 30 to 50 percent, and occasional low-velocity ghost notes.

**Controls:** The velocity value at each step scales the entire envelope response. High-velocity steps hit hard and open. Low-velocity steps produce quiet, restrained hits from the same source. Increase AMOUNT to expand the dynamic range between the loudest and quietest steps. Try pulling DECAY down to 10 o'clock for a shorter overall envelope while keeping the velocity-driven dynamics. The combination of consistent decay time and variable intensity is different from what an envelope with attack and sustain controls produces.

**Result:** A melodic or rhythmic sequence where each note carries its own dynamic level set by the sequenced velocity, without any additional VCA or envelope in the patch.

---

### Patch 3: ENV Output as Filter Modulation

A two-source patch where Punch V3 shapes one audio path through its VCA while its ENV output simultaneously opens the filter on a second audio path running through Moon Phase. One trigger event creates coordinated movement across both processing chains.

```
[Hermod+] ── Gate A ──────────────────────▶ [Punch V3 CH1 TRIG|CV]
          └─ Gate A ──────────────────────▶ [Arbhar STRIKE]
          └─ CV (1V/oct) ─────────────────▶ [Cs-L 1V/OCT]

[Cs-L OUT] ───────────────────────────────▶ [Punch V3 CH1 IN]
[Arbhar OUT L] ───────────────────────────▶ [Moon Phase IN L]
[Arbhar OUT R] ───────────────────────────▶ [Moon Phase IN R]

[Punch V3 CH1 ENV OUT] ───────────────────▶ [Moon Phase ST f CV]

                                             Mode: Vintage
                                             DECAY: 1-2 o'clock
                                             CURVE: 11 o'clock
                                             AMOUNT: 2 o'clock

                              [Punch V3 CH1 OUT] ──▶ [MixUp CH1]
                              [Moon Phase OUT L] ──▶ [MixUp CH3 L]
                              [Moon Phase OUT R] ──▶ [MixUp CH3 R]
```

**Setup:** Hermod+ gate goes to both Punch CH1 TRIG|CV and Arbhar STRIKE, so both respond to the same trigger event. Cs-L audio feeds Punch CH1. Arbhar stereo outputs feed Moon Phase IN L and R. Punch CH1 ENV OUT connects to Moon Phase ST f CV. Set Moon Phase ST f to 9 o'clock as the base (closed) position. Set Punch DECAY to 1-2 o'clock for a longer envelope that gives Moon Phase time to open fully and decay.

**Controls:** Each trigger event does two things simultaneously: it shapes the Cs-L audio through the Punch VCA, and it opens Moon Phase's filter on the Arbhar output via the ENV output. Adjust DECAY to change how long both events last. Longer DECAY means the filter on Moon Phase stays open longer, letting more Arbhar content through before closing. Shorter DECAY produces a brief simultaneous transient in both paths. Try the invert switch on the ENV output to close the filter on each hit rather than open it, ducking the Arbhar content in response to the trigger.

**Result:** Two simultaneous processing events from a single trigger: a shaped Cs-L voice from the VCA, and a filter-modulated Arbhar texture from the ENV output. The patch feels coordinated without requiring any additional envelope generator.

---

### Patch 4: Dual-Channel Independent Shaping

Both channels running simultaneously with different sources, different DECAY settings, and different mode choices. Demonstrates treating each channel as an independent voice processor rather than a matched stereo pair.

```
[Hermod+] ── Gate A (kick pattern) ──────▶ [Punch V3 CH1 TRIG|CV]
          └─ Gate B (off-beat pattern) ───▶ [Punch V3 CH2 TRIG|CV]
          └─ Velocity CV ───────────────── ▶ [Punch V3 CH2 ACC|VEL]

[Cs-L OUT] ───────────────────────────────▶ [Punch V3 CH1 IN]
[Arbhar OUT L] ───────────────────────────▶ [Punch V3 CH2 IN]

          CH1: Vintage, DECAY 10 o'clock, CURVE 3 o'clock
          CH2: CV, DECAY 2 o'clock, CURVE 9 o'clock

                              [Punch V3 CH1 OUT] ──▶ [MixUp CH1]
                              [Punch V3 CH2 OUT] ──▶ [MixUp CH2]
```

**Setup:** Program two separate gate patterns in Hermod+: a regular on-beat or kick-style pattern for CH1, and an off-beat or irregular pattern for CH2 with velocity variation. Cs-L feeds CH1 and Arbhar feeds CH2. Set CH1 to Vintage mode with a short, aggressive CURVE and a snappy DECAY. Set CH2 to CV mode with a smooth CURVE and a longer DECAY so the Arbhar content sustains more between hits.

**Controls:** CH1 produces consistent punchy hits from Cs-L with the Vintage character. CH2 produces velocity-responsive Arbhar hits with a longer, smoother decay. The two channels occupy different rhythmic spaces and have different dynamic characters. Try sending CH1 ENV OUT to Moon Phase ST f CV as in Patch 3 while CH2 runs simultaneously, adding the coordinated filter event to the rhythmic texture.

**Result:** Two independent voice-shaping channels in the same module, each with its own mode, timing, source, and character. The interplay between the consistent CH1 hits and the dynamic CH2 response creates rhythmic interest without additional modules.

---

## Common Mistakes

### "I have audio patched in but I hear nothing."

Punch V3 requires a trigger or gate signal at TRIG|CV to open the envelope. Without a trigger signal the VCA stays closed regardless of what is patched into IN. This is not a malfunction. It is the core behavior of the module.

**Fix:** Patch a gate or trigger source into TRIG|CV and confirm it is firing. A sequencer gate output, a clock signal, or a manual gate will all work.

---

### "I am in CV mode but the velocity input does not seem to change anything."

When no signal is patched into ACC|VEL in CV mode the module receives zero volts at that input, which produces a quiet or silent response. The module is waiting for a CV signal to scale the envelope.

**Fix:** Confirm a voltage source is actively patched into ACC|VEL and is sending positive voltage at the time of each trigger. A sequencer velocity output, an envelope, or even a fixed voltage from an offset source will activate the CV mode response. Also confirm the mode switch is in the CV position and not Vintage.

---

### "I am not using the ENV output at all."

The ENV output sends the internal decay envelope as a CV signal to any destination and is available whether or not audio is patched into IN. Ignoring it means leaving a free envelope generator unused in every patch.

**Fix:** Patch ENV OUT to any modulatable parameter on another module: a filter cutoff, a second VCA, a pitch input, or a stereo imager. The envelope that is already shaping the audio path can simultaneously animate something else in the patch at no additional cost.

---

### "Both channels are producing the same result."

Punch V3 is a dual-channel module, but both channels have independent mode switches, DECAY, CURVE, and AMOUNT controls. If the settings are identical the results will be identical.

**Fix:** Set each channel to a different mode, a different DECAY time, and a different CURVE position. Patch different sources into each IN and use separate trigger patterns for each TRIG|CV. The two channels become two distinct voice processors rather than duplicates.

---

## Advanced Learning Path

1. Learn the DECAY and CURVE interaction before adding CV modulation. These two controls define the complete character of the decay contour, and understanding their relationship at fixed settings gives you a reliable mental model for what to expect when you begin modulating them. Spend time at several CURVE positions across the full DECAY range before connecting any external CV.

2. Explore Vintage mode accent behavior before moving to CV mode. In Vintage mode the ACC|VEL input responds to the presence of a signal rather than its exact level: a gate present when TRIG|CV fires produces a more intense hit than a gate absent on that event. Programming accent patterns with a sequencer in Vintage mode teaches you the original drum machine design intention of the module before you move to continuous velocity expression.

3. Use DECAY CV to vary tail length per step. Patch a sequencer's secondary CV output into the DECAY CV input and program different voltages per step. Short DECAY on some steps and long DECAY on others produces rhythmic interest without changing pitch or dynamics. This technique works on melodic voices as well as percussive ones.

4. Make the ENV output a habit. Every time you use Punch V3, decide what the ENV output will do before treating the patch as finished. Even a small modulation depth on a filter cutoff or pitch input adds movement that the audio envelope alone does not produce. The ENV output is a free resource that costs nothing to use.

5. Try the invert switch deliberately rather than occasionally. An inverted envelope closes a parameter as the trigger fires and then lets it return to baseline as the decay falls. This behavior is useful for ducking effects (close a VCA on another channel), reverse-style filter sweeps (shut the filter on each hit), and counterpoint movement (when one element rises, another falls).

6. Use both channels on non-percussive sources. A drone or pad running through Punch CH1 in CV mode with a slow gate pattern and a long DECAY time produces a completely different result than the same sound without shaping. Punch gives any continuously running source a rhythmic pulse tied to the gate pattern. The vintage drum machine character of the module is not mandatory; it is one application among many.

7. Treat Punch V3 as an EG first and a VCA second. The ENV output is a first-class output, not a utility afterthought. In patches where you need an envelope generator but do not need to shape audio directly, patch a dummy cable or nothing into IN and use only ENV OUT. A single trigger event from Hermod+ gives you two independent decay envelopes, one per channel, each going wherever they are most useful in the patch.

## Pairs Well With

**Instruo Cs-L** is a natural source for Punch V3 because Cs-L produces complex oscillator content with its own tonal character, and Punch shapes that content's dynamics without modifying the timbre directly. Cs-L's range of waveform outputs gives Punch a variety of source material to work with from a single module, and Cs-L's 1V/oct tracking means a Hermod+ sequence drives both pitch and the triggering of Punch in a single coordinated patch.

**Qu-Bit Hermod+** provides the gate and velocity infrastructure that Punch V3's dual mode design is built to use. Gate outputs trigger Punch's envelopes with precise rhythmic timing. Velocity CV outputs from Hermod+ sequences scale the CV mode response step by step. Having separate gate outputs for each Punch channel means both channels can run independent rhythmic patterns from the same sequencer, which is the most efficient way to drive the dual-channel architecture.

**Patching Panda Moon Phase** receives Punch V3's ENV output as a filter modulation source. Each trigger event that shapes the audio VCA simultaneously opens or closes Moon Phase's ST f filter on a separate audio path. This coupling between the VCA envelope and a downstream filter creates coordinated movement across two separate processing chains from a single trigger source, without any additional envelope generator in the patch.

**Intellijel MixUp** is the natural downstream endpoint for Punch V3's dual channel outputs. CH1 OUT and CH2 OUT feed separate MixUp channels, where the mix level for each shaped voice can be adjusted independently. MixUp's mute function makes it straightforward to bring each Punch channel in and out of the mix during performance without disrupting the patch.
