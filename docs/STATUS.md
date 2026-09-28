# CausalGround — Research Status

Updated: 2026-09-29 (Asia/Seoul), v2 candidate audit

## Current state

- Session: **CausalGround 01 — 저장소 점검·가설 신규성 검증**
- Gate: **HOLD_FOR_NOVELTY**
- Research domain: LLM causal reasoning grounded in explicit causal models and evidence; retained.
- Original broad H1: retained as a research motivation / baseline question, **not accepted as the novel contribution**.
- Original H2: an unverified candidate; no novelty or empirical PASS.
- Revised primary hypothesis: **not selected or frozen**. See `docs/hypotheses.md`.
- R1: high method-collision risk after reading DoVerifier and CausalForge; not approved as a novel primary method.
- R2: computation-verification cue / applicability spillover, priority for targeted design audit only.
- R3: evidence enrichment without counterfactual identification gain, alternative requiring oracle construct validation.
- R4: assumption-dependent stale-result invalidation, deprioritized because of close existing work.
- Advisor approval: **not established in the inspected repository**. Do not infer approval from repository creation or topic selection.
- Experiments: no model inference, training, benchmark evaluation, or empirical hypothesis test performed in this session. A tiny explanatory counterfactual example was checked using exact fractional arithmetic; this is not an LLM result.

## Inspected repository snapshot

Repository: `JunKIM2603a/causal-ground`

At the initial read, GitHub reported a public repository, default branch `main`, with only `README.md` and one initial commit:

`bcb6c010c55a0493c2b8880a7ef92b5929c59ffe`

README blob: `3cc46e2b98ca8e2cb636906d2d1ad2c3c3762547`.

These are remote observations, not claims about any unpushed local work. Documentation is proposed on `docs/session-01-research-gates`; the initial README is preserved. At the start of this follow-up, PR #1 was open, draft, unmerged, with head `e7f12d290847bd54fb1c6e03752219d8d4b31a8e`. This follow-up adds commits on that same branch. Read the live branch and PR state before assuming a merge or a current head SHA.

## Completed in session 01

1. Inspected repository metadata, branches, root contents, README, and commit history through the GitHub connector.
2. Defined a six-session, completion-gated workflow in `docs/SESSION_WORKFLOW.md`.
3. Performed an initial literature collision review using primary public sources: `docs/literature/2026-09-29_novelty_triage.md`.
4. Separated project direction from an approved novel hypothesis.
5. Performed the v2 targeted audit of the relevant DoVerifier, CausalForge, CausalDS text and additional primary-source leads: `docs/literature/2026-09-29_h1_candidate_audit_v2.md`.
6. Added three explicitly unfrozen candidate directions, recorded reasons to deprioritize R4, and prepared next-work gates: `docs/plans/session01_next_work.md`.
7. Read the DoVerifier authors' README. No installation, license clearance, or code reproduction is claimed.

## Blocking work

1. Complete the precise novelty and construct-validity comparison for R2 and R3. Abstract-level overlap can defeat a broad claim, but non-discovery of a narrow match does not prove novelty.
2. For R2, separate truthful calculation-verification scope from generic authority cues, information additions, and trivial string/type checks. For R3, prove identified-set invariance of the proposed evidence-enrichment items before interpreting model behavior.
3. Specify one primary contrast, outcome, falsifier, meaningful minimum effect, acceptable valid-task regression, and negative-result interpretation. Obtain explicit agreement on one narrowed hypothesis.
4. Record the adviser-approval state before model experiments; freeze the full protocol in session 02 before confirmatory evaluation.
5. Resolve remaining literature/code-access gaps; CausalVerify arXiv pages could not be retrieved in the v2 audit. Do not count this lead as fully reviewed.

## Next allowed action

Continue **session 01** using `docs/plans/session01_next_work.md`: inspect R2's label/contrast rules and R3's oracle requirements, specify 8–12 hand-checkable fixtures, and decide whether either question survives the novelty/construct audit. The fixture suite is not yet implemented or complete.

Do not start training, a large benchmark sweep, or post-hoc hypothesis tuning. Documentation merge is not a novelty PASS or permission to bypass the research gate.

## Next-session rule

Move to **CausalGround 02 — 가설 동결·실험 설계·정답 검증** only after the session-01 exit criteria in `docs/SESSION_WORKFLOW.md` are satisfied. At transition, supply the next session name and a copyable handoff containing verified branch/commit IDs, decisions, pending items, and exact files to read.
