# Start Here

AI coding in 2026 is best understood as **software engineering with probabilistic collaborators**. The goal is not to maximize generated code. The goal is to maximize **verified useful work**.

## 1. Learn the mental model

An AI coding system can help with four broad stages:

- **Understand**: explain code, map repositories, summarize requirements.
- **Change**: generate code, refactor, migrate, write tests and documentation.
- **Act**: run commands, inspect logs, use APIs/tools, edit multiple files.
- **Evaluate**: review diffs, test behavior, compare implementations, find risks.

The more autonomy you give a system, the more important environment design, permissions, tests, observability and review become.

## 2. Your first safe workflow

Use this loop on a small real task:

1. State the expected behavior in plain language.
2. Ask the AI to inspect relevant files before editing.
3. Require a short implementation plan.
4. Ask for the smallest coherent change.
5. Run tests, lint, type-checking and the application.
6. Review the diff yourself.
7. Ask the AI to critique its own change against the acceptance criteria.
8. Commit only after you have independent evidence that the behavior is correct.

## 3. Five ideas beginners should learn early

### Context beats clever prompts

Good repository context, examples, conventions and acceptance criteria usually matter more than elaborate role-playing prompts.

### Tests are communication

Tests do more than catch regressions. They tell an agent exactly what “done” means in executable form.

### Agents need boundaries

Do not grant broad file, shell, network or deployment permissions when the task does not require them.

### Generated code has normal software risks

AI output can contain logic bugs, insecure defaults, stale APIs, unnecessary dependencies and licensing concerns. Review it like any other external contribution.

### Benchmarks are not your workflow

A high benchmark score does not guarantee strong performance on your codebase. Build small, representative evaluations for your own tasks.

## 4. Pick your path

- **New to programming?** Start with [`learning-paths/README.md`](learning-paths/README.md).
- **Already coding?** Read [`playbooks/agentic-workflow.md`](playbooks/agentic-workflow.md).
- **Responsible for production systems?** Read [`security/agent-safety.md`](security/agent-safety.md) and [`playbooks/verification-first.md`](playbooks/verification-first.md).
- **Evaluating tools/models?** Read [`benchmarks/README.md`](benchmarks/README.md).
- **Following the science?** Read [`research/2026-landscape.md`](research/2026-landscape.md).

## 5. A practical definition of good AI coding

A good AI coding workflow should improve at least one of these without quietly destroying the others:

- time to working change;
- defect rate;
- maintainability;
- security;
- developer understanding;
- review burden;
- cost;
- reproducibility.

If you only measure lines of code or apparent speed, you are measuring the wrong thing.
