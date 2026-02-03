---
title: "Configure Copilot coding agent as a bypass actor for rulesets"
date: "2025-11-13"
type: "improvements"
labels: ["copilot", "platform governance"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-13-configure-copilot-coding-agent-as-a-bypass-actor-for-rulesets"
fetched_at: "2026-02-03T14:40:06.090901Z"
---

# Configure Copilot coding agent as a bypass actor for rulesets

## Overview
Rulesets allow you to control how different actors can interact with a repository. You can use rulesets to enforce rules like:

## Detailed Explanation
### Overview
- Rulesets allow you to control how different actors can interact with a repository. You can use rulesets to enforce rules like:
- Only allow commits from email addresses that match a certain pattern.
- Ensure that commit messages follow a specific structure.
- Require commits to be signed.
- Copilot coding agent is our asynchronous developer agent that works in the background. It can’t always comply with every rule – for example, it can’t sign commits. When a repository includes rules that the agent can’t comply with, the agent is automatically disabled.
- Now, you can unblock usage of the coding agent by configuring Copilot coding agent as a bypass actor for select rulesets. This allows you to exempt Copilot from specific rules without relaxing your requirements for code pushed by humans.
- To learn more about Copilot coding agent, head to “About GitHub Copilot coding agent” in the GitHub Docs.

## Impact / Who’s Affected
- You can use rulesets to enforce rules like: Only allow commits from email addresses that match a certain pattern.

## Caveats / Limitations
- You can use rulesets to enforce rules like: Only allow commits from email addresses that match a certain pattern.

## Insights (derived from article language)
- To learn more about Copilot coding agent, head to “About GitHub Copilot coding agent” in the GitHub Docs.

## Article Content (cleaned)
[Rulesets](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) allow you to control how different actors can interact with a repository. You can use rulesets to enforce rules like:


* Only allow commits from email addresses that match a certain pattern.
* Ensure that commit messages follow a specific structure.
* Require commits to be signed.


[Copilot coding agent](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent) is our asynchronous developer agent that works in the background. It can’t always comply with every rule – for example, it can’t sign commits. When a repository includes rules that the agent can’t comply with, the agent is automatically disabled.


Now, you can unblock usage of the coding agent by [configuring Copilot coding agent as a bypass actor](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository#granting-bypass-permissions-for-your-branch-or-tag-ruleset) for select rulesets. This allows you to exempt Copilot from specific rules without relaxing your requirements for code pushed by humans.


To learn more about Copilot coding agent, head to [“About GitHub Copilot coding agent”](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent) in the GitHub Docs.
