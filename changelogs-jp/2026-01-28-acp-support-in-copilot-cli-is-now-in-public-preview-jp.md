---
title: "Copilot CLIでのACPサポートがパブリックプレビューに"
date: "2026-01-28"
type: "Improvement"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-28-acp-support-in-copilot-cli-is-now-in-public-preview"
fetched_at: "2026-02-03T14:50:49.360303Z"
lang: "ja"
---

# Copilot CLIでのACPサポートがパブリックプレビューに

## Overview
GitHub Copilot CLIがAgent Client Protocol（ACP）を実装しました。これは、AIエージェントとクライアント間の通信のための業界標準プロトコルです。これにより、サードパーティツール、IDE、自動化システムが拡張可能なインターフェースを通じてCopilotのエージェント機能と直接統合できるようになります。

## Detailed Explanation
### 概要
- GitHub Copilot CLIがAgent Client Protocol（ACP）を実装しました。これは、AIエージェントとクライアント間の通信のための業界標準プロトコルです。これにより、サードパーティツール、IDE、自動化システムが拡張可能なインターフェースを通じてCopilotのエージェント機能と直接統合できるようになります。

### 仕組み
- stdio経由でACPモードでCopilotを開始できます：copilot --acp
- または特定のポートでTCP経由で接続します：copilot --acp --port 8080
- ACPクライアントは次のことができます：
- 接続を初期化し、エージェントの機能を発見する。
- カスタム作業ディレクトリで分離されたセッションを作成する。
- テキスト、画像、コンテキストリソースを含むプロンプトを送信する。
- エージェントが作業する際のストリーミング更新を受信する。
- ツール実行の許可リクエストに応答する。
- 操作をキャンセルし、セッションライフサイクルを管理する。

### ユースケース
- IDE統合：任意のエディターまたは開発環境にCopilotサポートを構築する。
- CI/CDパイプライン：自動化されたワークフローでエージェントコーディングタスクを調整する。
- カスタムフロントエンド：特定の開発者ワークフロー用に特化したインターフェースを作成する。
- マルチエージェントシステム：標準プロトコルを使用してCopilotを他のAIエージェントと調整する。
- ACPドキュメントで詳細を確認し、GitHubコミュニティ内のディスカッションに参加してください。

## Insights (derived from article language)
- ACPドキュメントで詳細を確認し、GitHubコミュニティ内のディスカッションに参加してください。

## Article Content (cleaned)
GitHub Copilot CLIが[Agent Client Protocol（ACP）](https://zed.dev/acp)を実装しました。これは、AIエージェントとクライアント間の通信のための業界\-標準プロトコルです。これにより、サードパーティツール、IDE、自動化システムが拡張可能なインターフェースを通じてCopilotのエージェント機能と直接統合できるようになります。


## [How it works](https://github.blog/changelog/feed/#how-it-works)


stdio経由でACPモードでCopilotを開始できます：`copilot --acp`


または特定のポートでTCP経由で接続します：`copilot --acp --port 8080`


ACPクライアントは次のことができます：


* 接続を初期化し、エージェントの機能を発見する。
* カスタム作業ディレクトリで分離されたセッションを作成する。
* テキスト、画像、コンテキストリソースを含むプロンプトを送信する。
* エージェントが作業する際のストリーミング更新を受信する。
* ツール実行の許可リクエストに応答する。
* 操作をキャンセルし、セッションライフサイクルを管理する。


## [Use cases](https://github.blog/changelog/feed/#use-cases)


* IDE統合：任意のエディターまたは開発環境にCopilotサポートを構築する。
* CI/CDパイプライン：自動化されたワークフローでエージェントコーディングタスクを調整する。
* カスタムフロントエンド：特定の開発者ワークフロー用に特化したインターフェースを作成する。
* マルチ\-エージェントシステム：標準プロトコルを使用してCopilotを他のAIエージェントと調整する。


[ACPドキュメント](https://docs.github.com/copilot/reference/acp-server)で詳細を確認し、[GitHubコミュニティ](https://github.com/orgs/community/discussions/185860)内のディスカッションに参加してください。
