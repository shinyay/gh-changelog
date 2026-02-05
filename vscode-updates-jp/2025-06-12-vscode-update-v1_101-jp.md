---
title: "2025年5月（バージョン 1.101）"
lang: "ja"
date: "2025-06-12"
version_ref: "v1_101"
download_version: "1.101.2"
source_url: "https://code.visualstudio.com/updates/v1_101"
source_markdown_url: "https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_101.md"
fetched_at: "2026-02-05T09:12:58.153615Z"
---

# 2025年5月（バージョン 1.101）

## Overview
_リリース日: 2025-06-12_

このリリースは、MCP の機能拡張（プロンプト/リソース/認証/開発モードなど）と、チャットのツール運用（ツールセット）に重点を置きつつ、入力体験や拡張機能周りの安全性も強化しています。

- MCP: prompts/resources/sampling（試験的）/認証/開発モードなど、統合の“厚み”が増加。
- チャット: ツールを束ねる「tool sets」を導入し、道具選択の複雑さを軽減。
- チャット UI とコンテキスト扱い（現在ファイルなど）の改善、タスク診断情報の活用など、信頼性/説明可能性を向上。
- エディター: EditContext が Stable で既定有効化（IME 等の入力体験改善を意図）。
- 拡張機能: MCP 関連 API、VSCE のパッケージング時 secret scanning など。

## Source Content (normalized)
このセクションは、上流のリリースノート（英語）の内容を、見出し構造を維持したまま日本語で要点整理したものです。厳密な原文は次を参照してください。

- source_url: https://code.visualstudio.com/updates/v1_101
- source_markdown_url: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_101.md

## Chat
MCP の統合機能拡張と、ツール運用の UX 強化が目立ちます。

- MCP プロンプト: サーバー定義プロンプトをスラッシュコマンドとして利用できるように。
- MCP リソース: 添付や保存など、リソースをチャット文脈として扱う仕組みが追加。
- MCP sampling（試験的）: サーバー側がモデル応答を要求する流れ（ユーザー確認・ログなど）に対応。
- MCP 認証: 仕様に基づく認証フローに対応し、信頼済みサーバー管理などの UI が追加。
- MCP 開発モード: 監視・再起動・デバッグ接続など、ローカル開発支援を整備。
- tool sets: 複数ツールをまとめて 1 つの参照対象として扱い、エージェント運用を整理しやすく。

## Accessibility
アクセシビリティに関する変更点がまとめられています（詳細は上流リリースノート参照）。

## Editor Experience
入力や検索体験など、細部の品質改善が中心です。

- EditContext API が Stable で既定有効化（入力/IME 周りの改善を意図）。
- 設定検索の改善（プレビュー機能を含む）や、検索候補生成の性能改善など。

## Code Editing
コード編集機能の改善点がまとめられています（詳細は上流リリースノート参照）。

## Notebooks
ノートブック関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Source Control
ソース管理（Git）関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Tasks
タスク実行や診断情報の扱いなど、関連する改善点がまとめられています（詳細は上流リリースノート参照）。

## Terminal
ターミナル関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Remote Development
リモート開発関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Contributions to extensions
拡張機能へのコントリビューション観点の更新点がまとめられています（詳細は上流リリースノート参照）。

## Extension Authoring
拡張機能開発者向けの更新・注意点です。

- 拡張機能から MCP サーバー群を公開/管理するための API が追加。
- VSCE がパッケージング時に secret scanning を行い、潜在的な秘密情報を検出した場合に失敗できるように。
- Node.js v22 由来の互換性リスク（navigator グローバル等）について注意喚起があり、設定による回避策が示されています。

## Proposed APIs
提案中（安定化前）の API 変更点が列挙されています（利用時は互換性に注意）。

## Engineering
内部実装/基盤周りの変更点がまとめられています（詳細は上流リリースノート参照）。

## Notable fixes
既知不具合の主要な修正点が列挙されています。

## Thank you
この節はコミュニティへの謝辞です（貢献者一覧などは原文参照）。
