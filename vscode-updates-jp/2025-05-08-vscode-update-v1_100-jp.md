---
title: "2025年4月（バージョン 1.100）"
lang: "ja"
date: "2025-05-08"
version_ref: "v1_100"
download_version: "1.100.3"
source_url: "https://code.visualstudio.com/updates/v1_100"
source_markdown_url: "https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_100.md"
fetched_at: "2026-02-05T09:12:57.732195Z"
---

# 2025年4月（バージョン 1.100）

## Overview
_リリース日: 2025-05-08_

このリリースは、Copilot Chat の「再利用可能でチーム共有しやすいカスタマイズ」に軸足を置きつつ、エージェント編集の体感速度改善や MCP 対応の拡張を進めています。

- Markdown ベースの「instructions ファイル」と「prompt ファイル」を導入し、ガイドラインや定型依頼をファイルとして運用可能に。
- エージェントモードの編集が高速化（モデルに応じた差分適用方式の改善）。
- チャットから外部リソースを扱う道具立てを拡充（GitHub リポジトリ検索、拡張機能検索、Web ページ取得）。
- MCP は Streamable HTTP などの輸送方式や、画像出力を含むツール I/O 体験を改善。
- Linux では拡張機能の署名検証が必須化（ARM32 は例外あり）。

## Source Content (normalized)
このセクションは、上流のリリースノート（英語）の内容を、見出し構造を維持したまま日本語で要点整理したものです。厳密な原文は次を参照してください。

- source_url: https://code.visualstudio.com/updates/v1_100
- source_markdown_url: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_100.md

## Chat
チャットのカスタマイズと再利用性が大きく前進しています。

- instructions ファイル（ルール/ガイドライン）と prompt ファイル（定型依頼）の導入で、個人だけでなくチームでも運用しやすい形に。
- #githubRepo（任意の GitHub リポジトリを対象にコード断片検索）や #extensions（Marketplace 検索/導入）など、会話からの「探索→行動」をつなぐ仕組みが追加。
- #fetch（Web ページ取得）がページ全体の Markdown 化を含む形に強化され、文脈として扱いやすく。
- MCP（Model Context Protocol）については、Streamable HTTP と画像出力など、統合体験が拡充。

## Accessibility
アクセシビリティに関する変更点がまとめられています（詳細は上流リリースノート参照）。

## Editor Experience
作業の“ながら見”を助ける UI 改善が中心です。

- チャットやエディターのフローティングウィンドウ運用（コンパクト/常に手前など）を強化。
- ステージ済み差分の視認性向上（クイック diff 装飾）。

## Code Editing
エージェント編集の速度・信頼性改善を含む、コード編集周りの更新点がまとめられています。

## Notebooks
ノートブック関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Source Control
ソース管理（Git）周りの変更点がまとめられています（詳細は上流リリースノート参照）。

## Debugging
デバッグ関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Languages
言語別サポートの変更点がまとめられています（詳細は上流リリースノート参照）。

## Remote Development
リモート開発関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Contributions to extensions
拡張機能へのコントリビューション観点の更新点がまとめられています（詳細は上流リリースノート参照）。

## Extension Authoring
拡張機能の開発・配布・安全性に関する更新です。

- Linux で拡張機能の署名検証が必須化（ARM32 は例外とされる旨が記載）。

## Proposed APIs
提案中（安定化前）の API 変更点が列挙されています（利用時は互換性に注意）。

## Notable fixes
既知不具合の主要な修正点が列挙されています。

## Thank you
この節はコミュニティへの謝辞です（貢献者一覧などは原文参照）。
