# Team Operating Model for AI Coding

This playbook is for teams moving from individual experimentation to repeatable, governed AI-assisted development.

## 1. Define allowed work by risk tier

### Low risk

Examples: documentation, tests, code explanation, local refactors, generated fixtures.

Default: agent may act autonomously inside the repository sandbox, with normal PR review.

### Medium risk

Examples: feature implementation, dependency upgrades, database migrations, CI changes.

Default: agent may implement, but requires explicit review of architecture, tests and side effects.

### High risk

Examples: auth, cryptography, payments, production deployment, destructive data operations, IAM/secrets.

Default: agent assists, but humans retain decision authority and high-risk actions require explicit approval.

## 2. Standardize repository instructions

Store durable instructions close to the codebase:

- architecture overview;
- coding conventions;
- test commands;
- dependency policy;
- security expectations;
- files/directories the agent should not modify;
- release and deployment rules;
- definition of done.

Keep these instructions version controlled and short enough to remain useful.

## 3. Make CI the objective referee

At minimum, require the same gates for human- and AI-authored changes:

```text
format → lint → type check → unit tests → integration tests → security checks
```

Higher-risk repositories should add dependency scanning, SAST, secret scanning, policy checks and environment-specific validation.

## 4. Track outcomes, not activity

Do not optimize for prompts sent, generated lines, agent minutes or number of automated commits. Track outcomes such as:

- cycle time;
- time to review;
- escaped defects;
- rollback rate;
- security findings;
- rework percentage;
- developer time saved;
- cost per accepted change;
- developer understanding and satisfaction.

## 5. Create an internal evaluation set

Sample real tasks across your work distribution: bugs, features, tests, migrations, docs, refactors and security-sensitive work. Re-run the set when models or agent tooling changes.

## 6. Preserve accountability

Every merged change should still have an accountable human owner. Agent-generated summaries are useful, but they should not replace diff review or ownership.

## 7. Roll out progressively

A practical progression:

```text
Stage 0  Chat/explanation only
Stage 1  Small local code generation
Stage 2  Multi-file edits with tests
Stage 3  Repository agent with bounded tools
Stage 4  Parallel/subagent workflows
Stage 5  Automated low-risk issue/PR workflows with monitoring
```

Move stages because measured reliability justifies it—not because a new feature exists.

## 8. Incident response

Treat harmful AI-generated changes like other engineering incidents. Capture:

1. task and instructions;
2. model/agent/tool version;
3. available context and permissions;
4. tool trajectory/logs;
5. resulting diff;
6. tests/reviews that failed to catch it;
7. corrective controls.

Prefer fixing the system—tests, permissions, instructions, CI—over merely telling users to “prompt more carefully.”
