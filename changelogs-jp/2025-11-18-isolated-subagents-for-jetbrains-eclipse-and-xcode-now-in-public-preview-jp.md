---
title: "JetBrains、Eclipse、Xcode向けの独立したサブエージェントがパブリックプレビューに"
date: "2025-11-18"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-18-isolated-subagents-for-jetbrains-eclipse-and-xcode-now-in-public-preview"
fetched_at: "2026-02-03T14:50:55.228768Z"
lang: "ja"
---

# JetBrains、Eclipse、Xcode向けの独立したサブエージェントがパブリックプレビューに

## Overview
JetBrains IDE、Eclipse、Xcode全体で独立したサブエージェントがパブリックプレビューになったことをお知らせします！独立したコンテキストにより、現在のチャットセッションを離れることなく、集中したタスクを自律的なcopilotに委任できるため、Copilotがリサーチ、API設計、コードレビュー、またはプロジェクトコンテキストの収集を行う間も、作業の勢いを維持できます。各サブエージェントは独自の独立したコンテキスト内で動作するため、メインの会話がクリーンで集中した状態に保たれます。

## Detailed Explanation
### Overview
- JetBrains IDE、Eclipse、Xcode全体で独立したサブエージェントがパブリックプレビューになったことをお知らせします！独立したコンテキストにより、現在のチャットセッションを離れることなく、集中したタスクを自律的なcopilotに委任できるため、Copilotがリサーチ、API設計、コードレビュー、またはプロジェクトコンテキストの収集を行う間も、作業の勢いを維持できます。各サブエージェントは独自の独立したコンテキスト内で動作するため、メインの会話がクリーンで集中した状態に保たれます。

### ✨ What's new
- 専用サブエージェントコンテキスト：各サブエージェントは独自のコンテキストで実行され、長時間実行されるリサーチや分析プロンプトがメインの会話履歴を圧迫するのを防ぎます。
- 自律的実行：呼び出されると、サブエージェントはそれ以上のユーザー操作なしに進行するため、ドキュメントの発見、競合分析、技術コンテキストの組み立てなどのバックグラウンドタスクに最適です。

### ❓ How subagents work
- 前提条件：環境にカスタムエージェントを設定する必要があります。カスタムエージェントのドキュメントを読むか、利用可能なカスタムエージェントがわからない場合は、copilotに利用可能なカスタムエージェントをリストするように依頼してください。
- サブエージェントは2つの主要なメカニズムを通じて動作します：

### Automatic delegation
- Copilotは以下に基づいてタスクをプロアクティブに委任します：– リクエスト内のタスクの説明 – カスタムエージェント構成の説明フィールド – 現在のコンテキストと利用可能なツール

### Explicit invocation
- コマンドでメンションすることで、特定のサブエージェントをリクエストします：

### 🛠 Try it out
- サポートされているIDEでサブエージェントを始めるのは簡単です：
- IDEを更新：JetBrains IDE、Eclipse、またはXcodeで最新のGitHub Copilot拡張機能を実行していることを確認してください。
- Copilot Chatを開く：Copilot Chatで会話を開始または続行します。
- サブエージェントを呼び出す：サブエージェントはリクエストに基づいて自動呼び出しされるか、利用可能なカスタムエージェントを参照することで、キュレートされた指示と許可されたツールを備えた専門的なカスタムエージェントを明示的に呼び出すことができます。
- 応答をレビュー：サブエージェントがタスクを完了すると、その結果がメインの会話に戻り、フォローアップの質問や次のステップの準備が整います。

### 💬 Share your feedback
- フィードバックがロードマップを推進します。IDE内のフィードバックコントロールまたは既存のCopilotサポートチャネルを使用して、サブエージェントがどのように機能しているかをお知らせください。
- 製品内フィードバック：IDE内のフィードバックオプションを使用してください
- GitHubディスカッション：以下のチャネルで考えを共有してください：JetBrains GitHub Copilot in JetBrainsフィードバックリポジトリ Eclipse GitHub Copilot in Eclipseフィードバックリポジトリ Xcode GitHub Copilot in Xcodeフィードバックリポジトリ
- JetBrains GitHub Copilot in JetBrainsフィードバックリポジトリ
- Eclipse GitHub Copilot in Eclipseフィードバックリポジトリ
- Xcode GitHub Copilot in Xcodeフィードバックリポジトリ
- 今日から独立したサブエージェントにリサーチと分析を委任し始めて、プライマリチャットを優れたコードの出荷に集中させましょう。

## Impact / Who's Affected
- JetBrains IDE、Eclipse、Xcode全体で独立したサブエージェントがパブリックプレビューになったことをお知らせします！

## Article Content (cleaned)
JetBrains IDE、Eclipse、Xcode全体で独立したサブエージェントがパブリックプレビューになったことをお知らせします！独立したコンテキストにより、現在のチャットセッションを離れることなく、集中したタスクを自律的なcopilotに委任できるため、Copilotがリサーチ、API設計、コードレビュー、またはプロジェクトコンテキストの収集を行う間も、作業の勢いを維持できます。各サブエージェントは独自の独立したコンテキスト内で動作するため、メインの会話がクリーンで集中した状態に保たれます。


## [✨ What's new](#%e2%9c%a8-whats-new)


* **専用サブエージェントコンテキスト**：各サブエージェントは独自のコンテキストで実行され、長時間実行されるリサーチや分析プロンプトがメインの会話履歴を圧迫するのを防ぎます。
* **自律的実行**：呼び出されると、サブエージェントはそれ以上のユーザー操作なしに進行するため、ドキュメントの発見、競合分析、技術コンテキストの組み立てなどのバックグラウンドタスクに最適です。


## [❓ How subagents work](#%e2%9d%93-how-subagents-work)


**前提条件**：環境にカスタムエージェントを設定する必要があります。[カスタムエージェントのドキュメント](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)を読むか、利用可能なカスタムエージェントがわからない場合は、copilotに`利用可能なカスタムエージェントをリスト`するように依頼してください。


サブエージェントは2つの主要なメカニズムを通じて動作します：


### [Automatic delegation](#automatic-delegation)


Copilotは以下に基づいてタスクをプロアクティブに委任します：  

– リクエスト内のタスクの説明  

– カスタムエージェント構成の**説明**フィールド  

– 現在のコンテキストと利用可能なツール


### [Explicit invocation](#explicit-invocation)


コマンドでメンションすることで、特定のサブエージェントをリクエストします：



```
> Have the code-reviewer subagent look at my recent changes
> Let the documentation subagent generate API docs for this module

```

## [🛠 Try it out](#%f0%9f%9b%a0-try-it-out)


サポートされているIDEでサブエージェントを始めるのは簡単です：


1. **IDEを更新**：JetBrains IDE、Eclipse、またはXcodeで最新のGitHub Copilot拡張機能を実行していることを確認してください。
2. **Copilot Chatを開く**：Copilot Chatで会話を開始または続行します。
3. **サブエージェントを呼び出す**：サブエージェントはリクエストに基づいて自動呼び出しされるか、利用可能な[カスタムエージェント](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)を参照することで、キュレートされた指示と許可されたツールを備えた専門的なカスタムエージェントを明示的に呼び出すことができます。
4. **応答をレビュー**：サブエージェントがタスクを完了すると、その結果がメインの会話に戻り、フォローアップの質問や次のステップの準備が整います。


## [💬 Share your feedback](#%f0%9f%92%ac-share-your-feedback)


フィードバックがロードマップを推進します。IDE内のフィードバックコントロールまたは既存のCopilotサポートチャネルを使用して、サブエージェントがどのように機能しているかをお知らせください。


* **製品内フィードバック**：IDE内のフィードバックオプションを使用してください
* **GitHubディスカッション**：以下のチャネルで考えを共有してください：
	+ JetBrains [GitHub Copilot in JetBrainsフィードバックリポジトリ](https://github.com/microsoft/copilot-jetbrains-feedback/issues)
	+ Eclipse [GitHub Copilot in Eclipseフィードバックリポジトリ](https://github.com/microsoft/copilot-eclipse-feedback/issues)
	+ Xcode [GitHub Copilot in Xcodeフィードバックリポジトリ](https://github.com/github/CopilotForXcode/issues)


今日から独立したサブエージェントにリサーチと分析を委任し始めて、プライマリチャットを優れたコードの出荷に集中させましょう。
