//! Conservative research-level status classification for JSON preflight.
//! This is deliberately not a clinical migration validator.

use clinos_core::EvidenceStatus;
use clinos_fhir::PreflightSummary;

/// Entry omissions are unresolved, while successful structure inspection
/// leaves clinical equivalence NOT_TESTED, never PASS.
pub fn clinical_equivalence_status(summary: &PreflightSummary) -> EvidenceStatus {
    if summary.unresolved_entries > 0 {
        EvidenceStatus::Unresolved
    } else {
        EvidenceStatus::NotTested
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use clinos_fhir::inspect_json;

    #[test]
    fn no_false_clinical_pass() {
        let good = inspect_json(r#"{"resourceType":"Bundle","entry":[{"resource":{"resourceType":"Patient"}}]}"#)
            .expect("valid shape");
        assert_eq!(clinical_equivalence_status(&good), EvidenceStatus::NotTested);
    }

    #[test]
    fn unknown_entry_is_unresolved() {
        let ambiguous = inspect_json(r#"{"resourceType":"Bundle","entry":[{}]}"#).expect("shape");
        assert_eq!(clinical_equivalence_status(&ambiguous), EvidenceStatus::Unresolved);
    }
}
