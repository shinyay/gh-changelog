---
title: "Copilot コードレビューとコーディングエージェントがエージェント固有の指示をサポート"
date: "2025-11-12"
type: "improvements"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-12-copilot-code-review-and-coding-agent-now-support-agent-specific-instructions"
fetched_at: "2026-02-03T14:50:55.315997Z"
lang: "ja"
---

# Copilot コードレビューとコーディングエージェントがエージェント固有の指示をサポート

## Overview
Copilot コードレビューと Copilot コーディングエージェント向けに、ターゲットを絞ったカスタム指示を作成できるようになりました。.instructions.md カスタム指示の新しい excludeAgent プロパティにより、特定の指示が適用されるタイミングを正確に制御できます。

## Detailed Explanation
### 概要
- Copilot コードレビューと Copilot コーディングエージェント向けに、ターゲットを絞ったカスタム指示を作成できるようになりました。.instructions.md カスタム指示の新しい excludeAgent プロパティにより、特定の指示が適用されるタイミングを正確に制御できます。

### 🎯 おさらい: instructions.md ファイルを使用した Copilot のカスタマイズ
- .github/instructions ディレクトリにあるカスタム指示ファイルを使用して、リポジトリの特定の領域に対する Copilot の動作をガイドできます。
- applyTo プロパティを使用すると、パスグロブでパスやディレクトリを指定できるため、指示を希望する場所にのみ適用できます。たとえば、 applyTo: "app/models/**/*.rb" を指定することで、モデルにのみ適用される models.instructions.md ファイルを作成できます。

### 🛡️ excludeAgent を使用したエージェント固有のリポジトリ指示の導入
- 新しい excludeAgent プロパティにより、特定の指示ファイルを使用する Copilot エージェントを制御できます:
- excludeAgent: "code-review" を設定すると、Copilot コードレビューから指示ファイルを非表示にします。
- excludeAgent: "coding-agent" を設定すると、Copilot コーディングエージェントから指示ファイルを非表示にします。
- フロントマターに excludeAgent プロパティがない場合、指示ファイルはすべてのエージェントによって使用されます。
- この機能により、各エージェントに合わせてガイダンスをカスタマイズし、重複を減らし、焦点を絞った具体的な指示を提供できます。

### 🛠️ その他のカスタム指示の改善
- Copilot コードレビューは最近、特定の *.instructions.md ファイルの読み取りを妨げていたバグを修正しました。
- 効果的な指示ファイルの書き方のヒントについては、このブログ記事をご覧ください！
- 指示ファイルの作成の詳細については、Copilot 指示ドキュメントを参照してください。
- GitHub Community 内でディスカッションに参加してください。

## Key Changes
- Copilot コードレビューは最近、特定の *.instructions.md ファイルの読み取りを妨げていたバグを修正しました。
- 効果的な指示ファイルの書き方のヒントについては、このブログ記事をご覧ください！
- 指示ファイルの作成の詳細については、Copilot 指示ドキュメントを参照してください。
- GitHub Community 内でディスカッションに参加してください。

## Impact / Who's Affected
- たとえば、 applyTo: "app/models/**/*.rb" を指定することで、モデルにのみ適用される models.instructions.md ファイルを作成できます。🛡️ excludeAgent を使用したエージェント固有のリポジトリ指示の導入 新しい excludeAgent プロパティにより、特定の指示ファイルを使用する Copilot エージェントを制御できます: excludeAgent: "code-review" を設定すると、Copilot コードレビューから指示ファイルを非表示にします。

## Caveats / Limitations
- たとえば、 applyTo: "app/models/**/*.rb" を指定することで、モデルにのみ適用される models.instructions.md ファイルを作成できます。🛡️ excludeAgent を使用したエージェント固有のリポジトリ指示の導入 新しい excludeAgent プロパティにより、特定の指示ファイルを使用する Copilot エージェントを制御できます: excludeAgent: "code-review" を設定すると、Copilot コードレビューから指示ファイルを非表示にします。

## Article Content (cleaned)
Copilot コードレビューと Copilot コーディングエージェント向けに、ターゲットを絞ったカスタム指示を作成できるようになりました。`.instructions.md` カスタム指示の新しい `excludeAgent` プロパティにより、特定の指示が適用されるタイミングを正確に制御できます。


### [🎯 おさらい: `instructions.md` ファイルを使用した Copilot のカスタマイズ](#%f0%9f%8e%af-recap-customizing-copilot-using-instructions-md-files)


`.github/instructions` ディレクトリにあるカスタム指示ファイルを使用して、リポジトリの特定の領域に対する Copilot の動作をガイドできます。


`applyTo` プロパティを使用すると、パスグロブでパスやディレクトリを指定できるため、指示を希望する場所にのみ適用できます。たとえば、`applyTo: "app/models/**/*.rb"` を指定することで、モデルにのみ適用される `models.instructions.md` ファイルを作成できます。


### [🛡️ `excludeAgent` を使用したエージェント固有のリポジトリ指示の導入](#%f0%9f%9b%a1%ef%b8%8f-introducing-agent-specific-repository-instructions-with-excludeagent)


新しい `excludeAgent` プロパティにより、特定の指示ファイルを使用する Copilot エージェントを制御できます:


* `excludeAgent: "code-review"` を設定すると、Copilot コードレビューから指示ファイルを非表示にします。
* `excludeAgent: "coding-agent"` を設定すると、Copilot コーディングエージェントから指示ファイルを非表示にします。


フロントマターに `excludeAgent` プロパティがない場合、指示ファイルはすべてのエージェントによって使用されます。


この機能により、各エージェントに合わせてガイダンスをカスタマイズし、重複を減らし、焦点を絞った具体的な指示を提供できます。


![エージェント固有の指示を .instructions.md ファイルで指定する方法を示すスクリーンショット。](https://github.com/user-attachments/assets/2abfcfb4-3c6a-422b-8a02-02c923c46ae7)


### [🛠️ その他のカスタム指示の改善](#%f0%9f%9b%a0%ef%b8%8f-other-custom-instructions-improvements)


Copilot コードレビューは最近、特定の `*.instructions.md` ファイルの読み取りを妨げていたバグを修正しました。


効果的な指示ファイルの書き方のヒントについては、[このブログ記事](https://github.blog/ai-and-ml/unlocking-the-full-power-of-copilot-code-review-master-your-instructions-files)をご覧ください！




---


指示ファイルの作成の詳細については、[Copilot 指示ドキュメント](https://docs.github.com/copilot/how-tos/configure-custom-instructions/add-repository-instructions#creating-a-repository-custom-instructions-file)を参照してください。


[GitHub Community](https://github.com/orgs/community/discussions/categories/copilot-conversations) 内でディスカッションに参加してください。
