---
title: "Copilot coding agent がセルフホストランナーに対応"
date: "2025-10-28"
type: "improvements"
labels: ["actions", "copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-copilot-coding-agent-now-supports-self-hosted-runners"
fetched_at: "2026-02-03T14:50:55.592276Z"
lang: "ja"
---

# Copilot coding agent がセルフホストランナーに対応

## Overview
Actions Runner Controller (ARC) によって管理されるセルフホスト GitHub Actions ランナーを使用して、Copilot coding agent の開発環境を自社のインフラストラクチャで実行できるようになりました。これにより、パブリックインターネットで利用できない内部リソース（パッケージなど）へのアクセスを Copilot に提供できます。

## Detailed Explanation
### 概要
- Actions Runner Controller (ARC) によって管理されるセルフホスト GitHub Actions ランナーを使用して、Copilot coding agent の開発環境を自社のインフラストラクチャで実行できるようになりました。これにより、パブリックインターネットで利用できない内部リソース（パッケージなど）へのアクセスを Copilot に提供できます。
- Copilot coding agent は非同期で自律的なバックグラウンドエージェントです。タスクを Copilot に委任すると、ドラフトのプルリクエストを開き、バックグラウンドで変更を加え、レビューを要求します。Copilot は GitHub Actions によって提供される独自の一時的な開発環境で動作し、リポジトリのビルドプロセスや自動テストなどを実行できます。
- ARC スケールセットは、coding agent の開発環境をカスタマイズする際に、`copilot-setup-steps.yml` 設定ファイルの `runs-on:` ターゲットとしてサポートされています。開始するには：
- ARC をデプロイし、スケールセットを設定します。
- `copilot-setup-steps.yml` の `runs-on:` ターゲットをスケールセットに更新します。
- 詳細については、GitHub Copilot coding agent の開発環境のカスタマイズに関するドキュメントを参照してください。

## Article Content (cleaned)
Actions Runner Controller (ARC) によって管理されるセルフホスト GitHub Actions ランナーを使用して、Copilot coding agent の開発環境を自社のインフラストラクチャで実行できるようになりました。これにより、パブリックインターネットで利用できない内部リソース（パッケージなど）へのアクセスを Copilot に提供できます。


[Copilot coding agent](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent?utm_source=changelog-docs-cca-selfhosted-runners&utm_medium=changelog&utm_campaign=universe25) は非同期で自律的なバックグラウンドエージェントです。タスクを Copilot に委任すると、ドラフトのプルリクエストを開き、バックグラウンドで変更を加え、レビューを要求します。Copilot は GitHub Actions によって提供される独自の一時的な開発環境で動作し、リポジトリのビルドプロセスや自動テストなどを実行できます。


ARC スケールセットは、coding agent の開発環境をカスタマイズする際に、`copilot-setup-steps.yml` 設定ファイルの `runs-on:` ターゲットとしてサポートされています。開始するには：


1. [ARC をデプロイ](https://docs.github.com/actions/tutorials/use-actions-runner-controller/quickstart?utm_source=changelog-docs-cca-selfhosted-runners&utm_medium=changelog&utm_campaign=universe25)し、スケールセットを設定します。
2. `copilot-setup-steps.yml` の `runs-on:` ターゲットをスケールセットに更新します。



```
jobs:
  copilot-setup-steps:
    runs-on: arc-scale-set-name

```

詳細については、[GitHub Copilot coding agent の開発環境のカスタマイズに関するドキュメント](https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment?utm_source=changelog-docs-cca-selfhosted-runners&utm_medium=changelog&utm_campaign=universe25)を参照してください。
