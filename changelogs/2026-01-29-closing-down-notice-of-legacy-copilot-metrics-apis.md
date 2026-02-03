---
title: "Closing down notice of legacy Copilot metrics APIs"
date: "2026-01-29"
type: "Retired"
labels: ["account management", "copilot", "enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-29-closing-down-notice-of-legacy-copilot-metrics-apis"
fetched_at: "2026-02-03T14:40:04.804110Z"
---

# Closing down notice of legacy Copilot metrics APIs

## Overview
We are closing down three legacy Copilot metrics APIs as part of our transition to newer, more comprehensive usage metrics endpoints. Support for these APIs will be limited, and no new features will be developed.

## Detailed Explanation
### Overview
- We are closing down three legacy Copilot metrics APIs as part of our transition to newer, more comprehensive usage metrics endpoints. Support for these APIs will be limited, and no new features will be developed.
- The User-level Feature Engagement Metrics API and Direct Data Access API will sunset on March 2nd, 2026.
- The Copilot Metrics API will sunset on April 2nd, 2026.
- We strongly recommend transitioning any existing workflows to the latest Copilot usage metrics endpoints to avoid disruption.

### What do these APIs do?
- These APIs provide visibility into adoption and usage of GitHub Copilot features:
- User-level Feature Engagement Metrics API offers a simplified view of user adoption of specific Copilot features through binary indicators.
- Direct Data Access API provides user-level event data for Copilot code completion activity within supported IDEs.
- Copilot Metrics API provides aggregated usage metrics, primarily focused on IDE usage.

### Why?
- We have released a new set of Copilot usage metrics APIs that provide significantly more depth and flexibility. By consolidating to our latest APIs, we are able to:
- Provide a single, unified source of truth for Copilot metrics.
- Deliver more granular and valuable insights, including IDE agents, models, languages, lines of code, and fine-grained permissions.
- Reduce support overhead and streamline the product experience.

### What’s recommended moving forward?
- We recommend transitioning to the latest Copilot usage metrics APIs , which provide comprehensive usage data at the enterprise, organization, and user levels.
- These endpoints return aggregated metrics with expanded IDE telemetry, including:
- Edit modes and agent usage.
- Suggested versus accepted lines of code.
- Language and model breakdowns.
- Additional usage dimensions not available in the legacy APIs.
- The new APIs are currently in public preview and will be generally available in the near future.

## Impact / Who’s Affected
- Support for these APIs will be limited, and no new features will be developed.
- The User-level Feature Engagement Metrics API and Direct Data Access API will sunset on March 2nd, 2026.
- The Copilot Metrics API will sunset on April 2nd, 2026.
- The new APIs are currently in public preview and will be generally available in the near future.

## Caveats / Limitations
- Support for these APIs will be limited, and no new features will be developed.

## Insights (derived from article language)
- We recommend transitioning to the latest Copilot usage metrics APIs , which provide comprehensive usage data at the enterprise, organization, and user levels.

## Article Content (cleaned)
We are closing down three legacy Copilot metrics APIs as part of our transition to newer, more comprehensive usage metrics endpoints. Support for these APIs will be limited, and no new features will be developed.


* The User\-level Feature Engagement Metrics API and Direct Data Access API will sunset on March 2nd, 2026\.
* The Copilot Metrics API will sunset on April 2nd, 2026\.


We strongly recommend transitioning any existing workflows to the [latest Copilot usage metrics endpoints](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics?apiVersion=2022-11-28) to avoid disruption.


### [What do these APIs do?](https://github.blog/changelog/feed/#what-do-these-apis-do)


These APIs provide visibility into adoption and usage of GitHub Copilot features:


* [User\-level Feature Engagement Metrics API](https://docs.github.com/enterprise-cloud@latest/early-access/copilot/user-level-feature-engagement-metrics-api) offers a simplified view of user adoption of specific Copilot features through binary indicators.
* [Direct Data Access API](https://docs.github.com/enterprise-cloud@latest/early-access/copilot/direct-data-access) provides user\-level event data for Copilot code completion activity within supported IDEs.
* [Copilot Metrics API](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-metrics?apiVersion=2022-11-28) provides aggregated usage metrics, primarily focused on IDE usage.


### [Why?](https://github.blog/changelog/feed/#why)


We have released a new set of Copilot usage metrics APIs that provide significantly more depth and flexibility. By consolidating to our latest APIs, we are able to:


* Provide a single, unified source of truth for Copilot metrics.
* Deliver more granular and valuable insights, including IDE agents, models, languages, lines of code, and fine\-grained permissions.
* Reduce support overhead and streamline the product experience.


### [What’s recommended moving forward?](https://github.blog/changelog/feed/#whats-recommended-moving-forward)


We recommend transitioning to the [latest Copilot usage metrics APIs](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics?apiVersion=2022-11-28), which provide comprehensive usage data at the enterprise, organization, and user levels.


These endpoints return aggregated metrics with expanded IDE telemetry, including:


* Edit modes and agent usage.
* Suggested versus accepted lines of code.
* Language and model breakdowns.
* Additional usage dimensions not available in the legacy APIs.


The new APIs are currently in public preview and will be generally available in the near future.
