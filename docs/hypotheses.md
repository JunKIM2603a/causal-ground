# CausalGround — Hypothesis register

Updated: 2026-09-29

## Version and decision policy

No primary hypothesis is frozen. Topic selection is not novelty verification. Changes are versioned; old hypotheses and negative outcomes are not erased. Researcher agreement and the required approval state must be recorded before experimental execution.

## H1-v0 — retained as motivation, not a novel contribution

Providing an LLM with explicit causal structure and external causal-computation results improves system accuracy/consistency relative to language-only reasoning.

Status: **BROAD_NOVELTY_NOT_ACCEPTED** following the initial review in `docs/literature/2026-09-29_novelty_triage.md`. This is not an empirical rejection of H1-v0.

## H2-v0 — unverified

The grounding benefit becomes larger when observational associations conflict with causal effects.

Status: **NOT_FROZEN / NOVELTY_UNVERIFIED**. The exact interaction, comparison, and task population remain unspecified. It must not be treated as an established novel hypothesis.

## Candidate R1 — correct computation versus applicable evidence

Status: **DRAFT_FOR_NOVELTY_AUDIT**. This is a proposal for investigation, not a selected replacement H1, not a tested finding, and not a claim that the issue is unstudied.

### Research question

Can a causal-grounded LLM distinguish a tool result that is mathematically correct for its declared query from a result that is actually applicable to the user's current causal question?

Potential mismatches include observation versus intervention, different conditioning evidence, a changed causal graph or assumptions, and a different target population. Begin with a small, explicitly specified intervention task; do not begin with all mismatch types or unrestricted counterfactuals.

### Candidate method hypothesis H1-R1

Holding the model, underlying causal facts, and evaluation items fixed, a query-scope validation pipeline reduces acceptance of internally correct but inapplicable tool results relative to matched-information prose and generic self-check baselines, without an unacceptable loss of correct handling of applicable results.

This claim is deliberately not frozen: the concrete mechanism, primary estimand, minimum effect, utility guardrail, budget matching, and novelty distinction must be specified first. The main scientific question cannot be reduced to a trivial exact-ID check.

### Worked mathematical fixture — NOT a model experiment

Let Z be Bernoulli(0.5), Y=Z, P(X=1 | Z=1)=0.9, and P(X=1 | Z=0)=0.1. The graph is Z->X and Z->Y, with no edge X->Y.

Then P(Y=1 | X=1)=0.9, while P(Y=1 | do(X=1))=0.5.

A tool returning the first value is correct for an observational query but does not answer a request for the second. This example illustrates the distinction only. It is not a new causal theorem, not evidence that an LLM makes this error, and not a research success.

### Controls that must survive the audit

1. LLM-only and strong language-only reasoning using the information appropriate to their stated role.
2. Prose versus structured causal inputs containing the same facts when testing the representation.
3. Same-information generic self-check with measured inference cost.
4. Deterministic query/scope matching baseline and an oracle semantic-compatibility checker. If an ordinary checker solves the proposed task, do not disguise this as novel LLM reasoning.
5. Causal engine alone, LLM plus engine, and an oracle-input ceiling; distinguish parsing, computation, applicability validation, and final answer errors.
6. Valid-result controls and semantics-preserving paraphrases/aliases, so rejecting everything or exact string matching does not count as a useful solution.

### Provisional metrics and falsification

Candidate outcomes: inapplicable-result acceptance rate, valid-result handling accuracy, rejection/answer coverage, end-to-end accuracy, and token/runtime cost. Denominators must be fixed by ground-truth task categories, not chosen post hoc by the model's actions.

The method hypothesis is unsupported if the benefit disappears under matched information/budget, is matched by a simple baseline with no new insight, or requires excessive rejection of valid results. Equivalence or bounded-effect conclusions require a predeclared meaningful effect and sufficient precision; a nonsignificant p-value is not enough.

### Novelty blockers

DoVerifier already studies symbolic validity of causal expressions. CausalForge explicitly separates formal validity from fidelity to the intended scientific statement. CausalDS studies identification and abstention. General agent/tool-output reliability work may cover the same failure mechanism. Full-method comparisons are required before claiming a gap.

## Next decision

Approve, revise, or reject Candidate R1 after the targeted literature audit. Do not freeze it merely to move to session 02 or meet a date. Keep the project domain while avoiding another broad, already-studied H1.
