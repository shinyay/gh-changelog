---
title: "GitHub Actions で 1 vCPU Linux ランナーが一般提供開始"
date: "2026-01-22"
type: "new releases"
labels: ["actions"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-22-1-vcpu-linux-runner-now-generally-available-in-github-actions"
fetched_at: "2026-02-03T14:50:54.721404Z"
lang: "ja"
---

# GitHub Actions で 1 vCPU Linux ランナーが一般提供開始

## Overview
GitHub Actions の 1 vCPU Linux ランナーが一般提供されるようになりました。すべてのお客様がこれらの低コストランナーを利用できるようになりました。これらのランナーは、自動化タスク、issue 操作、および一般的な重量級 CI/CD ビルド以外の短時間実行ジョブ向けに最適化されています。

## Detailed Explanation
### Overview
- GitHub Actions の 1 vCPU Linux ランナーが一般提供されるようになりました。すべてのお客様がこれらの低コストランナーを利用できるようになりました。これらのランナーは、自動化タスク、issue 操作、および一般的な重量級 CI/CD ビルド以外の短時間実行ジョブ向けに最適化されています。

### Runner details
- これらのランナーは 1 vCPU と 5 GB RAM を備えています。これらのランナーを使用すると、Actions ワークフローは専用 VM インスタンスではなくコンテナ内で実行され、GitHub 全体での自動化タスクのコスト効率の高いパフォーマンスの高い実行が可能になります。各コンテナはハイパーバイザーレベル 2 の分離を提供し、ジョブが完了すると自動的に廃止されます。
- このランナータイプを使用するジョブは、実行時間が 15 分に制限されています。この制限を超えるジョブは終了して失敗します。
- これらのランナーの適切な使用例には、次のようなジョブが含まれます:
- issue の自動ラベル付け
- 基本的な言語コンパイル (例: webpack ビルド)
- リンティングとフォーマット
- 外部ツールへの API 呼び出し
- シンプルな python スクリプトの実行

### Get started today
- 開始するには、新規または既存のジョブ定義で新しいランナータイプ `ubuntu-slim` をターゲットにするだけです。

### Helpful resources
- インストールされているソフトウェアの完全なリストを表示したり、1 vCPU Linux ランナーを使用する際に問題を報告したりするには、runner-images リポジトリにアクセスしてください。
- これらの軽量ランナーの価格情報については、GitHub Actions の課金ページを参照してください。
- 追加のドキュメントについては、シングル CPU ランナーの GitHub Docs リファレンスを参照してください。

## Impact / Who's Affected
- GitHub Actions の 1 vCPU Linux ランナーが一般提供されるようになりました。
- このランナータイプを使用するジョブは、実行時間が 15 分に制限されています。

## Caveats / Limitations
- このランナータイプを使用するジョブは、実行時間が 15 分に制限されています。

## Article Content (cleaned)
GitHub Actions の 1 vCPU Linux ランナーが一般提供されるようになりました。すべてのお客様がこれらの低コストランナーを利用できるようになりました。これらのランナーは、自動化タスク、issue 操作、および一般的な重量級 CI/CD ビルド以外の短時間実行ジョブ向けに最適化されています。


## [Runner details](#runner-details)


これらのランナーは 1 vCPU と 5 GB RAM を備えています。これらのランナーを使用すると、Actions ワークフローは専用 VM インスタンスではなくコンテナ内で実行され、GitHub 全体での自動化タスクのコスト効率の高いパフォーマンスの高い実行が可能になります。各コンテナはハイパーバイザーレベル 2 の分離を提供し、ジョブが完了すると自動的に廃止されます。


このランナータイプを使用するジョブは、実行時間が 15 分に制限されています。この制限を超えるジョブは終了して失敗します。


これらのランナーの適切な使用例には、次のようなジョブが含まれます:


* issue の自動ラベル付け
* 基本的な言語コンパイル (例: webpack ビルド)
* リンティングとフォーマット
* 外部ツールへの API 呼び出し
* シンプルな python スクリプトの実行


## [Get started today](#get-started-today)


開始するには、新規または既存のジョブ定義で新しいランナータイプ `ubuntu-slim` をターゲットにするだけです。


## [Helpful resources](#helpful-resources)


インストールされているソフトウェアの完全なリストを表示したり、1 vCPU Linux ランナーを使用する際に問題を報告したりするには、[runner-images リポジトリ](https://github.com/actions/runner-images/blob/main/images/ubuntu-slim/ubuntu-slim-Readme.md) にアクセスしてください。


これらの軽量ランナーの価格情報については、[GitHub Actions の課金](https://docs.github.com/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions) ページを参照してください。


追加のドキュメントについては、[シングル CPU ランナーの GitHub Docs リファレンス](https://docs.github.com/actions/reference/runners/github-hosted-runners#single-cpu-runners) を参照してください。
