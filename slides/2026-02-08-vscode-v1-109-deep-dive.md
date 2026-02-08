---
marp: true
theme: github-dark
paginate: true
header: "VS Code v1.109 Deep Dive"
footer: "January 2026 Release — February 8, 2026"
---

# VS Code v1.109 Deep Dive
## January 2026 Release — AI & Agent 徹底解説

マルチエージェント開発の新時代へ

---

# Table of Contents

1. **Chat UX** — より速く、よりスマートに
2. **Agent Session Management** — マルチエージェント統合管理
3. **Agent Customization** — AI をチームに最適化
4. **Agent Extensibility** — Claude Agent & MCP Apps
5. **Agent Optimizations** — Copilot Memory & 高速検索
6. **Agent Security & Trust** — サンドボックスと安全性
7. **Azure 連携** — モデル構成と MCP
8. **Workbench & Editor** — 統合ブラウザほか

---

<!-- Section: Chat UX -->

# Chat UX
## より速く、よりスマートに

---

# Anthropic モデルの Thinking Tokens
## Chat UX

- Claude モデルが **thinking tokens** に対応 — モデルの推論過程を可視化
- 詳細 or コンパクトな表示スタイルを選択可能
- ツール呼び出しの間にモデルの思考プロセスが表示される
- 失敗したツール呼び出しは自動展開で詳細表示
- スクロール可能な思考コンテンツとシマーアニメーション

---

# Mermaid ダイアグラム in Chat
## Chat UX

- チャット応答内で **Mermaid ダイアグラム**をインタラクティブに描画
- `renderMermaidDiagram` ツールを使用
- フローチャート、シーケンス図などで複雑な概念を視覚化
- Alt/Option + マウスホイールでズーム、ドラッグでパン
- エディタで全画面表示可能、ソースコードのコピーも対応

---

# Ask Questions ツール (Experimental)
## Chat UX

- エージェントが不明点を**質問で確認**するツール
- 単一選択/複数選択/自由入力に対応
- 推奨回答がハイライト表示され素早い意思決定が可能
- キーボード操作: 上下キーで選択、数字キーで直接回答
- **Plan エージェント**もこのツールを活用して実装計画の精度を向上

---

# Plan エージェントの進化
## Chat UX

- `/plan` コマンドでタスクの実装計画を構造化
- **4 フェーズのイテレーティブワークフロー**:
  1. **Discovery** — コードベースを自律的に探索
  2. **Alignment** — 曖昧さを質問で解消
  3. **Design** — ファイル位置・コード込みの詳細プランを作成
  4. **Refinement** — 検証基準を追加、決定事項を文書化

---

# コンテキストウィンドウの可視化
## Chat UX

- チャット入力エリアに**コンテキストウィンドウインジケータ**を追加
- ホバーでカテゴリ別のトークン使用量の内訳を表示
- モデルがコンテキストをどう使っているか一目で把握
- コンテキスト窓の圧迫状況をリアルタイムに確認可能

---

# インライン Chat UX の刷新 (Preview)
## Chat UX

- テキスト選択時にインラインチャットを起動しやすくする新しいアフォーダンス
- 軽量でコンテキストに沿ったレンダリングモード
- エディタ内での対話がより自然に
- `inlineChat.affordance` / `inlineChat.renderMode` で設定

---

# ターミナルコマンド出力の強化
## Chat UX

- **構文ハイライト**: Node, Python, Ruby のインラインコードを色分け表示
- **作業ディレクトリ**: コマンド実行先のフォルダを明示
- **コマンドの意図**: ホバーで「なぜ」実行するかの説明を表示
- **出力ストリーミング**: 長時間コマンドは自動展開
- **インタラクティブ入力**: 埋め込みターミナルに直接入力可能

---

<!-- Section: Agent Session Management -->

# Agent Session Management
## マルチエージェント統合管理

---

# エージェントセッションの種類と切り替え
## Agent Session Management

- **Local** — VS Code 内でインタラクティブに実行
- **Background** — ローカルでバックグラウンド実行
- **Cloud** — GitHub 上で自律的に実行
- **Partner Agents** — Claude, Codex 等の外部エージェント
- セッションタイプピッカーでワンクリック切り替え
- 進行中のセッションを別の環境に**ハンドオフ**可能

---

# Agent Sessions ビューの強化
## Agent Session Management

- サイドバイサイド表示でセッションリストをリサイズ可能
- **複数選択**で一括操作
- スタックビューの改善でフィルタ・ナビゲーション向上
- **Agent Status Indicator**: コマンドセンターで注意が必要なセッションを即座に把握
- チャットボタンの動作をカスタマイズ可能（サイドバー/最大化/非表示を切替）

---

# サブエージェントの並列実行
## Agent Session Management

- サブエージェントが**並列実行**に対応
- 独立したタスクの同時処理でワークフローを高速化
- 各サブエージェントは独自のコンテキストウィンドウで動作
- メインエージェントのコンテキストを消費しない
- タスク内容、使用ツール、カスタムエージェント名が表示される

---

# Search サブエージェント (Experimental)
## Agent Session Management

- コードベース検索を**分離されたエージェントループ**で実行
- 複数クエリの反復的精緻化が可能
- メインエージェントのコンテキストウィンドウを保全
- メインエージェントは検索中も別作業を継続
- `github.copilot.chat.searchSubagent.enabled` で有効化

---

# Cloud Agent の新機能
## Agent Session Management

- **モデル選択**: クラウドエージェントセッションのモデルを選べる
- **カスタムエージェント**: リポジトリのデフォルトブランチからカスタムエージェントを使用
- **パートナーエージェント**: Claude, Codex 等を選択可能
- **マルチルートワークスペース対応**: フォルダを選んでクラウドエージェントに指定
- **Checkout**: GitHub Pull Requests 拡張が未インストールでも自動インストール

---

# Background Agent の強化
## Agent Session Management

- カスタムエージェントのサポート追加
- **画像をコンテキストとして添付**可能
- マルチルートワークスペース対応
- 各ターンの最後に Git ワークツリーに**自動コミット**
- Keep/Undo アクションを廃止し、ワーキングセットの表示を簡素化

---

<!-- Section: Agent Customization -->

# Agent Customization
## AI をチームに最適化

---

# `/init` でワークスペースを AI 対応に
## Agent Customization

- `/init` コマンドで AI 指示ファイルを自動生成
- 既存の `copilot-instructions.md` や `AGENTS.md` を検出
- プロジェクト構造・コーディングパターンを分析
- ワークスペースに最適化された包括的な指示を生成
- プロンプトファイルとして実装されているためカスタマイズ可能

---

# Agent Skills が GA に
## Agent Customization

- **Agent Skills が正式リリース**（デフォルト有効）
- テスト戦略、API 設計、パフォーマンス最適化などの専門知識をパッケージ化
- **Chat: Configure Skills** / **Chat: New Skill File** コマンドで管理
- `.github/skills` / `.claude/skills` / `~/.copilot/skills` から検索
- 拡張機能から `chatSkills` コントリビューションポイントでスキルを配布可能

---

# Organization-wide Instructions
## Agent Customization

- **組織レベルのカスタム指示**を自動適用
- GitHub 組織で設定された Copilot カスタム指示がチャットに反映
- チーム全体で一貫したガイダンスを実現
- デフォルトで有効、個別に無効化可能
- 以前リリースされた組織レベルカスタムエージェントと連携

---

# カスタムエージェントの呼び出し制御
## Agent Customization

- `user-invokable: false` — ドロップダウンに表示せずサブエージェント専用に
- `disable-model-invocation` — 他のエージェントからの自動呼び出しを防止
- `agents:` — 使用可能なサブエージェントのリストを制限
- **複数モデル指定**: フォールバックオプションとして複数モデルを設定可能

```markdown
---
name: Foo
tools: ['agent']
agents: ['Modify', 'Search']
model: ['Claude Sonnet 4.5 (copilot)', 'GPT-5 (copilot)']
---
```

---

# Agent Orchestration パターン
## Agent Customization

- 複数の専門エージェントが**協調して目標を達成**するパターン
- メリット:
  - **コンテキスト効率**: 各サブエージェントが専用のコンテキストウィンドウ
  - **専門化**: タスクに最適化されたモデルを使い分け
  - **並列実行**: 独立タスクを同時処理
- コミュニティの実装例:
  - **Copilot Orchestra** — Conductor が計画・実装・レビューを統合
  - **GitHub Copilot Atlas** — Prometheus, Oracle, Sisyphus 等の専門エージェント

---

<!-- Section: Agent Extensibility -->

# Agent Extensibility
## Claude Agent & MCP Apps

---

# Claude Agent (Preview)
## Agent Extensibility

- **Anthropic の Claude Agent SDK** を VS Code 内で直接利用
- GitHub Copilot サブスクリプション内の Claude モデルで動作
- Anthropic の公式エージェントハーネスと**同じプロンプト・ツール・アーキテクチャ**
- セッションタイプピッカーで Local / Background / Cloud と並んで選択
- 活発に開発中 — 今後さらに機能追加予定

---

# Anthropic モデルの強化
## Agent Extensibility

- **Messages API + Interleaved Thinking**: ツール呼び出し間でモデルが推論
- Thinking budget をトークン数で設定（0 で無効化）
- **Tool Search Tool**: 大量のツールから最適なものを自動選択
- **Context Editing (Experimental)**: 前のターンのツール結果と思考を削除
  - 要約を遅延させ、より多くのコンテキストを維持
  - `github.copilot.chat.anthropic.contextEditing.enabled` で有効化

---

# MCP Apps サポート
## Agent Extensibility

- **MCP Apps**: MCP サーバーがクライアント内にリッチな UI を表示
- インタラクティブなビジュアライゼーション（フレームグラフ等）を直接描画
- サーバーがアプリを返すと自動表示
- **カスタムレジストリ対応**: `registryBaseUrl` プロパティで
  プライベートレジストリ（Azure DevOps フィード、カスタム PyPI リポジトリ等）を指定可能

---

<!-- Section: Agent Optimizations -->

# Agent Optimizations
## Copilot Memory & 高速検索

---

# Copilot Memory (Preview)
## Agent Optimizations

- **セッション間で重要な情報を記憶**するメモリ機能
- チャットから直接 Copilot Memory にアクセス・更新
- 「疑問がある場合は必ず確認質問する」などのルールを保存
- エージェントが自動的にメモリの保存/取得タイミングを判断
- GitHub の Copilot 設定からメモリを表示・管理
- `github.copilot.chat.copilotMemory.enabled` で有効化

---

# External Indexing (Preview)
## Agent Optimizations

- **GitHub 以外のワークスペースでもリモートインデックスが利用可能**
- `#codebase` 使用時にインデックスを構築してセマンティック検索
- 初回はリポジトリサイズとネットワーク速度に依存（数分かかる場合あり）
- 以降はキャッシュされたインデックスで高速検索
- ファイルの保存時にインデックスが自動更新
- 段階的にロールアウト中

---

# ワークスペース外ファイルの読み取り
## Agent Optimizations

- エージェントが**ワークスペース外のファイル・ディレクトリ**も読み取り可能に
- 以前は自動的に拒否されていたアクセスを許可/拒否のプロンプトで制御
- セッション全体で同一フォルダへのアクセスを一括許可可能
- 関連する設定ファイルやライブラリの参照に便利

---

# パフォーマンス改善
## Agent Optimizations

- **大規模チャット**: 長い会話のスクロールと表示が高速化
- 会話の永続化を最適化し信頼性を向上
- **並列依存タスク**: ビルドタスクの並列処理で大幅な高速化
- 独立したビルドステップを持つプロジェクトで顕著な改善

---

<!-- Section: Agent Security & Trust -->

# Agent Security & Trust
## サンドボックスと安全性

---

# Terminal Sandboxing (Experimental)
## Agent Security & Trust

- エージェントが実行するターミナルコマンドの**ファイルシステムアクセスを制限**
- ワークスペースフォルダのみ読み書き可能
- **ネットワークアクセス**をドメイン単位で制御可能
- サンドボックス有効時は確認ダイアログなしで実行
- macOS / Linux のみ対応（Windows は未対応）
- `chat.tools.terminal.sandbox.enabled` で有効化

---

# ターミナルツールのライフサイクル改善
## Agent Security & Trust

- コマンドを**手動でバックグラウンドに移行**可能
- `timeout` プロパティで予期せぬ状態からの自動復帰
- `awaitTerminal` ツール: バックグラウンドターミナルの完了を待機
- `killTerminal` ツール: 不要なバックグラウンドターミナルのクリーンアップ
- `echo "successful"` や `sleep n` のハック的手法を解消

---

# ターミナル自動承認の拡張
## Agent Security & Trust

- 以下のコマンドがデフォルトで**自動承認**に追加:
  - `Set-Location`, `dir`, `od`, `xxd`
  - `docker` — 安全なサブコマンド全般
  - `npm`, `yarn`, `pnpm` — 安全なサブコマンド全般
- `chat.tools.terminal.enableAutoApprove` で有効化

---

<!-- Section: Azure -->

# Azure 連携
## モデル構成と MCP

---

# Azure モデルの構成
## Azure 連携

- **Language Models エディタ**で Azure モデルをネイティブに構成
- `chatLanguageModels.json` にスニペットテンプレートを挿入
- モデル ID、名前、エンドポイント URL、トークン上限などを設定
- 複数プロバイダ構成: 個人キーとチームキーを分けて管理可能
- 既存の GitHub Copilot Chat 設定は自動移行

---

# Language Models エディタの新機能
## Azure 連携

- **同一プロバイダで複数構成**: 異なる API キーで複数グループを作成
- プロバイダグループの管理: 設定変更・削除が可能に
- キーボードアクセス、コンテキストメニュー、複数選択に対応
- モデル構成ファイルを直接編集・共有可能
- **Provider Configuration API (Proposed)**: 拡張機能がスキーマを宣言し
  VS Code が構成 UI を自動提供

---

# カスタムレジストリ対応 (MCP)
## Azure 連携

- MCP サーバーマニフェストの `registryBaseUrl` プロパティをサポート
- **Azure DevOps フィード**やカスタム PyPI リポジトリからMCP サーバーをデプロイ
- 組織のプライベートレジストリを利用した MCP サーバー管理が可能
- エンタープライズ環境でのセキュアなエージェント拡張を実現

---

<!-- Section: Workbench -->

# Workbench & Editor
## 統合ブラウザと開発体験の向上

---

# 統合ブラウザ (Preview)
## Workbench

- iframe の制限を克服した**本格的なブラウザ**を VS Code に内蔵
- ウェブサイトへの**ログインが可能** (Google, GitHub, Stack Overflow 等)
- 永続データストレージ（グローバル/ワークスペース/エフェメラル）
- **DevTools 搭載**: 開発者ツールをフル機能で利用
- 要素を選択してチャットエージェントに送信可能
- `Browser: Open Integrated Browser` コマンドで起動

---

# エディタの改善
## Coding & Editor

- **ダブルクリックで括弧/文字列の中身を選択**: 開始括弧の直後、あるいは
  閉じ引用符の直前でダブルクリック
- **ブラケットマッチングの文字色**: `editorBracketMatch.foreground` で設定
- **Ghost Text の視認性向上**: 短い候補に点線アンダーライン
- **スニペットのファイルパターン**: `include`/`exclude` で表示対象を限定
- **Shebang 検出の改善**: `#!/usr/bin/env -S deno -A` を TypeScript と正しく認識

---

# その他の注目ポイント
## Engineering & Enterprise

- **macOS DMG インストーラー**: ドラッグ&ドロップでインストール
- **Windows 11 コンテキストメニュー統合**: トップレベルに VS Code を表示
- **Copilot 拡張機能の廃止**: Copilot Chat 拡張に統合完了
- **組織ポリシーの信頼性向上**: オフライン起動時もポリシーを適用
- **Kitty keyboard protocol**: ターミナル体験の向上

---

# Key Takeaways

- VS Code が**マルチエージェント開発の統合プラットフォーム**へ進化
- **Claude Agent (Preview)** でAnthropicのエージェントSDKをネイティブ統合
- **Agent Orchestration** パターンで複雑なワークフローを構築可能
- **Copilot Memory** でセッション間のコンテキストを維持
- **Terminal Sandboxing** でエージェントの安全な実行を実現
- **Azure モデル構成** と **MCP カスタムレジストリ** でエンタープライズ対応強化

---

# Key Takeaways (続き)

- **Agent Skills GA** と組織レベル指示でチーム全体のAI品質を統一
- **サブエージェント並列実行** と **External Indexing** で大幅な高速化
- **統合ブラウザ** で開発・テスト・デバッグを VS Code 内で完結
- **Plan エージェント** の 4 フェーズワークフローでAI の計画品質が飛躍的に向上
- **MCP Apps** が MCP サーバーにリッチ UI 描画の道を開く

---

# Thank You

Source: [VS Code January 2026 Release Notes](https://code.visualstudio.com/updates/v1_109)
