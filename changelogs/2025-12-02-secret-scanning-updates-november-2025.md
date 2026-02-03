---
title: "Secret scanning updates — November 2025"
date: "2025-12-02"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-02-secret-scanning-updates-november-2025"
fetched_at: "2026-02-03T14:40:05.853001Z"
---

# Secret scanning updates — November 2025

## Overview
GitHub secret scanning continually adds support for new secret types. The following updates were made during the month of November.

## Detailed Explanation
### Overview
- GitHub secret scanning continually adds support for new secret types. The following updates were made during the month of November.
- New provider patterns : Secret scanning added 24 new secret types from providers including Azure, Databricks, Microsoft, Paddle, PostHog, and more.
- Improved private key detection : New patterns for Elliptic Curve and generic PKCS#8 private keys, plus improved detection of escaped newlines.
- Extended metadata : Discord discord_bot_token now supports extended metadata checks.
- Validity checks: Validation for AWS Access Key IDs has been improved.
- Unlisted gists : Secrets in unlisted GitHub gists are now reported to secret scanning partners.

### New patterns added
- We added the following new patterns this month. Secret scanning automatically detects any secrets matching these patterns in your repositories.

### Private key patterns added
- As announced on November 12 , secret scanning now detects additional private key formats:
- Like other generic patterns, both types can be configured for inclusion with push protection, but aren’t included by default.

### Detector upgrades and improvements
- The following private key patterns now also detect keys containing escaped newlines ( \n ), a common format in configuration files and environment variables:
- ec_private_key
- github_ssh_private_key
- openssh_private_key
- rsa_private_key
- Sentry token types were also renamed to match Sentry’s updated naming conventions:
- The following secret type now supports extended metadata checks, providing additional context like owner information, creation dates, and organizational details.
- We’ve upgraded validity checks for the following type. With recent improvements to our validation of AWS Access Key IDs, most customers will see alerts that were previously labeled “unknown” switch to “valid” or “invalid”.

### Partner notification updates
- As announced on November 25 , secrets found in unlisted GitHub gists are now reported to secret scanning partners. Since unlisted gists are accessible to anyone with the URL, leaked secrets in gists should be treated like any other publicly exposed credential.
- Learn more about secret scanning and see the full list of supported secrets in our product documentation.

## Key Changes
- The following private key patterns now also detect keys containing escaped newlines ( \n ), a common format in configuration files and environment variables:
- ec_private_key
- github_ssh_private_key
- openssh_private_key
- rsa_private_key
- Sentry token types were also renamed to match Sentry’s updated naming conventions:
- The following secret type now supports extended metadata checks, providing additional context like owner information, creation dates, and organizational details.
- We’ve upgraded validity checks for the following type. With recent improvements to our validation of AWS Access Key IDs, most customers will see alerts that were previously labeled “unknown” switch to “valid” or “invalid”.

## Impact / Who’s Affected
- Provider Secret type Partner User Push protection Azure azure_immersive_reader_key ✓ ✓ ✓ (configurable) Azure azure_logic_apps_url ✓ ✓ ✓ (configurable) crates.io cratesio_api_token ✓ ✓ ✓ (configurable) Databricks databricks_account_session_token ✓ ✓ ✓ (configurable) Databricks databricks_federated_account_session_token ✓ ✓ ✓ (configurable) Databricks databricks_oauth_code ✓ ✓ ✓ (configurable) Databricks databricks_oauth_refresh_token ✓ ✓ ✓ (configurable) Databricks databricks_oauth_secret_token ✓ ✓ ✓ (configurable) Databricks databricks_oauth_single_use_refresh_token_child ✓ ✓ ✓ (configurable) Databricks databricks_oauth_single_use_refresh_token_parent ✓ ✓ ✓ (configurable) Databricks databricks_scoped_api_token ✓ ✓ ✓ (configurable) Databricks databricks_scoped_internal_token ✓ ✓ ✓ (configurable) Databricks databricks_token ✓ ✓ ✓ (configurable) Databricks databricks_workspace_session_token ✓ ✓ ✓ (configurable) Microsoft power_automate_webhook_sas ✓ ✓ ✓ (configurable) OneSignal onesignal_rich_authentication_token ✓ ✓ ✓ (configurable) Paddle paddle_api_key ✓ ✓ ✓ (configurable) Paddle paddle_sandbox_api_key ✓ ✓ ✓ (configurable) Pineapple Technologies Limited pineapple_technologies_incident_api_key ✓ ✓ ✓ (configurable) PostHog posthog_feature_flags_secure_api_key ✓ ✓ (configurable) PostHog posthog_personal_api_key ✓ ✓ (configurable) Rainforest Pay rainforest_api_key ✓ ✓ ✓ (configurable) Rainforest Pay rainforest_sandbox_api_key ✓ ✓ ✓ (configurable) Raycast raycast_access_token ✓ ✓ ✓ (configurable) Private key patterns added As announced on November 12 , secret scanning now detects additional private key formats: Provider Secret type Description Generic ec_private_key Elliptic Curve private keys Generic generic_private_key Generic PKCS#8 private keys Like other generic patterns, both types can be configured for inclusion with push protection, but aren’t included by default.

## Caveats / Limitations
- Provider Secret type Partner User Push protection Azure azure_immersive_reader_key ✓ ✓ ✓ (configurable) Azure azure_logic_apps_url ✓ ✓ ✓ (configurable) crates.io cratesio_api_token ✓ ✓ ✓ (configurable) Databricks databricks_account_session_token ✓ ✓ ✓ (configurable) Databricks databricks_federated_account_session_token ✓ ✓ ✓ (configurable) Databricks databricks_oauth_code ✓ ✓ ✓ (configurable) Databricks databricks_oauth_refresh_token ✓ ✓ ✓ (configurable) Databricks databricks_oauth_secret_token ✓ ✓ ✓ (configurable) Databricks databricks_oauth_single_use_refresh_token_child ✓ ✓ ✓ (configurable) Databricks databricks_oauth_single_use_refresh_token_parent ✓ ✓ ✓ (configurable) Databricks databricks_scoped_api_token ✓ ✓ ✓ (configurable) Databricks databricks_scoped_internal_token ✓ ✓ ✓ (configurable) Databricks databricks_token ✓ ✓ ✓ (configurable) Databricks databricks_workspace_session_token ✓ ✓ ✓ (configurable) Microsoft power_automate_webhook_sas ✓ ✓ ✓ (configurable) OneSignal onesignal_rich_authentication_token ✓ ✓ ✓ (configurable) Paddle paddle_api_key ✓ ✓ ✓ (configurable) Paddle paddle_sandbox_api_key ✓ ✓ ✓ (configurable) Pineapple Technologies Limited pineapple_technologies_incident_api_key ✓ ✓ ✓ (configurable) PostHog posthog_feature_flags_secure_api_key ✓ ✓ (configurable) PostHog posthog_personal_api_key ✓ ✓ (configurable) Rainforest Pay rainforest_api_key ✓ ✓ ✓ (configurable) Rainforest Pay rainforest_sandbox_api_key ✓ ✓ ✓ (configurable) Raycast raycast_access_token ✓ ✓ ✓ (configurable) Private key patterns added As announced on November 12 , secret scanning now detects additional private key formats: Provider Secret type Description Generic ec_private_key Elliptic Curve private keys Generic generic_private_key Generic PKCS#8 private keys Like other generic patterns, both types can be configured for inclusion with push protection, but aren’t included by default.

## Insights (derived from article language)
- Learn more about secret scanning and see the full list of supported secrets in our product documentation.

## Article Content (cleaned)
GitHub secret scanning continually adds support for new secret types. The following updates were made during the month of November.


* **New provider patterns**: Secret scanning added 24 new secret types from providers including Azure, Databricks, Microsoft, Paddle, PostHog, and more.
* **Improved private key detection**: New patterns for Elliptic Curve and generic PKCS\#8 private keys, plus improved detection of escaped newlines.
* **Extended metadata**: Discord `discord_bot_token` now supports extended metadata checks.
* **Validity checks:** Validation for AWS Access Key IDs has been improved.
* **Unlisted gists**: Secrets in unlisted GitHub gists are now reported to secret scanning partners.


## [New patterns added](#new-patterns-added)


We added the following new patterns this month. Secret scanning automatically detects any secrets matching these patterns in your repositories.




| Provider | Secret type | Partner | User | Push protection |
| --- | --- | --- | --- | --- |
| Azure | `azure_immersive_reader_key` | ✓ | ✓ | ✓ (configurable) |
| Azure | `azure_logic_apps_url` | ✓ | ✓ | ✓ (configurable) |
| crates.io | `cratesio_api_token` | ✓ | ✓ | ✓ (configurable) |
| Databricks | `databricks_account_session_token` | ✓ | ✓ | ✓ (configurable) |
| Databricks | `databricks_federated_account_session_token` | ✓ | ✓ | ✓ (configurable) |
| Databricks | `databricks_oauth_code` | ✓ | ✓ | ✓ (configurable) |
| Databricks | `databricks_oauth_refresh_token` | ✓ | ✓ | ✓ (configurable) |
| Databricks | `databricks_oauth_secret_token` | ✓ | ✓ | ✓ (configurable) |
| Databricks | `databricks_oauth_single_use_refresh_token_child` | ✓ | ✓ | ✓ (configurable) |
| Databricks | `databricks_oauth_single_use_refresh_token_parent` | ✓ | ✓ | ✓ (configurable) |
| Databricks | `databricks_scoped_api_token` | ✓ | ✓ | ✓ (configurable) |
| Databricks | `databricks_scoped_internal_token` | ✓ | ✓ | ✓ (configurable) |
| Databricks | `databricks_token` | ✓ | ✓ | ✓ (configurable) |
| Databricks | `databricks_workspace_session_token` | ✓ | ✓ | ✓ (configurable) |
| Microsoft | `power_automate_webhook_sas` | ✓ | ✓ | ✓ (configurable) |
| OneSignal | `onesignal_rich_authentication_token` | ✓ | ✓ | ✓ (configurable) |
| Paddle | `paddle_api_key` | ✓ | ✓ | ✓ (configurable) |
| Paddle | `paddle_sandbox_api_key` | ✓ | ✓ | ✓ (configurable) |
| Pineapple Technologies Limited | `pineapple_technologies_incident_api_key` | ✓ | ✓ | ✓ (configurable) |
| PostHog | `posthog_feature_flags_secure_api_key` |  | ✓ | ✓ (configurable) |
| PostHog | `posthog_personal_api_key` |  | ✓ | ✓ (configurable) |
| Rainforest Pay | `rainforest_api_key` | ✓ | ✓ | ✓ (configurable) |
| Rainforest Pay | `rainforest_sandbox_api_key` | ✓ | ✓ | ✓ (configurable) |
| Raycast | `raycast_access_token` | ✓ | ✓ | ✓ (configurable) |


### [Private key patterns added](#private-key-patterns-added)


[As announced on November 12](https://github.blog/changelog/2025-11-12-secret-scanning-improves-private-key-detection/), secret scanning now detects additional private key formats:




| Provider | Secret type | Description |
| --- | --- | --- |
| Generic | `ec_private_key` | Elliptic Curve private keys |
| Generic | `generic_private_key` | Generic PKCS\#8 private keys |


Like other generic patterns, both types can be configured for inclusion with push protection, but aren’t included by default.


## [Detector upgrades and improvements](#detector-upgrades-and-improvements)


The following private key patterns now also detect keys containing escaped newlines (`\n`), a common format in configuration files and environment variables:


* `ec_private_key`
* `github_ssh_private_key`
* `openssh_private_key`
* `rsa_private_key`


Sentry token types were also renamed to match Sentry’s updated naming conventions:




| Previous name | New name |
| --- | --- |
| `sentry_organization_token` | `sentry_org_auth_token` |
| `sentry_personal_token` | `sentry_user_auth_token` |


The following secret type now supports extended metadata checks, providing additional context like owner information, creation dates, and organizational details.




| Provider | Secret type |
| --- | --- |
| Discord | `discord_bot_token` |


We’ve upgraded validity checks for the following type. With recent improvements to our validation of AWS Access Key IDs, most customers will see alerts that were previously labeled “unknown” switch to “valid” or “invalid”.




| Provider | Pattern | Validity |
| --- | --- | --- |
| Amazon Web Services (AWS) | `aws_access_key_id` | ✓ |


## [Partner notification updates](#partner-notification-updates)


[As announced on November 25](https://github.blog/changelog/2025-11-25-secrets-in-unlisted-github-gists-are-now-reported-to-secret-scanning-partners/), secrets found in unlisted GitHub gists are now reported to secret scanning partners. Since unlisted gists are accessible to anyone with the URL, leaked secrets in gists should be treated like any other publicly exposed credential.


Learn more about [secret scanning](https://docs.github.com/code-security/secret-scanning/introduction/about-secret-scanning) and see the [full list of supported secrets](https://docs.github.com/code-security/secret-scanning/introduction/supported-secret-scanning-patterns) in our product documentation.
