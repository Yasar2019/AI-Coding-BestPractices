# AI Coding Benchmark Literacy

Benchmarks are useful when you understand what they measure—and dangerous when treated as universal rankings.

## What a benchmark score does *not* tell you

A single pass rate does not automatically tell you:

- how a tool performs on your languages/frameworks;
- whether patches are secure or maintainable;
- how much human supervision was required;
- how expensive or slow the run was;
- whether the agent used retries, hidden scaffolding or custom tools;
- whether the benchmark resembles your real backlog.

## SWE-bench

SWE-bench evaluates models/agents on real GitHub software issues by asking them to produce patches for repository-level tasks. The ecosystem includes original, Lite, Verified, Multimodal and other variants.

As of 2026, the public leaderboard also emphasizes a standardized **bash-only** setting with a common mini-SWE-agent environment, which makes some model comparisons more meaningful than comparisons across completely different agent scaffolds.

Official project: https://www.swebench.com/

## SecureAgentBench

SecureAgentBench focuses on whether agent-generated code is not only functionally correct but also secure in realistic vulnerability scenarios. That distinction is essential: code can pass functional tests and still introduce exploitable weaknesses.

Paper: https://arxiv.org/abs/2509.22097

## SWE-bench Science

SWE-bench Science extends repository-level evaluation into scientific software. The 2026 paper includes 119 tasks from 98 repositories across 20 scientific domains and reports substantial remaining difficulty even for strong contemporary agents.

Paper: https://arxiv.org/abs/2608.19799

## How to compare coding systems responsibly

Compare systems on a matrix rather than a single score:

| Dimension | Question |
|---|---|
| Correctness | Does the patch solve the task? |
| Security | Does it avoid known/new vulnerabilities? |
| Maintainability | Is the implementation understandable and idiomatic? |
| Autonomy | How much supervision is needed? |
| Cost | What is the total inference/tool cost? |
| Latency | How long does useful completion take? |
| Reliability | How often does the workflow succeed across reruns? |
| Breadth | Which languages/frameworks/task types work well? |
| Review burden | How much human time is needed before merge? |

## Build your own mini-benchmark

The best evaluation for your team is usually a small, versioned dataset of representative tasks.

1. Select 20–100 real historical tasks.
2. Remove tasks that leak the final patch to the model.
3. Define acceptance tests and review criteria.
4. Run each tool/model under documented conditions.
5. Track pass rate, cost, latency, retries and review time.
6. Re-run after model/tool upgrades.

Keep the benchmark private if it contains proprietary code.

## Avoid leaderboard overfitting

Do not redesign your workflow around one public benchmark. Public benchmark performance can be affected by dataset familiarity, benchmark-specific scaffolding and differences between benchmark tasks and real engineering work.

## Practical scorecard

```text
Task success:       __ / 10
Security:           __ / 10
Maintainability:    __ / 10
Review effort:      __ / 10
Speed:              __ / 10
Cost efficiency:    __ / 10
Tool reliability:   __ / 10
Overall fit:        __ / 10
```

## Primary references

- SWE-bench project and leaderboards: https://www.swebench.com/
- SWE-bench Science: https://arxiv.org/abs/2608.19799
- SecureAgentBench: https://arxiv.org/abs/2509.22097
- METR developer productivity study: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- METR 2026 follow-up/design update: https://metr.org/blog/2026-02-24-uplift-update/
