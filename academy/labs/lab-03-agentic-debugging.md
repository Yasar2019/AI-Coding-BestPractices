# Lab 03 — Agentic Debugging

## Goal

Practice a disciplined debugging loop where the agent must **reproduce before patching**.

## Debugging protocol

Use this order:

```text
REPRODUCE → LOCALIZE → HYPOTHESIZE → TEST HYPOTHESIS → PATCH → REGRESS
```

Skipping directly to patching is one of the easiest ways for an AI coding agent to produce plausible but unrelated edits.

## Scenario

A retry helper is supposed to call a flaky operation up to `max_attempts` times and return immediately when it succeeds. If all attempts fail, it should re-raise the final exception.

The implementation in [`../exercises/retry_helper/retry_helper.py`](../exercises/retry_helper/retry_helper.py) contains intentional defects.

## Step 1 — Reproduce

```bash
cd academy/exercises/retry_helper
python -m unittest -v
```

Do not modify anything yet. Record:

- which tests fail;
- the observed output or exception;
- whether failures share one root cause.

## Step 2 — Localize

Ask the agent to identify the smallest region of code that can explain the failure. A good debugging agent should inspect the implementation and tests before proposing edits.

Example instruction:

```text
Run the failing tests first. Do not edit yet.
For each failure, identify the smallest code path that could explain it.
State your hypothesis and what observation would falsify it.
Only then propose a minimal patch.
```

The falsification requirement matters. It pushes the agent away from storytelling and toward testable reasoning.

## Step 3 — Patch minimally

Constraints:

- preserve `retry(operation, max_attempts)`;
- do not add dependencies;
- do not catch `BaseException`;
- do not call the operation after it has succeeded;
- do not suppress the final failure.

## Step 4 — Regress

After the patch:

```bash
python -m unittest -v
```

Then inspect the diff. A green suite does not justify unrelated refactoring.

## Advanced challenge

Add one test that verifies `max_attempts=1` performs exactly one call. Then decide what should happen for `max_attempts <= 0`, document that contract, and encode it in a test before implementation.

## Debugging scorecard

Give yourself one point for each:

- reproduced the bug before editing;
- stated a falsifiable hypothesis;
- changed only the causal code path;
- added/preserved regression tests;
- ran the full relevant suite after the patch;
- inspected the final diff.

**6/6** is the target.

## Key lesson

> Debugging quality improves when agents are forced to gather evidence between reasoning steps instead of producing one uninterrupted chain of guesses.
