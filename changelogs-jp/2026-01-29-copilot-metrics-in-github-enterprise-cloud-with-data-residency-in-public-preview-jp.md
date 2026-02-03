---
title: "データレジデンシーを備えたGitHub Enterprise CloudでのCopilotメトリクスがパブリックプレビューに"
date: "2026-01-29"
type: "Release"
labels: ["copilot", "enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-29-copilot-metrics-in-github-enterprise-cloud-with-data-residency-in-public-preview"
fetched_at: "2026-02-03T14:50:49.270734Z"
lang: "ja"
---

# データレジデンシーを備えたGitHub Enterprise CloudでのCopilotメトリクスがパブリックプレビューに

## Overview
データレジデンシーがコンプライアンスと地域要件にとってどれほど重要かを理解しています。そのため、Copilotの使用、コード生成ダッシュボード、および対応するAPIが、データレジデンシーを備えたGitHub Enterprise Cloudの顧客に利用可能になりました。

## Detailed Explanation
### 概要
- データレジデンシーがコンプライアンスと地域要件にとってどれほど重要かを理解しています。そのため、Copilotの使用、コード生成ダッシュボード、および対応するAPIが、データレジデンシーを備えたGitHub Enterprise Cloudの顧客に利用可能になりました。

### 何が含まれていますか？
- データレジデンシーを備えたGitHub Enterprise Cloudの顧客は、次の情報を確認できるようになりました：
- Copilot使用ダッシュボード：チームがGitHub Copilotをどのように使用しているかについて、明確で実用的な洞察を得ます。ダッシュボードは、コード補完アクティビティ、IDE使用、生成されたコード行数などの可視性を提供します。
- コード生成ダッシュボード：補完、チャット、エージェント機能にわたって提案、追加、または削除された行を定量化することで、Copilotの出力を観察します。
- きめ細かい権限：View enterprise Copilot metricsエンタープライズロールが割り当てられている場合、APIとダッシュボードにアクセスできます。これは、エンタープライズ管理者や請求マネージャーだけでなく、このロールが割り当てられたすべてのユーザーが、エンタープライズの詳細なCopilot使用メトリクスを表示できることを意味します。
- 組織の使用：さまざまなCopilot機能の使用統計、ユーザーエンゲージメントデータ、機能採用メトリクスを含む、組織独自のCopilot採用と使用メトリクスにプログラムでアクセスします。詳細については、APIドキュメントをご覧ください。
- APIアクセス：カスタムレポート、監視、コンプライアンス、高度な分析のために、組織全体のCopilot使用データにプログラムでアクセスします。

### 可用性
- データレジデンシーを備えたGitHub Enterprise Cloudに移行する既存のGitHub Enterprise Cloud顧客の場合、使用データはエンタープライズ間で分割されることに注意してください。履歴使用は既存のエンタープライズに関連付けられたままであり、移行後の使用は、アカウント変更により新しいデータレジデンシーエンタープライズに帰属します。
- ユーザーがIDE内で複数のGitHubアカウントにログインしている場合、生成された使用はすべてデータレジデンシーを備えたGitHub Enterprise Cloudアカウントに帰属し、他のアカウント間で共有されません。
- ダッシュボードにアクセスするには、エンタープライズアカウント→「AI Controls」→「Copilot」→「Metrics」→「Copilot usage metrics」に移動します。その後、「Insights」→「Copilot usage」または「Code generation」の下にダッシュボードが表示されます。また、エンタープライズ管理者、請求マネージャーであるか、Copilotメトリクスへのアクセスを許可する適切なきめ細かい権限を持っていることを確認してください。
- APIアクセスについては、Copilot使用メトリクスAPIドキュメントをご覧ください。
- GitHubコミュニティ内のディスカッションに参加してください。

## Impact / Who’s Affected
- そのため、Copilotの使用、コード生成ダッシュボード、および対応するAPIが、データレジデンシーを備えたGitHub Enterprise Cloudの顧客に利用可能になりました。

## Caveats / Limitations
- データレジデンシーがコンプライアンスと地域要件にとってどれほど重要かを理解しています。
- 可用性 データレジデンシーを備えたGitHub Enterprise Cloudに移行する既存のGitHub Enterprise Cloud顧客の場合、使用データはエンタープライズ間で分割されることに注意してください。

## Insights (derived from article language)
- 可用性 データレジデンシーを備えたGitHub Enterprise Cloudに移行する既存のGitHub Enterprise Cloud顧客の場合、使用データはエンタープライズ間で分割されることに注意してください。
- その後、「Insights」→「Copilot usage」または「Code generation」の下にダッシュボードが表示されます。

## Article Content (cleaned)
データレジデンシーがコンプライアンスと地域要件にとってどれほど重要かを理解しています。そのため、Copilotの使用、コード生成ダッシュボード、および対応するAPIが、データレジデンシーを備えたGitHub Enterprise Cloudの顧客に利用可能になりました。


### [What's included?](https://github.blog/changelog/feed/#whats-included)


データレジデンシーを備えたGitHub Enterprise Cloudの顧客は、次の情報を確認できるようになりました：


* **Copilot使用ダッシュボード**：チームがGitHub Copilotをどのように使用しているかについて、明確で実用的な洞察を得ます。ダッシュボードは、コード補完アクティビティ、IDE使用、生成されたコード行数などの可視性を提供します。
* **コード生成ダッシュボード**：補完、チャット、エージェント機能にわたって提案、追加、または削除された行を定量化することで、Copilotの出力を観察します。
* **きめ細かい権限**：`View enterprise Copilot metrics`エンタープライズロールが割り当てられている場合、APIとダッシュボードにアクセスできます。これは、エンタープライズ管理者や請求マネージャーだけでなく、このロールが割り当てられたすべてのユーザーが、エンタープライズの詳細なCopilot使用メトリクスを表示できることを意味します。
* **組織の使用**：さまざまなCopilot機能の使用統計、ユーザーエンゲージメントデータ、機能採用メトリクスを含む、組織独自のCopilot採用と使用メトリクスにプログラムでアクセスします。詳細については、[APIドキュメント](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics?apiVersion=2022-11-28#get-copilot-organization-usage-metrics-for-a-specific-day)をご覧ください。
* **APIアクセス**：カスタムレポート、監視、コンプライアンス、高度な分析のために、組織全体のCopilot使用データにプログラムでアクセスします。


### [Availability](https://github.blog/changelog/feed/#availability)


* データレジデンシーを備えたGitHub Enterprise Cloudに移行する既存のGitHub Enterprise Cloud顧客の場合、使用データはエンタープライズ間で分割されることに注意してください。履歴使用は既存のエンタープライズに関連付けられたままであり、移行後の使用は、アカウント変更により新しいデータレジデンシーエンタープライズに帰属します。
* ユーザーがIDE内で複数のGitHubアカウントにログインしている場合、生成された使用はすべてデータレジデンシーを備えたGitHub Enterprise Cloudアカウントに帰属し、他のアカウント間で共有されません。
* ダッシュボードにアクセスするには、エンタープライズアカウント→「AI Controls」→「Copilot」→「Metrics」→「Copilot usage metrics」に移動します。その後、「Insights」→「Copilot usage」または「Code generation」の下にダッシュボードが表示されます。また、エンタープライズ管理者、請求マネージャーであるか、Copilotメトリクスへのアクセスを許可する適切なきめ細かい権限を持っていることを確認してください。
* APIアクセスについては、[Copilot使用メトリクスAPIドキュメント](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics?apiVersion=2022-11-28)をご覧ください。


[GitHubコミュニティ](https://github.com/orgs/community/discussions/185365)内のディスカッションに参加してください。
