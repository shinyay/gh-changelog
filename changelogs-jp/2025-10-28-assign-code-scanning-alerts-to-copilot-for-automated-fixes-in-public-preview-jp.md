---
title: "code scanning アラートを Copilot に割り当てて自動修正（パブリックプレビュー）"
date: "2025-10-28"
type: "new releases"
labels: ["application security", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-assign-code-scanning-alerts-to-copilot-for-automated-fixes-in-public-preview"
fetched_at: "2026-02-03T14:50:55.693811Z"
lang: "ja"
---

# code scanning アラートを Copilot に割り当てて自動修正（パブリックプレビュー）

## Overview
GitHub の code scanning アラートを Copilot に直接割り当て、自動的な修復（remediation）を支援させられるようになりました。Copilot coding agent の機能がセキュリティ脆弱性にも拡張され、よくある問題をより早く解決できます。

## Detailed Explanation
### Overview
- GitHub の code scanning アラートを Copilot に直接割り当て、自動的な修復（remediation）を支援させられるようになりました。Copilot coding agent の機能がセキュリティ脆弱性にも拡張され、よくある問題をより早く解決できます。
- Copilot coding agent は Copilot Autofix と連携し、開発者がセキュリティ修正の計画と実装に費やす時間を削減します。まず、アラートページまたはセキュリティキャンペーンにアラートを含めることで、GitHub 上で code scanning アラートの autofix 提案を生成します。代わりに REST API で autofix 提案を生成することもできます。その後、以下の割り当て方法のいずれかで Copilot を割り当て、修復を開始します。

### Bulk assignment
- リポジトリのセキュリティキャンペーンへ移動し、1件以上のアラートを選択して、**Assign Copilot** をクリックします。複数のアラートを 1 つのプルリクエストで修正できます。

### Individual assignment
- アラート詳細ページから特定のアラートを割り当て、対象を絞って修正できます。
- 割り当て後、Copilot が脆弱性を分析し、修復計画を作成して、ドラフトのプルリクエストを開きます。コード変更が完了すると、プルリクエストはレビュー可能になります。GitHub UI のリンクから、各プルリクエストの進捗を簡単に追跡できます。
- この機能は、GitHub Enterprise Cloud 上で GitHub Code Security または GitHub Advanced Security と Copilot coding agent を利用しているお客様向けに提供されています。
- GitHub code scanning とセキュリティキャンペーンの詳細、または Copilot coding agent の利用開始についてはドキュメントを参照してください。

## Impact / Who’s Affected
- この機能は、GitHub Enterprise Cloud 上で GitHub Code Security または GitHub Advanced Security と Copilot coding agent を利用しているお客様向けに提供されています。

## Insights (derived from article language)
- GitHub code scanning とセキュリティキャンペーンの詳細、または Copilot coding agent の利用開始についてはドキュメントを参照してください。

## Article Content (cleaned)
GitHub の code scanning アラートを Copilot に直接割り当て、自動的な修復（remediation）を支援させられるようになりました。Copilot coding agent の機能がセキュリティ脆弱性にも拡張され、よくある問題をより早く解決できます。


Copilot coding agent は Copilot Autofix と連携し、開発者がセキュリティ修正の計画と実装に費やす時間を削減します。まず、アラートページまたはセキュリティキャンペーンにアラートを含めることで、GitHub 上で code scanning アラートの autofix 提案を生成します。代わりに REST API で autofix 提案を生成することもできます。その後、以下の割り当て方法のいずれかで Copilot を割り当て、修復を開始します。


### [Bulk assignment](#bulk-assignment)


リポジトリのセキュリティキャンペーンへ移動し、1件以上のアラートを選択して、**Assign Copilot** をクリックします。複数のアラートを 1 つのプルリクエストで修正できます。


![セキュリティキャンペーンで autofix 提案のある複数アラートが選択され、Assign to Copilot ボタンが表示されている画面](https://github.com/user-attachments/assets/f7abb217-b134-4f5e-b6d4-6cec4acefa5d)


### [Individual assignment](#individual-assignment)


アラート詳細ページから特定のアラートを割り当て、対象を絞って修正できます。


![autofix 提案がある個別の code scanning アラートに対し、右側の assignee picker から Copilot を割り当てる画面](https://github.com/user-attachments/assets/ca39933d-7cf5-4248-b06d-94a1cf621734)


割り当て後、Copilot が脆弱性を分析し、修復計画を作成して、ドラフトのプルリクエストを開きます。コード変更が完了すると、プルリクエストはレビュー可能になります。GitHub UI のリンクから、各プルリクエストの進捗を簡単に追跡できます。


この機能は、GitHub Enterprise Cloud 上で GitHub Code Security または GitHub Advanced Security と Copilot coding agent を利用しているお客様向けに提供されています。


[GitHub code scanning](https://docs.github.com/code-security/code-scanning?utm_source=changelog-docs-assign-alerts-to-copilot&utm_medium=changelog&utm_campaign=universe25) と [security campaigns](https://docs.github.com/enterprise-cloud@latest/code-security/securing-your-organization/fixing-security-alerts-at-scale/about-security-campaigns?utm_source=changelog-docs-assign-alerts-to-copilot&utm_medium=changelog&utm_campaign=universe25) の詳細、または [Copilot coding agent の利用開始](https://github.com/features/copilot?utm_source=changelog-copilot-assign-alerts-to-copilot&utm_medium=changelog&utm_campaign=universe25) を参照してください。
