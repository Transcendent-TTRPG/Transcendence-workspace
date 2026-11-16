"""Static registration checks for #168; these do not simulate exposure or balance."""

from html import unescape
from pathlib import Path
import re
import unittest

import yaml

from test_lost_dose import CardStructure


ROOT = Path(__file__).resolve().parents[2]
PUB = ROOT / "Transcendence-publications"
CORE = PUB / "core-books/transcendence-techniques"
CARDS = PUB / "technique-cards/transcendence-technique-cards/cards/es/bufoni"
CARD_ID = "bufoni-el-aliento-reservado"


class ReservedBreathRegistrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = yaml.safe_load((ROOT / "Transcendence-design/data/system/techniques.yaml").read_text())
        cls.record = next(t for t in cls.data["pilot_examples"] if t.get("id") == 168)
        cls.contract = cls.record["inhalation_prevention"]
        cls.es = (CORE / "es/168-el-aliento-reservado.md").read_text()
        cls.en = (CORE / "en/168-the-reserved-breath.md").read_text()
        cls.card = (CARDS / "el-aliento-reservado.html").read_text()
        cls.sheet = (CARDS / "imprimir-bufoni.html").read_text()

    def test_unique_id_and_required_fields(self):
        self.assertEqual(sum(t.get("id") == 168 for t in self.data["pilot_examples"]), 1)
        for field in self.data["required_fields"]:
            self.assertIn(field, self.record)
        self.assertEqual(self.record["name"], "El aliento reservado")
        self.assertEqual(self.record["name_en"], "The Reserved Breath")
        self.assertEqual(self.record["status"], "authored")

    def test_two_novice_roots_without_species_gate(self):
        self.assertEqual(self.record["origin"], {"main": "Swimming", "secondary": ["Poison Resistance"]})
        self.assertEqual(self.record["requirements"]["rank"], "Novice")
        self.assertEqual(self.record["requirements"]["support_specializations"], ["Swimming"])
        self.assertEqual(self.record["requirements"]["resistances"], [{"competency": "Poison Resistance", "minimum_rank": "Novice"}])
        self.assertEqual(self.record["world_origin"]["source"], "Bufoni")
        self.assertNotIn("species", self.record["requirements"])

    def test_contextual_swimming_activation_not_poison_resistance(self):
        roll = self.record["activation_roll"]
        self.assertEqual(roll["competency"], "Swimming")
        self.assertEqual(roll["difficulty_source"], "narrator_declared_before_roll")
        for key in ["poison_resistance_added_to_roll", "original_poison_resistance_threshold_automatically_reused", "creature_nature_difficulty_applied"]:
            self.assertFalse(roll[key], key)
        self.assertFalse(self.contract["poison_resistance_progress_granted_by_activation_roll"])

    def test_before_entry_and_before_resistance_not_retroactive(self):
        self.assertTrue(self.contract["declare_before_inhalation"])
        self.assertTrue(self.contract["declare_before_poison_resistance_roll"])
        self.assertTrue(self.contract["difficulty_declared_before_roll"])

    def test_perceived_threat_without_free_detection_or_identification(self):
        self.assertTrue(self.contract["perceived_threat_required"])
        self.assertFalse(self.contract["compound_identification_required"])
        self.assertFalse(self.contract["detection_or_identification_granted"])

    def test_one_inhaled_application_and_normal_failure_resolution(self):
        self.assertTrue(self.contract["prevents_selected_inhaled_application_on_success"])
        self.assertTrue(self.contract["normal_exposure_and_resistance_on_failure"])
        self.assertFalse(self.contract["automatic_poisoning_on_failure"])
        self.assertEqual(self.contract["attempts_per_practitioner_per_application"], 1)

    def test_not_passive_and_cost_paid_even_on_failure(self):
        self.assertEqual(self.record["type"], "reactive")
        self.assertEqual(self.record["category"], "utility")
        self.assertEqual(self.record["cost"], {"rhythm_cost": 0, "attrition_cost": 1})
        self.assertTrue(self.contract["costs_paid_on_failure"])
        self.assertEqual(self.record["duration"], {"model": "instant"})

    def test_no_continuous_exposure_slicing_or_future_protection(self):
        self.assertTrue(self.contract["discrete_imminent_application_required"])
        for key in ["continuous_exposure_eligible", "continuous_exposure_split_into_reactive_applications", "later_applications_covered"]:
            self.assertFalse(self.contract[key], key)

    def test_no_other_routes_treatment_oxygen_or_swimming_upgrade(self):
        for key in ["other_entry_routes_prevented", "internal_poison_cured", "suffocation_protection_granted", "oxygen_or_extraordinary_air_reserve_granted", "other_creatures_protected", "displacement_granted", "literal_swimming_improved"]:
            self.assertFalse(self.contract[key], key)
        self.assertIsNone(self.record["saving_roll"])
        self.assertIsNone(self.record["impact"])

    def test_approved_effect_preserved_in_core_and_card(self):
        work = (ROOT / "docs/work-runs/2026-10-16-bufoni-07-nadar.md").read_text()
        approved = work.split("## Approved ES effect\n\n", 1)[1].split("\n\n## Integration", 1)[0]
        effect = self.es.split("## Efecto\n\n", 1)[1].split("\n\n## Ejemplo", 1)[0]
        card_effect = re.search(r'<section class="effect">(.*?)</section>', self.card, re.S).group(1)
        paragraphs = re.findall(r"<p>(.*?)</p>", card_effect, re.S)
        self.assertEqual(effect, approved)
        self.assertEqual("\n\n".join(unescape(p) for p in paragraphs), approved)

    def test_localized_fields_valid_refs_and_draft_status(self):
        self.assertIn("| Personal | Tú | Instantáneo | T.E. (Nadar) |", self.es)
        self.assertIn("| Personal | You | Instantaneous | S.R. (Swimming) |", self.en)
        for content in [self.es, self.en]:
            self.assertIn("| — | — | 0 | 1 |", content)
            fm = yaml.safe_load(content.split("---", 2)[1])
            self.assertEqual(fm["status"], "draft")
            self.assertIs(fm["canonical"], False)
            for ref in fm["related"]:
                self.assertTrue((PUB / ref).is_file(), ref)
            for ref in fm["authority_refs"]:
                self.assertTrue((ROOT / ref).is_file(), ref)
        for surface in [self.es, self.card]:
            self.assertNotIn("Hereda Efectos", surface)
            self.assertNotIn("No Hereda Efectos", surface)

    def test_bilingual_effect_has_same_restrictions(self):
        for phrase in ["before inhaling", "before resolving its R.R.", "must perceive the threat", "before the roll", "On failure", "once against each application", "even if you fail", "other entry routes", "active poisons", "Suffocation", "continuous exposure", "later applications"]:
            self.assertIn(phrase, self.en)
        self.assertIn("Poison Resistance at Novice rank or higher", self.en)

    def test_card_stats_and_html_integrity(self):
        stats = dict(re.findall(r"<span>([^<]+)</span><strong>([^<]+)</strong>", self.card))
        self.assertEqual(stats, {"Rango": "Personal", "Área": "Tú", "Duración": "Instantáneo", "Tirada": "T.E. (Nadar)", "Salvación": "—", "Impacto": "—", "Ritmo": "0", "Desgaste": "1"})
        for content in [self.card, self.sheet]:
            parser = CardStructure()
            parser.feed(content)
            self.assertEqual(parser.stack, [])
            self.assertLessEqual(parser.svg_refs, parser.ids)
            self.assertEqual(len(parser.article_ids), len(set(parser.article_ids)))
            for stylesheet in parser.stylesheets:
                self.assertTrue((CARDS / stylesheet).is_file())

    def test_print_matches_source_and_retains_modern_card_sources(self):
        parser = CardStructure()
        parser.feed(self.sheet)
        self.assertEqual([len(p) for p in parser.pages], [6, 2])
        self.assertEqual(parser.pages[1], ["bufoni-la-dosis-perdida", CARD_ID])
        def articles(content):
            return re.findall(r"<article\b[^>]*>.*?</article>", content, re.S)
        self.assertIn(articles(self.card)[0], articles(self.sheet))
        for source in CARDS.glob("*.html"):
            if source.name.startswith("imprimir-"):
                continue
            self.assertEqual(len(articles(source.read_text())), 1)
            if source.name == "golpe-sin-eco.html":
                # Legacy print wording was already compressed differently.
                # Preserve that inherited article; do not normalize it in #168.
                self.assertIn("bufoni-golpe-sin-eco", parser.article_ids)
                continue
            self.assertIn(articles(source.read_text())[0], articles(self.sheet), source.name)

    def test_registered_name_catalog_and_explicit_runtime_gap(self):
        glossary = (PUB / "canon/glossary.md").read_text()
        self.assertIn("| El aliento reservado | The Reserved Breath |", glossary)
        catalog = (ROOT / "Transcendence-design/docs/system/technique-surface-catalog.md").read_text()
        row = next(line for line in catalog.splitlines() if line.startswith("| Nadar |"))
        self.assertIn("| 2 |", row)
        self.assertIn("Tomar la Corriente (#38)", row)
        self.assertIn("El aliento reservado (#168", row)
        reference = (ROOT / "Transcendence-design/docs/system/technique-el-aliento-reservado.md").read_text()
        self.assertIn("**new_subsystem**", reference)
        self.assertIn("Saved minimum cost question", reference)
        self.assertIn("not an executed experiment", reference)


if __name__ == "__main__":
    unittest.main()
