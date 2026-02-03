---
title: "Conda ecosystem support for Dependabot version updates now generally available"
date: "2025-12-16"
type: "improvements"
labels: ["supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-16-conda-ecosystem-support-for-dependabot-now-generally-available"
fetched_at: "2026-02-03T14:50:54.902726Z"
---

# Conda ecosystem support for Dependabot version updates now generally available

## Overview
Dependabot now supports parsing and updating environment.yml Conda environment specification files. This release includes version updates for Conda-based projects.

## Detailed Explanation
### Overview
- Dependabot now supports parsing and updating environment.yml Conda environment specification files. This release includes version updates for Conda-based projects.

### Why it matters
- Many projects rely on Conda for managing dependencies and environments. Extending Dependabot’s support to Conda allows teams who use Conda to benefit from automated dependency management. Organizations can more effectively keep their Conda-based environments up to date, reducing the risk of vulnerabilities and improving their project security.

### Details
- Dependabot will detect Conda environment files and create update pull requests. These updates cover version updates for dependencies listed in the Conda manifest files.
- To help you get started, full documentation, examples, and usage notes are available in the Dependabot documentation .

### Availability
- This capability is available on github.com today and will be coming to GitHub Enterprise Server (GHES) with version 3.21.
- Join the discussion within the Dependabot Community .

## Caveats / Limitations
- To help you get started, full documentation, examples, and usage notes are available in the Dependabot documentation .

## Article Content (cleaned)
Dependabot now supports parsing and updating `environment.yml` Conda environment specification files. This release includes version updates for Conda\-based projects.


### [Why it matters](#why-it-matters)


Many projects rely on Conda for managing dependencies and environments. Extending Dependabot’s support to Conda allows teams who use Conda to benefit from automated dependency management. Organizations can more effectively keep their Conda\-based environments up to date, reducing the risk of vulnerabilities and improving their project security.


### [Details](#details)


Dependabot will detect Conda environment files and create update pull requests. These updates cover version updates for dependencies listed in the Conda manifest files.


To help you get started, full documentation, examples, and usage notes are available in the [Dependabot documentation](https://docs.github.com/code-security/dependabot/ecosystems-supported-by-dependabot/supported-ecosystems-and-repositories#supported-ecosystems-and-repositories).


### [Availability](#availability)


This capability is available on github.com today and will be coming to GitHub Enterprise Server (GHES) with version 3\.21\.


Join the discussion within the [Dependabot Community](https://github.com/dependabot/dependabot-core/issues/2227).
