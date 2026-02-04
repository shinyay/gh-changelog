---
title: "組織のCopilot使用状況を追跡"
date: "2025-12-16"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-16-track-organization-copilot-usage"
fetched_at: "2026-02-03T14:50:54.930576Z"
lang: "ja"
---

# 組織のCopilot使用状況を追跡

## Overview
Copilot使用状況API経由で組織のCopilot使用メトリクスにアクセスできるようになりました。

## Detailed Explanation
### Overview
- Copilot使用状況API経由で組織のCopilot使用メトリクスにアクセスできるようになりました。
- APIには、さまざまなCopilot機能の使用統計、ユーザーエンゲージメントデータ、機能導入メトリクスなど、集約されたユーザー固有のメトリクスを含むレポートが含まれています。
- これらのメトリクスを表示するには、Copilot使用メトリクスポリシーを有効にする必要があります。
- エンタープライズアカウントでこの設定を有効にするには、Enterprisesページに移動し、エンタープライズを選択して、AI Controlsタブをクリックします。左サイドバーでCopilotを選択し、Metricsまでスクロールします。Enabled everywhereを選択します。
- スタンドアロン組織アカウントでこの設定を有効にするには、Organizationページに移動し、組織を選択して、Settingsタブをクリックします。左サイドバーでCopilot > Policiesを選択します。Features > Copilot usage metricsまでスクロールします。Enabledを選択します。
- 組織オーナーおよびView Organization Copilot Metrics権限を持つ組織カスタムロールを持つユーザーがAPIにアクセスできます。
- 詳細については、ドキュメントをご覧ください。

## Insights (derived from article language)
- 詳細については、ドキュメントをご覧ください。

## Article Content (cleaned)
[Copilot使用状況API](https://docs.github.com/en/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics?apiVersion=2022-11-28#get-copilot-organization-usage-metrics-for-a-specific-day)経由で組織のCopilot使用メトリクスにアクセスできるようになりました。


APIには、さまざまなCopilot機能の使用統計、ユーザーエンゲージメントデータ、機能導入メトリクスなど、集約されたユーザー固有のメトリクスを含むレポートが含まれています。


これらのメトリクスを表示するには、**Copilot使用メトリクス**ポリシーを有効にする必要があります。


* エンタープライズアカウントでこの設定を有効にするには、[Enterprisesページ](https://github.com/settings/enterprises)に移動し、エンタープライズを選択して、**AI Controls**タブをクリックします。左サイドバーで**Copilot**を選択し、**Metrics**までスクロールします。**Enabled everywhere**を選択します。
* スタンドアロン組織アカウントでこの設定を有効にするには、[Organizationページ](https://github.com/settings/organizations)に移動し、組織を選択して、**Settings**タブをクリックします。左サイドバーで**Copilot** \> **Policies**を選択します。**Features** \> **Copilot usage metrics**までスクロールします。**Enabled**を選択します。


組織オーナーおよび`View Organization Copilot Metrics`権限を持つ組織カスタムロールを持つユーザーがAPIにアクセスできます。


詳細については、[ドキュメント](https://docs.github.com/en/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics?apiVersion=2022-11-28#get-copilot-organization-usage-metrics-for-a-specific-day)をご覧ください。
