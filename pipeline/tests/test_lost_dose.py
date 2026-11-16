"""Static authoring checks for #167; no runtime or empirical balance claims."""

from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[2]
PUBLICATIONS = ROOT / "Transcendence-publications"
CORE = PUBLICATIONS / "core-books/transcendence-techniques"
CARDS = PUBLICATIONS / "technique-cards/transcendence-technique-cards/cards/es/bufoni"
CARD_ID = "bufoni-la-dosis-perdida"


class CardStructure(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.ids = set()
        self.svg_refs = set()
        self.stylesheets = []
        self.pages = []
        self.article_ids = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag not in {"meta", "link", "br", "hr", "img", "input"}:
            self.stack.append(tag)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                raise AssertionError(f"Duplicate HTML id: {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "use":
            self.svg_refs.add(attrs["href"][1:])
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.stylesheets.append(attrs["href"])
        if tag == "div" and "print-page" in attrs.get("class", "").split():
            self.pages.append([])
        if tag == "article":
            self.article_ids.append(attrs["data-card-id"])
            if self.pages:
                self.pages[-1].append(attrs["data-card-id"])

    def handle_endtag(self, tag):
        if not self.stack or self.stack.pop() != tag:
            raise AssertionError(f"Unbalanced HTML end tag: {tag}")


class LostDoseRegistrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = yaml.safe_load((ROOT / "Transcendence-design/data/system/techniques.yaml").read_text())
        cls.record = next(t for t in cls.data["pilot_examples"] if t.get("id") == 167)
        cls.contract = cls.record["external_poison_neutralization"]
        cls.es = (CORE / "es/167-la-dosis-perdida.md").read_text()
        cls.en = (CORE / "en/167-the-lost-dose.md").read_text()
        cls.card = (CARDS / "la-dosis-perdida.html").read_text()
        cls.print_sheet = (CARDS / "imprimir-bufoni.html").read_text()

    def test_unique_id_and_required_authority_fields(self):
        self.assertEqual(sum(t.get("id") == 167 for t in self.data["pilot_examples"]), 1)
        for field in self.data["required_fields"]:
            self.assertIn(field, self.record)
        self.assertEqual(self.record["status"], "authored")
        self.assertEqual(self.record["name"], "La dosis perdida")
        self.assertEqual(self.record["name_en"], "The Lost Dose")

    def test_effect_matches_creator_approved_draft(self):
        work = (ROOT / "docs/work-runs/2026-10-14-bufoni-06-alquimia.md").read_text()
        draft = "Cuando se realice un ataque" + work.split("\nCuando se realice un ataque", 1)[1].split("\n\nEjemplo:", 1)[0]
        effect = self.es.split("## Efecto\n\n", 1)[1].split("\n\n## Ejemplo", 1)[0]
        self.assertEqual(effect, draft)

    def test_competency_and_species_origin_are_not_species_gate(self):
        self.assertEqual(self.record["origin"]["main"], "Alchemy")
        self.assertEqual(self.record["world_origin"]["source"], "Bufoni")
        self.assertEqual(self.record["requirements"]["support_specializations"], ["Alchemy"])
        self.assertNotIn("species", self.record["requirements"])
        self.assertEqual(self.record["requirements"]["rank"], "Novice")

    def test_roll_tie_and_range_contract(self):
        self.assertEqual(self.record["activation_roll"]["competency"], "Alchemy")
        self.assertEqual(self.contract["comparison"], "original_attacker_attack_roll")
        self.assertTrue(self.contract["strict_superiority_required"])
        self.assertTrue(self.contract["failure_includes_tie"])
        self.assertFalse(self.contract["attacker_roll_rerolled_or_modified"])
        self.assertEqual(self.contract["poisoned_point_max_distance_m"], 1)
        self.assertTrue(self.contract["physical_access_to_poisoned_point_required"])

    def test_timing_and_attack_preservation(self):
        self.assertEqual(self.record["type"], "reactive")
        self.assertTrue(self.contract["declare_before_defense_resolution"])
        self.assertTrue(self.contract["attack_continues_with_normal_defense_impact_and_other_effects"])
        self.assertFalse(self.contract["physical_damage_negated"])
        self.assertFalse(self.contract["weapon_damaged_or_disarmed"])

    def test_cost_dose_and_repeat_attempt_limits(self):
        self.assertEqual(self.record["cost"], {"rhythm_cost": 3, "attrition_cost": 1})
        self.assertEqual(self.contract["external_poison_doses_neutralized_on_success"], 1)
        self.assertEqual(self.contract["neutralizer_doses_consumed_per_attempt"], 1)
        self.assertTrue(self.contract["consume_neutralizer_on_failure"])
        self.assertTrue(self.contract["costs_paid_on_failure"])
        self.assertEqual(self.contract["attempts_per_practitioner_per_attack"], 1)

    def test_application_not_clinical_treatment_or_handling_immunity(self):
        for key in ["medical_treatment_applied", "medicine_roll_required", "medical_kit_required", "internal_poison_cured", "glands_or_internal_secretions_disabled"]:
            self.assertFalse(self.contract[key], key)
        self.assertTrue(self.contract["poison_handling_and_self_contamination_rules_preserved"])
        self.assertTrue(self.contract["product_compatibility_and_quality_rules_preserved"])
        product = yaml.safe_load((ROOT / "Transcendence-design" / self.contract["product_authority"]).read_text())["alchemy"]["poison_neutralizers"]
        self.assertFalse(product["clinical_use"]["external_weapon_application_granted_by_product"])

    def test_no_movement_projectiles_or_future_dose_protection(self):
        self.assertTrue(self.contract["third_party_attack_eligible"])
        for key in ["displacement_granted", "projectile_interception_granted", "new_poison_doses_automatically_neutralized", "identification_automatically_granted"]:
            self.assertFalse(self.contract[key], key)
        self.assertEqual(self.record["duration"], {"model": "instant"})
        self.assertIsNone(self.record["impact"])
        self.assertIsNone(self.record["saving_roll"])

    def test_localized_stat_fields_and_no_natural_weapon_keywords(self):
        self.assertIn("| 1m | 1 Superficie u Objeto | Instantáneo | T.E. (Alquimia) |", self.es)
        self.assertIn("| 1m | 1 Surface or Object | Instantaneous | S.R. (Alchemy) |", self.en)
        for core in [self.es, self.en]:
            self.assertIn("| — | — | 3 | 1 |", core)
            fm = yaml.safe_load(core.split("---", 2)[1])
            self.assertEqual(fm["status"], "draft")
            self.assertIs(fm["canonical"], False)
            for ref in fm["related"]:
                self.assertTrue((PUBLICATIONS / ref).is_file(), ref)
            for ref in fm["authority_refs"]:
                self.assertTrue((ROOT / ref).is_file(), ref)
        for surface in [self.es, self.card]:
            self.assertNotIn("Hereda Efectos", surface)
            self.assertNotIn("No Hereda Efectos", surface)

    def test_html_structure_icons_and_stylesheets(self):
        for name, html in [("la-dosis-perdida.html", self.card), ("imprimir-bufoni.html", self.print_sheet)]:
            parser = CardStructure()
            parser.feed(html)
            self.assertEqual(parser.stack, [], name)
            self.assertLessEqual(parser.svg_refs, parser.ids)
            self.assertEqual(len(parser.article_ids), len(set(parser.article_ids)))
            for css in parser.stylesheets:
                self.assertTrue((CARDS / css).is_file(), css)

    def test_card_and_print_copy_identical_with_six_plus_two_pagination(self):
        def article(html):
            return next(a for a in re.findall(r"<article\b[^>]*>.*?</article>", html, re.S) if CARD_ID in a)
        self.assertEqual(article(self.card), article(self.print_sheet))
        parser = CardStructure()
        parser.feed(self.print_sheet)
        self.assertEqual([len(page) for page in parser.pages], [6, 2])
        self.assertEqual(parser.pages[1], [CARD_ID, "bufoni-el-aliento-reservado"])

    def test_card_keeps_exact_primary_stats(self):
        stats = dict(re.findall(r"<span>([^<]+)</span><strong>([^<]+)</strong>", self.card))
        self.assertEqual(stats, {
            "Rango": "1m", "Área": "1 Superficie u Objeto", "Duración": "Instantáneo",
            "Tirada": "T.E. (Alquimia)", "Salvación": "—", "Impacto": "—", "Ritmo": "3", "Desgaste": "1",
        })
        for phrase in ["tipo conocido", "antes de la defensa", "otra criatura", "Si no la superas", "Kit de Medicina", "autocontaminación", "aunque falles", "proyectiles", "Una dosis nueva"]:
            self.assertIn(phrase, self.card)


if __name__ == "__main__":
    unittest.main()
