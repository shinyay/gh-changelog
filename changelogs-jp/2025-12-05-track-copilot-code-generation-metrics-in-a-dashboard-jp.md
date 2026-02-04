---
title: "ダッシュボードでCopilotコード生成メトリクスを追跡"
date: "2025-12-05"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-05-track-copilot-code-generation-metrics-in-a-dashboard"
fetched_at: "2026-02-03T14:50:55.039198Z"
lang: "ja"
---

# ダッシュボードでCopilotコード生成メトリクスを追跡

## Overview
GitHub Copilotのコード行数(LoC)メトリクスをコード生成インサイトダッシュボードで表示できるようになりました。

## Detailed Explanation
### 概要
- GitHub Copilotのコード行数(LoC)メトリクスをコード生成インサイトダッシュボードで表示できるようになりました。
- 開始するには、Enterprisesページに移動し、エンタープライズを選択して、**Insights**タブをクリックします。左サイドバーで**Code generation**を選択します。より詳細なデータを含むNDJSONダウンロードも、ダッシュボードの右上隅で利用できます。
- ダッシュボードには、エンタープライズ全体の集計されたコード生成アクティビティが表示されます:
  - **AIで変更されたコード行数**: すべてのモードにわたって追加または削除されたコード行の合計。
  - **ユーザー主導のコード変更**: 補完とチャットアクションを通じて提案または手動で追加された行。
  - **エージェント主導のコード変更**: edit、agent、およびカスタムモードにわたってエージェントによって自動的に追加または削除された行。
  - **モデルと言語別のアクティビティ**: モデルと言語でグループ化された、ユーザー主導およびエージェント主導のアクティビティの両方。
- これらのメトリクスを表示するには、**Copilot usage metrics**ポリシーが有効になっている必要があります。有効にするには、Enterprisesページに移動し、エンタープライズを選択して、**AI Controls**タブをクリックします。左サイドバーで**Copilot**を選択し、**Metrics**までスクロールします。
- エンタープライズオーナー、請求マネージャー、および**View Enterprise Copilot Metrics**権限を持つエンタープライズカスタムロールを持つユーザーは、ダッシュボードにアクセスできます。
- 詳細については、ドキュメントをご覧ください。

## Insights (derived from article language)
- 詳細については、ドキュメントをご覧ください。

## Article Content (cleaned)
GitHub Copilotのコード行数(LoC)メトリクスをコード生成インサイトダッシュボードで表示できるようになりました。


開始するには、[Enterprises](https://github.com/settings/enterprises)ページに移動し、エンタープライズを選択して、**Insights**タブをクリックします。左サイドバーで**Code generation**を選択します。より詳細なデータを含むNDJSONダウンロードも、ダッシュボードの右上隅で利用できます。


ダッシュボードには、エンタープライズ全体の集計されたコード生成アクティビティが表示されます:


* **AIで変更されたコード行数:** すべてのモードにわたって追加または削除されたコード行の合計。
* **ユーザー主導のコード変更:** 補完とチャットアクションを通じて提案または手動で追加された行。
* **エージェント主導のコード変更:** edit、agent、およびカスタムモードにわたってエージェントによって自動的に追加または削除された行。
* **モデルと言語別のアクティビティ:** モデルと言語でグループ化された、ユーザー主導およびエージェント主導のアクティビティの両方。


これらのメトリクスを表示するには、**Copilot usage metrics**ポリシーが有効になっている必要があります。有効にするには、[Enterprises](https://github.com/settings/enterprises)ページに移動し、エンタープライズを選択して、**AI Controls**タブをクリックします。左サイドバーで**Copilot**を選択し、**Metrics**までスクロールします。


エンタープライズオーナー、請求マネージャー、および**View Enterprise Copilot Metrics**権限を持つエンタープライズカスタムロールを持つユーザーは、ダッシュボードにアクセスできます。


詳細については、[ドキュメント](https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/administer-copilot/manage-for-enterprise/view-code-generation)をご覧ください。
