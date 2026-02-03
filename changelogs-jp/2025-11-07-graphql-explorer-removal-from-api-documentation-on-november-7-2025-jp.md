---
title: "2025年11月7日に API ドキュメントから GraphQL Explorer を削除"
date: "2025-11-07"
type: "deprecations"
labels: ["ecosystem and accessibility"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-07-graphql-explorer-removal-from-api-documentation-on-november-7-2025"
fetched_at: "2026-02-03T14:50:55.378499Z"
lang: "ja"
---

# 2025年11月7日に API ドキュメントから GraphQL Explorer を削除

## Overview
編集者注記（2025年11月18日）: エンタープライズへの影響を明確にするため、この投稿を更新しました。

## Detailed Explanation
### 概要
- 編集者注記（2025年11月18日）: エンタープライズへの影響を明確にするため、この投稿を更新しました。
- 以前の発表通知に従い、GraphQL Explorer を廃止しました。

### 影響を受けるユーザー
- 監査ログを使用する顧客は、エンタープライズ内の複数のユーザーについて org_credential_authorization.deauthorize 、 oauth_authorization.destroy 、および oauth_access.destroy イベントを確認します。これらのイベントは、GraphQL Explorer の OAuth App の削除に関連しています。

### この変更が重要な理由
- Explorer の廃止により、GitHub GraphQL API での迅速なテストやプロトタイピングに使用していた開発者のワークフローが中断されることを理解しています。全体的な使用率は限定的でしたが、この変更が依存していたユーザーにとって残念なものであることを認識しています。
- Explorer を廃止する決定は軽々しく行われたものではなく、技術的負債の増大、コストのかかる継続的なメンテナンス（特にセキュリティとアクセシビリティ）、およびコンプライアンスを維持できないサードパーティライブラリへの依存によって推進されています。

### あなたがすべきこと
- 現在 GraphQL Explorer を使用している場合は、GitHub GraphQL API を使用するためのローカル開発ツールに移行することをお勧めします。更新されたドキュメントには、人気のある GraphQL クライアントの使用を開始するためのガイダンスが含まれています。

### 詳細を知る
- GitHub GraphQL API の使用について詳しくは、GraphQL API ドキュメントを参照してください。
- フィードバックや質問がありますか？ GitHub Community で会話に参加してください。
- この変更は、GitHub の API をより高速で、よりスケーラブルで、誰にとっても使いやすくするという私たちの継続的なコミットメントをサポートしています。

## Impact / Who's Affected
- 以前の発表通知に従い、GraphQL Explorer を廃止しました。
- 全体的な使用率は限定的でしたが、この変更が依存していたユーザーにとって残念なものであることを認識しています。

## Caveats / Limitations
- 編集者注記（2025年11月18日）: エンタープライズへの影響を明確にするため、この投稿を更新しました。
- 全体的な使用率は限定的でしたが、この変更が依存していたユーザーにとって残念なものであることを認識しています。

## Insights (derived from article language)
- あなたがすべきこと 現在 GraphQL Explorer を使用している場合は、GitHub GraphQL API を使用するためのローカル開発ツールに移行することをお勧めします。
- 詳細を知る GitHub GraphQL API の使用について詳しくは、GraphQL API ドキュメントを参照してください。

## Article Content (cleaned)
*編集者注記（2025年11月18日）: エンタープライズへの影響を明確にするため、この投稿を更新しました。*


[以前の発表通知](https://github.blog/changelog/2025-08-22-graphql-explorer-removal-from-api-documentation-on-november-1-2025/)に従い、GraphQL Explorer を廃止しました。


## [影響を受けるユーザー](#who-this-affects)


[監査ログ](https://docs.github.com/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization)を使用する顧客は、エンタープライズ内の複数のユーザーについて `org_credential_authorization.deauthorize`、`oauth_authorization.destroy`、および `oauth_access.destroy` イベントを確認します。これらのイベントは、GraphQL Explorer の OAuth App の削除に関連しています。


## [この変更が重要な理由](#why-this-change-matters)


Explorer の廃止により、GitHub GraphQL API での迅速なテストやプロトタイピングに使用していた開発者のワークフローが中断されることを理解しています。全体的な使用率は限定的でしたが、この変更が依存していたユーザーにとって残念なものであることを認識しています。


Explorer を廃止する決定は軽々しく行われたものではなく、技術的負債の増大、コストのかかる継続的なメンテナンス（特にセキュリティとアクセシビリティ）、およびコンプライアンスを維持できないサードパーティライブラリへの依存によって推進されています。


## [あなたがすべきこと](#what-you-should-do)


現在 GraphQL Explorer を使用している場合は、GitHub GraphQL API を使用するためのローカル開発ツールに移行することをお勧めします。[更新されたドキュメント](https://docs.github.com/graphql/guides/using-graphql-clients)には、人気のある GraphQL クライアントの使用を開始するためのガイダンスが含まれています。


## [詳細を知る](#learn-more)


GitHub GraphQL API の使用について詳しくは、[GraphQL API ドキュメント](https://docs.github.com/graphql)を参照してください。


フィードバックや質問がありますか？ [GitHub Community](https://github.com/orgs/community/discussions/categories/announcements) で会話に参加してください。




---


*この変更は、GitHub の API をより高速で、よりスケーラブルで、誰にとっても使いやすくするという私たちの継続的なコミットメントをサポートしています。*
