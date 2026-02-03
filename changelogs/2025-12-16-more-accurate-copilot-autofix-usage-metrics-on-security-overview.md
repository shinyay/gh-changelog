---
title: "More accurate Copilot Autofix usage metrics on security overview"
date: "2025-12-16"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-16-more-accurate-copilot-autofix-usage-metrics-on-security-overview"
fetched_at: "2026-02-03T14:50:54.932756Z"
---

# More accurate Copilot Autofix usage metrics on security overview

## Overview
We have enhanced the metrics displayed on the security overview dashboard for CodeQL alerts fixed with Copilot autofixes.

## Detailed Explanation
### Overview
- We have enhanced the metrics displayed on the security overview dashboard for CodeQL alerts fixed with Copilot autofixes.
- This improvement specifically refines how we calculate how much of an autofix suggestion was used to remediate CodeQL alerts detected in pull requests and in scans of the default branch. This provides more accurate metrics on the “CodeQL pull request insights” dashboard and security overview Remediation tab, giving you better insight into how Copilot Autofix helps prevent new vulnerabilities from being merged into your code and helps reduce the security debt on your default branches.
- This change will retroactively affect dashboard metrics related to CodeQL alerts detected in pull requests and on a repository’s default branch that were fixed using autofix suggestions. The “Alerts fixed with autofix suggestions” and “Percentage of remediated alerts with autofix suggestion” will be sequentially recalculated over the next 10 days, and changes in these values are expected.
- This update is now generally available on GitHub Enterprise Cloud.
- Learn more by checking out our security overview documentation and our code scanning documentation .

## Impact / Who’s Affected
- This update is now generally available on GitHub Enterprise Cloud.

## Insights (derived from article language)
- Learn more by checking out our security overview documentation and our code scanning documentation .

## Article Content (cleaned)
We have enhanced the metrics displayed on the security overview dashboard for CodeQL alerts fixed with Copilot autofixes.


This improvement specifically refines how we calculate how much of an autofix suggestion was used to remediate CodeQL alerts detected in pull requests and in scans of the default branch. This provides more accurate metrics on the “CodeQL pull request insights” dashboard and security overview **Remediation** tab, giving you better insight into how Copilot Autofix helps prevent new vulnerabilities from being merged into your code and helps reduce the security debt on your default branches.


![Screenshot of table showing CodeQL pull request alerts fixed with Copilot autofixes on the security overview dashboard](https://github.com/user-attachments/assets/8e9d36b1-98dd-4d90-9d09-b2026331dd58)


This change will retroactively affect dashboard metrics related to CodeQL alerts detected in pull requests and on a repository’s default branch that were fixed using autofix suggestions. The “Alerts fixed with autofix suggestions” and “Percentage of remediated alerts with autofix suggestion” will be sequentially recalculated over the next 10 days, and changes in these values are expected.


This update is now generally available on GitHub Enterprise Cloud.


Learn more by checking out our [security overview documentation](https://docs.github.com/enterprise-cloud@latest/code-security/security-overview/about-security-overview) and our [code scanning documentation](https://docs.github.com/enterprise-cloud@latest/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning).
