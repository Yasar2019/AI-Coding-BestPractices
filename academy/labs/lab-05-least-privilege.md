# Lab 05 — Least Privilege for Coding Agents

## Goal

Design the smallest permission set an AI agent needs to complete a software task safely.

## Scenario

Task: update a date-formatting helper and its tests.

Available capabilities:

- read repository files;
- write repository files;
- execute local tests;
- execute arbitrary shell commands;
- access the network;
- read environment variables;
- push directly to `main`;
- deploy to production.

## Exercise

Classify each capability as:

- **Required**
- **Useful but optional**
- **Not justified**

Then define an approval gate for any capability whose effect could escape the local working copy.

## Recommended answer

For this task, a strong default is:

| Capability | Decision | Why |
|---|---|---|
| Read repository files | Required | Needed to inspect implementation and tests |
| Write repository files | Required | Needed to create the patch |
| Run local tests | Required | Provides executable verification |
| Arbitrary shell | Optional / constrained | Prefer an allowlisted test command |
| Network | Not justified | Date formatting should not require external access |
| Environment variables | Not justified | Creates unnecessary secret exposure |
| Push to `main` | Not justified | Use branch + review |
| Production deploy | Not justified | Completely outside task scope |

## Design principle

> **Capability should follow task necessity, not model capability.**

The fact that an agent *can* use a tool is not evidence that it *should*.

## Approval boundaries

Human approval is especially valuable before:

- destructive filesystem operations;
- network calls that send data externally;
- credential or secret access;
- package installation from new sources;
- cloud or production writes;
- direct pushes to protected branches;
- database migrations;
- permission changes.

## Reflection

Least privilege reduces the impact of model mistakes, prompt injection, compromised dependencies, and ambiguous instructions. It also makes agent behavior easier to reason about and audit.

## References

- NIST, *AI Risk Management Framework*: https://www.nist.gov/itl/ai-risk-management-framework
- OWASP GenAI Security Project: https://genai.owasp.org/
- GitHub, code security documentation: https://docs.github.com/en/code-security
