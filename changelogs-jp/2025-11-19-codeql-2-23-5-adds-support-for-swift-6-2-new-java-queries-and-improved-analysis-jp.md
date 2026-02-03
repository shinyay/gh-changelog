---
title: "CodeQL 2.23.5がSwift 6.2のサポート、新しいJavaクエリ、改善された分析精度を追加"
date: "2025-11-19"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-19-codeql-2-23-5-adds-support-for-swift-6-2-new-java-queries-and-improved-analysis-accuracy"
fetched_at: "2026-02-03T14:50:55.179992Z"
lang: "ja"
---

# CodeQL 2.23.5がSwift 6.2のサポート、新しいJavaクエリ、改善された分析精度を追加

## Overview
CodeQLは、コード内のセキュリティ問題を発見して修復するGitHubコードスキャニングの背後にある静的解析エンジンです。最近、CodeQL 2.23.5をリリースし、並行性の問題を検出するための3つの新しいJavaセキュリティクエリを導入し、コードスキャニング結果の精度を向上させました。

## Detailed Explanation
### Overview
- CodeQLは、コード内のセキュリティ問題を発見して修復するGitHubコードスキャニングの背後にある静的解析エンジンです。最近、CodeQL 2.23.5をリリースし、並行性の問題を検出するための3つの新しいJavaセキュリティクエリを導入し、コードスキャニング結果の精度を向上させました。
- 言語とフレームワークのサポート
- Swift：CodeQLはSwift 6.2をサポートするようになり、このバージョンでビルドされたプロジェクトを分析できます。
- Rust：actix-webウェブフレームワークのサポートを追加し、mysqlおよびmysql_asyncライブラリのサポートを拡張しました。
- C#：.NET CLI（dotnet）がC#コンパイラ（csc）を直接呼び出す場合のmacOSとLinux用のトレーサーサポートを追加し、これらのプラットフォームで.NET 10 RC2の基本的なトレースと抽出機能を提供します。
- クエリの変更
- C#
- cs/dereferenced-value-may-be-nullクエリを完全に書き直し、非常に多くの誤検出を除去しました。このクエリはpath-problemクエリからproblemクエリに変更されたため、パスは報告されなくなりました。
- cs/constant-conditionクエリを更新し、より広範囲の高信頼度結果を報告するようになりました。
- cs/web/missing-x-frame-optionsクエリを改善し、ルート"要素にネストされた設定を正しく処理するようになりました。
- Java/Kotlin
- java/sensitive-cookie-not-httponlyクエリを実験的なものからメインクエリパックに昇格させました。
- @ThreadSafeでマークされたクラスの並行性の問題を検出する3つの新しいクエリを追加しました：java/escapingはスレッドセーフクラスからエスケープする値を検出します。java/not-threadsafeはスレッドセーフクラスのデータ競合を検出します。java/safe-publicationはスレッドセーフクラスの安全でない公開を検出します。
- String.matchesへの呼び出しは、java/ssrfクエリのサニタイザーとして扱われるようになり、誤検出の発生を減らすことができます。
- java/escapingはスレッドセーフクラスからエスケープする値を検出します。
- java/not-threadsafeはスレッドセーフクラスのデータ競合を検出します。
- java/safe-publicationはスレッドセーフクラスの安全でない公開を検出します。
- Python
- py/insecure-cookieクエリを複数のクエリに分割しました：py/insecure-cookieはSecureフラグが設定されていないケースをチェックします。py/client-exposed-cookieはHttpOnlyフラグが設定されていないケースをチェックします。py/samesite-noneはSameSite属性がNoneに設定されているケースをチェックします。
- これらのクエリは、クッキーに機密データが含まれていることが検出された場合にのみアラートを出すようになりました。
- py/insecure-cookieはSecureフラグが設定されていないケースをチェックします。
- py/client-exposed-cookieはHttpOnlyフラグが設定されていないケースをチェックします。
- py/samesite-noneはSameSite属性がNoneに設定されているケースをチェックします。
- 変更の完全なリストについては、バージョン2.23.5の完全な変更履歴を参照してください。
- 利用可能性
- CodeQLの各新バージョンは、github.comのGitHubコードスキャニングユーザーに自動的にデプロイされます。CodeQL 2.23.5の新機能は、GitHub Enterprise Server（GHES）リリース3.20にも含まれます。古いバージョンのGHESを使用している場合は、手動でCodeQLバージョンをアップグレードしてください。

## Impact / Who's Affected
- Java/Kotlin java/sensitive-cookie-not-httponlyクエリを実験的なものからメインクエリパックに昇格させました。
- Python py/insecure-cookieクエリを複数のクエリに分割しました：py/insecure-cookieはSecureフラグが設定されていないケースをチェックします。py/client-exposed-cookieはHttpOnlyフラグが設定されていないケースをチェックします。py/samesite-noneはSameSite属性がNoneに設定されているケースをチェックします。
- これらのクエリは、クッキーに機密データが含まれていることが検出された場合にのみアラートを出すようになりました。

## Caveats / Limitations
- Java/Kotlin java/sensitive-cookie-not-httponlyクエリを実験的なものからメインクエリパックに昇格させました。
- Python py/insecure-cookieクエリを複数のクエリに分割しました：py/insecure-cookieはSecureフラグが設定されていないケースをチェックします。py/client-exposed-cookieはHttpOnlyフラグが設定されていないケースをチェックします。py/samesite-noneはSameSite属性がNoneに設定されているケースをチェックします。
- これらのクエリは、クッキーに機密データが含まれていることが検出された場合にのみアラートを出すようになりました。

## Article Content (cleaned)
CodeQLは、コード内のセキュリティ問題を発見して修復するGitHubコードスキャニングの背後にある静的解析エンジンです。最近、[CodeQL 2\.23\.5](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.5/)をリリースし、並行性の問題を検出するための3つの新しいJavaセキュリティクエリを導入し、コードスキャニング結果の精度を向上させました。


**言語とフレームワークのサポート**


* **Swift**：CodeQLはSwift 6\.2をサポートするようになり、このバージョンでビルドされたプロジェクトを分析できます。
* **Rust**：`actix-web`ウェブフレームワークのサポートを追加し、`mysql`および`mysql_async`ライブラリのサポートを拡張しました。
* **C\#**：.NET CLI（`dotnet`）がC\#コンパイラ（`csc`）を直接呼び出す場合のmacOSとLinux用のトレーサーサポートを追加し、これらのプラットフォームで.NET 10 RC2の基本的なトレースと抽出機能を提供します。


**クエリの変更**


**C\#**


* `cs/dereferenced-value-may-be-null`クエリを完全に書き直し、非常に多くの誤検出を除去しました。このクエリは`path-problem`クエリから`problem`クエリに変更されたため、パスは報告されなくなりました。
* `cs/constant-condition`クエリを更新し、より広範囲の高信頼度結果を報告するようになりました。
* `cs/web/missing-x-frame-options`クエリを改善し、ルート"要素にネストされた設定を正しく処理するようになりました。


**Java/Kotlin**


* `java/sensitive-cookie-not-httponly`クエリを実験的なものからメインクエリパックに昇格させました。
* `@ThreadSafe`でマークされたクラスの並行性の問題を検出する3つの新しいクエリを追加しました：
	+ `java/escaping`はスレッドセーフクラスからエスケープする値を検出します。
	+ `java/not-threadsafe`はスレッドセーフクラスのデータ競合を検出します。
	+ `java/safe-publication`はスレッドセーフクラスの安全でない公開を検出します。
* `String.matches`への呼び出しは、`java/ssrf`クエリのサニタイザーとして扱われるようになり、誤検出の発生を減らすことができます。


**Python**


* `py/insecure-cookie`クエリを複数のクエリに分割しました：
	+ `py/insecure-cookie`は`Secure`フラグが設定されていないケースをチェックします。
	+ `py/client-exposed-cookie`は`HttpOnly`フラグが設定されていないケースをチェックします。
	+ `py/samesite-none`は`SameSite`属性が`None`に設定されているケースをチェックします。
* これらのクエリは、クッキーに機密データが含まれていることが検出された場合にのみアラートを出すようになりました。


変更の完全なリストについては、[バージョン2\.23\.5の完全な変更履歴](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.5/)を参照してください。


**利用可能性**


CodeQLの各新バージョンは、github.comのGitHubコードスキャニングユーザーに自動的にデプロイされます。CodeQL 2\.23\.5の新機能は、GitHub Enterprise Server（GHES）リリース3\.20にも含まれます。古いバージョンのGHESを使用している場合は、[手動でCodeQLバージョンをアップグレード](https://docs.github.com/enterprise-server@3.18/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access)してください。
