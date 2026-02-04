---
title: "コストセンター使用量を除外するエンタープライズスコープの予算がパブリックプレビューに"
date: "2026-01-20"
type: "improvements"
labels: ["enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-19-enterprise-scoped-budgets-that-exclude-cost-center-usage-in-public-preview"
fetched_at: "2026-02-03T14:50:54.750207Z"
lang: "ja"
---

# コストセンター使用量を除外するエンタープライズスコープの予算がパブリックプレビューに

## Overview
GitHub Enterprise のお客様は、コストセンター使用量を除外するエンタープライズスコープの予算を設定できるようになり、エンタープライズの特定の部分が追加の使用量を発生させることを許可しながら、残りの部分を制限できるようになりました。

## Detailed Explanation
### Overview
- GitHub Enterprise のお客様は、コストセンター使用量を除外するエンタープライズスコープの予算を設定できるようになり、エンタープライズの特定の部分が追加の使用量を発生させることを許可しながら、残りの部分を制限できるようになりました。
- 以前は、デフォルトの制限を適用するために、エンタープライズのすべての部分に個別の予算を作成する必要がありました。この改善により、エンタープライズは、コストセンター使用量を除外するエンタープライズスコープの予算を適用し、コストセンターを使用して追加の使用量へのアクセスを選択的に付与できるようになりました。

### Key details
- このオプションは、エンタープライズスコープの予算でのみ利用可能で、新規または既存の予算に適用できます。
- 既存のエンタープライズスコープの予算は、デフォルトでコストセンター使用量を引き続き含みます。
- このオプションは REST API を通じて利用可能で、この設定への変更は監査ログに記録されます。
- 詳細については、「メーター制品の支出を制御するための予算の設定」を参照してください。

## Impact / Who’s Affected
- Key details このオプションは、エンタープライズスコープの予算でのみ利用可能で、新規または既存の予算に適用できます。

## Caveats / Limitations
- Key details このオプションは、エンタープライズスコープの予算でのみ利用可能で、新規または既存の予算に適用できます。

## Insights (derived from article language)
- 詳細については、「メーター制品の支出を制御するための予算の設定」を参照してください。

## Article Content (cleaned)
GitHub Enterprise のお客様は、コストセンター使用量を除外するエンタープライズスコープの予算を設定できるようになり、エンタープライズの特定の部分が追加の使用量を発生させることを許可しながら、残りの部分を制限できるようになりました。


以前は、デフォルトの制限を適用するために、エンタープライズのすべての部分に個別の予算を作成する必要がありました。この改善により、エンタープライズは、コストセンター使用量を除外するエンタープライズスコープの予算を適用し、コストセンターを使用して追加の使用量へのアクセスを選択的に付与できるようになりました。


![Screenshot showing the new option to exclude cost center usage when configuring an enterprise budget](https://github.com/user-attachments/assets/30311d80-9e91-4f32-860c-4e49e5b450e9)


### [Key details](#key-details)


* このオプションは、エンタープライズスコープの予算でのみ利用可能で、新規または既存の予算に適用できます。
* 既存のエンタープライズスコープの予算は、デフォルトでコストセンター使用量を引き続き含みます。
* このオプションは REST API を通じて利用可能で、この設定への変更は監査ログに記録されます。


詳細については、「[メーター制品の支出を制御するための予算の設定](https://docs.github.com/enterprise-cloud@latest/billing/tutorials/set-up-budgets)」を参照してください。
