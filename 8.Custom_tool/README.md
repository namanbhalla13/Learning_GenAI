# 🧠 LangChain Tools – Notes & README

This document explains **3 ways to create tools in LangChain**:

1. `@tool` decorator (simple & quick)
2. `StructuredTool` (with schema control)
3. `BaseTool` (fully customizable)

---

# 📌 1. Using `@tool` Decorator

* `@tool` automatically converts a function into a LangChain tool
* Infers:

  * name → function name
  * description → docstring
  * args → function parameters

## 🟢 Output Understanding

* `result` → function execution output
* `name` → tool name (`multiply`)
* `description` → taken from docstring
* `args` → input parameters
* `args_schema` → JSON schema for inputs

## 👍 When to Use

* Quick prototyping
* Simple tools
* Minimal configuration needed

---

# 📌 2. Using `StructuredTool`

* Uses **Pydantic schema** for input validation
* Explicitly define:

  * input structure
  * descriptions
* More control than `@tool`

## 🟢 Key Features

* Input validation
* Better documentation
* Clear schema for LLMs

## 👍 When to Use

* When input needs validation
* When working with structured agents
* When clarity & schema matter

---

# 📌 3. Using `BaseTool` (Custom Tool)


* Full control over tool behavior
* Define:

  * name
  * description
  * schema
  * execution logic (`_run`)

## 🟢 Key Features

* Maximum flexibility
* Can add:

  * async support (`_arun`)
  * custom logic
  * external APIs
  * logging / retries

## 👍 When to Use

* Complex tools
* Production systems
* Custom execution logic needed

---

# 🔍 Comparison Table

| Feature          | @tool     | StructuredTool | BaseTool |
| ---------------- | --------- | -------------- | -------- |
| Ease of use      | ⭐⭐⭐⭐⭐     | ⭐⭐⭐⭐           | ⭐⭐       |
| Input validation | ❌         | ✅              | ✅        |
| Customization    | ❌         | ⚠️ Limited     | ✅        |
| Best for         | Quick use | Structured use | Advanced |

---

# 🚀 Summary

* Use **`@tool`** → for quick and simple tools
* Use **`StructuredTool`** → for structured input & validation
* Use **`BaseTool`** → for full customization and production use
