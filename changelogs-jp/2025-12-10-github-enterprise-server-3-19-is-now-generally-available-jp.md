---
title: "GitHub Enterprise Server 3.19が一般提供開始"
date: "2025-12-10"
type: "new releases"
labels: ["collaboration tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-10-github-enterprise-server-3-19-is-now-generally-available"
fetched_at: "2026-02-03T14:50:54.998820Z"
lang: "ja"
---

# GitHub Enterprise Server 3.19が一般提供開始

## Overview
GitHub Enterprise Server (GHES) 3.19は、デプロイメントの効率性、監視機能、コードセキュリティ、およびポリシー管理を強化します。3.19リリースのハイライトは次のとおりです:

## Detailed Explanation
### 概要
- GitHub Enterprise Server (GHES) 3.19は、デプロイメントの効率性、監視機能、コードセキュリティ、およびポリシー管理を強化します。3.19リリースのハイライトは次のとおりです:
- リポジトリ作成のための改善されたより直感的なフローが利用可能になりました。新しいフォームは、リポジトリメタデータの収集、カスタムプロパティの適用、および作成時のリポジトリポリシーの適用のための最新のインターフェースを提供します。これにより、エンタープライズ全体で一貫したリポジトリ構成が保証されます。このアップデートの詳細については、[改善されたリポジトリ作成エクスペリエンス](https://github.blog/changelog/2025-08-26-improved-repository-creation-generally-available-plus-ruleset-insights-improvements/)をお読みください。
- エンタープライズ管理者は、ルールセット履歴、インポート、エクスポートの一般提供により、ルールをより効率的に管理できます。ルールセット履歴により変更の追跡とロールバックが可能になり、インポートとエクスポートによりGitHubの[ruleset-recipesリポジトリ](https://github.com/github/ruleset-recipes)のものを含むルールセットの共有と再利用が簡素化されます。詳細については、[ルールセットの管理に関するドキュメント](https://docs.github.com/enterprise-server@3.19/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository)をお読みください。
- 管理者は、ワークフローがパブリックリポジトリのアクションを使用する際に特定のアクションをブロックし、SHAベースのピン留めを要求するポリシーを適用できます。これらのポリシーは、承認されたアクションのみが使用され、不変のSHAによって参照されることを保証することにより、ワークフローのセキュリティを向上させるのに役立ちます。詳細については、[ブロッキングとSHAピン留めアクション](https://github.blog/changelog/2025-08-15-github-actions-policy-now-supports-blocking-and-sha-pinning-actions/)をお読みください。
- エンタープライズが所有するGitHub Appsのアプリケーションマネージャーとしてユーザーを指定できるようになりました。アプリマネージャーはアプリケーション登録を更新できますが、アプリケーションのインストールは管理できません。また、アプリマネージャー機能をロールプラットフォームを使用するように拡張しました。これにより、組織チームが個々の組織所有アプリのアプリマネージャーとして割り当てられ、新しい組織アプリマネージャーロールをチームとユーザーに割り当てることができ、組織が所有するすべてのアプリへのアクセスが提供されます。詳細については、[GitHub App Managers](https://docs.github.com/enterprise-server@3.19/apps/maintaining-github-apps/about-github-app-managers)をご覧ください。
- バージョン3.19以降、GHESの新規インストールではOpenTelemetryメトリクスが有効になり、Collectdメトリクスがデフォルトで無効になります。必要に応じて2つの間で切り替えることができます。アップグレードされたインスタンスは現在の設定を保持します。今後2〜3リリースで、OpenTelemetryメトリクスが唯一サポートされるメトリクスになります。詳細については、[OpenTelemetryメトリクス](https://docs.github.com/enterprise-server@3.19/admin/monitoring-and-managing-your-instance/monitoring-your-instance/opentelemetry-metrics)をお読みください。
- より柔軟性と制御性を高めるためにSSHおよびTLS暗号を設定できるようになり、弱い暗号を回避する機能も含まれます。デフォルトの暗号をリストし、使用する暗号を選択できます。詳細については、[暗号スイートと暗号化アルゴリズムの設定](https://docs.github.com/enterprise-server@3.19/admin/configuring-settings/hardening-security-for-your-enterprise/configuring-tls-and-ssh-ciphers)をお読みください。
- GHES 3.19の詳細については、[リリースノート](https://docs.github.com/enterprise-server@3.19/admin/release-notes)をご確認いただくか、今すぐ[ダウンロード](https://enterprise.github.com/releases/3.19.0/download)してください。バージョン3.19へのアップグレードまたはこれらの新機能の使用で問題が発生した場合は、[サポートチーム](https://support.github.com/features/enterprise-administrators-server)にお問い合わせください。
- フィードバックを共有し、質問するには、[コミュニティディスカッション](https://github.com/orgs/community/discussions/181173)にご参加ください。

## Impact / Who's Affected
- 3.19リリースのハイライトは次のとおりです: リポジトリ作成のための改善されたより直感的なフローが利用可能になりました。
- これらのポリシーは、承認されたアクションのみが使用され、不変のSHAによって参照されることを保証することにより、ワークフローのセキュリティを向上させるのに役立ちます。
- 今後2〜3リリースで、OpenTelemetryメトリクスが唯一サポートされるメトリクスになります。

## Caveats / Limitations
- これらのポリシーは、承認されたアクションのみが使用され、不変のSHAによって参照されることを保証することにより、ワークフローのセキュリティを向上させるのに役立ちます。
- 今後2〜3リリースで、OpenTelemetryメトリクスが唯一サポートされるメトリクスになります。
- GHES 3.19の詳細については、リリースノートをご確認いただくか、今すぐダウンロードしてください。

## Insights (derived from article language)
- GHES 3.19の詳細については、リリースノートをご確認いただくか、今すぐダウンロードしてください。

## Article Content (cleaned)
GitHub Enterprise Server (GHES) 3\.19は、デプロイメントの効率性、監視機能、コードセキュリティ、およびポリシー管理を強化します。3\.19リリースのハイライトは次のとおりです:


* リポジトリ作成のための改善されたより直感的なフローが利用可能になりました。新しいフォームは、リポジトリメタデータの収集、カスタムプロパティの適用、および作成時のリポジトリポリシーの適用のための最新のインターフェースを提供します。これにより、エンタープライズ全体で一貫したリポジトリ構成が保証されます。このアップデートの詳細については、[改善されたリポジトリ作成エクスペリエンス](https://github.blog/changelog/2025-08-26-improved-repository-creation-generally-available-plus-ruleset-insights-improvements/)をお読みください。
* エンタープライズ管理者は、ルールセット履歴、インポート、エクスポートの一般提供により、ルールをより効率的に管理できます。ルールセット履歴により変更の追跡とロールバックが可能になり、インポートとエクスポートによりGitHubの[ruleset\-recipesリポジトリ](https://github.com/github/ruleset-recipes)のものを含むルールセットの共有と再利用が簡素化されます。詳細については、[ルールセットの管理に関するドキュメント](https://docs.github.com/enterprise-server@3.19/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository)をお読みください。
* 管理者は、ワークフローがパブリックリポジトリのアクションを使用する際に特定のアクションをブロックし、SHAベースのピン留めを要求するポリシーを適用できます。これらのポリシーは、承認されたアクションのみが使用され、不変のSHAによって参照されることを保証することにより、ワークフローのセキュリティを向上させるのに役立ちます。詳細については、[ブロッキングとSHAピン留めアクション](https://github.blog/changelog/2025-08-15-github-actions-policy-now-supports-blocking-and-sha-pinning-actions/)をお読みください。
* エンタープライズが所有するGitHub Appsのアプリケーションマネージャーとしてユーザーを指定できるようになりました。アプリマネージャーはアプリケーション登録を更新できますが、アプリケーションのインストールは管理できません。また、アプリマネージャー機能をロールプラットフォームを使用するように拡張しました。これにより、組織チームが個々の組織所有アプリのアプリマネージャーとして割り当てられ、新しい組織アプリマネージャーロールをチームとユーザーに割り当てることができ、組織が所有するすべてのアプリへのアクセスが提供されます。詳細については、[GitHub App Managers](https://docs.github.com/enterprise-server@3.19/apps/maintaining-github-apps/about-github-app-managers)をご覧ください。
* バージョン3\.19以降、GHESの新規インストールではOpenTelemetryメトリクスが有効になり、Collectdメトリクスがデフォルトで無効になります。必要に応じて2つの間で切り替えることができます。アップグレードされたインスタンスは現在の設定を保持します。今後2〜3リリースで、OpenTelemetryメトリクスが唯一サポートされるメトリクスになります。詳細については、[OpenTelemetryメトリクス](https://docs.github.com/enterprise-server@3.19/admin/monitoring-and-managing-your-instance/monitoring-your-instance/opentelemetry-metrics)をお読みください。
* より柔軟性と制御性を高めるためにSSHおよびTLS暗号を設定できるようになり、弱い暗号を回避する機能も含まれます。デフォルトの暗号をリストし、使用する暗号を選択できます。詳細については、[暗号スイートと暗号化アルゴリズムの設定](https://docs.github.com/enterprise-server@3.19/admin/configuring-settings/hardening-security-for-your-enterprise/configuring-tls-and-ssh-ciphers)をお読みください。


GHES 3\.19の詳細については、[リリースノート](https://docs.github.com/enterprise-server@3.19/admin/release-notes)をご確認いただくか、今すぐ[ダウンロード](https://enterprise.github.com/releases/3.19.0/download)してください。バージョン3\.19へのアップグレードまたはこれらの新機能の使用で問題が発生した場合は、[サポートチーム](https://support.github.com/features/enterprise-administrators-server)にお問い合わせください。


フィードバックを共有し、質問するには、[コミュニティディスカッション](https://github.com/orgs/community/discussions/181173)にご参加ください。
