---
title: "Dependabot now supports OIDC authentication"
date: "2026-02-03"
type: "Improvement"
labels: ["supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-02-03-dependabot-now-supports-oidc-authentication"
fetched_at: "2026-02-05T04:46:41.073305Z"
---

# Dependabot now supports OIDC authentication

## Overview
Dependabot can now use OpenID Connect (OIDC) to authenticate with private registries, eliminating the need to store long-lived credentials as repository secrets.

## Detailed Explanation
### Overview
- Dependabot can now use OpenID Connect (OIDC) to authenticate with private registries, eliminating the need to store long-lived credentials as repository secrets.

### What’s new
- With OIDC-based authentication, Dependabot update jobs can dynamically obtain short-lived credentials from your cloud identity provider, just like GitHub Actions workflows using OIDC federation .

### Supported registries
- AWS CodeArtifact
- Azure DevOps Artifacts
- JFrog Artifactory

### Benefits
- Enhanced security: Eliminates static, long-lived credentials from your repositories. Short-lived, dynamically generated tokens reduce operational overhead and attack surface.
- Simpler management: Enables secure, policy-compliant access to private registries.
- Avoid rate limiting: Dynamic credentials help you avoid hitting rate limits associated with static tokens.

### Getting started
- To enable OIDC authentication for your private registry, update your dependabot.yml configuration to use the new OIDC authentication type for supported registries. See our documentation on private registry configuration for setup instructions and examples.

### Learn more
- Configuring access to private registries for Dependabot
- About OpenID Connect

## Insights (derived from article language)
- Learn more Configuring access to private registries for Dependabot About OpenID Connect

## Article Content (cleaned)
Dependabot can now use OpenID Connect (OIDC) to authenticate with private registries, eliminating the need to store long\-lived credentials as repository secrets.


## [What’s new](https://github.blog/changelog/feed/#whats-new)


With OIDC\-based authentication, Dependabot update jobs can dynamically obtain short\-lived credentials from your cloud identity provider, just like GitHub Actions workflows using [OIDC federation](https://docs.github.com/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect).


### [Supported registries](https://github.blog/changelog/feed/#supported-registries)


* **AWS CodeArtifact**
* **Azure DevOps Artifacts**
* **JFrog Artifactory**


## [Benefits](https://github.blog/changelog/feed/#benefits)


* **Enhanced security:** Eliminates static, long\-lived credentials from your repositories. Short\-lived, dynamically generated tokens reduce operational overhead and attack surface.
* **Simpler management:** Enables secure, policy\-compliant access to private registries.
* **Avoid rate limiting:** Dynamic credentials help you avoid hitting rate limits associated with static tokens.


## [Getting started](https://github.blog/changelog/feed/#getting-started)


To enable OIDC authentication for your private registry, update your `dependabot.yml` configuration to use the new OIDC authentication type for supported registries. See our [documentation on private registry configuration](https://docs.github.com/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot) for setup instructions and examples.


## [Learn more](https://github.blog/changelog/feed/#learn-more)


* [Configuring access to private registries for Dependabot](https://docs.github.com/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot)
* [About OpenID Connect](https://docs.github.com/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
