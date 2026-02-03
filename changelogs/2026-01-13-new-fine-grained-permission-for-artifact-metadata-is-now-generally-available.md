---
title: "New fine-grained permission for artifact metadata is now generally available"
date: "2026-01-13"
type: "new releases"
labels: ["actions", "application security", "supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-13-new-fine-grained-permission-for-artifact-metadata-is-now-generally-available"
fetched_at: "2026-02-03T14:50:54.813228Z"
---

# New fine-grained permission for artifact metadata is now generally available

## Overview
GitHub has introduced a new artifact_metadata permission to give you more precise control over API access to artifact-related metadata. This permission replaces the broader contents:read and contents:write permissions for the artifact metadata APIs .

## Detailed Explanation
### Overview
- GitHub has introduced a new artifact_metadata permission to give you more precise control over API access to artifact-related metadata. This permission replaces the broader contents:read and contents:write permissions for the artifact metadata APIs .
- Transition any workflows currently using the contents permission for artifact metadata APIs to the new artifact_metadata permission before February 3, 2026, when support for the old permission will be deprecated.

### Learn more
- Artifact metadata APIs documentation
- Repository permissions for artifact metadata
- Actions permissions reference
- How artifact metadata improves security alerts

## Impact / Who’s Affected
- Transition any workflows currently using the contents permission for artifact metadata APIs to the new artifact_metadata permission before February 3, 2026, when support for the old permission will be deprecated.

## Insights (derived from article language)
- Learn more Artifact metadata APIs documentation Repository permissions for artifact metadata Actions permissions reference How artifact metadata improves security alerts

## Article Content (cleaned)
GitHub has introduced a new `artifact_metadata` permission to give you more precise control over API access to artifact\-related metadata. This permission replaces the broader `contents:read` and `contents:write` permissions for the [artifact metadata APIs](https://docs.github.com/rest/orgs/artifact-metadata).


Transition any workflows currently using the `contents` permission for artifact metadata APIs to the new `artifact_metadata` permission before February 3, 2026, when support for the old permission will be deprecated.


### [Learn more](#learn-more)


* [Artifact metadata APIs documentation](https://docs.github.com/rest/orgs/artifact-metadata)
* [Repository permissions for artifact metadata](https://docs.github.com/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens#repository-permissions-for-artifact-metadata)
* [Actions permissions reference](https://docs.github.com/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idpermissions)
* [How artifact metadata improves security alerts](https://docs.github.com/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)
