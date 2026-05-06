# Guide Audit Report

Generated: 2026-05-06

---

## Summary

| Metric | Count |
|--------|-------|
| Guides scanned | 93 |
| Guides with issues | 10 |
| Guides clean | 83 |
| Total issues | 18 |
| ❌ Errors (fix now) | 4 |
| ⚠️  Warnings (fix when touching) | 14 |
| 📌 Deferred (tracked, low priority) | 0 |

---

## Issues by Category

### YAML Frontmatter

| File | Line | Severity | Issue |
|------|------|----------|-------|
| `cre8audio_function_junction_guide.md` | — | ⚠️  warning | `use_cases` has 5 items; maximum is 4 |
| `instruo_arbhar_guide.md` | — | ⚠️  warning | `use_cases` has 5 items; maximum is 4 |
| `pittsburgh_modular_local_parks_guide.md` | — | ⚠️  warning | `use_cases` has 5 items; maximum is 4 |
| `pittsburgh_modular_the_toad_guide.md` | — | ⚠️  warning | `use_cases` has 5 items; maximum is 4 |
| `pittsburgh_modular_the_toad_guide.md` | — | ⚠️  warning | `use_cases` item too short (1 word): "phasing" |
| `pittsburgh_modular_the_toad_guide.md` | — | ⚠️  warning | `use_cases` item too short (1 word): "self-oscillation" |
| `qubit_mojave_guide.md` | — | ⚠️  warning | `use_cases` has 5 items; maximum is 4 |
| `qubit_prism_guide.md` | — | ⚠️  warning | `use_cases` has 6 items; maximum is 4 |
| `qubit_stardust_guide.md` | — | ⚠️  warning | `use_cases` has 5 items; maximum is 4 |
| `tesseract_modular_radioactive_guide.md` | — | ⚠️  warning | `use_cases` has 5 items; maximum is 4 |

### Missing or Misplaced Sections

| File | Line | Severity | Issue |
|------|------|----------|-------|
| `patching_panda_etna_guide.md` | — | ❌ error | Missing `## Why [Module] Excels` section (no 'Why' heading found) |
| `pittsburgh_modular_local_parks_guide.md` | — | ❌ error | Missing `## Why [Module] Excels` section (no 'Why' heading found) |
| `pittsburgh_modular_the_toad_guide.md` | — | ❌ error | Missing `## Why [Module] Excels` section (no 'Why' heading found) |
| `tesseract_modular_radioactive_guide.md` | — | ❌ error | Missing `## Why [Module] Excels` section (no 'Why' heading found) |

### Format Issues

| File | Line | Severity | Issue |
|------|------|----------|-------|
| `qubit_aurora_guide.md` | 46 | ⚠️  warning | Old color label: "7. FFT size defaults to 4096 (blue Reverse LED). To change it, hold Shift and press Revers" |
| `qubit_mojave_guide.md` | 56 | ⚠️  warning | Old color label: "**Gen button and Gen Gate input** trigger a single grain independent of the clock rate. Th" |
| `qubit_prism_guide.md` | 213 | ⚠️  warning | Old color label: "**Fix:** Press the Filter Type button to cycle to LPF (blue), HPF (green), or BPF (red). T" |
| `qubit_stardust_guide.md` | 84 | ⚠️  warning | Old color label: "**Effect Mode button** cycles through four effect modes, each assigning a different pair o" |

---

## Per-Guide Detail

**`cre8audio_function_junction_guide.md`** — 1 warning
  - ⚠️ `yaml_use_cases_count` — `use_cases` has 5 items; maximum is 4

**`instruo_arbhar_guide.md`** — 1 warning
  - ⚠️ `yaml_use_cases_count` — `use_cases` has 5 items; maximum is 4

**`patching_panda_etna_guide.md`** — 1 error
  - ❌ `section_why_excels` — Missing `## Why [Module] Excels` section (no 'Why' heading found)

**`pittsburgh_modular_local_parks_guide.md`** — 1 error, 1 warning
  - ❌ `section_why_excels` — Missing `## Why [Module] Excels` section (no 'Why' heading found)
  - ⚠️ `yaml_use_cases_count` — `use_cases` has 5 items; maximum is 4

**`pittsburgh_modular_the_toad_guide.md`** — 1 error, 3 warnings
  - ❌ `section_why_excels` — Missing `## Why [Module] Excels` section (no 'Why' heading found)
  - ⚠️ `yaml_use_cases_count` — `use_cases` has 5 items; maximum is 4
  - ⚠️ `yaml_use_cases_too_short` — `use_cases` item too short (1 word): "phasing"
  - ⚠️ `yaml_use_cases_too_short` — `use_cases` item too short (1 word): "self-oscillation"

**`qubit_aurora_guide.md`** — 1 warning
  - ⚠️ `color_labels` — Old color label: "7. FFT size defaults to 4096 (blue Reverse LED). To change it, hold Shift and press Revers" *(line 46)*

**`qubit_mojave_guide.md`** — 2 warnings
  - ⚠️ `yaml_use_cases_count` — `use_cases` has 5 items; maximum is 4
  - ⚠️ `color_labels` — Old color label: "**Gen button and Gen Gate input** trigger a single grain independent of the clock rate. Th" *(line 56)*

**`qubit_prism_guide.md`** — 2 warnings
  - ⚠️ `yaml_use_cases_count` — `use_cases` has 6 items; maximum is 4
  - ⚠️ `color_labels` — Old color label: "**Fix:** Press the Filter Type button to cycle to LPF (blue), HPF (green), or BPF (red). T" *(line 213)*

**`qubit_stardust_guide.md`** — 2 warnings
  - ⚠️ `yaml_use_cases_count` — `use_cases` has 5 items; maximum is 4
  - ⚠️ `color_labels` — Old color label: "**Effect Mode button** cycles through four effect modes, each assigning a different pair o" *(line 84)*

**`tesseract_modular_radioactive_guide.md`** — 1 error, 1 warning
  - ❌ `section_why_excels` — Missing `## Why [Module] Excels` section (no 'Why' heading found)
  - ⚠️ `yaml_use_cases_count` — `use_cases` has 5 items; maximum is 4

---

## Clean Guides (83)

No issues detected:

- `2hp_swarm_guide.md`
- `2hp_verb_guide.md`
- `4ms_company_listen_io_guide.md`
- `4ms_company_metamodule_guide.md`
- `4ms_rcd_v2_guide.md`
- `4ms_scm_plus_guide.md`
- `after_later_audio_cloaks_guide.md`
- `after_later_audio_mingles_guide.md`
- `alm_busy_circuits_mco_alm021_guide.md`
- `alm_busy_circuits_pamelas_pro_workout_guide.md`
- `altered_states_machines_eris_guide.md`
- `atovproject_lx-euclid_guide.md`
- `behringer_dual_envelope_generator_1003_utility_guide.md`
- `bela_gliss_guide.md`
- `bizarre_jezabel_pkhia_mk2_guide.md`
- `blue_lantern_astroid_guide.md`
- `blue_lantern_cmos_party_guide.md`
- `blue_lantern_modules_blm_looping_simple_adsr_v21_guide.md`
- `cre8audio_cellz_guide.md`
- `cre8audio_chipz_cellz_niftycase_bundle_guide.md`
- `cre8audio_chipz_guide.md`
- `divkid_ochd_and_expander_guide.md`
- `doepfer_a124_wasp_se_guide.md`
- `doepfer_a_130_2_guide.md`
- `dsp_coffee_yys_guide.md`
- `dspcoffee_kali_guide.md`
- `earthquaker_devices_afterneath_guide.md`
- `endorphines_blck_noir_guide.md`
- `endorphines_furthrrrr_generator_guide.md`
- `endorphines_ghost_guide.md`
- `endorphines_grand_terminal_guide.md`
- `endorphines_ground_control_guide.md`
- `endorphines_new_godspeed_guide.md`
- `endorphines_queen_of_pentacles_guide.md`
- `endorphines_squawk_dirty_to_me_guide.md`
- `erica_synths_black_envelope_generator_2_guide.md`
- `erica_synths_black_polyvoks_vcf_guide.md`
- `erica_synths_black_quad_vca2_guide.md`
- `erica_synths_pico_drum2_guide.md`
- `erica_synths_pico_dsp_guide.md`
- `erica_synths_pico_lfo_sh_guide.md`
- `erica_synths_pico_vca2_guide.md`
- `erica_synths_pico_voice_guide.md`
- `expert_sleepers_disting_mk4_guide.md`
- `frap_tools_411_guide.md`
- `gamechanger_audio_plasma_voice_guide.md`
- `instruo_csl_guide.md`
- `intellijel_mixup_guide.md`
- `intellijel_stomp_guide.md`
- `make_noise_maths_guide.md`
- `make_noise_pressure_points_guide.md`
- `make_noise_wogglebug_guide.md`
- `mordax_data_guide.md`
- `mutable_instruments_links_guide.md`
- `mutable_marbles_guide.md`
- `mutable_plaits_guide.md`
- `mutable_rings_guide.md`
- `noise_engineering_bia_guide.md`
- `noise_engineering_loquelic_iteritas_guide.md`
- `noise_engineering_mia_guide.md`
- `noise_engineering_numeric_repetitor_guide.md`
- `noise_engineering_pons_asinorum_guide.md`
- `noise_engineering_ruina_versio_guide.md`
- `patching_panda_moon_phase_guide.md`
- `patching_panda_punch_v3_guide.md`
- `qubit_bloom_v1_guide.md`
- `qubit_chord_v2_guide.md`
- `qubit_nautilus_guide.md`
- `rossum_electro_music_mob_of_emus_guide.md`
- `schlappi_engineering_100_grit_guide.md`
- `soma_lyra8_fx_guide.md`
- `squarp_hermod_plus_guide.md`
- `ssf_ssg_stereo_field_guide.md`
- `tesseract_modular_selam_guide.md`
- `tiptop_audio_forbidden_planet_guide.md`
- `tiptop_audio_miso_guide.md`
- `turing_machine_ecosystem_guide.md`
- `vostok_instruments_ceres_guide.md`
- `vpme_qd_qex_drum_workstation_guide.md`
- `vpme_qd_qex_euclidean_circles_ecosystem_guide.md`
- `winterbloom_castor_pollux_ii_guide.md`
- `xaoc_devices_belgrad_guide.md`
- `xaoc_devices_zadar_nin_guide.md`
