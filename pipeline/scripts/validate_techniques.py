#!/usr/bin/env python3
import yaml
import sys
import os
import re

# Adjust paths relative to workspace root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TECHNIQUES_PATH = os.path.join(BASE_DIR, 'Transcendence-design', 'data', 'system', 'techniques.yaml')
AILMENTS_PATH = os.path.join(BASE_DIR, 'Transcendence-design', 'data', 'system', 'ailments.yaml')
SIM_TECHNIQUES_DIR = os.path.join(BASE_DIR, 'Transcendence-design', 'sim', 'data', 'techniques')

# Mirror of SUPPORTED_EFFECT_IDS in sim/engine/effects.py — keep in sync when adding new effect handlers.
SUPPORTED_EFFECT_IDS = {
    # Handled by apply_effect_definition in engine/effects.py
    "grant_hidden_state",
    "grant_hidden_state_limited",
    "apply_ailment",
    "apply_procedural_state",
    "mark_immediate_route_readable",
    "blur_declared_sensory_channel",
    "deny_clean_separation_if_check_succeeds",
    # Handled at exchange/activation level in engine/activations.py
    "weapon_exchange_primary",
    "indirect_surface_ranged_attack",
    "false_line_combined_resolution",
    "utility_check_primary",
    "same_exchange_ignore_block_rank_bonus",
    "reposition_after_hit_half_move",
    "reposition_after_hit_distance",
    "advance_before_exchange_distance",
    "reduce_target_movement_rank_bonus",
}

def load_yaml(filepath):
    try:
        with open(filepath, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        sys.exit(1)

def main():
    print(f"Loading data from {TECHNIQUES_PATH}...")
    tech_data = load_yaml(TECHNIQUES_PATH)
    ailments_data = load_yaml(AILMENTS_PATH)

    valid_ailments = {entry.get('name', '').lower() for entry in ailments_data.get('entries', [])}
    for entry in ailments_data.get('entries', []):
        if 'name_en' in entry:
            valid_ailments.add(entry['name_en'].lower())
            
    # Valid wound/damage terms from mechanics
    valid_wounds = {'lacerado', 'perforado', 'contuso', 'crítico', 'romper parte', 'amputado', 'fatiga', 'fatigado'}

    techniques = tech_data.get('pilot_examples', [])
    if not techniques:
        print("No techniques found under 'pilot_examples'.")
        sys.exit(1)

    errors = 0
    warnings = 0

    tier_map = {
        'Novice': 1,
        'Adept': 2,
        'Expert': 3,
        'Master': 4
    }

    for idx, tech in enumerate(techniques):
        name = tech.get('name', f"Unknown at index {idx}")
        
        # 1. Basic Schema Validation
        required_fields = ['name', 'status', 'purpose', 'origin']
        for field in required_fields:
            if field not in tech:
                print(f"[ERROR] Technique '{name}' is missing required field: '{field}'")
                errors += 1

        # 2. Cost Validation
        cost = tech.get('cost')
        if cost:
            rhythm = cost.get('rhythm_cost')
            attrition = cost.get('attrition_cost')
            
            if rhythm is not None and not (0 <= rhythm <= 9):
                print(f"[WARNING] '{name}' has Rhythm {rhythm} outside normal band (0-9).")
                warnings += 1
                
            if attrition is not None and attrition >= 4:
                print(f"[WARNING] '{name}' has Attrition {attrition}. This is an exceptional overextension.")
                warnings += 1

        # 3. Tier Validation
        reqs = tech.get('requirements', {})
        rank = reqs.get('rank')
        tier = reqs.get('technique_tier')
        
        if rank and tier:
            expected_tier = tier_map.get(rank)
            if expected_tier and tier != expected_tier:
                print(f"[ERROR] '{name}' has Rank '{rank}' but Tier is {tier} (expected {expected_tier}).")
                errors += 1

        # 4. Ailments / Wounds cross-reference
        # We check the "effect" field for capitalized terms which usually denote Ailments or Statuses
        effect_text = tech.get('effect', '')
        if effect_text:
            # Find capitalized words that might be ailments (very naive heuristic)
            # A more robust check would look at specific structured fields, but we do text search here.
            pass

    # Validate sim YAML effect IDs against engine support
    sim_techniques_checked = 0
    if os.path.isdir(SIM_TECHNIQUES_DIR):
        for filename in sorted(os.listdir(SIM_TECHNIQUES_DIR)):
            if not filename.endswith('.yaml'):
                continue
            filepath = os.path.join(SIM_TECHNIQUES_DIR, filename)
            try:
                with open(filepath) as f:
                    sim_data = yaml.safe_load(f)
            except Exception as e:
                print(f"[ERROR] Could not load sim techniques file '{filename}': {e}")
                errors += 1
                continue
            if isinstance(sim_data, dict):
                sim_data = sim_data.get('techniques', [])
            if not isinstance(sim_data, list):
                continue
            for entry in sim_data:
                tech_id = entry.get('id', '<unknown>')
                sim_techniques_checked += 1
                for effect in entry.get('effects', []):
                    eid = effect.get('id')
                    if eid and eid not in SUPPORTED_EFFECT_IDS:
                        print(
                            f"[ERROR] sim/{filename} technique '{tech_id}' uses unsupported effect_id '{eid}'. "
                            "Add a handler in engine/effects.py or engine/activations.py, "
                            "then add it to SUPPORTED_EFFECT_IDS in both effects.py and validate_techniques.py."
                        )
                        errors += 1

    print(f"\nValidation completed: {len(techniques)} canonical techniques, {sim_techniques_checked} sim techniques checked.")
    if errors > 0:
        print(f"FAILED: {errors} errors, {warnings} warnings.")
        sys.exit(1)
    else:
        print(f"SUCCESS: 0 errors, {warnings} warnings.")

if __name__ == '__main__':
    main()
