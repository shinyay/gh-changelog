---
title: "CodeQL 2.23.9 がリリースされました"
date: "2026-01-20"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-20-codeql-2-23-9-has-been-released"
fetched_at: "2026-02-03T14:50:54.737833Z"
lang: "ja"
---

# CodeQL 2.23.9 がリリースされました

## Overview
CodeQL は GitHub コードスキャンの背後にある静的解析エンジンで、コード内のセキュリティ問題を検出して修復します。最近、CodeQL 2.23.9 をリリースしました。CodeQL CLI にユーザー向けの変更はなく、クエリの変更もありませんが、2.23.9 がリリースされたことを認識するためにこの変更ログを投稿しています。

## Detailed Explanation
### Overview
- CodeQL は GitHub コードスキャンの背後にある静的解析エンジンで、コード内のセキュリティ問題を検出して修復します。最近、CodeQL 2.23.9 をリリースしました。CodeQL CLI にユーザー向けの変更はなく、クエリの変更もありませんが、2.23.9 がリリースされたことを認識するためにこの変更ログを投稿しています。

### Deprecation notice
- Kotlin バージョン 1.6 および 1.7 のサポートは非推奨となり、2026年2月にリリース予定の CodeQL 2.24.1 で削除されます。そのバージョンから、Kotlin データベースを抽出するには Kotlin 1.8 以降を使用する必要があります。
- CodeQL の新しいバージョンはすべて、github.com の GitHub コードスキャンのユーザーに自動的にデプロイされます。CodeQL 2.23.9 の新機能は、将来の GitHub Enterprise Server (GHES) リリースにも含まれます。古いバージョンの GHES を使用している場合は、CodeQL バージョンを手動でアップグレードできます。

## Impact / Who's Affected
- Deprecation notice Kotlin バージョン 1.6 および 1.7 のサポートは非推奨となり、2026年2月にリリース予定の CodeQL 2.24.1 で削除されます。

## Article Content (cleaned)
CodeQL は [GitHub コードスキャン](https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql) の背後にある静的解析エンジンで、コード内のセキュリティ問題を検出して修復します。最近、[CodeQL 2.23.9](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.9/) をリリースしました。CodeQL CLI にユーザー向けの変更はなく、クエリの変更もありませんが、2.23.9 がリリースされたことを認識するためにこの変更ログを投稿しています。


## [Deprecation notice](#deprecation-notice)


Kotlin バージョン 1.6 および 1.7 のサポートは非推奨となり、2026年2月にリリース予定の CodeQL 2.24.1 で削除されます。そのバージョンから、Kotlin データベースを抽出するには Kotlin 1.8 以降を使用する必要があります。


CodeQL の新しいバージョンはすべて、github.com の GitHub コードスキャンのユーザーに自動的にデプロイされます。CodeQL 2.23.9 の新機能は、将来の GitHub Enterprise Server (GHES) リリースにも含まれます。古いバージョンの GHES を使用している場合は、[CodeQL バージョンを手動でアップグレード](https://docs.github.com/enterprise-server@3.19/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access) できます。
