---
title: "Copilot metrics in GitHub Enterprise Cloud with data residency in public preview"
date: "2026-01-29"
type: "Release"
labels: ["copilot", "enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-29-copilot-metrics-in-github-enterprise-cloud-with-data-residency-in-public-preview"
fetched_at: "2026-02-03T14:50:49.270734Z"
---

# Copilot metrics in GitHub Enterprise Cloud with data residency in public preview

## Overview
We know how important data residency is for compliance and regional requirements. To that point, the Copilot usage, code generation dashboards, and corresponding API are now available to customers on GitHub Enterprise Cloud with data residency.

## Detailed Explanation
### Overview
- We know how important data residency is for compliance and regional requirements. To that point, the Copilot usage, code generation dashboards, and corresponding API are now available to customers on GitHub Enterprise Cloud with data residency.

### What’s included?
- Customers on GitHub Enterprise Cloud with data residency can now see the following information:
- Copilot usage dashboard : Get clear, actionable insights into how your teams are using GitHub Copilot. The dashboard provides visibility into code completion activity, IDE usage, lines of code generated, and more.
- Code generation dashboard : Observe Copilot’s output by quantifying the lines it suggested, added, or deleted across completions, chat, and agent features.
- Fine-grain permissions : Access the APIs and dashboard if you are assigned the View enterprise Copilot metrics enterprise role. This means that all users assigned this role, not just enterprise admins or billing managers, are empowered to view granular Copilot usage metrics for the enterprise.
- Organization usage : Programmatically access your organization’s own Copilot adoption and usage metrics, including usage statistics for various Copilot features, user engagement data, and feature adoption metrics. For more information, see our API documentation .
- API access : Programmatically access Copilot usage data across your organization for custom reporting, monitoring, compliance, and advanced analytics.

### Availability
- For existing GitHub Enterprise Cloud customers migrating to GitHub Enterprise Cloud with data residency, note that usage data will be split across enterprises. Historical usage will remain associated with your existing enterprise, while usage after migration will be attributed to the new data residency enterprise due to account changes.
- If users are logged into multiple GitHub accounts within the IDE, usage generated will all be attributed to the GitHub Enterprise Cloud with data residency account and not shared across other accounts.
- To access the dashboard, navigate to your enterprise account → “AI Controls” → “Copilot” → “Metrics” → “Copilot usage metrics”. You should then see the dashboard under “Insights” → “Copilot usage” or “Code generation”. Please also ensure you are either an enterprise administrator, billing manager, or have the proper fine-grained permissions that grant you access to Copilot metrics.
- For API access, visit our Copilot usage metrics API documentation .
- Join the discussion within GitHub Community .

## Impact / Who’s Affected
- To that point, the Copilot usage, code generation dashboards, and corresponding API are now available to customers on GitHub Enterprise Cloud with data residency.

## Caveats / Limitations
- We know how important data residency is for compliance and regional requirements.
- Availability For existing GitHub Enterprise Cloud customers migrating to GitHub Enterprise Cloud with data residency, note that usage data will be split across enterprises.

## Insights (derived from article language)
- Availability For existing GitHub Enterprise Cloud customers migrating to GitHub Enterprise Cloud with data residency, note that usage data will be split across enterprises.
- You should then see the dashboard under “Insights” → “Copilot usage” or “Code generation”.

## Article Content (cleaned)
We know how important data residency is for compliance and regional requirements. To that point, the Copilot usage, code generation dashboards, and corresponding API are now available to customers on GitHub Enterprise Cloud with data residency.


### [What’s included?](https://github.blog/changelog/feed/#whats-included)


Customers on GitHub Enterprise Cloud with data residency can now see the following information:


* **Copilot usage dashboard**: Get clear, actionable insights into how your teams are using GitHub Copilot. The dashboard provides visibility into code completion activity, IDE usage, lines of code generated, and more.
* **Code generation dashboard**: Observe Copilot’s output by quantifying the lines it suggested, added, or deleted across completions, chat, and agent features.
* **Fine\-grain permissions**: Access the APIs and dashboard if you are assigned the `View enterprise Copilot metrics` enterprise role. This means that all users assigned this role, not just enterprise admins or billing managers, are empowered to view granular Copilot usage metrics for the enterprise.
* **Organization usage**: Programmatically access your organization’s own Copilot adoption and usage metrics, including usage statistics for various Copilot features, user engagement data, and feature adoption metrics. For more information, see [our API documentation](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics?apiVersion=2022-11-28#get-copilot-organization-usage-metrics-for-a-specific-day).
* **API access**: Programmatically access Copilot usage data across your organization for custom reporting, monitoring, compliance, and advanced analytics.


### [Availability](https://github.blog/changelog/feed/#availability)


* For existing GitHub Enterprise Cloud customers migrating to GitHub Enterprise Cloud with data residency, note that usage data will be split across enterprises. Historical usage will remain associated with your existing enterprise, while usage after migration will be attributed to the new data residency enterprise due to account changes.
* If users are logged into multiple GitHub accounts within the IDE, usage generated will all be attributed to the GitHub Enterprise Cloud with data residency account and not shared across other accounts.
* To access the dashboard, navigate to your enterprise account → “AI Controls” → “Copilot” → “Metrics” → “Copilot usage metrics”. You should then see the dashboard under “Insights” → “Copilot usage” or “Code generation”. Please also ensure you are either an enterprise administrator, billing manager, or have the proper fine\-grained permissions that grant you access to Copilot metrics.
* For API access, visit our [Copilot usage metrics API documentation](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics?apiVersion=2022-11-28).


Join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/185365).
