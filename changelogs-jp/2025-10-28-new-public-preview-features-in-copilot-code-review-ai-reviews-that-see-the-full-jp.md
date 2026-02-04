---
title: "Copilot コードレビューの新しいパブリックプレビュー機能：全体像を把握する AI レビュー"
date: "2025-10-28"
type: "new releases"
labels: ["copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-new-public-preview-features-in-copilot-code-review-ai-reviews-that-see-the-full-picture"
fetched_at: "2026-02-03T14:50:55.542154Z"
lang: "ja"
---

# Copilot コードレビューの新しいパブリックプレビュー機能：全体像を把握する AI レビュー

## Overview
Copilot コードレビュー（CCR）は、LLM 検出とツール呼び出しを ESLint や CodeQL などの決定論的ツールと組み合わせることで、よりスマートなレビューを提供し、修正のために Copilot コーディングエージェントへのシームレスな引き継ぎを実現します。

## Detailed Explanation
### Overview
- Copilot コードレビュー（CCR）は、LLM 検出とツール呼び出しを ESLint や CodeQL などの決定論的ツールと組み合わせることで、よりスマートなレビューを提供し、修正のために Copilot コーディングエージェントへのシームレスな引き継ぎを実現します。

### Rich context with tool calling 🧰
- CCR は、エージェント型ツール呼び出しを活用して、コード、ディレクトリ構造、参照などのプロジェクト全体のコンテキストを積極的に収集します。これにより、CCR は変更がより広範なプロジェクトアーキテクチャにどのように適合するかを理解できます。
- 💡 重要な理由：フィードバックが具体的で正確になり、ノイズが少なくなるため、より迅速にクリーンなコードを提供できます。

### New deterministic detections with CodeQL and ESLint🕵️‍♀️
- CCR は近日中に CodeQL と主要な Linter（ESLint から開始）を統合し、セマンティック解析とクラシックなルールベースのチェックを組み合わせます。この LLM インテリジェンスと決定論的精度の融合により、セキュリティと品質のための高品質で一貫性のある検出結果を提供します。
- 💡 重要な理由：開発者は、セキュリティ脆弱性から保守性の問題まで、重大な問題が確実に捕捉され、明確に説明されることを信頼できます。
- 編集者注（2025年10月31日）：重要な理由の説明を更新しました。

### Seamless handoff to Copilot coding agent 🤝
- 提案された変更を Copilot コーディングエージェントに直接引き継ぐことができるようになりました。プルリクエストで `@copilot` をメンションすると、CCR は提案された修正をスタックされたプルリクエストに自動的に適用し、レビューとマージの準備が整います。
- 💡 重要な理由：手動クリーンアップとレビューサイクルが減少し、より価値の高いエンジニアリング作業に集中できます。
- [デモ動画：CCR コメントからの実装提案ボタンの使用]

### Customizable workflows and editor availability 🛠️
- カスタマイズ可能なワークフローと複数エディターのサポートがすでに一般提供されており、CCR はコードの記述からレビューとマージまで、開発プロセスのあらゆる段階にシームレスに適合します。
- チームは `instructions.md` または `copilot-instructions.md` ファイルを通じて独自のレビュー基準とトーンを定義し、CCR が優先する内容（例：テストカバレッジ、パフォーマンス、可読性）を形作ることができます。CCR は VS Code、Visual Studio、JetBrains、Xcode、および github.com で利用でき、どこで作業していても一貫したフィードバックを保証します。
- 💡 重要な理由：CCR はチームの基準に適応し、作業場所で対応します。

### Getting started 🚀
- ツール呼び出しと決定論的検出はパブリックプレビュー中で、Copilot Pro および Copilot Pro Plus ユーザーにはデフォルトで有効になっています。Copilot Business および Copilot Enterprise ユーザーは、Copilot コードレビューポリシーを使用してオプトインできます。
- GitHub Community でディスカッションに参加してください。

## Impact / Who’s Affected
- より価値の高いエンジニアリング作業に集中できます。[デモ動画：CCR コメントからの実装提案ボタンの使用] カスタマイズ可能なワークフローとエディターの可用性 🛠️ カスタマイズ可能なワークフローと複数エディターのサポートがすでに一般提供されており、CCR はコードの記述からレビューとマージまで、開発プロセスのあらゆる段階にシームレスに適合します。
- Getting started 🚀 ツール呼び出しと決定論的検出はパブリックプレビュー中で、Copilot Pro および Copilot Pro Plus ユーザーにはデフォルトで有効になっています。

## Caveats / Limitations
- 編集者注（2025年10月31日）：重要な理由の説明を更新しました。

## Article Content (cleaned)
Copilot コードレビュー（CCR）は、LLM 検出とツール呼び出しを ESLint や CodeQL などの決定論的ツールと組み合わせることで、よりスマートなレビューを提供し、修正のために Copilot コーディングエージェントへのシームレスな引き継ぎを実現します。


### [Rich context with tool calling 🧰](#rich-context-with-tool-calling-%f0%9f%a7%b0)


CCR は、エージェント型ツール呼び出しを活用して、コード、ディレクトリ構造、参照などのプロジェクト全体のコンテキストを積極的に収集します。これにより、CCR は変更がより広範なプロジェクトアーキテクチャにどのように適合するかを理解できます。


💡 *重要な理由：* フィードバックが具体的で正確になり、ノイズが少なくなるため、より迅速にクリーンなコードを提供できます。


![Diagram of tools in Copilot code review](https://github.com/user-attachments/assets/6de9a8a5-eb27-4075-8e89-038a6a823b8c)


### [New deterministic detections with CodeQL and ESLint🕵️‍♀️](#new-deterministic-detections-with-codeql-and-eslint%f0%9f%95%b5%ef%b8%8f%e2%99%80%ef%b8%8f)


CCR は近日中に CodeQL と主要な Linter（ESLint から開始）を統合し、セマンティック解析とクラシックなルールベースのチェックを組み合わせます。この LLM インテリジェンスと決定論的精度の融合により、セキュリティと品質のための高品質で一貫性のある検出結果を提供します。


💡 *重要な理由：* 開発者は、セキュリティ脆弱性から保守性の問題まで、重大な問題が確実に捕捉され、明確に説明されることを信頼できます。


*編集者注（2025年10月31日）：重要な理由の説明を更新しました。*


### [Seamless handoff to Copilot coding agent 🤝](#seamless-handoff-to-copilot-coding-agent-%f0%9f%a4%9d)


提案された変更を **Copilot コーディングエージェント** に直接引き継ぐことができるようになりました。プルリクエストで `@copilot` をメンションすると、CCR は提案された修正をスタックされたプルリクエストに自動的に適用し、レビューとマージの準備が整います。


💡 *重要な理由：* 手動クリーンアップとレビューサイクルが減少し、より価値の高いエンジニアリング作業に集中できます。


\[デモ動画：CCR コメントからの実装提案ボタンの使用]


### [Customizable workflows and editor availability 🛠️](#customizable-workflows-and-editor-availability-%f0%9f%9b%a0%ef%b8%8f)


カスタマイズ可能なワークフローと複数エディターのサポートがすでに一般提供されており、CCR はコードの記述からレビューとマージまで、開発プロセスのあらゆる段階にシームレスに適合します。


チームは `instructions.md` または `copilot-instructions.md` ファイルを通じて独自のレビュー基準とトーンを定義し、CCR が優先する内容（例：テストカバレッジ、パフォーマンス、可読性）を形作ることができます。CCR は VS Code、Visual Studio、JetBrains、Xcode、および github.com で利用でき、どこで作業していても一貫したフィードバックを保証します。


💡 *重要な理由：* CCR はチームの基準に適応し、作業場所で対応します。


![Image of copilot-instructions.md containing a list of instructions for Copilot code review to follow written in plain text.](https://github.com/user-attachments/assets/97de7185-908c-4702-bc5c-7dc2dafe5b09)


### [Getting started 🚀](#getting-started-%f0%9f%9a%80)


ツール呼び出しと決定論的検出はパブリックプレビュー中で、Copilot Pro および Copilot Pro Plus ユーザーにはデフォルトで有効になっています。Copilot Business および Copilot Enterprise ユーザーは、Copilot コードレビューポリシーを使用してオプトインできます。


[GitHub Community](https://github.com/orgs/community/discussions/177790?utm_source=changelog-community-copilot-code-review&utm_medium=changelog&utm_campaign=universe25) でディスカッションに参加してください。
