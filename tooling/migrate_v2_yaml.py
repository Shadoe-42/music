#!/usr/bin/env python3
"""
YAML v2 Migration Script
Adds form_factor, functions, behavior_tags, and use_cases to all 68 guides.
Also adds capability flags (memory, transport, screen, hybrid) where clearly applicable.

Usage:
    python3 tooling/migrate_v2_yaml.py [--dry-run]

    --dry-run   Print what would change without writing files.
"""

import argparse
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Migration data
# Fields added to each guide's YAML frontmatter.
# All fields inserted after secondary_roles, before hp.
# Capability flags (memory/transport/screen/hybrid) included only where known.
# ---------------------------------------------------------------------------

MIGRATION = {
    "4ms_company_listen_io_guide.md": {
        "form_factor": "eurorack",
        "functions": ["audio-interface"],
        "behavior_tags": ["clean", "stable", "linear", "reactive"],
        "use_cases": ["stereo output to external mixer", "headphone monitoring in patch", "recording Eurorack audio"],
    },
    "4ms_company_metamodule_guide.md": {
        "form_factor": "eurorack",
        "functions": ["audio-interface"],
        "behavior_tags": ["stable", "performance-oriented", "generative"],
        "use_cases": ["VCV Rack patch in hardware", "software-defined synthesis", "generative patch deployment"],
        "memory": "full",
        "hybrid": "true",
    },
    "4ms_rcd_v2_guide.md": {
        "form_factor": "eurorack",
        "functions": ["clock-divider"],
        "behavior_tags": ["stable", "percussive", "linear", "performance-oriented"],
        "use_cases": ["polyrhythmic clock division", "rhythmic gate patterns", "clock distribution"],
        "transport": "receive",
    },
    "4ms_scm_plus_guide.md": {
        "form_factor": "eurorack",
        "functions": ["clock-multiplier", "clock-divider"],
        "behavior_tags": ["stable", "percussive", "linear"],
        "use_cases": ["clock multiplication for fast divisions", "swing and shuffle timing", "polyrhythmic clock source"],
        "transport": "receive",
    },
    "after_later_audio_cloaks_guide.md": {
        "form_factor": "eurorack",
        "functions": ["vca", "mixer"],
        "behavior_tags": ["clean", "stable", "linear", "reactive"],
        "use_cases": ["audio mixing and routing", "CV-controlled voice mixing", "signal summing"],
    },
    "after_later_audio_mingles_guide.md": {
        "form_factor": "eurorack",
        "functions": ["mixer", "lfo"],
        "behavior_tags": ["clean", "warm", "stable", "performance-oriented"],
        "use_cases": ["audio mixing and routing", "VC panning and stereo placement", "modulated mixing"],
    },
    "alm_busy_circuits_mco_alm021_guide.md": {
        "form_factor": "eurorack",
        "functions": ["oscillator"],
        "behavior_tags": ["stable", "clean", "bright", "linear"],
        "use_cases": ["lead voice", "bass voice", "stable pitch reference"],
    },
    "alm_busy_circuits_pamelas_pro_workout_guide.md": {
        "form_factor": "eurorack",
        "functions": ["clock-source", "euclidean-generator", "lfo"],
        "behavior_tags": ["stable", "percussive", "linear", "performance-oriented", "generative"],
        "use_cases": ["clock source for full system", "euclidean rhythm source", "gate and trigger source"],
        "memory": "full",
        "transport": "receive",
        "screen": "true",
    },
    "atovproject_lx-euclid_guide.md": {
        "form_factor": "eurorack",
        "functions": ["euclidean-generator", "sequencer"],
        "behavior_tags": ["stable", "percussive", "linear", "generative"],
        "use_cases": ["euclidean rhythm source", "polyrhythmic pattern generator", "rhythmic gate patterns"],
    },
    "behringer_dual_envelope_generator_1003_utility_guide.md": {
        "form_factor": "eurorack",
        "functions": ["envelope-generator"],
        "behavior_tags": ["stable", "gated", "linear", "reactive"],
        "use_cases": ["envelope shaping", "gate and trigger source", "drum envelope control"],
    },
    "bizarre_jezabel_pkhia_mk2_guide.md": {
        "form_factor": "eurorack",
        "functions": ["wavefolder"],
        "behavior_tags": ["dirty", "harmonic", "nonlinear", "reactive", "performance-oriented"],
        "use_cases": ["waveshaping and distortion", "timbral movement and shaping", "harmonic enrichment"],
    },
    "blue_lantern_astroid_guide.md": {
        "form_factor": "eurorack",
        "functions": ["drum-voice"],
        "behavior_tags": ["percussive", "gated", "warm", "dirty", "performance-oriented"],
        "use_cases": ["808 style kick drum voice", "analog percussion synthesis", "percussive bass layer"],
    },
    "blue_lantern_cmos_party_guide.md": {
        "form_factor": "eurorack",
        "functions": ["logic-processor"],
        "behavior_tags": ["stable", "percussive", "reactive", "linear"],
        "use_cases": ["trigger pattern generation", "clock manipulation", "audio rate logic processing"],
    },
    "blue_lantern_modules_blm_looping_simple_adsr_v21_guide.md": {
        "form_factor": "eurorack",
        "functions": ["envelope-generator"],
        "behavior_tags": ["stable", "gated", "free-running", "linear"],
        "use_cases": ["envelope shaping", "modulation source", "looping LFO-style envelope"],
    },
    "cre8audio_cellz_guide.md": {
        "form_factor": "eurorack",
        "functions": ["sequencer"],
        "behavior_tags": ["stable", "performance-oriented", "reactive", "sensitive"],
        "use_cases": ["gate and trigger source", "performance touch control", "pitch CV source"],
    },
    "cre8audio_chipz_cellz_niftycase_bundle_guide.md": {
        "form_factor": "eurorack",
        "functions": ["oscillator", "sequencer"],
        "behavior_tags": ["stable", "warm", "performance-oriented"],
        "use_cases": ["complete starter system", "beginner voice and control", "semi-modular exploration"],
    },
    "cre8audio_chipz_guide.md": {
        "form_factor": "eurorack",
        "functions": ["oscillator"],
        "behavior_tags": ["stable", "bright", "harmonic", "linear"],
        "use_cases": ["lead voice", "chiptune synthesis", "bass voice"],
    },
    "cre8audio_function_junction_guide.md": {
        "form_factor": "eurorack",
        "functions": ["cv-processor", "mixer", "logic-processor"],
        "behavior_tags": ["stable", "linear", "reactive"],
        "use_cases": ["CV scaling and utility", "audio mixing and routing", "signal distribution"],
    },
    "divkid_ochd_and_expander_guide.md": {
        "form_factor": "eurorack",
        "functions": ["lfo"],
        "behavior_tags": ["free-running", "evolving", "stable", "generative"],
        "use_cases": ["modulation source", "evolving ambient texture", "stochastic modulation"],
    },
    "doepfer_a124_wasp_se_guide.md": {
        "form_factor": "eurorack",
        "functions": ["filter"],
        "behavior_tags": ["dirty", "warm", "harmonic", "nonlinear", "unstable"],
        "use_cases": ["timbral movement and shaping", "dirty filter character", "lead voice when self-oscillating"],
    },
    "doepfer_a_130_2_guide.md": {
        "form_factor": "eurorack",
        "functions": ["vca"],
        "behavior_tags": ["clean", "stable", "linear", "reactive"],
        "use_cases": ["envelope shaping", "audio mixing and routing", "CV-controlled attenuation"],
    },
    "dspcoffee_kali_guide.md": {
        "form_factor": "eurorack",
        "functions": ["fx-time", "lfo"],
        "behavior_tags": ["evolving", "warm", "nonlinear", "generative", "performance-oriented"],
        "use_cases": ["evolving ambient texture", "stereo signal processing", "modulation source", "self-evolving patch element"],
        "memory": "full",
        "screen": "true",
    },
    "earthquaker_devices_afterneath_guide.md": {
        "form_factor": "eurorack",
        "functions": ["fx-time"],
        "behavior_tags": ["evolving", "dark", "nonlinear", "generative"],
        "use_cases": ["evolving ambient texture", "dark atmospheric layer", "drone foundation"],
    },
    "endorphines_blck_noir_guide.md": {
        "form_factor": "eurorack",
        "functions": ["drum-voice"],
        "behavior_tags": ["percussive", "gated", "dirty", "warm", "harmonic", "performance-oriented"],
        "use_cases": ["rhythmic percussion layer", "analog drum voice set", "full drum kit synthesis"],
        "memory": "basic",
        "screen": "true",
        "hybrid": "true",
    },
    "endorphines_ghost_guide.md": {
        "form_factor": "eurorack",
        "functions": ["fx-time", "fx-modulation"],
        "behavior_tags": ["evolving", "clean", "warm", "nonlinear"],
        "use_cases": ["evolving ambient texture", "stereo signal processing", "dark atmospheric layer"],
    },
    "endorphines_ground_control_guide.md": {
        "form_factor": "eurorack",
        "functions": ["sequencer", "clock-source"],
        "behavior_tags": ["stable", "performance-oriented", "reactive", "linear"],
        "use_cases": ["generative melodic sequence", "gate and trigger source", "clock source for full system"],
        "memory": "full",
        "transport": "full",
        "screen": "true",
    },
    "endorphines_queen_of_pentacles_guide.md": {
        "form_factor": "eurorack",
        "functions": ["drum-voice", "sample-player"],
        "behavior_tags": ["percussive", "gated", "dirty", "warm", "performance-oriented"],
        "use_cases": ["hybrid drum voice set", "rhythmic percussion layer", "full drum kit with samples"],
        "memory": "basic",
        "screen": "true",
        "hybrid": "true",
    },
    "endorphines_squawk_dirty_to_me_guide.md": {
        "form_factor": "eurorack",
        "functions": ["filter"],
        "behavior_tags": ["dirty", "warm", "nonlinear", "reactive", "performance-oriented"],
        "use_cases": ["timbral movement and shaping", "stereo signal processing", "aggressive filter character"],
    },
    "erica_synths_black_envelope_generator_2_guide.md": {
        "form_factor": "eurorack",
        "functions": ["envelope-generator"],
        "behavior_tags": ["stable", "gated", "linear", "reactive"],
        "use_cases": ["envelope shaping", "gate and trigger source", "modulation source"],
    },
    "erica_synths_black_polyvoks_vcf_guide.md": {
        "form_factor": "eurorack",
        "functions": ["filter"],
        "behavior_tags": ["dirty", "harsh", "nonlinear", "unstable", "performance-oriented"],
        "use_cases": ["timbral movement and shaping", "dirty filter character", "aggressive sound design"],
    },
    "erica_synths_black_quad_vca2_guide.md": {
        "form_factor": "eurorack",
        "functions": ["vca", "mixer"],
        "behavior_tags": ["clean", "stable", "linear", "reactive"],
        "use_cases": ["audio mixing and routing", "CV-controlled mixing", "voice summing"],
    },
    "erica_synths_pico_drum2_guide.md": {
        "form_factor": "eurorack",
        "functions": ["sample-player"],
        "behavior_tags": ["percussive", "gated", "reactive", "stable"],
        "use_cases": ["rhythmic percussion layer", "sample playback", "drum voice in small system"],
    },
    "erica_synths_pico_dsp_guide.md": {
        "form_factor": "eurorack",
        "functions": ["fx-time", "fx-modulation"],
        "behavior_tags": ["stable", "clean", "evolving", "linear"],
        "use_cases": ["stereo signal processing", "evolving ambient texture", "reverb and delay in small system"],
        "memory": "none",
    },
    "erica_synths_pico_lfo_sh_guide.md": {
        "form_factor": "eurorack",
        "functions": ["lfo", "sample-hold"],
        "behavior_tags": ["free-running", "stable", "stochastic", "generative"],
        "use_cases": ["modulation source", "random CV generator", "stochastic modulation"],
    },
    "erica_synths_pico_vca2_guide.md": {
        "form_factor": "eurorack",
        "functions": ["vca"],
        "behavior_tags": ["clean", "stable", "linear", "reactive"],
        "use_cases": ["envelope shaping", "audio mixing and routing", "CV scaling and utility"],
    },
    "erica_synths_pico_voice_guide.md": {
        "form_factor": "eurorack",
        "functions": ["oscillator", "filter", "envelope-generator"],
        "behavior_tags": ["warm", "stable", "gated", "linear", "performance-oriented"],
        "use_cases": ["complete voice in small system", "lead voice", "bass voice"],
    },
    "expert_sleepers_disting_mk4_guide.md": {
        "form_factor": "eurorack",
        "functions": ["oscillator", "fx-time", "envelope-generator"],
        "behavior_tags": ["stable", "linear", "reactive", "performance-oriented"],
        "use_cases": ["utility fill-in role", "problem-solving in-patch", "whatever is needed right now"],
        "memory": "none",
        "screen": "true",
    },
    "frap_tools_411_guide.md": {
        "form_factor": "eurorack",
        "functions": ["vca", "mixer"],
        "behavior_tags": ["clean", "stable", "linear", "reactive"],
        "use_cases": ["audio mixing and routing", "CV-controlled mixing", "signal distribution"],
    },
    "instruo_arbhar_guide.md": {
        "form_factor": "eurorack",
        "functions": ["granular"],
        "behavior_tags": ["evolving", "nonlinear", "stochastic", "generative", "performance-oriented"],
        "use_cases": ["granular texture bed", "evolving ambient texture", "dark atmospheric layer"],
    },
    "instruo_csl_guide.md": {
        "form_factor": "eurorack",
        "functions": ["complex-oscillator"],
        "behavior_tags": ["harmonic", "warm", "nonlinear", "evolving", "performance-oriented"],
        "use_cases": ["lead voice", "complex harmonic texture", "bass voice", "chord voice"],
    },
    "intellijel_mixup_guide.md": {
        "form_factor": "eurorack",
        "functions": ["mixer"],
        "behavior_tags": ["clean", "stable", "linear"],
        "use_cases": ["audio mixing and routing", "signal summing", "stereo bus mixing"],
    },
    "intellijel_stomp_guide.md": {
        "form_factor": "eurorack",
        "functions": ["audio-interface", "switch-router"],
        "behavior_tags": ["clean", "stable", "linear", "reactive"],
        "use_cases": ["guitar pedal integration in Eurorack", "effects loop routing", "audio interface for pedals"],
    },
    "make_noise_maths_guide.md": {
        "form_factor": "eurorack",
        "functions": ["function-generator", "cv-processor"],
        "behavior_tags": ["free-running", "evolving", "nonlinear", "performance-oriented", "generative"],
        "use_cases": ["envelope shaping", "modulation source", "CV scaling and utility", "self-evolving patch element"],
    },
    "make_noise_pressure_points_guide.md": {
        "form_factor": "eurorack",
        "functions": ["sequencer"],
        "behavior_tags": ["stable", "performance-oriented", "reactive", "sensitive", "gated"],
        "use_cases": ["performance touch control", "pitch CV source", "gate and trigger source"],
    },
    "make_noise_wogglebug_guide.md": {
        "form_factor": "eurorack",
        "functions": ["random-source", "noise-source"],
        "behavior_tags": ["stochastic", "evolving", "noisy", "chaotic", "generative"],
        "use_cases": ["stochastic modulation", "random CV generator", "chaotic texture source"],
    },
    "mordax_data_guide.md": {
        "form_factor": "eurorack",
        "functions": ["oscilloscope", "tuner"],
        "behavior_tags": ["stable", "clean", "linear", "reactive"],
        "use_cases": ["signal analysis and measurement", "tuning and calibration", "patch visualization"],
        "screen": "true",
    },
    "mutable_instruments_links_guide.md": {
        "form_factor": "eurorack",
        "functions": ["mult", "attenuator"],
        "behavior_tags": ["clean", "stable", "linear"],
        "use_cases": ["signal distribution", "CV scaling and utility", "audio mixing and routing"],
    },
    "mutable_marbles_guide.md": {
        "form_factor": "eurorack",
        "functions": ["random-source", "sequencer"],
        "behavior_tags": ["stochastic", "evolving", "generative", "free-running", "performance-oriented"],
        "use_cases": ["generative melodic sequence", "stochastic modulation", "random CV generator", "self-evolving patch element"],
    },
    "mutable_plaits_guide.md": {
        "form_factor": "eurorack",
        "functions": ["complex-oscillator", "drum-voice"],
        "behavior_tags": ["harmonic", "stable", "warm", "gated", "performance-oriented"],
        "use_cases": ["lead voice", "bass voice", "percussive voice", "chord voice"],
    },
    "mutable_rings_guide.md": {
        "form_factor": "eurorack",
        "functions": ["resonator", "physical-model"],
        "behavior_tags": ["harmonic", "sustained", "metallic", "evolving", "performance-oriented"],
        "use_cases": ["harmonic pad", "evolving ambient texture", "chord voice", "drone foundation"],
    },
    "noise_engineering_loquelic_iteritas_guide.md": {
        "form_factor": "eurorack",
        "functions": ["fm-oscillator"],
        "behavior_tags": ["harsh", "inharmonic", "harmonic", "nonlinear", "performance-oriented"],
        "use_cases": ["lead voice", "inharmonic texture", "metallic percussion voice"],
    },
    "noise_engineering_numeric_repetitor_guide.md": {
        "form_factor": "eurorack",
        "functions": ["sequencer", "euclidean-generator"],
        "behavior_tags": ["stable", "percussive", "generative", "stochastic", "performance-oriented"],
        "use_cases": ["rhythmic pattern generator", "euclidean rhythm source", "polyrhythmic gate patterns"],
    },
    "noise_engineering_ruina_versio_guide.md": {
        "form_factor": "eurorack",
        "functions": ["distortion"],
        "behavior_tags": ["dirty", "harsh", "nonlinear", "performance-oriented", "harmonic"],
        "use_cases": ["waveshaping and distortion", "aggressive sound design", "timbral movement and shaping"],
    },
    "patching_panda_moon_phase_guide.md": {
        "form_factor": "eurorack",
        "functions": ["filter"],
        "behavior_tags": ["clean", "stable", "dark", "nonlinear", "performance-oriented"],
        "use_cases": ["stereo signal processing", "timbral movement and shaping", "evolving ambient texture"],
    },
    "patching_panda_punch_v3_guide.md": {
        "form_factor": "eurorack",
        "functions": ["vca", "envelope-generator"],
        "behavior_tags": ["percussive", "gated", "reactive", "warm", "performance-oriented"],
        "use_cases": ["percussive voice shaping", "drum hit dynamics", "envelope shaping"],
    },
    "qubit_bloom_v1_guide.md": {
        "form_factor": "eurorack",
        "functions": ["sequencer"],
        "behavior_tags": ["stable", "generative", "stochastic", "evolving", "performance-oriented"],
        "use_cases": ["generative melodic sequence", "self-evolving patch element", "probability-based variation"],
        "memory": "full",
        "transport": "receive",
        "screen": "true",
    },
    "rossum_electro_music_mob_of_emus_guide.md": {
        "form_factor": "eurorack",
        "functions": ["fm-oscillator"],
        "behavior_tags": ["harmonic", "inharmonic", "stable", "performance-oriented", "nonlinear"],
        "use_cases": ["lead voice", "chord voice", "complex FM texture", "metallic percussion voice"],
        "memory": "full",
        "screen": "true",
    },
    "soma_lyra8_fx_guide.md": {
        "form_factor": "eurorack",
        "functions": ["fx-modulation", "distortion"],
        "behavior_tags": ["dirty", "warm", "chaotic", "nonlinear", "generative", "evolving"],
        "use_cases": ["dark atmospheric layer", "drone foundation", "chaotic texture source", "self-evolving patch element"],
    },
    "squarp_hermod_plus_guide.md": {
        "form_factor": "eurorack",
        "functions": ["sequencer", "signal-router"],
        "behavior_tags": ["stable", "performance-oriented", "reactive", "linear"],
        "use_cases": ["generative melodic sequence", "clock source for full system", "MIDI and CV integration hub"],
        "memory": "full",
        "transport": "full",
        "screen": "true",
    },
    "tiptop_audio_forbidden_planet_guide.md": {
        "form_factor": "eurorack",
        "functions": ["filter"],
        "behavior_tags": ["warm", "clean", "stable", "nonlinear", "reactive"],
        "use_cases": ["timbral movement and shaping", "filter as primary voice character", "lead voice when self-oscillating"],
    },
    "tiptop_audio_miso_guide.md": {
        "form_factor": "eurorack",
        "functions": ["vca", "attenuator", "cv-processor"],
        "behavior_tags": ["clean", "stable", "linear", "reactive"],
        "use_cases": ["CV scaling and utility", "signal distribution", "attenuation and inversion"],
    },
    "turing_machine_ecosystem_guide.md": {
        "form_factor": "eurorack",
        "functions": ["sequencer", "random-source"],
        "behavior_tags": ["stochastic", "evolving", "generative", "chaotic", "performance-oriented"],
        "use_cases": ["generative melodic sequence", "stochastic modulation", "self-evolving patch element", "probability-based variation"],
        "transport": "receive",
    },
    "vostok_instruments_ceres_guide.md": {
        "form_factor": "eurorack",
        "functions": ["vca", "mixer"],
        "behavior_tags": ["clean", "stable", "linear", "reactive"],
        "use_cases": ["audio mixing and routing", "CV-controlled mixing", "voice summing"],
    },
    "vpme_qd_qex_drum_workstation_guide.md": {
        "form_factor": "eurorack",
        "functions": ["sample-player", "sequencer"],
        "behavior_tags": ["percussive", "gated", "stable", "performance-oriented", "reactive"],
        "use_cases": ["rhythmic percussion layer", "full drum kit with samples", "sequenced drum workstation"],
        "memory": "full",
        "transport": "full",
        "screen": "true",
    },
    "vpme_qd_qex_euclidean_circles_ecosystem_guide.md": {
        "form_factor": "eurorack",
        "functions": ["euclidean-generator", "clock-divider"],
        "behavior_tags": ["stable", "percussive", "generative", "linear"],
        "use_cases": ["euclidean rhythm source", "polyrhythmic pattern generator", "rhythmic gate patterns"],
    },
    "winterbloom_castor_pollux_ii_guide.md": {
        "form_factor": "eurorack",
        "functions": ["oscillator", "fx-modulation"],
        "behavior_tags": ["warm", "stable", "harmonic", "bright", "evolving"],
        "use_cases": ["lead voice", "chord voice", "lush stereo oscillator", "bass voice"],
        "memory": "full",
        "hybrid": "true",
    },
    "xaoc_devices_belgrad_guide.md": {
        "form_factor": "eurorack",
        "functions": ["filter", "wavefolder"],
        "behavior_tags": ["warm", "harmonic", "nonlinear", "evolving", "performance-oriented"],
        "use_cases": ["timbral movement and shaping", "complex filter character", "self-evolving patch element"],
    },
    "xaoc_devices_zadar_nin_guide.md": {
        "form_factor": "eurorack",
        "functions": ["function-generator"],
        "behavior_tags": ["free-running", "gated", "evolving", "nonlinear", "generative", "performance-oriented"],
        "use_cases": ["envelope shaping", "modulation source", "generative CV source", "stochastic modulation"],
        "memory": "full",
        "screen": "true",
    },
}

# Ordered list of all v2 capability flag keys (inserted after use_cases, before hp)
# Only included in output when explicitly set in MIGRATION data above.
CAPABILITY_FLAG_KEYS = ["memory", "transport", "screen", "hybrid", "cv"]

# Fields that are lists in the output
LIST_FIELDS = {"functions", "behavior_tags", "use_cases", "secondary_roles"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def format_list(items):
    if not items:
        return "[]"
    return "[" + ", ".join(items) + "]"


def migrate_guide(path, new_fields, dry_run=False):
    content = path.read_text(encoding="utf-8")

    if not content.startswith("---"):
        return f"SKIP  {path.name}  (no frontmatter)"

    end_idx = content.find("\n---", 3)
    if end_idx == -1:
        return f"SKIP  {path.name}  (malformed frontmatter — no closing ---)"

    fm_block = content[4:end_idx]       # text between the two --- markers
    rest = content[end_idx:]             # starts with \n---

    fm_lines = fm_block.splitlines()

    # Find insertion point: after secondary_roles line
    insert_after = -1
    for i, line in enumerate(fm_lines):
        if line.startswith("secondary_roles:"):
            insert_after = i
            break

    if insert_after == -1:
        return f"WARN  {path.name}  (secondary_roles not found — skipped)"

    # Core fields: form_factor, functions, behavior_tags, use_cases
    # Strip any pre-existing occurrences of these from the rest of the frontmatter
    # (should not be present in v1, but guard against partial migrations)
    core_keys = ["form_factor", "functions", "behavior_tags", "use_cases"]
    cap_keys  = set(CAPABILITY_FLAG_KEYS)

    before = fm_lines[:insert_after + 1]   # up to and including secondary_roles
    after_raw = fm_lines[insert_after + 1:]  # hp and any pre-existing cap flags

    # Strip any pre-existing core field lines from after_raw (idempotency guard)
    all_new_keys = set(core_keys)
    after_stripped = [l for l in after_raw
                      if not any(l.startswith(k + ":") for k in all_new_keys)]

    # Separate after_stripped into: hp line(s) + pre-existing cap flag lines
    hp_and_other = []
    existing_cap_lines = {}   # key -> line string, preserving existing values
    for line in after_stripped:
        key = line.split(":")[0].strip()
        if key in cap_keys:
            existing_cap_lines[key] = line
        else:
            hp_and_other.append(line)

    # Build the new core field lines
    new_core_lines = []
    for key in core_keys:
        if key in new_fields:
            val = new_fields[key]
            if isinstance(val, list):
                new_core_lines.append(f"{key}: {format_list(val)}")
            else:
                new_core_lines.append(f"{key}: {val}")

    # Build final capability flag lines:
    # Start from existing, then override/add with migration data.
    # Output in canonical key order.
    merged_cap = dict(existing_cap_lines)  # key -> full "key: value" line
    for key in CAPABILITY_FLAG_KEYS:
        if key in new_fields:
            merged_cap[key] = f"{key}: {new_fields[key]}"

    final_cap_lines = [merged_cap[k] for k in CAPABILITY_FLAG_KEYS if k in merged_cap]

    # Reconstruct frontmatter
    updated_lines = before + new_core_lines + hp_and_other + final_cap_lines
    new_fm = "\n".join(updated_lines)
    new_content = "---\n" + new_fm + rest

    if not dry_run:
        path.write_text(new_content, encoding="utf-8")
        return f"OK    {path.name}"
    else:
        added = len(new_core_lines)
        return f"DRY   {path.name}  (+{added} core fields, {len(final_cap_lines)} cap flags)"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Migrate guides to YAML v2 schema")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing")
    parser.add_argument("--modular-dir", default="modular", help="Path to modular guide directory")
    args = parser.parse_args()

    modular_dir = Path(args.modular_dir)
    if not modular_dir.is_dir():
        print(f"ERROR: {modular_dir} is not a directory")
        return

    ok = warn = skip = 0
    for fname, fields in sorted(MIGRATION.items()):
        path = modular_dir / fname
        if not path.exists():
            print(f"MISS  {fname}  (file not found)")
            skip += 1
            continue
        result = migrate_guide(path, fields, dry_run=args.dry_run)
        print(result)
        if result.startswith("OK") or result.startswith("DRY"):
            ok += 1
        elif result.startswith("WARN"):
            warn += 1
        else:
            skip += 1

    total = ok + warn + skip
    verb = "Would update" if args.dry_run else "Updated"
    print(f"\n{verb} {ok}/{total} guides  |  {warn} warnings  |  {skip} skipped")


if __name__ == "__main__":
    main()
