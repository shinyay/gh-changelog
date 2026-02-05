---
title: "2025年6月（バージョン 1.102）"
lang: "ja"
date: "2025-07-09"
version_ref: "v1_102"
download_version: "1.102.3"
source_url: "https://code.visualstudio.com/updates/v1_102"
source_markdown_url: "https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_102.md"
fetched_at: "2026-02-05T09:12:58.432746Z"
---

# 2025年6月（バージョン 1.102）

## Overview
_リリース日: 2025-07-09_

このリリースは、Copilot Chat のオープンソース化と MCP の一般提供（GA）を大きな節目として、MCP サーバーの発見/導入/管理 UX や、モード/プロンプト/指示ファイルの運用改善を進めています。

- Copilot Chat 拡張機能が MIT ライセンスで公開され、透明性とコミュニティ参加が強化。
- MCP が GA となり、サーバーの発見/インストール/管理がより“製品機能”として整備。
- MCP 設定はプロファイル単位の `mcp.json` として扱われ、同期/移行にも対応。
- チャットのデバッグ/検査機能が強化（ただしログに個人情報が含まれうる点に注意）。
- ターミナル自動承認（allow/deny ルール）は試験的機能として提供。

## Source Content (normalized)
このセクションは、上流のリリースノート（英語）の内容を、見出し構造を維持したまま日本語で要点整理したものです。厳密な原文は次を参照してください。

- source_url: https://code.visualstudio.com/updates/v1_102
- source_markdown_url: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_102.md

## Chat
カスタマイズ資産（モード/プロンプト/指示ファイル）を“書いて管理する”運用を後押ししています。

- モード定義などのメタデータ編集支援（補完/検証/ホバー）が強化。
- 条件に応じて指示ファイルを必要時に読み込む仕組みが追加され、大規模なルールセットを扱いやすく。
- 依頼/ツール呼び出しの詳細を検査できるデバッグビューが追加（共有時の情報漏えいに注意）。

## MCP
MCP が GA となり、導入/運用の UX が拡充されています。

- サーバーの発見/インストール（キュレーション/UX 入口）と、管理ビュー（開始/停止/ログ/設定など）を提供。
- MCP サーバー設定をユーザー設定から分離し、プロファイル単位の `mcp.json` に移行。
- 仕様に基づく elicitations（サーバーからの入力要求）など、エコシステム対応も進行。

## Accessibility
アクセシビリティに関する変更点がまとめられています（詳細は上流リリースノート参照）。

## Code Editing
コード編集機能の改善点がまとめられています（詳細は上流リリースノート参照）。

## Editor Experience
エディター体験の改善点がまとめられています（詳細は上流リリースノート参照）。

## Tasks
タスク実行に関する変更点がまとめられています（詳細は上流リリースノート参照）。

## Terminal
ターミナル自動承認（試験的）など、ターミナル関連の改善点がまとめられています（詳細は上流リリースノート参照）。

## Contributions to extensions
拡張機能へのコントリビューション観点の更新点がまとめられています（詳細は上流リリースノート参照）。

## Extension Authoring
拡張機能開発者向けの更新点がまとめられています（詳細は上流リリースノート参照）。

## Proposed APIs
提案中（安定化前）の API 変更点が列挙されています（利用時は互換性に注意）。

## Engineering
内部実装/基盤周りの変更点がまとめられています（詳細は上流リリースノート参照）。

## Notable fixes
既知不具合の主要な修正点が列挙されています。

## Thank you
この節はコミュニティへの謝辞です（貢献者一覧などは原文参照）。
