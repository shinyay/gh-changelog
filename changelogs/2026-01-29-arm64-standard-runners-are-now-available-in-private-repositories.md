---
title: "arm64 standard runners are now available in private repositories"
date: "2026-01-29"
type: "Improvement"
labels: ["actions"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-29-arm64-standard-runners-are-now-available-in-private-repositories"
fetched_at: "2026-02-03T14:50:49.323999Z"
---

# arm64 standard runners are now available in private repositories

## Overview
Linux and Windows arm64 standard GitHub-hosted runners are now supported in private repositories. You can now use these free-tier eligible arm64 runners in all repositories, letting you take advantage of the performance benefits of arm64 processors and run native multi-architecture builds without the overhead of virtualization or emulation.

## Detailed Explanation
### Overview
- Linux and Windows arm64 standard GitHub-hosted runners are now supported in private repositories. You can now use these free-tier eligible arm64 runners in all repositories, letting you take advantage of the performance benefits of arm64 processors and run native multi-architecture builds without the overhead of virtualization or emulation.
- Because these are standard GitHub-hosted runners, usage counts towards the free minutes included in your plan .

### What’s new
- Linux and Windows arm64 standard hosted runners are now supported in all repositories.
- In private repositories, these runners have two vCPUs; in public repositories, they have four vCPUs.
- These runners use an arm64 processor and images managed by Arm, LLC.
- As standard GitHub-hosted runners, they are eligible for use towards your GitHub plan’s free minute allocation in private repositories. macOS arm64 standard runners are already available for private repositories. This update extends private repository arm64 support to Linux and Windows.
- This is ideal for teams targeting arm64 production, such as containerized services or multi-architecture builds, who want native performance using standard GitHub-hosted runners in private repositories.

### Get started
- To start building on arm64, add one of the following supported labels to the runs-on field in your workflow:
- windows-11-arm
- ubuntu-24.04-arm
- ubuntu-22.04-arm
- For more details on arm64 runners and usage, see our documentation for standard GitHub-hosted runners .
- These runners are fully supported standard GitHub-hosted runners and are suitable for production CI workloads.
- Join the discussion within GitHub Community .

## Impact / Who’s Affected
- Linux and Windows arm64 standard GitHub-hosted runners are now supported in private repositories.
- What’s new Linux and Windows arm64 standard hosted runners are now supported in all repositories.

## Insights (derived from article language)
- Get started To start building on arm64, add one of the following supported labels to the runs-on field in your workflow: windows-11-arm ubuntu-24.04-arm ubuntu-22.04-arm For more details on arm64 runners and usage, see our documentation for standard GitHub-hosted runners .

## Article Content (cleaned)
Linux and Windows arm64 standard GitHub\-hosted runners are now supported in private repositories. You can now use these free\-tier eligible arm64 runners in all repositories, letting you take advantage of the performance benefits of arm64 processors and run native multi\-architecture builds without the overhead of virtualization or emulation.


Because these are standard GitHub\-hosted runners, usage counts towards the [free minutes included in your plan](https://docs.github.com/billing/concepts/product-billing/github-actions#free-use-of-github-actions).


## [What’s new](https://github.blog/changelog/feed/#whats-new)


* Linux and Windows arm64 standard hosted runners are now supported in all repositories.
* In private repositories, these runners have two vCPUs; in public repositories, they have four vCPUs.
* These runners use an arm64 processor and images managed by Arm, LLC.


As standard GitHub\-hosted runners, they are eligible for use towards your GitHub plan’s free minute allocation in private repositories. macOS arm64 standard runners are already available for private repositories. This update extends private repository arm64 support to Linux and Windows.


This is ideal for teams targeting arm64 production, such as containerized services or multi\-architecture builds, who want native performance using standard GitHub\-hosted runners in private repositories.


## [Get started](https://github.blog/changelog/feed/#get-started)


To start building on arm64, add one of the following supported labels to the runs\-on field in your workflow:


* `windows-11-arm`
* `ubuntu-24.04-arm`
* `ubuntu-22.04-arm`


For more details on arm64 runners and usage, see [our documentation for standard GitHub\-hosted runners](https://docs.github.com/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for--private-repositories).


These runners are fully supported standard GitHub\-hosted runners and are suitable for production CI workloads.


Join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/185840).
