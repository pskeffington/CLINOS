# CLINOS open, non-identifying research corpus (G0)

**Status:** RESEARCH / STRUCTURAL-ONLY; this does not clear CLINOS-003's clinical-semantic dependency.

## Admission contract
Only accept (a) locally authored synthetic fixtures; (b) Synthea-generated fictional records produced locally from a pinned, Apache-2.0 version after removing direct and quasi-identifying fields; (c) individually inspected examples from CC0-covered HL7 FHIR R4 specification materials, excluding third-party terminology and identifiable example content; or (d) specifically reviewed Apache-2.0 source-code mock fixtures after file-by-file provenance checks. Do not equate a code repository's license to unrestricted rights over all datasets in it.

**No live patient records, real de-identified records, credentialed datasets, clinical portal scrapes, public leak mirrors, GitHub EHI patient specimens, or material of uncertain origin.** Do not auto-download web content merely because it is accessible. Respect robots, source terms, licenses, rate limits and applicable privacy agreements. No outbound telemetry.

## First-wave source registry
| Source | URI | License basis | Admission | Acquisition mechanism |
|---|---|---|---|---|
| CLINOS locally authored structural fixtures | generated within CLINOS | project-owned | ALLOW, structural-only | deterministic stdlib generator; no clinical codes |
| Synthea software | https://github.com/synthetichealth/synthea | Apache-2.0, see pinned LICENSE | CONDITIONAL | pin commit and generate locally; sanitize and scan each output |
| HL7 FHIR R4 specification | https://hl7.org/fhir/R4/license.html | CC0 for specified spec materials; third-party IP excluded | CONDITIONAL | pin selected artifact and verify individual example is safe |
| Medplum source mock tests | https://github.com/medplum/medplum | Apache-2.0 for code, content-level review still necessary | HOLD | hand-curated mock fixture review only |
| Epic EHI Tables docs | https://open.epic.com/EHITables | reuse rights not cleared | REFERENCE-ONLY | link to documentation; do not scrape or redistribute |
| SMART hosted sandbox | service-specific terms | not a blanket dataset license | HOLD | do not bulk scrape |
| MIMIC/real EHR datasets | access agreements | not an open identifier-free default | DENY for this corpus | never import |

## Data minimization and rejection
Disallow names, birth/death dates, street/ZIP/address, geolocation, contact data, email, phone, MRNs, SSNs, account numbers, IP addresses, free-text clinical notes, image metadata, human-origin persistent IDs and exact real event timestamps. Synthetic linkage tokens may be used **only** when generated locally, clearly labeled artificial, and not derived from a person's identifier. Events use relative sequence offsets, not calendar times. For external inputs, reject by default until a documented field-level sanitizer and independent privacy review are implemented; do not simply trust generator claims.

Keep generator seed, generator commit, source URL, license snapshot, transformation version, SHA-256 of final admitted bytes, fields dropped, manual reviewer and disposition in a local provenance manifest. No raw rejected artifact in git/CI logs; quarantine securely or delete as approved. Do not log values while scanning. Hashes are for integrity, not anonymization.

## Separation of gates
1. **G0:** structural toy fixtures, offline stdlib tests, no clinical assertions: permissible as isolated draft research.
2. **CLINOS-001 + semantic and terminology approval:** required before fixtures claim real clinical relationships, value sets, units or mappings.
3. **Independent QA and privacy sign-off:** needed before promoting any fixture to validation ground truth.
4. **No clinical equivalence claim** from synthetic input, schema validity, or successful round-trip alone.

## Next implementation sequence
- G0-A: ship minimal local generator + deterministic unit tests, inspect output for prohibited fields.
- G0-B: pin Synthea revision, inspect its licenses and module outputs; propose deterministic stripping policy; no raw import yet.
- G0-C: add gated candidate ingestion (manifest, SHA-256, allowlist, schema check, rejection report without contents).
- G1: after upstream approvals, define semantics for encounter/order/result mutation fixtures and independent oracle.

See CLINOS-003 issue #4 and CLINOS-001 PR #9. This document is not approval for the later stages.
