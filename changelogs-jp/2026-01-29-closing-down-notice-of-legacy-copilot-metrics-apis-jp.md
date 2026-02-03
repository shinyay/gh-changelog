---
title: "レガシーCopilotメトリクスAPIの終了通知"
date: "2026-01-29"
type: "Retired"
labels: ["account management", "copilot", "enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-29-closing-down-notice-of-legacy-copilot-metrics-apis"
fetched_at: "2026-02-03T14:50:49.341904Z"
lang: "ja"
---

# レガシーCopilotメトリクスAPIの終了通知

## Overview
新しい、より包括的な使用メトリクスエンドポイントへの移行の一環として、3つのレガシーCopilotメトリクスAPIを終了します。これらのAPIのサポートは限定的であり、新機能は開発されません。

## Detailed Explanation
### 概要
- 新しい、より包括的な使用メトリクスエンドポイントへの移行の一環として、3つのレガシーCopilotメトリクスAPIを終了します。これらのAPIのサポートは限定的であり、新機能は開発されません。
- ユーザーレベル機能エンゲージメントメトリクスAPIとダイレクトデータアクセスAPIは、2026年3月2日に終了します。
- CopilotメトリクスAPIは、2026年4月2日に終了します。
- 中断を避けるために、既存のワークフローを最新のCopilot使用メトリクスエンドポイントに移行することを強くお勧めします。

### これらのAPIは何をしますか？
- これらのAPIは、GitHub Copilot機能の採用と使用に関する可視性を提供します：
- ユーザーレベル機能エンゲージメントメトリクスAPIは、バイナリインジケータを通じて特定のCopilot機能のユーザー採用の簡略化されたビューを提供します。
- ダイレクトデータアクセスAPIは、サポートされているIDE内のCopilotコード補完アクティビティのユーザーレベルイベントデータを提供します。
- CopilotメトリクスAPIは、主にIDE使用に焦点を当てた集約された使用メトリクスを提供します。

### なぜですか？
- より深い柔軟性を提供する新しいCopilot使用メトリクスAPIのセットをリリースしました。最新のAPIに統合することで、次のことができます：
- Copilotメトリクスの単一の統一された信頼できる情報源を提供する。
- IDEエージェント、モデル、言語、コード行、きめ細かい権限を含む、より詳細で価値のある洞察を提供する。
- サポートオーバーヘッドを削減し、製品体験を合理化する。

### 今後推奨されることは何ですか？
- エンタープライズ、組織、ユーザーレベルでの包括的な使用データを提供する最新のCopilot使用メトリクスAPIへの移行をお勧めします。
- これらのエンドポイントは、以下を含む拡張されたIDEテレメトリで集約されたメトリクスを返します：
- 編集モードとエージェントの使用。
- 提案されたコード行と承認されたコード行。
- 言語とモデルの内訳。
- レガシーAPIでは利用できない追加の使用ディメンション。
- 新しいAPIは現在パブリックプレビュー中であり、近い将来一般提供される予定です。

## Impact / Who’s Affected
- これらのAPIのサポートは限定的であり、新機能は開発されません。
- ユーザーレベル機能エンゲージメントメトリクスAPIとダイレクトデータアクセスAPIは、2026年3月2日に終了します。
- CopilotメトリクスAPIは、2026年4月2日に終了します。
- 新しいAPIは現在パブリックプレビュー中であり、近い将来一般提供される予定です。

## Caveats / Limitations
- これらのAPIのサポートは限定的であり、新機能は開発されません。

## Insights (derived from article language)
- エンタープライズ、組織、ユーザーレベルでの包括的な使用データを提供する最新のCopilot使用メトリクスAPIへの移行をお勧めします。

## Article Content (cleaned)
新しい、より包括的な使用メトリクスエンドポイントへの移行の一環として、3つのレガシーCopilotメトリクスAPIを終了します。これらのAPIのサポートは限定的であり、新機能は開発されません。


* ユーザー\-レベル機能エンゲージメントメトリクスAPIとダイレクトデータアクセスAPIは、2026年3月2日に終了します。
* CopilotメトリクスAPIは、2026年4月2日に終了します。


中断を避けるために、既存のワークフローを[最新のCopilot使用メトリクスエンドポイント](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics?apiVersion=2022-11-28)に移行することを強くお勧めします。


### [What do these APIs do?](https://github.blog/changelog/feed/#what-do-these-apis-do)


これらのAPIは、GitHub Copilot機能の採用と使用に関する可視性を提供します：


* [ユーザー\-レベル機能エンゲージメントメトリクスAPI](https://docs.github.com/enterprise-cloud@latest/early-access/copilot/user-level-feature-engagement-metrics-api)は、バイナリインジケータを通じて特定のCopilot機能のユーザー採用の簡略化されたビューを提供します。
* [ダイレクトデータアクセスAPI](https://docs.github.com/enterprise-cloud@latest/early-access/copilot/direct-data-access)は、サポートされているIDE内のCopilotコード補完アクティビティのユーザー\-レベルイベントデータを提供します。
* [CopilotメトリクスAPI](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-metrics?apiVersion=2022-11-28)は、主にIDE使用に焦点を当てた集約された使用メトリクスを提供します。


### [Why?](https://github.blog/changelog/feed/#why)


より深い柔軟性を提供する新しいCopilot使用メトリクスAPIのセットをリリースしました。最新のAPIに統合することで、次のことができます：


* Copilotメトリクスの単一の統一された信頼できる情報源を提供する。
* IDEエージェント、モデル、言語、コード行、きめ細かい権限を含む、より詳細で価値のある洞察を提供する。
* サポートオーバーヘッドを削減し、製品体験を合理化する。


### [What's recommended moving forward?](https://github.blog/changelog/feed/#whats-recommended-moving-forward)


エンタープライズ、組織、ユーザーレベルでの包括的な使用データを提供する[最新のCopilot使用メトリクスAPI](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics?apiVersion=2022-11-28)への移行をお勧めします。


これらのエンドポイントは、以下を含む拡張されたIDEテレメトリで集約されたメトリクスを返します：


* 編集モードとエージェントの使用。
* 提案されたコード行と承認されたコード行。
* 言語とモデルの内訳。
* レガシーAPIでは利用できない追加の使用ディメンション。


新しいAPIは現在パブリックプレビュー中であり、近い将来一般提供される予定です。
