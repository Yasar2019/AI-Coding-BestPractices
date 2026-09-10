# Lab 02 — Verification Engineering

## Goal

Learn to turn an ambiguous natural-language requirement into **executable evidence** before asking an AI agent to implement it.

## Scenario

You maintain an e-commerce helper that computes an order total. The requirement says:

> “Apply a 10% discount for orders of $100 or more.”

That sentence is not enough to safely implement production behavior. You must define what counts toward the threshold, how rounding works, and what happens at exact boundaries.

## Step 1 — Convert prose into invariants

Before editing code, write the behaviors that must always be true:

1. subtotal below 100.00 → no discount;
2. subtotal exactly 100.00 → 10% discount;
3. subtotal above 100.00 → 10% discount;
4. empty cart → total 0.00;
5. negative quantities are rejected;
6. output is rounded to two decimal places.

Notice what happened: the vague feature request became a testable contract.

## Step 2 — Predict failure modes

An AI-generated patch may still:

- use `>` instead of `>=`;
- apply the threshold after tax or shipping;
- round each line item rather than the final total;
- silently accept negative quantities;
- mutate input data;
- add unnecessary dependencies.

The purpose of verification engineering is to make these failures observable.

## Step 3 — Run the exercise

Use the runnable exercise in [`../exercises/order_total/`](../exercises/order_total/).

```bash
cd academy/exercises/order_total
python -m unittest -v
```

The starter implementation is intentionally wrong. Your task is to repair `order_total.py` **without weakening the tests**.

## Step 4 — Ask an AI agent well

A strong request looks like this:

```text
Inspect order_total.py and test_order_total.py.
Do not change the tests unless you first explain why the specification is contradictory.
Fix the implementation with the smallest patch that satisfies the tests.
Preserve the public function signature and avoid new dependencies.
After editing, run: python -m unittest -v
Then summarize the root cause, changed behavior, and verification evidence.
```

Why is this stronger than “fix the bug”?

- scope is bounded;
- tests act as an executable contract;
- the agent cannot quietly redefine success;
- dependencies and API changes are constrained;
- a concrete verification command is mandatory.

## Step 5 — Review the diff

Passing tests are necessary, not sufficient. Inspect whether the patch:

- is smaller than needed;
- duplicates logic;
- hides behavior behind magic constants;
- changes unrelated code;
- introduces unsafe numeric assumptions.

## Reflection

Answer these before marking the lab complete:

1. Which requirement was most likely to be misunderstood by a model?
2. Which test would catch an off-by-one threshold mistake?
3. What does a passing test suite *not* prove?
4. What additional test would you add for a real payment system?

## Completion standard

You should be able to explain this statement:

> A good AI coding workflow does not merely ask the model for the right answer; it builds an environment where wrong answers are likely to fail visibly.
