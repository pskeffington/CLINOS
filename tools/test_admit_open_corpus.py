"""Security-negative tests for the nonclinical, local-only admission gate."""
import importlib.util
import json
from pathlib import Path
import unittest

DIR = Path(__file__).parent
def load(name):
    spec = importlib.util.spec_from_file_location(name, DIR / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
toy = load("generate_open_corpus")
gate = load("admit_open_corpus")

class AdmissionTests(unittest.TestCase):
    def test_accept_exact_local_bytes(self):
        sample = toy.encode(toy.build(42))
        result = gate.inspect_bytes(sample)
        self.assertEqual(result["admission"], "PASS_STRUCTURAL_TOY_ONLY")
        self.assertFalse(result["external_data_admitted"])
        self.assertEqual(result["clinical_equivalence"], "NOT_TESTED")

    def test_reject_modified_relationship(self):
        value = toy.build(42)
        value["events"][1]["person_ref"] = "SYN-P-modified"
        with self.assertRaises(gate.AdmissionError):
            gate.inspect_bytes(toy.encode(value))

    def test_reject_identifying_field(self):
        value = toy.build(42)
        value["events"][0]["name"] = "a patient"
        payload = (json.dumps(value) + "\n").encode("utf8")
        with self.assertRaises(gate.AdmissionError):
            gate.inspect_bytes(payload)

    def test_reject_unapproved_external_like_envelope(self):
        with self.assertRaises(gate.AdmissionError):
            gate.inspect_bytes(b'{"resourceType":"Patient","id":"123"}')

    def test_reject_duplicate_json_keys(self):
        with self.assertRaises(gate.AdmissionError):
            gate.inspect_bytes(b'{"seed":42,"seed":43}')

    def test_reject_invalid_unicode(self):
        with self.assertRaises(gate.AdmissionError):
            gate.inspect_bytes(b"\xff\xfe")

    def test_reject_oversize(self):
        with self.assertRaises(gate.AdmissionError):
            gate.inspect_bytes(b"x" * (gate.MAX_BYTES + 1))

    def test_reject_boolean_seed(self):
        sample = toy.build(42)
        sample["seed"] = True
        with self.assertRaises(gate.AdmissionError):
            gate.inspect_bytes(json.dumps(sample).encode())

    def test_reject_noncanonical_whitespace(self):
        sample = toy.encode(toy.build(42)).rstrip()
        with self.assertRaises(gate.AdmissionError):
            gate.inspect_bytes(sample)

    def test_deterministic_manifest(self):
        sample = toy.encode(toy.build(2026))
        self.assertEqual(gate.inspect_bytes(sample), gate.inspect_bytes(sample))

if __name__ == "__main__":
    unittest.main()
