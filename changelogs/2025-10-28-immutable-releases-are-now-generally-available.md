---
title: "Immutable releases are now generally available"
date: "2025-10-28"
type: "improvements"
labels: ["supply chain security", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-immutable-releases-are-now-generally-available"
fetched_at: "2026-02-03T14:40:06.650256Z"
---

# Immutable releases are now generally available

## Overview
GitHub releases now support immutability, adding a new layer of supply chain security. With immutable releases, assets and tags are protected from tampering after publication, so the software you publish—and your users consume—remains secure and trustworthy.

## Detailed Explanation
### Overview
- GitHub releases now support immutability, adding a new layer of supply chain security. With immutable releases, assets and tags are protected from tampering after publication, so the software you publish—and your users consume—remains secure and trustworthy.

### About immutable releases
- Immutable releases offer:
- Immutable assets : Once you publish a release as immutable, its assets can’t be added, modified, or deleted. This helps protect distributed artifacts from supply chain attacks.
- Tag protection : Tags for new immutable releases are protected and can’t be deleted or moved.
- Release attestations : Immutable releases receive signed attestations so you can easily verify the authenticity and integrity of assets, both on GitHub and in external environments.

### How to enable immutable releases
- You can enable immutable releases at the repository or organization level in your settings. Once enabled:
- All new releases are immutable (i.e., assets are locked and tags are protected).
- Existing releases remain mutable unless you republish them.
- Disabling immutability doesn’t affect releases created while it was enabled. They remain immutable.

### Release attestations and verification
- Release attestations let you verify that an artifact is authentic and unchanged, even outside GitHub. Attestations use the Sigstore bundle format , so you can easily verify releases and assets using the GitHub CLI or integrate with any Sigstore-compatible tooling to automate policy enforcement in your CI/CD pipelines. For instructions on how to verify the integrity of a release, see our docs on verifying the integrity of a release .
- We’d love your feedback. Share your thoughts and questions on the GitHub Community .
- For more information, see our immutable releases documentation .

## Article Content (cleaned)
GitHub releases now support immutability, adding a new layer of supply chain security. With immutable releases, assets and tags are protected from tampering after publication, so the software you publish—and your users consume—remains secure and trustworthy.


### [About immutable releases](#about-immutable-releases)


Immutable releases offer:


* **Immutable assets**: Once you publish a release as immutable, its assets can’t be added, modified, or deleted. This helps protect distributed artifacts from supply chain attacks.
* **Tag protection**: Tags for new immutable releases are protected and can’t be deleted or moved.
* **Release attestations**: Immutable releases receive signed attestations so you can easily verify the authenticity and integrity of assets, both on GitHub and in external environments.


### [How to enable immutable releases](#how-to-enable-immutable-releases)


You can enable immutable releases at the repository or organization level in your settings. Once enabled:


* All new releases are immutable (i.e., assets are locked and tags are protected).
* Existing releases remain mutable unless you republish them.


Disabling immutability doesn’t affect releases created while it was enabled. They remain immutable.


### [Release attestations and verification](#release-attestations-and-verification)


Release attestations let you verify that an artifact is authentic and unchanged, even outside GitHub. Attestations use the [Sigstore bundle format](https://docs.sigstore.dev/about/bundle/), so you can easily verify releases and assets using the GitHub CLI or integrate with any Sigstore\-compatible tooling to automate policy enforcement in your CI/CD pipelines. For instructions on how to verify the integrity of a release, see [our docs on verifying the integrity of a release](https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/verifying-the-integrity-of-a-release?tool=cli?utm_source=changelog-docs-immutable-releases&utm_medium=changelog&utm_campaign=universe25).


We’d love your feedback. Share your thoughts and questions on the [GitHub Community](https://gh.io/immutable-releases-ga?utm_source=changelog-community-immutable-releases&utm_medium=changelog&utm_campaign=universe25).


For more information, see our [immutable releases documentation](https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/immutable-releases?utm_source=changelog-docs-immutable-releases&utm_medium=changelog&utm_campaign=universe25).
