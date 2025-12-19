# Prompt Engineering: Tips and Examples

Prompt engineering is the practice of crafting clear instructions so AI systems return **useful, reliable** results. This guide focuses on professional usage patterns and verification.

**Last updated:** 2025-12-19

---

## 🎯 What Is Prompt Engineering?

Prompt engineering is the process of shaping inputs to guide AI models toward the desired output. Clear prompts reduce ambiguity, improve consistency, and help you verify results.

**References:**
- OpenAI API docs: https://platform.openai.com/docs
- Anthropic Claude docs: https://docs.anthropic.com/

---

## 📋 General Tips

### 1) Be Specific
- Provide clear instructions and relevant context.
- Example:
  - **Before:** "Summarize this text."
  - **After:** "Summarize this text in 100 words, highlighting risks and recommendations."

### 2) Set Explicit Constraints
- Define output length, format, and tone.
- Example: "Return JSON with fields: title, summary, risks."

### 3) Use Examples
- Few-shot examples reduce ambiguity.
- Example:
  - **Input:** “The ball was thrown by John.”
  - **Output:** “John threw the ball.”

### 4) Iterate
- Start simple and refine based on outputs.
- Ask for assumptions and edge cases.

### 5) Ask for Checks
- Add explicit requests for tests, validation, or citations.

---

## 🔧 Prompt Examples

### Summarization
```
Summarize this article in 75 words for a non-technical audience.
Include the main conclusion and any stated limitations.
```

### Code Assistance
```
Write a Python function that validates email addresses.
Constraints: no external dependencies, return bool.
Add unit tests.
```

### Debugging
```
Review this stack trace and code.
Explain the root cause and propose a minimal fix.
```

---

## 📊 Measuring Prompt Effectiveness

| Metric | What to Check |
|--------|---------------|
| Accuracy | Correctness vs. expected result |
| Relevance | Does it answer the question? |
| Clarity | Is the output understandable? |
| Efficiency | Does it avoid unnecessary content? |

---

## 🧠 Advanced Techniques

### 1) Multi-Step Prompts
Break complex tasks into steps to reduce errors.

### 2) Role Assignment
"You are a senior backend engineer…" can anchor expertise and tone.

### 3) Context Control
State what the model **should ignore** to avoid irrelevant output.

---

## 🧪 Testing Prompts

See **[testing_prompts.md](testing_prompts.md)** for systematic refinement strategies.

---

## 📚 Resources

- OpenAI Docs: https://platform.openai.com/docs
- Prompt Engineering Guide: https://www.promptingguide.ai/
- Anthropic Claude Docs: https://docs.anthropic.com/
