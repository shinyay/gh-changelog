---
title: "Visual Studio CodeのGitHub Copilotで自動モデル選択が一般提供開始"
date: "2025-12-10"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-10-auto-model-selection-is-generally-available-in-github-copilot-in-visual-studio-code"
fetched_at: "2026-02-03T14:50:54.988574Z"
lang: "ja"
---

# Visual Studio CodeのGitHub Copilotで自動モデル選択が一般提供開始

## Overview
GitHub Copilotの自動モデル選択がVisual Studio Codeのすべての Copilotプランで一般提供開始となりました。自動モードでは、Copilotが現在のモデルの可用性に基づいて自動的にモデルを選択します。

## Detailed Explanation
### 概要
- GitHub Copilotの自動モデル選択がVisual Studio Codeのすべての Copilotプランで一般提供開始となりました。自動モードでは、Copilotが現在のモデルの可用性に基づいて自動的にモデルを選択します。

### 仕組み
- 自動モードは動的で、リアルタイムの可用性に基づいてモデルにルーティングします。お気に入りのモデルへの同じアクセスを提供しながら、レート制限を軽減します。自動モードは、プランとポリシーに基づいてGPT-5.1-Codex-Max、GPT-5 mini、GPT-4.1、Sonnet 4.5、Haiku 4.5などのモデルにルーティングします。自動モードがルーティングするモデルは時間とともに変化します。
- **透明性**: モデルの応答にカーソルを合わせると、どのモデルが使用されたかを確認できます。
- **制御を維持**: 自動モードと特定のモデルをいつでも切り替えることができます。
- **ポリシーを尊重**: 自動モードはすべてのユーザーおよび管理者のモデル設定を尊重します。

### プレミアムリクエストの使用
- 自動モードのプレミアムリクエスト使用は、選択されたモデルに基づいて請求されます。これは現在、上記の0倍から1倍の乗数を持つモデルに制限されています。すべての有料サブスクライバーは、自動モードを使用する際にモデル乗数の10%割引を受けられます(例: 自動モードが1倍の乗数を持つモデルを使用する場合、1ではなく0.9プレミアムリクエストを消費します)。

### 今後の展開
- 今日、自動モードはお客様に代わって容易に利用可能な高品質モデルにルーティングします。
- 近日中に、自動モードはさらにインテリジェントになり、Copilotがタスクに最も適したモデルを選択し、リクエストの複雑さレベルにモデルを合わせる拡張機能を獲得します。
- 質問やフィードバックがありますか? [コミュニティディスカッション](https://github.com/orgs/community/discussions/categories/copilot-conversations)に参加して、ご意見をお聞かせください。

## Impact / Who’s Affected
- GitHub Copilotの自動モデル選択がVisual Studio Codeのすべての Copilotプランで一般提供開始となりました。
- **プレミアムリクエストの使用**: 自動モードのプレミアムリクエスト使用は、選択されたモデルに基づいて請求されます。これは現在、上記の0倍から1倍の乗数を持つモデルに制限されています。

## Caveats / Limitations
- **プレミアムリクエストの使用**: 自動モードのプレミアムリクエスト使用は、選択されたモデルに基づいて請求されます。これは現在、上記の0倍から1倍の乗数を持つモデルに制限されています。

## Article Content (cleaned)
[GitHub Copilotの自動モデル選択](https://docs.github.com/copilot/concepts/auto-model-selection)がVisual Studio Codeのすべての Copilotプランで一般提供開始となりました。自動モードでは、Copilotが現在のモデルの可用性に基づいて自動的にモデルを選択します。


### [仕組み](#how-it-works)


自動モードは動的で、リアルタイムの可用性に基づいてモデルにルーティングします。お気に入りのモデルへの同じアクセスを提供しながら、レート制限を軽減します。自動モードは、プランとポリシーに基づいてGPT\-5\.1\-Codex\-Max、GPT\-5 mini、GPT\-4\.1、Sonnet 4\.5、Haiku 4\.5などのモデルにルーティングします。自動モードがルーティングするモデルは時間とともに変化します。


* **透明性**: モデルの応答にカーソルを合わせると、どのモデルが使用されたかを確認できます。
* **制御を維持**: 自動モードと特定のモデルをいつでも切り替えることができます。
* **ポリシーを尊重**: 自動モードはすべてのユーザーおよび管理者のモデル設定を尊重します。


## [Premium request use](#premium-request-use)


自動モードのプレミアムリクエスト使用は、選択されたモデルに基づいて請求されます。これは現在、上記の[0倍から1倍の乗数を持つモデル](https://docs.github.com/copilot/concepts/billing/copilot-requests#model-multipliers)に制限されています。すべての有料サブスクライバーは、自動モードを使用する際にモデル乗数の10%割引を受けられます(例: 自動モードが1倍の乗数を持つモデルを使用する場合、1ではなく0\.9プレミアムリクエストを消費します)。


## [Where we’re headed](#where-were-headed)


今日、自動モードはお客様に代わって容易に利用可能な高品質モデルにルーティングします。


近日中に、自動モードはさらにインテリジェントになり、Copilotがタスクに最も適したモデルを選択し、リクエストの複雑さレベルにモデルを合わせる拡張機能を獲得します。


質問やフィードバックがありますか? [コミュニティディスカッション](https://github.com/orgs/community/discussions/categories/copilot-conversations)に参加して、ご意見をお聞かせください。
