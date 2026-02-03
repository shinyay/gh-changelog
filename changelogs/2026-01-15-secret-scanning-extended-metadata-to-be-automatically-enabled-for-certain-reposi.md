---
title: "Secret scanning extended metadata to be automatically enabled for certain repositories"
date: "2026-01-15"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-15-secret-scanning-extended-metadata-to-be-automatically-enabled-for-certain-repositories"
fetched_at: "2026-02-03T14:50:54.758028Z"
---

# Secret scanning extended metadata to be automatically enabled for certain repositories

## Overview
GitHub secret scanning is adding support for extended metadata checks in security configurations, starting February 18, 2026.

## Detailed Explanation
### Overview
- GitHub secret scanning is adding support for extended metadata checks in security configurations, starting February 18, 2026.
- Extended metadata checks are a nested feature under validity checks. If you’ve already enabled validity checks for your repositories via security configurations, you’ll automatically have extended metadata checks enabled.

### What are extended metadata checks?
- With extended metadata checks, secret scanning alerts now display details about a secret’s owner, secret creation and expiry dates, and project or organization context when information is available from the secret provider. This feature extends validity checks to additional context about the secret.
- For example, leaked OpenAI keys with information available will display the secret owner’s name, email, and identifier, in addition to information about the organization.
- These new metadata keys expand on existing validity checks to give more actionable context for triage and remediation, enabling development and security teams to assess exposure faster and prioritize remediation.
- Note: The availability of metadata depends on the secret provider, the type of token, and sometimes even the secret itself. GitHub makes a best effort to display all available metadata, but not every key will always be present.

### What’s changing?
- Extended metadata checks are currently available to Enterprise Cloud customers with secret scanning who have validity checks enabled. Starting on this date, users will be able to enable or disable the feature at organization and enterprise levels with security configurations. Repositories with validity checks enabled with security configurations will see metadata checks automatically enabled for them at this time.

### Learn more and share feedback
- Learn more about securing your repositories with secret scanning or share feedback about secret scanning and extended metadata checks.

## Caveats / Limitations
- Note: The availability of metadata depends on the secret provider, the type of token, and sometimes even the secret itself.

## Insights (derived from article language)
- Learn more and share feedback Learn more about securing your repositories with secret scanning or share feedback about secret scanning and extended metadata checks.

## Article Content (cleaned)
GitHub secret scanning is adding support for [extended metadata checks](https://github.blog/changelog/2025-10-28-introducing-extended-metadata-checks-for-secret-scanning/) in security configurations, starting February 18, 2026\.


Extended metadata checks are a nested feature under validity checks. If you’ve already enabled validity checks for your repositories via security configurations, you’ll automatically have extended metadata checks enabled.


### [What are extended metadata checks?](#what-are-extended-metadata-checks)


With extended metadata checks, secret scanning alerts now display details about a secret’s owner, secret creation and expiry dates, and project or organization context when information is available from the secret provider. This feature extends validity checks to additional context about the secret.


For example, leaked OpenAI keys with information available will display the secret owner’s name, email, and identifier, in addition to information about the organization.


These new metadata keys expand on existing validity checks to give more actionable context for triage and remediation, enabling development and security teams to assess exposure faster and prioritize remediation.


**Note:** The availability of metadata depends on the secret provider, the type of token, and sometimes even the secret itself. GitHub makes a best effort to display all available metadata, but not every key will always be present.


### [What’s changing?](#whats-changing)


Extended metadata checks are currently available to Enterprise Cloud customers with secret scanning who have validity checks enabled. Starting on this date, users will be able to enable or disable the feature at organization and enterprise levels with security configurations. Repositories with validity checks enabled with security configurations will see metadata checks automatically enabled for them at this time.


### [Learn more and share feedback](#learn-more-and-share-feedback)


Learn more about [securing your repositories with secret scanning](https://docs.github.com/code-security/concepts/secret-security/about-secret-scanning) or [share feedback](https://github.com/orgs/community/discussions/177054) about secret scanning and extended metadata checks.
