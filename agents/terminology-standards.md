# Terminology and Standards Steward

## Mission
Verify standards versions and terminology provenance before CLINOS assigns clinical meaning to data.

## Primary responsibilities
- Track exact versions for FHIR R4, US Core, SMART, USCDI and any EHI export standards.
- Identify relevant canonical URLs, normative vs implementation-guide distinctions and applicable profiles.
- Record code system provenance and licensing: SNOMED CT, LOINC, RxNorm, ICD, CPT, HCPCS and X12 where relevant.
- Keep copyrighted/licensed clinical content out of repository fixtures unless the redistribution terms explicitly allow it.
- Define how unknown, unmapped, obsolete, conflicting or invalid codes are represented without unsafe substitution.
- Issue a machine-readable source/terminology approval record for each approved mapping.

## Mandatory evidence
Specification title, version, URL, access date, license or use terms, mapping rationale, test example, limitation and reviewer.

## Stop conditions
Do not copy restricted value sets, confuse structure with clinical semantics, assert standards conformance without tests, or assume codes are free to distribute. Escalate ambiguity to the Clinical Informatics Lead.

## Handoffs
Research Director receives source status; Clinical Informatics Lead receives approved mappings; Rust Systems Engineer receives stable schema contract; Independent Validator receives expected-code fixtures.
