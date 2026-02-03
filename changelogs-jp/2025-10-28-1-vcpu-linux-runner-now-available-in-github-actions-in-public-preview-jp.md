---
title: "GitHub Actions の 1 vCPU Linux ランナーがパブリックプレビューで利用可能に"
date: "2025-10-28"
type: "new releases"
labels: ["actions", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-1-vcpu-linux-runner-now-available-in-github-actions-in-public-preview"
fetched_at: "2026-02-03T14:50:55.690458Z"
lang: "ja"
---

# GitHub Actions の 1 vCPU Linux ランナーがパブリックプレビューで利用可能に

## Overview
GitHub Actions の 1 vCPU Linux ランナーがパブリックプレビューになりました。軽量な処理を実行したいユーザーは、より低コストなランナーを利用できます。これらのランナーは、自動化タスク、Issue 操作、そして一般的な重い CI/CD ビルドとは異なる短時間ジョブ向けに最適化されています。

## Detailed Explanation
### Overview
- GitHub Actions の 1 vCPU Linux ランナーがパブリックプレビューになりました。軽量な処理を実行したいユーザーは、より低コストなランナーを利用できます。これらのランナーは、自動化タスク、Issue 操作、そして一般的な重い CI/CD ビルドとは異なる短時間ジョブ向けに最適化されています。

### Runner details
- これらのランナーは 1 vCPU と 5 GB の RAM を備えています。このランナーを使用すると、Actions のワークフローは専用の VM インスタンスではなくコンテナ内で実行されるため、GitHub 全体での自動化タスクをコスト効率よく高パフォーマンスに実行できます。各コンテナはハイパーバイザレベル 2 の分離を提供し、ジョブ完了時に自動的に破棄されます。
- このランナー種別を利用するジョブは、実行時間が 15 分に制限されます。この上限を超えるジョブは強制終了され、失敗となります。
- このランナーの代表的なユースケースは次のようなジョブです:
- Issue の自動ラベリング
- 基本的な言語コンパイル（例: webpack ビルド）
- Lint とフォーマット

### Get started today
- 使い始めるには、新規または既存のジョブ定義で新しいランナータイプ ubuntu-slim をターゲットにするだけです。
- より大きいランナーの料金情報は、GitHub Actions の課金ページを参照してください。
- GitHub Community でのディスカッションに参加してください。

## Impact / Who’s Affected
- GitHub Actions の 1 vCPU Linux ランナーがパブリックプレビューになりました。
- このランナー種別を利用するジョブは、実行時間が 15 分に制限されます。

## Caveats / Limitations
- このランナー種別を利用するジョブは、実行時間が 15 分に制限されます。

## Article Content (cleaned)
GitHub Actions の 1 vCPU Linux ランナーがパブリックプレビューになりました。軽量な処理を実行したいユーザーは、より低コストなランナーを利用できます。これらのランナーは、自動化タスク、Issue 操作、そして一般的な重い CI/CD ビルドとは異なる短時間ジョブ向けに最適化されています。


## [Runner details](#runner-details)


これらのランナーは 1 vCPU と 5 GB の RAM を備えています。このランナーを使用すると、Actions のワークフローは専用の VM インスタンスではなくコンテナ内で実行されるため、GitHub 全体での自動化タスクをコスト効率よく高パフォーマンスに実行できます。各コンテナはハイパーバイザレベル 2 の分離を提供し、コンテナはジョブ完了時に自動的に破棄されます。


このランナー種別を利用するジョブは、実行時間が 15 分に制限されます。この上限を超えるジョブは強制終了され、失敗となります。


このランナーの代表的なユースケースは次のようなジョブです:


* Issue の自動ラベリング
* 基本的な言語コンパイル（例: webpack ビルド）
* Lint とフォーマット


## [Get started today](#get-started-today)


使い始めるには、新しいランナータイプ `ubuntu-slim` を新規または既存のジョブ定義でターゲットにするだけです。


より大きいランナーの料金情報は、[GitHub Actions の課金](https://docs.github.com/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions?utm_source=changelog-docs-1-vcpu-linux-runner&utm_medium=changelog&utm_campaign=universe25)ページを参照してください。


[GitHub Community](https://github.com/orgs/community/discussions/categories/announcements?utm_source=changelog-community-1-vcpu-linux-runner&utm_medium=changelog&utm_campaign=universe25) でのディスカッションに参加してください。
