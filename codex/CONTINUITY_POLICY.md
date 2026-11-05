# CLINOS continuity / anti-stall policy

This policy allows the **invoked** Codex Orchestrator and Block Resolution Agent to continue useful engineering when one dependency is blocked. It does not authorize autonomous deployment, scheduled runs, clinical approval, security exceptions or merges.

## Blocked != idle
When a task fails, keep its actual status, evidence and branch intact. Before ending a Codex session, produce a next-action decision and, if authorized, start **one** different task from the ready queue. Do not spin through blocked jobs, perform blind retries or conflate fallback activity with unblocking the original task.

## Hard stops
- PHI, secrets, unexpected live-system access, unauthorized export, unclear licensing, access-control bypass, patient-care or clinical-safety concerns.
- Missing independent signoff for clinical mappings, privacy, QA, or protected branch policy.
- Work that requires silent permission/security setting changes.
Hard stops cannot be overridden by a fallback or the Orchestrator. Escalate to the designated human reviewer.

## Continuation selection
Filter task queue in order:
1. Explicitly PLANNED/READY, no unfulfilled dependencies, with a defined order and synthetic/public inputs.
2. No conflict with in-flight working tree, files, contracts or PR; branch separately.
3. No clinical semantic modification awaiting reviewer or uncertain rights.
4. Highest priority first; tie-break on lowest dependency count and smallest verifiable slice.
5. If nothing qualifies, produce a blocker report and **stop**. No invented work or fabricated approvals.

## Example: GitHub Actions startup_failure
Input: exact-head CI run has startup_failure and no runner jobs. Allowed: inspect workflow settings metadata and exact SHA; preserve local check results; attempt one authorized workflow rerun; attach logs if available. Not allowed: disable CI required checks, reduce permissions or mark CI PASS. Fallback: independent standards and OSS literature audit, if G0 policy is accessible and the task is scoped to research.

## State transitions
```text
IN_PROGRESS -> BLOCKED -> (RETRY_ONCE | FIX_NARROW | FALLBACK | ESCALATE)
                                      |
                    evidence confirms recovery
                                      v
                           IN_REVIEW -> PASS
```
FALLBACK is not a status change for the original blocked task. Record independent fallback task state separately.

## Evidence ledger
Every decision records task, exact SHA, CI run URL/job evidence, classification, chosen action, prior attempts, authorization, selected alternative and next recheck criterion. Template: `codex/BLOCK_DECISION_TEMPLATE.md`. Store decisions with the relevant issue and PR; use the file template for durable records.

## Tier 2 decision escalation
When permitted retries and fallback selection fail, do not loop or invent a PASS. Route the complete blocker record to `agents/resolution-decision.md` using `codex/ESCALATION_CHAIN.md`. Record the outcome with `codex/RESOLUTION_DECISION_TEMPLATE.md`; resume only authorized independent work. A Tier 2 disposition is not release approval.
