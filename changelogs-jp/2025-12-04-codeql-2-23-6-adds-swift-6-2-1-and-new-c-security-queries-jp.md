---
title: "CodeQL 2.23.6がSwift 6.2.1と新しいC#セキュリティクエリを追加"
date: "2025-12-04"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-04-codeql-2-23-6-adds-swift-6-2-1-and-new-c-security-queries"
fetched_at: "2026-02-03T14:50:55.066341Z"
lang: "ja"
---

# CodeQL 2.23.6がSwift 6.2.1と新しいC#セキュリティクエリを追加

## Overview
CodeQLは、コード内のセキュリティ問題を検出して修正するGitHub code scanningの背後にある静的解析エンジンです。最近、CodeQL 2.23.6をリリースしました。これは、Swift 6.2.1のサポートを追加し、2つのC# Cookieセキュリティクエリを昇格し、言語間でさまざまな精度の改善を含んでいます。

## Detailed Explanation
### Overview
- CodeQLは、コード内のセキュリティ問題を検出して修正するGitHub code scanningの背後にある静的解析エンジンです。最近、CodeQL 2.23.6をリリースしました。これは、Swift 6.2.1のサポートを追加し、2つのC# Cookieセキュリティクエリを昇格し、言語間でさまざまな精度の改善を含んでいます。

### 言語とフレームワークのサポート
- Swift：CodeQLは、Swift 6.2.1でビルドされたアプリの解析をサポートするようになりました。
- Rust：`poem`クレートのCookieメソッドのモデルを追加しました。

### クエリの変更
- C#：`cs/web/cookie-secure-not-set`および`cs/web/cookie-httponly-not-set`クエリが実験的なものからメインクエリパックに昇格しました。これらのクエリは、適切なセキュリティ属性なしで作成されたCookieを検出します。Guardsライブラリを改善して選言を認識するようにし、`cs/constant-condition`、`cs/inefficient-containskey`、および`cs/dereferenced-value-may-be-null`クエリの精度が向上しました。
- Rust：`rust/regex-injection`、`rust/sql-injection`、および`rust/log-injection`クエリに汚染フローバリアを追加し、誤検出結果の頻度を削減しました。
- Java/Kotlin：`java/overly-large-range`および`java/insecure-cookie`の`security-severity`スコアを5.0から4.0に削減し、影響をより適切に反映するようにしました。
- JavaScript/TypeScript：`js/xss-through-dom`の`security-severity`スコアを6.1から7.8に引き上げて他のXSSクエリと整合させ、`js/overly-large-range`のスコアを5.0から4.0に削減しました。
- Python：`py/overly-large-range`の`security-severity`スコアを5.0から4.0に削減し、影響をより適切に反映するようにしました。
- Ruby：`rb/overly-large-range`の`security-severity`スコアを5.0から4.0に削減し、影響をより適切に反映するようにしました。
- `cs/web/cookie-secure-not-set`および`cs/web/cookie-httponly-not-set`クエリが実験的なものからメインクエリパックに昇格しました。これらのクエリは、適切なセキュリティ属性なしで作成されたCookieを検出します。
- Guardsライブラリを改善して選言を認識するようにし、`cs/constant-condition`、`cs/inefficient-containskey`、および`cs/dereferenced-value-may-be-null`クエリの精度が向上しました。
- 変更の完全なリストについては、バージョン2.23.6の完全な変更ログをご覧ください。CodeQLの新しいバージョンはすべて、github.comのGitHub code scanningのユーザーに自動的にデプロイされます。CodeQL 2.23.6の新機能は、GitHub Enterprise Server (GHES) 3.20リリースにも含まれます。古いバージョンのGHESを使用している場合は、CodeQLバージョンを手動でアップグレードできます。

## Key Changes
- C#：`cs/web/cookie-secure-not-set`および`cs/web/cookie-httponly-not-set`クエリが実験的なものからメインクエリパックに昇格しました。これらのクエリは、適切なセキュリティ属性なしで作成されたCookieを検出します。Guardsライブラリを改善して選言を認識するようにし、`cs/constant-condition`、`cs/inefficient-containskey`、および`cs/dereferenced-value-may-be-null`クエリの精度が向上しました。
- Rust：`rust/regex-injection`、`rust/sql-injection`、および`rust/log-injection`クエリに汚染フローバリアを追加し、誤検出結果の頻度を削減しました。
- Java/Kotlin：`java/overly-large-range`および`java/insecure-cookie`の`security-severity`スコアを5.0から4.0に削減し、影響をより適切に反映するようにしました。
- JavaScript/TypeScript：`js/xss-through-dom`の`security-severity`スコアを6.1から7.8に引き上げて他のXSSクエリと整合させ、`js/overly-large-range`のスコアを5.0から4.0に削減しました。
- Python：`py/overly-large-range`の`security-severity`スコアを5.0から4.0に削減し、影響をより適切に反映するようにしました。
- Ruby：`rb/overly-large-range`の`security-severity`スコアを5.0から4.0に削減し、影響をより適切に反映するようにしました。
- `cs/web/cookie-secure-not-set`および`cs/web/cookie-httponly-not-set`クエリが実験的なものからメインクエリパックに昇格しました。これらのクエリは、適切なセキュリティ属性なしで作成されたCookieを検出します。
- Guardsライブラリを改善して選言を認識するようにし、`cs/constant-condition`、`cs/inefficient-containskey`、および`cs/dereferenced-value-may-be-null`クエリの精度が向上しました。
- 変更の完全なリストについては、バージョン2.23.6の完全な変更ログをご覧ください。CodeQLの新しいバージョンはすべて、github.comのGitHub code scanningのユーザーに自動的にデプロイされます。CodeQL 2.23.6の新機能は、GitHub Enterprise Server (GHES) 3.20リリースにも含まれます。古いバージョンのGHESを使用している場合は、CodeQLバージョンを手動でアップグレードできます。

## Impact / Who’s Affected
- クエリの変更 C#：`cs/web/cookie-secure-not-set`および`cs/web/cookie-httponly-not-set`クエリが実験的なものからメインクエリパックに昇格しました。

## Caveats / Limitations
- クエリの変更 C#：`cs/web/cookie-secure-not-set`および`cs/web/cookie-httponly-not-set`クエリが実験的なものからメインクエリパックに昇格しました。

## Article Content (cleaned)
CodeQLは、コード内のセキュリティ問題を検出して修正する[GitHub code scanning](https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql)の背後にある静的解析エンジンです。最近、[CodeQL 2\.23\.6](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.6/)をリリースしました。これは、Swift 6\.2\.1のサポートを追加し、2つのC\# Cookieセキュリティクエリを昇格し、言語間でさまざまな精度の改善を含んでいます。


## [Language and framework support](#language-and-framework-support)


* **Swift**：CodeQLは、Swift 6\.2\.1でビルドされたアプリの解析をサポートするようになりました。
* **Rust**：`poem`クレートのCookieメソッドのモデルを追加しました。


## [Query changes](#query-changes)


* **C\#**：
	+ `cs/web/cookie-secure-not-set`および`cs/web/cookie-httponly-not-set`クエリが実験的なものからメインクエリパックに昇格しました。これらのクエリは、適切なセキュリティ属性なしで作成されたCookieを検出します。
	+ Guardsライブラリを改善して選言を認識するようにし、`cs/constant-condition`、`cs/inefficient-containskey`、および`cs/dereferenced-value-may-be-null`クエリの精度が向上しました。
* **Rust**：`rust/regex-injection`、`rust/sql-injection`、および`rust/log-injection`クエリに汚染フローバリアを追加し、誤検出結果の頻度を削減しました。
* **Java/Kotlin**：`java/overly-large-range`および`java/insecure-cookie`の`security-severity`スコアを5\.0から4\.0に削減し、影響をより適切に反映するようにしました。
* **JavaScript/TypeScript**：`js/xss-through-dom`の`security-severity`スコアを6\.1から7\.8に引き上げて他のXSSクエリと整合させ、`js/overly-large-range`のスコアを5\.0から4\.0に削減しました。
* **Python**：`py/overly-large-range`の`security-severity`スコアを5\.0から4\.0に削減し、影響をより適切に反映するようにしました。
* **Ruby**：`rb/overly-large-range`の`security-severity`スコアを5\.0から4\.0に削減し、影響をより適切に反映するようにしました。


変更の完全なリストについては、[バージョン2\.23\.6の完全な変更ログ](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.6/)をご覧ください。CodeQLの新しいバージョンはすべて、github.comのGitHub code scanningのユーザーに自動的にデプロイされます。CodeQL 2\.23\.6の新機能は、GitHub Enterprise Server (GHES) 3\.20リリースにも含まれます。古いバージョンのGHESを使用している場合は、[CodeQLバージョンを手動でアップグレード](https://docs.github.com/enterprise-server@3.17/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access)できます。
