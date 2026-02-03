---
title: "Organization custom properties now generally available"
date: "2026-01-13"
type: "improvements"
labels: ["enterprise management tools", "platform governance"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-13-organization-custom-properties-now-generally-available"
fetched_at: "2026-02-03T14:40:05.231075Z"
---

# Organization custom properties now generally available

## Overview
Organization custom properties are now generally available, giving enterprise administrators a powerful way to tag organizations with metadata and automatically target enterprise rulesets.

## Detailed Explanation
### Overview
- Organization custom properties are now generally available, giving enterprise administrators a powerful way to tag organizations with metadata and automatically target enterprise rulesets.

### Why organization custom properties
- Enterprises often organize their GitHub presence around business units, geographic regions, compliance frameworks, or development stages. Until now, applying consistent rulesets meant manually selecting organizations one-by-one or relying on naming conventions that don’t scale.
- With organization custom properties, you can:
- Define once, apply everywhere: Tag organizations with properties like region: EMEA , compliance: SOC2 , or business-unit: Platform and let your rulesets do the rest.
- Eliminate configuration drift: Rulesets automatically apply to any organization matching your criteria, even newly created ones.
- Adapt to your enterprise structure: Whether you organize by department, regulatory requirements, or project lifecycle, custom properties meet you where you are.
- Imagine you need to enforce stricter code review requirements for all organizations handling customer data in the EU. Instead of maintaining a manual list, create a ruleset that targets region: EU and data-classification: customer-data . When a new EU-based team spins up their organization, the policies apply automatically.

### How it works
- Enterprise administrators define custom properties at the enterprise level and assign values to individual organizations. Properties support:
- Single-select : Choose one value from a predefined list
- Multi-select : Choose multiple values from a predefined list
- Text : Enter free-form text
- True/false : Set a boolean value
- URL : Enter URL value
- Once you’ve tagged your organizations, enterprise rulesets can target them based on any combination of properties.

### Get started
- Organization custom properties are available to all GitHub Enterprise Cloud customers.
- Enterprise administrators can access custom properties in the organization section of their enterprise settings.
- For more information, see “ Managing custom properties for organizations in your enterprise ” in GitHub Docs.

## Impact / Who’s Affected
- Organization custom properties are now generally available, giving enterprise administrators a powerful way to tag organizations with metadata and automatically target enterprise rulesets.

## Article Content (cleaned)
Organization custom properties are now generally available, giving enterprise administrators a powerful way to tag organizations with metadata and automatically target enterprise rulesets.


## [Why organization custom properties](#why-organization-custom-properties)


Enterprises often organize their GitHub presence around business units, geographic regions, compliance frameworks, or development stages. Until now, applying consistent rulesets meant manually selecting organizations one\-by\-one or relying on naming conventions that don’t scale.


With organization custom properties, you can:


* **Define once, apply everywhere:** Tag organizations with properties like `region: EMEA`, `compliance: SOC2`, or `business-unit: Platform` and let your rulesets do the rest.
* **Eliminate configuration drift:** Rulesets automatically apply to any organization matching your criteria, even newly created ones.
* **Adapt to your enterprise structure:** Whether you organize by department, regulatory requirements, or project lifecycle, custom properties meet you where you are.


Imagine you need to enforce stricter code review requirements for all organizations handling customer data in the EU. Instead of maintaining a manual list, create a ruleset that targets `region: EU` and `data-classification: customer-data`. When a new EU\-based team spins up their organization, the policies apply automatically.


## [How it works](#how-it-works)


![A screenshot showing the "region" custom property settings, including its name, description, type, options, and other attributes](https://github.com/user-attachments/assets/f802250c-45ed-4532-8d49-1bc7333ccc9b)


Enterprise administrators define custom properties at the enterprise level and assign values to individual organizations. Properties support:


* **Single\-select**: Choose one value from a predefined list
* **Multi\-select**: Choose multiple values from a predefined list
* **Text**: Enter free\-form text
* **True/false**: Set a boolean value
* **URL**: Enter URL value


Once you’ve tagged your organizations, enterprise rulesets can target them based on any combination of properties.


![A screenshot of the "Regional Compliance" code ruleset settings, showing its evaluation status, an empty bypass list, and target organizations defined by region and compliance frameworks.](https://github.com/user-attachments/assets/19aee9db-45e6-43b9-b956-c85b58b0bdec)


## [Get started](#get-started)


Organization custom properties are available to all GitHub Enterprise Cloud customers.


Enterprise administrators can access custom properties in the organization section of their enterprise settings.


For more information, see “[Managing custom properties for organizations in your enterprise](https://gh.io/org-properties-docs)” in GitHub Docs.
