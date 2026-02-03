---
title: "Notifications triggered by spam accounts are now correctly hidden"
date: "2025-12-04"
type: "improvements"
labels: ["collaboration tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-04-notifications-triggered-by-spam-accounts-are-now-correctly-hidden"
fetched_at: "2026-02-03T14:50:55.054636Z"
---

# Notifications triggered by spam accounts are now correctly hidden

## Overview
We’ve improved the way notifications from spammy repositories and users are handled, resulting in clearer, more accurate notification counts.

## Detailed Explanation
### Overview
- We’ve improved the way notifications from spammy repositories and users are handled, resulting in clearer, more accurate notification counts.

### Notifications triggered by spam accounts are now correctly hidden
- We’ve updated notification handling so that when a user or repository is flagged as spam, all notifications originating from their activity are reliably hidden, including past mentions from suspicious accounts. Previously, notifications triggered by spammy activity could remain visible and contribute to your unread repository counters, even after hiding or flagging them. This led to confusion and unnecessary clutter in the notification experience.
- Now, once an account or repository is marked as spam, notifications they triggered will no longer show up in sidebar counters or counts, even if you were mentioned by them before the spam was detected. As part of this change, close to 6 million spam-related notifications were cleaned up across GitHub to help keep your notifications clear and actionable.

### How to give feedback
- If you have thoughts or feedback on this release, leave a comment on our Community discussion post .

## Article Content (cleaned)
We’ve improved the way notifications from spammy repositories and users are handled, resulting in clearer, more accurate notification counts.


### [Notifications triggered by spam accounts are now correctly hidden](#notifications-triggered-by-spam-accounts-are-now-correctly-hidden)


We’ve updated notification handling so that when a user or repository is flagged as spam, all notifications originating from their activity are reliably hidden, including past mentions from suspicious accounts. Previously, notifications triggered by spammy activity could remain visible and contribute to your unread repository counters, even after hiding or flagging them. This led to confusion and unnecessary clutter in the notification experience.


Now, once an account or repository is marked as spam, notifications they triggered will no longer show up in sidebar counters or counts, even if you were mentioned by them before the spam was detected. As part of this change, close to 6 million spam\-related notifications were cleaned up across GitHub to help keep your notifications clear and actionable.


### [How to give feedback](#how-to-give-feedback)


If you have thoughts or feedback on this release, leave a comment on our [Community discussion post](https://github.com/orgs/community/discussions/180956).
