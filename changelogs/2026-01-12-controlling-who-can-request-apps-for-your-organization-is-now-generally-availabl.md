---
title: "Controlling who can request apps for your organization is now generally available"
date: "2026-01-12"
type: "improvements"
labels: ["enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-12-controlling-who-can-request-apps-for-your-organization-is-now-generally-available"
fetched_at: "2026-02-03T14:50:54.819673Z"
---

# Controlling who can request apps for your organization is now generally available

## Overview
Organizations now have more granular control over who can request GitHub Apps and OAuth apps. This enhancement helps you implement stricter governance policies while maintaining flexibility for your security posture. This capability is now generally available.

## Detailed Explanation
### Overview
- Organizations now have more granular control over who can request GitHub Apps and OAuth apps. This enhancement helps you implement stricter governance policies while maintaining flexibility for your security posture. This capability is now generally available.

### What’s changed
- Previously, organizations could only disable app access requests from outside collaborators. Now, you can choose from three graduated control options:
- Members and outside collaborators : Members and outside collaborators can request apps. This is the existing default behavior.
- Members only : Block outside collaborators from requesting apps while permitting organization members to do so.
- Disable app access requests : Prevent both members and outside collaborators from requesting any apps.
- To configure this change, navigate to your organization’s settings, select Member Privileges , and choose your preferred option under “App access requests”. This graduated control mechanism ensures all third-party apps go through proper approval channels and security reviews before being considered for installation.
- To learn more, see “Limiting app requests” . This will be included in GHES 3.21.

### How to give feedback
- If you have any questions or feedback, drop a comment in our Community discussion .

## Impact / Who’s Affected
- This capability is now generally available.
- What’s changed Previously, organizations could only disable app access requests from outside collaborators.
- Members only : Block outside collaborators from requesting apps while permitting organization members to do so.

## Caveats / Limitations
- What’s changed Previously, organizations could only disable app access requests from outside collaborators.
- Members only : Block outside collaborators from requesting apps while permitting organization members to do so.

## Insights (derived from article language)
- This graduated control mechanism ensures all third-party apps go through proper approval channels and security reviews before being considered for installation.
- To learn more, see “Limiting app requests” .

## Article Content (cleaned)
Organizations now have more granular control over who can request GitHub Apps and OAuth apps. This enhancement helps you implement stricter governance policies while maintaining flexibility for your security posture. This capability is now generally available.


### [What’s changed](#whats-changed)


Previously, organizations could only disable app access requests from outside collaborators. Now, you can choose from three graduated control options:


* **Members and outside collaborators**: Members and outside collaborators can request apps. This is the existing default behavior.
* **Members only**: Block outside collaborators from requesting apps while permitting organization members to do so.
* **Disable app access requests**: Prevent both members and outside collaborators from requesting any apps.


![A radio button menu showing three options within an organization's settings page to choose who can request GitHub or OAuth apps](https://github.com/user-attachments/assets/154ca23d-f556-43f5-ba6d-9a4d2c2fcf28)


To configure this change, navigate to your organization’s settings, select **Member Privileges**, and choose your preferred option under “App access requests”. This graduated control mechanism ensures all third\-party apps go through proper approval channels and security reviews before being considered for installation.


To learn more, see [“Limiting app requests”](https://docs.github.com/organizations/managing-programmatic-access-to-your-organization/limiting-oauth-app-and-github-app-access-requests). This will be included in GHES 3\.21\.


### [How to give feedback](#how-to-give-feedback)


If you have any questions or feedback, drop a comment in our [Community discussion](https://github.com/orgs/community/discussions/183833).
