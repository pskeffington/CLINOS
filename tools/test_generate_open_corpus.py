"""Offline tests for the CLINOS structural toy corpus. No EHR data."""
import importlib.util
import json
import pathlib
import unittest

SOURCE = pathlib.Path(__file__).with_name("generate_open_corpus.py")
spec = importlib.util.spec_from_file_location("generate_open_corpus", SOURCE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class StructuralToyTests(unittest.TestCase):
    def test_reproducible(self):
        self.assertEqual(mod.encode(mod.build(42)), mod.encode(mod.build(42)))

    def test_seed_distinguishes_local_ids(self):
        self.assertNotEqual(mod.encode(mod.build(1)), mod.encode(mod.build(2)))

    def test_no_direct_identifiers(self):
        content = mod.encode(mod.build(42))
        data = json.loads(content)
        self.assertTrue(data["synthetic"])
        self.assertEqual(data["events"][1]["person_ref"], data["events"][0]["id"])
        self.assertTrue(all(event["id"].startswith("SYN-") for event in data["events"]))

    def test_nested_identifier_rejection(self):
        for key in ("name", "birthDate", "address", "identifier", "text"):
            with self.subTest(key=key), self.assertRaises(ValueError):
                mod.encode({"safe": [{"nested": {key: "forbidden"}}]})

    def test_no_external_import_semantics(self):
        self.assertIn("not FHIR", mod.build(12)["limitations"])
        self.assertEqual(mod.build(12)["corpus_type"], "CLINOS_NONCLINICAL_STRUCTURAL_TOY_V1")

    def test_seed_range(self):
        for seed in (-1, 2**32):
            with self.assertRaises(ValueError):
                mod.build(seed)

if __name__ == "__main__":
    unittest.main()
