---
title: "Isolated Subagents for JetBrains, Eclipse, and Xcode now in public preview"
date: "2025-11-18"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-18-isolated-subagents-for-jetbrains-eclipse-and-xcode-now-in-public-preview"
fetched_at: "2026-02-03T14:50:55.228768Z"
---

# Isolated Subagents for JetBrains, Eclipse, and Xcode now in public preview

## Overview
We’re excited to share that isolated subagents are now in public preview across JetBrains IDEs, Eclipse, and Xcode! Empowered by isolated context, subagents let you delegate focused tasks to autonomous copilots without leaving your current chat session, so you can keep momentum while Copilot researches, designs APIs, reviews code, or gathers project context on your behalf. Each subagent operates within its own isolated context, ensuring your main conversation stays clean and focused.

## Detailed Explanation
### Overview
- We’re excited to share that isolated subagents are now in public preview across JetBrains IDEs, Eclipse, and Xcode! Empowered by isolated context, subagents let you delegate focused tasks to autonomous copilots without leaving your current chat session, so you can keep momentum while Copilot researches, designs APIs, reviews code, or gathers project context on your behalf. Each subagent operates within its own isolated context, ensuring your main conversation stays clean and focused.

### ✨ What’s new
- Dedicated subagent context – Each subagent runs with its own context, preventing long-running research or analysis prompts from crowding out your main conversation history.
- Autonomous execution – Once invoked, a subagent proceeds without further user interaction, making it ideal for background tasks such as documentation discovery, competitive analysis, or assembling technical context.

### ❓ How subagents work
- Prerequisites : You need custom agents configured in your environment. Read the custom agents documentation or ask copilot to list the available custom agents if you’re unsure what’s available.
- Subagents operate through two primary mechanisms:

### Automatic delegation
- Copilot proactively delegates tasks based on: – The task description in your request – The description field in custom agent configurations – Current context and available tools

### Explicit invocation
- Request a specific subagent by mentioning it in your command:

### 🛠 Try it out
- Getting started with subagents in supported IDEs is straightforward:
- Update your IDE : Make sure you’re running the latest GitHub Copilot extension in JetBrains IDEs, Eclipse, or Xcode.
- Open Copilot Chat : Start or continue a conversation in Copilot Chat.
- Invoke a subagent : Subagents can be auto-invoked based on your request, or you can explicitly call a specialized custom agent—complete with curated instructions and allowed tools—by referencing the available custom agents .
- Review the response : When the subagent completes its task, its results appear back in the main conversation, ready for follow-up questions or next steps.

### 💬 Share your feedback
- Your feedback drives our roadmap. Let us know how subagents are working for you by using the feedback controls in your IDE or through your existing Copilot support channels.
- In-product feedback : Use the feedback options within your IDE
- GitHub discussions : Share your thoughts in the following channels: JetBrains GitHub Copilot in JetBrains feedback repository Eclipse GitHub Copilot in Eclipse feedback repository Xcode GitHub Copilot in Xcode feedback repository
- JetBrains GitHub Copilot in JetBrains feedback repository
- Eclipse GitHub Copilot in Eclipse feedback repository
- Xcode GitHub Copilot in Xcode feedback repository
- Start delegating research and analysis to isolated subagents today, and keep your primary chat focused on shipping great code.

## Impact / Who’s Affected
- We’re excited to share that isolated subagents are now in public preview across JetBrains IDEs, Eclipse, and Xcode!

## Article Content (cleaned)
We’re excited to share that isolated subagents are now in public preview across JetBrains IDEs, Eclipse, and Xcode! Empowered by isolated context, subagents let you delegate focused tasks to autonomous copilots without leaving your current chat session, so you can keep momentum while Copilot researches, designs APIs, reviews code, or gathers project context on your behalf. Each subagent operates within its own isolated context, ensuring your main conversation stays clean and focused.


## [✨ What’s new](#%e2%9c%a8-whats-new)


* **Dedicated subagent context** – Each subagent runs with its own context, preventing long\-running research or analysis prompts from crowding out your main conversation history.
* **Autonomous execution** – Once invoked, a subagent proceeds without further user interaction, making it ideal for background tasks such as documentation discovery, competitive analysis, or assembling technical context.


## [❓ How subagents work](#%e2%9d%93-how-subagents-work)


**Prerequisites**: You need custom agents configured in your environment. Read the [custom agents documentation](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents) or ask copilot to `list the available custom agents` if you’re unsure what’s available.


Subagents operate through two primary mechanisms:


### [Automatic delegation](#automatic-delegation)


Copilot proactively delegates tasks based on:  

– The task description in your request  

– The **description** field in custom agent configurations  

– Current context and available tools


### [Explicit invocation](#explicit-invocation)


Request a specific subagent by mentioning it in your command:



```
> Have the code-reviewer subagent look at my recent changes
> Let the documentation subagent generate API docs for this module

```

## [🛠 Try it out](#%f0%9f%9b%a0-try-it-out)


Getting started with subagents in supported IDEs is straightforward:


1. **Update your IDE**: Make sure you’re running the latest GitHub Copilot extension in JetBrains IDEs, Eclipse, or Xcode.
2. **Open Copilot Chat**: Start or continue a conversation in Copilot Chat.
3. **Invoke a subagent**: Subagents can be auto\-invoked based on your request, or you can explicitly call a specialized custom agent—complete with curated instructions and allowed tools—by referencing the available [custom agents](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents).
4. **Review the response**: When the subagent completes its task, its results appear back in the main conversation, ready for follow\-up questions or next steps.


## [💬 Share your feedback](#%f0%9f%92%ac-share-your-feedback)


Your feedback drives our roadmap. Let us know how subagents are working for you by using the feedback controls in your IDE or through your existing Copilot support channels.


* **In\-product feedback**: Use the feedback options within your IDE
* **GitHub discussions**: Share your thoughts in the following channels:
	+ JetBrains [GitHub Copilot in JetBrains feedback repository](https://github.com/microsoft/copilot-jetbrains-feedback/issues)
	+ Eclipse [GitHub Copilot in Eclipse feedback repository](https://github.com/microsoft/copilot-eclipse-feedback/issues)
	+ Xcode [GitHub Copilot in Xcode feedback repository](https://github.com/github/CopilotForXcode/issues)


Start delegating research and analysis to isolated subagents today, and keep your primary chat focused on shipping great code.
