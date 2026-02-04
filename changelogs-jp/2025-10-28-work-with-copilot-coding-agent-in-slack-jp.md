---
title: "Slack で Copilot コーディングエージェントを使用する"
date: "2025-10-28"
type: "new releases"
labels: ["copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-work-with-copilot-coding-agent-in-slack"
fetched_at: "2026-02-03T14:50:55.551297Z"
lang: "ja"
---

# Slack で Copilot コーディングエージェントを使用する

## Overview
Slack 用 GitHub アプリが GitHub Copilot コーディングエージェントと連携し、Slack の会話から直接プルリクエストを生成できるようになりました。

## Detailed Explanation
### Overview
- Slack 用 GitHub アプリが GitHub Copilot コーディングエージェントと連携し、Slack の会話から直接プルリクエストを生成できるようになりました。
- 編集者注（2025年10月28日）：この機能が広く利用可能になったため、段階的なロールアウトへの言及を削除しました。
- Slack スレッドでプロンプトとともに @GitHub をメンションすると、Copilot コーディングエージェントがバックグラウンドで作業を開始し、プルリクエストのレビュー準備ができたら返信します。
- Copilot コーディングエージェントは、バグ修正、段階的な新機能、テストカバレッジ、リファクタリングなどのタスクをオフロードするのに最適な非同期かつ自律型の開発者エージェントです。より複雑な問題に集中できるようになります。

### Try it out
- GitHub アカウントで Copilot コーディングエージェントが有効になっていることを確認してください。Copilot コーディングエージェントは、すべての有料 Copilot プランで利用できます。Copilot Business または Enterprise のサブスクライバーの場合、管理者がポリシーを有効にする必要があります。
- Slack ワークスペースで GitHub アプリをインストールまたはアップグレードしてください。
- Slack スレッドで「ナビゲーションアイコンの欠けているツールチップを修正」のようなプロンプトとともに @GitHub をメンションして、Copilot コーディングエージェントを開始し、スレッドで直接進捗を追跡します。
- GitHub アカウントをリンクしてください。
- 新しい Copilot コーディングエージェント機能はオプションであり、新しい権限が必要です。アップグレードしない場合は、通知、Issue のトリアージ、プルリクエスト管理のために、従来どおり GitHub アプリを引き続き使用できます。
- Slack 用 GitHub アプリは、現在一般提供されている Microsoft Teams 用 GitHub アプリに加わります。
- Slack または Teams との Copilot コーディングエージェントの統合について詳しく学び、GitHub Community でディスカッションに参加してください。

## Impact / Who’s Affected
- 新しい Copilot コーディングエージェント機能はオプションであり、新しい権限が必要です。
- Slack 用 GitHub アプリは、現在一般提供されている Microsoft Teams 用 GitHub アプリに加わります。

## Caveats / Limitations
- 編集者注（2025年10月28日）：この機能が広く利用可能になったため、段階的なロールアウトへの言及を削除しました。
- 新しい Copilot コーディングエージェント機能はオプションであり、新しい権限が必要です。

## Insights (derived from article language)
- Slack スレッドで「ナビゲーションアイコンの欠けているツールチップを修正」のようなプロンプトとともに @GitHub をメンションして、Copilot コーディングエージェントを開始し、スレッドで直接進捗を追跡します。
- 新しい Copilot コーディングエージェント機能はオプションであり、新しい権限が必要です。
- Slack または Teams との Copilot コーディングエージェントの統合について詳しく学び、GitHub Community でディスカッションに参加してください。

## Article Content (cleaned)
Slack 用 [GitHub アプリ](https://slack.com/marketplace/A01BP7R4KNY-github)が [GitHub Copilot コーディングエージェント](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent?utm_source=changelog-docs-copilot-coding-agent-slack&utm_medium=changelog&utm_campaign=universe25)と連携し、Slack の会話から直接プルリクエストを生成できるようになりました。


*編集者注（2025年10月28日）：この機能が広く利用可能になったため、段階的なロールアウトへの言及を削除しました。*


Slack スレッドでプロンプトとともに `@GitHub` をメンションすると、Copilot コーディングエージェントがバックグラウンドで作業を開始し、プルリクエストのレビュー準備ができたら返信します。


Copilot コーディングエージェントは、バグ修正、段階的な新機能、テストカバレッジ、リファクタリングなどのタスクをオフロードするのに最適な非同期かつ自律型の開発者エージェントです。より複雑な問題に集中できるようになります。


  




### [Try it out](#try-it-out)


1. GitHub アカウントで Copilot コーディングエージェントが有効になっていることを確認してください。Copilot コーディングエージェントは、すべての有料 Copilot プランで利用できます。Copilot Business または Enterprise のサブスクライバーの場合、管理者が[ポリシーを有効にする](https://docs.github.com/enterprise-cloud@latest/copilot/concepts/agents/coding-agent/coding-agent-for-business-and-enterprise#copilot-coding-agent-policies-for-copilot-business-and-copilot-enterprise?utm_source=changelog-docs-copilot-coding-agent-slack&utm_medium=changelog&utm_campaign=universe25)必要があります。
2. Slack ワークスペースで [GitHub アプリ](https://slack.github.com)をインストールまたはアップグレードしてください。
3. Slack スレッドで「ナビゲーションアイコンの欠けているツールチップを修正」のようなプロンプトとともに `@GitHub` をメンションして、Copilot コーディングエージェントを開始し、スレッドで直接進捗を追跡します。
4. GitHub アカウントをリンクしてください。


新しい Copilot コーディングエージェント機能はオプションであり、新しい権限が必要です。アップグレードしない場合は、通知、Issue のトリアージ、プルリクエスト管理のために、従来どおり GitHub アプリを引き続き使用できます。


Slack 用 GitHub アプリは、現在一般提供されている [Microsoft Teams 用 GitHub アプリ](https://github.blog/changelog/2025-09-19-work-with-copilot-coding-agent-in-microsoft-teams/?utm_source=changelog-docs-copilot-coding-agent-slack&utm_medium=changelog&utm_campaign=universe25)に加わります。


[Slack](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/integrate-coding-agent-with-slack?utm_source=changelog-docs-copilot-coding-agent-slack&utm_medium=changelog&utm_campaign=universe25) または [Teams](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/integrate-coding-agent-with-teams?utm_source=changelog-docs-copilot-coding-agent-slack&utm_medium=changelog&utm_campaign=universe25) との Copilot コーディングエージェントの統合について詳しく学び、[GitHub Community](https://github.com/orgs/community/discussions/177494?utm_source=changelog-community-copilot-coding-agent-slack&utm_medium=changelog&utm_campaign=universe25) でディスカッションに参加してください。
