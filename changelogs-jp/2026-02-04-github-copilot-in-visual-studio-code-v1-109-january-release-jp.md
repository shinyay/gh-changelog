---
title: "Visual Studio Code 向け GitHub Copilot v1.109（2026年1月リリース）"
date: "2026-02-04"
type: "Release"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-02-04-github-copilot-in-visual-studio-code-v1-109-january-release"
fetched_at: "2026-02-05T04:46:41.050560Z"
lang: "ja"
---

# Visual Studio Code 向け GitHub Copilot v1.109（2026年1月リリース）

## Overview
2026年1月のリリースでは、Visual Studio Code 向け GitHub Copilot において、エージェント主導のワークフロー、エージェントセッション管理の改善、そして IDE 内での Anthropic Claude エージェント対応など、大きな改善が入ったと説明されています。

## Detailed Explanation
### 概要
- 本リリースは、エージェント主導のワークフロー、セッション管理の改善、Claude by Anthropic のエージェント対応（IDE 内）などの改善を含みます。

### Agent extensibility（モデル + 連携）
- Claude エージェント対応がパブリックプレビューとして追加され、Copilot サブスクリプション内の Claude モデルを使って、Anthropic の公式 Claude Agent SDK にタスクを委譲できるようになります。
- MCP アプリとの連携により、VS Code 内でよりツール駆動・対話的な Copilot 体験が可能になります。

### Copilot Chat & UX
- ストリーミングの応答性が改善され、チャット体験が高速・軽快になったとされています。
- 推論結果の品質向上により、より信頼できる回答とタスク実行が期待できると説明されています。
- thinking tokens や、エージェントが前提を置かず質問する挙動など、推論の可視化/理解を助ける要素が触れられています。
- エディタのインラインチャットが刷新され、コンテキスト内でのやりとりが自然で効果的になることが狙いです。

### マルチエージェント開発とセッション管理
- Copilot / Claude / Local agents / Background agents / Cloud agents など複数の種類にまたがる委譲と管理が改善されたとされています。
- 必要に応じて途中介入できるハンドオフ体験や、対応が必要なセッションを示すステータス表示、並列に動くサブエージェントが挙げられています。

### カスタマイズと最適化
- Agent orchestrations により、チームやプロジェクト向けの再利用可能なワークフローを構築できます。
- Agent Skills と組織全体のカスタマイズにより、環境をまたいだ一貫した結果を狙えるとされています。
- Copilot Memory は、関連する文脈を保持してエージェントがより賢く動けるようにするものとして紹介されています。
- 外部インデックスによる高速なコード検索が、巨大リポジトリでの応答性改善として言及されています。

### セキュリティと信頼
- ターミナルコマンドのサンドボックス化により、エージェントが提案/実行するコマンドへの信頼性を高める（実験的、macOS/Linux のみ）と説明されています。
- 自動承認ルール、タイムアウト/待機/停止などのターミナルライフサイクル改善も触れられています。

### 関連する VS Code の生産性アップデート
- 統合ブラウザー、ターミナル強化、コーディング/エディタ改善、拡張機能/API アップデートなども併せて紹介されています（Copilot そのものではない項目も含む）。

## Impact / Who’s Affected
- VS Code 内でエージェントを使う利用者は、モデル/連携の拡張やセッション管理改善の影響を受けます。
- macOS/Linux 利用者は、実験的機能としてターミナルコマンドサンドボックスの恩恵を受ける可能性があります。

## Caveats / Limitations
- ターミナルコマンドサンドボックスは実験的で、macOS/Linux のみと記載されています。

## Article Content (cleaned)
2026年1月のリリースでは、[Visual Studio Code](https://aka.ms/VSCode/109) 向け GitHub Copilot に大きな改善が追加されたと説明されています。具体的には、エージェント主導のワークフロー、エージェントセッション管理の改善、そして IDE 内での Anthropic Claude エージェント対応の導入が挙げられています。


### [Agent extensibility (models \+ integrations)](https://github.blog/changelog/feed/#agent-extensibility-models-integrations)


* Claude エージェント対応がパブリックプレビューとして追加され、Copilot サブスクリプション内の Claude モデルを使って、Anthropic の公式 Claude Agent SDK にタスクを委譲できるようになります。
* MCP アプリとの連携により、VS Code 内でよりツール駆動で対話的な Copilot 体験が可能になります。


### [Copilot Chat \& UX](https://github.blog/changelog/feed/#copilot-chat-ux)


* ストリーミングの応答性が改善され、チャット体験がより高速・軽快になります。
* 推論結果の品質向上により、より信頼できる回答やタスク実行が期待できると説明されています。
* thinking tokens や、前提を置かず質問するエージェントなどにより、推論の可視性が高まります。
* エディタのインラインチャットが刷新され、コーディング中の文脈内やりとりがより自然で効果的になることが狙いです。


### [Multiagent development \& session management](https://github.blog/changelog/feed/#multiagent-development-session-management)


* 次のような対象にまたがって作業を委譲しやすくなるよう、エージェントセッション管理が改善されたとされています:
	+ Copilot
	+ Claude
	+ Local agents
	+ Background agents
	+ Cloud agents
* 必要に応じて作業へ介入できる、シームレスなハンドオフ/介入体験が挙げられています。
* 対応が必要なセッションを示すステータス表示や、並列で動作するサブエージェントによる高速化が触れられています。


### [Copilot agent customization](https://github.blog/changelog/feed/#copilot-agent-customization)


* Agent orchestrations により、チームやプロジェクトに合わせた再利用可能なワークフローを構築できます。
* Agent Skills と組織全体のカスタマイズで、開発者や環境をまたいだ一貫性の高い成果を狙えると説明されています。


### [Agent optimizations (smarter \+ faster)](https://github.blog/changelog/feed/#agent-optimizations-smarter-faster)


* Copilot Memory は、関連する文脈を保持することでエージェントがより賢く動けるよう支援するものとして紹介されています。
* 外部インデックスによる高速なコード検索により、大規模リポジトリ開発時の取得速度と応答性が改善されます。


### [Agent security \& trust](https://github.blog/changelog/feed/#agent-security-trust)


* ターミナルコマンドのサンドボックス化により、エージェントがコマンドを提案/実行する際の信頼性が高まると説明されています（実験的、macOS/Linux のみ）。
* 自動承認ルールにより、不要なプロンプトを減らしつつ、エージェント主導の操作に対する安全性と制御を向上させます。
* タイムアウト、待機、停止などにより、バックグラウンドコマンドの制御を改善するターミナルライフサイクル改善が挙げられています。


### [Related VS Code productivity updates (not Copilot\-related)](https://github.blog/changelog/feed/#related-vs-code-productivity-updates-not-copilot-related)


* **Integrated browser**: エディタを離れずにアプリのテスト/実行が可能です。
* **Terminal enhancements**: ターミナル利用に関する使い勝手の改善が含まれます。
* **Coding \& editor improvements**: 日常のコーディングフローに関する複数の改善が含まれます。
* **Extensions \& API updates**: 拡張機能作者向けに、よりリッチな体験を構築するための新機能が追加されます。


Happy coding!


[GitHub Community](https://github.com/orgs/community/discussions/categories/announcements) でディスカッションに参加できます。
