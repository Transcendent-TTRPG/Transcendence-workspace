"""Cross-surface checks for #107; not a gameplay or balance simulator."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[2]
PUBLICATIONS = ROOT / "Transcendence-publications"
CORE = PUBLICATIONS / "core-books/transcendence-techniques/es/107-adaptabilidad.md"
CARDS = PUBLICATIONS / "technique-cards/transcendence-technique-cards/cards/es/panin"


class CardText(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.text = []
        self.feed(source)

    def handle_data(self, data):
        self.text.extend(data.split())


class AdaptabilitySyncTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        source = ROOT / "Transcendence-design/data/system/techniques.yaml"
        cls.rule = next(t for t in yaml.safe_load(source.read_text())["pilot_examples"]
                        if t.get("id") == 107)

    def test_capacity_and_cost_match_authored_surfaces(self):
        core = CORE.read_text()
        rule = self.rule
        self.assertEqual(rule["cost"]["rhythm_cost"], 3)
        self.assertEqual(rule["cost"]["attrition_cost"], 1)
        self.assertIn("| — | — | 3 | 1 |", core)
        for row in rule["adaptation_model"]["simultaneous_capacity"]:
            band = (f'{row["minimum_nr"]}–{row["maximum_nr"]}'
                    if "maximum_nr" in row else f'{row["minimum_nr"]}+')
            self.assertIn(f'| {band} | {row["pairs"]} |', core)
        self.assertEqual(rule["adaptation_model"]["pairs_changed_per_use"], 1)

    def test_source_card_and_print_sheet_are_identical(self):
        article = re.compile(r'<article\b.*?</article>', re.S)
        source = article.findall((CARDS / "adaptabilidad.html").read_text())
        printed = article.findall((CARDS / "imprimir-panin.html").read_text())
        self.assertEqual(len(source), 1)
        self.assertEqual(source, printed)
        words = " ".join(CardText(source[0]).text)
        for preserved in ("origen entrenado", "asociación espontánea", "sin conocer ni nombrar",
                          "nivel + rango propios de destino o rango actual de origen",
                          "descansar no la cancela", "no duplica progreso en origen",
                          "conservas lo aprendido al sustituir"):
            self.assertIn(preserved, words)
        for obsolete in ("Abandona temporalmente", "Cede hasta", "Especializaciones Sustituibles"):
            self.assertNotIn(obsolete, words)

    def test_example_and_local_links_resolve(self):
        for path in (CORE, CORE.parent / "ejemplos/adaptabilidad.md",
                     PUBLICATIONS / "core-books/transcendence-corebook/06-species/es/10-panin.md"):
            text = path.read_text()
            metadata = yaml.safe_load(text.split("---", 2)[1])
            self.assertEqual(metadata["status"], "draft")
            self.assertIs(metadata["canonical"], False)
            for link in re.findall(r'\]\(([^)]+)\)', text):
                if "://" not in link and not link.startswith("#"):
                    self.assertTrue((path.parent / link.split("#")[0]).exists(), (path, link))

    def test_spontaneous_fiction_retains_active_mechanics_and_information_limits(self):
        model = self.rule["adaptation_model"]
        self.assertEqual(self.rule["type"], "active")
        self.assertFalse(model["conscious_named_activation_required_in_fiction"])
        self.assertFalse(model["automatic_bonus_to_every_roll"])
        self.assertFalse(model["unknown_knowledge_granted"])
        self.assertFalse(model["selection_grants_progress"])
        roster = yaml.safe_load((ROOT / "Transcendence-narrative-engine/rosters/"
                                "contenedores-vacios/panin-01.yaml").read_text())
        legacy = next(x for x in roster["species_profile"]["legacies"] if x["id"] == "adaptability")
        self.assertEqual(legacy["access_at_awakening"], "available_spontaneous_association")
        self.assertTrue(all(t["access_at_awakening"] == "blocked"
                            for t in roster["combat_profile"]["learned_techniques"]))
        self.assertTrue(all(not entries for entries in roster["continuity"].values()))


if __name__ == "__main__":
    unittest.main()
