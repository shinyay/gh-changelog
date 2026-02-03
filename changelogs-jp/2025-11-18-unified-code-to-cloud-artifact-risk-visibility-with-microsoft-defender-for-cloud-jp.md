---
title: "Microsoft Defender for Cloudとの統合コードからクラウドへのアーティファクトリスク可視化がパブリックプレビューになりました"
date: "2025-11-18"
type: "new releases"
labels: ["application security", "supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-18-unified-code-to-cloud-artifact-risk-visibility-with-microsoft-defender-for-cloud-now-in-public-preview"
fetched_at: "2026-02-03T14:50:55.220489Z"
lang: "ja"
---

# Microsoft Defender for Cloudとの統合コードからクラウドへのアーティファクトリスク可視化がパブリックプレビューになりました

## Overview
GitHubは、コード、ビルドアーティファクト、本番環境のコンテキストを接続することで、チームが重要なセキュリティリスクを追跡、優先順位付け、修復することをより簡単にしました。以下は、提供された新機能とその使用方法です：

## Detailed Explanation
### Overview
- GitHubは、コード、ビルドアーティファクト、本番環境のコンテキストを接続することで、チームが重要なセキュリティリスクを追跡、優先順位付け、修復することをより簡単にしました。以下は、提供された新機能とその使用方法です：

### Linked artifacts with full traceability
- GitHub Actions経由でビルドされたアーティファクトは、Azure Container RegistryやJFrog Artifactoryなどの外部レジストリに最終的に保存される場合でも、GitHub内に「リンクされたアーティファクト」として表示されるようになりました。各リンクされたアーティファクトについて、GitHubは新しいメタデータを表示します：どのリポジトリがアーティファクトをビルドしたか、どのパッケージレジストリにアーティファクトが保存されているか、どこにデプロイされたかが表示されます。すべての証明されたアーティファクトは、ソースコードリポジトリに自動的にマッピングされるため、すべてのアーティファクトをその起源まで追跡できます。これは、ストレージとデプロイメント記録のための新しいArtifact Metadata APIによって実現されており、CI/CDワークフローや外部システムがプログラム的にデータをGitHubに送信し、リンクビューを最新の状態に保つことができます。

### Runtime risk context in partnership with Microsoft Defender for Cloud
- GitHubは、アーティファクトのランタイムリスクを表示するようになりました。これには、インターネットに公開されているか、本番環境で機密データを処理しているかなどが含まれます。このコンテキストは、Microsoft Defender for Cloudによってネイティブに提供されており、Deployment Record APIのネイティブ実装を含むため、ワークフローの変更を必要とせずにデプロイメント記録とランタイムリスク属性を自動的に入力します。これにより、セキュリティチームと開発チームの両方が、ビルドアーティファクトの使用方法とデプロイ後に発生する可能性のある実際のリスクの種類について共有可視性を得ることができます。

### Production-aware filtering and campaign targeting
- チームが最も重要なセキュリティアラートの優先順位を付けるのを支援するため、GitHub Advanced Securityは、Code Scanning、Dependabot、セキュリティキャンペーンで本番環境コンテキストフィルターをサポートするようになりました。組織レベルのアラートリストとキャンペーン作成フローで新しいフィルターオプションが見つかります：
- artifact-registry-url:でレジストリでフィルタリング
- has:deploymentを使用してデプロイメントステータスでフィルタリング
- runtime-risk:でランタイムリスクに焦点を当てる（例：runtime-risk:internet-exposedまたはruntime-risk:sensitive-data）
- これらのフィルターにより、セキュリティチームとAppSecチームは、理論的なリスクだけでなく、実際に本番環境に影響を与える問題を修復するためのターゲットキャンペーンを開始できます。問題を個別にまたは一括でCopilotコーディングエージェントに割り当てることができます。次に、エージェントは提案された修正を含むドラフトプルリクエストを生成し、その推論とステップを説明して、ハンドオフを合理化し、手動トリアージ時間を短縮します。

### Getting started
- GitHubでリンクされたアーティファクトを表示するには、新しいAPIを使用してアーティファクトメタデータを送信するようにビルドおよびCIワークフローを更新します（Microsoft Defender for Cloudを既に使用している場合を除き、その場合はコンテナのデプロイメントとリスクコンテキストが自動的に処理されます）。
- セキュリティビューで新しいフィルターオプションを使用して、デプロイされ、公開されているものにトリアージとキャンペーンを集中させます。
- 重要なセキュリティ問題またはキャンペーンを、GitHubの問題またはキャンペーンビューから直接Copilotコーディングエージェントに割り当てます。
- これらの改善により、実際のビジネスへの影響がある脆弱性に焦点を当てて修復することが可能になり、GitHub上で協力する開発者、AppSec、クラウドセキュリティチームのコラボレーションと可視性が向上します。
- サポートや質問については、コミュニティディスカッションでディスカッションを開いてください。

## Article Content (cleaned)
GitHubは、コード、ビルドアーティファクト、本番環境のコンテキストを接続することで、チームが重要なセキュリティリスクを追跡、優先順位付け、修復することをより簡単にしました。以下は、提供された新機能とその使用方法です：


## [Linked artifacts with full traceability](#linked-artifacts-with-full-traceability)


GitHub Actions経由でビルドされたアーティファクトは、Azure Container RegistryやJFrog Artifactoryなどの外部レジストリに最終的に保存される場合でも、GitHub内に「リンクされたアーティファクト」として表示されるようになりました。各リンクされたアーティファクトについて、GitHubは新しいメタデータを表示します：どのリポジトリがアーティファクトをビルドしたか、どのパッケージレジストリにアーティファクトが保存されているか、どこにデプロイされたかが表示されます。すべての証明されたアーティファクトは、ソースコードリポジトリに自動的にマッピングされるため、すべてのアーティファクトをその起源まで追跡できます。これは、[ストレージ](https://docs.github.com/rest/orgs/artifact-metadata?apiVersion=2022-11-28#create-artifact-metadata-storage-record)と[デプロイメント](https://docs.github.com/rest/orgs/artifact-metadata?apiVersion=2022-11-28#create-artifact-metadata-deployment-record)記録のための新しい[Artifact Metadata API](https://docs.github.com/rest/orgs/artifact-metadata?apiVersion=2022-11-28)によって実現されており、CI/CDワークフローや外部システムがプログラム的にデータをGitHubに送信し、リンクビューを最新の状態に保つことができます。


## [Runtime risk context in partnership with Microsoft Defender for Cloud](#runtime-risk-context-in-partnership-with-microsoft-defender-for-cloud)


GitHubは、アーティファクトのランタイムリスクを表示するようになりました。これには、インターネットに公開されているか、本番環境で機密データを処理しているかなどが含まれます。このコンテキストは、Microsoft Defender for Cloudによってネイティブに提供されており、[Deployment Record API](https://docs.github.com/rest/orgs/artifact-metadata?apiVersion=2022-11-28#create-artifact-metadata-deployment-record)のネイティブ実装を含むため、ワークフローの変更を必要とせずにデプロイメント記録とランタイムリスク属性を自動的に入力します。これにより、セキュリティチームと開発チームの両方が、ビルドアーティファクトの使用方法とデプロイ後に発生する可能性のある実際のリスクの種類について共有可視性を得ることができます。


## [Production\-aware filtering and campaign targeting](#production-aware-filtering-and-campaign-targeting)


チームが最も重要なセキュリティアラートの優先順位を付けるのを支援するため、GitHub Advanced Securityは、Code Scanning、Dependabot、セキュリティキャンペーンで本番環境コンテキストフィルターをサポートするようになりました。組織レベルのアラートリストとキャンペーン作成フローで新しいフィルターオプションが見つかります：


* `artifact-registry-url:`でレジストリでフィルタリング
* `has:deployment`を使用してデプロイメントステータスでフィルタリング
* `runtime-risk:`でランタイムリスクに焦点を当てる（例：`runtime-risk:internet-exposed`または`runtime-risk:sensitive-data`）


![新しい本番環境コンテキストフィルターを使用したキャンペーン作成フロー](https://github.com/user-attachments/assets/090c0ba9-385c-4514-bbd1-5c45ae681950)


これらのフィルターにより、セキュリティチームとAppSecチームは、理論的なリスクだけでなく、実際に本番環境に影響を与える問題を修復するためのターゲットキャンペーンを開始できます。問題を個別にまたは一括でCopilotコーディングエージェントに割り当てることができます。次に、エージェントは提案された修正を含むドラフトプルリクエストを生成し、その推論とステップを説明して、ハンドオフを合理化し、手動トリアージ時間を短縮します。


## [Getting started](#getting-started)


* GitHubでリンクされたアーティファクトを表示するには、[新しいAPI](https://docs.github.com/rest/orgs/artifact-metadata?apiVersion=2022-11-28)を使用してアーティファクトメタデータを送信するようにビルドおよびCIワークフローを更新します（Microsoft Defender for Cloudを既に使用している場合を除き、その場合はコンテナのデプロイメントとリスクコンテキストが自動的に処理されます）。
* セキュリティビューで新しいフィルターオプションを使用して、デプロイされ、公開されているものにトリアージとキャンペーンを集中させます。
* 重要なセキュリティ問題またはキャンペーンを、GitHubの問題またはキャンペーンビューから直接Copilotコーディングエージェントに割り当てます。


これらの改善により、実際のビジネスへの影響がある脆弱性に焦点を当てて修復することが可能になり、GitHub上で協力する開発者、AppSec、クラウドセキュリティチームのコラボレーションと可視性が向上します。


サポートや質問については、[コミュニティディスカッション](https://github.com/orgs/community/discussions)でディスカッションを開いてください。
