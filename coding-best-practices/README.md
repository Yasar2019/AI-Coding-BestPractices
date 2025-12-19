# Coding Best Practices with AI

This guide focuses on **reliability, safety, and professional workflows** when using AI coding assistants.

**Last updated:** 2025-12-19

---

## 1) Reliability First

- **Treat AI output as a draft.** Always verify with tests and documentation.
- **Use tight constraints.** Define inputs, outputs, edge cases, and error handling requirements.
- **Ask for reasoning + assumptions.** This makes hidden risks easier to spot.

**References:**
- OpenAI Docs: https://platform.openai.com/docs
- GitHub Copilot Docs: https://docs.github.com/en/copilot

---

## 2) Suggested Workflow

1. **Define the spec** (acceptance criteria, constraints).
2. **Ask AI for a plan** (with steps and dependencies).
3. **Generate a patch** (or multiple alternatives).
4. **Review for correctness and security.**
5. **Write or expand tests.**
6. **Document changes and cite sources.**

---

## 3) Verification Checklist

Use this checklist before merging AI-assisted changes:

- ✅ Unit tests updated/added
- ✅ Edge cases handled
- ✅ Linting & formatting clean
- ✅ No secrets or sensitive data added
- ✅ Security risks reviewed
- ✅ External claims include citations

**References:**
- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- GitHub Code Security Docs: https://docs.github.com/en/code-security

---

## 4) Secure Prompting & Data Safety

- **Never share secrets.** Use environment variables and secret managers instead.
- **Redact customer data.** Use synthetic or anonymized examples.
- **Prefer approved tools** for private codebases.

**References:**
- OpenAI policies: https://openai.com/policies
- GitHub Copilot trust & safety: https://docs.github.com/en/copilot

---

## 5) Code Review: AI-Specific Risks

**Common risks:**
- Hallucinated APIs or undocumented behavior
- Incorrect edge-case handling
- Insecure defaults (e.g., missing auth checks)
- Performance regressions

**Mitigation tips:**
- Verify every external API with official docs
- Require tests for edge cases
- Run static analysis where possible

---

## 6) Testing Guidance

- **Unit tests:** small, fast, deterministic
- **Integration tests:** real dependencies where possible
- **Golden files/snapshots:** for stable outputs
- **Regression tests:** after AI refactors

**References:**
- pytest docs: https://docs.pytest.org/
- JUnit 5 user guide: https://junit.org/junit5/docs/current/user-guide/

---

## 7) Documentation Standards

When AI helps generate or modify code:

- Explain **what** and **why** (not just the how)
- Add examples for critical workflows
- Cite external references

---

## 8) Example Prompt (Code Review)

```
You are a senior code reviewer.
Review this change for correctness, security, performance, and maintainability.
Return a list of issues with severity and concrete fixes.
```

---

## 9) When Not to Use AI

Avoid or heavily constrain AI usage for:

- Cryptography design
- Authentication & authorization logic
- Safety-critical systems
- Legal or regulatory compliance logic

---

## 10) Recommended Reading

- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- ACM Digital Library: https://dl.acm.org/
