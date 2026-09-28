"""Unit tests for exact mathematical construction; no model inference."""
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_research_fixtures.py"
SPEC = importlib.util.spec_from_file_location("fixtures", PATH)
fx = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fx)


class TestConstruction(unittest.TestCase):
    def test_full_report(self):
        report = fx.validate()
        self.assertEqual(len(report["r3"]), 12)
        self.assertEqual(len(report["r2"]), 10)
        self.assertEqual(report["analytic_grid_pairs"], 121)
        self.assertEqual(report["llm_calls"], 0)

    def test_two_world_witnesses(self):
        rows = fx.response_constraints("3/10", "2/5")
        for world in [(F(3, 5), 0, F(1, 10), F(3, 10)),
                      (F(3, 10), F(3, 10), F(2, 5), 0)]:
            self.assertTrue(all(sum(a*b for a,b in zip(c, world)) == r for c,r in rows))

    def test_entire_interval_attainable(self):
        # Constructive proof family, not just two endpoint examples.
        for i in range(31):
            q = F(i, 100)
            world = (F(3, 5)-q, q, F(1, 10)+q, F(3, 10)-q)
            self.assertTrue(all(p >= 0 for p in world))
            self.assertEqual(sum(world), 1)
            self.assertEqual(world[1] + world[3], F(3, 10))
            self.assertEqual(world[2] + world[3], F(2, 5))

    def test_monotonicity_control(self):
        self.assertEqual(fx.pns_bounds("3/5", "3/10", True), (F(3,10), F(3,10)))

    def test_contradictory_assumptions(self):
        self.assertIsNone(fx.pns_bounds("3/10", "3/5", True))

    def test_redundant_constraint(self):
        rows = fx.response_constraints("3/10", "2/5")
        self.assertEqual(fx.vertices(rows), fx.vertices(rows + [rows[-1]]))

    def test_probability_validation(self):
        for invalid in ["-1/10", "11/10", 0.3, True]:
            with self.assertRaises(ValueError):
                fx.prob_value(invalid)

    def test_query_validation(self):
        for intervention, evidence in [({"W":1}, {}), ({"X":2}, {}),
                                       ({"X":True}, {}), ({"X":1}, {"X":0})]:
            with self.assertRaises(ValueError):
                fx.outcome("fork", intervention, evidence)

    def test_unknown_model(self):
        with self.assertRaises(ValueError):
            fx.outcome("not_a_model", {}, {})

    def test_fork_distinguishes_observation_intervention(self):
        self.assertEqual(fx.outcome("fork", {}, {"X":1}), F(9,10))
        self.assertEqual(fx.outcome("fork", {"X":1}, {}), F(1,2))

    def test_randomized_exchange(self):
        self.assertEqual(fx.outcome("randomized", {}, {"X":1}),
                         fx.outcome("randomized", {"X":1}, {}))

    def test_scope_numerical_tie_is_not_primary(self):
        report = fx.validate()
        tie = next(r for r in report["r2"] if r["id"] == "r2_09")
        self.assertEqual(tie["target_value"], tie["tool_value"])
        self.assertFalse(tie["primary_eligible"])


if __name__ == "__main__":
    unittest.main()
