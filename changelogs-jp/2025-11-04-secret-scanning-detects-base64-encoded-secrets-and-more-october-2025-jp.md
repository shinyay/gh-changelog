---
title: "シークレットスキャンが Base64 エンコードされたシークレットを検出 — 2025年10月"
date: "2025-11-04"
type: "new releases"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-04-secret-scanning-now-detects-base64-encoded-secrets"
fetched_at: "2026-02-03T14:50:55.459294Z"
lang: "ja"
---

# シークレットスキャンが Base64 エンコードされたシークレットを検出 — 2025年10月

## Overview
GitHub シークレットスキャンは、新しいシークレットタイプのサポートを継続的に追加しています。10月に以下の更新が行われました。

## Detailed Explanation
### シークレットスキャン — 2025年10月
- GitHub シークレットスキャンは、新しいシークレットタイプのサポートを継続的に追加しています。10月に以下の更新が行われました。
- Base64 エンコードされたシークレット：シークレットスキャンが、サードパーティクラウドプロバイダーからのシークレットタイプの Base64 エンコード版を検出するようになりました。
- 拡張メタデータチェック：シークレットスキャンが、所有者情報、作成日、シークレットに関する組織の詳細などの追加コンテキストのチェックをサポートするようになりました。
- 有効性チェック：シークレットスキャンが Grafana と Notion の有効性チェックサポートを追加しました。

### Base64 エンコードされたシークレット検出
- GitHub シークレットスキャンが、サードパーティプロバイダーからのシークレットタイプに対して、Base64 形式で難読化されたシークレットを検出および防止するようになりました。
- Base64 エンコードされたシークレットはデフォルトでプッシュ保護されます。GitHub は、追加のタイプのサポートを順次追加していきます。

### 拡張メタデータチェック
- GitHub Universe 2025 で発表されたように、以下のシークレットタイプが拡張メタデータチェックをサポートするようになりました。

### 有効性チェック
- 以下のシークレットタイプに、検出されたシークレットがアクティブかどうかを確認する有効性チェックが含まれるようになりました。
- シークレットスキャンの詳細と、サポートされているシークレットの完全なリストについては、製品ドキュメントをご覧ください。

## Insights (derived from article language)
- プロバイダー シークレットタイプ Grafana grafana_cloud_api_token Notion notion_api_token シークレットスキャンの詳細と、サポートされているシークレットの完全なリストについては、製品ドキュメントをご覧ください。

## Article Content (cleaned)
## [シークレットスキャン — 2025年10月](#secret-scanning-october-2025)


GitHub シークレットスキャンは、新しいシークレットタイプのサポートを継続的に追加しています。10月に以下の更新が行われました。


* **Base64 エンコードされたシークレット**：シークレットスキャンが、サードパーティクラウドプロバイダーからのシークレットタイプの Base64 エンコード版を検出するようになりました。
* **拡張メタデータチェック**：シークレットスキャンが、所有者情報、作成日、シークレットに関する組織の詳細などの追加コンテキストのチェックをサポートするようになりました。
* **有効性チェック**：シークレットスキャンが Grafana と Notion の有効性チェックサポートを追加しました。


### [Base64 エンコードされたシークレット検出](#base64-encoded-secret-detection)


GitHub シークレットスキャンが、サードパーティプロバイダーからのシークレットタイプに対して、Base64 形式で難読化されたシークレットを検出および防止するようになりました。




| プロバイダー | シークレットタイプ |
| --- | --- |
| Alibaba | `alibaba_cloud_access_key_secret` |
| Amazon AWS | `aws_access_key_id` |
| Amazon AWS | `aws_secret_access_key` |
| Amazon AWS | `aws_temporary_access_key_id` |
| Anthropic | `anthropic_api_key` |
| Azure | `azure_cache_for_redis_access_key` |
| Azure | `azure_cosmosdb_key_identifiable` |
| Azure | `azure_function_key` |
| Azure | `azure_openai_key` |
| Azure | `azure_storage_account_key` |
| Brevo | `sendinblue_api_key` |
| Databricks | `databricks_access_token` |
| GitHub Secret Scanning | `secret_scanning_sample_token` |
| GitLab | `gitlab_access_token` |
| Google | `google_oauth_client_id` |
| Google | `google_oauth_client_secret` |
| Google | `google_oauth_refresh_token` |
| Groq | `groq_api_key` |
| Hugging Face | `hf_user_access_token` |
| JFrog | `jfrog_platform_reference_token` |
| Twilio | `twilio_account_sid` |


Base64 エンコードされたシークレットはデフォルトでプッシュ保護されます。GitHub は、追加のタイプのサポートを順次追加していきます。


## [拡張メタデータチェック](#extended-metadata-checks)


[GitHub Universe 2025 で発表された](https://github.blog/changelog/2025-10-28-introducing-extended-metadata-checks-for-secret-scanning/)ように、以下のシークレットタイプが拡張メタデータチェックをサポートするようになりました。




| プロバイダー | シークレットタイプ |
| --- | --- |
| Adafruit | `adafruit_io_key` |
| Anthropic | `anthropic_api_key` |
| Apify | `apify_api_token` |
| Contentful | `contentful_personal_access_token` |
| Discord | `discord_bot_token` |
| Dropbox | `dropbox_access_token` |
| Dropbox | `dropbox_short_lived_access_token` |
| Fastly | `fastly_api_token` |
| Figma | `figma_pat` |
| GitLab | `gitlab_access_token` |
| Google | `google_oauth_access_token` |
| Hugging Face | `hf_user_access_token` |
| Intercom | `intercom_access_token` |
| Mailchimp | `mailchimp_api_key` |
| Mailgun | `mailgun_api_key` |
| Mailgun | `mailgun_smtp_credential` |
| Mapbox | `mapbox_secret_access_token` |
| Notion | `notion_integration_token` |
| OpenAI | `openai_api_key` |
| Postman | `postman_api_key` |
| SendGrid | `sendgrid_api_key` |
| Slack | `slack_api_token` |
| Slack | `slack_incoming_webhook_url` |
| Slack | `slack_workflow_webhook_url` |
| Stripe | `stripe_api_key` |
| Stripe | `stripe_test_secret_key` |
| Tailscale | `tailscale_api_key` |
| Telegram | `telegram_bot_token` |
| Terraform Cloud | `terraform_api_token` |


## [有効性チェック](#validity-checks)


以下のシークレットタイプに、検出されたシークレットがアクティブかどうかを確認する有効性チェックが含まれるようになりました。




| プロバイダー | シークレットタイプ |
| --- | --- |
| Grafana | `grafana_cloud_api_token` |
| Notion | `notion_api_token` |


[シークレットスキャン](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning?utm_source=changelog-docs-extended-metadata-checks&utm_medium=changelog&utm_campaign=universe25)の詳細と、[サポートされているシークレットの完全なリスト](https://docs.github.com/code-security/secret-scanning/introduction/supported-secret-scanning-patterns)については、製品ドキュメントをご覧ください。
