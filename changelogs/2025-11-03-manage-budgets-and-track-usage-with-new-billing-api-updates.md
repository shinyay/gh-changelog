---
title: "Manage budgets and track usage with new billing API updates"
date: "2025-11-03"
type: "new releases"
labels: ["account management", "enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-03-manage-budgets-and-track-usage-with-new-billing-api-updates"
fetched_at: "2026-02-03T14:40:06.389484Z"
---

# Manage budgets and track usage with new billing API updates

## Overview
We’re expanding our billing APIs with new capabilities to help you programmatically manage budgets, track usage, and access cost center data.

## Detailed Explanation
### Overview
- We’re expanding our billing APIs with new capabilities to help you programmatically manage budgets, track usage, and access cost center data.

### Manage budgets via APIs
- You can now manage the full lifecycle of budgets via API. Previously, budgets could only be managed through the UI. Now, you can programmatically create, update, and delete budgets, as well as adjust the budget amount and alert notifications. There is currently a temporary limit of 50 budgets per account. This API is now available in public preview.
- For more details, refer to our documentation on REST API endpoints for budgets .

### Track usage with the new Usage summary API
- The new Usage summary API allows you to retrieve usage information for your entire account or filter by specific organizations, repositories, cost centers, products, or SKUs. Usage can be queried by year, month, or day. This API is now available in public preview.
- For more details, refer to our documentation on the Usage summary REST API endpoint .

### Additional improvements
- Cost center API improvement : The Get all cost centers for an enterprise API now includes an optional state parameter, which allows you to only get active cost centers by adding ?state=active when calling the endpoint.
- Usage report API changes : We’ve removed the hour parameter from the existing usage report API and reduced the granularity of the response when using the day parameter to provide daily totals instead of hourly breakdowns. For more details, refer to our documentation on the Get billing usage report for an enterprise REST API endpoint .

### Who can use these features
- Enterprise owners and billing managers on GitHub Enterprise plans.
- Organization owners on GitHub Team plans.
- Individuals on personal plans.
- Join the discussion within GitHub Community .

## Key Changes
- Cost center API improvement : The Get all cost centers for an enterprise API now includes an optional state parameter, which allows you to only get active cost centers by adding ?state=active when calling the endpoint.
- Usage report API changes : We’ve removed the hour parameter from the existing usage report API and reduced the granularity of the response when using the day parameter to provide daily totals instead of hourly breakdowns. For more details, refer to our documentation on the Get billing usage report for an enterprise REST API endpoint .
- Enterprise owners and billing managers on GitHub Enterprise plans.
- Organization owners on GitHub Team plans.
- Individuals on personal plans.
- Join the discussion within GitHub Community .

## Impact / Who’s Affected
- Previously, budgets could only be managed through the UI.
- This API is now available in public preview.
- Additional improvements Cost center API improvement : The Get all cost centers for an enterprise API now includes an optional state parameter, which allows you to only get active cost centers by adding ?state=active when calling the endpoint.

## Caveats / Limitations
- Previously, budgets could only be managed through the UI.
- Additional improvements Cost center API improvement : The Get all cost centers for an enterprise API now includes an optional state parameter, which allows you to only get active cost centers by adding ?state=active when calling the endpoint.

## Insights (derived from article language)
- For more details, refer to our documentation on REST API endpoints for budgets .
- For more details, refer to our documentation on the Usage summary REST API endpoint .
- For more details, refer to our documentation on the Get billing usage report for an enterprise REST API endpoint .

## Article Content (cleaned)
We’re expanding our billing APIs with new capabilities to help you programmatically manage budgets, track usage, and access cost center data.


### [Manage budgets via APIs](#manage-budgets-via-apis)


You can now manage the full lifecycle of budgets via API. Previously, budgets could only be managed through the UI. Now, you can programmatically create, update, and delete budgets, as well as adjust the budget amount and alert notifications. There is currently a temporary limit of 50 budgets per account. This API is now available in public preview.


For more details, refer to [our documentation on REST API endpoints for budgets](https://gh.io/budget-api-docs).


### [Track usage with the new Usage summary API](#track-usage-with-the-new-usage-summary-api)


The new Usage summary API allows you to retrieve usage information for your entire account or filter by specific organizations, repositories, cost centers, products, or SKUs. Usage can be queried by year, month, or day. This API is now available in public preview.


For more details, refer to [our documentation on the Usage summary REST API endpoint](https://gh.io/usage-summary-api).


### [Additional improvements](#additional-improvements)


* **Cost center API improvement**: The [Get all cost centers for an enterprise API](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/cost-centers?apiVersion=2022-11-28#get-all-cost-centers-for-an-enterprise) now includes an optional `state` parameter, which allows you to only get active cost centers by adding `?state=active` when calling the endpoint.
* **Usage report API changes**: We’ve removed the `hour` parameter from the existing usage report API and reduced the granularity of the response when using the `day` parameter to provide daily totals instead of hourly breakdowns. For more details, refer to [our documentation on the Get billing usage report for an enterprise REST API endpoint](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/usage?apiVersion=2022-11-28#get-billing-usage-report-for-an-enterprise).


### [Who can use these features](#who-can-use-these-features)


* Enterprise owners and billing managers on GitHub Enterprise plans.
* Organization owners on GitHub Team plans.
* Individuals on personal plans.


Join the discussion within [GitHub Community](https://gh.io/billing-api-community-feedback).
