---
title: "Dependabot-based dependency graphs for Go"
date: "2025-12-09"
type: "improvements"
labels: ["supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-09-dependabot-dgs-for-go"
fetched_at: "2026-02-03T14:50:55.028774Z"
---

# Dependabot-based dependency graphs for Go

## Overview
Continuing the supply chain security theme of continually improving our package ecosystem support, Go projects will now see more complete and accurate transitive dependency trees in their dependency graphs and Software Bill of Materials (SBOMs).

## Detailed Explanation
### Overview
- Continuing the supply chain security theme of continually improving our package ecosystem support, Go projects will now see more complete and accurate transitive dependency trees in their dependency graphs and Software Bill of Materials (SBOMs).
- Since Go resolves dependency versions dynamically, getting an accurate picture of a project’s dependencies cannot rely on static parsing. Now, when a commit updates a project’s go.mod , GitHub runs a new type of Dependabot job that builds a dependency snapshot and uploads it to the Dependency Submission API.
- This approach is similar to dependency autosubmission for other ecosystems, but it will not incur charges for actions minutes. It can also access organization-wide configurations for private registries you’ve set up for Dependabot.
- For more information, see Configuring the dependency graph .

## Article Content (cleaned)
Continuing the supply chain security theme of continually improving our package ecosystem support, Go projects will now see more complete and accurate transitive dependency trees in their dependency graphs and Software Bill of Materials (SBOMs).


Since Go resolves dependency versions dynamically, getting an accurate picture of a project’s dependencies cannot rely on static parsing. Now, when a commit updates a project’s `go.mod`, GitHub runs a new type of Dependabot job that builds a dependency snapshot and uploads it to the Dependency Submission API.


This approach is similar to dependency autosubmission for other ecosystems, but it will not incur charges for actions minutes. It can also access organization\-wide configurations for private registries you’ve set up for Dependabot.


For more information, see [Configuring the dependency graph](https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph).
