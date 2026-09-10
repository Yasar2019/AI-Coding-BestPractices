# Agent Security & Safety

Modern coding agents can read files, execute commands, access developer tools and sometimes interact with external services. That makes them useful—and creates a broader attack surface than ordinary autocomplete.

## Threat model

Think about four surfaces:

1. **Input risk** — malicious or misleading instructions in issues, docs, webpages, logs or generated content.
2. **Tool risk** — shell, filesystem, browser, cloud, database or API actions with excessive permissions.
3. **Code risk** — vulnerable, incorrect or dependency-heavy generated patches.
4. **Workflow risk** — agents taking irreversible actions without adequate review or telemetry.

## Minimum controls

- Grant the **least privilege** needed for the task.
- Keep secrets out of prompts and logs.
- Separate read-only inspection from write/execute actions.
- Require approval for destructive, privileged or production-facing operations.
- Preserve tool/action logs for auditability.
- Use branch/PR workflows instead of direct production edits.
- Scan dependencies, secrets and code before merge.
- Treat content retrieved from external systems as untrusted input.

## Prompt injection for coding agents

A coding agent may encounter instructions embedded in:

- README files;
- issue descriptions;
- web pages;
- build logs;
- comments;
- package metadata;
- generated files.

The agent should not automatically treat every instruction it reads as authoritative. Repository policy and the user's explicit task should take precedence over untrusted content.

## High-risk actions that deserve human approval

- deleting or rewriting data;
- changing auth/authorization logic;
- rotating or exposing credentials;
- production deployments;
- modifying CI/CD permissions;
- changing cloud/IAM configuration;
- sending external communications;
- initiating payments or billing changes.

## Secure-code verification

Functional tests are not enough. Add security-specific checks for relevant code paths:

```text
[ ] authentication/authorization tests
[ ] injection tests
[ ] unsafe deserialization checks
[ ] input validation
[ ] output encoding
[ ] secret scanning
[ ] dependency vulnerability scan
[ ] static analysis
[ ] least-privilege review
```

## Why this matters

SecureAgentBench evaluated realistic repository-level code-agent tasks derived from real vulnerability contexts. Its authors reported that even the best evaluated agent/model combination solved only 15.2% of tasks in a way that was both correct and secure, and that explicit security instructions alone did not significantly fix the problem. This is a strong reminder that security must be enforced with tooling and review, not just prompt wording.

## Primary references

- SecureAgentBench (2025): https://arxiv.org/abs/2509.22097
- OpenAI, *Running Codex safely at OpenAI* (2026): https://openai.com/index/running-codex-safely/
- Anthropic, *Trustworthy agents in practice* (2026): https://www.anthropic.com/research/trustworthy-agents
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework

## Principle

> Do not ask a model to “be safe” and assume the problem is solved. Build safety into permissions, environments, tests, review gates and observability.
