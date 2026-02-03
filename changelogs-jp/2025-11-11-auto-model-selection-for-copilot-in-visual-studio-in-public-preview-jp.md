---
title: "Visual Studio の Copilot の自動モデル選択がパブリックプレビューで利用可能"
date: "2025-11-11"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-11-auto-model-selection-for-copilot-in-visual-studio-in-public-preview"
fetched_at: "2026-02-03T14:50:55.338162Z"
lang: "ja"
---

# Visual Studio の Copilot の自動モデル選択がパブリックプレビューで利用可能

## Overview
Visual Studio の GitHub Copilot に、Copilot がモデルを選択する「自動」オプションがモデルピッカーに追加されました。自動はすべての Copilot プランで利用できるようになりました。

## Detailed Explanation
### 概要
- Visual Studio の GitHub Copilot に、Copilot がモデルを選択する「自動」オプションがモデルピッカーに追加されました。自動はすべての Copilot プランで利用できるようになりました。

### 仕組み
- この初期プレビューでは、自動はモデルの可用性を最適化し、現在、サブスクリプションタイプに応じて GPT-5、GPT-5 mini、GPT-4.1、Sonnet 4.5、および Haiku 4.5 にルーティングします。より多くのモデルが近日公開予定です。
- 透明性 : モデルの応答にカーソルを合わせることで、使用されたモデルを確認できます。
- コントロールを維持 : 自動と任意の特定のモデルをいつでも切り替えることができます。
- ポリシーを尊重 : 自動はすべてのユーザーモデル設定を尊重します。

### プレミアムリクエストの使用
- 自動のプレミアムリクエストの使用は、選択するモデルに基づいており、現在は上記の 0x から 1x の乗数を持つモデルに制限されています。Copilot Pro、Pro+、Business、および Enterprise サブスクライバーは、自動を使用する際にモデル乗数に対して 10% の割引を受けます（例: 自動が 1x 乗数を持つモデルを使用する場合、1 ではなく 0.9 プレミアムリクエストを消費します）。

### はじめに
- 個人ユーザーの場合は、Visual Studio の Copilot Chat に移動し、モデルピッカーで「自動」を選択してください。
- Copilot Business または Copilot Enterprise サブスクライバーの場合、使用する前に管理者が「エディタープレビュー機能ポリシー」を有効にする必要があります。自動に関するドキュメントで詳細をご確認ください。

### これは始まりに過ぎません
- この自動のプレビューは可用性を最適化していますが、タスクを考慮してより賢くするための今後の更新に積極的に取り組んでいます。このプレビューに対するあなたのフィードバックが、次の展開を直接形作ります。
- 質問やフィードバックがありますか？ぜひお聞かせください！コミュニティディスカッションに参加して共有してください。

## Impact / Who’s Affected
- 自動はすべての Copilot プランで利用できるようになりました。
- プレミアムリクエストの使用 自動のプレミアムリクエストの使用は、選択するモデルに基づいており、現在は上記の 0x から 1x の乗数を持つモデルに制限されています。

## Caveats / Limitations
- プレミアムリクエストの使用 自動のプレミアムリクエストの使用は、選択するモデルに基づいており、現在は上記の 0x から 1x の乗数を持つモデルに制限されています。

## Insights (derived from article language)
- 自動に関するドキュメントで詳細をご確認ください。

## Article Content (cleaned)
Visual Studio の GitHub Copilot に、Copilot がモデルを選択する「**自動**」オプションがモデルピッカーに追加されました。自動はすべての Copilot プランで利用できるようになりました。


### [仕組み](#how-it-works)


この初期プレビューでは、自動はモデルの可用性を最適化し、現在、サブスクリプションタイプに応じて GPT-5、GPT-5 mini、GPT-4.1、Sonnet 4.5、および Haiku 4.5 にルーティングします。より多くのモデルが近日公開予定です。


* **透明性**: モデルの応答にカーソルを合わせることで、使用されたモデルを確認できます。
* **コントロールを維持**: 自動と任意の特定のモデルをいつでも切り替えることができます。
* **ポリシーを尊重**: 自動はすべてのユーザーモデル設定を尊重します。


### [プレミアムリクエストの使用](#premium-request-use)


自動のプレミアムリクエストの使用は、選択するモデルに基づいており、現在は[上記の 0x から 1x の乗数を持つモデル](https://docs.github.com/copilot/concepts/billing/copilot-requests#model-multipliers)に制限されています。Copilot Pro、Pro+、Business、および Enterprise サブスクライバーは、自動を使用する際にモデル乗数に対して 10% の割引を受けます（例: 自動が 1x 乗数を持つモデルを使用する場合、1 ではなく 0.9 プレミアムリクエストを消費します）。


### [はじめに](#getting-started)


個人ユーザーの場合は、Visual Studio の Copilot Chat に移動し、モデルピッカーで「**自動**」を選択してください。


Copilot Business または Copilot Enterprise サブスクライバーの場合、使用する前に管理者が「**エディタープレビュー機能ポリシー**」を有効にする必要があります。[自動に関するドキュメント](https://docs.github.com/copilot/concepts/auto-model-selection)で詳細をご確認ください。


### [これは始まりに過ぎません](#this-is-just-the-beginning)


この自動のプレビューは可用性を最適化していますが、タスクを考慮してより賢くするための今後の更新に積極的に取り組んでいます。このプレビューに対するあなたのフィードバックが、次の展開を直接形作ります。


質問やフィードバックがありますか？ぜひお聞かせください！[コミュニティディスカッション](https://github.com/orgs/community/discussions/categories/copilot-conversations)に参加して共有してください。
