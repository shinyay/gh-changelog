---
title: "Rate limiting for actions cache entries"
date: "2026-01-16"
type: "deprecations"
labels: ["actions"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-16-rate-limiting-for-actions-cache-entries"
fetched_at: "2026-02-03T14:40:05.155292Z"
---

# Rate limiting for actions cache entries

## Overview
GitHub Actions cache now has a rate limit of 200 uploads/minute per repo. This limit only impacts uploads of new cache entries—it does not impact cache entries that are downloaded in job runs.

## Detailed Explanation
### Overview
- GitHub Actions cache now has a rate limit of 200 uploads/minute per repo. This limit only impacts uploads of new cache entries—it does not impact cache entries that are downloaded in job runs.
- We’ve implemented this limit in response to repositories that upload a high volume of cache entries in very short periods of time which increase cache thrash and impact system stability. We’re working with the authors of some marketplace actions to use behavior that reduces these challenges.
- Users impacted by the rate limits can expect some new cache entry uploads to be rejected until the rate limit resets.

## Impact / Who’s Affected
- This limit only impacts uploads of new cache entries—it does not impact cache entries that are downloaded in job runs.

## Caveats / Limitations
- This limit only impacts uploads of new cache entries—it does not impact cache entries that are downloaded in job runs.

## Article Content (cleaned)
GitHub Actions cache now has a rate limit of 200 uploads/minute per repo. This limit only impacts uploads of new cache entries—it does not impact cache entries that are downloaded in job runs.


We’ve implemented this limit in response to repositories that upload a high volume of cache entries in very short periods of time which increase cache thrash and impact system stability. We’re working with the authors of some marketplace actions to use behavior that reduces these challenges.


Users impacted by the rate limits can expect some new cache entry uploads to be rejected until the rate limit resets.
