---
title: "Claude と Codex が GitHub でパブリックプレビューとして利用可能に"
date: "2026-02-04"
type: "Release"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-02-04-claude-and-codex-are-now-available-in-public-preview-on-github"
fetched_at: "2026-02-05T04:46:41.067153Z"
lang: "ja"
---

# Claude と Codex が GitHub でパブリックプレビューとして利用可能に

## Overview
Anthropic の Claude と OpenAI Codex が、Copilot Pro+ および Copilot Enterprise 向けのコーディングエージェントとしてパブリックプレビューで利用可能になりました。

## Detailed Explanation
### パブリックプレビューの内容
- Anthropic の Claude と OpenAI Codex が、Copilot Pro+ / Copilot Enterprise のコーディングエージェントとして利用できます。
- github.com、GitHub Mobile、VS Code からエージェントセッションを開始し、作業を割り当てられます。Issue / Pull Request / 有効化済みリポジトリの Agents タブ / VS Code の Agent sessions ビューなどが入口です。
- 追加サブスクリプションは不要で、既存の Copilot サブスクリプションに含まれると説明されています。
- パブリックプレビュー期間中、各コーディングエージェントセッションは 1 回のプレミアムリクエストを消費します。

### Copilot Pro+ の有効化
- Copilot のコーディングエージェント設定に移動します。
- エージェントがアクセス可能なリポジトリを選びます。
- 「Claude」「Codex」または両方をトグルで有効化します。

### Copilot Enterprise の有効化
- 企業管理者がエンタープライズ/組織レベルでパートナーエージェントを有効化する必要があります。
- 具体的には Enterprise AI Controls の Agents タブ、および組織の Settings → Copilot → Coding agent で Partner Agents を有効化します。

### 使い方（Web / Mobile / PR）
- GitHub.com と GitHub Mobile の Agents タブなどから新しいセッションを作成し、進捗を追跡したり完了済みセッションを確認できます。
- Issue の Assignees から Claude / Codex / Copilot を割り当てると、エージェントが作業を開始し、レビュー用のドラフト PR を作成すると説明されています。
- PR では @copilot / @claude / @codex を使って追加の指示やフィードバックが可能です。

### VS Code からの利用
- VS Code 1.109 以降が必要です。
- Agent sessions ビューからセッション種別（Local / Cloud / Background）とエージェントを選びます（Background は Copilot のみ）。

## Impact / Who’s Affected
- Copilot Pro+ / Copilot Enterprise の利用者は、Claude と Codex を選択肢としてエージェントセッションを開始・割り当てできるようになります。
- パブリックプレビュー期間中は、各セッションがプレミアムリクエストを消費します。

## Caveats / Limitations
- 本機能はパブリックプレビューです。
- パブリックプレビュー期間中、各コーディングエージェントセッションは 1 回のプレミアムリクエストを消費します。
- VS Code の Background セッションは Copilot のみです。

## Insights (derived from article language)
- Web / Mobile / IDE 間でセッションをまたいだ体験を強く押しており、「どこからでも開始して追跡できる」ことが価値として描かれています。

## Article Content (cleaned)
# [Claude and Codex coding agents are now in public preview](https://github.blog/changelog/feed/#claude-and-codex-coding-agents-are-now-in-public-preview)


Anthropic の Claude と OpenAI Codex が、Copilot Pro\+ および Copilot Enterprise のコーディングエージェントとしてパブリックプレビューで利用可能になりました。


github.com、GitHub Mobile、VS Code からエージェントセッションを開始し、作業を割り当てられます。Issue、Pull Request、有効化済みリポジトリの Agents タブ、VS Code の Agent sessions ビューなどから利用できます。


追加サブスクリプションは不要で、既存の Copilot サブスクリプションに含まれると説明されています。パブリックプレビュー期間中、各コーディングエージェントセッションは 1 回のプレミアムリクエストを消費します。




---


## [How to enable Claude and Codex](https://github.blog/changelog/feed/#how-to-enable-claude-and-codex)


### [For Copilot Pro\+ subscribers](https://github.blog/changelog/feed/#for-copilot-pro-subscribers)


1. [Copilot coding agent settings](https://github.com/settings/copilot/coding_agent?utm_source=changelog-3p-agents-cca-settings-cta&utm_medium=changelog&utm_campaign=agent-3p-platform-feb-2026) に移動します。
2. エージェントがアクセス可能なリポジトリを選びます。
3. 「Claude」「Codex」または両方を **On** に切り替えます。


### [For Copilot Enterprise subscribers](https://github.blog/changelog/feed/#for-copilot-enterprise-subscribers)


以下の設定を企業管理者が有効化する必要があります。


* Enable agents at the enterprise level:
	1. 「Enterprise AI Controls」に移動します。
	2. **Agents** タブを開きます。
	3. 「Partner Agents」で「Claude」「Codex」または両方を有効化します。
* Enable agents at the organization level:
	1. 組織の **Settings** に移動します。
	2. **Copilot** タブを選びます。
	3. **Coding agent** を開きます。
	4. 「Partner Agents」で「Claude」「Codex」または両方を有効化します。




---


## [How to use agents](https://github.blog/changelog/feed/#how-to-use-agents)


### [Create and view sessions from the Agents tab on GitHub (web and mobile app)](https://github.blog/changelog/feed/#create-and-view-sessions-from-the-agents-tab-on-github-web-and-mobile-app)


GitHub.com と GitHub Mobile アプリでは、いくつかの方法で新しいエージェントセッションを作成できます。


* GitHub.com では、エージェントが有効化されているリポジトリの **Agents** タブに移動するか、ヘッダーのエージェントドロップダウンからタスクを開始します。
* GitHub Mobile アプリでは、Home やリポジトリから **Agents** ビューを開くか、Home / Repository などから **+** ボタンをタップします。


いずれの入口でも、リクエストを入力し、入力欄の Copilot アイコンから利用するエージェントを選択して送信します。エージェントは作業を開始し、進捗をリアルタイムで追跡するか、完了済みセッションをセッション一覧から確認できます。


### [Assign agents to issues](https://github.blog/changelog/feed/#assign-agents-to-issues)


Assignees ドロップダウンを使い、Issue に Claude / Codex / Copilot、または 3 つすべてを割り当てます。選択したエージェントは作業を開始し、レビュー用のドラフト Pull Request を提出すると説明されています。


### [Work with agents in pull requests](https://github.blog/changelog/feed/#work-with-agents-in-pull-requests)


* エージェントは（必要に応じて）ドラフト Pull Request を作成し、レビューのフィードバックに追従しながら完了まで反復できます。
* Assignees からオープンな Pull Request を任意のエージェントに割り当てることもできます。
* レビューコメントでは @copilot / @claude / @codex を使って指示できます。
* **View session** ボタンから概要と詳細なアクティビティログを確認できます。


### [Start agent sessions in VS Code](https://github.blog/changelog/feed/#start-agent-sessions-in-vs-code)


1. VS Code 1\.109 以降を利用します。
2. タイトルバーのチャットアイコン、またはコマンドパレット（`Ctrl+Shift+P` / `Cmd+Shift+P`）で **Agent sessions** を検索してビューを開きます。
3. セッション種別とエージェントを選択します。


* **Local**: 高速な対話型支援
* **Cloud**: GitHub 上で自律的に実行されるタスク
* **Background**: ローカルで非同期に実行されるタスク（**Copilot のみ**）


[Watch this demo video](https://youtu.be/GuTQDXKwdJQ?si=gN9ZWpEKa1KvbEqz) で動作例を確認できます。




---


## [Try it now](https://github.blog/changelog/feed/#try-it-now)


* [Enable Claude and Codex today](https://github.com/settings/copilot/coding_agent?utm_source=changelog-3p-agents-cca-settings-cta&utm_medium=changelog&utm_campaign=agent-3p-platform-feb-2026)




---


## [Learn more](https://github.blog/changelog/feed/#learn-more)


* [full blog post here](https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/?utm_source=changelog-3p-agents-blog-cta&utm_medium=changelog&utm_campaign=agent-3p-platform-feb-2026) の詳細記事
* [our third\-party agents documentation](https://docs.github.com/copilot/concepts/agents/about-third-party-agents?utm_source=changelog-3p-agents-docs-cta&utm_medium=changelog&utm_campaign=agent-3p-platform-feb-2026)（サードパーティエージェントのドキュメント）
* フィードバック共有用の [discussion post](https://github.com/orgs/community/discussions/186179?utm_source=changelog-3p-agents-discussion-cta&utm_medium=changelog&utm_campaign=agent-3p-platform-feb-2026)
* モバイルでの新しいセッション作成方法についての [changelog about new ways to create agent sessions](https://github.blog/changelog/2025-12-16-more-direct-access-to-agent-session-creation-across-github-mobile/)
