---
title: "Better diagnostics for VNET injected runners and required self-hosted runner upgrades"
date: "2025-12-12"
type: "improvements"
labels: ["actions"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-12-better-diagnostics-for-vnet-injected-runners-and-required-self-hosted-runner-upgrades"
fetched_at: "2026-02-03T14:50:54.954892Z"
---

# Better diagnostics for VNET injected runners and required self-hosted runner upgrades

## Overview
Editor’s note (December 19, 2025): We updated this post to indicate new dates for when self-hosted runners need to be updated to v2.329.0 or later. The original upgrade date has been pushed back to March, 2026, and we added a brown out period starting in February, 2026.

## Detailed Explanation
### Overview
- Editor’s note (December 19, 2025): We updated this post to indicate new dates for when self-hosted runners need to be updated to v2.329.0 or later. The original upgrade date has been pushed back to March, 2026, and we added a brown out period starting in February, 2026.
- GitHub-hosted larger runners with Azure private networking (Azure VNET-injection) now display detailed network diagnostics when connectivity issues occur.
- Instead of generic pool errors, you’ll see:
- Per-endpoint visibility : Drill down into each required endpoint to see exactly where connections are failing.
- Connection metrics : View attempt counts, failure rates, and success percentages for comprehensive health insights.
- Failure classification : Identify specific issues such as connection timeouts, proxy misconfigurations, DNS resolution failures, TLS interception problems, and blocked domains.
- This enables you to quickly diagnose and resolve network configuration problems without contacting support.

### Required upgrade for self-hosted runners
- GitHub Actions is undergoing a rearchitecture to deliver improved reliability, scalability, and new features for CI/CD and developer automation. As part of this effort, older versions of the actions runner will no longer be supported.
- What’s changing
- GitHub will require self hosted runners to use v2.329.0 or later during configuration. Runners using legacy versions will be blocked from connecting to GitHub Actions. This change ensures compatibility with the new architecture and prevents workflow failures during future rollouts.
- Previously, outdated runners could self-upgrade after configuration. Going forward, runners must meet the minimum version requirement before they can register.
- We will start brown outs on 02/09/2026 and the full enforcement will start on 03/02/2026.
- Action required
- Upgrade your self-hosted runners to v2.329.0 or later as soon as possible. For guidance, see the self-hosted runner documentation .

### Actions runner Docker image updated to Ubuntu 24.04
- The Actions runner Docker image will be updated from Ubuntu 22.04 to Ubuntu 24.04 in the upcoming v2.331.0 release, targeted for January 2026. This update provides access to newer system libraries, security patches, and improved compatibility with modern tooling. If you use custom Docker images based on the actions runner, review your dependencies to ensure compatibility with Ubuntu 24.04. See pull request #4018 for details.

## Caveats / Limitations
- Editor’s note (December 19, 2025): We updated this post to indicate new dates for when self-hosted runners need to be updated to v2.329.0 or later.

## Article Content (cleaned)
*Editor’s note (December 19, 2025\): We updated this post to indicate new dates for when self\-hosted runners need to be updated to v2\.329\.0 or later. The original upgrade date has been pushed back to March, 2026, and we added a brown out period starting in February, 2026\.*


GitHub\-hosted larger runners with Azure private networking (Azure VNET\-injection) now display detailed network diagnostics when connectivity issues occur.


Instead of generic pool errors, you’ll see:


* **Per\-endpoint visibility**: Drill down into each required endpoint to see exactly where connections are failing.
* **Connection metrics**: View attempt counts, failure rates, and success percentages for comprehensive health insights.
* **Failure classification**: Identify specific issues such as connection timeouts, proxy misconfigurations, DNS resolution failures, TLS interception problems, and blocked domains.


This enables you to quickly diagnose and resolve network configuration problems without contacting support.


### [Required upgrade for self\-hosted runners](#required-upgrade-for-self-hosted-runners)


GitHub Actions is undergoing a rearchitecture to deliver improved reliability, scalability, and new features for CI/CD and developer automation. As part of this effort, older versions of the actions runner will no longer be supported.


**What’s changing**


GitHub will require self hosted runners to use v2\.329\.0 or later during configuration. Runners using legacy versions will be blocked from connecting to GitHub Actions. This change ensures compatibility with the new architecture and prevents workflow failures during future rollouts.


Previously, outdated runners could self\-upgrade after configuration. Going forward, runners must meet the minimum version requirement before they can register.


We will start brown outs on 02/09/2026 and the full enforcement will start on 03/02/2026\.


**Action required**


Upgrade your self\-hosted runners to v2\.329\.0 or later as soon as possible. For guidance, see the [self\-hosted runner documentation](https://docs.github.com/actions/reference/runners/self-hosted-runners#runner-software-updates-on-self-hosted-runners).


### [Actions runner Docker image updated to Ubuntu 24\.04](#actions-runner-docker-image-updated-to-ubuntu-24-04)


The Actions runner Docker image will be updated from Ubuntu 22\.04 to Ubuntu 24\.04 in the upcoming v2\.331\.0 release, targeted for January 2026\. This update provides access to newer system libraries, security patches, and improved compatibility with modern tooling. If you use custom Docker images based on the actions runner, review your dependencies to ensure compatibility with Ubuntu 24\.04\. See [pull request \#4018](https://github.com/actions/runner/pull/4018) for details.
