---
title: "Required review by specific teams now available in rulesets"
date: "2025-11-04"
type: "improvements"
labels: ["collaboration tools", "platform governance"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-03-required-review-by-specific-teams-now-available-in-rulesets"
fetched_at: "2026-02-03T14:50:55.468584Z"
---

# Required review by specific teams now available in rulesets

## Overview
You can now require approvals from specific teams to merge changes into protected branches based on files and folders, giving you more control over who approves changes into specific branches.

## Detailed Explanation
### Overview
- You can now require approvals from specific teams to merge changes into protected branches based on files and folders, giving you more control over who approves changes into specific branches.

### What’s new
- With this new addition to rulesets , you can:
- Protect sensitive branches by enforcing stricter review policies for your release or production branches.
- Scale your policies across any repository, organization, or your entire enterprise for consistent enforcement.
- Target specific files and folders and require a specific number of reviews from specified teams.

### How this differs from CODEOWNERS
- While CODEOWNERS is great for defining ownership, this new ruleset focuses on policy enforcement. It makes it simple to require specific approvals on sensitive branches and critical code paths, all while scaling seamlessly across your enterprise.
- This new rule is designed to augment CODEOWNER files but not replace them. The CODEOWNERS files will continue to be the way to manage ownership, support individuals as reviewers, and request reviews even if not required.
- Learn more in our documentation about rulesets .
- Join the discussion and share your feedback within GitHub Community .

## Insights (derived from article language)
- Learn more in our documentation about rulesets .

## Article Content (cleaned)
You can now require approvals from specific teams to merge changes into protected branches based on files and folders, giving you more control over who approves changes into specific branches.


## [What’s new](#whats-new)


![Screenshot of the required reviewer rule dialog with the Bakers team selected as reviewer, two required approvals, and file patterns set to match GitHub workflow and YAML files](https://github.com/user-attachments/assets/039259c4-3aca-4850-9579-b57550f3c8b3)


With this new addition to [rulesets](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), you can:


* **Protect sensitive branches** by enforcing stricter review policies for your release or production branches.
* **Scale your policies** across any repository, organization, or your entire enterprise for consistent enforcement.
* **Target specific files and folders** and require a specific number of reviews from specified teams.


## [How this differs from CODEOWNERS](#how-this-differs-from-codeowners)


While CODEOWNERS is great for defining ownership, this new ruleset focuses on policy enforcement. It makes it simple to require specific approvals on sensitive branches and critical code paths, all while scaling seamlessly across your enterprise.


This new rule is designed to augment CODEOWNER files but not replace them. The CODEOWNERS files will continue to be the way to manage ownership, support individuals as reviewers, and request reviews even if not required.


Learn more in [our documentation about rulesets](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).


Join the discussion and share your feedback within [GitHub Community](https://gh.io/required-reviewer-feedback).
