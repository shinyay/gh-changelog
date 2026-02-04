---
title: "GitHub Copilot のカスタムエージェント"
date: "2025-10-28"
type: "new releases"
labels: ["copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-custom-agents-for-github-copilot"
fetched_at: "2026-02-03T14:50:55.662560Z"
lang: "ja"
---

# GitHub Copilot のカスタムエージェント

## Overview
GitHub Copilot のカスタムエージェントにより、シンプルなファイルベースの設定を通じて、ユーザーと組織が Copilot coding agent (CCA) を簡単に特化させることができます。

## Detailed Explanation
### 概要
- GitHub Copilot のカスタムエージェントにより、シンプルなファイルベースの設定を通じて、ユーザーと組織が Copilot coding agent (CCA) を簡単に特化させることができます。
- 任意のリポジトリの `.github/agents` 以下、または `{org}/.github` または `{org}/.github-private` リポジトリの `agents` フォルダーに設定ファイルを追加することで、チームのワークフロー、規約、独自のニーズを捉えたエージェントペルソナを定義できます。これらのエージェントは、プロンプト、ツール選択、Model Context Protocol (MCP) サーバーでさらにカスタマイズして、特定のユースケースに最適化できます。
- GitHub Copilot を使用している人なら誰でも、個人の開発者、チームの一員、組織の管理者であっても、カスタムエージェントを定義して使用できます。カスタムエージェントは、github.com の Copilot coding agent、Copilot CLI で動作し、将来の Visual Studio Code リリースにも対応予定です。

### 主な利点
- ワークフロー固有のプロンプトとツール選択を使用して、集中したチームメイトのように振る舞うエージェントの特化を定義します。
- リポジトリまたは組織設定の既知の場所に設定ファイルを配置することで、組織固有またはチーム固有のエージェントを追加します。
- 標準の Copilot 指示を超えてエージェントの動作を洗練させ、コーディング規約、コンプライアンス、カスタム自動化の実施を容易にします。
- エージェントがカスタムツールと MCP サーバーを使用できるようにし、タスクの完了方法をきめ細かく制御します。
- シンプルな Markdown ファイルを追加するだけで素早く開始できます。別途インストールや複雑なセットアップは不要です。

### 例
- React や Vue のチーム規約を実施するフロントエンドエンジニアのサブエージェントや、GitHub CLI で追加タスクを自動化するカスタム MCP を使用するエージェントを想像してください。カスタムエージェントを使用すると、これらの動作を中央ファイルで定義でき、簡単にアクセスして保守できます。
- どこから始めればよいかわからない？一部の素晴らしいパートナーが、ワークフローを改善するためのカスタムエージェントを作成しています。
- これらやその他のサンプルエージェントは @github/awesome-copilot で見つけることができます。
- カスタムエージェントに関するドキュメントを読んで詳細を確認し、GitHub Community でディスカッションに参加してください。

## Insights (derived from article language)
- どこから始めればよいかわからない？
- カスタムエージェントに関するドキュメントを読んで詳細を確認し、GitHub Community でディスカッションに参加してください。

## Article Content (cleaned)
GitHub Copilot のカスタムエージェントにより、シンプルなファイルベースの設定を通じて、ユーザーと組織が Copilot coding agent (CCA) を簡単に特化させることができます。


任意のリポジトリの `.github/agents` 以下、または `{org}/.github` または `{org}/.github-private` リポジトリの `agents` フォルダーに設定ファイルを追加することで、チームのワークフロー、規約、独自のニーズを捉えたエージェントペルソナを定義できます。これらのエージェントは、プロンプト、ツール選択、Model Context Protocol (MCP) サーバーでさらにカスタマイズして、特定のユースケースに最適化できます。


GitHub Copilot を使用している人なら誰でも、個人の開発者、チームの一員、組織の管理者であっても、カスタムエージェントを定義して使用できます。カスタムエージェントは、github.com の Copilot coding agent、Copilot CLI で動作し、将来の Visual Studio Code リリースにも対応予定です。


### [主な利点](#key-benefits)


* ワークフロー固有のプロンプトとツール選択を使用して、集中したチームメイトのように振る舞うエージェントの特化を定義します。
* リポジトリまたは組織設定の既知の場所に設定ファイルを配置することで、組織固有またはチーム固有のエージェントを追加します。
* 標準の Copilot 指示を超えてエージェントの動作を洗練させ、コーディング規約、コンプライアンス、カスタム自動化の実施を容易にします。
* エージェントがカスタムツールと MCP サーバーを使用できるようにし、タスクの完了方法をきめ細かく制御します。
* シンプルな Markdown ファイルを追加するだけで素早く開始できます。別途インストールや複雑なセットアップは不要です。


### [例](#examples)


React や Vue のチーム規約を実施するフロントエンドエンジニアのサブエージェントや、GitHub CLI で追加タスクを自動化するカスタム MCP を使用するエージェントを想像してください。カスタムエージェントを使用すると、これらの動作を中央ファイルで定義でき、簡単にアクセスして保守できます。


どこから始めればよいかわからない？一部の素晴らしいパートナーが、ワークフローを改善するためのカスタムエージェントを作成しています。  

![Custom agent launch partners](https://github.com/user-attachments/assets/1d77e22d-4ce2-415e-b91c-5332167f7873)


これらやその他のサンプルエージェントは [@github/awesome-copilot](https://github.com/github/awesome-copilot?utm_source=changelog-awesome-copilot-cutom-agents&utm_medium=changelog&utm_campaign=universe25) で見つけることができます。


[カスタムエージェントに関するドキュメント](https://gh.io/customagents?utm_source=changelog-docs-custom-agents&utm_medium=changelog&utm_campaign=universe25)を読んで詳細を確認し、[GitHub Community](https://github.com/orgs/community/discussions/177930?utm_source=changelog-community-custom-agents&utm_medium=changelog&utm_campaign=universe25) でディスカッションに参加してください。
