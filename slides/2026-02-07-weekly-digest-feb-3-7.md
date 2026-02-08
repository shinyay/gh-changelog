---
marp: true
theme: github-dark
paginate: true
header: "GitHub Changelog Update"
footer: "Weekly Digest — Feb 3–7, 2026"
---

# GitHub Changelog Weekly Digest
## February 3–7, 2026

15 entries across Copilot, Pull Requests, Actions, Security, and more

**Shinya Yanagihara** (Dev GBB)

---

# Table of Contents

1. 🤖 **Copilot & AI Models** (6 entries)
2. 🔀 **Pull Requests & Issues** (3 entries)
3. ⚙️ **GitHub Actions** (2 entries)
4. 🔒 **Security & Dependabot** (3 entries)
5. 📱 **GitHub Mobile** (1 entry)

---

<!-- Section: Copilot & AI Models -->

# 🤖 Copilot & AI Models

---

# Claude Opus 4.6 — Now GA for Copilot
## Overview

- Claude Opus 4.6 is **generally available** across VS Code, Visual Studio, github.com, GitHub Mobile, and CLI
- Designed for agentic coding with strong planning and tool-calling capabilities
- Available to Copilot Pro, Pro+, Business, and Enterprise users

---

## Key Changes & Caveats

- Selectable in model picker across all six Copilot surfaces
- Also available for Copilot coding agent (Pro and Pro+ only)
- Enterprise/Business admins must enable the Claude Opus 4.6 policy in Copilot settings
- ⚠️ Rollout is gradual — may not be immediately visible to all users

---

# Claude & Codex — Partner Coding Agents
## Overview

- Claude (Anthropic) and OpenAI Codex available as **partner coding agents** in public preview
- For Copilot Pro+ and Enterprise customers
- Usable across GitHub web, mobile, and VS Code

---

## How It Works

- Assign agents to issues via Assignees dropdown — they create draft PRs
- Address agents in comments: `@copilot`, `@claude`, or `@codex`
- Session types in VS Code: Local (fast), Cloud (autonomous), Background (Copilot only)
- ⚠️ Each coding agent session consumes **one premium request** during preview

---

# Copilot in VS Code v1.109 — January Release
## Overview

- Improved agent-driven workflows with expanded model integrations
- Claude agent support in public preview via Anthropic's official SDK
- Richer MCP app interactions and revamped inline chat UX

---

## Key Changes

- Multi-agent session management with parallel subagent support
- Copilot Memory retains context across interactions
- Faster code search via external indexing for large repos
- Terminal command sandboxing (experimental, macOS/Linux only)

---

# Copilot in Visual Studio — January Update
## Overview

- Colorized code completions with syntax highlighting for better readability
- Partial acceptance of completions — accept only the portion you need
- Improved Markdown preview controls with Mermaid diagram zoom support
- Editor productivity improvements: faster scrolling, HTML-rich copy/paste

---

# Simplified Copilot Model Enablement
## Overview

- New models now available **directly** in Copilot features — no settings pages needed
- Applies to Copilot Pro+, Pro, and Free users
- Choose a model manually or let Auto mode select for you
- Existing data-usage policies remain unchanged

---

# Copilot Chat on the Web — Tool Call Visibility
## Overview

- Chat responses now show **tool call details** in real time
- Export conversations to JSON or Markdown for documentation
- Improved repository attachment search and recommendations
- Helps users understand, debug, and share Copilot interactions

---

<!-- Section: Pull Requests & Issues -->

# 🔀 Pull Requests & Issues

---

# PR Files Changed — February 5 Updates
## Performance

- Up to **67% faster** interactions for large pull requests
- Tab navigation (Conversations → Files) reduced from 10+ seconds to a few seconds
- Selective virtualization applied only to the largest PRs
- Fixed high memory usage; improved Safari stability

---

## CODEOWNERS & Bug Fixes

- **CODEOWNERS validation** added to new Files changed experience
- Required reviewers correctly surfaced based on CODEOWNERS rules
- Small-screen layout and overflow issues fixed for mobile viewports
- Bug fixes: notification read state, sticky headers, code snippet colors, large diff commenting

---

# Pinned Comments on GitHub Issues
## Overview

- Pin a comment to the top of any issue via the "..." menu
- Surfaces key decisions, updates, or next steps without scrolling
- New nudge discourages low-quality "+1" / "same here" comments
- Encourages reactions and subscriptions instead — reducing noise and notifications

---

<!-- Section: GitHub Actions -->

# ⚙️ GitHub Actions

---

# Actions — Early February 2026 Updates
## Runner Scale Set Client (Public Preview)

- Standalone **Go-based module** for custom autoscaling without Kubernetes
- Platform agnostic: containers, VMs, bare metal on Windows, Linux, macOS
- Supports agentic workflows including Copilot coding agent
- Not a replacement for ARC — complements it for non-K8s environments

---

## Action Allowlisting & New Runner Images

- Action allowlisting expanded to **all plan types** (Free, Team, Enterprise)
- Enables least-privilege enforcement against compromised actions
- New runner images in public preview:
  - `windows-2025-vs2026` — Windows Server 2025 + Visual Studio 2026
  - `macos-26-large` — macOS 26 Intel for larger runners

---

# Self-Hosted Runner Version Enforcement
## Timeline Extended

- Deadline extended by one week to **March 16, 2026**
- Minimum version: **v2.329.0** (released Oct 15, 2025)
- Brownout period: Feb 16 – Mar 16 with escalating configuration blocks
- After enforcement, runners below v2.329.0 are **permanently blocked**
- ⚠️ Action required: update runner images, scripts, and templates before deadline

---

<!-- Section: Security & Dependabot -->

# 🔒 Security & Dependabot

---

# CodeQL 2.24.1
## Key Improvements

- Maven private registries now serve as **plugin repositories** in Default Setup
- Kotlin 2.3.0 support added; Kotlin 1.6.x/1.7.x dropped
- New experimental `py/prompt-injection` query for LLM prompt injection detection
- Python taint models added for `openai` and `agents` modules
- C# 14, C23/C++26 language feature support expanded

---

## Query Accuracy

- Six C/C++ buffer overflow queries produce **fewer false positives**
- Improved `java/unreleased-lock` query accuracy
- Fixed Actions analysis crash on long `${{ ... }}` expressions
- Remote flow sources modeled for Python `websockets` package

---

# Dependabot OIDC Authentication
## Overview

- Dependabot can now use **OIDC** to authenticate to private registries
- Short-lived credentials replace long-lived stored secrets
- Supported registries: AWS CodeArtifact, Azure DevOps Artifacts, JFrog Artifactory
- Update `dependabot.yml` to opt in — reduces secret sprawl and attack surface

---

# Dependabot Proxy — Now Open Source
## Overview

- The Dependabot Proxy is now **open source under MIT license**
- HTTP proxy handling auth for GitHub API and private registries (Go-based)
- Supports npm, Maven, Docker, Cargo, Helm, NuGet, pip, RubyGems, Terraform
- Enables security audits, community contributions, and bug reports

---

<!-- Section: GitHub Mobile -->

# 📱 GitHub Mobile

---

# Mobile — Comment on Unchanged Lines in PRs
## Overview

- Expand diffs to comment on **unchanged lines** within pull request files
- Comments on unchanged lines from github.com now visible on mobile
- Add reviewer context or suggested changes outside immediate diff hunks
- Brings mobile PR review closer to the full web experience

---

# Key Takeaways

- **Claude Opus 4.6 GA** + Claude/Codex partner agents bring multi-model agentic coding to Copilot
- **PR Files changed** gets 67% faster, gains CODEOWNERS validation
- **Actions scale set client** enables custom autoscaling without Kubernetes
- **CodeQL 2.24.1** adds LLM prompt injection detection and Maven plugin registry support
- **Dependabot OIDC** eliminates long-lived secrets for private registries
- **Pinned comments** on issues improve signal-to-noise in discussions

---

# Thank You

Source: [GitHub Changelog](https://github.blog/changelog/) — Feb 3–7, 2026

**Shinya Yanagihara** (Dev GBB)
