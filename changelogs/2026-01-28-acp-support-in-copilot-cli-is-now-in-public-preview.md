---
title: "ACP support in Copilot CLI is now in public preview"
date: "2026-01-28"
type: "Improvement"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-28-acp-support-in-copilot-cli-is-now-in-public-preview"
fetched_at: "2026-02-03T14:40:04.816974Z"
---

# ACP support in Copilot CLI is now in public preview

## Overview
GitHub Copilot CLI now implements the Agent Client Protocol (ACP) , an industry-standard protocol for communication between AI agents and clients. This enables third-party tools, IDEs, and automation systems to integrate directly with Copilot’s agentic capabilities through an extensible interface.

## Detailed Explanation
### Overview
- GitHub Copilot CLI now implements the Agent Client Protocol (ACP) , an industry-standard protocol for communication between AI agents and clients. This enables third-party tools, IDEs, and automation systems to integrate directly with Copilot’s agentic capabilities through an extensible interface.

### How it works
- You can start Copilot in ACP mode via stdio: copilot --acp
- Or connect via TCP on a specific port: copilot --acp --port 8080
- ACP clients can then:
- Initialize a connection and discover agent capabilities.
- Create isolated sessions with custom working directories.
- Send prompts with text, images, and context resources.
- Receive streaming updates as the agent works.
- Respond to permission requests for tool execution.
- Cancel operations and manage session lifecycle.

### Use cases
- IDE integrations: Build Copilot support into any editor or development environment.
- CI/CD pipelines: Orchestrate agentic coding tasks in automated workflows.
- Custom frontends: Create specialized interfaces for specific developer workflows.
- Multi-agent systems: Coordinate Copilot with other AI agents using a standard protocol.
- Learn more in our ACP documentation and join the discussion within GitHub Community .

## Insights (derived from article language)
- Learn more in our ACP documentation and join the discussion within GitHub Community .

## Article Content (cleaned)
GitHub Copilot CLI now implements the [Agent Client Protocol (ACP)](https://zed.dev/acp), an industry\-standard protocol for communication between AI agents and clients. This enables third\-party tools, IDEs, and automation systems to integrate directly with Copilot’s agentic capabilities through an extensible interface.


## [How it works](https://github.blog/changelog/feed/#how-it-works)


You can start Copilot in ACP mode via stdio: `copilot --acp`


Or connect via TCP on a specific port: `copilot --acp --port 8080`


ACP clients can then:


* Initialize a connection and discover agent capabilities.
* Create isolated sessions with custom working directories.
* Send prompts with text, images, and context resources.
* Receive streaming updates as the agent works.
* Respond to permission requests for tool execution.
* Cancel operations and manage session lifecycle.


## [Use cases](https://github.blog/changelog/feed/#use-cases)


* IDE integrations: Build Copilot support into any editor or development environment.
* CI/CD pipelines: Orchestrate agentic coding tasks in automated workflows.
* Custom frontends: Create specialized interfaces for specific developer workflows.
* Multi\-agent systems: Coordinate Copilot with other AI agents using a standard protocol.


Learn more in our [ACP documentation](https://docs.github.com/copilot/reference/acp-server) and join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/185860).
