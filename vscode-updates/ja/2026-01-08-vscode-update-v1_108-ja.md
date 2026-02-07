---
title: "2025年12月リリース (version 1.108)"
date: "2026-01-08"
version_ref: "v1_108"
source_url: "https://code.visualstudio.com/updates/v1_108"
lang: "ja"
---

# 2025年12月リリース (version 1.108)

## リリース概要

VS Code 1.108 は例年どおり12月のハウスキーピング期間に重点を置いたリリースである。GitHub Issues を約6,000件削減し、1,000件以上をトリアージした。大規模な新機能の追加は控えめだが、Agent Skills（Experimental）の導入、Agent Sessions ビューの改善、ターミナルツールの自動承認ルール拡充、Terminal IntelliSense の UX 刷新、Git blame 設定の改善など、多岐にわたる品質向上が図られている。Update 1.108.1 / 1.108.2 の修正リリースも提供されている。

## 注目の新機能・変更点

1. **Agent Skills (Experimental)** — コーディングエージェントにドメイン固有の知識と機能を教えるスキルシステムが導入された。`.github/skills` フォルダに `SKILL.md` で定義する。
2. **Terminal tool auto approve の拡充** — `git ls-files`、`rg`、`sed` 等が自動承認対象に追加。ワークスペース内の npm スクリプトもデフォルト自動承認に。
3. **Terminal IntelliSense の UX 刷新** — インラインでのサジェスト表示に切り替わり、従来のウィジェットは非表示がデフォルトに。
4. **Git blame information settings の改善** — `git.blame.editorDecoration.template` でカスタムテンプレートを設定可能に。
5. **チャットセッション復元動作の変更** — 再起動時に空のチャットビューで開始するように変更。従来のセッション自動復元は設定で復元可能。
6. **ハウスキーピング** — 約6,000件の Issue 削減と1,000件超のトリアージを実施。
7. **Terminal tool のシェル履歴制御** — エージェント経由のターミナルコマンドがシェル履歴に追加されないように変更。
8. **Agent Sessions ビューの改善** — キーボードアクセス、セッションのグルーピング、変更ファイル表示、一括アーカイブをサポート。
9. **拡張機能の TypeScript オーサリング (Experimental)** — TypeScript で直接拡張機能を実行可能にする実験的機能。
10. **スニペット変換の強化** — 新しいスニペット変換（`capitalize` / `notCapitalize`）が追加。

## セクション別詳細解説

### Agents

#### 概要
Agent Skills の Experimental 導入と Agent Sessions ビューの改善が行われた。エージェントに対してドメイン固有の知識を提供する仕組みが整備されつつある。

#### 機能詳細

#### Agent Skills (Experimental)

VS Code に Agent Skills が導入された。コーディングエージェントに新しい機能やドメイン固有の知識を教える仕組み。

- スキルは `SKILL.md` ファイルを含むフォルダとして定義
- VS Code はワークスペースの `.github/skills` フォルダ（または互換性のため `.claude/skills/`）から自動検出
- リクエストに関連する場合にオンデマンドでチャットコンテキストにロード
- `chat.useAgentSkills` を `true` にして有効化
- 詳細は [Agent Skills ドキュメント](https://code.visualstudio.com/docs/copilot/customization/agent-skills)を参照

**ステータス**: **[Experimental]**
**対象ユーザー**: エージェントの出力品質をドメイン固有に向上させたいユーザー

#### Improvements to Agent Sessions view

Agent Sessions ビューに複数の改善が加えられた。

- キーボードアクセス対応（アーカイブ、既読状態変更、セッション開封）
- サイドバイサイド表示時に状態と経過時間でセッションをグルーピング
- セッションの変更ファイルと関連 PR の情報を表示
- 新しいグループセクションから複数セッションの一括アーカイブ
- アクセシビリティ全般の改善
- `chat.viewSessions.orientation` の `auto` オプションが廃止。代替として `sideBySide` を使用

**ステータス**: **[GA]**
**対象ユーザー**: 複数のエージェントセッションを管理するユーザー

> 📷 [画像: Agent Sessions ビューでの変更ファイルと関連 PR 表示](https://code.visualstudio.com/assets/updates/1_108/agentsessions-trimmed.png)

### Chat

#### 概要
チャットセッションの Quick Pick が Agent Sessions ビューベースに統合され、タイトルコントロールの改善、再起動時の動作変更、ターミナルツールの自動承認ルール拡充、シェル履歴制御の追加が行われた。

#### 機能詳細

#### Chat picker is based on agent sessions

チャットセッション用の Quick Pick が Agent Sessions ビューと同じ情報に基づくようになった。以前のチャットセッションへのアクセス、アーカイブ、リネーム、削除が可能。

- Quick Open（`Ctrl+P`）で `agent ` と入力してもアクセス可能

**ステータス**: **[GA]**
**対象ユーザー**: チャットセッションを頻繁に切り替えるユーザー

> 📷 [画像: エージェントセッションリストを表示するチャット Quick Pick](https://code.visualstudio.com/assets/updates/1_108/agent-picker.png)

#### Chat title improvements

Chat ビューのタイトルコントロールが、Activity Bar の設定に関係なく常に表示されるようになった。タイトルをクリックしてセッション Quick Pick を開き、別のセッションに素早く切り替え可能。

**ステータス**: **[GA]**
**対象ユーザー**: すべてのチャットユーザー

> 📷 [画像: チャットタイトルコントロール](https://code.visualstudio.com/assets/updates/1_108/agent-title.png)

#### Open empty Chat on restart

VS Code 再起動時にチャットセッションが自動復元されなくなり、空のチャットビューで開始するように変更された。

- `chat.restoreLastPanelSession` 設定で従来の動作に戻すことが可能

**ステータス**: **[GA]**（動作変更）
**対象ユーザー**: すべてのチャットユーザー

#### Terminal tool auto approve default rules

ターミナル自動承認（`chat.tools.terminal.enableAutoApprove`）有効時に自動承認されるコマンドが追加された。

- `git ls-files`
- `git --no-pager <safe_subcommand>`
- `git -C <dir> <safe_subcommand>`
- `rg`（`--pre` と `--hostname-bin` を除く）
- `sed`（一部の引数・使用パターンを除く）
- `Out-String`
- `package.json` 内の npm スクリプト（`npm`、`pnpm`、`yarn` 経由）がデフォルトで自動承認
  - `chat.tools.terminal.autoApproveWorkspaceNpmScripts` で無効化可能
- ルールにより明示的に拒否された場合、情報メッセージが表示されるようになった

**ステータス**: **[GA]**
**対象ユーザー**: エージェントモードでターミナルツールを利用するユーザー

> 📷 [画像: ルールによる自動承認拒否のメッセージ](https://code.visualstudio.com/assets/updates/1_108/terminal-tool-deny.png)

#### Add session and workspace rules for future terminal tool commands

Allow ドロップダウンのコマンド許可オプションに、現在のセッションまたはワークスペースに対して許可するアクションが追加された。

**ステータス**: **[GA]**
**対象ユーザー**: ターミナルツールの承認を細かく制御したいユーザー

> 📷 [画像: ターミナルツールの Allow ドロップダウン](https://code.visualstudio.com/assets/updates/1_108/terminal-tool-allow-dropdown.png)

#### Terminal tool preventing adding to shell history

シェル統合が有効な場合、ターミナルツール経由のコマンドがシェル履歴に追加されなくなった。bash、zsh、pwsh、fish に対応。

- bash の場合は `HISTCONTROL=ignorespace` を設定し、コマンドの先頭にスペースを追加
- `chat.tools.terminal.preventShellHistory` で従来の動作（履歴に追加）に戻すことが可能

**ステータス**: **[GA]**
**対象ユーザー**: エージェントモードでターミナルを利用するユーザー

### Accessibility

#### 概要
チャット応答のリアルタイムストリーミング表示、MCP サーバー出力のノイズ除去、ウィンドウタイトルへの言語 ID 変数の追加など、アクセシビリティの改善が行われた。

#### 機能詳細

#### Streaming chat responses in Accessible View

Accessible View でチャット応答がリアルタイムにストリーミング表示されるようになった。以前は更新内容を確認するために Accessible View を閉じて再度開く必要があった。

**ステータス**: **[GA]**
**対象ユーザー**: スクリーンリーダーを使用するユーザー

#### MCP server output excluded from Accessible View

ノイズ軽減のため、MCP サーバー出力がデフォルトで Accessible View から除外されるようになった。標準的なチャット出力はテキストエリアとして完全にアクセス可能。

**ステータス**: **[GA]**
**対象ユーザー**: スクリーンリーダーを使用するユーザー

#### Language ID variable in window title

`window.title` 設定で新しい変数 `${activeEditorLanguageId}` が使用可能になった。アクティブなエディタの言語識別子を表示し、Talon などのアクセシビリティツールが現在のプログラミング言語を判別して適切な音声コマンドを有効にするのに役立つ。

```json
"window.title": "${activeEditorLanguageId} - ${activeEditorShort}"
```

**ステータス**: **[GA]**
**対象ユーザー**: 音声操作ツール等を使用するユーザー

### Editor Experience

#### 概要
プロファイルのドラッグ＆ドロップインポート、ブレッドクラムパスのコピー、ワークスペースシンボル検索での特殊文字対応が改善された。

#### 機能詳細

#### Import profile by drag and drop

`.code-profile` ファイルを VS Code にドラッグ＆ドロップすることで設定プロファイルをインポートできるようになった。チームメイトとのプロファイル共有や新環境セットアップが容易になる。ファイルをドロップするとプロファイルエディタが開き、プレビューとインポートが可能。

**ステータス**: **[GA]**
**対象ユーザー**: すべてのユーザー

#### Copy breadcrumbs path

**設定**: `breadcrumbs.symbolPathSeparator`

**Copy Breadcrumbs Path** コマンドでブレッドクラムパスをクリップボードにコピーできるようになった。シンボルの正確な位置をチームと共有する場合やドキュメント作成に便利。

- `breadcrumbs.symbolPathSeparator` でブレッドクラムセグメントの区切り文字をカスタマイズ可能

> 📷 [画像: Copy Breadcrumbs Path コマンド](https://code.visualstudio.com/assets/updates/1_108/breadcrumbs_copy_path.png)

**ステータス**: **[GA]**
**対象ユーザー**: コードナビゲーションを多用するユーザー

#### Go to Symbol in Workspace supports special characters in query

**Go to Symbol in Workspace**（`Ctrl+T`）で検索クエリに `#` 文字が含まれている場合に結果が全てフィルタアウトされるバグが修正された。

- rust-analyzer のように `#` を修飾子として使用する言語拡張で有効（例: `main#` で現在のワークスペース内の関数のみを検索）

**ステータス**: **[GA]**（バグ修正）
**対象ユーザー**: Rust 等の言語拡張ユーザー

### Code Editing

#### 概要
スニペット変換に `snakecase` と `kebabcase` が新たに追加された。

#### 機能詳細

#### New snippet transformations

2つの新しいスニペット変換が利用可能になった。

- `snakecase` — ファイル名等を snake_case に変換。例: `MyFileName.txt` → `my_file_name.txt`
- `kebabcase` — ファイル名等を kebab-case に変換。例: `MyFileName.txt` → `my-file-name.txt`

使用例:
```text
${TM_FILENAME/(.*)/${1:/snakecase}/}
```

**ステータス**: **[GA]**
**対象ユーザー**: スニペットを活用する開発者

### Source Control

#### 概要
Git blame の設定改善、コミットメッセージエディタの UX 向上、ワークツリーのリポジトリエクスプローラ表示（Experimental）が追加された。

#### 機能詳細

#### Git blame information settings

**設定**: `git.blame.ignoreWhitespace`（デフォルト: `true`）、`git.blame.editorDecoration.disableHover`（デフォルト: `true`）

- `git.blame.ignoreWhitespace` — ホワイトスペースの変更を無視して blame を表示。リフォーマットされたコードで実際の機能的な変更を行ったコミットを特定するのに有用。
- `git.blame.editorDecoration.disableHover` — blame デコレーションのホバーツールチップを無効化。インライン表示のみでクリーンな編集体験を提供。

**ステータス**: **[GA]**
**対象ユーザー**: Git blame を利用する開発者

#### Authoring commit messages using the editor

フルエディタでのコミットメッセージ作成において、コミットやキャンセルのアクションがエディタの右下隅のオーバーレイコントロールに移動され、発見しやすくなった。

**ステータス**: **[GA]**（UX改善）
**対象ユーザー**: Git コミットメッセージをエディタで作成するユーザー

#### Worktrees in the Source Control Repositories view (Experimental)

**設定**: `scm.repositories.explorer`（`true` で有効化）、`scm.repositories.selectionMode`（`single` に設定）

Source Control Repositories ビューに **Worktrees** ノードが追加された。

- リポジトリのワークツリー一覧を表示
- インラインアクションで新しいウィンドウでワークツリーを開く
- コンテキストメニューから現在のウィンドウで開く、削除が可能

> 📷 [画像: Source Control Repositories ビューの Worktrees ノード](https://code.visualstudio.com/assets/updates/1_108/repository-explorer-worktrees.png)

**ステータス**: **[Experimental]**
**対象ユーザー**: Git worktree を活用する開発者

### Terminal

#### 概要
Terminal IntelliSense のデフォルト UX が大幅に刷新され、パフォーマンス改善、カスタムグリフの大幅拡充（約800文字）、カーリーアンダーラインの描画改善、リサイズ時のオーバーレイ表示、新しい VT シーケンスサポートが追加された。

#### 機能詳細

#### Terminal IntelliSense default UX rework

Terminal IntelliSense のデフォルト動作が変更された。前2リリースで全 Stable ユーザーにロールアウトされたが、パワーユーザーからマッスルメモリが壊れるとのフィードバックを受けて再調整。

**主な変更点:**
- 機能自体は引き続きデフォルトで有効
- Quick suggestions・Suggest on trigger characters がデフォルトで **無効** に変更。明示的に `Ctrl+Space` でトリガーする方式に
- ステータスバーの UI を改善: 左側に「selection mode」の切り替え（Tab / Enter の挙動を制御）、右側にアイコン表示
- 新しい「目」アイコンで Quick suggestions を再度有効化可能
- ターミナル初回起動時にサジェストのトリガー方法を説明するヒントを表示（「don't show」で恒久的に非表示可能）

**その他の改善:**
- macOS / Linux で実行可能ビット付きファイルを表示
- `npm` と `git` の補完を改善
- ファイル・フォルダのサジェストのバリデーション改善
- サジェスト詳細の高さ制約でレイアウトオーバーフローを防止
- ターミナルビューの移動時もサジェストが正しく動作

> 📷 [画像: サジェストステータスバー](https://code.visualstudio.com/assets/updates/1_108/terminal-suggest.png)
> 📷 [画像: ターミナル初回ヒント](https://code.visualstudio.com/assets/updates/1_108/terminal-initial-hint.png)

**ステータス**: **[GA]**（動作変更）
**対象ユーザー**: ターミナルを日常的に利用する開発者

#### Performance and stability improvements

ターミナルのパフォーマンスと安定性に複数の重要な改善が行われた。

- **macOS / Linux でのペースト高速化**: 50文字以上のペーストやエージェントの大きなコマンド実行がスロットリングされなくなり、KB/MB 単位のデータでも瞬時に適用。macOS でのクラッシュも修正。（[node-pty#831](https://github.com/microsoft/node-pty/pull/831)）
- **レイアウトスラッシング修正**: エディタがラグくなる原因となっていたレイアウトスラッシングの問題を複数修正。（[vscode#285031](https://github.com/microsoft/vscode/issues/285031)、[vscode#285032](https://github.com/microsoft/vscode/issues/285032)、[xterm.js#5548](https://github.com/xtermjs/xterm.js/issues/5548)）
- **フォントクラッシュ修正**: CommitMono 等のフォント設定時のクラッシュを修正。（[vscode#239541](https://github.com/microsoft/vscode/issues/239541)）

**ステータス**: **[GA]**
**対象ユーザー**: すべてのターミナルユーザー

#### More comprehensive custom glyphs

ターミナルの GPU アクセラレーテッドレンダラーのカスタムグリフサポートが大幅に拡充され、約 **800文字** をサポート。フォント設定不要で表示でき、行の高さや文字間隔に応じてスケーリングされる。

サポートされる Unicode 範囲:
- Box Drawing（`U+2500`–`U+257F`）
- Block Elements（`U+2580`–`U+259F`）
- Braille Patterns（`U+2800`–`U+28FF`）
- Powerline Symbols（`U+E0A0`–`U+E0D4`、Private Use Area）
- Progress Indicators（`U+EE00`–`U+EE0B`、Private Use Area）
- Git Branch Symbols（`U+F5D0`–`U+F60D`、Private Use Area）
- Symbols for Legacy Computing（`U+1FB00`–`U+1FBFF`）

> 📷 [画像: 約800のカスタムグリフ一覧](https://code.visualstudio.com/assets/updates/1_108/terminal-custom-glyphs.png)

**ステータス**: **[GA]**
**対象ユーザー**: ターミナルで特殊文字を表示するユーザー

#### Improved rendering of curly underlines

ターミナルのカーリーアンダーラインの描画品質が向上し、エディタでの表示に近い外観になった。

確認コマンド（bash）:
```bash
echo -e '\x1b[4:3mCurly\x1b[0m \x1b[4:3m\x1b[58;5;1mRed\x1b[0m'
```

> 📷 [画像: 改善されたカーリーアンダーライン](https://code.visualstudio.com/assets/updates/1_108/terminal-curly-underline.png)

**ステータス**: **[GA]**
**対象ユーザー**: ターミナルユーザー

#### Dimensions visual overlay on resize

[ghostty](https://github.com/ghostty-org/ghostty) にインスパイアされた機能。ターミナルのリサイズ時に現在のサイズ（カラム × 行）をオーバーレイ表示するようになった。テスト用に特定のサイズに調整する場合に便利。

> 📷 [画像: リサイズ時のオーバーレイ](https://code.visualstudio.com/assets/updates/1_108/terminal-resize-overlay.png)

**ステータス**: **[GA]**
**対象ユーザー**: ターミナルユーザー

#### New VT features

ターミナルで新しい VT 機能/シーケンスのサポートが追加された。

- **Synchronized output** — レンダリングを一時停止してバッチ更新するためのシーケンス。バッファ書き換え時のティアリング防止に有用。
  - DECRQM（`CSI ? 2026 $ p`）
  - BSU（`CSI ? 2026 h`）
  - ESU（`CSI ? 2026 l`）
- **XTVERSION**（`CSI > 0 q`）— アプリケーションがターミナルの詳細を照会可能。VS Code は "xterm.js" とそのバージョンを返す。

**ステータス**: **[GA]**
**対象ユーザー**: VT シーケンスを利用するターミナルアプリケーション開発者

### Debug

#### 概要
ブレークポイントをファイルごとにツリー表示する機能が追加された。

#### 機能詳細

#### Organize breakpoints by file

**設定**: `debug.breakpointsView.presentation`（`tree` に設定）

ブレークポイントをファイル別にグループ化してツリー表示できるようになった。

> 📷 [画像: ファイルごとにツリー表示されたブレークポイント](./images/1_108/debug-bp-tree.png)

**ステータス**: **[GA]**
**対象ユーザー**: デバッグを頻繁に行う開発者

### Testing

#### 概要
テストカバレッジツールバーにカバレッジされていない領域間のナビゲーションボタンが追加された。

#### 機能詳細

#### Navigate to uncovered regions

テストカバレッジツールバーにナビゲーションボタンが追加され、カバーされていないコード領域間をジャンプできるようになった。ツールバーは **Test: Show Coverage Toolbar** コマンドで表示を切り替え可能。

> 📷 [画像: テストカバレッジツールバーのナビゲーションボタン](./images/1_108/coverage-navigation.png)

**ステータス**: **[GA]**
**対象ユーザー**: テストカバレッジを重視する開発者

### Contributions to extensions

#### GitHub Pull Requests 拡張

[GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) 拡張に以下の新機能が追加された。

- PR のベースブランチを description webview から変更可能
- オープンな PR をドラフトに変換可能
- 既存の PR に対しても PR 説明文を生成可能（新規 PR のみでなく）

詳細は [changelog for the 0.126.0](https://github.com/microsoft/vscode-pull-request-github/blob/main/CHANGELOG.md#01260) を参照。

### Extension Authoring

#### 概要
Quick Pick API にプロンプト表示とリソース URI プロパティが追加された。

#### 機能詳細

#### New Quick Pick properties for prompts and resource URIs

Quick Pick API に2つの新しいプロパティが追加された。

**`prompt` プロパティ（`QuickPick`）**
入力ボックスの下にガイダンステキストを持続的に表示する。ユーザーが入力中も表示され続ける。

```typescript
const quickPick = vscode.window.createQuickPick();
quickPick.prompt = 'Select a file to open';
quickPick.items = items;
quickPick.show();
```

**`resourceUri` プロパティ（`QuickPickItem`）**
リソース URI からアイテムのプロパティを自動導出する。設定時に VS Code が以下を自動的に導出:

- `label` — ファイル名から（空文字列に設定時）
- `description` — ファイルパスから（`undefined` または空文字列に設定時）
- `icon` — 現在のファイルアイコンテーマから（`iconPath` が `ThemeIcon.File` / `ThemeIcon.Folder` の場合）

```typescript
const items: vscode.QuickPickItem[] = [
  {
    label: '',
    resourceUri: vscode.Uri.file('/path/to/app.ts'),
    iconPath: vscode.ThemeIcon.File
  },
  {
    label: '',
    resourceUri: vscode.Uri.file('/path/to/src'),
    iconPath: vscode.ThemeIcon.Folder
  }
];
```

**ステータス**: **[GA]**
**対象ユーザー**: VS Code 拡張機能開発者

### Engineering

#### 概要
年末恒例のハウスキーピングで約6,000件の Issue を削減。TypeScript での拡張機能オーサリング（Experimental）も追加。

#### 機能詳細

#### Housekeeping

12月の年次ハウスキーピングとして、管理対象の全リポジトリで GitHub Issues と PR のクリーンアップが行われた。

- オープンな Issue を **5,951件** 削減
- 新たに **1,203件** をトリアージ
- コアの `microsoft/vscode` リポジトリ単体では **2,872件** クローズ、**1,697件** トリアージ
- 2025年6月の Copilot オープンソース化に伴い `microsoft/vscode-copilot-release` の全 Issue をトリアージし **1,659件** クローズ、残り175件のみに

改善されたトリアージツールと重複排除プロセスにより、陳腐化した Issue や解決済みの Issue を大量にクローズ。

> 📷 [画像: 全 VS Code 管理リポジトリの Issue グラフ](https://code.visualstudio.com/assets/updates/1_108/combined-graph.png)
> 📷 [画像: ハウスキーピング中にクローズされた Issue 数](https://code.visualstudio.com/assets/updates/1_108/issue-reduction.png)
> 📷 [画像: トリアージされた未知の Issue 数](https://code.visualstudio.com/assets/updates/1_108/unknown-reduction.png)
> 📷 [画像: microsoft/vscode の Issue グラフ](https://code.visualstudio.com/assets/updates/1_108/vscode-graph.png)
> 📷 [画像: microsoft/vscode-copilot-release の Issue グラフ](https://code.visualstudio.com/assets/updates/1_108/vscode-copilot-release-graph.png)
> 📷 [画像: microsoft/vscode の歴史的 Issue データ](https://code.visualstudio.com/assets/updates/1_108/historical-vscode-graph.png)

#### Authoring extensions in TypeScript (Experimental)

ビルドステップなしで TypeScript で直接 VS Code 拡張機能をオーサリングできるようになった（Experimental）。

- ビルドステップ不要で TypeScript のまま拡張機能を実行可能
- テストの記述・実行、拡張機能の公開など多くの側面がまだ未テスト
- 詳細は [GitHub コメント](https://github.com/microsoft/vscode/issues/263558#issuecomment-3656380346) を参照

**ステータス**: **[Experimental]**
**対象ユーザー**: 拡張機能開発者

### Notable fixes

- [vscode#283356](https://github.com/microsoft/vscode/issues/283356) — チャット出力をスクロールする際にジャンプする回帰的なバグを修正

## 設定項目まとめ

### 新規設定・変更された設定

| 設定キー | 概要 | デフォルト値 |
|---|---|---|
| `chat.useAgentSkills` | Agent Skills の有効化（Experimental） | `false` |
| `chat.viewSessions.orientation` | セッションビューの向き（`auto` オプションが **廃止**、`sideBySide` を使用） | — |
| `chat.restoreLastPanelSession` | 再起動時に前回のチャットセッションを復元 | `false`（変更） |
| `chat.tools.terminal.enableAutoApprove` | ターミナルツールの自動承認 | — |
| `chat.tools.terminal.autoApproveWorkspaceNpmScripts` | ワークスペース内 npm スクリプトの自動承認 | `true`（新規） |
| `chat.tools.terminal.preventShellHistory` | ターミナルツールのコマンドをシェル履歴に追加しない | `true`（新規） |
| `breadcrumbs.symbolPathSeparator` | ブレッドクラムパスの区切り文字 | — |
| `git.blame.ignoreWhitespace` | blame でホワイトスペース変更を無視 | `true`（新規） |
| `git.blame.editorDecoration.disableHover` | blame デコレーションのホバー無効化 | `true`（新規） |
| `scm.repositories.explorer` | リポジトリエクスプローラの有効化（Experimental） | `false` |
| `scm.repositories.selectionMode` | リポジトリ選択モード | — |
| `debug.breakpointsView.presentation` | ブレークポイントの表示形式（`tree` でファイル別） | — |

## Breaking Changes / 非推奨化

| 項目 | 内容 |
|---|---|
| `chat.viewSessions.orientation` の `auto` 廃止 | `auto` オプションが削除。代替として `sideBySide` を使用 |
| Terminal IntelliSense の UX 変更 | Quick suggestions / Suggest on trigger characters がデフォルト無効に。`Ctrl+Space` で明示的トリガーに変更 |
| チャットセッション復元動作の変更 | 再起動時に空のチャットビューで開始するように変更。`chat.restoreLastPanelSession` で復元可能 |
| ターミナル履歴への追加抑止 | エージェント経由コマンドがシェル履歴に追加されないように変更。`chat.tools.terminal.preventShellHistory` で制御 |

## 開発者・拡張機能作成者向け

### Quick Pick API の新プロパティ

- `QuickPick.prompt` — 入力ボックス下にガイダンステキストを常時表示
- `QuickPickItem.resourceUri` — リソース URI からラベル・説明・アイコンを自動導出
- ファイル/フォルダ選択インターフェースの構築に便利

### Extension Authoring in TypeScript (Experimental)

- ビルドステップ不要で TypeScript のまま拡張機能を実行可能
- まだ実験段階: テストの記述・実行と公開はまだ未テスト

## エンジニアリング・基盤改善

- **ハウスキーピング**: 全リポジトリで約6,000件の Issue 削減、1,200件超のトリアージ
- **TypeScript 拡張オーサリング**: ビルドステップ不要の実験的機能を導入
- **ターミナル**: node-pty のペーストスロットリング除去、レイアウトスラッシング修正、フォントクラッシュ修正
- **メモリリーク修正**: Simon Siefke 氏による大量のメモリリーク修正（terminal editor、process、accessibility signal、IPC、chat widget 等17件）

## コミュニティ貢献

### 主な貢献者と貢献内容

| 貢献者 | 主な貢献 |
|---|---|
| **Simon Siefke** | メモリリーク修正を17件以上実施（terminal、chat、debug、IPC 等多岐にわたる） |
| **RedCMD** | TS/JS テンプレートブラケット、PHP インデント修正、FormatOnSave 修正、C の `# pragma` フォールディング |
| **tamuratak** | ChatWidget の修正、sed の大文字 `-I` オプション検出、コンテキストハンドリング修正 |
| **joeriddles** | snakecase スニペット構文の追加 |
| **kortin99** | kebab-case スニペット構文の追加 |
| **tharani-2006** | ターミナルリサイズ時のディメンションオーバーレイ |
| **murataslan1** | スクロール時のジャンプ修正、ターミナルライフサイクル改善 |
| **Beace** | terminal WebGL コンテキストのメモリリーク修正 |
| **rducom** | PowerShell プロンプト検出の ReDoS 修正 |
| **jcpetruzza** | デバッグ「continue」時の UI フリーズ修正 |

### Issue tracking 貢献者

- John Murray、RedCMD、Takashi Tamura、Andrii Dieiev、Alberto Santini

### その他のリポジトリへの貢献

- **vscode-copilot-chat**: Gemini プロバイダのエラーハンドリング改善、システムプロンプト更新
- **vscode-js-profile-visualizer**: 不要な package-lock.json ファイルの削除

## まとめと所感

VS Code 1.108 は12月のハウスキーピングリリースであり、大規模な新機能追加よりもプロジェクトの健全性維持を重視したリリースである。

**最も重要な変更点:**
1. **Agent Skills (Experimental)** の導入により、コーディングエージェントのドメイン固有カスタマイズが可能に
2. **Terminal IntelliSense の UX 刷新** — パワーユーザーのフィードバックを受けてデフォルト動作を変更。明示的トリガー方式に移行
3. **ハウスキーピングの成果** — 約6,000件のIssue削減は過去最大級の成果

**動作変更に注意が必要な項目:**
- Terminal IntelliSense のデフォルト UX が変更。従来のように入力時に自動表示させるにはステータスバーの「目」アイコンで再有効化が必要
- チャットセッションの自動復元がデフォルトで無効に
- `chat.viewSessions.orientation` の `auto` オプションが廃止
- エージェント経由のターミナルコマンドがシェル履歴に追加されなくなった

**コミュニティ貢献のハイライト:**
Simon Siefke 氏による17件以上のメモリリーク修正は特筆すべき貢献であり、VS Code の安定性向上に大きく寄与している。snakecase/kebabcase スニペット変換やターミナルリサイズオーバーレイなど、コミュニティ発の機能追加も複数取り込まれている。

