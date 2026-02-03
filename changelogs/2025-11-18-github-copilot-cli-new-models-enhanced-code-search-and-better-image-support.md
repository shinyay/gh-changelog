---
title: "GitHub Copilot CLI: New models, enhanced code search, and better image support"
date: "2025-11-18"
type: "improvements"
labels: ["client apps", "copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-18-github-copilot-cli-new-models-enhanced-code-search-and-better-image-support"
fetched_at: "2026-02-03T14:50:55.189982Z"
---

# GitHub Copilot CLI: New models, enhanced code search, and better image support

## Overview
GitHub Copilot CLI continues to evolve with significant improvements to search capabilities, better image support, access to and support for the latest AI models, and reliability enhancements. Here's what we've been working on lately.

## Detailed Explanation
### Overview
- GitHub Copilot CLI continues to evolve with significant improvements to search capabilities, better image support, access to and support for the latest AI models, and reliability enhancements. Here's what we've been working on lately.

### Latest AI models now available
- We've added support for the newest models from OpenAI and Google to keep you on the cutting edge:
- GPT-5.1, GPT-5.1-Codex, and GPT-5.1-Codex-Mini
- Gemini 3 Pro

### More powerful code search
- Copilot now searches your codebase more efficiently! We've bundled ripgrep into Copilot CLI and added grep and glob tools to quickly and powerfully find the right context.

### Better image support
- Previously, @ -mentioning an image file added it to Copilot's context. Based on your feedback, we've enhanced this by allowing images to be added through pasting and drag-and-drop.

### Additional developer delighters
- /share command easily saves your chat session as Markdown files or GitHub gists
- Removed unnecessary permissions checks when suggested commands contained heredocs and other special characters
- Improved support for ! shell mode commands in PowerShell
- Improved automation scenarios using the headless -p mode by exiting with nonzero codes when encountering permission or communication errors
- Enhanced the output of the /session command and improved its styling
- Improved whitespace, formatting, and UI interactions across the application
- Added support for MCP server tool notifications
- Improved Copilot's handling of long-running shell commands

### Reliability and bugfixes
- We’ve fixed a number of user-reported bugs and reliability issues:
- Prevented memory leaks when executing long-running shell commands
- Implemented various bugfixes around custom agent configuration
- Improved handling of Ctrl+C signals and abort operations
- Removed the internal NODE_ENV variable from the shell tool's environment, preventing a clash in Node development scenarios
- Fixed an issue blocking Windows Terminal keyboard input
- Improved error messages when using unsupported models in the /model command
- Fixed an issue where background color values were printed to the input box on first launch

### Share your feedback
- Update GitHub Copilot CLI by running npm install -g @github/copilot@latest in your terminal. Thank you to everyone who has submitted feedback via the /feedback command and by opening issues in our public repository . Your continued feedback is invaluable as we continue to ship improvements.

## Impact / Who’s Affected
- Latest AI models now available We've added support for the newest models from OpenAI and Google to keep you on the cutting edge: GPT-5.1, GPT-5.1-Codex, and GPT-5.1-Codex-Mini Gemini 3 Pro More powerful code search Copilot now searches your codebase more efficiently!

## Article Content (cleaned)
`GitHub Copilot CLI continues to evolve with significant improvements to search capabilities, better image support, access to and support for the latest AI models, and reliability enhancements. Here's what we've been working on lately.`


## [Latest AI models now available](#latest-ai-models-now-available)


We've added support for the newest models from OpenAI and Google to keep you on the cutting edge:


* GPT\-5\.1, GPT\-5\.1\-Codex, and GPT\-5\.1\-Codex\-Mini
* Gemini 3 Pro


## [More powerful code search](#more-powerful-code-search)


Copilot now searches your codebase more efficiently! We've bundled `ripgrep` into Copilot CLI and added `grep` and `glob` tools to quickly and powerfully find the right context.


## [Better image support](#better-image-support)


Previously, `@`\-mentioning an image file added it to Copilot's context. Based on your feedback, we've enhanced this by allowing images to be added through pasting and drag\-and\-drop.


## [Additional developer delighters](#additional-developer-delighters)


* `/share` command easily saves your chat session as Markdown files or GitHub gists
* Removed unnecessary permissions checks when suggested commands contained heredocs and other special characters
* Improved support for `!` shell mode commands in PowerShell
* Improved automation scenarios using the headless `-p` mode by exiting with nonzero codes when encountering permission or communication errors
* Enhanced the output of the `/session` command and improved its styling
* Improved whitespace, formatting, and UI interactions across the application
* Added support for MCP server tool notifications
* Improved Copilot's handling of long\-running shell commands


## [Reliability and bugfixes](#reliability-and-bugfixes)


We’ve fixed a number of user\-reported bugs and reliability issues:


* Prevented memory leaks when executing long\-running shell commands
* Implemented various bugfixes around custom agent configuration
* Improved handling of Ctrl\+C signals and abort operations
* Removed the internal `NODE_ENV` variable from the shell tool's environment, preventing a clash in Node development scenarios
* Fixed an issue blocking Windows Terminal keyboard input
* Improved error messages when using unsupported models in the `/model` command
* Fixed an issue where background color values were printed to the input box on first launch


## [Share your feedback](#share-your-feedback)


Update GitHub Copilot CLI by running `npm install -g @github/copilot@latest` in your terminal. Thank you to everyone who has submitted feedback via the `/feedback` command and by opening issues in [our public repository](https://github.com/github/copilot-cli). Your continued feedback is invaluable as we continue to ship improvements.
