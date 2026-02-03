---
title: "npm classic tokens revoked, session-based auth and CLI token management now available"
date: "2025-12-09"
type: "deprecations"
labels: ["supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-09-npm-classic-tokens-revoked-session-based-auth-and-cli-token-management-now-available"
fetched_at: "2026-02-03T14:40:05.732750Z"
---

# npm classic tokens revoked, session-based auth and CLI token management now available

## Overview
As previously announced , we’re completing the npm classic token deprecation today. This marks a major milestone in the security hardening initiative to strengthen npm’s authentication system.

## Detailed Explanation
### Overview
- As previously announced , we’re completing the npm classic token deprecation today. This marks a major milestone in the security hardening initiative to strengthen npm’s authentication system.

### npm classic tokens permanently revoked
- We’ve permanently revoked all existing npm classic tokens. They can no longer authenticate, be recreated, or be recovered.

### New session-based authentication
- Starting today, when you use npm login you’ll receive a two-hour session token instead of long-lived tokens. These sessions automatically expire after two hours, requiring reauthentication to continue publishing. Unlike traditional tokens, session tokens won’t appear in your UI or CLI token lists—they work behind the scenes to maintain your authenticated session. During these sessions, 2FA is enforced for publishing operations, adding an extra layer of security.

### New CLI token management tool for granular tokens
- npm is introducing a new command-line tool specifically designed for managing granular access tokens. This new CLI tool provides the ability to create, list, and revoke granular tokens directly from your terminal, eliminating the need to visit the npm website for token management.
- This provides the same convenient command-line experience previously available only for classic tokens.
- Full documentation for the new token management commands will be available in the npm CLI documentation .

### Secure-by-default 2FA for new packages (new)
- Starting this week, 2FA enforcement is shifting to become the default option for all new package publications. When you create a new package, 2FA will be enabled by default in the package settings. This ensures packages are protected from the moment they’re created without requiring manual security configuration. Existing packages retain their current 2FA settings.

### Legacy API endpoint support temporarily restored
- We’ve temporarily restored support for the legacy API endpoint ( /user/org.couchdb.user: ) that was causing compatibility issues in November. This endpoint now generates the same two-hour session tokens used by npm login , requiring re-authentication every two hours when publishing.
- This is a temporary measure to provide a transition period. The removal of this legacy endpoint is imminent and planned for the coming months. We strongly recommend migrating to modern authentication methods now to avoid disruption.
- Note: This endpoint primarily affects users of Yarn v1 and v2. If you’re using these versions, we recommend updating to modern package managers or authentication methods that support current npm security standards.

### If you were still using npm classic tokens
- Your npm classic tokens stopped working today. Here’s how to restore access:
- For local development, run npm login to create a new two-hour session. You’ll need to reauthenticate periodically, but this ensures better security.
- For CI/CD workflows, create granular access tokens using the new CLI commands ( npm token create ) or at npmjs.com/settings/~/tokens . When setting up these tokens, you may enable Bypass 2FA for noninteractive automated workflows and set appropriate expiration (write tokens limited to 90 days maximum). For the most secure deployment, consider adopting OIDC trusted publishing , which eliminates the need to generate and manage tokens for publishing packages.

### What’s next?
- Thank you for your patience as we strengthen npm’s security. These changes protect the entire JavaScript ecosystem while maintaining the workflows you depend on. For more details on our security roadmap and ongoing improvements, see our community discussion .

## Impact / Who’s Affected
- This provides the same convenient command-line experience previously available only for classic tokens.
- When setting up these tokens, you may enable Bypass 2FA for noninteractive automated workflows and set appropriate expiration (write tokens limited to 90 days maximum).

## Caveats / Limitations
- This provides the same convenient command-line experience previously available only for classic tokens.
- Note: This endpoint primarily affects users of Yarn v1 and v2.
- When setting up these tokens, you may enable Bypass 2FA for noninteractive automated workflows and set appropriate expiration (write tokens limited to 90 days maximum).

## Insights (derived from article language)
- If you’re using these versions, we recommend updating to modern package managers or authentication methods that support current npm security standards.
- For the most secure deployment, consider adopting OIDC trusted publishing , which eliminates the need to generate and manage tokens for publishing packages.
- For more details on our security roadmap and ongoing improvements, see our community discussion .

## Article Content (cleaned)
As [previously announced](https://github.blog/changelog/2025-11-05-npm-security-update-classic-token-creation-disabled-and-granular-token-changes/), we’re completing the npm classic token deprecation today. This marks a major milestone in the [security hardening initiative](https://github.com/orgs/community/discussions/178140) to strengthen npm’s authentication system.


## [What’s changing today (December 9, 2025\)](#whats-changing-today-december-9-2025)


### [npm classic tokens permanently revoked](#npm-classic-tokens-permanently-revoked)


We’ve permanently revoked all existing npm classic tokens. They can no longer authenticate, be recreated, or be recovered.


### [New session\-based authentication](#new-session-based-authentication)


Starting today, when you use `npm login` you’ll receive a two\-hour session token instead of long\-lived tokens. These sessions automatically expire after two hours, requiring reauthentication to continue publishing. Unlike traditional tokens, session tokens won’t appear in your UI or CLI token lists—they work behind the scenes to maintain your authenticated session. During these sessions, 2FA is enforced for publishing operations, adding an extra layer of security.


### [New CLI token management tool for granular tokens](#new-cli-token-management-tool-for-granular-tokens)


npm is introducing a new command\-line tool specifically designed for managing granular access tokens. This new CLI tool provides the ability to create, list, and revoke granular tokens directly from your terminal, eliminating the need to visit the npm website for token management.


This provides the same convenient command\-line experience previously available only for classic tokens.


Full documentation for the new token management commands will be available in the [npm CLI documentation](https://docs.npmjs.com/cli/).


### [Secure\-by\-default 2FA for new packages (new)](#secure-by-default-2fa-for-new-packages-new)


Starting this week, 2FA enforcement is shifting to become the default option for all new package publications. When you create a new package, 2FA will be enabled by default in the package settings. This ensures packages are protected from the moment they’re created without requiring manual security configuration. Existing packages retain their current 2FA settings.


### [Legacy API endpoint support temporarily restored](#legacy-api-endpoint-support-temporarily-restored)


We’ve temporarily restored support for the legacy API endpoint (`/user/org.couchdb.user:`) that was causing compatibility issues in November. This endpoint now generates the same two\-hour session tokens used by `npm login`, requiring re\-authentication every two hours when publishing.


This is a temporary measure to provide a transition period. The removal of this legacy endpoint is imminent and planned for the coming months. We strongly recommend migrating to modern authentication methods now to avoid disruption.


**Note:** This endpoint primarily affects users of Yarn v1 and v2\. If you’re using these versions, we recommend updating to modern package managers or authentication methods that support current npm security standards.


## [What you need to do](#what-you-need-to-do)


### [If you were still using npm classic tokens](#if-you-were-still-using-npm-classic-tokens)


Your npm classic tokens stopped working today. Here’s how to restore access:


For local development, run `npm login` to create a new two\-hour session. You’ll need to reauthenticate periodically, but this ensures better security.


For CI/CD workflows, create granular access tokens using the new CLI commands (`npm token create`) or at [npmjs.com/settings/\~/tokens](https://www.npmjs.com/settings/~/tokens). When setting up these tokens, you may enable **Bypass 2FA** for noninteractive automated workflows and set appropriate expiration (write tokens limited to 90 days maximum). For the most secure deployment, consider adopting [OIDC trusted publishing](https://docs.npmjs.com/trusted-publishers), which eliminates the need to generate and manage tokens for publishing packages.


## [What’s next?](#whats-next)


Thank you for your patience as we strengthen npm’s security. These changes protect the entire JavaScript ecosystem while maintaining the workflows you depend on. For more details on our security roadmap and ongoing improvements, see our [community discussion](https://github.com/orgs/community/discussions/179562).
