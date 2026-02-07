---
title: "VS Code v1.100 (2025年4月) 日本語詳細解説"
date: "2025-05-08"
version_ref: "v1_100"
source_url: "https://code.visualstudio.com/updates/v1_100"
lang: "ja"
---

# VS Code v1.100 (2025年4月) 日本語詳細解説

## リリース概要

VS Code v1.100（2025年4月リリース）は、カスタムインストラクションと再利用可能なプロンプトファイルの正式導入を中心とした、AI 支援開発の基盤を大幅に強化するアップデートである。エージェントモードでの編集速度が向上し、プロンプトキャッシングによる応答高速化も実現した。MCP では Streamable HTTP トランスポートと画像出力のサポートが追加され、プロトコルの対応範囲が拡大した。エディタ体験ではフローティングウィンドウの Compact / Always-on-top モード、ステージ済み変更のクイック diff デコレーション、Next Edit Suggestions（NES）のデフォルト有効化など、日常のワークフローを改善する機能が多数導入されている。

## 注目の新機能・変更点

1. **インストラクション / プロンプトファイル**: `.instructions.md`（カスタムルール）と `.prompt.md`（再利用可能なチャットリクエスト）の 2 つのファイル形式が整理・統合され、AI 体験のカスタマイズが容易になった。
2. **エージェントモード編集の高速化**: OpenAI の apply patch 形式（GPT 4.1 / o4-mini）と Anthropic の replace string ツール（Claude Sonnet 3.7 / 3.5）をサポートし、大きなファイルでの編集が大幅に高速化された。
3. **会話要約とプロンプトキャッシング**: エージェントモードのプロンプト構築がプロンプトキャッシングに最適化され、繰り返しリクエストの応答が高速化された。
4. **MCP Streamable HTTP サポート**: MCP サーバーの新しい Streamable HTTP トランスポートがサポートされ、既存 SSE サーバーとの後方互換性も確保されている。
5. **フローティングウィンドウの Compact / Always-on-top モード**: フローティングウィンドウに Compact モード（UI 要素を非表示にして省スペース化）と Always-on-top モード（常に最前面表示）が追加された。
6. **ステージ済み変更のクイック diff デコレーション**: エディタ上でステージ済みの変更を直接確認できるようになり、Source Control ビューを開かずに変更状態を把握できる。
7. **Next Edit Suggestions (NES) デフォルト有効化**: NES が VS Code Insiders でデフォルト有効化され、Stable にも段階的に展開中。新しいモデルにより、より高速で文脈に即した提案が可能になった。
8. **`#githubRepo` ツール**: エディタで開いていない GitHub リポジトリのコードスニペットをチャットから検索できるようになった。
9. **Inline chat V2 (Preview)**: インラインチャットが刷新され、チャット編集と同じロジックを使用することでコンテキスト活用とコード編集戦略が改善された。
10. **Linux での拡張機能署名検証の必須化**: 拡張機能の署名検証が全プラットフォーム（Windows / macOS / Linux）で必須になり、セキュリティが強化された。

## セクション別詳細解説

### Chat

#### 概要

Chat セクションは v1.100 最大の更新領域であり、インストラクション / プロンプトファイルの統合、エージェントモード編集の高速化、`#githubRepo` / `#extensions` ツール、MCP の Streamable HTTP / 画像出力サポート、Inline chat V2、UI 要素のチャット送信など、幅広い機能追加・改善が行われた。

#### 機能詳細

#### Prompt and instructions files

VS Code の AI 体験をカスタマイズするための 2 つのファイル形式が統合・整理された。

##### Instructions files

`chat.instructionsFilesLocations` 設定に関連する機能。インストラクションファイル（`.instructions.md`）はコードスタイルルールやフレームワーク指定など、AI モデルへの共通ガイドラインをMarkdown で記述する。単独のチャットリクエストではなく、リクエストに付加するコンテキストとして機能する。

- ユーザーデータフォルダまたはワークスペースに配置可能
- **手動添付**: **Add Context** > **Instructions...** またはコマンドパレットから **Chat: Attach Instructions...**
- **自動添付**: YAML Front Matter の `applyTo` ヘッダーに glob パターンを指定すると、一致するファイルがリクエストに含まれる場合に自動的に添付される

```md
---
applyTo: '**/*.ts'
---
Place curly braces on separate lines for multi-line blocks:
if (condition)
{
    doSomething();
}
```

- **Chat: New Instructions File...** コマンドで新規作成
- ユーザーデータフォルダに作成したファイルは Settings Sync で複数マシン間で同期可能（**Prompts and Instructions** オプションを有効にする）

##### Prompt files

`chat.promptFilesLocations` 設定に関連する機能。プロンプトファイル（`.prompt.md`）はプロンプトテキスト・チャットモード・使用するツールを含む、スタンドアロンの完全なチャットリクエストを定義する。共通タスクの再利用に有用。

- ユーザーデータフォルダまたはワークスペースに配置可能
- 実行方法:
  - チャット入力フィールドで `/` + プロンプトファイル名
  - エディタで開いて Play ボタンを押す
  - **Chat: Run Prompt File...** コマンド
- YAML Front Matter で `mode`（`ask` / `edit` / `agent`）と `tools` を指定可能

```md
---
mode: 'agent'
tools: ['getCurrentMilestone', 'getReleaseFeatures', 'file_search', 'semantic_search', 'read_file', 'insert_edit_into_file', 'create_file', 'replace_string_in_file', 'fetch_webpage', 'vscode_search_extensions_internal']
---
Generate release notes for the features I worked in the current release...
```

> 📷 [画像: スラッシュコマンドでプロンプトを実行](https://code.visualstudio.com/assets/updates/1_100/run-prompt-as-slash-command.png)

> 📷 [画像: エディタの Play ボタンからプロンプトを実行](https://code.visualstudio.com/assets/updates/1_100/run-prompt-from-play-button.png)

##### Improvements and notes

- インストラクション / プロンプトファイルが独自の言語 ID を持つようになった（「Prompt」「Instructions」）。未保存のドキュメントを一時的なプロンプトファイルとして使用可能
- **Chat: Use Prompt** コマンドが **Chat: Run Prompt** にリネームされ、選択したプロンプトを即時実行するようになった
- 両ファイル形式で `description` メタデータをサポート。将来的に `applyTo` と組み合わせた自動インクルードのルールに使用予定

#### Faster agent mode edits

エージェントモードの編集が大幅に高速化された。

- **OpenAI**: apply patch 編集フォーマット（GPT 4.1 / o4-mini）をサポート。VS Code Insiders でデフォルト有効、Stable にも段階的展開中
- **Anthropic**: replace string ツール（Claude Sonnet 3.7 / 3.5）をサポート。全ユーザーに Stable / Insiders 両方で利用可能
- 特に大きなファイルで顕著な速度向上

#### Base model in chat

GPT-4.1 がチャットのデフォルトベースモデルとして段階的に展開中。モデルスイッチャーからいつでも別のモデルに変更可能。

#### Search code of a GitHub repository with the `#githubRepo` tool

`#githubRepo` ツールにより、エディタで開いていない GitHub リポジトリのコードスニペットをチャットから検索できるようになった。

- `user/repo` 形式で対象リポジトリを指定（例: `#githubRepo microsoft/vscode`）
- カスタムインストラクションでこのツールの使用方法をヒントとして設定可能
- 現在作業中のリポジトリについては `#codebase` ツールを使用
- Issue / PR の操作には [GitHub MCP server](https://github.com/github/github-mcp-server) を使用

```md
---
applyTo: '**'
---
Use the `#githubRepo` tool with `microsoft/vscode` to find relevant code snippets in the VS Code codebase.
Use the `#githubRepo` tool with `microsoft/typescript` to answer questions about how TypeScript is implemented.
```

> 📷 [画像: #githubRepo ツールをエージェントモードでインストラクションファイルのヒントと共に使用](https://code.visualstudio.com/assets/updates/1_100/github-repo-tool-example.png)

#### Find Marketplace extensions with the extensions tool

`#extensions` ツールにより、チャットから Marketplace の拡張機能を検索できるようになった。プロンプトに基づいて自動的に呼び出されるか、`#extensions` で明示的に参照可能。検索結果からの直接インストールにも対応。

> 🎬 [動画: extensions ツールで人気の Java 拡張機能を表示](https://code.visualstudio.com/assets/updates/1_100/extensions-agent-tool.mp4)

#### Improvements to the web page fetch tool

Fetch ツール（`#fetch`）に大幅な改善が加えられた。

- **ページ全体をコンテキストに追加**: 以前はサブセットのみだったが、ページ全体がコンテキストとして追加されるようになった。コンテキストウィンドウを超過する場合は、関連度の低いセクションを自動的に除外する
- **標準化されたページフォーマット（Markdown）**: 以前のカスタム階層形式から Markdown に変換されるようになり、関連性検出の信頼性が向上。大半の言語モデルが Markdown を深く理解しているため、推論精度も向上

#### Chat input improvements

チャット入力ボックスに複数の改善:

- **添付ファイル**: `#` でコンテキストを参照すると添付ピルとしても表示され、モデルに送信される内容が明確になった
- **コンテキストピッカー**: ファイル・フォルダ・その他の添付タイプの選択が簡素化された
- **Done ボタンの廃止**: 混乱を招いていた Done ボタンが削除された。新しいセッションは **新しいチャットの作成**（`workbench.action.chat.newChat`）でのみ開始される

#### Chat mode keyboard shortcuts

- `workbench.action.chat.open`: チャットビューを開く（従来通り）
- `workbench.action.chat.openAgent`: チャットビューを開いてエージェントモードに切り替え
- `workbench.action.chat.openEdit`: Edit モード
- `workbench.action.chat.openAsk`: Ask モード

#### Autofix diagnostics from agent mode edits

`github.copilot.chat.agent.autoFix` 設定に関連する機能。エージェントモードのファイル編集で新しいエラーが発生した場合、エージェントモードがそれを自動検出し、フォローアップ編集を提案するようになった。フォローアップのプロンプト送信が不要になる。

#### Handling of undo and manual edits in agent mode

エージェントモードセッション中の手動編集の処理が改善された。以前はモデルが混乱する場合があったが、エージェントが手動変更を認識し、変更された可能性のあるファイルを編集前に必要に応じて再読み込みするようになった。

#### Conversation summary and prompt caching

エージェントモードのプロンプト構築がプロンプトキャッシングに最適化された。プロンプトキャッシングは安定したプロンプトプレフィックスを維持することでモデル応答を高速化する手法。

- 会話が長くなったりコンテキストが大きくなると、「Summarized conversation history」メッセージが表示される
- FIFO でキャッシュを破壊する代わりに、それまでの会話を最重要情報とタスクの現状サマリーに圧縮する
- プロンプトプレフィックスが安定し、応答速度を維持できる

> 📷 [画像: チャットビューで会話サマリーメッセージが表示されている](https://code.visualstudio.com/assets/updates/1_100/summarized-conversation.png)

#### MCP support for Streamable HTTP

MCP サーバーの新しい Streamable HTTP トランスポートがサポートされた。既存の SSE サーバーとの設定互換性があり、同じ形式で設定できる。

```json
{
  "servers": {
    "my-mcp-server": {
      "url": "http://localhost:3000/mcp"
    }
  }
}
```

#### MCP support for image output

MCP サーバーがツール出力の一部として画像を生成する場合のサポートが追加された。すべての言語モデルがツール出力からの画像読み取りをサポートしているわけではない点に注意（例: GPT-4.1 はビジョン機能を持つが、現時点ではツールからの画像読み取りをサポートしていない）。

#### Enhanced input, output, and progress from MCP servers

MCP サーバーのツール入出力を表示する UI が強化され、MCP の新しいプログレスメッセージもサポートされた。

> 🎬 [動画: MCP サーバーの強化された入出力・プログレス表示](https://code.visualstudio.com/assets/updates/1_100/mcp-confirm.mp4)

#### MCP config generation uses inputs

**MCP: Add Server** コマンドによる AI アシスト設定生成で、シークレットをインラインに含めるのではなく `inputs` として生成するようになった。これによりシークレットのセキュリティが向上する。

#### Inline chat V2 (Preview)

**[Preview]** `inlineChat.enableV2` 設定で有効化可能。インラインチャット（`inlineChat.start`）が刷新され、チャット編集と同じロジックを使用するようになった。利用可能なコンテキストの活用とコード編集戦略が改善されている。

- `inlineChat.hideOnRequest` 設定を有効にすると、リクエスト送信後にインラインチャットが非表示になり、チャット編集オーバーレイに最小化される

> 🎬 [動画: Inline chat V2 と hide-on-request の動作](https://code.visualstudio.com/assets/updates/1_100/inlinechat2.mp4)

#### Select and attach UI elements to chat (Experimental)

**[Experimental]** `chat.sendElementsToChat.enabled` 設定で制御（デフォルト有効）。Simple Browser でローカルホストのサイトを開き、Web 要素を選択してチャットにコンテキストとして添付できる。選択した要素のスクリーンショットと HTML / CSS が添付される。

- `chat.sendElementsToChat.attachCSS`: 関連 CSS の添付を制御
- `chat.sendElementsToChat.attachImages`: スクリーンショットの添付を制御

> 🎬 [動画: Web 要素を選択してチャットに添付し、ヒーロー要素に背景画像を追加する](https://code.visualstudio.com/assets/updates/1_100/ui-element-selection-demo.mp4)

#### Create and launch tasks in agent mode (Experimental)

**[Experimental]** `github.copilot.chat.newWorkspaceCreation.enabled` 設定に関連する機能。前回のリリースで導入されたワークスペース作成フローの末尾に、アプリ起動用のタスク作成・実行プロンプトが追加された。プロジェクト起動プロセスの合理化とタスクの再利用を可能にする。

### Accessibility

#### 概要

アクセシビリティでは、マージエディタの操作性改善、NES の通知サウンド、エージェントモードでの確認ダイアログのアクセシブルビュー対応、保存サウンドの独立化が行われた。

#### 機能詳細

#### Merge editor improvements

マージエディタのアクセシビリティが向上した。アクセシビリティヘルプダイアログ（`editor.action.accessibilityHelp`）で利用可能なアクションを確認できる。主なアクションは `Merge Editor: Complete Merge`（`mergeEditor.acceptMerge`）と `Toggle Between Merge Editor Inputs`（`mergeEditor.toggleBetweenInputs`）。現在フォーカスしている入力が支援技術にアナウンスされるようになった。

#### Next edit suggestion enhancements

- `accessibility.signals.nextEditSuggestion`: 予測提案が利用可能な場合に通知する設定
- アクセシブルビュー（`editor.action.accessibleView`）で提案の確認・承認が可能
- `accessibility.signals.diffLineAdded` / `accessibility.signals.diffLineRemoved`: diff ナビゲーション時の音声キュー

#### Review Copilot user requests from the accessible view

エージェントモードでのツール実行やターミナルコマンドのユーザー権限確認アクションを、アクセシブルビュー（`editor.action.accessibleView`）で確認可能になった。

#### Unique accessibility sounds

`accessibility.signals.save.sound` が独自のサウンドを持つようになり、`accessibility.signals.terminalCommandSucceeded.sound` とは別のサウンドが使用される。

### Editor Experience

#### 概要

エディタ体験では、フローティングウィンドウの Compact / Always-on-top モード、Secondary Side Bar のデフォルト表示設定、Linux での拡張機能署名検証必須化、セマンティックテキスト検索のキーワード候補など、多方面の改善が行われた。

#### 機能詳細

#### Floating window modes

フローティングウィンドウに 2 つの新モードが追加された。

- **Compact モード**: 一部の UI 要素を非表示にしてコンテンツのスペースを確保
- **Always-on-top モード**: ウィンドウが他のすべてのウィンドウの前面に常時表示

チャットを新しいウィンドウで作成する際にデフォルトで Compact モードが使用される。Always-on-top と組み合わせることで、チャットビューを常に手元に配置できる。

関連コマンド:
- `workbench.action.toggleWindowAlwaysOnTop`
- `workbench.action.enableWindowAlwaysOnTop` / `disableWindowAlwaysOnTop`
- `workbench.action.toggleCompactAuxiliaryWindow`
- `workbench.action.enableCompactAuxiliaryWindow` / `disableCompactAuxiliaryWindow`

> 🎬 [動画: フローティングウィンドウの Compact モード](https://code.visualstudio.com/assets/updates/1_100/floating-compact.mp4)

> 🎬 [動画: フローティングウィンドウの Always-on-top モード](https://code.visualstudio.com/assets/updates/1_100/floating-pinned.mp4)

#### Secondary Side Bar default visibility

`workbench.secondarySideBar.defaultVisibility` 設定により、新しいワークスペースやウィンドウを開いた際の Secondary Side Bar のデフォルト表示を制御できるようになった。

- `hidden`（デフォルト）: 非表示
- `visibleInWorkspace`: フォルダまたはマルチルートワークスペースを開いた場合に表示
- `visible`: 常に表示

一度ワークスペースを開いた後は、表示状態がワークスペースの状態として保存され、設定値を上書きする。

#### Mandatory extension signature verification

拡張機能の署名検証が全プラットフォーム（Windows / macOS / Linux）で必須になった。Linux でも拡張機能のインストール前に署名が適切に検証されるようになり、潜在的に悪意のある拡張機能のインストールを防止する。

> Linux ARM32 ビルドでは [issue #248308](https://github.com/microsoft/vscode/issues/248308) により、署名検証の必須化は無効のまま。次のリリースで解決予定。

#### Learn more links for malicious extensions

悪意ある拡張機能として識別された場合、その理由を説明する追加情報へのリンク（「Learn More」）が提供されるようになった。GitHub の issue やドキュメントに接続され、セキュリティ上の懸念を理解する助けとなる。

#### Prevent installation of Copilot Chat pre-release versions in VS Code stable

VS Code Stable で Copilot Chat 拡張機能のプレリリースバージョンのインストールが防止されるようになった。誤って破損した状態に陥ることを回避する措置。

#### Command to open a view without focus

ビュー（ツリービューとウェブビュービュー）をフォーカスせずに開けるようになった。`your-view-id.open` コマンドに `{ preserveFocus: boolean }` 引数を渡して使用する。拡張機能やキーボードショートカットでビューを開きつつ、現在のエディタからフォーカスを奪わない用途に有用。

#### Semantic text search with keyword suggestions (Experimental)

**[Experimental]** `github.copilot.chat.search.keywordSuggestions` 設定で有効化。セマンティックテキスト検索に AI 駆動のキーワード候補が追加された。探しているコードを見つけるのに役立つ、関連する参照や定義が候補として表示される。

> 🎬 [動画: AI 駆動のキーワード候補](https://code.visualstudio.com/assets/updates/1_100/ai-keywords.mp4)

### Code Editing

#### 概要

コード編集では、Next Edit Suggestions（NES）の新モデル導入、インポート提案の追加、NES のデフォルト有効化、HTML / Markdown での alt テキスト生成が追加された。

#### 機能詳細

#### New Next Edit Suggestions (NES) model

`github.copilot.nextEditSuggestions.enabled` 設定に関連する機能。NES を駆動する新しいモデルが導入された。より高速で文脈に即したコード推薦を提供し、レイテンシが削減されている。最近の編集内容により密接に整合する、侵入度の低い提案を実現。

#### Import suggestions

`github.copilot.nextEditSuggestions.fixes` 設定で有効化。NES が JavaScript / TypeScript ファイルで不足しているインポート文を自動提案するようになった。今後、追加言語へのサポート拡張を予定。

> 📷 [画像: NES がインポート文を提案](https://code.visualstudio.com/assets/updates/1_100/nes-import.png)

#### Next Edit Suggestions (NES) on by default

NES が VS Code Insiders でデフォルト有効化され、Stable にも段階的に展開中。

#### Generate alt text in HTML or Markdown

HTML / Markdown ファイルで画像の alt テキストを生成・更新できるようになった。埋め込み画像を含む行に移動し、`editor.action.quickFix` またはライトバルブアイコンから実行する。

> 📷 [画像: HTML の画像要素に対する alt テキスト生成](https://code.visualstudio.com/assets/updates/1_100/generate-alt-text.png)

### Notebooks

#### 概要

ノートブックでは、検索・置換の履歴永続化、セル出力のチャットへのドラッグ＆ドロップ、エージェントモード用のセル実行・カーネルステート取得・パッケージ管理ツールが追加された。

#### 機能詳細

#### Find and replace history persistence

ノートブックの検索コントロールで検索・置換の履歴が永続化されるようになった。リロード後も保持される。`editor.find.history` および `editor.find.replaceHistory` 設定で制御。

#### Drag and drop cell outputs to chat

セル出力をチャットビューにドラッグ＆ドロップで添付できるようになった。現在、画像およびテキスト出力をサポート。画像 MIME タイプの出力は直接ドラッグ可能。テキスト出力はテキスト選択との競合を避けるため、`Alt` キーを押しながらドラッグする。

> 🎬 [動画: 複数のセル出力をドラッグ＆ドロップでチャットコンテキストに添付](https://code.visualstudio.com/assets/updates/1_100/output-dnd.mp4)

#### Notebook tools for agent mode

##### Run cell

エージェントにノートブックセルを実行する LLM ツールが追加された。セル実行結果に基づいて更新したり、データ探索を自動的に行いながらノートブックを構築できる。

> 🎬 [動画: Copilot がノートブックセルを実行し、エラーに基づいて更新してリトライする](https://code.visualstudio.com/assets/updates/1_100/agent-notebook-run-edit-loop.mp4)

##### Get kernel state

エージェントがカーネルセッションで実行済みのセルやアクティブな変数を Kernel State ツールで確認できるようになった。

##### List/Install packages

Jupyter 拡張機能がノートブックのカーネルとして使用されている環境へのパッケージ一覧表示・インストールツールを提供。Python Environments 拡張機能が利用可能な場合はそれに委譲し、そうでなければ pip パッケージマネージャーを使用する。

### Source Control

#### 概要

長年の要望であったステージ済み変更のエディタ上でのクイック diff デコレーションが追加され、ソース管理ビューを開かずに変更状態を確認できるようになった。

#### 機能詳細

#### Quick diff decorations for staged changes

ステージ済み変更のクイック diff デコレーションがエディタに追加された。

- テーマトークンでカラーをカスタマイズ可能:
  - `editorGutter.addedSecondaryBackground`
  - `editorGutter.modifiedSecondaryBackground`
  - `editorGutter.deletedSecondaryBackground`
- エディタガターのコンテキストメニューの **Diff Decorations** サブメニューから非表示にできる

> 🎬 [動画: diff デコレーションを使用してエディタからステージ済み変更を管理](https://code.visualstudio.com/assets/updates/1_100/staged-changes-diff-decorations.mp4)

### Debugging

#### 概要

ディスアセンブリビューにコンテキストメニューが追加され、JavaScript デバッガの Network ビューが最近の Node.js バージョンでデフォルト有効化された。

#### 機能詳細

#### Disassembly view context menu

コミュニティ貢献により、ディスアセンブリビューにコンテキストメニューが追加された。

> 📷 [画像: ディスアセンブリビューのコンテキストメニュー](https://code.visualstudio.com/assets/updates/1_100/disassembly-context.png)

#### JavaScript debugger Network view

Node.js の最近のバージョンで強化されたネットワークデバッグ機能に対応し、[実験的ネットワークビュー](https://code.visualstudio.com/updates/v1_93#_experimental-network-view) が十分にサポートする最近の Node.js バージョン（v22.14.0 以上）でデフォルト有効化された。

### Languages

#### 概要

CSS / HTML プロパティのブラウザサポート表示、`.*.env` ファイルのデフォルトシンタックスハイライト、TypeScript / JavaScript の展開可能ホバー（Experimental）が追加された。

#### 機能詳細

#### Show browser support for CSS and HTML

CSS プロパティ、HTML 要素、HTML 属性にホバーした際に、[Baseline](https://developer.mozilla.org/docs/Glossary/Baseline/Compatibility) を使用したブラウザサポートのサマリーが表示されるようになった。

> 📷 [画像: CSS ホバーでの Baseline ブラウザサポート表示](https://code.visualstudio.com/assets/updates/1_100/css-baseline.png)

#### Default syntax highlighting for `.*.env` files

`.*.env` 形式のファイル名が `.ini` ファイルとしてシンタックスハイライトされるようになった。

#### Expandable hovers for JavaScript and TypeScript (Experimental)

**[Experimental]** `typescript.experimental.expandableHover` 設定で有効化。ホバーコントロールの `+` / `-` でより多い、またはより少ない型情報を表示できる。TypeScript 5.9 以上が必要（[TypeScript nightly 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-next) で利用可能）。

> 🎬 [動画: TypeScript の展開可能ホバー](https://code.visualstudio.com/assets/updates/1_100/expandable-hover.mp4)

### Remote Development

#### 概要

Dev Container の features / images がインストラクションファイルを含むようになり、VS Code チャットがこのコンテキストを自動的に利用して提案の精度を向上させる。

#### 機能詳細

#### Dev container instructions files

Dev Container features と images にツールと設定を記述するインストラクションファイルが含まれるようになった。VS Code チャットはこのコンテキストを自動的に使用し、開発中の提案の関連性と正確性が向上した。

### Contributions to extensions

#### 概要

Python 拡張機能群でブランチカバレッジ、Quick Create 環境作成、チャットツール、カラーピッカー、AI Code Action 等が追加された。GitHub Pull Requests 拡張機能ではアクティブ PR に関するチャット質問機能が追加された。

#### 機能詳細

#### Python

##### Branch coverage support

テスティングエクスプローラーで Python のブランチカバレッジがサポートされた。`coveragepy` バージョン 7.7 以上が必要（`pip install coverage==7.7` でアップグレード）。

> 🎬 [動画: テストエクスプローラーでのブランチカバレッジ実行と表示](https://code.visualstudio.com/assets/updates/1_100/python-branch-coverage.mp4)

##### Python Environments Quick Create command

Python Environments 拡張機能に Quick Create が追加された。マシン上の最新 Python バージョンを検出し、仮想環境の作成とワークスペース依存関係のインストールをワンクリックで実行できる。venv ベースでは `.venv`、conda ベースでは `.conda` がワークスペースに作成される。**Python: Create Environment** コマンドから利用可能。

> 📷 [画像: Python: Create Environment Quick Pick での Quick Create](https://code.visualstudio.com/assets/updates/1_100/python-envs-quick-create.png)

##### Python Environments chat tools

Python Environments 拡張機能（プレビュー）に 2 つのチャットツールが追加された: 「Get Python Environment Information」と「Install Python Package」。`#pythonGetEnvironmentInfo` `#pythonInstallPackage` で参照するか、エージェントモードが自動的に呼び出す。

> 🎬 [動画: エージェントモードで環境情報ツールが暗黙的に呼び出される](https://code.visualstudio.com/assets/updates/1_100/python-get-env-tool.mp4)

> 🎬 [動画: numpy のインストールパッケージツール](https://code.visualstudio.com/assets/updates/1_100/python-install-pkg-tool.mp4)

##### Color picker when using Pylance

Pylance が Python ファイルで認識されるカラー値に対してインタラクティブなカラースウォッチをエディタに表示するようになった。`python.analysis.enableColorPicker` 設定で有効化。#RGB（"#001122"）および #RGBA（"#001122FF"）形式をサポート。

> 📷 [画像: #RGB カラー形式に対するエディタ内カラースウォッチ](https://code.visualstudio.com/assets/updates/1_100/pylance-color-picker.png)

##### AI Code Actions: Convert Format String (Experimental)

**[Experimental]** Pylance で文字列結合を f-string または `format()` に変換する AI Code Action が追加された。ライトバルブまたは `Ctrl + .` / `Cmd + .` から使用可能。

```json
"python.analysis.aiCodeActions": {"convertFormatString": true}
```

> 📷 [画像: AI 駆動の文字列変換 Code Actions](https://code.visualstudio.com/assets/updates/1_100/pylance-convert-string.png)

#### GitHub Pull Requests and Issues

GitHub Pull Requests 拡張機能の主な更新:

- アクティブな PR についてチャットで質問可能（例: `#activePullRequest` のすべてのコメントに対応）
- Issue をウェブビューで表示可能
- 「Pull Requests」「Issues」「Notifications」ビューの改善
- GitHub Project Padawan のリリースに向けて、Issue への Copilot 割り当てや `@` メンションに対応

## 設定項目まとめ

### Chat

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `chat.instructionsFilesLocations` | インストラクションファイルの配置フォルダ | — | GA |
| `chat.promptFilesLocations` | プロンプトファイルの配置フォルダ | — | GA |
| `github.copilot.chat.agent.autoFix` | エージェントモード編集後のエラー自動修正 | — | GA |
| `inlineChat.enableV2` | Inline chat V2 の有効化 | `false` | Preview |
| `inlineChat.hideOnRequest` | リクエスト時にインラインチャットを非表示 | `false` | Preview |
| `chat.sendElementsToChat.enabled` | UI 要素のチャット送信機能 | `true`（Simple Browser で有効） | Experimental |
| `chat.sendElementsToChat.attachCSS` | 選択要素の CSS を添付 | — | Experimental |
| `chat.sendElementsToChat.attachImages` | 選択要素のスクリーンショットを添付 | — | Experimental |
| `github.copilot.chat.newWorkspaceCreation.enabled` | ワークスペース作成フローでのタスク起動 | — | Experimental |

### Accessibility

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `accessibility.signals.nextEditSuggestion` | NES 予測提案の通知サウンド | — | GA |
| `accessibility.signals.diffLineAdded` | diff 行追加時の音声キュー | — | GA |
| `accessibility.signals.diffLineRemoved` | diff 行削除時の音声キュー | — | GA |
| `accessibility.signals.save.sound` | 保存時のサウンド（独立化） | — | GA |

### Editor Experience

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `workbench.secondarySideBar.defaultVisibility` | Secondary Side Bar のデフォルト表示 | `hidden` | GA |
| `github.copilot.chat.search.keywordSuggestions` | セマンティック検索の AI キーワード候補 | — | Experimental |

### Code Editing

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `github.copilot.nextEditSuggestions.enabled` | NES の有効化 | — | GA (段階的展開) |
| `github.copilot.nextEditSuggestions.fixes` | NES のインポート提案 | — | GA |

### Notebooks

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `editor.find.history` | 検索履歴の永続化 | — | GA |
| `editor.find.replaceHistory` | 置換履歴の永続化 | — | GA |

### Languages

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `typescript.experimental.expandableHover` | TypeScript / JS の展開可能ホバー | — | Experimental |

### Contributions to extensions (Python)

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `python.analysis.enableColorPicker` | Pylance のカラーピッカー | — | GA |
| `python.analysis.aiCodeActions` | AI Code Actions（文字列変換等） | — | Experimental |

## Breaking Changes / 非推奨化

### 拡張機能署名検証の Linux 必須化

- **何が変わったか**: 拡張機能の署名検証が Linux でも必須になった（以前は Windows / macOS のみ）。
- **影響を受けるユーザー**: Linux で VS Code を使用しているすべてのユーザー。署名が検証できない拡張機能はインストールできなくなる。
- **対処法**: 使用している拡張機能が署名済みであることを確認する。Linux ARM32 では [issue #248308](https://github.com/microsoft/vscode/issues/248308) により現時点では無効。

### Copilot Chat プレリリースの Stable インストール防止

- **何が変わったか**: VS Code Stable で Copilot Chat 拡張機能のプレリリースバージョンがインストールできなくなった。
- **影響を受けるユーザー**: Stable ビルドでプレリリース版を使用していたユーザー。
- **対処法**: プレリリース版は VS Code Insiders で使用する。

## 開発者・拡張機能作成者向け

### Text Encodings（Finalized API）

テキストエンコーディングの API がファイナライズされた。

- `TextDocument` の現在の `encoding` を取得
- 特定の `encoding` で `TextDocument` を開く
- 特定の `encoding` で `string` を `Uint8Array` にエンコード
- 特定の `encoding` で `Uint8Array` を `string` にデコード

### ESM support for extensions

NodeJS 拡張機能ホストが JavaScript モジュール（ESM）をサポートするようになった。拡張機能の `package.json` に `"type": "module"` を追加するだけで、`import` / `export` 文と `import('vscode')` が使用可能。

- Web Worker 拡張機能ホストでは未対応（[issue #130367](https://github.com/microsoft/vscode/issues/130367) で進捗を追跡）
- サンプル: https://github.com/jrieken/vscode-esm-sample-extension

### Proposed API: Tool calling for images

> ⚠️ この API はプロポーザル段階であり、今後変更または削除される可能性があります。
> プロポーザルファイル: `vscode.proposed.languageModelDataPart.d.ts`

前回のイテレーションで追加された画像添付・ビジョンリクエストの API が拡張され、ツール呼び出し結果に画像を含められるようになった。[API プロポーザル issue #245104](https://github.com/microsoft/vscode/issues/245104)

### Proposed API: MCP servers contributed by extensions

> ⚠️ この API はプロポーザル段階であり、今後変更または削除される可能性があります。
> プロポーザルファイル: `vscode.proposed.languageModelDataPart.d.ts`

拡張機能からプログラム的に MCP サーバーを登録できる API。設定ファイルや `mcp.json` にハードコードする代替手段となる。[API プロポーザル issue #243522](https://github.com/microsoft/vscode/issues/243522)、[サンプル](https://github.com/microsoft/vscode-extension-samples/tree/main/mcp-extension-sample/)

### Proposed API: MCP Tool Annotations

> ⚠️ この API はプロポーザル段階であり、今後変更または削除される可能性があります。

VS Code が MCP サーバーのツールに設定された[ツールアノテーション](https://modelcontextprotocol.io/docs/concepts/tools#tool-annotations)の人間可読名を表示するようになった。`readOnlyHint: true` が設定されたツールはユーザー確認なしで実行が許可される。

### Proposed API: Variable line heights

> ⚠️ この API はプロポーザル段階であり、今後変更または削除される可能性があります。

Monaco エディタで `IModelDecorationOptions` 型の行高さ値を設定することで、可変行高さを定義できるようになった。同じ行に 2 つの行高さが設定された場合、大きい方が使用される。現時点では拡張機能には公開されていないが、テスト後に展開予定。

> 🎬 [動画: エディタでの可変行高さ](https://code.visualstudio.com/assets/updates/1_100/variable-line-heights.mp4)

## エンジニアリング・基盤改善

このリリースでは、Engineering セクションとして独立した項目はソースに記載されていない。基盤関連の改善としては、エージェントモードのプロンプトキャッシング最適化（会話要約とプロンプトキャッシングのセクションで記述済み）がある。

## Notable fixes

- [vscode#244939](https://github.com/microsoft/vscode/issues/244939) — 個人用 Microsoft アカウントが非常に短時間（数分〜数時間）でログアウトする問題を修正

## コミュニティ貢献

多くの外部コントリビューターによる貢献が行われた。特に影響の大きいものをピックアップする:

- **[@thegecko](https://github.com/thegecko)**: ディスアセンブリビューにコンテキストメニューを追加 ([PR #212500](https://github.com/microsoft/vscode/pull/212500))
- **[@andrewbranch](https://github.com/andrewbranch)**: 組み込み TS/JS 拡張機能を tsgo に置き換えるための無効化を許可 ([PR #246858](https://github.com/microsoft/vscode/pull/246858))
- **[@BABA983](https://github.com/BABA983)**: 全組み合わせを承認するコマンドを追加 ([PR #225132](https://github.com/microsoft/vscode/pull/225132))
- **[@gabritto](https://github.com/gabritto)**: TypeScript の展開可能ホバーの再追加とデフォルト有効化 ([PR #246899](https://github.com/microsoft/vscode/pull/246899), [PR #247343](https://github.com/microsoft/vscode/pull/247343))
- **[@nknguyenhc](https://github.com/nknguyenhc)**: HTML スクリプト内のビルトインシンボルの定義へ移動 ([PR #244074](https://github.com/microsoft/vscode/pull/244074))
- **[@whistlegraph](https://github.com/whistlegraph)**: Pointer Lock Web API の有効化 ([PR #210875](https://github.com/microsoft/vscode/pull/210875))
- **[@pisv](https://github.com/pisv)**: マージエディタの `LineRange.join(other)` バグ修正 ([PR #227585](https://github.com/microsoft/vscode/pull/227585))
- **[@huntertran](https://github.com/huntertran)**: git blame ホバーのコミット説明で改行処理を修正 ([PR #245779](https://github.com/microsoft/vscode/pull/245779))
- **[@rviscomi](https://github.com/rviscomi)**: CSS ホバーカードに Baseline ステータスを追加 ([PR #428](https://github.com/microsoft/vscode-css-languageservice/pull/428))
- **[@AlterNT](https://github.com/AlterNT)**: CSS `@scope` のサポート追加 ([PR #434](https://github.com/microsoft/vscode-css-languageservice/pull/434))

## まとめと所感

VS Code v1.100 は、インストラクション / プロンプトファイルの正式整備によって AI カスタマイズの基盤が確立された重要なリリースである。エージェントモードの編集高速化（OpenAI apply patch / Anthropic replace string）とプロンプトキャッシングにより、実務でのエージェント利用がより実用的になった。MCP の Streamable HTTP サポートは SSE からの自然な進化であり、既存設定との後方互換性が維持されている点は移行の障壁を低くしている。フローティングウィンドウの Compact / Always-on-top とステージ済み変更のクイック diff デコレーションは、日常的なマルチウィンドウ作業とバージョン管理ワークフローの改善として即座に恩恵を受けられる。NES のデフォルト有効化により、コード編集の効率化が全ユーザーに段階的に波及する。
