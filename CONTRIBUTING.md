# Contributing to AI Coding Best Practices

Thank you for helping improve this project. Contributions are welcome from beginners, working engineers, researchers, educators, security practitioners, and engineering teams.

The goal is not to collect as much AI content as possible. The goal is to build a **maintainable, evidence-backed, practical learning resource**.

## High-value contributions

Especially useful contributions include:

- corrections to outdated or inaccurate claims;
- stronger primary sources for existing claims;
- reproducible Academy labs;
- representative evaluation tasks;
- real-world failure patterns with defensible evidence;
- security and governance improvements;
- accessibility and learning-design improvements;
- fixes to interactive content, tests, CI, or documentation.

## Before opening a pull request

1. Read [QUICKSTART.md](QUICKSTART.md) and [ROADMAP.md](ROADMAP.md).
2. Search existing issues and pull requests for similar work.
3. Keep the change focused enough to review independently.
4. Run the relevant local checks.

For major curriculum, architecture, or evaluation changes, opening an issue first is encouraged.

## Source and research policy

When adding a factual or time-sensitive claim:

1. Prefer the primary source.
2. Include the publication date when relevant.
3. State what population, benchmark, or task set the claim applies to.
4. Include material limitations.
5. Distinguish peer-reviewed work, preprints, vendor research, and practitioner reports.
6. Do not turn one benchmark snapshot into a timeless model ranking.
7. Do not cite a marketing claim as if it were independent evidence.

Preferred evidence order:

1. peer-reviewed publication or strong research preprint;
2. official benchmark/project documentation;
3. primary vendor engineering/research documentation;
4. standards and security organizations;
5. reputable secondary reporting when primary evidence is unavailable.

## Adding an Academy lab

A strong lab should include:

- target level and approximate scope;
- a concrete scenario;
- explicit learning objectives;
- an activity that requires judgment, not only reading;
- a verification or reflection step;
- completion criteria;
- source links when factual claims are involved.

Runnable labs should include tests where practical. Intentionally failing starter code is welcome when the failure is part of the learning design.

## Adding an evaluation task

Evaluation tasks should be:

- representative of a recognizable software-engineering activity;
- versionable;
- independently verifiable where possible;
- explicit about expected behavior;
- safe to execute in the intended environment.

Do not submit benchmark results without enough metadata to interpret them. At minimum record model/version, agent/harness, repository/task version, permissions, retries, verification, and interaction policy.

Synthetic or illustrative data **must** be labeled clearly and must never be presented as measured model performance.

## Code contributions

Create a focused branch:

```bash
git checkout -b feature/your-change
```

Keep code dependency-light unless a new dependency has a strong justification.

For Python changes in the current public preview, use the standard library where practical and add tests for behavior changes.

## Local checks

For the evaluation harness:

```bash
python -m unittest evaluation/test_harness.py -v
python evaluation/harness.py evaluation/sample_results.jsonl
```

For the Academy exercises:

```bash
cd academy/exercises/order_total
python -m unittest -v

cd ../retry_helper
python -m unittest -v
```

Note: the two Academy starter implementations are intentionally defective for teaching purposes, so their exercise suites are expected to fail until a learner fixes them. CI validates their syntax rather than requiring the starter exercises to pass.

## Pull request checklist

Before submitting a PR, confirm:

- [ ] The change has a clear purpose.
- [ ] New claims have appropriate sources and limitations.
- [ ] New links use the correct repository paths.
- [ ] New code has relevant tests.
- [ ] Synthetic/demo data is clearly labeled.
- [ ] Security controls were not weakened to make a demo pass.
- [ ] The change does not silently expand agent permissions or dependency scope.
- [ ] Documentation explains how another contributor can verify the change.

## Commit and PR quality

Use descriptive commits and a PR description that explains:

- what changed;
- why it changed;
- how it was verified;
- any known limitations or follow-up work.

## Security

Do not include real secrets, credentials, private customer data, proprietary code, or sensitive logs in issues, labs, fixtures, examples, or pull requests.

Security labs in this repository are defensive and simulation-based. Contributions should preserve that posture.

## Code of Conduct

Be respectful and constructive. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

By contributing, you agree that your contributions are licensed under the repository's [MIT License](LICENSE).

## Questions

Open an issue in this repository if the contribution path is unclear:

https://github.com/Yasar2019/AI-Coding-BestPractices/issues
