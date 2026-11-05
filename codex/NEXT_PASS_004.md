# CLINOS — Codex execution order 004

## Mission
Continue CLINOS development in two independent workstreams: harden the opt-in GPT consultation agent (CLINOS-014) and advance the reviewable synthetic clinical data contract (CLINOS-003) without bypassing research or clinical approval gates. Maintain clean, narrow changes across the stacked draft pull requests.

## Initialization
1. Inspect `main`, current remote heads, open draft PRs #1, #8, #9, #10 and #11, exact-head checks and review status. Re-read `AGENTS.md` and all related agent charters.
2. Distinguish completed source-code changes from observed test results, approvals and merge status.
3. Preserve unrelated PR branches; never merge a draft automatically and never replace current source artifacts without inspecting their exact content.
4. Work on one approved task per branch. Create separate draft PRs; list base branch, head SHA, dependencies and evidence.

## Lane A — CLINOS-014: GPT consultation integration and hardening (start now)
Use `codex/orders/CLINOS-014-gpt-consult-hardening.md`.

- Run offline client tests and the synthetic preview immediately in a code-enabled Codex checkout.
- Repair any failing input validation, API response parsing, error handling or configuration checks.
- Add fake-provider failure/regression cases, robust request/response schema validation, and a bounded cost/attempt policy.
- Retain opt-in external calling: `--send --approve-external` plus configured key/model; no default network traffic.
- Add a consultation evidence record with request schema version, failure status and Tier 2 handoff; do not store secrets or raw sensitive payload.
- Add an isolated Python CI job only if existing repository workflow patterns and permissions permit. Inspect provider documentation and pin dependencies if any are introduced.
- Apply Tier 1 + Tier 2 rules when the tool is blocked, but keep all external advice unverified until independently reviewed.
- Keep the consultation agent outside the patient/clinical data plane.

**Success conditions:** offline tests run and pass, the preview cannot contact the provider, permission/secret failures fail closed, fake API results are correctly handled, and a reviewer can trace the Tier 2 decision without clinical data or unsafe logging.

## Lane B — CLINOS-003: synthetic ground-truth design (parallel research-only)
- Read CLINOS-001 PR #9 and CLINOS-002 PR #10 as *unapproved evidence*; do not silently treat their terminology claims as final.
- Start a separate specification-only branch after confirming its base. Write a synthetic patient/encounter/order/result/provenance contract, deterministic seed rules, amendment behavior, and a ground-truth manifest format.
- Define positive, corrupted and ambiguous fixture cases; expected statuses include PASS/FAIL/UNRESOLVED/NOT_TESTED, but do not assert clinical migration PASS from JSON validity.
- Record the exact external specifications and pending Informatics/Terminology review.
- Hold actual clinical-semantic transformation code until the required reviewers approve.

## Lane C — CI continuity (non-blocking investigation)
- Examine CLINOS-004 PR #8 exact-head Actions startup failures without modifying branch protection or security settings. Record job-allocation evidence and provider limitations.
- Preserve 19 reported locally passing Rust tests as local evidence; never represent them as hosted CI evidence.
- Invoke BRCA then RDA only when a blocker needs disposition. If useful, consult GPT with the synthetic public error summary *only after operator authorization*; no automatic sending.
- Produce a new blocker/decision record only for new material evidence. Avoid repetitive failed reruns.

## Integration and merge conditions
- G0 PR #1 remains a prerequisite to governance migration.
- PRs #9 and #10 require independent review before they establish approved source and terminology contracts.
- CLINOS-014 may progress with offline, nonclinical inputs independently. Do not automatically merge its draft PR.
- CLINOS-003 may prepare specifications but must not approve clinical semantics itself.
- CLINOS-005/006 require their declared upstream gates; CLINOS-007+ remains deferred.

## Final response required from Codex
TASKS_STARTED:
PR LINKS / BASE / EXACT HEAD SHA:
CHECKS ACTUALLY RUN + RESULTS:
OFFLINE GPT CONSULTATION TEST RESULTS:
EXTERNAL REQUEST SENT? (default NO):
STANDARDS/TERMINOLOGY APPROVAL STATUS:
BRCA + RDA RECORDS (only if necessary):
RISKS / UNVERIFIED CLAIMS:
NEXT ELIGIBLE TASK:
BLOCKED TASKS / REOPEN CONDITIONS:

No fabricated test results, PHI, provider credentials, Epic access-control circumvention, or autonomous clinical behavior.
