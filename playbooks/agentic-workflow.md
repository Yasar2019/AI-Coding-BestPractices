# Agentic Coding Workflow

A coding agent is most useful when it operates inside a **bounded evidence loop**.

## The seven-step loop

### 1. Inspect

Require the agent to inspect the repository structure, relevant code, tests and configuration before making changes.

### 2. Define success

Turn the task into explicit acceptance criteria. Prefer executable criteria: tests, schemas, benchmark thresholds or reproducible commands.

### 3. Plan

Ask for a short implementation plan that identifies files, dependencies, risks and validation steps. Plans should be cheap to revise.

### 4. Implement narrowly

Prefer the smallest coherent patch. Avoid unrelated cleanup unless it is required for correctness.

### 5. Run evidence-producing tools

Examples:

- unit/integration/end-to-end tests;
- type checking;
- linting and formatting;
- static analysis/SAST;
- dependency and secret scanning;
- application runtime checks;
- targeted benchmarks.

### 6. Review the diff

Review what actually changed, not merely the agent's summary. Look for omitted requirements, accidental deletions, hidden behavior changes, dependency additions and security regressions.

### 7. Reflect and improve instructions

When an agent repeatedly makes the same mistake, improve repository instructions, tests, fixtures or tooling rather than repeatedly adding longer prompts.

## A strong task packet

```text
GOAL
What behavior should change?

CONTEXT
Which parts of the repo matter? What conventions already exist?

CONSTRAINTS
APIs, compatibility, performance, security, dependency rules.

ACCEPTANCE CRITERIA
Observable outcomes that define done.

VERIFICATION
Commands/tests that must pass.

BOUNDARIES
What must not be changed? What actions need approval?
```

## Context engineering

Context engineering is the discipline of giving an AI system the right information and tools at the right time. Useful context includes:

- repository architecture and conventions;
- relevant files rather than the entire codebase by default;
- examples of accepted implementations;
- API contracts and schemas;
- failing tests/logs;
- current dependency versions;
- explicit product constraints;
- tool permissions and environmental limits.

Too little context causes guessing. Too much irrelevant context can distract the model, increase cost and hide the important constraints.

## Parallelism: use comparison, not chaos

Parallel agents are useful when tasks are independent or when multiple approaches can be compared objectively. Examples include investigating separate failures, generating alternative designs, or independently reviewing the same patch.

Avoid parallel edits to tightly coupled files unless merge/reconciliation cost is worth it.

## Human checkpoints

Require explicit human review before actions with high blast radius, such as:

- production deployment;
- destructive database operations;
- security/identity changes;
- secrets/credential management;
- billing or irreversible cloud operations;
- major dependency upgrades;
- changes to legal, financial or safety-critical logic.

## Anti-patterns

- "Build the entire application" with no success criteria.
- Trusting an agent's statement that tests passed without seeing tool output.
- Giving broad shell/network permissions for a tiny editing task.
- Asking for repeated rewrites instead of exposing a failing test.
- Letting an agent silently add dependencies.
- Measuring productivity by generated lines of code.

## Practical prompt

```text
Inspect the relevant repository files before editing.
Restate the acceptance criteria and identify uncertainties.
Propose a short plan, then implement the smallest coherent change.
Run the relevant tests/type checks/linting after the edit.
Report the exact evidence and any remaining risks.
Do not modify unrelated files or add dependencies without justification.
```

## Further reading

See also:

- [Verification First](verification-first.md)
- [Agent Security](../security/agent-safety.md)
- [Benchmark Literacy](../benchmarks/README.md)
- [2026 Research Landscape](../research/2026-landscape.md)
