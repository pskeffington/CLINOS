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
