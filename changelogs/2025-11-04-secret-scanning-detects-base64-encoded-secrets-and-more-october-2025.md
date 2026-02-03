---
title: "Secret scanning detects Base64-encoded secrets and more — October 2025"
date: "2025-11-04"
type: "new releases"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-04-secret-scanning-now-detects-base64-encoded-secrets"
fetched_at: "2026-02-03T14:50:55.459294Z"
---

# Secret scanning detects Base64-encoded secrets and more — October 2025

## Overview
GitHub secret scanning continually adds support for new secret types. The following updates were made during the month of October.

## Detailed Explanation
### Secret scanning — October 2025
- GitHub secret scanning continually adds support for new secret types. The following updates were made during the month of October.
- Base64-encoded secrets: Secret scanning now detects Base64-encoded variants for secret types from third-party cloud providers.
- Extended metadata checks: Secret scanning now supports checks for additional context like owner information, creation dates, and organizational details about a secret.
- Validity checks: secret scanning adds validity check support for Grafana and Notion.

### Base64-encoded secret detection
- GitHub secret scanning now detects and prevents obfuscated secrets in Base64 format for secret types from third-party providers.
- Base64-encoded secrets are push protected by default. GitHub will continue to add support for additional types on a rolling basis.

### Extended metadata checks
- As announced at GitHub Universe 2025 , the following secret types now support extended metadata checks.

### Validity checks
- The following secret types now include validity checks to confirm whether detected secrets are active.
- Learn more about secret scanning and see the full list of supported secrets in our product documentation.

## Insights (derived from article language)
- Provider Secret type Grafana grafana_cloud_api_token Notion notion_api_token Learn more about secret scanning and see the full list of supported secrets in our product documentation.

## Article Content (cleaned)
## [Secret scanning — October 2025](#secret-scanning-october-2025)


GitHub secret scanning continually adds support for new secret types. The following updates were made during the month of October.


* **Base64\-encoded secrets:** Secret scanning now detects Base64\-encoded variants for secret types from third\-party cloud providers.
* **Extended metadata checks:** Secret scanning now supports checks for additional context like owner information, creation dates, and organizational details about a secret.
* **Validity checks:** secret scanning adds validity check support for Grafana and Notion.


### [Base64\-encoded secret detection](#base64-encoded-secret-detection)


GitHub secret scanning now detects and prevents obfuscated secrets in Base64 format for secret types from third\-party providers.




| Provider | Secret type |
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


Base64\-encoded secrets are push protected by default. GitHub will continue to add support for additional types on a rolling basis.


## [Extended metadata checks](#extended-metadata-checks)


[As announced at GitHub Universe 2025](https://github.blog/changelog/2025-10-28-introducing-extended-metadata-checks-for-secret-scanning/), the following secret types now support extended metadata checks.




| Provider | Secret type |
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


## [Validity checks](#validity-checks)


The following secret types now include validity checks to confirm whether detected secrets are active.




| Provider | Secret type |
| --- | --- |
| Grafana | `grafana_cloud_api_token` |
| Notion | `notion_api_token` |


Learn more about [secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning?utm_source=changelog-docs-extended-metadata-checks&utm_medium=changelog&utm_campaign=universe25) and see the [full list of supported secrets](https://docs.github.com/code-security/secret-scanning/introduction/supported-secret-scanning-patterns) in our product documentation.
