---
title: "GitHub Copilot policy update for unconfigured policies"
date: "2025-11-04"
type: "improvements"
labels: ["copilot", "enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-04-github-copilot-policy-update-for-unconfigured-policies"
fetched_at: "2026-02-03T14:40:06.366502Z"
---

# GitHub Copilot policy update for unconfigured policies

## Overview
We have fixed an issue that occasionally caused Copilot policies for an organization to show the wrong options when the enterprise policy was set to Unconfigured .

## Detailed Explanation
### Overview
- We have fixed an issue that occasionally caused Copilot policies for an organization to show the wrong options when the enterprise policy was set to Unconfigured .

### What’s changed
- The Copilot policies updates restore the intended flow of policy delegation between enterprises and organizations. Now, if an enterprise policy is set to Unconfigured , the corresponding organization policy will default to Disabled instead of allowing organizations to set it to Enabled .
- This ensures that policies remain restricted unless the enterprise admin explicitly enables or delegates the policy.
- To prevent an undesired disruption in service, formerly affected organization policies which are currently set to Enabled are not changed by this update. However, once an admin sets a policy to Disabled , it cannot be changed at the organization level again unless the enterprise policy is updated to permit it. Organization policies for future releases will automatically inherit the correct Disabled setting when the enterprise policy is Unconfigured .

### Learn more
- For more information visit our documentation about managing Copilot policies .

## Insights (derived from article language)
- Learn more For more information visit our documentation about managing Copilot policies .

## Article Content (cleaned)
We have fixed an issue that occasionally caused Copilot policies for an organization to show the wrong options when the enterprise policy was set to `Unconfigured`.


## [What’s changed](#whats-changed)


The Copilot policies updates restore the intended flow of policy delegation between enterprises and organizations. Now, if an enterprise policy is set to `Unconfigured`, the corresponding organization policy will default to `Disabled` instead of allowing organizations to set it to `Enabled`.


This ensures that policies remain restricted unless the enterprise admin explicitly enables or delegates the policy.


To prevent an undesired disruption in service, formerly affected organization policies which are currently set to `Enabled` are not changed by this update. However, once an admin sets a policy to `Disabled`, it cannot be changed at the organization level again unless the enterprise policy is updated to permit it. Organization policies for future releases will automatically inherit the correct `Disabled` setting when the enterprise policy is `Unconfigured`.


## [Learn more](#learn-more)


For more information visit [our documentation about managing Copilot policies](https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies).
