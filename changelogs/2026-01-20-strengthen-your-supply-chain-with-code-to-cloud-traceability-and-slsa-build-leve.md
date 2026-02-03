---
title: "Strengthen your supply chain with code-to-cloud traceability and SLSA Build Level 3 security"
date: "2026-01-20"
type: "improvements"
labels: ["actions", "application security", "supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-20-strengthen-your-supply-chain-with-code-to-cloud-traceability-and-slsa-build-level-3-security"
fetched_at: "2026-02-03T14:40:05.145184Z"
---

# Strengthen your supply chain with code-to-cloud traceability and SLSA Build Level 3 security

## Overview
You can now link build artifacts like containers and binaries to GitHub and add storage and deployment context, even if the artifacts live outside GitHub. This helps you get code-to-cloud traceability and prioritize security work based on what’s actually running in production.

## Detailed Explanation
### Overview
- You can now link build artifacts like containers and binaries to GitHub and add storage and deployment context, even if the artifacts live outside GitHub. This helps you get code-to-cloud traceability and prioritize security work based on what’s actually running in production.

### Artifact metadata APIs
- New REST API endpoints let you associate build artifacts with their storage location, track promotion through your release pipeline, and add production context like deployment data and runtime risk:
- Storage records capture an artifact’s location in a package registry.
- Deployment records capture where an artifact is deployed and runtime risk factors such as whether the deployed workload is exposed to the internet or processes sensitive data.
- You can call these APIs from your CI/CD workflows, external CD tooling, or cloud runtime monitors. Our launch partners—Microsoft Defender for Cloud (for deployment and runtime data, in public preview) and JFrog Artifactory (for storage and promotion context)—have built native integrations you can enable without additional configuration.

### Linked artifacts view
- A new view in your organization’s Packages tab displays all linked artifacts with their attestations, storage locations, and deployment history. This gives you unified visibility across your software supply chain.
- If you use GitHub artifact attestations , each artifact is cryptographically bound to its source repository and build workflow, helping you achieve SLSA Build Level 3 security. The artifact view surfaces all attestations created for an artifact, including build provenance, attested SBOMs, and any custom attestations that fit your software development lifecycle.

### Production-context filtering for security alerts
- If you add storage and deployment records, you can filter GitHub Dependabot alerts, GitHub code scanning alerts, and security campaigns based on what’s deployed or exposed in production, including:
- artifact-registry and artifact-registry-url
- has:deployment and runtime-risk
- Combine these with existing filters like EPSS and CVSS scores to focus your remediation efforts on the vulnerabilities that matter most.

### How to link artifacts to GitHub
- Artifact attestations : GitHub’s attest-build-provenance action can automatically create storage records when you publish artifacts.
- Partner integrations : Microsoft Defender for Cloud and JFrog Artifactory can send records directly to GitHub.
- REST API : Upload storage and deployment records programmatically for any artifact, from any source.

### Additional resources
- About linked artifacts
- Artifact metadata API reference
- Prioritize security alerts based on production context
- Microsoft Defender for Cloud integration with GitHub Advanced Security
- Use the GitHub and JFrog integration for secure, traceable builds
- Join the discussion in GitHub Community .

## Impact / Who’s Affected
- Our launch partners—Microsoft Defender for Cloud (for deployment and runtime data, in public preview) and JFrog Artifactory (for storage and promotion context)—have built native integrations you can enable without additional configuration.

## Article Content (cleaned)
You can now link build artifacts like containers and binaries to GitHub and add storage and deployment context, even if the artifacts live outside GitHub. This helps you get code\-to\-cloud traceability and prioritize security work based on what’s actually running in production.


## [What’s new](#whats-new)


### [Artifact metadata APIs](#artifact-metadata-apis)


New REST API endpoints let you associate build artifacts with their storage location, track promotion through your release pipeline, and add production context like deployment data and runtime risk:


* **[Storage records](https://docs.github.com/rest/orgs/artifact-metadata#create-artifact-metadata-storage-record)** capture an artifact’s location in a package registry.
* **[Deployment records](https://docs.github.com/rest/orgs/artifact-metadata#create-an-artifact-deployment-record)** capture where an artifact is deployed and runtime risk factors such as whether the deployed workload is exposed to the internet or processes sensitive data.


You can call these APIs from your CI/CD workflows, external CD tooling, or cloud runtime monitors. Our launch partners—Microsoft Defender for Cloud (for deployment and runtime data, in public preview) and JFrog Artifactory (for storage and promotion context)—have built native integrations you can enable without additional configuration.


### [Linked artifacts view](#linked-artifacts-view)


A new view in your organization’s **Packages** tab displays all linked artifacts with their attestations, storage locations, and deployment history. This gives you unified visibility across your software supply chain.


If you use [GitHub artifact attestations](https://docs.github.com/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations), each artifact is cryptographically bound to its source repository and build workflow, helping you achieve [SLSA Build Level 3](https://github.blog/enterprise-software/devsecops/enhance-build-security-and-reach-slsa-level-3-with-github-artifact-attestations/) security. The artifact view surfaces all attestations created for an artifact, including build provenance, attested SBOMs, and any custom attestations that fit your software development lifecycle.


### [Production\-context filtering for security alerts](#production-context-filtering-for-security-alerts)


If you add storage and deployment records, you can filter GitHub Dependabot alerts, GitHub code scanning alerts, and security campaigns based on what’s deployed or exposed in production, including:


* `artifact-registry` and `artifact-registry-url`
* `has:deployment` and `runtime-risk`


Combine these with [existing filters like EPSS and CVSS scores](https://docs.github.com/code-security/how-tos/manage-security-alerts/manage-dependabot-alerts/viewing-and-updating-dependabot-alerts#prioritizing-dependabot-alerts) to focus your remediation efforts on the vulnerabilities that matter most.


## [How to link artifacts to GitHub](#how-to-link-artifacts-to-github)


* **Artifact attestations**: GitHub’s [`attest-build-provenance` action](https://github.com/marketplace/actions/attest-build-provenance) can automatically create storage records when you publish artifacts.
* **Partner integrations**: Microsoft Defender for Cloud and JFrog Artifactory can send records directly to GitHub.
* **REST API**: Upload storage and deployment records programmatically for any artifact, from any source.


## [Additional resources](#additional-resources)


* [About linked artifacts](https://docs.github.com/code-security/concepts/supply-chain-security/linked-artifacts)
* [Artifact metadata API reference](https://docs.github.com/rest/orgs/artifact-metadata)
* [Prioritize security alerts based on production context](https://docs.github.com/code-security/tutorials/secure-your-organization/prioritize-alerts-in-production-code)
* [Microsoft Defender for Cloud integration with GitHub Advanced Security](https://learn.microsoft.com/azure/defender-for-cloud/github-advanced-security-overview)
* [Use the GitHub and JFrog integration for secure, traceable builds](https://github.blog/enterprise-software/devsecops/how-to-use-the-github-and-jfrog-integration-for-secure-traceable-builds-from-commit-to-production/)


Join the discussion in [GitHub Community](https://github.com/orgs/community/discussions/categories/announcements).
