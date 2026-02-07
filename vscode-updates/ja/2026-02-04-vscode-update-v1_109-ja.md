---
title: "2026年1月リリース (version 1.109)"
date: "2026-02-04"
version_ref: "v1_109"
source_url: "https://code.visualstudio.com/updates/v1_109"
lang: "ja"
---

# 2026年1月リリース (version 1.109)

## リリース概要

VS Code 1.109 は「マルチエージェント開発のホーム」というビジョンをさらに推し進めるリリースである。Chat UX の高速化と thinking tokens の可視化、ローカル・バックグラウンド・クラウドにまたがるエージェントセッション管理、カスタムエージェントの GA 化、Claude Agent プレビュー、MCP Apps 対応など、エージェント関連の機能が大幅に拡充された。さらに、エディタ内蔵ブラウザ（Preview）、ターミナルサンドボックス（Experimental）、Copilot Memory（Preview）などの新機能が加わり、開発ワークフロー全体の効率と安全性が向上している。

## 注目の新機能・変更点

1. **Anthropic モデルの thinking tokens 表示** — Claude モデルの推論プロセスがチャット上で可視化され、ツール呼び出しとインターリーブ表示される。
2. **Agent Skills GA 化** — カスタムエージェントのスキル定義が正式リリースとなり、Organization-wide instructions にも対応。
3. **Claude Agent (Preview)** — Anthropic の Claude がエージェントモードでネイティブサポートされ、拡張的なツール利用が可能に。
4. **Copilot Memory (Preview)** — ユーザーの好みやプロジェクト情報をセッション横断で記憶し、パーソナライズされた応答を提供。
5. **統合ブラウザ (Preview)** — エディタ内で Web アプリをプレビュー・デバッグできる Simple Browser の進化版。
6. **ターミナルサンドボックス (Experimental)** — エージェントのターミナルコマンド実行をサンドボックス環境で安全に制限。
7. **エージェントセッション管理の統合ビュー** — ローカル・バックグラウンド・クラウドエージェントを一元管理し、並行実行・タスク委譲が容易に。
8. **Mermaid ダイアグラム対応** — チャット応答内でインタラクティブな Mermaid ダイアグラムをレンダリング可能に。
9. **Plan agent の強化** — 4 フェーズの反復ワークフロー（Discovery → Alignment → Design → Refinement）で高品質な実装計画を生成。
10. **External indexing for non-GitHub workspaces (Preview)** — GitHub 以外のワークスペースでも外部インデックスによる高速コード検索が利用可能に。

## セクション別詳細解説

### Upcoming events

#### 概要
VS Code チームが主催するオンラインイベントの告知。

#### Agent Sessions Day
- **日時**: 2026年2月19日
- **内容**: 本リリースの最新アップデートをライブデモで紹介。VS Code がどのようにユニファイドなエージェント UX へ進化したかを解説する。
- **URL**: https://youtube.com/live/tAezuMSJuFs

> 📷 [画像: Agent Session Day イベントのビジュアル](https://code.visualstudio.com/assets/updates/1_109/agent-sessions-day-2026.webp)

### Chat UX

#### 概要
チャット応答の高速化、Anthropic モデルの推論トークン可視化、インラインチャットの刷新など、チャット体験全体の品質向上が図られたセクション。Mermaid ダイアグラムのレンダリング、Ask Questions ツール、Plan agent の強化、コンテキストウィンドウの使用状況表示なども含まれる。

#### 機能詳細

#### Anthropic models now show thinking tokens

Anthropic の Claude モデルで thinking tokens がサポートされ、モデルの推論プロセスをチャット上で確認できるようになった。

- `chat.thinking.style` で思考表示のスタイル（詳細 / コンパクト）を選択可能
- `chat.agent.thinking.terminalTools` でツール呼び出し・レスポンスとインターリーブ表示
- `chat.tools.autoExpandFailures` で失敗したツール呼び出しを自動展開してコンテキストを表示
- `chat.agent.thinking.collapsedTools` でツール表示の折りたたみを制御
- スクロール可能な思考コンテンツやシマーアニメーションなど、視覚的な改善も多数

**ステータス**: **[GA]**
**対象ユーザー**: Anthropic Claude モデルを利用するすべてのユーザー

> 🎬 [動画: チャットでのスクロール可能な思考コンテンツとシマーアニメーション](https://code.visualstudio.com/assets/updates/1_109/thinking-scrolling-shimmer.mp4)

#### Mermaid diagrams in chat responses

チャット応答内で `renderMermaidDiagram` ツールを使ってインタラクティブな Mermaid ダイアグラム（フローチャート、シーケンス図など）をレンダリングできるようになった。

- `Alt/Option` + マウスホイールでズーム、`Alt/Option` + ドラッグでパン
- `Alt/Option` + クリックでズームイン、`Shift` 追加でズームアウト
- フルサイズエディタで開くボタン
- 右クリックで Mermaid ソースコードをコピー

**ステータス**: **[GA]**
**対象ユーザー**: チャット機能を利用するすべてのユーザー

> 📷 [画像: チャット応答内の Mermaid ダイアグラム](https://code.visualstudio.com/assets/updates/1_109/chat-mermaid.png)

#### Ask Questions tool (Experimental)

エージェントが不明な点について `askQuestions` ツールで確認質問を行えるようになった。単一選択 / 複数選択オプション、自由テキスト入力、推奨回答のハイライトなどの UI が提供される。

- `chat.askQuestions.enabled` で有効化
- キーボードで `Up` / `Down` で回答間を移動、番号キーで選択、`Escape` で質問をスキップ
- Plan agent もこのツールを活用し、実装計画の精度を向上

**ステータス**: **[Experimental]**
**対象ユーザー**: エージェントモードを利用するユーザー
**有効化方法**: `chat.askQuestions.enabled` を有効にする

> 📷 [画像: Ask Questions ツールの質問カルーセルとテーマタイプオプション](https://code.visualstudio.com/assets/updates/1_109/ask-questions-ui.png)

#### Plan agent

ビルトインの Plan agent が強化され、コーディング前に構造化された実装計画を作成できるようになった。

- 4 フェーズの反復ワークフロー:
  1. **Discovery** — コードベースを自律的に探索し、関連ファイルやプロジェクト構造を把握
  2. **Alignment** — 計画確定前に確認質問を行い、曖昧さを早期に解消
  3. **Design** — 明確なステップ、ファイル位置、コードスニペットを含む包括的な実装計画を策定
  4. **Refinement** — 検証基準の追加と、計画中の意思決定を文書化
- `/plan` コマンドで Plan agent を直接起動可能

**ステータス**: **[GA]**
**対象ユーザー**: 複雑なタスクの計画を行いたいすべてのユーザー

#### Context window details

チャット入力エリアにコンテキストウィンドウインジケータが追加され、モデルのトークン使用状況をカテゴリ別に確認できるようになった。インジケータにホバーすると内訳が表示される。

**ステータス**: **[GA]**
**対象ユーザー**: チャット機能を利用するすべてのユーザー

> 📷 [画像: コンテキストウィンドウコントロールとカテゴリ別内訳のホバーメッセージ](https://code.visualstudio.com/assets/updates/1_109/context-window-widget.png)

#### Inline chat UX revamp (Preview)

インラインチャット体験の刷新が進行中。2つのプレビュー機能が導入された。

- `inlineChat.affordance` — テキスト選択時にインラインチャットをトリガーしやすくするアフォーダンス
- `inlineChat.renderMode` — 軽量でコンテキストに沿ったレンダリングモード

**ステータス**: **[Preview]**
**対象ユーザー**: インラインチャットを利用するユーザー
**有効化方法**: `inlineChat.affordance` および `inlineChat.renderMode` を設定

> 🎬 [動画: インラインチャットのアフォーダンスとコンテキスト入力](https://code.visualstudio.com/assets/updates/1_109/inline-chat.mp4)

#### Model descriptions in the model picker

モデルピッカーでモデルにホバーまたはキーボードフォーカスすると、モデルの詳細情報が一目で確認できるようになった。

**ステータス**: **[GA]**
**対象ユーザー**: 複数モデルを使い分けるユーザー

> 📷 [画像: モデルピッカーでのモデル詳細フライアウト（Claude Opus を選択）](https://code.visualstudio.com/assets/updates/1_109/model-picker.png)

#### Terminal command output

ターミナルツールのコマンド出力表示が大幅に改善された。

##### Richer command details
- **インライン Node / Python / Ruby のシンタックスハイライト** — Python コード等がハイライト表示され、レビューが容易に
- **作業ディレクトリの表示** — コマンドが実行されるディレクトリがタイトルに表示
- **コマンドの意図の説明** — ホバーで「何のために」実行するかの説明が表示

> 📷 [画像: インライン Python 呼び出しのシンタックスハイライト](https://code.visualstudio.com/assets/updates/1_109/terminal-python-presenter.png)
> 📷 [画像: コマンド実行ディレクトリの表示](https://code.visualstudio.com/assets/updates/1_109/terminal-tool-cd-presentation.png)
> 📷 [画像: コマンドの目的（goal）のホバー表示](https://code.visualstudio.com/assets/updates/1_109/terminal-tool-goal.png)

##### Output streaming
長時間実行コマンドの出力が自動展開され、リアルタイムで状況を確認可能。短時間で完了するコマンドは折りたたまれたまま表示される。

> 🎬 [動画: 長時間コマンドでのターミナル出力自動展開](https://code.visualstudio.com/assets/updates/1_109/embedded-terminal-streaming.mp4)

##### Interactive input
埋め込みターミナルが完全にインタラクティブになり、確認プロンプトやユーザー入力が必要な場合に直接タイプ可能。カーソルが表示され、入力可能状態が明確になった。

> 🎬 [動画: 埋め込みターミナルへの直接入力](https://code.visualstudio.com/assets/updates/1_109/embedded-terminal-input.mp4)

##### Delete all hidden terminals
ターミナルパネルの「Hidden Terminals」項目に削除アイコンが追加され、非表示ターミナルを一括削除可能。

> 📷 [画像: Hidden terminals の削除アイコン](https://code.visualstudio.com/assets/updates/1_109/delete-hidden-terminals.png)

**ステータス**: **[GA]**
**対象ユーザー**: エージェントモードでターミナルツールを利用するユーザー

#### Tell us what you think about our new themes (Experimental)

新しい実験的テーマ `VS Code Light` と `VS Code Dark` が開発中。シャドウと透過を活用し、フォーカスの向上と UI の軽快さを実現する。

- 開発中（work-in-progress）であり、フィードバックを [vscode リポジトリ](https://github.com/microsoft/vscode/issues) で受付中

**ステータス**: **[Experimental]**
**対象ユーザー**: テーマのカスタマイズに関心のあるユーザー

> 📷 [画像: 新しい実験的 VS Code Dark テーマ](https://code.visualstudio.com/assets/updates/1_109/vscode-dark-experimental-theme.webp)
> 📷 [画像: 新しい実験的 VS Code Light テーマ](https://code.visualstudio.com/assets/updates/1_109/vscode-light-experimental-theme.webp)

### Agent Session Management

#### 概要
ローカル・バックグラウンド・クラウドの各エージェント環境を横断して複数セッションを並行管理できる統合ビューが導入された。セッション間の切り替え、委譲、進捗追跡が一元化され、エージェントが独立して動作する間もユーザーの生産性を維持できる。

#### 機能詳細

#### Switching and delegating between agent types

チャット入力エリアに新しいセッションタイプピッカーが追加され、エージェントセッションの種類（ローカル / バックグラウンド / クラウド / 外部プロバイダ）を簡単に切り替えられるようになった。

- セッション開始時にエージェントタイプを選択
- 進行中のセッションを別のエージェントタイプに委譲可能（例: ローカルで計画 → クラウドで実装）
- `workbench.action.chat.newLocalChat` コマンドが追加され、キーボードショートカットに割り当てて素早くローカルチャットを開始可能

**ステータス**: **[GA]**
**対象ユーザー**: 複数環境でエージェントを使い分けるユーザー

> 📷 [画像: セッションタイプピッカーでの環境切り替え](https://code.visualstudio.com/assets/updates/1_109/session-type-picker-continue.png)

#### Keeping track of agent sessions

複数のエージェントセッションを管理するための機能が強化された。

##### Agent Sessions view
- セッションリストのサイドバイサイド表示時のリサイズ対応
- 複数セッションを選択して一括操作
- スタック表示の改善によるナビゲーションとフィルタリングの向上

> 🎬 [動画: Chat ビューでのエージェントセッション管理](https://code.visualstudio.com/assets/updates/1_109/agent-sessions-viewer.mp4)

##### Agent status indicator
VS Code のコマンドセンターにエージェントステータスインジケータが追加された。

- 進行中、未読、注意が必要なセッションの状態を表示
- インジケータをクリックしてセッションリストを開きフィルタリング
- `chat.agentsControl.enabled` でインジケータを有効化
- `chat.agentsControl.clickBehavior` でコマンドセンターのチャットボタンのクリック動作を設定（デフォルトはサイドバー → 最大化 → 非表示のサイクル）

**ステータス**: **[GA]**
**対象ユーザー**: 複数エージェントセッションを並行利用するユーザー

> 📷 [画像: 注意が必要なセッション数を表示するエージェントステータスインジケータ](https://code.visualstudio.com/assets/updates/1_109/agent-status-indicator/input-needed.png)

#### Subagents

エージェントがサブエージェントを使ってサブタスクを実行できる機能が強化された。サブエージェントは独立したコンテキストウィンドウで動作するため、メインエージェントのコンテキストを消費しない。

- サブエージェントの**並列実行**が可能になり、独立タスクの分割で大幅な高速化
- 各サブエージェントのタスク内容、使用カスタムエージェント、使用中ツールの詳細表示
- 展開するとサブエージェントの初期プロンプト全文と返却結果を確認可能
- `chat.customAgentInSubagent.enabled` でカスタムエージェントのサブエージェント利用を制御

##### Search subagent (Experimental)
- コードベース検索を分離されたエージェントループで実行する検索サブエージェント
- 反復的な検索の精製、複数クエリの試行、ワークスペースの異なる部分の探索が可能
- メインエージェントのコンテキストウィンドウを保持しつつ、並行して検索を実行
- `github.copilot.chat.searchSubagent.enabled` で有効化

**ステータス**: サブエージェント自体は **[GA]**、Search subagent は **[Experimental]**
**対象ユーザー**: 複雑なタスクを分割して効率化したいユーザー

> 📷 [画像: 2つのアクティブなサブエージェントとスピナー](https://code.visualstudio.com/assets/updates/1_109/subagents.png)

#### Cloud agents

クラウドエージェントセッションの設定オプションが拡充された。

- **モデル選択** — クラウドエージェントで使用するモデルを選択可能
- **カスタムエージェント対応** — ターゲットの GitHub リポジトリのデフォルトブランチで利用可能なカスタムエージェントを選択
- **マルチルートワークスペース対応** — マルチルートまたは空のワークスペースで、クラウドエージェントに使用するフォルダを選択可能
- **Checkout の常時表示** — GitHub Pull Requests 拡張機能がインストールされていなくても Checkout オプションが表示され、選択時に自動インストール

**ステータス**: **[GA]**
**対象ユーザー**: クラウドエージェントを利用するユーザー

> 📷 [画像: クラウドエージェントのモデル選択ピッカー](https://code.visualstudio.com/assets/updates/1_109/cloud-agent/model-picker.png)
> 📷 [画像: クラウドエージェントのカスタムエージェント選択](https://code.visualstudio.com/assets/updates/1_109/cloud-agent/custom-agent.png)
> 📷 [画像: マルチルートサポート](https://code.visualstudio.com/assets/updates/1_109/cloud-agent/cloud-repository-picker.png)

#### Background agents

バックグラウンドエージェントがローカル・クラウドエージェントと同等の機能を持つよう改善された。

- **カスタムエージェント対応** — バックグラウンドエージェントでもカスタムエージェントを選択可能
- **画像添付** — コンテキストとして画像を添付可能
- **マルチルートワークスペース対応** — 使用するフォルダを選択可能
- **ターンごとの自動コミット** — バックグラウンドエージェントがターン終了時に Git worktree への変更を自動コミット。Keep/Undo アクションが不要になり、変更ファイルの表示が簡素化

##### Agent sessions welcome page (Experimental)
- 複数エージェントの並行管理時に最近のセッションを一覧表示する新しいウェルカムページ
- `workbench.startupEditor` を `agentSessionsWelcomePage` に設定して有効化

**ステータス**: バックグラウンドエージェント改善は **[GA]**、Welcome page は **[Experimental]**
**対象ユーザー**: バックグラウンドエージェントを活用するユーザー

> 📷 [画像: バックグラウンドエージェントのカスタムエージェント選択](https://code.visualstudio.com/assets/updates/1_109/background-agent-custom-agent.png)
> 📷 [画像: バックグラウンドエージェントでの画像サポート](https://code.visualstudio.com/assets/updates/1_109/background-agent-image-support.png)
> 📷 [画像: バックグラウンドエージェントのマルチルートサポート](https://code.visualstudio.com/assets/updates/1_109/background-agent-multi-root.png)
> 📷 [画像: Agent Sessions Welcome Page](https://code.visualstudio.com/assets/updates/1_109/agent-sessions-welcome-page.png)

### Agent Customization

#### 概要
AI がコードベースとどう連携するかを制御し、チーム全体で共有するためのカスタマイズ機能が大幅に拡充された。Agent Skills の GA 化、Organization-wide instructions のサポート、カスタムエージェントの呼び出し制御、複数モデルサポート、Language Models エディタの改善など、エージェントの振る舞いをきめ細かく制御できるようになった。

#### 機能詳細

#### Set up your workspace for AI with `/init`

チャットで `/init` スラッシュコマンドを実行すると、ワークスペースの既存 AI 設定ファイル（`copilot-instructions.md`、`AGENTS.md` など）を検出し、プロジェクト構造とコーディングパターンを分析して、プロジェクトに合わせたワークスペース指示を自動生成・更新する。

- `/init` コマンドは contributed prompt file として実装されているため、基盤プロンプトを変更してカスタマイズ可能

**ステータス**: **[GA]**
**対象ユーザー**: プロジェクトの AI 設定を素早く整備したいユーザー

#### Agent Skills are generally available

Agent Skills が正式リリースされ、デフォルトで有効化された。スキルは特定のドメイン（テスト戦略、API 設計、パフォーマンス最適化など）に特化した機能・知識・ワークフローを提供する。

- **Chat: Configure Skills** コマンドで利用可能なスキルを一覧表示
- **Chat: New Skill File** で新しいスキルを作成
- デフォルトのスキル検索パス: `.github/skills`、`.claude/skills`（ワークスペース）、`~/.copilot/skills`、`~/.claude/skills`（ユーザーホーム）
- `chat.agentSkillsLocations` でカスタムパスを追加可能
- 拡張機能作者は `chatSkills` contribution point でスキルを配布可能

```json
{
  "contributes": {
    "chatSkills": [
      {
        "path": "./skills/my-skill"
      }
    ]
  }
}
```

**ステータス**: **[GA]**
**対象ユーザー**: AI の出力品質を向上させたいすべてのユーザー、拡張機能開発者

> 📷 [画像: Chat ビューでの Configure Skills オプション](https://code.visualstudio.com/assets/updates/1_109/configure-skills.png)

#### Organization-wide instructions

GitHub Organization が Copilot 用にカスタム指示を設定している場合、それがチャットセッションに自動的に適用されるようになった。

- デフォルトで有効。`github.copilot.chat.organizationInstructions.enabled` を `false` にして無効化可能
- 以前のリリースで追加された Organization レベルのカスタムエージェントに加え、カスタム指示もサポート

**ステータス**: **[GA]**
**対象ユーザー**: GitHub Organization に所属するチーム

#### Custom agent file locations

カスタムエージェント定義ファイル（`.agent.md`）の検索先ディレクトリを設定可能になった。

- デフォルト: `.github/agents`
- `chat.agentFilesLocations` で追加ディレクトリを指定し、プロジェクト横断やワークスペース外の中央管理に対応

```json
{
    "chat.agentFilesLocations": {
        "~/.vscode/agents": true,
        "shared/team-agents": true
    }
}
```

**ステータス**: **[GA]**
**対象ユーザー**: 複数プロジェクトでエージェントを共有するユーザー

#### Control how custom agents are invoked

カスタムエージェントの frontmatter に新しい属性が追加され、呼び出し方法を細かく制御可能になった。

- `user-invokable` — エージェントドロップダウンに表示するか制御。`false` でプログラム的またはサブエージェント経由のみアクセス可能
- `disable-model-invocation` — 他のエージェントからサブエージェントとして呼び出されることを防止
- `agents` — 当該エージェントが呼び出せるサブエージェントを制限。`agent` ツールと併用
- カスタムエージェントのサブエージェント利用には `chat.customAgentInSubagent.enabled` の有効化が必要

```Markdown
---
name: my-internal-agent
user-invokable: false
---

This agent can only be invoked as a subagent
```

```Markdown
---
name: Foo
tools: ['agent']
agents: ['Modify', 'Search']
---

This agent can only use the Modify and Search subagents.
```

**ステータス**: **[GA]**（サブエージェント連携は設定依存）
**対象ユーザー**: エージェントオーケストレーションを構築するユーザー

#### Multiple model support for custom agents

カスタムエージェントの frontmatter で複数モデルを指定可能になった。リスト内の最初の利用可能なモデルが使用され、フォールバックとして機能する。

```Markdown
---
name: my-agent
model: ['Claude Sonnet 4.5 (copilot)', 'GPT-5 (copilot)']
---

This agent prefers Claude Sonnet 4.5 but falls back to GPT-5 if unavailable.
```

**ステータス**: **[GA]**
**対象ユーザー**: 複数モデルを使い分けるカスタムエージェント作成者

#### Chat customization diagnostics

チャットカスタマイズファイル（エージェント、プロンプト、指示、スキル）のロード状況とエラーを一覧表示する診断ビューが追加された。

- Chat ビューで右クリック → **Diagnostics** で Markdown ドキュメントを表示
- ユーザープロファイル、ワークスペース、拡張機能、GitHub Organization から読み込まれたファイルを一覧

**ステータス**: **[GA]**
**対象ユーザー**: カスタマイズの問題をトラブルシューティングするユーザー

> 📷 [画像: Chat Customization Diagnostics ビュー](https://code.visualstudio.com/assets/updates/1_109/chat-customization-diagnostics.png)

#### Language Models editor

言語モデルを管理・設定する Language Models エディタが機能強化された。

- **プロバイダごとに複数設定** — 同一プロバイダで異なる API キーの設定を作成可能（個人用 / チーム用の使い分け）
- **Azure プロバイダのモデル設定** — `chatLanguageModels.json` にスニペットテンプレートを挿入して設定
- **プロバイダグループ管理** — 既存グループの設定更新やグループ削除
- **UI 改善** — キーボードでのモデル表示切り替え、コンテキストメニュー、マルチセレクトによる一括操作
- **設定ファイルの分離** — モデル設定が `chatLanguageModels.json` に格納され、直接編集・共有が容易
- **モデルプロバイダ設定 UI** — プロバイダが設定スキーマを宣言し、VS Code が設定 UI を提供（Proposed API）

**ステータス**: **[GA]**（プロバイダ設定 UI は **[Proposed API]**）
**対象ユーザー**: 複数の言語モデルプロバイダを利用するユーザー

> 📷 [画像: 複数 Gemini グループの設定](https://code.visualstudio.com/assets/updates/1_109/chat-lm-editor-groups.png)
> 🎬 [動画: Azure モデル設定](https://code.visualstudio.com/assets/updates/1_109/chat-lm-editor-azure-config.mp4)
> 🎬 [動画: Language Models エディタの UI 改善](https://code.visualstudio.com/assets/updates/1_109/chat-lm-editor-improv.mp4)
> 📷 [画像: 設定ファイルを開くファイルアイコン](https://code.visualstudio.com/assets/updates/1_109/language-models-editor-config-file.png)

#### Language model configuration

言語モデルの設定に関する複数の改善。

- **Plan 実装のデフォルトモデル (Experimental)** — `github.copilot.chat.implementAgent.model` で Plan agent の実装ステップに使用するデフォルトモデルを指定（形式: `Model Name (vendor)`）
- **インラインチャットのデフォルトモデル** — `inlineChat.defaultModel` でインラインチャットに使用するモデルを固定可能
- **エージェントハンドオフのモデル指定** — `.agent.md` 内のハンドオフ設定でオプショナルな `model` パラメータを指定可能

**ステータス**: Plan 実装モデルは **[Experimental]**、その他は **[GA]**
**対象ユーザー**: モデル選択を細かく制御したいユーザー

> 📷 [画像: implementAgent.model 設定](https://code.visualstudio.com/assets/updates/1_109/implement-agent-model-setting.png)
> 📷 [画像: インラインチャットのデフォルトモデル設定](https://code.visualstudio.com/assets/updates/1_109/inline-chat-default-model.png)
> 📷 [画像: エージェントハンドオフのモデルパラメータ](https://code.visualstudio.com/assets/updates/1_109/handoff-model-parameter.png)

#### Agent customization skill (Experimental)

新しい **agent-customization** スキルが追加された。カスタムエージェント、指示、プロンプト、スキルの作成方法に関する質問があった場合、エージェントが自動的にこのスキルをロードして正確なガイダンスを提供する。

- カバー範囲: Custom Agents（`.agent.md`）、Custom Instructions（`.instructions.md`）、Prompt Files（`.prompt.md`）、Skills（`SKILL.md`）、Workspace Instructions（`copilot-instructions.md`、`AGENTS.md`）
- `chat.agentCustomizationSkill.enabled` で有効化

**ステータス**: **[Experimental]**
**対象ユーザー**: AI カスタマイズの方法を学びたいユーザー

### Agent Extensibility

#### 概要
Claude Agent のネイティブサポート、MCP Apps によるリッチなインタラクティブ UI、エージェントオーケストレーションパターンの確立など、エージェントの拡張性が大幅に向上したセクション。Anthropic モデルの機能改善も含まれる。

#### 機能詳細

#### Agent orchestration

エージェントオーケストレーションは、複数の専門エージェントが協調して共通の目標を達成する複雑な AI ワークフローを構築するためのパターン。

- **コンテキスト効率**: 各サブエージェントが専用コンテキストウィンドウで動作し、コンテキストオーバーフローを防止
- **専門化**: 異なるエージェントがタスクに最適化された異なるモデルを使用可能
- **並列実行**: 独立タスクを複数サブエージェントで並列実行

VS Code はカスタムエージェント、サブエージェント、呼び出し制御を組み合わせてオーケストレーションフローを構築できる。コミュニティの実装例:

- [Copilot Orchestra](https://github.com/ShepAlderson/copilot-orchestra) — Conductor が計画・実装・コードレビューのサブエージェントをオーケストレーション
- [GitHub Copilot Atlas](https://github.com/bigguy345/Github-Copilot-Atlas) — Prometheus（計画）、Oracle（調査）、Sisyphus（実装）、Explorer（コード探索）の専門エージェント群

**ステータス**: **[GA]**
**対象ユーザー**: 複雑なワークフローを自動化したいユーザー

> 📷 [画像: エージェントオーケストレーションの概念図](https://code.visualstudio.com/assets/updates/1_109/agent-orchestration-diagram.png)

#### Claude Agent (Preview)

Claude Agent SDK のネイティブサポートがプレビューとして導入された。GitHub Copilot サブスクリプションに含まれる Claude モデルを使って、Claude Agent SDK にタスクを委譲できる。

- Anthropic 公式の Claude Agent ハーネスを使用しており、他の Claude Agent 実装と同じプロンプト、ツール、アーキテクチャを共有
- セッションタイプピッカーで Local / Background / Cloud と並んで Claude Agent を選択可能
- 活発な開発中であり、今後のリリースで機能追加予定

**ステータス**: **[Preview]**
**対象ユーザー**: Anthropic Claude のエージェント機能を活用したいユーザー

> 📷 [画像: セッションタイプピッカーでの Claude Agent](https://code.visualstudio.com/assets/updates/1_109/claude-agent.png)

#### Anthropic models

Anthropic モデルサポートに複数の改善が加えられた。

- **Messages API with interleaved thinking** — Messages API 経由でインターリーブされた推論を実現。ツール呼び出し間で Claude が推論し、文脈に沿った応答を提供。`github.copilot.chat.anthropic.thinking.budgetTokens` で思考トークンの予算を設定（`0` で拡張思考を無効化）
- **Tool search tool** — 利用可能な大量のツールから最適なものを Claude が自律的に選択。`github.copilot.chat.anthropic.toolSearchTool.enabled` で切り替え
- **Context editing (Experimental)** — 長い会話でのコンテキスト管理を効率化。過去のターンのツール結果と思考トークンをクリアし、要約を遅延させてコンテキストを維持。`github.copilot.chat.anthropic.contextEditing.enabled` で有効化

**ステータス**: Messages API / Tool search は **[GA]**、Context editing は **[Experimental]**
**対象ユーザー**: Anthropic モデルを使用するすべてのユーザー

#### Support for MCP Apps

MCP Apps のサポートが追加された。MCP Apps は MCP サーバーがクライアント上でリッチなインタラクティブ UI を表示する機能で、サーバーが返すアプリは自動的に表示される。

- [MCP Apps デモリポジトリ](https://github.com/digitarald/mcp-apps-playground)
- [MCP Apps SDK](https://github.com/modelcontextprotocol/ext-apps/)
- [VS Code MCP ドキュメント](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)
- [MCP サーバー開発ガイド](https://code.visualstudio.com/docs/copilot/guides/mcp-developer-guide)

**ステータス**: **[GA]**
**対象ユーザー**: MCP サーバー開発者、MCP を活用するユーザー

> 📷 [画像: MCP App によるインタラクティブなフレームグラフ表示](https://code.visualstudio.com/assets/updates/1_109/mcp-apps-flame-graph.png)

#### Support for custom registry base URLs for MCP packages

MCP サーバーマニフェストファイルで `registryBaseUrl` プロパティがサポートされた。組織内の Azure DevOps フィードやカスタム PyPI リポジトリなど、プライベートまたは代替パッケージレジストリからの MCP サーバーデプロイが可能になった。

**ステータス**: **[GA]**
**対象ユーザー**: プライベートレジストリを運用する組織

### Agent Optimizations

#### 概要
Copilot Memory によるセッション横断のコンテキスト記憶、非 GitHub ワークスペースでの外部インデックスによる高速コード検索、ワークスペース外ファイルの読み取り許可、パフォーマンス改善など、エージェントの効率と精度を向上させる機能群。

#### 機能詳細

#### Copilot Memory (Preview)

セッション間で重要な情報を記憶・呼び出しできる Copilot Memory が追加された。

- チャット中のメモリツールで直接メモリの取得・更新が可能
- 情報を記憶すべきタイミング（例: 「疑問がある時は必ず確認質問をする」）とメモリを参照すべきタイミングを自律的に判断
- `github.copilot.chat.copilotMemory.enabled` を `true` にして有効化
- [GitHub の Copilot 設定](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory)でメモリの一覧表示・管理

**ステータス**: **[Preview]**
**対象ユーザー**: 反復的なコンテキスト提供を減らしたいすべてのユーザー

> 📷 [画像: メモリツールと保存されたメモリ一覧](https://code.visualstudio.com/assets/updates/1_109/copilot-memory-tool.png)

#### External indexing for non-GitHub workspaces (Preview)

GitHub でホストされていないワークスペースでもリモートインデックスによる高速コード検索が利用可能になった。

- `#codebase` を非 GitHub ワークスペースで使用すると、コードベースのインデックスを構築
- 初回リクエスト時にインデックスが構築され（リポジトリサイズとネットワーク速度に依存）、以降はキャッシュを使用
- ファイル変更・保存時にインデックスが自動更新
- `github.copilot.chat.advanced.workspace.codeSearchExternalIngest.enabled` で有効化
- GitHub ホストのワークスペースはすでにリモートインデックスをサポート済み

**ステータス**: **[Preview]**
**対象ユーザー**: 非 GitHub ワークスペースでコード検索を高速化したいユーザー

#### Read files outside workspace

エージェントがワークスペース外のファイルやディレクトリを読み取れるようになった。

- 以前は自動拒否されていた外部ファイルアクセスに対してユーザーに許可/拒否のプロンプトを表示
- セッション全体に対してアクセスを許可し、同一フォルダ配下の繰り返し確認を回避可能

**ステータス**: **[GA]**
**対象ユーザー**: ワークスペース外のリソースを参照する必要のあるユーザー

> 📷 [画像: ワークスペース外ファイルアクセスの許可/拒否プロンプト](https://code.visualstudio.com/assets/updates/1_109/agent-external-file-access.png)

#### Performance improvements

パフォーマンスに関する複数の改善。

- **長いチャット会話** — 長い会話の開きやスクロールがスムーズに。会話の永続化も最適化され信頼性向上
- **並列依存タスク** — エージェント経由のタスク実行で、依存タスクがシーケンシャルではなく並列処理に。複数の独立ビルドステップを持つプロジェクトでビルド時間が大幅に短縮

**ステータス**: **[GA]**
**対象ユーザー**: すべてのユーザー

### Agent Security and Trust

#### 概要
エージェントが実行するターミナルコマンドの安全性を高めるための機能群。ファイルシステムとネットワークアクセスを制限するサンドボックス、安全なコマンドの自動承認、ターミナルツールのライフサイクル改善が含まれる。

#### 機能詳細

#### Terminal sandboxing (Experimental)

エージェントが実行するターミナルコマンドをサンドボックス環境で制限する機能がExperimental として導入された。

- ファイルシステムアクセスをワークスペースフォルダのみに制限
- ネットワークアクセスを信頼済みドメインのみに制限可能
- `chat.tools.terminal.sandbox.enabled` を `true` にして有効化
- サンドボックス有効時:
  - コマンドはカレントディレクトリへの読み書き権限をデフォルトで保持
  - 標準の確認ダイアログなしで実行（制御された環境のため）
  - ネットワークアクセスはデフォルトですべてのドメインでブロック
- macOS / Linux のみサポート（Windows では設定は効果なし）
- `chat.tools.terminal.sandbox.linuxFileSystem`、`chat.tools.terminal.sandbox.macFileSystem`、`chat.tools.terminal.sandbox.network` で詳細設定

**ステータス**: **[Experimental]**
**対象ユーザー**: エージェントのコマンド実行セキュリティを強化したいユーザー

#### Terminal tool lifecycle improvements

ターミナルツールのライフサイクルに関する複数の改善。

- ターミナルツール呼び出しを手動でバックグラウンドに移行可能（エージェントが他の作業を継続）
- `timeout` プロパティが必須化（`0` でタイムアウトなし）。想定外の事態でエージェントに制御を返すための安全措置
- 新しい `awaitTerminal` ツール — バックグラウンドターミナルの完了を待機。`echo "successful"` や `sleep n` の代替
- 新しい `killTerminal` ツール — バックグラウンドターミナルを終了してクリーンアップ
- カレントディレクトリに関する指示の改善（非バックグラウンドターミナルはディレクトリを保持、バックグラウンドは常にワークスペースディレクトリで開始）

**ステータス**: **[GA]**
**対象ユーザー**: エージェントモードでターミナルツールを利用するユーザー

> 📷 [画像: バックグラウンド実行継続ボタン](https://code.visualstudio.com/assets/updates/1_109/terminal-tool-continue-in-background.png)

#### Terminal auto-approval

ターミナル自動承認（`chat.tools.terminal.enableAutoApprove`）が有効な場合に自動承認されるコマンドが追加された。

- `Set-Location`、`dir`、`od`、`xxd`（フラグと単一入力ファイル）
- `docker` — すべての安全なサブコマンド
- `npm`、`yarn`、`pnpm` — すべての安全なサブコマンド

**ステータス**: **[GA]**
**対象ユーザー**: エージェントの確認プロンプトを減らしたいユーザー

### Terminal enhancements

#### 概要
ターミナル体験の改善。Sticky scroll の選択的無視、Kitty keyboard protocol のサポート、制限付きワークスペースでのターミナル利用許可、winpty サポートの廃止など、品質向上の改善が含まれる。

#### 機能詳細

#### Selectively ignore sticky scroll

Sticky scroll で表示したくないコマンド（`clear` など）を `terminal.integrated.stickyScroll.ignoredCommands` で設定可能になった。デフォルトで `copilot`、`claude`、`codex`、`gemini` などのエージェント CLI が除外済み。

**ステータス**: **[GA]**
**対象ユーザー**: ターミナルの sticky scroll を利用するユーザー

#### Removal of winpty support

[node-pty](https://github.com/microsoft/node-pty) から winpty サポートが削除された。Windows 10 version 1809（2018年秋）より前のバージョンではターミナルが動作しなくなる。[ConPTY](https://devblogs.microsoft.com/commandline/windows-command-line-introducing-the-windows-pseudo-console-conpty/) への移行が推奨される。`"terminal.integrated.windowsUseConptyDll": true` で動作する可能性があるが、Experimental 扱い。

**ステータス**: **[GA]**（Breaking Change）
**対象ユーザー**: 古い Windows バージョンを使用しているユーザー

#### Allow terminals to be opened in restricted workspaces

ワークスペースの信頼が付与されていない場合でもターミナルを開けるオプトイン設定が追加された。

- `terminal.integrated.allowInUntrustedWorkspace` で有効化
- セキュリティを意識しているユーザーがシェル設定でコード実行を防止している場合に有用

**ステータス**: **[GA]**
**対象ユーザー**: 制限付きワークスペースでターミナルを利用したいユーザー

#### New VT features

##### Kitty keyboard protocol (Experimental)
[Kitty keyboard protocol](https://sw.kovidgoyal.net/kitty/keyboard-protocol/) が実装され、安定版にロールアウト。従来のキーストロークエンコーディングの制限を解消する。

- Alt と Ctrl 以外のモディファイアや複数モディファイアのエンコード
- キーの押下・リリース・リピートイベントの処理
- `Escape` キーのような曖昧なキーストロークの解消
- 一部のエージェント CLI で Shift+Enter が `/terminalSetup` なしで動作するようになる
- `terminal.integrated.enableKittyKeyboardProtocol` で有効化

##### Win32 input mode (Experimental)
Windows と ConPTY 向けの [win32 input mode](https://github.com/microsoft/vscode/issues/286896) の Experimental バージョン。Kitty keyboard protocol と類似の目的だが Windows に特化。

- `terminal.integrated.enableWin32InputMode` で有効化（本リリースではデフォルト無効）

##### その他
- Bold と faint SGR プロパティの独立制御（`SGR 222`、`SGR 221`）のサポート

**ステータス**: **[Experimental]**
**対象ユーザー**: ターミナルアプリケーションのキー入力を改善したいユーザー

### Coding and editor

#### 概要
日常のコーディング体験を改善する複数の機能強化。ブラケットマッチングの前景色カスタマイズ、ダブルクリックによるブラケット/文字列コンテンツ選択、TypeScript リネーム提案、ゴーストテキストの視認性向上、スニペットのファイルパターン制限、shebang 言語検出の改善が含まれる。

#### 機能詳細

#### Bracket matching foreground color

マッチングブラケットのテキスト色を `editorBracketMatch.foreground` カラートークンでカスタマイズ可能になった。従来は背景色（`editorBracketMatch.background`）とボーダー色（`editorBracketMatch.border`）のみ変更可能だった。

```json
{
    "workbench.colorCustomizations": {
        "editorBracketMatch.foreground": "#ff0000"
    }
}
```

デフォルトは `null`（通常のテキスト色を継承）。

**ステータス**: **[GA]**
**対象ユーザー**: エディタの見た目をカスタマイズしたいユーザー

#### Select bracket and string content with double-click

開きブラケットの直後、または閉じブラケットの直前でダブルクリックすると、ブラケット内のコンテンツ全体を選択可能になった。文字列（引用符）にも同様に動作する。

**ステータス**: **[GA]**
**対象ユーザー**: すべてのエディタユーザー

> 🎬 [動画: エディタでの新しいダブルクリック動作](https://code.visualstudio.com/assets/updates/1_109/editor-double-click.mp4)

#### Rename suggestions for TypeScript

TypeScript のリネーム提案が、既存の宣言を上書き入力する場合にも動作するようになった。例えば `let index = 0;` を `let chunkIndex = 0;` にタイプで変更すると、Next edit suggestions が `Shift+Tab` で `index` → `chunkIndex` のリネームを提案する。

- 現時点では TypeScript のみ対応

**ステータス**: **[GA]**
**対象ユーザー**: TypeScript 開発者

> 🎬 [動画: エディタでのリネーム後提案](https://code.visualstudio.com/assets/updates/1_109/post-rename.mp4)

#### Improved ghost text visibility

インライン提案（ゴーストテキスト）が3文字未満の連続する非空白文字の場合、点線下線が表示されるようになった。`)` のような1文字の提案が既存コードと区別しやすくなる。

**ステータス**: **[GA]**
**対象ユーザー**: インライン提案を利用するすべてのユーザー

> 📷 [画像: 短い提案での点線下線付きゴーストテキスト](https://code.visualstudio.com/assets/updates/1_109/ghost-text-underline.png)

#### Snippet file patterns

スニペットが表示されるファイルを `include` / `exclude` glob パターンで制御可能になった。

```json
{
    "Travis CI node_js": {
        "include": ".travis.yml",
        "prefix": "node",
        "body": ["language: node_js", "node_js:", "  - $1"],
        "description": "Node.js configuration for Travis CI"
    }
}
```

- パターンにパス区切りが含まれる場合は絶対パスにマッチ、含まれない場合はファイル名のみにマッチ
- `include` / `exclude` とも単一パターンまたはパターン配列を指定可能

**ステータス**: **[GA]**
**対象ユーザー**: スニペットの適用範囲を制御したいユーザー

#### Improved shebang language detection

shebang の言語検出が改善され、`#!/usr/bin/env -S deno -A` のような追加フラグ付きの `/usr/bin/env` 使用時に正しく TypeScript と検出されるようになった。Deno や Bun で TypeScript スクリプトを書く場合に有用。

**ステータス**: **[GA]**
**対象ユーザー**: Deno / Bun でスクリプトを書く開発者

### Workbench and productivity

#### 概要
統合ブラウザ（Preview）、エディタ復元制御、高度な設定表示、プロファイルのドラッグ＆ドロップインポート、SCM ビューの改善、セキュリティ改善（自動タスクのデフォルト無効化）、アクセシビリティ改善など、ワークベンチ全体の生産性向上に関する機能群。

#### 機能詳細

#### Integrated browser (Preview)

VS Code デスクトップ向けの新しい統合ブラウザが導入された。従来の Simple Browser（iframe ベース）の制限を克服し、Web サイト認証や Google / GitHub / Stack Overflow などの閲覧が可能になった。

- **永続データストレージ** — グローバル / ワークスペース / インメモリ（エフェメラル）のスコープ設定
- **エレメントをチャットに送信** — 要素を選択してエージェントに支援を依頼
- **フル機能の DevTools** 搭載
- **キーボードショートカット** 対応
- **ページ内検索** 対応
- **Browser: Open Integrated Browser** コマンドで起動
- `workbench.browser.openLocalhostLinks` で localhost リンクを統合ブラウザで開く
- `simpleBrowser.useIntegratedBrowser` で Simple Browser を置換
- `livePreview.useIntegratedBrowser` で Live Preview 拡張で使用

**ステータス**: **[Preview]**
**対象ユーザー**: エディタ内で Web アプリのプレビュー・デバッグを行いたいすべてのユーザー

> 🎬 [動画: 統合ブラウザの機能紹介](https://code.visualstudio.com/assets/updates/1_109/integrated-browser.mp4)

#### Restore editors on workspace open

`workbench.editor.restoreEditors` 設定でワークスペースオープン時にエディタを復元するかどうかを制御可能になった。無効化すると、前回のセッションのタブを開かずにクリーンな状態で開始する。

- 未保存（dirty）のエディタはデータ損失防止のため常に復元される

**ステータス**: **[GA]**
**対象ユーザー**: ワークスペースの起動動作をカスタマイズしたいユーザー

#### Advanced settings

`workbench.settings.showAdvancedSettings` を有効にすると、設定エディタで常に高度な設定を表示可能。毎回 `@tag:advanced` フィルタを適用する手間が不要になる。

**ステータス**: **[GA]**
**対象ユーザー**: 高度な設定を頻繁に変更するユーザー

#### Import profiles via drag and drop

`.code-profile` ファイルを VS Code ウィンドウにドラッグ＆ドロップして設定プロファイルをインポート可能になった。

**ステータス**: **[GA]**
**対象ユーザー**: プロファイルを共有・適用するユーザー

#### Output channel filter improvements

Output パネルのフィルタが否定パターンと複数フィルタに対応した。

- `!debug` で "debug" を含む行を非表示
- カンマで複数パターンを結合

**ステータス**: **[GA]**
**対象ユーザー**: Output パネルを利用するユーザー

#### Filter problems by source

Problems パネルで診断のソース/オーナーによるフィルタリングが可能になった。

- `source:ts` で TypeScript 診断のみ表示
- `!source:cSpell` でスペルチェッカー警告を非表示

**ステータス**: **[GA]**
**対象ユーザー**: 多数の診断ソースを扱うユーザー

#### Extension editor shows configuration defaults

拡張機能エディタの Feature Contributions タブで、拡張機能が提供する設定のデフォルト値が表示されるようになった。

**ステータス**: **[GA]**
**対象ユーザー**: 拡張機能の設定を確認したいユーザー

#### Include additional files in git worktrees (Experimental)

バックグラウンドエージェント用に作成される git worktree に追加ファイルをコピーする設定。

- `git.worktreeIncludeFiles` でファイルや glob パターンを指定
- git に管理されていないローカル設定ファイルやビルドアーティファクトのコピーに有用

**ステータス**: **[Experimental]**
**対象ユーザー**: バックグラウンドエージェントで git worktree を使用するユーザー

#### Collapse All action in SCM view

Source Control ビューの Changes セクションで、ルートノードのコンテキストメニューから **Collapse All** アクションで展開されたディレクトリ構造を一括折りたたみ可能。

**ステータス**: **[GA]**
**対象ユーザー**: 大量の変更ファイルを扱うユーザー

#### Git: Delete command

新しい **Git: Delete** コマンドでコマンドパレットから `git rm` を直接実行可能。ワーキングディレクトリと Git インデックスの両方からファイルを削除し、エディタを閉じる。コミット済みで未変更のファイルのみ成功するため、通常のファイル削除より安全。

**ステータス**: **[GA]**
**対象ユーザー**: Git を使用するすべてのユーザー

#### Disable blame editor decoration hover

`git.blame.editorDecoration.hoverEnabled` を `false` に設定すると、インライン Git blame デコレーションのホバーポップアップを無効化可能。blame 情報は表示したままポップアップの邪魔を避けられる。

**ステータス**: **[GA]**
**対象ユーザー**: Git blame を利用するユーザー

#### Automatic tasks disabled by default

セキュリティ向上のため、`task.allowAutomaticTasks` のデフォルトが `on` から `off` に変更された。ワークスペースを開いた際の `tasks.json` で定義されたタスクの意図しない実行を防止する。

- 以前の動作に戻すには `task.allowAutomaticTasks` を `on` に設定

**ステータス**: **[GA]**（Breaking Change）
**対象ユーザー**: 自動タスクを利用していたユーザー

#### Accessibility improvements

アクセシビリティに関する複数の改善。

- **ストリーミング応答のアクセシブルビュー** — AI モデルの応答がリアルタイムでアクセシブルビューにストリーミング表示。thinking コンテンツも含む
- **安定したカーソル位置** — アクセシブルビューでのコンテンツ更新時にカーソル位置が維持され、スクリーンリーダーのナビゲーションが中断されない
- **新規チャットセッションの ARIA アラート** — 新しいチャットセッション作成時にスクリーンリーダーに通知
- **ツール呼び出し情報の改善** — アクセシブルビューでのツール呼び出し情報がより完全に
- **カーソル位置アナウンスコマンド** — `Ctrl/Cmd+Alt+Shift+G` で現在の行・列位置を読み上げ

**ステータス**: **[GA]**
**対象ユーザー**: スクリーンリーダーを使用するユーザー

#### Enterprise improvements

GitHub Organization ポリシーの適用信頼性が向上した。

- 複数アカウントがサインインしている場合、優先 GitHub Copilot アカウントに基づいてポリシーが正しく適用
- 起動時のネットワーク一時的不可用時でも Organization ポリシーが一貫して適用

**ステータス**: **[GA]**
**対象ユーザー**: 管理されたエンタープライズ環境のユーザー

### Extensions and API

#### 概要
拡張機能作成者向けの新しい API と機能。Finalized な Quick Input Button API、チャットモデルプロバイダの設定スキーマ宣言（Proposed）、チャットリソースプロバイダ（Proposed）、チャットセッションアイテムコントローラ（Proposed）、チャット出力レンダラ更新（Proposed）など、拡張機能エコシステムを拡張する多数の API が含まれる。

#### 機能詳細

#### GitHub Pull Requests

[GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) 拡張機能が引き続き改善。[0.128.0 のchangelog](https://github.com/microsoft/vscode-pull-request-github/blob/main/CHANGELOG.md#01280) を参照。

**ステータス**: **[GA]**

#### Finalized Quick Input Button Location APIs

`QuickPick` や `InputBox` の `buttons` プロパティで各ボタンの配置場所を `location` プロパティで指定可能になった。

- `Title` — クイック入力のタイトルエリア（デフォルト）
- `Inline` — 入力ボックスの右側に描画
- `Input` — 入力ボックス内の右側に描画

**ステータス**: **[GA]**（Finalized API）
**対象ユーザー**: 拡張機能開発者

#### Finalized Quick Input Button Toggle APIs

クイック入力にトグルボタンを作成可能。`QuickInputButton` の `toggle` プロパティに `{ checked: boolean }` を設定し、`checked` プロパティでオン/オフ状態を読み書きする。

**ステータス**: **[GA]**（Finalized API）
**対象ユーザー**: 拡張機能開発者

#### Proposed APIs

以下はすべてプロポーザル段階の API であり、今後変更または削除される可能性がある。

#### Chat Model Provider Configuration

> ⚠️ この API はプロポーザル段階であり、今後変更または削除される可能性があります。
> プロポーザルファイル: `vscode.proposed.lmConfiguration.d.ts`

チャットモデルプロバイダ拡張機能が `languageModelChatProviders` contribution point で設定要件（API キー、モデル設定など）を宣言し、VS Code がネイティブ UI を提供する新しい API。

- プリミティブ型（`string`、`number`、`boolean`）にはネイティブ UI コントロールを提供
- 複合型（`array`、`object`）には JSON エディタで設定ファイルを直接編集（スキーマバリデーション + IntelliSense サポート）
- `secret` プロパティでセキュアストレージとマスク表示を自動処理
- 将来のリリースで既存の `managementCommand` プロパティを置換予定

**シンプルな設定例（API キーのみ）:**
```json
{
  "contributes": {
    "languageModelChatProviders": [
      {
        "vendor": "my-provider",
        "displayName": "My Provider",
        "configuration": {
          "properties": {
            "apiKey": {
              "type": "string",
              "secret": true,
              "description": "API key for My Provider",
              "title": "API Key"
            }
          },
          "required": ["apiKey"]
        }
      }
    ]
  }
}
```

**プロバイダ側での設定取得:**
```ts
vscode.lm.registerLanguageModelChatProvider('my-provider', {
  provideLanguageModelResponse: (messages, options, extensionToken, configuration, token) => {
    const apiKey = configuration.apiKey;
    const models = configuration.models;
    // Use configuration to make API calls...
  }
});
```

**ステータス**: **[Proposed API]**
**対象ユーザー**: 言語モデルプロバイダ拡張機能の開発者

#### Chat prompt files API

> ⚠️ この API はプロポーザル段階であり、今後変更または削除される可能性があります。
> プロポーザルファイル: `vscode.proposed.chatPromptFiles.d.ts`

拡張機能がプログラム的に動的なチャットリソース（プロンプトファイル、カスタムエージェント、指示、スキル）を提供できる API。

```ts
vscode.chat.registerSkillProvider({
  onDidChangeSkills: onDidChangeEvent,
  provideSkills(context, token): ChatResource[] {
    return [{ uri: vscode.Uri.parse('my-extension:/skills/debugging/SKILL.md') }];
  }
});
// registerCustomAgentProvider(), registerInstructionsProvider(), registerPromptFileProvider() も同様
```

**ステータス**: **[Proposed API]**
**対象ユーザー**: チャットリソースを動的に提供したい拡張機能開発者

#### Chat item controller API

> ⚠️ この API はプロポーザル段階であり、今後変更または削除される可能性があります。

チャットセッションビューにアイテムを提供するための API が、プロバイダベースからコントローラベースに刷新された。

- 拡張機能が VS Code にプッシュ型で変更を通知（従来はプル型）
- `ChatSessionItems` がマネージドオブジェクトとなり、プロパティ更新でリアルタイム反映

```ts
const controller = vscode.chat.createChatSessionItemController(
    'myExtension.chatSessions',
    async (token: vscode.CancellationToken) => {
        const sessions = await fetchSessionsFromBackend();
        const items = sessions.map(session =>
            controller.createChatSessionItem(
                vscode.Uri.parse(`my-scheme://session/${session.id}`),
                session.title
            )
        );
        controller.items.replace(items);
    }
);
```

**ステータス**: **[Proposed API]**
**対象ユーザー**: チャットセッション連携を行う拡張機能開発者

#### Chat output renderer API updates

> ⚠️ この API はプロポーザル段階であり、今後変更または削除される可能性があります。

チャット応答でカスタムインタラクティブコンテンツをレンダリングする API が更新された。

- レンダラが `Webview` ではなく `ChatOutputWebview` として渡されるようになり、dispose イベントの監視とリソースクリーンアップが可能
- [サンプル拡張機能](https://github.com/microsoft/vscode-extension-samples/tree/main/chat-output-renderer-sample)を参照

**ステータス**: **[Proposed API]**
**対象ユーザー**: チャット出力のカスタムレンダリングを行う拡張機能開発者

#### Portable mode detection

> ⚠️ この API はプロポーザル段階であり、今後変更または削除される可能性があります。
> プロポーザルファイル: `vscode.proposed.envIsAppPortable.d.ts`

`env.isAppPortable` プロパティで VS Code がポータブルモードで動作しているかを検出可能。

```ts
if (vscode.env.isAppPortable) {
    // Running in portable mode
}
```

**ステータス**: **[Proposed API]**
**対象ユーザー**: ポータブルモード対応を行う拡張機能開発者

## 開発者・拡張機能作成者向け

### Finalized APIs

- **Quick Input Button Location API** — ボタンの配置場所（Title / Inline / Input）を制御
- **Quick Input Button Toggle API** — トグルボタンの作成と状態管理

### Proposed APIs

| API | プロポーザルファイル | 概要 |
|---|---|---|
| Chat Model Provider Configuration | `vscode.proposed.lmConfiguration.d.ts` | モデルプロバイダの設定スキーマ宣言とネイティブ UI |
| Chat prompt files API | `vscode.proposed.chatPromptFiles.d.ts` | 動的チャットリソース（プロンプト、エージェント、指示、スキル）の提供 |
| Chat item controller API | (chatSessionsProvider) | チャットセッションビューへのコントローラベースのアイテム提供 |
| Chat output renderer API | — | チャット応答でのカスタム WebView レンダリング |
| Portable mode detection | `vscode.proposed.envIsAppPortable.d.ts` | ポータブルモード検出 |

> ⚠️ これらの API はすべてプロポーザル段階であり、今後変更または削除される可能性があります。

## エンジニアリング・基盤改善

- **macOS 向け DMG イメージ** — ネイティブなドラッグ＆ドロップインストール体験を提供。すべてのサポートアーキテクチャで [VS Code ダウンロードページ](https://code.visualstudio.com/download)から入手可能
- **Windows 11 コンテキストメニュー統合** — ファイルエクスプローラーの右クリックメニューのトップレベルに VS Code エントリが追加。「Show more options」の選択が不要に
- **Windows のインストールレイアウト再設計** — インプレースアップデートの信頼性問題に対処。[Chromium のアップデートクライアント](https://github.com/microsoft/vscode/issues/249239)にインスパイアされたバージョン付きパッケージパスを採用
- **macOS での連続アップデート回避** — 前のアップデートが適用待ちの間に新しいアップデートが利用可能になった場合、前のアップデートを無効化して新しいものを適用。2回の再起動が不要に
- **Copilot 拡張機能の廃止** — GitHub Copilot 拡張機能が廃止され、すべての AI 機能は GitHub Copilot Chat 拡張機能に統合。VS Code アップデート時に廃止された拡張機能は自動アンインストール
- **Codicons の npm パッケージ化** — Codicons が `@vscode/codicons` npm パッケージから消費されるように変更（直接バンドルから移行）

> 📷 [画像: macOS DMG イメージ](https://code.visualstudio.com/assets/updates/1_109/macos-dmg-installer.png)
> 📷 [画像: Windows 11 コンテキストメニュー](https://code.visualstudio.com/assets/updates/1_109/win11-context-menu.png)
> 📷 [画像: 廃止された Copilot 拡張機能とアクティブな Copilot Chat 拡張機能](https://code.visualstudio.com/assets/updates/1_109/copilot-extension-deprecated.png)

## Notable fixes

- [vscode#276558](https://github.com/microsoft/vscode/issues/276558) — `editor.hover.enabled` を `onModifierKeyPressed` に設定している場合に、モディファイアキー押下でホバーが即座にトリガーされない問題を修正
- [vscode#58814](https://github.com/microsoft/vscode/issues/58814) — ターミナルプロセスへのファイルディスクリプタリークを修正

## コミュニティ貢献

主要な外部コントリビューション:

- **[@ChaseKnowlden](https://github.com/ChaseKnowlden)** — キーボードモディファイアホバーの即時トリガー修正 ([PR #276582](https://github.com/microsoft/vscode/pull/276582))
- **[@tamuratak](https://github.com/tamuratak)** — NativeEditContext / TextAreaEditContext でのアニメーションフレーム単位の DOM 更新最適化によるレンダリングパフォーマンス向上 ([PR #285906](https://github.com/microsoft/vscode/pull/285906))
- **[@SimonSiefke](https://github.com/SimonSiefke)** — フォルダ設定とタスクサービスのメモリリーク修正 ([PR #279230](https://github.com/microsoft/vscode/pull/279230), [PR #289863](https://github.com/microsoft/vscode/pull/289863))
- **[@KanishkRanjan](https://github.com/KanishkRanjan)** — 設定ツリーの安定化と起動時のゴーストスクロール修正 ([PR #278931](https://github.com/microsoft/vscode/pull/278931))
- **[@lucas-gomes-santana](https://github.com/lucas-gomes-santana)** — 非ラテン文字スクリプトでのスニペット大文字/小文字変換改善 ([PR #287150](https://github.com/microsoft/vscode/pull/287150))
- **[@daviddossett](https://github.com/daviddossett)** — ボタンと入力のポリッシュ ([PR #280457](https://github.com/microsoft/vscode/pull/280457))

その他、Issue tracking では [@gjsjohnmurray](https://github.com/gjsjohnmurray)、[@RedCMD](https://github.com/RedCMD)、[@IllusionMH](https://github.com/IllusionMH)、[@albertosantini](https://github.com/albertosantini) が貢献。`vscode-copilot-chat`、`vscode-js-debug`、`vscode-python-environments` 等の関連リポジトリにも多数の外部コントリビューションがあった。

## 設定項目まとめ

### Chat UX

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `chat.thinking.style` | 思考トークンの表示スタイル（詳細/コンパクト） | — | GA |
| `chat.agent.thinking.collapsedTools` | ツール表示の折りたたみ制御 | — | GA |
| `chat.agent.thinking.terminalTools` | ツール呼び出しとの思考インターリーブ表示 | — | GA |
| `chat.tools.autoExpandFailures` | 失敗したツール呼び出しの自動展開 | — | GA |
| `chat.askQuestions.enabled` | Ask Questions ツールの有効化 | — | Experimental |
| `inlineChat.affordance` | インラインチャットのアフォーダンス | — | Preview |
| `inlineChat.renderMode` | インラインチャットのレンダリングモード | — | Preview |

### Agent Session Management

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `chat.agentsControl.enabled` | エージェントステータスインジケータの有効化 | — | GA |
| `chat.agentsControl.clickBehavior` | コマンドセンターのチャットボタンのクリック動作 | — | GA |
| `chat.customAgentInSubagent.enabled` | カスタムエージェントのサブエージェント利用 | — | GA |
| `github.copilot.chat.searchSubagent.enabled` | 検索サブエージェントの有効化 | — | Experimental |
| `workbench.startupEditor` | スタートアップエディタ（`agentSessionsWelcomePage` オプション追加） | — | Experimental |

### Agent Customization

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `chat.useAgentSkills` | Agent Skills の使用 | `true` | GA |
| `chat.agentSkillsLocations` | スキル定義の検索パス | — | GA |
| `github.copilot.chat.organizationInstructions.enabled` | Organization-wide instructions の有効化 | `true` | GA |
| `chat.agentFilesLocations` | カスタムエージェント定義の検索パス | — | GA |
| `github.copilot.chat.implementAgent.model` | Plan 実装のデフォルトモデル | — | Experimental |
| `inlineChat.defaultModel` | インラインチャットのデフォルトモデル | — | GA |
| `chat.agentCustomizationSkill.enabled` | agent-customization スキルの有効化 | — | Experimental |

### Agent Extensibility (Anthropic models)

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `github.copilot.chat.anthropic.thinking.budgetTokens` | 拡張思考のトークン予算 | — | GA |
| `github.copilot.chat.anthropic.toolSearchTool.enabled` | Tool search tool の有効化 | — | GA |
| `github.copilot.chat.anthropic.contextEditing.enabled` | Context editing の有効化 | — | Experimental |

### Agent Optimizations

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `github.copilot.chat.copilotMemory.enabled` | Copilot Memory の有効化 | — | Preview |
| `github.copilot.chat.advanced.workspace.codeSearchExternalIngest.enabled` | 外部インデックスの有効化 | — | Preview |

### Agent Security and Trust

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `chat.tools.terminal.sandbox.enabled` | ターミナルサンドボックスの有効化 | `false` | Experimental |
| `chat.tools.terminal.sandbox.linuxFileSystem` | Linux ファイルシステムサンドボックス設定 | — | Experimental |
| `chat.tools.terminal.sandbox.macFileSystem` | macOS ファイルシステムサンドボックス設定 | — | Experimental |
| `chat.tools.terminal.sandbox.network` | ネットワークサンドボックス設定 | — | Experimental |
| `chat.tools.terminal.enableAutoApprove` | ターミナル自動承認の有効化 | — | GA |

### Terminal enhancements

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `terminal.integrated.stickyScroll.ignoredCommands` | Sticky scroll で無視するコマンド | — | GA |
| `terminal.integrated.allowInUntrustedWorkspace` | 制限付きワークスペースでのターミナル許可 | — | GA |
| `terminal.integrated.enableKittyKeyboardProtocol` | Kitty keyboard protocol の有効化 | — | Experimental |
| `terminal.integrated.enableWin32InputMode` | Win32 input mode の有効化 | — | Experimental |

### Workbench and productivity

| 設定キー | 説明 | デフォルト | ステータス |
|---|---|---|---|
| `workbench.browser.openLocalhostLinks` | localhost リンクを統合ブラウザで開く | — | Preview |
| `simpleBrowser.useIntegratedBrowser` | Simple Browser を統合ブラウザに置換 | — | Preview |
| `livePreview.useIntegratedBrowser` | Live Preview で統合ブラウザを使用 | — | Preview |
| `workbench.editor.restoreEditors` | ワークスペースオープン時のエディタ復元 | — | GA |
| `workbench.settings.showAdvancedSettings` | 高度な設定の常時表示 | — | GA |
| `git.worktreeIncludeFiles` | Git worktree に追加コピーするファイル | — | Experimental |
| `git.blame.editorDecoration.hoverEnabled` | Blame デコレーションのホバー有効化 | `true` | GA |
| `task.allowAutomaticTasks` | 自動タスクの許可 | `off` | GA |

## Breaking Changes / 非推奨化

1. **winpty サポートの廃止** — Windows 10 version 1809 より前のバージョンではターミナルが動作しなくなる。ConPTY への移行が必要。対処法: Windows 10 の新しいバージョンまたは Windows 11 へアップグレード。
2. **自動タスクのデフォルト無効化** — `task.allowAutomaticTasks` のデフォルトが `off` に変更。影響: ワークスペースオープン時の自動タスクが実行されなくなる。対処法: ユーザー設定で `on` に変更。
3. **Copilot 拡張機能の廃止** — GitHub Copilot 拡張機能が廃止され、GitHub Copilot Chat 拡張機能に統合。影響: VS Code アップデート時に自動アンインストール。対処法: Copilot Chat 拡張機能が自動的にすべての機能を提供するため、追加の操作は不要。

## まとめと所感

VS Code 1.109 はエージェント中心のワークフローを大幅に強化するリリースである。特に Agent Skills の GA 化、Claude Agent のプレビュー導入、エージェントオーケストレーションパターンの確立は、VS Code を単なるエディタからマルチエージェント開発プラットフォームへと進化させる重要なステップとなっている。実務面では、ターミナルサンドボックスとメモリ機能がエージェント利用の安全性とパーソナライゼーションを向上させ、統合ブラウザが Web 開発ワークフローのコンテキストスイッチを削減する。エンジニアリング面でも Windows インストールの信頼性改善や macOS DMG サポートなど、基盤品質が着実に向上している。
