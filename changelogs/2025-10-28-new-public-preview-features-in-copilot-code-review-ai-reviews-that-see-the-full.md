---
title: "New public preview features in Copilot code review: AI reviews that see the full picture"
date: "2025-10-28"
type: "new releases"
labels: ["copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-new-public-preview-features-in-copilot-code-review-ai-reviews-that-see-the-full-picture"
fetched_at: "2026-02-03T14:50:55.542154Z"
---

# New public preview features in Copilot code review: AI reviews that see the full picture

## Overview
Copilot code review (CCR) now blends LLM detections and tool calling with deterministic tools like ESLint and CodeQL, delivering smarter reviews and a seamless handoff to the Copilot coding agent for fixes.

## Detailed Explanation
### Overview
- Copilot code review (CCR) now blends LLM detections and tool calling with deterministic tools like ESLint and CodeQL, delivering smarter reviews and a seamless handoff to the Copilot coding agent for fixes.

### Rich context with tool calling 🧰
- CCR now leverages agentic tool calling to actively gather full project context, including code, directory structure, and references. This enables CCR to understand how your changes fit within the broader project architecture.
- 💡 Why it matters: Feedback is specific, accurate, and with less noise, helping you ship cleaner code faster.

### New deterministic detections with CodeQL and ESLint🕵️‍♀️
- CCR will soon integrate CodeQL and leading linters (starting with ESLint) to combine semantic analysis and classic rule-based checks. This fusion of LLM intelligence and deterministic precision will deliver high-signal, consistent findings for security and quality.
- 💡 Why it matters: Developers can trust that critical issues, from security vulnerabilities to maintainability problems, are reliably caught and clearly explained.
- Editor’s note (October 31, 2025): Updated the why it matters description.

### Seamless handoff to Copilot coding agent 🤝
- You can now hand off suggested changes directly to the Copilot coding agent . Mention @copilot in your pull request, and CCR will automatically apply the suggested fixes in a stacked pull request, ready for you to review and merge.
- 💡 Why it matters: Less manual cleanup and fewer review cycles. So you stay focused on higher-value engineering work.
- [Demo video: Use of implement suggestion button from CCR comment]

### Customizable workflows and editor availability 🛠️
- With customizable workflows and multi-editor support already generally available, CCR now fits seamlessly into every step of your development process, from writing code to reviewing and merging.
- Teams can define their own review standards and tone through instructions.md or copilot-instructions.md files, shaping what CCR prioritizes (e.g., test coverage, performance, or readability). CCR is available in VS Code, Visual Studio, JetBrains, Xcode, and on github.com, ensuring consistent feedback wherever you work.
- 💡 Why it matters: CCR adapts to your team’s standards and meets you where you work.

### Getting started 🚀
- Tool calling and deterministic detections are in public preview, enabled by default for Copilot Pro and Copilot Pro Plus users. Copilot Business and Copilot Enterprise users can opt in using the Copilot code review policies.
- Join the discussion within GitHub Community .

## Impact / Who’s Affected
- So you stay focused on higher-value engineering work. [Demo video: Use of implement suggestion button from CCR comment] Customizable workflows and editor availability 🛠️ With customizable workflows and multi-editor support already generally available, CCR now fits seamlessly into every step of your development process, from writing code to reviewing and merging.
- Getting started 🚀 Tool calling and deterministic detections are in public preview, enabled by default for Copilot Pro and Copilot Pro Plus users.

## Caveats / Limitations
- Editor’s note (October 31, 2025): Updated the why it matters description.

## Article Content (cleaned)
Copilot code review (CCR) now blends LLM detections and tool calling with deterministic tools like ESLint and CodeQL, delivering smarter reviews and a seamless handoff to the Copilot coding agent for fixes.


### [Rich context with tool calling 🧰](#rich-context-with-tool-calling-%f0%9f%a7%b0)


CCR now leverages agentic tool calling to actively gather full project context, including code, directory structure, and references. This enables CCR to understand how your changes fit within the broader project architecture.


💡 *Why it matters:* Feedback is specific, accurate, and with less noise, helping you ship cleaner code faster.


![Diagram of tools in Copilot code review](https://github.com/user-attachments/assets/6de9a8a5-eb27-4075-8e89-038a6a823b8c)


### [New deterministic detections with CodeQL and ESLint🕵️‍♀️](#new-deterministic-detections-with-codeql-and-eslint%f0%9f%95%b5%ef%b8%8f%e2%99%80%ef%b8%8f)


CCR will soon integrate CodeQL and leading linters (starting with ESLint) to combine semantic analysis and classic rule\-based checks. This fusion of LLM intelligence and deterministic precision will deliver high\-signal, consistent findings for security and quality.


💡 *Why it matters:* Developers can trust that critical issues, from security vulnerabilities to maintainability problems, are reliably caught and clearly explained.


*Editor’s note (October 31, 2025\): Updated the why it matters description.*


### [Seamless handoff to Copilot coding agent 🤝](#seamless-handoff-to-copilot-coding-agent-%f0%9f%a4%9d)


You can now hand off suggested changes directly to the **Copilot coding agent**. Mention `@copilot` in your pull request, and CCR will automatically apply the suggested fixes in a stacked pull request, ready for you to review and merge.


💡 *Why it matters:* Less manual cleanup and fewer review cycles. So you stay focused on higher\-value engineering work.


\[Demo video: Use of implement suggestion button from CCR comment]


### [Customizable workflows and editor availability 🛠️](#customizable-workflows-and-editor-availability-%f0%9f%9b%a0%ef%b8%8f)


With customizable workflows and multi\-editor support already generally available, CCR now fits seamlessly into every step of your development process, from writing code to reviewing and merging.


Teams can define their own review standards and tone through `instructions.md` or `copilot-instructions.md` files, shaping what CCR prioritizes (e.g., test coverage, performance, or readability). CCR is available in VS Code, Visual Studio, JetBrains, Xcode, and on github.com, ensuring consistent feedback wherever you work.


💡 *Why it matters:* CCR adapts to your team’s standards and meets you where you work.


![Image of copilot-instructions.md containing a list of instructions for Copilot code review to follow written in plain text.](https://github.com/user-attachments/assets/97de7185-908c-4702-bc5c-7dc2dafe5b09)


### [Getting started 🚀](#getting-started-%f0%9f%9a%80)


Tool calling and deterministic detections are in public preview, enabled by default for Copilot Pro and Copilot Pro Plus users. Copilot Business and Copilot Enterprise users can opt in using the Copilot code review policies.


Join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/177790?utm_source=changelog-community-copilot-code-review&utm_medium=changelog&utm_campaign=universe25).
