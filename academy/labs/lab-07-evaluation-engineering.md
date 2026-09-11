# Lab 07 — Evaluation Engineering

**Level:** Intermediate → Advanced  
**Time:** 30–60 minutes  
**Goal:** Build an evaluation that helps you choose an AI coding workflow without hiding trade-offs behind one headline score.

## Scenario

Your team is deciding between two coding-agent configurations. One looks stronger on a public leaderboard. The other seems easier to review on your repository.

Your job is to design an internal evaluation that produces useful evidence.

## Part A — Define representative tasks

Choose 5–15 tasks from real work. Include a mix such as:

- bounded bug fixes;
- test generation;
- code review fixes;
- repository navigation;
- dependency or CI changes;
- security-sensitive review;
- one task where the correct decision may be to stop and ask for approval.

For each task, write explicit acceptance criteria before running an agent.

### Reflection

Why is a random collection of toy coding questions a weak deployment evaluation?

## Part B — Freeze the environment

Record:

- repository commit;
- model/version;
- agent/harness version;
- task text;
- system/repository instructions;
- available tools;
- network policy;
- retry budget;
- human interaction policy;
- verification commands.

If these change, treat the result as a new configuration.

## Part C — Record multidimensional outcomes

Use [`../../evaluation/`](../../evaluation/) and record one JSONL row per attempt.

Do **not** reduce everything to a single score. At minimum compare:

1. task pass rate;
2. executable test evidence;
3. unsafe actions or policy violations;
4. human intervention/review minutes;
5. wall-clock time;
6. cost when available.

## Part D — Run the demo harness

From the repository root:

```bash
python evaluation/harness.py evaluation/sample_results.jsonl
```

The bundled records are explicitly synthetic and exist only to demonstrate the format.

Then duplicate the file and replace it with your own recorded attempts.

## Part E — Interpret the result

Suppose Configuration A has a higher task pass rate but also:

- more unsafe actions;
- twice the review time;
- three times the cost.

Configuration B has slightly lower raw success but is stable and easy to review.

There is no universal winner. Your decision depends on the workload and risk tolerance.

## What good evaluation looks like

A strong evaluation is:

- **representative** of actual work;
- **reproducible** enough to rerun;
- **versioned** when tasks/configurations change;
- **multi-dimensional** rather than leaderboard-only;
- **failure-aware**—it records *how* systems fail;
- **safe**—high-risk behavior counts against a configuration even if the final patch passes tests.

## Current research lesson

Software-engineering evaluation is itself an engineering problem. Benchmark validity, contamination, execution environments, task construction, and harness behavior can change the apparent performance of coding agents. Treat public benchmark numbers as evidence about a particular setup, not timeless properties of a model.

See:

- [Benchmark literacy](../../benchmarks/README.md)
- [Evaluation Engineering](../../evaluation/README.md)
- OpenAI (2026), *Separating signal from noise in coding evaluations*: https://openai.com/index/separating-signal-from-noise-coding-evaluations/
- OmniCode (2026): https://arxiv.org/abs/2602.02262
- Shayanfar et al. (2026), benchmark task-demand profiling: https://arxiv.org/abs/2609.01271

## Completion criteria

You are done when you can explain:

- what your evaluation actually measures;
- what it does **not** measure;
- why its tasks resemble your deployment workload;
- how another person could reproduce the configuration;
- which metrics would make you reject a system even if its pass rate were high.
