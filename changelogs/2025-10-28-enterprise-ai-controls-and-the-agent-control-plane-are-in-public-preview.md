---
title: "Enterprise AI controls & the agent control plane are in public preview"
date: "2025-10-28"
type: "new releases"
labels: ["copilot", "enterprise management tools", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-enterprise-ai-controls-the-agent-control-plane-are-in-public-preview"
fetched_at: "2026-02-03T14:50:55.568122Z"
---

# Enterprise AI controls & the agent control plane are in public preview

## Overview
We’re introducing a new enterprise-level experience focused on administrative functions for AI systems, available today to all GitHub Enterprise Cloud customers using Copilot. This is your agent control plane, a suite of enterprise governance features designed to give organizations deeper control over how agents operate across their environments.

## Detailed Explanation
### Overview
- We’re introducing a new enterprise-level experience focused on administrative functions for AI systems, available today to all GitHub Enterprise Cloud customers using Copilot. This is your agent control plane, a suite of enterprise governance features designed to give organizations deeper control over how agents operate across their environments.
- Enterprise administrators are often charged with enabling AI capabilities for their teams while keeping their businesses safe. To do this job well, we’re improving awareness of agentic activity, increasing auditability, and launching complimentary capabilities that make custom agents enterprise-ready. Answering questions about what agents are doing in your enterprise has never been easier.

### AI controls are in the agent control plane
- Let’s start with some basic features of the agent control plane:
- One consolidated view and top-level navigation for all administrative tasks related to AI systems in GitHub.
- Administrators can manage their agentic fleet. The few agents now, and the thousands in the future, are operationalized here for your enterprise.
- The permanent home for enterprise-level policies and configuration of Copilot and AI-related systems.

### Enterprise-ready custom agents
- With the launch of custom agents, enterprises will want to determine a path toward standardized adoption:
- Configure one organization to host the enterprise standard for custom agents.
- Use a 1-click push rule to protect the static file path for custom agents (i.e., .github/agents/*.md ) across your enterprise from edits.
- Adjust push rules to fit your organizational design and experimentation tolerances.
- Select Enterprise-defined custom agents when assigning Copilot coding agent to any issue.

### Agent session activity
- Develop awareness of agent activity in the enterprise:
- See enterprise-wide agent sessions for the last 24 hours.
- Filter on agent type and the task state (e.g., completed, cancelled, in progress).
- Navigate directly to the target repository, if you have authorization to do so.

### Agentic audit logs
- What are your agents really doing? The audit logs have the answer:
- New fields for agent activity (e.g., pull_request.create executed by Copilot): Identify an actor_is_agent . Show user and user_id to identify who the agent is acting on behalf of.
- A new event for agent_session.task shows which sessions have started, finished, or failed to complete.
- You can quickly navigate to agent-related audit logs from the AI controls tab.
- Identify an actor_is_agent .
- Show user and user_id to identify who the agent is acting on behalf of.

### AI administration fine-grained permissions (FGPs) are coming soon!
- AI and Copilot administration is a job done by a team of people at most companies. And that team is not always responsible for running all of GitHub Enterprise. Later this week you can:
- Utilize a new FGP that grants access to the AI controls view.
- Build an enterprise custom role to decentralize administration of AI systems without granting broad enterprise ownership.
- Assign the enterprise custom role to an enterprise team to manage at scale.

### MCP enterprise allowlist
- Set enterprise-wide MCP allowlist via MCP registry URL to govern MCP connections in VS Code Insiders.
- Configure MCP policies from the AI controls experience.
- Omit local servers from registry to prevent the use of untrusted tools.
- Support for VS Code and other IDEs in general availability will be coming soon!
- To learn more, see our documentation on AI controls and the agent control plane .
- Join the discussion within GitHub Community .

## Insights (derived from article language)
- To learn more, see our documentation on AI controls and the agent control plane .

## Article Content (cleaned)
We’re introducing a new enterprise\-level experience focused on administrative functions for AI systems, available today to all GitHub Enterprise Cloud customers using Copilot. This is your agent control plane, a suite of enterprise governance features designed to give organizations deeper control over how agents operate across their environments.


Enterprise administrators are often charged with enabling AI capabilities for their teams while keeping their businesses safe. To do this job well, we’re improving awareness of agentic activity, increasing auditability, and launching complimentary capabilities that make custom agents enterprise\-ready. Answering questions about what agents are doing in your enterprise has never been easier.


### [AI controls are in the agent control plane](#ai-controls-are-in-the-agent-control-plane)


Let’s start with some basic features of the agent control plane:


* One consolidated view and top\-level navigation for all administrative tasks related to AI systems in GitHub.
* Administrators can manage their agentic fleet. The few agents now, and the thousands in the future, are operationalized here for your enterprise.
* The permanent home for enterprise\-level policies and configuration of Copilot and AI\-related systems.


### [Enterprise\-ready custom agents](#enterprise-ready-custom-agents)


With the launch of custom agents, enterprises will want to determine a path toward standardized adoption:


* Configure one organization to host the enterprise standard for custom agents.
* Use a 1\-click push rule to protect the static file path for custom agents (i.e., `.github/agents/*.md`) across your enterprise from edits.
* Adjust push rules to fit your organizational design and experimentation tolerances.
* Select Enterprise\-defined custom agents when assigning Copilot coding agent to any issue.


### [Agent session activity](#agent-session-activity)


Develop awareness of agent activity in the enterprise:


* See enterprise\-wide agent sessions for the last 24 hours.
* Filter on agent type and the task state (e.g., completed, cancelled, in progress).
* Navigate directly to the target repository, if you have authorization to do so.


### [Agentic audit logs](#agentic-audit-logs)


What are your agents really doing? The audit logs have the answer:


* New fields for agent activity (e.g., `pull_request.create` executed by Copilot):
	+ Identify an `actor_is_agent`.
	+ Show `user` and `user_id` to identify who the agent is acting on behalf of.
* A new event for `agent_session.task` shows which sessions have started, finished, or failed to complete.
* You can quickly navigate to agent\-related audit logs from the **AI controls** tab.


### [AI administration fine\-grained permissions (FGPs) are coming soon!](#ai-administration-fine-grained-permissions-fgps-are-coming-soon)


AI and Copilot administration is a job done by a team of people at most companies. And that team is not always responsible for running all of GitHub Enterprise. Later this week you can:


* Utilize a new FGP that grants access to the AI controls view.
* Build an enterprise custom role to decentralize administration of AI systems without granting broad enterprise ownership.
* Assign the enterprise custom role to an enterprise team to manage at scale.


### [MCP enterprise allowlist](#mcp-enterprise-allowlist)


Set enterprise\-wide MCP allowlist via MCP registry URL to govern MCP connections in VS Code Insiders.


* Configure MCP policies from the AI controls experience.
* Omit local servers from registry to prevent the use of untrusted tools.


Support for VS Code and other IDEs in general availability will be coming soon!


To learn more, see [our documentation on AI controls and the agent control plane](https://docs.github.com/copilot/concepts/agents/enterprise-management?utm_source=changelog-docs-enterprise-controls&utm_medium=changelog&utm_campaign=universe25).


Join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/178247?utm_source=changelog-community-enterprise-controls&utm_medium=changelog&utm_campaign=universe25).
