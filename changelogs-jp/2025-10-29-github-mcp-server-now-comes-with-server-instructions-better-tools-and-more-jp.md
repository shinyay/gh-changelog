---
title: "GitHub MCP Server にサーバー命令、改善されたツールなどが追加されました"
date: "2025-10-29"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-29-github-mcp-server-now-comes-with-server-instructions-better-tools-and-more"
fetched_at: "2026-02-03T14:50:55.508229Z"
lang: "ja"
---

# GitHub MCP Server にサーバー命令、改善されたツールなどが追加されました

## Overview
GitHub MCP Server にサーバー命令が追加され、モデルによる新しく優れた使用方法が実現されました。

## Detailed Explanation
### Overview
- GitHub MCP Server にサーバー命令が追加され、モデルによる新しく優れた使用方法が実現されました。
- また、より多くのツールをより少数でより強力なツールに統合することで、GitHub MCP Server のフットプリントを削減し続けています。
- さらに、GitHub MCP Server をニーズに合わせて構成することが格段に簡単になりました！
- 詳細については、GitHub MCP Server リポジトリをご覧ください。

### Server instructions and multitool workflows
- サーバー命令は、Model Context Protocol 仕様の機能で、モデルが MCP サーバーを効果的に使用するためのガイドとなるシステムプロンプトのように機能します。これらは、ツールの相互依存性の尊重（「ツール B の前に常にツール A を使用する」）、マルチツールワークフローの実行（「プルリクエストのレビューを求められたら、常にツール A から始め、次にツール B を使用し、最後にツール C を使用する」）、またはほとんどのツールに共通する一般的なガイダンスの提供（「利用可能な場合は常にページネーションを使用する」）などに特に有用です。
- GitHub MCP Server にサーバー命令が追加されたことで、新しい可能性が解放されました。モデルは、プルリクエストのレビューや Issue またはディスカッションの管理などのタスクについて、より正確なワークフローに従うようになります。また、全般的にツールをより効果的に使用するようになります。
- サーバー命令が GitHub MCP Server の一部になったことで、MCP サーバーの進化に合わせて継続的に改善していきます！いつものように、開発者のニーズに最適に対応するために命令を調整する方法について、ユーザーからのフィードバックに注意深く耳を傾けています。

### Consolidating tools into more powerful multifunctional tools: pull requests, issues, sub-issues
- 関連するツールをより統一された多機能ツールにマージすることで、GitHub MCP Server をよりシンプルかつパフォーマンスの高いものにする作業を継続しています。以前と同様に、統合された各ツールは単一の `method` パラメータを通じて複数の操作をサポートし、構成をよりスリムに、AI の推論をより明確に、パフォーマンスをより高速にします。
- 前回のリリースでのプルリクエストツールの統合と同様に、次のプルリクエストレビューツールが単一の強力な `pull_request_review_write` ツールに統合されました：
- create_and_submit_pull_request_review
- create_pending_pull_request_review
- submit_pending_pull_request_review
- delete_pending_pull_request_review
- 新しいツールには、これらのタスクを実行するための `method` パラメータがあります：
- create
- submit_pending
- delete_pending
- 次の Issue ツールが単一の強力な `issue_read` ツールに統合されました：
- get_issue
- get_issue_comments
- list_labels（issue_number を指定）
- list_sub_issues
- 新しいツールには、これらの操作を実行するための `method` パラメータがあります：
- get
- get_comments
- get_labels
- get_sub_issues
- さらに、次の Issue ツールが単一の `issue_write` ツールに統合されました：
- create_issue
- update_issue
- 新しいツールには、これらの操作のための `method` パラメータがあります：
- create
- update
- 最後に、次のサブ Issue ツールが単一の `sub_issue_write` ツールに統合されました：
- add_sub_issue
- remove_sub_issue
- reprioritize_sub_issue
- 新しいツールには、これらの操作を実行するための `method` パラメータがあります：
- add
- reprioritize
- remove
- よく使用するツールが見つからない場合は、新しい多機能ツールに統合されたか、デフォルト構成から移動した可能性があります。

### Easier server configuration with the new default keyword
- 以前は、MCP サーバーを構成する際に、ツールセットを1つずつ入力して構成する必要がありました。`default` キーワードを導入することで、このプロセスを簡単にしました。サーバーを構成する際に、このキーワードを使用してデフォルトのツールセットを参照できます。
- これで、`code_security` のようなツールセットをデフォルトの MCP 構成に追加することが、リモート MCP サーバーの場合は `X-MCP-Toolsets:"default,code_security"`、ローカル MCP サーバーの場合は `--toolsets default,code_security` のように簡単になりました。
- 以前と同様に、`default` ツールセットには次のツールセットが含まれることに注意してください：
- `context` – 現在のユーザーと GitHub コンテキスト
- `repos` – リポジトリ操作
- `issues` – Issue トラッキング
- `pull_requests` – プルリクエストワークフロー
- `users` – ユーザー情報

## Impact / Who's Affected
- 前回のリリースでのプルリクエストツールの統合と同様に、次のプルリクエストレビューツールが単一の強力な pull_request_review_write ツールに統合されました：create_and_submit_pull_request_review create_pending_pull_request_review submit_pending_pull_request_review delete_pending_pull_request_review 新しいツールには、これらのタスクを実行するための method パラメータがあります：create submit_pending delete_pending 次の Issue ツールが単一の強力な issue_read ツールに統合されました：get_issue get_issue_comments list_labels（issue_number を指定）list_sub_issues 新しいツールには、これらの操作を実行するための method パラメータがあります：get get_comments get_labels get_sub_issues さらに、次の Issue ツールが単一の issue_write ツールに統合されました：create_issue update_issue 新しいツールには、これらの操作のための method パラメータがあります：create update 最後に、次のサブ Issue ツールが単一の sub_issue_write ツールに統合されました：add_sub_issue remove_sub_issue reprioritize_sub_issue 新しいツールには、これらの操作を実行するための method パラメータがあります：add reprioritize remove よく使用するツールが見つからない場合は、新しい多機能ツールに統合されたか、デフォルト構成から移動した可能性があります。
- Easier server configuration with the new default keyword 以前は、MCP サーバーを構成する際に、ツールセットを1つずつ入力して構成する必要がありました。

## Caveats / Limitations
- 前回のリリースでのプルリクエストツールの統合と同様に、次のプルリクエストレビューツールが単一の強力な pull_request_review_write ツールに統合されました：create_and_submit_pull_request_review create_pending_pull_request_review submit_pending_pull_request_review delete_pending_pull_request_review 新しいツールには、これらのタスクを実行するための method パラメータがあります：create submit_pending delete_pending 次の Issue ツールが単一の強力な issue_read ツールに統合されました：get_issue get_issue_comments list_labels（issue_number を指定）list_sub_issues 新しいツールには、これらの操作を実行するための method パラメータがあります：get get_comments get_labels get_sub_issues さらに、次の Issue ツールが単一の issue_write ツールに統合されました：create_issue update_issue 新しいツールには、これらの操作のための method パラメータがあります：create update 最後に、次のサブ Issue ツールが単一の sub_issue_write ツールに統合されました：add_sub_issue remove_sub_issue reprioritize_sub_issue 新しいツールには、これらの操作を実行するための method パラメータがあります：add reprioritize remove よく使用するツールが見つからない場合は、新しい多機能ツールに統合されたか、デフォルト構成から移動した可能性があります。
- Easier server configuration with the new default keyword 以前は、MCP サーバーを構成する際に、ツールセットを1つずつ入力して構成する必要がありました。
- 以前と同様に、default ツールセットには次のツールセットが含まれることに注意してください：context – 現在のユーザーと GitHub コンテキスト repos – リポジトリ操作 issues – Issue トラッキング pull_requests – プルリクエストワークフロー users – ユーザー情報

## Insights (derived from article language)
- 詳細については、GitHub MCP Server リポジトリをご覧ください。
- 以前と同様に、default ツールセットには次のツールセットが含まれることに注意してください：context – 現在のユーザーと GitHub コンテキスト repos – リポジトリ操作 issues – Issue トラッキング pull_requests – プルリクエストワークフロー users – ユーザー情報

## Article Content (cleaned)
GitHub MCP Server にサーバー命令が追加され、モデルによる新しく優れた使用方法が実現されました。


また、より多くのツールをより少数でより強力なツールに統合することで、GitHub MCP Server のフットプリントを削減し続けています。


さらに、GitHub MCP Server をニーズに合わせて構成することが格段に簡単になりました！


詳細については、[GitHub MCP Server リポジトリ](https://github.com/github/github-mcp-server)をご覧ください。


## [Server instructions and multitool workflows](#server-instructions-and-multitool-workflows)


サーバー命令は、Model Context Protocol 仕様の機能で、モデルが MCP サーバーを効果的に使用するためのガイドとなるシステムプロンプトのように機能します。これらは、ツールの相互依存性の尊重（「ツール B の前に常にツール A を使用する」）、マルチツールワークフローの実行（「プルリクエストのレビューを求められたら、常にツール A から始め、次にツール B を使用し、最後にツール C を使用する」）、またはほとんどのツールに共通する一般的なガイダンスの提供（「利用可能な場合は常にページネーションを使用する」）などに特に有用です。


GitHub MCP Server にサーバー命令が追加されたことで、新しい可能性が解放されました。モデルは、プルリクエストのレビューや Issue またはディスカッションの管理などのタスクについて、より正確なワークフローに従うようになります。また、全般的にツールをより効果的に使用するようになります。


サーバー命令が GitHub MCP Server の一部になったことで、MCP サーバーの進化に合わせて継続的に改善していきます！いつものように、開発者のニーズに最適に対応するために命令を調整する方法について、ユーザーからのフィードバックに注意深く耳を傾けています。


## [Consolidating tools into more powerful multifunctional tools: pull requests, issues, sub\-issues](#consolidating-tools-into-more-powerful-multifunctional-tools-pull-requests-issues-sub-issues)


関連するツールをより統一された多機能ツールにマージすることで、GitHub MCP Server をよりシンプルかつパフォーマンスの高いものにする作業を継続しています。以前と同様に、統合された各ツールは単一の `method` パラメータを通じて複数の操作をサポートし、構成をよりスリムに、AI の推論をより明確に、パフォーマンスをより高速にします。


前回のリリースでのプルリクエストツールの統合と同様に、次のプルリクエストレビューツールが単一の強力な `pull_request_review_write` ツールに統合されました：


* `create_and_submit_pull_request_review`
* `create_pending_pull_request_review`
* `submit_pending_pull_request_review`
* `delete_pending_pull_request_review`


新しいツールには、これらのタスクを実行するための `method` パラメータがあります：


* `create`
* `submit_pending`
* `delete_pending`


次の Issue ツールが単一の強力な `issue_read` ツールに統合されました：


* `get_issue`
* `get_issue_comments`
* `list_labels (with issue_number)`
* `list_sub_issues`


新しいツールには、これらの操作を実行するための `method` パラメータがあります：


* `get`
* `get_comments`
* `get_labels`
* `get_sub_issues`


さらに、次の Issue ツールが単一の `issue_write` ツールに統合されました：


* `create_issue`
* `update_issue`


新しいツールには、これらの操作のための `method` パラメータがあります：


* `create`
* `update`


最後に、次のサブ Issue ツールが単一の `sub_issue_write` ツールに統合されました：


* `add_sub_issue`
* `remove_sub_issue`
* `reprioritize_sub_issue`


新しいツールには、これらの操作を実行するための `method` パラメータがあります：


* `add`
* `reprioritize`
* `remove`


よく使用するツールが見つからない場合は、新しい多機能ツールに統合されたか、デフォルト構成から移動した可能性があります。


## [Easier server configuration with the new `default` keyword](#easier-server-configuration-with-the-new-default-keyword)


以前は、MCP サーバーを構成する際に、ツールセットを1つずつ入力して構成する必要がありました。`default` キーワードを導入することで、このプロセスを簡単にしました。サーバーを構成する際に、このキーワードを使用してデフォルトのツールセットを参照できます。


これで、`code_security` のようなツールセットをデフォルトの MCP 構成に追加することが、リモート MCP サーバーの場合は `X-MCP-Toolsets:"default,code_security"`、ローカル MCP サーバーの場合は `--toolsets default,code_security` のように簡単になりました。


以前と同様に、`default` ツールセットには次のツールセットが含まれることに注意してください：


* `context` – 現在のユーザーと GitHub コンテキスト
* `repos` – リポジトリ操作
* `issues` – Issue トラッキング
* `pull_requests` – プルリクエストワークフロー
* `users` – ユーザー情報
