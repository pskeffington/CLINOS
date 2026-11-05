# GPT solution-mechanics consultation protocol

This CLINOS auxiliary agent is not part of the clinical data plane. It is a **manual opt-in** engineering consultation path.

## Example local workflow
```sh
python3 tools/gpt_solution_consult.py --input tools/fixtures/gpt-consult-ci.json
# Review the exact preview. Only then run:
OPENAI_MODEL=<approved-model-id> OPENAI_API_KEY=<secret> \
  python3 tools/gpt_solution_consult.py \
  --input tools/fixtures/gpt-consult-ci.json --send --approve-external
```

Never place credentials in committed files or command-line arguments. The model ID must come from current provider documentation or your approved configuration, not guesses. Requests use OpenAI's Responses API; this is not the retired Assistants API.

## Escalation integration
- Tier 1 documents confirmed failures and bounded remediation.
- Tier 2 decides whether a consultation would materially help. Do not call GPT for missing legal/clinical authorization.
- Consultant builds a small curated problem statement and obtains operator approval for external transmission.
- Returned solution mechanics are classified **PROPOSED_UNVERIFIED**; Tier 2 independently assesses admissibility and requests implementation/test evidence.
- Orchestrator may then open a separately reviewed draft task. Original blocker status is unchanged until its acceptance evidence passes.

## Provider failure
HTTP/API error, malformed response, timeout or missing configuration -> `NOT_QUERIED`/`NO_VALID_PROPOSAL` with generic error; no automatic retry loop, no release-gate change.

## Test requirements
- Preview never needs an API key or network connection.
- Sending requires both flags and a configured model/key.
- Raw input includes only exact allowlisted fields; extra keys are rejected.
- Empty, oversized, and likely secret/identifier-bearing payloads are rejected conservatively.
- Tests use a fake transport; no live API calls in CI.
- Query output is untrusted, capped and schema-validated; no returned script is executed.
- The actual provider invocation must be verified separately when authorized; offline tests do not prove successful network access.

## API source
OpenAI Responses API documentation: https://platform.openai.com/docs/api-reference/responses

## Next verification pass
Follow `codex/orders/CLINOS-014-gpt-consult-hardening.md` for offline test execution, payload and schema hardening, fake transport failure cases, audit metadata and independent security/QA review. Existing sample consultation behavior remains experimental and must be verified on a real code-enabled checkout. No live API calls in CI.
