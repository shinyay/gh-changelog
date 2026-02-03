---
title: "GitHub Copilot CLI：カスタムエージェントの使用と Copilot コーディングエージェントへの委任"
date: "2025-10-28"
type: "improvements"
labels: ["client apps", "copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-github-copilot-cli-use-custom-agents-and-delegate-to-copilot-coding-agent"
fetched_at: "2026-02-03T14:50:55.673183Z"
lang: "ja"
---

# GitHub Copilot CLI：カスタムエージェントの使用と Copilot コーディングエージェントへの委任

## Overview
初期パブリックプレビューリリース以降、GitHub Copilot CLI に日々改善を加えてきました。パブリックリポジトリでの皆様からのフィードバックに耳を傾けることに加えて、Copilot CLI をより拡張可能にし、より広範な GitHub Copilot エコシステムに接続するいくつかの大きな機能に取り組んできました。

## Detailed Explanation
### 概要
- 初期パブリックプレビューリリース以降、GitHub Copilot CLI に日々改善を加えてきました。パブリックリポジトリでの皆様からのフィードバックに耳を傾けることに加えて、Copilot CLI をより拡張可能にし、より広範な GitHub Copilot エコシステムに接続するいくつかの大きな機能に取り組んできました。

### カスタムエージェントが GitHub Copilot CLI で利用可能に
- カスタムエージェントが GitHub Copilot で利用可能になり、チームのワークフロー、規約、独自のニーズを捉えたエージェントペルソナを定義できます。これらのエージェントは、プロンプト、ツールの選択、Model Context Protocol (MCP) サーバーを使ってさらにカスタマイズでき、特定のユースケースに最適化できます。
- リポジトリの .github/agents または {org}/.github リポジトリでエージェントを定義することに加えて、GitHub Copilot CLI は ~/.copilot/agents のカスタムエージェント設定を認識します。
- /agent スラッシュコマンドでエージェントを明示的に対話的に呼び出すことができます。カスタムエージェントは Copilot のツールとしても利用可能になり、必要に応じてモデルが関連するカスタムエージェントを使用して新しいエージェントループを開始します。

### GitHub Copilot CLI から Copilot コーディングエージェントにタスクを委任
- Copilot コーディングエージェントは、非同期で自律的なバックグラウンドエージェントです。GitHub Copilot CLI から /delegate TASK-DESCRIPTION スラッシュコマンドを実行すると、ステージされていない変更が新しいブランチにコミットされます。その後、Copilot コーディングエージェントがドラフトプルリクエストを開き、バックグラウンドで変更を加え、レビューをリクエストします。Copilot は、このプロセスが始まるとターミナルでプルリクエストとコーディングエージェントのセッションへのリンクを提供します。

### ストリーミング、並列ツール呼び出し、パフォーマンス向上
- Copilot の出力がトークンごとにターミナルにストリーミングされ、よりスナップ感のあるフィードバックを提供します。
- Copilot は複数のツール呼び出しを並列実行でき、より複雑なタスクの完了時間を短縮します。
- GitHub Copilot CLI の継続的なパフォーマンス改善を行い、アプリケーションのメモリフットプリントの削減と画面のちらつきバグの修正を含みます。

### フィードバックの共有
- ターミナルで npm install -g @github/copilot@latest を実行して GitHub Copilot CLI を更新してください。/feedback コマンドやパブリックリポジトリへの issue のオープンを通じてフィードバックを提出してくださった皆様に感謝します。継続的なフィードバックは、日々改善を続ける上で非常に貴重です。

## Key Changes
記事では明示されていません。

## Impact / Who's Affected
- 初期パブリックプレビューリリース以降、GitHub Copilot CLI に日々改善を加えてきました。
- カスタムエージェントが GitHub Copilot CLI で利用可能に カスタムエージェントが GitHub Copilot で利用可能になり、チームのワークフロー、規約、独自のニーズを捉えたエージェントペルソナを定義できます。

## Caveats / Limitations
記事では明示されていません。

## Insights (derived from article language)
記事では明示されていません。

## Article Content (cleaned)
初期パブリックプレビューリリース以降、GitHub Copilot CLI に [日々改善](https://github.com/github/copilot-cli/releases?utm_source=changelog-copilot-cli&utm_medium=changelog&utm_campaign=universe25) を加えてきました。パブリックリポジトリでの皆様からのフィードバックに耳を傾けることに加えて、Copilot CLI をより拡張可能にし、より広範な GitHub Copilot エコシステムに接続するいくつかの大きな機能に取り組んできました。


## [カスタムエージェントが GitHub Copilot CLI で利用可能に](#custom-agents-are-available-in-github-copilot-cli)


[カスタムエージェントが GitHub Copilot で利用可能になり](https://github.blog/changelog/2025-11-27-custom-agents-for-github-copilot/)、チームのワークフロー、規約、独自のニーズを捉えたエージェントペルソナを定義できます。これらのエージェントは、プロンプト、ツールの選択、Model Context Protocol (MCP) サーバーを使ってさらにカスタマイズでき、特定のユースケースに最適化できます。


リポジトリの `.github/agents` または `{org}/.github` リポジトリでエージェントを定義することに加えて、GitHub Copilot CLI は `~/.copilot/agents` のカスタムエージェント設定を認識します。


`/agent` スラッシュコマンドでエージェントを明示的に対話的に呼び出すことができます。カスタムエージェントは Copilot のツールとしても利用可能になり、必要に応じてモデルが関連するカスタムエージェントを使用して新しいエージェントループを開始します。


## [GitHub Copilot CLI から Copilot コーディングエージェントにタスクを委任](#delegate-tasks-to-copilot-coding-agent-from-github-copilot-cli)


[Copilot コーディングエージェント](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent?utm_source=changelog-docs-copilot-cli&utm_medium=changelog&utm_campaign=universe25) は、非同期で自律的なバックグラウンドエージェントです。GitHub Copilot CLI から `/delegate TASK-DESCRIPTION` スラッシュコマンドを実行すると、ステージされていない変更が新しいブランチにコミットされます。その後、Copilot コーディングエージェントがドラフトプルリクエストを開き、バックグラウンドで変更を加え、レビューをリクエストします。Copilot は、このプロセスが始まるとターミナルでプルリクエストとコーディングエージェントのセッションへのリンクを提供します。


## [ストリーミング、並列ツール呼び出し、パフォーマンス向上](#streaming-parallel-tool-calling-improved-performance)


* Copilot の出力がトークンごとにターミナルにストリーミングされ、よりスナップ感のあるフィードバックを提供します。
* Copilot は複数のツール呼び出しを並列実行でき、より複雑なタスクの完了時間を短縮します。
* GitHub Copilot CLI の継続的なパフォーマンス改善を行い、アプリケーションのメモリフットプリントの削減と画面のちらつきバグの修正を含みます。


## [フィードバックの共有](#share-your-feedback)


ターミナルで `npm install -g @github/copilot@latest` を実行して GitHub Copilot CLI を更新してください。`/feedback` コマンドや [パブリックリポジトリ](https://github.com/github/copilot-cli?utm_source=changelog-copilot-cli&utm_medium=changelog&utm_campaign=universe25) への issue のオープンを通じてフィードバックを提出してくださった皆様に感謝します。継続的なフィードバックは、日々改善を続ける上で非常に貴重です。
