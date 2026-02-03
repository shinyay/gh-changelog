---
title: "MCP registry and allowlist controls for VS Code Stable in public preview"
date: "2025-11-18"
type: "improvements"
labels: ["copilot", "platform governance"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-18-internal-mcp-registry-and-allowlist-controls-for-vs-code-stable-in-public-preview"
fetched_at: "2026-02-03T14:50:55.263280Z"
---

# MCP registry and allowlist controls for VS Code Stable in public preview

## Overview
Enterprise and organization administrators can now configure MCP registries and enforce allowlist policies in the latest release of VS Code Stable , bringing these governance controls to the majority of Copilot users. Additionally, the latest version of Visual Studio now supports registry discovery, with enforcement coming in a future release.

## Detailed Explanation
### Overview
- Enterprise and organization administrators can now configure MCP registries and enforce allowlist policies in the latest release of VS Code Stable , bringing these governance controls to the majority of Copilot users. Additionally, the latest version of Visual Studio now supports registry discovery, with enforcement coming in a future release.

### Understanding MCP registries and allowlists
- An MCP registry is a catalog of MCP servers. GitHub administrators can upload a URL for an internal registry in their enterprise or organization’s Copilot policies page. The registry serves two purposes:
- Discovery : It makes approved MCP servers visible and easily installable in MCP-compatible Copilot host applications (like Copilot in VS Code).
- Allowlisting : When combined with the Registry-only policy, it prevents any usage of MCP servers (at runtime) that are not defined in the internal registry.
- Think of the uploaded registry as a recommended vendor list, while the “Restrict MCP access to registry servers” policy determines whether that list is strictly enforced or simply recommended.

### Setting up your registry
- You can host your MCP registry using a couple of approaches:
- Azure API Center : You can use Microsoft’s managed Azure API Center service for dynamic registry management with enterprise MCP governance features.
- Self-hosting : You can fork and self-host the open-source MCP Registry or publish your own custom implementation that supports URL routing. Self-hosted registries must follow the v0.1 MCP registry specification . The registry must support the required endpoints and include proper CORS headers.

### Current availability
- VS Code Stable now has the full experience available: – Registry servers appear in the MCP servers sidebar panel. – Registry-only policy actively blocks servers that aren’t on the registry at runtime. – Clear policy messaging shows which organization or enterprise is enforcing restrictions.
- Visual Studio now supports internal MCP registries configured in GitHub.com: – Registry servers appear in the MCP servers interface for discovery. – Allowlist enforcement is not yet available. All servers can run regardless of policy setting.
- This VS Code Stable release brings MCP governance controls to the majority of Copilot users, allowing enterprises and organizations to enforce company policies across their developer base. Visual Studio users can begin discovering approved servers through internal registries, with allowlist enforcement support coming in a future release.
- For information on support statuses by Copilot host application, see Support surfaces for MCP usage in your company .

### Policy options
- When configuring your MCP access policy, you have two choices:
- Allow all (default): Your registry servers appear as recommendations, but developers can use any MCP server.
- Registry only : Developers can only use servers listed in your registry. All others are blocked with a clear policy message.
- Local vs. remote server enforcement : Remote MCP servers are validated against both the server name and the remote install URL, providing strict enforcement. Local server enforcement currently validates against server name only, meaning the configuration can be edited locally. For enterprises with strict security requirements, we recommend configuring remote servers only in your registry.

### Getting started
- This feature is available for Copilot Business and Copilot Enterprise customers. With VS Code Stable support, you can now deploy and enforce MCP governance controls more widely across your organization.
- For setup instructions and registry format specifications, see Configure an MCP registry for your organization or enterprise .

## Impact / Who’s Affected
- Allowlisting : When combined with the Registry-only policy, it prevents any usage of MCP servers (at runtime) that are not defined in the internal registry.
- Current availability VS Code Stable now has the full experience available: – Registry servers appear in the MCP servers sidebar panel. – Registry-only policy actively blocks servers that aren’t on the registry at runtime. – Clear policy messaging shows which organization or enterprise is enforcing restrictions.
- Registry only : Developers can only use servers listed in your registry.
- Local server enforcement currently validates against server name only, meaning the configuration can be edited locally.
- For enterprises with strict security requirements, we recommend configuring remote servers only in your registry.

## Caveats / Limitations
- Allowlisting : When combined with the Registry-only policy, it prevents any usage of MCP servers (at runtime) that are not defined in the internal registry.
- Current availability VS Code Stable now has the full experience available: – Registry servers appear in the MCP servers sidebar panel. – Registry-only policy actively blocks servers that aren’t on the registry at runtime. – Clear policy messaging shows which organization or enterprise is enforcing restrictions.
- Registry only : Developers can only use servers listed in your registry.
- Local server enforcement currently validates against server name only, meaning the configuration can be edited locally.
- For enterprises with strict security requirements, we recommend configuring remote servers only in your registry.

## Insights (derived from article language)
- For enterprises with strict security requirements, we recommend configuring remote servers only in your registry.

## Article Content (cleaned)
Enterprise and organization administrators can now configure MCP registries and enforce allowlist policies in the [latest release of VS Code Stable](https://code.visualstudio.com/updates/v1_106#_mcp-server-access-for-your-organization), bringing these governance controls to the majority of Copilot users. Additionally, the [latest version of Visual Studio](https://learn.microsoft.com/en-us/visualstudio/releases/2026/release-notes) now supports registry discovery, with enforcement coming in a future release.


## [Understanding MCP registries and allowlists](#understanding-mcp-registries-and-allowlists)


An MCP registry is a catalog of MCP servers. GitHub administrators can upload a URL for an internal registry in their enterprise or organization’s Copilot policies page. The registry serves two purposes:


* **Discovery**: It makes approved MCP servers visible and easily installable in MCP\-compatible Copilot host applications (like Copilot in VS Code).
* **Allowlisting**: When combined with the Registry\-only policy, it prevents any usage of MCP servers (at runtime) that are not defined in the internal registry.


Think of the uploaded registry as a recommended vendor list, while the “Restrict MCP access to registry servers” policy determines whether that list is strictly enforced or simply recommended.


## [Setting up your registry](#setting-up-your-registry)


You can host your MCP registry using a couple of approaches:


* **Azure API Center**: You can use Microsoft’s managed [Azure API Center](https://learn.microsoft.com/azure/api-center/overview) service for dynamic registry management with enterprise MCP governance features.
* **Self\-hosting**: You can fork and self\-host the open\-source [MCP Registry](https://github.com/modelcontextprotocol/registry) or publish your own custom implementation that supports URL routing. Self\-hosted registries must follow the [v0\.1 MCP registry specification](https://registry.modelcontextprotocol.io/docs). The registry must support the required endpoints and include proper CORS headers.


## [Current availability](#current-availability)


**VS Code Stable** now has the full experience available:  

– Registry servers appear in the MCP servers sidebar panel.  

– Registry\-only policy actively blocks servers that aren’t on the registry at runtime.  

– Clear policy messaging shows which organization or enterprise is enforcing restrictions.


**Visual Studio** now supports internal MCP registries configured in GitHub.com:  

– Registry servers appear in the MCP servers interface for discovery.  

– Allowlist enforcement is not yet available. All servers can run regardless of policy setting.


This VS Code Stable release brings MCP governance controls to the majority of Copilot users, allowing enterprises and organizations to enforce company policies across their developer base. Visual Studio users can begin discovering approved servers through internal registries, with allowlist enforcement support coming in a future release.


For information on support statuses by Copilot host application, see [Support surfaces for MCP usage in your company](https://docs.github.com/en/copilot/concepts/mcp-management#supported-surfaces).


## [Policy options](#policy-options)


When configuring your MCP access policy, you have two choices:


* **Allow all** (default): Your registry servers appear as recommendations, but developers can use any MCP server.
* **Registry only**: Developers can only use servers listed in your registry. All others are blocked with a clear policy message.


**Local vs. remote server enforcement**: Remote MCP servers are validated against both the server name and the remote install URL, providing strict enforcement. Local server enforcement currently validates against server name only, meaning the configuration can be edited locally. For enterprises with strict security requirements, we recommend configuring remote servers only in your registry.


## [Getting started](#getting-started)


This feature is available for Copilot Business and Copilot Enterprise customers. With VS Code Stable support, you can now deploy and enforce MCP governance controls more widely across your organization.


For setup instructions and registry format specifications, see [Configure an MCP registry for your organization or enterprise](https://docs.github.com/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-server-access).
