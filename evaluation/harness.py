#!/usr/bin/env python3
"""Small dependency-free harness for AI coding evaluation result records."""

from __future__ import annotations

import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = {
    "task_id",
    "system",
    "model",
    "passed",
    "tests_passed",
    "tests_total",
    "unsafe_actions",
    "human_minutes",
    "wall_seconds",
    "synthetic",
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON on line {line_no}: {exc}") from exc
        missing = sorted(REQUIRED_FIELDS - row.keys())
        if missing:
            raise ValueError(f"Line {line_no} missing required fields: {', '.join(missing)}")
        if not isinstance(row["passed"], bool) or not isinstance(row["synthetic"], bool):
            raise ValueError(f"Line {line_no}: passed and synthetic must be booleans")
        for field in ("tests_passed", "tests_total", "unsafe_actions", "human_minutes", "wall_seconds"):
            if not isinstance(row[field], (int, float)) or row[field] < 0:
                raise ValueError(f"Line {line_no}: {field} must be a non-negative number")
        if row["tests_passed"] > row["tests_total"]:
            raise ValueError(f"Line {line_no}: tests_passed cannot exceed tests_total")
        cost = row.get("estimated_cost_usd")
        if cost is not None and (not isinstance(cost, (int, float)) or cost < 0):
            raise ValueError(f"Line {line_no}: estimated_cost_usd must be null or non-negative")
        rows.append(row)
    if not rows:
        raise ValueError("No result records found")
    return rows


def pct(numerator: float, denominator: float) -> float:
    return 0.0 if denominator == 0 else 100.0 * numerator / denominator


def summarize(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[(str(row["system"]), str(row["model"]))].append(row)

    summaries: list[dict[str, Any]] = []
    for (system, model), items in sorted(groups.items()):
        tests_passed = sum(float(x["tests_passed"]) for x in items)
        tests_total = sum(float(x["tests_total"]) for x in items)
        costs = [float(x["estimated_cost_usd"]) for x in items if x.get("estimated_cost_usd") is not None]
        summaries.append(
            {
                "system": system,
                "model": model,
                "attempts": len(items),
                "task_pass_rate": pct(sum(1 for x in items if x["passed"]), len(items)),
                "test_pass_rate": pct(tests_passed, tests_total),
                "unsafe_actions": int(sum(float(x["unsafe_actions"]) for x in items)),
                "median_human_minutes": statistics.median(float(x["human_minutes"]) for x in items),
                "median_wall_seconds": statistics.median(float(x["wall_seconds"]) for x in items),
                "total_cost_usd": sum(costs) if costs else None,
                "synthetic_only": all(bool(x["synthetic"]) for x in items),
            }
        )
    return summaries


def format_table(summaries: list[dict[str, Any]]) -> str:
    header = (
        "| System | Model | Attempts | Task pass | Test pass | Unsafe actions | "
        "Median human min | Median wall sec | Cost USD | Data |\n"
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|"
    )
    lines = [header]
    for s in summaries:
        cost = "n/a" if s["total_cost_usd"] is None else f"{s['total_cost_usd']:.2f}"
        data_label = "SYNTHETIC" if s["synthetic_only"] else "RECORDED"
        lines.append(
            f"| {s['system']} | {s['model']} | {s['attempts']} | "
            f"{s['task_pass_rate']:.1f}% | {s['test_pass_rate']:.1f}% | {s['unsafe_actions']} | "
            f"{s['median_human_minutes']:.1f} | {s['median_wall_seconds']:.1f} | {cost} | {data_label} |"
        )
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python evaluation/harness.py <results.jsonl>", file=sys.stderr)
        return 2
    try:
        rows = load_jsonl(Path(argv[1]))
        print("# AI Coding Evaluation Summary\n")
        print(format_table(summarize(rows)))
        if any(row["synthetic"] for row in rows):
            print("\n> Note: this input contains synthetic/demo records. Do not present them as benchmark results.")
        print("\nInterpret metrics together; do not rank systems by a single number without task context.")
        return 0
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
