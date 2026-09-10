# Lab 06 — Secrets, Dependencies, and Supply-Chain Risk

## Goal

Learn to stop an AI coding workflow from turning a small implementation task into a secret-handling or dependency-chain incident.

## Scenario

You ask an agent to add CSV export to an internal tool. It proposes:

1. reading `.env` to find an API token “in case the export library needs cloud access”;
2. installing a newly discovered package named `fast-csv-export-plus` from a public registry;
3. running the package's post-install script;
4. committing the generated lockfile and export code;
5. skipping dependency review because “the package is popular enough.”

None of those extra actions are required by the feature specification.

## Exercise

For each proposal, classify it as:

- justified;
- unjustified;
- requires explicit human approval.

Then redesign the workflow so the feature can be implemented with the smallest reasonable trust surface.

## Recommended secure workflow

1. Confirm whether the standard library or an already-approved dependency can perform CSV serialization.
2. Do **not** read `.env`, credentials, tokens, SSH keys, browser profiles, or cloud configuration unless the task explicitly requires them.
3. If a new dependency is truly needed:
   - verify the exact package name and publisher;
   - inspect release history and maintenance status;
   - review license and security advisories;
   - pin or constrain the version appropriately;
   - inspect install/build scripts when relevant;
   - run dependency/security scanning;
   - obtain human approval before introducing it into a sensitive codebase.
4. Run tests with synthetic data.
5. Review the diff and lockfile separately.

## Secret-handling rules

- Never include real secrets in prompts, examples, logs, fixtures, screenshots, generated documentation, or commits.
- Prefer fake values such as `example-token-not-real` in educational material.
- If a secret is accidentally exposed, treat it as compromised: rotate/revoke it and remove it from accessible history according to your organization's incident process.
- Do not assume a secret is safe merely because a repository is private.

## Supply-chain checklist

- [ ] Exact package identity verified
- [ ] Package source/maintainer reviewed
- [ ] Dependency is actually necessary
- [ ] Version policy defined
- [ ] Install scripts understood where relevant
- [ ] Known vulnerabilities checked
- [ ] License acceptable
- [ ] Lockfile reviewed
- [ ] No unexpected transitive dependency explosion
- [ ] No credentials required for an otherwise local feature

## Reflection

AI agents reduce the friction of adding dependencies—which is useful, but also dangerous. A one-line package-install suggestion can introduce thousands of lines of transitive code and executable install hooks. Treat dependency introduction as a security-relevant architecture decision, not as harmless autocomplete.

## References

- GitHub, dependency and supply-chain security: https://docs.github.com/en/code-security/supply-chain-security
- OpenSSF, best practices and software supply-chain resources: https://openssf.org/
- OWASP, Software Component Verification Standard / dependency guidance: https://owasp.org/
