---
title: "GitHub Spark: Improvements, DPA coverage, & dedicated SKU"
date: "2025-12-10"
type: "improvements"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-10-github-spark-improvements-dpa-coverage-dedicated-sku"
fetched_at: "2026-02-03T14:40:05.684909Z"
---

# GitHub Spark: Improvements, DPA coverage, & dedicated SKU

## Overview
As of October 27th, Spark is covered by the GitHub Data Protection Agreement, which means how data is handled in Spark matches products in general availability, even though it’s still currently in public preview. This enables organizations with stricter data requirements to leverage Spark like any other generally available product. To learn more, read our documentation about how DPA applies to preview features .

## Detailed Explanation
### Spark is covered by the GitHub Data Protection Agreement
- As of October 27th, Spark is covered by the GitHub Data Protection Agreement, which means how data is handled in Spark matches products in general availability, even though it’s still currently in public preview. This enables organizations with stricter data requirements to leverage Spark like any other generally available product. To learn more, read our documentation about how DPA applies to preview features .

### Dedicated SKU & budget controls for Spark
- Organization admins will now see a dedicated SKU for Spark in their billing views. This means admins can view spending for Spark separately from all other Copilot usage in billing dashboards and CSV exports. They can also set granular premium request budgets and overage policies specifically for Spark. Admins also have the option to set a bundled premium request budget for all products that leverage premium requests. These can all be managed in the Billing and licensing tab for your organization.

### Improved visual quality of generated apps
- We’ve shipped changes to the Spark agent to improve the visual quality of generated apps. You should now see apps with more unique designs and higher quality UI and UX. Check out some examples of improvements below:

### Agent improvements
- The Spark agent now better respects previous manual user edits, ensuring it doesn’t overwrite any manual changes made by users.
- We also made improvements to how our agent handles producing highly complex apps that go beyond the context window of available models, helping ensure that even for highly complex use cases, we can produce apps.

### Repository creation org admin setting
- Org admins can now force repository creation for all Sparks into the organization rather than personal user accounts. This setting is off by default, and can be enabled by org admins on the Copilot Settings page.

### Other improvements
- Numerous accessibility improvements to make building and editing sparks even more accessible to all users.
- We now show the live preview of your app as soon as all code generation is completed by the agent so you can start interacting with your app as quickly as possible.
- We removed test paths for a specific custom domain used in development of Spark to help eliminate potential security risks.
- Multiple bug fixes for issues that led to UI, iteration, publishing, and repository creation issues.
- Improvements to ensure no manual commits made to sparks are lost.
- Changes to the Spark UI to prevent users from being able to submit multiple simultaneous requests to the agent which led to errors.

### Try out these improvements today
- Visit github.com/spark to build your next app.

## Key Changes
- The Spark agent now better respects previous manual user edits, ensuring it doesn’t overwrite any manual changes made by users.
- We also made improvements to how our agent handles producing highly complex apps that go beyond the context window of available models, helping ensure that even for highly complex use cases, we can produce apps.
- Numerous accessibility improvements to make building and editing sparks even more accessible to all users.
- We now show the live preview of your app as soon as all code generation is completed by the agent so you can start interacting with your app as quickly as possible.
- We removed test paths for a specific custom domain used in development of Spark to help eliminate potential security risks.
- Multiple bug fixes for issues that led to UI, iteration, publishing, and repository creation issues.
- Improvements to ensure no manual commits made to sparks are lost.
- Changes to the Spark UI to prevent users from being able to submit multiple simultaneous requests to the agent which led to errors.
- Visit github.com/spark to build your next app.

## Impact / Who’s Affected
- Spark is covered by the GitHub Data Protection Agreement As of October 27th, Spark is covered by the GitHub Data Protection Agreement, which means how data is handled in Spark matches products in general availability, even though it’s still currently in public preview.
- This enables organizations with stricter data requirements to leverage Spark like any other generally available product.

## Insights (derived from article language)
- To learn more, read our documentation about how DPA applies to preview features .
- You should now see apps with more unique designs and higher quality UI and UX.

## Article Content (cleaned)
### [We’ve released a number of improvements, a dedicated SKU for Spark, and ensured Spark is covered by the GitHub DPA! Read on to hear about all of the changes.](#weve-released-a-number-of-improvements-a-dedicated-sku-for-spark-and-ensured-spark-is-covered-by-the-github-dpa-read-on-to-hear-about-all-of-the-changes)


## [Spark is covered by the GitHub Data Protection Agreement](#spark-is-covered-by-the-github-data-protection-agreement)


As of October 27th, Spark is covered by the GitHub Data Protection Agreement, which means how data is handled in Spark matches products in general availability, even though it’s still currently in public preview. This enables organizations with stricter data requirements to leverage Spark like any other generally available product. To learn more, read [our documentation about how DPA applies to preview features](https://docs.github.com/site-policy/github-terms/github-dpa-previews).


## [Dedicated SKU \& budget controls for Spark](#dedicated-sku-budget-controls-for-spark)


Organization admins will now see a dedicated SKU for Spark in their billing views. This means admins can view spending for Spark separately from all other Copilot usage in billing dashboards and CSV exports. They can also set granular premium request budgets and overage policies specifically for Spark. Admins also have the option to set a bundled premium request budget for all products that leverage premium requests. These can all be managed in the **Billing and licensing** tab for your organization.  

![Spark SKU in billing view](https://github.com/user-attachments/assets/c951537d-9d12-42d7-974c-8f85fff3fc8c)  

![Sample granular SKU budget settings](https://github.com/user-attachments/assets/5af97045-d435-486b-810e-f22a1c5e49fd)


## [Improved visual quality of generated apps](#improved-visual-quality-of-generated-apps)


We’ve shipped changes to the Spark agent to improve the visual quality of generated apps. You should now see apps with more unique designs and higher quality UI and UX. Check out some examples of improvements below:  

![Side-by-side comparison of to-do app generated after and before improvements](https://github.com/user-attachments/assets/d1f76d73-ea17-4a04-be8d-e84fbd598f02)  

![Side-by-side comparison of actions app generated after and before improvements](https://github.com/user-attachments/assets/c63be308-c281-47e2-8820-9f6720697362)  

![Side-by-side comparison of timer app generated after and before improvements](https://github.com/user-attachments/assets/be8ede73-d3d4-4509-ba2e-45fe2c2c5f0f)


## [Agent improvements](#agent-improvements)


* The Spark agent now better respects previous manual user edits, ensuring it doesn’t overwrite any manual changes made by users.
* We also made improvements to how our agent handles producing highly complex apps that go beyond the context window of available models, helping ensure that even for highly complex use cases, we can produce apps.


## [Repository creation org admin setting](#repository-creation-org-admin-setting)


Org admins can now force repository creation for all Sparks into the organization rather than personal user accounts. This setting is **off** by default, and can be enabled by org admins on the Copilot Settings page.  

![Org admin setting for spark repository creation rules](https://github.com/user-attachments/assets/7e69b3be-5fe9-440f-8c93-7b89f5f7cc4a)


## [Other improvements](#other-improvements)


* Numerous accessibility improvements to make building and editing sparks even more accessible to all users.
* We now show the live preview of your app as soon as all code generation is completed by the agent so you can start interacting with your app as quickly as possible.
* We removed test paths for a specific custom domain used in development of Spark to help eliminate potential security risks.
* Multiple bug fixes for issues that led to UI, iteration, publishing, and repository creation issues.
* Improvements to ensure no manual commits made to sparks are lost.
* Changes to the Spark UI to prevent users from being able to submit multiple simultaneous requests to the agent which led to errors.


## [Try out these improvements today](#try-out-these-improvements-today)


Visit [github.com/spark](https://github.com/spark) to build your next app.
