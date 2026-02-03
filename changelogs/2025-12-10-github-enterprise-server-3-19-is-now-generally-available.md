---
title: "GitHub Enterprise Server 3.19 is now generally available"
date: "2025-12-10"
type: "new releases"
labels: ["collaboration tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-10-github-enterprise-server-3-19-is-now-generally-available"
fetched_at: "2026-02-03T14:50:54.998820Z"
---

# GitHub Enterprise Server 3.19 is now generally available

## Overview
GitHub Enterprise Server (GHES) 3.19 enhances deployment efficiency, monitoring capabilities, code security, and policy management. Here are a few highlights in the 3.19 release:

## Detailed Explanation
### Overview
- GitHub Enterprise Server (GHES) 3.19 enhances deployment efficiency, monitoring capabilities, code security, and policy management. Here are a few highlights in the 3.19 release:
- An improved and more intuitive flow for creating repositories is now available. The new form provides a modern interface for collecting repository metadata, enforcing custom properties, and applying repository policies at creation time. This helps ensure consistent repository configuration across your enterprise. For more information about this update, read about the improved repository creation experience .
- Enterprise administrators can manage rules more efficiently with the general availability of ruleset history, import, and export. Ruleset history allows tracking and rolling back changes, while import and export simplify sharing and reusing rulesets, including those from GitHub’s ruleset-recipes repository . For more information, read our documentation on managing rulesets .
- Administrators can enforce policies to block specific actions and require SHA-based pinning when workflows use actions from public repositories. These policies help improve workflow security by ensuring only approved actions are used and referenced by immutable SHAs. For more information, read blocking and SHA pinning actions .
- You can now designate users as application managers of GitHub Apps owned by the enterprise. App managers can update application registration, but they cannot manage application installations. We’ve also enhanced the app manager feature to use the roles platform. This means that organization teams can now be assigned as app managers of individual organization-owned apps, and a new organization app manager role can be assigned to teams and users, giving them access to all of the apps owned by an organization. For more information, see GitHub App Managers .
- Starting with version 3.19, new installations of GHES will have OpenTelemetry metrics enabled and Collectd metrics disabled by default. You can choose to switch between the two if needed. Upgraded instances will keep their current settings. In the next two to three releases, OpenTelemetry metrics will become the only supported metrics. For more information, read OpenTelemetry metrics .
- You can now configure SSH and TLS ciphers for greater flexibility and control over which ciphers are used, including the ability to avoid weak ciphers. You can list the default ciphers and select which ones you want to use. For more information, read configuring cipher suites and cryptographic algorithms .
- Enterprise administrators can manage rules more efficiently with the general availability of ruleset history, import, and export. Ruleset history allows tracking and rolling back changes, while import and export simplify sharing and reusing rulesets, including those from GitHub’s ruleset-recipes repository . For more information, read our documentation on managing rulesets .
- Administrators can enforce policies to block specific actions and require SHA-based pinning when workflows use actions from public repositories. These policies help improve workflow security by ensuring only approved actions are used and referenced by immutable SHAs. For more information, read blocking and SHA pinning actions .
- You can now designate users as application managers of GitHub Apps owned by the enterprise. App managers can update application registration, but they cannot manage application installations. We’ve also enhanced the app manager feature to use the roles platform. This means that organization teams can now be assigned as app managers of individual organization-owned apps, and a new organization app manager role can be assigned to teams and users, giving them access to all of the apps owned by an organization. For more information, see GitHub App Managers .
- Starting with version 3.19, new installations of GHES will have OpenTelemetry metrics enabled and Collectd metrics disabled by default. You can choose to switch between the two if needed. Upgraded instances will keep their current settings. In the next two to three releases, OpenTelemetry metrics will become the only supported metrics. For more information, read OpenTelemetry metrics .
- You can now configure SSH and TLS ciphers for greater flexibility and control over which ciphers are used, including the ability to avoid weak ciphers. You can list the default ciphers and select which ones you want to use. For more information, read configuring cipher suites and cryptographic algorithms .
- To learn more about GHES 3.19, check out the release notes , or download it now. If you have any issues upgrading to version 3.19 or experience any issues using these new features, please contact our support team .
- Join the community discussion to share your feedback and ask questions.

## Impact / Who’s Affected
- Here are a few highlights in the 3.19 release: An improved and more intuitive flow for creating repositories is now available.
- These policies help improve workflow security by ensuring only approved actions are used and referenced by immutable SHAs.
- In the next two to three releases, OpenTelemetry metrics will become the only supported metrics.

## Caveats / Limitations
- These policies help improve workflow security by ensuring only approved actions are used and referenced by immutable SHAs.
- In the next two to three releases, OpenTelemetry metrics will become the only supported metrics.
- To learn more about GHES 3.19, check out the release notes , or download it now.

## Insights (derived from article language)
- To learn more about GHES 3.19, check out the release notes , or download it now.

## Article Content (cleaned)
GitHub Enterprise Server (GHES) 3\.19 enhances deployment efficiency, monitoring capabilities, code security, and policy management. Here are a few highlights in the 3\.19 release:


* An improved and more intuitive flow for creating repositories is now available. The new form provides a modern interface for collecting repository metadata, enforcing custom properties, and applying repository policies at creation time. This helps ensure consistent repository configuration across your enterprise. For more information about this update, read about [the improved repository creation experience](https://github.blog/changelog/2025-08-26-improved-repository-creation-generally-available-plus-ruleset-insights-improvements/).
* Enterprise administrators can manage rules more efficiently with the general availability of ruleset history, import, and export. Ruleset history allows tracking and rolling back changes, while import and export simplify sharing and reusing rulesets, including those from [GitHub’s ruleset\-recipes repository](https://github.com/github/ruleset-recipes). For more information, read [our documentation on managing rulesets](https://docs.github.com/enterprise-server@3.19/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository).
* Administrators can enforce policies to block specific actions and require SHA\-based pinning when workflows use actions from public repositories. These policies help improve workflow security by ensuring only approved actions are used and referenced by immutable SHAs. For more information, read [blocking and SHA pinning actions](https://github.blog/changelog/2025-08-15-github-actions-policy-now-supports-blocking-and-sha-pinning-actions/).
* You can now designate users as application managers of GitHub Apps owned by the enterprise. App managers can update application registration, but they cannot manage application installations. We’ve also enhanced the app manager feature to use the roles platform. This means that organization teams can now be assigned as app managers of individual organization\-owned apps, and a new organization app manager role can be assigned to teams and users, giving them access to all of the apps owned by an organization. For more information, see [GitHub App Managers](https://docs.github.com/enterprise-server@3.19/apps/maintaining-github-apps/about-github-app-managers).
* Starting with version 3\.19, new installations of GHES will have OpenTelemetry metrics enabled and Collectd metrics disabled by default. You can choose to switch between the two if needed. Upgraded instances will keep their current settings. In the next two to three releases, OpenTelemetry metrics will become the only supported metrics. For more information, read [OpenTelemetry metrics](https://docs.github.com/enterprise-server@3.19/admin/monitoring-and-managing-your-instance/monitoring-your-instance/opentelemetry-metrics).
* You can now configure SSH and TLS ciphers for greater flexibility and control over which ciphers are used, including the ability to avoid weak ciphers. You can list the default ciphers and select which ones you want to use. For more information, read [configuring cipher suites and cryptographic algorithms](https://docs.github.com/enterprise-server@3.19/admin/configuring-settings/hardening-security-for-your-enterprise/configuring-tls-and-ssh-ciphers).


To learn more about GHES 3\.19, check out the [release notes](https://docs.github.com/enterprise-server@3.19/admin/release-notes), or [download it](https://enterprise.github.com/releases/3.19.0/download) now. If you have any issues upgrading to version 3\.19 or experience any issues using these new features, please [contact our support team](https://support.github.com/features/enterprise-administrators-server).


Join the [community discussion](https://github.com/orgs/community/discussions/181173) to share your feedback and ask questions.
