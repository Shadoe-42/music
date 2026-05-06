# Modular Synthesis Guides

**93 comprehensive guides for Eurorack and modular synthesis modules.**

Each guide covers Historical Context, Quick Start, Key Specifications, Why This Excels, Patch Examples, Common Mistakes, Advanced Learning Path, and Pairs Well With. The goal is transferable understanding: not just how to operate a module, but why it works the way it does and how that knowledge applies across your whole system.

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
- [05 — Signal Types and Mults](basics/05_signal_types_and_mults.md) — what is actually going through your cables
- [06 — Signal Chain](basics/06_signal_chain.md) — how audio and CV move through a patch from source to output
- [07 — Your First System](basics/07_your_first_system.md) — the physical connectivity needed to make sounds
- [08 — Studio Integration](basics/08_studio_integration.md) — connecting modular to DAWs, audio interfaces, and external gear
- [09 — Patch Infrastructure](basics/09_patch_infrastructure.md) — multiples, utilities, and the hidden plumbing of a working system

After working through the basics, use the role-organized table below to find guides relevant to what you want to build.

---

## Finding Guides by Role

Modules are organized by their **primary signal function** — what they fundamentally do to signal, regardless of brand or form factor. This maps to the same functional roles found in DAWs, guitar pedals, DJ gear, and hardware synthesizers. A filter is a SHAPER whether it's a VCF module, a guitar pedal, or a channel EQ.

Most modules serve more than one role depending on how they're patched. The role listed is the primary function — the thing the module does most of the time in most patches.

---

<!-- GENERATED:role_tables:start -->
### SOURCE
*Generates signal — audio, CV, gates, or noise.*

| Module | Function | Guide |
|--------|----------|-------|
| 2HP Swarm | Oscillator | [Guide](2hp_swarm_guide.md) |
| ALM Busy Circuits MCO ALM021 | Oscillator | [Guide](alm_busy_circuits_mco_alm021_guide.md) |
| Cre8audio Chipz | Oscillator | [Guide](cre8audio_chipz_guide.md) |
| Endorphin.es BLCK_NOIR | Drum Voice | [Guide](endorphines_blck_noir_guide.md) |
| Endorphin.es Furthrrrr Generator | Complex Oscillator, Wavefolder | [Guide](endorphines_furthrrrr_generator_guide.md) |
| Endorphin.es New Godspeed | Oscillator, Wavefolder | [Guide](endorphines_new_godspeed_guide.md) |
| Endorphin.es Queen of Pentacles | Drum Voice, Sample Player | [Guide](endorphines_queen_of_pentacles_guide.md) |
| Erica Synths Pico Drum2 | Sample Player | [Guide](erica_synths_pico_drum2_guide.md) |
| Erica Synths Pico Voice | Complex Oscillator, Filter, Envelope Generator | [Guide](erica_synths_pico_voice_guide.md) |
| Instruo Cs-L | Complex Oscillator | [Guide](instruo_csl_guide.md) |
| Mutable Instruments Plaits | Complex Oscillator, Drum Voice | [Guide](mutable_plaits_guide.md) |
| Mutable Instruments Rings | Resonator, Physical Model | [Guide](mutable_rings_guide.md) |
| Noise Engineering Loquelic Iteritas | FM Oscillator | [Guide](noise_engineering_loquelic_iteritas_guide.md) |
| Pittsburgh Modular Local Parks | Oscillator, Wavefolder | [Guide](pittsburgh_modular_local_parks_guide.md) |
| Qu-Bit Electronix Qu-Bit Chord V2 | Complex Oscillator | [Guide](qubit_chord_v2_guide.md) |
| Rossum Electro-Music Mob of Emus | FM Oscillator | [Guide](rossum_electro_music_mob_of_emus_guide.md) |
| Tesseract Modular Radioactive | Oscillator, Envelope Generator, Wavefolder | [Guide](tesseract_modular_radioactive_guide.md) |
| VPME QD + QEX Drum Workstation | Sample Player, Sequencer | [Guide](vpme_qd_qex_drum_workstation_guide.md) |
| Winterbloom Castor & Pollux II | Oscillator, FX Modulation | [Guide](winterbloom_castor_pollux_ii_guide.md) |

---

### SHAPER
*Transforms signal character — timbre, spectrum, space, texture.*

| Module | Function | Guide |
|--------|----------|-------|
| 2HP Verb | FX Time | [Guide](2hp_verb_guide.md) |
| Bizarre Jezabel PKHIA MK2 | Filter | [Guide](bizarre_jezabel_pkhia_mk2_guide.md) |
| Doepfer A-124 Wasp SE | Filter | [Guide](doepfer_a124_wasp_se_guide.md) |
| DSPcoffee Kali | FX Time, Distortion, FX Modulation | [Guide](dspcoffee_kali_guide.md) |
| EarthQuaker Devices Afterneath | FX Time | [Guide](earthquaker_devices_afterneath_guide.md) |
| Endorphin.es Ghost | FX Time, Filter, Dynamics | [Guide](endorphines_ghost_guide.md) |
| Endorphin.es Grand Terminal | Filter, Envelope Generator, FX Time | [Guide](endorphines_grand_terminal_guide.md) |
| Endorphin.es Squawk Dirty to Me | Filter | [Guide](endorphines_squawk_dirty_to_me_guide.md) |
| Erica Synths Black Polyvoks VCF | Filter | [Guide](erica_synths_black_polyvoks_vcf_guide.md) |
| Erica Synths Pico DSP | FX Time, FX Modulation | [Guide](erica_synths_pico_dsp_guide.md) |
| Instruo Arbhar | Granular | [Guide](instruo_arbhar_guide.md) |
| Noise Engineering Ruina Versio | Distortion | [Guide](noise_engineering_ruina_versio_guide.md) |
| Patching Panda Etna | Filter, Sequencer | [Guide](patching_panda_etna_guide.md) |
| Patching Panda Moon Phase | Filter | [Guide](patching_panda_moon_phase_guide.md) |
| Pittsburgh Modular The Toad | FX Modulation, LFO | [Guide](pittsburgh_modular_the_toad_guide.md) |
| Qu-Bit Electronix Aurora | FX Time, FX Spectral, FX Pitch | [Guide](qubit_aurora_guide.md) |
| Qu-Bit Electronix Nautilus | FX Time, FX Pitch | [Guide](qubit_nautilus_guide.md) |
| Qu-Bit Electronix Qu-Bit Mojave | Granular, FX Time | [Guide](qubit_mojave_guide.md) |
| Qu-Bit Electronix Qu-Bit Prism | FX Spectral, FX Time, Granular | [Guide](qubit_prism_guide.md) |
| Qu-Bit Electronix Qu-Bit Stardust | Looper, FX Time, Sample Player | [Guide](qubit_stardust_guide.md) |
| Schlappi Engineering 100 Grit | Distortion, Filter, VCA | [Guide](schlappi_engineering_100_grit_guide.md) |
| Soma Laboratory Soma Lyra-8 FX | FX Time, Distortion, FX Modulation | [Guide](soma_lyra8_fx_guide.md) |
| Steady State Fate SSG Stereo Field | Filter, VCA, Wavefolder | [Guide](ssf_ssg_stereo_field_guide.md) |
| Tiptop Audio Forbidden Planet | Filter | [Guide](tiptop_audio_forbidden_planet_guide.md) |
| Xaoc Devices Belgrad | Filter, Wavefolder | [Guide](xaoc_devices_belgrad_guide.md) |

---

### AMPLIFIER
*Controls signal level — gain staging, mixing, dynamics.*

| Module | Function | Guide |
|--------|----------|-------|
| Doepfer A-130-2 | VCA | [Guide](doepfer_a_130_2_guide.md) |
| Erica Synths Black Quad VCA2 | VCA, Mixer | [Guide](erica_synths_black_quad_vca2_guide.md) |
| Erica Synths Pico VCA2 | VCA | [Guide](erica_synths_pico_vca2_guide.md) |
| Frap Tools 411 | VCA, Mixer | [Guide](frap_tools_411_guide.md) |
| Intellijel MixUp | Mixer | [Guide](intellijel_mixup_guide.md) |
| Tiptop Audio MISO | VCA, Attenuator, CV Processor | [Guide](tiptop_audio_miso_guide.md) |
| Vostok Instruments Ceres | VCA, Mixer | [Guide](vostok_instruments_ceres_guide.md) |

---

### MODULATOR
*Generates time-varying control signals — envelopes, LFOs, random, function generators.*

| Module | Function | Guide |
|--------|----------|-------|
| Behringer Dual Envelope Generator 1003 | Envelope Generator | [Guide](behringer_dual_envelope_generator_1003_utility_guide.md) |
| Blue Lantern BLM Looping Simple ADSR v21 | Envelope Generator | [Guide](blue_lantern_modules_blm_looping_simple_adsr_v21_guide.md) |
| Cre8audio Function Junction | Function Generator, Mixer | [Guide](cre8audio_function_junction_guide.md) |
| DivKid Ochd + Expander | LFO | [Guide](divkid_ochd_and_expander_guide.md) |
| Erica Synths Black Envelope Generator 2 | Envelope Generator | [Guide](erica_synths_black_envelope_generator_2_guide.md) |
| Erica Synths Pico LFO SH | LFO, Sample Hold | [Guide](erica_synths_pico_lfo_sh_guide.md) |
| Make Noise Maths | Function Generator, CV Processor | [Guide](make_noise_maths_guide.md) |
| Make Noise Wogglebug | Random Source, Noise Source | [Guide](make_noise_wogglebug_guide.md) |
| Mutable Instruments Marbles | Random Source, Sequencer | [Guide](mutable_marbles_guide.md) |
| Noise Engineering Pons Asinorum | Envelope Generator, LFO | [Guide](noise_engineering_pons_asinorum_guide.md) |
| Patching Panda Punch V3 | VCA, Envelope Generator | [Guide](patching_panda_punch_v3_guide.md) |
| Tesseract Modular Selam | Function Generator, Attenuator, Slew Limiter | [Guide](tesseract_modular_selam_guide.md) |
| Xaoc Devices Zadar + NIN | Function Generator | [Guide](xaoc_devices_zadar_nin_guide.md) |

---

### CONTROLLER
*Defines timing, sequencing, and performance structure.*

| Module | Function | Guide |
|--------|----------|-------|
| 4ms Company 4ms Rotating Clock Divider v2 | Clock Divider | [Guide](4ms_rcd_v2_guide.md) |
| 4ms Company 4ms SCM Plus | Clock Multiplier, Clock Divider | [Guide](4ms_scm_plus_guide.md) |
| ALM Busy Circuits Pamela's PRO Workout | Clock Source, Euclidean Generator, LFO | [Guide](alm_busy_circuits_pamelas_pro_workout_guide.md) |
| AtoVproject lx-euclid | Euclidean Generator, Sequencer | [Guide](atovproject_lx-euclid_guide.md) |
| Bela Gliss | Sequencer, Function Generator, CV Processor | [Guide](bela_gliss_guide.md) |
| Cre8audio Cellz | Sequencer | [Guide](cre8audio_cellz_guide.md) |
| Endorphin.es Ground Control | Sequencer, Clock Source | [Guide](endorphines_ground_control_guide.md) |
| Make Noise Pressure Points | Sequencer | [Guide](make_noise_pressure_points_guide.md) |
| Music Thing Modular Turing Machine Ecosystem | Sequencer, Random Source | [Guide](turing_machine_ecosystem_guide.md) |
| Noise Engineering Numeric Repetitor | Sequencer, Euclidean Generator | [Guide](noise_engineering_numeric_repetitor_guide.md) |
| Qubit Bloom v1 | Sequencer | [Guide](qubit_bloom_v1_guide.md) |
| Squarp Hermod+ | Sequencer, Signal Router | [Guide](squarp_hermod_plus_guide.md) |
| VPME QD + QEX Euclidean Circles Ecosystem | Euclidean Generator, Clock Divider | [Guide](vpme_qd_qex_euclidean_circles_ecosystem_guide.md) |

---

### ROUTER
*Distributes, combines, switches, or applies logic to signal paths.*

| Module | Function | Guide |
|--------|----------|-------|
| After Later Audio Cloaks | VCA, Mixer | [Guide](after_later_audio_cloaks_guide.md) |
| After Later Audio Mingles | Mixer, LFO | [Guide](after_later_audio_mingles_guide.md) |
| Blue Lantern CMOS Party | Logic Processor | [Guide](blue_lantern_cmos_party_guide.md) |
| Intellijel Stomp | Audio Interface, Switch Router | [Guide](intellijel_stomp_guide.md) |
| Mutable Instruments Links | Mult, Attenuator | [Guide](mutable_instruments_links_guide.md) |

---

### ANALYZER
*Observes, measures, and displays signal behavior.*

| Module | Function | Guide |
|--------|----------|-------|
| Mordax Data | Oscilloscope, Tuner | [Guide](mordax_data_guide.md) |

---

### EVENT_VOICE
*Trigger-dependent sound engine with internally managed amplitude envelope.*

| Module | Function | Guide |
|--------|----------|-------|
| Blue Lantern Astroid | Drum Voice | [Guide](blue_lantern_astroid_guide.md) |
| Gamechanger Audio Plasma Voice | Voice Engine, Oscillator, Distortion | [Guide](gamechanger_audio_plasma_voice_guide.md) |
| Noise Engineering Basimilus Iteritas Alter | Drum Voice, FM Oscillator, Wavefolder | [Guide](noise_engineering_bia_guide.md) |
| Noise Engineering Manis Iteritas Alia | Drum Voice, FM Oscillator, Distortion | [Guide](noise_engineering_mia_guide.md) |

---

### UTILITY
*Multi-function, hybrid, or cross-category modules.*

| Module | Function | Guide |
|--------|----------|-------|
| 4ms Company Listen IO | Audio Interface | [Guide](4ms_company_listen_io_guide.md) |
| 4ms Company MetaModule | Audio Interface | [Guide](4ms_company_metamodule_guide.md) |
| Altered States Machines Eris | Mixer, CV Processor, Switch Router | [Guide](altered_states_machines_eris_guide.md) |
| Cre8audio Chipz + Cellz + Niftycase Bundle | Oscillator, Sequencer | [Guide](cre8audio_chipz_cellz_niftycase_bundle_guide.md) |
| DSP Coffee YYS | Attenuator, Mixer, CV Processor | [Guide](dsp_coffee_yys_guide.md) |
| Expert Sleepers Disting MK4 | Oscillator, FX Time, Envelope Generator | [Guide](expert_sleepers_disting_mk4_guide.md) |

---

<!-- GENERATED:role_tables:end -->


## Conceptual and Integration Guides

These guides cover synthesis concepts and cross-module integration rather than individual modules.

| Document | Description |
|----------|-------------|
| [Semi-Modular Integration Guide](semi_modular_integration_guide.md) | How semi-modular synthesizers connect to and expand Eurorack systems |

---

## Patch Library

Complete patch walkthroughs organized by experience level. Each patch documents the full signal path, module list, and what the patch teaches.

**Beginner** (`patches/beginner/`)
- [01 — First Voice](patches/beginner/01_first_voice.md)
- [02 — Clock and Sequence](patches/beginner/02_clock_sequence.md)
- [03 — Modulation Magic](patches/beginner/03_modulation_magic.md)
- [04 — Random and Chaos](patches/beginner/04_random_chaos.md)
- [05 — Drum Machine](patches/beginner/05_drum_machine.md)
- [06 — Multiple Voices](patches/beginner/06_multiple_voices.md)

**Intermediate** (`patches/intermediate/`)
- [Disting as Clock Source](patches/intermediate/disting_clock_source.md)
- [Simple Patches](patches/intermediate/simple_patches.md)
- [Trinity Minimal](patches/intermediate/trinity_minimal.md)

**Advanced** (`patches/advanced/`)
- [Ambient Evolution](patches/advanced/ambient_evolution.md)
- [Cascading Chaos](patches/advanced/cascading_chaos.md)
- [Industrial Evolution](patches/advanced/industrial_evolution.md)

---

## About the Role System

Modules are tagged with a **primary role** and **secondary roles** reflecting how they function in a signal chain. The same taxonomy applies across domains — a SHAPER is a SHAPER whether it's a VCF module, a guitar distortion pedal, a DJ EQ, or a DAW plugin. This makes existing knowledge from any domain transferable.

**The nine roles:**
SOURCE · SHAPER · AMPLIFIER · MODULATOR · CONTROLLER · ROUTER · ANALYZER · EVENT_VOICE · UTILITY

Role metadata is present in all guide frontmatter and drives the automated table generation above. The same taxonomy applies across domains — pedals, standalone synths, rack gear — enabling cross-domain search as those guide sets are added.

---

*For full project philosophy, guide structure documentation, and methodology, see the [repository README](../README.md).*
