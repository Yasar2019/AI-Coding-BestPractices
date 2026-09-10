# AI Coding Academy

The Academy turns this repository into a structured, practice-first learning system.

## Philosophy

AI coding is not a single skill. Strong practitioners combine software engineering fundamentals, context design, agent/tool orchestration, verification, security, evaluation, and judgment about when *not* to use AI.

Every module follows the same loop:

> **Learn → Predict → Try → Verify → Reflect**

## Curriculum map

| Level | Module | Outcome |
|---|---|---|
| 0 | Foundations | Understand what coding assistants and agents can/cannot do |
| 1 | Context Engineering | Give an agent the smallest sufficient context for reliable work |
| 2 | Verification | Convert requirements into executable evidence |
| 3 | Agentic Workflows | Run reproduce-inspect-plan-edit-test-review loops |
| 4 | Security | Bound tools, secrets, network and destructive actions |
| 5 | Evaluation | Compare models/agents on representative tasks |
| 6 | Team Systems | Build governed workflows for shared repositories |
| 7 | Advanced Agent Design | Decomposition, subagents, memory, tools and recovery strategies |

## Current labs

1. [Lab 01 — Context Engineering](labs/lab-01-context-engineering.md)
2. [Lab 02 — Verification Engineering](labs/lab-02-verification-engineering.md)
3. [Lab 03 — Agentic Debugging](labs/lab-03-agentic-debugging.md)

Labs 02 and 03 include runnable Python exercises with intentional defects. The goal is not to guess the fix from the prose; the goal is to practice using specifications, tests, falsifiable hypotheses, and diff review as evidence.

## Run the exercises

```bash
cd academy/exercises/order_total
python -m unittest -v

cd ../retry_helper
python -m unittest -v
```

The initial failures are intentional. Learners should repair the implementation **without weakening the tests**.

## Interactive Academy

Open [academy/index.html](index.html) for the browser-based Academy experience. It includes:

- module navigation;
- local progress tracking;
- verification-focused knowledge checks;
- debugging score guidance;
- direct links to runnable labs.

Progress is stored locally in the browser; there is no account or backend dependency.

## Scoring model

The Academy uses four dimensions:

- **Correctness** — does the implementation satisfy the specification?
- **Evidence** — is there independent verification?
- **Safety** — was the blast radius appropriately controlled?
- **Understanding** — can the learner explain the change and trade-offs?

For debugging exercises, also score the process: reproduce first, form a falsifiable hypothesis, patch minimally, run regressions, and inspect the final diff.

## What comes next

Future phases will add secure tool-use simulations, repository-scale refactoring exercises, model/agent evaluation harnesses, benchmark experiments, multi-agent decomposition labs, richer progress tracking, and eventually a public Academy website.
