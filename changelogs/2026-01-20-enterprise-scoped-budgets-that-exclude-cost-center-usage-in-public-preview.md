---
title: "Enterprise-scoped budgets that exclude cost center usage in public preview"
date: "2026-01-20"
type: "improvements"
labels: ["enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-19-enterprise-scoped-budgets-that-exclude-cost-center-usage-in-public-preview"
fetched_at: "2026-02-03T14:40:05.148483Z"
---

# Enterprise-scoped budgets that exclude cost center usage in public preview

## Overview
GitHub Enterprise customers can now configure enterprise-scoped budgets that exclude cost center usage, allowing specific portions of an enterprise to incur additional usage while limiting the rest.

## Detailed Explanation
### Overview
- GitHub Enterprise customers can now configure enterprise-scoped budgets that exclude cost center usage, allowing specific portions of an enterprise to incur additional usage while limiting the rest.
- Previously, this required creating distinct budgets for every part of an enterprise to enforce a default limit. With this improvement, enterprises can now apply an enterprise-scoped budget that excludes cost center usage and selectively grant access to additional usage using cost centers.

### Key details
- This option is only available for enterprise-scoped budgets and can be applied to new or existing budgets.
- Existing enterprise-scoped budgets continue to include cost center usage by default.
- This option is available through the REST API, and changes to this setting are recorded in the audit log.
- To learn more, see “ Setting up budgets to control spending on metered products .”

## Impact / Who’s Affected
- Key details This option is only available for enterprise-scoped budgets and can be applied to new or existing budgets.

## Caveats / Limitations
- Key details This option is only available for enterprise-scoped budgets and can be applied to new or existing budgets.

## Insights (derived from article language)
- To learn more, see “ Setting up budgets to control spending on metered products .”

## Article Content (cleaned)
GitHub Enterprise customers can now configure enterprise\-scoped budgets that exclude cost center usage, allowing specific portions of an enterprise to incur additional usage while limiting the rest.


Previously, this required creating distinct budgets for every part of an enterprise to enforce a default limit. With this improvement, enterprises can now apply an enterprise\-scoped budget that excludes cost center usage and selectively grant access to additional usage using cost centers.


![Screenshot showing the new option to exclude cost center usage when configuring an enterprise budget](https://github.com/user-attachments/assets/30311d80-9e91-4f32-860c-4e49e5b450e9)


### [Key details](#key-details)


* This option is only available for enterprise\-scoped budgets and can be applied to new or existing budgets.
* Existing enterprise\-scoped budgets continue to include cost center usage by default.
* This option is available through the REST API, and changes to this setting are recorded in the audit log.


To learn more, see “[Setting up budgets to control spending on metered products](https://docs.github.com/enterprise-cloud@latest/billing/tutorials/set-up-budgets).”
