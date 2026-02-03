---
title: "シークレットスキャニングが秘密鍵の検出を改善、Sentry パターン名を更新"
date: "2025-11-12"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-12-secret-scanning-improves-private-key-detection"
fetched_at: "2026-02-03T14:50:55.330837Z"
lang: "ja"
---

# シークレットスキャニングが秘密鍵の検出を改善、Sentry パターン名を更新

## Overview
リポジトリで暗号化資格情報が露出するリスクを減らすため、シークレットスキャニングは追加の秘密鍵フォーマットを検出し、既存の秘密鍵検出器をアップグレードしました。

## Detailed Explanation
### 概要
- リポジトリで暗号化資格情報が露出するリスクを減らすため、シークレットスキャニングは追加の秘密鍵フォーマットを検出し、既存の秘密鍵検出器をアップグレードしました。
- さらに、Sentry トークン名は、Sentry のトークン命名規則の変更に合わせて更新されました。

### 追加された新しいパターン
- シークレットスキャニングは、以下の追加の秘密鍵フォーマットを検出するようになりました。
- 汎用秘密鍵パターンは、PKCS#8 フォーマットの RSA 鍵と、標準の BEGIN PRIVATE KEY ヘッダーを使用する他の秘密鍵を検出します。このパターンは、重複アラートを回避するために GitHub 秘密鍵を自動的にフィルタリングします。

### 検出器の改善
- 今週から、以下の秘密鍵パターンは、構成ファイルや環境変数の一般的なフォーマットであるエスケープされた改行 ( \n ) を含む鍵も検出するようになります。

### シークレットタイプの名前変更
- Sentry は最近、トークンタイプ全体で命名規則の変更を展開しました。これらの変更に合わせて、以下のシークレットタイプの名前が変更されます。
- 非プロバイダーシークレットパターンとシークレットスキャニングについて詳しく知る。

## Key Changes
- 今週から、以下の秘密鍵パターンは、構成ファイルや環境変数の一般的なフォーマットであるエスケープされた改行 ( \n ) を含む鍵も検出するようになります。

## Insights (derived from article language)
- シークレットタイプ（新） スラッグ（新） シークレットタイプ（旧） スラッグ（旧） Sentry Organization Token sentry_organization_token Sentry Org Auth Token sentry_org_auth_token Sentry Personal Token sentry_personal_token Sentry User Auth Token sentry_user_auth_token 非プロバイダーシークレットパターンとシークレットスキャニングについて詳しく知る。

## Article Content (cleaned)
リポジトリで暗号化資格情報が露出するリスクを減らすため、シークレットスキャニングは追加の秘密鍵フォーマットを検出し、既存の秘密鍵検出器をアップグレードしました。


さらに、Sentry トークン名は、Sentry のトークン命名規則の変更に合わせて更新されました。


## [New patterns added](#new-patterns-added)


シークレットスキャニングは、以下の追加の秘密鍵フォーマットを検出するようになりました。




| シークレットタイプ | 検出されるフォーマット |
| --- | --- |
| `ec_private_key` | 楕円曲線秘密鍵 |
| `generic_private_key` | 汎用 PKCS#8 秘密鍵 |


汎用秘密鍵パターンは、PKCS#8 フォーマットの RSA 鍵と、標準の `BEGIN PRIVATE KEY` ヘッダーを使用する他の秘密鍵を検出します。このパターンは、重複アラートを回避するために GitHub 秘密鍵を自動的にフィルタリングします。


## [Detector improvements](#detector-improvements)


今週から、以下の秘密鍵パターンは、構成ファイルや環境変数の一般的なフォーマットであるエスケープされた改行 (`\n`) を含む鍵も検出するようになります。




| シークレットタイプ |
| --- |
| `ec_private_key` |
| `github_ssh_private_key` |
| `openssh_private_key` |
| `rsa_private_key` |


## [Secret types renamed](#secret-types-renamed)


Sentry は最近、トークンタイプ全体で命名規則の変更を展開しました。これらの変更に合わせて、以下のシークレットタイプの名前が変更されます。




| シークレットタイプ（新） | スラッグ（新） | シークレットタイプ（旧） | スラッグ（旧） |
| --- | --- | --- | --- |
| Sentry Organization Token | `sentry_organization_token` | Sentry Org Auth Token | `sentry_org_auth_token` |
| Sentry Personal Token | `sentry_personal_token` | Sentry User Auth Token | `sentry_user_auth_token` |


[非プロバイダーシークレットパターン](https://docs.github.com/enterprise-cloud@latest/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#non-provider-patterns)と[シークレットスキャニング](https://docs.github.com/code-security/secret-scanning/introduction/about-secret-scanning)について詳しく知る。
