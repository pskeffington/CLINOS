//! Minimal, non-conformance JSON shape inspection of FHIR-shaped inputs.
//!
//! This is NOT a FHIR profile validator, terminology mapper, migration engine,
//! or assessment of clinical correctness. No source content is echoed.

use serde_json::Value;
use std::collections::BTreeMap;
use std::fmt;

pub const MAX_INPUT_BYTES: usize = 4 * 1024 * 1024;

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum PreflightError {
    TooLarge,
    InvalidJson,
    RootNotObject,
    MissingResourceType,
    InvalidBundleEntry,
}

impl fmt::Display for PreflightError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let message = match self {
            Self::TooLarge => "input exceeds 4 MiB structural preflight limit",
            Self::InvalidJson => "input is not valid JSON",
            Self::RootNotObject => "root JSON value must be an object",
            Self::MissingResourceType => "root resourceType must be a non-empty string",
            Self::InvalidBundleEntry => "Bundle entry must be an array if present",
        };
        f.write_str(message)
    }
}

impl std::error::Error for PreflightError {}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct PreflightSummary {
    pub root_resource_type: String,
    pub total_entries: usize,
    pub unresolved_entries: usize,
    pub resource_type_counts: BTreeMap<String, usize>,
}

pub fn inspect_json(input: &str) -> Result<PreflightSummary, PreflightError> {
    if input.len() > MAX_INPUT_BYTES {
        return Err(PreflightError::TooLarge);
    }

    let value: Value = serde_json::from_str(input).map_err(|_| PreflightError::InvalidJson)?;
    let object = value.as_object().ok_or(PreflightError::RootNotObject)?;
    let kind = object
        .get("resourceType")
        .and_then(Value::as_str)
        .filter(|value| !value.trim().is_empty())
        .ok_or(PreflightError::MissingResourceType)?;

    let mut summary = PreflightSummary {
        root_resource_type: kind.to_owned(),
        total_entries: 0,
        unresolved_entries: 0,
        resource_type_counts: BTreeMap::new(),
    };

    if kind == "Bundle" {
        if let Some(entries) = object.get("entry") {
            let array = entries
                .as_array()
                .ok_or(PreflightError::InvalidBundleEntry)?;
            summary.total_entries = array.len();
            for entry in array {
                let resource_type = entry
                    .get("resource")
                    .and_then(Value::as_object)
                    .and_then(|resource| resource.get("resourceType"))
                    .and_then(Value::as_str)
                    .filter(|value| !value.trim().is_empty());
                match resource_type {
                    Some(name) => *summary.resource_type_counts.entry(name.to_owned()).or_insert(0) += 1,
                    None => summary.unresolved_entries += 1,
                }
            }
        }
    } else {
        summary.resource_type_counts.insert(kind.to_owned(), 1);
    }

    Ok(summary)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn deterministic_bundle_summary() {
        let input = r#"{"resourceType":"Bundle","entry":[{"resource":{"resourceType":"Observation"}},{"resource":{"resourceType":"Patient"}},{"resource":{"resourceType":"Observation"}}]}"#;
        let found = inspect_json(input).expect("shape should parse");
        assert_eq!(found.root_resource_type, "Bundle");
        assert_eq!(found.total_entries, 3);
        assert_eq!(found.unresolved_entries, 0);
        assert_eq!(found.resource_type_counts.get("Observation"), Some(&2));
        assert_eq!(found.resource_type_counts.get("Patient"), Some(&1));
    }

    #[test]
    fn missing_embedded_resource_is_unresolved_not_invented() {
        let found = inspect_json(r#"{"resourceType":"Bundle","entry":[{}]}"#).expect("parse");
        assert_eq!(found.unresolved_entries, 1);
        assert!(found.resource_type_counts.is_empty());
    }

    #[test]
    fn bad_json_rejected() {
        assert_eq!(inspect_json("{"), Err(PreflightError::InvalidJson));
    }

    #[test]
    fn missing_root_type_rejected() {
        assert_eq!(inspect_json("{}"), Err(PreflightError::MissingResourceType));
    }

    #[test]
    fn non_object_root_rejected() {
        assert_eq!(inspect_json("[]"), Err(PreflightError::RootNotObject));
    }

    #[test]
    fn invalid_entry_shape_rejected() {
        assert_eq!(
            inspect_json(r#"{"resourceType":"Bundle","entry":{}}"#),
            Err(PreflightError::InvalidBundleEntry)
        );
    }

    #[test]
    fn oversized_input_rejected() {
        let oversized = "x".repeat(MAX_INPUT_BYTES + 1);
        assert_eq!(inspect_json(&oversized), Err(PreflightError::TooLarge));
    }
}
