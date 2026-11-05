# CLINOS-002 OSS ecosystem / license research evidence

**Task / issue:** CLINOS-002 / #3  
**Branch:** `codex/clinos-002-oss-audit`  
**Base:** `codex/g0-agent-roadmap-literature-scaffold` at `bbe40ea72cff62e9aa79a790bfb0eb6886a24437`  
**Owner:** Research Director workflow (Codex execution)  
**Independent reviewers:** Independent Validator and Terminology Steward — pending  
**Execution status:** IN_PROGRESS; nine repositories inventoried; draft PR #10 open; independent review pending
**Current branch head before this evidence refresh:** `f38142ebcb5458a7f5d5c034b1c8fb89fd5b38ae` (PR metadata is authoritative for the resulting head)
**Related independent task:** CLINOS-001 is also IN_PROGRESS on `codex/clinos-001-standards-audit`, draft PR #9
**Data boundary:** public source/metadata only; no candidate code cloned/built, no networked service tested, no patient/export data fetched

**Cross-task CI status:** PR #8 head `906f2cdc823470a234b3aa2fb7677b29d163803b`; exact-head run [41944441203](https://github.com/pskeffington/CLINOS/actions/runs/41944441203) ended `startup_failure` with zero jobs/artifacts. Hosted CI remains blocked; Tier 1 fallback and Tier 2 DEFER remain in effect.

## Method and reproducibility

Read-only GitHub metadata checks were run for each candidate:

- `gh api repos/<owner>/<repo> --jq '[.full_name,.default_branch,.pushed_at,.license.spdx_id,.html_url] | @tsv'`
- `gh api repos/<owner>/<repo>/releases/latest --jq '[.tag_name,.published_at,.html_url] | @tsv'` (404 recorded as no latest release)
- `gh api repos/<owner>/<repo>/commits/HEAD --jq '[.sha,.commit.author.date,.html_url] | @tsv'`
- `gh api repos/<owner>/<repo>/license --jq '[.license.spdx_id,.html_url] | @tsv'`

README, release, license and focused official docs were read for role and scope. Exact release/commit snapshots and license caveats appear in `research/oss_feature_matrix.md` and matrix rows SRC-005 through SRC-012.

## Nine assessed candidates

| Candidate | Snapshot | License observation | Evidence status |
|---|---|---|---|
| OpenEMR | v8_5_0 (2026-10-27); HEAD `b29475ea04f3098a06c3bd3e0279d7ac35ad2302` | GPL-3.0 | INVENTORIED |
| OpenMRS Core | 2.8.10 (2026-10-06); HEAD `891b80745b4229f297aec50a54043e1569061b01` | API `NOASSERTION`; LICENSE text MPL-2.0 plus healthcare disclaimer | INVENTORIED with file-level/license review caveat |
| OpenMRS FHIR2 module | 2.5.2 (2026-09-29); HEAD `74b81d6a58cb934cbca3b523334723903d90adb1` | API `NOASSERTION`; inspect LICENSE/notices before reuse | INVENTORIED with unresolved license metadata caveat |
| Medplum | v5.2.14 (2026-11-03); HEAD `c6c86f9e1f93a8f2cb6d6e694066edb7128dc24f` | Apache-2.0 | INVENTORIED |
| HAPI FHIR | v8.10.2 (2026-10-30); HEAD `852fe5fa7261deb6147d2ccc564b3d4d938fe3cb` | Apache-2.0 | INVENTORIED |
| Inferno Core | v1.6.0 (2026-10-27); HEAD `94f381e5e57751cf702f93987250f4277bb2ab57` | Apache-2.0 | INVENTORIED |
| Synthea | master-branch-latest release (2026-10-21); HEAD `bd8a52ba0a54ad8c6a1004b74787a14d8c25dbcc` | Apache-2.0 | INVENTORIED |
| OHIF Viewers | v3.13.14 (2026-11-03); HEAD `f4a15ef9114e3e95fc739c1c15b76f046fd2cc25` | MIT | INVENTORIED |
| EHI to FHIR | no latest release; main HEAD `e86e00ca322174c520d4e682457a20dd913033cb` (2026-06-19) | MIT | INVENTORIED; do not fetch/process sensitive report/source records |

## Results and limitations

- The matrix classifies proposed CLINOS features REUSE/INTEGRATE/DIFFERENTIATE/DEFER, with source links and tested-vs-described distinctions.
- Nine candidates meet the order's minimum eight-repository inventory threshold. This is not a complete market scan or proof of novelty.
- API metadata `NOASSERTION` for OpenMRS is not treated as evidence of unlicensed code; actual LICENSE text and notices need reviewer/legal interpretation.
- Candidate projects were not cloned, built, benchmarked, security-reviewed or tested against live/synthetic endpoints. GitHub default-branch commit/release values are point-in-time observations.
- Public EHI-to-FHIR repository description indicates real-record-derived material; no source record or report artifact was downloaded or used. Claims in its README were not independently reproduced.
- License IDs do not constitute legal advice, compatibility analysis, or transitive dependency review.
- Six additional, specific hypotheses have been added to `research/gap_register.csv`; all remain UNVERIFIED pending task-specific evidence.

## Independent review and next action

Independent Validator and Terminology Steward review is pending. They should check license notices, candidate scope, privacy handling and the feature disposition table. CLINOS-002 remains IN_PROGRESS until that review is recorded; no integration/reuse is authorized merely by this inventory.
