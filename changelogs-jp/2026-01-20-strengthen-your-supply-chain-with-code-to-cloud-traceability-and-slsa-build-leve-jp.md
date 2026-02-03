---
title: "コードからクラウドへのトレーサビリティと SLSA Build Level 3 セキュリティでサプライチェーンを強化"
date: "2026-01-20"
type: "improvements"
labels: ["actions", "application security", "supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-20-strengthen-your-supply-chain-with-code-to-cloud-traceability-and-slsa-build-level-3-security"
fetched_at: "2026-02-03T14:50:54.748106Z"
lang: "ja"
---

# コードからクラウドへのトレーサビリティと SLSA Build Level 3 セキュリティでサプライチェーンを強化

## Overview
コンテナやバイナリなどのビルドアーティファクトを GitHub にリンクし、ストレージとデプロイメントのコンテキストを追加できるようになりました。アーティファクトが GitHub の外にある場合でも可能です。これにより、コードからクラウドへのトレーサビリティを取得し、本番環境で実際に実行されているものに基づいてセキュリティ作業の優先順位を付けることができます。

## Detailed Explanation
### Overview
- コンテナやバイナリなどのビルドアーティファクトを GitHub にリンクし、ストレージとデプロイメントのコンテキストを追加できるようになりました。アーティファクトが GitHub の外にある場合でも可能です。これにより、コードからクラウドへのトレーサビリティを取得し、本番環境で実際に実行されているものに基づいてセキュリティ作業の優先順位を付けることができます。

### Artifact metadata APIs
- 新しい REST API エンドポイントにより、ビルドアーティファクトをストレージの場所に関連付け、リリースパイプラインを通じてプロモーションを追跡し、デプロイメントデータやランタイムリスクなどの本番コンテキストを追加できます:
- Storage records は、パッケージレジストリ内のアーティファクトの場所をキャプチャします。
- Deployment records は、アーティファクトがデプロイされている場所と、デプロイされたワークロードがインターネットに公開されているか、機密データを処理しているかなどのランタイムリスク要因をキャプチャします。
- これらの API は、CI/CD ワークフロー、外部 CD ツール、またはクラウドランタイムモニターから呼び出すことができます。ローンチパートナー (デプロイメントとランタイムデータ用の Microsoft Defender for Cloud (パブリックプレビュー中) と、ストレージとプロモーションコンテキスト用の JFrog Artifactory) は、追加の設定なしで有効にできるネイティブ統合を構築しました。

### Linked artifacts view
- 組織の Packages タブの新しいビューには、すべてのリンクされたアーティファクトとその認証、ストレージの場所、デプロイメント履歴が表示されます。これにより、ソフトウェアサプライチェーン全体にわたる統一された可視性が得られます。
- GitHub アーティファクト認証を使用すると、各アーティファクトはソースリポジトリとビルドワークフローに暗号的にバインドされ、SLSA Build Level 3 セキュリティの達成に役立ちます。アーティファクトビューには、ビルド来歴、認証された SBOM、ソフトウェア開発ライフサイクルに適合するカスタム認証を含む、アーティファクトに対して作成されたすべての認証が表示されます。

### Production-context filtering for security alerts
- ストレージとデプロイメントレコードを追加すると、デプロイされているものや本番環境で公開されているものに基づいて、GitHub Dependabot アラート、GitHub コードスキャンアラート、セキュリティキャンペーンをフィルタリングできます:
- artifact-registry および artifact-registry-url
- has:deployment および runtime-risk
- これらを EPSS や CVSS スコアなどの既存のフィルターと組み合わせて、最も重要な脆弱性に修復の取り組みを集中させることができます。

### How to link artifacts to GitHub
- Artifact attestations : GitHub の attest-build-provenance アクションは、アーティファクトを公開する際にストレージレコードを自動的に作成できます。
- Partner integrations : Microsoft Defender for Cloud と JFrog Artifactory は、レコードを直接 GitHub に送信できます。
- REST API : 任意のソースからの任意のアーティファクトに対して、ストレージとデプロイメントレコードをプログラムでアップロードします。

### Additional resources
- About linked artifacts
- Artifact metadata API reference
- Prioritize security alerts based on production context
- Microsoft Defender for Cloud integration with GitHub Advanced Security
- Use the GitHub and JFrog integration for secure, traceable builds
- GitHub Community でディスカッションに参加してください。

## Impact / Who’s Affected
- ローンチパートナー (デプロイメントとランタイムデータ用の Microsoft Defender for Cloud (パブリックプレビュー中) と、ストレージとプロモーションコンテキスト用の JFrog Artifactory) は、追加の設定なしで有効にできるネイティブ統合を構築しました。

## Article Content (cleaned)
コンテナやバイナリなどのビルドアーティファクトを GitHub にリンクし、ストレージとデプロイメントのコンテキストを追加できるようになりました。アーティファクトが GitHub の外にある場合でも可能です。これにより、コードからクラウドへのトレーサビリティを取得し、本番環境で実際に実行されているものに基づいてセキュリティ作業の優先順位を付けることができます。


## [What’s new](#whats-new)


### [Artifact metadata APIs](#artifact-metadata-apis)


新しい REST API エンドポイントにより、ビルドアーティファクトをストレージの場所に関連付け、リリースパイプラインを通じてプロモーションを追跡し、デプロイメントデータやランタイムリスクなどの本番コンテキストを追加できます:


* **[Storage records](https://docs.github.com/rest/orgs/artifact-metadata#create-artifact-metadata-storage-record)** は、パッケージレジストリ内のアーティファクトの場所をキャプチャします。
* **[Deployment records](https://docs.github.com/rest/orgs/artifact-metadata#create-an-artifact-deployment-record)** は、アーティファクトがデプロイされている場所と、デプロイされたワークロードがインターネットに公開されているか、機密データを処理しているかなどのランタイムリスク要因をキャプチャします。


これらの API は、CI/CD ワークフロー、外部 CD ツール、またはクラウドランタイムモニターから呼び出すことができます。ローンチパートナー (デプロイメントとランタイムデータ用の Microsoft Defender for Cloud (パブリックプレビュー中) と、ストレージとプロモーションコンテキスト用の JFrog Artifactory) は、追加の設定なしで有効にできるネイティブ統合を構築しました。


### [Linked artifacts view](#linked-artifacts-view)


組織の **Packages** タブの新しいビューには、すべてのリンクされたアーティファクトとその認証、ストレージの場所、デプロイメント履歴が表示されます。これにより、ソフトウェアサプライチェーン全体にわたる統一された可視性が得られます。


[GitHub アーティファクト認証](https://docs.github.com/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations) を使用すると、各アーティファクトはソースリポジトリとビルドワークフローに暗号的にバインドされ、[SLSA Build Level 3](https://github.blog/enterprise-software/devsecops/enhance-build-security-and-reach-slsa-level-3-with-github-artifact-attestations/) セキュリティの達成に役立ちます。アーティファクトビューには、ビルド来歴、認証された SBOM、ソフトウェア開発ライフサイクルに適合するカスタム認証を含む、アーティファクトに対して作成されたすべての認証が表示されます。


### [Production-context filtering for security alerts](#production-context-filtering-for-security-alerts)


ストレージとデプロイメントレコードを追加すると、デプロイされているものや本番環境で公開されているものに基づいて、GitHub Dependabot アラート、GitHub コードスキャンアラート、セキュリティキャンペーンをフィルタリングできます:


* `artifact-registry` および `artifact-registry-url`
* `has:deployment` および `runtime-risk`


これらを [EPSS や CVSS スコアなどの既存のフィルター](https://docs.github.com/code-security/how-tos/manage-security-alerts/manage-dependabot-alerts/viewing-and-updating-dependabot-alerts#prioritizing-dependabot-alerts) と組み合わせて、最も重要な脆弱性に修復の取り組みを集中させることができます。


## [How to link artifacts to GitHub](#how-to-link-artifacts-to-github)


* **Artifact attestations**: GitHub の [`attest-build-provenance` アクション](https://github.com/marketplace/actions/attest-build-provenance) は、アーティファクトを公開する際にストレージレコードを自動的に作成できます。
* **Partner integrations**: Microsoft Defender for Cloud と JFrog Artifactory は、レコードを直接 GitHub に送信できます。
* **REST API**: 任意のソースからの任意のアーティファクトに対して、ストレージとデプロイメントレコードをプログラムでアップロードします。


## [Additional resources](#additional-resources)


* [About linked artifacts](https://docs.github.com/code-security/concepts/supply-chain-security/linked-artifacts)
* [Artifact metadata API reference](https://docs.github.com/rest/orgs/artifact-metadata)
* [Prioritize security alerts based on production context](https://docs.github.com/code-security/tutorials/secure-your-organization/prioritize-alerts-in-production-code)
* [Microsoft Defender for Cloud integration with GitHub Advanced Security](https://learn.microsoft.com/azure/defender-for-cloud/github-advanced-security-overview)
* [Use the GitHub and JFrog integration for secure, traceable builds](https://github.blog/enterprise-software/devsecops/how-to-use-the-github-and-jfrog-integration-for-secure-traceable-builds-from-commit-to-production/)


[GitHub Community](https://github.com/orgs/community/discussions/categories/announcements) でディスカッションに参加してください。
