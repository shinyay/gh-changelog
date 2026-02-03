---
title: "Improved onboarding flow for GitHub Projects"
date: "2025-11-06"
type: "improvements"
labels: ["projects and issues"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-06-improved-onboarding-flow-for-github-projects"
fetched_at: "2026-02-03T14:50:55.400701Z"
---

# Improved onboarding flow for GitHub Projects

## Overview
We’ve improved the GitHub Projects onboarding flow to help you get started faster, with options to connect and import items from a repository, set a default repository for new issues, use new default workflows to set up your project, and more.

## Detailed Explanation
### Overview
- We’ve improved the GitHub Projects onboarding flow to help you get started faster, with options to connect and import items from a repository, set a default repository for new issues, use new default workflows to set up your project, and more.

### 🚀 Key improvements
- Import items from a repository
- During onboarding, you can now choose to import open issues, open pull requests, or both from a specified repository. The selected items are automatically imported when the project is created, so you can start with your existing content right away.
- Set a default repository
- In project settings, you can now select a default repository. All new issues created in this project will be automatically associated with the selected repository.
- Pull request linked to issue workflow
- A new default workflow, Pull request linked to issue , automatically sets the status of an issue to “In progress” whenever a linked pull request exists.

### 🛠 Additional onboarding improvements
- New projects now show linked pull requests and sub-issues as default fields.
- The Team planning template now defaults to Table view instead of Board view.
- Insights and Workflows buttons have been elevated in the UI for easier discovery.
- Polishing and minor fixes to make onboarding smoother and more reliable.

### 🤖 API improvements
- We’ve made improvements to the Projects GraphQL API making it easier to automate your project workflows.
- You’ll now see project_v2_item_status_changed , added_to_project_v2 , removed_from_project_v2 , and converted_from_draft events. These events allow you to understand information such as how long an item was “In progress” before moving to “Done”.
- You can filter project items using the query argument with any project filter. Check out the ProjectsV2 GraphQL documentation for more details.

### ✍ Tell us what you think!
- Join the conversation in the GitHub Community , or select Give feedback from the project … menu to share your thoughts.

## Key Changes
- Import items from a repository
- During onboarding, you can now choose to import open issues, open pull requests, or both from a specified repository. The selected items are automatically imported when the project is created, so you can start with your existing content right away.
- Set a default repository
- In project settings, you can now select a default repository. All new issues created in this project will be automatically associated with the selected repository.
- Pull request linked to issue workflow
- A new default workflow, Pull request linked to issue , automatically sets the status of an issue to “In progress” whenever a linked pull request exists.
- New projects now show linked pull requests and sub-issues as default fields.
- The Team planning template now defaults to Table view instead of Board view.
- Insights and Workflows buttons have been elevated in the UI for easier discovery.
- Polishing and minor fixes to make onboarding smoother and more reliable.
- We’ve made improvements to the Projects GraphQL API making it easier to automate your project workflows.
- You’ll now see project_v2_item_status_changed , added_to_project_v2 , removed_from_project_v2 , and converted_from_draft events. These events allow you to understand information such as how long an item was “In progress” before moving to “Done”.
- You can filter project items using the query argument with any project filter. Check out the ProjectsV2 GraphQL documentation for more details.

## Insights (derived from article language)
- Check out the ProjectsV2 GraphQL documentation for more details. ✍ Tell us what you think!

## Article Content (cleaned)
We’ve improved the GitHub Projects onboarding flow to help you get started faster, with options to connect and import items from a repository, set a default repository for new issues, use new default workflows to set up your project, and more.


## [🚀 Key improvements](#%f0%9f%9a%80-key-improvements)


**Import items from a repository**


[https://github.blog/wp\-content/uploads/2025/11/import\_items.mp4\#t\=0\.001](https://github.blog/wp-content/uploads/2025/11/import_items.mp4#t=0.001)
During onboarding, you can now choose to import open issues, open pull requests, or both from a specified repository. The selected items are automatically imported when the project is created, so you can start with your existing content right away.


**Set a default repository**


[https://github.blog/wp\-content/uploads/2025/11/default\_repo.mp4\#t\=0\.001](https://github.blog/wp-content/uploads/2025/11/default_repo.mp4#t=0.001)
In project settings, you can now select a default repository. All new issues created in this project will be automatically associated with the selected repository.


**Pull request linked to issue workflow**


[https://github.blog/wp\-content/uploads/2025/11/linked\_PRs\_workflow.mp4\#t\=0\.001](https://github.blog/wp-content/uploads/2025/11/linked_PRs_workflow.mp4#t=0.001)
A new default workflow, **Pull request linked to issue**, automatically sets the status of an issue to “In progress” whenever a linked pull request exists.


## [🛠 Additional onboarding improvements](#%f0%9f%9b%a0-additional-onboarding-improvements)


* New projects now show **linked pull requests and sub\-issues** as default fields.
* The **Team planning template** now defaults to Table view instead of Board view.
* **Insights** and **Workflows** buttons have been elevated in the UI for easier discovery.
* Polishing and minor fixes to make onboarding smoother and more reliable.


## [🤖 API improvements](#%f0%9f%a4%96-api-improvements)


We’ve made improvements to the Projects GraphQL API making it easier to automate your project workflows.


* You’ll now see [`project_v2_item_status_changed`](https://docs.github.com/graphql/reference/objects#projectv2itemstatuschangedevent), [`added_to_project_v2`](https://docs.github.com/graphql/reference/objects#addedtoprojectv2event), [`removed_from_project_v2`](https://docs.github.com/graphql/reference/objects#removedfromprojectv2event), and [`converted_from_draft`](https://docs.github.com/graphql/reference/objects#convertedfromdraftevent) events. These events allow you to understand information such as how long an item was “In progress” before moving to “Done”.
* You can filter project items using the `query` argument with any project filter. Check out the [ProjectsV2 GraphQL documentation](https://docs.github.com/graphql/reference/objects#projectv2) for more details.


## [✍ Tell us what you think!](#%e2%9c%8d-tell-us-what-you-think)


Join the conversation in the [GitHub Community](https://github.com/orgs/community/discussions/178930), or select **Give feedback** from the project **…** menu to share your thoughts.
