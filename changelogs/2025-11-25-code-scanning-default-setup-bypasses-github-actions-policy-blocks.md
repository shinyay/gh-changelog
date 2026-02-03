---
title: "Code scanning default setup bypasses GitHub Actions policy blocks"
date: "2025-11-25"
type: "improvements"
labels: ["actions", "application security", "platform governance"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-25-code-scanning-default-setup-bypasses-github-actions-policy-blocks"
fetched_at: "2026-02-03T14:50:55.143693Z"
---

# Code scanning default setup bypasses GitHub Actions policy blocks

## Overview
GitHub code scanning default setup now runs even if your organization has GitHub Actions policies that restrict which workflows can run. In the past, restrictive actions policies could block code scanning default setup from running and reduce your security coverage. With this update, you can limit which GitHub Actions workflows run (e.g., allowing only enterprise-approved workflows), but the code scanning default setup workflow will still run as long as GitHub Actions is enabled.

## Detailed Explanation
### Overview
- GitHub code scanning default setup now runs even if your organization has GitHub Actions policies that restrict which workflows can run. In the past, restrictive actions policies could block code scanning default setup from running and reduce your security coverage. With this update, you can limit which GitHub Actions workflows run (e.g., allowing only enterprise-approved workflows), but the code scanning default setup workflow will still run as long as GitHub Actions is enabled.
- The only actions policy that still affects this workflow is Disable actions . If GitHub Actions is disabled at the organization or repository level, code scanning default setup will not run.
- This change is now generally available for all GitHub plans and no action is required. It will be coming to Enterprise Server in 3.19.
- For more details, see the documentation for code scanning default setup .

## Impact / Who’s Affected
- With this update, you can limit which GitHub Actions workflows run (e.g., allowing only enterprise-approved workflows), but the code scanning default setup workflow will still run as long as GitHub Actions is enabled.
- The only actions policy that still affects this workflow is Disable actions .
- This change is now generally available for all GitHub plans and no action is required.

## Caveats / Limitations
- With this update, you can limit which GitHub Actions workflows run (e.g., allowing only enterprise-approved workflows), but the code scanning default setup workflow will still run as long as GitHub Actions is enabled.
- The only actions policy that still affects this workflow is Disable actions .

## Insights (derived from article language)
- For more details, see the documentation for code scanning default setup .

## Article Content (cleaned)
GitHub code scanning default setup now runs even if your organization has GitHub Actions policies that restrict which workflows can run. In the past, restrictive actions policies could block code scanning default setup from running and reduce your security coverage. With this update, you can limit which GitHub Actions workflows run (e.g., allowing only enterprise\-approved workflows), but the code scanning default setup workflow will still run as long as GitHub Actions is enabled.


The only actions policy that still affects this workflow is `Disable actions`. If GitHub Actions is disabled at the organization or repository level, code scanning default setup will not run.


This change is now generally available for all GitHub plans and no action is required. It will be coming to Enterprise Server in 3\.19\.


For more details, see [the documentation for code scanning default setup](https://docs.github.com/code-security/code-scanning/default-setup).
