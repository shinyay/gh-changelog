---
title: "Dependabot が OIDC 認証に対応"
date: "2026-02-03"
type: "Improvement"
labels: ["supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-02-03-dependabot-now-supports-oidc-authentication"
fetched_at: "2026-02-05T04:46:41.073305Z"
lang: "ja"
---

# Dependabot が OIDC 認証に対応

## Overview
Dependabot が OpenID Connect (OIDC) を使ってプライベートレジストリに認証できるようになりました。これにより、長期間有効な認証情報をリポジトリのシークレットとして保存する必要がなくなります。

## Detailed Explanation
### 概要
- Dependabot が OpenID Connect (OIDC) を使ってプライベートレジストリに認証できるようになり、長期間有効な認証情報をリポジトリのシークレットとして保存する必要がなくなります。

### 変更点
- OIDC ベースの認証により、Dependabot の更新ジョブはクラウドの ID プロバイダーから短期間の認証情報を動的に取得できます。これは GitHub Actions ワークフローの OIDC フェデレーションと同様の考え方です。

### 対応レジストリ
- AWS CodeArtifact
- Azure DevOps Artifacts
- JFrog Artifactory

### 利点
- セキュリティの向上: 静的で長期間有効な認証情報をリポジトリから排除できます。短命で動的に生成されるトークンにより、運用負荷と攻撃面が減ります。
- 管理の簡素化: ポリシーに準拠した形でプライベートレジストリへ安全にアクセスしやすくなります。
- レート制限の回避: 静的トークンに起因するレート制限に当たりにくくなる可能性があります。

### はじめ方
- 対応するプライベートレジストリで OIDC 認証を有効にするには、`dependabot.yml` を更新して新しい OIDC 認証タイプを使用します。手順と例は、プライベートレジストリ設定のドキュメントを参照してください。

### 参考
- Configuring access to private registries for Dependabot
- About OpenID Connect

## Insights (derived from article language)
- 「Learn more」で提示されている通り、具体的な設定方法はドキュメント参照が前提になっています。

## Article Content (cleaned)
Dependabot は OpenID Connect (OIDC) を使ってプライベートレジストリに認証できるようになり、長期間有効な認証情報をリポジトリのシークレットとして保存する必要がなくなります。


## [What’s new](https://github.blog/changelog/feed/#whats-new)


OIDC\-based authentication により、Dependabot の更新ジョブはクラウドの ID プロバイダーから短期間の認証情報を動的に取得できます。これは GitHub Actions ワークフローが [OIDC federation](https://docs.github.com/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect) を利用するのと同様です。


### [Supported registries](https://github.blog/changelog/feed/#supported-registries)


* **AWS CodeArtifact**
* **Azure DevOps Artifacts**
* **JFrog Artifactory**


## [Benefits](https://github.blog/changelog/feed/#benefits)


* **Enhanced security:** 静的で長期間有効な認証情報をリポジトリから排除できます。短命で動的に生成されるトークンにより、運用負荷と攻撃面が減ります。
* **Simpler management:** ポリシーに準拠した形でプライベートレジストリへ安全にアクセスできるようになります。
* **Avoid rate limiting:** 静的トークンに起因するレート制限に当たりにくくなる可能性があります。


## [Getting started](https://github.blog/changelog/feed/#getting-started)


対応するプライベートレジストリで OIDC 認証を有効にするには、`dependabot.yml` を更新して新しい OIDC 認証タイプを使用します。手順と例は、[documentation on private registry configuration](https://docs.github.com/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot) を参照してください。


## [Learn more](https://github.blog/changelog/feed/#learn-more)


* [Configuring access to private registries for Dependabot](https://docs.github.com/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot)
* [About OpenID Connect](https://docs.github.com/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
