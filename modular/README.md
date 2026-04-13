# Modular Synthesis Guides

**60+ comprehensive guides for Eurorack and modular synthesis modules.**

Each guide covers Quick Start, Essential Parameters, Why This Excels, Patch Examples, Common Mistakes, Advanced Learning Path, and Pairs Well With. The goal is transferable understanding — not just how to operate a module, but why it works the way it does and how that knowledge applies across your whole system.

For the full project philosophy and methodology, see the [repository README](../README.md).

---

## New to Modular Synthesis?

**Start in the `/basics` directory before diving into individual module guides.**

The basics sequence builds from the ground up:

- [00 — Before You Buy Anything](basics/00_before_you_buy_anything.md) — what modular actually is, what it costs, what to expect
- [01 — Making Sound](basics/01_making_sound.md) — voltage, signal flow, your first patch
- [02 — Controlling Sound](basics/02_controlling_sound.md) — envelopes, filters, shaping a voice
- [03 — Musical Phrases](basics/03_musical_phrases.md) — sequencers, melody, rhythm
- [04 — Rhythm and Percussion](basics/04_rhythm_and_percussion.md) — drum voices, percussion architecture

After working through the basics, use the role-organized table below to find guides relevant to what you want to build.

---

## Finding Guides by Role

Modules are organized by their **primary signal function** — what they fundamentally do to signal, regardless of brand or form factor. This maps to the same functional roles found in DAWs, guitar pedals, DJ gear, and hardware synthesizers. A filter is a SHAPER whether it's a VCF module, a guitar pedal, or a channel EQ.

Most modules serve more than one role depending on how they're patched. The role listed is the primary function — the thing the module does most of the time in most patches.

---

### SOURCE
*Generates signal — audio, CV, gates, or noise.*

| Module | Function | Guide |
|--------|----------|-------|
| ALM Busy Circuits MCO ALM021 | Compact analog oscillator with through-zero FM | [Guide](alm_busy_circuits_mco_alm021_guide.md) |
| Cre8audio Chipz | Chip-style digital oscillator with classic waveforms | [Guide](cre8audio_chipz_guide.md) |
| Endorphin.es BLCK_NOIR | Analog drum and noise synthesizer with CV control | [Guide](endorphines_blck_noir_guide.md) |
| Endorphin.es Queen of Pentacles | Hybrid analog/sample module with spectral design | [Guide](endorphines_queen_of_pentacles_guide.md) |
| Erica Synths Pico Drum2 | Compact digital drum voice with multiple algorithms | [Guide](erica_synths_pico_drum2_guide.md) |
| Erica Synths Pico Voice | All-in-one compact oscillator/voice module | [Guide](erica_synths_pico_voice_guide.md) |
| Instruo Cs-L | West Coast complex oscillator with wavefolder and FM | [Guide](instruo_csl_guide.md) |
| Mutable Instruments Plaits | Macro-oscillator with 16 synthesis algorithms | [Guide](mutable_plaits_guide.md) |
| Mutable Instruments Rings | Physical modeling resonator; self-oscillates as a voice | [Guide](mutable_rings_guide.md) |
| Noise Engineering Loquelic Iteritas | Aggressive digital oscillator with phase-modulation architecture | [Guide](noise_engineering_loquelic_iteritas_guide.md) |
| Rossum Electro-Music Mob of Emus | Six-oscillator harmonic synthesizer with euclidean gates | [Guide](rossum_electro_music_mob_of_emus_guide.md) |
| VPME QD + QEX Drum Workstation | Quad drum voice module with sample and synthesis engines | [Guide](vpme_qd_qex_drum_workstation_guide.md) |
| Winterbloom Castor & Pollux II | Dual analog oscillator pair with choral drift | [Guide](winterbloom_castor_pollux_ii_guide.md) |

---

### SHAPER
*Transforms signal character — timbre, spectrum, space, texture.*

| Module | Function | Guide |
|--------|----------|-------|
| Bizarre Jezabel PKHIA MK2 | Analog wavefolder with harmonic generation | [Guide](bizarre_jezabel_pkhia_mk2_guide.md) |
| Doepfer A-124 Wasp SE | Aggressive CMOS filter clone with nonlinear character | [Guide](doepfer_a124_wasp_se_guide.md) |
| DSPcoffee Kali | Algorithmic reverb with multiple room models | [Guide](dspcoffee_kali_guide.md) |
| EarthQuaker Devices Afterneath | Nine-mode reverb/resonator/pitch-shifter | [Guide](earthquaker_devices_afterneath_guide.md) |
| Endorphin.es Ghost | Multi-effects processor with configurable routing order | [Guide](endorphines_ghost_guide.md) |
| Endorphin.es Squawk Dirty to Me | Eight-mode multimode filter with VCA and META CV | [Guide](endorphines_squawk_dirty_to_me_guide.md) |
| Erica Synths Black Polyvoks VCF | Soviet-era filter clone with aggressive character | [Guide](erica_synths_black_polyvoks_vcf_guide.md) |
| Erica Synths Pico DSP | Compact multi-algorithm effects processor | [Guide](erica_synths_pico_dsp_guide.md) |
| Instruo Arbhar | Granular processor with real-time and buffer modes | [Guide](instruo_arbhar_guide.md) |
| Noise Engineering Ruina Versio | Stereo distortion processor on the Versio firmware platform | [Guide](noise_engineering_ruina_versio_guide.md) |
| Soma Lyra-8 FX | Experimental effects processor with organic character | [Guide](soma_lyra8_fx_guide.md) |
| Tiptop Audio Forbidden Planet | State-variable filter with resonant character | [Guide](tiptop_audio_forbidden_planet_guide.md) |

---

### AMPLIFIER
*Controls signal level — gain staging, mixing, dynamics.*

| Module | Function | Guide |
|--------|----------|-------|
| Erica Synths Black Quad VCA2 | Four-channel VCA with normalization and lin/exp response | [Guide](erica_synths_black_quad_vca2_guide.md) |
| Erica Synths Pico VCA2 | Compact dual VCA with CV control | [Guide](erica_synths_pico_vca2_guide.md) |
| Intellijel MixUp | Four-channel stereo mixer with aux send | [Guide](intellijel_mixup_guide.md) |
| Tiptop Audio MISO | Attenuverter, mixer, and DC offset in 4HP | [Guide](tiptop_audio_miso_guide.md) |

---

### MODULATOR
*Generates time-varying control signals — envelopes, LFOs, random, function generators.*

| Module | Function | Guide |
|--------|----------|-------|
| Behringer Dual Envelope Generator 1003 | Dual ADSR with shared timing and bipolar outputs | [Guide](behringer_dual_envelope_generator_1003_utility_guide.md) |
| Blue Lantern Astroid | Multi-waveform LFO with CV control | [Guide](blue_lantern_astroid_guide.md) |
| Blue Lantern BLM Looping Simple ADSR v21 | Looping ADSR envelope with gate and trigger modes | [Guide](blue_lantern_modules_blm_looping_simple_adsr_v21_guide.md) |
| DivKid Ochd + Expander | Eight slow random LFOs for organic modulation | [Guide](divkid_ochd_and_expander_guide.md) |
| Erica Synths Black Envelope Generator 2 | Dual envelope with looping and complex shapes | [Guide](erica_synths_black_envelope_generator_2_guide.md) |
| Erica Synths Pico LFO SH | Compact LFO with sample-and-hold | [Guide](erica_synths_pico_lfo_sh_guide.md) |
| Make Noise Maths | Analog function generator; envelope, LFO, slew, logic | [Guide](make_noise_maths_guide.md) |
| Make Noise Wogglebug | Analog random voltage and gate generator | [Guide](make_noise_wogglebug_guide.md) |
| Mutable Instruments Marbles | Probabilistic random source with quantized and free outputs | [Guide](mutable_marbles_guide.md) |
| Patching Panda Moon Phase | Quadrature LFO with phase relationships | [Guide](patching_panda_moon_phase_guide.md) |
| Patching Panda Punch v3 | Snappy envelope/function generator with punch character | [Guide](patching_panda_punch_v3_guide.md) |
| Xaoc Devices Zadar + NIN | Four-channel envelope with vector shape drawing | [Guide](xaoc_devices_zadar_nin_guide.md) |

---

### CONTROLLER
*Defines timing, sequencing, and performance structure.*

| Module | Function | Guide |
|--------|----------|-------|
| 4ms Rotating Clock Divider v2 | Eight-output clock divider with rotation | [Guide](4ms_rcd_v2_guide.md) |
| 4ms SCM Plus | Clock multiplier with rotate, slip, shuffle, and skip | [Guide](4ms_scm_plus_guide.md) |
| ALM Busy Circuits Pamela's PRO Workout | Master clock with 8 programmable CV/gate outputs | [Guide](alm_busy_circuits_pamelas_pro_workout_guide.md) |
| AtoVproject lx-euclid | Touch-interface euclidean sequencer with four algorithms | [Guide](atovproject_lx-euclid_guide.md) |
| Cre8audio Cellz | Capacitive touch sequencer with probability | [Guide](cre8audio_cellz_guide.md) |
| Endorphin.es Ground Control | 42HP polymetric performance sequencer with CV modulation matrix | [Guide](endorphines_ground_control_guide.md) |
| Make Noise Pressure Points | Touch-plate controller and CV sequencer | [Guide](make_noise_pressure_points_guide.md) |
| Noise Engineering Numeric Repetitor | Prime-number rhythm generator with CV morphing | [Guide](noise_engineering_numeric_repetitor_guide.md) |
| Qubit Bloom v1 | Generative sequencer with algorithmic branching | [Guide](qubit_bloom_v1_guide.md) |
| Squarp Hermod+ | MIDI/CV sequencer with effects and advanced routing | [Guide](squarp_hermod_plus_guide.md) |
| Turing Machine Ecosystem | Binary shift register with probability-controlled evolution | [Guide](turing_machine_ecosystem_guide.md) |
| VPME QD + QEX Euclidean Circles Ecosystem | Euclidean gate sequencer with four independent channels | [Guide](vpme_qd_qex_euclidean_circles_ecosystem_guide.md) |

---

### ROUTER
*Distributes, combines, switches, or applies logic to signal paths.*

| Module | Function | Guide |
|--------|----------|-------|
| After Later Audio Cloaks | Eight-channel mute/unmute utility | [Guide](after_later_audio_cloaks_guide.md) |
| After Later Audio Mingles | Passive four-channel mult and mixer | [Guide](after_later_audio_mingles_guide.md) |
| Blue Lantern CMOS Party | Boolean logic processor with all standard gate operations | [Guide](blue_lantern_cmos_party_guide.md) |
| Cre8audio Function Junction | Logic, comparator, and utility functions | [Guide](cre8audio_function_junction_guide.md) |
| Intellijel Stomp | Guitar pedal interface adapter and signal router | [Guide](intellijel_stomp_guide.md) |
| Mutable Instruments Links | Buffered mult and unity-gain mixer | [Guide](mutable_instruments_links_guide.md) |

---

### ANALYZER
*Observes, measures, and displays signal behavior.*

| Module | Function | Guide |
|--------|----------|-------|
| Mordax Data | Oscilloscope, tuner, spectrum analyzer, and CV meter | [Guide](mordax_data_guide.md) |

---

### UTILITY
*Multi-function, hybrid, or cross-category modules.*

| Module | Function | Guide |
|--------|----------|-------|
| 4ms Company Listen IO | Audio interface and monitoring module | [Guide](4ms_company_listen_io_guide.md) |
| 4ms Company MetaModule | Runs VCV Rack patches in hardware; multi-function platform | [Guide](4ms_company_metamodule_guide.md) |
| Cre8audio Chipz + Cellz + Niftycase Bundle | Ecosystem guide for the complete Cre8audio bundle | [Guide](cre8audio_chipz_cellz_niftycase_bundle_guide.md) |
| Expert Sleepers Disting MK4 | 75+ algorithm multi-function module | [Guide](expert_sleepers_disting_mk4_guide.md) |

---

## Conceptual and Integration Guides

These guides cover synthesis concepts and cross-module integration rather than individual modules.

| Document | Description |
|----------|-------------|
| [Semi-Modular Integration Guide](semi_modular_integration_guide.md) | How semi-modular synthesizers connect to and expand Eurorack systems |

---

## About the Role System

Modules are tagged with a **primary role** and **secondary roles** reflecting how they function in a signal chain. The same taxonomy applies across domains — a SHAPER is a SHAPER whether it's a VCF module, a guitar distortion pedal, a DJ EQ, or a DAW plugin. This makes existing knowledge from any domain transferable.

**The eight roles:**
SOURCE · SHAPER · AMPLIFIER · MODULATOR · CONTROLLER · ROUTER · ANALYZER · UTILITY

Role metadata is being added to guide frontmatter progressively. When complete, it will enable automated table generation and cross-domain search.

---

*For full project philosophy, guide structure documentation, and methodology, see the [repository README](../README.md).*
