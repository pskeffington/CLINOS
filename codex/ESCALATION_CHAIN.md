# CLINOS engineering escalation chain

1. **Codex Orchestrator** observes task failure, records exact commit and available evidence.
2. **Tier 1 — Block Resolution and Continuity Agent** classifies the blocker, attempts permitted bounded remediation, and selects a ready independent task if possible.
3. **Tier 2 — Resolution Decision Agent** receives unresolved Tier 1 records and selects scope split, alternate method, deferral, research, human escalation, or stop.
4. **Codex Orchestrator** executes only authorized next tasks. Independent reviewers retain their normal approval authority.

## Routing contract
- Tier 2 requires the Tier 1 blocker record.
- A blocked job stays blocked until its original acceptance and approval requirements are actually met.
- Any alternate approach must satisfy the same approved acceptance criteria.
- Clinical correctness, patient privacy, licensing, repository access, security, CI and branch review requirements remain unchanged.
- If no task is eligible, record the decision and stop that execution; do not invent work.
- Avoid circular retries: reopen only when new material evidence is available.

## Example
For CLINOS-004 GitHub Actions startup failure, Tier 1 captures the failed workflow evidence and limited diagnostics. Tier 2 may defer hosted CI verification and recommend CLINOS-001 or CLINOS-002 research. It must not mark hosted CI as passed or merge a PR lacking required reviews.

The agent roles are documentation for invoked Codex sessions; separate runner configuration is necessary for continuous automation.
