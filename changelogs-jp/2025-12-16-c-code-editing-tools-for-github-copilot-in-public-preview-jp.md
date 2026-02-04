---
title: "GitHub CopilotのC++コード編集ツールがパブリックプレビュー"
date: "2025-12-16"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-16-c-code-editing-tools-for-github-copilot-in-public-preview"
fetched_at: "2026-02-03T14:50:54.900039Z"
lang: "ja"
---

# GitHub CopilotのC++コード編集ツールがパブリックプレビュー

## Overview
GitHub CopilotのC++コード編集ツールが、最新のVisual Studio 2026 Insidersリリースでパブリックプレビューになりました。これらのツールは、信頼性の高いマルチファイル編集サポートのための深いシンボル認識を提供することで、Copilotが大規模にC++コードを理解および変更する能力を拡張します。

## Detailed Explanation
### Overview
- GitHub CopilotのC++コード編集ツールが、最新のVisual Studio 2026 Insidersリリースでパブリックプレビューになりました。これらのツールは、信頼性の高いマルチファイル編集サポートのための深いシンボル認識を提供することで、Copilotが大規模にC++コードを理解および変更する能力を拡張します。
- C++コード編集ツールは、プロジェクト内のシンボルに対して豊富なセマンティックデータを提供し、Copilotエージェントモードが次のことを可能にします：
- コードベース全体のすべての参照を表示します。
- シンボルの型、宣言、スコープ、その他のメタデータを理解します。
- クラス継承階層を視覚化します。
- 関数呼び出しチェーンを追跡します。

### 始め方
- Visual Studio 2026 InsidersでC++プロジェクトを開きます。
- **Tools** > **Options**、**GitHub** > **Copilot**に移動し、C++コード編集ツールを有効にします a. 有効にした後、ソリューションを閉じて再度開く必要がある場合があります
- Copilot Chatを開き、**Tools**アイコンを使用して特定のC++ツールを有効にします。
- GitHub Copilotは、これらのツールを呼び出して、より正確でコンテキストを認識したコード提案を提供し、コーディング体験をよりスムーズで効率的にします。たとえば、これらのツールは、新しい機能を追加したり、パラメーターを更新したりする場合に、関数のすべてのインスタンス全体で更新を行うのに役立ちます。
- 最良の結果を得るには、ツール呼び出しに最適化されたモデルを使用し、可能な場合は明示的なシンボルを含む明確で具体的なプロンプトを提供してください。

### フィードバックをお聞かせください
- フィードバックを送信するには、Visual Studioのフィードバックアイコンから問題を報告するか、改善を提案してください。

## Impact / Who’s Affected
- GitHub CopilotのC++コード編集ツールが、最新のVisual Studio 2026 Insidersリリースでパブリックプレビューになりました。

## Article Content (cleaned)
GitHub CopilotのC\+\+コード編集ツールが、最新のVisual Studio 2026 Insidersリリースでパブリックプレビューになりました。これらのツールは、信頼性の高いマルチ\-ファイル編集サポートのための深いシンボル認識を提供することで、Copilotが大規模にC\+\+コードを理解および変更する能力を拡張します。


C\+\+コード編集ツールは、プロジェクト内のシンボルに対して豊富なセマンティックデータを提供し、Copilotエージェントモードが次のことを可能にします：


* コードベース全体のすべての参照を表示します。
* シンボルの型、宣言、スコープ、その他のメタデータを理解します。
* クラス継承階層を視覚化します。
* 関数呼び出しチェーンを追跡します。


## [How to get started](#how-to-get-started)


1. Visual Studio 2026 InsidersでC\+\+プロジェクトを開きます。
2. **Tools** \> **Options**、**GitHub** \> **Copilot**に移動し、C\+\+コード編集ツールを有効にします  

a. 有効にした後、ソリューションを閉じて再度開く必要がある場合があります
3. Copilot Chatを開き、**Tools**アイコンを使用して特定のC\+\+ツールを有効にします。


![Visual Studioのエージェントモードで、GitHub Copilotが呼び出すことができるC++コード編集ツール（get_Symbol_references、get_symbol_info、その他のC++言語サービス操作を含む）](https://github.com/user-attachments/assets/19c78848-466f-4bac-be64-08347ef1eb68)


GitHub Copilotは、これらのツールを呼び出して、より正確でコンテキストを認識したコード提案を提供し、コーディング体験をよりスムーズで効率的にします。たとえば、これらのツールは、新しい機能を追加したり、パラメーターを更新したりする場合に、関数のすべてのインスタンス全体で更新を行うのに役立ちます。


![関連するシンボル情報と参照を取得することでプロンプトを支援するC++コード編集ツールの例](https://github.com/user-attachments/assets/3b98c50c-38a6-4d35-88de-15c394cb1c1c)


最良の結果を得るには、ツール呼び出しに最適化されたモデルを使用し、可能な場合は明示的なシンボルを含む明確で具体的なプロンプトを提供してください。


## [Tell us your feedback](#tell-us-your-feedback)


フィードバックを送信するには、Visual Studioのフィードバックアイコンから問題を報告するか、改善を提案してください。


![バグレポートと提案を送信するオプションを示すプルダウンメニュー付きのVisual Studioフィードバックアイコン](https://github.com/user-attachments/assets/b9738f4b-7bfd-47a6-8c0d-9b8e911f847d)
