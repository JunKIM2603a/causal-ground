# CausalGround — Research Status

Updated: 2026-09-29 (Asia/Seoul)

## Current state

- Session: **CausalGround 01 — 저장소 점검·가설 신규성 검증**
- Gate: **HOLD_FOR_NOVELTY**
- Research domain: LLM causal reasoning grounded in explicit causal models and evidence; retained.
- Original broad H1: retained as a research motivation / baseline question, **not accepted as the novel contribution**.
- Original H2: an unverified candidate; no novelty or empirical PASS.
- Revised primary hypothesis: **not frozen**. See `docs/hypotheses.md` for a candidate requiring further review.
- Advisor approval: **not established in the inspected repository**. Do not infer approval from repository creation or topic selection.
- Experiments: no model inference, training, benchmark evaluation, or empirical hypothesis test performed in this session.

## Inspected repository snapshot

Repository: `JunKIM2603a/causal-ground`

At the initial read, GitHub reported a public repository, default branch `main`, with only `README.md` and one initial commit:

`bcb6c010c55a0493c2b8880a7ef92b5929c59ffe`

README blob: `3cc46e2b98ca8e2cb636906d2d1ad2c3c3762547`.

These are remote observations, not claims about any unpushed local work. Documentation in this change is proposed on `docs/session-01-research-gates`; the initial README is preserved. Read the live branch and PR state before assuming this proposal has been merged.

## Completed in session 01

1. Inspected repository metadata, branches, root contents, README, and commit history through the GitHub connector.
2. Defined a six-session, completion-gated workflow in `docs/SESSION_WORKFLOW.md`.
3. Performed an initial literature collision review using primary public sources. See `docs/literature/2026-09-29_novelty_triage.md`.
4. Separated the project direction from an approved novel hypothesis.

## Blocking work

1. Read the nearest competing methods in sufficient detail to establish the precise remaining gap. An abstract-level match can defeat a broad novelty claim, but does not establish the absence of a narrower contribution.
2. Audit the candidate on causal-result applicability against DoVerifier, CausalForge, CausalDS, Causal Agent, and general tool-output reliability work.
3. Specify one primary contrast, outcome, falsifier, realistic minimum effect, and negative-result interpretation. Obtain explicit agreement on the narrowed hypothesis.
4. Record the adviser-approval state before model experiments; freeze the full protocol in session 02 before confirmatory evaluation.

## Next allowed action

Continue **session 01** with the targeted novelty and construct-validity audit. Do not start training, a large benchmark sweep, or post-hoc hypothesis tuning. Documentation merge is not a novelty PASS or permission to bypass the research gate.

## Next-session rule

Move to **CausalGround 02 — 가설 동결·실험 설계·정답 검증** only after the session-01 exit criteria in `docs/SESSION_WORKFLOW.md` are satisfied. At transition, supply the next session name and a copyable handoff containing verified branch/commit IDs, decisions, pending items, and exact files to read.
