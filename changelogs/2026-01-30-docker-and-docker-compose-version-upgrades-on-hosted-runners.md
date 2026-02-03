---
title: "Docker and Docker Compose version upgrades on hosted runners"
date: "2026-01-30"
type: "Improvement"
labels: ["actions"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-30-docker-and-docker-compose-version-upgrades-on-hosted-runners"
fetched_at: "2026-02-03T14:40:04.749054Z"
---

# Docker and Docker Compose version upgrades on hosted runners

## Overview
On February 9th, 2026, Docker and Docker Compose will be updated on all Windows and Ubuntu runner images except ubuntu-slim . This update allows you to take advantage of the latest features in these tools.

## Detailed Explanation
### Overview
- On February 9th, 2026, Docker and Docker Compose will be updated on all Windows and Ubuntu runner images except ubuntu-slim . This update allows you to take advantage of the latest features in these tools.

### New Versions
- Docker Engine: v29.1
- Docker Compose: v2.40 (or higher if new v2 minor versions release before our change)
- You may need to update your workflows if you rely on Docker functionality slated for removal in v29 .

### Keep up to date on upcoming runner image changes
- We regularly update runner images for improved performance, enhanced functionality, and security improvements. You can find a list of other upcoming changes, updates, and deprecations to runner images in the runner-images repository . Check regularly to confirm that your runner images will not be impacted by any scheduled updates.

## Key Changes
- We regularly update runner images for improved performance, enhanced functionality, and security improvements. You can find a list of other upcoming changes, updates, and deprecations to runner images in the runner-images repository . Check regularly to confirm that your runner images will not be impacted by any scheduled updates.

## Caveats / Limitations
- On February 9th, 2026, Docker and Docker Compose will be updated on all Windows and Ubuntu runner images except ubuntu-slim .

## Article Content (cleaned)
On February 9th, 2026, Docker and Docker Compose will be updated on all Windows and Ubuntu runner images except `ubuntu-slim`. This update allows you to take advantage of the latest features in these tools.


### [New Versions](https://github.blog/changelog/feed/#new-versions)


* Docker Engine: `v29.1`
* Docker Compose: `v2.40` (or higher if new v2 minor versions release before our change)


You may need to update your workflows if you rely on Docker functionality [slated for removal in v29](https://docs.docker.com/engine/deprecated/).


### [Keep up to date on upcoming runner image changes](https://github.blog/changelog/feed/#keep-up-to-date-on-upcoming-runner-image-changes)


We regularly update runner images for improved performance, enhanced functionality, and security improvements. You can find a list of other upcoming changes, updates, and deprecations to runner images in the [runner\-images repository](https://github.com/actions/runner-images/labels/Announcement). Check regularly to confirm that your runner images will not be impacted by any scheduled updates.
