---
title: "Custom labels configuration option for Dependabot self-hosted and larger GitHub-hosted Actions runners now generally available at the organization level"
date: "2025-11-25"
type: "improvements"
labels: ["supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-25-custom-labels-configuration-option-for-dependabot-self-hosted-and-larger-github-hosted-actions-runners-now-generally-available-at-the-organization-level"
fetched_at: "2026-02-03T14:50:55.148651Z"
---

# Custom labels configuration option for Dependabot self-hosted and larger GitHub-hosted Actions runners now generally available at the organization level

## Overview
Dependabot update jobs can now target specific self-hosted and larger GitHub-hosted Actions runners using custom labels. Previously, Dependabot required the single dependabot label. This change gives you finer control, improves governance in environments restricted to one label (such as some Kubernetes-based runner controllers), and lets you segment workloads for security or performance, by defining custom labels for runners set at the Organization level.

## Detailed Explanation
### Overview
- Dependabot update jobs can now target specific self-hosted and larger GitHub-hosted Actions runners using custom labels. Previously, Dependabot required the single dependabot label. This change gives you finer control, improves governance in environments restricted to one label (such as some Kubernetes-based runner controllers), and lets you segment workloads for security or performance, by defining custom labels for runners set at the Organization level.
- What’s new: – Use any custom label (not just dependabot ) to route Dependabot jobs to matching self-hosted and larger GitHub-hosted runners – Optionally scope runners by runner group name for more granular control – Reduced operational friction in setups that previously had to dedicate a runner solely to the fixed dependabot label – Keep using the default dependabot label if you prefer; no change required if you don’t need custom targeting
- Existing workflows that rely on the dependabot label will continue to work without changes. If a specified label has no online runners, Dependabot queues the job until a matching runner becomes available . Ensure labels are spelled correctly to avoid configuration errors.
- Check out the docs to learn more about using custom labels with self-hosted runners and managing Dependabot on self-hosted runners .
- Join the discussion within GitHub Community .

## Insights (derived from article language)
- Check out the docs to learn more about using custom labels with self-hosted runners and managing Dependabot on self-hosted runners .

## Article Content (cleaned)
Dependabot update jobs can now target specific self\-hosted and larger GitHub\-hosted Actions runners using custom labels. Previously, Dependabot required the single `dependabot` label. This change gives you finer control, improves governance in environments restricted to one label (such as some Kubernetes\-based runner controllers), and lets you segment workloads for security or performance, by defining custom labels for runners set at the Organization level.


What’s new:  

– Use any custom label (not just `dependabot`) to route Dependabot jobs to matching self\-hosted and larger GitHub\-hosted runners  

– Optionally scope runners by runner group name for more granular control  

– Reduced operational friction in setups that previously had to dedicate a runner solely to the fixed `dependabot` label  

– Keep using the default `dependabot` label if you prefer; no change required if you don’t need custom targeting


Existing workflows that rely on the `dependabot` label will continue to work without changes. **If a specified label has no online runners, Dependabot queues the job until a matching runner becomes available**. Ensure labels are spelled correctly to avoid configuration errors.


Check out the docs to learn more about [using custom labels with self\-hosted runners](https://docs.github.com/actions/how-tos/manage-runners/self-hosted-runners/apply-labels) and [managing Dependabot on self\-hosted runners](https://docs.github.com/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners).


Join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/categories/announcements).
