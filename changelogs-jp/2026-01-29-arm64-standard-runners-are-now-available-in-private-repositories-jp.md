---
title: "arm64標準ランナーがプライベートリポジトリで利用可能に"
date: "2026-01-29"
type: "Improvement"
labels: ["actions"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-29-arm64-standard-runners-are-now-available-in-private-repositories"
fetched_at: "2026-02-03T14:50:49.323999Z"
lang: "ja"
---

# arm64標準ランナーがプライベートリポジトリで利用可能に

## Overview
LinuxおよびWindows arm64標準GitHub-hostedランナーがプライベートリポジトリでサポートされるようになりました。これらの無料枠対象のarm64ランナーをすべてのリポジトリで使用できるようになり、arm64プロセッサのパフォーマンス上の利点を活用し、仮想化やエミュレーションのオーバーヘッドなしにネイティブマルチアーキテクチャビルドを実行できます。

## Detailed Explanation
### 概要
- LinuxおよびWindows arm64標準GitHub-hostedランナーがプライベートリポジトリでサポートされるようになりました。これらの無料枠対象のarm64ランナーをすべてのリポジトリで使用できるようになり、arm64プロセッサのパフォーマンス上の利点を活用し、仮想化やエミュレーションのオーバーヘッドなしにネイティブマルチアーキテクチャビルドを実行できます。
- これらは標準のGitHub-hostedランナーであるため、使用量はプランに含まれる無料分にカウントされます。

### 新機能
- LinuxおよびWindows arm64標準hostedランナーがすべてのリポジトリでサポートされるようになりました。
- プライベートリポジトリでは、これらのランナーは2つのvCPUを持ちます。パブリックリポジトリでは、4つのvCPUを持ちます。
- これらのランナーは、arm64プロセッサとArm, LLCが管理するイメージを使用します。
- 標準のGitHub-hostedランナーとして、プライベートリポジトリでのGitHubプランの無料分割り当ての使用に適格です。macOS arm64標準ランナーは、プライベートリポジトリですでに利用可能です。この更新により、プライベートリポジトリのarm64サポートがLinuxおよびWindowsに拡張されます。
- これは、コンテナ化されたサービスやマルチアーキテクチャビルドなど、arm64本番環境をターゲットとし、プライベートリポジトリで標準のGitHub-hostedランナーを使用してネイティブパフォーマンスを求めるチームに最適です。

### 始め方
- arm64でのビルドを開始するには、ワークフローのruns-onフィールドに次のサポートされているラベルのいずれかを追加します：
- windows-11-arm
- ubuntu-24.04-arm
- ubuntu-22.04-arm
- arm64ランナーと使用法の詳細については、標準GitHub-hostedランナーのドキュメントをご覧ください。
- これらのランナーは、完全にサポートされている標準のGitHub-hostedランナーであり、本番CIワークロードに適しています。
- GitHubコミュニティ内のディスカッションに参加してください。

## Impact / Who's Affected
- LinuxおよびWindows arm64標準GitHub-hostedランナーがプライベートリポジトリでサポートされるようになりました。
- 新機能 LinuxおよびWindows arm64標準hostedランナーがすべてのリポジトリでサポートされるようになりました。

## Insights (derived from article language)
- 始め方 arm64でのビルドを開始するには、ワークフローのruns-onフィールドに次のサポートされているラベルのいずれかを追加します：windows-11-arm ubuntu-24.04-arm ubuntu-22.04-arm arm64ランナーと使用法の詳細については、標準GitHub-hostedランナーのドキュメントをご覧ください。

## Article Content (cleaned)
LinuxおよびWindows arm64標準GitHub\-hostedランナーがプライベートリポジトリでサポートされるようになりました。これらの無料\-枠対象のarm64ランナーをすべてのリポジトリで使用できるようになり、arm64プロセッサのパフォーマンス上の利点を活用し、仮想化やエミュレーションのオーバーヘッドなしにネイティブマルチ\-アーキテクチャビルドを実行できます。


これらは標準のGitHub\-hostedランナーであるため、使用量は[プランに含まれる無料分](https://docs.github.com/billing/concepts/product-billing/github-actions#free-use-of-github-actions)にカウントされます。


## [What's new](https://github.blog/changelog/feed/#whats-new)


* LinuxおよびWindows arm64標準hostedランナーがすべてのリポジトリでサポートされるようになりました。
* プライベートリポジトリでは、これらのランナーは2つのvCPUを持ちます。パブリックリポジトリでは、4つのvCPUを持ちます。
* これらのランナーは、arm64プロセッサとArm, LLCが管理するイメージを使用します。


標準のGitHub\-hostedランナーとして、プライベートリポジトリでのGitHubプランの無料分割り当ての使用に適格です。macOS arm64標準ランナーは、プライベートリポジトリですでに利用可能です。この更新により、プライベートリポジトリのarm64サポートがLinuxおよびWindowsに拡張されます。


これは、コンテナ化されたサービスやマルチ\-アーキテクチャビルドなど、arm64本番環境をターゲットとし、プライベートリポジトリで標準のGitHub\-hostedランナーを使用してネイティブパフォーマンスを求めるチームに最適です。


## [Get started](https://github.blog/changelog/feed/#get-started)


arm64でのビルドを開始するには、ワークフローのruns\-onフィールドに次のサポートされているラベルのいずれかを追加します：


* `windows-11-arm`
* `ubuntu-24.04-arm`
* `ubuntu-22.04-arm`


arm64ランナーと使用法の詳細については、[標準GitHub\-hostedランナーのドキュメント](https://docs.github.com/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for--private-repositories)をご覧ください。


これらのランナーは、完全にサポートされている標準のGitHub\-hostedランナーであり、本番CIワークロードに適しています。


[GitHubコミュニティ](https://github.com/orgs/community/discussions/185840)内のディスカッションに参加してください。
