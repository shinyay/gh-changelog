---
title: "Enterprise governance and policy improvements for secret scanning"
date: "2025-12-16"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-16-enterprise-governance-and-policy-improvements-for-secret-scanning-now-generally-available"
fetched_at: "2026-02-03T14:40:05.460001Z"
---

# Enterprise governance and policy improvements for secret scanning

## Overview
At GitHub, we care deeply about ensuring enterprise-readiness of our products. From recent improvements including enterprise-level delegated bypass controls for push protection , to support for the new Enterprise Security Manager role , secret scanning is no exception.

## Detailed Explanation
### Overview
- At GitHub, we care deeply about ensuring enterprise-readiness of our products. From recent improvements including enterprise-level delegated bypass controls for push protection , to support for the new Enterprise Security Manager role , secret scanning is no exception.
- Today, we’re announcing additional recent improvements to alert-level and enterprise-level permissions for secret scanning. With these improvements, we’re unlocking more ways to scale governance and policy across GitHub, enhancing the ability for enterprises to more easily manage secret scanning alerts, custom patterns, and push protection bypasses.

### Permissions for secret scanning alert assignees
- We’ve expanded permissions for secret scanning alert assignees, in order to make alerts more actionable.
- Assignment for anyone with alert write permissions: Added the ability to modify assignees for anyone with the ability to modify/resolve secret scanning alerts. Anyone with the ability to dismiss or reopen a secret scanning alert should be able to add or remove the alert assignment.
- Assignees and alert write permissions: Added the ability for alert assignees to modify alerts, including resolving the alert and removing themselves as an assignee.

### Enterprise owners and enterprise security managers with custom patterns
- We’ve made custom pattern management at the enterprise level more permissive; previously, only the pattern creator could edit them.
- Custom pattern management: Enterprise owners and enterprise security managers can now edit any custom patterns, regardless of whether or not they created them. This solves a common pain point with orphaned custom patterns at the enterprise level.

### Enterprise teams, roles, and apps with push protection bypasses
- We have expanded support for Enterprise teams, organization roles, and GitHub Apps to provide more flexible and secure policy management.
- Delegated push protection bypasses: To better manage push protection bypasses at scale, you can now also delegate push protection bypass permissions to Enterprise Teams, roles, and apps. This streamlines the process for handling bypass requests across the enterprise.
- Removed 1 actor requirement for bypass lists: Later this month, we’re removing the need to add at least 1 actor to the “push protection bypass list” in security configurations. With this change, customers can use custom roles with the push protection bypass fine-grained permission without needing to provide access to a team or default role.
- Removed 1 actor requirement for bypass lists: Later this month, we’re removing the need to add at least 1 actor to the “push protection bypass list” in security configurations. With this change, customers can use custom roles with the push protection bypass fine-grained permission without needing to provide access to a team or default role.
- Learn more about delegated bypasses for push protection , custom patterns , and getting started with secret scanning .

## Impact / Who’s Affected
- Enterprise owners and enterprise security managers with custom patterns We’ve made custom pattern management at the enterprise level more permissive; previously, only the pattern creator could edit them.

## Caveats / Limitations
- From recent improvements including enterprise-level delegated bypass controls for push protection , to support for the new Enterprise Security Manager role , secret scanning is no exception.
- Enterprise owners and enterprise security managers with custom patterns We’ve made custom pattern management at the enterprise level more permissive; previously, only the pattern creator could edit them.

## Insights (derived from article language)
- Learn more about delegated bypasses for push protection , custom patterns , and getting started with secret scanning .

## Article Content (cleaned)
At GitHub, we care deeply about ensuring enterprise\-readiness of our products. From recent improvements including enterprise\-level [delegated bypass controls for push protection](https://github.blog/changelog/2025-09-16-delegated-bypass-controls-for-push-protection-now-available-at-the-enterprise-level/), to support for the new [Enterprise Security Manager role](https://github.blog/changelog/2025-10-23-managing-roles-and-governance-via-enterprise-teams-is-in-public-preview), secret scanning is no exception.


Today, we’re announcing additional recent improvements to alert\-level and enterprise\-level permissions for secret scanning. With these improvements, we’re unlocking more ways to scale governance and policy across GitHub, enhancing the ability for enterprises to more easily manage secret scanning alerts, custom patterns, and push protection bypasses.


### [Permissions for secret scanning alert assignees](#permissions-for-secret-scanning-alert-assignees)


We’ve expanded permissions for secret scanning alert assignees, in order to make alerts more actionable.


* **Assignment for anyone with alert `write` permissions:** Added the ability to modify assignees for anyone with the ability to modify/resolve secret scanning alerts. Anyone with the ability to dismiss or reopen a secret scanning alert should be able to add or remove the alert assignment.
* **Assignees and alert `write` permissions:** Added the ability for alert assignees to modify alerts, including resolving the alert and removing themselves as an assignee.


### [Enterprise owners and enterprise security managers with custom patterns](#enterprise-owners-and-enterprise-security-managers-with-custom-patterns)


We’ve made custom pattern management at the enterprise level more permissive; previously, only the pattern creator could edit them.


* **Custom pattern management:** Enterprise owners and enterprise security managers can now edit any custom patterns, regardless of whether or not they created them. This solves a common pain point with orphaned custom patterns at the enterprise level.


### [Enterprise teams, roles, and apps with push protection bypasses](#enterprise-teams-roles-and-apps-with-push-protection-bypasses)


We have expanded support for Enterprise teams, organization roles, and GitHub Apps to provide more flexible and secure policy management.


* **Delegated push protection bypasses:** To better manage push protection bypasses at scale, you can now also delegate push protection bypass permissions to Enterprise Teams, roles, and apps. This streamlines the process for handling bypass requests across the enterprise.
* **Removed 1 actor requirement for bypass lists:** Later this month, we’re removing the need to add at least 1 actor to the “push protection bypass list” in security configurations. With this change, customers can use custom roles with the push protection bypass fine\-grained permission without needing to provide access to a team or default role.


Learn more about [delegated bypasses for push protection](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection), [custom patterns](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning), and getting started with [secret scanning](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/introduction/about-secret-scanning).
