---
title: "GitHub Actions cache size can now exceed 10 GB per repository"
date: "2025-11-20"
type: "improvements"
labels: ["actions"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-20-github-actions-cache-size-can-now-exceed-10-gb-per-repository"
fetched_at: "2026-02-03T14:40:05.908431Z"
---

# GitHub Actions cache size can now exceed 10 GB per repository

## Overview
You can now store more build dependencies between workflow runs with expanded GitHub Actions cache storage. Repositories can go beyond the previous 10 GB per-repository cache cap using a pay-as-you-go model. All repositories will continue to receive access to 10 GB, which is provided at no additional cost. Enterprise, Organization, and Repository admins can increase these limits. When you increase these limits, your cache can exceed 10 GB per repo, and you’ll automatically be charged based on the storage used. This storage cost is comparable to storage for Git LFS and Codespaces storage—and going beyond the 10 GB per repo limit requires a valid Pro, Team, or Enterprise account.

## Detailed Explanation
### GitHub Actions cache size can now exceed 10 GB per repository
- You can now store more build dependencies between workflow runs with expanded GitHub Actions cache storage. Repositories can go beyond the previous 10 GB per-repository cache cap using a pay-as-you-go model. All repositories will continue to receive access to 10 GB, which is provided at no additional cost. Enterprise, Organization, and Repository admins can increase these limits. When you increase these limits, your cache can exceed 10 GB per repo, and you’ll automatically be charged based on the storage used. This storage cost is comparable to storage for Git LFS and Codespaces storage—and going beyond the 10 GB per repo limit requires a valid Pro, Team, or Enterprise account.

### Managing cache and billing policies
- We are introducing two cache management policies: cache size eviction limit (GB) and cache retention limit (days). Use the retention limit to set how long your cache entries are kept after last access, and the size eviction limit to set the maximum total cache size for each repository. By default, you receive a 10 GB cache size limit and a seven-day retention limit at no additional cost. If you increase the cache size limit beyond your plan’s defaults, you will be charged for extra cached storage. When a repo’s cache exceeds its limit, the least recently used cache entries are automatically evicted to stay within the configured size. If you keep the defaults, nothing will change.
- Enterprise, Organization, and Repository admins can manage cache policies to control how much cache is used. These policies can be managed via the Actions settings (for Repositories and Organizations) or via Policies (for Enterprises), and the policies cascade down (e.g. if the max for an enterprise is 15 GB per repo and 14 days, the max for every organization in that enterprise is 15 GB per repo and 14 days).
- In addition, billing owners can set budgets based on this new SKU. In the event a budget has been reached, cache will become read-only for all repositories making use of higher limits until the next billing cycle.
- Learn more about managing cache storage in the GitHub Actions documentation .

## Impact / Who’s Affected
- This storage cost is comparable to storage for Git LFS and Codespaces storage—and going beyond the 10 GB per repo limit requires a valid Pro, Team, or Enterprise account.
- In the event a budget has been reached, cache will become read-only for all repositories making use of higher limits until the next billing cycle.

## Caveats / Limitations
- This storage cost is comparable to storage for Git LFS and Codespaces storage—and going beyond the 10 GB per repo limit requires a valid Pro, Team, or Enterprise account.
- In the event a budget has been reached, cache will become read-only for all repositories making use of higher limits until the next billing cycle.

## Insights (derived from article language)
- This storage cost is comparable to storage for Git LFS and Codespaces storage—and going beyond the 10 GB per repo limit requires a valid Pro, Team, or Enterprise account.
- Learn more about managing cache storage in the GitHub Actions documentation .

## Article Content (cleaned)
### [GitHub Actions cache size can now exceed 10 GB per repository](#github-actions-cache-size-can-now-exceed-10-gb-per-repository)


You can now store more build dependencies between workflow runs with expanded GitHub Actions cache storage. Repositories can go beyond the previous 10 GB per\-repository cache cap using a pay\-as\-you\-go model. All repositories will continue to receive access to 10 GB, which is provided at no additional cost. Enterprise, Organization, and Repository admins can increase these limits. When you increase these limits, your cache can exceed 10 GB per repo, and you’ll automatically be charged based on the storage used. This storage cost is comparable to storage for Git LFS and Codespaces storage—and going beyond the 10 GB per repo limit requires a valid Pro, Team, or Enterprise account.


### [Managing cache and billing policies](#managing-cache-and-billing-policies)


We are introducing two cache management policies: cache size eviction limit (GB) and cache retention limit (days). Use the retention limit to set how long your cache entries are kept after last access, and the size eviction limit to set the maximum total cache size for each repository. By default, you receive a 10 GB cache size limit and a seven\-day retention limit at no additional cost. If you increase the cache size limit beyond your plan’s defaults, you will be charged for extra cached storage. When a repo’s cache exceeds its limit, the least recently used cache entries are automatically evicted to stay within the configured size. If you keep the defaults, nothing will change.


Enterprise, Organization, and Repository admins can manage cache policies to control how much cache is used. These policies can be managed via the Actions settings (for Repositories and Organizations) or via Policies (for Enterprises), and the policies cascade down (e.g. if the max for an enterprise is 15 GB per repo and 14 days, the max for every organization in that enterprise is 15 GB per repo and 14 days).


In addition, billing owners can set budgets based on this new SKU. In the event a budget has been reached, cache will become read\-only for all repositories making use of higher limits until the next billing cycle.


Learn more about managing cache storage in [the GitHub Actions documentation](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows).
