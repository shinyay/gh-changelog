---
title: "Delegate AI controls management to members of your enterprise"
date: "2025-11-03"
type: "new releases"
labels: ["copilot", "enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-03-delegate-ai-controls-management-to-members-of-your-enterprise"
fetched_at: "2026-02-03T14:50:55.472602Z"
---

# Delegate AI controls management to members of your enterprise

## Overview
Enterprise owners can now delegate AI and Copilot policy as well as setup administration to their enterprise members and teams. You can now do this without granting broad enterprise ownership. These new fine-grained permissions (FGPs) can grant read or write access to the agent control plane in the enterprise account.

## Detailed Explanation
### Overview
- Enterprise owners can now delegate AI and Copilot policy as well as setup administration to their enterprise members and teams. You can now do this without granting broad enterprise ownership. These new fine-grained permissions (FGPs) can grant read or write access to the agent control plane in the enterprise account.
- At Universe 2025, we announced the public preview of the agent control plane . This is a suite of governance features designed to give enterprises deeper control over and greater ability to audit the use of Copilot features, custom agents, and MCP configurations across their business.
- Enterprise owners can now delegate management of the features in the agent control plane by creating a new enterprise custom role with one of the below FGPs:
- View enterprise AI controls : Allows the role to view all settings in the AI Controls tab for your enterprise.
- Manage enterprise AI controls : Allows the role to manage all settings in the AI Controls tab for your enterprise.
- Note : The above FGPs do not grant access to the deep links in the AI Controls tab like access management, audit logs, or rulesets, unless the corresponding FGPs that control those enterprise views are also added to the custom role. For example, Enterprise owners need to explicitly add the Read enterprise audit logs FGP to allow the custom role to view audit log events for your enterprise. This helps AI managers monitor agentic activity.
- An enterprise role with the above FGPs can then be assigned to individual members or to an enterprise team to enable AI management at scale.
- To learn more, see our documentation on establishing AI managers in your enterprise .
- Join the discussion within GitHub Community .

## Impact / Who’s Affected
- At Universe 2025, we announced the public preview of the agent control plane .

## Caveats / Limitations
- Note : The above FGPs do not grant access to the deep links in the AI Controls tab like access management, audit logs, or rulesets, unless the corresponding FGPs that control those enterprise views are also added to the custom role.

## Insights (derived from article language)
- To learn more, see our documentation on establishing AI managers in your enterprise .

## Article Content (cleaned)
Enterprise owners can now delegate AI and Copilot policy as well as setup administration to their enterprise members and teams. You can now do this without granting broad enterprise ownership. These new fine\-grained permissions (FGPs) can grant read or write access to the agent control plane in the enterprise account.


At Universe 2025, we announced the [public preview of the agent control plane](https://github.blog/changelog/2025-10-28-enterprise-ai-controls-the-agent-control-plane-are-in-public-preview/). This is a suite of governance features designed to give enterprises deeper control over and greater ability to audit the use of Copilot features, custom agents, and MCP configurations across their business.


Enterprise owners can now delegate management of the features in the agent control plane by creating a new enterprise custom role with one of the below FGPs:


* **View enterprise AI controls**: Allows the role to view all settings in the **AI Controls** tab for your enterprise.
* **Manage enterprise AI controls**: Allows the role to manage all settings in the **AI Controls** tab for your enterprise.


**Note**: The above FGPs do not grant access to the deep links in the **AI Controls** tab like access management, audit logs, or rulesets, unless the corresponding FGPs that control those enterprise views are also added to the custom role.  

For example, Enterprise owners need to explicitly add the **Read enterprise audit logs** FGP to allow the custom role to view audit log events for your enterprise. This helps AI managers monitor agentic activity.


An enterprise role with the above FGPs can then be assigned to individual members or to an enterprise team to enable AI management at scale.


To learn more, see our documentation on [establishing AI managers in your enterprise](https://docs.github.com/copilot/tutorials/roll-out-at-scale/establish-ai-managers).


Join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/178247?utm_source=changelog-community-enterprise-controls&utm_medium=changelog&utm_campaign=universe25).
