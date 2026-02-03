---
title: "GitHub Projects のオンボーディングフローの改善"
date: "2025-11-06"
type: "improvements"
labels: ["projects and issues"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-06-improved-onboarding-flow-for-github-projects"
fetched_at: "2026-02-03T14:50:55.400701Z"
lang: "ja"
---

# GitHub Projects のオンボーディングフローの改善

## Overview
GitHub Projects のオンボーディングフローを改善し、リポジトリからアイテムを接続してインポートするオプション、新しい Issue のデフォルトリポジトリの設定、新しいデフォルトワークフローを使用したプロジェクトのセットアップなど、より迅速に開始できるようにしました。

## Detailed Explanation
### 概要
- GitHub Projects のオンボーディングフローを改善し、リポジトリからアイテムを接続してインポートするオプション、新しい Issue のデフォルトリポジトリの設定、新しいデフォルトワークフローを使用したプロジェクトのセットアップなど、より迅速に開始できるようにしました。

### 🚀 主な改善点
- リポジトリからアイテムをインポート
- オンボーディング中に、指定されたリポジトリからオープンな Issue、オープンなプルリクエスト、またはその両方をインポートすることを選択できるようになりました。選択したアイテムは、プロジェクトの作成時に自動的にインポートされるため、既存のコンテンツですぐに開始できます。
- デフォルトリポジトリを設定
- プロジェクト設定で、デフォルトリポジトリを選択できるようになりました。このプロジェクトで作成されたすべての新しい Issue は、選択したリポジトリに自動的に関連付けられます。
- プルリクエストが Issue にリンクされたワークフロー
- 新しいデフォルトワークフロー「Pull request linked to issue」は、リンクされたプルリクエストが存在するときに、Issue のステータスを自動的に「In progress」に設定します。

### 🛠 その他のオンボーディングの改善
- 新しいプロジェクトには、リンクされたプルリクエストとサブ Issue がデフォルトフィールドとして表示されるようになりました。
- Team planning テンプレートは、Board ビューではなく Table ビューがデフォルトになりました。
- Insights と Workflows ボタンが UI で見つけやすいように昇格されました。
- オンボーディングをよりスムーズで信頼性の高いものにするための改善とマイナー修正。

### 🤖 API の改善
- Projects GraphQL API を改善し、プロジェクトワークフローの自動化を容易にしました。
- project_v2_item_status_changed、added_to_project_v2、removed_from_project_v2、および converted_from_draft イベントが表示されるようになりました。これらのイベントにより、アイテムが「In progress」から「Done」に移行するまでの時間などの情報を理解できます。
- 任意のプロジェクトフィルターで query 引数を使用してプロジェクトアイテムをフィルタリングできます。詳細については、ProjectsV2 GraphQL ドキュメントをご覧ください。

### ✍ ご意見をお聞かせください！
- GitHub Community で会話に参加するか、プロジェクトの「…」メニューから「Give feedback」を選択して、ご意見を共有してください。

## Key Changes
- リポジトリからアイテムをインポート
- オンボーディング中に、指定されたリポジトリからオープンな Issue、オープンなプルリクエスト、またはその両方をインポートすることを選択できるようになりました。選択したアイテムは、プロジェクトの作成時に自動的にインポートされるため、既存のコンテンツですぐに開始できます。
- デフォルトリポジトリを設定
- プロジェクト設定で、デフォルトリポジトリを選択できるようになりました。このプロジェクトで作成されたすべての新しい Issue は、選択したリポジトリに自動的に関連付けられます。
- プルリクエストが Issue にリンクされたワークフロー
- 新しいデフォルトワークフロー「Pull request linked to issue」は、リンクされたプルリクエストが存在するときに、Issue のステータスを自動的に「In progress」に設定します。
- 新しいプロジェクトには、リンクされたプルリクエストとサブ Issue がデフォルトフィールドとして表示されるようになりました。
- Team planning テンプレートは、Board ビューではなく Table ビューがデフォルトになりました。
- Insights と Workflows ボタンが UI で見つけやすいように昇格されました。
- オンボーディングをよりスムーズで信頼性の高いものにするための改善とマイナー修正。
- Projects GraphQL API を改善し、プロジェクトワークフローの自動化を容易にしました。
- project_v2_item_status_changed、added_to_project_v2、removed_from_project_v2、および converted_from_draft イベントが表示されるようになりました。これらのイベントにより、アイテムが「In progress」から「Done」に移行するまでの時間などの情報を理解できます。
- 任意のプロジェクトフィルターで query 引数を使用してプロジェクトアイテムをフィルタリングできます。詳細については、ProjectsV2 GraphQL ドキュメントをご覧ください。

## Insights (derived from article language)
- 詳細については、ProjectsV2 GraphQL ドキュメントをご覧ください。✍ ご意見をお聞かせください！

## Article Content (cleaned)
GitHub Projects のオンボーディングフローを改善し、リポジトリからアイテムを接続してインポートするオプション、新しい Issue のデフォルトリポジトリの設定、新しいデフォルトワークフローを使用したプロジェクトのセットアップなど、より迅速に開始できるようにしました。


## [🚀 主な改善点](#%f0%9f%9a%80-key-improvements)


**リポジトリからアイテムをインポート**


[https://github.blog/wp\-content/uploads/2025/11/import\_items.mp4\#t\=0\.001](https://github.blog/wp-content/uploads/2025/11/import_items.mp4#t=0.001)
オンボーディング中に、指定されたリポジトリからオープンな Issue、オープンなプルリクエスト、またはその両方をインポートすることを選択できるようになりました。選択したアイテムは、プロジェクトの作成時に自動的にインポートされるため、既存のコンテンツですぐに開始できます。


**デフォルトリポジトリを設定**


[https://github.blog/wp\-content/uploads/2025/11/default\_repo.mp4\#t\=0\.001](https://github.blog/wp-content/uploads/2025/11/default_repo.mp4#t=0.001)
プロジェクト設定で、デフォルトリポジトリを選択できるようになりました。このプロジェクトで作成されたすべての新しい Issue は、選択したリポジトリに自動的に関連付けられます。


**プルリクエストが Issue にリンクされたワークフロー**


[https://github.blog/wp\-content/uploads/2025/11/linked\_PRs\_workflow.mp4\#t\=0\.001](https://github.blog/wp-content/uploads/2025/11/linked_PRs_workflow.mp4#t=0.001)
新しいデフォルトワークフロー「**Pull request linked to issue**」は、リンクされたプルリクエストが存在するときに、Issue のステータスを自動的に「In progress」に設定します。


## [🛠 その他のオンボーディングの改善](#%f0%9f%9b%a0-additional-onboarding-improvements)


* 新しいプロジェクトには、**リンクされたプルリクエストとサブ Issue** がデフォルトフィールドとして表示されるようになりました。
* **Team planning テンプレート**は、Board ビューではなく Table ビューがデフォルトになりました。
* **Insights** と **Workflows** ボタンが UI で見つけやすいように昇格されました。
* オンボーディングをよりスムーズで信頼性の高いものにするための改善とマイナー修正。


## [🤖 API の改善](#%f0%9f%a4%96-api-improvements)


Projects GraphQL API を改善し、プロジェクトワークフローの自動化を容易にしました。


* [`project_v2_item_status_changed`](https://docs.github.com/graphql/reference/objects#projectv2itemstatuschangedevent)、[`added_to_project_v2`](https://docs.github.com/graphql/reference/objects#addedtoprojectv2event)、[`removed_from_project_v2`](https://docs.github.com/graphql/reference/objects#removedfromprojectv2event)、および [`converted_from_draft`](https://docs.github.com/graphql/reference/objects#convertedfromdraftevent) イベントが表示されるようになりました。これらのイベントにより、アイテムが「In progress」から「Done」に移行するまでの時間などの情報を理解できます。
* 任意のプロジェクトフィルターで `query` 引数を使用してプロジェクトアイテムをフィルタリングできます。詳細については、[ProjectsV2 GraphQL ドキュメント](https://docs.github.com/graphql/reference/objects#projectv2)をご覧ください。


## [✍ ご意見をお聞かせください！](#%e2%9c%8d-tell-us-what-you-think)


[GitHub Community](https://github.com/orgs/community/discussions/178930) で会話に参加するか、プロジェクトの **…** メニューから **Give feedback** を選択して、ご意見を共有してください。
