# Release Notes

## Public Preview — September 2026

This is the first version of **AI Coding Best Practices** intended to be shared broadly.

It is not a claim that the curriculum is complete. It is a stable public-preview milestone with a coherent handbook, interactive learning tools, hands-on labs, security guidance, evaluation tooling, and a transparent roadmap.

## Highlights

### A complete learning spine

The repository now connects:

**context → implementation → verification → debugging → security → evaluation → team practice**

That sequence is designed for both beginners and experienced engineers.

### Seven Academy labs

The Academy now includes practical modules on:

1. Context Engineering
2. Verification Engineering
3. Agentic Debugging
4. Prompt Injection
5. Least Privilege
6. Secrets & Supply Chain
7. Evaluation Engineering

### Runnable exercises

Verification and debugging labs include intentionally broken Python exercises with regression tests. Learners practice proving a fix rather than trusting generated output.

### Security-first agent design

The project treats a coding agent as a system with permissions, tools, network access, credentials, untrusted inputs, approval gates, and audit requirements—not merely as a chatbot that produces code.

### Evaluation Engineering

A new dependency-free harness helps teams record:

- task success;
- executable test evidence;
- unsafe actions;
- human intervention time;
- wall-clock time;
- estimated cost.

The bundled demonstration results are explicitly labeled synthetic and must not be presented as benchmark measurements.

### Interactive content

The repository includes two static browser experiences:

- the AI Coding Dashboard;
- the AI Coding Academy.

They require no framework or backend.

## Current limitations

This public preview does not yet include:

- a hosted GitHub Pages site;
- automatic execution of external coding agents;
- a public model leaderboard;
- statistically rigorous repeated-run comparisons;
- repository-scale multi-agent labs;
- multilingual curriculum tracks.

Those gaps are intentional and documented in [ROADMAP.md](ROADMAP.md).

## Research stance

The project does not assume that AI coding always improves productivity or that benchmark scores directly predict team outcomes. Public benchmarks, controlled studies, vendor research, and practitioner evidence are presented with source links and limitations where possible.

## How to start

Use [QUICKSTART.md](QUICKSTART.md) for the 10-minute path.

## Feedback

The highest-value feedback at this stage is:

- incorrect or outdated claims;
- missing primary sources;
- confusing exercises;
- broken reproducibility;
- security guidance that lacks a realistic threat model;
- real-world evaluation tasks worth adding to the starter suite.

Please open an issue or contribute through [CONTRIBUTING.md](CONTRIBUTING.md).
