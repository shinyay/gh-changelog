---
title: "Secret scanningアップデート — 2025年11月"
date: "2025-12-02"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-02-secret-scanning-updates-november-2025"
fetched_at: "2026-02-03T14:50:55.119892Z"
lang: "ja"
---

# Secret scanningアップデート — 2025年11月

## Overview
GitHubのsecret scanningは、新しいシークレットタイプのサポートを継続的に追加しています。11月に行われた以下の更新内容をご紹介します。

## Detailed Explanation
### Overview
- GitHubのsecret scanningは、新しいシークレットタイプのサポートを継続的に追加しています。11月に行われた以下の更新内容をご紹介します。
- 新しいプロバイダーパターン：Secret scanningは、Azure、Databricks、Microsoft、Paddle、PostHogなどのプロバイダーから24の新しいシークレットタイプを追加しました。
- 改善されたプライベートキー検出：Elliptic Curveおよび汎用PKCS#8プライベートキーの新しいパターンと、エスケープされた改行の検出が改善されました。
- 拡張メタデータ：Discordの`discord_bot_token`が拡張メタデータチェックをサポートするようになりました。
- 有効性チェック：AWS Access Key IDの検証が改善されました。
- 非公開gist：非公開GitHubリスト内のシークレットが、secret scanningパートナーに報告されるようになりました。

### 追加された新しいパターン
- 今月、以下の新しいパターンを追加しました。Secret scanningは、リポジトリ内のこれらのパターンに一致するシークレットを自動的に検出します。

### 追加されたプライベートキーパターン
- 11月12日に発表されたとおり、secret scanningは追加のプライベートキー形式を検出するようになりました：
- 他の汎用パターンと同様に、両方のタイプをプッシュ保護に含めるように構成できますが、デフォルトでは含まれていません。

### ディテクターのアップグレードと改善
- 以下のプライベートキーパターンは、構成ファイルや環境変数で一般的な形式であるエスケープされた改行（`\n`）を含むキーも検出するようになりました：
- ec_private_key
- github_ssh_private_key
- openssh_private_key
- rsa_private_key
- Sentryトークンタイプも、Sentryの更新された命名規則に合わせて名前が変更されました：
- 以下のシークレットタイプは拡張メタデータチェックをサポートするようになり、所有者情報、作成日、組織の詳細などの追加コンテキストを提供します。
- 以下のタイプの有効性チェックをアップグレードしました。AWS Access Key IDの検証の最近の改善により、ほとんどのお客様は、以前「不明」とラベル付けされていたアラートが「有効」または「無効」に切り替わるのを確認できます。

### パートナー通知の更新
- 11月25日に発表されたとおり、非公開GitHubリスト内で見つかったシークレットは、secret scanningパートナーに報告されるようになりました。非公開gistはURLを持つ誰でもアクセスできるため、gist内で漏洩したシークレットは他の公開された認証情報と同様に扱う必要があります。
- Secret scanningの詳細とサポートされているシークレットの完全なリストについては、製品ドキュメントをご覧ください。

## Key Changes
- 以下のプライベートキーパターンは、構成ファイルや環境変数で一般的な形式であるエスケープされた改行（`\n`）を含むキーも検出するようになりました：
- ec_private_key
- github_ssh_private_key
- openssh_private_key
- rsa_private_key
- Sentryトークンタイプも、Sentryの更新された命名規則に合わせて名前が変更されました：
- 以下のシークレットタイプは拡張メタデータチェックをサポートするようになり、所有者情報、作成日、組織の詳細などの追加コンテキストを提供します。
- 以下のタイプの有効性チェックをアップグレードしました。AWS Access Key IDの検証の最近の改善により、ほとんどのお客様は、以前「不明」とラベル付けされていたアラートが「有効」または「無効」に切り替わるのを確認できます。

## Impact / Who’s Affected
- プロバイダー シークレットタイプ パートナー ユーザー プッシュ保護 Azure azure_immersive_reader_key ✓ ✓ ✓ (設定可能) Azure azure_logic_apps_url ✓ ✓ ✓ (設定可能) crates.io cratesio_api_token ✓ ✓ ✓ (設定可能) Databricks databricks_account_session_token ✓ ✓ ✓ (設定可能) Databricks databricks_federated_account_session_token ✓ ✓ ✓ (設定可能) Databricks databricks_oauth_code ✓ ✓ ✓ (設定可能) Databricks databricks_oauth_refresh_token ✓ ✓ ✓ (設定可能) Databricks databricks_oauth_secret_token ✓ ✓ ✓ (設定可能) Databricks databricks_oauth_single_use_refresh_token_child ✓ ✓ ✓ (設定可能) Databricks databricks_oauth_single_use_refresh_token_parent ✓ ✓ ✓ (設定可能) Databricks databricks_scoped_api_token ✓ ✓ ✓ (設定可能) Databricks databricks_scoped_internal_token ✓ ✓ ✓ (設定可能) Databricks databricks_token ✓ ✓ ✓ (設定可能) Databricks databricks_workspace_session_token ✓ ✓ ✓ (設定可能) Microsoft power_automate_webhook_sas ✓ ✓ ✓ (設定可能) OneSignal onesignal_rich_authentication_token ✓ ✓ ✓ (設定可能) Paddle paddle_api_key ✓ ✓ ✓ (設定可能) Paddle paddle_sandbox_api_key ✓ ✓ ✓ (設定可能) Pineapple Technologies Limited pineapple_technologies_incident_api_key ✓ ✓ ✓ (設定可能) PostHog posthog_feature_flags_secure_api_key ✓ ✓ (設定可能) PostHog posthog_personal_api_key ✓ ✓ (設定可能) Rainforest Pay rainforest_api_key ✓ ✓ ✓ (設定可能) Rainforest Pay rainforest_sandbox_api_key ✓ ✓ ✓ (設定可能) Raycast raycast_access_token ✓ ✓ ✓ (設定可能) 追加されたプライベートキーパターン 11月12日に発表されたとおり、secret scanningは追加のプライベートキー形式を検出するようになりました： プロバイダー シークレットタイプ 説明 Generic ec_private_key Elliptic Curveプライベートキー Generic generic_private_key 汎用PKCS#8プライベートキー 他の汎用パターンと同様に、両方のタイプをプッシュ保護に含めるように構成できますが、デフォルトでは含まれていません。

## Caveats / Limitations
- プロバイダー シークレットタイプ パートナー ユーザー プッシュ保護 Azure azure_immersive_reader_key ✓ ✓ ✓ (設定可能) Azure azure_logic_apps_url ✓ ✓ ✓ (設定可能) crates.io cratesio_api_token ✓ ✓ ✓ (設定可能) Databricks databricks_account_session_token ✓ ✓ ✓ (設定可能) Databricks databricks_federated_account_session_token ✓ ✓ ✓ (設定可能) Databricks databricks_oauth_code ✓ ✓ ✓ (設定可能) Databricks databricks_oauth_refresh_token ✓ ✓ ✓ (設定可能) Databricks databricks_oauth_secret_token ✓ ✓ ✓ (設定可能) Databricks databricks_oauth_single_use_refresh_token_child ✓ ✓ ✓ (設定可能) Databricks databricks_oauth_single_use_refresh_token_parent ✓ ✓ ✓ (設定可能) Databricks databricks_scoped_api_token ✓ ✓ ✓ (設定可能) Databricks databricks_scoped_internal_token ✓ ✓ ✓ (設定可能) Databricks databricks_token ✓ ✓ ✓ (設定可能) Databricks databricks_workspace_session_token ✓ ✓ ✓ (設定可能) Microsoft power_automate_webhook_sas ✓ ✓ ✓ (設定可能) OneSignal onesignal_rich_authentication_token ✓ ✓ ✓ (設定可能) Paddle paddle_api_key ✓ ✓ ✓ (設定可能) Paddle paddle_sandbox_api_key ✓ ✓ ✓ (設定可能) Pineapple Technologies Limited pineapple_technologies_incident_api_key ✓ ✓ ✓ (設定可能) PostHog posthog_feature_flags_secure_api_key ✓ ✓ (設定可能) PostHog posthog_personal_api_key ✓ ✓ (設定可能) Rainforest Pay rainforest_api_key ✓ ✓ ✓ (設定可能) Rainforest Pay rainforest_sandbox_api_key ✓ ✓ ✓ (設定可能) Raycast raycast_access_token ✓ ✓ ✓ (設定可能) 追加されたプライベートキーパターン 11月12日に発表されたとおり、secret scanningは追加のプライベートキー形式を検出するようになりました： プロバイダー シークレットタイプ 説明 Generic ec_private_key Elliptic Curveプライベートキー Generic generic_private_key 汎用PKCS#8プライベートキー 他の汎用パターンと同様に、両方のタイプをプッシュ保護に含めるように構成できますが、デフォルトでは含まれていません。

## Insights (derived from article language)
- Secret scanningの詳細とサポートされているシークレットの完全なリストについては、製品ドキュメントをご覧ください。

## Article Content (cleaned)
GitHubのsecret scanningは、新しいシークレットタイプのサポートを継続的に追加しています。11月に行われた以下の更新内容をご紹介します。


* **新しいプロバイダーパターン**：Secret scanningは、Azure、Databricks、Microsoft、Paddle、PostHogなどのプロバイダーから24の新しいシークレットタイプを追加しました。
* **改善されたプライベートキー検出**：Elliptic Curveおよび汎用PKCS\#8プライベートキーの新しいパターンと、エスケープされた改行の検出が改善されました。
* **拡張メタデータ**：Discordの`discord_bot_token`が拡張メタデータチェックをサポートするようになりました。
* **有効性チェック：** AWS Access Key IDの検証が改善されました。
* **非公開gist**：非公開GitHubリスト内のシークレットが、secret scanningパートナーに報告されるようになりました。


## [New patterns added](#new-patterns-added)


今月、以下の新しいパターンを追加しました。Secret scanningは、リポジトリ内のこれらのパターンに一致するシークレットを自動的に検出します。




| プロバイダー | シークレットタイプ | パートナー | ユーザー | プッシュ保護 |
| --- | --- | --- | --- | --- |
| Azure | `azure_immersive_reader_key` | ✓ | ✓ | ✓ (設定可能) |
| Azure | `azure_logic_apps_url` | ✓ | ✓ | ✓ (設定可能) |
| crates.io | `cratesio_api_token` | ✓ | ✓ | ✓ (設定可能) |
| Databricks | `databricks_account_session_token` | ✓ | ✓ | ✓ (設定可能) |
| Databricks | `databricks_federated_account_session_token` | ✓ | ✓ | ✓ (設定可能) |
| Databricks | `databricks_oauth_code` | ✓ | ✓ | ✓ (設定可能) |
| Databricks | `databricks_oauth_refresh_token` | ✓ | ✓ | ✓ (設定可能) |
| Databricks | `databricks_oauth_secret_token` | ✓ | ✓ | ✓ (設定可能) |
| Databricks | `databricks_oauth_single_use_refresh_token_child` | ✓ | ✓ | ✓ (設定可能) |
| Databricks | `databricks_oauth_single_use_refresh_token_parent` | ✓ | ✓ | ✓ (設定可能) |
| Databricks | `databricks_scoped_api_token` | ✓ | ✓ | ✓ (設定可能) |
| Databricks | `databricks_scoped_internal_token` | ✓ | ✓ | ✓ (設定可能) |
| Databricks | `databricks_token` | ✓ | ✓ | ✓ (設定可能) |
| Databricks | `databricks_workspace_session_token` | ✓ | ✓ | ✓ (設定可能) |
| Microsoft | `power_automate_webhook_sas` | ✓ | ✓ | ✓ (設定可能) |
| OneSignal | `onesignal_rich_authentication_token` | ✓ | ✓ | ✓ (設定可能) |
| Paddle | `paddle_api_key` | ✓ | ✓ | ✓ (設定可能) |
| Paddle | `paddle_sandbox_api_key` | ✓ | ✓ | ✓ (設定可能) |
| Pineapple Technologies Limited | `pineapple_technologies_incident_api_key` | ✓ | ✓ | ✓ (設定可能) |
| PostHog | `posthog_feature_flags_secure_api_key` |  | ✓ | ✓ (設定可能) |
| PostHog | `posthog_personal_api_key` |  | ✓ | ✓ (設定可能) |
| Rainforest Pay | `rainforest_api_key` | ✓ | ✓ | ✓ (設定可能) |
| Rainforest Pay | `rainforest_sandbox_api_key` | ✓ | ✓ | ✓ (設定可能) |
| Raycast | `raycast_access_token` | ✓ | ✓ | ✓ (設定可能) |


### [追加されたプライベートキーパターン](#private-key-patterns-added)


[11月12日に発表されたとおり](https://github.blog/changelog/2025-11-12-secret-scanning-improves-private-key-detection/)、secret scanningは追加のプライベートキー形式を検出するようになりました：




| プロバイダー | シークレットタイプ | 説明 |
| --- | --- | --- |
| Generic | `ec_private_key` | Elliptic Curveプライベートキー |
| Generic | `generic_private_key` | 汎用PKCS\#8プライベートキー |


他の汎用パターンと同様に、両方のタイプをプッシュ保護に含めるように構成できますが、デフォルトでは含まれていません。


## [Detector upgrades and improvements](#detector-upgrades-and-improvements)


以下のプライベートキーパターンは、構成ファイルや環境変数で一般的な形式であるエスケープされた改行（`\n`）を含むキーも検出するようになりました：


* `ec_private_key`
* `github_ssh_private_key`
* `openssh_private_key`
* `rsa_private_key`


Sentryトークンタイプも、Sentryの更新された命名規則に合わせて名前が変更されました：




| 以前の名前 | 新しい名前 |
| --- | --- |
| `sentry_organization_token` | `sentry_org_auth_token` |
| `sentry_personal_token` | `sentry_user_auth_token` |


以下のシークレットタイプは拡張メタデータチェックをサポートするようになり、所有者情報、作成日、組織の詳細などの追加コンテキストを提供します。




| プロバイダー | シークレットタイプ |
| --- | --- |
| Discord | `discord_bot_token` |


以下のタイプの有効性チェックをアップグレードしました。AWS Access Key IDの検証の最近の改善により、ほとんどのお客様は、以前「不明」とラベル付けされていたアラートが「有効」または「無効」に切り替わるのを確認できます。




| プロバイダー | パターン | 有効性 |
| --- | --- | --- |
| Amazon Web Services (AWS) | `aws_access_key_id` | ✓ |


## [Partner notification updates](#partner-notification-updates)


[11月25日に発表されたとおり](https://github.blog/changelog/2025-11-25-secrets-in-unlisted-github-gists-are-now-reported-to-secret-scanning-partners/)、非公開GitHubリスト内で見つかったシークレットは、secret scanningパートナーに報告されるようになりました。非公開gistはURLを持つ誰でもアクセスできるため、gist内で漏洩したシークレットは他の公開された認証情報と同様に扱う必要があります。


Secret scanningの詳細とサポートされているシークレットの完全なリストについては、[secret scanning](https://docs.github.com/code-security/secret-scanning/introduction/about-secret-scanning)および[サポートされているシークレットの完全なリスト](https://docs.github.com/code-security/secret-scanning/introduction/supported-secret-scanning-patterns)の製品ドキュメントをご覧ください。
