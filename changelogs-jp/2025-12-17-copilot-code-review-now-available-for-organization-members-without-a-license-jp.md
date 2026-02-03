---
title: "Copilotコードレビューがライセンスのない組織メンバーに利用可能に"
date: "2025-12-17"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-17-copilot-code-review-now-available-for-organization-members-without-a-license"
fetched_at: "2026-02-03T14:50:54.885119Z"
lang: "ja"
---

# Copilotコードレビューがライセンスのない組織メンバーに利用可能に

## Overview
組織は、Copilotライセンスを持たない貢献者からのプルリクエストを含む、すべてのプルリクエストにCopilotコードレビューを適用できるようになりました。使用量はプレミアムリクエストとして組織にシームレスに請求され、ライセンス管理は不要です。これにより、エンタープライズとオープンソースメンテナーは、すべてのプルリクエストで一貫したCopilot駆動の詳細な分析により、より広範なカバレッジと信頼性を得られます。

## Detailed Explanation
### Overview
- 組織は、Copilotライセンスを持たない貢献者からのプルリクエストを含む、すべてのプルリクエストにCopilotコードレビューを適用できるようになりました。使用量はプレミアムリクエストとして組織にシームレスに請求され、ライセンス管理は不要です。これにより、エンタープライズとオープンソースメンテナーは、すべてのプルリクエストで一貫したCopilot駆動の詳細な分析により、より広範なカバレッジと信頼性を得られます。
- 編集者注（2025年12月19日）：機能が完全に利用可能になったため、段階的なロールアウトに関する文を削除しました。

### Standardize code review across your organization
- 優れたソフトウェアを構築することはチームの努力であり、コアチームと共に働く多くの貢献者が関与します。すべての貢献者に完全なCopilotライセンスが必要なわけではありませんが、すべての人のプルリクエストはCopilotコードレビューから恩恵を受けることができます。
- 以前は、ライセンスを持つユーザーのみがCopilotコードレビューの提案を受け取りました。このリリースにより、貢献者がライセンスを持っているかどうかに関係なく、組織のリポジトリ内のすべてのプルリクエストにCopilotコードレビューを拡張できます。ライセンスのない貢献者のプルリクエストのレビューはプレミアムリクエストとして組織に請求され、ライセンスユーザーはエクスペリエンスに変更なく毎月のプレミアムリクエストの割り当てを引き続き使用します。
- 主な利点：
- 包括的なカバレッジ：リポジトリ全体で一貫したCopilot駆動の詳細な分析を適用します。
- シームレスな課金：追加のCopilotシートやセットアップを管理せずに、ライセンスのないユーザーが消費したプレミアムリクエストに対して支払います。
- エンタープライズグレードのコントロール：この機能には明示的なオプトインが必要で、組織全体のコードレビューポリシーを管理し続けることができます。

### Getting started
- 組織またはオープンソースプロジェクトのすべての（ライセンスありおよびライセンスなし）メンバーからのプルリクエストでCopilotコードレビューを有効にするには、エンタープライズ/組織管理者は最初にCopilotを有効にし、次に2つのポリシーにオプトインする必要があります：
- プレミアムリクエストの有料使用を有効にして、組織内の誰でもCopilotコードレビューにプレミアムリクエストを使用できるようにします。
- Copilotコードレビューポリシーを有効にし、トグルライセンスのないメンバーがgithub.comでCopilotコードレビューを使用することを許可をオンにします。
- Copilotコードレビューポリシーを有効にし、トグルライセンスのないメンバーがgithub.comでCopilotコードレビューを使用することを許可をオンにします。

### Monitor usage and manage costs
- アカウントのBilling & Licensingページのプレミアムリクエスト分析ダッシュボードで、プレミアムリクエストの消費と料金を追跡できます。Copilotコードレビューの使用をフィルタリングし、ユーザーごとにグループ化して、ライセンスありとライセンスなしの使用状況を確認できます。ライセンスのないメンバーからのCopilotコードレビューの使用は、組織に直接請求されるため、含まれる割り当てが関連付けられません。
- また、この機能を有効にする際に、予測可能な支出を確保し、予期しない料金を回避するために、プレミアムリクエスト予算を設定することを強くお勧めします。
- 詳細については、Copilotコードレビューのドキュメントをご覧ください。GitHub Communityでディスカッションに参加してください。

## Impact / Who's Affected
- 以前は、ライセンスを持つユーザーのみがCopilotコードレビューの提案を受け取りました。
- エンタープライズグレードのコントロール：この機能には明示的なオプトインが必要で、組織全体のコードレビューポリシーを管理し続けることができます。

## Caveats / Limitations
- 編集者注（2025年12月19日）：機能が完全に利用可能になったため、段階的なロールアウトに関する文を削除しました。
- 以前は、ライセンスを持つユーザーのみがCopilotコードレビューの提案を受け取りました。
- エンタープライズグレードのコントロール：この機能には明示的なオプトインが必要で、組織全体のコードレビューポリシーを管理し続けることができます。

## Insights (derived from article language)
- エンタープライズグレードのコントロール：この機能には明示的なオプトインが必要で、組織全体のコードレビューポリシーを管理し続けることができます。
- 詳細については、Copilotコードレビューのドキュメントをご覧ください。

## Article Content (cleaned)
組織は、[Copilotライセンスを持たない貢献者からのプルリクエストを含む、すべてのプルリクエストにCopilotコードレビューを適用](https://docs.github.com/enterprise-cloud@latest/copilot/concepts/agents/code-review)できるようになりました。使用量はプレミアムリクエストとして組織にシームレスに請求され、ライセンス管理は不要です。これにより、エンタープライズとオープンソースメンテナーは、すべてのプルリクエストで一貫したCopilot駆動の詳細な分析により、より広範なカバレッジと信頼性を得られます。


*編集者注（2025年12月19日\)：機能が完全に利用可能になったため、段階的なロールアウトに関する文を削除しました。*


## [Standardize code review across your organization](#standardize-code-review-across-your-organization)


優れたソフトウェアを構築することはチームの努力であり、コアチームと共に働く多くの貢献者が関与します。すべての貢献者に完全なCopilotライセンスが必要なわけではありませんが、すべての人のプルリクエストはCopilotコードレビューから恩恵を受けることができます。


以前は、ライセンスを持つユーザーのみがCopilotコードレビューの提案を受け取りました。このリリースにより、貢献者がライセンスを持っているかどうかに関係なく、組織のリポジトリ内のすべてのプルリクエストにCopilotコードレビューを拡張できます。ライセンスのない貢献者のプルリクエストのレビューはプレミアムリクエストとして組織に請求され、ライセンスユーザーはエクスペリエンスに変更なく毎月のプレミアムリクエストの割り当てを引き続き使用します。


**主な利点：**


* 包括的なカバレッジ：リポジトリ全体で一貫したCopilot駆動の詳細な分析を適用します。
* シームレスな課金：追加のCopilotシートやセットアップを管理せずに、ライセンスのないユーザーが消費したプレミアムリクエストに対して支払います。
* エンタープライズグレードのコントロール：この機能には明示的なオプトインが必要で、組織全体のコードレビューポリシーを管理し続けることができます。


## [Getting started](#getting-started)


組織またはオープンソースプロジェクトのすべての（ライセンスありおよびライセンスなし）メンバーからのプルリクエストでCopilotコードレビューを有効にするには、エンタープライズ/組織管理者は最初にCopilotを有効にし、次に2つのポリシーにオプトインする必要があります：


1. [**プレミアムリクエストの有料使用**](https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/manage-and-track-spending/manage-request-allowances#setting-a-policy-for-paid-usage)を有効にして、組織内の誰でもCopilotコードレビューにプレミアムリクエストを使用できるようにします。
![Screen shot of the policy setting to allow the enterprise to pay for premium requests beyond the included usage](https://github.com/user-attachments/assets/1cdba29d-09b2-4795-a2e1-c15c4d603f32)
2. **Copilotコードレビュー**ポリシーを有効にし、トグル[**ライセンスのないメンバーがgithub.comでCopilotコードレビューを使用することを許可**](https://docs.github.com/enterprise-cloud@latest/copilot/concepts/agents/code-review)をオンにします。


![Screen shot of the new policy setting to allow organization members without Copilot license to use Copilot code review in github.com](https://github.com/user-attachments/assets/a3e6b355-e525-49a9-869a-44e4fb594a1c)


## [Monitor usage and manage costs](#monitor-usage-and-manage-costs)


アカウントのBilling \& Licensingページの[プレミアムリクエスト分析ダッシュボード](https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/manage-and-track-spending/monitor-premium-requests#viewing-detailed-analytics-of-your-usage)で、プレミアムリクエストの消費と料金を追跡できます。Copilotコードレビューの使用をフィルタリングし、ユーザーごとにグループ化して、ライセンスありとライセンスなしの使用状況を確認できます。ライセンスのないメンバーからのCopilotコードレビューの使用は、組織に直接請求されるため、含まれる割り当てが関連付けられません。


また、この機能を有効にする際に、予測可能な支出を確保し、予期しない料金を回避するために、[プレミアムリクエスト予算を設定](https://docs.github.com/enterprise-cloud@latest/billing/tutorials/set-up-budgets)することを強くお勧めします。


詳細については、[Copilotコードレビューのドキュメント](https://docs.github.com/enterprise-cloud@latest/copilot/concepts/agents/code-review)をご覧ください。[GitHub Community](https://github.com/orgs/community/discussions/178962)でディスカッションに参加してください。
