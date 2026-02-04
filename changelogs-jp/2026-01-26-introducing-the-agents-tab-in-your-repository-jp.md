---
title: "リポジトリにAgentsタブを導入"
date: "2026-01-26"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-26-introducing-the-agents-tab-in-your-repository"
fetched_at: "2026-02-03T14:50:54.704270Z"
lang: "ja"
---

# リポジトリにAgentsタブを導入

## Overview
Copilotコーディングエージェントタスクを管理する場所を再設計しました。新しいAgentsタブで、ミッションコントロールスタイルのビューを直接リポジトリに追加しています。

## Detailed Explanation
### 概要
- Copilotコーディングエージェントタスクを管理する場所を再設計しました。新しいAgentsタブで、ミッションコントロールスタイルのビューを直接リポジトリに追加しています。
- 別のページに移動する代わりに、エージェントセッションがコード、プルリクエスト、issueと並んで配置されるようになりました。リポジトリのすべてのセッションを1か所で表示し、新しいセッションを作成し、コードベースを離れることなくタスクを切り替えることができます。ワンクリックリンクで、関連するプルリクエストに直接ジャンプできます。セッションをアーカイブして整理し、セッション履歴をページングすることもできます。

### 再設計されたセッションログ
- セッションログが読みやすく、追跡しやすくなりました。類似のツール呼び出しがグループ化され、ノイズが減り、フローがより明確になります。ツール出力はインラインプレビューをレンダリングし、ファイルの変更は使い慣れたdiffビューで表示され、ワンクリックで展開できます。すべてのツール呼び出しには独特のアイコンがあり、bashコマンドが完全な透明性のために表示されるようになりました。

### Copilot CLIで再開
- ターミナルで作業することを好む場合、Copilot CLIで直接Copilotセッションを続けることができるようになりました。「Continue in Copilot CLI」をクリックし、コマンドをコピーして、中断したところから続けることができます。

### 始め方
- リポジトリに移動します。
- 新しいAgentsタブをクリックします。
- タスクを作成します。
- CLIでセッションを開くには、「Continue in Copilot CLI」をクリックします。
- コマンドをコピーしてターミナルに貼り付け、Copilot CLIを開始します。
- 注：Agentsタブを表示するには、リポジトリでCopilotコーディングエージェントが有効になっていることを確認してください。
- コミュニティディスカッションに参加してください。

## Caveats / Limitations
- 注：Agentsタブを表示するには、リポジトリでCopilotコーディングエージェントが有効になっていることを確認してください。

## Article Content (cleaned)
Copilotコーディングエージェントタスクを管理する場所を再設計しました。新しい**Agents**タブで、[ミッションコントロールスタイルのビュー](https://github.blog/changelog/2025-10-28-a-mission-control-to-assign-steer-and-track-copilot-coding-agent-tasks/?utm_source=blog-day1-recap-mission-control-cta&utm_medium=blog&utm_campaign=universe25)を直接リポジトリに追加しています。


別のページに移動する代わりに、エージェントセッションがコード、プルリクエスト、issueと並んで配置されるようになりました。リポジトリのすべてのセッションを1か所で表示し、新しいセッションを作成し、コードベースを離れることなくタスクを切り替えることができます。ワンクリックリンクで、関連するプルリクエストに直接ジャンプできます。セッションをアーカイブして整理し、セッション履歴をページングすることもできます。


## [Redesigned session logs](#redesigned-session-logs)


セッションログが読みやすく、追跡しやすくなりました。類似のツール呼び出しがグループ化され、ノイズが減り、フローがより明確になります。ツール出力はインラインプレビューをレンダリングし、ファイルの変更は使い慣れたdiffビューで表示され、ワンクリックで展開できます。すべてのツール呼び出しには独特のアイコンがあり、bashコマンドが完全な透明性のために表示されるようになりました。


![A sample view of the Agents tab with a list of agents on the left and the interaction with the agent on the right.](https://github.com/user-attachments/assets/cbf6faf4-acab-4441-b3dd-2436b4af642b)


## [Resume with the Copilot CLI](#resume-with-the-copilot-cli)


ターミナルで作業することを好む場合、Copilot CLIで直接Copilotセッションを続けることができるようになりました。**Continue in Copilot CLI**をクリックし、コマンドをコピーして、中断したところから続けることができます。


![A menu with the option to Continue in Copilot CLI.](https://github.com/user-attachments/assets/2b6d2909-f7dc-4f2b-b498-3e11a69a1b22)


## [To get started](#to-get-started)


1. リポジトリに移動します。
2. 新しい**Agents**タブをクリックします。
3. タスクを作成します。
4. CLIでセッションを開くには、**Continue in Copilot CLI**をクリックします。
5. コマンドをコピーしてターミナルに貼り付け、[Copilot CLI](https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli)を開始します。


注：**Agents**タブを表示するには、リポジトリで[Copilotコーディングエージェントが有効](https://docs.github.com/copilot/concepts/agents/coding-agent/access-management)になっていることを確認してください。


[コミュニティディスカッション](https://github.com/orgs/community/discussions/185364)に参加してください。
