---
title: "MCP registry and allowlist controls for Copilot in JetBrains, Eclipse, and Xcode now in public preview"
date: "2025-10-28"
type: "improvements"
labels: ["copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-mcp-registry-and-allowlist-controls-for-copilot-in-jetbrains-eclipse-and-xcode-now-in-public-preview"
fetched_at: "2026-02-03T14:40:06.636712Z"
---

# MCP registry and allowlist controls for Copilot in JetBrains, Eclipse, and Xcode now in public preview

## Overview
Enterprise and organization administrators can now configure which MCP servers their developers can discover and use in JetBrains, Eclipse, and Xcode nightly and prerelease builds.

## Detailed Explanation
### Overview
- Enterprise and organization administrators can now configure which MCP servers their developers can discover and use in JetBrains, Eclipse, and Xcode nightly and prerelease builds.

### MCP registry
- An MCP registry is a directory of Model Context Protocol (MCP) servers. Developers using JetBrains IDEs, Eclipse, and Xcode can now browse and install MCP servers directly from a registry within their IDE, streamlining discovery and setup.

### Allowlist controls
- Administrators now have more oversight around which MCP servers are available to developers.
- Note: These features are in early public preview and may evolve as we gather feedback. Current enforcement is based on MCP server name matching, with additional validation and more granular policy options planned for future releases.

### For admins: Configure registry controls
- Allowlist controls are available only for Copilot Business and Copilot Enterprise customers.
- Go to your GitHub Enterprise settings in the new AI Controls tab and find “MCP”. Or at the organization-level, Organization settings → Policies → Copilot → Policies .
- Enable MCP servers in Copilot .
- Add your MCP registry URL.
- Choose enforcement mode: Allow all (default): Developers can use any MCP server. Registry servers appear as recommended. Registry only: Developers can only run servers from your registry. Others are blocked at runtime.
- Allow all (default): Developers can use any MCP server. Registry servers appear as recommended.
- Registry only: Developers can only run servers from your registry. Others are blocked at runtime.
- For detailed setup and registry format specifications, see our MCP setup documentation .

### For developers: MCP registry in your IDE
- What you’ll see varies depending on your organization’s policy:
- Allow all: All servers work. Registry servers are easily discoverable.
- Registry only: Servers not in the registry are blocked at runtime with a warning.

### JetBrains IDEs (nightly)
- Sign in and open Copilot chat, then click the MCP registry icon.
- Browse, install, or uninstall MCP servers from the registry.
- Optionally, click Configure MCP Registry URL to use a custom registry.

### Eclipse (prerelease)
- In the Copilot chat panel top bar, click the MCP registry icon.
- Browse, install, or uninstall MCP servers from the registry.
- Optionally, click Configure Registry URL to use a custom registry.

### Xcode (prerelease)
- Open GitHub Copilot for Xcode, sign in, and click Configure MCP server in the chat panel.
- Under MCP registry URL, click Browse MCP Servers… to view and manage servers.
- Optionally, click Edit URL to use a custom registry.

### Installation
- You can try this out in the latest nightly release of Copilot for JetBrains, and the prerelease versions of Copilot for Eclipse and Xcode. Please install from one of the following locations:
- GitHub Copilot for JetBrains IDEs (nightly)
- GitHub Copilot for Eclipse (prerelease)
- GitHub Copilot for Xcode (prerelease)
- You will also need to have a valid Copilot license .

### Share your feedback
- We value your feedback! Share your experience through the following channels:
- GitHub Copilot for JetBrains IDEs
- GitHub Copilot for Eclipse
- GitHub Copilot for Xcode

## Impact / Who’s Affected
- Note: These features are in early public preview and may evolve as we gather feedback.
- For admins: Configure registry controls Allowlist controls are available only for Copilot Business and Copilot Enterprise customers.
- Registry only: Developers can only run servers from your registry.
- Registry only: Servers not in the registry are blocked at runtime with a warning.

## Caveats / Limitations
- Note: These features are in early public preview and may evolve as we gather feedback.
- For admins: Configure registry controls Allowlist controls are available only for Copilot Business and Copilot Enterprise customers.
- Registry only: Developers can only run servers from your registry.
- Registry only: Servers not in the registry are blocked at runtime with a warning.

## Article Content (cleaned)
Enterprise and organization administrators can now configure which MCP servers their developers can discover and use in JetBrains, Eclipse, and Xcode nightly and prerelease builds.


## [What’s new](#whats-new)


### [MCP registry](#mcp-registry)


An MCP registry is a directory of Model Context Protocol (MCP) servers. Developers using JetBrains IDEs, Eclipse, and Xcode can now browse and install MCP servers directly from a registry within their IDE, streamlining discovery and setup.


### [Allowlist controls](#allowlist-controls)


Administrators now have more oversight around which MCP servers are available to developers.



> **Note:** These features are in early public preview and may evolve as we gather feedback. Current enforcement is based on MCP server name matching, with additional validation and more granular policy options planned for future releases.


### [For admins: Configure registry controls](#for-admins-configure-registry-controls)


Allowlist controls are available only for Copilot Business and Copilot Enterprise customers.


1. Go to your GitHub Enterprise settings in the new **AI Controls** tab and find “MCP”. Or at the organization\-level, **Organization settings** → **Policies** → **Copilot** → **Policies**.
2. Enable **MCP servers in Copilot**.
3. Add your MCP registry URL.
4. Choose enforcement mode:
	* Allow all (default): Developers can use any MCP server. Registry servers appear as recommended.
	* Registry only: Developers can only run servers from your registry. Others are blocked at runtime.


For detailed setup and registry format specifications, see [our MCP setup documentation](https://docs.github.com/copilot/how-tos/administer-copilot/configure-mcp-server-access?utm_source=changelog-docs-mcp-registry-allowlist&utm_medium=changelog&utm_campaign=universe25).


### [For developers: MCP registry in your IDE](#for-developers-mcp-registry-in-your-ide)


What you’ll see varies depending on your organization’s policy:


* Allow all: All servers work. Registry servers are easily discoverable.
* Registry only: Servers not in the registry are blocked at runtime with a warning.


## [Set up your MCP registry](#set-up-your-mcp-registry)


### [JetBrains IDEs (nightly)](#jetbrains-ides-nightly)


1. Sign in and open Copilot chat, then click the **MCP registry** icon.
2. Browse, install, or uninstall MCP servers from the registry.
3. Optionally, click **Configure MCP Registry URL** to use a custom registry.


### [Eclipse (prerelease)](#eclipse-prerelease)


1. In the Copilot chat panel top bar, click the **MCP registry** icon.
2. Browse, install, or uninstall MCP servers from the registry.
3. Optionally, click **Configure Registry URL** to use a custom registry.


### [Xcode (prerelease)](#xcode-prerelease)


1. Open GitHub Copilot for Xcode, sign in, and click **Configure MCP** server in the chat panel.
2. Under MCP registry URL, click **Browse MCP Servers…** to view and manage servers.
3. Optionally, click **Edit URL** to use a custom registry.


## [Installation](#installation)


You can try this out in the latest nightly release of Copilot for JetBrains, and the prerelease versions of Copilot for Eclipse and Xcode. Please install from one of the following locations:


* [GitHub Copilot for JetBrains IDEs (nightly)](http://aka.ms/copilot-jb-mcpreg-allowlist-preview)
* [GitHub Copilot for Eclipse (prerelease)](https://aka.ms/copilot-ecl-mcpreg-allowlist-preview)
* [GitHub Copilot for Xcode (prerelease)](http://aka.ms/copilot-xd-mcpreg-allowlist-preview)


You will also need to have a valid [Copilot license](https://github.com/features/copilot?utm_source=changelog-copilot-mcp-registry-allowlist&utm_medium=changelog&utm_campaign=universe25).


## [Share your feedback](#share-your-feedback)


We value your feedback! Share your experience through the following channels:


* [GitHub Copilot for JetBrains IDEs](https://github.com/microsoft/copilot-intellij-feedback/issues?utm_source=changelog-jetbrains-mcp-registry-allowlist&utm_medium=changelog&utm_campaign=universe25)
* [GitHub Copilot for Eclipse](https://github.com/microsoft/copilot-eclipse-feedback/issues?utm_source=changelog-eclipse-mcp-registry-allowlist&utm_medium=changelog&utm_campaign=universe25)
* [GitHub Copilot for Xcode](https://github.com/github/CopilotForXcode/issues?utm_source=changelog-xcode-mcp-registry-allowlist&utm_medium=changelog&utm_campaign=universe25)
