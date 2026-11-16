"""Registration and publication checks; not a treatment runtime or balance test.

Run from the workspace: .venv/bin/python -B -m unittest discover -s pipeline/tests -v
"""

from pathlib import Path
import re
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[2]
DESIGN = ROOT / "Transcendence-design"
PUBLICATIONS = ROOT / "Transcendence-publications"
ALCHEMY = PUBLICATIONS / "core-books/transcendence-corebook/10-equipment-and-resources/es/05-alquimia.md"
POISONS = PUBLICATIONS / "core-books/transcendence-corebook/11-ailments/es/04-venenos.md"


class UniqueKeyLoader(yaml.SafeLoader):
    """Fail if a new registration accidentally hides an existing YAML key."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key!r} at {key_node.start_mark}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def load_yaml(path):
    return yaml.load(path.read_text(), Loader=UniqueKeyLoader)


class PoisonNeutralizerRegistrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.materials = load_yaml(DESIGN / "data/system/materials-and-fabrication.yaml")
        cls.family = cls.materials["alchemy"]["poison_neutralizers"]
        cls.catalog = cls.family["formula_catalog"]
        cls.alchemy_text = ALCHEMY.read_text()
        cls.product_text = cls.alchemy_text.split("## Neutralizadores específicos\n", 1)[1]

    def test_yaml_keys_and_catalog_ids_are_unique(self):
        for relative in ["concept-registry.yaml", "decision-registry.yaml", "knowledge-manifest.yaml"]:
            load_yaml(DESIGN / "data/knowledge" / relative)
        ids = [item["id"] for item in self.catalog]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(ids), 3)

    def test_quality_coverage_is_explicit_not_severity(self):
        compatibility = self.family["compatibility"]
        self.assertEqual(compatibility["supported_poison_qualities"], {
            "common": ["common"],
            "rare": ["common", "rare"],
            "exceptional": ["common", "rare", "exceptional"],
        })
        self.assertIn("ailment_severity", compatibility["do_not_infer_from"])
        self.assertIn("symptoms", compatibility["do_not_infer_from"])
        self.assertEqual(compatibility["unknown_poison_quality"], "requires_authored_source_definition")

    def test_only_the_named_poison_is_registered_as_compatible(self):
        self.assertEqual(set(self.family["authored_poison_references"]), {"confusion_poison"})
        for item in self.catalog:
            self.assertEqual(item["compatible_poison_formula_id"], "confusion_poison")
        source = self.family["authored_poison_references"]["confusion_poison"]
        self.assertEqual(source["verified_preparation_qualities"], ["common"])
        self.assertTrue((PUBLICATIONS / source["publication_source"]).is_file())

    def test_approved_recipe_values(self):
        expected = {
            "common": ("fluid", 2, 8, 12, "1d4", "Challenging"),
            "rare": ("gland", 3, 15, 24, "1d3", "Demanding"),
            "exceptional": ("nervous_system", 4, 24, 36, "1d2", "Extreme"),
        }
        for item in self.catalog:
            with self.subTest(quality=item["quality"]):
                self.assertEqual(item["formula_rarity"], item["quality"])
                self.assertEqual(item["creature_reagent"]["units"], 1)
                self.assertEqual((
                    item["creature_reagent"]["type"], item["botanical_units"],
                    item["minimum_botanical_index"], item["progress_hours"],
                    item["dose_yield"], item["fabrication_difficulty"],
                ), expected[item["quality"]])

    def test_recipe_time_and_yield_inherit_rarity(self):
        rarity_rules = self.materials["production_documents"]["formulas"]["rarity"]
        for item in self.catalog:
            rule = rarity_rules[item["formula_rarity"]]
            self.assertEqual(rule["build_time"], f"{item['progress_hours']} hours")
            self.assertEqual(rule["default_doses"], item["dose_yield"])

    def test_botanical_requirements_are_attainable_with_catalogued_indices(self):
        plant_catalog = self.materials["plants"]["baseline_catalog"]
        indices = [entry["alchemical_index"] for tier in plant_catalog.values() for entry in tier.values()]
        for item in self.catalog:
            self.assertGreater(item["minimum_botanical_index"], 0)
            self.assertLessEqual(item["minimum_botanical_index"], item["botanical_units"] * max(indices))

    def test_manufacturing_requires_formula_and_fixed_infrastructure(self):
        manufacturing = self.family["manufacturing"]
        self.assertTrue(manufacturing["formula_required"])
        self.assertEqual(manufacturing["required_infrastructure"], "fixed_alembic_or_furnace")
        self.assertFalse(manufacturing["field_kit_finishes_compound"])
        self.assertEqual(manufacturing["progress_interval_hours"], 1)

    def test_dose_consumption_covers_failure_but_not_invalid_attempt(self):
        dose = self.family["clinical_use"]["dose_consumption"]
        self.assertEqual(dose["administered_doses_per_attempt"], 1)
        self.assertTrue(dose["consumed_on_success"])
        self.assertTrue(dose["consumed_on_failure"])
        self.assertTrue(dose["invalid_prerequisites_do_not_automatically_consume_dose"])
        self.assertEqual(self.family["clinical_use"]["failure"], "poison_unchanged")

    def test_clinical_delivery_does_not_grant_weapon_reaction(self):
        use = self.family["clinical_use"]
        self.assertEqual(use["administration_route"], "ingestion")
        self.assertFalse(use["external_weapon_application_granted_by_product"])
        self.assertIn("El producto no concede una aplicación reactiva sobre armas.", self.product_text)

    def test_superior_quality_does_not_change_same_poison_treatment(self):
        for value in self.family["compatibility"]["higher_neutralizer_quality"].values():
            self.assertIs(value, False)
        profiles = self.family["treatment_profiles"]
        self.assertEqual(set(profiles), {"common_confusion_poison"})
        profile = profiles["common_confusion_poison"]
        self.assertEqual(profile["poison_quality"], "common")
        self.assertEqual(profile["minimum_medical_kit"], "basic")
        self.assertEqual(profile["difficulty_band"], "Challenging")
        self.assertEqual(profile["atb"], {
            "action_type": "active", "rhythm_cost": 6,
            "attrition_cost": 1, "paid_on_failure": True,
        })

    def test_stability_applies_to_finished_product_not_raw_inputs(self):
        conservation = self.family["conservation"]
        self.assertEqual(conservation["finished_product_class"], "stable")
        self.assertEqual(set(conservation["conditions"]), {
            "sealed_container", "uncontaminated", "normal_storage_conditions",
        })
        self.assertTrue(conservation["raw_inputs_keep_their_own_conservation_rules"])
        self.assertFalse(conservation["invulnerable_to_environment_or_container_damage"])

    def test_spanish_recipe_table_matches_all_numeric_fields(self):
        labels = {"common": "Común", "rare": "Rara", "exceptional": "Excepcional"}
        reagent_labels = {"fluid": "Fluido", "gland": "Glándula", "nervous_system": "Sistema nervioso"}
        difficulty_labels = {"Challenging": "Desafiante", "Demanding": "Exigente", "Extreme": "Extrema"}
        for item in self.catalog:
            expected = (
                f"| {labels[item['quality']]} | {reagent_labels[item['creature_reagent']['type']]} ×1"
                f" | {item['botanical_units']} | {item['minimum_botanical_index']}"
                f" | {item['progress_hours']} | {item['dose_yield']}"
                f" | {difficulty_labels[item['fabrication_difficulty']]} |"
            )
            self.assertIn(expected, self.product_text)
        self.assertIn("Ritmo 6 / Desgaste 1", self.product_text)
        self.assertIn("### Ejemplo de neutralización", self.product_text)

    def test_cross_references_and_knowledge_registration(self):
        poison_text = POISONS.read_text()
        match = re.search(r"\[Alquimia — Neutralizadores específicos\]\(([^)]+)\)", poison_text)
        self.assertIsNotNone(match)
        file_path, anchor = match.group(1).split("#", 1)
        self.assertEqual((POISONS.parent / file_path).resolve(), ALCHEMY.resolve())
        self.assertEqual(anchor, "neutralizadores-específicos")
        registry = load_yaml(DESIGN / "data/knowledge/concept-registry.yaml")
        concept = next(item for item in registry["concepts"] if item["id"] == "specific_poison_neutralizer")
        for path in concept["authority_paths"]:
            self.assertTrue((ROOT / path).is_file(), path)
        glossary = (PUBLICATIONS / "canon/glossary.md").read_text()
        self.assertIn("| Neutralizador específico | Specific Poison Neutralizer | No |", glossary)

    def test_registration_does_not_claim_runtime_or_english_publication(self):
        integration = self.family["integration"]
        self.assertFalse(integration["runtime_supported"])
        self.assertEqual(integration["runtime_gap_classification"], "new_subsystem")
        self.assertEqual(integration["publication_languages"]["en"], "deferred_existing_chapter_has_only_README")


if __name__ == "__main__":
    unittest.main()
