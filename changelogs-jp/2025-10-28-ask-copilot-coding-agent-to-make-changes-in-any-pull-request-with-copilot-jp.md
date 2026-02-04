---
title: "@copilot で任意のプルリクエストへの変更を Copilot coding agent に依頼可能に"
date: "2025-10-28"
type: "improvements"
labels: ["copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-ask-copilot-coding-agent-to-make-changes-in-any-pull-request-with-copilot"
fetched_at: "2026-02-03T14:50:55.584684Z"
lang: "ja"
---

# @copilot で任意のプルリクエストへの変更を Copilot coding agent に依頼可能に

## Overview
Copilot はゼロから新しいプルリクエストを作成するだけでなく、人が作成した既存のプルリクエストに対しても変更を手伝えるようになりました。コメントで @copilot にメンションするだけです。

## Detailed Explanation
### 概要
- Copilot はゼロから新しいプルリクエストを作成するだけでなく、人が作成した既存のプルリクエストに対しても変更を手伝えるようになりました。コメントで @copilot にメンションするだけです。
- Copilot coding agent は、非同期・自律型のバックグラウンドエージェントです。Copilot にタスクを委任すると、バックグラウンドで作業し、その後あなたにレビューを依頼します。
- コメントで @copilot にメンションすると、Copilot は既存のプルリクエストの上に新しいプルリクエストを作成します。このとき、既存のプルリクエストのブランチをベースブランチとして使用します。依頼した変更が完了すると、Copilot は新しいプルリクエストでレビューを依頼します。
- 元のプルリクエストはあなたがコントロールできます。新しいプルリクエストをあなたのブランチにマージして Copilot の提案変更を受け入れるまで、元のプルリクエストは変更されません。
- 別のプルリクエストのブランチへマージするプルリクエストは、見つけやすいように明確にマークされます。
- Copilot coding agent は Copilot Pro、Copilot Pro+、Copilot Business、Copilot Enterprise の加入者が利用できます。Copilot Business または Copilot Enterprise の場合、利用する前に管理者が「Policies」ページから Copilot coding agent を有効化する必要があります。
- Copilot coding agent の詳細は、coding agent のドキュメントを参照してください。

## Insights (derived from article language)
- Copilot coding agent の詳細は、coding agent のドキュメントを参照してください。

## Article Content (cleaned)
Copilot はゼロから新しいプルリクエストを作成するだけでなく、人が作成した既存のプルリクエストに対しても変更を手伝えるようになりました。コメントで `@copilot` にメンションするだけです。


[Copilot coding agent](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent?utm_source=changelog-docs-mention-copilot-in-pr&utm_medium=changelog&utm_campaign=universe25) は、非同期・自律型のバックグラウンドエージェントです。Copilot にタスクを委任すると、バックグラウンドで作業し、その後あなたにレビューを依頼します。


コメントで `@copilot` にメンションすると、Copilot は既存のプルリクエストの上に新しいプルリクエストを作成します。このとき、既存のプルリクエストのブランチをベースブランチとして使用します。依頼した変更が完了すると、Copilot は新しいプルリクエストでレビューを依頼します。


元のプルリクエストはあなたがコントロールできます。新しいプルリクエストをあなたのブランチにマージして Copilot の提案変更を受け入れるまで、元のプルリクエストは変更されません。


別のプルリクエストのブランチへマージするプルリクエストは、見つけやすいように明確にマークされます。


![別のプルリクエストのブランチへマージされることを示す「Parent」タグ付きプルリクエストのスクリーンショット](https://github.com/user-attachments/assets/121e3d3f-0df5-44ea-9626-a28cd54bc227)


Copilot coding agent は Copilot Pro、Copilot Pro\+、Copilot Business、Copilot Enterprise の加入者が利用できます。Copilot Business または Copilot Enterprise の場合、利用する前に管理者が [「Policies」ページから Copilot coding agent を有効化](https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/agents/copilot-coding-agent/enabling-copilot-coding-agent?utm_source=changelog-docs-mention-copilot-in-pr&utm_medium=changelog&utm_campaign=universe25) する必要があります。


Copilot coding agent の詳細は、[coding agent のドキュメント](https://docs.github.com/enterprise-cloud@latest/copilot/concepts/agents/coding-agent/about-coding-agent?utm_source=changelog-docs-mention-copilot-in-pr&utm_medium=changelog&utm_campaign=universe25)を参照してください。
