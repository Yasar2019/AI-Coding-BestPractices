import json
import tempfile
import unittest
from pathlib import Path

from evaluation.harness import load_jsonl, summarize


class HarnessTests(unittest.TestCase):
    def write_rows(self, rows):
        handle = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=False)
        with handle:
            for row in rows:
                handle.write(json.dumps(row) + "\n")
        return Path(handle.name)

    def base_row(self, **overrides):
        row = {
            "task_id": "t1",
            "system": "agent-a",
            "model": "model-a",
            "passed": True,
            "tests_passed": 4,
            "tests_total": 4,
            "unsafe_actions": 0,
            "human_minutes": 2.0,
            "wall_seconds": 10.0,
            "estimated_cost_usd": 0.1,
            "synthetic": False,
        }
        row.update(overrides)
        return row

    def test_loads_valid_rows(self):
        path = self.write_rows([self.base_row()])
        rows = load_jsonl(path)
        self.assertEqual(len(rows), 1)
        self.assertTrue(rows[0]["passed"])

    def test_rejects_impossible_test_counts(self):
        path = self.write_rows([self.base_row(tests_passed=5, tests_total=4)])
        with self.assertRaises(ValueError):
            load_jsonl(path)

    def test_rejects_missing_required_field(self):
        row = self.base_row()
        del row["wall_seconds"]
        path = self.write_rows([row])
        with self.assertRaises(ValueError):
            load_jsonl(path)

    def test_summary_keeps_metrics_separate(self):
        rows = [
            self.base_row(),
            self.base_row(task_id="t2", passed=False, tests_passed=2, human_minutes=6.0, wall_seconds=20.0),
        ]
        summary = summarize(rows)[0]
        self.assertEqual(summary["attempts"], 2)
        self.assertEqual(summary["task_pass_rate"], 50.0)
        self.assertEqual(summary["test_pass_rate"], 75.0)
        self.assertEqual(summary["median_human_minutes"], 4.0)
        self.assertEqual(summary["unsafe_actions"], 0)

    def test_summary_labels_synthetic_only(self):
        rows = [self.base_row(synthetic=True)]
        self.assertTrue(summarize(rows)[0]["synthetic_only"])


if __name__ == "__main__":
    unittest.main()
