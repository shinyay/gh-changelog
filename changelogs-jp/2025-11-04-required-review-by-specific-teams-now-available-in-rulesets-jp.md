---
title: "ルールセットで特定チームによる必須レビューが利用可能に"
date: "2025-11-04"
type: "improvements"
labels: ["collaboration tools", "platform governance"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-03-required-review-by-specific-teams-now-available-in-rulesets"
fetched_at: "2026-02-03T14:50:55.468584Z"
lang: "ja"
---

# ルールセットで特定チームによる必須レビューが利用可能に

## Overview
ファイルとフォルダーに基づいて、保護されたブランチへの変更マージに特定チームからの承認を要求できるようになり、特定ブランチへの変更承認者をより細かく制御できます。

## Detailed Explanation
### 概要
- ファイルとフォルダーに基づいて、保護されたブランチへの変更マージに特定チームからの承認を要求できるようになり、特定ブランチへの変更承認者をより細かく制御できます。

### 新機能
- ルールセットへの新しい追加により、次のことが可能になります：
- リリースまたは本番環境ブランチに対して、より厳格なレビューポリシーを適用して機密性の高いブランチを保護します。
- 一貫した適用のために、リポジトリ、組織、またはエンタープライズ全体にわたってポリシーを拡張します。
- 特定のファイルとフォルダーをターゲットにし、指定されたチームから特定数のレビューを要求します。

### CODEOWNERS との違い
- CODEOWNERS は所有権の定義に優れていますが、この新しいルールセットはポリシーの適用に焦点を当てています。機密性の高いブランチと重要なコードパスで特定の承認を簡単に要求でき、エンタープライズ全体でシームレスに拡張できます。
- この新しいルールは CODEOWNER ファイルを補完するように設計されており、置き換えるものではありません。CODEOWNERS ファイルは引き続き所有権の管理、個人をレビュアーとしてサポート、および必須でない場合でもレビューをリクエストする方法として機能します。
- 詳細については、ルールセットに関するドキュメントをご覧ください。
- GitHub Community でディスカッションに参加してフィードバックを共有してください。

## Insights (derived from article language)
- 詳細については、ルールセットに関するドキュメントをご覧ください。

## Article Content (cleaned)
ファイルとフォルダーに基づいて、保護されたブランチへの変更マージに特定チームからの承認を要求できるようになり、特定ブランチへの変更承認者をより細かく制御できます。


## [新機能](#whats-new)


![Screenshot of the required reviewer rule dialog with the Bakers team selected as reviewer, two required approvals, and file patterns set to match GitHub workflow and YAML files](https://github.com/user-attachments/assets/039259c4-3aca-4850-9579-b57550f3c8b3)


[ルールセット](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)への新しい追加により、次のことが可能になります：


* **機密性の高いブランチを保護**：リリースまたは本番環境ブランチに対して、より厳格なレビューポリシーを適用します。
* **ポリシーを拡張**：一貫した適用のために、リポジトリ、組織、またはエンタープライズ全体にわたってポリシーを拡張します。
* **特定のファイルとフォルダーをターゲット**：指定されたチームから特定数のレビューを要求します。


## [CODEOWNERS との違い](#how-this-differs-from-codeowners)


CODEOWNERS は所有権の定義に優れていますが、この新しいルールセットはポリシーの適用に焦点を当てています。機密性の高いブランチと重要なコードパスで特定の承認を簡単に要求でき、エンタープライズ全体でシームレスに拡張できます。


この新しいルールは CODEOWNER ファイルを補完するように設計されており、置き換えるものではありません。CODEOWNERS ファイルは引き続き所有権の管理、個人をレビュアーとしてサポート、および必須でない場合でもレビューをリクエストする方法として機能します。


詳細については、[ルールセットに関するドキュメント](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)をご覧ください。


[GitHub Community](https://gh.io/required-reviewer-feedback) でディスカッションに参加してフィードバックを共有してください。
