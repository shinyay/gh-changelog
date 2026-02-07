---
title: "GitHub Actions: Self-hosted runner minimum version enforcement extended"
date: "2026-02-05"
type: "Retired"
labels: ["actions"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-02-05-github-actions-self-hosted-runner-minimum-version-enforcement-extended"
fetched_at: "2026-02-07T21:06:48.080040Z"
---

# GitHub Actions: Self-hosted runner minimum version enforcement extended

## Overview
We’ve extended the timeline for configuration‑time version enforcement of the minimum self‑hosted runner requirement by one week. You now have until March 16, 2026 to upgrade your runners to v2.329.0 or later.

## Detailed Explanation
### Overview
- We’ve extended the timeline for configuration‑time version enforcement of the minimum self‑hosted runner requirement by one week. You now have until March 16, 2026 to upgrade your runners to v2.329.0 or later.
- This extends the timeline we shared in our December 2025 announcement .

### What’s changing
- Starting March 16, 2026, GitHub Actions will block configurations from self-hosted runners older than v2.329.0 (released October 15, 2025). Between February 16 and March 16, we’ll run a brownout period with scheduled configuration blocks to help you identify runners that need updates.
- After March 16, runners must meet the minimum version requirement before registration. Older runners won’t be able to connect or self-upgrade after running the configuration script.

### Brownout schedule
- During the brownout period, we’ll temporarily block configurations from runners below v2.329.0. This table shows when blocks will occur in major timezones:
- *Times marked with an asterisk fall on the next day in that timezone.
- Full enforcement begins March 16, 2026 . At that time, all configurations from runners below v2.329.0 will be permanently blocked.

### What you need to do
- Update all self-hosted runners to v2.329.0 or later by March 16, 2026:
- Download the latest runner release from the Actions Runner releases page .
- Update your installation scripts, images, or automation to install v2.329.0 or later before running ./config.sh .
- Recreate or redeploy any runners built from images or templates that contain older versions.
- Review the upgrade documentation for detailed guidance.

## Article Content (cleaned)
We’ve extended the timeline for configuration‑time version enforcement of the minimum self‑hosted runner requirement by one week. You now have until March 16, 2026 to upgrade your runners to v2\.329\.0 or later.


This extends the timeline we shared in our [December 2025 announcement](https://github.blog/changelog/2025-12-12-better-diagnostics-for-vnet-injected-runners-and-required-self-hosted-runner-upgrades/#required-upgrade-for-self-hosted-runners).


### [What’s changing](https://github.blog/changelog/feed/#whats-changing)


Starting March 16, 2026, GitHub Actions will block configurations from self\-hosted runners older than v2\.329\.0 (released October 15, 2025\). Between February 16 and March 16, we’ll run a brownout period with scheduled configuration blocks to help you identify runners that need updates.


After March 16, runners must meet the minimum version requirement before registration. Older runners won’t be able to connect or self\-upgrade after running the configuration script.


### [Brownout schedule](https://github.blog/changelog/feed/#brownout-schedule)


During the brownout period, we’ll temporarily block configurations from runners below v2\.329\.0\. This table shows when blocks will occur in major timezones:




| Week | Dates (2026\) | UTC Time | US Pacific | US Eastern | Central Europe | India | Japan/Korea | Australia East |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Feb 16 (Sun) | 08:00\-09:00 | 00:00\-01:00 | 03:00\-04:00 | 09:00\-10:00 | 13:30\-14:30 | 17:00\-18:00 | 19:00\-20:00 |
| 2 | Feb 23 (Sun) | 08:00\-10:00 | 00:00\-02:00 | 03:00\-05:00 | 09:00\-11:00 | 13:30\-15:30 | 17:00\-19:00 | 19:00\-21:00 |
| 2 | Feb 25 (Tue) | 16:00\-18:00 | 08:00\-10:00 | 11:00\-13:00 | 17:00\-19:00 | 21:30\-23:30 | 01:00\-03:00\* | 03:00\-05:00\* |
| 3 | Mar 2 (Mon) | 00:00\-04:00 | 16:00\-20:00\* | 19:00\-23:00\* | 01:00\-05:00 | 05:30\-09:30 | 09:00\-13:00 | 11:00\-15:00 |
| 3 | Mar 4 (Wed) | 12:00\-16:00 | 04:00\-08:00 | 07:00\-11:00 | 13:00\-17:00 | 17:30\-21:30 | 21:00\-01:00\* | 23:00\-03:00\* |
| 3 | Mar 6 (Fri) | 20:00\-00:00\* | 12:00\-16:00 | 15:00\-19:00 | 21:00\-01:00\* | 01:30\-05:30\* | 05:00\-09:00\* | 07:00\-11:00\* |
| 4 | Mar 9 (Mon) | 08:00 onwards | 00:00 onwards | 03:00 onwards | 09:00 onwards | 13:30 onwards | 17:00 onwards | 19:00 onwards |


\*Times marked with an asterisk fall on the next day in that timezone.


**Full enforcement begins March 16, 2026**. At that time, all configurations from runners below v2\.329\.0 will be permanently blocked.


### [What you need to do](https://github.blog/changelog/feed/#what-you-need-to-do)


Update all self\-hosted runners to v2\.329\.0 or later by March 16, 2026:


1. Download the latest runner release from the [Actions Runner releases page](https://github.com/actions/runner/releases).
2. Update your installation scripts, images, or automation to install v2\.329\.0 or later before running `./config.sh`.
3. Recreate or redeploy any runners built from images or templates that contain older versions.
4. Review the [upgrade documentation](https://docs.github.com/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners#communication-requirements) for detailed guidance.
