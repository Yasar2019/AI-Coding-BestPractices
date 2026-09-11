# AI Coding Research Landscape — 2026

This page tracks notable evidence about AI-assisted and agentic software engineering. It distinguishes **capability benchmarks**, **real-world developer studies**, **security evaluations**, **usage research**, and **evaluation methodology**.

> Last reviewed: 2026-09-11

## 1. Real developer productivity is context-dependent

### METR randomized controlled trial (2025)

METR studied 16 experienced open-source developers working on 246 real tasks in repositories they knew well. In the early-2025 setup studied, allowing AI tools increased completion time by **19%** on average, even though developers believed AI had sped them up.

Important limitation: this was a specific population, task distribution and tool generation; it should not be generalized into “AI always slows programmers down.”

Primary source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

### METR follow-up (2026)

METR reported that later experiments were affected by selection bias because many developers no longer wanted to work without AI. The organization stated that AI likely produced more speedup in early 2026 than in its earlier experiment, but that its newer data could not reliably estimate the magnitude.

Primary source: https://metr.org/blog/2026-02-24-uplift-update/

**Takeaway:** productivity claims need task-, user- and tool-specific evidence.

## 2. Expertise still matters in agentic coding

Anthropic analyzed roughly **400,000 Claude Code sessions** from October 2025 through April 2026. Its research found that people generally made more of the planning decisions while the coding agent made more execution decisions. Greater domain expertise was associated with stronger outcomes and more work accomplished per instruction.

Primary source: https://www.anthropic.com/research/claude-code-expertise

**Takeaway:** agents do not eliminate expertise; they can amplify it.

## 3. Security remains a major weakness

SecureAgentBench introduced 105 realistic repository-level tasks tied to vulnerability scenarios and evaluated both functional correctness and security. The authors reported a best correct-and-secure rate of **15.2%** among the evaluated combinations, and found that simply adding explicit security instructions was not enough to solve the problem.

Primary source: https://arxiv.org/abs/2509.22097

**Takeaway:** secure coding requires external controls, tests and analysis—not just better prompting.

## 4. Scientific software remains hard

SWE-bench Science (2026) introduced **119 tasks from 98 GitHub repositories across 20 scientific domains**. The paper reported that even its strongest evaluated agent remained below 50% pass@1, with failures involving scientific abstraction, incomplete repair coverage, exploration mistakes and poor generalization.

Primary source: https://arxiv.org/abs/2608.19799

**Takeaway:** domain knowledge and repository context still constrain autonomous coding.

## 5. Task type can matter more than agent brand

A 2026 study using 7,156 AI-generated pull requests from the AIDev dataset compared several popular coding agents. The authors found strong differences by task category and reported that no single agent was best across all task types.

Primary source: https://arxiv.org/abs/2602.08915

**Takeaway:** evaluate systems against your own task distribution instead of choosing solely from global rankings.

## 6. SWE-bench remains useful—but must be interpreted carefully

SWE-bench evaluates patches for real GitHub issues. Its ecosystem includes several dataset variants, and the public leaderboard increasingly separates standardized agent environments from custom-agent runs.

Official project: https://www.swebench.com/

**Takeaway:** compare like with like. Model + agent scaffold + tools + budget + retries all affect results.

## 7. Agent governance has become part of software engineering

As coding agents gain shell, filesystem and external-tool access, operational safety becomes an engineering concern. OpenAI's 2026 guidance on running Codex emphasizes technical boundaries, human approval for higher-risk actions and agent-native telemetry. Anthropic similarly highlights prompt injection and unintended actions as core governance challenges for agents.

Primary sources:

- https://openai.com/index/running-codex-safely/
- https://www.anthropic.com/research/trustworthy-agents

## 8. Benchmark quality itself can distort conclusions

In July 2026, OpenAI published an audit of SWE-Bench Pro and estimated that roughly **30% of tasks were broken** under its audit criteria. The post argues that invalid or ambiguous tasks can materially distort capability estimates.

Primary source: https://openai.com/index/separating-signal-from-noise-coding-evaluations/

Important limitation: this is a vendor-conducted benchmark audit and should not be treated as independent consensus about every SWE-Bench variant.

**Takeaway:** benchmark integrity is part of evaluation engineering. A precise score on a flawed task set can still be misleading.

## 9. Broader software-engineering task coverage matters

OmniCode (2026) introduced **1,794 tasks** across Python, Java and C++, covering bug fixing, test generation, code-review fixing and style fixing. Its authors report substantial variation by language and task category, with some agent configurations performing much worse outside Python bug fixing.

Primary source: https://arxiv.org/abs/2602.02262

**Takeaway:** patch generation alone is not a complete proxy for software engineering ability.

## 10. “Bug fix” and “feature” labels can hide very different task demands

A September 2026 preprint proposed a Spread–Novelty–Centrality profile for repository-level coding tasks and applied it across multiple benchmarks and thousands of agent trajectories. The authors found that nominal task labels were weak proxies for actual engineering demands and that agent behavior exposed differences not visible from labels alone.

Primary source: https://arxiv.org/abs/2609.01271

Important limitation: this is a recent preprint and should be treated as evolving evidence rather than settled methodology.

**Takeaway:** internal evaluations should characterize task difficulty and structure, not merely assign broad labels.

## 11. Research principles for this repository

When adding a study:

1. Link the primary paper/project page.
2. State publication date.
3. Identify sample/task distribution.
4. Distinguish correlation from causal evidence.
5. Include limitations.
6. Avoid turning benchmark snapshots into timeless rankings.
7. Separate vendor usage studies from independent evaluations.
8. Record when a claim is based on a recent preprint rather than peer-reviewed work.

## Research watchlist

Future updates should track:

- long-horizon autonomous software engineering;
- multi-agent coordination;
- code-review agents;
- secure code generation;
- repository-memory/context systems;
- human skill formation and deskilling;
- cost-adjusted benchmark performance;
- software engineering in scientific and safety-critical domains;
- agent observability and governance;
- evaluation contamination and benchmark saturation;
- benchmark task validity and task-demand profiling.

## Suggested citation format

```text
Author(s). Title. Venue/Organization, Year.
URL: <primary source>
Accessed: YYYY-MM-DD
Claim used: <specific result>
Limitations: <brief note>
```
