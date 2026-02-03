---
title: "Copilot coding agent タスクを割り当て・誘導・追跡するためのミッションコントロール"
date: "2025-10-28"
type: "new releases"
labels: ["copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-a-mission-control-to-assign-steer-and-track-copilot-coding-agent-tasks"
fetched_at: "2026-02-03T14:50:55.529023Z"
lang: "ja"
---

# Copilot coding agent タスクを割り当て・誘導・追跡するためのミッションコントロール

## Overview
github.com での Copilot coding agent タスク管理の方法を再設計しました。進捗の追跡、変更の監視、タスク管理のためにページ間を行き来する代わりに、必要なものがすべて 1 つの整理された中央ビューに集約されます。

## Detailed Explanation
### Overview
- github.com での Copilot coding agent タスク管理の方法を再設計しました。進捗の追跡、変更の監視、タスク管理のためにページ間を行き来する代わりに、必要なものがすべて 1 つの整理された中央ビューに集約されます。
- Copilot のアクティビティを 1 つの画面で俯瞰できます。Overview と Files changed タブのすぐ隣にセッションログを表示できるため、ページを離れずに関連情報を確認できます。Copilot のコミットの根拠（rationale）も、コンテキストの中でリアルタイムに把握できます。

### Real-time steering
- Copilot の応答性がこれまで以上に向上しました。リアルタイムステアリングにより、Copilot が作業中でもガイドできます。セッション実行中に入力を与えると、現在のツール呼び出しが完了し次第、Copilot はそれに合わせて適応します。フィードバックも簡単になり、@copilot を付けてプルリクエストコメントへ飛ぶ必要はありません。チャット入力から誘導するか、Files changed ビューに直接コメントを追加するだけです。

### Centralizing your task management
- 新しいタスクビューで、タスク間の切り替えがスムーズになります。タスクの状態をひと目で確認でき、Copilot が入力を必要としたタイミングですぐに参加できます。タスク上のクイックリンクから、プルリクエストへ直接移動できます。

### More creation flexibility
- agents パネルや github.com/copilot/agents にある既存の選択肢に加えて、github.com 上で直接 Copilot coding agent タスクを作成できるようになりました。github.com/copilot では（チャットで /task を入力して）作成でき、GitHub Mobile の agents タスクページからも作成できます。どこからタスクを開始しても、カスタムエージェントを選んで Copilot の出力をさらにカスタマイズできます。

### Continue where you prefer working
- Copilot の作業をベースに進めたい場合でも、完全に自分でコントロールしたい場合でも、Codespaces、VS Code Insiders、または GitHub CLI でセッションを開けます。
- この機能は、Copilot coding agent にアクセスできるすべてのユーザーが利用できます。Copilot と共同作業するには、リポジトリへの書き込み権限が必要です。VSCode Insiders でセッションにアクセスするには、GitHub Copilot Chat および GitHub Pull Requests 拡張機能とあわせて、最新バージョンの VScode Insiders がインストールされていることを確認してください。
- GitHub Community でのディスカッションに参加してください。

## Article Content (cleaned)
github.com での [Copilot coding agent](https://github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/) タスク管理の方法を再設計しました。進捗の追跡、変更の監視、タスク管理のためにページ間を行き来する代わりに、必要なものがすべて 1 つの整理された中央ビューに集約されます。


Copilot のアクティビティを 1 つの画面で俯瞰できます。**Overview** と **Files changed** タブのすぐ隣にセッションログを表示できるため、ページを離れずに関連情報を確認できます。Copilot のコミットの根拠（rationale）も、コンテキストの中でリアルタイムに把握できます。


## [Real\-time steering](#real-time-steering)


Copilot の応答性がこれまで以上に向上しました。リアルタイムステアリングにより、Copilot が作業中でもガイドできます。セッション実行中に入力を与えると、現在のツール呼び出しが完了し次第、Copilot はそれに合わせて適応します。フィードバックも簡単になり、プルリクエストコメントへ飛んで @copilot する必要はありません。チャット入力から誘導するか、**Files changed** ビューに直接コメントを追加するだけです。


  



## [Centralizing your task management](#centralizing-your-task-management)


新しいタスクビューで、タスク間の切り替えがスムーズになります。タスクの状態をひと目で確認でき、Copilot が入力を必要としたタイミングですぐに参加できます。タスク上のクイックリンクから、プルリクエストへ直接移動できます。


![Agent sessions in one view](https://github.com/user-attachments/assets/1dffaa3b-ff6f-4c6e-a8aa-964841ea6725)


## [More creation flexibility](#more-creation-flexibility)


[agents パネル](https://github.blog/changelog/2025-08-19-agents-panel-launch-copilot-coding-agent-tasks-anywhere-on-github-com/) や github.com/copilot/agents にある既存の選択肢に加えて、github.com 上で直接 [Copilot coding agent タスクを作成](https://github.blog/changelog/2025-11-20-updated-copilot-input-on-the-home-dashboard/)できるようになりました。github.com/copilot では（チャットで `/task` を入力して）作成でき、GitHub Mobile の agents タスクページからも作成できます。どこからタスクを開始しても、[カスタムエージェント](https://github.blog/changelog/2025-11-27-custom-agents-for-github-copilot/) を選んで Copilot の出力をさらにカスタマイズできます。


  



## [Continue where you prefer working](#continue-where-you-prefer-working)


Copilot の作業をベースに進めたい場合でも、完全に自分でコントロールしたい場合でも、Codespaces、VS Code Insiders、または GitHub CLI でセッションを開けます。


  



この機能は、Copilot coding agent にアクセスできるすべてのユーザーが利用できます。Copilot と共同作業するには、リポジトリへの書き込み権限が必要です。VSCode Insiders でセッションにアクセスするには、GitHub Copilot Chat および GitHub Pull Requests 拡張機能とあわせて、最新バージョンの VScode Insiders がインストールされていることを確認してください。


[GitHub Community](https://github.com/orgs/community/discussions/177791?utm_source=changelog-community-mission-control&utm_medium=changelog&utm_campaign=universe25) でのディスカッションに参加してください。
