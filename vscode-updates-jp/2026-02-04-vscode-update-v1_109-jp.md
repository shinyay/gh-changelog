---
title: "2026年1月（バージョン 1.109）"
lang: "ja"
date: "2026-02-04"
version_ref: "v1_109"
download_version: "1.109.0"
source_url: "https://code.visualstudio.com/updates/v1_109"
source_markdown_url: "https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_109.md"
fetched_at: "2026-02-05T08:27:34.521564Z"
---

# 2026年1月（バージョン 1.109）

## Overview
_リリース日: 2026-02-04_

このリリースは、エージェントを“機能”ではなく“運用体験”として整備する方向性がさらに進みます。セッション管理・委譲・カスタマイズ（Skills/指示）・信頼/安全（ターミナル制約）といった、組織的利用を前提にしたコントロール面が目立ちます。

- チャット: 思考表示の見せ方や、ツール失敗時の自動展開など、デバッグ/追跡性を改善。
- セッション: ステータス表示や切り替え/一括操作など、管理 UX を強化。
- `/init`: リポジトリの慣習に沿ったワークスペース指示を生成/更新する導線。
- Agent Skills: 一般提供・既定有効化として扱われ、スキル作成/設定の体験も整備。
- 組織指示: 組織単位の指示と、その読み込み診断が追加。
- MCP Apps: チャット応答内でのインタラクティブ UI 表示をサポート。
- ターミナル: サンドボックス（実験的）など、実行権限/アクセスを制限する方向へ。
- ワークベンチ: 統合ブラウザー（プレビュー）を導入。
- 既存 Copilot 拡張は非推奨となり、Copilot Chat へ収束する旨の記載。

## Source Content (normalized)
このセクションは、上流のリリースノート（英語）の内容を、見出し構造を維持したまま日本語で要点整理したものです。厳密な原文は次を参照してください。

- source_url: https://code.visualstudio.com/updates/v1_109
- source_markdown_url: https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_109.md

## Upcoming events
今後のイベント/告知がまとめられています（詳細は上流リリースノート参照）。

## Chat UX
チャットの可観測性（思考表示、ツール失敗の展開など）と、追跡しやすい UI の改善が含まれます。

## Agent Session Management
セッションの開始/切り替え、状態表示、一括操作など、日常運用の管理 UX が強化されています。

## Agent Customization
`/init` による指示生成、Skills の一般提供・既定有効化、組織指示や診断情報など、標準化/統制のための仕組みが整備されています。

## Agent Extensibility
MCP Apps など、チャットを拡張してよりインタラクティブな体験を提供する機構が追加されています。

## Agent Optimizations
エージェント運用の改善（性能/体験/ツール連携など）がまとめられています（詳細は上流リリースノート参照）。

## Agent Security and Trust
ターミナル実行の制約（サンドボックス等の実験的機能）や、信頼/安全に関する強化点がまとめられています。

## Terminal enhancements
背景実行の制御や待機/停止など、ターミナル運用の改善点がまとめられています（詳細は上流リリースノート参照）。

## Coding and editor
コーディング体験/エディター周りの改善点がまとめられています（詳細は上流リリースノート参照）。

## Workbench and productivity
統合ブラウザー（プレビュー）など、ワークベンチ/生産性機能の更新点がまとめられています。

## Extensions and API
拡張機能/ API 周りの更新点がまとめられています（詳細は上流リリースノート参照）。

## Engineering
内部実装/基盤周りの変更点がまとめられています（詳細は上流リリースノート参照）。

## Notable fixes
既知不具合の主要な修正点が列挙されています。

## Thank you
この節はコミュニティへの謝辞です（貢献者一覧などは原文参照）。
