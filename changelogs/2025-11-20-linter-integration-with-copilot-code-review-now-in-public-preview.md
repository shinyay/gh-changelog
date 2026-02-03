---
title: "Linter integration with Copilot code review now in public preview"
date: "2025-11-20"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-20-linter-integration-with-copilot-code-review-now-in-public-preview"
fetched_at: "2026-02-03T14:50:55.164057Z"
---

# Linter integration with Copilot code review now in public preview

## Overview
Copilot code review now surfaces actionable feedback from linters, so the small stuff is never missed—and you can customize which linters are used via repository rulesets. This feature is available in public preview for paid GitHub users.

## Detailed Explanation
### Overview
- Copilot code review now surfaces actionable feedback from linters, so the small stuff is never missed—and you can customize which linters are used via repository rulesets. This feature is available in public preview for paid GitHub users.

### New static analysis tools in Copilot code review
- In addition to CodeQL quality detections enabled at GitHub Universe 2025, you can now get results from the following static analysis tools in Copilot code review:
- ESLint highlights issues for JavaScript and TypeScript projects.
- PMD scans for problems in Java, Apex, and other supported languages.

### Configure which tools are used with a repository rule
- While CodeQL is on by default for public preview participants, you can now control which tools you want Copilot code review using. We’ve added a new repository rule, “Manage static analysis tools in Copilot code review,” which allows you to turn CodeQL, ESLint, and PMD on and off. With this rule, you can enable these features at the Enterprise, Organization, Team or Repository level, and do specific branch and repo targeting.
- Demo of opening the repository ruleset page and creating a ruleset with the new rule
- Go to Settings > Rules > Rulesets in a repository where you have admin access.
- Add or edit a ruleset and select the new “Manage static analysis tools in Copilot code review” rule.
- Select which static analysis tools you want Copilot code review to include: ESLint, PMD, and/or CodeQL. Note that CodeQL is enabled by default, and can now be disabled via the rule.
- Save the rule and open a new pull request to see Copilot code review run with your new linter setup.
- Learn more about configuring repository rules for Copilot code review .
- Join the discussion within the GitHub Community .

## Impact / Who’s Affected
- This feature is available in public preview for paid GitHub users.
- Configure which tools are used with a repository rule While CodeQL is on by default for public preview participants, you can now control which tools you want Copilot code review using.

## Caveats / Limitations
- Note that CodeQL is enabled by default, and can now be disabled via the rule.

## Insights (derived from article language)
- Note that CodeQL is enabled by default, and can now be disabled via the rule.
- Learn more about configuring repository rules for Copilot code review .

## Article Content (cleaned)
Copilot code review now surfaces actionable feedback from linters, so the small stuff is never missed—and you can customize which linters are used via repository rulesets. This feature is available in public preview for paid GitHub users.


### [New static analysis tools in Copilot code review](#new-static-analysis-tools-in-copilot-code-review)


In addition to CodeQL quality detections enabled at GitHub Universe 2025, you can now get results from the following static analysis tools in Copilot code review:


* ESLint highlights issues for JavaScript and TypeScript projects.
* PMD scans for problems in Java, Apex, and other supported languages.


### [Configure which tools are used with a repository rule](#configure-which-tools-are-used-with-a-repository-rule)


While CodeQL is on by default for public preview participants, you can now control which tools you want Copilot code review using. We’ve added a new repository rule, “Manage static analysis tools in Copilot code review,” which allows you to turn CodeQL, ESLint, and PMD on and off. With this rule, you can enable these features at the Enterprise, Organization, Team or Repository level, and do specific branch and repo targeting.


  

Demo of opening the repository ruleset page and creating a ruleset with the new rule  




#### [Get started](#get-started)


1. Go to **Settings** \> **Rules** \> **Rulesets** in a repository where you have admin access.
2. Add or edit a ruleset and select the new “Manage static analysis tools in Copilot code review” rule.
3. Select which static analysis tools you want Copilot code review to include: ESLint, PMD, and/or CodeQL. *Note that CodeQL is enabled by default, and can now be disabled via the rule.*
4. Save the rule and open a new pull request to see Copilot code review run with your new linter setup.


[Learn more about configuring repository rules for Copilot code review](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/manage-tools).


Join the discussion within the [GitHub Community](https://github.com/orgs/community/discussions/categories/copilot-conversations).
