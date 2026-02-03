---
title: "Assign issues to Copilot using the API"
date: "2025-12-03"
type: "improvements"
labels: ["copilot", "projects and issues"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-03-assign-issues-to-copilot-using-the-api"
fetched_at: "2026-02-03T14:40:05.800653Z"
---

# Assign issues to Copilot using the API

## Overview
You can now assign issues to Copilot using both GraphQL and the REST API. You can also configure the target repository, base branch, custom instructions, and custom agents.

## Detailed Explanation
### Overview
- You can now assign issues to Copilot using both GraphQL and the REST API. You can also configure the target repository, base branch, custom instructions, and custom agents.

### GraphQL support
- You can assign issues to Copilot using the following mutations:
- updateIssue
- createIssue
- addAssigneesToAssignable
- replaceActorsForAssignable
- All requests must include this header:

### REST API support
- You can also assign issues to Copilot via the following REST API endpoints:
- Add assignees to an issue
- Create an issue
- Update an issue
- Join the community discussion to share your feedback or learn more in our documentation on assigning issues to Copilot .

## Insights (derived from article language)
- GraphQL support You can assign issues to Copilot using the following mutations: updateIssue createIssue addAssigneesToAssignable replaceActorsForAssignable All requests must include this header: GraphQL-Features: issues_copilot_assignment_api_support REST API support You can also assign issues to Copilot via the following REST API endpoints: Add assignees to an issue Create an issue Update an issue Join the community discussion to share your feedback or learn more in our documentation on assigning issues to Copilot .

## Article Content (cleaned)
You can now assign issues to Copilot using both GraphQL and the REST API. You can also configure the target repository, base branch, custom instructions, and custom agents.


## [GraphQL support](#graphql-support)


You can assign issues to Copilot using the following mutations:


* [`updateIssue`](https://docs.github.com/graphql/reference/mutations#updateissue)
* [`createIssue`](https://docs.github.com/graphql/reference/mutations#createissue)
* [`addAssigneesToAssignable`](https://docs.github.com/graphql/reference/mutations#addassigneestoassignable)
* [`replaceActorsForAssignable`](https://docs.github.com/graphql/reference/mutations#replaceactorsforassignable)


All requests must include this header:



```
GraphQL-Features: issues_copilot_assignment_api_support

```

## [REST API support](#rest-api-support)


You can also assign issues to Copilot via the following REST API endpoints:


* [Add assignees to an issue](https://docs.github.com/rest/issues/assignees?apiVersion=2022-11-28#add-assignees-to-an-issue)
* [Create an issue](https://docs.github.com/rest/issues/issues?apiVersion=2022-11-28#create-an-issue)
* [Update an issue](https://docs.github.com/rest/issues/issues?apiVersion=2022-11-28#update-an-issue)


Join the [community discussion](https://github.com/orgs/community/discussions/173575) to share your feedback or learn more in [our documentation on assigning issues to Copilot](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr).
