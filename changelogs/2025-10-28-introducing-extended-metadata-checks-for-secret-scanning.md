---
title: "Introducing extended metadata checks for secret scanning"
date: "2025-10-28"
type: "new releases"
labels: ["application security", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-introducing-extended-metadata-checks-for-secret-scanning"
fetched_at: "2026-02-03T14:40:06.594602Z"
---

# Introducing extended metadata checks for secret scanning

## Overview
To help you understand ownership and impact of a leaked secret, GitHub secret scanning now surfaces additional metadata for supported secret types.

## Detailed Explanation
### Overview
- To help you understand ownership and impact of a leaked secret, GitHub secret scanning now surfaces additional metadata for supported secret types.

### What’s changing?
- Secret scanning already performs validity checks for most secret providers, verifying whether a detected secret is active. This update extends those checks to include additional metadata fields from supported providers.
- Available in public preview for supported secret types, alerts now display details about a secret’s owner, secret creation and expiry dates, and project or organization context when information is available from the secret provider.
- For example, leaked OpenAI keys will display the secret owner’s name, email, and identifier, in addition to information about the organization when available. These new metadata keys expand on existing validity checks to give more actionable context for triage and remediation, enabling development and security teams to assess exposure faster and prioritize remediation.
- Please note, metadata availability will vary by secret provider, token type, and possibly even for a specific secret at different points in time. GitHub makes a best effort to display metadata for the secret, but not all metadata keys may be available for a secret.

### What secret types are supported?
- GitHub will continually add support for additional secret types on a rolling basis. In addition to previously announced support for active GitHub tokens, metadata checks are now supported for the following types:
- See the full list of supported secrets or keep an eye on the GitHub changelog for updates.

### When is the analysis run for a given secret?
- GitHub will run extended metadata checks for secret scanning alerts when a secret is both confirmed active and in the list of supported secret types. In addition, an admin or security manager first needs to enable extended metadata checks for a given repository.

### Where is metadata displayed?
- Extended metadata is shown in the right-hand side of an alert, along with additional information about the alert, like alert assignees or associated security campaigns.

### Who can use this feature?
- Extended metadata checks are available in public preview for GitHub Secret Protection and GitHub Advanced Security customers on github.com, including GitHub Enterprise Cloud with data residency.

### Get started with metadata checks
- The feature can be enabled from the repository settings page. Validity checks must be enabled in order to enable the extended checks. Once enabled, additional information will be displayed in the alert details view for active secrets when available.

### Learn more and share feedback
- Learn more about securing your repositories with secret scanning or share feedback about secret scanning and extended metadata checks.

## Impact / Who’s Affected
- Available in public preview for supported secret types, alerts now display details about a secret’s owner, secret creation and expiry dates, and project or organization context when information is available from the secret provider.
- In addition to previously announced support for active GitHub tokens, metadata checks are now supported for the following types: Provider Token Extended Metadata Adafruit ADAFRUIT_AIO_KEY ✅ Anthropic ANTHROPIC_API_KEY ✅ Apify APIFY_API_TOKEN ✅ Contentful CONTENTFUL_PERSONAL_ACCESS_TOKEN ✅ Discord DISCORD_API_TOKEN ✅ Discord DISCORD_API_TOKEN_V2 ✅ Dropbox DROPBOX_OAUTH2_ACCESS_TOKEN ✅ Dropbox DROPBOX_OAUTH2_SHORT_LIVED_ACCESS_TOKEN ✅ Fastly FASTLY_API_TOKEN ✅ Figma FIGMA_PAT ✅ GitLab GITLAB_ACCESS_TOKEN ✅ Google GOOGLE_OAUTH_ACCESS_TOKEN ✅ Hugging Face HUGGING_FACE_USER_ACCESS_TOKEN ✅ Intercom INTERCOM_ACCESS_TOKEN ✅ Mailchimp MAILCHIMP_API ✅ Mailgun MAILGUN ✅ Mailgun MAILGUN_LEGACY ✅ Mapbox MAPBOX_SECRET_ACCESS_TOKEN ✅ Notion NOTION_INTEGRATION_TOKEN ✅ OpenAI OPENAI_API_KEY ✅ OpenAI OPENAI_API_KEY_V2 ✅ Postman POSTMAN_API_KEY_V2 ✅ SendGrid SENDGRID_API_KEY ✅ Slack SLACK ✅ Slack SLACK_OPAQUE ✅ Stripe STRIPE_LIVE_API_SECRET_KEY ✅ Stripe STRIPE_TEST_API_SECRET_KEY ✅ Tailscale TAILSCALE_API_KEY ✅ Telegram TELEGRAM_BOT_TOKEN ✅ Terraform Cloud TERRAFORM_CLOUD_ENTERPRISE_TOKEN ✅ See the full list of supported secrets or keep an eye on the GitHub changelog for updates.
- Extended metadata checks are available in public preview for GitHub Secret Protection and GitHub Advanced Security customers on github.com, including GitHub Enterprise Cloud with data residency.

## Caveats / Limitations
- Please note, metadata availability will vary by secret provider, token type, and possibly even for a specific secret at different points in time.

## Insights (derived from article language)
- Learn more and share feedback Learn more about securing your repositories with secret scanning or share feedback about secret scanning and extended metadata checks.

## Article Content (cleaned)
To help you understand ownership and impact of a leaked secret, GitHub secret scanning now surfaces additional metadata for supported secret types.


### [What’s changing?](#whats-changing)


Secret scanning already performs validity checks for most secret providers, verifying whether a detected secret is active. This update extends those checks to include additional metadata fields from supported providers.


Available in public preview for supported secret types, alerts now display details about a secret’s owner, secret creation and expiry dates, and project or organization context when information is available from the secret provider.


For example, leaked OpenAI keys will display the secret owner’s name, email, and identifier, in addition to information about the organization when available. These new metadata keys expand on existing validity checks to give more actionable context for triage and remediation, enabling development and security teams to assess exposure faster and prioritize remediation.


Please note, metadata availability will vary by secret provider, token type, and possibly even for a specific secret at different points in time. GitHub makes a best effort to display metadata for the secret, but not all metadata keys may be available for a secret.


### [What secret types are supported?](#what-secret-types-are-supported)


GitHub will continually add support for additional secret types on a rolling basis. In addition to previously announced support for active GitHub tokens, metadata checks are now supported for the following types:




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


See the [full list of supported secrets](https://docs.github.com/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets?utm_source=changelog-docs-extended-metadata-checks&utm_medium=changelog&utm_campaign=universe25) or keep an eye on the GitHub changelog for updates.


### [When is the analysis run for a given secret?](#when-is-the-analysis-run-for-a-given-secret)


GitHub will run extended metadata checks for secret scanning alerts when a secret is both confirmed active and in the list of supported secret types. In addition, an admin or security manager first needs to enable extended metadata checks for a given repository.


### [Where is metadata displayed?](#where-is-metadata-displayed)


Extended metadata is shown in the right\-hand side of an alert, along with additional information about the alert, like alert assignees or associated security campaigns.


### [Who can use this feature?](#who-can-use-this-feature)


Extended metadata checks are available in public preview for GitHub Secret Protection and GitHub Advanced Security customers on github.com, including GitHub Enterprise Cloud with data residency.


### [Get started with metadata checks](#get-started-with-metadata-checks)


The feature can be enabled from the repository settings page. Validity checks must be enabled in order to enable the extended checks. Once enabled, additional information will be displayed in the alert details view for active secrets when available.


### [Learn more and share feedback](#learn-more-and-share-feedback)


Learn more about [securing your repositories with secret scanning](https://docs.github.com/code-security/secret-scanning/introduction/about-secret-scanning?utm_source=changelog-docs-extended-metadata-checks&utm_medium=changelog&utm_campaign=universe25) or [share feedback](https://gh.io/secret-scanning-feedback?utm_source=changelog-feedback-extended-metadata-checks&utm_medium=changelog&utm_campaign=universe25) about secret scanning and extended metadata checks.
