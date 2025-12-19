# AI Coding Cheat Sheet (Professional Edition)

A concise, practical guide for using AI in software engineering — from prompt design to verification, security, and documentation.

**Last updated:** 2025-12-19

---

## 1) Golden Rules (Read First)

1. **Verify everything.** Treat AI output as a draft, not truth. Validate with tests, logs, and official docs.
2. **Be explicit.** Clear scope, constraints, and success criteria improve output quality.
3. **Protect sensitive data.** Never paste secrets or proprietary data into tools that don’t allow it.
4. **Use AI to accelerate, not replace, engineering judgment.**
5. **Cite sources in documentation and decisions.** When it matters, link the official source.

**References:**
- OpenAI API documentation: https://platform.openai.com/docs
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework

---

## 2) Quick Workflow (End-to-End)

1. **Define the task** (inputs, outputs, constraints).
2. **Ask for a plan** (list steps and assumptions).
3. **Generate a draft** (code or text).
4. **Review for correctness** (edge cases, security, performance).
5. **Verify with tests** (unit, integration, linting).
6. **Document changes** (include citations for external facts).

---

## 3) Prompt Patterns That Work

### A) Code Generation (Reliable Output)
```
You are a senior software engineer. 
Task: Implement [feature] in [language/framework].
Constraints: [time/space complexity, dependencies, conventions].
Inputs: [data shapes, types, edge cases].
Outputs: [function signature, return format].
Also provide: tests + reasoning + any assumptions.
```

### B) Debugging
```
You are a debugger. 
Given the error and code, identify the root cause and propose fixes.
Include: failing line(s), explanation, and a patch suggestion.
Error:
[stack trace]
Code:
[snippet]
```

### C) Code Review
```
Review the following code for: correctness, security, performance, style.
Return a list with severity (low/medium/high) and concrete fixes.
```

### D) Documentation
```
Summarize this feature for README.md in ~150 words.
Include: purpose, usage, examples, and limitations.
```

---

## 4) Verification Checklist (Before You Ship)

- ✅ Tests added or updated
- ✅ Edge cases considered
- ✅ Security risks reviewed (injection, auth, data exposure)
- ✅ Performance impact reviewed
- ✅ Citations for external facts and claims

**References:**
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- GitHub Secure Development guides: https://docs.github.com/en/code-security

---

## 5) Security & Privacy Guardrails

- **Never paste secrets** (API keys, tokens, passwords) into AI prompts.
- **Redact or obfuscate** sensitive data before sharing.
- **Prefer local or enterprise tools** for confidential codebases.

**References:**
- OpenAI data usage policy: https://openai.com/policies
- GitHub Copilot trust & safety: https://docs.github.com/en/copilot

---

## 6) When AI Is Best (and When It Isn’t)

✅ **Great For:**
- Scaffolding boilerplate
- Explaining unfamiliar code
- Drafting tests
- Identifying potential edge cases
- Summarizing docs

⚠️ **Use Caution:**
- Security-critical code
- Financial / legal logic
- Complex concurrency
- Licensing-sensitive code

---

## 7) Evaluation: How to Measure Quality

| Dimension | What to Check | Example Signal |
|----------|---------------|----------------|
| Accuracy | Correct output? | Tests pass | 
| Coverage | Handles edge cases? | Explicit tests | 
| Security | No unsafe patterns? | Lint/SAST flags | 
| Maintainability | Readable, well-structured? | Clear naming | 
| Performance | Meets constraints? | Benchmarks | 

---

## 8) High-Quality Sources to Cite

- OpenAI Docs: https://platform.openai.com/docs
- GitHub Copilot Docs: https://docs.github.com/en/copilot
- Anthropic Claude Docs: https://docs.anthropic.com/
- Google Gemini Docs: https://ai.google.dev/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- ACM Digital Library (research): https://dl.acm.org/
- arXiv (research preprints): https://arxiv.org/

---

## 9) One-Minute Prompt Upgrade

**Before:**
```
Fix this bug.
```

**After:**
```
Act as a senior debugger.
Given the stack trace, explain the root cause and propose a minimal patch.
List the exact file + line changes.
Add tests to prevent regression.
```

---

## 10) Quick Templates (Copy/Paste)

### Unit Test Generation
```
Write unit tests for [function/class].
Include edge cases and failure paths.
Use [test framework].
```

### Refactor for Readability
```
Refactor this code to improve readability.
Preserve behavior and add comments for non-obvious logic.
```

### Summarize a File
```
Summarize this file in 5 bullet points.
Highlight risks and TODOs.
```

---

## 11) Reminder for Responsible Use

AI can be a powerful accelerator, but production-quality results come from **verification**, **testing**, and **engineering judgment**.
