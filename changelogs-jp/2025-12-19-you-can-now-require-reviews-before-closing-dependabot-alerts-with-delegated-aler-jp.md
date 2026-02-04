---
title: "委任されたアラート却下によりDependabotアラートを閉じる前にレビューを要求可能に"
date: "2025-12-19"
type: "improvements"
labels: ["supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-19-you-can-now-require-reviews-before-closing-dependabot-alerts-with-delegated-alert-dismissal"
fetched_at: "2026-02-03T14:50:54.837326Z"
lang: "ja"
---

# 委任されたアラート却下によりDependabotアラートを閉じる前にレビューを要求可能に

## Overview
委任されたアラート却下により、Dependabotアラートが閉じられる前にレビュープロセスを要求できるようになります。この機能はGitHub Code Securityのお客様が利用でき、UIとAPIの両方で使用できます。

## Detailed Explanation
### Overview
- 委任されたアラート却下により、Dependabotアラートが閉じられる前にレビュープロセスを要求できるようになります。この機能はGitHub Code Securityのお客様が利用でき、UIとAPIの両方で使用できます。
- これにより、セキュリティリスクをより適切に管理し、監査とコンプライアンスの要件を満たすことができます。委任されたアラート却下により、[code scanning](https://docs.github.com/code-security/code-scanning/managing-your-code-scanning-configuration/enabling-delegated-alert-dismissal-for-code-scanning)および[Secret Scanning](https://docs.github.com/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/enabling-delegated-alert-dismissal-for-secret-scanning)で利用可能な同じガバナンス制御がDependabotアラートにも提供されます。
- この機能は組織に以下の支援を提供します：
- 脆弱性アラートへの対処時に開発チーム全体で**説明責任を向上**させます。
- 偶発的または不正な却下などの**安全でない活動を防止**します。
- アラート活動のガバナンスと監査を容易にすることで、**大規模なアラート管理**を実現します。
- DependabotのためのDelegated alert dismissalは、github.comおよびGitHub Enterprise Server 3.21でコードセキュリティのお客様が現在利用できます。
- Dependabotアラート却下リクエストについて詳しく学ぶには、code securityに関するドキュメントをご覧ください。

## Insights (derived from article language)
- Dependabotアラート却下リクエストについて詳しく学ぶには、code securityに関するドキュメントをご覧ください。

## Article Content (cleaned)
委任されたアラート却下により、Dependabotアラートが閉じられる前にレビュープロセスを要求できるようになります。この機能はGitHub Code Securityのお客様が利用でき、UIとAPIの両方で使用できます。


これにより、セキュリティリスクをより適切に管理し、監査とコンプライアンスの要件を満たすことができます。委任されたアラート却下により、[code scanning](https://docs.github.com/code-security/code-scanning/managing-your-code-scanning-configuration/enabling-delegated-alert-dismissal-for-code-scanning)および[Secret Scanning](https://docs.github.com/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/enabling-delegated-alert-dismissal-for-secret-scanning)で利用可能な同じガバナンス制御がDependabotアラートにも提供されます。


この機能は組織に以下の支援を提供します：


* 脆弱性アラートへの対処時に開発チーム全体で**説明責任を向上**させます。
* 偶発的または不正な却下などの**安全でない活動を防止**します。
* アラート活動のガバナンスと監査を容易にすることで、**大規模なアラート管理**を実現します。


DependabotのためのDelegated alert dismissalは、github.comおよびGitHub Enterprise Server 3\.21でコードセキュリティのお客様が現在利用できます。


Dependabotアラート却下リクエストについて詳しく学ぶには、[code securityに関するドキュメント](https://docs.github.com/enterprise-cloud@latest/code-security)をご覧ください。
