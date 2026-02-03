---
title: "Secret scanning improves private key detection, updates Sentry pattern names"
date: "2025-11-12"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-12-secret-scanning-improves-private-key-detection"
fetched_at: "2026-02-03T14:50:55.330837Z"
---

# Secret scanning improves private key detection, updates Sentry pattern names

## Overview
To reduce the risk of cryptographic credentials being exposed in your repositories, secret scanning now detects additional private key formats and has upgraded existing private key detectors.

## Detailed Explanation
### Overview
- To reduce the risk of cryptographic credentials being exposed in your repositories, secret scanning now detects additional private key formats and has upgraded existing private key detectors.
- In addition, Sentry token names have been updated to match Sentry’s change to token naming conventions.

### New patterns added
- Secret scanning now detects the following additional private key formats.
- The generic private key pattern detects RSA keys in PKCS#8 format and other private keys using the standard BEGIN PRIVATE KEY header. This pattern automatically filters out GitHub private keys to avoid duplicate alerts.

### Detector improvements
- Starting this week, the following private key patterns will also detect keys that contain escaped newlines ( \n ), a common format in configuration files and environment variables.

### Secret types renamed
- Sentry recently rolled out changes to naming conventions across their token types. To align with these changes, the following secret types are being renamed.
- Learn more about non-provider secret patterns and secret scanning .

## Key Changes
- Starting this week, the following private key patterns will also detect keys that contain escaped newlines ( \n ), a common format in configuration files and environment variables.

## Insights (derived from article language)
- Secret type (new) Slug (new) Secret type (prev) Slug (prev) Sentry Organization Token sentry_organization_token Sentry Org Auth Token sentry_org_auth_token Sentry Personal Token sentry_personal_token Sentry User Auth Token sentry_user_auth_token Learn more about non-provider secret patterns and secret scanning .

## Article Content (cleaned)
To reduce the risk of cryptographic credentials being exposed in your repositories, secret scanning now detects additional private key formats and has upgraded existing private key detectors.


In addition, Sentry token names have been updated to match Sentry’s change to token naming conventions.


## [New patterns added](#new-patterns-added)


Secret scanning now detects the following additional private key formats.




| Secret type | Format detected |
| --- | --- |
| `ec_private_key` | Elliptic Curve private keys |
| `generic_private_key` | Generic PKCS\#8 private keys |


The generic private key pattern detects RSA keys in PKCS\#8 format and other private keys using the standard `BEGIN PRIVATE KEY` header. This pattern automatically filters out GitHub private keys to avoid duplicate alerts.


## [Detector improvements](#detector-improvements)


Starting this week, the following private key patterns will also detect keys that contain escaped newlines (`\n`), a common format in configuration files and environment variables.




| Secret type |
| --- |
| `ec_private_key` |
| `github_ssh_private_key` |
| `openssh_private_key` |
| `rsa_private_key` |


## [Secret types renamed](#secret-types-renamed)


Sentry recently rolled out changes to naming conventions across their token types. To align with these changes, the following secret types are being renamed.




| Secret type (new) | Slug (new) | Secret type (prev) | Slug (prev) |
| --- | --- | --- | --- |
| Sentry Organization Token | `sentry_organization_token` | Sentry Org Auth Token | `sentry_org_auth_token` |
| Sentry Personal Token | `sentry_personal_token` | Sentry User Auth Token | `sentry_user_auth_token` |


Learn more about [non\-provider secret patterns](https://docs.github.com/enterprise-cloud@latest/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#non-provider-patterns) and [secret scanning](https://docs.github.com/code-security/secret-scanning/introduction/about-secret-scanning).
