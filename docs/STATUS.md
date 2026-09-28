# CausalGround — Research Status

Updated: 2026-09-29 (Asia/Seoul), v3 construct audit

## Current state

- Session: **CausalGround 01 — 저장소 점검·가설 신규성 검증**
- Gate: **HOLD_FOR_NOVELTY_AND_SELECTION**
- Research domain retained: reliable LLM causal reasoning grounded in explicit models and evidence.
- Primary H1: **NOT SELECTED / NOT FROZEN / NOT EMPIRICALLY TESTED**.
- Next protocol candidate recommendation: **R3a — truthful, nonredundant second-intervention evidence that leaves the target counterfactual identified set unchanged**.
- This recommendation supersedes v2's investigation priority for R2, not the historical hypothesis record. See `docs/literature/2026-09-29_construct_audit_v3.md` for the current definition.
- R1: high method-collision risk; retained as possible baseline/mitigation, not a novel primary method.
- R2: alternative; numerical fixtures checked, verification-label and generic-authority controls unfinished.
- R3: narrowed to R3a, with exact mathematical construction checks now implemented.
- R4: deprioritized because of close existing work.
- Advisor approval: **not established in inspected sources**. Topic/repository selection is not approval.
- LLM calls: **0**. GPU/model experiments: **0**. Training: **0**.
- CPU mathematical validation: **12 unit tests passed**, R2 10 numerical fixtures, R3 12 fixtures, 121 analytic-vs-vertex comparisons. These are construction checks, NOT evidence for an LLM hypothesis.

## Repository observations and history

Initial `main` contained README and commit `bcb6c010c55a0493c2b8880a7ef92b5929c59ffe`.
At the start of v3, PR #1 was open/draft/unmerged with head `0b0b8d672fa8138b4972731b8ee6340627c5db8c` on `docs/session-01-research-gates`.
Changes stay on this branch; main and the original README are not directly modified. These are remote GitHub observations, not a statement about unpushed local work. Read live PR state before assuming the latest SHA or a merge.

## Completed work

1. Repository inspection, six-session workflow and broad-H1 novelty triage.
2. v2 targeted literature audit and R1/R2/R3/R4 candidate record, preserved in existing documents.
3. v3 targeted comparisons with CausalDS, The Information Shadow, GSM-IC, AbstentionBench, ToolMaze, Who Do LLMs Trust?, Partial Identification from LLM Prompts, CounterBench and classical probabilities-of-causation work. Reading depth is stated per source in v3; not a systematic exhaustive review.
4. Exact continuous four-response-type oracle using rational Gaussian elimination and all active-zero-coordinate subsets; comparison to closed-form sharp bounds.
5. R3: 6 nonredundant identified-set-invariant fixtures, 2 shrinking-bound, 3 point-identified and 1 inconsistent-assumption controls. R2: 5 numerically distinct mismatches and 5 valid/equal-value controls.
6. Unit tests executed in the ChatGPT CPU container under Python 3.13.5, not the user's PC or GitHub Actions. No external packages or model weights.
7. DoVerifier root contents inspected; no root LICENSE/package manifest seen. Full license audit, installation and reproduction remain unperformed. No third-party source copied; DoVerifier is not a prerequisite for the new PNS construction.

## Current artifacts

- `docs/literature/2026-09-29_construct_audit_v3.md`: current candidate recommendation, source comparison, proof, controls, and next protocol draft.
- `scripts/validate_research_fixtures.py`: exact CPU-only numerical fixture validation and full report exporter.
- `tests/test_research_fixtures.py`: 12 unit tests, including inconsistent inputs and numerical-tie controls.
- `results/validation/session01_validation_summary.json`: executed checks, source hashes and limitations.
- Existing `docs/hypotheses.md` and v2 files remain historical, unfrozen candidates. Do not mistake their old priority for a final selection.

## Remaining blockers and next concrete work

The core mathematical requirement for R3a is satisfied in the specified binary model class, but neither benchmark readiness nor novelty is certified.

1. Complete the precise adjacent comparison for CounterBench/evidence-sufficiency work. CausalVerify's arXiv pages still could not be fetched; do not claim a full review.
2. Finalize the **R3a question/answer contract and submission protocol**, rather than keep generating candidates. Explicitly ask what is determined by the given information, not a Bayesian best guess. Specify allowed conditional estimates, bounds, abstention, inconsistency and parse errors.
3. Build and test natural-language rendering, length/repetition/irrelevant-information controls, input/output separation and grouped splits. Current fixtures are mathematical specifications only.
4. Record researcher selection, model/revision, primary contrast, delta/epsilon, power/precision plan and adviser approval. No model experiment until required approval is established; no confirmatory experiment before protocol freeze.

## Next-session rule

Remain in session 01. Move to **CausalGround 02 — 가설 동결·실험 설계·정답 검증** only after the session-01 choice/novelty exit conditions are met. This commit is not a H1 PASS, experiment authorization, or automatic session transition. At transition, state it explicitly and provide a verified-SHA handoff.
