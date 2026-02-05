---
title: "2025年10月（バージョン 1.106）"
lang: "ja"
date: "2025-11-12"
version_ref: "v1_106"
download_version: "1.106.3"
source_url: "https://code.visualstudio.com/updates/v1_106"
source_markdown_url: "https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_106.md"
fetched_at: "2026-02-05T08:27:33.653776Z"
---

# 2025年10月（バージョン 1.106）

## Overview
_リリース日: 2025-11-12_

このリリースは「Agent HQ」的な運用（セッション管理・計画・委譲）を中核に据え、クラウド/CLI/複数プロバイダーの横断運用を意識した統合を進めています。同時に、AI 機能のオープンソース化/統合や、エディター周辺 UX の底上げも含まれます。

- Agent Sessions の標準有効化や、単一ビューでの統合表示など、セッション中心の運用を推進。
- Plan agent により、実装前に確認・計画を立てる流れを強化。
- Copilot CLI など、周辺からのセッション作成/再開/委譲の導線を整備。
- “chat modes” を “custom agents” として整理し、`.github/agents` に定義する方針を提示。
- インライン提案のオープンソース化（リポジトリ統合）や、拡張機能統合方針などの話題。

## Source Content (normalized)
このセクションは、上流のリリースノート（英語）の内容を、見出し構造を維持したまま日本語で要点整理したものです。厳密な原文は次を参照してください。

- source_url: https://code.visualstudio.com/updates/v1_106
- source_markdown_url: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_106.md

## Agents
エージェントの“司令塔”としての体験（セッション/計画/委譲）が強調されています。

- セッション一覧や検索など、運用の中心としての UI が整備。
- Plan agent が clarifying questions → 計画承認 → 実装の流れを支援。
- プロバイダー横断でのセッション統合や deep link など、外部との連携も改善。

## Code Editing
差分レビューや入力支援など、編集体験の改善が含まれます。

- 差分エディターで削除行の選択/コピーが可能に。
- インライン提案の整理（snooze など）や、関連する UI/挙動の改善。

## Editor Experience
アイコンや設定 UI、検索など、ワークベンチ全体の改善点がまとめられています（詳細は上流リリースノート参照）。

## Chat
チャット/エージェント機能の統合方針や、セッション中心運用への接続点がまとめられています（詳細は上流リリースノート参照）。

## MCP
MCP 連携に関する更新点がまとめられています（詳細は上流リリースノート参照）。

## Accessibility
アクセシビリティに関する変更点がまとめられています（詳細は上流リリースノート参照）。

## Notebooks
ノートブック関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Source Control
ソース管理（Git）関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Testing
テスト関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Terminal
ターミナル関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Authentication
認証関連の変更点がまとめられています（詳細は上流リリースノート参照）。

## Languages
言語別サポートの変更点がまとめられています（詳細は上流リリースノート参照）。

## Contributions to extensions
拡張機能へのコントリビューション観点の更新点がまとめられています（詳細は上流リリースノート参照）。

## Preview Features
プレビュー/実験的機能が列挙されています（有効化条件や制約は原文参照）。

## Extension Authoring
custom agents（旧 chat modes）の定義/メタデータや、エディターでの支援（検証/補完）など、拡張・運用に関する更新点がまとめられています（詳細は上流リリースノート参照）。

## Proposed APIs
提案中（安定化前）の API 変更点が列挙されています（利用時は互換性に注意）。

## Engineering
内部実装/基盤周りの変更点がまとめられています（詳細は上流リリースノート参照）。

## Notable fixes
既知不具合の主要な修正点が列挙されています。

## Thank you
この節はコミュニティへの謝辞です（貢献者一覧などは原文参照）。
