---
title: "GitHub Copilot CLI：新モデル、強化されたコード検索、改善された画像サポート"
date: "2025-11-18"
type: "improvements"
labels: ["client apps", "copilot"]
author: "Allison"
source_url: "https://github.com/blog/changelog/2025-11-18-github-copilot-cli-new-models-enhanced-code-search-and-better-image-support"
fetched_at: "2026-02-03T14:50:55.189982Z"
lang: "ja"
---

# GitHub Copilot CLI：新モデル、強化されたコード検索、改善された画像サポート

## Overview
GitHub Copilot CLIは、検索機能の大幅な改善、より良い画像サポート、最新のAIモデルへのアクセスとサポート、信頼性の向上など、継続的に進化しています。最近取り組んでいる内容をご紹介します。

## Detailed Explanation
### Overview
- GitHub Copilot CLIは、検索機能の大幅な改善、より良い画像サポート、最新のAIモデルへのアクセスとサポート、信頼性の向上など、継続的に進化しています。最近取り組んでいる内容をご紹介します。

### Latest AI models now available
- OpenAIとGoogleの最新モデルのサポートを追加し、最先端を維持できるようにしました：
- GPT-5.1、GPT-5.1-Codex、GPT-5.1-Codex-Mini
- Gemini 3 Pro

### More powerful code search
- Copilotがコードベースをより効率的に検索できるようになりました！Copilot CLIにripgrepをバンドルし、適切なコンテキストを迅速かつ強力に見つけるための`grep`および`glob`ツールを追加しました。

### Better image support
- 以前は、`@`メンションで画像ファイルをCopilotのコンテキストに追加していました。フィードバックに基づき、ペーストやドラッグ&ドロップで画像を追加できるように機能強化しました。

### Additional developer delighters
- `/share`コマンドでチャットセッションをMarkdownファイルまたはGitHub gistsとして簡単に保存できます
- heredocやその他の特殊文字を含む推奨コマンドでの不要な権限チェックを削除しました
- PowerShellでの`!`シェルモードコマンドのサポートを改善しました
- ヘッドレス`-p`モードを使用した自動化シナリオで、権限またはコミュニケーションエラーが発生した際にゼロ以外のコードで終了するように改善しました
- `/session`コマンドの出力を強化し、スタイルを改善しました
- アプリケーション全体で空白、フォーマット、UI操作を改善しました
- MCPサーバーツール通知のサポートを追加しました
- 長時間実行されるシェルコマンドのCopilotの処理を改善しました

### Reliability and bugfixes
- ユーザーから報告されたバグと信頼性の問題を多数修正しました：
- 長時間実行されるシェルコマンド実行時のメモリリークを防止しました
- カスタムエージェント構成に関するさまざまなバグ修正を実装しました
- Ctrl+Cシグナルと中止操作の処理を改善しました
- シェルツールの環境から内部`NODE_ENV`変数を削除し、Node開発シナリオでの競合を防止しました
- Windows Terminalキーボード入力をブロックする問題を修正しました
- `/model`コマンドでサポートされていないモデルを使用する際のエラーメッセージを改善しました
- 初回起動時に背景色の値が入力ボックスに印刷される問題を修正しました

### Share your feedback
- ターミナルで`npm install -g @github/copilot@latest`を実行して、GitHub Copilot CLIを更新してください。`/feedback`コマンドおよび公開リポジトリで問題を開くことでフィードバックを提出していただいたすべての方に感謝します。改善を続けていく上で、継続的なフィードバックは非常に貴重です。

## Impact / Who's Affected
- Latest AI models now available OpenAIとGoogleの最新モデルのサポートを追加し、最先端を維持できるようにしました：GPT-5.1、GPT-5.1-Codex、GPT-5.1-Codex-Mini Gemini 3 Pro More powerful code search Copilotがコードベースをより効率的に検索できるようになりました！

## Article Content (cleaned)
`GitHub Copilot CLIは、検索機能の大幅な改善、より良い画像サポート、最新のAIモデルへのアクセスとサポート、信頼性の向上など、継続的に進化しています。最近取り組んでいる内容をご紹介します。`


## [Latest AI models now available](#latest-ai-models-now-available)


OpenAIとGoogleの最新モデルのサポートを追加し、最先端を維持できるようにしました：


* GPT-5.1、GPT-5.1-Codex、GPT-5.1-Codex-Mini
* Gemini 3 Pro


## [More powerful code search](#more-powerful-code-search)


Copilotがコードベースをより効率的に検索できるようになりました！Copilot CLIに`ripgrep`をバンドルし、適切なコンテキストを迅速かつ強力に見つけるための`grep`および`glob`ツールを追加しました。


## [Better image support](#better-image-support)


以前は、`@`メンションで画像ファイルをCopilotのコンテキストに追加していました。フィードバックに基づき、ペーストやドラッグ&ドロップで画像を追加できるように機能強化しました。


## [Additional developer delighters](#additional-developer-delighters)


* `/share`コマンドでチャットセッションをMarkdownファイルまたはGitHub gistsとして簡単に保存できます
* heredocやその他の特殊文字を含む推奨コマンドでの不要な権限チェックを削除しました
* PowerShellでの`!`シェルモードコマンドのサポートを改善しました
* ヘッドレス`-p`モードを使用した自動化シナリオで、権限またはコミュニケーションエラーが発生した際にゼロ以外のコードで終了するように改善しました
* `/session`コマンドの出力を強化し、スタイルを改善しました
* アプリケーション全体で空白、フォーマット、UI操作を改善しました
* MCPサーバーツール通知のサポートを追加しました
* 長時間実行されるシェルコマンドのCopilotの処理を改善しました


## [Reliability and bugfixes](#reliability-and-bugfixes)


ユーザーから報告されたバグと信頼性の問題を多数修正しました：


* 長時間実行されるシェルコマンド実行時のメモリリークを防止しました
* カスタムエージェント構成に関するさまざまなバグ修正を実装しました
* Ctrl+Cシグナルと中止操作の処理を改善しました
* シェルツールの環境から内部`NODE_ENV`変数を削除し、Node開発シナリオでの競合を防止しました
* Windows Terminalキーボード入力をブロックする問題を修正しました
* `/model`コマンドでサポートされていないモデルを使用する際のエラーメッセージを改善しました
* 初回起動時に背景色の値が入力ボックスに印刷される問題を修正しました


## [Share your feedback](#share-your-feedback)


ターミナルで`npm install -g @github/copilot@latest`を実行して、GitHub Copilot CLIを更新してください。`/feedback`コマンドおよび[公開リポジトリ](https://github.com/github/copilot-cli)で問題を開くことでフィードバックを提出していただいたすべての方に感謝します。改善を続けていく上で、継続的なフィードバックは非常に貴重です。
