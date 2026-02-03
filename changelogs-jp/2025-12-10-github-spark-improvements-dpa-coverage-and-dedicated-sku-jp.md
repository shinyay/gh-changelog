---
title: "GitHub Spark: 改善、DPAカバレッジ、専用SKU"
date: "2025-12-10"
type: "improvements"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-10-github-spark-improvements-dpa-coverage-dedicated-sku"
fetched_at: "2026-02-03T14:50:54.994503Z"
lang: "ja"
---

# GitHub Spark: 改善、DPAカバレッジ、専用SKU

## Overview
10月27日時点で、SparkはGitHub Data Protection Agreementの対象となり、Sparkでのデータの取り扱いはパブリックプレビュー中であっても一般提供の製品と同様になります。これにより、より厳格なデータ要件を持つ組織が、他の一般提供製品と同様にSparkを活用できるようになります。詳細については、[プレビュー機能にDPAがどのように適用されるか](https://docs.github.com/site-policy/github-terms/github-dpa-previews)に関するドキュメントをお読みください。

## Detailed Explanation
### SparkはGitHub Data Protection Agreementの対象
- 10月27日時点で、SparkはGitHub Data Protection Agreementの対象となり、Sparkでのデータの取り扱いはパブリックプレビュー中であっても一般提供の製品と同様になります。これにより、より厳格なデータ要件を持つ組織が、他の一般提供製品と同様にSparkを活用できるようになります。詳細については、[プレビュー機能にDPAがどのように適用されるか](https://docs.github.com/site-policy/github-terms/github-dpa-previews)に関するドキュメントをお読みください。

### Spark専用SKUと予算管理
- 組織管理者は、請求ビューでSpark専用のSKUを確認できるようになりました。これは、管理者が請求ダッシュボードとCSVエクスポートで他のすべてのCopilot使用量とは別にSparkの支出を表示できることを意味します。また、Spark専用の詳細なプレミアムリクエスト予算と超過ポリシーを設定することもできます。管理者は、プレミアムリクエストを活用するすべての製品に対して、バンドルされたプレミアムリクエスト予算を設定するオプションもあります。これらはすべて、組織の**Billing and licensing**タブで管理できます。

### 生成されたアプリの視覚的品質の向上
- 生成されたアプリの視覚的品質を向上させるために、Sparkエージェントに変更を実装しました。より独自性のあるデザインと、より高品質なUIおよびUXを持つアプリが表示されるようになります。以下の改善例をご覧ください:

### エージェントの改善
- Sparkエージェントは、ユーザーによる以前の手動編集をより尊重し、ユーザーが行った手動変更を上書きしないようにします。
- また、利用可能なモデルのコンテキストウィンドウを超える非常に複雑なアプリの生成方法を改善し、非常に複雑なユースケースでもアプリを生成できるようにしました。

### リポジトリ作成の組織管理者設定
- 組織管理者は、すべてのSparksのリポジトリ作成を個人ユーザーアカウントではなく組織に強制できるようになりました。この設定はデフォルトでオフになっており、組織管理者がCopilot設定ページで有効にできます。

### その他の改善
- すべてのユーザーにとってSparkの構築と編集をさらにアクセスしやすくするための、多数のアクセシビリティの改善。
- エージェントによるすべてのコード生成が完了次第、アプリのライブプレビューを表示するようになり、できるだけ早くアプリと対話できるようになりました。
- Sparkの開発で使用される特定のカスタムドメインのテストパスを削除し、潜在的なセキュリティリスクを排除しました。
- UI、反復、公開、およびリポジトリ作成の問題につながる問題の複数のバグ修正。
- Sparkに対する手動コミットが失われないようにするための改善。
- エラーにつながるエージェントへの複数の同時リクエストの送信を防ぐためのSpark UIへの変更。

### 今日これらの改善を試す
- 次のアプリを構築するには、[github.com/spark](https://github.com/spark)にアクセスしてください。

## Key Changes
- Sparkエージェントは、ユーザーによる以前の手動編集をより尊重し、ユーザーが行った手動変更を上書きしないようにします。
- また、利用可能なモデルのコンテキストウィンドウを超える非常に複雑なアプリの生成方法を改善し、非常に複雑なユースケースでもアプリを生成できるようにしました。
- すべてのユーザーにとってSparkの構築と編集をさらにアクセスしやすくするための、多数のアクセシビリティの改善。
- エージェントによるすべてのコード生成が完了次第、アプリのライブプレビューを表示するようになり、できるだけ早くアプリと対話できるようになりました。
- Sparkの開発で使用される特定のカスタムドメインのテストパスを削除し、潜在的なセキュリティリスクを排除しました。
- UI、反復、公開、およびリポジトリ作成の問題につながる問題の複数のバグ修正。
- Sparkに対する手動コミットが失われないようにするための改善。
- エージェントへの複数の同時リクエストの送信を防ぐためのSpark UIへの変更。
- 次のアプリを構築するには、github.com/sparkにアクセスしてください。

## Impact / Who's Affected
- **SparkはGitHub Data Protection Agreementの対象**: 10月27日時点で、SparkはGitHub Data Protection Agreementの対象となり、Sparkでのデータの取り扱いはパブリックプレビュー中であっても一般提供の製品と同様になります。
- これにより、より厳格なデータ要件を持つ組織が、他の一般提供製品と同様にSparkを活用できるようになります。

## Insights (derived from article language)
- 詳細については、プレビュー機能にDPAがどのように適用されるかに関するドキュメントをお読みください。
- より独自性のあるデザインと、より高品質なUIおよびUXを持つアプリが表示されるようになります。

## Article Content (cleaned)
### [多数の改善、Spark専用SKU、およびSparkがGitHub DPAの対象となることを保証するリリースを行いました！すべての変更について読み進めてください。](#weve-released-a-number-of-improvements-a-dedicated-sku-for-spark-and-ensured-spark-is-covered-by-the-github-dpa-read-on-to-hear-about-all-of-the-changes)


## [SparkはGitHub Data Protection Agreementの対象](#spark-is-covered-by-the-github-data-protection-agreement)


10月27日時点で、SparkはGitHub Data Protection Agreementの対象となり、Sparkでのデータの取り扱いはパブリックプレビュー中であっても一般提供の製品と同様になります。これにより、より厳格なデータ要件を持つ組織が、他の一般提供製品と同様にSparkを活用できるようになります。詳細については、[プレビュー機能にDPAがどのように適用されるか](https://docs.github.com/site-policy/github-terms/github-dpa-previews)に関するドキュメントをお読みください。


## [Spark専用SKUと予算管理](#dedicated-sku-budget-controls-for-spark)


組織管理者は、請求ビューでSpark専用のSKUを確認できるようになりました。これは、管理者が請求ダッシュボードとCSVエクスポートで他のすべてのCopilot使用量とは別にSparkの支出を表示できることを意味します。また、Spark専用の詳細なプレミアムリクエスト予算と超過ポリシーを設定することもできます。管理者は、プレミアムリクエストを活用するすべての製品に対して、バンドルされたプレミアムリクエスト予算を設定するオプションもあります。これらはすべて、組織の**Billing and licensing**タブで管理できます。  

![請求ビューのSpark SKU](https://github.com/user-attachments/assets/c951537d-9d12-42d7-974c-8f85fff3fc8c)  

![サンプル詳細SKU予算設定](https://github.com/user-attachments/assets/5af97045-d435-486b-810e-f22a1c5e49fd)


## [生成されたアプリの視覚的品質の向上](#improved-visual-quality-of-generated-apps)


生成されたアプリの視覚的品質を向上させるために、Sparkエージェントに変更を実装しました。より独自性のあるデザインと、より高品質なUIおよびUXを持つアプリが表示されるようになります。以下の改善例をご覧ください:  

![改善前後に生成されたto\-doアプリの並列比較](https://github.com/user-attachments/assets/d1f76d73-ea17-4a04-be8d-e84fbd598f02)  

![改善前後に生成されたactionsアプリの並列比較](https://github.com/user-attachments/assets/c63be308-c281-47e2-8820-9f6720697362)  

![改善前後に生成されたtimerアプリの並列比較](https://github.com/user-attachments/assets/be8ede73-d3d4-4509-ba2e-45fe2c2c5f0f)


## [エージェントの改善](#agent-improvements)


* Sparkエージェントは、ユーザーによる以前の手動編集をより尊重し、ユーザーが行った手動変更を上書きしないようにします。
* また、利用可能なモデルのコンテキストウィンドウを超える非常に複雑なアプリの生成方法を改善し、非常に複雑なユースケースでもアプリを生成できるようにしました。


## [リポジトリ作成の組織管理者設定](#repository-creation-org-admin-setting)


組織管理者は、すべてのSparksのリポジトリ作成を個人ユーザーアカウントではなく組織に強制できるようになりました。この設定は**オフ**がデフォルトで、組織管理者がCopilot設定ページで有効にできます。  

![Sparkリポジトリ作成ルールの組織管理者設定](https://github.com/user-attachments/assets/7e69b3be-5fe9-440f-8c93-7b89f5f7cc4a)


## [その他の改善](#other-improvements)


* すべてのユーザーにとってSparkの構築と編集をさらにアクセスしやすくするための、多数のアクセシビリティの改善。
* エージェントによるすべてのコード生成が完了次第、アプリのライブプレビューを表示するようになり、できるだけ早くアプリと対話できるようになりました。
* Sparkの開発で使用される特定のカスタムドメインのテストパスを削除し、潜在的なセキュリティリスクを排除しました。
* UI、反復、公開、およびリポジトリ作成の問題につながる問題の複数のバグ修正。
* Sparkに対する手動コミットが失われないようにするための改善。
* エラーにつながるエージェントへの複数の同時リクエストの送信を防ぐためのSpark UIへの変更。


## [今日これらの改善を試す](#try-out-these-improvements-today)


次のアプリを構築するには、[github.com/spark](https://github.com/spark)にアクセスしてください。
