---
title: "GitHub MCP Server: New Projects tools, OAuth scope filtering, and new features"
date: "2026-01-28"
type: "Release"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-28-github-mcp-server-new-projects-tools-oauth-scope-filtering-and-new-features"
fetched_at: "2026-02-03T14:50:49.392520Z"
---

# GitHub MCP Server: New Projects tools, OAuth scope filtering, and new features

## Detailed Explanation
### Overview
- The GitHub MCP Server has arrived with improved capabilities to manage GitHub Projects with more efficient usage of the context window, automatic tool filtering based on your token’s permissions, and features including Insiders and HTTP server mode!
- Visit the GitHub MCP Server repository to learn more.

### Consolidated GitHub Projects toolset
- Previously, the Projects toolset, as with other now-consolidated toolsets, used a significant portion of the context window for the tools list. As a result, we’ve reduced token usage by around 23,000 tokens (50%). Managing GitHub Projects is now simpler with a new consolidated set of tools that replace the previous approach. The new projects toolset provides unified access to project management capabilities:
- projects_list : List projects for a user, organization, or repository.
- projects_get : Retrieve detailed information about a specific project, including fields and items.
- projects_write : Create, update, and manage project items with full field support.
- The consolidated tools handle owner type detection automatically—you no longer need to specify whether the owner is a user or organization.

### OAuth scope filtering
- The GitHub MCP Server now manages tool availability based on your authentication method.
- When using a classic Personal Access Token ( ghp_ prefix), the server automatically detects your token’s OAuth scopes and hides tools you don’t have permission to use. This reduces clutter and prevents errors from attempting operations your token can’t perform. To learn more about creating a personal access token (PAT) for yourself, check out our docs on managing your personal access tokens .

### How it works
- At startup, the server detects if your token is a classic PAT.
- It discovers your token’s scopes via a lightweight API call.
- Tools requiring scopes your token doesn’t have are automatically hidden.

### Insiders mode for experimental features
- We’re introducing Insiders mode , an opt-in mechanism that lets you access experimental and preview functionality in the GitHub MCP Server. This will be available for both local and remote server deployments.

### How it works
- Users explicitly opt in by setting a configuration header or using the new /insiders URL.
- When enabled, the MCP Server grants access to experimental features, behavior changes under evaluation, and functionality not yet generally available.
- Removing the header or reverting to the standard URL instantly restores standard generally available behavior.

### HTTP server mode with OAuth support
- Enterprise users are now able to run the GitHub MCP Server in HTTP mode with OAuth token support.

### What’s coming
- HTTP server mode : Run the local MCP server as an HTTP server on a configurable port.
- Per-request OAuth tokens : Support tokens via Authorization header.
- Fallback support : Falls back to GITHUB_PERSONAL_ACCESS_TOKEN if no header is provided.
- Enterprise Server compatibility : Full support for GitHub Enterprise Server deployments.
- This allows enterprise teams to deploy a shared MCP server with OAuth token forwarding, eliminating the need for every user to manage their own personal access tokens.

### Copilot coding agent tools
- The GitHub MCP Server adds new tools and improvements for working with the Copilot coding agent.
- The new get_copilot_job_status tool lets you check on Copilot’s progress. You can query by job ID or pull request number.
- Both assign_copilot_to_issue and create_pull_request_with_copilot now support a base_ref parameter:
- Feature branches : Start Copilot’s work from any branch, not just the default.
- Stacked PRs : Build on existing work by specifying a feature branch as the base.
- Sequential tasks : Chain multiple Copilot assignments together.
- Task assignments now return a job ID or pull request link immediately, so you can track status right away.
- The assign_copilot_to_issue tool now supports custom instructions.

### Getting started
- To get started, enable the copilot toolset.
- Visit the GitHub MCP Server repository to learn more.
- Try out these features today! If you have feedback, please open an issue in our open-source GitHub MCP Server repository .

## Key Changes
- We’re introducing Insiders mode , an opt-in mechanism that lets you access experimental and preview functionality in the GitHub MCP Server. This will be available for both local and remote server deployments.

## Impact / Who’s Affected
- When enabled, the MCP Server grants access to experimental features, behavior changes under evaluation, and functionality not yet generally available.
- Removing the header or reverting to the standard URL instantly restores standard generally available behavior.

## Insights (derived from article language)
- Visit the GitHub MCP Server repository to learn more.
- To learn more about creating a personal access token (PAT) for yourself, check out our docs on managing your personal access tokens .

## Article Content (cleaned)
![A code snippet defines a GitHub server configuration with an HTTP endpoint, an api.githubcopilot.com MCP insiders URL, and an X‑MCP‑Toolsets header set to projects.](https://github.com/user-attachments/assets/c80409be-8021-4b1e-9533-7dfa7f9b270d)


The GitHub MCP Server has arrived with improved capabilities to manage GitHub Projects with more efficient usage of the context window, automatic tool filtering based on your token’s permissions, and features including Insiders and HTTP server mode!


Visit the [GitHub MCP Server repository](https://github.com/github/github-mcp-server) to learn more.


## [Consolidated GitHub Projects toolset](https://github.blog/changelog/feed/#consolidated-github-projects-toolset)


Previously, the Projects toolset, as with other now\-consolidated toolsets, used a significant portion of the context window for the tools list. As a result, we’ve reduced token usage by around **23,000 tokens** (50%). Managing GitHub Projects is now simpler with a new consolidated set of tools that replace the previous approach. The new `projects` toolset provides unified access to project management capabilities:


* **`projects_list`**: List projects for a user, organization, or repository.
* **`projects_get`**: Retrieve detailed information about a specific project, including fields and items.
* **`projects_write`**: Create, update, and manage project items with full field support.


The consolidated tools handle owner type detection automatically—you no longer need to specify whether the owner is a user or organization.


## [OAuth scope filtering](https://github.blog/changelog/feed/#oauth-scope-filtering)


The GitHub MCP Server now manages tool availability based on your authentication method.


When using a classic Personal Access Token (`ghp_` prefix), the server automatically detects your token’s OAuth scopes and hides tools you don’t have permission to use. This reduces clutter and prevents errors from attempting operations your token can’t perform. To learn more about creating a personal access token (PAT) for yourself, check out our docs on [managing your personal access tokens](https://docs.github.com/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).


### [How it works](https://github.blog/changelog/feed/#how-it-works)


1. At startup, the server detects if your token is a classic PAT.
2. It discovers your token’s scopes via a lightweight API call.
3. Tools requiring scopes your token doesn’t have are automatically hidden.




| Token Type | Behavior |
| --- | --- |
| Classic PAT (`ghp_`) | Tools filtered based on token scopes |
| Fine\-grained PAT (`github_pat_`) | All tools shown, API enforces permissions |
| OAuth (remote server) | Dynamic scope challenges on\-demand |


## [Insiders mode for experimental features](https://github.blog/changelog/feed/#insiders-mode-for-experimental-features)


We’re introducing **Insiders mode**, an opt\-in mechanism that lets you access experimental and preview functionality in the GitHub MCP Server. This will be available for both local and remote server deployments.


### [How it works](https://github.blog/changelog/feed/#how-it-works)


* Users explicitly opt in by setting a configuration header or using the new `/insiders` URL.
* When enabled, the MCP Server grants access to experimental features, behavior changes under evaluation, and functionality not yet generally available.
* Removing the header or reverting to the standard URL instantly restores standard generally available behavior.


## [HTTP server mode with OAuth support](https://github.blog/changelog/feed/#http-server-mode-with-oauth-support)


Enterprise users are now able to run the GitHub MCP Server in HTTP mode with OAuth token support.


### [What’s coming](https://github.blog/changelog/feed/#whats-coming)


* **HTTP server mode**: Run the local MCP server as an HTTP server on a configurable port.
* **Per\-request OAuth tokens**: Support tokens via Authorization header.
* **Fallback support**: Falls back to `GITHUB_PERSONAL_ACCESS_TOKEN` if no header is provided.
* **Enterprise Server compatibility**: Full support for GitHub Enterprise Server deployments.


This allows enterprise teams to deploy a shared MCP server with OAuth token forwarding, eliminating the need for every user to manage their own personal access tokens.


## [Copilot coding agent tools](https://github.blog/changelog/feed/#copilot-coding-agent-tools)


The GitHub MCP Server adds new tools and improvements for working with the Copilot coding agent.


The new `get_copilot_job_status` tool lets you check on Copilot’s progress. You can query by job ID or pull request number.


![Checking the status of Copilot coding agent jobs](https://github.com/user-attachments/assets/1acaa644-3718-4e5f-846c-6c19eee9faa4)


Both `assign_copilot_to_issue` and `create_pull_request_with_copilot` now support a `base_ref` parameter:


* **Feature branches**: Start Copilot’s work from any branch, not just the default.
* **Stacked PRs**: Build on existing work by specifying a feature branch as the base.
* **Sequential tasks**: Chain multiple Copilot assignments together.


Task assignments now return a job ID or pull request link immediately, so you can track status right away.


The `assign_copilot_to_issue` tool now supports custom instructions.


### [Getting started](https://github.blog/changelog/feed/#getting-started)


To get started, enable the `copilot` toolset.


Visit the [GitHub MCP Server repository](https://github.com/github/github-mcp-server) to learn more.


Try out these features today! If you have feedback, please open an issue in our open\-source [GitHub MCP Server repository](https://github.com/github/github-mcp-server).
