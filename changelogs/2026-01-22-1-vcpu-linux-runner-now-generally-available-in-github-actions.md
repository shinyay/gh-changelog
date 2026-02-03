---
title: "1 vCPU Linux runner now generally available in GitHub Actions"
date: "2026-01-22"
type: "new releases"
labels: ["actions"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-22-1-vcpu-linux-runner-now-generally-available-in-github-actions"
fetched_at: "2026-02-03T14:50:54.721404Z"
---

# 1 vCPU Linux runner now generally available in GitHub Actions

## Overview
GitHub Actions 1 vCPU Linux runners are now generally available. All customers can now take advantage of these lower cost runners. These runners are optimized for automation tasks, issue operations, and short running jobs outside of typical heavyweight CI/CD builds.

## Detailed Explanation
### Overview
- GitHub Actions 1 vCPU Linux runners are now generally available. All customers can now take advantage of these lower cost runners. These runners are optimized for automation tasks, issue operations, and short running jobs outside of typical heavyweight CI/CD builds.

### Runner details
- These runners have one vCPU and 5 GBs RAM. When using these runners, your actions workflows execute inside of a container rather than a dedicated VM instance, enabling cost-effective, performant execution of automation tasks across GitHub. Each container provides hypervisor level 2 isolation, and the container is automatically decommissioned when a job is completed.
- Jobs that use this runner type are limited to 15 minutes of execution time. Jobs exceeding this limit will be terminated and fail.
- Good use cases for these runners include jobs like:
- Auto-labeling issues
- Basic language compilation (e.g., webpack builds)
- Linting and formatting
- Making API calls to external tools
- Running simple python scripts

### Get started today
- To get started, simply target the new runner type ubuntu-slim in any new or existing job definitions.

### Helpful resources
- To view the full list of installed software or report issues when using 1 vCPU Linux runners, visit the runner-images repository .
- For pricing information on these lightweight runners see the billing for GitHub Actions page.
- For additional documentation, see the GitHub Docs reference for single-CPU runners .

## Impact / Who’s Affected
- GitHub Actions 1 vCPU Linux runners are now generally available.
- Jobs that use this runner type are limited to 15 minutes of execution time.

## Caveats / Limitations
- Jobs that use this runner type are limited to 15 minutes of execution time.

## Article Content (cleaned)
GitHub Actions 1 vCPU Linux runners are now generally available. All customers can now take advantage of these lower cost runners. These runners are optimized for automation tasks, issue operations, and short running jobs outside of typical heavyweight CI/CD builds.


## [Runner details](#runner-details)


These runners have one vCPU and 5 GBs RAM. When using these runners, your actions workflows execute inside of a container rather than a dedicated VM instance, enabling cost\-effective, performant execution of automation tasks across GitHub. Each container provides hypervisor level 2 isolation, and the container is automatically decommissioned when a job is completed.


Jobs that use this runner type are limited to 15 minutes of execution time. Jobs exceeding this limit will be terminated and fail.


Good use cases for these runners include jobs like:


* Auto\-labeling issues
* Basic language compilation (e.g., webpack builds)
* Linting and formatting
* Making API calls to external tools
* Running simple python scripts


## [Get started today](#get-started-today)


To get started, simply target the new runner type `ubuntu-slim` in any new or existing job definitions.


## [Helpful resources](#helpful-resources)


To view the full list of installed software or report issues when using 1 vCPU Linux runners, visit the [runner\-images repository](https://github.com/actions/runner-images/blob/main/images/ubuntu-slim/ubuntu-slim-Readme.md).


For pricing information on these lightweight runners see the [billing for GitHub Actions](https://docs.github.com/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions) page.


For additional documentation, see the [GitHub Docs reference for single\-CPU runners](https://docs.github.com/actions/reference/runners/github-hosted-runners#single-cpu-runners).
