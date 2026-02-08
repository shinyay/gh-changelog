---
title: "CodeQL 2.24.1 が Maven プライベートレジストリサポートを改善し、クエリ精度を向上"
date: "2026-02-07"
type: "Improvement"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-02-06-codeql-2-24-1-improves-maven-private-registry-support-and-improves-query-accuracy"
fetched_at: "2026-02-07T07:18:40.680515Z"
lang: "ja"
---

# CodeQL 2.24.1 が Maven プライベートレジストリサポートを改善し、クエリ精度を向上

## Overview
CodeQL は [GitHub コードスキャニング](https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql) の基盤となる静的解析エンジンで、コード内のセキュリティ問題を検出・修正します。今回リリースされた CodeQL 2.24.1 では、Maven プライベートパッケージレジストリのサポートが改善され、最新バージョンの Kotlin への対応や、コードスキャニング結果の精度を向上させるさまざまな改善が含まれています。

## Detailed Explanation
### Overview
- CodeQL は [GitHub コードスキャニング](https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql) の基盤となる静的解析エンジンです。CodeQL 2.24.1 では、Maven プライベートパッケージレジストリのサポート、最新の Kotlin バージョン対応、およびコードスキャニング精度の向上が含まれています。

### Language and framework support
- Java/Kotlin
- Kotlin 2.3.0 までのバージョンの解析がサポートされました。
- Struts フレームワークライブラリで Struts 7.x のパッケージ名がサポートされました。
- 組織の Default Setup で Maven 互換のプライベートパッケージレジストリを構成すると、CodeQL が Maven をプラグインリポジトリとしても使用するよう構成し、プライベートレジストリから Maven プラグインを取得できるようになりました。
- 注意: [既にアナウンスされた通り](https://github.blog/changelog/2026-01-20-codeql-2-23-9-has-been-released/)、Kotlin 1.6.x および 1.7.x シリーズのサポートは廃止されました。
- C/C++
- C23 および C++26 の `#embed` プリプロセッサディレクティブがサポートされました。
- C#
- C# 14: null 条件付き代入がサポートされました。
- Python
- Python の models-as-data 言語で `ListElement` パスを通じてリスト要素を参照できるようになりました。
- `agents` および `openai` モジュールの汚染フローと型モデルが追加され、`websockets` パッケージのリモートフローソースもモデル化されました。

### Query changes
- C/C++
- `GuardCondition` ライブラリのバグが修正され、二項論理演算子がガード条件として認識されないことがあった問題が解消されました。
- バッファサイズの測定精度が向上し、`cpp/static-buffer-overflow`、`cpp/overflow-buffer`、`cpp/badly-bounded-write`、`cpp/overrunning-write`、`cpp/overrunning-write-with-float`、`cpp/very-likely-overrunning-write` クエリの偽陽性が減少しました。
- Java
- `java/unreleased-lock` クエリの精度が改善されました。
- Python
- LLM を使用するコードにおけるプロンプトインジェクションの脆弱性を検出する実験的なクエリ `py/prompt-injection` が追加されました。
- GitHub Actions
- 約 300 文字を超える `${{ ... }}` 式を解析する際のクラッシュが修正されました。
- 変更の完全なリストについては、[バージョン 2.24.1 の完全な変更ログ](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.24.1/)を参照してください。CodeQL の新バージョンは github.com のコードスキャニングユーザーに自動デプロイされます。CodeQL 2.24.1 の新機能は将来の GitHub Enterprise Server (GHES) リリースにも含まれます。古いバージョンの GHES を使用されている場合は、[CodeQL バージョンを手動でアップグレード](https://docs.github.com/enterprise-server@3.19/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access)できます。

## Key Changes
- C/C++
- `GuardCondition` ライブラリのバグが修正され、二項論理演算子がガード条件として認識されないことがあった問題が解消されました。
- バッファサイズの測定精度が向上し、`cpp/static-buffer-overflow`、`cpp/overflow-buffer`、`cpp/badly-bounded-write`、`cpp/overrunning-write`、`cpp/overrunning-write-with-float`、`cpp/very-likely-overrunning-write` クエリの偽陽性が減少しました。
- Java
- `java/unreleased-lock` クエリの精度が改善されました。
- Python
- LLM を使用するコードにおけるプロンプトインジェクション脆弱性を検出する実験的なクエリ `py/prompt-injection` が追加されました。
- GitHub Actions
- 約 300 文字を超える `${{ ... }}` 式を解析する際のクラッシュが修正されました。
- 変更の完全なリストについては、[バージョン 2.24.1 の完全な変更ログ](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.24.1/)を参照してください。CodeQL の新バージョンは github.com のコードスキャニングユーザーに自動デプロイされます。CodeQL 2.24.1 の新機能は将来の GitHub Enterprise Server (GHES) リリースにも含まれます。古いバージョンの GHES を使用されている場合は、[CodeQL バージョンを手動でアップグレード](https://docs.github.com/enterprise-server@3.19/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access)できます。

## Impact / Who’s Affected
- Java/Kotlin: Kotlin 2.3.0 までのバージョンの解析がサポートされました。

## Caveats / Limitations
- 注意: 既にアナウンスされた通り、Kotlin 1.6.x および 1.7.x シリーズのサポートは廃止されました。

## Article Content (cleaned)
CodeQL は [GitHub コードスキャニング](https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql) の基盤となる静的解析エンジンで、コード内のセキュリティ問題を検出・修正します。今回リリースされた [CodeQL 2.24.1](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.24.1/) では、Maven プライベートパッケージレジストリのサポートが改善され、最新バージョンの Kotlin への対応や、コードスキャニング結果の精度を向上させるさまざまな改善が含まれています。


## [Language and framework support](https://github.blog/changelog/feed/#language-and-framework-support)


**Java/Kotlin**


* Kotlin 2.3.0 までのバージョンの解析がサポートされました。
* Struts フレームワークライブラリで Struts 7.x のパッケージ名がサポートされました。
* 組織の Default Setup で Maven 互換のプライベートパッケージレジストリを構成すると、CodeQL が Maven をプラグインリポジトリとしても使用するよう構成し、プライベートレジストリから Maven プラグインを取得できるようになりました。
* **注意**: [既にアナウンスされた通り](https://github.blog/changelog/2026-01-20-codeql-2-23-9-has-been-released/)、Kotlin 1.6.x および 1.7.x シリーズのサポートは廃止されました。


**C/C\+\+**


* C23 および C\+\+26 の `#embed` プリプロセッサディレクティブがサポートされました。


**C\#**


* C\# 14: null 条件付き代入がサポートされました。


**Python**


* Python の models-as-data 言語で `ListElement` パスを通じてリスト要素を参照できるようになりました。
* `agents` および `openai` モジュールの汚染フローと型モデルが追加され、`websockets` パッケージのリモートフローソースもモデル化されました。


## [Query changes](https://github.blog/changelog/feed/#query-changes)


**C/C\+\+**


* `GuardCondition` ライブラリのバグが修正され、二項論理演算子がガード条件として認識されないことがあった問題が解消されました。これにより、`GuardCondition` を使用しているクエリの結果が改善される可能性があります。
* バッファサイズの測定精度が向上し、`cpp/static-buffer-overflow`、`cpp/overflow-buffer`、`cpp/badly-bounded-write`、`cpp/overrunning-write`、`cpp/overrunning-write-with-float`、`cpp/very-likely-overrunning-write` クエリの偽陽性が減少しました。


**Java**


* `java/unreleased-lock` クエリの精度が改善されました。


**Python**


* LLM を使用するコードにおけるプロンプトインジェクションの脆弱性を検出する実験的なクエリ `py/prompt-injection` が追加されました。


**GitHub Actions**


* 約 300 文字を超える `${{ ... }}` 式を解析する際のクラッシュが修正されました。


変更の完全なリストについては、[バージョン 2.24.1 の完全な変更ログ](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.24.1/)を参照してください。CodeQL の新バージョンは github.com のコードスキャニングユーザーに自動デプロイされます。CodeQL 2.24.1 の新機能は将来の GitHub Enterprise Server (GHES) リリースにも含まれます。古いバージョンの GHES を使用されている場合は、[CodeQL バージョンを手動でアップグレード](https://docs.github.com/enterprise-server@3.19/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access)できます。
