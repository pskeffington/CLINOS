use std::{
    fs,
    path::PathBuf,
    process::{Command, Output},
    sync::atomic::{AtomicU64, Ordering},
};

static NEXT_ID: AtomicU64 = AtomicU64::new(0);

fn temp_path(label: &str) -> PathBuf {
    let id = NEXT_ID.fetch_add(1, Ordering::Relaxed);
    std::env::temp_dir().join(format!("clinos-{label}-{}-{id}", std::process::id()))
}

fn run(args: &[&str]) -> Output {
    Command::new(env!("CARGO_BIN_EXE_clinos"))
        .args(args)
        .output()
        .expect("CLI process should start")
}

#[test]
fn help_is_successful() {
    let output = run(&["--help"]);
    assert!(output.status.success());
    assert!(String::from_utf8_lossy(&output.stdout).contains("Usage: clinos preflight"));
}

#[test]
fn missing_file_fails_without_echoing_path() {
    let path = temp_path("missing-secret-marker");
    let output = run(&["preflight", path.to_str().unwrap()]);
    assert_eq!(output.status.code(), Some(66));
    let combined = format!(
        "{}{}",
        String::from_utf8_lossy(&output.stdout),
        String::from_utf8_lossy(&output.stderr)
    );
    assert!(!combined.contains("missing-secret-marker"));
}

#[test]
fn malformed_json_fails_without_echoing_payload() {
    let path = temp_path("malformed");
    fs::write(
        &path,
        r#"{"resourceType":"Patient","id":"SYNTHETIC-SECRET""#,
    )
    .unwrap();
    let output = run(&["preflight", path.to_str().unwrap()]);
    let _ = fs::remove_file(&path);
    assert_eq!(output.status.code(), Some(65));
    let combined = format!(
        "{}{}",
        String::from_utf8_lossy(&output.stdout),
        String::from_utf8_lossy(&output.stderr)
    );
    assert!(!combined.contains("SYNTHETIC-SECRET"));
}

#[test]
fn oversized_file_fails() {
    let path = temp_path("oversized");
    fs::write(&path, vec![b' '; clinos_fhir::MAX_INPUT_BYTES + 1]).unwrap();
    let output = run(&["preflight", path.to_str().unwrap()]);
    let _ = fs::remove_file(&path);
    assert_eq!(output.status.code(), Some(65));
    assert!(String::from_utf8_lossy(&output.stderr).contains("size limit"));
}

#[test]
fn invalid_utf8_fails_closed() {
    let path = temp_path("invalid-utf8");
    fs::write(&path, [0xff, 0xfe]).unwrap();
    let output = run(&["preflight", path.to_str().unwrap()]);
    let _ = fs::remove_file(&path);
    assert_eq!(output.status.code(), Some(66));
    assert!(String::from_utf8_lossy(&output.stderr).contains("UTF-8"));
}

#[test]
fn privacy_sensitive_fields_never_appear_in_report() {
    let path = temp_path("privacy");
    fs::write(&path, r#"{"resourceType":"Patient","id":"SYNTHETIC-SECRET","name":[{"family":"PRIVATE-FAMILY"}],"telecom":[{"value":"private@example.invalid"}]}"#).unwrap();
    let output = run(&["preflight", path.to_str().unwrap()]);
    let _ = fs::remove_file(&path);
    assert!(output.status.success());
    let stdout = String::from_utf8_lossy(&output.stdout);
    assert!(!stdout.contains("SYNTHETIC-SECRET"));
    assert!(!stdout.contains("PRIVATE-FAMILY"));
    assert!(!stdout.contains("private@example.invalid"));
    assert!(stdout.contains("NOT_TESTED"));
}

#[test]
fn invalid_input_shape_fails_without_echoing_payload() {
    let path = temp_path("invalid-shape");
    fs::write(
        &path,
        r#"{"resourceType":"Bundle","entry":["SECRET-PAYLOAD"]}"#,
    )
    .unwrap();
    let output = run(&["preflight", path.to_str().unwrap()]);
    let _ = fs::remove_file(&path);
    assert_eq!(output.status.code(), Some(65));
    assert!(!String::from_utf8_lossy(&output.stderr).contains("SECRET-PAYLOAD"));
}
