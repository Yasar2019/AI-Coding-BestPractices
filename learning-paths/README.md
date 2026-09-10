# Learning Paths

Choose a path based on what you need to accomplish, not on hype around a particular model.

## 🌱 Beginner — AI-assisted developer

**Goal:** use AI without losing understanding.

1. Learn basic Git, tests, debugging and reading stack traces.
2. Use AI first for explanations, examples and small changes.
3. Practice writing acceptance criteria before asking for code.
4. Learn to inspect diffs and reject unnecessary changes.
5. Finish with one small project where every generated change is tested.

**Milestone:** you can explain every important line of an AI-generated patch before merging it.

## 🧑‍💻 Intermediate — AI-accelerated engineer

**Goal:** delegate bounded engineering tasks reliably.

1. Build repository-level instructions and conventions.
2. Use plan → edit → test → review loops.
3. Ask agents to inspect before changing code.
4. Use linters, static analysis, tests and runtime logs as feedback tools.
5. Learn context management: give only the files, docs and constraints that matter.
6. Evaluate tools against a small benchmark drawn from your own backlog.

**Milestone:** you can delegate a multi-file task and independently verify the result.

## 🧠 Advanced — Agentic software engineer

**Goal:** design reliable human-agent systems.

1. Decompose complex work into independently verifiable subtasks.
2. Design permission boundaries for shell, filesystem, network and external tools.
3. Use specialized agents or parallel attempts when comparison adds value.
4. Build task-specific evaluation suites and regression datasets.
5. Instrument cost, latency, retries, failed tool calls and human review time.
6. Treat prompts/instructions as versioned engineering artifacts.
7. Model prompt injection and supply-chain threats.

**Milestone:** your agent workflows are reproducible, observable and measurable.

## 🏢 Staff / Lead / Enterprise

**Goal:** scale AI coding without scaling hidden risk.

1. Define approved use cases and data-handling rules.
2. Separate experimentation from production permissions.
3. Standardize repository instructions, CI gates and code ownership.
4. Track outcomes: lead time, escaped defects, rollback rate, review burden and developer satisfaction.
5. Maintain a vendor-neutral evaluation harness.
6. Review agent/tool permissions as part of security architecture.
7. Create an incident process for harmful or incorrect AI-generated changes.

**Milestone:** your organization can explain where AI helps, where it does not, and what evidence supports that conclusion.

## Suggested project progression

| Stage | Project | What AI should do | What you must verify |
|---|---|---|---|
| 1 | CLI todo app | scaffold + tests | behavior + code understanding |
| 2 | REST API | endpoints + validation | API contract + security |
| 3 | Existing repo bug | inspect + patch | regression test + minimal diff |
| 4 | Framework migration | plan + iterative edits | compatibility + performance |
| 5 | Production feature | bounded agent workflow | full CI + threat model + review |

Continue with the [agentic workflow playbook](../playbooks/agentic-workflow.md).
