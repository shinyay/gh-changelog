---
title: "GitHub Code Quality がパブリックプレビューで利用可能に"
date: "2025-10-28"
type: "new releases"
labels: ["application security", "platform governance", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-github-code-quality-in-public-preview"
fetched_at: "2026-02-03T14:50:55.535491Z"
lang: "ja"
---

# GitHub Code Quality がパブリックプレビューで利用可能に

## Overview
GitHub Code Quality がパブリックプレビューで利用可能になりました！すべてのプルリクエストが改善の機会に変わります。コンテキスト内の検出結果、ワンクリック Copilot 修正、信頼性とメンテナンス性のスコアにより、細かい修正を追いかける時間を減らし、構築に集中できる時間が増えます。プルリクエストとバックログの両方で品質の問題を表示するため、必要なタイミングで技術的負債を修正できます。

## Detailed Explanation
### 概要
- GitHub Code Quality がパブリックプレビューで利用可能になりました！すべてのプルリクエストが改善の機会に変わります。コンテキスト内の検出結果、ワンクリック Copilot 修正、信頼性とメンテナンス性のスコアにより、細かい修正を追いかける時間を減らし、構築に集中できる時間が増えます。プルリクエストとバックログの両方で品質の問題を表示するため、必要なタイミングで技術的負債を修正できます。

### 対象者
- コードの品質に関するコンテキスト内フィードバックを求め、技術的負債をレビュー可能な修正に変換する簡単な方法を求める開発者とエンジニアリングチーム。

### ハイライト
- ワンクリック有効化：GitHub Code Quality を迅速かつ簡単に試せます。
- アクション可能な検出結果：CodeQL ベースの品質ルールが、Java、C#、Python、JavaScript、Go、Ruby のメンテナンス性と信頼性の問題を検出します。
- コンテキスト内レビュー：プルリクエスト内で直接品質検出結果を確認でき、すぐに行動できるガイダンスを提供します。
- 品質スコアで進捗を追跡：品質リポジトリビューでは、ルールごとに検出結果をグループ化して修正の優先順位をつけられます。信頼性とメンテナンス性のスコアは重大度を要約し、改善対象の特定を支援します。

### 試し方
- 組織でプレビュー機能が有効になっている場合は、リポジトリの設定 > コード品質に移動して機能を有効にします。
- サポートされている言語でプルリクエストを開き、インラインの検出結果と自動修正の提案を確認します。
- まだアクセスできない場合は、組織管理者にプレビューフラグの有効化を依頼してください。詳細は Code Quality の有効化に関するドキュメントをご覧ください。

### 近日公開予定
- 組織レベルのダッシュボードと有効化機能により、コード品質を大規模に管理。
- テストカバレッジメトリクスによる実用的な品質データの提供。
- プログラムでコード品質データを取得したり、大規模に有効化するための API。
- プルリクエスト向けの Copilot による品質推奨機能により、静的解析の検出結果を補完。

### 可用性と価格
- GitHub Code Quality は現在、GitHub Enterprise Cloud と Team で利用可能ですが、Enterprise Server では利用できません。プレビュー期間中は無料ですが、スキャンには Actions 分が発生します。

### 詳細情報
- GitHub Code Quality のドキュメントをご確認ください。GitHub Community の Code Quality アナウンスでディスカッションに参加し、フィードバックをお寄せください。

## Key Changes
記事では明示されていません。

## Impact / Who's Affected
- GitHub Code Quality がパブリックプレビューで利用可能になりました！

## Caveats / Limitations
記事では明示されていません。

## Insights (derived from article language)
- 詳細情報 GitHub Code Quality のドキュメントをご確認ください。

## Article Content (cleaned)
GitHub Code Quality がパブリックプレビューで利用可能になりました！すべてのプルリクエストが改善の機会に変わります。コンテキスト内の検出結果、ワンクリック Copilot 修正、信頼性とメンテナンス性のスコアにより、細かい修正を追いかける時間を減らし、構築に集中できる時間が増えます。プルリクエストとバックログの両方で品質の問題を表示するため、必要なタイミングで技術的負債を修正できます。


### [対象者](#who-this-is-for)


コードの品質に関するコンテキスト内フィードバックを求め、技術的負債をレビュー可能な修正に変換する簡単な方法を求める開発者とエンジニアリングチーム。


### [ハイライト](#highlights)


* *ワンクリック有効化*: GitHub Code Quality を迅速かつ簡単に試せます。
* *アクション可能な検出結果*: CodeQL ベースの品質ルールが、Java、C\#、Python、JavaScript、Go、Ruby のメンテナンス性と信頼性の問題を検出します。
* *コンテキスト内レビュー*: プルリクエスト内で直接品質検出結果を確認でき、すぐに行動できるガイダンスを提供します。
* *品質スコアで進捗を追跡*: 品質リポジトリビューでは、ルールごとに検出結果をグループ化して修正の優先順位をつけられます。信頼性とメンテナンス性のスコアは重大度を要約し、改善対象の特定を支援します。


### [試し方](#how-to-try-it)


1. 組織でプレビュー機能が有効になっている場合は、リポジトリの **設定** \> **コード品質** に移動して機能を有効にします。
2. サポートされている言語でプルリクエストを開き、インラインの検出結果と自動修正の提案を確認します。
3. まだアクセスできない場合は、組織管理者にプレビューフラグの有効化を依頼してください。詳細は [Code Quality の有効化に関するドキュメント](https://docs.github.com/code-security/code-quality/how-tos/enable-code-quality?utm_source=changelog-docs-gh-code-quality&utm_medium=changelog&utm_campaign=universe25) をご覧ください。


### [近日公開予定](#coming-soon)


* 組織レベルのダッシュボードと有効化機能により、コード品質を大規模に管理。
* テストカバレッジメトリクスによる実用的な品質データの提供。
* プログラムでコード品質データを取得したり、大規模に有効化するための API。
* プルリクエスト向けの Copilot による品質推奨機能により、静的解析の検出結果を補完。


### [可用性と価格](#availability-and-pricing)


GitHub Code Quality は現在、GitHub Enterprise Cloud と Team で利用可能ですが、Enterprise Server では利用できません。プレビュー期間中は無料ですが、スキャンには Actions 分が発生します。


### [詳細情報](#learn-more)


[GitHub Code Quality のドキュメント](https://docs.github.com/code-security/code-quality/how-tos/enable-code-quality?utm_source=changelog-docs-gh-code-quality&utm_medium=changelog&utm_campaign=universe25) をご確認ください。  

[GitHub Community の Code Quality アナウンス](https://github.com/orgs/community/discussions/177488?utm_source=changelog-community-gh-code-quality&utm_medium=changelog&utm_campaign=universe25) でディスカッションに参加し、フィードバックをお寄せください。
