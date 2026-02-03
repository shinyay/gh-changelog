---
title: "GitHub Copilot CLI: Use custom agents and delegate to Copilot coding agent"
date: "2025-10-28"
type: "improvements"
labels: ["client apps", "copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-github-copilot-cli-use-custom-agents-and-delegate-to-copilot-coding-agent"
fetched_at: "2026-02-03T14:50:55.673183Z"
---

# GitHub Copilot CLI: Use custom agents and delegate to Copilot coding agent

## Overview
Since our initial public preview release, we’ve shipped daily improvements to GitHub Copilot CLI. In addition to listening to feedback from developers like you in our public repository, we’ve been working on some larger features that make Copilot CLI more extensible and more connected to the broader GitHub Copilot ecosystem.

## Detailed Explanation
### Overview
- Since our initial public preview release, we’ve shipped daily improvements to GitHub Copilot CLI. In addition to listening to feedback from developers like you in our public repository, we’ve been working on some larger features that make Copilot CLI more extensible and more connected to the broader GitHub Copilot ecosystem.

### Custom agents are available in GitHub Copilot CLI
- Custom agents are now available in GitHub Copilot , allowing you to define agent personas that capture your team’s workflows, conventions, and unique needs. You can further tailor these agents with prompts, tool selections, and Model Context Protocol (MCP) servers to optimize for specific use cases.
- In addition to defining agents under .github/agents in a repository or in the {org}/.github repository, GitHub Copilot CLI will recognize custom agent configurations in ~/.copilot/agents .
- You can explicitly invoke an agent interactively with the /agent slash command. Your custom agents are also made available as tools to Copilot, and the model will start a new agentic loop using a relevant custom agent when necessary.

### Delegate tasks to Copilot coding agent from GitHub Copilot CLI
- Copilot coding agent is our asynchronous, autonomous background agent. Running the /delegate TASK-DESCRIPTION slash command from GitHub Copilot CLI will commit any unstaged changes to a new branch. After that, Copilot coding agent will open a draft pull request, make changes in the background, and then request a review from you. Copilot will provide a link to the pull request and its coding agent’s session in your terminal once this process begins.

### Streaming, parallel tool calling, improved performance
- Copilot’s output now streams to your terminal token-by-token, providing snappier feedback.
- Copilot can execute multiple tool calls in parallel, speeding up completion time on more complex tasks.
- We’ve made continued performance improvements to GitHub Copilot CLI, including decreasing the application’s memory footprint and fixing screen flickering bugs.

### Share your feedback
- Update GitHub Copilot CLI by running npm install -g @github/copilot@latest in your terminal. Thank you to everyone who has submitted feedback via the /feedback command and by opening issues in our public repository . Your continued feedback is invaluable as we continue to ship improvements daily.

## Impact / Who’s Affected
- Since our initial public preview release, we’ve shipped daily improvements to GitHub Copilot CLI.
- Custom agents are available in GitHub Copilot CLI Custom agents are now available in GitHub Copilot , allowing you to define agent personas that capture your team’s workflows, conventions, and unique needs.

## Article Content (cleaned)
Since our initial public preview release, we’ve shipped [daily improvements](https://github.com/github/copilot-cli/releases?utm_source=changelog-copilot-cli&utm_medium=changelog&utm_campaign=universe25) to GitHub Copilot CLI. In addition to listening to feedback from developers like you in our public repository, we’ve been working on some larger features that make Copilot CLI more extensible and more connected to the broader GitHub Copilot ecosystem.


## [Custom agents are available in GitHub Copilot CLI](#custom-agents-are-available-in-github-copilot-cli)


[Custom agents are now available in GitHub Copilot](https://github.blog/changelog/2025-11-27-custom-agents-for-github-copilot/), allowing you to define agent personas that capture your team’s workflows, conventions, and unique needs. You can further tailor these agents with prompts, tool selections, and Model Context Protocol (MCP) servers to optimize for specific use cases.


In addition to defining agents under `.github/agents` in a repository or in the `{org}/.github` repository, GitHub Copilot CLI will recognize custom agent configurations in `~/.copilot/agents`.


You can explicitly invoke an agent interactively with the `/agent` slash command. Your custom agents are also made available as tools to Copilot, and the model will start a new agentic loop using a relevant custom agent when necessary.


## [Delegate tasks to Copilot coding agent from GitHub Copilot CLI](#delegate-tasks-to-copilot-coding-agent-from-github-copilot-cli)


[Copilot coding agent](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent?utm_source=changelog-docs-copilot-cli&utm_medium=changelog&utm_campaign=universe25) is our asynchronous, autonomous background agent. Running the `/delegate TASK-DESCRIPTION` slash command from GitHub Copilot CLI will commit any unstaged changes to a new branch. After that, Copilot coding agent will open a draft pull request, make changes in the background, and then request a review from you. Copilot will provide a link to the pull request and its coding agent’s session in your terminal once this process begins.


## [Streaming, parallel tool calling, improved performance](#streaming-parallel-tool-calling-improved-performance)


* Copilot’s output now streams to your terminal token\-by\-token, providing snappier feedback.
* Copilot can execute multiple tool calls in parallel, speeding up completion time on more complex tasks.
* We’ve made continued performance improvements to GitHub Copilot CLI, including decreasing the application’s memory footprint and fixing screen flickering bugs.


## [Share your feedback](#share-your-feedback)


Update GitHub Copilot CLI by running `npm install -g @github/copilot@latest` in your terminal. Thank you to everyone who has submitted feedback via the `/feedback` command and by opening issues in [our public repository](https://github.com/github/copilot-cli?utm_source=changelog-copilot-cli&utm_medium=changelog&utm_campaign=universe25). Your continued feedback is invaluable as we continue to ship improvements daily.
