---
title: "GitHub Copilot CLI: エージェントの強化、コンテキスト管理、新しいインストール方法"
date: "2026-01-14"
type: "improvements"
labels: ["client apps", "copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-14-github-copilot-cli-enhanced-agents-context-management-and-new-ways-to-install"
fetched_at: "2026-02-03T14:50:54.791888Z"
lang: "ja"
---

# GitHub Copilot CLI: エージェントの強化、コンテキスト管理、新しいインストール方法

## Overview
2025年を締めくくり2026年を迎えるにあたり、GitHub Copilot CLI でエージェントを操作する新しい方法を提供し続け、すべての開発者向けにターミナルネイティブなエクスペリエンスを改善してきました。前回のアップデート以降の新機能をご紹介します。

## Detailed Explanation
### Overview
- 2025年を締めくくり2026年を迎えるにあたり、GitHub Copilot CLI でエージェントを操作する新しい方法を提供し続け、すべての開発者向けにターミナルネイティブなエクスペリエンスを改善してきました。前回のアップデート以降の新機能をご紹介します。

### New models and easier model management
- GPT-5 mini と GPT-4.1 は、Copilot サブスクリプションに含まれ、有料プランでプレミアムリクエストを消費しないモデルとして利用可能になりました。すべてのモデルオプションを表示するには `/model` を実行してください。
- ポリシー設定で無効になっているモデルを選択すると、CLI がターミナルを離れることなく直接有効化を促すようになりました。これは、Copilot Pro/Pro+ ユーザー向けのモデルピッカー、`/model` コマンド、`--model` フラグで機能します。

### Built-in custom agents
- Copilot CLI には、一般的なタスク用の専用カスタムエージェントが含まれるようになりました:
- Explore : 高速なコードベース分析。メインコンテキストを散らかすことなく、コードについて質問できます。
- Task : テストやビルドなどのコマンドを実行します。成功時は簡潔なサマリー、失敗時は完全な出力を受け取ります。
- Plan : 依存関係と構造を分析して実装計画を作成します。
- Code-review : 高いシグナル対ノイズ比で変更をレビューし、本当の問題のみを表面化することに焦点を当てます。
- Copilot は、適切な場合にこれらのエージェントに自動的に委任し、複数のエージェントを並列で実行できます。
- Agent Skills と組み合わせることで、Copilot CLI エクスペリエンスにエージェントワークフローをより簡単に統合できます。

### New ways to install
- Windows (WinGet):
- macOS および Linux (Homebrew):
- macOS および Linux (インストールスクリプト):
- パッケージマネージャーとインストールスクリプトによるインストールは自動的に更新されます。
- Codespaces と dev container: Copilot CLI はデフォルトの GitHub Codespaces イメージに含まれており、Dev Container Feature として利用できます。
- スタンドアロンの実行可能ファイルも、すべてのプラットフォーム向けに GitHub リリースアーティファクトで利用できます。

### Automation and scripting
- 新しいフラグにより、`copilot -p` を介したスクリプトやパイプラインでの Copilot CLI の使用が容易になりました:
- すべてのオプションフラグのリストについては、`copilot --help` を参照してください。
- CI/CD 認証: `GITHUB_ASKPASS` をトークンを返す実行可能ファイルにポイントします。これは、認証情報マネージャーやパイプラインに役立ちます。
- Copilot Spaces: GitHub MCP サーバーに、プロジェクト固有のコンテキスト用の Copilot Spaces ツールが含まれるようになりました。

### Context management
- 自動コンパクション : トークン制限の 95% に近づくと、Copilot が自動的に履歴を圧縮します。
- `/compact` : いつでも手動でコンテキストを圧縮できます。
- `/context` : 詳細な内訳でトークン使用量を可視化します。
- `--resume` : TAB を押してローカルセッションとリモート Copilot コーディングエージェントセッションを切り替えます。

### Terminal experience
- より良い diff : インライン構文ハイライトで何が変更されたかを正確に表示します。Git の設定されたページャーと統合されるようになりました。
- タブ補完 : `/cwd` と `/add-dir` でパスを自動補完します。
- Ctrl+T : サポートされているモデルでモデル推論の可視性を切り替えます。
- よりクリーンな履歴 : エージェント実行コマンドは Bash/PowerShell 履歴から除外されます。

### Web access controls
- 新しい `web_fetch` ツールは、URL からコンテンツをマークダウンとして取得します。URL アクセスは、`~/.copilot/config` の `allowed_urls` と `denied_urls` パターンで制御されます。これらのルールは、`curl` や `wget` などのシェルコマンドにも適用されます。

### Share your feedback
- パッケージマネージャーで更新するか、`npm install -g @github/copilot@latest` を実行してください。
- Copilot CLI の公開リポジトリでディスカッションに参加してください。

## Impact / Who's Affected
- New models and easier model management GPT-5 mini と GPT-4.1 は、Copilot サブスクリプションに含まれ、有料プランでプレミアムリクエストを消費しないモデルとして利用可能になりました。
- Code-review : 高いシグナル対ノイズ比で変更をレビューし、本当の問題のみを表面化することに焦点を当てます。

## Caveats / Limitations
- Code-review : 高いシグナル対ノイズ比で変更をレビューし、本当の問題のみを表面化することに焦点を当てます。

## Article Content (cleaned)
2025年を締めくくり2026年を迎えるにあたり、GitHub Copilot CLI でエージェントを操作する新しい方法を提供し続け、すべての開発者向けにターミナルネイティブなエクスペリエンスを改善してきました。前回のアップデート以降の新機能をご紹介します。


## [New models and easier model management](#new-models-and-easier-model-management)


![This image shows the full model list of Copilot CLI, including new 0x models GPT-5 mini and GPT-4.1. One model, GPT-5.2, has not been enabled by this user, and they see a 'requires enablement' prompt to turn on access](https://github.com/user-attachments/assets/e7a818e6-cfdf-417f-9129-ffe4b5b46077)


**GPT-5 mini** と **GPT-4.1** は、Copilot サブスクリプションに含まれ、有料プランでプレミアムリクエストを消費しないモデルとして利用可能になりました。すべてのモデルオプションを表示するには `/model` を実行してください。


ポリシー設定で無効になっているモデルを選択すると、CLI がターミナルを離れることなく直接有効化を促すようになりました。これは、Copilot Pro/Pro+ ユーザー向けのモデルピッカー、`/model` コマンド、`--model` フラグで機能します。


## [Built-in custom agents](#built-in-custom-agents)


![This image shows the built-in explore agent searching the codebase for authentication patterns across the codebase](https://github.com/user-attachments/assets/f83db7a4-ed8b-4d45-aa7b-e10b08f8d72a)


Copilot CLI には、一般的なタスク用の専用カスタムエージェントが含まれるようになりました:


* **Explore**: 高速なコードベース分析。メインコンテキストを散らかすことなく、コードについて質問できます。
* **Task**: テストやビルドなどのコマンドを実行します。成功時は簡潔なサマリー、失敗時は完全な出力を受け取ります。
* **Plan**: 依存関係と構造を分析して実装計画を作成します。
* **Code-review**: 高いシグナル対ノイズ比で変更をレビューし、本当の問題のみを表面化することに焦点を当てます。


Copilot は、適切な場合にこれらのエージェントに自動的に委任し、複数のエージェントを並列で実行できます。


[Agent Skills](https://github.blog/changelog/2025-12-18-github-copilot-now-supports-agent-skills/) と組み合わせることで、Copilot CLI エクスペリエンスにエージェントワークフローをより簡単に統合できます。


## [New ways to install](#new-ways-to-install)


**Windows (WinGet):**



```
winget install GitHub.Copilot

```

**macOS および Linux (Homebrew):**



```
brew install copilot-cli

```

**macOS および Linux (インストールスクリプト):**



```
curl -fsSL https://gh.io/copilot-install | bash

```

パッケージマネージャーとインストールスクリプトによるインストールは**自動的に更新されます**。


**Codespaces と dev container:** Copilot CLI はデフォルトの GitHub Codespaces イメージに含まれており、[Dev Container Feature](https://github.com/devcontainers/features) として利用できます。


スタンドアロンの実行可能ファイルも、すべてのプラットフォーム向けに [GitHub リリースアーティファクト](https://github.com/github/copilot-cli/releases) で利用できます。


## [Automation and scripting](#automation-and-scripting)


新しいフラグにより、`copilot -p` を介したスクリプトやパイプラインでの Copilot CLI の使用が容易になりました:




| Flag | Description |
| --- | --- |
| `--silent` | クリーンで解析可能な出力のために統計とログを抑制します |
| `--share [PATH]` | セッショントランスクリプトをマークダウンファイルにエクスポートします |
| `--share-gist` | セッションを共有可能な GitHub gist にエクスポートします |
| `--available-tools` | 特定のツールを許可リストに追加します |
| `--excluded-tools` | 特定のツールを拒否リストに追加します |
| `--additional-mcp-config` | セッションごとに MCP 設定ファイルを追加します |


すべてのオプションフラグのリストについては、`copilot --help` を参照してください。


**CI/CD 認証:** `GITHUB_ASKPASS` をトークンを返す実行可能ファイルにポイントします。これは、認証情報マネージャーやパイプラインに役立ちます。


**Copilot Spaces:** GitHub MCP サーバーに、プロジェクト固有のコンテキスト用の Copilot Spaces ツールが含まれるようになりました。


## [Context management](#context-management)


![This image shows the output of the /context command and the /compact command](https://github.com/user-attachments/assets/a6088645-33da-4c29-a6cf-c97b7d51c7a3)


* **自動コンパクション**: トークン制限の 95% に近づくと、Copilot が自動的に履歴を圧縮します。
* **`/compact`**: いつでも手動でコンテキストを圧縮できます。
* **`/context`**: 詳細な内訳でトークン使用量を可視化します。
* **`--resume`**: `TAB` を押してローカルセッションとリモート Copilot コーディングエージェントセッションを切り替えます。


## [Terminal experience](#terminal-experience)


* **より良い diff**: インライン構文ハイライトで何が変更されたかを正確に表示します。Git の設定されたページャーと統合されるようになりました。
* **タブ補完**: `/cwd` と `/add-dir` でパスを自動補完します。
* **Ctrl+T**: サポートされているモデルでモデル推論の可視性を切り替えます。
* **よりクリーンな履歴**: エージェント実行コマンドは Bash/PowerShell 履歴から除外されます。


## [Web access controls](#web-access-controls)


新しい `web_fetch` ツールは、URL からコンテンツをマークダウンとして取得します。URL アクセスは、`~/.copilot/config` の `allowed_urls` と `denied_urls` パターンで制御されます。これらのルールは、`curl` や `wget` などのシェルコマンドにも適用されます。


## [Share your feedback](#share-your-feedback)


パッケージマネージャーで更新するか、`npm install -g @github/copilot@latest` を実行してください。


Copilot CLI の [公開リポジトリ](https://github.com/github/copilot-cli) でディスカッションに参加してください。
