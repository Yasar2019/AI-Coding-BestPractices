# AI Coding Best Practices — 2026 Global Handbook

> A practical, evidence-backed, beginner-to-expert guide to AI-assisted and agentic software engineering.

**Updated:** 2026-09-10  
**Scope:** AI coding assistants, coding agents, context engineering, prompting, verification, security, evaluation, benchmarks, team workflows, and research.

## Why this repository exists

AI coding has moved beyond autocomplete. Modern agents can inspect repositories, edit many files, run commands and tests, use tools, review code, and work for extended periods. That changes the engineering problem: the key skill is no longer simply “write a better prompt,” but **design a reliable human–agent development loop**.

This repository teaches that loop from first principles and keeps claims linked to primary sources.

## Start here

| Your level | Recommended path |
|---|---|
| 🌱 Beginner | [START_HERE.md](START_HERE.md) → [Learning Paths](learning-paths/README.md) → [Cheat Sheet](AI_CHEATSHEET.md) |
| 🧑‍💻 Developer | [Agentic Workflow](playbooks/agentic-workflow.md) → [Verification First](playbooks/verification-first.md) |
| 🧠 Advanced / Staff+ | [Research Landscape](research/2026-landscape.md) → [Benchmarks](benchmarks/README.md) → [Agent Security](security/agent-safety.md) |
| 🏢 Team / Enterprise | [Team Operating Model](playbooks/team-operating-model.md) → [Agent Security](security/agent-safety.md) |

## Interactive AI Coding Dashboard

Open [`dashboard/index.html`](dashboard/index.html) locally for an interactive learning dashboard with:

- role-based learning-path filtering;
- verification and security checklists;
- an AI task-risk classifier;
- research and benchmark cards;
- workflow maturity scoring;
- searchable resources.

The dashboard is dependency-free HTML/CSS/JavaScript, so it can be served directly with GitHub Pages or any static host.

## The core workflow

```text
1. UNDERSTAND  → inspect code, requirements, constraints
2. PLAN        → define scope, acceptance criteria, test strategy
3. IMPLEMENT   → use the smallest useful agent loop
4. VERIFY      → tests, types, lint, security, runtime evidence
5. REVIEW      → human review of behavior, architecture, risk
6. MEASURE     → quality, cost, latency, rework, escaped defects
7. LEARN       → improve repo instructions, tooling and evals
```

### The rule that matters most

> **Never treat model confidence as verification. Give the agent executable evidence whenever possible.**

This aligns with current vendor guidance and with the broader research trend toward tool-using, test-driven agent loops.

## Repository map

```text
AI_CHEATSHEET.md                Quick reference
START_HERE.md                   Beginner-friendly orientation
ai-tools/                       Tool guidance
prompt-engineering/             Prompting and context patterns
coding-best-practices/          Software engineering fundamentals
learning-paths/                 Beginner → expert curricula
playbooks/                      Repeatable team and individual workflows
security/                       Agent, tool, secret and supply-chain safety
benchmarks/                     How to read coding-agent benchmarks
research/                       2026 landscape + primary references
case_studies/                   Evidence-backed examples
resources/                      Curated learning material
dashboard/                      Interactive static dashboard
```

## What changed in the 2026 edition

- Shift from **prompt engineering** to **context + environment + verification engineering**.
- Dedicated coverage of coding agents, subagents, plan modes, repository instructions, hooks/tools and MCP-style integrations.
- A security model for agents that can execute shell/file/tool actions.
- Benchmark literacy: SWE-bench, broader software-engineering benchmarks, dialogue evaluation and end-to-end project evaluation.
- Research summaries on real developer productivity, agentic coding usage, secure coding and research-extension benchmarks.
- Practical guidance for choosing when to use AI—and when manual engineering is faster or safer.
- An interactive dashboard for different experience levels.

## Evidence snapshot

Research does **not** support a simplistic “AI always makes developers faster” story. A 2025 METR randomized study of experienced open-source developers found the studied early-2025 AI setup increased task completion time by 19% in that setting. Later research continues to show that expertise, task structure, tool feedback, and agent environment strongly shape outcomes. Likewise, 2026 security benchmarks show that generating code that is simultaneously correct and secure remains difficult.

See [research/2026-landscape.md](research/2026-landscape.md) for the evidence and limitations.

## Source policy

We prioritize:

1. peer-reviewed papers and conference proceedings;
2. official benchmark/project pages;
3. primary vendor documentation;
4. standards and security organizations;
5. reputable secondary reporting only when primary material is unavailable.

Every time-sensitive metric should include a date. Benchmark scores are snapshots, not permanent rankings.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md). If you add a factual claim, include a primary source where possible and state the date for fast-moving facts.

## License

See [LICENSE](LICENSE).
