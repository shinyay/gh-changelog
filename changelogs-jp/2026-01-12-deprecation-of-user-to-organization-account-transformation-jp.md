---
title: "ユーザーから組織へのアカウント変換の廃止"
date: "2026-01-12"
type: "deprecations"
labels: ["account management"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-12-deprecation-of-user-to-organization-account-transformation"
fetched_at: "2026-02-03T14:50:54.823136Z"
lang: "ja"
---

# ユーザーから組織へのアカウント変換の廃止

## Overview
2026年1月12日現在、個人ユーザーアカウントを組織に直接変換する機能を廃止します。個人アカウントを維持しながら、リポジトリを選択的に組織に移行するためのMove workフローを使用できるようになりました。

## Detailed Explanation
### Overview
- 2026年1月12日現在、個人ユーザーアカウントを組織に直接変換する機能を廃止します。個人アカウントを維持しながら、リポジトリを選択的に組織に移行するためのMove workフローを使用できるようになりました。
- ユーザーアカウントを変換する代わりに、新しいMove workフローを使用してリポジトリを移行します：
- ユーザープロフィール設定に移動し、SSO and organizationsをクリックします。
- 「Move to an organization」セクションで、Move work to an organizationをクリックします。
- 転送するリポジトリを選択します。
- 既存の組織を選択するか、新しい組織を作成します。
- 現在のユーザー名を組織に使用したい場合は、まず個人アカウントの名前を変更する必要があります：
- ユーザー名を新しいものに変更します。
- 元のユーザー名で組織を作成するか、workを移動します。
- Move work機能はGHESでは利用できません。リポジトリを移行するには、リポジトリ転送ドキュメントに従ってください。

## Insights (derived from article language)
- What you should do ユーザーアカウントを変換する代わりに、新しいMove workフローを使用してリポジトリを移行します：ユーザープロフィール設定に移動し、SSO and organizationsをクリックします。

## Article Content (cleaned)
2026年1月12日現在、個人ユーザーアカウントを組織に直接変換する機能を廃止します。個人アカウントを維持しながら、リポジトリを選択的に組織に移行するための**Move work**フローを使用できるようになりました。


#### [What you should do](#what-you-should-do)


ユーザーアカウントを変換する代わりに、新しい**Move work**フローを使用してリポジトリを移行します：


1. ユーザープロフィール設定に移動し、**SSO and organizations**をクリックします。
2. 「Move to an organization」セクションで、**Move work to an organization**をクリックします。
3. 転送するリポジトリを選択します。
4. 既存の組織を選択するか、新しい組織を作成します。


#### [Keeping your username for the organization](#keeping-your-username-for-the-organization)


現在のユーザー名を組織に使用したい場合は、まず個人アカウントの名前を変更する必要があります：


1. [ユーザー名を](https://docs.github.com/account-and-profile/how-tos/account-management/changing-your-username#changing-your-username)新しいものに変更します。
2. 元のユーザー名で組織を作成するか、workを移動します。


#### [For GitHub Enterprise Server users](#for-github-enterprise-server-users)


**Move work**機能はGHESでは利用できません。リポジトリを移行するには、[リポジトリ転送ドキュメント](https://docs.github.com/enterprise-server@3.19/repositories/creating-and-managing-repositories/transferring-a-repository)に従ってください。
