---
title: "Go向けのDependabotベースの依存関係グラフ"
date: "2025-12-09"
type: "improvements"
labels: ["supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-09-dependabot-dgs-for-go"
fetched_at: "2026-02-03T14:50:55.028774Z"
lang: "ja"
---

# Go向けのDependabotベースの依存関係グラフ

## Overview
パッケージエコシステムのサポートを継続的に改善するサプライチェーンセキュリティのテーマに沿って、Goプロジェクトでは依存関係グラフとソフトウェア部品表(SBOM)でより完全で正確な推移的依存関係ツリーを表示できるようになりました。

## Detailed Explanation
### 概要
- パッケージエコシステムのサポートを継続的に改善するサプライチェーンセキュリティのテーマに沿って、Goプロジェクトでは依存関係グラフとソフトウェア部品表(SBOM)でより完全で正確な推移的依存関係ツリーを表示できるようになりました。
- Goは依存関係のバージョンを動的に解決するため、プロジェクトの依存関係を正確に把握することは静的な解析に依存できません。コミットがプロジェクトの`go.mod`を更新すると、GitHubは新しいタイプのDependabotジョブを実行し、依存関係スナップショットを構築してDependency Submission APIにアップロードします。
- このアプローチは他のエコシステムの依存関係自動送信と似ていますが、アクション時間の料金は発生しません。また、Dependabot用に設定した組織全体のプライベートレジストリ構成にアクセスすることもできます。
- 詳細については、依存関係グラフの設定をご覧ください。

## Article Content (cleaned)
パッケージエコシステムのサポートを継続的に改善するサプライチェーンセキュリティのテーマに沿って、Goプロジェクトでは依存関係グラフとソフトウェア部品表(SBOM)でより完全で正確な推移的依存関係ツリーを表示できるようになりました。


Goは依存関係のバージョンを動的に解決するため、プロジェクトの依存関係を正確に把握することは静的な解析に依存できません。コミットがプロジェクトの`go.mod`を更新すると、GitHubは新しいタイプのDependabotジョブを実行し、依存関係スナップショットを構築してDependency Submission APIにアップロードします。


このアプローチは他のエコシステムの依存関係自動送信と似ていますが、アクション時間の料金は発生しません。また、Dependabot用に設定した組織全体のプライベートレジストリ構成にアクセスすることもできます。


詳細については、[依存関係グラフの設定](https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph)をご覧ください。
