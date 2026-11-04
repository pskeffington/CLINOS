//! Shared evidence states for CLINOS research tooling.
//! No state here establishes clinical equivalence or patient safety.

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum EvidenceStatus {
    Pass,
    Fail,
    Unresolved,
    NotTested,
}

impl EvidenceStatus {
    pub const fn as_str(self) -> &'static str {
        match self {
            Self::Pass => "PASS",
            Self::Fail => "FAIL",
            Self::Unresolved => "UNRESOLVED",
            Self::NotTested => "NOT_TESTED",
        }
    }
}

#[cfg(test)]
mod tests {
    use super::EvidenceStatus;

    #[test]
    fn states_have_stable_names() {
        assert_eq!(EvidenceStatus::Pass.as_str(), "PASS");
        assert_eq!(EvidenceStatus::Fail.as_str(), "FAIL");
        assert_eq!(EvidenceStatus::Unresolved.as_str(), "UNRESOLVED");
        assert_eq!(EvidenceStatus::NotTested.as_str(), "NOT_TESTED");
    }
}
