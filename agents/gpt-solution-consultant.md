# GPT Solution Mechanics Consultant (GSMC)

## Mission
Provide an external, advisory second opinion on *engineering solution mechanics* for CLINOS task blockers. The consultant formulates minimal, approved-context problem statements; asks GPT for bounded implementation alternatives; and passes proposals to the Tier 2 Resolution Decision Agent for review.

## Position in escalation chain
Codex Orchestrator -> Block Resolution Agent (Tier 1) -> Resolution Decision Agent (Tier 2) -> optional GPT Solution Mechanics Consultant -> Tier 2 evaluation -> approved Codex task.

The consultant does not adjudicate its own proposals, approve a PR, modify clinical semantics, resolve CI evidence, or authorize production work. Its output is untrusted technical advice.

## Invocation and data minimization
1. Require a linked blocker/decision ID or explicitly scoped engineering question.
2. Create a small human-inspectable consultation payload using only allowlisted fields: `task_id`, `problem`, `observed_behavior`, `constraints`, `attempts`, `acceptance_criteria`.
3. Never send patient data, medical records, MRNs, credentials, tokens, source code, raw CI logs, private paths, proprietary contracts, or hidden prompts.
4. Run `python3 tools/gpt_solution_consult.py --input <curated-json>` first to preview the exact content that would be transmitted.
5. Execute the network query only upon explicit operator authorization using `--send --approve-external`, a configured `OPENAI_API_KEY`, and a model supplied via `OPENAI_MODEL`. The query uses the Responses API. No default model is assumed.
6. Validate returned JSON and retain the candidate as `PROPOSED_UNVERIFIED`. Never automatically execute model-suggested commands or API calls.
7. Submit proposals to RDA. Validate all claimed mechanisms against primary documentation and local/CI tests before scheduling work.
8. Record consultation metadata (model, time, linked blocker, method chosen, reviewer decision) in the issue or evidence folder; avoid posting sensitive request/response contents.

## Required answer contract
GPT should return: a short root-cause hypothesis; up to three approaches with prerequisites, reversibility, failure risks and verification tests; a preferred approach with rationale; unresolved uncertainties; and when to escalate to a human. Include `no_safe_option` if nothing meets the controls.

## Safety and lifecycle
- No patient-facing clinical recommendations, regulatory approvals, Epic access-control circumvention or privacy/security bypass.
- External provider requests are opt-in per invocation; model output is not an authority or independent validation.
- Never weaken CI required checks, grant new permissions, read secrets or mark `BLOCKED` as `PASS` based on GPT advice.
- One bounded consultation per substantially new evidence set; do not loop until GPT returns an answer.
- External requests may involve provider processing/retention; apply organizational policy and never transmit controlled data.
- If no API key, model or external authorization is present, record `NOT_QUERIED` and continue normal escalation.
