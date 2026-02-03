---
title: "新しい請求 API アップデートで予算管理と使用量追跡が可能に"
date: "2025-11-03"
type: "new releases"
labels: ["account management", "enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-03-manage-budgets-and-track-usage-with-new-billing-api-updates"
fetched_at: "2026-02-03T14:50:55.481769Z"
lang: "ja"
---

# 新しい請求 API アップデートで予算管理と使用量追跡が可能に

## Overview
請求 API を拡張し、プログラムで予算を管理し、使用量を追跡し、コストセンターデータにアクセスできる新機能を提供します。

## Detailed Explanation
### 概要
- 請求 API を拡張し、プログラムで予算を管理し、使用量を追跡し、コストセンターデータにアクセスできる新機能を提供します。

### API 経由での予算管理
- API を介して予算のライフサイクル全体を管理できるようになりました。以前は、予算は UI を通じてのみ管理可能でした。現在は、プログラムで予算の作成、更新、削除、および予算額とアラート通知の調整が可能です。現在、アカウントごとに 50 個の予算という一時的な制限があります。この API は現在パブリックプレビューで利用可能です。
- 詳細については、予算の REST API エンドポイントに関するドキュメントをご参照ください。

### 新しい Usage summary API で使用量を追跡
- 新しい Usage summary API を使用すると、アカウント全体の使用量情報を取得したり、特定の組織、リポジトリ、コストセンター、製品、または SKU でフィルタリングしたりできます。使用量は年、月、または日単位でクエリできます。この API は現在パブリックプレビューで利用可能です。
- 詳細については、Usage summary REST API エンドポイントに関するドキュメントをご参照ください。

### その他の改善
- コストセンター API の改善：エンタープライズのすべてのコストセンターを取得する API に、オプションの state パラメータが追加されました。これにより、エンドポイント呼び出し時に ?state=active を追加することで、アクティブなコストセンターのみを取得できます。
- 使用量レポート API の変更：既存の使用量レポート API から hour パラメータを削除し、day パラメータ使用時のレスポンスの粒度を下げて、時間ごとの内訳ではなく日次合計を提供するようにしました。詳細については、エンタープライズの請求使用量レポートを取得する REST API エンドポイントに関するドキュメントをご参照ください。

### この機能を使用できるユーザー
- GitHub Enterprise プランのエンタープライズオーナーおよび請求マネージャー
- GitHub Team プランの組織オーナー
- 個人プランの個人ユーザー
- GitHub Community でディスカッションに参加してください。

## Key Changes
- コストセンター API の改善：エンタープライズのすべてのコストセンターを取得する API に、オプションの state パラメータが追加されました。これにより、エンドポイント呼び出し時に ?state=active を追加することで、アクティブなコストセンターのみを取得できます。
- 使用量レポート API の変更：既存の使用量レポート API から hour パラメータを削除し、day パラメータ使用時のレスポンスの粒度を下げて、時間ごとの内訳ではなく日次合計を提供するようにしました。詳細については、エンタープライズの請求使用量レポートを取得する REST API エンドポイントに関するドキュメントをご参照ください。
- GitHub Enterprise プランのエンタープライズオーナーおよび請求マネージャー
- GitHub Team プランの組織オーナー
- 個人プランの個人ユーザー
- GitHub Community でディスカッションに参加してください。

## Impact / Who's Affected
- 以前は、予算は UI を通じてのみ管理可能でした。
- この API は現在パブリックプレビューで利用可能です。
- その他の改善 コストセンター API の改善：エンタープライズのすべてのコストセンターを取得する API に、オプションの state パラメータが追加されました。これにより、エンドポイント呼び出し時に ?state=active を追加することで、アクティブなコストセンターのみを取得できます。

## Caveats / Limitations
- 以前は、予算は UI を通じてのみ管理可能でした。
- その他の改善 コストセンター API の改善：エンタープライズのすべてのコストセンターを取得する API に、オプションの state パラメータが追加されました。これにより、エンドポイント呼び出し時に ?state=active を追加することで、アクティブなコストセンターのみを取得できます。

## Insights (derived from article language)
- 詳細については、予算の REST API エンドポイントに関するドキュメントをご参照ください。
- 詳細については、Usage summary REST API エンドポイントに関するドキュメントをご参照ください。
- 詳細については、エンタープライズの請求使用量レポートを取得する REST API エンドポイントに関するドキュメントをご参照ください。

## Article Content (cleaned)
請求 API を拡張し、プログラムで予算を管理し、使用量を追跡し、コストセンターデータにアクセスできる新機能を提供します。


### [API 経由での予算管理](#manage-budgets-via-apis)


API を介して予算のライフサイクル全体を管理できるようになりました。以前は、予算は UI を通じてのみ管理可能でした。現在は、プログラムで予算の作成、更新、削除、および予算額とアラート通知の調整が可能です。現在、アカウントごとに 50 個の予算という一時的な制限があります。この API は現在パブリックプレビューで利用可能です。


詳細については、[予算の REST API エンドポイントに関するドキュメント](https://gh.io/budget-api-docs)をご参照ください。


### [新しい Usage summary API で使用量を追跡](#track-usage-with-the-new-usage-summary-api)


新しい Usage summary API を使用すると、アカウント全体の使用量情報を取得したり、特定の組織、リポジトリ、コストセンター、製品、または SKU でフィルタリングしたりできます。使用量は年、月、または日単位でクエリできます。この API は現在パブリックプレビューで利用可能です。


詳細については、[Usage summary REST API エンドポイントに関するドキュメント](https://gh.io/usage-summary-api)をご参照ください。


### [その他の改善](#additional-improvements)


* **コストセンター API の改善**：[エンタープライズのすべてのコストセンターを取得する API](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/cost-centers?apiVersion=2022-11-28#get-all-cost-centers-for-an-enterprise) に、オプションの `state` パラメータが追加されました。これにより、エンドポイント呼び出し時に `?state=active` を追加することで、アクティブなコストセンターのみを取得できます。
* **使用量レポート API の変更**：既存の使用量レポート API から `hour` パラメータを削除し、`day` パラメータ使用時のレスポンスの粒度を下げて、時間ごとの内訳ではなく日次合計を提供するようにしました。詳細については、[エンタープライズの請求使用量レポートを取得する REST API エンドポイントに関するドキュメント](https://docs.github.com/en/enterprise-cloud@latest/rest/billing/usage?apiVersion=2022-11-28#get-billing-usage-report-for-an-enterprise)をご参照ください。


### [この機能を使用できるユーザー](#who-can-use-these-features)


* GitHub Enterprise プランのエンタープライズオーナーおよび請求マネージャー
* GitHub Team プランの組織オーナー
* 個人プランの個人ユーザー


[GitHub Community](https://gh.io/billing-api-community-feedback) でディスカッションに参加してください。
