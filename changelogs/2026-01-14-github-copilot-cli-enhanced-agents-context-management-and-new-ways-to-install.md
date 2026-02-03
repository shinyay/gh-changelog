---
title: "GitHub Copilot CLI: Enhanced agents, context management, and new ways to install"
date: "2026-01-14"
type: "improvements"
labels: ["client apps", "copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install"
fetched_at: "2026-02-03T14:40:05.216902Z"
---

# GitHub Copilot CLI: Enhanced agents, context management, and new ways to install

## Overview
As we wrapped up 2025 and rang in 2026, we’ve continued to deliver new ways of working with agents in GitHub Copilot CLI while improving the terminal-native experience for all developers. Here’s what’s new since our last update.

## Detailed Explanation
### Overview
- As we wrapped up 2025 and rang in 2026, we’ve continued to deliver new ways of working with agents in GitHub Copilot CLI while improving the terminal-native experience for all developers. Here’s what’s new since our last update.

### New models and easier model management
- GPT-5 mini and GPT-4.1 , models that are included with your Copilot subscription and do not consume premium requests on paid plans, are now available. Run /model to see all model options.
- If you select a model that’s disabled in your policy settings, the CLI now prompts you to enable it directly—no need to leave the terminal. This works in the model picker, /model command, and --model flag for Copilot Pro/Pro+ users.

### Built-in custom agents
- Copilot CLI now includes specialized custom agents for common tasks:
- Explore : Fast codebase analysis. Ask questions about your code without cluttering your main context.
- Task : Runs commands like tests and builds. Receive brief summaries on success, full output on failure.
- Plan : Creates implementation plans by analyzing dependencies and structure.
- Code-review : Reviews changes with high signal-to-noise ratio, focused on only surfacing genuine issues.
- Copilot delegates to these agents automatically when appropriate and can run multiple agents in parallel.
- When combined with Agent Skills , you can more easily integrate agentic workflows into yoiur Copilot CLI experience.

### New ways to install
- Windows (WinGet):
- macOS and Linux (Homebrew):
- macOS and Linux (install script):
- Package manager and install script installations automatically update .
- Codespaces and dev containers: Copilot CLI is included in the default GitHub Codespaces image and available as a Dev Container Feature .
- Standalone executables are also available in GitHub release artifacts for all platforms.

### Automation and scripting
- New flags make Copilot CLI easier to use in scripts and pipelines via copilot -p :
- Refer to copilot --help for a list of all optional flags.
- CI/CD authentication: Set GITHUB_ASKPASS to point to an executable that returns your token—useful for credential managers and pipelines.
- Copilot Spaces: The GitHub MCP server now includes Copilot Spaces tools for project-specific context.

### Context management
- Auto-compaction : When approaching 95% of the token limit, Copilot automatically compresses your history.
- /compact : Manually compress context anytime.
- /context : Visualize token usage with a detailed breakdown.
- --resume : Press TAB to cycle through local sessions and remote Copilot coding agent sessions.

### Terminal experience
- Better diffs : Intra-line syntax highlighting shows exactly what changed. It now integrates with Git’s configured pager.
- Tab completion : Autocomplete paths in /cwd and /add-dir .
- Ctrl+T : Toggle model reasoning visibility in supported models.
- Cleaner history : Agent-run commands excluded from Bash/PowerShell history.

### Web access controls
- The new web_fetch tool retrieves content from URLs as markdown. URL access is controlled through ~/.copilot/config with allowed_urls and denied_urls patterns. These rules also apply to shell commands like curl and wget .

### Share your feedback
- Update with your package manager, or run npm install -g @github/copilot@latest .
- Join the discussion in Copilot CLI’s public repository .

## Impact / Who’s Affected
- New models and easier model management GPT-5 mini and GPT-4.1 , models that are included with your Copilot subscription and do not consume premium requests on paid plans, are now available.
- Code-review : Reviews changes with high signal-to-noise ratio, focused on only surfacing genuine issues.

## Caveats / Limitations
- Code-review : Reviews changes with high signal-to-noise ratio, focused on only surfacing genuine issues.

## Article Content (cleaned)
As we wrapped up 2025 and rang in 2026, we’ve continued to deliver new ways of working with agents in GitHub Copilot CLI while improving the terminal\-native experience for all developers. Here’s what’s new since our last update.


## [New models and easier model management](#new-models-and-easier-model-management)


![This image shows the full model list of Copilot CLI, including new 0x models GPT-5 mini and GPT-4.1. One model, GPT-5.2, has not been enabled by this user, and they see a 'requires enablement' prompt to turn on access](https://github.com/user-attachments/assets/e7a818e6-cfdf-417f-9129-ffe4b5b46077)


**GPT\-5 mini** and **GPT\-4\.1**, models that are included with your Copilot subscription and do not consume premium requests on paid plans, are now available. Run `/model` to see all model options.


If you select a model that’s disabled in your policy settings, the CLI now prompts you to enable it directly—no need to leave the terminal. This works in the model picker, `/model` command, and `--model` flag for Copilot Pro/Pro\+ users.


## [Built\-in custom agents](#built-in-custom-agents)


![This image shows the built-in explore agent searching the codebase for authentication patterns across the codebase](https://github.com/user-attachments/assets/f83db7a4-ed8b-4d45-aa7b-e10b08f8d72a)


Copilot CLI now includes specialized custom agents for common tasks:


* **Explore**: Fast codebase analysis. Ask questions about your code without cluttering your main context.
* **Task**: Runs commands like tests and builds. Receive brief summaries on success, full output on failure.
* **Plan**: Creates implementation plans by analyzing dependencies and structure.
* **Code\-review**: Reviews changes with high signal\-to\-noise ratio, focused on only surfacing genuine issues.


Copilot delegates to these agents automatically when appropriate and can run multiple agents in parallel.


When combined with [Agent Skills](https://github.blog/changelog/2025-12-18-github-copilot-now-supports-agent-skills/), you can more easily integrate agentic workflows into yoiur Copilot CLI experience.


## [New ways to install](#new-ways-to-install)


**Windows (WinGet):**



```
winget install GitHub.Copilot

```

**macOS and Linux (Homebrew):**



```
brew install copilot-cli

```

**macOS and Linux (install script):**



```
curl -fsSL https://gh.io/copilot-install | bash

```

Package manager and install script installations **automatically update**.


**Codespaces and dev containers:** Copilot CLI is included in the default GitHub Codespaces image and available as a [Dev Container Feature](https://github.com/devcontainers/features).


Standalone executables are also available in [GitHub release artifacts](https://github.com/github/copilot-cli/releases) for all platforms.


## [Automation and scripting](#automation-and-scripting)


New flags make Copilot CLI easier to use in scripts and pipelines via `copilot -p`:




| Flag | Description |
| --- | --- |
| `--silent` | Suppress stats and logs for clean, parseable output |
| `--share [PATH]` | Export session transcript to markdown file |
| `--share-gist` | Export session to a shareable GitHub gist |
| `--available-tools` | Allowlist specific tools |
| `--excluded-tools` | Denylist specific tools |
| `--additional-mcp-config` | Add MCP config files per\-session |


Refer to `copilot --help` for a list of all optional flags.


**CI/CD authentication:** Set `GITHUB_ASKPASS` to point to an executable that returns your token—useful for credential managers and pipelines.


**Copilot Spaces:** The GitHub MCP server now includes Copilot Spaces tools for project\-specific context.


## [Context management](#context-management)


![This image shows the output of the /context command and the /compact command](https://github.com/user-attachments/assets/a6088645-33da-4c29-a6cf-c97b7d51c7a3)


* **Auto\-compaction**: When approaching 95% of the token limit, Copilot automatically compresses your history.
* **`/compact`**: Manually compress context anytime.
* **`/context`**: Visualize token usage with a detailed breakdown.
* **`--resume`**: Press `TAB` to cycle through local sessions and remote Copilot coding agent sessions.


## [Terminal experience](#terminal-experience)


* **Better diffs**: Intra\-line syntax highlighting shows exactly what changed. It now integrates with Git’s configured pager.
* **Tab completion**: Autocomplete paths in `/cwd` and `/add-dir`.
* **Ctrl\+T**: Toggle model reasoning visibility in supported models.
* **Cleaner history**: Agent\-run commands excluded from Bash/PowerShell history.


## [Web access controls](#web-access-controls)


The new `web_fetch` tool retrieves content from URLs as markdown. URL access is controlled through `~/.copilot/config` with `allowed_urls` and `denied_urls` patterns. These rules also apply to shell commands like `curl` and `wget`.


## [Share your feedback](#share-your-feedback)


Update with your package manager, or run `npm install -g @github/copilot@latest`.


Join the discussion in Copilot CLI’s [public repository](https://github.com/github/copilot-cli).
