---
title: "CodeQL 2.23.7と2.23.8がGoとRustのセキュリティクエリを追加"
date: "2025-12-18"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-18-codeql-2-23-7-and-2-23-8-add-security-queries-for-go-and-rust"
fetched_at: "2026-02-03T14:50:54.850960Z"
lang: "ja"
---

# CodeQL 2.23.7と2.23.8がGoとRustのセキュリティクエリを追加

## Overview
CodeQLは、GitHubのCode ScanningおよびCode Quality製品の背後にある静的解析エンジンで、コード品質とセキュリティに関する問題を発見して修正します。最近、CodeQL 2.23.7と2.23.8をリリースしました。これらのリリースは、GoとRustの新しいセキュリティクエリ、全体的な分析精度の向上、複数の言語にわたるフレームワークの更新をもたらします。

## Detailed Explanation
### Overview
- CodeQLは、GitHubのCode ScanningおよびCode Quality製品の背後にある静的解析エンジンで、コード品質とセキュリティに関する問題を発見して修正します。最近、CodeQL 2.23.7と2.23.8をリリースしました。これらのリリースは、GoとRustの新しいセキュリティクエリ、全体的な分析精度の向上、複数の言語にわたるフレームワークの更新をもたらします。

### Query changes
- Go
- `Secure`フラグが設定されていないクッキーを検出する新しいクエリ`go/cookie-secure-not-set`を追加しました。これにより機密情報の漏洩が発生する可能性があります。
- 壊れたまたは弱い暗号化アルゴリズムの使用を検出する新しいクエリ`go/weak-crypto-algorithm`を追加しました。
- 機密データに対する壊れたまたは弱い暗号化ハッシュアルゴリズムの使用を検出する新しいクエリ`go/weak-sensitive-data-hashing`を追加しました。
- `go/cookie-http-only-not-set`クエリが実験クエリパックから昇格し、`HttpOnly`フラグを使用しないクッキーを特定し、クロスサイトスクリプティングの脆弱性につながる可能性があります。このクエリは、GitHubユーザー@edvraaによって元々寄稿されました。
- Rust
- クロスサイトスクリプティングのセキュリティ脆弱性を検出する新しいクエリ`rust/xss`を追加しました。
- 無効化されたTLS証明書チェックを検出する新しいクエリ`rust/disabled-certificate-check`を追加しました。
- Rust用のCodeQLクエリの作成方法を学ぶのに役立つ3つのサンプルクエリ（`rust/examples/empty-if`、`rust/examples/simple-sql-injection`、`rust/examples/simple-constant-password`）を追加しました。

### Language and framework support
- Java/Kotlin
- Java分析は、Mavenビルドで`--source`および`--target`コンパイラフラグを強制しなくなりました。Mavenはプロジェクト独自のコンパイラ設定を使用するようになり、ビルドの互換性が向上します。
- 文字列の固定長のプレフィックスまたはサフィックスのみを抽出する操作（Javaの`substring`やKotlinの`take`など）は、7文字以下に制限されている場合、`java/sensitive-log`クエリのサニタイザーとして扱われます。これは、ログメッセージの内容が切り捨てられるためです。
- JavaScript/TypeScript
- `app/pages`フォルダーのサーバーサイドテイントソースを分析が見逃す原因となっていたNext.jsモデルのバグを修正しました。
- Rust
- `rust/access-invalid-pointer`クエリが新しいフローソースとバリアで改善されました。
- C#
- ビルドレス分析（デフォルトで使用）を使用する場合、コンパイルエラーがデバッグログに含まれるようになりました。
- ビルドレスモードで依存関係のダウンロード用のカスタムディレクトリを指定する新しい抽出オプションを追加しました。`-O buildless_dependency_dir=<path>`を使用してターゲットディレクトリを設定します。
- Python
- `find_module`でインポートが見つからない場合に`KeyError`が発生するPython抽出のインポート処理のバグを修正しました。これは、GitHubユーザー@akoeplingerによるオープンソースCodeQLリポジトリへの寄稿です。
- 変更の完全なリストについては、バージョン2.23.7と2.23.8の完全な変更ログを参照してください。CodeQLの新しいバージョンはすべて、GitHub.comのGitHub Code ScanningおよびGitHub Code Qualityのユーザーに自動的にデプロイされます。これらのリリースで導入された機能と修正は、GitHub Enterprise Server（GHES）バージョン3.20に含まれます。古いバージョンのGHESを使用している場合は、CodeQLバージョンを手動でアップグレードできます。

## Key Changes
- Go
- `Secure`フラグが設定されていないクッキーを検出する新しいクエリ`go/cookie-secure-not-set`を追加しました。これにより機密情報の漏洩が発生する可能性があります。
- 壊れたまたは弱い暗号化アルゴリズムの使用を検出する新しいクエリ`go/weak-crypto-algorithm`を追加しました。
- 機密データに対する壊れたまたは弱い暗号化ハッシュアルゴリズムの使用を検出する新しいクエリ`go/weak-sensitive-data-hashing`を追加しました。
- `go/cookie-http-only-not-set`クエリが実験クエリパックから昇格し、`HttpOnly`フラグを使用しないクッキーを特定し、クロスサイトスクリプティングの脆弱性につながる可能性があります。このクエリは、GitHubユーザー@edvraaによって元々寄稿されました。
- Rust
- クロスサイトスクリプティングのセキュリティ脆弱性を検出する新しいクエリ`rust/xss`を追加しました。
- 無効化されたTLS証明書チェックを検出する新しいクエリ`rust/disabled-certificate-check`を追加しました。
- Rust用のCodeQLクエリの作成方法を学ぶのに役立つ3つのサンプルクエリ（`rust/examples/empty-if`、`rust/examples/simple-sql-injection`、`rust/examples/simple-constant-password`）を追加しました。

## Impact / Who’s Affected
- `go/cookie-http-only-not-set`クエリが実験クエリパックから昇格し、`HttpOnly`フラグを使用しないクッキーを特定し、クロスサイトスクリプティングの脆弱性につながる可能性があります。
- 文字列の固定長のプレフィックスまたはサフィックスのみを抽出する操作（Javaの`substring`やKotlinの`take`など）は、7文字以下に制限されている場合、`java/sensitive-log`クエリのサニタイザーとして扱われます。これは、ログメッセージの内容が切り捨てられるためです。

## Caveats / Limitations
- `go/cookie-http-only-not-set`クエリが実験クエリパックから昇格し、`HttpOnly`フラグを使用しないクッキーを特定し、クロスサイトスクリプティングの脆弱性につながる可能性があります。
- 文字列の固定長のプレフィックスまたはサフィックスのみを抽出する操作（Javaの`substring`やKotlinの`take`など）は、7文字以下に制限されている場合、`java/sensitive-log`クエリのサニタイザーとして扱われます。これは、ログメッセージの内容が切り捨てられるためです。

## Article Content (cleaned)
CodeQLは、GitHubの[Code Scanning](https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql)および[Code Quality](https://docs.github.com/code-security/code-quality/concepts/about-code-quality)製品の背後にある静的解析エンジンで、コード品質とセキュリティに関する問題を発見して修正します。最近、[CodeQL 2\.23\.7と2\.23\.8](https://codeql.github.com/docs/codeql-overview/codeql-changelog/)をリリースしました。これらのリリースは、GoとRustの新しいセキュリティクエリ、全体的な分析精度の向上、複数の言語にわたるフレームワークの更新をもたらします。


## [Query changes](#query-changes)


**Go**


* `Secure`フラグが設定されていないクッキーを検出する新しいクエリ`go/cookie-secure-not-set`を追加しました。これにより機密情報の漏洩が発生する可能性があります。
* 壊れたまたは弱い暗号化アルゴリズムの使用を検出する新しいクエリ`go/weak-crypto-algorithm`を追加しました。
* 機密データに対する壊れたまたは弱い暗号化ハッシュアルゴリズムの使用を検出する新しいクエリ`go/weak-sensitive-data-hashing`を追加しました。
* `go/cookie-http-only-not-set`クエリが実験クエリパックから昇格し、`HttpOnly`フラグを使用しないクッキーを特定し、クロスサイトスクリプティングの脆弱性につながる可能性があります。このクエリは、GitHubユーザー@edvraaによって元々寄稿されました。


**Rust**


* クロスサイトスクリプティングのセキュリティ脆弱性を検出する新しいクエリ`rust/xss`を追加しました。
* 無効化されたTLS証明書チェックを検出する新しいクエリ`rust/disabled-certificate-check`を追加しました。
* Rust用のCodeQLクエリの作成方法を学ぶのに役立つ3つのサンプルクエリ（`rust/examples/empty-if`、`rust/examples/simple-sql-injection`、`rust/examples/simple-constant-password`）を追加しました。


## [Language and framework support](#language-and-framework-support)


**Java/Kotlin**


* Java分析は、Mavenビルドで`--source`および`--target`コンパイラフラグを強制しなくなりました。Mavenはプロジェクト独自のコンパイラ設定を使用するようになり、ビルドの互換性が向上します。
* 文字列の固定長のプレフィックスまたはサフィックスのみを抽出する操作（Javaの`substring`やKotlinの`take`など）は、7文字以下に制限されている場合、`java/sensitive-log`クエリのサニタイザーとして扱われます。これは、ログメッセージの内容が切り捨てられるためです。


**JavaScript/TypeScript**


* `app/pages`フォルダーのサーバーサイドテイントソースを分析が見逃す原因となっていたNext.jsモデルのバグを修正しました。


**Rust**


* `rust/access-invalid-pointer`クエリが新しいフローソースとバリアで改善されました。


**C\#**


* [ビルドレス分析](https://docs.github.com/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#codeql-build-modes)（デフォルトで使用）を使用する場合、コンパイルエラーがデバッグログに含まれるようになりました。
* ビルドレスモードで依存関係のダウンロード用のカスタムディレクトリを指定する新しい抽出オプションを追加しました。`-O buildless_dependency_dir=<path>`を使用してターゲットディレクトリを設定します。


**Python**


* `find_module`でインポートが見つからない場合に`KeyError`が発生するPython抽出のインポート処理のバグを修正しました。これは、GitHubユーザー@akoeplingerによる[オープンソースCodeQLリポジトリへの寄稿](https://github.com/github/codeql/pull/20908)です。




---


変更の完全なリストについては、バージョン[2\.23\.7](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.7/)と[2\.23\.8](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.8/)の完全な変更ログを参照してください。CodeQLの新しいバージョンはすべて、GitHub.comのGitHub Code ScanningおよびGitHub Code Qualityのユーザーに自動的にデプロイされます。これらのリリースで導入された機能と修正は、GitHub Enterprise Server（GHES）バージョン3\.20に含まれます。古いバージョンのGHESを使用している場合は、[CodeQLバージョンを手動でアップグレード](https://docs.github.com/enterprise-server@3.18/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access)できます。
