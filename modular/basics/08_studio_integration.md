# Studio Integration

**How the rack connects to your mixer, interface, DAW, and external gear , and why the signal chain between them requires attention.**

Every sound you make in the rack eventually has to leave it. It goes to a mixer, an audio interface, a DAW, a PA system, a pair of headphones, or some combination of all of these depending on whether you are recording, performing, or simply exploring. The rack produces audio at its own voltage level using its own internal logic. The world outside the rack operates at different levels and with different expectations. Bridging that gap reliably, without losing signal quality, introducing clipping, or building a chain you cannot troubleshoot, is what studio integration is about.

This guide covers the level problem, the role of in-rack mixing before the signal exits, the specific modules in this system that handle the transition (MixUp, Cockpit 2, and ListenIO), and how those modules connect to the equipment outside the rack. A note on scope: the external equipment in this guide is described generically. A companion document covering the specific studio gear in this setup will address the other end of the chain in detail; this document can be amended at that time to show the full picture.

---

## The Level Problem

Eurorack operates at a higher voltage level than nearly every other audio format it might connect to.

A typical Eurorack audio signal swings between roughly +5V and -5V, producing about 10 volts peak-to-peak (10Vpp). Some modules run hotter: oscillators with a lot of headroom, distortion modules near saturation, or matrix mixers summing multiple signals can exceed this. The system is designed to handle it.

The formats outside the rack are considerably quieter. Professional line level (the standard for studio mixers, audio interfaces, and outboard gear) runs at +4 dBu, which corresponds to approximately 1.23V RMS or around 3.5Vpp. Consumer line level (the -10 dBV standard found on home electronics and some instruments) is quieter still, around 0.316V RMS. The gap between modular and professional line is roughly a factor of 3 in voltage; the gap between modular and consumer line is much larger.

This difference is not a design flaw in either system. Eurorack needs high voltage headroom to carry signals with enough dynamic range to be musically useful as control voltages, which can range from slow DC offsets to fast audio-rate modulation without distorting. Professional studio equipment is optimized for the dynamic ranges of conventional instruments. They have different jobs.

The practical consequence: patching a Eurorack audio output directly into a mixer channel, audio interface input, or guitar amplifier input will almost always overdrive the destination input. The signal will clip, distort, or both. The solution is attenuation: reducing the modular signal before it reaches the outside world. The inverse applies in the other direction: external signals arriving at a modular input need amplification to reach a level the rack can work with.

---

## The Conversion Chain

A complete integration chain from rack to recording looks like this:

```
[Rack voices and effects]
         │
         │  modular level (~10Vpp)
         ▼
[In-rack submixer: MixUp]
         │
         │  modular level (consolidated stereo)
         ▼
[In-rack output stage: Cockpit 2]
         │
         │  attenuated to line level
         ▼
[Rack-mounted mixer or audio interface]
         │
         │  line level (+4 dBu)
         ▼
[DAW / PA / monitoring chain]
```

Each stage in this chain has a specific job. In-rack mixing consolidates multiple voices into a stereo pair before the signal exits. The output stage attenuates the modular signal to line level. The mixer or interface receives a clean line-level signal it can handle correctly.

ListenIO adds a parallel path for signals moving in the opposite direction, which is covered separately below.

---

## In-Rack Mixing: Why It Matters Before the Signal Leaves

It is technically possible to skip in-rack mixing and run multiple module outputs directly to separate inputs on an external mixer or audio interface. Each voice gets its own channel. Levels and balance are handled on the desk.

This works, but it trades rack problems for desk problems. Every modular output sent directly to an external input is another channel that needs a pad switch engaged, another gain knob to trim, and another input used up. As the patch grows (more voices, more effects returns, more layers), the patch cables running to the external equipment multiply. The external mixer becomes part of the patch: if you mute something on the desk, that decision is not visible in the rack. If you want to reroute something, you are pulling cables from the back of the desk, not the front of the case.

In-rack mixing resolves this by doing the organization work inside the rack where it belongs. Voices are balanced and summed to a stereo pair before the signal exits. The signal leaving the rack is a finished or nearly-finished mix, not a collection of individual sources. The external equipment receives something it can work with rather than something it needs to further organize.

The secondary benefit is gain staging. When multiple modular signals sum together at a mix bus, the total level rises. Managing that sum inside the rack, before attenuation, keeps the external equipment operating in its comfortable range. Adding levels together in the rack and then attenuating once is cleaner than sending multiple hot signals to separate inputs and trying to manage the sum at the desk.

---

## MixUp: Submixer Inside the Rack

The Intellijel MixUp is a six-HP stereo mixer that handles voice consolidation before the signal reaches the output stage.

MixUp has four input channels. Channels 1 and 2 accept mono signals with individual level knobs and mute switches: individual voices, mono effects, single oscillator outputs, or anything that needs to be placed into a stereo field. Channels 3 and 4 accept stereo pairs. Channel 3 has a shared level knob and mute switch for both sides. Channel 4 accepts a stereo pair at fixed unity gain with no panel controls, making it appropriate for a submix arriving from another MixUp unit or any source already at the correct level.

When a mono signal is patched into CH1 or CH2 with no stereo panning available, it appears on both MIX L and MIX R at equal level, centered in the stereo field. Stereo positioning of mono sources requires either a panning module upstream or accepting center placement for everything that arrives on channels 1 and 2.

Multiple MixUp units can be chained via back-panel headers, expanding the available input count without using additional front-panel outputs. Two MixUp units linked this way share a common mix bus: the sum of both units appears at the outputs of the primary unit.

In this system, MixUp feeds Cockpit 2. Voices and effects are balanced inside MixUp, and the stereo output becomes one of Cockpit 2's input channels. MixUp can also connect directly to an audio interface or output module when Cockpit 2 is not in the signal path for a particular patch.

---

## Cockpit 2: The Output Stage

The Endorphin.es Cockpit 2 is the final stage before the signal exits the rack. It is a four-channel stereo performance mixer with digital encoder control and a three-mode sidechain compressor.

Cockpit 2 handles one job at the system level: receive the consolidated stereo signal from the in-rack mix, set the final output level, and send a clean stereo pair to the rack-mounted mixer or console. Everything before Cockpit 2 is internal rack organization. Everything after Cockpit 2 is external equipment.

The four input channels accept stereo pairs, making Cockpit 2 suitable for receiving the MixUp output, an effects return, a secondary voice chain, or any other source that has already been mixed to stereo. The digital encoder controls channel levels, and the front-panel layout keeps the most important performance controls accessible during a live patch.

The sidechain compressor adds mix-bus dynamics control. In a sidechain configuration, a strong signal on one channel (typically a kick or other dominant transient) triggers gain reduction on another channel. This creates the pumping effect common in dance music, where the bass or pad briefly ducks each time the kick hits. In this rack, the Cockpit 2 sidechain operates on the output mix, allowing the relationship between elements to be shaped dynamically without a dedicated compressor module or external dynamics processor.

Cockpit 2 handles audio signals only. It is not a clock router, MIDI interface, or CV hub. Its role is audio mixing and level management at the point where the rack meets the outside world.

---

## ListenIO: Bidirectional Level Translation

The 4ms Company ListenIO handles signal conversion in both directions: modular level to line level for signals leaving the rack, and line level to modular level for signals entering the rack.

The module has two independent conversion stages. They operate completely independently of one another and can be used simultaneously or individually depending on what the patch requires.

### Outbound: Modular to Line Level

The bottom half of ListenIO attenuates modular-level audio down to line level for connection to a mixer, audio interface, or monitoring chain. The Level knob controls the amount of attenuation. The output appears at stereo line-level jacks and at a dual headphone jack for direct monitoring.

This path is useful when a signal needs to exit the rack to an external destination that is not the main stereo output. An effect being sent to an external processor, a parallel signal for recording separately, or a secondary output for a monitor mix can all use the ListenIO outbound stage while the main mix travels through Cockpit 2 on a different path.

The headphone jack on the ListenIO outbound stage makes it practical for monitoring during patching without committing the signal to the main output chain. Checking a new patch element in isolation, before it enters the main mix, is faster through a dedicated headphone output than through the main stereo chain.

### Inbound: Line Level to Modular

The top half of ListenIO amplifies external line-level signals up to modular level for use inside the rack. The Gain knob controls the amplification, which can reach up to approximately 30 times the input voltage.

The primary use for this stage is bringing external sound sources into the rack as audio. A synthesizer, drum machine, electric instrument through a DI, or any line-level signal source becomes available as a modular-level audio signal that can then be routed through filters, effects, VCAs, or any other processing in the rack.

This changes the rack from a closed system into an open one. The rack can process external audio the same way it processes internally generated audio. A drum machine running into the ListenIO input can be patched through the Forbidden Planet filter. An external synthesizer can run through the rack's reverb. The output of an external mixer can enter the rack for processing and exit through a different path.

The LED bar graph on the top section shows input level after the gain stage is applied. Four to six active LEDs on louder passages, with the red clip indicator not triggering, is the target range. Over-gained input will clip at the ListenIO input stage before it reaches the rack; the distortion this produces is not musically useful in most contexts and is not the same as intentional analog saturation.

The inbound and outbound stages are not linked. Running audio in one direction does not affect the other. In practice, most patches use one direction at a time: either bringing external audio in for rack processing, or sending modular audio out for recording or monitoring. Using both simultaneously (external audio in while modular audio exits) is possible and the module supports it, but the routing logic of the patch needs to be managed carefully to avoid signal path confusion.

---

## Audio Interface Integration

The audio interface is the bridge between the analog rack and the digital recording environment.

An interface converts analog audio signals to digital data for the computer and converts the computer's digital playback back to analog. It handles the analog-to-digital conversion (ADC) for incoming signals and digital-to-analog conversion (DAC) for outgoing signals. The quality of an interface's converters matters for recording fidelity; for Eurorack specifically, the interface also needs inputs that can handle a hot line-level signal without introducing noise at low gain settings.

There are two approaches to integrating the rack with an interface.

**Mixer, then interface:** The rack output (from Cockpit 2) goes to a channel on a mixing desk. The mixing desk's stereo bus or group output goes to the interface for recording. This approach keeps mixing and routing decisions in the analog domain until the last moment and keeps the interface inputs reserved for the final mix rather than individual sources. It also means the monitoring chain runs through the mixer, which adds monitoring options and tactile control.

**Direct to interface:** The rack output goes directly from Cockpit 2 to two channels on the audio interface (one per side of the stereo pair). Mixing and routing happens in the DAW rather than on a desk. This is a simpler physical chain with fewer pieces of equipment. It is appropriate when the DAW will handle final mix decisions, when no hardware mixer is in the chain, or when the interface has enough high-quality inputs to justify direct recording.

Neither approach is inherently better. The tradeoff is between analog mixing flexibility and chain simplicity.

**Input headroom:** Most audio interfaces accept line-level inputs on quarter-inch or XLR jacks. The nominal input level is +4 dBu for professional gear. The Cockpit 2 output is line-level after its internal attenuation, so it should feed the interface input at approximately unity gain: no pad switch needed, no extreme gain reduction required. If the interface input is overloading, reduce the Cockpit 2 output level before reaching for the interface input trim. The problem is upstream.

**Latency and monitoring:** Digital audio processing introduces latency: a small delay between when a signal enters the interface and when it appears at the output. For playback this is not audible. For real-time monitoring through a DAW, it is: if you are listening to the rack through the computer's speakers via the DAW, you will hear a delayed version of what you are playing. The solution is direct monitoring, available on most interfaces. Direct monitoring routes the interface input directly to the interface output in the analog domain, bypassing the computer entirely, so there is no latency in the monitoring path. The DAW still records the signal; it just does not need to be in the monitoring loop.

---

## Routing Diagrams

### Recording a Stereo Mix to DAW

```
[Voice 1: oscillator + filter + VCA] [A]
[Voice 2: oscillator + filter + VCA] [A]
[Drum voice: percussion module]       [A]
[Effects return: stereo reverb]       [A]
         │
         ▼
[MixUp CH1: Voice 1]
[MixUp CH2: Voice 2]
[MixUp CH3: Drum voice (mono → center)]
[MixUp CH3 return: reverb L/R]
         │
         │  stereo mix
         ▼
[Cockpit 2 CH1 L/R]
         │
         │  attenuated line level
         ▼
[Audio interface: line inputs L/R]
         │
         ▼
[DAW: stereo recording track]
```

The DAW receives a pre-mixed stereo signal. Individual voices are not separated at the interface. If stem recording (separate tracks per voice) is needed, each voice exits the rack individually to separate interface inputs, bypassing the in-rack mix.

---

### External Synth into the Rack for Processing

```
[External synthesizer: line output]
         │
         │  line level (~3.5Vpp)
         ▼
[ListenIO: top section, inbound]
[Gain knob: set for 4-6 LEDs active]
         │
         │  amplified to modular level
         ▼
[Rack effects: filter, reverb, VCA]
         │
         │  processed modular level
         ▼
[MixUp or Cockpit 2]
         │
         │  mixed with other voices, attenuated
         ▼
[Audio interface or mixer]
```

The external synthesizer's audio becomes part of the rack patch. It can be routed through any module that accepts audio. The result exits through the same output stage as everything else generated internally.

---

### Modular to Headphone Monitoring (Isolated)

```
[Work-in-progress voice]
         │
         │  modular level
         ▼
[ListenIO: bottom section, outbound]
[Level knob: set for comfortable headphone volume]
         │
         ▼
[Headphones: ListenIO headphone jack]
```

The main mix through Cockpit 2 is unaffected. This path is for checking a signal independently: verifying a patch element before it enters the main mix, monitoring a modulation source as audio to check its shape, or simply listening without routing changes to the main output.

---

## Common Mistakes

**Patching modular outputs directly to consumer inputs.** Guitar amplifier instrument inputs, consumer stereo receivers, headphone amplifiers not designed for line level, and some audio interface inputs without pad switches will be overdriven by modular-level audio. The result is distortion that does not go away no matter how much you lower the gain, because the input stage is already clipping. Always confirm the destination's expected input level before connecting the rack to it.

**Not setting the ListenIO gain before patching further.** The Gain knob on the inbound section amplifies incoming signals by up to 30 times. Leaving it at maximum and patching the output to a sensitive destination will produce an overloaded signal at the first module in the chain. Set the gain with the LED bar graph: find the range where 4-6 LEDs are active on program peaks without the red indicator triggering, then patch further.

**Using the main output chain for monitoring during patching.** If the main output is running to an interface for recording and the monitoring is through the DAW, there is latency in the monitoring path. Patching a new voice and hearing it delayed makes it difficult to judge how it sits in the mix. Use the ListenIO headphone output or a dedicated monitoring path for patch development, and keep the main output clean for the recording.

**Expecting stereo placement from MixUp channels 1 and 2.** Mono sources on CH1 and CH2 appear centered in the stereo field. If a source needs to sit left or right of center, it requires a panning module before MixUp, a stereo-output module (some percussion and effects modules provide separate L/R outputs), or placement on CH3 or CH4 after panning externally. The mix will feel narrow if everything is centered; plan stereo placement before signals reach the mix bus.

**Forgetting Cockpit 2's output level when changing patches.** Cockpit 2 retains its settings between patches. If a previous patch was quiet and a new one is loud, the Cockpit 2 output level set for the old patch may allow the new patch to overdrive the interface input before you have adjusted anything. Build the habit of checking the Cockpit 2 output level at the start of a new patch, especially if the voice count or signal architecture changed significantly.

**Running the ListenIO inbound and outbound simultaneously without a routing plan.** Both sections of ListenIO can run at the same time, but the two paths are independent. If external audio enters via the inbound stage and exits via the outbound stage, with the modular routing in between, that is a complete processing path and requires the same planning as any other patch chain. Confusion arises when the inbound output and the outbound input are accidentally connected to overlapping destinations, creating routing loops or doubled signals. Map the intended path before patching.

---

## What Comes Next

This guide described the modules in this system that handle studio integration. The full-length guides for each module cover their controls in detail:

- **Intellijel MixUp:** channel routing, mute behavior, chaining multiple units
- **4ms Company Listen IO:** gain calibration, monitoring workflow, both conversion stages
- **Endorphin.es Cockpit 2:** channel assignment, encoder operation, sidechain compressor modes

A future document will address the specific external equipment in this studio: the mixer, the audio interface, and the monitoring chain. This guide will be amended at that time to reflect those specifics.
