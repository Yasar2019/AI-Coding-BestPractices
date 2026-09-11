# AI Coding Best Practices

> **A practical, evidence-backed handbook + interactive Academy for AI-assisted and agentic software engineering.**

![Status](https://img.shields.io/badge/status-public_preview-5eead4)
[![Content checks](https://github.com/Yasar2019/AI-Coding-BestPractices/actions/workflows/content-check.yml/badge.svg)](https://github.com/Yasar2019/AI-Coding-BestPractices/actions/workflows/content-check.yml)
![License](https://img.shields.io/badge/license-MIT-blue)

**Public Preview · September 2026**  
For beginners, working developers, staff+ engineers, security practitioners, and teams adopting coding agents.

## Why this project exists

AI coding has moved far beyond autocomplete. Modern agents can inspect repositories, edit multiple files, run commands and tests, use external tools, review code, and work for extended periods.

That changes the engineering skill that matters most:

> **Generated code is a hypothesis. Engineering evidence decides whether it ships.**

This repository teaches how to design reliable human–agent workflows around that principle: context, implementation, verification, debugging, security, evaluation, and team governance.

## Start in 10 minutes

**New here? → [QUICKSTART.md](QUICKSTART.md)**

You can immediately:

- open the [interactive AI Coding Dashboard](dashboard/index.html);
- use the [AI Coding Academy](academy/index.html);
- run intentionally broken exercises and verify your fixes with tests;
- practice agent-security scenarios safely;
- evaluate your own coding-agent configuration with the [evaluation harness](evaluation/README.md).

## Choose your path

| You are… | Start here |
|---|---|
| 🌱 New to AI coding | [Start Here](START_HERE.md) → [Cheat Sheet](AI_CHEATSHEET.md) → Academy Labs 01–02 |
| 🧑‍💻 Working developer | [Agentic Workflow](playbooks/agentic-workflow.md) → [Verification First](playbooks/verification-first.md) → Labs 02–03 |
| 🔐 Security / platform engineer | [Agent Safety](security/agent-safety.md) → Labs 04–06 |
| 🧠 Staff+ / researcher | [Research Landscape](research/2026-landscape.md) → [Benchmark Literacy](benchmarks/README.md) → Lab 07 |
| 🏢 Team / engineering leader | [Team Operating Model](playbooks/team-operating-model.md) → [Evaluation Engineering](evaluation/README.md) |

## What is included today

### 📘 Global handbook

Guidance on:

- context and prompt engineering;
- coding-agent workflows;
- verification-first development;
- debugging with falsifiable hypotheses;
- agent permissions and approval gates;
- secrets, dependencies, and supply-chain risk;
- benchmark interpretation;
- team operating models;
- research-backed AI-coding practices.

### 🎓 AI Coding Academy

Seven current labs:

1. [Context Engineering](academy/labs/lab-01-context-engineering.md)
2. [Verification Engineering](academy/labs/lab-02-verification-engineering.md)
3. [Agentic Debugging](academy/labs/lab-03-agentic-debugging.md)
4. [Prompt Injection](academy/labs/lab-04-prompt-injection.md)
5. [Least Privilege](academy/labs/lab-05-least-privilege.md)
6. [Secrets & Supply Chain](academy/labs/lab-06-secrets-supply-chain.md)
7. [Evaluation Engineering](academy/labs/lab-07-evaluation-engineering.md)

The Academy follows:

```text
Learn → Predict → Try → Verify → Reflect
```

### 🧪 Runnable exercises

Clone the repository and run:

```bash
git clone https://github.com/Yasar2019/AI-Coding-BestPractices.git
cd AI-Coding-BestPractices/academy/exercises/order_total
python -m unittest -v
```

The starter implementation is intentionally wrong. Your job is to reproduce the failure, repair the causal defect, rerun the regression suite, and inspect the diff.

### 📊 Evaluation Engineering

The dependency-free evaluation harness keeps important signals separate:

- task pass rate;
- executable test evidence;
- unsafe actions;
- human intervention time;
- wall-clock latency;
- estimated cost.

Try it:

```bash
python evaluation/harness.py evaluation/sample_results.jsonl
```

**Important:** bundled results are synthetic demo data, not claims about any real model or agent.

## The core AI coding loop

```text
1. UNDERSTAND  → inspect code, requirements, constraints
2. PLAN        → define scope, acceptance criteria, test strategy
3. IMPLEMENT   → use the smallest sufficient agent loop
4. VERIFY      → tests, types, lint, security, runtime evidence
5. REVIEW      → inspect behavior, architecture, risk, and diff
6. MEASURE     → quality, cost, latency, rework, safety events
7. LEARN       → improve instructions, tooling, task design, evals
```

## Interactive tools

### AI Coding Dashboard

[`dashboard/index.html`](dashboard/index.html) includes:

- role-based learning paths;
- AI task-risk classification;
- workflow maturity scoring;
- verification guidance;
- research and benchmark navigation.

### AI Coding Academy

[`academy/index.html`](academy/index.html) includes:

- lab navigation;
- browser-local progress tracking;
- interactive knowledge checks;
- a security permission matrix.

Both are plain HTML/CSS/JavaScript—no framework or backend required.

## Evidence, not hype

This project does **not** assume AI coding always increases productivity, that passing tests proves security, or that one public leaderboard predicts performance on your repository.

The research section deliberately includes positive results, negative results, benchmark limitations, and study constraints. Fast-moving claims are dated and linked to primary sources where possible.

See:

- [2026 Research Landscape](research/2026-landscape.md)
- [Benchmark Literacy](benchmarks/README.md)
- [Evaluation Engineering](evaluation/README.md)
- [Agent Safety](security/agent-safety.md)

## Repository map

```text
QUICKSTART.md                    10-minute onboarding
AI_CHEATSHEET.md                 Daily quick reference
START_HERE.md                    Beginner orientation
academy/                         Curriculum, labs, exercises, quizzes
dashboard/                       Interactive AI coding dashboard
evaluation/                      Internal eval methodology + harness
playbooks/                       Repeatable engineering workflows
security/                        Agent/tool/security guidance
benchmarks/                      Benchmark literacy
research/                        2026 evidence and primary references
ai-tools/                        Tool guidance
prompt-engineering/              Prompt/context patterns
coding-best-practices/           Software-engineering fundamentals
case_studies/                    Evidence-backed examples
resources/                       Curated learning resources
ROADMAP.md                       Transparent project roadmap
RELEASE_NOTES.md                 Public-preview release notes
CITATION.cff                     Citation metadata
```

## Project status

This is a **public preview**, not a finished encyclopedia.

The current version is designed to be useful and shareable now. Upcoming work includes richer evaluation statistics, repository-scale labs, multi-agent workflows, public-site deployment, and community task packs.

See the transparent [ROADMAP.md](ROADMAP.md).

## Contributing

Contributions are welcome—especially:

- corrections to outdated or weakly sourced claims;
- better primary references;
- new reproducible labs;
- representative evaluation tasks;
- accessibility and learning improvements;
- real-world failure patterns with defensible evidence.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR.

## Source policy

Preferred evidence order:

1. peer-reviewed publications and strong research preprints;
2. official benchmark/project documentation;
3. primary vendor engineering/research documentation;
4. standards and security organizations;
5. reputable secondary sources only when primary evidence is unavailable.

Benchmark results are treated as **configuration- and date-specific snapshots**, not permanent model rankings.

## Cite this project

GitHub citation metadata is available in [`CITATION.cff`](CITATION.cff).

## License

MIT — see [LICENSE](LICENSE).
