---
title: "エンタープライズのメンバーに AI コントロール管理を委任する"
date: "2025-11-03"
type: "new releases"
labels: ["copilot", "enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-03-delegate-ai-controls-management-to-members-of-your-enterprise"
fetched_at: "2026-02-03T14:50:55.472602Z"
lang: "ja"
---

# エンタープライズのメンバーに AI コントロール管理を委任する

## Overview
エンタープライズオーナーは、AI および Copilot ポリシーとセットアップ管理をエンタープライズメンバーおよびチームに委任できるようになりました。広範なエンタープライズ所有権を付与することなく、これを実行できるようになりました。これらの新しい細かい権限（FGP）は、エンタープライズアカウントのエージェントコントロールプレーンへの読み取りまたは書き込みアクセスを付与できます。

## Detailed Explanation
### Overview
- エンタープライズオーナーは、AI および Copilot ポリシーとセットアップ管理をエンタープライズメンバーおよびチームに委任できるようになりました。広範なエンタープライズ所有権を付与することなく、これを実行できるようになりました。これらの新しい細かい権限（FGP）は、エンタープライズアカウントのエージェントコントロールプレーンへの読み取りまたは書き込みアクセスを付与できます。
- Universe 2025 で、エージェントコントロールプレーンのパブリックプレビューを発表しました。これは、エンタープライズがビジネス全体で Copilot 機能、カスタムエージェント、MCP 構成の使用をより深くコントロールし、監査する能力を高めるように設計されたガバナンス機能のスイートです。
- エンタープライズオーナーは、以下の FGP のいずれかを使用して新しいエンタープライズカスタムロールを作成することで、エージェントコントロールプレーンの機能の管理を委任できるようになりました：
- View enterprise AI controls：エンタープライズの「AI Controls」タブのすべての設定を表示する権限をロールに付与します。
- Manage enterprise AI controls：エンタープライズの「AI Controls」タブのすべての設定を管理する権限をロールに付与します。
- 注：上記の FGP は、対応する FGP がカスタムロールにも追加されない限り、アクセス管理、監査ログ、ルールセットなどの「AI Controls」タブ内のディープリンクへのアクセスを付与しません。たとえば、エンタープライズオーナーは、カスタムロールがエンタープライズの監査ログイベントを表示できるようにするために、Read enterprise audit logs FGP を明示的に追加する必要があります。これにより、AI マネージャーはエージェント活動を監視できます。
- 上記の FGP を持つエンタープライズロールは、個々のメンバーまたはエンタープライズチームに割り当てることができ、規模での AI 管理を実現できます。
- 詳細については、エンタープライズで AI マネージャーを確立する方法に関するドキュメントをご覧ください。
- GitHub Community でディスカッションに参加してください。

## Impact / Who’s Affected
- Universe 2025 で、エージェントコントロールプレーンのパブリックプレビューを発表しました。

## Caveats / Limitations
- 注：上記の FGP は、対応する FGP がカスタムロールにも追加されない限り、アクセス管理、監査ログ、ルールセットなどの「AI Controls」タブ内のディープリンクへのアクセスを付与しません。

## Insights (derived from article language)
- 詳細については、エンタープライズで AI マネージャーを確立する方法に関するドキュメントをご覧ください。

## Article Content (cleaned)
エンタープライズオーナーは、AI および Copilot ポリシーとセットアップ管理をエンタープライズメンバーおよびチームに委任できるようになりました。広範なエンタープライズ所有権を付与することなく、これを実行できるようになりました。これらの新しい細かい権限（FGP）は、エンタープライズアカウントのエージェントコントロールプレーンへの読み取りまたは書き込みアクセスを付与できます。


Universe 2025 で、[エージェントコントロールプレーンのパブリックプレビュー](https://github.blog/changelog/2025-10-28-enterprise-ai-controls-the-agent-control-plane-are-in-public-preview/)を発表しました。これは、エンタープライズがビジネス全体で Copilot 機能、カスタムエージェント、MCP 構成の使用をより深くコントロールし、監査する能力を高めるように設計されたガバナンス機能のスイートです。


エンタープライズオーナーは、以下の FGP のいずれかを使用して新しいエンタープライズカスタムロールを作成することで、エージェントコントロールプレーンの機能の管理を委任できるようになりました：


* **View enterprise AI controls**：エンタープライズの **AI Controls** タブのすべての設定を表示する権限をロールに付与します。
* **Manage enterprise AI controls**：エンタープライズの **AI Controls** タブのすべての設定を管理する権限をロールに付与します。


**注**：上記の FGP は、対応する FGP がカスタムロールにも追加されない限り、アクセス管理、監査ログ、ルールセットなどの **AI Controls** タブ内のディープリンクへのアクセスを付与しません。  

たとえば、エンタープライズオーナーは、カスタムロールがエンタープライズの監査ログイベントを表示できるようにするために、**Read enterprise audit logs** FGP を明示的に追加する必要があります。これにより、AI マネージャーはエージェント活動を監視できます。


上記の FGP を持つエンタープライズロールは、個々のメンバーまたはエンタープライズチームに割り当てることができ、規模での AI 管理を実現できます。


詳細については、[エンタープライズで AI マネージャーを確立する](https://docs.github.com/copilot/tutorials/roll-out-at-scale/establish-ai-managers)方法に関するドキュメントをご覧ください。


[GitHub Community](https://github.com/orgs/community/discussions/178247?utm_source=changelog-community-enterprise-controls&utm_medium=changelog&utm_campaign=universe25) でディスカッションに参加してください。
