---
title: "Custom agents for GitHub Copilot"
date: "2025-10-28"
type: "new releases"
labels: ["copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-custom-agents-for-github-copilot"
fetched_at: "2026-02-03T14:40:06.671136Z"
---

# Custom agents for GitHub Copilot

## Overview
Custom agents for GitHub Copilot make it easy for users and organizations to specialize their Copilot coding agent (CCA) through simple, file-based configurations.

## Detailed Explanation
### Overview
- Custom agents for GitHub Copilot make it easy for users and organizations to specialize their Copilot coding agent (CCA) through simple, file-based configurations.
- By adding a configuration file under .github/agents in any repository or in the agents folder in the {org}/.github or {org}/.github-private repository, you can define agent personas that capture your team’s workflows, conventions, and unique needs. These agents can be further tailored with prompts, tool selections, and Model Context Protocol (MCP) servers to optimize for specific use cases.
- Anyone using GitHub Copilot can define and use custom agents, whether you’re an individual developer, part of a team, or managing an organization. Custom agents work across Copilot coding agent in github.com, the Copilot CLI, and will be coming to a future release of Visual Studio Code.

### Key benefits
- Define agent specializations that act like focused teammates, using prompts and tool selections unique to your workflow.
- Add organization-specific or team-specific agents by placing configuration files in a known location in your repository or organization settings.
- Refine agent behaviors beyond standard Copilot instructions, making it easier to enforce coding conventions, compliance, or custom automations.
- Enable agents to use custom tools and MCP servers, giving you fine-grained control over how tasks are completed.
- Get started quickly by adding a simple markdown file. There’s no need for a separate installation or complex setup.

### Examples
- Imagine a frontend engineer subagent that enforces team conventions for React or Vue, or an agent that uses a custom MCP to automate additional tasks with the GitHub CLI. With custom agents, you can define these behaviors in a central file, making them easily accessible and maintainable.
- Not sure where to begin? Some of our awesome partners have created custom agents to help you improve your workflow.
- You can find those and more sample agents at @github/awesome-copilot .
- Learn more by reading our docs on custom agents and join the discussion within GitHub Community .

## Insights (derived from article language)
- Not sure where to begin?
- Learn more by reading our docs on custom agents and join the discussion within GitHub Community .

## Article Content (cleaned)
Custom agents for GitHub Copilot make it easy for users and organizations to specialize their Copilot coding agent (CCA) through simple, file\-based configurations.


By adding a configuration file under `.github/agents` in any repository or in the `agents` folder in the `{org}/.github` or `{org}/.github-private` repository, you can define agent personas that capture your team’s workflows, conventions, and unique needs. These agents can be further tailored with prompts, tool selections, and Model Context Protocol (MCP) servers to optimize for specific use cases.


Anyone using GitHub Copilot can define and use custom agents, whether you’re an individual developer, part of a team, or managing an organization. Custom agents work across Copilot coding agent in github.com, the Copilot CLI, and will be coming to a future release of Visual Studio Code.


### [Key benefits](#key-benefits)


* Define agent specializations that act like focused teammates, using prompts and tool selections unique to your workflow.
* Add organization\-specific or team\-specific agents by placing configuration files in a known location in your repository or organization settings.
* Refine agent behaviors beyond standard Copilot instructions, making it easier to enforce coding conventions, compliance, or custom automations.
* Enable agents to use custom tools and MCP servers, giving you fine\-grained control over how tasks are completed.
* Get started quickly by adding a simple markdown file. There’s no need for a separate installation or complex setup.


### [Examples](#examples)


Imagine a frontend engineer subagent that enforces team conventions for React or Vue, or an agent that uses a custom MCP to automate additional tasks with the GitHub CLI. With custom agents, you can define these behaviors in a central file, making them easily accessible and maintainable.


Not sure where to begin? Some of our awesome partners have created custom agents to help you improve your workflow.  

![Custom agent launch partners](https://github.com/user-attachments/assets/1d77e22d-4ce2-415e-b91c-5332167f7873)


You can find those and more sample agents at [@github/awesome\-copilot](https://github.com/github/awesome-copilot?utm_source=changelog-awesome-copilot-cutom-agents&utm_medium=changelog&utm_campaign=universe25).


Learn more by reading [our docs on custom agents](https://gh.io/customagents?utm_source=changelog-docs-custom-agents&utm_medium=changelog&utm_campaign=universe25) and join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/177930?utm_source=changelog-community-custom-agents&utm_medium=changelog&utm_campaign=universe25).
