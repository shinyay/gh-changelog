---
title: "Secret scanning alert assignees, security campaigns are generally available"
date: "2025-11-25"
type: "new releases"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-25-secret-scanning-alert-assignees-security-campaigns-are-generally-available"
fetched_at: "2026-02-03T14:50:55.138466Z"
---

# Secret scanning alert assignees, security campaigns are generally available

## Overview
To help you track and remediate secret scanning alerts more effectively, secret scanning alert assignees and security campaigns are now generally available.

## Detailed Explanation
### Overview
- To help you track and remediate secret scanning alerts more effectively, secret scanning alert assignees and security campaigns are now generally available.

### What’s new?
- Notifications: Alert assignees receive email notifications if subscribed to participating and @mentions from their repository watching settings. Previously, assignees only received email notifications when subscribed to All events or Security Alert events .
- Campaign list views: Alerts in campaign list views now support the same filters and bulk actions as existing alert lists. You can now also view repository-level campaign list views, which are visible to anyone with permissions to view the repository-level alert list.
- REST API and webhooks: REST API support is now available for viewing and updating secret scanning security campaigns, along with REST API support for viewing, assigning, and unassigning users to a secret scanning alert. Webhooks  for alert assignees are also available and are similar to webhooks for pull request and issue assignment.

### What are security campaigns?
- Secret scanning security campaigns allow you to target specific alerts in your organization, set remediation deadlines, and notify admins and security managers about the campaign. Secret scanning campaigns can be created and published from the security overview dashboard.

### What are alert assignees?
- Alert assignees make it easier to track and drive remediation efforts for your alerts. You can assign the alert to anyone with write access to the repository. If that user didn’t have access to view the alert at the time they were assigned, they’ll receive permissions to view and edit the alert. If they received permissions by being assigned to the alert, they’ll lose permissions if they are unassigned. Secret scanning alert assignees will be available for GitHub Enterprise Server customers starting with version 3.20.
- Learn more about security campaigns and alert assignment for secret scanning alerts.

## Impact / Who’s Affected
- To help you track and remediate secret scanning alerts more effectively, secret scanning alert assignees and security campaigns are now generally available.
- Previously, assignees only received email notifications when subscribed to All events or Security Alert events .
- REST API and webhooks: REST API support is now available for viewing and updating secret scanning security campaigns, along with REST API support for viewing, assigning, and unassigning users to a secret scanning alert.

## Caveats / Limitations
- Previously, assignees only received email notifications when subscribed to All events or Security Alert events .

## Insights (derived from article language)
- Learn more about security campaigns and alert assignment for secret scanning alerts.

## Article Content (cleaned)
To help you track and remediate secret scanning alerts more effectively, secret scanning alert assignees and security campaigns are now generally available.


### [What’s new?](#whats-new)


* **Notifications:** Alert assignees receive email notifications if subscribed to `participating and @mentions` from their repository watching settings. Previously, assignees only received email notifications when subscribed to `All events` or `Security Alert events`.
* **Campaign list views:** Alerts in campaign list views now support the same filters and bulk actions as existing alert lists. You can now also view repository\-level campaign list views, which are visible to anyone with permissions to view the repository\-level alert list.
* **REST API and webhooks:** REST API support is now available for viewing and updating secret scanning security campaigns, along with REST API support for viewing, assigning, and unassigning users to a secret scanning alert. Webhooks for alert assignees are also available and are similar to webhooks for pull request and issue assignment.


### [What are security campaigns?](#what-are-security-campaigns)


Secret scanning security campaigns allow you to target specific alerts in your organization, set remediation deadlines, and notify admins and security managers about the campaign. Secret scanning campaigns can be created and published from the security overview dashboard.


### [What are alert assignees?](#what-are-alert-assignees)


Alert assignees make it easier to track and drive remediation efforts for your alerts. You can assign the alert to anyone with `write` access to the repository. If that user didn’t have access to view the alert at the time they were assigned, they’ll receive permissions to view and edit the alert. If they received permissions by being assigned to the alert, they’ll lose permissions if they are unassigned. Secret scanning alert assignees will be available for GitHub Enterprise Server customers starting with version 3\.20\.


Learn more about [security campaigns](https://docs.github.com/enterprise-cloud@latest/code-security/securing-your-organization/fixing-security-alerts-at-scale/creating-managing-security-campaigns) and [alert assignment](https://docs.github.com/code-security/secret-scanning/managing-alerts-from-secret-scanning/viewing-alerts#filtering-alerts) for secret scanning alerts.
