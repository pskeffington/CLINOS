# Agent roles and handoffs

Agents are roles for planning and review; these files do not imply autonomous background execution.

| Agent | Decision authority | Handoff artifact |
|---|---|---|
| Research Director | Source admissibility and literature claims | Literature matrix + gap register |
| Clinical Informatics Lead | Clinical data semantics and mappings | Mapping specification + invariant cases |
| Rust Systems Engineer | Core implementation architecture | Change set + deterministic tests |
| Migration Audit Engineer | Data fidelity and error-injection cases | Reconciliation manifest |
| Workflow Simulation Engineer | Synthetic workflow models | Scenarios + state transition traces |
| Security & Privacy Reviewer | Privacy and threat-model gate | Threat/risk decision |
| Independent Validator | Release veto | Signed-off validation report |

## Shared review rules
- A developer may not approve their own validation evidence.
- Unresolved terminology or clinical linkages block a claim of lossless migration.
- All test fixtures are synthetic until formal authorization says otherwise.
- Research findings include primary URL, publication/version/date, access date, license, applicability, and confidence.
- Escalate contradictions to Research Director and Informatics Lead; no silent resolution.

## Additional roles
| Agent | Decision authority | Handoff artifact |
|---|---|---|
| Codex Orchestrator | Dependency checking and task dispatch; no unilateral signoff | Execution packet, branch/PR and task status |
| Terminology and Standards Steward | Specification, code-set license and canonical source approval | Reviewed terminology/source contract |
| Block Resolution and Continuity Agent | Diagnose blockers, bounded retry, independent fallback selection; no approval overrides | Structured blocker decision and next eligible task |

**Operational files:** `codex/CODEX_PROMPT.md` is the master Codex instruction sheet; `codex/orders/` contains task-specific contracts. `docs/TASK_QUEUE.md` is the status source of truth.

**Blocker control:** `agents/block-resolution.md`, `codex/CONTINUITY_POLICY.md` and `codex/BLOCK_DECISION_TEMPLATE.md` define safe continuation; they do not launch an always-on service.
