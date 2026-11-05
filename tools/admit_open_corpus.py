#!/usr/bin/env python3
"""Fail-closed admission for *locally generated* CLINOS toy data only.

Not an external EHR data importer, sanitizer, clinical validator, or de-identifier.
Rejects any input not byte-for-byte reproducible by the pinned toy generator.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

SOURCE = Path(__file__).with_name("generate_open_corpus.py")
spec = importlib.util.spec_from_file_location("clinos_toy", SOURCE)
toy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(toy)
MAX_BYTES = 8192
TRANSFORM_VERSION = "CLINOS-G0-TOY-ADMISSION-1"

class AdmissionError(ValueError):
    pass

def _no_duplicates(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise AdmissionError("duplicate JSON key; values withheld")
        out[key] = value
    return out

def inspect_bytes(payload: bytes) -> dict:
    if len(payload) > MAX_BYTES:
        raise AdmissionError("fixture exceeds local toy byte limit")
    try:
        obj = json.loads(payload.decode("utf-8"), object_pairs_hook=_no_duplicates)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise AdmissionError("invalid UTF-8 or JSON; values withheld") from exc
    if not isinstance(obj, dict) or type(obj.get("seed")) is not int:
        raise AdmissionError("unexpected toy envelope or seed type")
    try:
        expected = toy.encode(toy.build(obj["seed"]))
    except (ValueError, TypeError) as exc:
        raise AdmissionError("invalid synthetic seed") from exc
    if payload != expected:
        raise AdmissionError("fixture differs from locally reproducible toy; not admitted")
    sha = hashlib.sha256(payload).hexdigest()
    return {
        "admission": "PASS_STRUCTURAL_TOY_ONLY",
        "corpus_type": "CLINOS_NONCLINICAL_STRUCTURAL_TOY_V1",
        "fixture_sha256": sha,
        "fixture_bytes": len(payload),
        "transform_version": TRANSFORM_VERSION,
        "source_class": "CLINOS_LOCAL_GENERATOR_ONLY",
        "clinical_equivalence": "NOT_TESTED",
        "external_data_admitted": False,
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    if args.input.resolve() == args.manifest.resolve():
        parser.error("input and manifest cannot be the same file")
    try:
        if args.input.stat().st_size > MAX_BYTES:
            raise AdmissionError("fixture exceeds local toy byte limit")
        report = inspect_bytes(args.input.read_bytes())
    except (OSError, AdmissionError) as exc:
        parser.exit(2, "REJECTED: " + ("cannot read input" if isinstance(exc, OSError) else str(exc)) + "\n")
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"admission": report["admission"], "fixture_sha256": report["fixture_sha256"]}, sort_keys=True))

if __name__ == "__main__":
    main()
