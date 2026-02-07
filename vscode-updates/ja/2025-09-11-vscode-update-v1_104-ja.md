---
title: "Visual Studio Code August 2025 (v1.104) 日本語詳細解説"
date: "2025-09-11"
version_ref: "v1_104"
source_url: "https://code.visualstudio.com/updates/v1_104"
lang: "ja"
---

# Visual Studio Code August 2025 (v1.104) 日本語詳細解説

## リリース概要

VS Code v1.104（2025年8月）は、AI エージェント機能のセキュリティと使いやすさの両立に大きく踏み込んだリリースである。モデルの自動選択（Auto model selection）による最適化、機密ファイル編集時の確認プロンプト、ターミナルコマンドの自動承認の安全性強化など、エージェントモードを安全に活用するための仕組みが数多く導入された。また、`AGENTS.md` ファイルのサポート（Experimental）や coding agent との連携強化により、チーム開発における AI エージェント活用の幅が広がっている。拡張機能開発者向けには `LanguageModelChatProviders` API がファイナライズされ、サードパーティモデルの統合が正式にサポートされた。なお、1.104.1〜1.104.3 のリカバリーアップデートがリリースされている。

## 注目の新機能・変更点

1. **Auto model selection（Preview）** — モデルピッカーで「Auto」を選択すると、VS Code が最適なモデルを自動選択し、レート制限を軽減する。有料ユーザーは 10% のリクエスト割引も適用される。
2. **機密ファイル編集の確認プロンプト** — エージェントモードで設定ファイルや dotfile など重要なファイルを変更する際、ユーザー確認を明示的に求めるようになった。
3. **AGENTS.md ファイルサポート（Experimental）** — ワークスペースルートに `AGENTS.md` を配置すると、自動的にチャットコンテキストとして読み込まれる。
4. **ターミナル自動承認の安全性強化** — 新設定・明示的オプトイン・ルール可視化・`curl`/`wget` 警告など、多角的にセキュリティが強化された。
5. **Global auto approve の見直し** — 設定名が `chat.tools.global.autoApprove` に変更され、初回使用時に警告ダイアログが表示されるようになった。
6. **LanguageModelChatProviders API のファイナライズ** — 拡張機能からチャットにサードパーティモデルを提供可能になった。
7. **数式レンダリングの GA 化** — KaTeX によるインライン・ブロック数式の表示がデフォルトで有効化された。
8. **coding agent との連携強化（Experimental）** — Chat Sessions ビューの大幅強化、TODO コメントからの coding agent 委任、チャットからの委任フローが改善された。
9. **変更ファイルリストの UX 改善** — デフォルトで折りたたみ表示、ファイルごとの変更行数表示、ステージ/コミット時の自動承認など QoL 向上。
10. **Python 開発体験の向上** — Pipenv サポート、AI ホバーサマリー（Experimental）、コードスニペット実行ツールなどが追加された。

## セクション別詳細解説

### Chat

#### 概要

Chat セクションは本リリースで最大の領域を占め、モデル自動選択、セキュリティ強化、coding agent 連携、UX 改善など多岐にわたる機能が導入された。エージェントモードの安全性と生産性を両立させることが全体的なテーマである。

#### 機能詳細

#### Auto model selection (Preview)

モデルピッカーで「Auto」を選択すると、VS Code がリクエストに最適なモデル（Claude Sonnet 4、GPT-5、GPT-5 mini、GPT-4.1）を自動選択する。組織でアクセスが無効化されているモデルは除外される。

- **何が変わったか**: ユーザーがモデルを手動選択する必要がなくなり、パフォーマンス最適化とレート制限軽減が自動化された
- **ステータス**: **[Preview]** — 個人プランユーザーから段階的にロールアウト中
- **対象ユーザー**: すべての GitHub Copilot ユーザー（VS Code）
- **使い方**: モデルピッカーから「Auto」を選択。ホバーで選択されたモデルとモデル乗数を確認可能
- 有料ユーザーには 10% のリクエスト割引が適用される

> 📷 [画像: モデルピッカーで Auto オプションを表示](https://code.visualstudio.com/assets/updates/1_104/model-dropdown-auto.png)

> 📷 [画像: ホバーで選択されたモデルを表示](https://code.visualstudio.com/assets/updates/1_104/auto-model-multiplier.png)

#### Confirm edits to sensitive files

エージェントモードで機密ファイル（設定ファイル、dotfile、ワークスペース外のファイル等）を編集する際に、ユーザー確認ダイアログが表示されるようになった。

- **何が変わったか**: エージェントが重要なファイルを自律的に変更する前に確認を求めるようになった
- **関連する設定項目**: `chat.tools.edits.autoApprove` — 確認が必要なファイルパターンを設定可能
- **ステータス**: **[GA]**
- **対象ユーザー**: エージェントモードを使用するすべてのユーザー
- **使い方**: デフォルトでシステムフォルダ・dotfile・ワークスペース外ファイルに確認が必要。パターンは設定でカスタマイズ可能

> 📷 [画像: 機密ファイル編集の確認ダイアログ](https://code.visualstudio.com/assets/updates/1_104/chat-edit-sensitive-file.png)

#### Support for AGENTS.md files (Experimental)

ワークスペースルートに `AGENTS.md` ファイルを配置すると、チャットリクエストのコンテキストとして自動的に読み込まれる。

- **何が変わったか**: 複数の AI エージェントを使用するチームが、共通の指示やコンテキストを `AGENTS.md` に記述できるようになった
- **関連する設定項目**: `chat.useAgentsMdFile` — `AGENTS.md` の読み込みを制御（デフォルト有効）
- **ステータス**: **[Experimental]**
- **対象ユーザー**: チームで AI エージェントを活用する開発者
- **使い方**: ワークスペースルートに `AGENTS.md` を配置するだけ。詳細は <https://agents.md/> を参照

#### Improved changed files experience

エージェントモードでの変更ファイルリストが大幅に改善された。

- **何が変わったか**:
  - ファイルリストがデフォルトで折りたたまれ、チャット会話にスペースを確保
  - 変更の承認（keep/accept）時にリストからファイルが除去される
  - Source Control ビューでのステージ/コミットが自動的に変更を承認する
  - ファイルごとの変更行数（追加/削除）が表示される
- **ステータス**: **[GA]**
- **対象ユーザー**: エージェントモードを使用するすべてのユーザー

> 🎬 [動画: 変更ファイルリストの展開とエントリの承認によるリストからの削除](https://code.visualstudio.com/assets/updates/1_104/changed-files-list.mp4)

#### Use custom chat modes in prompt files

プロンプトファイルで使用するチャットモードとして、ビルトインモード（`agent`、`edit`、`ask`）に加え、カスタムチャットモードも指定可能になった。

- **何が変わったか**: プロンプトファイルの実行時にカスタムチャットモードを参照できるようになった
- **ステータス**: **[GA]**
- **対象ユーザー**: プロンプトファイルを活用するユーザー
- **使い方**: プロンプトファイル内でカスタムモード名を指定。IntelliSense による補完もサポート

> 📷 [画像: プロンプトファイルでのカスタムチャットモードの IntelliSense](https://code.visualstudio.com/assets/updates/1_104/custom_modes_in_prompt_files.png)

#### Configure prompt file suggestions (Experimental)

チャットのウェルカムビューに表示するプロンプトファイルの候補を、コンテキスト条件に基づいて設定できるようになった。

- **何が変わったか**: when-clause 式を使ってファイルタイプやワークスペースに応じたプロンプト候補表示が可能になった
- **関連する設定項目**: `chat.promptFilesRecommendations` — boolean 値または when-clause 式でプロンプトファイルの表示条件を設定

```jsonc
{
  "chat.promptFilesRecommendations": {
    "plan": true,                            // 常に表示
    "a11y-audit": "resourceExtname == .html", // HTML ファイルのみ
    "document": "resourceLangId == markdown", // Markdown ファイルのみ
    "debug": false                           // 表示しない
  }
}
```

- **ステータス**: **[Experimental]**
- **対象ユーザー**: チームでプロンプトファイルを標準化したい組織

#### Select tools in tool sets

ツールピッカーでツールセット内の個別ツールの有効/無効を切り替えられるようになった。

- **何が変わったか**: ツールセット（`edit`、`search` など）の中身が表示され、個別に制御可能に
- **ステータス**: **[GA]**
- **対象ユーザー**: エージェントモードでツール選択を細かく制御したいユーザー
- **使い方**: Chat ビューの「Configure Tools...」ボタンからツールピッカーにアクセス

> 📷 [画像: ツールピッカーでの展開されたツールセット](https://code.visualstudio.com/assets/updates/1_104/tools_in_toolsets.png)

#### Configure font used in chat

Chat ビューのフォントファミリーとフォントサイズを設定可能になった。

- **何が変わったか**: チャットメッセージに使用するフォントをカスタマイズできるようになった
- **関連する設定項目**: `chat.fontFamily`、`chat.fontSize`
- **ステータス**: **[GA]**
- **対象ユーザー**: チャットの表示をカスタマイズしたいすべてのユーザー
- リスト内のコンテンツにはまだ反映されないが、今後のリリースで対応予定

> 📷 [画像: カスタムフォントとフォントサイズを適用した Chat ビュー](https://code.visualstudio.com/assets/updates/1_104/chat-configure-font.png)

#### Collaborate with coding agents (Experimental)

coding agent との連携が大幅に強化された。Chat Sessions ビュー・GitHub coding agent 統合・委任フローの 3 領域で改善が行われている。

##### Chat Sessions view

Chat Sessions ビューがローカルセッションと外部提供セッションを統合管理する単一ビューに進化した。

- **関連する設定項目**: `chat.agentSessionsViewLocation`
- **Status Bar からの進捗追跡**: 複数の coding agent の進捗をステータスバーから監視可能
- **マルチセッション対応**: 同一ビューから複数セッションの起動・管理が可能
- **コンテキストメニューの拡充**: coding agent との対話アクションが増加
- **リッチ記述**: 各リスト項目に詳細なコンテキスト情報を表示

##### GitHub coding agent integration

GitHub coding agent とのチャットセッション統合が改善された。

- チャットエディタからコード変更の表示・適用、PR のチェックアウトが可能
- ローカルチャットから GitHub agent タスクへのシームレスな遷移
- カード・ツールレンダリングの視覚的改善
- セッション読み込みのパフォーマンス向上

> 🎬 [動画: Chat Sessions ビューと GitHub coding agent との統合](https://code.visualstudio.com/assets/updates/1_104/chat-sessions-view.mp4)

##### Delegate to coding agent

ローカルタスクを Copilot coding agent に委任する方法が拡充された。

- **TODO コメントからの委任**: `TODO` で始まるコメントに Code Action が表示され、coding agent セッションを即座に開始可能
- **チャットからの委任**: ファイル参照を含むコンテキストが GitHub coding agent に転送され、タスクを計画してから委任するフローが可能。新しいチャットエディタでリアルタイムの進捗を確認可能
- **関連する設定項目**: `githubPullRequests.codingAgent.uiIntegration`

> 📷 [画像: TODO コメント上のコードアクション「Delegate to coding agent」](https://code.visualstudio.com/assets/updates/1_104/coding-agent-todo.png)

> 🎬 [動画: サイドバーチャットから coding agent にタスクを委任](https://code.visualstudio.com/assets/updates/1_104/delegate-to-coding-agent.mp4)

- **ステータス**: **[Experimental]**
- **対象ユーザー**: GitHub Copilot coding agent を使用する開発者

#### Social sign in with Google

Google アカウントによる GitHub Copilot へのサインイン/サインアップが GA となり、すべてのユーザーにロールアウト中。

- **何が変わったか**: Google アカウントを使った認証オプションが正式に利用可能になった
- **ステータス**: **[GA]**
- **対象ユーザー**: すべての VS Code ユーザー

> 📷 [画像: Google アカウントオプションを含むサインインダイアログ](https://code.visualstudio.com/assets/updates/1_104/google.png)

#### Terminal auto approve

ターミナルコマンドの自動承認機能が、使いやすさとセキュリティの両面で大幅に改善された。

- **何が変わったか**:
  - `chat.tools.terminal.enableAutoApprove` 設定で有効/無効を制御可能（組織による Device Management 経由の制御にも対応）
  - 実際に有効化する前に Chat ビューでの明示的なオプトインが必要
  - 自動承認ルールの追加・設定画面へのアクセスが Chat ビューから可能
  - 適用されたルールが Chat ビューに表示され、ルール設定への直接アクセスが可能
  - デフォルトルールが安全性とノイズ低減のために改善
  - バックスラッシュ/フォワードスラッシュを含む非正規表現ルールがパスとして扱われ、スラッシュ違いや `./` プレフィックスも許容
  - `curl`、`wget`、`Invoke-RestMethod`、`Invoke-WebRequest` でインターネットからコンテンツを取得する際に警告を表示（プロンプトインジェクション対策）
- **関連する設定項目**: `chat.tools.terminal.enableAutoApprove`
- **ステータス**: **[GA]**
- **対象ユーザー**: エージェントモードでターミナルコマンドを使用するすべてのユーザー

> 📷 [画像: ターミナル自動承認のオプトインドロップダウン](https://code.visualstudio.com/assets/updates/1_104/terminal-auto-approve-opt-in.png)

> 📷 [画像: 自動承認ルール追加のリンク](https://code.visualstudio.com/assets/updates/1_104/terminal-auto-approve-new-links.png)

#### Global auto approve

グローバル自動承認の設定名が変更され、初回使用時の安全対策が追加された。

- **何が変わったか**:
  - 設定名が `chat.tools.autoApprove` → `chat.tools.global.autoApprove` に変更（自動マイグレーションなし）
  - 初回使用時に警告ダイアログが表示され、意図せず有効化してしまうリスクを軽減
  - ターミナル自動承認の前提条件であるという誤解を解消
- **関連する設定項目**: `chat.tools.global.autoApprove`
- **ステータス**: **[GA]**
- **対象ユーザー**: グローバル自動承認を使用していた/使用を検討するすべてのユーザー
- **対処法**: 以前 `chat.tools.autoApprove` を有効にしていたユーザーは、新しい設定名で再設定が必要

> 📷 [画像: グローバル自動承認の警告ダイアログ](https://code.visualstudio.com/assets/updates/1_104/global-auto-approve-warning.png)

#### Math rendering enabled by default

KaTeX によるチャットレスポンス内の数式レンダリングが GA となり、デフォルトで有効化された。

- **何が変わったか**: インライン数式（`$...$`）とブロック数式（`$$...$$`）の表示がデフォルトで有効に
- **関連する設定項目**: `chat.math.enabled` — 無効化する場合に使用
- **ステータス**: **[GA]**
- **対象ユーザー**: チャットで数式を扱うすべてのユーザー

> 📷 [画像: Chat ビューでのインラインおよびブロック数式の表示](https://code.visualstudio.com/assets/updates/1_104/chat-math.png)

#### Chat view default visibility

ワークスペースを最初に開いた際に、Chat ビュー（Secondary Side Bar）がデフォルトで表示されるようになった。

- **何が変わったか**: ワークスペースの初回起動時に Chat ビューが自動的に表示される
- **関連する設定項目**: `workbench.secondarySideBar.defaultVisibility` — 動作をカスタマイズ可能
- **ステータス**: **[GA]**
- **対象ユーザー**: すべてのユーザー
- **使い方**: Chat ビューのドロップダウンからもデフォルト表示の設定を変更可能

> 📷 [画像: Chat ビューメニューでの Secondary Side Bar デフォルト表示設定](https://code.visualstudio.com/assets/updates/1_104/auxview.png)

#### Improved task support

エージェントモードでのタスク実行サポートが 3 つの観点で改善された。

- **入力要求の検出**: タスクやターミナルコマンドがユーザー入力を要求する際、エージェントが自動検出してチャットで応答を促す。`[Y] Yes [N] No` のようなオプションがある場合は確認プロンプトに表示される
- **Problem matcher ベースのエラー検出**: problem matcher を使用するタスクでは、LLM による出力評価ではなく problem matcher の結果に基づいてエラーを収集・表示。問題箇所への直接ナビゲーションが可能
- **複合タスクのサポート**: 複合タスク実行時に各依存タスクの進捗と出力を個別に表示。マルチステップのワークフローに対応

> 🎬 [動画: 入力要求の検出と応答](https://code.visualstudio.com/assets/updates/1_104/prompt-input-demo.mp4)

> 🎬 [動画: VS Code - Build タスクの実行時のエージェント動作](https://code.visualstudio.com/assets/updates/1_104/build-task.mp4)

- **ステータス**: **[GA]**
- **対象ユーザー**: エージェントモードでタスクを実行するすべてのユーザー

#### Improved terminal support

ターミナルツール関連の信頼性とカスタマイズ性が向上した。

- **コアへの移行**: `terminalSelection` と `terminalLastCommand` ツールが拡張機能からコアに移行され、信頼性が向上
- **シェル統合タイムアウトの設定**: `chat.tools.terminal.shellIntegrationTimeout` 設定でタイムアウトを構成可能。シェルの起動が遅い環境（重い PowerShell プロファイル等）で有用
- **Command Prompt の回避**: シェル統合が十分にサポートされていない Command Prompt の代わりに Windows PowerShell を使用するよう変更。`runInTerminal` ツールの信頼性が向上
- **ステータス**: **[GA]**

#### Todo List tool

エージェントが複雑なタスクを小さなタスクに分割して進捗を報告する Todo List ツールがデフォルトで有効化された。

- **何が変わったか**: Todo リストが Chat ビュー上部の Todo コントロールに表示され、作業進行に合わせて自動的に折りたたまれ、現在進行中のタスクのみ表示される
- **ステータス**: **[GA]**
- **対象ユーザー**: エージェントモードを使用するすべてのユーザー

#### Skip tool calls

エージェントがツール呼び出しの確認を求めた際に、そのツール呼び出しをスキップしてエージェントの処理を継続できるようになった。

- **何が変わったか**: 確認ダイアログで「スキップ」を選択可能に。リクエスト全体のキャンセルや新しいリクエストの入力も引き続き可能
- **ステータス**: **[GA]**
- **対象ユーザー**: エージェントモードを使用するすべてのユーザー

#### Improvements to semantic workspace search

`#codebase` ツールが新しい Embeddings モデルにアップグレードされた。

- **何が変わったか**: コード検索の結果品質が向上し、ディスク上のストレージ使用量が従来モデルの 6% に削減された
- **ステータス**: **[GA]** — 数週間かけて段階的にロールアウト。Insiders ではすでに利用可能
- **対象ユーザー**: セマンティック検索を使用するすべてのユーザー
- アクション不要で自動的にアップデートされる

#### Hide and disable GitHub Copilot AI features

ビルトインの AI 機能（チャット、コード補完、Next Edit Suggestions）を無効化・非表示にする新設定が追加された。

- **何が変わったか**:
  - デバイス間で同期される新設定 `chat.disableAIFeatures` が導入
  - Copilot 拡張機能がインストールされている場合はそれも無効化
  - プロファイルごと・ワークスペースごとの設定が可能
  - 「Hide AI Features」コマンドが更新され、この設定を表示するようになった
- **関連する設定項目**: `chat.disableAIFeatures`
- **ステータス**: **[GA]**
- **対象ユーザー**: AI 機能を選択的に無効化したいユーザー・組織
- 以前 AI 機能を非表示にしていたユーザーはその状態が維持される。デバイス間同期が必要な場合は新設定を追加で設定

### MCP

#### 概要

MCP（Model Context Protocol）関連では、サーバー指示のサポートと設定の整理が行われた。自動検出のデフォルト無効化により、MCP 環境が成熟していることを反映した変更が加えられている。

#### 機能詳細

#### Support for server instructions

VS Code が MCP サーバーの instructions を読み取り、ベースプロンプトに含めるようになった。

- **何が変わったか**: MCP サーバーが提供する指示がチャットのコンテキストに自動的に組み込まれる
- **ステータス**: **[GA]**
- **対象ユーザー**: MCP サーバーを使用するすべてのユーザー

#### MCP auto discovery disabled by default

他のアプリ（Claude Code など）にインストールされた MCP サーバーの自動検出がデフォルトで無効化された。

- **何が変わったか**: VS Code の MCP サポートが成熟したため、自動検出はデフォルト無効に変更
- **関連する設定項目**: `chat.mcp.discovery.enabled` — 再有効化する場合に使用
- **ステータス**: **[GA]**
- **対象ユーザー**: 他のアプリの MCP サーバーを VS Code で使用していたユーザー

#### Enable MCP

MCP の有効/無効を制御する設定が新しい設定名に移行された。

- **何が変わったか**: `chat.mcp.enabled`（boolean）→ `chat.mcp.access`（文字列値）に変更
  - `all`: すべての MCP サーバーの実行を許可（旧 `true`）
  - `none`: MCP サポートを完全に無効化（旧 `false`）
- **関連する設定項目**: `chat.mcp.access`
- **ステータス**: **[GA]**
- **対象ユーザー**: MCP 設定をカスタマイズしているすべてのユーザー

### Accessibility

#### 概要

アクセシビリティ関連では、チャット確認ダイアログにフォーカスを移動する新コマンドが追加された。

#### 機能詳細

#### Focus chat confirmation action

新コマンド **Focus Chat Confirmation**（`workbench.action.chat.focusConfirmation`）が追加された。

- **何が変わったか**: 確認ダイアログが存在する場合はフォーカスを移動し、存在しない場合はスクリーンリーダーユーザーに確認不要であることを通知する
- **ステータス**: **[GA]**
- **対象ユーザー**: スクリーンリーダーを使用するユーザー、キーボードナビゲーションを活用するユーザー

### Code Editing

#### 概要

インラインサジェストの表示遅延を設定可能にする新設定が追加された。

#### 機能詳細

#### Configurable inline suggestion delay

インラインサジェストが表示されるまでの最小遅延を設定できるようになった。

- **何が変わったか**: タイプ後にサジェストが表示されるまでの時間を調整可能に
- **関連する設定項目**: `editor.inlineSuggest.minShowDelay` — サジェストの最小表示遅延を設定
- **ステータス**: **[GA]**
- **対象ユーザー**: サジェストが即座に表示されてタイピングの邪魔になると感じるユーザー

### Editor Experience

#### 概要

Windows でのウィンドウ枠線カラー、エディタタブインデックス表示、スクロールバーの可視性制御、Issue Reporter の改善など、エディタの視覚面とユーザビリティを向上させる機能が複数追加された。

#### 機能詳細

#### Window border color support on Windows

Windows 環境で VS Code ウィンドウに色付きの枠線を表示できるようになった。

- **何が変わったか**: ウィンドウ枠線のカラーを設定可能に。ワークスペースごとに異なる色を設定でき、複数ウィンドウの識別が容易に
- **関連する設定項目**: `window.border` — `default`/`system`/`off`/カラー値（Hex/RGB/RGBA/HSL/HSLA）
- `default` 設定時は `window.activeBorder`/`window.inactiveBorder` カラーキーによるテーマカスタマイズが可能。`workbench.colorCustomizations` で上書きも可能
- **ステータス**: **[GA]**
- **対象ユーザー**: Windows ユーザー

> 📷 [画像: 異なる枠線カラーを持つ複数の VS Code ウィンドウ](https://code.visualstudio.com/assets/updates/1_104/border.png)

#### Manage extension account preference

拡張機能が使用する認証アカウントを変更するコマンドが追加された。

- **何が変わったか**: **Accounts: Manage Extension Account Preferences** コマンドで、認証アカウントにアクセスしている拡張機能の一覧を表示し、使用するアカウントを変更可能。新しいアカウントへのサインインもリストから直接可能
- **ステータス**: **[GA]**
- **対象ユーザー**: 複数の認証アカウントを使い分ける開発者

#### Editor tab index

エディタタブにインデックス番号を表示できるようになった。

- **何が変わったか**: タブのラベルにインデックス番号を表示し、キーボードショートカットによるタブ切り換えを支援
- **関連する設定項目**: `workbench.editor.showTabIndex`
- **ステータス**: **[GA]**
- **対象ユーザー**: 多数のタブを開いてキーボードで操作するユーザー

> 📷 [画像: インデックス番号が表示されたエディタタブ](https://code.visualstudio.com/assets/updates/1_104/editorTabIndex.png)

#### Editor tab bar scrollbar visibility

エディタタブバーのスクロールバー表示タイミングを制御できるようになった。

- **何が変わったか**: スクロールバーの表示を `auto`（ホバー時のみ）/`visible`（常時）/`hidden`（非表示）から選択可能に
- **関連する設定項目**: `workbench.editor.titleScrollbarVisibility` — デフォルトは `auto`
- **ステータス**: **[GA]**
- **対象ユーザー**: タブバーの表示をカスタマイズしたいユーザー

#### Issue reporter improvements

Issue Reporter でレポートの作成方法を選択できるようになった。

- **何が変わったか**: レポートボタンのドロップダウンから **Create on GitHub** または **Preview on GitHub** を選択可能に
- **ステータス**: **[GA]**
- **対象ユーザー**: VS Code や拡張機能のバグ報告を行うすべてのユーザー

> 📷 [画像: Issue Reporter のドロップダウンメニュー](https://code.visualstudio.com/assets/updates/1_104/issue-reporter-dropdown.png)

### Notebooks

#### 概要

ノートブック向けの Next Edit Suggestions の品質向上が実験的に導入された。

#### 機能詳細

#### Improved NES suggestions (Experimental)

ノートブックでの Next Edit Suggestions の品質を向上させる実験的機能が追加された。

- **何が変わったか**: 従来はアクティブセルの内容のみを参照していたが、ノートブック全体の内容にアクセスしてより正確なサジェストを生成可能に
- **関連する設定項目**: `github.copilot.chat.notebook.enhancedNextEditSuggestions.enabled`
- **ステータス**: **[Experimental]**
- **対象ユーザー**: Jupyter Notebook で Copilot を使用する開発者

### Source Control

#### 概要

Git worktree の変更をプレビューし、ワークスペースに移行する機能が追加された。

#### 機能詳細

#### Preview and migrate Git worktree changes

Git worktree のファイルを現在のワークスペースと比較し、変更をマージできるようになった。

- **何が変わったか**:
  - Source Control Changes ビューで worktree ファイルを右クリック → **Compare with Workspace** で差分プレビュー
  - **Migrate Worktree Changes...** コマンド（`git.migrateWorktreeChanges`）で worktree の変更を現在のワークスペースにマージ
- **ステータス**: **[GA]**
- **対象ユーザー**: Git worktree を使用する開発者

> 📷 [画像: worktree ファイルの比較コンテキストメニュー](https://code.visualstudio.com/assets/updates/1_104/image.png)

### Terminal

#### 概要

ターミナルウィンドウの発見可能性向上、エディタ内ターミナルのアクション統一、IntelliSense の改善、sticky scroll のデフォルト有効化など、ターミナル全体の UX が大幅に強化された。

#### 機能詳細

#### Terminal window discoverability and polish

ターミナルを別ウィンドウで開く機能のエントリポイントが増設された。

- **何が変わったか**:
  - 新コマンド `workbench.action.terminal.newInNewWindow`
  - 空のエディタ・タブウェルメニューに「New Terminal」エントリ追加
  - ターミナルドロップダウンに「New Terminal Window」エントリ追加
  - トップレベルターミナルメニューに「New Terminal Window」エントリ追加
  - 別ウィンドウがコンパクトモードで開き、新しいタブ追加時に自動的にコンパクトモードを解除
- **ステータス**: **[GA]**
- **対象ユーザー**: ターミナルを別ウィンドウで使用したいすべてのユーザー

> 📷 [画像: コンパクトモードのターミナルウィンドウ](https://code.visualstudio.com/assets/updates/1_104/terminal-window.png)

#### Terminal actions in terminal editors

ターミナルビューで利用可能なアクション（新規ターミナル、クリア等）が、エディタエリアやターミナルウィンドウのターミナルでも利用可能になった。

- **何が変わったか**: ターミナルのアクションが表示場所に関わらず統一された
- **ステータス**: **[GA]**
- 右クリックでオーバーフローメニューからアクションを移動可能

> 📷 [画像: エディタアクションメニューのターミナルアクション](https://code.visualstudio.com/assets/updates/1_104/terminal-editor-actions.png)

#### Terminal IntelliSense improvements (Preview)

ターミナル IntelliSense が複数の面で改善された。

- **何が変わったか**:
  - パフォーマンス改善（特に Windows 環境で顕著）
  - `git` 補完が Windows でより信頼性が向上（`sed` 依存の廃止）
  - `git` 補完にコミット・ブランチ・リモート・スタッシュ・タグの馴染みのあるアイコンが追加
  - 多数の補完スペック追加: `adb`、`basename`、`bundle`、`clear`、`cut`、`date`、`dd`、`diff`、`dig`、`dirname`、`docker-compose`、`docker`、`dotnet`、`env`、`export`、`fdisk`、`fmt`、`fold`、`gh`、`go`、`htop`、`id`、`jq`、`ln`、`lsblk`、`lsof`、`mount`、`nl`、`od`、`paste`、`ping`、`pkill`、`readlink`、`rsync`、`ruby`、`ruff`、`sed`、`seq`、`shred`、`sort`、`source`、`split`、`stat`、`su`、`sudo`、`tac`、`tar`、`tee`、`time`、`tr`、`traceroute`、`tree`、`truncate`、`uniq`、`unzip`、`wc`、`where`、`whereis`、`which`、`who`、`xargs`、`xxd`、`yo`、`zip`
- **ステータス**: **[Preview]**

> 📷 [画像: git checkout での新アイコン表示](https://code.visualstudio.com/assets/updates/1_104/terminal-suggest.png)

#### Terminal sticky scroll improvements

ターミナルの sticky scroll がデフォルトで有効化され、ページャー使用時の動作改善や `editor.tabFocusMode` 設定との互換性が確保された。

- **何が変わったか**: sticky scroll がデフォルト有効に。ページャー使用時の改善、tab focus mode との互換性向上
- **ステータス**: **[GA]**
- **対象ユーザー**: ターミナルを使用するすべてのユーザー

### Languages

#### 概要

JavaScript/TypeScript では非推奨の bower.json IntelliSense が削除された。Python では Pipenv サポート、AI ホバーサマリー、コードスニペット実行ツールなど、多くの新機能が追加された。

#### 機能詳細

#### JavaScript and TypeScript

bower.json のビルトイン IntelliSense が削除された。

- **何が変わったか**: 2017年に非推奨となった Bower のサポートを削除。使用率が低く、積極的なメンテナンスが行われていなかったため
- **対処法**: Bower から `npm` または `yarn` への移行を推奨。拡張機能による継続サポートは可能
- **対象ユーザー**: bower.json IntelliSense を使用していたユーザー（ごく少数）

#### Python

##### Python Environments extension support for Pipenv

Pipenv 環境の検出と選択が Python 拡張機能と同様にサポートされた。

- **何が変わったか**: Pipenv 環境が Environment Manager ビューに表示され、他の環境タイプと並んでグループ化・表示される
- **ステータス**: **[GA]**
- **対象ユーザー**: Pipenv を使用する Python 開発者

> 📷 [画像: Python サイドバーの Pipenv 環境表示](https://code.visualstudio.com/assets/updates/1_104/pipenv-supported-screenshot.png)

##### Configure environment variable injection

`.env` ファイルからの環境変数注入を制御する新設定が追加された。

- **何が変わったか**: Python Environments 拡張機能が有効な場合に、`.env` ファイルからの環境変数注入のオン/オフを切り替え可能に
- **関連する設定項目**: `python.useEnvFile`
- **ステータス**: **[GA]**

##### Python Environments extension improvements

Python Environments 拡張機能のバグ修正と改善が継続的に行われている。

- **使い方**: 拡張機能をインストールし、`"python.useEnvironmentsExtension": true` を `settings.json` に追加

##### AI-powered hover summaries with Pylance (Experimental)

ドキュメントのないシンボルに対して AI 生成のホバーサマリーを表示する実験的機能が追加された。

- **何が変わったか**: `python.analysis.aiHoverSummaries` 設定を有効にすると、ドキュメントが存在しないシンボルに対してその場で AI サマリーを生成・表示
- **関連する設定項目**: `python.analysis.aiHoverSummaries`
- **ステータス**: **[Experimental]** — Pylance プレリリース版で利用可能
- **対象ユーザー**: GitHub Copilot Pro、Pro+、Enterprise ユーザー

> 🎬 [動画: Pylance の AI ホバーサマリー](https://code.visualstudio.com/assets/updates/1_104/pylance-hover-summaries.mp4)

##### Run code snippet tool

GitHub Copilot がPython コードスニペットをメモリ内で直接実行できるツールが追加された。

- **何が変わったか**: `python -c "code"` やテンポラリファイルの代わりに、ワークスペースの正しい Python インタプリタを使ってメモリ内でスニペットを実行。シェルエスケープの問題も回避
- **使い方**: Pylance プレリリース版をインストールし、Chat ビューの **Add context...** > **Tools** メニューから `pylancerunCodeSnippet` ツールを選択
- **ステータス**: **[GA]**（Pylance プレリリース版）
- **対象ユーザー**: エージェントモードで Python コードの検証を行うユーザー

> 🎬 [動画: pylancerunCodeSnippet ツールによるコード実行](https://code.visualstudio.com/assets/updates/1_104/pylance-run-code-snippet.mp4)

##### Pylance IntelliSense enabled in all Python documents

Pylance IntelliSense がすべての Python ドキュメント（ターミナル、diff ビューを含む）でデフォルト有効になった。

- **何が変わったか**: `python.analysis.supportAllPythonDocuments` 設定が削除され、全 Python ドキュメントで IntelliSense がデフォルト有効に
- **ステータス**: **[GA]**（Pylance プレリリース版）

##### Activation hooks

Python のアクティベーションフックがシェル統合スクリプトから実行可能になった。

- **何が変わったか**: シェルプロファイルの変更が不要になり、より信頼性の高いターミナルアクティベーションが実現。Copilot ターミナルが正しくアクティベートされることも保証
- **関連する設定項目**: `python-envs.terminal.autoActivationType` を `shellStartup` に設定時に有効
- **ステータス**: **[GA]**

### Contributions to extensions

#### 概要

GitHub Pull Requests 拡張機能に複数の改善が追加された。

#### 機能詳細

#### GitHub Pull Requests

- 狭いウィンドウでサイドバーコンテンツが折りたたまれるように改善
- PR と Issue の Webview がリロード後に復元されるようになった
- 新しい「TODO」Code Action で Copilot coding agent に直接委任可能
- `githubPullRequests.ignoreSubmodules` 設定でサブモジュールを無視可能
- **ステータス**: **[GA]**
- 詳細は [changelog for 0.118.0](https://github.com/microsoft/vscode-pull-request-github/blob/main/CHANGELOG.md#01180) を参照

## 設定項目まとめ

### Chat

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `chat.tools.edits.autoApprove` | 確認が必要な機密ファイルのパターンを設定 | システムフォルダ・dotfile・ワークスペース外 | GA |
| `chat.useAgentsMdFile` | AGENTS.md ファイルの自動読み込みを制御 | `true` | Experimental |
| `chat.promptFilesRecommendations` | プロンプトファイル候補の表示条件を設定 | — | Experimental |
| `chat.fontFamily` | Chat ビューのフォントファミリー | — | GA |
| `chat.fontSize` | Chat ビューのフォントサイズ | — | GA |
| `chat.agentSessionsViewLocation` | Chat Sessions ビューの表示位置 | — | Experimental |
| `chat.tools.terminal.enableAutoApprove` | ターミナル自動承認の有効/無効 | — | GA |
| `chat.tools.global.autoApprove` | グローバル自動承認（旧 chat.tools.autoApprove） | — | GA |
| `chat.math.enabled` | 数式レンダリングの有効/無効 | `true` | GA |
| `workbench.secondarySideBar.defaultVisibility` | Secondary Side Bar のデフォルト表示 | 表示 | GA |
| `chat.disableAIFeatures` | AI 機能の無効化・非表示 | — | GA |
| `chat.tools.terminal.shellIntegrationTimeout` | シェル統合のタイムアウト時間 | — | GA |

### MCP

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `chat.mcp.discovery.enabled` | MCP サーバー自動検出の有効/無効 | `false` | GA |
| `chat.mcp.access` | MCP サポートのアクセスレベル（all/none） | — | GA |

### Code Editing

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `editor.inlineSuggest.minShowDelay` | インラインサジェストの最小表示遅延 | — | GA |

### Editor Experience

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `window.border` | ウィンドウ枠線カラー（Windows のみ） | — | GA |
| `workbench.editor.showTabIndex` | タブにインデックス番号を表示 | — | GA |
| `workbench.editor.titleScrollbarVisibility` | タブバースクロールバーの表示 | `auto` | GA |

### Notebooks

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `github.copilot.chat.notebook.enhancedNextEditSuggestions.enabled` | ノートブック全体を参照した NES | — | Experimental |

### Languages (Python)

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `python.useEnvFile` | .env ファイルからの環境変数注入を制御 | — | GA |
| `python.analysis.aiHoverSummaries` | AI ホバーサマリーの有効/無効 | — | Experimental |

### Contributions to extensions

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `githubPullRequests.codingAgent.uiIntegration` | coding agent の UI 統合を制御 | — | Experimental |
| `githubPullRequests.ignoreSubmodules` | サブモジュールを無視 | — | GA |

## Breaking Changes / 非推奨化

1. **`chat.tools.autoApprove` → `chat.tools.global.autoApprove`**: グローバル自動承認の設定名が変更された。自動マイグレーションなし。以前の設定を使用していたユーザーは新しい設定名で再設定が必要。初回使用時に警告ダイアログが表示される。

2. **bower.json IntelliSense の削除**: ビルトインの bower.json IntelliSense が削除された。Bower は 2017 年に非推奨化されており、使用率が低かった。`npm` または `yarn` への移行を推奨。拡張機能による継続サポートは可能。

3. **`python.analysis.supportAllPythonDocuments` の削除**: Pylance IntelliSense がすべての Python ドキュメントでデフォルト有効になったため、この設定は不要となり削除された（Pylance プレリリース版）。

4. **`chat.mcp.enabled` → `chat.mcp.access`**: MCP の有効/無効を制御する設定が boolean から文字列値（`all`/`none`）に変更された。

## 開発者・拡張機能作成者向け

### Finalized APIs

#### shellIntegrationNonce for extension launched terminals

`createTerminal` の `TerminalOptions` と `ExtensionTerminalOptions` に `shellIntegrationNonce` パラメータを渡せるようになった。拡張機能がシェル統合エスケープシーケンスで使用される nonce を制御可能になる。

#### Language Model Chat Provider API

`LanguageModelChatProviders` API がファイナライズされた。拡張機能からクラウドホスト型またはローカルの言語モデルを1つ以上提供可能になり、ユーザーはモデルピッカーからこれらのモデルを選択できる。

- すでに [AI Toolkit for VS Code](https://aka.ms/AIToolkit)、[Cerebras Inference](https://aka.ms/vscode/cerebras)、[Hugging Face](https://aka.ms/vscode/huggingface) が本 API を活用
- [Language Model Chat Provider extension guide](https://code.visualstudio.com/api/extension-guides/ai/language-model-chat-provider) および [extension sample](https://github.com/microsoft/vscode-extension-samples/tree/main/chat-model-provider-sample) を参照
- **注意**: この API から提供されるモデルは現在、[個人向け GitHub Copilot プラン](https://docs.github.com/en/copilot/concepts/billing/individual-plans)のユーザーのみが利用可能

### Proposed APIs

#### Authentication: Supporting `WWW-Authenticate` challenges in `getSession`

> ⚠️ この API はプロポーザル段階であり、今後変更または削除される可能性があります。
> プロポーザルファイル: `vscode.proposed.authenticationChallenges.d.ts`

HTTP の 401 レスポンスに含まれる `WWW-Authenticate` ヘッダーのチャレンジを認証プロバイダーに渡す仕組みが提案された。

- **呼び出し側**: `vscode.authentication.getSession` に `AuthenticationWWWAuthenticateRequest`（`wwwAuthenticate` ヘッダー値と任意のスコープ）を渡せるようになった
- **認証プロバイダー側**: `getSessionsFromChallenges` と `createSessionFromChallenges` メソッドが追加。`AuthenticationProviderOptions` で `supportsChallenges: true` を宣言して登録
- **ユースケース例**: Azure MFA — MFA なしで取得したトークンで Azure API を呼び出し、401 と `WWW-Authenticate` ヘッダーが返却された場合、そのヘッダー値を渡して MFA を満たす新しいセッションを取得

```ts
const newRequest = {
  wwwAuthenticate: theRawHeaderValue,
  scopes: scopesFromPreviousRequest
}
const sessionWithMFA = await vscode.authentication.getSession('microsoft', newRequest, options)
```

- **次のステップ**: 次のイテレーションで `getSession`（呼び出し側）部分がファイナライズ予定。`AuthenticationProvider` 側の変更形状についてフィードバックを募集中
- [プロポーザル全文は GitHub で確認可能](https://github.com/microsoft/vscode/blob/a924f20c72bd8f9665894be8213ce7f5680ab528/src/vscode-dts/vscode.proposed.authenticationChallenges.d.ts)
- MCP サーバーが `WWW-Authenticate` ヘッダーでより多くのスコープを要求する [MCP 仕様プロポーザル](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/835) も関連

#### View containers in the Secondary Side Bar

> ⚠️ この API はプロポーザル段階であり、今後変更または削除される可能性があります。
> プロポーザルファイル: `vscode.proposed.contribSecondarySideBar.d.ts`

拡張機能が `activitybar` と `panel` に加えて `secondarySidebar` にもビューコンテナを提供できるようになった。

- **何が変わったか**: `contribSecondarySideBar` プロポーザル API の背後で Secondary Side Bar へのビューコンテナ提供が可能に
- ファイナライズは近い見込み

## エンジニアリング・基盤改善

### Exploring Playwright and Playwright MCP in the inner development loop of VS Code

VS Code チームが AI 機能を活用した内部開発ループの改善を探求している。既存の [Playwright](https://playwright.dev/) ベースのスモークテスト自動化プロジェクトを拡張し、ローカルの VS Code インスタンスを操作できる MCP サーバーを作成した。

- ビルド/テスト時のアーティファクト（コンパイル、リンター、テスト等）からコンテキストを受け取る既存のエージェントフローに加え、実行中の VS Code インスタンスと対話して変更が実行時に期待通りの効果を持つか検証可能に
- [test/mcp フォルダ](https://github.com/microsoft/vscode/tree/main/test/mcp) にコードが公開されている
- [Contribution Guidelines](https://github.com/microsoft/vscode/wiki/How-to-Contribute) に従ってローカル Code OSS を起動し、[prompt file](https://github.com/microsoft/vscode/blob/cd7de11f65cd5ff6a491f04fc013e363780bde31/.github/prompts/playwright.prompt.md) を使って Agent モードで `/playwright` で質問可能
- [VS Code Insiders podcast](https://www.vscodepodcast.com/3) でも取り上げられた

## Notable fixes

- [vscode#151902](https://github.com/microsoft/vscode/issues/151902) — Terminal: コピーオンセレクション + 1.68 での新しいハイライトで、CMD+F 時に前の用語がコピーされる問題を修正
- [vscode#222075](https://github.com/microsoft/vscode/issues/222075) — ページャーで Page Down 使用時にターミナル sticky scroll が 1 フレーム表示される問題を修正
- [xtermjs/xterm.js#5390](https://github.com/xtermjs/xterm.js/pull/5390) — alt バッファ終了後のスクロールバーテレポートを修正

## コミュニティ貢献

主要な外部コントリビューションをピックアップする。

- **[@SimonSiefke](https://github.com/SimonSiefke)**: パターン入力ウィジェット、codelens コントローラー、アクセシビリティシグナルスケジューラー、QuickDiffModel の 4 件のメモリリークを修正（[#258152](https://github.com/microsoft/vscode/pull/258152)、[#263136](https://github.com/microsoft/vscode/pull/263136)、[#263147](https://github.com/microsoft/vscode/pull/263147)、[#265007](https://github.com/microsoft/vscode/pull/265007)）
- **[@swordjjjkkk (Truman)](https://github.com/swordjjjkkk)**: エディタタブにインデックス番号を表示する機能を実装（[#209196](https://github.com/microsoft/vscode/pull/209196)）
- **[@terreng (Terren)](https://github.com/terreng)**: タイトルスクロールバーの表示制御オプションを実装（[#246161](https://github.com/microsoft/vscode/pull/246161)）
- **[@joelverhagen (Joel Verhagen)](https://github.com/joelverhagen)**: MCP アシスト型インストール関連の複数改善（[#259081](https://github.com/microsoft/vscode/pull/259081)、[#259634](https://github.com/microsoft/vscode/pull/259634)、[#260215](https://github.com/microsoft/vscode/pull/260215)）
- **[@rwoll (Ross Wollman)](https://github.com/rwoll)**: 自動化でのエージェントループ完了待機、モデル切り替え、チャットコマンド解析など複数の改善（[#262370](https://github.com/microsoft/vscode/pull/262370)、[#262420](https://github.com/microsoft/vscode/pull/262420)、[#263458](https://github.com/microsoft/vscode/pull/263458)）
- **[@kenherring (Ken Herring)](https://github.com/kenherring)**: terminal.copyOnSelection と findWidget のフォーカス時コピー抑制を修正（[#254065](https://github.com/microsoft/vscode/pull/254065)）
- **[@tmm1 (Aman Karmani)](https://github.com/tmm1)**: disposable リーク修正、SQLite insert の upsert 構文最適化など（[#261710](https://github.com/microsoft/vscode/pull/261710)、[#261999](https://github.com/microsoft/vscode/pull/261999)）
- **[@kplates](https://github.com/kplates)**: ファイル検索でのファイルタイプ包含/除外機能（[#254285](https://github.com/microsoft/vscode/pull/254285)）

## まとめと所感

VS Code v1.104 は、エージェントモードの「安全に使える」基盤整備に重点が置かれたリリースである。ターミナル自動承認の多層的な安全対策、機密ファイル編集の確認プロンプト、グローバル自動承認の見直しなど、ユーザーが意図せずリスクを負うことを防ぐ仕組みが丁寧に設計されている。`LanguageModelChatProviders` API のファイナライズにより、サードパーティモデルのエコシステムが正式に開かれた点も重要である。Python 開発者にとっては Pipenv サポート、AI ホバーサマリー、コードスニペット実行ツールが実務的な改善をもたらす。Playwright MCP による内部開発ループの探求は、VS Code チーム自身が AI エージェントを開発プロセスに深く組み込む方向性を示しており、今後の展開が注目される。
