# AI Coding Cheat Sheet — 2026 Edition

A compact field guide for AI-assisted and agentic software engineering.

**Updated:** 2026-09-10

## The golden loop

```text
UNDERSTAND → PLAN → IMPLEMENT → VERIFY → REVIEW → MEASURE → LEARN
```

### 1. UNDERSTAND

Before editing, inspect:

- repository structure;
- relevant code and tests;
- architecture/conventions;
- dependency versions;
- error logs or failing behavior;
- constraints and acceptance criteria.

### 2. PLAN

Ask for a short plan containing:

```text
Goal
Files likely affected
Risks / assumptions
Implementation steps
Verification commands
```

Plans should be easy to revise. Do not turn planning into an essay.

### 3. IMPLEMENT

Prefer:

- the smallest coherent diff;
- existing abstractions over unnecessary new ones;
- no unrelated cleanup;
- no silent dependencies;
- iterative edit → test loops.

### 4. VERIFY

Use executable evidence whenever possible:

```text
[ ] format
[ ] lint
[ ] type check
[ ] unit tests
[ ] integration / E2E tests
[ ] security checks
[ ] dependency scan
[ ] runtime verification
[ ] performance benchmark when relevant
```

### 5. REVIEW

Inspect the actual diff. Check:

- omitted requirements;
- accidental behavior changes;
- overengineering;
- insecure defaults;
- new dependencies;
- missing error paths;
- weak AI-generated tests;
- hidden compatibility breaks.

### 6. MEASURE

Do not use generated lines of code as the main success metric. Prefer:

- accepted task completion;
- review time;
- escaped defects;
- rework;
- rollback rate;
- cost per useful change;
- latency;
- developer time saved.

### 7. LEARN

If the agent repeatedly makes the same mistake, improve:

- repo instructions;
- tests;
- examples;
- fixtures;
- tool configuration;
- permissions;
- evaluation tasks.

Do not endlessly lengthen prompts.

---

## Universal task packet

```text
GOAL
Describe the behavior that should change.

CONTEXT
Point to relevant architecture, files, examples and conventions.

CONSTRAINTS
Compatibility, APIs, performance, dependencies, security.

ACCEPTANCE CRITERIA
Observable outcomes defining done.

VERIFICATION
Exact commands/tests that must pass.

BOUNDARIES
What must not change? Which actions require approval?
```

---

## Prompt patterns

### Repository task

```text
Inspect the relevant files before editing.
Restate the acceptance criteria and uncertainties.
Propose a short implementation plan.
Implement the smallest coherent patch.
Run the relevant tests, type checks and linting.
Report exact verification evidence and remaining risks.
Do not modify unrelated files or add dependencies without justification.
```

### Debugging

```text
Reproduce or trace the failure before proposing a fix.
Identify the root cause, not only the symptom.
Make the smallest correction.
Add a regression test that fails before the fix and passes after it.
```

### Code review

```text
Review this diff for:
1. correctness
2. security
3. missing edge cases
4. compatibility
5. maintainability
6. unnecessary complexity
7. test quality

Rank findings by severity and cite exact files/lines.
```

### Refactor

```text
Preserve externally observable behavior.
Explain the invariant being preserved.
Keep the patch narrow.
Run existing tests before and after the change.
Do not mix feature work into the refactor.
```

---

## Context engineering

Give the system what it needs, not everything you have.

Useful context:

- architecture summary;
- relevant source files;
- interfaces/schemas;
- tests;
- examples of preferred style;
- current logs/errors;
- dependency constraints;
- product requirements.

Avoid dumping an entire repository when a small working set is sufficient.

---

## Agent permission ladder

```text
LOWER BLAST RADIUS
read files
→ write branch files
→ run local commands
→ network/tool access
→ cloud/database write
→ production/destructive actions
HIGHER BLAST RADIUS
```

Use least privilege. Add human approval as blast radius rises.

---

## Security quick check

Never rely on “write secure code” as the only control.

```text
[ ] no secrets in prompt/context/logs
[ ] untrusted retrieved content treated as untrusted
[ ] auth/authz paths tested
[ ] input validation checked
[ ] injection risks reviewed
[ ] dependency additions reviewed/scanned
[ ] secret scan run
[ ] static security analysis run where useful
[ ] high-risk tool actions require approval
```

Research reminder: SecureAgentBench reported only 15.2% correct-and-secure solutions for its best evaluated agent/model combination on 105 realistic vulnerability-oriented tasks.

Source: https://arxiv.org/abs/2509.22097

---

## Benchmark sanity check

Before citing a coding-agent score, ask:

```text
Which dataset/version?
Which agent scaffold?
Which model?
Which tool permissions?
How many retries / what budget?
What date?
Does it test security?
Does it resemble my tasks?
```

SWE-bench official project: https://www.swebench.com/

---

## Productivity sanity check

Evidence remains context-dependent. METR's early-2025 randomized study of experienced OSS developers found a 19% slowdown in its studied setting, while its 2026 follow-up said newer data was too selection-biased to cleanly estimate current speedup and suggested current tools likely help more than the earlier generation.

Sources:

- https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- https://metr.org/blog/2026-02-24-uplift-update/

---

## When AI is usually a strong fit

- codebase explanation;
- scaffolding;
- test generation followed by review;
- repetitive migrations;
- bounded refactors;
- debugging with logs/tests;
- documentation;
- multi-file mechanical edits;
- alternative implementation exploration.

## Use extra caution when

- requirements are ambiguous;
- the change is security-critical;
- the agent cannot run meaningful verification;
- production/data operations are irreversible;
- code is highly concurrent or timing-sensitive;
- domain correctness requires specialist knowledge;
- the system proposes large unrelated rewrites.

---

## Team rule of thumb

> **The model proposes. The environment tests. The engineer decides.**

More detailed guides:

- [Start Here](START_HERE.md)
- [Agentic Workflow](playbooks/agentic-workflow.md)
- [Verification First](playbooks/verification-first.md)
- [Agent Security](security/agent-safety.md)
- [Benchmarks](benchmarks/README.md)
- [Research Landscape](research/2026-landscape.md)
- [Interactive Dashboard](dashboard/index.html)
