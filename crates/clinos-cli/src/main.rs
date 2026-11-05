//! CLINOS prototype CLI. No clinical interpretation or Epic-specific integration.

use clinos_evidence::preflight_report;
use clinos_fhir::{inspect_json, MAX_INPUT_BYTES};
use clinos_integrity::clinical_equivalence_status;
use std::{env, fs::File, io::Read, process};

fn usage() {
    println!("CLINOS research prototype\nUsage: clinos preflight <synthetic-json-file>\n\nPerforms only JSON structural inspection. FHIR conformance and clinical equivalence are NOT_TESTED.");
}

fn run() -> Result<(), u8> {
    let arguments: Vec<String> = env::args().skip(1).collect();
    if arguments.as_slice() == ["--help"] || arguments.as_slice() == ["help"] {
        usage();
        return Ok(());
    }
    if arguments.len() != 2 || arguments[0] != "preflight" {
        usage();
        return Err(64);
    }

    // Read a bounded file before parsing; never echo source content on errors.
    let mut file = File::open(&arguments[1]).map_err(|_| {
        eprintln!("cannot read input as UTF-8 text");
        66
    })?;
    let mut bytes = Vec::with_capacity(MAX_INPUT_BYTES.min(64 * 1024));
    file.by_ref()
        .take((MAX_INPUT_BYTES + 1) as u64)
        .read_to_end(&mut bytes)
        .map_err(|_| {
            eprintln!("cannot read input as UTF-8 text");
            66
        })?;
    if bytes.len() > MAX_INPUT_BYTES {
        eprintln!("input exceeds prototype size limit");
        return Err(65);
    }
    let input = String::from_utf8(bytes).map_err(|_| {
        eprintln!("cannot read input as UTF-8 text");
        66
    })?;
    let summary = inspect_json(&input).map_err(|error| {
        eprintln!("structural preflight failed: {error}");
        65
    })?;
    let status = clinical_equivalence_status(&summary);
    let report = preflight_report(&summary, status);
    println!("{report}");
    Ok(())
}

fn main() {
    if let Err(exit_code) = run() {
        process::exit(i32::from(exit_code));
    }
}
