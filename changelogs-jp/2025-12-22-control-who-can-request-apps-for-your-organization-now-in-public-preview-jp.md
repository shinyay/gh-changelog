---
title: "組織へのアプリリクエスト権限の制御がパブリックプレビューで利用可能に"
date: "2025-12-22"
type: "improvements"
labels: ["enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-22-control-who-can-request-apps-for-your-organization"
fetched_at: "2026-02-03T14:50:54.834843Z"
lang: "ja"
---

# 組織へのアプリリクエスト権限の制御がパブリックプレビューで利用可能に

## Overview
組織は、GitHub AppsおよびOAuth appsをリクエストできるユーザーをより細かく制御できるようになりました。この機能強化により、セキュリティ体制の柔軟性を維持しながら、より厳格なガバナンスポリシーを実装できます。この機能は現在パブリックプレビューで利用可能です。

## Detailed Explanation
### Overview
- 組織は、GitHub AppsおよびOAuth appsをリクエストできるユーザーをより細かく制御できるようになりました。この機能強化により、セキュリティ体制の柔軟性を維持しながら、より厳格なガバナンスポリシーを実装できます。この機能は現在パブリックプレビューで利用可能です。

### What's changed
- 以前は、組織は外部コラボレーターからのアプリアクセスリクエストを無効にすることしかできませんでした。現在、3つの段階的な制御オプションから選択できます：
- Members and outside collaborators：メンバーと外部コラボレーターがアプリをリクエストできます（既存のデフォルト動作）。
- Members only：組織メンバーにはアプリのリクエストを許可しながら、外部コラボレーターをブロックします。
- Disable app access requests：メンバーと外部コラボレーターの両方がアプリをリクエストできないようにします。
- この変更を設定するには、組織の設定に移動し、Member Privilegesを選択し、App access requestsの下で希望のオプションを選択します。この新しい制御メカニズムにより、インストールを検討する前に、すべてのサードパーティアプリが適切な承認チャネルとセキュリティレビューを経由することが保証されます。
- 詳細については、「Limiting app requests」を参照してください。これはGHES 3.21に含まれる予定です。

### How to give feedback
- ご質問やフィードバックがある場合は、GitHub Communityにアクセスしてください。

## Impact / Who's Affected
- この機能は現在パブリックプレビューで利用可能です。
- What's changed 以前は、組織は外部コラボレーターからのアプリアクセスリクエストを無効にすることしかできませんでした。
- Members only：組織メンバーにはアプリのリクエストを許可しながら、外部コラボレーターをブロックします。

## Caveats / Limitations
- What's changed 以前は、組織は外部コラボレーターからのアプリアクセスリクエストを無効にすることしかできませんでした。
- Members only：組織メンバーにはアプリのリクエストを許可しながら、外部コラボレーターをブロックします。

## Insights (derived from article language)
- この新しい制御メカニズムにより、インストールを検討する前に、すべてのサードパーティアプリが適切な承認チャネルとセキュリティレビューを経由することが保証されます。
- 詳細については、「Limiting app requests」を参照してください。

## Article Content (cleaned)
組織は、GitHub AppsおよびOAuth appsをリクエストできるユーザーをより細かく制御できるようになりました。この機能強化により、セキュリティ体制の柔軟性を維持しながら、より厳格なガバナンスポリシーを実装できます。この機能は現在パブリックプレビューで利用可能です。


### [What's changed](#whats-changed)


以前は、組織は外部コラボレーターからのアプリアクセスリクエストを無効にすることしかできませんでした。現在、3つの段階的な制御オプションから選択できます：


* **Members and outside collaborators**：メンバーと外部コラボレーターがアプリをリクエストできます（既存のデフォルト動作）。
* **Members only**：組織メンバーにはアプリのリクエストを許可しながら、外部コラボレーターをブロックします。
* **Disable app access requests**：メンバーと外部コラボレーターの両方がアプリをリクエストできないようにします。


![Three options within an organization's settings page to choose who can request GitHub or OAuth apps](https://github.com/user-attachments/assets/086f553d-0dec-4f8a-aa6a-e513d6384c66)


この変更を設定するには、組織の設定に移動し、**Member Privileges**を選択し、**App access requests**の下で希望のオプションを選択します。この新しい制御メカニズムにより、インストールを検討する前に、すべてのサードパーティアプリが適切な承認チャネルとセキュリティレビューを経由することが保証されます。


詳細については、[「Limiting app requests」](https://docs.github.com/organizations/managing-programmatic-access-to-your-organization/limiting-oauth-app-and-github-app-access-requests)を参照してください。これはGHES 3\.21に含まれる予定です。


### [How to give feedback](#how-to-give-feedback)


ご質問やフィードバックがある場合は、[GitHub Community](https://github.com/orgs/community/discussions)にアクセスしてください。
