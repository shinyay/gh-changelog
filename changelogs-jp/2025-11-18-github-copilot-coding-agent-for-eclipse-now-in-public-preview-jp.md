---
title: "Eclipse用GitHub Copilotコーディングエージェントがパブリックプレビューに"
date: "2025-11-18"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-18-github-copilot-coding-agent-for-eclipse-now-in-public-preview"
fetched_at: "2026-02-03T14:50:55.254978Z"
lang: "ja"
---

# Eclipse用GitHub Copilotコーディングエージェントがパブリックプレビューに

## Overview
GitHub CopilotコーディングエージェントがEclipse向けにパブリックプレビューで利用可能になりました。このリリースにより、CopilotがネイティブのEclipseワークフローに直接統合されます。

## Detailed Explanation
### Overview
- GitHub CopilotコーディングエージェントがEclipse向けにパブリックプレビューで利用可能になりました。このリリースにより、CopilotがネイティブのEclipseワークフローに直接統合されます。

### What's new
- Eclipseから委任：Copilot Chatでタスクを説明し、Eclipseを離れることなくエージェントに引き渡します。CopilotはGitHubの管理されたクラウド環境で作業を実行し、ドラフトプルリクエストを開き、完了時にレビューをキューに入れます。
- インラインジョブトラッキング：Copilot Chatにライブステータス、ドラフトプルリクエストへのリンク、作業をキャンセルまたは再開するためのクイックアクションを含むジョブカードが表示されます。サイドバーの新しい「GitHub Coding Agent Jobs」ビューでは、アクティブなタスクと過去のタスクを1か所で管理できます。

### Try it out
- EclipseでコーディングエージェントをHubert始めるには：
- 前提条件：GitHub Copilotライセンスとリポジトリへの書き込みアクセス権があることを確認してください。
- Copilot Chatを開く：EclipseでCopilot Chatツールウィンドウにアクセスします。チャットウィンドウの上部に、**Agent**や**Ask**などのモードオプションが表示されます（通常はタブまたはドロップダウンとして）。
- タスクを割り当てる：チャットボックスでタスクを説明し、**Delegate to coding agent**ボタンをクリックしてコーディングエージェントを起動します。
- 進行状況を追跡：割り当て後、Copilot Chatにジョブカードが表示されます。GitHub（Web）で開くか、IDE内で追跡します。IDE内では、組み込みのGitHubプルリクエストツールを使用して、差分、ステータスを表示したり、セッションをキャンセルしたりできます。ステータス変更（完了、エラーなど）の通知を受け取ります。
- 割り当て後、Copilot Chatにジョブカードが表示されます。
- GitHub（Web）で開くか、IDE内で追跡します。
- IDE内では、組み込みのGitHubプルリクエストツールを使用して、差分、ステータスを表示したり、セッションをキャンセルしたりできます。
- ステータス変更（完了、エラーなど）の通知を受け取ります。

### Share your feedback
- フィードバックが改善を推進します。Copilotコーディングエージェントのご経験についてぜひお聞かせください：
- 製品内フィードバック：Eclipse IDE内のフィードバックオプションを使用してください
- GitHubディスカッション：GitHub Copilot in Eclipseフィードバックリポジトリで考えを共有してください
- 今日から始めて、Eclipse IDEでCopilotコーディングエージェントによる自律的な開発を体験してください。

## Impact / Who’s Affected
- GitHub CopilotコーディングエージェントがEclipse向けにパブリックプレビューで利用可能になりました。

## Insights (derived from article language)
- タスクを割り当てる：チャットボックスでタスクを説明し、**Delegate to coding agent**ボタンをクリックしてコーディングエージェントを起動します。

## Article Content (cleaned)
GitHub CopilotコーディングエージェントがEclipse向けにパブリックプレビューで利用可能になりました。このリリースにより、[Copilot](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent?utm_source=changelog-docs-cca-eclipse)がネイティブのEclipseワークフローに直接統合されます。


## [What’s new](#whats-new)


* **Eclipseから委任**：Copilot Chatでタスクを説明し、Eclipseを離れることなくエージェントに引き渡します。CopilotはGitHubの管理されたクラウド環境で作業を実行し、ドラフトプルリクエストを開き、完了時にレビューをキューに入れます。
* **インラインジョブトラッキング**：Copilot Chatにライブステータス、ドラフトプルリクエストへのリンク、作業をキャンセルまたは再開するためのクイックアクションを含むジョブカードが表示されます。サイドバーの新しい*GitHub Coding Agent Jobs*ビューでは、アクティブなタスクと過去のタスクを1か所で管理できます。


## [Try it out](#try-it-out)


Eclipseでコーディングエージェントを始めるには：


1. **前提条件**：[GitHub Copilotライセンス](https://github.com/features/copilot)とリポジトリへの書き込みアクセス権があることを確認してください。
2. **Copilot Chatを開く**：EclipseでCopilot Chatツールウィンドウにアクセスします。チャットウィンドウの上部に、**Agent**や**Ask**などのモードオプションが表示されます（通常はタブまたはドロップダウンとして）。
3. **タスクを割り当てる**：チャットボックスでタスクを説明し、**Delegate to coding agent**ボタンをクリックしてコーディングエージェントを起動します。
4. **進行状況を追跡**：
	1. 割り当て後、Copilot Chatにジョブカードが表示されます。
	2. GitHub（Web）で開くか、IDE内で追跡します。
	3. IDE内では、組み込みのGitHubプルリクエストツールを使用して、差分、ステータスを表示したり、セッションをキャンセルしたりできます。
	4. ステータス変更（完了、エラーなど）の通知を受け取ります。  
	
	![Screenshot showing Copilot coding agent in Eclipse](https://github.com/user-attachments/assets/1e5a5537-7bc1-424b-8fd9-745f545f9e00)


## [Share your feedback](#share-your-feedback)


フィードバックが改善を推進します。Copilotコーディングエージェントのご経験についてぜひお聞かせください：


* **製品内フィードバック**：Eclipse IDE内のフィードバックオプションを使用してください
* **GitHubディスカッション**：[GitHub Copilot in Eclipseフィードバックリポジトリ](https://github.com/microsoft/copilot-eclipse-feedback/issues)で考えを共有してください


今日から始めて、Eclipse IDEでCopilotコーディングエージェントによる自律的な開発を体験してください。
