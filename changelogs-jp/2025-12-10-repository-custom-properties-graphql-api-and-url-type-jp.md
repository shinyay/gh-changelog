---
title: "リポジトリカスタムプロパティ: GraphQL APIとURLタイプ"
date: "2025-12-10"
type: "improvements"
labels: ["enterprise management tools", "platform governance"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-09-repository-custom-properties-graphql-api-and-url-type"
fetched_at: "2026-02-03T14:50:55.019867Z"
lang: "ja"
---

# リポジトリカスタムプロパティ: GraphQL APIとURLタイプ

## Overview
GitHubカスタムリポジトリプロパティに2つの新しい機能を追加し、大規模なリポジトリの整理と管理をより簡単にしました。

## Detailed Explanation
### 概要
- GitHubカスタムリポジトリプロパティに2つの新しい機能を追加し、大規模なリポジトリの整理と管理をより簡単にしました。

### GraphQL経由でカスタムプロパティを管理
- GraphQL APIを使用してカスタムリポジトリプロパティを管理できるようになりました。これにより、既存のワークフローと自動化ツールでカスタムプロパティの作成、更新、削除にプログラムでアクセスできます。
- 詳細については、[カスタムプロパティのGraphQL APIドキュメント](https://docs.github.com/en/graphql/reference)をご覧ください。**注意:** GraphQLドキュメントの公開には遅延があり、公開まで24時間かかる場合があります。

### 新しいURLプロパティタイプ
- カスタムリポジトリプロパティは、組み込み検証機能を備えた`URL`タイプをサポートするようになりました。これにより、管理者はランブック、監視ダッシュボード、外部ドキュメントなどの関連リソースを、無効なURLを心配することなくリポジトリに添付しやすくなります。
- `URL`プロパティを作成すると、GitHubは値が適切にフォーマットされたURLであることを自動的に検証し、組織全体で一貫性を確保します。
- 詳細については、[リポジトリのカスタムプロパティ管理に関するドキュメント](https://docs.github.com/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization)をご覧ください。
- [コミュニティディスカッション](https://gh.io/props-gql-url-discussion)でフィードバックを共有してください。

## Caveats / Limitations
- **注意:** GraphQLドキュメントの公開には遅延があり、公開まで24時間かかる場合があります。

## Insights (derived from article language)
- 詳細については、カスタムプロパティのGraphQL APIドキュメントをご覧ください。

## Article Content (cleaned)
GitHubカスタムリポジトリプロパティに2つの新しい機能を追加し、大規模なリポジトリの整理と管理をより簡単にしました。


### [GraphQL経由でカスタムプロパティを管理](#manage-custom-properties-via-graphql)


GraphQL APIを使用してカスタムリポジトリプロパティを管理できるようになりました。これにより、既存のワークフローと自動化ツールでカスタムプロパティの作成、更新、削除にプログラムでアクセスできます。


詳細については、[カスタムプロパティのGraphQL APIドキュメント](https://docs.github.com/en/graphql/reference)をご覧ください。**注意:** GraphQLドキュメントの公開には遅延があり、公開まで24時間かかる場合があります。


### [新しいURLプロパティタイプ](#new-url-property-type)


![タイプがURLに設定された「AzureK8Fleet」という名前のカスタムプロパティの設定を示すGitHub「New property」インターフェース。フォームには、Microsoft Azure Kubernetes Fleetポータルに直接リンクするデフォルト値が含まれています。](https://github.com/user-attachments/assets/fb05d0b9-2093-4cc5-8d1e-f761bb75da5a)


カスタムリポジトリプロパティは、組み込み検証機能を備えた`URL`タイプをサポートするようになりました。これにより、管理者はランブック、監視ダッシュボード、外部ドキュメントなどの関連リソースを、無効なURLを心配することなくリポジトリに添付しやすくなります。


`URL`プロパティを作成すると、GitHubは値が適切にフォーマットされたURLであることを自動的に検証し、組織全体で一貫性を確保します。


詳細については、[リポジトリのカスタムプロパティ管理に関するドキュメント](https://docs.github.com/organizations/managing-organization-settings/managing-custom-properties-for-repositories-in-your-organization)をご覧ください。


[コミュニティディスカッション](https://gh.io/props-gql-url-discussion)でフィードバックを共有してください。
