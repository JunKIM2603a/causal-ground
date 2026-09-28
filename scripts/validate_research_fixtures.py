#!/usr/bin/env python3
"""CPU-only exact fixtures for CausalGround session 01; NOT LLM experiments.

No external dependencies. Continuous binary response-type probabilities, not
an empirical sample/grid of possible worlds. No general do-calculus engine.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
from typing import Iterable

Row = tuple[tuple[F, ...], F]
Point = tuple[F, ...]


def prob_value(value: str | int | F) -> F:
    if isinstance(value, (float, bool)):
        raise ValueError("Use exact integer/fraction/decimal strings, not floats/bools")
    v = F(value)
    if not 0 <= v <= 1:
        raise ValueError("Probability must lie in [0,1]")
    return v


def unique_solution(rows: list[Row], n: int = 4) -> Point | None:
    """Exact Gaussian elimination; None means inconsistent or non-unique."""
    a = [list(map(F, c)) + [F(b)] for c, b in rows]
    if any(len(row) != n + 1 for row in a):
        raise ValueError("Wrong constraint dimension")
    pivot_cols: list[int] = []
    r = 0
    for col in range(n):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        d = a[r][col]
        a[r] = [x / d for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][col]:
                d = a[i][col]
                a[i] = [x - d * y for x, y in zip(a[i], a[r])]
        pivot_cols.append(col)
        r += 1
    if any(not any(row[:n]) and row[n] for row in a) or r < n:
        return None
    answer = [F(0)] * n
    for i, col in enumerate(pivot_cols):
        answer[col] = a[i][n]
    return tuple(answer)


def vertices(rows: list[Row]) -> list[Point]:
    """Enumerate ALL vertices of {p>=0: A p=b}, for a bounded 4-atom simplex.

    Every vertex has enough active zero coordinates for a unique solution.
    Enumerating all zero-coordinate subsets therefore covers degeneracy too.
    """
    found: set[Point] = set()
    for size in range(5):
        for zeros in combinations(range(4), size):
            active = rows + [(tuple(F(int(j == i)) for j in range(4)), F(0))
                             for i in zeros]
            v = unique_solution(active)
            if v is not None and all(x >= 0 for x in v):
                if all(sum(c * x for c, x in zip(cs, v)) == b for cs, b in rows):
                    found.add(v)
    return sorted(found)


def response_constraints(p1: str | F, p0: str | F | None = None,
                         monotone: bool = False) -> list[Row]:
    # Atom order: (Y0,Y1) = 00, 01, 10, 11. Target PNS is atom 01.
    rows: list[Row] = [((F(1),) * 4, F(1)),
                       ((F(0), F(1), F(0), F(1)), prob_value(p1))]
    if p0 is not None:
        rows.append(((F(0), F(0), F(1), F(1)), prob_value(p0)))
    if monotone:
        rows.append(((F(0), F(0), F(1), F(0)), F(0)))
    return rows


def pns_bounds(p1: str | F, p0: str | F | None = None,
               monotone: bool = False) -> tuple[F, F] | None:
    vs = vertices(response_constraints(p1, p0, monotone))
    return (min(v[1] for v in vs), max(v[1] for v in vs)) if vs else None


# Six primary construction examples; controls below are NOT primary H1 items.
R3_CASES = [
    ("r3_01", "1/10", "1/5", False, "invariant", ("0", "1/10")),
    ("r3_02", "1/5", "3/10", False, "invariant", ("0", "1/5")),
    ("r3_03", "3/10", "2/5", False, "invariant", ("0", "3/10")),
    ("r3_04", "2/5", "1/2", False, "invariant", ("0", "2/5")),
    ("r3_05", "1/4", "13/20", False, "invariant", ("0", "1/4")),
    ("r3_06", "1/2", "1/2", False, "invariant", ("0", "1/2")),
    ("r3_07", "3/5", "3/10", False, "narrower", ("3/10", "3/5")),
    ("r3_08", "3/10", "4/5", False, "narrower", ("0", "1/5")),
    ("r3_09", "3/10", "0", False, "point", ("3/10", "3/10")),
    ("r3_10", "3/5", "3/10", True, "point", ("3/10", "3/10")),
    ("r3_11", "3/10", "3/5", True, "inconsistent", None),
    ("r3_12", "0", "2/5", False, "point", ("0", "0")),
]


# Model: Z~Bernoulli(pz); X~Bernoulli(ax[Z]); Y~Bernoulli(by[X][Z]).
# Independent exogenous noises, fully specified population probabilities.
MODELS = {
    "fork": ("1/2", ("1/10", "9/10"), (("0", "1"), ("0", "1"))),
    "randomized": ("1/2", ("1/2", "1/2"), (("1/5", "1/5"), ("4/5", "4/5"))),
    "modifier": ("1/2", ("1/2", "1/2"), (("1/10", "2/5"), ("1/5", "9/10"))),
    "tie": ("1/2", ("1/5", "3/5"), (("1/10", "9/10"), ("3/5", "3/5"))),
}


def outcome(model: str, intervention: dict[str, int], evidence: dict[str, int]) -> F:
    if model not in MODELS:
        raise ValueError("Unknown fixture model")
    for d in (intervention, evidence):
        if any(k not in {"X", "Z"} or type(v) is not int or v not in (0, 1)
               for k, v in d.items()):
            raise ValueError("Only binary X/Z are supported")
    if any(k in evidence and evidence[k] != v for k, v in intervention.items()):
        raise ValueError("Contradictory intervention and evidence")
    pz, ax, by = MODELS[model]
    numerator = denominator = F(0)
    for z, x in product((0, 1), repeat=2):
        state = {"Z": z, "X": x}
        if any(state[k] != v for k, v in intervention.items()):
            continue
        if any(state[k] != v for k, v in evidence.items()):
            continue
        weight = F(1)
        for name, value, p in (("Z", z, pz), ("X", x, ax[z])):
            if name not in intervention:
                pp = prob_value(p)
                weight *= pp if value else 1 - pp
        denominator += weight
        numerator += weight * prob_value(by[x][z])
    if not denominator:
        raise ValueError("Zero-probability conditioning event")
    return numerator / denominator


# Query = (interventions, evidence). Reference scope labels are fixture-specific;
# the numerical evaluator does NOT implement a general semantic verifier.
R2_CASES = [
    ("r2_01", "fork", ({"X": 1}, {}), ({}, {"X": 1}), "1/2", "9/10", "mismatch"),
    ("r2_02", "fork", ({}, {"X": 1}), ({"X": 1}, {}), "9/10", "1/2", "mismatch"),
    ("r2_03", "fork", ({"X": 0}, {}), ({}, {"X": 0}), "1/2", "1/10", "mismatch"),
    ("r2_04", "fork", ({"X": 1}, {}), ({"X": 1}, {}), "1/2", "1/2", "same_query"),
    ("r2_05", "randomized", ({"X": 1}, {}), ({}, {"X": 1}), "4/5", "4/5", "valid_exchange"),
    ("r2_06", "randomized", ({"X": 1}, {}), ({"X": 1, "Z": 1}, {}), "4/5", "4/5", "irrelevant_intervention"),
    ("r2_07", "modifier", ({"X": 1}, {}), ({"X": 1}, {"Z": 1}), "11/20", "9/10", "mismatch"),
    ("r2_08", "randomized", ({"X": 1}, {}), ({"X": 0}, {}), "4/5", "1/5", "mismatch"),
    ("r2_09", "tie", ({"X": 1}, {}), ({}, {"X": 1}), "3/5", "3/5", "numeric_tie_excluded"),
    ("r2_10", "fork", ({"X": 1}, {}), ({"X": 0}, {}), "1/2", "1/2", "no_causal_effect"),
]


def json_safe(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(k): json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(v) for v in value]
    return value


def validate() -> dict:
    r3 = []
    for item, p1, p0, monotone, kind, expected in R3_CASES:
        base = pns_bounds(p1)
        expanded = pns_bounds(p1, p0, monotone)
        gold = tuple(map(F, expected)) if expected is not None else None
        if expanded != gold:
            raise AssertionError((item, expanded, gold))
        old_vertices = vertices(response_constraints(p1))
        new_rows = response_constraints(p1, p0, monotone)
        removed = [v for v in old_vertices if any(
            sum(a * b for a, b in zip(c, v)) != rhs for c, rhs in new_rows)]
        if kind == "invariant" and not (base == expanded and base[0] < base[1] and removed):
            raise AssertionError("Invalid nonredundant invariant fixture")
        r3.append(dict(id=item, role=kind, p1=F(p1), p0=F(p0), monotone=monotone,
                       base_bounds=base, expanded_bounds=expanded,
                       removed_old_vertex=removed[0] if removed else None,
                       expanded_vertices=vertices(new_rows)))
    # Independent analytic formula vs exact vertex enumeration, incl. boundaries.
    checked = 0
    for a, b in product(range(11), repeat=2):
        p1, p0 = F(a, 10), F(b, 10)
        expected = (max(F(0), p1 - p0), min(p1, 1 - p0))
        if pns_bounds(p1, p0) != expected:
            raise AssertionError("Sharp-bound formula mismatch")
        checked += 1
    r2 = []
    for item, model, target, tool, tg, sr, scope in R2_CASES:
        target_value, tool_value = outcome(model, *target), outcome(model, *tool)
        if (target_value, tool_value) != (F(tg), F(sr)):
            raise AssertionError((item, target_value, tool_value))
        primary = scope == "mismatch"
        if primary and target_value == tool_value:
            raise AssertionError("Primary mismatch cannot have a numerical tie")
        r2.append(dict(id=item, model=model, target=target, tool=tool,
                       target_value=target_value, tool_value=tool_value,
                       computation_correct_for_declared_query=True,
                       reference_scope=scope, primary_eligible=primary))
    return json_safe(dict(status="CONSTRUCTION_CHECKS_PASS_NOT_H1_EVIDENCE",
                          source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                          python=platform.python_version(), llm_calls=0, gpu_experiments=0,
                          model_experiments=False, oracle="exact_fraction_vertex_enumeration",
                          analytic_grid_pairs=checked, r3=r3, r2=r2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    report = json.dumps(validate(), ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w" if args.overwrite else "x", encoding="utf-8") as out:
            out.write(report)
        print(f"Wrote {args.output}; mathematical construction checks only.")
    else:
        print(report, end="")


if __name__ == "__main__":
    main()
