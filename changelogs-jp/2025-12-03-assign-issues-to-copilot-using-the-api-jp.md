---
title: "APIを使用してCopilotに課題を割り当てる"
date: "2025-12-03"
type: "improvements"
labels: ["copilot", "projects and issues"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-03-assign-issues-to-copilot-using-the-api"
fetched_at: "2026-02-03T14:50:55.080952Z"
lang: "ja"
---

# APIを使用してCopilotに課題を割り当てる

## Overview
GraphQLとREST APIの両方を使用して、Copilotに課題を割り当てることができるようになりました。また、ターゲットリポジトリ、ベースブランチ、カスタム命令、カスタムエージェントを構成することもできます。

## Detailed Explanation
### Overview
- GraphQLとREST APIの両方を使用して、Copilotに課題を割り当てることができるようになりました。また、ターゲットリポジトリ、ベースブランチ、カスタム命令、カスタムエージェントを構成することもできます。

### GraphQLサポート
- 以下のミューテーションを使用してCopilotに課題を割り当てることができます：
- updateIssue
- createIssue
- addAssigneesToAssignable
- replaceActorsForAssignable
- すべてのリクエストには、このヘッダーを含める必要があります：

### REST APIサポート
- 以下のREST APIエンドポイント経由でもCopilotに課題を割り当てることができます：
- 課題に担当者を追加する
- 課題を作成する
- 課題を更新する
- フィードバックを共有するか、Copilotへの課題の割り当てに関するドキュメントで詳細を確認するには、コミュニティディスカッションにご参加ください。

## Insights (derived from article language)
- GraphQLサポート 以下のミューテーションを使用してCopilotに課題を割り当てることができます： updateIssue createIssue addAssigneesToAssignable replaceActorsForAssignable すべてのリクエストには、このヘッダーを含める必要があります： GraphQL-Features: issues_copilot_assignment_api_support REST APIサポート 以下のREST APIエンドポイント経由でもCopilotに課題を割り当てることができます： 課題に担当者を追加する 課題を作成する 課題を更新する フィードバックを共有するか、Copilotへの課題の割り当てに関するドキュメントで詳細を確認するには、コミュニティディスカッションにご参加ください。

## Article Content (cleaned)
GraphQLとREST APIの両方を使用して、Copilotに課題を割り当てることができるようになりました。また、ターゲットリポジトリ、ベースブランチ、カスタム命令、カスタムエージェントを構成することもできます。


## [GraphQLサポート](#graphql-support)


以下のミューテーションを使用してCopilotに課題を割り当てることができます：


* [`updateIssue`](https://docs.github.com/graphql/reference/mutations#updateissue)
* [`createIssue`](https://docs.github.com/graphql/reference/mutations#createissue)
* [`addAssigneesToAssignable`](https://docs.github.com/graphql/reference/mutations#addassigneestoassignable)
* [`replaceActorsForAssignable`](https://docs.github.com/graphql/reference/mutations#replaceactorsforassignable)


すべてのリクエストには、このヘッダーを含める必要があります：



```
GraphQL-Features: issues_copilot_assignment_api_support

```

## [REST APIサポート](#rest-api-support)


以下のREST APIエンドポイント経由でもCopilotに課題を割り当てることができます：


* [課題に担当者を追加する](https://docs.github.com/rest/issues/assignees?apiVersion=2022-11-28#add-assignees-to-an-issue)
* [課題を作成する](https://docs.github.com/rest/issues/issues?apiVersion=2022-11-28#create-an-issue)
* [課題を更新する](https://docs.github.com/rest/issues/issues?apiVersion=2022-11-28#update-an-issue)


フィードバックを共有するか、[Copilotへの課題の割り当てに関するドキュメント](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr)で詳細を確認するには、[コミュニティディスカッション](https://github.com/orgs/community/discussions/173575)にご参加ください。
