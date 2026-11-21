"""Offline tests for scripts/build_readmes.py. Run: python -m unittest discover tests"""
import datetime as dt
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("build", ROOT / "scripts" / "build_readmes.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

REG = json.loads((ROOT / "data" / "products.json").read_text())
TODAY = dt.date(2026, 11, 21)


def stats(created_overrides=None, downloads=None):
    repos = {}
    for p in REG["products"]:
        for repo in [p["repo"], *p.get("includes", [])]:
            repos[repo] = {"stars": 1, "created": "2026-01-01", "pushed": "2026-11-01", "release": "v1.0.0"}
    for repo, created in (created_overrides or {}).items():
        repos[repo]["created"] = created
    return {"repos": repos, "org_stars": 497, "built": TODAY.isoformat(),
            "downloads": downloads if downloads is not None else {"npm": 68379, "pypi": 133201}}


class Counts(unittest.TestCase):
    def test_product_count_includes_bundled_products(self):
        # 16 rows, brief2mp4 row also counts brief2motion
        self.assertEqual(len(REG["products"]), 16)
        self.assertEqual(build.product_count(REG), 17)

    def test_ten_papers_each_mapped_to_a_registry_product(self):
        slugs = {p["slug"] for p in REG["products"]}
        self.assertEqual(len(REG["papers"]), 10)
        self.assertTrue(all(x["product"] in slugs for x in REG["papers"]))

    def test_compact_never_rounds_up(self):
        self.assertEqual(build._compact(201580), "201k")
        self.assertEqual(build._compact(9999), "9.9k")
        self.assertEqual(build._compact(999), "999")


class Tiers(unittest.TestCase):
    def test_recent_non_flagship_goes_to_new_and_ages_out(self):
        s = stats({"qualixar/modstage": "2026-11-01"})
        _, new, core = build.split_tiers(REG, s, TODAY)
        self.assertIn("modstage", [p["slug"] for p in new])
        later = TODAY + dt.timedelta(days=60)
        _, new_later, core_later = build.split_tiers(REG, s, later)
        self.assertNotIn("modstage", [p["slug"] for p in new_later])
        self.assertIn("modstage", [p["slug"] for p in core_later])

    def test_flagship_never_moves_to_new(self):
        s = stats({"qualixar/superlocalmemory": "2026-11-20"})
        flagship, new, _ = build.split_tiers(REG, s, TODAY)
        self.assertIn("superlocalmemory", [p["slug"] for p in flagship])
        self.assertNotIn("superlocalmemory", [p["slug"] for p in new])


class Render(unittest.TestCase):
    def test_org_readme_has_live_badges_hero_and_counts(self):
        out = build.render_org(REG, stats(), TODAY)
        self.assertIn("**17** open-source products", out)
        self.assertIn("**10** arXiv preprints", out)
        self.assertIn("**201k+ downloads**", out)
        self.assertIn("img.shields.io/npm/dt/superlocalmemory", out)
        self.assertIn("img.shields.io/pepy/dt/superlocalmemory", out)
        self.assertEqual(out.count("img.shields.io/github/stars/qualixar/"), 1 + 16)
        self.assertNotIn("Choose a starting point", out)

    def test_missing_downloads_drop_the_number_not_show_zero(self):
        out = build.render_org(REG, stats(downloads={}), TODAY)
        self.assertNotIn("0+ downloads", out)
        self.assertNotIn("downloads** across", out)

    def test_personal_readme_states_confirmed_credentials(self):
        out = build.render_personal(REG, stats(), TODAY)
        self.assertIn("16 years in IT", out)
        self.assertIn("5× Global Technology Innovation Award winner (2021–2025)", out)
        self.assertIn("All 17 products", out)

    def test_no_release_means_no_release_badge(self):
        s = stats()
        s["repos"]["qualixar/qualixar-os"]["release"] = None
        row = build._row(REG, s, next(p for p in REG["products"] if p["slug"] == "qualixar-os"))
        self.assertNotIn("v/release", row)


class HeroSvg(unittest.TestCase):
    def test_counts_in_hero_image_follow_registry(self):
        with tempfile.TemporaryDirectory() as d:
            svg = Path(d) / "hero.svg"
            svg.write_text("<text>10 CORE PRODUCTS   •   10 PUBLIC ARXIV PREPRINTS</text>")
            self.assertTrue(build.patch_hero_svg(REG, svg))
            self.assertIn(">17 CORE PRODUCTS   •   10 PUBLIC ARXIV PREPRINTS<", svg.read_text())
            self.assertFalse(build.patch_hero_svg(REG, svg))  # idempotent


if __name__ == "__main__":
    unittest.main()
