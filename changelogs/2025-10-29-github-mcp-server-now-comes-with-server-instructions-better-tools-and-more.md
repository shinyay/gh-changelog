---
title: "GitHub MCP Server now comes with server instructions, better tools, and more"
date: "2025-10-29"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-29-github-mcp-server-now-comes-with-server-instructions-better-tools-and-more"
fetched_at: "2026-02-03T14:40:06.432820Z"
---

# GitHub MCP Server now comes with server instructions, better tools, and more

## Overview
The GitHub MCP Server now comes with server instructions that unlock new and better ways in which it can be used by models.

## Detailed Explanation
### Overview
- The GitHub MCP Server now comes with server instructions that unlock new and better ways in which it can be used by models.
- We’ve also continued to decrease the footprint of the GitHub MCP Server by consolidating more tools into fewer, more powerful tools.
- And now, configuring the GitHub MCP Server to your needs just got way easier!
- Visit the GitHub MCP Server repository to learn more.

### Server instructions and multitool workflows
- Server instructions are a feature of the Model Context Protocol specification which acts like a system prompt that guides the model in effectively using an MCP server. They’re especially useful for things like respecting tool interdependence (“always use tool A before tool B”), following multitool workflows (“when asked to review a pull request, always start off with tool A, then use tool B, and finally tool C”) or giving general guidance for commonalities that underlie most tools (“always use pagination when available”).
- With the addition of server instructions to the GitHub MCP Server, we’ve unlocked new possibilities. Models will now be much better at following precise workflows for tasks like reviewing pull requests and managing issues or discussions. They will also generally use tools more effectively across the board.
- Now that server instructions are part of the GitHub MCP Server, we will work on continuously improving them as our MCP server evolves! As always, we are listening closely to feedback from our users on how we can tweak instructions to best serve developer needs.

### Consolidating tools into more powerful multifunctional tools: pull requests, issues, sub-issues
- We’re continuing our work to make the GitHub MCP Server simpler and more performant by merging more related tools into unified, multifunctional ones. Just like before, each consolidated tool supports multiple operations through a single method parameter, making configurations leaner, AI reasoning clearer, and performance faster.
- Similar to the consolidation of the pull request tools in the previous release, the following pull request review tools have now been consolidated into a single, powerful pull_request_review_write tool:
- create_and_submit_pull_request_review
- create_pending_pull_request_review
- submit_pending_pull_request_review
- delete_pending_pull_request_review
- The new tool has a method parameter to perform these tasks:
- create
- submit_pending
- delete_pending
- The following issue tools have been consolidated into a single, powerful issue_read tool:
- get_issue
- get_issue_comments
- list_labels (with issue_number)
- list_sub_issues
- The new tool has a method parameter to perform these operations:
- get
- get_comments
- get_labels
- get_sub_issues
- Furthermore, the following issue tools are consolidated into a single issue_write tool:
- create_issue
- update_issue
- The new tool has a method parameter for these operations:
- create
- update
- Finally, the following sub-issue tools have been consolidated into a single sub_issue_write tool:
- add_sub_issue
- remove_sub_issue
- reprioritize_sub_issue
- The new tool has a method parameter to perform these operations:
- add
- reprioritize
- remove
- If you notice that a commonly used tool is missing, it’s likely been consolidated into a new multifunctional tool or moved out of the default configuration.

### Easier server configuration with the new default keyword
- Previously, toolsets could only be configured by typing them out one by one when configuring the MCP server. We’ve made this process easier by introducing the default keyword. You can use this keyword when configuring your server to refer to the default toolset.
- Now, adding a toolset like code_security to your default MCP configuration is as simple as X-MCP-Toolsets:"default,code_security" for the remote MCP server or --toolsets default,code_security for the local MCP server.
- Note that just as before, the default toolset will contain the following toolsets:
- context – Current user and GitHub context
- repos – Repository operations
- issues – Issue tracking
- pull_requests – Pull request workflows
- users – User information

## Impact / Who’s Affected
- Similar to the consolidation of the pull request tools in the previous release, the following pull request review tools have now been consolidated into a single, powerful pull_request_review_write tool: create_and_submit_pull_request_review create_pending_pull_request_review submit_pending_pull_request_review delete_pending_pull_request_review The new tool has a method parameter to perform these tasks: create submit_pending delete_pending The following issue tools have been consolidated into a single, powerful issue_read tool: get_issue get_issue_comments list_labels (with issue_number) list_sub_issues The new tool has a method parameter to perform these operations: get get_comments get_labels get_sub_issues Furthermore, the following issue tools are consolidated into a single issue_write tool: create_issue update_issue The new tool has a method parameter for these operations: create update Finally, the following sub-issue tools have been consolidated into a single sub_issue_write tool: add_sub_issue remove_sub_issue reprioritize_sub_issue The new tool has a method parameter to perform these operations: add reprioritize remove If you notice that a commonly used tool is missing, it’s likely been consolidated into a new multifunctional tool or moved out of the default configuration.
- Easier server configuration with the new default keyword Previously, toolsets could only be configured by typing them out one by one when configuring the MCP server.

## Caveats / Limitations
- Similar to the consolidation of the pull request tools in the previous release, the following pull request review tools have now been consolidated into a single, powerful pull_request_review_write tool: create_and_submit_pull_request_review create_pending_pull_request_review submit_pending_pull_request_review delete_pending_pull_request_review The new tool has a method parameter to perform these tasks: create submit_pending delete_pending The following issue tools have been consolidated into a single, powerful issue_read tool: get_issue get_issue_comments list_labels (with issue_number) list_sub_issues The new tool has a method parameter to perform these operations: get get_comments get_labels get_sub_issues Furthermore, the following issue tools are consolidated into a single issue_write tool: create_issue update_issue The new tool has a method parameter for these operations: create update Finally, the following sub-issue tools have been consolidated into a single sub_issue_write tool: add_sub_issue remove_sub_issue reprioritize_sub_issue The new tool has a method parameter to perform these operations: add reprioritize remove If you notice that a commonly used tool is missing, it’s likely been consolidated into a new multifunctional tool or moved out of the default configuration.
- Easier server configuration with the new default keyword Previously, toolsets could only be configured by typing them out one by one when configuring the MCP server.
- Note that just as before, the default toolset will contain the following toolsets: context – Current user and GitHub context repos – Repository operations issues – Issue tracking pull_requests – Pull request workflows users – User information

## Insights (derived from article language)
- Visit the GitHub MCP Server repository to learn more.
- Note that just as before, the default toolset will contain the following toolsets: context – Current user and GitHub context repos – Repository operations issues – Issue tracking pull_requests – Pull request workflows users – User information

## Article Content (cleaned)
The GitHub MCP Server now comes with server instructions that unlock new and better ways in which it can be used by models.


We’ve also continued to decrease the footprint of the GitHub MCP Server by consolidating more tools into fewer, more powerful tools.


And now, configuring the GitHub MCP Server to your needs just got way easier!


Visit the [GitHub MCP Server repository](https://github.com/github/github-mcp-server) to learn more.


## [Server instructions and multitool workflows](#server-instructions-and-multitool-workflows)


Server instructions are a feature of the Model Context Protocol specification which acts like a system prompt that guides the model in effectively using an MCP server. They’re especially useful for things like respecting tool interdependence (“always use tool A before tool B”), following multitool workflows (“when asked to review a pull request, always start off with tool A, then use tool B, and finally tool C”) or giving general guidance for commonalities that underlie most tools (“always use pagination when available”).


With the addition of server instructions to the GitHub MCP Server, we’ve unlocked new possibilities. Models will now be much better at following precise workflows for tasks like reviewing pull requests and managing issues or discussions. They will also generally use tools more effectively across the board.


Now that server instructions are part of the GitHub MCP Server, we will work on continuously improving them as our MCP server evolves! As always, we are listening closely to feedback from our users on how we can tweak instructions to best serve developer needs.


## [Consolidating tools into more powerful multifunctional tools: pull requests, issues, sub\-issues](#consolidating-tools-into-more-powerful-multifunctional-tools-pull-requests-issues-sub-issues)


We’re continuing our work to make the GitHub MCP Server simpler and more performant by merging more related tools into unified, multifunctional ones. Just like before, each consolidated tool supports multiple operations through a single `method` parameter, making configurations leaner, AI reasoning clearer, and performance faster.


Similar to the consolidation of the pull request tools in the previous release, the following pull request review tools have now been consolidated into a single, powerful `pull_request_review_write` tool:


* `create_and_submit_pull_request_review`
* `create_pending_pull_request_review`
* `submit_pending_pull_request_review`
* `delete_pending_pull_request_review`


The new tool has a `method` parameter to perform these tasks:


* `create`
* `submit_pending`
* `delete_pending`


The following issue tools have been consolidated into a single, powerful `issue_read` tool:


* `get_issue`
* `get_issue_comments`
* `list_labels (with issue_number)`
* `list_sub_issues`


The new tool has a `method` parameter to perform these operations:


* `get`
* `get_comments`
* `get_labels`
* `get_sub_issues`


Furthermore, the following issue tools are consolidated into a single `issue_write` tool:


* `create_issue`
* `update_issue`


The new tool has a `method` parameter for these operations:


* `create`
* `update`


Finally, the following sub\-issue tools have been consolidated into a single `sub_issue_write` tool:


* `add_sub_issue`
* `remove_sub_issue`
* `reprioritize_sub_issue`


The new tool has a `method` parameter to perform these operations:


* `add`
* `reprioritize`
* `remove`


If you notice that a commonly used tool is missing, it’s likely been consolidated into a new multifunctional tool or moved out of the default configuration.


## [Easier server configuration with the new `default` keyword](#easier-server-configuration-with-the-new-default-keyword)


Previously, toolsets could only be configured by typing them out one by one when configuring the MCP server. We’ve made this process easier by introducing the `default` keyword. You can use this keyword when configuring your server to refer to the default toolset.


Now, adding a toolset like `code_security` to your default MCP configuration is as simple as `X-MCP-Toolsets:"default,code_security"` for the remote MCP server or `--toolsets default,code_security` for the local MCP server.


Note that just as before, the `default` toolset will contain the following toolsets:


* `context` – Current user and GitHub context
* `repos` – Repository operations
* `issues` – Issue tracking
* `pull_requests` – Pull request workflows
* `users` – User information
