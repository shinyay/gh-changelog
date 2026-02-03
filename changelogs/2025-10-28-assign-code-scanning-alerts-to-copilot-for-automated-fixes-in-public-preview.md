---
title: "Assign code scanning alerts to Copilot for automated fixes in public preview"
date: "2025-10-28"
type: "new releases"
labels: ["application security", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-assign-code-scanning-alerts-to-copilot-for-automated-fixes-in-public-preview"
fetched_at: "2026-02-03T14:50:55.693811Z"
---

# Assign code scanning alerts to Copilot for automated fixes in public preview

## Overview
You can now assign GitHub code scanning alerts directly to Copilot to assist with automated remediation. This extends Copilot coding agent capabilities to security vulnerabilities, enabling faster resolution of common issues.

## Detailed Explanation
### Overview
- You can now assign GitHub code scanning alerts directly to Copilot to assist with automated remediation. This extends Copilot coding agent capabilities to security vulnerabilities, enabling faster resolution of common issues.
- Copilot coding agent works alongside Copilot Autofix to reduce the time developers spend planning and implementing security fixes. First, generate an autofix suggestion for your code scanning alerts on GitHub through the alert pages or by including your alerts in a security campaign. Alternatively, you can generate autofix suggestions using the REST API. Then assign Copilot to kick off remediation through one of the following assignment methods.

### Bulk assignment
- Go to a security campaign in your repository, select one or more alerts, and click Assign Copilot to fix several alerts in one pull request.

### Individual assignment
- Assign specific alerts from the alert detail page for targeted fixes.
- Once assigned, Copilot analyzes the vulnerability, creates a remediation plan, and opens a draft pull request. When the code changes are complete, the pull request is ready for review. Links in the GitHub UI help you easily track the progress of each pull request.
- This feature is now available for customers using GitHub Code Security or GitHub Advanced Security and Copilot coding agent on GitHub Enterprise Cloud.
- Learn more about GitHub code scanning and security campaigns or get started with Copilot coding agent .

## Impact / Who’s Affected
- This feature is now available for customers using GitHub Code Security or GitHub Advanced Security and Copilot coding agent on GitHub Enterprise Cloud.

## Insights (derived from article language)
- Learn more about GitHub code scanning and security campaigns or get started with Copilot coding agent .

## Article Content (cleaned)
You can now assign GitHub code scanning alerts directly to Copilot to assist with automated remediation. This extends Copilot coding agent capabilities to security vulnerabilities, enabling faster resolution of common issues.


Copilot coding agent works alongside Copilot Autofix to reduce the time developers spend planning and implementing security fixes. First, generate an autofix suggestion for your code scanning alerts on GitHub through the alert pages or by including your alerts in a security campaign. Alternatively, you can generate autofix suggestions using the REST API. Then assign Copilot to kick off remediation through one of the following assignment methods.


### [Bulk assignment](#bulk-assignment)


Go to a security campaign in your repository, select one or more alerts, and click **Assign Copilot** to fix several alerts in one pull request.


![In a security campaign, multiple alerts that have autofix suggestions are selected and the Assign to Copilot button is visible.](https://github.com/user-attachments/assets/f7abb217-b134-4f5e-b6d4-6cec4acefa5d)


### [Individual assignment](#individual-assignment)


Assign specific alerts from the alert detail page for targeted fixes.


![For individual code scanning alerts that have autofix suggestions, Copilot is assigned using the assignee picker on the right-hand side.](https://github.com/user-attachments/assets/ca39933d-7cf5-4248-b06d-94a1cf621734)


Once assigned, Copilot analyzes the vulnerability, creates a remediation plan, and opens a draft pull request. When the code changes are complete, the pull request is ready for review. Links in the GitHub UI help you easily track the progress of each pull request.


This feature is now available for customers using GitHub Code Security or GitHub Advanced Security and Copilot coding agent on GitHub Enterprise Cloud.


Learn more about [GitHub code scanning](https://docs.github.com/code-security/code-scanning?utm_source=changelog-docs-assign-alerts-to-copilot&utm_medium=changelog&utm_campaign=universe25) and [security campaigns](https://docs.github.com/enterprise-cloud@latest/code-security/securing-your-organization/fixing-security-alerts-at-scale/about-security-campaigns?utm_source=changelog-docs-assign-alerts-to-copilot&utm_medium=changelog&utm_campaign=universe25) or [get started with Copilot coding agent](https://github.com/features/copilot?utm_source=changelog-copilot-assign-alerts-to-copilot&utm_medium=changelog&utm_campaign=universe25).
