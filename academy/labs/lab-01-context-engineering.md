# Lab 01 — Context Engineering

**Level:** Beginner → Intermediate  
**Time:** ~30–45 minutes  
**Goal:** Learn why giving *more* context is not always better, and how to provide the *right* context for an AI coding task.

## Scenario

You maintain a small API. A user reports:

> “The `/discount` endpoint sometimes returns negative prices. Fix it and add tests.”

An inexperienced AI workflow might paste the whole repository into a model and ask it to “fix the bug.” A stronger workflow first identifies the smallest useful context.

## Step 1 — Predict before asking AI

Before using any assistant, answer:

1. Which files are most likely relevant?
2. What behavior should never happen?
3. What edge cases might produce negative values?
4. What test would prove the bug is fixed?

Write your answers down. Prediction forces you to form a mental model before delegating.

## Step 2 — Compare three prompts

### Prompt A — vague

```text
Fix the discount bug.
```

### Prompt B — overloaded

```text
Here is my entire repository. Find anything wrong, fix the discount bug,
refactor the project, improve security, and add tests.
```

### Prompt C — bounded context

```text
Task: Fix the /discount endpoint so the final price can never be negative.

Inspect these files first:
- src/discount.ts
- src/routes/discount.ts
- tests/discount.test.ts

Requirements:
- Preserve the existing API response shape.
- A discount larger than the original price must produce 0, never a negative value.
- Existing valid discount behavior must remain unchanged.
- Add regression tests for the failing edge case.

Before editing, explain the likely root cause and the files you expect to change.
After editing, run the relevant tests and summarize the evidence.
```

## Step 3 — Analyze the difference

Prompt C is stronger because it gives the agent:

- a clear objective;
- the likely context boundary;
- invariant behavior (`price >= 0`);
- compatibility constraints;
- a regression-test requirement;
- a required inspect-before-edit step;
- an explicit verification step.

The goal is **not maximum context**. The goal is **minimum sufficient context plus strong feedback**.

## Step 4 — Build the verification oracle

For this task, the strongest simple oracle is executable:

```text
Given originalPrice >= 0 and discount >= 0,
finalPrice must always be >= 0.
```

Useful tests include:

```text
price=100, discount=20  -> 80
price=100, discount=100 -> 0
price=100, discount=150 -> 0
price=0, discount=10    -> 0
```

An AI explanation is *not* the oracle. Passing tests implementing the invariant provide much stronger evidence.

## Step 5 — Context budget exercise

Classify each item as **Must provide**, **Useful if needed**, or **Noise** for this bug:

- discount calculation function;
- route handler;
- existing discount tests;
- README logo assets;
- unrelated database migration files;
- package test command;
- coding conventions;
- full Git history;
- failing stack trace or reproduction input.

### Suggested answer

**Must provide / inspect:** calculation logic, route behavior if transformation happens there, tests, reproduction input.  
**Useful if needed:** test command, coding conventions, adjacent types.  
**Usually noise:** logo assets, unrelated migrations, full Git history.

## Step 6 — Upgrade the prompt yourself

Rewrite Prompt C for one of these tasks:

1. A login form accepts an invalid email.
2. A React component rerenders excessively.
3. A Python CSV parser crashes on empty files.
4. A database migration is too slow.

Your prompt should contain:

- task;
- relevant files or discovery instruction;
- constraints;
- acceptance criteria;
- verification command or evidence;
- explicit instruction to avoid unrelated edits.

## Knowledge check

1. Why can dumping an entire repository into context reduce quality?
2. What is an invariant?
3. Why should the agent inspect before editing?
4. What is stronger evidence: “the model says the fix works” or a regression test?
5. When should you expand the context boundary?

## Completion criteria

You have completed this lab when you can explain this principle in your own words:

> **Good context engineering gives the model enough information to reason correctly while keeping scope, permissions, and verification explicit.**

## Further reading

- Repository playbook: [`../../playbooks/agentic-workflow.md`](../../playbooks/agentic-workflow.md)
- Verification guide: [`../../playbooks/verification-first.md`](../../playbooks/verification-first.md)
- Security model: [`../../security/agent-safety.md`](../../security/agent-safety.md)
