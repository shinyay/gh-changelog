---
title: "Deprecation of user to organization account transformation"
date: "2026-01-12"
type: "deprecations"
labels: ["account management"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-12-deprecation-of-user-to-organization-account-transformation"
fetched_at: "2026-02-03T14:50:54.823136Z"
---

# Deprecation of user to organization account transformation

## Overview
As of January 12, 2026, we’re deprecating the ability to convert a personal user account directly into an organization. You can now use the Move work flow to selectively migrate repositories to organizations while maintaining your personal account.

## Detailed Explanation
### Overview
- As of January 12, 2026, we’re deprecating the ability to convert a personal user account directly into an organization. You can now use the Move work flow to selectively migrate repositories to organizations while maintaining your personal account.
- Instead of transforming your user account, use the new Move work flow to migrate your repositories:
- Go to your user profile settings and click SSO and organizations .
- In the “Move to an organization” section, click Move work to an organization .
- Select the repositories you want to transfer.
- Choose an existing organization or create a new one.
- If you want your organization to use your current username, you’ll need to rename your personal account first:
- Change your username to something new.
- Create or move work to an organization with your original username.
- The Move work feature is not available on GHES. To migrate repositories, please follow our repository transfer documentation .

## Insights (derived from article language)
- What you should do Instead of transforming your user account, use the new Move work flow to migrate your repositories: Go to your user profile settings and click SSO and organizations .

## Article Content (cleaned)
As of January 12, 2026, we’re deprecating the ability to convert a personal user account directly into an organization. You can now use the **Move work** flow to selectively migrate repositories to organizations while maintaining your personal account.


#### [What you should do](#what-you-should-do)


Instead of transforming your user account, use the new **Move work** flow to migrate your repositories:


1. Go to your user profile settings and click **SSO and organizations**.
2. In the “Move to an organization” section, click **Move work to an organization**.
3. Select the repositories you want to transfer.
4. Choose an existing organization or create a new one.


#### [Keeping your username for the organization](#keeping-your-username-for-the-organization)


If you want your organization to use your current username, you’ll need to rename your personal account first:


1. [Change your username](https://docs.github.com/account-and-profile/how-tos/account-management/changing-your-username#changing-your-username) to something new.
2. Create or move work to an organization with your original username.


#### [For GitHub Enterprise Server users](#for-github-enterprise-server-users)


The **Move work** feature is not available on GHES. To migrate repositories, please follow our [repository transfer documentation](https://docs.github.com/enterprise-server@3.19/repositories/creating-and-managing-repositories/transferring-a-repository).
