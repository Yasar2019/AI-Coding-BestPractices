# Verification-First AI Coding

AI coding becomes reliable when every important claim can be converted into evidence.

## Verification ladder

Use the strongest practical evidence available:

1. **Static structure** — syntax, formatting, types, imports.
2. **Unit behavior** — focused tests for functions/classes.
3. **Integration behavior** — interactions between modules/services.
4. **System behavior** — end-to-end workflows.
5. **Security evidence** — SAST, dependency scans, authorization tests, threat modeling.
6. **Performance evidence** — benchmark under representative load.
7. **Production evidence** — telemetry, canaries, rollback readiness.

Passing a lower level does not imply the higher levels are correct.

## Before asking an agent to code

Write acceptance criteria that can be checked independently. Good criteria are observable:

```text
Given an expired session token,
when the user requests /account,
then the API returns 401,
no account data is included,
and an authentication failure is logged without the token value.
```

## During implementation

Prefer short loops:

```text
inspect → edit → test → inspect failure → edit → retest
```

A long, unobserved implementation run accumulates assumptions and makes failures harder to localize.

## After implementation

Ask these questions:

- Which acceptance criterion does each test prove?
- Which behavior is still untested?
- Did the patch change public interfaces?
- Did it add dependencies or permissions?
- Is error handling observable and safe?
- Can we reproduce the claimed result from a clean checkout?

## Review generated tests too

AI-generated tests can encode the same misunderstanding as AI-generated implementation. Watch for:

- assertions that only confirm mocks;
- missing negative/failure cases;
- tests coupled to implementation details;
- snapshots that accept incorrect output wholesale;
- tests that never execute the risky branch;
- flaky timing assumptions.

## Definition of done template

```text
[ ] Acceptance criteria are explicit
[ ] Relevant automated tests pass
[ ] Type/lint/static checks pass
[ ] Security-sensitive paths reviewed
[ ] New dependencies justified and scanned
[ ] Diff contains no unrelated changes
[ ] Runtime behavior manually checked where useful
[ ] Documentation updated
[ ] Remaining uncertainty is stated explicitly
```

## Principle

> The model proposes. The environment tests. The engineer decides.
