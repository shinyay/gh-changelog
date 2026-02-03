---
title: "コードスキャンアラートアサイニーが一般提供開始"
date: "2025-12-16"
type: "new releases"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-16-code-scanning-alert-assignees-are-now-generally-available"
fetched_at: "2026-02-03T14:50:54.940330Z"
lang: "ja"
---

# コードスキャンアラートアサイニーが一般提供開始

## Overview
コードスキャンアラートアサイニーが一般提供され、アラートの明確な所有権を割り当てることで、チームがセキュリティの脆弱性をより効果的に追跡および修復できるようになります。

## Detailed Explanation
### Overview
- コードスキャンアラートアサイニーが一般提供され、アラートの明確な所有権を割り当てることで、チームがセキュリティの脆弱性をより効果的に追跡および修復できるようになります。

### 一般提供の新機能
- パブリックプレビュー以降、次の機能が追加されました：
- Copilotへの割り当て：開発者が潜在的な脆弱性を修復するために費やす時間を削減するために、Copilotコーディングエージェントに修正を委任できます。
- 通知：割り当てられたアラートアサイニーは、リポジトリの監視設定に基づいて、割り当てられたときに電子メール通知を受け取ります。
- Webhook：アサイニーの変更に対するWebhookイベントにより、既存のワークフローと自動化にアラートの割り当てを統合できます。
- REST APIサポート：REST APIを使用して、コードスキャンアラートにユーザーをプログラム的に表示、割り当て、割り当て解除でき、一括操作とカスタム統合が可能になります。

### コードスキャンアラートアサイニーの開始
- アラート詳細ページから、アラートが識別されたリポジトリへの`write`アクセス権を持つユーザーに、任意のコードスキャンアラートを割り当てることができるようになりました。コードスキャンアラートにユーザーを割り当てることで、開発者がissueやプルリクエストに既に使用しているワークフローと同じワークフローにセキュリティ作業が組み込まれます。アサイニーにより、チームは次のことができます：
- 特定の脆弱性の明確な所有権を持つ。
- GitHubで直接修復作業を追跡する。
- 責任を可視化し、実行可能にすることで修正を加速する。
- コードスキャンアラートアサイニーは、github.comのGitHub Code SecurityまたはGitHub Advanced Securityを使用しているお客様が利用でき、GitHub Enterprise Serverのお客様はバージョン3.20から利用できるようになります。
- コードスキャンアラートの管理とアラートの割り当てについて詳しく学びましょう。

## Impact / Who's Affected
- コードスキャンアラートアサイニーが一般提供され、アラートの明確な所有権を割り当てることで、チームがセキュリティの脆弱性をより効果的に追跡および修復できるようになります。
- パブリックプレビュー以降、次の機能が追加されました：Copilotへの割り当て：開発者が潜在的な脆弱性を修復するために費やす時間を削減するために、Copilotコーディングエージェントに修正を委任できます。

## Insights (derived from article language)
- コードスキャンアラートの管理とアラートの割り当てについて詳しく学びましょう。

## Article Content (cleaned)
コードスキャンアラートアサイニーが一般提供され、アラートの明確な所有権を割り当てることで、チームがセキュリティの脆弱性をより効果的に追跡および修復できるようになります。


### [一般提供の新機能](#whats-new-in-general-availability)


[パブリックプレビュー](https://github.blog/changelog/2025-09-23-accelerate-remediation-with-security-campaigns-and-assignable-alerts-for-code-scanning-and-secret-scanning)以降、次の機能が追加されました：


* **Copilotへの割り当て：** 開発者が潜在的な脆弱性を修復するために費やす時間を削減するために、[Copilotコーディングエージェントに修正を委任](https://github.blog/changelog/2025-10-28-assign-code-scanning-alerts-to-copilot-for-automated-fixes-in-public-preview)できます。
* **通知：** 割り当てられたアラートアサイニーは、リポジトリの監視設定に基づいて、割り当てられたときに電子メール通知を受け取ります。
* **Webhook：** アサイニーの変更に対するWebhookイベントにより、既存のワークフローと自動化にアラートの割り当てを統合できます。
* **REST APIサポート：** REST APIを使用して、コードスキャンアラートにユーザーをプログラム的に表示、割り当て、割り当て解除でき、一括操作とカスタム統合が可能になります。


![Copilot Autofixによって生成された修正提案を含むコードスキャンアラート。テキストには、見つかったエラーと問題を修復するために必要な手順が詳しく記載されています。右側のボックスは、Copilotが割り当てられているAssigneesセクションを強調表示しています](https://github.com/user-attachments/assets/ca39933d-7cf5-4248-b06d-94a1cf621734)


### [コードスキャンアラートアサイニーの開始](#getting-started-with-code-scanning-alert-assignees)


アラート詳細ページから、アラートが識別されたリポジトリへの`write`アクセス権を持つユーザーに、任意のコードスキャンアラートを割り当てることができるようになりました。コードスキャンアラートにユーザーを割り当てることで、開発者がissueやプルリクエストに既に使用しているワークフローと同じワークフローにセキュリティ作業が組み込まれます。アサイニーにより、チームは次のことができます：


* **特定の脆弱性の明確な所有権を持つ。**
* **GitHubで直接修復作業を追跡する。**
* **責任を可視化し、実行可能にすることで修正を加速する。**


コードスキャンアラートアサイニーは、github.comのGitHub Code SecurityまたはGitHub Advanced Securityを使用しているお客様が利用でき、GitHub Enterprise Serverのお客様はバージョン3\.20から利用できるようになります。


[コードスキャンアラートの管理](https://docs.github.com/code-security/code-scanning/managing-code-scanning-alerts/managing-code-scanning-alerts-for-your-repository)と[アラートの割り当て](https://docs.github.com/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-assignment)について詳しく学びましょう。
