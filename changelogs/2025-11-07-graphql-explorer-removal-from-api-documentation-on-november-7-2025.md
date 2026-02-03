---
title: "GraphQL Explorer removal from API documentation on November 7, 2025"
date: "2025-11-07"
type: "deprecations"
labels: ["ecosystem and accessibility"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-07-graphql-explorer-removal-from-api-documentation-on-november-7-2025"
fetched_at: "2026-02-03T14:40:06.204745Z"
---

# GraphQL Explorer removal from API documentation on November 7, 2025

## Overview
Editor’s note (November 18, 2025): We’ve updated this post to clarify impact on enterprises.

## Detailed Explanation
### Overview
- Editor’s note (November 18, 2025): We’ve updated this post to clarify impact on enterprises.
- Following the previous announcement notice , we retired GraphQL Explorer.

### Who this affects
- Customers who use the audit log will see org_credential_authorization.deauthorize , oauth_authorization.destroy , and oauth_access.destroy events for multiple users in their enterprise. These events are associated with the deletion of GraphQL Explorer’s OAuth App.

### Why this change matters
- We understand that retiring the Explorer will disrupt the workflow of developers who used it for quick testing or prototyping with the GitHub GraphQL API. Although its overall usage was limited, we know this change is disappointing for users who relied on it.
- The decision to retire the Explorer has not been made lightly and is driven by increasing technical debt, costly ongoing maintenance (especially for security and accessibility), and reliance on third-party libraries we can’t keep compliant.

### What you should do
- If you currently use the GraphQL Explorer, we recommend transitioning to a local development tool for working with the GitHub GraphQL API. Our updated documentation includes guidance on getting started with popular GraphQL clients.

### Learn more
- To learn more about working with the GitHub GraphQL API, see our GraphQL API documentation .
- Have feedback or questions? Join the conversation in the GitHub Community .
- This change supports our ongoing commitment to make GitHub’s APIs faster, more scalable, and easier to use for everyone.

## Impact / Who’s Affected
- Following the previous announcement notice , we retired GraphQL Explorer.
- Although its overall usage was limited, we know this change is disappointing for users who relied on it.

## Caveats / Limitations
- Editor’s note (November 18, 2025): We’ve updated this post to clarify impact on enterprises.
- Although its overall usage was limited, we know this change is disappointing for users who relied on it.

## Insights (derived from article language)
- What you should do If you currently use the GraphQL Explorer, we recommend transitioning to a local development tool for working with the GitHub GraphQL API.
- Learn more To learn more about working with the GitHub GraphQL API, see our GraphQL API documentation .

## Article Content (cleaned)
*Editor’s note (November 18, 2025\): We’ve updated this post to clarify impact on enterprises.*


Following the [previous announcement notice](https://github.blog/changelog/2025-08-22-graphql-explorer-removal-from-api-documentation-on-november-1-2025/), we retired GraphQL Explorer.


## [Who this affects](#who-this-affects)


Customers who use the [audit log](https://docs.github.com/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization) will see `org_credential_authorization.deauthorize`, `oauth_authorization.destroy`, and `oauth_access.destroy` events for multiple users in their enterprise. These events are associated with the deletion of GraphQL Explorer’s OAuth App.


## [Why this change matters](#why-this-change-matters)


We understand that retiring the Explorer will disrupt the workflow of developers who used it for quick testing or prototyping with the GitHub GraphQL API. Although its overall usage was limited, we know this change is disappointing for users who relied on it.


The decision to retire the Explorer has not been made lightly and is driven by increasing technical debt, costly ongoing maintenance (especially for security and accessibility), and reliance on third\-party libraries we can’t keep compliant.


## [What you should do](#what-you-should-do)


If you currently use the GraphQL Explorer, we recommend transitioning to a local development tool for working with the GitHub GraphQL API. Our [updated documentation](https://docs.github.com/graphql/guides/using-graphql-clients) includes guidance on getting started with popular GraphQL clients.


## [Learn more](#learn-more)


To learn more about working with the GitHub GraphQL API, see our [GraphQL API documentation](https://docs.github.com/graphql).


Have feedback or questions? Join the conversation in the [GitHub Community](https://github.com/orgs/community/discussions/categories/announcements).




---


*This change supports our ongoing commitment to make GitHub’s APIs faster, more scalable, and easier to use for everyone.*
