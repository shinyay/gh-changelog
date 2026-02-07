---
title: "Visual Studio Code June 2025 (v1.102) 日本語詳細解説"
date: "2025-07-09"
version_ref: "v1_102"
source_url: "https://code.visualstudio.com/updates/v1_102"
lang: "ja"
---

# Visual Studio Code June 2025 (v1.102) 日本語詳細解説

## リリース概要

VS Code v1.102（2025年6月）は、GitHub Copilot Chat 拡張機能のオープンソース化と MCP サポートの GA（一般提供）を二大マイルストーンとするリリースである。Chat 領域ではカスタムモードの改善、カスタムインストラクションの自動生成、ターミナル自動承認やリクエスト編集の実験的機能が導入された。MCP では Elicitations 対応、サーバー管理ビュー、プロファイル統合、Dev Container 対応など、開発者体験が一気にプロダクショングレードに引き上げられている。また、Copilot coding agent セッションの開始・追跡機能が GitHub Pull Requests 拡張機能に統合され、バックグラウンドでのタスク委任フローが実現した。なお、1.102.1〜1.102.3 で複数のバグ修正リカバリが提供されている。

## 注目の新機能・変更点

1. **GitHub Copilot Chat のオープンソース化** — `microsoft/vscode-copilot-chat` リポジトリが MIT ライセンスで公開され、コミュニティによるエージェントモード・インラインチャット・MCP 統合の実装確認・貢献が可能に。
2. **MCP サポートの GA** — MCP が VS Code で一般提供開始。GitHub Copilot ポリシーによる組織レベルのサーバー制御も可能に。
3. **MCP サーバーの管理ビューとギャラリー** — Extensions ビュー内に MCP サーバーの管理セクションが追加され、Web ギャラリーからのワンクリックインストールが可能に。
4. **MCP サーバーのプロファイル統合** — MCP サーバーが専用 `mcp.json` で管理されるファーストクラスリソースとなり、Settings Sync にも対応。
5. **カスタムインストラクションの自動生成** — `Chat: Generate Instructions` コマンドでコードベースを分析し、プロジェクトに適したインストラクションを自動生成。
6. **ターミナル自動承認（Experimental）** — 許可リスト・拒否リストによるターミナルコマンドの自動承認メカニズムが導入された。
7. **Copilot coding agent セッション（Preview）** — `#copilotCodingAgent` ツールでローカルの変更を coding agent に引き継ぎ、バックグラウンドで処理可能に。
8. **以前のリクエスト編集（Experimental）** — チャットの過去リクエストをクリックしてテキスト・コンテキスト・モード・モデルを変更し再送信可能に。
9. **チャットモードの改善** — 言語モデルの指定、vscode リンクによるモード・プロンプト・インストラクションのインポートが可能に。
10. **ミドルクリックスクロール** — エディタでマウスのミドルボタンによるスクロールが可能に。

## セクション別詳細解説

### Chat

#### 概要

Chat セクションは本リリース最大の領域であり、Copilot Chat のオープンソース化を筆頭に、カスタムモード改善、インストラクション自動生成・オンデマンド読み込み、ターミナル自動承認、リクエスト編集、CLI からのチャット開始など 15 以上の機能改善が含まれる。

#### 機能詳細

#### Copilot Chat is open source

GitHub Copilot Chat 拡張機能がオープンソース化された。

- **何が変わったか**: `microsoft/vscode-copilot-chat` リポジトリが MIT ライセンスで公開。エージェントモード、インラインチャット、MCP 統合の実装をコミュニティが閲覧・貢献可能に
- **ステータス**: **[GA]**
- **対象ユーザー**: すべての VS Code ユーザーおよび Copilot 拡張機能開発者
- 詳細ブログ: [Open Source AI Editor - First Milestone](https://code.visualstudio.com/blogs/2025/06/30/openSourceAIEditorFirstMilestone)

#### Chat mode improvements

カスタムチャットモードに複数の改善が加えられた。

- **何が変わったか**:
  - **言語モデルの指定**: `chatmode.md` ファイルの `model` メタデータでモデルを指定可能に。IntelliSense によるモデル ID 補完もサポート
  - **編集サポートの強化**: チャットモード・プロンプト・インストラクションファイルのエディタで、すべてのメタデータプロパティに対する補完・バリデーション・ホバーが利用可能に
  - **Configure Chat メニュー**: Chat ビューのツールバーからカスタムモード、インストラクション、プロンプト、ツールセットを一元管理
  - **vscode リンクによるインポート**: gist や [awesome-copilot](https://github.com/github/awesome-copilot) リポジトリなどの外部リンクからチャットモード・プロンプト・インストラクションファイルをインポート可能に
- **ステータス**: **[GA]**
- **対象ユーザー**: カスタムチャットモードを活用するすべてのユーザー

> 📷 [画像: chatmode.md でのモデル指定 IntelliSense](https://code.visualstudio.com/assets/updates/1_102/prompt-file-model-code-completion.png)

> 📷 [画像: ツールのホバー情報](https://code.visualstudio.com/assets/updates/1_102/tools-hover.png)

> 📷 [画像: Configure Chat メニュー](https://code.visualstudio.com/assets/updates/1_102/chat-gear.png)

#### Generate custom instructions

`Chat: Generate Instructions` コマンドによるカスタムインストラクションの自動生成が導入された。

- **何が変わったか**: コマンドパレットまたは Chat ビューの Configure メニューから実行すると、エージェントモードがコードベースを分析し、プロジェクトの構造・技術・パターンに合わせたインストラクションを生成。`.github/copilot-instructions.md` ファイルを作成、または既存ファイルの改善を提案
- **ステータス**: **[GA]**
- **対象ユーザー**: カスタムインストラクションの設定を始めたいすべてのユーザー
- **使い方**: コマンドパレットで `Chat: Generate Instructions` を実行

#### Load instruction files on demand

インストラクションファイルのオンデマンド読み込みが可能になった。

- **何が変わったか**: LLM がリクエストごとにすべてのインストラクションファイル（glob パターン・説明付き）のリストを受け取り、必要に応じてオンデマンドで読み込むようになった。明示的にコンテキストに追加されていないファイルも LLM が自律的に参照可能
- **ステータス**: **[GA]**
- **対象ユーザー**: `.instructions.md` ファイルを使用するプロジェクト

> 📷 [画像: LLM によるインストラクションファイルのオンデマンド読み込み](https://code.visualstudio.com/assets/updates/1_102/instructions-loading-on-demand.png)

#### Edit previous requests (Experimental)

以前のチャットリクエストを編集・再送信する実験的機能が導入された。

- **何が変わったか**: 過去のリクエストをクリックしてテキスト・添付コンテキスト・モード・モデルを変更可能。変更を送信すると後続のリクエストが削除され、編集が元に戻され、新しいリクエストとして送信される
- **関連する設定項目**: `chat.editRequests` — `inline`（リクエスト上でインライン編集）、`hover`（ホバーツールバーからインライン編集）、`input`（入力ボックスで編集）の 3 モードから選択
- **ステータス**: **[Experimental]**
- **対象ユーザー**: チャットの試行錯誤を効率化したいユーザー

> 🎬 [動画: 以前のリクエストの編集プロセス](https://code.visualstudio.com/assets/updates/1_102/edit-previous-requests.mp4)

#### Terminal auto approval (Experimental)

エージェントモードにターミナルコマンドの自動承認メカニズムが導入された。

- **何が変わったか**:
  - **許可リスト（allowList）**: コマンドプレフィックスまたは正規表現にマッチするコマンドを承認なしで実行可能に
  - **拒否リスト（denyList）**: allowList をオーバーライドして特定のコマンドを強制承認に
  - チェーンコマンド（`&&`）やインラインコマンド（`$()`）も各サブコマンドを個別にチェック
  - 設定はユーザースコープとワークスペーススコープでマージされる
- **関連する設定項目**: `github.copilot.chat.agent.terminal.allowList`、`github.copilot.chat.agent.terminal.denyList`
- **ステータス**: **[Experimental]**
- **対象ユーザー**: エージェントモードを頻繁に使用するユーザー
- 次のリリースで `github.copilot.` プレフィックスの削除と設定の統合が計画されている

```json
"github.copilot.chat.agent.terminal.allowList": {
  "npm run test": true,
  "/^git (status|log)$/": true
}
```

> 🎬 [動画: ターミナルコマンドの自動承認デモ](https://code.visualstudio.com/assets/updates/1_102/terminal-auto-approve.mp4)

#### Terminal command simplification

エージェントモードが `cd` 文を含むコマンドを簡略化するようになった。

- **何が変わったか**: 現在の作業ディレクトリと一致する `cd` コマンドが自動的に除去され、簡略化されたコマンドが実行される
- **ステータス**: **[GA]**

> 📷 [画像: cd コマンドの簡略化](https://code.visualstudio.com/assets/updates/1_102/terminal-working-dir.png)

#### Agent awareness of tasks and terminals

エージェントモードがバックグラウンドターミナルと実行中タスクを認識するようになった。

- **何が変わったか**: エージェントが作成したバックグラウンドターミナルとアクティブなタスクを把握可能に。新しい `GetTaskOutput` ツールでタスク出力を読み取り、重複タスクの実行を防止
- **ステータス**: **[GA]**

> 📷 [画像: ビルドタスクのステータスをエージェントが要約](https://code.visualstudio.com/assets/updates/1_102/task-status.png)

#### Maximized chat view

Secondary Side Bar を最大化してエディタ領域全体に拡大する機能が追加された。

- **何が変わったか**: 最大化・復元をトグルするアイコンが追加。状態はリスタート間で保持される。コマンド `workbench.action.toggleMaximizedAuxiliaryBar` も利用可能
- **ステータス**: **[GA]**

> 🎬 [動画: Secondary Side Bar の最大化](https://code.visualstudio.com/assets/updates/1_102/auxmax.mp4)

#### Agent mode badge indicator

エージェントがユーザー確認を必要とする際にアプリケーションアイコンにバッジを表示するようになった。

- **何が変わったか**: ウィンドウがフォーカスされていない状態でエージェントが確認を必要とするとき、Dock アイコンにバッジが表示される。関連ウィンドウがフォーカスされると消える
- **関連する設定項目**: `chat.notifyWindowOnConfirmation`
- **ステータス**: **[GA]**

#### Start chat from the command line

VS Code CLI に `chat` サブコマンドが追加された。

- **何が変わったか**: `code chat [options] [prompt]` でコマンドラインからチャットセッションを開始可能に
- **オプション**:
  - `-m --mode <mode>`: チャットモード（ask/edit/agent/カスタムモード、デフォルト: agent）
  - `-a --add-file <path>`: コンテキストにファイルを追加
  - `--maximize`: Chat ビューを最大化
  - `-r --reuse-window` / `-n --new-window`: ウィンドウ制御
  - stdin からの読み込みもサポート（末尾に `-` を付加）
- **ステータス**: **[GA]**

> 🎬 [動画: Chat CLI によるチャットセッション開始](https://code.visualstudio.com/assets/updates/1_102/chatcli.mp4)

#### Fetch tool supports non-HTTP URLs

Fetch ツールが `file://` URL などの非 HTTP URL をサポートするようになった。

- **何が変わったか**: モデルが `file://` URL で Fetch ツールを呼び出した場合、そのファイルまたはリソースのコンテンツを返す。画像もサポート
- **ステータス**: **[GA]**

#### Clearer language model access management

拡張機能の言語モデルアクセス管理の UX が改善された。

- **何が変わったか**: Account メニューの紛らわしい「AccountName (GitHub Copilot Chat)」項目を削除し、新しい「**Manage Language Model Access...**」項目に置換。Quick Pick で拡張機能のモデルアクセス権限を管理可能に
- **ステータス**: **[GA]**
- 今後、モデル単位のより細かいアクセス制御が検討される予定

> 📷 [画像: 言語モデルアクセス管理 Quick Pick](https://code.visualstudio.com/assets/updates/1_102/lm-access-qp.png)

#### Reading chat requests

Copilot Chat のデバッグビューが一般ユーザーにも公開された。

- **何が変わったか**: `Show Chat Debug View` コマンドで、各リクエストのプロンプト全文・有効なツール・レスポンス・ツール呼び出しなどの詳細情報をツリービューで確認可能に。右クリックの「Export As...」でログを保存可能
- **ステータス**: **[GA]**
- **注意**: ログにはファイル内容やターミナル出力などの個人情報が含まれる場合がある。共有前に内容を確認すること

#### Edit Tool Improvements

GPT-4 モデルおよび Sonnet モデルの編集ツールの予測可能性と信頼性が向上した。

- **何が変わったか**: 編集動作の信頼性が向上。今後も改善が継続される
- **ステータス**: **[GA]**

### MCP

#### 概要

MCP セクションでは、MCP サポートの GA 化を中心に、Elicitations 対応、サーバー管理ビュー・ギャラリー、プロファイル統合・Settings Sync 対応、Dev Container 対応、認証管理の簡素化など、MCP エコシステムの成熟を示す多数の改善が含まれる。

#### 機能詳細

#### MCP support in VS Code is generally available

MCP サポートが VS Code で一般提供開始された。

- **何が変わったか**: 過去数ヶ月にわたる MCP 仕様の全機能サポートを経て、MCP が GA に到達。組織は GitHub Copilot ポリシーで MCP サーバーの利用可能性を制御可能
- **ステータス**: **[GA]**
- **対象ユーザー**: すべての VS Code ユーザー
- **使い方**: [キュレーションリスト](https://code.visualstudio.com/mcp)から MCP サーバーをインストール

> 📷 [画像: MCP Servers ページ](https://code.visualstudio.com/assets/updates/1_102/mcp-servers-page.png)

#### Support for elicitations

最新の MCP 仕様に追加された Elicitations をサポートした。

- **何が変わったか**: MCP サーバーが MCP クライアント（VS Code）にユーザー入力を要求できる [Elicitations](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation) 仕様に対応
- **ステータス**: **[GA]**
- **対象ユーザー**: Elicitations を使用する MCP サーバーの利用者・開発者

> 🎬 [動画: MCP サーバーの Elicitation デモ](https://code.visualstudio.com/assets/updates/1_102/mcp-server-elicit.mp4)

#### MCP server discovery and installation

Extensions ビューに MCP サーバーのディスカバリ・インストール機能が追加された。

- **何が変わったか**: Extensions ビューに「MCP Servers」セクションが追加。Web ギャラリーで **Install** を選択すると VS Code が起動し、サーバーの readme とマニフェスト情報を確認後にインストール可能。インストール後は Extensions ビューの「MCP SERVERS - INSTALLED」セクションに表示され、ツールが Chat ビューの Quick Pick で利用可能に
- **ステータス**: **[GA]**

> 🎬 [動画: MCP サーバーのインストールフロー](https://code.visualstudio.com/assets/updates/1_102/mcp-servers-discovery-install.mp4)

#### MCP server management view

Extensions ビューに MCP サーバーの管理ビューが追加された。

- **何が変わったか**: 「MCP SERVERS - INSTALLED」ビューでインストール済みサーバーの一覧・コンテキストメニュー操作が可能に:
  - **Start/Stop/Restart Server**: サーバーの実行状態を制御
  - **Disconnect Account**: アカウントアクセスの削除
  - **Show Output**: トラブルシューティング用のサーバー出力ログを表示
  - **Show Configuration**: ランタイム設定を開く
  - **Configure Model Access**: モデルアクセス権限を管理
  - **Show Sampling Requests**: デバッグ用のサンプリングリクエストを表示
  - **Browse Resources**: サーバー提供リソースを探索
  - **Uninstall**: サーバーの削除
- サーバー選択時にエディタで readme・マニフェスト・ランタイム設定を表示
- **ステータス**: **[GA]**

> 📷 [画像: MCP サーバー管理ビュー](https://code.visualstudio.com/assets/updates/1_102/mcp-servers-installed-view.png)

> 📷 [画像: MCP サーバーのコンテキストメニュー](https://code.visualstudio.com/assets/updates/1_102/mcp-server-context-menu.png)

> 📷 [画像: MCP サーバーエディタとランタイム設定](https://code.visualstudio.com/assets/updates/1_102/mcp-server-editor-configuration.png)

#### MCP servers as first class resources

MCP サーバーがプロファイル統合のファーストクラスリソースとして扱われるようになった。

- **何が変わったか**:
  - **専用ストレージ**: MCP サーバーがユーザー設定ではなく、プロファイルごとの `mcp.json` ファイルに保存
  - **プロファイル固有**: 各 VS Code プロファイルが独自の MCP サーバーセットを保持。ワークフローやプロジェクトごとに異なるサーバー構成が可能
  - **Settings Sync 統合**: MCP サーバーが Settings Sync でデバイス間同期。同期内容の細粒度制御が可能
- **ステータス**: **[GA]**
- **対象ユーザー**: すべての MCP サーバー利用者

##### MCP migration support

既存の MCP 設定からの自動マイグレーションが提供される。

- **何が変わったか**: `settings.json` 内の既存 MCP サーバー設定を自動検出し、プロファイル固有の `mcp.json` に移行。リアルタイムマイグレーションでは即座に通知が表示される。ローカル・リモート・WSL・Codespaces すべてに対応
- **ステータス**: **[GA]**

##### Dev Container support for MCP configuration

Dev Container の設定ファイルで MCP サーバーの構成がサポートされた。

- **何が変わったか**: `devcontainer.json` および `devcontainer-feature.json` で `customizations.vscode.mcp` パスに MCP サーバー設定を記述可能。コンテナ作成時にリモートの `mcp.json` に書き込まれる
- **ステータス**: **[GA]**

```json
{
  "image": "mcr.microsoft.com/devcontainers/typescript-node:latest",
  "customizations": {
    "vscode": {
      "mcp": {
        "servers": {
          "playwright": {
            "command": "npx",
            "args": ["@playwright/mcp@latest"]
          }
        }
      }
    }
  }
}
```

##### Commands to access MCP resources

MCP 設定ファイルへのアクセスコマンドが追加された。

- **何が変わったか**: **MCP: Open User Configuration** と **MCP: Open Remote User Configuration** コマンドで `mcp.json` ファイルに直接アクセス可能
- **ステータス**: **[GA]**

#### Quick management of MCP authentication

MCP 認証の管理が簡素化された。

- **何が変わったか**: MCP ビューの歯車メニュー、MCP エディタの歯車メニュー、Quick Pick からアカウントのサインアウトまたは切断が可能に。**Disconnect** は他の MCP サーバーや拡張機能もアカウントを使用している場合に表示され、**Sign Out** はそのサーバーのみが使用している場合に表示される
- **ステータス**: **[GA]**

> 📷 [画像: MCP ビュー歯車メニューでの Disconnect Account](https://code.visualstudio.com/assets/updates/1_102/mcp-view-signout.png)

> 📷 [画像: MCP Quick Pick での Disconnect Account](https://code.visualstudio.com/assets/updates/1_102/mcp-qp-signout.png)

### Accessibility

#### 概要

アクセシビリティではエディタ内からの全編集の承認、ユーザーアクション必要時のサウンド通知、チャットレンダリングエラーのアラートが追加された。

#### 機能詳細

#### Keep all edits from within the editor

エディタにフォーカスがある状態で全編集を承認可能になった。

- **何が変わったか**: 従来 Chat ビューにフォーカスが必要だった「Keep All Edits」操作が、エディタからも `chatEditor.action.acceptAllEdits` コマンドで実行可能に
- **ステータス**: **[GA]**

#### User action required sound

チャットがユーザーアクションを必要とする際のサウンドシグナルが調整された。

- **何が変わったか**: デフォルト値が `auto` に設定され、スクリーンリーダー使用者にサウンド通知が自動的に有効化される
- **関連する設定項目**: `accessibility.signals.chatUserActionRequired`
- **ステータス**: **[GA]**

#### Alert when rendering errors occur in chat

チャットのレンダリングエラー時にスクリーンリーダーユーザーへのアラートが追加された。

- **何が変わったか**: 従来通知されなかったレンダリングエラーが、アラートとしてスクリーンリーダーに伝達され、キーボードでフォーカス可能に
- **ステータス**: **[GA]**

### Code Editing

#### 概要

エディタでのミドルクリックスクロールとインラインサジェスチョンのスヌーズ機能が新たに追加された。

#### 機能詳細

#### Scroll on middle click

マウスのミドルボタン（スクロールホイール）でエディタをスクロールする機能が追加された。

- **何が変わったか**: ミドルボタンをクリック（または長押し）すると、カーソルがパニングアイコンに変わり、マウス移動に応じてスムーズにスクロール。クリックポイントからの距離でスクロール速度が決定。ミドルボタンを離すか再クリックで終了
- **関連する設定項目**: `editor.scrollOnMiddleClick:true`
- **ステータス**: **[GA]**
- **既知の競合**: `editor.columnSelection`（列選択）や `editor.selectionClipboard`（Linux の選択クリップボード）との干渉あり。同時に有効にしないことを推奨

> 🎬 [動画: ミドルクリックスクロール](https://code.visualstudio.com/assets/updates/1_102/middle-scroll.mp4)

#### Snooze code completions

インラインサジェスチョンと Next Edit Suggestions (NES) を一時停止する機能が追加された。

- **何が変わったか**: ステータスバーの Copilot ダッシュボードまたはコマンドパレットの **Snooze Inline Suggestions** から、一定時間サジェスチョンを抑制可能。カスタムキーバインドで特定の時間を指定することも可能
- **ステータス**: **[GA]**
- **使い方**: Copilot ダッシュボードでスヌーズ時間を選択

```json
{
  "key": "...",
  "command": "editor.action.inlineSuggest.snooze",
  "args": 10
}
```

> 📷 [画像: Copilot ダッシュボードのスヌーズボタン](https://code.visualstudio.com/assets/updates/1_102/nes-snooze.png)

### Editor Experience

#### 概要

Windows アクセントカラーのサポートと設定エディタの AI 検索トグルのプレビューが追加された。

#### 機能詳細

#### Windows accent color

Windows のアクセントカラーをウィンドウフレームの枠線に使用する機能が追加された。

- **何が変わったか**: Windows の設定で「タイトルバーとウィンドウの枠線にアクセントカラーを表示する」が有効な場合、VS Code のウィンドウ枠線にアクセントカラーが反映される
- **関連する設定項目**: `window.border` — `default`（Windows のアクセントカラーを使用）、`off`（無効）、またはカスタムカラー値
- **ステータス**: **[GA]**
- **対象ユーザー**: Windows ユーザー
- 現時点ではワークスペースごとの設定は不可だが、対応予定

> 📷 [画像: 赤いアクセントカラーの枠線](https://code.visualstudio.com/assets/updates/1_102/window-accent.png)

#### Settings search suggestions (Preview)

設定エディタのスパークルトグルが AI 検索結果と通常検索結果の切り替えとして機能するようになった。

- **何が変わったか**: AI 検索結果は文字列マッチングではなくセマンティック類似性に基づく結果を表示。例えば「increase text size」で `editor.fontSize` が表示される。AI 結果がある場合のみトグルが有効化
- **関連する設定項目**: `workbench.settings.showAISearchToggle:true`
- **ステータス**: **[Preview]**
- 次のイテレーションでデフォルト有効化が計画されている

> 🎬 [動画: 設定エディタでの AI/非 AI 結果切り替え](https://code.visualstudio.com/assets/updates/1_102/settings-search-toggle-stable.mp4)

### Tasks

#### 概要

実行中タスクの一括再実行と、タスク再起動時の `tasks.json` 再読み込みが追加された。

#### 機能詳細

#### Rerun all running tasks

実行中のすべてのタスクを一括再実行するコマンドが追加された。

- **何が変わったか**: `Tasks: Rerun All Running Tasks` コマンドで、複数の並行タスクを個別に停止・再実行する手間なく一括再起動可能に
- **ステータス**: **[GA]**

#### Restart task reloads updated tasks.json

**Restart Task** コマンドが `tasks.json` を再読み込みするようになった。

- **何が変わったか**: タスク再起動前に `tasks.json` を再読み込みし、最新の設定変更が反映されるようになった。従来は設定変更が反映されない場合があった
- **ステータス**: **[GA]**

### Terminal

#### 概要

ターミナルサジェスト機能のプレビューに大幅な改善が加わり、選択モード、複数コマンドサポート、シンボリックリンク情報、ソート改善、Git Bash 改善が含まれる。

#### 機能詳細

#### Terminal Suggest (Preview)

ターミナルサジェスト機能に大幅な改善が加えられた。

##### Selection mode

サジェスチョンの選択モードを制御する設定が追加された。

- **何が変わったか**: デフォルトでは `Tab` でサジェスチョンを受け入れる仕様を明確化。`partial`（デフォルト: ナビゲーション発生まで Tab で受け入れ）、`always`、`never` から選択可能
- **関連する設定項目**: `terminal.integrated.suggest.selectionMode`
- **ステータス**: **[Preview]**

> 📷 [画像: Tab でサジェスチョンを受け入れる表示](https://code.visualstudio.com/assets/updates/1_102/terminal-selection-mode.png)

##### Learn more

サジェストコントロールのステータスバーに「Learn More」アクションが追加された。

- **何が変わったか**: 最初の 10 回または 10 秒間表示されるとハイライトされ、設定・無効化・ドキュメントへの導線として機能
- **ステータス**: **[Preview]**

> 📷 [画像: ステータスバーの Learn More アクション](https://code.visualstudio.com/assets/updates/1_102/terminal-suggest-discoverability.png)

##### Multi-command support

ターミナルサジェストが複数コマンド行に対応した。

- **何が変わったか**: `;`、`&&` 等のシェル演算子でリンクされたコマンドに対して、行内のすべてのコマンドのサジェスチョンを提供
- **ステータス**: **[Preview]**

> 📷 [画像: 複数コマンドラインでのサジェスチョン](https://code.visualstudio.com/assets/updates/1_102/terminal-suggest-multi.png)

##### Symlink information

サジェスト詳細にシンボリックリンクの実際のパスが表示されるようになった。

- **何が変わったか**: シンボリックリンクのファイルとフォルダに専用アイコンが追加され、実パスが表示される
- **ステータス**: **[Preview]**

> 📷 [画像: シンボリックリンクのパス表示](https://code.visualstudio.com/assets/updates/1_102/terminal-symlink.png)

##### Improved sorting

サジェスチョンのソートが改善された。

- **何が変わったか**: `main` や `master` ブランチが他のブランチより優先表示されるなど、より関連性の高い候補が先に表示される
- **ステータス**: **[Preview]**

> 📷 [画像: main/master ブランチの優先表示](https://code.visualstudio.com/assets/updates/1_102/terminal-suggest-sorting.png)

##### Git bash improvements

Git Bash でのパス補完とビルトインコマンドサジェスチョンが追加された。

- **何が変わったか**: Git Bash のフォルダ・ファイルパス補完が正しくサポートされ、ビルトインコマンドもサジェスチョンとして表示
- **ステータス**: **[Preview]**

> 📷 [画像: Git Bash でのビルトインコマンドサジェスチョン](https://code.visualstudio.com/assets/updates/1_102/terminal-git-bash.png)

### Contributions to extensions

#### 概要

GitHub Pull Requests 拡張機能で Copilot coding agent のセッション開始・ステータス追跡・セッションログが追加され、Python 関連では Python Environments 拡張機能の同梱と Pylance MCP ツールの実験的導入が行われた。GitHub 認証のサインインフローも刷新された。

#### 機能詳細

#### GitHub Pull Requests

##### Start a coding agent session (Preview)

`#copilotCodingAgent` ツールで coding agent セッションを開始可能になった。

- **何が変わったか**: ローカルの変更をリモートブランチに自動プッシュし、ユーザーの指示とともに coding agent セッションを開始。バックグラウンドで変更を処理させることが可能
- **関連する設定項目**: `githubPullRequests.codingAgent.uiIntegration` — 有効にすると Chat ビューに「Delegate to coding agent」ボタンが表示
- **ステータス**: **[Preview]**
- **対象ユーザー**: Copilot coding agent が有効なリポジトリで作業するユーザー

> 📷 [画像: coding agent へのセッション引き継ぎ](https://code.visualstudio.com/assets/updates/1_102/coding-agent-start.png)

##### Status tracking

coding agent PR のステータス追跡が改善された。

- **何が変わったか**: 「Copilot on my behalf」クエリで coding agent PR のステータスが目立つ形で表示され、新しい変更にはバッジ表示
- **ステータス**: **[Preview]**

> 📷 [画像: coding agent PR のステータス表示](https://code.visualstudio.com/assets/updates/1_102/coding-agent-status.png)

##### Session log

coding agent のセッションログが VS Code 内で閲覧可能になった。

- **何が変わったか**: coding agent がとったアクション（コード変更・ツール使用）の履歴を直接確認可能
- **ステータス**: **[Preview]**

> 📷 [画像: coding agent セッションログ](https://code.visualstudio.com/assets/updates/1_102/coding-agent-session-log.png)

##### Enhancements on `#activePullRequest` tool

`#activePullRequest` ツールが coding agent セッション情報も返すようになった。

- **何が変わったか**: coding agent 経由で作成された PR を開く際にツールが自動的にアタッチされ、コンテキストを保ちながら PR 作業を継続可能
- **ステータス**: **[GA]**

#### Python

##### Python Environments extension improvements

Python Environments 拡張機能に複数の改善が加えられた。

- **何が変わったか**:
  - Poetry 2.0.0 以降でのターミナルアクティベーション対応
  - 同一ワークスペース内での複数仮想環境のユニーク命名作成が可能に
  - 生成される `.venv` フォルダがデフォルトで git-ignore に
  - 環境削除プロセスの改善
- **ステータス**: **[GA]**

##### Python Environments included as part of the Python extension

Python Environments 拡張機能が Python 拡張機能のオプショナル依存関係として段階的にロールアウト開始された。

- **何が変わったか**: Python Debugger や Pylance と同様に、Python 拡張機能と一緒に自動インストールされるようになった
- **使い方**: 拡張機能インストール後、`"python.useEnvironmentsExtension": true` を settings.json に追加
- **ステータス**: **[GA]** — 段階的ロールアウト中

##### Disabled PyREPL for Python 3.13

Python 3.13 以上で PyREPL が無効化された。

- **何が変わったか**: インタラクティブターミナルでのインデントとカーソルの問題に対処するため無効化。詳細は [#25164](https://github.com/microsoft/vscode-python/issues/25164) を参照
- **ステータス**: **[GA]**

##### Pylance MCP tools (Experimental)

Pylance 拡張機能に実験的な MCP ツールが追加された。

- **何が変わったか**: Pylance のドキュメント、インポート分析、環境管理などへのアクセスを提供する MCP ツールが追加。Pylance のプレリリース版で利用可能
- **ステータス**: **[Experimental]**
- **対象ユーザー**: Pylance を使用する Python 開発者

#### GitHub authentication

##### Revamped GitHub sign-in flow

GitHub サインインフローが刷新された。

- **何が変わったか**: ループバック URL (`http://localhost:PORT/`) を使用するフローがデフォルトに。カスタム URL スキーム（`vscode://`）に依存しないため信頼性が向上。ループバック URL 到達後にはリダイレクトで VS Code に復帰するため利便性も確保
- **ステータス**: **[GA]**
- ランディングページのデザインも刷新。今後、他のサインイン体験にも新デザインが適用予定

## 設定項目まとめ

### Chat

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `chat.editRequests` | 以前のリクエスト編集の動作モード（inline/hover/input） | — | Experimental |
| `github.copilot.chat.agent.terminal.allowList` | ターミナル自動承認の許可リスト | `{}` | Experimental |
| `github.copilot.chat.agent.terminal.denyList` | ターミナル自動承認の拒否リスト | — | Experimental |
| `chat.notifyWindowOnConfirmation` | エージェント確認時のバッジ表示 | — | GA |

### Accessibility

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `accessibility.signals.chatUserActionRequired` | チャットがユーザーアクション必要時のサウンド | `auto` | GA |

### Code Editing

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `editor.scrollOnMiddleClick` | ミドルクリックスクロールの有効化 | `true` | GA |

### Editor Experience

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `window.border` | ウィンドウ枠線の色 (default/off/カスタム値) | — | GA |
| `workbench.settings.showAISearchToggle` | 設定エディタの AI 検索トグル | `true` | Preview |

### Terminal

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `terminal.integrated.suggest.selectionMode` | サジェスト選択モード (partial/always/never) | `partial` | Preview |

### Contributions to extensions

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `githubPullRequests.codingAgent.uiIntegration` | coding agent UI 統合の有効化 | — | Experimental |
| `python.useEnvironmentsExtension` | Python Environments 拡張機能の有効化 | — | GA |

## Breaking Changes / 非推奨化

1. **MCP サーバー設定の移行**: MCP サーバーが `settings.json` からプロファイル固有の `mcp.json` に移行された。既存設定は自動マイグレーションされるが、`settings.json` からの手動削除が推奨される。
2. **GitHub Copilot Chat の Account メニュー変更**: Account メニューの「AccountName (GitHub Copilot Chat)」が削除され、「Manage Language Model Access...」に置換された。
3. **ターミナル自動承認設定のプレフィックス変更予告**: `github.copilot.chat.agent.terminal.allowList` / `denyList` は次のリリースで `github.copilot.` プレフィックスが削除され、統合される予定。

## 開発者・拡張機能作成者向け

### Finalized APIs

#### Allow opening files when using `vscode.openFolder` command

`vscode.openFolder` コマンドに `filesToOpen` オプションが追加された。

- **何が変わったか**: 拡張機能が `vscode.openFolder` コマンド実行時に、開くファイルを `filesToOpen?: UriComponents[]` として指定可能に

```ts
vscode.commands.executeCommand('vscode.openFolder', <folder uri>, { filesToOpen: [ /* files to open */]});
```

### Proposed APIs

このリリースでは Proposed API の追加はなし。

## エンジニアリング・基盤改善

### CSS minification using `esbuild`

JavaScript に加え、CSS ファイルのバンドルとミニファイにも `esbuild` が使用されるようになった。

### Strict layer checks using `tsconfig.json`

複数の `tsconfig.json` ファイルを使用して、ソースコードが[ターゲット環境ルール](https://github.com/microsoft/vscode/wiki/Source-Code-Organization#target-environments)に準拠しているかを検証する仕組みが導入された。CI は `npm run valid-layers-check` を実行し、例えば `node` ランタイムにのみ存在する型が `browser` レイヤーに追加された場合にビルドを失敗させる。

### `vscode-bisect` for sanity testing

`vscode-bisect` プロジェクトに `--sanity` オプションが追加され、リリース前に必須の[サニティチェック](https://github.com/microsoft/vscode/wiki/Sanity-Check)を素早く実行可能に。

## Notable fixes

- [vscode-copilot-release#6073](https://github.com/microsoft/vscode-copilot-release/issues/6073) — Windows PowerShell でエージェントが `&&` を提案すべきでない問題を修正

## コミュニティ貢献

主要な外部コントリビューションをピックアップする。

- **[@UziTech (Tony Brix)](https://github.com/UziTech)**: ミドルマウスボタンスクロール機能を実装（[#245882](https://github.com/microsoft/vscode/pull/245882)）
- **[@JJJJJJ-git](https://github.com/JJJJJJ-git)**: ChatService の undo バグを修正（[#253478](https://github.com/microsoft/vscode/pull/253478)）
- **[@notoriousmango (Seong Min Park)](https://github.com/notoriousmango)**: webview テーマにフォントリガチャを追加、失敗テストの再実行・デバッグアクションを追加（[#250998](https://github.com/microsoft/vscode/pull/250998)、[#251679](https://github.com/microsoft/vscode/pull/251679)）
- **[@raffaeu (Raffaele Garofalo)](https://github.com/raffaeu)**: エディタ sticky scroll のリファクタリング（[#248131](https://github.com/microsoft/vscode/pull/248131)）
- **[@liuxingbaoyu](https://github.com/liuxingbaoyu)**: Unicode ユーザー名で PowerShell が動作しない問題を修正（[#251534](https://github.com/microsoft/vscode/pull/251534)）
- **[@heoh (HeoHeo)](https://github.com/heoh)**: Markdown プレビューの EOF でのスクロール問題を修正（[#251228](https://github.com/microsoft/vscode/pull/251228)）
- **[@Enzo-Nunes (Enzo Nunes)](https://github.com/Enzo-Nunes)**: Makefile の行コメントアクションを修正（[#243283](https://github.com/microsoft/vscode/pull/243283)）
- **[@Sublimeful (Jian Qiang Wu)](https://github.com/Sublimeful)**: ターミナルがない状態での Run Recent Command を実装（[#250799](https://github.com/microsoft/vscode/pull/250799)）

## まとめと所感

VS Code v1.102 は、Copilot Chat のオープンソース化と MCP の GA 化という二つの大きなマイルストーンを達成したリリースである。特に MCP については、サーバーのディスカバリ・インストール・管理ビュー・プロファイル統合・Dev Container 対応と、エコシステムとしての基盤が一気に整った。ターミナル自動承認やリクエスト編集はまだ実験段階だが、エージェントモードの操作効率を大幅に向上させる可能性を持つ。coding agent セッションの VS Code 内開始も、IDE をハブとしたバックグラウンドタスク委任ワークフローの具体化として注目に値する。実務的には、MCP 設定の `mcp.json` への自動マイグレーションが行われるため、既存ユーザーは `settings.json` の整理を確認しておくとよい。
