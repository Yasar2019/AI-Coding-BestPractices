# 10-Minute Quickstart

Welcome to the **AI Coding Best Practices Public Preview**.

You do not need to read the whole repository to get value from it. Use this path first.

## Minute 0–2 — Learn the core rule

AI-generated code is a **hypothesis**, not proof.

A reliable workflow looks like:

```text
Understand → Plan → Implement → Verify → Review → Measure → Learn
```

Read the short [AI Coding Cheat Sheet](AI_CHEATSHEET.md).

## Minute 2–5 — Try the interactive tools

Open locally in your browser:

- [`dashboard/index.html`](dashboard/index.html) — task-risk classifier, workflow maturity, research radar;
- [`academy/index.html`](academy/index.html) — interactive learning checks and Academy progress.

Both are dependency-free static pages.

## Minute 5–8 — Run a real exercise

Clone the repository and try the verification lab:

```bash
git clone https://github.com/Yasar2019/AI-Coding-BestPractices.git
cd AI-Coding-BestPractices/academy/exercises/order_total
python -m unittest -v
```

The starter implementation is intentionally incorrect.

Your job is to:

1. read the specification in [Lab 02](academy/labs/lab-02-verification-engineering.md);
2. reproduce the failures;
3. make the smallest causal fix;
4. rerun the tests;
5. inspect your diff.

Do not weaken the tests to make the exercise pass.

## Minute 8–10 — Evaluate your own AI workflow

From the repository root:

```bash
python evaluation/harness.py evaluation/sample_results.jsonl
```

The bundled results are **synthetic demo data**. The point is the evaluation format: task success, tests, unsafe actions, human effort, latency, and cost are reported separately.

Then read [Lab 07 — Evaluation Engineering](academy/labs/lab-07-evaluation-engineering.md) and replace the demo records with your own runs.

## Pick your next path

- **New to AI coding:** [START_HERE.md](START_HERE.md)
- **Daily developer:** [Agentic Workflow](playbooks/agentic-workflow.md)
- **Security-minded:** [Agent Safety](security/agent-safety.md) + Labs 04–06
- **Tech lead / manager:** [Team Operating Model](playbooks/team-operating-model.md)
- **Research / advanced:** [2026 Research Landscape](research/2026-landscape.md) + [Benchmark Literacy](benchmarks/README.md)

## Public preview status

This project is useful today but still evolving. See [ROADMAP.md](ROADMAP.md) for what is complete, in progress, and planned.

If you find an incorrect claim, broken lab, missing source, or better workflow pattern, contributions are welcome through [CONTRIBUTING.md](CONTRIBUTING.md).
