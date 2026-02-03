---
title: "Changes to GitHub Dependabot pull request comment commands"
date: "2026-01-27"
type: "deprecations"
labels: ["supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-27-changes-to-github-dependabot-pull-request-comment-commands"
fetched_at: "2026-02-03T14:50:54.700278Z"
---

# Changes to GitHub Dependabot pull request comment commands

## Overview
As we announced in October of 2025 , we deprecated several Dependabot-specific pull request comment commands today in favor of GitHub’s native pull request features and functionality.

## Detailed Explanation
### Overview
- As we announced in October of 2025 , we deprecated several Dependabot-specific pull request comment commands today in favor of GitHub’s native pull request features and functionality.
- This change is intended to reduce confusion, improve reliability, and encourage use of the GitHub platform’s built-in tools for working with pull requests.

### Dependabot comment command deprecations
- These comment commands are no longer supported:
- @dependabot merge
- @dependabot cancel merge
- @dependabot squash and merge
- @dependabot close
- @dependabot reopen

### Migration guidance
- Please update your workflows to rely on GitHub’s native features. For merging, closing, or reopening pull requests, we recommend using GitHub’s built-in UI, the GitHub CLI , and the REST API endpoints for pull requests .

## Impact / Who’s Affected
- As we announced in October of 2025 , we deprecated several Dependabot-specific pull request comment commands today in favor of GitHub’s native pull request features and functionality.

## Insights (derived from article language)
- For merging, closing, or reopening pull requests, we recommend using GitHub’s built-in UI, the GitHub CLI , and the REST API endpoints for pull requests .

## Article Content (cleaned)
As we [announced in October of 2025](https://github.blog/changelog/2025-10-07-upcoming-changes-to-github-dependabot-pull-request-comment-commands/), we deprecated several Dependabot\-specific pull request comment commands today in favor of GitHub’s native pull request features and functionality.


This change is intended to reduce confusion, improve reliability, and encourage use of the GitHub platform’s built\-in tools for working with pull requests.


### [Dependabot comment command deprecations](#dependabot-comment-command-deprecations)


These comment commands are no longer supported:


* `@dependabot merge`
* `@dependabot cancel merge`
* `@dependabot squash and merge`
* `@dependabot close`
* `@dependabot reopen`


### [Migration guidance](#migration-guidance)


Please update your workflows to rely on GitHub’s native features. For merging, closing, or reopening pull requests, we recommend using GitHub’s built\-in UI, the [GitHub CLI](https://cli.github.com/manual/gh_pr), and the [REST API endpoints for pull requests](https://docs.github.com/rest/pulls?apiVersion=2022-11-28).
