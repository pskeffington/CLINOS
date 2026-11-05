# CLINOS-001 standards / EHI research evidence

**Task / issue:** CLINOS-001 / #2  
**Branch:** `codex/clinos-001-standards-audit`  
**Base:** `codex/g0-agent-roadmap-literature-scaffold` at `bbe40ea72cff62e9aa79a790bfb0eb6886a24437`  
**Owner:** Research Director workflow (Codex execution)  
**Independent reviewers:** Clinical Informatics Lead and Terminology Steward — pending  
**Execution status:** IN_PROGRESS; primary-source inventory authored; draft PR #9 open; independent approval and applicability mapping outstanding
**Related independent task:** CLINOS-002 is also IN_PROGRESS on `codex/clinos-002-oss-audit`, draft PR #10
**Data boundary:** public specifications and metadata only; no patient records, Epic endpoints, or exports accessed  
**Claims:** no conformance, Epic compatibility, legal clearance, or clinical equivalence claims

**Cross-task CI status:** PR #8 head `906f2cdc823470a234b3aa2fb7677b29d163803b`; exact-head run [41944441203](https://github.com/pskeffington/CLINOS/actions/runs/41944441203) ended `startup_failure` with zero jobs/artifacts. Hosted CI remains blocked; Tier 1 fallback and Tier 2 DEFER remain in effect.

## Reproducible source check

Initial access date was 2026-11-04; eCFR §170.315(b)(10) and the US Core STU 9 IP review were rechecked on 2026-11-05. Sources were opened via official publisher/owner websites. Primary references and exact versions/current-publication observations are in `research/standards_inventory.md` and CSV source rows SRC-001 through SRC-004 and SRC-013 through SRC-018.

| Topic | Observed evidence | Limit / next review |
|---|---|---|
| FHIR | R4 v4.0.1, technical correction dated 2019-10-30; HL7 says current published base release is 5.0.0. R4 content has mixed normative/trial-use statuses. | Informatics must select use-case artifacts and versions. CC0 spec-text license does not grant third-party code-system rights. |
| US Core | STU 9 v9.0.0, based on FHIR 4.0.1; generated 2026-05-31; Trial-use, Maturity Level 3. | HL7 IP review lists distinct third-party content/terms; FHIR CC0 alone does not authorize redistribution of all guide-derived material. Applicability remains for Informatics/Terminology review. |
| SMART | STU 2.2 v2.2.0, active 2023-03-01, generated 2024-04-30, R4 IG. | Publisher/IP statements appear in the guide; no blanket CC0 grant for all guide content was verified. Registration and server/operator authorization remain separate and can be out of band; no endpoint or auth was attempted. |
| USCDI | Official version list identifies v7 (July 2026) as current at access. | Data classes/elements are not a FHIR schema or complete EHI mapping. |
| ONC EHI Export | eCFR §170.315(b)(10) covers the EHI a product can store at the time of certification for single-patient and population exports; computable output, public format hyperlink and current format documentation are required. | It does not mandate FHIR or guarantee post-certification deployment completeness or semantic fidelity. The linked ONC CCG is informative, not a substitute for the regulation. |
| Epic public docs | Epic on FHIR documentation lists APIs across DSTU2/STU3/R4 and registration/customer authorization constraints; EHI Tables docs describe TSV/schema and warn local versions/customization differ. | Public docs are not authorization to access a customer installation or proof of full interoperability. Public schema terms not legally reviewed. |
| HL7 v2 | Family identified as separate from FHIR. | Applicable edition, local profile, trigger event and workflow were not established; source row remains UNRESOLVED. |
| Terminology | FHIR license explicitly says implementer rights for referenced third-party SNOMED CT, LOINC, CPT and other content are separate. | No code sets added. SNOMED/LOINC intended-use and redistribution clearance remain unresolved. |

## Candidate resource scope (not a mapping)

The work-order list (Patient, Encounter, Observation, ServiceRequest, DiagnosticReport, Provenance, and medication-related R4 resources) is recorded in `research/standards_inventory.md` as `CANDIDATE_NOT_SELECTED`. No workflow, source field inventory, profile applicability, terminology, or mappings were selected. This makes the requested scope explicit while preserving the semantic review gate. GAP-014 tracks the unselected resource scope; GAP-015 tracks terminology rights.

## Checks and status

- Read-only official-source research: PASS as a research action; no external implementation tested.
- Standards inventory and source matrix additions: authored, pending independent review.
- HL7 v2 edition/profile applicability: UNRESOLVED.
- Terminology legal/use clearance: NOT_TESTED / pending responsible review; HL7 US Core IP review identifies item-specific third-party terms.
- Resource/workflow applicability: UNRESOLVED; candidate scope listed without mappings.
- Gap register updated with unresolved standards, terminology, v2, and Epic documentation reuse questions.
- Clinical mapping approval: NOT_TESTED; no mappings were implemented.
- Independent review: NOT_TESTED.

## Changed artifacts

- `research/standards_inventory.md`
- `research/literature_matrix.csv`
- `research/gap_register.csv`
- `docs/TASK_QUEUE.md`
- `evidence/CLINOS-001/SUMMARY.md`

## Next decision

Informatics and Terminology reviewers should confirm candidate FHIR/US Core/USCDI versions, applicable profiles, and code-system use terms. Until then CLINOS-003 synthetic clinical ground truth and CLINOS-005 semantic reconciliation remain blocked. CLINOS-007 must not begin normalization implementation from this inventory alone.
