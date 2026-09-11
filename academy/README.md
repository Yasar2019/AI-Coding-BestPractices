# AI Coding Academy

The Academy turns this repository into a structured, practice-first learning system for modern AI-assisted and agentic software engineering.

## Philosophy

Strong AI coding practice combines software engineering fundamentals, context design, agent/tool orchestration, verification, debugging, security, evaluation, and judgment about when *not* to use AI.

Every module follows:

> **Learn → Predict → Try → Verify → Reflect**

## Curriculum map

| Level | Module | Outcome |
|---|---|---|
| 0 | Foundations | Understand what coding assistants and agents can/cannot do |
| 1 | Context Engineering | Give an agent the smallest sufficient context for reliable work |
| 2 | Verification | Convert requirements into executable evidence |
| 3 | Agentic Workflows | Run reproduce-inspect-plan-edit-test-review loops |
| 4 | Security | Bound tools, secrets, network and destructive actions |
| 5 | Evaluation | Compare agent configurations on representative tasks |
| 6 | Team Systems | Build governed workflows for shared repositories |
| 7 | Advanced Agent Design | Decomposition, subagents, memory, tools and recovery strategies |

## Current labs

1. [Lab 01 — Context Engineering](labs/lab-01-context-engineering.md)
2. [Lab 02 — Verification Engineering](labs/lab-02-verification-engineering.md)
3. [Lab 03 — Agentic Debugging](labs/lab-03-agentic-debugging.md)
4. [Lab 04 — Prompt Injection](labs/lab-04-prompt-injection.md)
5. [Lab 05 — Least Privilege](labs/lab-05-least-privilege.md)
6. [Lab 06 — Secrets & Supply Chain](labs/lab-06-secrets-supply-chain.md)
7. [Lab 07 — Evaluation Engineering](labs/lab-07-evaluation-engineering.md)

Labs 02 and 03 include runnable Python exercises with intentional defects. Labs 04–06 are safe defensive security simulations. Lab 07 introduces reproducible internal evaluation and the repository's lightweight evaluation harness.

## Run the exercises

```bash
cd academy/exercises/order_total
python -m unittest -v

cd ../retry_helper
python -m unittest -v
```

The initial failures are intentional. Repair the implementation **without weakening the tests**.

## Run the evaluation demo

From the repository root:

```bash
python evaluation/harness.py evaluation/sample_results.jsonl
```

The sample results are synthetic. They demonstrate the format and reporting methodology only.

## Interactive Academy

Open [academy/index.html](index.html) for the browser-based Academy experience. It includes:

- module navigation;
- local progress tracking;
- verification and debugging checks;
- security scenario checks;
- a permission-risk matrix;
- direct links to labs and exercises.

Progress is stored locally in the browser; there is no account or backend dependency.

## Security operating model

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

Repository text, webpages, issue bodies, dependency metadata, logs, and tool outputs can contain untrusted or adversarial instructions. Treat them as data unless an explicitly trusted source designates them as instructions.

## Evaluation operating model

```text
REPRESENTATIVE TASKS
  ↓
FROZEN CONFIGURATION
  ↓
MULTIPLE OUTCOME METRICS
  ↓
FAILURE ANALYSIS
  ↓
REPEAT / VERSION
  ↓
DEPLOYMENT DECISION
```

Do not collapse task success, safety, cost, latency, and human effort into one opaque number unless you can justify the weighting for your actual workload.

## Scoring model

The Academy uses four core dimensions:

- **Correctness** — does the implementation satisfy the specification?
- **Evidence** — is there independent verification?
- **Safety** — was the blast radius appropriately controlled?
- **Understanding** — can the learner explain the change and trade-offs?

For evaluation work, add:

- **Representativeness** — do tasks resemble real work?
- **Reproducibility** — can the configuration be rerun?
- **Failure visibility** — do you record how systems fail, not only whether they pass?

## Public preview status

The Academy is usable now and still expanding. Next work will focus on repository-scale tasks, richer evaluation statistics, code-review exercises, multi-agent workflows, and public-site deployment.

See [../ROADMAP.md](../ROADMAP.md).
