---
title: "Copilot code review and coding agent now support agent-specific instructions"
date: "2025-11-12"
type: "improvements"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-12-copilot-code-review-and-coding-agent-now-support-agent-specific-instructions"
fetched_at: "2026-02-03T14:50:55.315997Z"
---

# Copilot code review and coding agent now support agent-specific instructions

## Overview
You can now craft targeted custom instructions for Copilot code review and Copilot coding agent. The new excludeAgent property for .instructions.md custom instructions gives you exact control over when specific instructions apply.

## Detailed Explanation
### Overview
- You can now craft targeted custom instructions for Copilot code review and Copilot coding agent. The new excludeAgent property for .instructions.md custom instructions gives you exact control over when specific instructions apply.

### 🎯 Recap: Customizing Copilot using instructions.md files
- You can already use custom instruction files located in your .github/instructions directory to guide Copilot’s behavior for specific areas of your repository.
- The applyTo property lets you specify paths or directories with path globs, so your instructions apply where you want them to, and nowhere else. For example, you could create a models.instructions.md file which only applies to your models by specifying applyTo: "app/models/**/*.rb" .

### 🛡️ Introducing agent-specific repository instructions with excludeAgent
- The new excludeAgent property allows you to control which Copilot agents use a given instructions file:
- Set excludeAgent: "code-review" to hide your instructions file from Copilot code review.
- Set excludeAgent: "coding-agent" to hide your instructions file from Copilot coding agent.
- If you don’t have an excludeAgent property in your frontmatter, your instructions file will be used by all agents.
- This feature ensures you can tailor your guidance for each agent, reducing overlap and allowing you to provide focused, specific instructions.

### 🛠️ Other custom instructions improvements
- Copilot code review recently fixed a bug that prevented it from reading certain *.instructions.md files.
- For tips on how to write effective instructions files, check out this blog post !
- For details on creating instructions files, visit the Copilot instructions documentation .
- Join the discussion within GitHub Community .

## Key Changes
- Copilot code review recently fixed a bug that prevented it from reading certain *.instructions.md files.
- For tips on how to write effective instructions files, check out this blog post !
- For details on creating instructions files, visit the Copilot instructions documentation .
- Join the discussion within GitHub Community .

## Impact / Who’s Affected
- For example, you could create a models.instructions.md file which only applies to your models by specifying applyTo: "app/models/**/*.rb" . 🛡️ Introducing agent-specific repository instructions with excludeAgent The new excludeAgent property allows you to control which Copilot agents use a given instructions file: Set excludeAgent: "code-review" to hide your instructions file from Copilot code review.

## Caveats / Limitations
- For example, you could create a models.instructions.md file which only applies to your models by specifying applyTo: "app/models/**/*.rb" . 🛡️ Introducing agent-specific repository instructions with excludeAgent The new excludeAgent property allows you to control which Copilot agents use a given instructions file: Set excludeAgent: "code-review" to hide your instructions file from Copilot code review.

## Article Content (cleaned)
You can now craft targeted custom instructions for Copilot code review and Copilot coding agent. The new `excludeAgent` property for `.instructions.md` custom instructions gives you exact control over when specific instructions apply.


### [🎯 Recap: Customizing Copilot using `instructions.md` files](#%f0%9f%8e%af-recap-customizing-copilot-using-instructions-md-files)


You can already use custom instruction files located in your `.github/instructions` directory to guide Copilot’s behavior for specific areas of your repository.


The `applyTo` property lets you specify paths or directories with path globs, so your instructions apply where you want them to, and nowhere else. For example, you could create a `models.instructions.md` file which only applies to your models by specifying `applyTo: "app/models/**/*.rb"`.


### [🛡️ Introducing agent\-specific repository instructions with `excludeAgent`](#%f0%9f%9b%a1%ef%b8%8f-introducing-agent-specific-repository-instructions-with-excludeagent)


The new `excludeAgent` property allows you to control which Copilot agents use a given instructions file:


* Set `excludeAgent: "code-review"` to hide your instructions file from Copilot code review.
* Set `excludeAgent: "coding-agent"` to hide your instructions file from Copilot coding agent.


If you don’t have an `excludeAgent` property in your frontmatter, your instructions file will be used by all agents.


This feature ensures you can tailor your guidance for each agent, reducing overlap and allowing you to provide focused, specific instructions.


![Screenshot showing how to specify agent-specific instructions in .instructions.md files.](https://github.com/user-attachments/assets/2abfcfb4-3c6a-422b-8a02-02c923c46ae7)


### [🛠️ Other custom instructions improvements](#%f0%9f%9b%a0%ef%b8%8f-other-custom-instructions-improvements)


Copilot code review recently fixed a bug that prevented it from reading certain `*.instructions.md` files.


For tips on how to write effective instructions files, check out [this blog post](https://github.blog/ai-and-ml/unlocking-the-full-power-of-copilot-code-review-master-your-instructions-files)!




---


For details on creating instructions files, visit the [Copilot instructions documentation](https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions#creating-a-repository-custom-instructions-file).


Join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/categories/copilot-conversations).
