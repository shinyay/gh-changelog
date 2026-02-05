---
title: "2025年11月（バージョン 1.107）"
lang: "ja"
date: "2025-12-10"
version_ref: "v1_107"
download_version: "1.107.1"
source_url: "https://code.visualstudio.com/updates/v1_107"
source_markdown_url: "https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_107.md"
fetched_at: "2026-02-05T08:27:33.964571Z"
---

# 2025年11月（バージョン 1.107）

## Overview
_リリース日: 2025-12-10_

このリリースは“複数エージェントの同時運用”を前提に、セッション管理と委譲（Continue in）、背景エージェントの分離（Git worktree）と文脈添付の充実を進めています。1 つの会話で完結させるよりも、複数の作業者（ローカル/背景/クラウド）を切り替える運用が強調されています。

- Chat ビュー内にセッション一覧を統合し、状態/進捗/変更ファイルなどを把握しやすく。
- ローカルエージェントは UI を閉じても処理継続できるように。
- Continue in により、ローカル→背景/クラウドへの引き継ぎを支援。
- 背景エージェントを Git worktree で分離して衝突を減らす選択肢。
- 問題（Problems）、シンボル、コミットなどの“リッチな添付”で指示を具体化。

## Source Content (normalized)
このセクションは、上流のリリースノート（英語）の内容を、見出し構造を維持したまま日本語で要点整理したものです。厳密な原文は次を参照してください。

- source_url: https://code.visualstudio.com/updates/v1_107
- source_markdown_url: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_107.md

## Agents
複数セッション/複数プロバイダーの運用を前提に、管理・委譲・分離・添付の仕組みが強化されています。

- Chat ビューにセッション管理を統合し、一覧から切り替え/状態確認が可能に。
- 背景エージェントで worktree 分離を行い、変更衝突を軽減。
- さまざまな添付（問題、検索結果、コミットなど）で、背景エージェントに渡す入力の質を向上。

## Chat
チャット/セッション UI の統合や運用改善点がまとめられています（詳細は上流リリースノート参照）。

## MCP
MCP 連携に関する更新点がまとめられています（詳細は上流リリースノート参照）。

## Accessibility
アクセシビリティに関する変更点がまとめられています（詳細は上流リリースノート参照）。

## Editor Experience
エディター体験の改善点がまとめられています（詳細は上流リリースノート参照）。

## Code Editing
コード編集機能の改善点がまとめられています（詳細は上流リリースノート参照）。

## Source Control
ソース管理（Git）関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Debugging
デバッグ関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Terminal
ターミナル関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Authentication
認証関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Languages
言語別サポートの変更点がまとめられています（詳細は上流リリースノート参照）。

## Remote Development
リモート開発関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Enterprise
組織/エンタープライズ向けの設定・統制に関する更新点がまとめられています（詳細は上流リリースノート参照）。

## Contributions to extensions
拡張機能へのコントリビューション観点の更新点がまとめられています（詳細は上流リリースノート参照）。

## Proposed APIs
提案中（安定化前）の API 変更点が列挙されています（利用時は互換性に注意）。

## Engineering
内部実装/基盤周りの変更点がまとめられています（詳細は上流リリースノート参照）。

## Notable fixes
既知不具合の主要な修正点が列挙されています。

## Thank you
この節はコミュニティへの謝辞です（貢献者一覧などは原文参照）。
