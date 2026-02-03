---
title: "1 vCPU Linux runner now available in GitHub Actions in public preview"
date: "2025-10-28"
type: "new releases"
labels: ["actions", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-1-vcpu-linux-runner-now-available-in-github-actions-in-public-preview"
fetched_at: "2026-02-03T14:40:06.722149Z"
---

# 1 vCPU Linux runner now available in GitHub Actions in public preview

## Overview
GitHub Actions 1 vCPU Linux runners are now in public preview. Customers looking to run lightweight operations can take advantage of these lower cost runners. These runners are optimized for automation tasks, issue operations, and short running jobs outside of typical heavyweight CI/CD builds.

## Detailed Explanation
### Overview
- GitHub Actions 1 vCPU Linux runners are now in public preview. Customers looking to run lightweight operations can take advantage of these lower cost runners. These runners are optimized for automation tasks, issue operations, and short running jobs outside of typical heavyweight CI/CD builds.

### Runner details
- These runners have one vCPU and 5 GBs RAM. When using these runners, your actions workflows execute inside of a container rather than a dedicated VM instance, enabling cost-effective, performant execution of automation tasks across GitHub. Each container provides hypervisor level 2 isolation, and the container is automatically decomissioned when a job is completed.
- Jobs that use this runner type are limited to 15 minutes of execution time. Jobs exceeding this limit will be terminated and fail.
- Good use cases for these runners include jobs like:
- Auto-labelling issues
- Basic language compilation (e.g., webpack builds)
- Linting and formatting

### Get started today
- To get started, simply target the new runner type ubuntu-slim in any new or existing job definitions.
- For pricing information on these larger runners see the billing for GitHub Actions page.
- Join the discussion within GitHub Community .

## Impact / Who’s Affected
- GitHub Actions 1 vCPU Linux runners are now in public preview.
- Jobs that use this runner type are limited to 15 minutes of execution time.

## Caveats / Limitations
- Jobs that use this runner type are limited to 15 minutes of execution time.

## Article Content (cleaned)
GitHub Actions 1 vCPU Linux runners are now in public preview. Customers looking to run lightweight operations can take advantage of these lower cost runners. These runners are optimized for automation tasks, issue operations, and short running jobs outside of typical heavyweight CI/CD builds.


## [Runner details](#runner-details)


These runners have one vCPU and 5 GBs RAM. When using these runners, your actions workflows execute inside of a container rather than a dedicated VM instance, enabling cost\-effective, performant execution of automation tasks across GitHub. Each container provides hypervisor level 2 isolation, and the container is automatically decomissioned when a job is completed.


Jobs that use this runner type are limited to 15 minutes of execution time. Jobs exceeding this limit will be terminated and fail.


Good use cases for these runners include jobs like:


* Auto\-labelling issues
* Basic language compilation (e.g., webpack builds)
* Linting and formatting


## [Get started today](#get-started-today)


To get started, simply target the new runner type `ubuntu-slim` in any new or existing job definitions.


For pricing information on these larger runners see the [billing for GitHub Actions](https://docs.github.com/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions?utm_source=changelog-docs-1-vcpu-linux-runner&utm_medium=changelog&utm_campaign=universe25) page.


Join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/categories/announcements?utm_source=changelog-community-1-vcpu-linux-runner&utm_medium=changelog&utm_campaign=universe25).
