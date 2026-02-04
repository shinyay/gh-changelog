---
title: "アーティファクトメタデータ用の新しい細かい権限が一般提供開始"
date: "2026-01-13"
type: "new releases"
labels: ["actions", "application security", "supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-13-new-fine-grained-permission-for-artifact-metadata-is-now-generally-available"
fetched_at: "2026-02-03T14:50:54.813228Z"
lang: "ja"
---

# アーティファクトメタデータ用の新しい細かい権限が一般提供開始

## Overview
GitHubは、アーティファクト関連のメタデータへのAPIアクセスをより正確に制御できる新しい`artifact_metadata`権限を導入しました。この権限は、アーティファクトメタデータAPIのより広範な`contents:read`および`contents:write`権限に代わるものです。

## Detailed Explanation
### Overview
- GitHubは、アーティファクト関連のメタデータへのAPIアクセスをより正確に制御できる新しい`artifact_metadata`権限を導入しました。この権限は、アーティファクトメタデータAPIのより広範な`contents:read`および`contents:write`権限に代わるものです。
- 2026年2月3日に古い権限のサポートが廃止される前に、現在アーティファクトメタデータAPIに`contents`権限を使用しているワークフローを新しい`artifact_metadata`権限に移行してください。

### Learn more
- Artifact metadata APIs documentation
- Repository permissions for artifact metadata
- Actions permissions reference
- How artifact metadata improves security alerts

## Impact / Who’s Affected
- 2026年2月3日に古い権限のサポートが廃止される前に、現在アーティファクトメタデータAPIに`contents`権限を使用しているワークフローを新しい`artifact_metadata`権限に移行してください。

## Insights (derived from article language)
- Learn more Artifact metadata APIs documentation Repository permissions for artifact metadata Actions permissions reference How artifact metadata improves security alerts

## Article Content (cleaned)
GitHubは、アーティファクト関連のメタデータへのAPIアクセスをより正確に制御できる新しい`artifact_metadata`権限を導入しました。この権限は、[アーティファクトメタデータAPI](https://docs.github.com/rest/orgs/artifact-metadata)のより広範な`contents:read`および`contents:write`権限に代わるものです。


2026年2月3日に古い権限のサポートが廃止される前に、現在アーティファクトメタデータAPIに`contents`権限を使用しているワークフローを新しい`artifact_metadata`権限に移行してください。


### [Learn more](#learn-more)


* [Artifact metadata APIs documentation](https://docs.github.com/rest/orgs/artifact-metadata)
* [Repository permissions for artifact metadata](https://docs.github.com/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens#repository-permissions-for-artifact-metadata)
* [Actions permissions reference](https://docs.github.com/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idpermissions)
* [How artifact metadata improves security alerts](https://docs.github.com/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)
