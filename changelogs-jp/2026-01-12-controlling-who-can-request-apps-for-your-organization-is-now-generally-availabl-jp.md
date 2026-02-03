---
title: "組織へのアプリリクエスト権限の制御が一般提供開始"
date: "2026-01-12"
type: "improvements"
labels: ["enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-12-controlling-who-can-request-apps-for-your-organization-is-now-generally-available"
fetched_at: "2026-02-03T14:50:54.819673Z"
lang: "ja"
---

# 組織へのアプリリクエスト権限の制御が一般提供開始

## Overview
組織は、GitHub AppsおよびOAuth appsをリクエストできるユーザーをより細かく制御できるようになりました。この機能強化により、セキュリティ体制の柔軟性を維持しながら、より厳格なガバナンスポリシーを実装できます。この機能は現在一般提供されています。

## Detailed Explanation
### Overview
- 組織は、GitHub AppsおよびOAuth appsをリクエストできるユーザーをより細かく制御できるようになりました。この機能強化により、セキュリティ体制の柔軟性を維持しながら、より厳格なガバナンスポリシーを実装できます。この機能は現在一般提供されています。

### What's changed
- 以前は、組織は外部コラボレーターからのアプリアクセスリクエストを無効にすることしかできませんでした。現在、3つの段階的な制御オプションから選択できます：
- Members and outside collaborators：メンバーと外部コラボレーターがアプリをリクエストできます。これは既存のデフォルト動作です。
- Members only：組織メンバーにはアプリのリクエストを許可しながら、外部コラボレーターをブロックします。
- Disable app access requests：メンバーと外部コラボレーターの両方がアプリをリクエストできないようにします。
- この変更を設定するには、組織の設定に移動し、Member Privilegesを選択し、「App access requests」の下で希望のオプションを選択します。この段階的な制御メカニズムにより、インストールを検討する前に、すべてのサードパーティアプリが適切な承認チャネルとセキュリティレビューを経由することが保証されます。
- 詳細については、「Limiting app requests」を参照してください。これはGHES 3.21に含まれる予定です。

### How to give feedback
- ご質問やフィードバックがある場合は、コミュニティディスカッションにコメントを残してください。

## Impact / Who's Affected
- この機能は現在一般提供されています。
- What's changed 以前は、組織は外部コラボレーターからのアプリアクセスリクエストを無効にすることしかできませんでした。
- Members only：組織メンバーにはアプリのリクエストを許可しながら、外部コラボレーターをブロックします。

## Caveats / Limitations
- What's changed 以前は、組織は外部コラボレーターからのアプリアクセスリクエストを無効にすることしかできませんでした。
- Members only：組織メンバーにはアプリのリクエストを許可しながら、外部コラボレーターをブロックします。

## Insights (derived from article language)
- この段階的な制御メカニズムにより、インストールを検討する前に、すべてのサードパーティアプリが適切な承認チャネルとセキュリティレビューを経由することが保証されます。
- 詳細については、「Limiting app requests」を参照してください。

## Article Content (cleaned)
組織は、GitHub AppsおよびOAuth appsをリクエストできるユーザーをより細かく制御できるようになりました。この機能強化により、セキュリティ体制の柔軟性を維持しながら、より厳格なガバナンスポリシーを実装できます。この機能は現在一般提供されています。


### [What's changed](#whats-changed)


以前は、組織は外部コラボレーターからのアプリアクセスリクエストを無効にすることしかできませんでした。現在、3つの段階的な制御オプションから選択できます：


* **Members and outside collaborators**：メンバーと外部コラボレーターがアプリをリクエストできます。これは既存のデフォルト動作です。
* **Members only**：組織メンバーにはアプリのリクエストを許可しながら、外部コラボレーターをブロックします。
* **Disable app access requests**：メンバーと外部コラボレーターの両方がアプリをリクエストできないようにします。


![A radio button menu showing three options within an organization's settings page to choose who can request GitHub or OAuth apps](https://github.com/user-attachments/assets/154ca23d-f556-43f5-ba6d-9a4d2c2fcf28)


この変更を設定するには、組織の設定に移動し、**Member Privileges**を選択し、「App access requests」の下で希望のオプションを選択します。この段階的な制御メカニズムにより、インストールを検討する前に、すべてのサードパーティアプリが適切な承認チャネルとセキュリティレビューを経由することが保証されます。


詳細については、[「Limiting app requests」](https://docs.github.com/organizations/managing-programmatic-access-to-your-organization/limiting-oauth-app-and-github-app-access-requests)を参照してください。これはGHES 3\.21に含まれる予定です。


### [How to give feedback](#how-to-give-feedback)


ご質問やフィードバックがある場合は、[コミュニティディスカッション](https://github.com/orgs/community/discussions/183833)にコメントを残してください。
