---
title: "Copilot 使用状況メトリクスダッシュボードと API がパブリックプレビューで利用可能"
date: "2025-10-28"
type: "new releases"
labels: ["copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-copilot-usage-metrics-dashboard-and-api-in-public-preview"
fetched_at: "2026-02-03T14:50:55.578051Z"
lang: "ja"
---

# Copilot 使用状況メトリクスダッシュボードと API がパブリックプレビューで利用可能

## Overview
Copilot 使用状況メトリクスダッシュボードと対応する API が、GitHub Enterprise のパブリックプレビューで利用可能になりました。

## Detailed Explanation
### 概要
- Copilot 使用状況メトリクスダッシュボードと対応する API が、GitHub Enterprise のパブリックプレビューで利用可能になりました。
- AI 時代のソフトウェア開発では、チームが AI を使っているかどうかではなく、どれだけ上手に使っているかが重要です。
- GitHub Copilot 使用状況メトリクスダッシュボードと API は、Copilot を使用する GitHub Enterprise のお客様向けにパブリックプレビューで提供され、データでその疑問に答えるのに役立ちます。
- IDE での Copilot の採用とエンゲージメントがエンタープライズ全体とユーザー間でどのように異なるかを確認し、誰が、どこで、どのように使用しているかを理解できます。

### パブリックプレビューに含まれる内容
- Copilot 使用状況メトリクスダッシュボードは、エンタープライズ管理者と請求管理者に、Insights タブで Copilot の使用状況と採用状況を直接確認できるようにします。ダッシュボードは集約されたエンタープライズビューを提供し、NDJSON ダウンロードまたは API はより詳細な分析のためにユーザーレベルの粒度を提供します。
- このパブリックプレビューには、次のメトリクスが含まれます：
- エージェントモードを含む GitHub Copilot IDE モード全体での日次および週次アクティブユーザー。
- ユーザーベース全体でのエージェント採用。
- すべての IDE モードでの追加および削除されたコード行。
- IDE 全体での言語とモデルの使用パターン。
- これらのメトリクスは次のことを理解するのに役立ちます：
- 全体的な使用状況と採用：週次使用などの指標をレビューすることで、エンタープライズ全体での Copilot 採用の広範な視点を得られます。
- 特定のモデル、機能、言語の使用状況：チームが最も利用している AI モデルとプログラミング言語を確認し、さらなる価値を生み出せる領域を特定します。
- エージェント採用率：リファクタリング、デバッグ、複雑な問題解決などの高度なタスクに Copilot を使用している開発者の数を追跡します。エージェント採用率が高いということは、真に変革的なコーディングへの移行を示しています。
- これらはまとめて、誰が Copilot を採用しているか、どの程度一貫しているか、そしてエンタープライズ全体でその使用がどのようなものかを示す基礎的なメトリクスです。

### エンタープライズで Copilot 使用状況メトリクスを有効にする方法
- デフォルトでは、プライベートプレビューに参加していた場合を除き、Copilot 使用状況メトリクスは無効になっています。その場合は有効のままです。
- エンタープライズ管理者は次の手順で有効にできます：
- github.com で AI Controls タブに移動します。
- 左サイドバーで Copilot を選択します。
- "Metrics" セクションまでスクロールし、Copilot usage metrics が表示されます。
- Copilot usage metrics ポリシー設定を Enabled に変更します。これにより、エンタープライズの Copilot 使用状況メトリクスダッシュボードと API が有効になり、エンタープライズ管理者と請求管理者が使用状況と採用状況のデータを表示できるようになります。
- 有効にすると、エンタープライズレベルの Insights タブから直接、またはエンタープライズおよびユーザーレベル API を通じて Copilot 使用状況メトリクスダッシュボードにアクセスできます。

### 詳細
- Copilot 使用状況メトリクスダッシュボードのドキュメントを表示する。Copilot 使用状況メトリクス API を探索する。ディスカッションに参加してフィードバックを共有し、質問してください。
- 編集者注（2025年10月29日）：コミュニティディスカッションのリンクを正しいディスカッションページに更新しました。

## Impact / Who’s Affected
- Copilot 使用状況メトリクスダッシュボードと対応する API が、GitHub Enterprise のパブリックプレビューで利用可能になりました。
- GitHub Copilot 使用状況メトリクスダッシュボードと API は、Copilot を使用する GitHub Enterprise のお客様向けにパブリックプレビューで提供され、データでその疑問に答えるのに役立ちます。
- パブリックプレビューに含まれる内容 Copilot 使用状況メトリクスダッシュボードは、エンタープライズ管理者と請求管理者に、Insights タブで Copilot の使用状況と採用状況を直接確認できるようにします。
- このパブリックプレビューには、次のメトリクスが含まれます：エージェントモードを含む GitHub Copilot IDE モード全体での日次および週次アクティブユーザー。

## Caveats / Limitations
- 編集者注（2025年10月29日）：コミュニティディスカッションのリンクを正しいディスカッションページに更新しました。

## Insights (derived from article language)
- 詳細 Copilot 使用状況メトリクスダッシュボードのドキュメントを表示する。

## Article Content (cleaned)
Copilot 使用状況メトリクスダッシュボードと対応する API が、GitHub Enterprise のパブリックプレビューで利用可能になりました。


AI 時代のソフトウェア開発では、チームが AI を**使っているか**どうかではなく、**どれだけ上手に**使っているかが重要です。


GitHub Copilot 使用状況メトリクスダッシュボードと API は、Copilot を使用する GitHub Enterprise のお客様向けにパブリックプレビューで提供され、データでその疑問に答えるのに役立ちます。


IDE での Copilot の採用とエンゲージメントがエンタープライズ全体とユーザー間でどのように異なるかを確認し、誰が、どこで、どのように使用しているかを理解できます。


## [What’s included in the public preview](#whats-included-in-the-public-preview)


**Copilot 使用状況メトリクスダッシュボード**は、エンタープライズ管理者と請求管理者に、**Insights** タブで Copilot の使用状況と採用状況を直接確認できるようにします。ダッシュボードは集約されたエンタープライズビューを提供し、NDJSON ダウンロードまたは API はより詳細な分析のためにユーザーレベルの粒度を提供します。


このパブリックプレビューには、次のメトリクスが含まれます：


* エージェントモードを含む GitHub Copilot IDE モード全体での日次および週次アクティブユーザー。
* ユーザーベース全体でのエージェント採用。
* すべての IDE モードでの追加および削除されたコード行。
* IDE 全体での言語とモデルの使用パターン。


これらのメトリクスは次のことを理解するのに役立ちます：


* **全体的な使用状況と採用**：週次使用などの指標をレビューすることで、エンタープライズ全体での Copilot 採用の広範な視点を得られます。
* **特定のモデル、機能、言語の使用状況**：チームが最も利用している AI モデルとプログラミング言語を確認し、さらなる価値を生み出せる領域を特定します。
* **エージェント採用率**：リファクタリング、デバッグ、複雑な問題解決などの高度なタスクに Copilot を使用している開発者の数を追跡します。エージェント採用率が高いということは、真に変革的なコーディングへの移行を示しています。


これらはまとめて、誰が Copilot を採用しているか、どの程度一貫しているか、そしてエンタープライズ全体でその使用がどのようなものかを示す基礎的なメトリクスです。


## [How to enable Copilot usage metrics in your enterprise](#how-to-enable-copilot-usage-metrics-in-your-enterprise)


デフォルトでは、プライベートプレビューに参加していた場合を除き、**Copilot 使用状況メトリクス**は無効になっています。その場合は有効のままです。


エンタープライズ管理者は次の手順で有効にできます：


1. github.com で **AI Controls** タブに移動します。
2. 左サイドバーで **Copilot** を選択します。
3. "Metrics" セクションまでスクロールし、**Copilot usage metrics** が表示されます。
4. **Copilot usage metrics** ポリシー設定を **Enabled** に変更します。これにより、エンタープライズの Copilot 使用状況メトリクスダッシュボードと API が有効になり、エンタープライズ管理者と請求管理者が使用状況と採用状況のデータを表示できるようになります。


有効にすると、エンタープライズレベルの **Insights** タブから直接、または[エンタープライズおよびユーザーレベル API](https://docs.github.com/enterprise-cloud@latest/early-access/copilot-metrics/apis/about-the-copilot-metrics-apis?utm_source=changelog-docs-copilot-usage-metrics-dashboard&utm_medium=changelog&utm_campaign=universe25) を通じて Copilot 使用状況メトリクスダッシュボードにアクセスできます。


## [Learn more](#learn-more)


[使用状況メトリクスダッシュボードのドキュメント](https://docs.github.com/enterprise-cloud@latest/early-access/copilot-metrics/dashboards/about-the-copilot-metrics-dashboard?utm_source=changelog-docs-copilot-usage-metrics-dashboard&utm_medium=changelog&utm_campaign=universe25)を表示する。  

[Copilot 使用状況メトリクス API](https://docs.github.com/enterprise-cloud@latest/early-access/copilot-metrics/apis/about-the-copilot-metrics-apis?utm_source=changelog-docs-copilot-usage-metrics-dashboard&utm_medium=changelog&utm_campaign=universe25) を探索する。  

[ディスカッション](https://github.com/orgs/community/discussions/177273?utm_source=changelog-community-copilot-usage-metrics-dashboard&utm_medium=changelog&utm_campaign=universe25)に参加してフィードバックを共有し、質問してください。


*編集者注（2025年10月29日）：コミュニティディスカッションのリンクを正しいディスカッションページに更新しました。*
