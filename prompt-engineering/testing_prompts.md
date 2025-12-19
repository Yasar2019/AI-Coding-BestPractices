# Techniques for Testing and Refining Prompts

This guide outlines strategies for testing and refining prompts to improve effectiveness and reliability.

**Last updated:** 2025-12-19

---

## 1) Start Simple
Begin with a basic prompt to gauge model behavior.

**Example:**
```
What is recursion?
```

---

## 2) Evaluate Output Quality
Check for:
- **Accuracy** (is it correct?)
- **Relevance** (does it answer the question?)
- **Clarity** (is it readable?)
- **Completeness** (does it cover key details?)

---

## 3) Add Context
If the response is too generic, add constraints or background.

**Example:**
```
Explain recursion to a beginner using a real-world analogy in under 120 words.
```

---

## 4) Iterate Systematically
Use a feedback loop:
1. Prompt → Output
2. Identify weaknesses
3. Refine
4. Repeat

---

## 5) Test Edge Cases
Use unusual or boundary inputs to expose weaknesses.

**Example:**
```
Generate a step-by-step recipe for making bread using only ingredients available on Mars.
```

---

## 6) Use Structure
Structured prompts produce predictable outputs.

**Example:**
```
List three advantages and three disadvantages of microservices.
```

---

## 7) Document What Works
Track successful prompts and templates for reuse.

---

## References
- OpenAI Docs: https://platform.openai.com/docs
- Prompting Guide: https://www.promptingguide.ai/
