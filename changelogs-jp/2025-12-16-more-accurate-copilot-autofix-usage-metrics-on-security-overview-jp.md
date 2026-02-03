---
title: "セキュリティ概要でより正確なCopilot Autofix使用状況メトリクス"
date: "2025-12-16"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-16-more-accurate-copilot-autofix-usage-metrics-on-security-overview"
fetched_at: "2026-02-03T14:50:54.932756Z"
lang: "ja"
---

# セキュリティ概要でより正確なCopilot Autofix使用状況メトリクス

## Overview
Copilot autofixesで修正されたCodeQLアラートのセキュリティ概要ダッシュボードに表示されるメトリクスを強化しました。

## Detailed Explanation
### Overview
- Copilot autofixesで修正されたCodeQLアラートのセキュリティ概要ダッシュボードに表示されるメトリクスを強化しました。
- この改善は、プルリクエストおよびデフォルトブランチのスキャンで検出されたCodeQLアラートを修復するために、autofixの提案がどの程度使用されたかを計算する方法を具体的に洗練します。これにより、「CodeQL pull request insights」ダッシュボードとセキュリティ概要の「Remediation」タブでより正確なメトリクスが提供され、Copilot Autofixが新しい脆弱性がコードにマージされるのを防ぎ、デフォルトブランチのセキュリティ債務を削減するのに役立つ方法についてより良い洞察が得られます。
- この変更は、autofixの提案を使用して修正されたプルリクエストおよびリポジトリのデフォルトブランチで検出されたCodeQLアラートに関連するダッシュボードメトリクスに遡及的に影響します。「Alerts fixed with autofix suggestions」および「Percentage of remediated alerts with autofix suggestion」は、今後10日間にわたって順次再計算され、これらの値の変更が予想されます。
- このアップデートは、GitHub Enterprise Cloudで一般提供されるようになりました。
- セキュリティ概要ドキュメントとコードスキャニングドキュメントを確認して詳しく学びましょう。

## Impact / Who’s Affected
- このアップデートは、GitHub Enterprise Cloudで一般提供されるようになりました。

## Insights (derived from article language)
- セキュリティ概要ドキュメントとコードスキャニングドキュメントを確認して詳しく学びましょう。

## Article Content (cleaned)
Copilot autofixesで修正されたCodeQLアラートのセキュリティ概要ダッシュボードに表示されるメトリクスを強化しました。


この改善は、プルリクエストおよびデフォルトブランチのスキャンで検出されたCodeQLアラートを修復するために、autofixの提案がどの程度使用されたかを計算する方法を具体的に洗練します。これにより、「CodeQL pull request insights」ダッシュボードとセキュリティ概要の**Remediation**タブでより正確なメトリクスが提供され、Copilot Autofixが新しい脆弱性がコードにマージされるのを防ぎ、デフォルトブランチのセキュリティ債務を削減するのに役立つ方法についてより良い洞察が得られます。


![セキュリティ概要ダッシュボードでCopilot autofixesで修正されたCodeQLプルリクエストアラートを示すテーブルのスクリーンショット](https://github.com/user-attachments/assets/8e9d36b1-98dd-4d90-9d09-b2026331dd58)


この変更は、autofixの提案を使用して修正されたプルリクエストおよびリポジトリのデフォルトブランチで検出されたCodeQLアラートに関連するダッシュボードメトリクスに遡及的に影響します。「Alerts fixed with autofix suggestions」および「Percentage of remediated alerts with autofix suggestion」は、今後10日間にわたって順次再計算され、これらの値の変更が予想されます。


このアップデートは、GitHub Enterprise Cloudで一般提供されるようになりました。


[セキュリティ概要ドキュメント](https://docs.github.com/enterprise-cloud@latest/code-security/security-overview/about-security-overview)と[コードスキャニングドキュメント](https://docs.github.com/enterprise-cloud@latest/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning)を確認して詳しく学びましょう。
