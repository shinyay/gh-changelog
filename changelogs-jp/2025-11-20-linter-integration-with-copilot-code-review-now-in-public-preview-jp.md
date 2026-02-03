---
title: "Copilotコードレビューとのリンター統合がパブリックプレビューになりました"
date: "2025-11-20"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-20-linter-integration-with-copilot-code-review-now-in-public-preview"
fetched_at: "2026-02-03T14:50:55.164057Z"
lang: "ja"
---

# Copilotコードレビューとのリンター統合がパブリックプレビューになりました

## Overview
Copilotコードレビューは、リンターからの実用的なフィードバックを表示するようになり、小さなことも見逃されないようになりました。また、リポジトリルールセットを介して使用するリンターをカスタマイズできます。この機能は、有料GitHubユーザー向けにパブリックプレビューで利用可能です。

## Detailed Explanation
### Overview
- Copilotコードレビューは、リンターからの実用的なフィードバックを表示するようになり、小さなことも見逃されないようになりました。また、リポジトリルールセットを介して使用するリンターをカスタマイズできます。この機能は、有料GitHubユーザー向けにパブリックプレビューで利用可能です。

### New static analysis tools in Copilot code review
- GitHub Universe 2025で有効化されたCodeQL品質検出に加えて、Copilotコードレビューで以下の静的解析ツールから結果を取得できるようになりました：
- ESLintは、JavaScriptおよびTypeScriptプロジェクトの問題を強調表示します。
- PMDは、Java、Apex、およびその他のサポートされている言語の問題をスキャンします。

### Configure which tools are used with a repository rule
- パブリックプレビュー参加者にはCodeQLがデフォルトで有効になっていますが、Copilotコードレビューで使用するツールを制御できるようになりました。新しいリポジトリルール「Copilotコードレビューで静的解析ツールを管理」が追加され、CodeQL、ESLint、PMDのオン/オフを切り替えることができます。このルールを使用すると、Enterprise、Organization、Team、またはRepositoryレベルでこれらの機能を有効にし、特定のブランチとリポジトリをターゲットにすることができます。
- リポジトリルールセットページを開き、新しいルールでルールセットを作成するデモ
- 管理者アクセス権を持つリポジトリで、Settings > Rules > Rulesetsに移動します。
- ルールセットを追加または編集し、新しい「Copilotコードレビューで静的解析ツールを管理」ルールを選択します。
- Copilotコードレビューに含めたい静的解析ツールを選択します：ESLint、PMD、および/またはCodeQL。CodeQLはデフォルトで有効になっており、ルールを介して無効にできるようになりました。
- ルールを保存し、新しいプルリクエストを開いて、新しいリンター設定でCopilotコードレビューが実行されることを確認します。
- Copilotコードレビューのリポジトリルールの構成について詳しく学びましょう。
- GitHub Communityのディスカッションに参加してください。

## Impact / Who’s Affected
- この機能は、有料GitHubユーザー向けにパブリックプレビューで利用可能です。
- リポジトリルールで使用するツールを構成 パブリックプレビュー参加者にはCodeQLがデフォルトで有効になっていますが、Copilotコードレビューで使用するツールを制御できるようになりました。

## Caveats / Limitations
- CodeQLはデフォルトで有効になっており、ルールを介して無効にできるようになりました。

## Insights (derived from article language)
- CodeQLはデフォルトで有効になっており、ルールを介して無効にできるようになりました。
- Copilotコードレビューのリポジトリルールの構成について詳しく学びましょう。

## Article Content (cleaned)
Copilotコードレビューは、リンターからの実用的なフィードバックを表示するようになり、小さなことも見逃されないようになりました。また、リポジトリルールセットを介して使用するリンターをカスタマイズできます。この機能は、有料GitHubユーザー向けにパブリックプレビューで利用可能です。


### [New static analysis tools in Copilot code review](#new-static-analysis-tools-in-copilot-code-review)


GitHub Universe 2025で有効化されたCodeQL品質検出に加えて、Copilotコードレビューで以下の静的解析ツールから結果を取得できるようになりました：


* ESLintは、JavaScriptおよびTypeScriptプロジェクトの問題を強調表示します。
* PMDは、Java、Apex、およびその他のサポートされている言語の問題をスキャンします。


### [Configure which tools are used with a repository rule](#configure-which-tools-are-used-with-a-repository-rule)


パブリックプレビュー参加者にはCodeQLがデフォルトで有効になっていますが、Copilotコードレビューで使用するツールを制御できるようになりました。新しいリポジトリルール「Copilotコードレビューで静的解析ツールを管理」が追加され、CodeQL、ESLint、PMDのオン/オフを切り替えることができます。このルールを使用すると、Enterprise、Organization、Team、またはRepositoryレベルでこれらの機能を有効にし、特定のブランチとリポジトリをターゲットにすることができます。


  

リポジトリルールセットページを開き、新しいルールでルールセットを作成するデモ  




#### [Get started](#get-started)


1. 管理者アクセス権を持つリポジトリで、**Settings** \> **Rules** \> **Rulesets**に移動します。
2. ルールセットを追加または編集し、新しい「Copilotコードレビューで静的解析ツールを管理」ルールを選択します。
3. Copilotコードレビューに含めたい静的解析ツールを選択します：ESLint、PMD、および/またはCodeQL。*CodeQLはデフォルトで有効になっており、ルールを介して無効にできるようになりました。*
4. ルールを保存し、新しいプルリクエストを開いて、新しいリンター設定でCopilotコードレビューが実行されることを確認します。


[Copilotコードレビューのリポジトリルールの構成について詳しく学びましょう](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/manage-tools)。


[GitHub Community](https://github.com/orgs/community/discussions/categories/copilot-conversations)のディスカッションに参加してください。
