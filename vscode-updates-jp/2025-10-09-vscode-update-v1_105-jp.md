---
title: "2025年9月（バージョン 1.105）"
lang: "ja"
date: "2025-10-09"
version_ref: "v1_105"
download_version: "1.105.1"
source_url: "https://code.visualstudio.com/updates/v1_105"
source_markdown_url: "https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_105.md"
fetched_at: "2026-02-05T08:27:33.393874Z"
---

# 2025年9月（バージョン 1.105）

## Overview
_リリース日: 2025-10-09_

このリリースは「計画→実装」「委譲→分業」を前提に、エージェントワークフローの編成能力を引き上げています（多くは Insiders での提供）。ツール名の衝突回避や、ネストした `AGENTS.md` による指示の階層化など、チーム/組織での運用を意識した変更も含みます。

- Plan agent（Insiders）で、実装前にタスク分解と確認を行う流れを用意。
- handoffs（Insiders）で、モード/次の指示への誘導をメタデータで定義。
- subagents（Insiders）で、調査/分析を隔離コンテキストに委譲。
- Agent Sessions の統合範囲拡大（例: OpenAI Codex、Copilot CLI などの話題）。
- ツール名は fully qualified 名をサポートし、拡張/MCP/内蔵の衝突を回避。
- ネスト `AGENTS.md`（実験的）で、サブフォルダ単位の指示を適用可能に。

## Source Content (normalized)
このセクションは、上流のリリースノート（英語）の内容を、見出し構造を維持したまま日本語で要点整理したものです。厳密な原文は次を参照してください。

- source_url: https://code.visualstudio.com/updates/v1_105
- source_markdown_url: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_105.md

## VS Code at GitHub Universe
GitHub Universe での発表内容として、計画/委譲/分業を支える要素（Plan agent、handoffs、subagents、セッション統合など）が強調されています。

## Chat
チャット体験は「長い作業を回す」運用に寄せて改善されています。

- 返答到着の OS 通知など、待ち時間の体験改善。
- 実行中でも変更の keep/undo を扱いやすくするなど、エージェントループ中の摩擦低減。
- キーボード操作や履歴周りの改善も含む。

## MCP
MCP 連携に関する更新点がまとめられています（詳細は上流リリースノート参照）。

## Accessibility
アクセシビリティに関する変更点がまとめられています（詳細は上流リリースノート参照）。

## Editor Experience
エディター体験の改善点がまとめられています（詳細は上流リリースノート参照）。

## Source Control
ソース管理（Git）関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Testing
テスト関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Tasks
タスク関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Terminal
ターミナル関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Authentication
認証関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Languages
言語別サポートの変更点がまとめられています（詳細は上流リリースノート参照）。

## Contributions to extensions
拡張機能へのコントリビューション観点の更新点がまとめられています（詳細は上流リリースノート参照）。

## Extension Authoring
拡張機能/カスタムモード/プロンプト運用のスケールを意識した変更です。

- prompt/mode 定義などで fully qualified ツール名を使えるようになり、衝突回避が可能に。
- BYOK / OpenAI 互換のカスタムモデル向けに編集ツールの選択/最適化に関する仕組みが整理。

## Engineering
内部実装/基盤周りの変更点がまとめられています（詳細は上流リリースノート参照）。

## Notable fixes
既知不具合の主要な修正点が列挙されています。

## Thank you
この節はコミュニティへの謝辞です（貢献者一覧などは原文参照）。
