//! Deterministic, data-minimizing reports: no patient record contents.

use clinos_core::EvidenceStatus;
use clinos_fhir::PreflightSummary;
use serde_json::{json, Value};

pub fn preflight_report(summary: &PreflightSummary, status: EvidenceStatus) -> Value {
    json!({
        "schema": "clinos.structural-preflight.v0",
        "input_class": "synthetic-or-authorized-only",
        "root_resource_type": summary.root_resource_type,
        "total_entries": summary.total_entries,
        "unresolved_entries": summary.unresolved_entries,
        "resource_type_counts": summary.resource_type_counts,
        "clinical_equivalence": status.as_str(),
        "fhir_conformance": "NOT_TESTED",
        "warning": "Structural JSON preflight only; no clinical, terminology, or FHIR profile validation."
    })
}

#[cfg(test)]
mod tests {
    use super::*;
    use clinos_fhir::inspect_json;

    #[test]
    fn report_contains_no_patient_identifiers() {
        let input =
            r#"{"resourceType":"Patient","id":"PHI-DO-NOT-REPORT","name":[{"family":"Secret"}]}"#;
        let report =
            preflight_report(&inspect_json(input).unwrap(), EvidenceStatus::NotTested).to_string();
        assert!(!report.contains("PHI-DO-NOT-REPORT"));
        assert!(!report.contains("Secret"));
        assert!(report.contains("NOT_TESTED"));
    }
}
