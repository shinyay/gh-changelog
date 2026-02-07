---
title: "VS Code v1.101 (2025年5月) 日本語詳細解説"
date: "2025-06-12"
version_ref: "v1_101"
source_url: "https://code.visualstudio.com/updates/v1_101"
lang: "ja"
---

# VS Code v1.101 (2025年5月) 日本語詳細解説

## リリース概要

VS Code v1.101（2025年5月リリース）は、Model Context Protocol（MCP）の大幅な機能拡充を中心とした重要なアップデートである。MCP にプロンプト・リソース・サンプリング・認証サポートが追加され、エージェント開発のワークフローが飛躍的に広がった。また、ツールセット機能によりチャットで使用するツールのグループ化・管理が可能になり、カスタムチャットモード（Preview）により独自のワークフロー構築が実現した。ソース管理では Copilot coding agent の統合が進み、VS Code 内からタスクの割り当て・追跡ができるようになった。エディタ体験では EditContext API のデフォルト有効化、セマンティック検索の挙動制御など、多方面で改善が行われている。

## 注目の新機能・変更点

1. **MCP プロンプトサポート**: MCP サーバーが定義したプロンプトをスラッシュコマンドとしてチャットで利用可能になった。再利用可能なスニペットやタスクの生成を効率化する。
2. **MCP リソースサポート**: MCP サーバーが提供するリソースをチャットコンテキストとして添付したり、ツール呼び出し結果を保存・ブラウズできるようになった。
3. **MCP 認証サポート**: 認証が必要な MCP サーバーへの接続がサポートされ、OAuth 認可フロー・デバイスコードフローに対応した。
4. **チャットツールセット**: 複数のツールをグループ化してツールセットとして定義・管理できるようになり、エージェントモードでの効率的なツール管理が実現した。
5. **カスタムチャットモード (Preview)**: Ask・Edit・Agent に加えて独自のチャットモードを定義でき、利用可能なツールや LLM への指示を個別にカスタマイズできる。
6. **Copilot coding agent 統合**: GitHub Pull Requests 拡張機能から Copilot coding agent にタスクを割り当て、進捗を追跡できるようになった。
7. **EditContext API デフォルト有効化**: エディタ入力が EditContext API ベースに切り替わり、IME 関連の多数のバグが修正された。
8. **セマンティック検索の挙動オプション (Preview)**: テキスト検索結果が空の場合に自動実行、または常に並列実行するなど、セマンティック検索のトリガー方法を設定で制御可能になった。
9. **ターミナルでの言語サーバーベース補完**: Python REPL セッションで Pylance によるエディタ同等の補完が利用可能になった。
10. **Electron 35 アップデート**: Chromium 134 / Node.js 22.15.1 への更新。`navigator` グローバルオブジェクトの導入に伴い、拡張機能の Web 環境検出に破壊的変更あり。

## セクション別詳細解説

### Chat

#### 概要

Chat セクションは v1.101 の最大の更新領域であり、MCP の全面的な機能拡充（プロンプト・リソース・サンプリング・認証・開発モード）に加え、ツールセット、カスタムチャットモード、UX 改善など多数の機能が追加された。エージェントモードの実用性が大幅に向上している。

#### 機能詳細

#### Chat tool sets

VS Code でツールセットを定義できるようになった。ツールセットは複数のツールをグループ化したもので、個々のツールと同様にエージェントモードで使用できる。関連するツールをまとめて管理し、一括で有効化・無効化が可能。

- **作成方法**: コマンドパレットから **Configure Tool Sets** > **Create new tool sets file** を実行
- ツールセットは JSON ファイルで定義し、含めるツール・説明・アイコンを指定する
- チャットで `#ツールセット名` のように `#` メンションで参照するか、ツールピッカーから選択して使用する
- Proposed API またはUI 経由で定義可能

```json
{
  "gh-news": {
    "tools": [
      "list_notifications",
      "dismiss_notification",
      "get_notification_details"
    ],
    "description": "Manage GH notification",
    "icon": "github-project"
  }
}
```

> 📷 [画像: チャットビューでのツールセット使用例](https://code.visualstudio.com/assets/updates/1_101/tool-set-gh.png)

#### MCP support for prompts

MCP のプロンプト機能がサポートされた。MCP サーバーが定義したプロンプトは、チャット内でスラッシュコマンド（`/mcp.サーバー名.プロンプト名`）としてアクセスできる。

- プロンプト変数にプレーンテキストやコマンド出力を含めることが可能
- サーバーが提供する場合、補完もサポートされる
- 再利用可能なスニペットやタスクをプロンプトとして定義し、効率的にワークフローを構築できる

> 🎬 [動画: MCP プロンプトの使用例 — AI でプロンプトを生成し、Gistpad MCP サーバーで保存して changelog エントリを生成](https://code.visualstudio.com/assets/updates/1_101/mcp-prompts.mp4)

#### MCP support for resources

MCP のリソース機能がサポートされた。リソーステンプレートにも対応している。

- MCP ツール呼び出しから返されたリソースはモデルで利用可能。**Save** ボタンやエクスプローラービューへのドラッグで保存できる
- **Add Context...** > **MCP Resources...** からリソースをチャットコンテキストとして添付可能
- **MCP: Browse Resources** コマンドでサーバー横断的にリソースをブラウズ・表示できる

> 🎬 [動画: Gistpad MCP サーバーからリソースをチャットに添付する例](https://code.visualstudio.com/assets/updates/1_101/mcp-resources.mp4)

#### MCP support for sampling (Experimental)

**[Experimental]** MCP のサンプリング機能がサポートされた。サンプリングにより、MCP サーバーがモデルに対してリクエストを送信できる。

- MCP サーバーが初めてサンプリングリクエストを行う際に確認が求められる
- MCP サーバーがアクセスできるモデルを設定可能
- **MCP: List Servers** でリクエストログを確認できる
- まだ予備的な段階であり、今後のイテレーションで拡張・改善予定

> 🎬 [動画: MCP サンプリングの使用例](https://code.visualstudio.com/assets/updates/1_101/mcp-sampling.mp4)

#### MCP support for auth

認証が必要な MCP サーバーへの接続がサポートされた。ユーザーアカウントを使用して認証済み MCP サーバーとやり取りできる。

- MCP 認可仕様のクライアント実装をサポート:
  - [2025-3-26 仕様](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization): MCP サーバーが認可サーバーとして動作
  - [Draft 仕様](https://modelcontextprotocol.io/specification/draft/basic/authorization): MCP サーバーがリソースサーバーとして動作
- GitHub / Entra を認可サーバーとして使用する場合、アカウントメニューから信頼済み MCP サーバーの管理が可能
- 動的クライアント登録を使用するサーバー（例: Linear）にも対応
- コード認可フローとデバイスコードフローの両方をサポート
- **Authentication: Remove Dynamic Authentication Providers** コマンドで動的クライアント登録のクリーンアップが可能

> 📷 [画像: 信頼済み MCP サーバーの管理オプション](https://code.visualstudio.com/assets/updates/1_101/manage-trusted-mcp.png)

> 📷 [画像: 信頼済み MCP サーバーの Quick Pick](https://code.visualstudio.com/assets/updates/1_101/manage-trusted-mcp-quick-pick.png)

> 📷 [画像: アカウント設定の Quick Pick](https://code.visualstudio.com/assets/updates/1_101/account-pref-quick-pick.png)

> 📷 [画像: Linear がアカウントメニューに表示される例](https://code.visualstudio.com/assets/updates/1_101/linear-account-menu.png)

#### MCP development mode

MCP サーバーの開発モードが導入された。サーバー設定に `dev` キーを追加することで有効化できる。

- `watch`: ファイル変更を監視して MCP サーバーを自動再起動するための glob パターン
- `debug`: デバッガーのセットアップを有効化。現在は `node` および `python` で起動された Node.js / Python サーバーのデバッグをサポート

```diff
{
  "servers": {
    "gistpad": {
      "command": "node",
      "args": ["build/index.js"],
+     "dev": {
+       "watch": "build/**/*.js",
+       "debug": { "type": "node" }
+     },
```

#### Chat UX improvements

チャットの UX が複数の観点で改善された。

- ユーザーメッセージと AI レスポンスの視覚的な区別が明確になった
- リクエストの取り消しがより視認しやすくなった。リクエストにホバーして `X` ボタンを選択するか、`workbench.action.chat.undoEdits` キーボードショートカットで取り消し可能
- チャット入力ボックスの添付ファイルのナビゲーションが改善された

> 🎬 [動画: 新しいチャット UI/UX — リクエストを削除してその時点以降の編集を取り消す](https://code.visualstudio.com/assets/updates/1_101/new-chat-ui-ux.mp4)

#### Apply edits more efficiently

ファイル編集時の 2 つのアプローチ（ファイル全体の書き換え / 複数の小さな編集）が状況に応じて適切に使い分けられるようになった。大きなファイルでは小さな編集アプローチが使われ、必要に応じて自動保存やスクイグル（波線エラー表示）が条件的に無効化される。

- **Keep** / **Undo** のキーバインドが統合された:
  - 個別の変更: `chatEditor.action.acceptHunk` / `chatEditor.action.undoHunk`
  - ファイル全体の変更: `chatEditor.action.accept` / `chatEditor.action.reject`
- 既存の編集コマンド（**Delete All Left** など）との競合が解消された

#### Implicit context

現在のファイルをチャットコンテキストに追加する方法が簡素化された。

- 以前の「目のアイコンのトグル」に代わり、現在のファイルが推奨コンテキスト項目として提示される
- 選択するだけでコンテキストに追加・削除が可能。`Shift+Tab, Enter` でキーボード操作も可能
- エージェントモードでは、現在のエディタのヒント（ファイル名とカーソル位置のみ、内容は含まない）が自動的に含まれる

> 🎬 [動画: 現在のエディタが暗黙的なコンテキストとして提案・添付される](https://code.visualstudio.com/assets/updates/1_101/implicit-context-flow.mp4)

#### Fix task configuration errors

タスクやプロブレムマッチャーの設定エラーに対して、**Fix with Github Copilot** アクションが提供されるようになった。設定ファイルにエラーがある場合に、迅速に修正を適用できる。

#### Custom chat modes (Preview)

**[Preview]** 独自のカスタムチャットモードを定義できるようになった。デフォルトの Ask・Edit・Agent に加えて、特定のワークフロー向けにカスタマイズされたモードを作成可能。

- **Chat: Configure Chat Modes** コマンドからモードを定義
- `*.chatprompt.md` ファイルで指示内容と利用可能なツールを指定
- チャットビューのモードドロップダウンから選択して使用

利用例として、コードベースへの読み取り専用アクセスのみを持つ「Planning」モードなど、目的に応じた制限付きモードの作成が可能。

```md
---
description: Generate an implementation plan for new features or refactoring existing code.
tools: ['codebase', 'fetch', 'findTestFiles', 'githubRepo', 'search', 'usages']
---
# Planning mode instructions
You are in planning mode. Your task is to generate an implementation plan...
```

> 📷 [画像: チャットビューでカスタムチャットモードが選択されている](https://code.visualstudio.com/assets/updates/1_101/custom-chat-mode-view.png)

#### Task diagnostic awareness

チャットエージェントがタスクを実行する際、プロブレムマッチャーによって識別されたエラーや警告を認識できるようになった。この診断コンテキストにより、エージェントは発生した問題に対してより的確に対応できる。

#### Terminal cwd context

エージェントモードでターミナルを開いた際、シェル統合がアクティブであれば、チャットエージェントが現在の作業ディレクトリ（cwd）を認識するようになった。より正確でコンテキストを考慮したコマンドサポートが可能になる。

#### Floating window improvements

チャットセッションをフローティングウィンドウに移動した際、タイトルバーに 2 つの新しいアクションが追加された。

- 元の VS Code ウィンドウにチャットをドッキング
- フローティングウィンドウで新しいチャットセッションを開始

> 📷 [画像: フローティングウィンドウのチャットビュー - Dock と New Chat ボタン](https://code.visualstudio.com/assets/updates/1_101/chat-floating.png)

#### Fetch tool confirmation

Fetch ツールの確認ダイアログに、プロンプトインジェクションの可能性に関する警告メッセージが追加された。Web ページからの情報取得時のセキュリティリスクについてユーザーに通知する。

> 📷 [画像: Fetch ツールのプロンプトインジェクション警告](https://code.visualstudio.com/assets/updates/1_101/fetch-warning.png)

#### Customize more built-in tools

エージェントモードまたはカスタムモードで、すべてのビルトインツールを有効・無効に設定できるようになった。

- `editFiles` を無効化してファイル直接編集を禁止
- `runCommands` を無効化してターミナルコマンド実行を禁止
- **Configure Tools** ボタンからツールピッカーを開いて設定

一部のエントリは複数ツールをグループ化したツールセットであり、例えば `editFiles` はモデルファミリーごとのテキストファイル・ノートブック編集ツールをまとめている。

> 📷 [画像: ツールピッカーで editFiles が無効化されている](https://code.visualstudio.com/assets/updates/1_101/built-in-toolsets.png)

#### Send elements to chat (Experimental)

**[Experimental]** 前回のマイルストーンで導入された Simple Browser からの Web 要素選択機能が、[Live Preview 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server) にも対応した。HTML ファイルからライブサーバーを起動して Web 要素をチャットに送信できる。

> 📷 [画像: Live Preview 拡張機能での Web 要素選択オーバーレイ](https://code.visualstudio.com/assets/updates/1_101/live-preview-select-web-elements.png)

### Accessibility

#### 概要

アクセシビリティ関連では、チャットでのユーザーアクション要求を通知するサウンド、コードアクションの新しいサウンド、エージェントモードの確認ダイアログ情報の改善が行われた。

#### 機能詳細

#### User action required sound

チャットがユーザーアクションを必要とする場合にアクセシビリティシグナルが発信されるようになった。オプトイン方式で、`accessibility.signals.chatUserActionRequired` 設定で制御する。

#### New code action sounds

コードアクションに関する 2 つの新しいサウンドが導入された。

- コードアクションがトリガーされた時: `accessibility.signals.codeActionTriggered`
- コードアクションが適用された時: `accessibility.signals.codeActionApplied`

#### Agent mode accessibility improvements

アクセシブルビューに確認ダイアログの詳細情報が含まれるようになった。過去のツール実行、現在のツール実行、および保留中の確認情報（使用される入力を含む）がカバーされる。確認ダイアログが表示された際、アクションのタイトルが対応するコードブロックの ARIA ラベル、レスポンスの ARIA ラベル、およびライブアラートに含まれ、スクリーンリーダーユーザーにより良いコンテキストを提供する。

### Editor Experience

#### 概要

エディタ体験では、EditContext API のデフォルト有効化、`window.menuStyle` 設定の追加、セマンティック検索や AI 検索の挙動制御オプション、非公開拡張機能の警告表示などが追加された。Windows PowerShell でのシェル環境ディスカバリも実装されている。

#### 機能詳細

#### Find as you type

`editor.find.findOnType` 設定により、入力中に即座に検索する動作を制御できるようになった。デフォルトは `true`（従来通り入力中に検索）だが、`false` に設定すると Enter キーを押した後にのみ検索が実行される。

#### Custom menus with native window title bar

`window.menuStyle` 設定により、メニューバーやコンテキストメニューのスタイルを指定できるようになった（Windows / Linux ではメニューバーとコンテキストメニュー、macOS ではコンテキストメニューに適用）。

- `native`: OS でレンダリング
- `custom`: VS Code でレンダリング
- `inherit`: `window.titleBarStyle` の設定に合わせる（ネイティブタイトルバーとカスタムメニューバーの組み合わせが可能）

#### Linux native window context menu

カスタムタイトルバーでアプリケーションアイコンを右クリックした際に、ネイティブウィンドウコンテキストメニューがサポートされるようになった。

> 📷 [画像: カスタムタイトルバー上のネイティブウィンドウコンテキストメニュー](https://code.visualstudio.com/assets/updates/1_101/linux-os-title-menu.png)

#### Process explorer web support

プロセスエクスプローラーがワークベンチのフローティングウィンドウインフラストラクチャに変換された。これにより、リモート接続時（例: Codespaces）の Web 環境でもプロセスエクスプローラーが利用可能になった。

> 📷 [画像: フローティングウィンドウ内の VS Code プロセスエクスプローラー](https://code.visualstudio.com/assets/updates/1_101/process-explorer.png)

#### Windows shell environment discovery

Windows の PowerShell でシェル環境ディスカバリが実装された。VS Code が PowerShell プロファイルで設定された環境（Node.js のバージョンマネージャーによる PATH 更新など）を継承するようになった。

#### Unpublished extension warning

インストール済みの拡張機能が Marketplace で利用できなくなった（非公開化または削除された）場合、警告インジケーターが表示されるようになった。問題のある拡張機能の早期発見に役立つ。

> 📷 [画像: 拡張機能に Marketplace で利用不可を示す警告インジケーターが表示されている](https://code.visualstudio.com/assets/updates/1_101/pulled-extension.png)

#### Settings search suggestions (Preview)

**[Preview]** `workbench.settings.showAISearchToggle` 設定を有効にすると、設定エディタに AI 検索トグルが追加される。文字列マッチングではなく、意味的に類似した結果を検索できる。例えば「increase text size」で検索すると `editor.fontSize` 設定が見つかる。

> 🎬 [動画: 設定エディタでの AI 検索 — 「increase text size」で editor.fontSize が見つかる](https://code.visualstudio.com/assets/updates/1_101/settings-editor-ai-search.mp4)

#### Search keyword suggestions (Preview)

**[Preview]** 前回のマイルストーンで導入された検索ビューのキーワード候補のパフォーマンスが大幅に改善され、約 5 倍高速になった。設定名も `github.copilot.chat.search.keywordSuggestions` から `search.searchView.keywordSuggestions` に変更され、VS Code コアに移行された。

#### Semantic search behavior options (Preview)

**[Preview]** `search.searchView.semanticSearchBehavior` 設定により、セマンティック検索のトリガー方法を制御できるようになった。

- `manual`（デフォルト）: UI から手動でトリガーした場合のみ実行（`search.action.searchWithAI`）
- `runOnEmpty`: テキスト検索が結果なしの場合に自動実行
- `auto`: すべての検索クエリで常にテキスト検索と並列実行

#### Edit Context

**[GA]** `editor.editContext` 設定が Stable でデフォルト有効化された。エディタの入力が [EditContext API](https://developer.mozilla.org/en-US/docs/Web/API/EditContext_API) ベースになり、特に IME 体験に関連する多数のバグが修正された。今後、より汎用的で堅牢な入力体験への道を開くものとなる。

### Code Editing

#### 概要

コード編集では、Next Edit Suggestions（NES）のインポート提案が Python にも対応し、Tab キーによる連続承認フローが改善された。

#### 機能詳細

#### NES import suggestions

`github.copilot.nextEditSuggestions.fixes` 設定に関連して、NES のインポート提案がTypeScript / JavaScript に加えて Python にも対応した。不足しているインポート文を自動的に提案する機能の精度と信頼性が向上している。

- NES は VS Code Insiders ユーザー全員に有効化済み
- Stable ユーザーには 6 月中に段階的にデフォルト有効化される予定

> 📷 [画像: NES がインポート文を提案している](https://code.visualstudio.com/assets/updates/1_100/nes-import.png)

#### NES acceptance flow

NES の承認フローが改善され、キーボードナビゲーションがよりシームレスになった。提案を承認した後、再度入力を始めるまでは、単一の `Tab` キーで連続して次の提案を承認できる。入力を始めた場合は、最初の `Tab` でカーソルを次の提案に移動し、その後に承認する形になる。

### Notebooks

#### 概要

Notebooks セクションでは、エージェントによるセル実行のフォローモード、ノートブック設定ツール、長時間ワークフロー対応、セル実行確認時のプレビューなど、エージェントモードとの連携が大幅に強化された。

#### 機能詳細

#### Follow mode for agent cell execution

`github.copilot.chat.notebook.followCellExecution.enabled` 設定により、エージェントが実行中のセルにノートブックビューが自動スクロールするフォローモードが利用可能になった。

- エージェントがセル実行ツールを使用すると、ノートブックツールバーにピンアイコンが表示される
- エージェント応答中にフォローモードをトグルでき、特定のコード部分を確認したい場合にオフにできる
- 再度トグルオンすると、次の実行からフォローが再開される

> 🎬 [動画: フォローモードが有効な状態でエージェントがノートブックのセルを実行し、自動スクロールする](https://code.visualstudio.com/assets/updates/1_101/notebook-follow-mode.mp4)

#### Notebook tools for agent mode

##### Configure notebook

Jupyter 拡張機能がノートブックのカーネル設定ツールを提供するようになった。カーネルが選択済みか確認し、使用可能な状態にするツールで、必要に応じて仮想環境の作成プロセスを案内するか、既存の Python 環境の選択を促す。エージェントモードでのセル実行の前提条件を自動化し、ユーザー操作を最小化する。

> 🎬 [動画: AI が Python 環境を構成し、依存関係をインストールして最終的にノートブックのセルを実行する](https://code.visualstudio.com/assets/updates/1_101/notebook-tools.mp4)

##### Long running agent workflows

エージェントが内部的なノートブックサマリーツールにアクセスでき、正確なコンテキストを維持できるようになった。コンテキストが大きくなりすぎた場合の会話履歴の要約にもこのサマリーが含まれ、複雑な操作を通じてエージェントの継続性を確保する。

##### Cell preview in run confirmation

エージェントがセル実行の確認を求める際、セルのコードスニペットが表示されるようになった。チャットビュー内のセルリンクからノートブック内のセルに直接ナビゲートすることも可能。

> 🎬 [動画: AI がセル実行の確認を求め、セルへのリンクとコンテンツのプレビューが表示される](https://code.visualstudio.com/assets/updates/1_101/run-cell-confirmation.mp4)

### Source Control

#### 概要

ソース管理では、Copilot coding agent との VS Code 内統合、ソース管理グラフビューでのファイル表示、履歴アイテムのチャットコンテキストへの追加が実現した。

#### 機能詳細

#### Copilot coding agent integration

GitHub Pull Requests 拡張機能が拡張され、Copilot coding agent のタスク割り当て・追跡が VS Code 内から可能になった。

- **Assign to Copilot**: PR ビューまたは Issue ビューから Copilot にタスクを割り当て
- **Copilot on My Behalf** PR クエリ: Copilot が作業中の全 PR を一覧表示
- **PR ビュー**: Copilot coding agent のステータス確認とブラウザでのセッション詳細表示

> 📷 [画像: GitHub Pull Requests ビューでの Copilot への割り当てアクションと Copilot 作業クエリ](https://code.visualstudio.com/assets/updates/1_101/github-pull-request-coding-agent.png)

#### Source control history item details

要望の多かった機能として、ソース管理グラフビューでアイテムを選択するとそのリソース（変更されたファイル）が表示されるようになった。

- ツリービューまたはリストビューで表示（`...` メニューから切り替え）
- ホバー時の **Open Changes** アクションでマルチファイル diff エディタを開く
- 個別リソース選択でそのリソースの diff エディタを開く
- **Open File** アクションで特定バージョンのファイルを開く

> 🎬 [動画: ソース管理グラフビューでコミットのファイルを表示し、変更の diff エディタを開く](https://code.visualstudio.com/assets/updates/1_101/source-control-graph-view-resources.mp4)

#### Add history item to chat context

ソース管理の履歴アイテム（コミットや PR）をチャットリクエストのコンテキストとして追加できるようになった。

- **Add Context** > **Source Control** から選択
- ソース管理グラフで右クリック > **Copilot** > **Add History Item to Chat** でも追加可能

> 📷 [画像: チャット入力ボックスに履歴アイテムがコンテキストとして追加されている](https://code.visualstudio.com/assets/updates/1_101/chat-context-source-control-commit.png)

### Tasks

#### 概要

タスクに `instancePolicy` プロパティが追加され、タスクが `instanceLimit` に達した際の動作を制御できるようになった。

#### 機能詳細

#### Instance policy

タスクの `runOptions` に `instancePolicy` プロパティが追加された。タスクがインスタンス上限に達した際の動作を定義する。

- `prompt`（デフォルト）: プロンプトで確認
- `silent`: サイレントに処理
- `terminateNewest`: 最も新しいインスタンスを終了
- `terminateOldest`: 最も古いインスタンスを終了
- `warn`: 警告を表示

> 📷 [画像: tasks.json での instancePolicy の設定例](https://code.visualstudio.com/assets/updates/1_101/instancePolicy.png)

### Terminal

#### 概要

ターミナルで言語サーバーベースの補完が Python REPL セッションで利用可能になった。エディタで提供される同等の補完機能をターミナル内で利用できる。

#### 機能詳細

#### Language server based terminal suggest

Python REPL セッションで Pylance による言語サーバー補完が利用可能になった。エディタと同じ品質の言語補完がターミナル内で動作する。まず Python のサポートから開始し、将来的に他の言語への拡張を予定している。

有効化に必要な設定:

- `terminal.integrated.shellIntegration.enabled`: `true`
- `python.terminal.shellIntegration.enabled`: `true`
- `terminal.integrated.suggest.enabled`: `true`
- `python.analysis.supportAllPythonDocuments`: `true`

> 🎬 [動画: ターミナルの Python REPL で LSP 補完が動作している](https://code.visualstudio.com/assets/updates/1_101/lsp_completions.mp4)

### Remote Development

#### 概要

Remote Development 拡張機能パックに SSH 事前接続スクリプトとリモートエクスプローラーの改善が含まれている。

#### 機能詳細

[Remote Development リリースノート](https://github.com/microsoft/vscode-docs/blob/main/remote-release-notes/v1_101.md)で詳細を確認できる。主なハイライト:

- SSH 事前接続スクリプト
- リモートエクスプローラーの改善

### Contributions to extensions

#### 概要

Python 拡張機能にチャットツールが統合され、プロジェクトテンプレートからの作成機能が追加された。GitHub Pull Requests 拡張機能では通知ビューや Copilot coding agent 連携が強化されている。

#### 機能詳細

#### Python

##### Python chat tools

Python 拡張機能に以下のチャットツールが追加された:
- **Get information for a Python Environment**: Python 環境情報の取得
- **Get executable information for a Python Environment**: 実行可能ファイル情報の取得
- **Install Python Package**: パッケージのインストール
- **Configure Python Environment**: Python 環境の設定

`#getPythonEnvironmentInfo` や `#installPythonPackage` でプロンプトから直接参照するか、エージェントモードで自動的に呼び出される。以前 Python Environments 拡張機能（プレビュー）にあったツールが Python 拡張機能本体に移行されたため、Python 拡張機能をインストールしているすべてのユーザーが利用可能。

> 🎬 [動画: エージェントモードでモデルが暗黙的に Python ツールを呼び出す](https://code.visualstudio.com/assets/updates/1_101/python-tools.mp4)

##### Create a project from a template

Python Environments 拡張機能でプロジェクトテンプレートからの作成がサポートされた。**Python Envs: Create Project from Template** コマンドでパッケージまたはスクリプトの作成を選択できる。

- **パッケージ作成**: パッケージ名を指定して仮想環境を作成し、テストフォルダ、`pyproject.toml`、`dev-requirements.txt`、`__main__.py`、`__init__.py` を含むスキャフォルドされたプロジェクトを生成
- **スクリプト作成**: 指定した名前の新しい Python ファイルとボイラープレートコードを作成

##### PyEnv and Poetry support

Python Environments 拡張機能に `pyenv`（環境管理）と `poetry`（パッケージおよび環境管理）のサポートが追加された。

#### GitHub Pull Requests

GitHub Pull Requests 拡張機能の主な更新:

- プライベートリポジトリのコメントに含まれる画像が PR ファイルコメントに表示されるようになった
- 「Notifications」ビューがデフォルトで表示（折りたたまれた状態）
- タイムラインの Issue / PR リンクがブラウザではなく VS Code で開かれるようになった
- 「Assigned to Me」クエリが削除され、Copilot を持つリポジトリでは「Copilot on My Behalf」クエリが追加
- Copilot の「start working」「stop working」「View Session」がタイムラインに表示

## 設定項目まとめ

### Chat

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| — | ツールセットは JSON ファイルで直接定義 | — | GA |

### Accessibility

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `accessibility.signals.chatUserActionRequired` | チャットでユーザーアクション要求時のサウンド | — | GA (opt-in) |
| `accessibility.signals.codeActionTriggered` | コードアクションがトリガーされた時のサウンド | — | GA |
| `accessibility.signals.codeActionApplied` | コードアクションが適用された時のサウンド | — | GA |

### Editor Experience

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `editor.find.findOnType` | 入力中に即座に検索するか | `true` | GA |
| `window.menuStyle` | メニューバー / コンテキストメニューのスタイル | — | GA |
| `workbench.settings.showAISearchToggle` | 設定エディタの AI 検索トグルを表示 | — | Preview |
| `search.searchView.keywordSuggestions` | 検索ビューのキーワード候補 | — | Preview |
| `search.searchView.semanticSearchBehavior` | セマンティック検索のトリガー方法 | `manual` | Preview |
| `editor.editContext` | エディタ入力に EditContext API を使用 | `true` | GA |

### Code Editing

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `github.copilot.nextEditSuggestions.fixes` | NES インポート提案 | — | GA (段階的有効化) |

### Notebooks

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `github.copilot.chat.notebook.followCellExecution.enabled` | エージェントセル実行時のフォローモード | — | GA |

### Terminal

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `terminal.integrated.shellIntegration.enabled` | ターミナルのシェル統合 | `true` | GA |
| `python.terminal.shellIntegration.enabled` | Python ターミナルのシェル統合 | — | GA |
| `terminal.integrated.suggest.enabled` | ターミナルの補完提案を有効化 | — | GA |
| `python.analysis.supportAllPythonDocuments` | すべての Python ドキュメントの解析サポート | — | GA |

### Extension Authoring

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `extensions.supportNodeGlobalNavigator` | Node.js の navigator グローバルオブジェクトのポリフィル | `false`（ポリフィル有効） | GA |

## Breaking Changes / 非推奨化

### Web environment detection（`navigator` グローバルオブジェクト）

- **何が変わったか**: Electron 35 アップデートにより Node.js が v22 に更新され、デスクトップとリモートの拡張機能ホストに `navigator` グローバルオブジェクトが導入された。
- **影響を受けるユーザー**: `navigator` オブジェクトの存在を Web 環境の検出に使用している拡張機能の開発者。
- **対処法**:
  1. 拡張機能ホストログで `PendingMigrationError` を確認
  2. `typeof navigator === 'object'` のようなチェックを `typeof process === 'object' && process.versions.node` に移行
  3. `extensions.supportNodeGlobalNavigator` 設定を有効化して動作を確認
  4. 現在は `extensions.supportNodeGlobalNavigator` がデフォルト無効（ポリフィルが有効）だが、将来的にデフォルト有効に変更される可能性あり

## 開発者・拡張機能作成者向け

### MCP extension APIs

拡張機能から MCP サーバーのコレクションを公開できるようになった。MCP サーバーを拡張機能にバンドルしたり、他のソースから動的に MCP サーバーを検出する拡張機能を構築できる。

- [MCP 拡張機能開発ガイド](https://code.visualstudio.com/api/extension-guides/mcp)
- [MCP 拡張機能サンプル](https://github.com/microsoft/vscode-extension-samples/blob/main/mcp-extension-sample)

### Secret scanning when packaging extensions

VSCE が拡張機能パッケージング時にシークレットスキャンを実行するようになった。API キー、トークン、認証情報、`.env` ファイルなどの潜在的なシークレットが検出された場合、パッケージングプロセスでエラーが表示される。

- バイパスオプション: `--allow-package-secrets <secret_type>` または `--allow-package-env-file` フラグ

### Web environment detection

⚠️ **Breaking change** — 上記「Breaking Changes / 非推奨化」セクションを参照。

### Proposed API: Authentication Providers — Supported Authorization Servers for MCP

> ⚠️ この API はプロポーザル段階であり、今後変更または削除される可能性があります。
> プロポーザルファイル: `vscode.proposed.authIssuers.d.ts`

`AuthenticationProvider` が関連する認可サーバーを宣言できるようになる API プロポーザル。現在は MCP 認証で活用されている。

- `authorizationServerGlobs` プロパティで認可サーバーの URL パターンを拡張機能の `package.json` で宣言
- 一致するリクエストが来ると拡張機能がアクティベートされる
- `registerAuthenticationProvider` 時に `supportedAuthorizationServers` を指定する必要がある
- GitHub Authentication Provider の例:

```json
{
  "label": "GitHub",
  "id": "github",
  "authorizationServerGlobs": [
    "https://github.com/login/oauth"
  ]
}
```

```ts
vscode.authentication.registerAuthenticationProvider(
  type,
  this._githubServer.friendlyName,
  this,
  {
    supportsMultipleAccounts: true,
    supportedAuthorizationServers: [
      ghesUri ?? vscode.Uri.parse('https://github.com/login/oauth')
    ]
  }
);
```

- Microsoft Authentication Provider ではテナントに基づくワイルドカードパターンを使用

フィードバックは [GitHub issue #248775](https://github.com/microsoft/vscode/issues/248775) で受付中。

## エンジニアリング・基盤改善

### Electron 35 update

Stable リリースに Electron 35 アップデートが提供された。Chromium 134.0.6998.205 と Node.js 22.15.1 を含む。Insiders ビルドでのセルフホストと早期フィードバックに感謝を述べている。

### Adopting ESM in a real-world extension

前回のマイルストーンで発表された JavaScript モジュール（ESM）のサポートを、[GitHub Issue Notebooks](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-github-issue-notebooks) 拡張機能で実際に採用した。この拡張機能は NodeJS 拡張機能ホスト（ESM サポートあり）と Web Worker 拡張機能ホスト（ESM サポートなし）の両方で動作するため、より複雑なバンドラー設定が必要であった。[esbuild 設定](https://github.com/microsoft/vscode-github-issue-notebooks/blob/main/esbuild.mjs)を参考にできる。

## Notable fixes

- [vscode#250077](https://github.com/microsoft/vscode/issues/250077) — Tree-Sitter ベースのシンタックスハイライトがモデルサービスに依存する問題を修正

## コミュニティ貢献

多くの外部コントリビューターによる貢献が行われた。特に影響の大きいものをピックアップする:

- **[@alpalla](https://github.com/alpalla)**: タスクの `instancePolicy` を `runOptions` に追加 ([PR #117129](https://github.com/microsoft/vscode/pull/117129))
- **[@eronnen](https://github.com/eronnen)**: デバッグコンソールの最大行数を設定可能に ([PR #245915](https://github.com/microsoft/vscode/pull/245915))、ログの tmLanguage 更新、ディスアセンブリビューの改善（複数 PR）
- **[@gabritto](https://github.com/gabritto)**: TypeScript のホバー表示の最大長設定を追加 ([PR #248181](https://github.com/microsoft/vscode/pull/248181))
- **[@hickford](https://github.com/hickford)**: ワードラップに関係なくアクティブ行番号を正しくハイライト ([PR #240029](https://github.com/microsoft/vscode/pull/240029))
- **[@dylanchu](https://github.com/dylanchu)**: TerminalTaskSystem に nushell サポートを追加 ([PR #238440](https://github.com/microsoft/vscode/pull/238440))
- **[@mawosoft](https://github.com/mawosoft)**: strict モード有効時の PowerShell シェル統合を修正 ([PR #248625](https://github.com/microsoft/vscode/pull/248625))
- **[@joyceerhl](https://github.com/joyceerhl)**: チャット添付ウィジェットのリファクタリング、MCP ツール確認の修正など複数の改善
- **[@imfing](https://github.com/imfing)**: DynamicAuthProvider の認可 URL にスコープパラメータを条件付きで追加 ([PR #250084](https://github.com/microsoft/vscode/pull/250084))
- **[@rgant](https://github.com/rgant)**: CSS 言語サービスに `oklab` / `oklch` カラー関数のサポートを追加 ([PR #436](https://github.com/microsoft/vscode-css-languageservice/pull/436))

## まとめと所感

VS Code v1.101 は MCP プロトコルのフル機能実装（プロンプト・リソース・サンプリング・認証）を中心に、エージェント開発のエコシステムが一段と成熟したリリースである。ツールセットとカスタムチャットモードにより、チームごとのワークフローに合わせた柔軟な構成が可能になった点は実務上大きな恩恵がある。Copilot coding agent の VS Code 内統合も着実に進んでおり、PR ベースのタスク管理がエディタから離れることなく完結できるようになった。EditContext API のデフォルト有効化は IME ユーザーにとって待望の改善であり、日本語入力の安定性向上が期待できる。拡張機能開発者には `navigator` グローバルオブジェクトの破壊的変更への対応が必要であり、早めの移行が推奨される。
