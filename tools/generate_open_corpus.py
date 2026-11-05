#!/usr/bin/env python3
"""Offline deterministic, nonclinical CLINOS structural corpus generator.

No patient data is read or network calls made. Synthetic linkage tokens are local.
This is not FHIR validation or clinical ground truth.
"""
import argparse
import hashlib
import json
from pathlib import Path

PROHIBITED_KEYS = frozenset({
    "name", "given", "family", "birthDate", "deceasedDateTime",
    "address", "postalCode", "telecom", "email", "phone",
    "identifier", "ssn", "mrn", "photo", "text", "note",
    "narrative", "latitude", "longitude", "ipAddress",
})

def build(seed: int) -> dict:
    if not 0 <= seed <= 2**32 - 1:
        raise ValueError("seed outside uint32 range")
    prefix = hashlib.sha256(f"CLINOS-TOY-V1:{seed}".encode("ascii")).hexdigest()[:12]
    patient = "SYN-P-" + prefix
    encounter = "SYN-E-" + prefix
    return {
        "corpus_type": "CLINOS_NONCLINICAL_STRUCTURAL_TOY_V1",
        "synthetic": True,
        "seed": seed,
        "events": [
            {"kind": "person-token", "id": patient, "event_offset": 0},
            {"kind": "encounter-token", "id": encounter, "person_ref": patient, "event_offset": 1},
        ],
        "limitations": ["not FHIR", "not clinical", "not real patients", "no terminology"],
    }

def scan(value, path="$"):
    """Fail closed for prohibited key names anywhere in the generated object."""
    if isinstance(value, dict):
        for k, v in value.items():
            if k in PROHIBITED_KEYS or k.lower() in {x.lower() for x in PROHIBITED_KEYS}:
                raise ValueError(f"prohibited field at {path}; contents withheld")
            scan(v, path + "." + k)
    elif isinstance(value, list):
        for v in value:
            scan(v, path + "[]")

def encode(value: dict) -> bytes:
    scan(value)
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("utf-8")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20261104)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = encode(build(args.seed))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(json.dumps({
        "status": "STRUCTURAL_ONLY",
        "sha256": hashlib.sha256(payload).hexdigest(),
        "byte_count": len(payload),
        "output": str(args.output),
    }, sort_keys=True))

if __name__ == "__main__":
    main()
