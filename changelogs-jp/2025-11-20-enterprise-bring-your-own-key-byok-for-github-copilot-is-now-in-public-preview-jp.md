---
title: "GitHub Copilotのエンタープライズ向けBring Your Own Key（BYOK）がパブリックプレビューになりました"
date: "2025-11-20"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-20-enterprise-bring-your-own-key-byok-for-github-copilot-is-now-in-public-preview"
fetched_at: "2026-02-03T14:50:55.168998Z"
lang: "ja"
---

# GitHub Copilotのエンタープライズ向けBring Your Own Key（BYOK）がパブリックプレビューになりました

## Overview
エンタープライズ開発者は、Copilotの使用方法においてより柔軟性を求めてきました。多くのチームはすでに特定の大規模言語モデル（LLM）プロバイダーと協力しており、ニーズに合わせてカスタマイズされたモデルを維持しています。Copilotは長い間、デフォルトで高品質のGitHubホステッドモデルを提供してきましたが、これまでチームは組織が優先するモデルを直接接続することができませんでした。

## Detailed Explanation
### Overview
- エンタープライズ開発者は、Copilotの使用方法においてより柔軟性を求めてきました。多くのチームはすでに特定の大規模言語モデル（LLM）プロバイダーと協力しており、ニーズに合わせてカスタマイズされたモデルを維持しています。Copilotは長い間、デフォルトで高品質のGitHubホステッドモデルを提供してきましたが、これまでチームは組織が優先するモデルを直接接続することができませんでした。
- Bring Your Own Key（BYOK）により、Anthropic、Microsoft Foundry、OpenAI、xAIなどのサポートされているプロバイダーからのAPIキーをGitHub Copilotに接続することが可能になりました。接続すると、そのキーに関連付けられているすべてのモデルをGitHub.comおよびサポートされているIDEのCopilot Chatで使用できます。BYOKを介した使用は、選択したプロバイダーによって直接請求され、GitHub Copilotリクエストクォータにはカウントされません。これにより、チームは既存の契約やクレジットを活用しながら、組織またはエンタープライズレベルでアクセスを管理できます。

### Here's what's new
- CopilotにプロバイダーのAPIキーを接続 エンタープライズ管理者はエンタープライズレベルでAPIキーを追加でき、組織管理者は組織レベルでキーを追加できます。キーを接続すると、リンクされたプロバイダーからモデルを選択してGitHub Copilotで使用できます。
- モデルを一元管理 接続されたキーを介してモデルが利用可能になると、エンタープライズ管理者はエンタープライズ内のどの組織がそれらを使用できるかを決定します。組織管理者は、組織内でアクセスを構成します。エンタープライズ管理者と組織管理者の両方が、単一の設定エリアからモデルを有効化、無効化、構成できます。この一元化されたコントロールにより、一貫したセットアップが保証され、チームはニーズの変化に応じて迅速に適応できます。
- サポートされているIDEでBYOKモデルを使用 BYOKは、Visual Studio Code、JetBrains IDE、Eclipse、Xcodeの最新リリースのAgent、Plan、Ask、EditモードでAvailableです。
- プロバイダーによる請求処理 BYOKを介して行われたAPI呼び出しは、プロバイダーの条件に従って請求され、GitHub Copilotの使用クォータにはカウントされません。既存のクレジットまたはプロバイダーとのエンタープライズ契約を使用できます。

### Known limitation
- BYOKはOpenAI Responses APIをサポートしていません。Responsesエンドポイントを使用するように構成されたモデルは機能しません。BYOKにはOpenAI Completions APIが必要です。

### Start using BYOK today
- BYOKは現在、GitHub EnterpriseおよびBusinessの顧客向けにパブリックプレビューで利用可能です。エンタープライズまたは組織の設定でLLMプロバイダーのAPIキーを接続し、Copilot ChatおよびサポートされているIDEでモデルの使用を開始してください。詳細については、ドキュメントをご覧ください。

### Help us shape the future
- 私たちは始まったばかりであり、皆様のフィードバックが次に何をするかを導くのに役立ちます。GitHub Communityのディスカッションに参加して、フィードバックを共有し、他の開発者とつながりましょう。

## Impact / Who's Affected
- BYOKにはOpenAI Completions APIが必要です。
- 今すぐBYOKの使用を開始 BYOKは現在、GitHub EnterpriseおよびBusinessの顧客向けにパブリックプレビューで利用可能です。

## Caveats / Limitations
- BYOKにはOpenAI Completions APIが必要です。

## Insights (derived from article language)
- BYOKにはOpenAI Completions APIが必要です。
- 詳細については、ドキュメントをご覧ください。

## Article Content (cleaned)
エンタープライズ開発者は、Copilotの使用方法においてより柔軟性を求めてきました。多くのチームはすでに特定の大規模言語モデル（LLM）プロバイダーと協力しており、ニーズに合わせてカスタマイズされたモデルを維持しています。Copilotは長い間、デフォルトで高品質のGitHubホステッドモデルを提供してきましたが、これまでチームは組織が優先するモデルを直接接続することができませんでした。


Bring Your Own Key（BYOK）により、Anthropic、Microsoft Foundry、OpenAI、xAIなどのサポートされているプロバイダーからのAPIキーをGitHub Copilotに接続することが可能になりました。接続すると、そのキーに関連付けられているすべてのモデルをGitHub.comおよびサポートされているIDEのCopilot Chatで使用できます。BYOKを介した使用は、選択したプロバイダーによって直接請求され、GitHub Copilotリクエストクォータにはカウントされません。これにより、チームは既存の契約やクレジットを活用しながら、組織またはエンタープライズレベルでアクセスを管理できます。



### [Here's what's new](#heres-whats-new)


**CopilotにプロバイダーのAPIキーを接続**  

エンタープライズ管理者はエンタープライズレベルでAPIキーを追加でき、組織管理者は組織レベルでキーを追加できます。キーを接続すると、リンクされたプロバイダーからモデルを選択してGitHub Copilotで使用できます。


**モデルを一元管理**  

接続されたキーを介してモデルが利用可能になると、エンタープライズ管理者はエンタープライズ内のどの組織がそれらを使用できるかを決定します。組織管理者は、組織内でアクセスを構成します。エンタープライズ管理者と組織管理者の両方が、単一の設定エリアからモデルを有効化、無効化、構成できます。この一元化されたコントロールにより、一貫したセットアップが保証され、チームはニーズの変化に応じて迅速に適応できます。


**サポートされているIDEでBYOKモデルを使用**  

BYOKは、Visual Studio Code、JetBrains IDE、Eclipse、Xcodeの最新リリースのAgent、Plan、Ask、EditモードでAvailableです。


**プロバイダーによる請求処理**  

BYOKを介して行われたAPI呼び出しは、プロバイダーの条件に従って請求され、GitHub Copilotの使用クォータにはカウントされません。既存のクレジットまたはプロバイダーとのエンタープライズ契約を使用できます。


### [Known limitation](#known-limitation)


BYOKはOpenAI [Responses API](https://platform.openai.com/docs/api-reference/responses)をサポートしていません。Responsesエンドポイントを使用するように構成されたモデルは機能しません。BYOKにはOpenAI Completions APIが必要です。


### [Start using BYOK today](#start-using-byok-today)


BYOKは現在、GitHub EnterpriseおよびBusinessの顧客向けにパブリックプレビューで利用可能です。エンタープライズまたは組織の設定でLLMプロバイダーのAPIキーを接続し、Copilot ChatおよびサポートされているIDEでモデルの使用を開始してください。詳細については、[ドキュメント](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-your-own-api-keys)をご覧ください。


### [Help us shape the future](#help-us-shape-the-future)


私たちは始まったばかりであり、皆様のフィードバックが次に何をするかを導くのに役立ちます。[GitHub Community](https://github.com/orgs/community/discussions/179954)のディスカッションに参加して、フィードバックを共有し、他の開発者とつながりましょう。
