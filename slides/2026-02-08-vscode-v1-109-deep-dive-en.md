---
marp: true
theme: github-dark
paginate: true
header: "VS Code v1.109 Deep Dive"
footer: "January 2026 Release — February 8, 2026"
---

# VS Code v1.109 Deep Dive
## January 2026 Release — AI & Agent Edition

The new era of multi-agent development

**Shinya Yanagihara** (Dev GBB)

---

# Table of Contents

1. **Chat UX** — Faster, smarter, less friction
2. **Agent Session Management** — Unified multi-agent control
3. **Agent Customization** — Tailor AI for your team
4. **Agent Extensibility** — Claude Agent & MCP Apps
5. **Agent Optimizations** — Copilot Memory & fast search
6. **Agent Security & Trust** — Sandboxing & safety
7. **Azure Integration** — Model config & MCP
8. **Workbench & Editor** — Integrated browser & more

---

<!-- Section: Chat UX -->

# Chat UX
## Faster, Smarter, Less Friction

---

# Anthropic Thinking Tokens
## Chat UX

- Claude models now support **thinking tokens** — visibility into the model's reasoning
- Choose between detailed or compact thinking styles
- Model's thought process shown interleaved with tool calls and responses
- Failing tool calls automatically expand to show more context
- Scrollable thinking content with shimmer animations

---

# Mermaid Diagrams in Chat
## Chat UX

- Chat responses now render interactive **Mermaid diagrams**
- Uses the `renderMermaidDiagram` tool
- Flowcharts, sequence diagrams, and other visualizations for complex concepts
- Alt/Option + mouse wheel to zoom, drag to pan
- Open in full-sized editor, copy diagram source code

---

# Ask Questions Tool (Experimental)
## Chat UX

- Agent can now **ask clarifying questions** instead of making assumptions
- Single/multi-select options and free text input supported
- Recommended answers highlighted for quick decisions
- Keyboard navigation: Up/Down to select, number keys for direct answers
- **Plan agent** also leverages this tool for higher-quality implementation plans

---

# Plan Agent Evolution
## Chat UX

- Use `/plan` command to create structured implementation plans
- **4-phase iterative workflow**:
  1. **Discovery** — Autonomously explore your codebase
  2. **Alignment** — Ask clarifying questions to catch ambiguities early
  3. **Design** — Draft comprehensive plan with file locations and code snippets
  4. **Refinement** — Add verification criteria and document decisions

---

# Context Window Visibility
## Chat UX

- New **context window indicator** in the chat input area
- Hover for a per-category breakdown of token usage
- Understand at a glance how the model is using its context
- Monitor context pressure in real time

---

# Inline Chat UX Revamp (Preview)
## Chat UX

- New affordance to trigger inline chat more easily when selecting text
- Lightweight contextual rendering mode
- More natural in-editor interactions
- Configure via `inlineChat.affordance` / `inlineChat.renderMode`

---

# Terminal Command Output Enhancements
## Chat UX

- **Syntax highlighting**: Inline Node, Python, Ruby code colored in terminal output
- **Working directory**: Explicitly show which folder the command runs in
- **Command intent**: Hover to see "why" a command is being run
- **Output streaming**: Long-running commands auto-expand
- **Interactive input**: Type directly into embedded terminals

---

<!-- Section: Agent Session Management -->

# Agent Session Management
## Unified Multi-Agent Control

---

# Agent Session Types & Switching
## Agent Session Management

- **Local** — Interactive execution within VS Code
- **Background** — Local background execution
- **Cloud** — Autonomous execution on GitHub
- **Partner Agents** — Claude, Codex, and other external agents
- One-click switching via session type picker
- **Hand off** an in-progress session to a different environment

---

# Agent Sessions View Improvements
## Agent Session Management

- Resizable sessions list in side-by-side view
- **Multi-select** sessions for bulk operations
- Improved stacked view for better navigation and filtering
- **Agent Status Indicator**: Quickly see which sessions need attention from the command center
- Configurable chat button behavior (sidebar/maximized/hidden)

---

# Parallel Subagent Execution
## Agent Session Management

- Subagents now support **parallel execution**
- Speed up workflows by processing independent tasks simultaneously
- Each subagent operates in its own dedicated context window
- Does not consume the main agent's context budget
- Shows task details, tools in use, and custom agent names

---

# Search Subagent (Experimental)
## Agent Session Management

- Codebase search runs in an **isolated agent loop**
- Iteratively refine queries across multiple searches
- Preserves the main agent's context window
- Main agent continues working while search runs
- Enable with `github.copilot.chat.searchSubagent.enabled`

---

# Cloud Agent Enhancements
## Agent Session Management

- **Model selection**: Choose models for cloud agent sessions
- **Custom agents**: Use agents from your repository's default branch
- **Partner agents**: Select Claude, Codex, etc. where available
- **Multi-root workspace support**: Pick a folder for cloud agents
- **Checkout**: Auto-installs GitHub Pull Requests extension when needed

---

# Background Agent Improvements
## Agent Session Management

- Custom agent support added
- **Attach images as context**
- Multi-root workspace support
- **Auto-commit** to Git worktree at the end of each turn
- Removed Keep/Undo actions — simplified working set display

---

<!-- Section: Agent Customization -->

# Agent Customization
## Tailor AI for Your Team

---

# Set Up Your Workspace with `/init`
## Agent Customization

- `/init` command auto-generates AI instruction files
- Detects existing `copilot-instructions.md` and `AGENTS.md`
- Analyzes project structure and coding patterns
- Generates comprehensive workspace instructions tailored to your project
- Implemented as a prompt file — fully customizable

---

# Agent Skills Are Now GA
## Agent Customization

- **Agent Skills are generally available** (enabled by default)
- Package domain expertise: testing strategies, API design, performance optimization
- Manage via **Chat: Configure Skills** / **Chat: New Skill File** commands
- Searched in `.github/skills` / `.claude/skills` / `~/.copilot/skills`
- Extensions can distribute skills via `chatSkills` contribution point

---

# Organization-wide Instructions
## Agent Customization

- **Organization-level custom instructions** automatically applied
- GitHub org-configured Copilot instructions reflected in chat sessions
- Ensures consistent guidance across the entire team
- Enabled by default, individually disablable
- Works alongside previously released organization-level custom agents

---

# Custom Agent Invocation Control
## Agent Customization

- `user-invokable: false` — Hide from dropdown, subagent-only
- `disable-model-invocation` — Prevent auto-invocation by other agents
- `agents:` — Restrict which subagents an agent can invoke
- **Multiple model support**: Specify fallback models in order of preference

```markdown
---
name: Foo
tools: ['agent']
agents: ['Modify', 'Search']
model: ['Claude Sonnet 4.5 (copilot)', 'GPT-5 (copilot)']
---
```

---

# Agent Orchestration Patterns
## Agent Customization

- Multiple specialized agents **collaborate to achieve a common goal**
- Key benefits:
  - **Context efficiency**: Each subagent gets its own context window
  - **Specialization**: Use different models optimized for each task
  - **Parallel execution**: Independent tasks run simultaneously
- Community examples:
  - **Copilot Orchestra** — Conductor orchestrates planning, implementation, and review
  - **GitHub Copilot Atlas** — Prometheus, Oracle, Sisyphus, and Explorer agents

---

<!-- Section: Agent Extensibility -->

# Agent Extensibility
## Claude Agent & MCP Apps

---

# Claude Agent (Preview)
## Agent Extensibility

- **Anthropic's Claude Agent SDK** directly available in VS Code
- Runs on Claude models included in your GitHub Copilot subscription
- Uses the **same prompts, tools, and architecture** as Anthropic's official harness
- Select alongside Local / Background / Cloud in the session type picker
- In active development — more features coming soon

---

# Anthropic Model Enhancements
## Agent Extensibility

- **Messages API + Interleaved Thinking**: Model reasons between tool calls
- Configure thinking budget in tokens (set to 0 to disable)
- **Tool Search Tool**: Auto-discover the best tools from a large pool
- **Context Editing (Experimental)**: Clear previous turn's tool results and thinking
  - Defer summarization, maintain more context
  - Enable with `github.copilot.chat.anthropic.contextEditing.enabled`

---

# MCP Apps Support
## Agent Extensibility

- **MCP Apps**: MCP servers can display rich, interactive UI in the client
- Render interactive visualizations (flame graphs, etc.) directly in chat
- Apps display automatically when servers return them
- **Custom registry support**: Use `registryBaseUrl` property for
  private registries (Azure DevOps feeds, custom PyPI repositories, etc.)

---

<!-- Section: Agent Optimizations -->

# Agent Optimizations
## Copilot Memory & Fast Search

---

# Copilot Memory (Preview)
## Agent Optimizations

- **Store and recall important information across sessions**
- Chat can directly access and update Copilot Memory
- Save rules like "always ask clarifying questions when in doubt"
- Agent automatically decides when to store/retrieve memories
- View and manage all memories from GitHub's Copilot settings
- Enable with `github.copilot.chat.copilotMemory.enabled`

---

# External Indexing (Preview)
## Agent Optimizations

- **Non-GitHub workspaces can now be remotely indexed** for fast code search
- `#codebase` builds an index for semantic search capabilities
- First build may take a few minutes depending on repo size and network
- Subsequent requests use cached index — much faster
- Index auto-updates when files are saved
- Gradually rolling out over the coming weeks

---

# Read Files Outside Workspace
## Agent Optimizations

- Agents can now **read files and directories outside your workspace**
- Previously auto-denied — now controlled via allow/deny prompts
- Allow access for the entire session to avoid repeated prompts
- Useful for referencing config files and libraries outside the workspace

---

# Performance Improvements
## Agent Optimizations

- **Large chats**: Smoother scrolling and display for long conversations
- Optimized conversation persistence for better reliability
- **Parallel dependent tasks**: Build tasks processed in parallel instead of sequentially
- Significant speed improvements for projects with multiple independent build steps

---

<!-- Section: Agent Security & Trust -->

# Agent Security & Trust
## Sandboxing & Safety

---

# Terminal Sandboxing (Experimental)
## Agent Security & Trust

- **Restrict file system access** for agent-executed terminal commands
- Read/write limited to workspace folder only
- **Network access** controllable per domain
- No confirmation dialog needed when sandbox is enabled
- macOS / Linux only (Windows not yet supported)
- Enable with `chat.tools.terminal.sandbox.enabled`

---

# Terminal Tool Lifecycle Improvements
## Agent Security & Trust

- **Manually push commands to background** to free up the agent
- `timeout` property for automatic recovery from unexpected states
- `awaitTerminal` tool: Wait for background terminals to complete
- `killTerminal` tool: Clean up unneeded background terminals
- Eliminates hacky `echo "successful"` and `sleep n` workarounds

---

# Expanded Terminal Auto-Approval
## Agent Security & Trust

- The following commands now **auto-approved** by default:
  - `Set-Location`, `dir`, `od`, `xxd`
  - `docker` — All safe sub-commands
  - `npm`, `yarn`, `pnpm` — All safe sub-commands
- Enable with `chat.tools.terminal.enableAutoApprove`

---

<!-- Section: Azure -->

# Azure Integration
## Model Configuration & MCP

---

# Azure Model Configuration
## Azure Integration

- **Language Models editor** natively supports Azure model configuration
- Inserts snippet templates into `chatLanguageModels.json`
- Configure model ID, name, endpoint URL, token limits, and more
- Multiple provider configs: Separate personal and team API keys
- Existing GitHub Copilot Chat configurations auto-migrate

---

# Language Models Editor Enhancements
## Azure Integration

- **Multiple configs per provider**: Create groups with different API keys
- Provider group management: Update settings or remove entirely
- Keyboard access, context menus, and multi-select for bulk actions
- Directly edit and share model configuration files
- **Provider Configuration API (Proposed)**: Extensions declare schemas,
  VS Code auto-generates the configuration UI

---

# Custom Registry Support (MCP)
## Azure Integration

- `registryBaseUrl` property supported in MCP server manifests
- Deploy MCP servers from **Azure DevOps feeds** and custom PyPI repositories
- Manage MCP servers through your organization's private registries
- Enables secure agent extensibility in enterprise environments

---

<!-- Section: Workbench -->

# Workbench & Editor
## Integrated Browser & Developer Experience

---

# Integrated Browser (Preview)
## Workbench

- A **full-featured browser** built into VS Code — overcomes iframe limitations
- **Sign into websites** (Google, GitHub, Stack Overflow, etc.)
- Persistent data storage (global, workspace, or ephemeral)
- **Full DevTools** included
- Select elements and send them to a chat agent for assistance
- Launch via `Browser: Open Integrated Browser` command

---

# Editor Improvements
## Coding & Editor

- **Double-click to select bracket/string contents**: Click after opening bracket
  or before closing quote
- **Bracket matching foreground color**: Customize via `editorBracketMatch.foreground`
- **Improved ghost text visibility**: Dotted underline for short suggestions
- **Snippet file patterns**: `include`/`exclude` to scope snippets to specific files
- **Shebang detection**: `#!/usr/bin/env -S deno -A` correctly detected as TypeScript

---

# Other Notable Highlights
## Engineering & Enterprise

- **macOS DMG installer**: Drag-and-drop installation experience
- **Windows 11 context menu integration**: VS Code appears at the top level
- **Copilot extension deprecated**: Fully merged into Copilot Chat extension
- **Organization policy reliability**: Policies enforced even during offline startup
- **Kitty keyboard protocol**: Improved terminal keystroke handling

---

# Key Takeaways

- VS Code evolves into a **unified platform for multi-agent development**
- **Claude Agent (Preview)** natively integrates Anthropic's Agent SDK
- **Agent Orchestration** patterns enable complex collaborative workflows
- **Copilot Memory** maintains context across sessions
- **Terminal Sandboxing** ensures safe agent command execution
- **Azure model configuration** and **MCP custom registries** strengthen enterprise support

---

# Key Takeaways (continued)

- **Agent Skills GA** and org-level instructions unify AI quality across teams
- **Parallel subagent execution** and **External Indexing** deliver major speed gains
- **Integrated Browser** keeps development, testing, and debugging inside VS Code
- **Plan agent's** 4-phase workflow dramatically improves AI planning quality
- **MCP Apps** open the door to rich UI rendering from MCP servers

---

# Thank You

Source: [VS Code January 2026 Release Notes](https://code.visualstudio.com/updates/v1_109)

**Shinya Yanagihara** (Dev GBB)
