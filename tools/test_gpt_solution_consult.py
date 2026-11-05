"""Offline tests for GPT solution consultation. No provider calls."""
import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).with_name("gpt_solution_consult.py")
spec = importlib.util.spec_from_file_location("clinos_consult", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

PAYLOAD = {
    "task_id": "CLINOS-004",
    "problem": "No CI runner jobs were allocated.",
    "observed_behavior": "Provider reports startup_failure.",
    "attempts": ["Reviewed CI metadata"],
    "constraints": ["Do not relax required checks"],
    "acceptance_criteria": ["Obtain exact-head hosted run"],
}


class FakeResponse:
    def __init__(self, body):
        self.body = body

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def read(self, size):
        return self.body[:size]


class ConsultTests(unittest.TestCase):
    def test_allowlisted_payload(self):
        self.assertEqual(module.validate_payload(PAYLOAD), PAYLOAD)

    def test_unexpected_field_fails_closed(self):
        with self.assertRaises(module.ConsultationError):
            module.validate_payload({**PAYLOAD, "raw_log": "dump"})

    def test_identifier_format(self):
        with self.assertRaises(module.ConsultationError):
            module.validate_payload({**PAYLOAD, "task_id": "OTHER-004"})

    def test_sensitive_input_fails(self):
        with self.assertRaises(module.ConsultationError):
            module.validate_payload({**PAYLOAD, "problem": "patient_name=Alex"})

    def test_email_fails(self):
        with self.assertRaises(module.ConsultationError):
            module.validate_payload({**PAYLOAD, "problem": "mail me at test@example.com"})

    def test_large_input_fails(self):
        with self.assertRaises(module.ConsultationError):
            module.validate_payload({**PAYLOAD, "problem": "x" * 1300})

    def test_preview_does_not_contact_network(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "consult.json"
            path.write_text(json.dumps(PAYLOAD), encoding="utf-8")
            buf = io.StringIO()
            with patch.object(module.urllib.request, "urlopen", side_effect=AssertionError("network")):
                with redirect_stdout(buf):
                    code = module.main(["--input", str(path)])
            self.assertEqual(code, 0)
            report = json.loads(buf.getvalue())
            self.assertEqual(report["status"], "PREVIEW_ONLY")
            self.assertFalse(report["external_transmission"])

    def test_requires_model_for_request(self):
        with self.assertRaises(module.ConsultationError):
            module.build_request(PAYLOAD, "")

    def test_no_provider_persistence(self):
        body = module.build_request(PAYLOAD, "approved-model")
        self.assertIs(body["store"], False)
        self.assertIn("CLINOS-004", body["input"])

    def test_send_needs_explicit_approval(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "consult.json"
            path.write_text(json.dumps(PAYLOAD), encoding="utf-8")
            self.assertEqual(module.main(["--input", str(path), "--send"]), 2)

    def test_valid_response_is_advisory(self):
        proposal = {
            "root_cause_hypothesis": "Runner availability unclear",
            "approaches": [{
                "name": "Review settings", "mechanics": "Inspect metadata",
                "prerequisites": "Read access", "risks": "Unknown",
                "reversibility": "Read only", "verification": "Confirm jobs allocated"
            }],
            "preferred_approach": "Review settings",
            "uncertainties": ["Exact provider cause"],
            "human_escalation": "Request admin inspection",
            "no_safe_option": False,
        }
        mock_output = {"status": "completed", "output": [
            {"content": [{"type": "output_text", "text": json.dumps(proposal)}]}
        ]}
        transport = lambda request, timeout: FakeResponse(json.dumps(mock_output).encode())
        result = module.query(module.build_request(PAYLOAD, "approved-model"), "test-key", transport)
        self.assertEqual(result["status"], "PROPOSED_UNVERIFIED")

    def test_invalid_provider_response_fails(self):
        transport = lambda request, timeout: FakeResponse(b'{"status":"incomplete","output":[]}')
        with self.assertRaises(module.ConsultationError):
            module.query(module.build_request(PAYLOAD, "approved-model"), "test-key", transport)


if __name__ == "__main__":
    unittest.main()
