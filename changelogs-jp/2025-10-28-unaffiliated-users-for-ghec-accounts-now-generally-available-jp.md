---
title: "GHEC アカウントの非所属ユーザーが一般提供開始"
date: "2025-10-28"
type: "new releases"
labels: ["account management", "enterprise management tools", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-unaffiliated-users-for-ghec-accounts-now-generally-available"
fetched_at: "2026-02-03T14:50:55.642280Z"
lang: "ja"
---

# GHEC アカウントの非所属ユーザーが一般提供開始

## Overview
すべての GitHub Enterprise Cloud エンタープライズで非所属ユーザーにアクセスできるようになりました。非所属ユーザーとは、エンタープライズに属しているものの、エンタープライズ内のどの組織にも関連付けられていないエンタープライズメンバーです。これらのユーザーは、組織への関連付けなしに Copilot Business のライセンスを付与できます。

## Detailed Explanation
### Overview
- すべての GitHub Enterprise Cloud エンタープライズで非所属ユーザーにアクセスできるようになりました。非所属ユーザーとは、エンタープライズに属しているものの、エンタープライズ内のどの組織にも関連付けられていないエンタープライズメンバーです。これらのユーザーは、組織への関連付けなしに Copilot Business のライセンスを付与できます。
- 注：Enterprise Managed Users（EMU）を使用しているエンタープライズは、このリリースで新しい変更はありません。
- EMU を使用していないエンタープライズの場合、エンタープライズオーナーはユーザーをエンタープライズアカウントに直接招待できるようになりました。これらのユーザーはデフォルトで組織やライセンスにアクセスできませんが、後でエンタープライズチーム、組織、または Copilot Business ライセンスに割り当てることができます。非所属ユーザーはプライベートまたは内部リポジトリにアクセスできませんが、エンタープライズレベルで Copilot Business ライセンスを割り当てることや、エンタープライズチームに所属することは可能です。
- オフボーディングの重要な変更：すべての組織からユーザーが削除されると、そのユーザーは非所属ユーザーとしてエンタープライズに残ります。エンタープライズアカウントまたはエンタープライズチームを通じて Copilot Business ライセンスが直接割り当てられている場合、この関係はユーザーがエンタープライズ自体から削除されるまで持続します。
- エンタープライズオーナーは、エンタープライズ設定の「ポリシー」>「メンバー権限」>「エンタープライズ内の非所属ユーザー」でこの動作を構成できます。次のオプションのいずれかを選択できます：
- ユーザーを非所属ユーザーとしてエンタープライズに保持する。これが現在のデフォルト動作です。
- エンタープライズから自動的に削除する。これが以前のデフォルト動作でした。
- 自動削除を選択した場合、エンタープライズから既存の非所属ユーザーを削除するオプションもあります。
- または、ユーザーを手動でオフボードするには、「People」ビューでエンタープライズから削除アクションを実行するか、remove enterprise member graphql API を使用して自動化を作成する必要があります。これは、組織レベルで SCIM を構成している場合でも必要です。
- 詳細については、非所属ユーザーに関するドキュメントまたはエンタープライズアカウントでの Copilot Business ライセンスエクスペリエンスに関する changelog をご覧ください。
- GitHub Community でディスカッションに参加してください。

## Caveats / Limitations
- 注：Enterprise Managed Users（EMU）を使用しているエンタープライズは、このリリースで新しい変更はありません。
- オフボーディングの重要な変更：すべての組織からユーザーが削除されると、そのユーザーは非所属ユーザーとしてエンタープライズに残ります。

## Insights (derived from article language)
- 詳細については、非所属ユーザーに関するドキュメントまたはエンタープライズアカウントでの Copilot Business ライセンスエクスペリエンスに関する changelog をご覧ください。

## Article Content (cleaned)
すべての GitHub Enterprise Cloud エンタープライズで非所属ユーザーにアクセスできるようになりました。非所属ユーザーとは、エンタープライズに属しているものの、エンタープライズ内のどの組織にも関連付けられていないエンタープライズメンバーです。これらのユーザーは、[組織への関連付けなしに Copilot Business のライセンスを付与](https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-access/grant-access#assigning-licenses?utm_source=changelog-docs-unaffiliated-ghec-accounts&utm_medium=changelog&utm_campaign=universe25)できます。


**注**：Enterprise Managed Users（EMU）を使用しているエンタープライズは、このリリースで新しい変更はありません。


EMU を使用していないエンタープライズの場合、エンタープライズオーナーはユーザーをエンタープライズアカウントに直接招待できるようになりました。これらのユーザーはデフォルトで組織やライセンスにアクセスできませんが、後でエンタープライズチーム、組織、または Copilot Business ライセンスに割り当てることができます。非所属ユーザーはプライベートまたは内部リポジトリにアクセスできませんが、エンタープライズレベルで Copilot Business ライセンスを割り当てることや、エンタープライズチームに所属することは可能です。


**オフボーディングの重要な変更**：すべての組織からユーザーが削除されると、そのユーザーは非所属ユーザーとしてエンタープライズに残ります。エンタープライズアカウントまたはエンタープライズチームを通じて Copilot Business ライセンスが直接割り当てられている場合、この関係はユーザーがエンタープライズ自体から削除されるまで持続します。


エンタープライズオーナーは、**ポリシー** \> **メンバー権限** \> **エンタープライズ内の非所属ユーザー** でこの動作を構成できます。次のオプションのいずれかを選択できます：


* ユーザーを非所属ユーザーとしてエンタープライズに保持する。これが現在のデフォルト動作です。
* エンタープライズから自動的に削除する。これが以前のデフォルト動作でした。


自動削除を選択した場合、エンタープライズから既存の非所属ユーザーを削除するオプションもあります。


または、ユーザーを手動でオフボードするには、「People」ビューで[エンタープライズから削除アクション](https://docs.github.com/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/removing-a-member-from-your-enterprise?utm_source=changelog-docs-unaffiliated-ghec-accounts&utm_medium=changelog&utm_campaign=universe25)を実行するか、[remove enterprise member graphql API](https://docs.github.com/enterprise-cloud@latest/graphql/reference/mutations#removeenterprisemember?utm_source=changelog-docs-unaffiliated-ghec-accounts&utm_medium=changelog&utm_campaign=universe25) を使用して自動化を作成する必要があります。これは、組織レベルで SCIM を構成している場合でも必要です。


詳細については、[非所属ユーザーに関するドキュメント](https://docs.github.com/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/abilities-of-roles#unaffiliated-users?utm_source=changelog-docs-unaffiliated-ghec-accounts&utm_medium=changelog&utm_campaign=universe25)またはエンタープライズアカウントでの Copilot Business ライセンスエクスペリエンスに関する changelog をご覧ください。


[GitHub Community](https://github.com/orgs/community/discussions/177230?utm_source=changelog-community-unaffiliated-ghec-accounts&utm_medium=changelog&utm_campaign=universe25) でディスカッションに参加してください。
