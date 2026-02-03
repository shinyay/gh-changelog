---
title: "Enhanced MCP OAuth support for GitHub Copilot in JetBrains, Eclipse, and Xcode"
date: "2025-11-18"
type: "improvements"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-18-enhanced-mcp-oauth-support-for-github-copilot-in-jetbrains-eclipse-and-xcode"
fetched_at: "2026-02-03T14:50:55.198967Z"
---

# Enhanced MCP OAuth support for GitHub Copilot in JetBrains, Eclipse, and Xcode

## Overview
We’ve introduced enhanced authentication capabilities in GitHub Copilot plugins for JetBrains, Eclipse, and Xcode to support more third-party OAuth providers with a secure and flexible approach using Dynamic Client Registration (DCR) and fallback mechanisms.

## Detailed Explanation
### Overview
- We’ve introduced enhanced authentication capabilities in GitHub Copilot plugins for JetBrains, Eclipse, and Xcode to support more third-party OAuth providers with a secure and flexible approach using Dynamic Client Registration (DCR) and fallback mechanisms.

### What’s new
- GitHub Copilot plugins for JetBrains, Eclipse, and Xcode now support authentication for more identity providers (IdPs) beyond the GitHub MCP server, using OAuth 2.0 and OAuth 2.1 standards.
- MCP first attempts a Dynamic Client Registration (DCR) handshake for automatic client setup. If the IdP does not support DCR, Copilot falls back to a client-credentials workflow, allowing you to manually configure static client IDs and secrets. These improvements give developers greater flexibility to integrate enterprise IdPs or custom identity services while maintaining security and compliance.

### Try it out
- These enhancements are in preview and available today to all JetBrains IDEs , Eclipse , and Xcode users. You need to update the plugin or app to the latest version and will also need to have a valid Copilot license .
- For more details on MCP authentication, please refer to the official documentation .

### Share your feedback
- We value your feedback! Share your experience through the following channels: – GitHub Copilot for JetBrains IDEs – GitHub Copilot for Eclipse – GitHub Copilot for Xcode

## Insights (derived from article language)
- For more details on MCP authentication, please refer to the official documentation .

## Article Content (cleaned)
We’ve introduced enhanced authentication capabilities in GitHub Copilot plugins for JetBrains, Eclipse, and Xcode to support more third\-party OAuth providers with a secure and flexible approach using Dynamic Client Registration (DCR) and fallback mechanisms.


## [What’s new](#whats-new)


GitHub Copilot plugins for JetBrains, Eclipse, and Xcode now support authentication for more identity providers (IdPs) beyond the GitHub MCP server, using OAuth 2\.0 and OAuth 2\.1 standards.


MCP first attempts a Dynamic Client Registration (DCR) handshake for automatic client setup. If the IdP does not support DCR, Copilot falls back to a client\-credentials workflow, allowing you to manually configure static client IDs and secrets. These improvements give developers greater flexibility to integrate enterprise IdPs or custom identity services while maintaining security and compliance.


## [Try it out](#try-it-out)


These enhancements are in preview and available today to all [JetBrains IDEs](https://plugins.jetbrains.com/plugin/17718-github-copilot), [Eclipse](https://marketplace.eclipse.org/content/github-copilot), and [Xcode](https://github.com/github/copilotforXcode/) users. You need to update the plugin or app to the latest version and will also need to have a valid [Copilot license](https://github.com/features/copilot).


For more details on MCP authentication, please refer to the official [documentation](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization).


## [Share your feedback](#share-your-feedback)


We value your feedback! Share your experience through the following channels:  

– [GitHub Copilot for JetBrains IDEs](https://github.com/microsoft/copilot-intellij-feedback/issues)  

– [GitHub Copilot for Eclipse](https://github.com/microsoft/copilot-eclipse-feedback/issues)  

– [GitHub Copilot for Xcode](https://github.com/github/CopilotForXcode/issues)
