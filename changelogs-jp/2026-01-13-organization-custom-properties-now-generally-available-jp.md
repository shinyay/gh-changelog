---
title: "組織カスタムプロパティが一般提供開始"
date: "2026-01-13"
type: "improvements"
labels: ["enterprise management tools", "platform governance"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-13-organization-custom-properties-now-generally-available"
fetched_at: "2026-02-03T14:50:54.801696Z"
lang: "ja"
---

# 組織カスタムプロパティが一般提供開始

## Overview
組織カスタムプロパティが一般提供開始となり、エンタープライズ管理者に組織をメタデータでタグ付けし、エンタープライズルールセットを自動的にターゲット設定する強力な方法を提供します。

## Detailed Explanation
### Overview
- 組織カスタムプロパティが一般提供開始となり、エンタープライズ管理者に組織をメタデータでタグ付けし、エンタープライズルールセットを自動的にターゲット設定する強力な方法を提供します。

### Why organization custom properties
- エンタープライズは、ビジネスユニット、地理的地域、コンプライアンスフレームワーク、または開発段階に基づいてGitHubプレゼンスを編成することがよくあります。これまで、一貫したルールセットを適用するには、組織を1つずつ手動で選択するか、拡張性のない命名規則に依存する必要がありました。
- 組織カスタムプロパティを使用すると、次のことができます：
- 一度定義すれば、どこでも適用：`region: EMEA`、`compliance: SOC2`、または`business-unit: Platform`のようなプロパティで組織にタグを付け、ルールセットに任せます。
- 設定ドリフトを排除：新しく作成されたものも含め、条件に一致する組織にルールセットが自動的に適用されます。
- エンタープライズ構造に適応：部門、規制要件、またはプロジェクトライフサイクルで編成する場合でも、カスタムプロパティは対応します。
- EUで顧客データを扱うすべての組織に対して、より厳格なコードレビュー要件を強制する必要があるとします。手動リストを維持する代わりに、`region: EU`と`data-classification: customer-data`をターゲットとするルールセットを作成します。新しいEUベースのチームが組織を立ち上げると、ポリシーが自動的に適用されます。

### How it works
- エンタープライズ管理者は、エンタープライズレベルでカスタムプロパティを定義し、個々の組織に値を割り当てます。プロパティは次をサポートします：
- Single-select：定義済みリストから1つの値を選択
- Multi-select：定義済みリストから複数の値を選択
- Text：自由形式のテキストを入力
- True/false：ブール値を設定
- URL：URL値を入力
- 組織にタグを付けたら、エンタープライズルールセットはプロパティの任意の組み合わせに基づいてターゲット設定できます。

### Get started
- 組織カスタムプロパティは、すべてのGitHub Enterprise Cloudのお客様が利用できます。
- エンタープライズ管理者は、エンタープライズ設定の組織セクションでカスタムプロパティにアクセスできます。
- 詳細については、GitHub Docsの「Managing custom properties for organizations in your enterprise」を参照してください。

## Impact / Who’s Affected
- 組織カスタムプロパティが一般提供開始となり、エンタープライズ管理者に組織をメタデータでタグ付けし、エンタープライズルールセットを自動的にターゲット設定する強力な方法を提供します。

## Article Content (cleaned)
組織カスタムプロパティが一般提供開始となり、エンタープライズ管理者に組織をメタデータでタグ付けし、エンタープライズルールセットを自動的にターゲット設定する強力な方法を提供します。


## [Why organization custom properties](#why-organization-custom-properties)


エンタープライズは、ビジネスユニット、地理的地域、コンプライアンスフレームワーク、または開発段階に基づいてGitHubプレゼンスを編成することがよくあります。これまで、一貫したルールセットを適用するには、組織を1つずつ手動で選択するか、拡張性のない命名規則に依存する必要がありました。


組織カスタムプロパティを使用すると、次のことができます：


* **一度定義すれば、どこでも適用：**`region: EMEA`、`compliance: SOC2`、または`business-unit: Platform`のようなプロパティで組織にタグを付け、ルールセットに任せます。
* **設定ドリフトを排除：**新しく作成されたものも含め、条件に一致する組織にルールセットが自動的に適用されます。
* **エンタープライズ構造に適応：**部門、規制要件、またはプロジェクトライフサイクルで編成する場合でも、カスタムプロパティは対応します。


EUで顧客データを扱うすべての組織に対して、より厳格なコードレビュー要件を強制する必要があるとします。手動リストを維持する代わりに、`region: EU`と`data-classification: customer-data`をターゲットとするルールセットを作成します。新しいEUベースのチームが組織を立ち上げると、ポリシーが自動的に適用されます。


## [How it works](#how-it-works)


![A screenshot showing the "region" custom property settings, including its name, description, type, options, and other attributes](https://github.com/user-attachments/assets/f802250c-45ed-4532-8d49-1bc7333ccc9b)


エンタープライズ管理者は、エンタープライズレベルでカスタムプロパティを定義し、個々の組織に値を割り当てます。プロパティは次をサポートします：


* **Single\-select**：定義済みリストから1つの値を選択
* **Multi\-select**：定義済みリストから複数の値を選択
* **Text**：自由形式のテキストを入力
* **True/false**：ブール値を設定
* **URL**：URL値を入力


組織にタグを付けたら、エンタープライズルールセットはプロパティの任意の組み合わせに基づいてターゲット設定できます。


![A screenshot of the "Regional Compliance" code ruleset settings, showing its evaluation status, an empty bypass list, and target organizations defined by region and compliance frameworks.](https://github.com/user-attachments/assets/19aee9db-45e6-43b9-b956-c85b58b0bdec)


## [Get started](#get-started)


組織カスタムプロパティは、すべてのGitHub Enterprise Cloudのお客様が利用できます。


エンタープライズ管理者は、エンタープライズ設定の組織セクションでカスタムプロパティにアクセスできます。


詳細については、GitHub Docsの「[Managing custom properties for organizations in your enterprise](https://gh.io/org-properties-docs)」を参照してください。
