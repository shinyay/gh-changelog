---
title: "Dependabot version updates now support Bazel"
date: "2025-12-16"
type: "new releases"
labels: ["supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-16-dependabot-version-updates-now-support-bazel"
fetched_at: "2026-02-03T14:50:54.911102Z"
---

# Dependabot version updates now support Bazel

## Overview
Developers can now use Dependabot to automatically keep their Bazel dependencies up to date. For projects that use Bazel—either Bzlmod or WORKSPACE—Dependabot version updates can now ensure dependencies stay current with the latest releases.

## Detailed Explanation
### Overview
- Developers can now use Dependabot to automatically keep their Bazel dependencies up to date. For projects that use Bazel—either Bzlmod or WORKSPACE—Dependabot version updates can now ensure dependencies stay current with the latest releases.
- A huge thanks to the Bazel team for their contributions and collaboration bringing support to Dependabot.

### Background
- The open source community’s top requests for Bazel support for Dependabot included:
- Proper lockfile generation
- *.MODULE.bazel support
- WORKSPACE support (still widely used despite upcoming deprecation)
- Bazel uses two dependency systems, both the modern Bzlmod system ( MODULE.bazel files) and the legacy WORKSPACE system. Community feedback showed many teams still rely on WORKSPACE, so we built support for both. Additionally, Bazel’s MODULE.bazel.lock files capture complex transitive dependency graphs, including module extensions and repository rules. Incorrect lockfile generation breaks reproducible builds, so we worked closely with the Bazel community to get this right.

### Community partnership
- The Bazel community provided critical guidance:
- Fabian Meumertzheim: Lockfile semantics and behavior matching
- Yun Peng: Testing, validation, and implementation data
- Alex Eagle: File naming conventions and *.MODULE.bazel patterns
- Thank you especially to these folks, and to everyone who tested and provided feedback during our preview support for this ecosystem.

### How it works
- Dependency detection: Dependabot scans your MODULE.bazel , *.MODULE.bazel , or WORKSPACE files and checks the Bazel central registry for updates.
- Lockfile management: Dependabot regenerates lockfiles to maintain reproducible builds.
- Pull requests: Dependabot opens pull requests with updated declarations, regenerated lockfiles, release notes, and compatibility information.

### Getting started
- Requirements include:
- Bazel 7, 8, or 9
- A MODULE.bazel or WORKSPACE file at the repository root
- Engage with the Dependabot open source community on the topic of Bazel support.
- Learn more in our Dependabot version updates documentation .
- Learn more about Bazel .
- A MODULE.bazel or WORKSPACE file at the repository root
- Engage with the Dependabot open source community on the topic of Bazel support.

## Caveats / Limitations
- Pull requests: Dependabot opens pull requests with updated declarations, regenerated lockfiles, release notes, and compatibility information.

## Insights (derived from article language)
- Learn more in our Dependabot version updates documentation .
- Learn more about Bazel .

## Article Content (cleaned)
Developers can now use Dependabot to automatically keep their Bazel dependencies up to date. For projects that use Bazel—either Bzlmod or WORKSPACE—Dependabot version updates can now ensure dependencies stay current with the latest releases.


A huge thanks to the Bazel team for their contributions and collaboration bringing support to Dependabot.


## [Background](#background)


The open source community’s [top requests for Bazel support for Dependabot](https://github.com/bazelbuild/bazel/discussions/27142) included:


* Proper lockfile generation
* `*.MODULE.bazel` support
* WORKSPACE support (still widely used despite upcoming deprecation)


Bazel uses two dependency systems, both the modern Bzlmod system (`MODULE.bazel` files) and the legacy WORKSPACE system. Community feedback showed many teams still rely on WORKSPACE, so we built support for both. Additionally, Bazel’s `MODULE.bazel.lock` files capture complex transitive dependency graphs, including module extensions and repository rules. Incorrect lockfile generation breaks reproducible builds, so we worked closely with the Bazel community to get this right.


## [Community partnership](#community-partnership)


The Bazel community provided critical guidance:


* **Fabian Meumertzheim:** Lockfile semantics and behavior matching
* **Yun Peng:** Testing, validation, and implementation data
* **Alex Eagle:** File naming conventions and `*.MODULE.bazel` patterns


Thank you especially to these folks, and to everyone who tested and provided feedback during our preview support for this ecosystem.


## [How it works](#how-it-works)


1. **Dependency detection:** Dependabot scans your `MODULE.bazel`, `*.MODULE.bazel`, or WORKSPACE files and checks the Bazel central registry for updates.
2. **Lockfile management:** Dependabot regenerates lockfiles to maintain reproducible builds.
3. **Pull requests:** Dependabot opens pull requests with updated declarations, regenerated lockfiles, release notes, and compatibility information.


## [Getting started](#getting-started)


Requirements include:


* Bazel 7, 8, or 9
* A `MODULE.bazel` or `WORKSPACE` file at the repository root
* Engage with [the Dependabot open source community](https://github.com/dependabot/dependabot-core/issues/2196) on the topic of Bazel support.
* Learn more in [our Dependabot version updates documentation](https://docs.github.com/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates).
* Learn more about [Bazel](https://bazel.build/).
