---
title: "GitHub Copilot CLI: 構築前に計画し、進行中に舵を取る"
date: "2026-01-21"
type: "improvements"
labels: ["client apps", "copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-21-github-copilot-cli-plan-before-you-build-steer-as-you-go"
fetched_at: "2026-02-03T14:50:54.733310Z"
lang: "ja"
---

# GitHub Copilot CLI: 構築前に計画し、進行中に舵を取る

## Overview
GitHub Copilot CLI は、ターミナル内でのエージェント AI アシスタンスの限界を押し広げ続けています。今週は、強力な新しい推論モデル、リアルタイムで会話を操れるインテリジェントなワークフロー機能、GitHub CLI とのより緊密な統合をもたらします。新機能は以下の通りです。

## Detailed Explanation
### Overview
- GitHub Copilot CLI は、ターミナル内でのエージェント AI アシスタンスの限界を押し広げ続けています。今週は、強力な新しい推論モデル、リアルタイムで会話を操れるインテリジェントなワークフロー機能、GitHub CLI とのより緊密な統合をもたらします。新機能は以下の通りです。

### Plan mode
- 最もリクエストされた機能の 1 つがここにあります: plan mode は、Copilot が実装を開始する前に、共同計画エクスペリエンスを提供します。
- Shift + Tab を押して、プランモードに出入りします。プランモードでは、Copilot がリクエストを分析し、スコープと要件を理解するための明確化質問をし、コードを書く前に構造化された実装計画を構築します。
- エクスペリエンスは会話的です。Copilot は新しい ask_user ツールを使用して、フォローアップの質問を促し、機能スコープに関する仮定を確認し、設計の決定に関する入力を取得します。アプローチについて合意したら、専用パネルで計画を確認し、Copilot に実装を開始するよう指示できます。
- これにより、次のことができます:
- コードが書かれる前に誤解を早期にキャッチします。
- 実装アプローチについて情報に基づいた意思決定を行います。
- 複雑なマルチステップタスクのコントロールを維持します。

### Advanced reasoning models
- GPT-5.2-Codex: コード生成と理解に最適化された最新の Codex モデルが利用可能になりました。`/model` または `--model gpt-5.2-codex` で選択します。
- 設定可能な推論努力: 拡張思考をサポートする GPT モデルの場合、プロンプトにモデルが適用する推論努力の量を設定できるようになりました。これにより、タスクに応じて応答速度と推論の深さのバランスを取ることができます。
- 推論の可視性を切り替え: Ctrl + T を押して、生成中のモデルの推論ステップを表示または非表示にします。この設定はセッション間で持続するため、Copilot が複雑な問題にどのようにアプローチするかを常に確認できます。

### Steer the conversation
- 追加のメッセージをキューに入れる: Copilot が考えている間にインタラクションできるようになりました。フォローアップメッセージを送信して会話を別の方向に導いたり、Copilot が現在の応答を終えた後に処理する追加の指示をキューに入れたりできます。これにより、会話がより自然に感じられ、コントロールを維持できます。
- 拒否時のインラインフィードバック: ツールの許可リクエストを拒否するときに、Copilot にインラインフィードバックを提供できるため、完全に停止することなくアプローチを適応させることができます。これにより、特定のアクションから Copilot を遠ざけたい場合に会話がより自然に流れます。

### Background delegation
- 任意のプロンプトの前に `&` を付けて、クラウド内の GitHub Copilot コーディングエージェントに委任します (`/delegate` コマンドと同等)。これにより、Copilot が長いタスクを非同期で処理している間、ターミナルが他の作業に解放されます。

### Automatic context management
- 自動コンパクション: 会話がトークン制限の 95% に近づくと、Copilot はワークフローを中断することなくバックグラウンドで履歴を自動的に圧縮します。これにより、事実上無限のセッションが可能になります。
- 手動コントロール: `/compact` を使用して、いつでも手動でコンテキストを圧縮します。気が変わった場合は Escape を押してキャンセルします。
- 使用状況の可視化: `/context` コマンドは、コンテキストウィンドウがどのように使用されているかを理解できるように、詳細なトークン使用量の内訳を表示します。

### Enhanced permissions experience
- 並列リクエストの承認: セッション用に承認を選択すると、同じタイプの保留中の並列許可リクエストが自動承認され、複雑なマルチステップ操作中の中断が減ります。
- 便利なフラグ: 新しい `--allow-all` および `--yolo` フラグは、Copilot を自由に実行することを信頼する場合に、すべての許可を一度に有効にします。

### Code review
- 新しい `/review` コマンドは、CLI でコードの変更を直接分析します。ターミナルを離れることなく、ステージングされた変更またはステージングされていない変更に関するフィードバックを取得します。コミット前のクイックサニティチェックに最適です。

### Repository memory
- Copilot は、セッション間でコードベースに関する重要な事実を記憶できるようになりました。作業中、Copilot は学習する規約、パターン、設定を保存し、将来のセッションをより生産的にします。メモリストレージツールは、コーディング標準、プロジェクト構造の洞察、好みのアプローチなどのコンテキストをキャプチャします。Copilot のエージェントメモリ機能の詳細については、Copilot メモリに関するエンジニアリングブログ記事をご覧ください。

### Shell mode improvements
- 履歴フィルタリング: シェルモード履歴ナビゲーション (`!` プレフィックス) がプレフィックスでフィルタリングするようになりました。`!git` と入力して上矢印を押すと、以前の git コマンドのみを循環し、特定のコマンドをより迅速に見つけて再実行できます。
- よりクリーンな環境: Copilot は、Bash および PowerShell 履歴ファイルからシェルコマンドを除外し、シェル履歴をクリーンに保ちます。

### Developer quality-of-life
- `/resume` コマンド: ローカルおよびリモートの GitHub Copilot コーディングエージェントセッション間を簡単に切り替えます。
- `/cd` エイリアス: 作業ディレクトリを変更する `/cwd` の短縮形。
- 改善されたセッションイベント: より簡潔で視覚的にクリーンなセッションメッセージ。
- タブタイトル: 現在の意図がターミナルのタブタイトルに表示されるようになりました。
- カスタム指示: すべてのカスタム指示ファイルが、優先順位ベースのフォールバックを使用する代わりに結合されるようになりました。
- 再設計されたヘッダー: ブランド化されたマスコットと合理化されたウェルカムメッセージを備えた新しい CLI ヘッダー。

### New ways to access Copilot CLI
- GitHub CLI ユーザーは、`gh copilot` を実行することで、GitHub Copilot CLI の使用をより簡単に開始できます。コマンドを初めて実行すると、Copilot CLI のインストールを促すプロンプトが表示され、それ以降は `gh copilot` を便利なエントリポイントとして使用できます。これは GitHub Actions でもシームレスに動作します。確認プロンプトなしでインストールが自動的に行われます。

### Share your feedback
- パッケージマネージャーでアップデート (`brew upgrade copilot-cli`、`winget upgrade GitHub.Copilot`) するか、`npm install -g @github/copilot@latest` を実行するか、自動アップデートに任せてください。
- Copilot CLI の公開リポジトリでディスカッションに参加してください。

## Key Changes
- 履歴フィルタリング: シェルモード履歴ナビゲーション (`!` プレフィックス) がプレフィックスでフィルタリングするようになりました。`!git` と入力して上矢印を押すと、以前の git コマンドのみを循環し、特定のコマンドをより迅速に見つけて再実行できます。
- よりクリーンな環境: Copilot は、Bash および PowerShell 履歴ファイルからシェルコマンドを除外し、シェル履歴をクリーンに保ちます。

## Impact / Who's Affected
- Advanced reasoning models GPT-5.2-Codex: コード生成と理解に最適化された最新の Codex モデルが利用可能になりました。
- `!git` と入力して上矢印を押すと、以前の git コマンドのみを循環し、特定のコマンドをより迅速に見つけて再実行できます。

## Caveats / Limitations
- Repository memory Copilot は、セッション間でコードベースに関する重要な事実を記憶できるようになりました。
- `!git` と入力して上矢印を押すと、以前の git コマンドのみを循環し、特定のコマンドをより迅速に見つけて再実行できます。

## Insights (derived from article language)
- アプローチについて合意したら、専用パネルで計画を確認し、Copilot に実装を開始するよう指示できます。

## Article Content (cleaned)
GitHub Copilot CLI は、ターミナル内でのエージェント AI アシスタンスの限界を押し広げ続けています。今週は、強力な新しい推論モデル、リアルタイムで会話を操れるインテリジェントなワークフロー機能、GitHub CLI とのより緊密な統合をもたらします。新機能は以下の通りです。


## [Plan mode](#plan-mode)


![A terminal showing the Copilot CLI interface in plan mode with text indicating that it's in plan mode.](https://github.com/user-attachments/assets/e196c826-d333-4622-954a-e844403daebe)


最もリクエストされた機能の 1 つがここにあります: **plan mode** は、Copilot が実装を開始する前に、共同計画エクスペリエンスを提供します。


**Shift + Tab** を押して、プランモードに出入りします。プランモードでは、Copilot がリクエストを分析し、スコープと要件を理解するための明確化質問をし、コードを書く前に構造化された実装計画を構築します。


エクスペリエンスは会話的です。Copilot は新しい `ask_user` ツールを使用して、フォローアップの質問を促し、機能スコープに関する仮定を確認し、設計の決定に関する入力を取得します。アプローチについて合意したら、専用パネルで計画を確認し、Copilot に実装を開始するよう指示できます。


![A terminal window where Copilot asks a clarifying question to the user and provides a list of possible options.](https://github.com/user-attachments/assets/b09388d5-8984-471e-a272-258ad0a84281)


これにより、次のことができます:


* コードが書かれる前に誤解を早期にキャッチします。
* 実装アプローチについて情報に基づいた意思決定を行います。
* 複雑なマルチステップタスクのコントロールを維持します。


## [Advanced reasoning models](#advanced-reasoning-models)


![The Copilot CLI interface presenting a list of options (Low, Medium, High, Extra High) for configuring the reasoning effort of GPT-5.2-Codex.](https://github.com/user-attachments/assets/561bdf3e-66b2-4c75-8b1d-1deecc605b8d)


* **GPT-5.2-Codex:** コード生成と理解に最適化された最新の Codex モデルが利用可能になりました。`/model` または `--model gpt-5.2-codex` で選択します。
* **設定可能な推論努力:** 拡張思考をサポートする GPT モデルの場合、プロンプトにモデルが適用する推論努力の量を設定できるようになりました。これにより、タスクに応じて応答速度と推論の深さのバランスを取ることができます。
* **推論の可視性を切り替え:** **Ctrl + T** を押して、生成中のモデルの推論ステップを表示または非表示にします。この設定はセッション間で持続するため、Copilot が複雑な問題にどのようにアプローチするかを常に確認できます。


## [Steer the conversation](#steer-the-conversation)


![An example of the experience for providing inline feedback on tool call rejection.](https://github.com/user-attachments/assets/ca6d6919-8c83-48ba-a8b2-166ca00fc66a)


* **追加のメッセージをキューに入れる:** Copilot が考えている間にインタラクションできるようになりました。フォローアップメッセージを送信して会話を別の方向に導いたり、Copilot が現在の応答を終えた後に処理する追加の指示をキューに入れたりできます。これにより、会話がより自然に感じられ、コントロールを維持できます。
* **拒否時のインラインフィードバック:** ツールの許可リクエストを拒否するときに、Copilot にインラインフィードバックを提供できるため、完全に停止することなくアプローチを適応させることができます。これにより、特定のアクションから Copilot を遠ざけたい場合に会話がより自然に流れます。


## [Background delegation](#background-delegation)


任意のプロンプトの前に `&` を付けて、クラウド内の GitHub Copilot コーディングエージェントに委任します (`/delegate` コマンドと同等)。これにより、Copilot が長いタスクを非同期で処理している間、ターミナルが他の作業に解放されます。


## [Automatic context management](#automatic-context-management)


* **自動コンパクション:** 会話がトークン制限の 95% に近づくと、Copilot はワークフローを中断することなくバックグラウンドで履歴を自動的に圧縮します。これにより、事実上無限のセッションが可能になります。
* **手動コントロール:** `/compact` を使用して、いつでも手動でコンテキストを圧縮します。気が変わった場合は **Escape** を押してキャンセルします。
* **使用状況の可視化:** `/context` コマンドは、コンテキストウィンドウがどのように使用されているかを理解できるように、詳細なトークン使用量の内訳を表示します。


## [Enhanced permissions experience](#enhanced-permissions-experience)


* **並列リクエストの承認:** **セッション用に承認** を選択すると、同じタイプの保留中の並列許可リクエストが自動承認され、複雑なマルチステップ操作中の中断が減ります。
* **便利なフラグ:** 新しい `--allow-all` および `--yolo` フラグは、Copilot を自由に実行することを信頼する場合に、すべての許可を一度に有効にします。


## [Code review](#code-review)


![A response from Copilot in the CLI in response to a review request, marking out five security issues and asking if the user wants to have Copilot fix them.](https://github.com/user-attachments/assets/a8d6c4e4-409e-4bb9-ba80-e31a19c7a898)


新しい `/review` コマンドは、CLI でコードの変更を直接分析します。ターミナルを離れることなく、ステージングされた変更またはステージングされていない変更に関するフィードバックを取得します。コミット前のクイックサニティチェックに最適です。


## [Repository memory](#repository-memory)


Copilot は、セッション間でコードベースに関する重要な事実を記憶できるようになりました。作業中、Copilot は学習する規約、パターン、設定を保存し、将来のセッションをより生産的にします。メモリストレージツールは、コーディング標準、プロジェクト構造の洞察、好みのアプローチなどのコンテキストをキャプチャします。Copilot のエージェントメモリ機能の詳細については、[Copilot メモリに関するエンジニアリングブログ記事](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/) をご覧ください。


## [Shell mode improvements](#shell-mode-improvements)


* **履歴フィルタリング:** シェルモード履歴ナビゲーション (`!` プレフィックス) がプレフィックスでフィルタリングするようになりました。`!git` と入力して上矢印を押すと、以前の git コマンドのみを循環し、特定のコマンドをより迅速に見つけて再実行できます。
* **よりクリーンな環境:** Copilot は、Bash および PowerShell 履歴ファイルからシェルコマンドを除外し、シェル履歴をクリーンに保ちます。


## [Developer quality-of-life](#developer-quality-of-life)


* **`/resume` コマンド:** ローカルおよびリモートの GitHub Copilot コーディングエージェントセッション間を簡単に切り替えます。
* **`/cd` エイリアス:** 作業ディレクトリを変更する `/cwd` の短縮形。
* **改善されたセッションイベント:** より簡潔で視覚的にクリーンなセッションメッセージ。
* **タブタイトル:** 現在の意図がターミナルのタブタイトルに表示されるようになりました。
* **カスタム指示:** すべてのカスタム指示ファイルが、優先順位ベースのフォールバックを使用する代わりに結合されるようになりました。
* **再設計されたヘッダー:** ブランド化されたマスコットと合理化されたウェルカムメッセージを備えた新しい CLI ヘッダー。


## [New ways to access Copilot CLI](#new-ways-to-access-copilot-cli)


GitHub CLI ユーザーは、`gh copilot` を実行することで、GitHub Copilot CLI の使用をより簡単に開始できます。コマンドを初めて実行すると、Copilot CLI のインストールを促すプロンプトが表示され、それ以降は `gh copilot` を便利なエントリポイントとして使用できます。これは GitHub Actions でもシームレスに動作します。確認プロンプトなしでインストールが自動的に行われます。


## [Share your feedback](#share-your-feedback)


パッケージマネージャーでアップデート (`brew upgrade copilot-cli`、`winget upgrade GitHub.Copilot`) するか、`npm install -g @github/copilot@latest` を実行するか、自動アップデートに任せてください。


[Copilot CLI の公開リポジトリ](https://github.com/github/copilot-cli) でディスカッションに参加してください。
