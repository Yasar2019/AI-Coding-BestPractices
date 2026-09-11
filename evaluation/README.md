# Evaluation Engineering

AI coding tools should be evaluated on **your work**, under a reproducible configuration, with metrics that distinguish capability from cost, safety, and review burden.

This directory contains a small, dependency-free evaluation harness that can be used by an individual developer or a team.

## What this measures

The harness keeps these signals separate:

| Signal | Why it matters |
|---|---|
| Task success | Did the system satisfy the acceptance criteria? |
| Test evidence | How much of the executable verification passed? |
| Safety events | Did the run attempt a disallowed or high-risk action? |
| Human minutes | How much intervention/review did the run require? |
| Wall time | How long did the attempt take? |
| Estimated cost | What did the attempt cost, if known? |

A system that solves 90% of tasks with heavy human repair is different from one that solves 85% with almost no intervention. A single score can hide that difference.

## Included task suite

`tasks.json` defines a starter suite based on Academy exercises:

- specification-boundary bug fixing;
- retry/control-flow debugging;
- trust-boundary and least-privilege review.

These tasks are intentionally small. They demonstrate methodology, not a claim about the global ranking of any model or agent.

## Run the demo

From the repository root:

```bash
python evaluation/harness.py evaluation/sample_results.jsonl
```

The sample results are **synthetic demonstration data**. Replace them with records from your own runs.

Run harness tests:

```bash
python -m unittest evaluation/test_harness.py -v
```

## Result format

One JSON object per line:

```json
{
  "task_id": "order-total-boundaries",
  "system": "my-agent-config",
  "model": "model-version",
  "passed": true,
  "tests_passed": 6,
  "tests_total": 6,
  "unsafe_actions": 0,
  "human_minutes": 4.5,
  "wall_seconds": 52.1,
  "estimated_cost_usd": 0.18,
  "synthetic": false,
  "notes": "Minimal patch; all regression tests passed"
}
```

## Reproducibility checklist

Record, at minimum:

- exact model/version;
- agent or harness version;
- repository commit;
- task text/version;
- available tools and permissions;
- network access policy;
- retry budget;
- context/repository instructions;
- verification commands;
- whether the run was interactive or autonomous.

Without this metadata, a benchmark number is often difficult to interpret or reproduce.

## Benchmark literacy

Public benchmarks are useful, but they answer a specific question under a specific harness and dataset. In 2026, benchmark design itself is an active research topic: task validity, contamination, execution environments, task-demand differences, and agent scaffolding can materially change conclusions.

Recommended reading:

- SWE-bench: https://www.swebench.com/
- OpenAI, *Separating signal from noise in coding evaluations* (2026): https://openai.com/index/separating-signal-from-noise-coding-evaluations/
- OmniCode (2026): https://arxiv.org/abs/2602.02262
- *What Does an Agentic Software Engineering Benchmark Measure?* (2026): https://arxiv.org/abs/2609.01271
- Repository guide: [../benchmarks/README.md](../benchmarks/README.md)

## Evaluation principle

> **Use public benchmarks to understand capability trends. Use internal representative tasks to make deployment decisions.**
