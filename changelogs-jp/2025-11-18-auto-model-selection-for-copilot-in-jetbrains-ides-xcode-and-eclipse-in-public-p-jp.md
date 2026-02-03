---
title: "JetBrains IDE、Xcode、Eclipse用Copilotの自動モデル選択がパブリックプレビューに"
date: "2025-11-18"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-18-auto-model-selection-for-copilot-in-jetbrains-ides-xcode-and-eclipse-in-public-preview"
fetched_at: "2026-02-03T14:50:55.204377Z"
lang: "ja"
---

# JetBrains IDE、Xcode、Eclipse用Copilotの自動モデル選択がパブリックプレビューに

## Overview
JetBrains IDE、Xcode、Eclipse用のGitHub Copilotに、自動的にモデルを選択する「Auto」オプションが追加されました。Copilot Chatのモデルピッカーから「Auto」を選択してください。この機能はすべてのCopilotプランで利用できます。

## Detailed Explanation
### Overview
- JetBrains IDE、Xcode、Eclipse用のGitHub Copilotに、自動的にモデルを選択する「Auto」オプションが追加されました。Copilot Chatのモデルピッカーから「Auto」を選択してください。この機能はすべてのCopilotプランで利用できます。

### How it works
- この初期プレビューでは、Autoはモデルの可用性を最適化し、現在、サブスクリプションタイプに応じてGPT-5、GPT-5 mini、GPT-4.1、Sonnet 4.5、Haiku 4.5にリクエストをルーティングしています。今後さらに多くのモデルが追加される予定です。
- 透明性：モデルの応答にマウスを合わせることで、使用されたモデルを確認できます。
- コントロール維持：Autoと特定のモデルをいつでも切り替えられます。
- ポリシーの尊重：Autoはすべてのユーザーモデル設定を尊重します。

### Premium request use
- Autoのプレミアムリクエスト使用量は、選択されたモデルに基づいており、現在は上記のリストにある0倍から1倍の乗数を持つモデルに制限されています。Copilot Pro、Pro+、Business、EnterpriseサブスクライバーがAutoを使用すると、モデル乗数が10%割引されます（例：Autoが1倍の乗数を持つモデルを使用する場合、1ではなく0.9のプレミアムリクエストが消費されます）。

### Getting started
- 個人ユーザーの場合は、エディタのCopilot Chatでモデルピッカーの「Auto」を選択してください。
- Copilot BusinessまたはCopilot Enterpriseサブスクライバーの場合は、管理者が使用する前に「Editor preview features」ポリシーを有効にする必要があります。Autoに関するドキュメントの詳細をご覧ください。

### This is just the beginning
- このAutoプレビューはモデルの可用性を最適化していますが、タスクとコンテキストを考慮したより賢いものにするため、今後のアップデートに積極的に取り組んでいます。このプレビューに対するフィードバックは、次の内容を直接形作ります。
- 質問やフィードバックはありますか？ぜひお聞かせください！コミュニティディスカッションに参加して共有してください。

## Impact / Who's Affected
- プレミアムリクエスト使用量 Autoのプレミアムリクエスト使用量は、選択されたモデルに基づいており、現在は上記のリストにある0倍から1倍の乗数を持つモデルに制限されています。

## Caveats / Limitations
- プレミアムリクエスト使用量 Autoのプレミアムリクエスト使用量は、選択されたモデルに基づいており、現在は上記のリストにある0倍から1倍の乗数を持つモデルに制限されています。

## Insights (derived from article language)
- Autoに関するドキュメントの詳細をご覧ください。

## Article Content (cleaned)
JetBrains IDE、Xcode、Eclipse用のGitHub Copilotに、自動的にモデルを選択する**Auto**オプションが追加されました。Copilot Chatのモデルピッカーから**Auto**を選択してください。この機能はすべてのCopilotプランで利用できます。


### [How it works](#how-it-works)


この初期プレビューでは、Autoはモデルの可用性を最適化し、現在、サブスクリプションタイプに応じてGPT-5、GPT-5 mini、GPT-4.1、Sonnet 4.5、Haiku 4.5にリクエストをルーティングしています。今後さらに多くのモデルが追加される予定です。


* **透明性**：モデルの応答にマウスを合わせることで、使用されたモデルを確認できます。
* **コントロール維持**：Autoと特定のモデルをいつでも切り替えられます。
* **ポリシーの尊重**：Autoはすべてのユーザーモデル設定を尊重します。


### [Premium request use](#premium-request-use)


Autoのプレミアムリクエスト使用量は、選択されたモデルに基づいており、現在は[上記のリストにある0倍から1倍の乗数を持つモデル](https://docs.github.com/copilot/concepts/billing/copilot-requests#model-multipliers)に制限されています。Copilot Pro、Pro+、Business、EnterpriseサブスクライバーがAutoを使用すると、モデル乗数が10%割引されます（例：Autoが1倍の乗数を持つモデルを使用する場合、1ではなく0.9のプレミアムリクエストが消費されます）。


### [Getting started](#getting-started)


個人ユーザーの場合は、エディタのCopilot Chatでモデルピッカーの**Auto**を選択してください。


Copilot BusinessまたはCopilot Enterpriseサブスクライバーの場合は、管理者が使用する前に**Editor preview features**ポリシーを有効にする必要があります。[Autoに関するドキュメント](https://docs.github.com/copilot/concepts/auto-model-selection)の詳細をご覧ください。


### [This is just the beginning](#this-is-just-the-beginning)


このAutoプレビューはモデルの可用性を最適化していますが、タスクとコンテキストを考慮したより賢いものにするため、今後のアップデートに積極的に取り組んでいます。このプレビューに対するフィードバックは、次の内容を直接形作ります。


質問やフィードバックはありますか？ぜひお聞かせください！[コミュニティディスカッション](https://github.com/orgs/community/discussions/categories/copilot-conversations)に参加して共有してください。
