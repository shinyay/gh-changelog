---
title: "シークレットスキャンの拡張メタデータチェックの導入"
date: "2025-10-28"
type: "new releases"
labels: ["application security", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-introducing-extended-metadata-checks-for-secret-scanning"
fetched_at: "2026-02-03T14:50:55.618318Z"
lang: "ja"
---

# シークレットスキャンの拡張メタデータチェックの導入

## Overview
漏洩したシークレットの所有権と影響を把握しやすくするため、GitHub シークレットスキャンがサポートされているシークレットタイプの追加メタデータを表示するようになりました。

## Detailed Explanation
### Overview
- 漏洩したシークレットの所有権と影響を把握しやすくするため、GitHub シークレットスキャンがサポートされているシークレットタイプの追加メタデータを表示するようになりました。

### What's changing?
- シークレットスキャンはすでにほとんどのシークレットプロバイダーに対して妥当性チェックを実行し、検出されたシークレットがアクティブかどうかを検証しています。今回のアップデートは、サポートされているプロバイダーからの追加メタデータフィールドを含むように、これらのチェックを拡張します。
- サポートされているシークレットタイプのパブリックプレビューで利用可能になり、アラートはシークレットプロバイダーから情報が利用可能な場合、シークレットの所有者、シークレットの作成日と有効期限、プロジェクトまたは組織のコンテキストに関する詳細を表示するようになりました。
- たとえば、漏洩した OpenAI キーは、シークレット所有者の名前、メール、識別子に加えて、利用可能な場合は組織に関する情報も表示されます。これらの新しいメタデータキーは、既存の妥当性チェックを拡張してトリアージと修復のためのより実用的なコンテキストを提供し、開発チームとセキュリティチームがより迅速に露出を評価し、修復の優先順位を付けられるようにします。
- メタデータの利用可能性は、シークレットプロバイダー、トークンタイプ、さらには特定のシークレットによって異なる時点で異なる可能性があることに注意してください。GitHub はシークレットのメタデータを表示するために最善を尽くしますが、シークレットのすべてのメタデータキーが利用できるとは限りません。

### What secret types are supported?
- GitHub は段階的にさらなるシークレットタイプのサポートを継続的に追加します。以前に発表されたアクティブな GitHub トークンのサポートに加えて、メタデータチェックは現在、次のタイプでサポートされています:
- サポートされているシークレットの完全なリストを参照するか、アップデートについて GitHub changelog を確認してください。

### When is the analysis run for a given secret?
- GitHub は、シークレットがアクティブであることが確認され、サポートされているシークレットタイプのリストに含まれている場合、シークレットスキャンアラートに対して拡張メタデータチェックを実行します。さらに、管理者またはセキュリティマネージャーは、特定のリポジトリに対して拡張メタデータチェックを最初に有効にする必要があります。

### Where is metadata displayed?
- 拡張メタデータは、アラートの担当者や関連するセキュリティキャンペーンなどのアラートに関する追加情報と共に、アラートの右側に表示されます。

### Who can use this feature?
- 拡張メタデータチェックは、GitHub Secret Protection および GitHub Advanced Security のお客様向けに github.com でパブリックプレビューとして利用可能で、データレジデンシーを備えた GitHub Enterprise Cloud も含まれます。

### Get started with metadata checks
- この機能はリポジトリの設定ページから有効にできます。拡張チェックを有効にするには、妥当性チェックを有効にする必要があります。有効にすると、利用可能な場合、アクティブなシークレットのアラート詳細ビューに追加情報が表示されます。

### Learn more and share feedback
- シークレットスキャンでリポジトリを保護する方法の詳細を確認するか、シークレットスキャンと拡張メタデータチェックに関するフィードバックを共有してください。

## Impact / Who’s Affected
- サポートされているシークレットタイプに対して追加メタデータが表示されるようになりました
- シークレットの所有者、作成日、有効期限、組織コンテキストなどの情報を提供
- OpenAI、GitLab、Slack、Stripe など 27 種類以上のプロバイダーをサポート

## Caveats / Limitations
- GitHub Secret Protection および GitHub Advanced Security のお客様がパブリックプレビューで利用可能
- データレジデンシーを備えた GitHub Enterprise Cloud でも利用可能
- 管理者またはセキュリティマネージャーがリポジトリごとに有効化する必要があります

## Insights (derived from article language)
- メタデータの利用可能性は、シークレットプロバイダー、トークンタイプ、さらには特定のシークレットによって異なる時点で異なる可能性があります
- GitHub はシークレットのメタデータを表示するために最善を尽くしますが、すべてのメタデータキーが利用できるとは限りません

## Article Content (cleaned)
- 開発チームとセキュリティチームがより迅速に露出を評価し、修復の優先順位を付けられるようにします
- 妥当性チェックを有効にする必要があります

## Article Content (cleaned)
漏洩したシークレットの所有権と影響を把握しやすくするため、GitHub シークレットスキャンがサポートされているシークレットタイプの追加メタデータを表示するようになりました。


### [What's changing?](#whats-changing)


シークレットスキャンはすでにほとんどのシークレットプロバイダーに対して妥当性チェックを実行し、検出されたシークレットがアクティブかどうかを検証しています。今回のアップデートは、サポートされているプロバイダーからの追加メタデータフィールドを含むように、これらのチェックを拡張します。


サポートされているシークレットタイプのパブリックプレビューで利用可能になり、アラートはシークレットプロバイダーから情報が利用可能な場合、シークレットの所有者、シークレットの作成日と有効期限、プロジェクトまたは組織のコンテキストに関する詳細を表示するようになりました。


たとえば、漏洩した OpenAI キーは、シークレット所有者の名前、メール、識別子に加えて、利用可能な場合は組織に関する情報も表示されます。これらの新しいメタデータキーは、既存の妥当性チェックを拡張してトリアージと修復のためのより実用的なコンテキストを提供し、開発チームとセキュリティチームがより迅速に露出を評価し、修復の優先順位を付けられるようにします。


メタデータの利用可能性は、シークレットプロバイダー、トークンタイプ、さらには特定のシークレットによって異なる時点で異なる可能性があることに注意してください。GitHub はシークレットのメタデータを表示するために最善を尽くしますが、シークレットのすべてのメタデータキーが利用できるとは限りません。


### [What secret types are supported?](#what-secret-types-are-supported)


GitHub は段階的にさらなるシークレットタイプのサポートを継続的に追加します。以前に発表されたアクティブな GitHub トークンのサポートに加えて、メタデータチェックは現在、次のタイプでサポートされています:




| Provider | Token | Extended Metadata |
| --- | --- | --- |
| Adafruit | `ADAFRUIT_AIO_KEY` | ✅ |
| Anthropic | `ANTHROPIC_API_KEY` | ✅ |
| Apify | `APIFY_API_TOKEN` | ✅ |
| Contentful | `CONTENTFUL_PERSONAL_ACCESS_TOKEN` | ✅ |
| Discord | `DISCORD_API_TOKEN` | ✅ |
| Discord | `DISCORD_API_TOKEN_V2` | ✅ |
| Dropbox | `DROPBOX_OAUTH2_ACCESS_TOKEN` | ✅ |
| Dropbox | `DROPBOX_OAUTH2_SHORT_LIVED_ACCESS_TOKEN` | ✅ |
| Fastly | `FASTLY_API_TOKEN` | ✅ |
| Figma | `FIGMA_PAT` | ✅ |
| GitLab | `GITLAB_ACCESS_TOKEN` | ✅ |
| Google | `GOOGLE_OAUTH_ACCESS_TOKEN` | ✅ |
| Hugging Face | `HUGGING_FACE_USER_ACCESS_TOKEN` | ✅ |
| Intercom | `INTERCOM_ACCESS_TOKEN` | ✅ |
| Mailchimp | `MAILCHIMP_API` | ✅ |
| Mailgun | `MAILGUN` | ✅ |
| Mailgun | `MAILGUN_LEGACY` | ✅ |
| Mapbox | `MAPBOX_SECRET_ACCESS_TOKEN` | ✅ |
| Notion | `NOTION_INTEGRATION_TOKEN` | ✅ |
| OpenAI | `OPENAI_API_KEY` | ✅ |
| OpenAI | `OPENAI_API_KEY_V2` | ✅ |
| Postman | `POSTMAN_API_KEY_V2` | ✅ |
| SendGrid | `SENDGRID_API_KEY` | ✅ |
| Slack | `SLACK` | ✅ |
| Slack | `SLACK_OPAQUE` | ✅ |
| Stripe | `STRIPE_LIVE_API_SECRET_KEY` | ✅ |
| Stripe | `STRIPE_TEST_API_SECRET_KEY` | ✅ |
| Tailscale | `TAILSCALE_API_KEY` | ✅ |
| Telegram | `TELEGRAM_BOT_TOKEN` | ✅ |
| Terraform Cloud | `TERRAFORM_CLOUD_ENTERPRISE_TOKEN` | ✅ |


[サポートされているシークレットの完全なリスト](https://docs.github.com/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets?utm_source=changelog-docs-extended-metadata-checks&utm_medium=changelog&utm_campaign=universe25)を参照するか、アップデートについて GitHub changelog を確認してください。


### [When is the analysis run for a given secret?](#when-is-the-analysis-run-for-a-given-secret)


GitHub は、シークレットがアクティブであることが確認され、サポートされているシークレットタイプのリストに含まれている場合、シークレットスキャンアラートに対して拡張メタデータチェックを実行します。さらに、管理者またはセキュリティマネージャーは、特定のリポジトリに対して拡張メタデータチェックを最初に有効にする必要があります。


### [Where is metadata displayed?](#where-is-metadata-displayed)


拡張メタデータは、アラートの担当者や関連するセキュリティキャンペーンなどのアラートに関する追加情報と共に、アラートの右側に表示されます。


### [Who can use this feature?](#who-can-use-this-feature)


拡張メタデータチェックは、GitHub Secret Protection および GitHub Advanced Security のお客様向けに github.com でパブリックプレビューとして利用可能で、データレジデンシーを備えた GitHub Enterprise Cloud も含まれます。


### [Get started with metadata checks](#get-started-with-metadata-checks)


この機能はリポジトリの設定ページから有効にできます。拡張チェックを有効にするには、妥当性チェックを有効にする必要があります。有効にすると、利用可能な場合、アクティブなシークレットのアラート詳細ビューに追加情報が表示されます。


### [Learn more and share feedback](#learn-more-and-share-feedback)


[シークレットスキャンでリポジトリを保護する](https://docs.github.com/code-security/secret-scanning/introduction/about-secret-scanning?utm_source=changelog-docs-extended-metadata-checks&utm_medium=changelog&utm_campaign=universe25)方法の詳細を確認するか、シークレットスキャンと拡張メタデータチェックに関する[フィードバックを共有](https://gh.io/secret-scanning-feedback?utm_source=changelog-feedback-extended-metadata-checks&utm_medium=changelog&utm_campaign=universe25)してください。
