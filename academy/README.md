# AI Coding Academy

The Academy turns this repository into a structured, practice-first learning system.

## Philosophy

AI coding is not a single skill. Strong practitioners combine software engineering fundamentals, context design, agent/tool orchestration, verification, security, evaluation, and judgment about when *not* to use AI.

Every module follows the same loop:

> **Learn → Predict → Try → Verify → Reflect**

## Curriculum map

| Level | Module | Outcome |
|---|---|---|
| 0 | Foundations | Understand what coding assistants and agents can/cannot do |
| 1 | Context Engineering | Give an agent the smallest sufficient context for reliable work |
| 2 | Verification | Convert requirements into executable evidence |
| 3 | Agentic Workflows | Run reproduce-inspect-plan-edit-test-review loops |
| 4 | Security | Bound tools, secrets, network and destructive actions |
| 5 | Evaluation | Compare models/agents on representative tasks |
| 6 | Team Systems | Build governed workflows for shared repositories |
| 7 | Advanced Agent Design | Decomposition, subagents, memory, tools and recovery strategies |

## Current labs

1. [Lab 01 — Context Engineering](labs/lab-01-context-engineering.md)
2. [Lab 02 — Verification Engineering](labs/lab-02-verification-engineering.md)
3. [Lab 03 — Agentic Debugging](labs/lab-03-agentic-debugging.md)
4. [Lab 04 — Prompt Injection](labs/lab-04-prompt-injection.md)
5. [Lab 05 — Least Privilege](labs/lab-05-least-privilege.md)
6. [Lab 06 — Secrets & Supply Chain](labs/lab-06-secrets-supply-chain.md)

Labs 02 and 03 include runnable Python exercises with intentional defects. Labs 04–06 are safe security simulations: they teach trust boundaries, permission design, secret handling, dependency review, and human approval gates without asking learners to perform destructive actions.

## Run the exercises

```bash
cd academy/exercises/order_total
python -m unittest -v

cd ../retry_helper
python -m unittest -v
```

The initial failures are intentional. Learners should repair the implementation **without weakening the tests**.

## Interactive Academy

Open [academy/index.html](index.html) for the browser-based Academy experience. It includes:

- module navigation;
- local progress tracking;
- verification and debugging knowledge checks;
- security scenario checks;
- a permission-risk decision matrix;
- direct links to labs and exercises.

Progress is stored locally in the browser; there is no account or backend dependency.

## Security operating model

Use this mental model whenever an agent can act on tools or external systems:

```text
TRUST BOUNDARY
  ↓
TASK NECESSITY
  ↓
LEAST PRIVILEGE
  ↓
APPROVAL FOR HIGH-BLAST-RADIUS ACTIONS
  ↓
INDEPENDENT VERIFICATION
  ↓
AUDITABLE DIFF / LOGS
```

Repository text, webpages, issue bodies, dependency metadata, logs, and tool outputs can all contain untrusted or adversarial instructions. Treat them as data unless an explicitly trusted source designates them as instructions.

## Scoring model

The Academy uses four core dimensions:

- **Correctness** — does the implementation satisfy the specification?
- **Evidence** — is there independent verification?
- **Safety** — was the blast radius appropriately controlled?
- **Understanding** — can the learner explain the change and trade-offs?

For security labs, add four more questions:

1. Did you identify the trust boundary?
2. Did you minimize capabilities?
3. Did you require approval before irreversible or external actions?
4. Did you verify that safeguards were not weakened to make the task pass?

## What comes next

The next phase will focus on **evaluation engineering**: model/agent comparison harnesses, task suites, cost/latency tracking, pass@k-style thinking, benchmark interpretation, and an internal-evals workflow that teams can adapt to their own repositories.
