# Initial novelty collision review — 2026-09-29

## Scope and epistemic status

This is an **initial screening**, not an exhaustive systematic review, an independent reproduction, or a novelty PASS. Claims below distinguish source content from the project assessment. A paper's existence or abstract does not validate all of its empirical claims. arXiv-only status is reported as preprint unless a venue has been separately verified.

## Primary sources checked

| ID | Source | Inspected material | What the source supports | Consequence for CausalGround |
|---|---|---|---|---|
| P1 | Jin et al., **CLadder: Assessing Causal Reasoning in Language Models**, NeurIPS 2023. https://papers.nips.cc/paper_files/paper/2023/hash/631bb9434d718ea309af82566347d607-Abstract-Conference.html | Official proceedings abstract | Formal causal questions generated from causal graphs and an oracle inference engine; association/intervention/counterfactual tasks; CausalCoT prompting. | Synthetic SCM-related QA and structured causal prompting are not novel by themselves. |
| P2 | Han et al., **Causal Agent based on Large Language Model**, arXiv:2408.06849, first submitted 2024; revised version also exists. https://arxiv.org/abs/2408.06849 | Primary abstract/version page | LLM agents equipped with causal tools, reasoning and memory; evaluation across causal task levels. | The generic proposal to combine an LLM with causal computation directly overlaps prior work. |
| P3 | Xu and Fu, **NoisyCausal: A Benchmark for Evaluating Causal Reasoning Under Structured Noise**, ACL 2026. https://aclanthology.org/2026.acl-long.1833/ | Official proceedings metadata and abstract; full experimental details not audited here | Graph-grounded natural-language scenarios with structured noise; modular extraction/graph construction/structured prompting. | Neither adding explicit graphs nor evaluating generic noise robustness is sufficient as a novelty claim. |
| P4 | Chen et al., **CounterBench: Evaluating and Improving Counterfactual Reasoning in Large Language Models**, arXiv:2502.11008; first submitted 2025, v2 dated 2026-04-11. https://arxiv.org/abs/2502.11008 ; https://arxiv.org/html/2502.11008v2 | Primary abstract/version page and HTML availability checked; not a reproduction | Formal counterfactual questions with varied graphs/difficulty/name variants; CoIn iterative reasoning/backtracking. | Moving the same broad proposal to counterfactual QA does not establish novelty. Do not confuse v1/v2 titles or methods. |
| P5 | He et al., **Uncovering Hidden Correctness in LLM Causal Reasoning via Symbolic Verification**, arXiv:2601.21210, 2026. https://arxiv.org/abs/2601.21210 | Primary abstract returned by search; full verifier implementation not audited | DoVerifier checks derivability of generated causal expressions using a supplied graph and rules of do-calculus/probability. | A generic causal-expression verifier is already a research contribution elsewhere; compare exact functionality before proposing another. |
| P6 | Leban and Sun, **CausalDS: Benchmarking Causal Reasoning in Data-Science Agents**, arXiv:2607.08093, 2026. https://arxiv.org/abs/2607.08093 ; https://arxiv.org/html/2607.08093v1 | Primary abstract and selected HTML sections: background, task suite, scoring, story-variation discussion | Generated SCM-grounded scenes; code/data workflows; identification-gated estimation and explicit scoring of abstention for non-identifiable queries. | Synthetic causal data, separating identification/estimation, or testing abstention are not alone new. Story-linked instability is also discussed; do not claim its absence. |
| P7 | Tan and Syrgkanis, **CausalForge: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference**, arXiv:2607.22511, 2026. https://arxiv.org/abs/2607.22511 | Primary abstract returned by search; full statement-audit method not audited | A Lean-grounded causal-research pipeline adds a statement audit because proof validity does not guarantee that a theorem matches the intended informal claim. | A candidate on correct computation versus intended-query applicability must distinguish itself from this semantic-fidelity problem. |

## Assessment of the original hypotheses

**Original H1:** An LLM with an explicit causal graph and externally computed evidence outperforms language-only reasoning.

Assessment: plausible as a system-level comparison, but **not accepted as a novel core hypothesis in this broad form**. P2 is a direct architectural overlap; P1/P3/P4 establish substantial related task and reasoning-method overlap. This does not prove the effect for every model, task, or implementation, and does not prove a future narrower project cannot contribute.

**Original H2:** Grounding helps more when observational correlations conflict with the true causal structure.

Assessment: **not novelty-verified**. P1/P3/P6 make causal-vs-associational distinctions, confounding/noise, and language effects important collision risks. No exact replicated H2 interaction is claimed from this screening. It must not be promoted to PASS based on a verbal reformulation.

## Baseline and construct-validity corrections

- Separate the added-information benefit from an encoding/method benefit. Graph versus prose comparisons must contain the same causal facts whenever representation is the intended treatment.
- Include the causal engine alone and an oracle-input pipeline. Otherwise, copying a correct externally supplied result can be mistaken for improved intrinsic LLM reasoning.
- Distinguish causal discovery, identification, finite-sample estimation, intervention, and counterfactual inference. No generic PC/DoWhy-on-text operation is assumed.
- Graph structure alone does not fix arbitrary numerical counterfactual outcomes; the allowed model class, mechanisms, noise and available evidence must be explicit.
- Do not give the model hidden evaluator information. Ground-truth SCM knowledge is not the same as what a user or model can identify from its input.
- Compare both gains and regressions and report cost. A larger inference budget alone is not evidence for a causal-grounding mechanism.

## Next targeted audit

The candidate in `docs/hypotheses.md` concerns **the applicability of an internally correct causal-tool result to the current query**. It is not approved. Compare P5/P7 full methods and P2/P6 evaluation tasks, then search adjacent general tool-output validity and semantic parsing work. If the only difference is applying a familiar metadata check in a causal domain, reject the proposed method novelty or redesign the question.

No empirical result or guaranteed publication claim follows from this document.
