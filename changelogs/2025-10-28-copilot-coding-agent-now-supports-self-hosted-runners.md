---
title: "Copilot coding agent now supports self-hosted runners"
date: "2025-10-28"
type: "improvements"
labels: ["actions", "copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-copilot-coding-agent-now-supports-self-hosted-runners"
fetched_at: "2026-02-03T14:50:55.592276Z"
---

# Copilot coding agent now supports self-hosted runners

## Overview
You can now configure Copilot coding agent’s development environment to run in your own infrastructure using self-hosted GitHub Actions runners managed by Actions Runner Controller (ARC). With this setup, you can give Copilot access to internal resources (e.g. packages) not available on the public internet.

## Detailed Explanation
### Overview
- You can now configure Copilot coding agent’s development environment to run in your own infrastructure using self-hosted GitHub Actions runners managed by Actions Runner Controller (ARC). With this setup, you can give Copilot access to internal resources (e.g. packages) not available on the public internet.
- Copilot coding agent is our asynchronous, autonomous background agent. Delegate a task to Copilot and it opens a draft pull request, makes changes in the background, and then requests a review from you. Copilot works in its own ephemeral development environment, powered by GitHub Actions, where it can run the repository’s build process, automated tests, and more.
- ARC scale sets are supported as a runs-on: target for the copilot-setup-steps.yml configuration file when customizing the coding agent’s development environment. To get started:
- Deploy ARC and configure a scale set.
- Update the runs-on: target in copilot-setup-steps.yml to the scale set.
- For additional guidance, refer to our documentation on customizing the development environment for GitHub Copilot coding agent .

## Article Content (cleaned)
You can now configure Copilot coding agent’s development environment to run in your own infrastructure using self\-hosted GitHub Actions runners managed by Actions Runner Controller (ARC). With this setup, you can give Copilot access to internal resources (e.g. packages) not available on the public internet.


[Copilot coding agent](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent?utm_source=changelog-docs-cca-selfhosted-runners&utm_medium=changelog&utm_campaign=universe25) is our asynchronous, autonomous background agent. Delegate a task to Copilot and it opens a draft pull request, makes changes in the background, and then requests a review from you. Copilot works in its own ephemeral development environment, powered by GitHub Actions, where it can run the repository’s build process, automated tests, and more.


ARC scale sets are supported as a `runs-on:` target for the `copilot-setup-steps.yml` configuration file when customizing the coding agent’s development environment. To get started:


1. [Deploy ARC](https://docs.github.com/actions/tutorials/use-actions-runner-controller/quickstart?utm_source=changelog-docs-cca-selfhosted-runners&utm_medium=changelog&utm_campaign=universe25) and configure a scale set.
2. Update the `runs-on:` target in `copilot-setup-steps.yml` to the scale set.



```
jobs:
  copilot-setup-steps:
    runs-on: arc-scale-set-name

```

For additional guidance, refer to [our documentation on customizing the development environment for GitHub Copilot coding agent](https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment?utm_source=changelog-docs-cca-selfhosted-runners&utm_medium=changelog&utm_campaign=universe25).
