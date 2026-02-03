---
title: "GitHub MCPサーバー：新しいProjectsツール、OAuthスコープフィルタリング、新機能"
date: "2026-01-28"
type: "Release"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-28-github-mcp-server-new-projects-tools-oauth-scope-filtering-and-new-features"
fetched_at: "2026-02-03T14:50:49.392520Z"
lang: "ja"
---

# GitHub MCPサーバー：新しいProjectsツール、OAuthスコープフィルタリング、新機能

## Detailed Explanation
### 概要
- GitHub MCPサーバーが、コンテキストウィンドウのより効率的な使用でGitHub Projectsを管理する改善された機能、トークンの権限に基づく自動ツールフィルタリング、InsidersモードやHTTPサーバーモードを含む機能とともに到着しました！
- 詳細については、GitHub MCPサーバーリポジトリをご覧ください。

### 統合されたGitHub Projectsツールセット
- 以前、Projectsツールセットは、他の現在統合されたツールセットと同様に、ツールリストのためにコンテキストウィンドウの大部分を使用していました。その結果、トークン使用量を約23,000トークン（50%）削減しました。GitHub Projectsの管理が、以前のアプローチに代わる新しい統合されたツールセットでより簡単になりました。新しいprojectsツールセットは、プロジェクト管理機能への統一されたアクセスを提供します：
- projects_list：ユーザー、組織、またはリポジトリのプロジェクトをリストする。
- projects_get：フィールドとアイテムを含む特定のプロジェクトの詳細情報を取得する。
- projects_write：完全なフィールドサポートでプロジェクトアイテムを作成、更新、管理する。
- 統合されたツールは所有者タイプの検出を自動的に処理します。所有者がユーザーか組織かを指定する必要はありません。

### OAuthスコープフィルタリング
- GitHub MCPサーバーは、認証方法に基づいてツールの可用性を管理するようになりました。
- クラシックPersonal Access Token（ghp_プレフィックス）を使用する場合、サーバーはトークンのOAuthスコープを自動的に検出し、使用する権限がないツールを非表示にします。これにより、乱雑さが減り、トークンが実行できない操作を試みることによるエラーを防ぎます。自分用の個人アクセストークン（PAT）の作成の詳細については、個人アクセストークンの管理に関するドキュメントをご覧ください。

### 仕組み
- 起動時に、サーバーはトークンがクラシックPATかどうかを検出します。
- 軽量なAPI呼び出しを介してトークンのスコープを発見します。
- トークンが持っていないスコープを必要とするツールは自動的に非表示になります。

### 実験的機能のInsidersモード
- GitHub MCPサーバーで実験的およびプレビュー機能にアクセスできるオプトインメカニズムであるInsidersモードを導入しています。これは、ローカルとリモートサーバーの両方のデプロイメントで利用可能になります。

### 仕組み
- ユーザーは設定ヘッダーを設定するか、新しい/insiders URLを使用して明示的にオプトインします。
- 有効にすると、MCPサーバーは実験的機能、評価中の動作変更、まだ一般提供されていない機能へのアクセスを許可します。
- ヘッダーを削除するか、標準URLに戻すと、標準の一般提供動作が即座に復元されます。

### OAuthサポート付きHTTPサーバーモード
- エンタープライズユーザーは、OAuthトークンサポート付きのHTTPモードでGitHub MCPサーバーを実行できるようになりました。

### 今後の予定
- HTTPサーバーモード：設定可能なポートでローカルMCPサーバーをHTTPサーバーとして実行する。
- リクエストごとのOAuthトークン：Authorizationヘッダーを介したトークンのサポート。
- フォールバックサポート：ヘッダーが提供されない場合、GITHUB_PERSONAL_ACCESS_TOKENにフォールバックする。
- Enterprise Serverの互換性：GitHub Enterprise Serverデプロイメントの完全サポート。
- これにより、エンタープライズチームは、OAuthトークン転送を使用して共有MCPサーバーをデプロイでき、すべてのユーザーが自分の個人アクセストークンを管理する必要がなくなります。

### Copilotコーディングエージェントツール
- GitHub MCPサーバーは、Copilotコーディングエージェントを操作するための新しいツールと改善を追加します。
- 新しいget_copilot_job_statusツールを使用すると、Copilotの進行状況を確認できます。ジョブIDまたはプルリクエスト番号でクエリできます。
- assign_copilot_to_issueとcreate_pull_request_with_copilotの両方がbase_refパラメータをサポートするようになりました：
- 機能ブランチ：デフォルトブランチだけでなく、任意のブランチからCopilotの作業を開始する。
- スタックされたPR：機能ブランチをベースとして指定することで、既存の作業に基づいて構築する。
- シーケンシャルタスク：複数のCopilot割り当てを連鎖させる。
- タスクの割り当ては、ジョブIDまたはプルリクエストリンクを即座に返すため、すぐにステータスを追跡できます。
- assign_copilot_to_issueツールは、カスタム指示をサポートするようになりました。

### 始め方
- 始めるには、copilotツールセットを有効にします。
- 詳細については、GitHub MCPサーバーリポジトリをご覧ください。
- これらの機能を今すぐお試しください！フィードバックがある場合は、オープンソースのGitHub MCPサーバーリポジトリでissueを開いてください。

## Key Changes
- GitHub MCPサーバーで実験的およびプレビュー機能にアクセスできるオプトインメカニズムであるInsidersモードを導入しています。これは、ローカルとリモートサーバーの両方のデプロイメントで利用可能になります。

## Impact / Who's Affected
- 有効にすると、MCPサーバーは実験的機能、評価中の動作変更、まだ一般提供されていない機能へのアクセスを許可します。
- ヘッダーを削除するか、標準URLに戻すと、標準の一般提供動作が即座に復元されます。

## Insights (derived from article language)
- 詳細については、GitHub MCPサーバーリポジトリをご覧ください。
- 自分用の個人アクセストークン（PAT）の作成の詳細については、個人アクセストークンの管理に関するドキュメントをご覧ください。

## Article Content (cleaned)
![A code snippet defines a GitHub server configuration with an HTTP endpoint, an api.githubcopilot.com MCP insiders URL, and an X‑MCP‑Toolsets header set to projects.](https://github.com/user-attachments/assets/c80409be-8021-4b1e-9533-7dfa7f9b270d)


GitHub MCPサーバーが、コンテキストウィンドウのより効率的な使用でGitHub Projectsを管理する改善された機能、トークンの権限に基づく自動ツールフィルタリング、InsidersモードやHTTPサーバーモードを含む機能とともに到着しました！


詳細については、[GitHub MCPサーバーリポジトリ](https://github.com/github/github-mcp-server)をご覧ください。


## [Consolidated GitHub Projects toolset](https://github.blog/changelog/feed/#consolidated-github-projects-toolset)


以前、Projectsツールセットは、他の現在統合されたツールセットと同様に、ツールリストのためにコンテキストウィンドウの大部分を使用していました。その結果、トークン使用量を約**23,000トークン**（50%）削減しました。GitHub Projectsの管理が、以前のアプローチに代わる新しい統合されたツールセットでより簡単になりました。新しい`projects`ツールセットは、プロジェクト管理機能への統一されたアクセスを提供します：


* **`projects_list`**：ユーザー、組織、またはリポジトリのプロジェクトをリストする。
* **`projects_get`**：フィールドとアイテムを含む特定のプロジェクトの詳細情報を取得する。
* **`projects_write`**：完全なフィールドサポートでプロジェクトアイテムを作成、更新、管理する。


統合されたツールは所有者タイプの検出を自動的に処理します。所有者がユーザーか組織かを指定する必要はありません。


## [OAuth scope filtering](https://github.blog/changelog/feed/#oauth-scope-filtering)


GitHub MCPサーバーは、認証方法に基づいてツールの可用性を管理するようになりました。


クラシックPersonal Access Token（`ghp_`プレフィックス）を使用する場合、サーバーはトークンのOAuthスコープを自動的に検出し、使用する権限がないツールを非表示にします。これにより、乱雑さが減り、トークンが実行できない操作を試みることによるエラーを防ぎます。自分用の個人アクセストークン（PAT）の作成の詳細については、[個人アクセストークンの管理](https://docs.github.com/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)に関するドキュメントをご覧ください。


### [How it works](https://github.blog/changelog/feed/#how-it-works)


1. 起動時に、サーバーはトークンがクラシックPATかどうかを検出します。
2. 軽量なAPI呼び出しを介してトークンのスコープを発見します。
3. トークンが持っていないスコープを必要とするツールは自動的に非表示になります。




| Token Type | Behavior |
| --- | --- |
| Classic PAT (`ghp_`) | トークンスコープに基づいてツールがフィルタリングされる |
| Fine\-grained PAT (`github_pat_`) | すべてのツールが表示され、APIが権限を強制する |
| OAuth (remote server) | オンデマンドで動的スコープチャレンジ |


## [Insiders mode for experimental features](https://github.blog/changelog/feed/#insiders-mode-for-experimental-features)


GitHub MCPサーバーで実験的およびプレビュー機能にアクセスできるオプトインメカニズムである**Insidersモード**を導入しています。これは、ローカルとリモートサーバーの両方のデプロイメントで利用可能になります。


### [How it works](https://github.blog/changelog/feed/#how-it-works)


* ユーザーは設定ヘッダーを設定するか、新しい`/insiders` URLを使用して明示的にオプトインします。
* 有効にすると、MCPサーバーは実験的機能、評価中の動作変更、まだ一般提供されていない機能へのアクセスを許可します。
* ヘッダーを削除するか、標準URLに戻すと、標準の一般提供動作が即座に復元されます。


## [HTTP server mode with OAuth support](https://github.blog/changelog/feed/#http-server-mode-with-oauth-support)


エンタープライズユーザーは、OAuthトークンサポート付きのHTTPモードでGitHub MCPサーバーを実行できるようになりました。


### [What's coming](https://github.blog/changelog/feed/#whats-coming)


* **HTTPサーバーモード**：設定可能なポートでローカルMCPサーバーをHTTPサーバーとして実行する。
* **リクエストごとのOAuthトークン**：Authorizationヘッダーを介したトークンのサポート。
* **フォールバックサポート**：ヘッダーが提供されない場合、`GITHUB_PERSONAL_ACCESS_TOKEN`にフォールバックする。
* **Enterprise Serverの互換性**：GitHub Enterprise Serverデプロイメントの完全サポート。


これにより、エンタープライズチームは、OAuthトークン転送を使用して共有MCPサーバーをデプロイでき、すべてのユーザーが自分の個人アクセストークンを管理する必要がなくなります。


## [Copilot coding agent tools](https://github.blog/changelog/feed/#copilot-coding-agent-tools)


GitHub MCPサーバーは、Copilotコーディングエージェントを操作するための新しいツールと改善を追加します。


新しい`get_copilot_job_status`ツールを使用すると、Copilotの進行状況を確認できます。ジョブIDまたはプルリクエスト番号でクエリできます。


![Checking the status of Copilot coding agent jobs](https://github.com/user-attachments/assets/1acaa644-3718-4e5f-846c-6c19eee9faa4)


`assign_copilot_to_issue`と`create_pull_request_with_copilot`の両方が`base_ref`パラメータをサポートするようになりました：


* **機能ブランチ**：デフォルトブランチだけでなく、任意のブランチからCopilotの作業を開始する。
* **スタックされたPR**：機能ブランチをベースとして指定することで、既存の作業に基づいて構築する。
* **シーケンシャルタスク**：複数のCopilot割り当てを連鎖させる。


タスクの割り当ては、ジョブIDまたはプルリクエストリンクを即座に返すため、すぐにステータスを追跡できます。


`assign_copilot_to_issue`ツールは、カスタム指示をサポートするようになりました。


### [Getting started](https://github.blog/changelog/feed/#getting-started)


始めるには、`copilot`ツールセットを有効にします。


詳細については、[GitHub MCPサーバーリポジトリ](https://github.com/github/github-mcp-server)をご覧ください。


これらの機能を今すぐお試しください！フィードバックがある場合は、オープンソースの[GitHub MCPサーバーリポジトリ](https://github.com/github/github-mcp-server)でissueを開いてください。
