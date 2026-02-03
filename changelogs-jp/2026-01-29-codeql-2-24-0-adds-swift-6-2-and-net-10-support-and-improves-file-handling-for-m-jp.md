---
title: "CodeQL 2.24.0でSwift 6.2と.NET 10のサポートが追加され、縮小化されたJavaScriptのファイル処理が改善"
date: "2026-01-29"
type: "Improvement"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-29-codeql-2-24-0-adds-swift-6-2-support-net-10-compatibility-and-file-handling-for-minified-javascript"
fetched_at: "2026-02-03T14:50:49.253622Z"
lang: "ja"
---

# CodeQL 2.24.0でSwift 6.2と.NET 10のサポートが追加され、縮小化されたJavaScriptのファイル処理が改善

## Overview
CodeQLは、コード内のセキュリティ問題を発見して修正するGitHubコードスキャニングの背後にある静的解析エンジンです。最近、CodeQL 2.24.0をリリースしました。これは、新しい言語バージョンのサポートを追加し、フレームワークのカバレッジを拡大し、複数の言語でクエリの精度を向上させます。

## Detailed Explanation
### 概要
- CodeQLは、コード内のセキュリティ問題を発見して修正するGitHubコードスキャニングの背後にある静的解析エンジンです。最近、CodeQL 2.24.0をリリースしました。これは、新しい言語バージョンのサポートを追加し、フレームワークのカバレッジを拡大し、複数の言語でクエリの精度を向上させます。

### 言語とフレームワークのサポート
- Swift
- Swift 6.2.2および6.2.3でビルドされたアプリの分析をサポートするようにCodeQLを更新しました。
- C#
- .NET 10およびC# 14のサポートを追加しました。
- JavaScript/TypeScript
- CodeQLは、平均行長が200を超えるJavaScriptファイルを縮小化されたものとして扱い、分析しなくなりました。縮小化されたJavaScriptファイルを分析する必要があるシナリオでは、環境変数CODEQL_EXTRACTOR_JAVASCRIPT_ALLOW_MINIFIED_FILES=trueを設定できます。
- Next.js 16のuse cacheディレクティブのサポートを追加しました。
- React useRefフックのサポートを追加し、currentプロパティを介した改善されたデータフロー追跡を提供します。
- Python
- py/decompression-bombクエリがcompression.zstdライブラリ（Python 3.14で追加）をサポートするようになりました。
- urllib.parseのtaintフローモデルとpython-socketioパッケージのリモートフローソースを追加しました。
- エクストラクタは、デフォルトで非表示ディレクトリ内のファイルを分析するようになりました。
- Java/Kotlin
- SQL injectionとhardcoded credentialsクエリをサポートするcom.couchbaseのシンクモデルを追加しました。
- org.apache.commons.fileupload.FileItem、javax/jakarta.servlet.http.Part、org.apache.commons.fileupload.util.Streamsのより多くのデータフローモデルを追加しました。
- C/C++
- ファイル読み取り関数、コマンドラインおよび環境変数API、SQLiteおよびOpenSSLライブラリのフローモデルを含む、より多くのWindows APIのサポートを追加しました。
- Rust
- メソッド解決がDerefトレイトを考慮するようになりました。これは、Derefトレイトを実装するレシーバーのメソッド呼び出しが、ターゲットタイプで定義されたメソッドに正しく解決されることを意味します。
- Axum Webアプリケーションフレームワークのサポートを追加しました。
- 生ポインタの型推論を改善しました。これには、生借用演算子の型推論と生ポインタの逆参照が含まれます。

### クエリの変更
- C#
- ASP.NET Coreをサポートするために、Missing cross-site request forgery token validationクエリを拡張しました。
- NHibernate.ISession.CreateSQLQuery、NHibernate.IStatelessSession.CreateSQLQuery、NHibernate.Impl.AbstractSessionImpl.CreateSQLQueryをSQL injectionシンクとして追加しました。
- taint-trackingシンクと追加のtaintステップへの入力で、System.Collections.Generic.KeyValuePair.Valueの暗黙的な読み取りを追加しました。その結果、コンテナがtaintされている場合、taint-trackingクエリはより多くの結果を生成するようになります。
- JavaScript/TypeScript
- Next.jsモデルのバグを修正しました。このバグにより、apiおよびpagesフォルダの外に表示されるrouteまたはpageという名前のファイルのサーバー側taintソースが分析で見逃されていました。
- content-typeヘッダーが設定されていない場合、new Response(x)はreflected XSSシンクとして見なされなくなりました。これは、コンテンツタイプがデフォルトでtext/plainになるためです。
- Java/Kotlin
- Javaスレッドセーフティ解析が、コンストラクタ内のスレッドセーフクラスへの初期化を理解するようになりました。
- 正規表現チェックが値が安全であることを検証する場合にアラートを削除するために、java/ssrfにサニタイザを追加しました。
- すべてのSpring RestTemplateメソッドのURIテンプレート変数がrequest forgeryシンクと見なされるようになりました。これにより、java/ssrfクエリでより多くのアラートが発生する可能性があります。
- C/C++
- cpp/constant-comparisonクエリの精度を向上させて、偽陽性を減らしました。
- Rust
- rust/unused-variable、rust/unused-value、rust/access-invalid-pointer、rust/access-after-lifetime-endedクエリの精度を向上させて、偽陽性を減らしました。
- rust/hard-coded-cryptographic-valueクエリを拡張して、パスワード、初期化ベクトル、ノンス、ソルトを識別する新しいヒューリスティックシンクを追加しました。
- 変更の完全なリストについては、バージョン2.24.0の完全なchangelogを参照してください。CodeQLの新しいバージョンはすべて、github.comのGitHubコードスキャニングのユーザーに自動的にデプロイされます。CodeQL 2.24.0の新機能は、将来のGitHub Enterprise Server（GHES）リリースにも含まれる予定です。古いバージョンのGHESを使用している場合は、CodeQLバージョンを手動でアップグレードできます。

## Key Changes
- C#
- ASP.NET Coreをサポートするために、Missing cross-site request forgery token validationクエリを拡張しました。
- NHibernate.ISession.CreateSQLQuery、NHibernate.IStatelessSession.CreateSQLQuery、NHibernate.Impl.AbstractSessionImpl.CreateSQLQueryをSQL injectionシンクとして追加しました。
- taint-trackingシンクと追加のtaintステップへの入力で、System.Collections.Generic.KeyValuePair.Valueの暗黙的な読み取りを追加しました。その結果、コンテナがtaintされている場合、taint-trackingクエリはより多くの結果を生成するようになります。
- JavaScript/TypeScript
- Next.jsモデルのバグを修正しました。このバグにより、apiおよびpagesフォルダの外に表示されるrouteまたはpageという名前のファイルのサーバー側taintソースが分析で見逃されていました。
- content-typeヘッダーが設定されていない場合、new Response(x)はreflected XSSシンクとして見なされなくなりました。これは、コンテンツタイプがデフォルトでtext/plainになるためです。
- Java/Kotlin
- Javaスレッドセーフティ解析が、コンストラクタ内のスレッドセーフクラスへの初期化を理解するようになりました。
- 正規表現チェックが値が安全であることを検証する場合にアラートを削除するために、java/ssrfにサニタイザを追加しました。
- すべてのSpring RestTemplateメソッドのURIテンプレート変数がrequest forgeryシンクと見なされるようになりました。これにより、java/ssrfクエリでより多くのアラートが発生する可能性があります。
- C/C++
- cpp/constant-comparisonクエリの精度を向上させて、偽陽性を減らしました。
- Rust
- rust/unused-variable、rust/unused-value、rust/access-invalid-pointer、rust/access-after-lifetime-endedクエリの精度を向上させて、偽陽性を減らしました。
- rust/hard-coded-cryptographic-valueクエリを拡張して、パスワード、初期化ベクトル、ノンス、ソルトを識別する新しいヒューリスティックシンクを追加しました。
- 変更の完全なリストについては、バージョン2.24.0の完全なchangelogを参照してください。CodeQLの新しいバージョンはすべて、github.comのGitHubコードスキャニングのユーザーに自動的にデプロイされます。CodeQL 2.24.0の新機能は、将来のGitHub Enterprise Server（GHES）リリースにも含まれる予定です。古いバージョンのGHESを使用している場合は、CodeQLバージョンを手動でアップグレードできます。

## Insights (derived from article language)
- Rust メソッド解決がDerefトレイトを考慮するようになりました。これは、Derefトレイトを実装するレシーバーのメソッド呼び出しが、ターゲットタイプで定義されたメソッドに正しく解決されることを意味します。
- すべてのSpring RestTemplateメソッドのURIテンプレート変数がrequest forgeryシンクと見なされるようになりました。これにより、java/ssrfクエリでより多くのアラートが発生する可能性があります。

## Article Content (cleaned)
CodeQLは、[GitHubコードスキャニング](https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql)の背後にある静的解析エンジンです。これは、コード内のセキュリティ問題を発見して修正します。最近、[CodeQL 2\.24\.0](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.24.0/)をリリースしました。これは、新しい言語バージョンのサポートを追加し、フレームワークのカバレッジを拡大し、複数の言語でクエリの精度を向上させます。


## [Language and framework support](https://github.blog/changelog/feed/#language-and-framework-support)


**Swift**


* Swift 6\.2\.2および6\.2\.3でビルドされたアプリの分析をサポートするようにCodeQLを更新しました。


**C\#**


* .NET 10およびC\# 14のサポートを追加しました。


**JavaScript/TypeScript**


* CodeQLは、平均行長が200を超えるJavaScriptファイルを縮小化されたものとして扱い、分析しなくなりました。縮小化されたJavaScriptファイルを分析する必要があるシナリオでは、環境変数`CODEQL_EXTRACTOR_JAVASCRIPT_ALLOW_MINIFIED_FILES=true`を設定できます。
* Next.js 16の`use cache`ディレクティブのサポートを追加しました。
* React `useRef`フックのサポートを追加し、`current`プロパティを介した改善されたデータフロー追跡を提供します。


**Python**


* `py/decompression-bomb`クエリが`compression.zstd`ライブラリ（Python 3\.14で追加）をサポートするようになりました。
* `urllib.parse`のtaintフローモデルと`python-socketio`パッケージのリモートフローソースを追加しました。
* エクストラクタは、デフォルトで非表示ディレクトリ内のファイルを分析するようになりました。


**Java/Kotlin**


* SQL injectionとhardcoded credentialsクエリをサポートする`com.couchbase`のシンクモデルを追加しました。
* `org.apache.commons.fileupload.FileItem`、`javax/jakarta.servlet.http.Part`、`org.apache.commons.fileupload.util.Streams`のより多くのデータフローモデルを追加しました。


**C/C\+\+**


* ファイル読み取り関数、コマンド\-ラインおよび環境変数API、SQLiteおよびOpenSSLライブラリのフローモデルを含む、より多くのWindows APIのサポートを追加しました。


**Rust**


* メソッド解決が`Deref`トレイトを考慮するようになりました。これは、`Deref`トレイトを実装するレシーバーのメソッド呼び出しが、ターゲットタイプで定義されたメソッドに正しく解決されることを意味します。
* Axum Webアプリケーションフレームワークのサポートを追加しました。
* 生ポインタの型推論を改善しました。これには、生借用演算子の型推論と生ポインタの逆参照が含まれます。


## [Query changes](https://github.blog/changelog/feed/#query-changes)


**C\#**


* ASP.NET Coreをサポートするために、`Missing cross-site request forgery token validation`クエリを拡張しました。
* `NHibernate.ISession.CreateSQLQuery`、`NHibernate.IStatelessSession.CreateSQLQuery`、`NHibernate.Impl.AbstractSessionImpl.CreateSQLQuery`をSQL injectionシンクとして追加しました。
* taint\-trackingシンクと追加のtaintステップへの入力で、`System.Collections.Generic.KeyValuePair.Value`の暗黙的な読み取りを追加しました。その結果、コンテナがtaintされている場合、taint\-trackingクエリはより多くの結果を生成するようになります。


**JavaScript/TypeScript**


* Next.jsモデルのバグを修正しました。このバグにより、`api`および`pages`フォルダの外に表示される`route`または`page`という名前のファイルのサーバー\-側taintソースが分析で見逃されていました。
* `content-type`ヘッダーが設定されていない場合、`new Response(x)`はreflected XSSシンクとして見なされなくなりました。これは、コンテンツタイプがデフォルトで`text/plain`になるためです。


**Java/Kotlin**


* Javaスレッドセーフティ解析が、コンストラクタ内のスレッド\-セーフクラスへの初期化を理解するようになりました。
* 正規表現チェックが値が安全であることを検証する場合にアラートを削除するために、`java/ssrf`にサニタイザを追加しました。
* すべてのSpring `RestTemplate`メソッドのURIテンプレート変数がrequest forgeryシンクと見なされるようになりました。これにより、`java/ssrf`クエリでより多くのアラートが発生する可能性があります。


**C/C\+\+**


* `cpp/constant-comparison`クエリの精度を向上させて、偽陽性を減らしました。


**Rust**


* `rust/unused-variable`、`rust/unused-value`、`rust/access-invalid-pointer`、`rust/access-after-lifetime-ended`クエリの精度を向上させて、偽陽性を減らしました。
* `rust/hard-coded-cryptographic-value`クエリを拡張して、パスワード、初期化ベクトル、ノンス、ソルトを識別する新しいヒューリスティックシンクを追加しました。


変更の完全なリストについては、[バージョン2\.24\.0の完全なchangelog](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.24.0/)を参照してください。CodeQLの新しいバージョンはすべて、github.comのGitHubコードスキャニングのユーザーに自動的にデプロイされます。CodeQL 2\.24\.0の新機能は、将来のGitHub Enterprise Server（GHES）リリースにも含まれる予定です。古いバージョンのGHESを使用している場合は、[CodeQLバージョンを手動でアップグレード](https://docs.github.com/enterprise-server@3.19/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access)できます。
