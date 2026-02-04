---
title: "Copilot coding agent がコードのセキュリティと品質を自動検証するように"
date: "2025-10-28"
type: "improvements"
labels: ["application security", "copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-copilot-coding-agent-now-automatically-validates-code-security-and-quality"
fetched_at: "2026-02-03T14:50:55.678652Z"
lang: "ja"
---

# Copilot coding agent がコードのセキュリティと品質を自動検証するように

## Overview
GitHub Copilot coding agent は、GitHub の非同期・自律型の開発者エージェントです。新機能の実装、バグ修正、テストカバレッジ改善など、幅広いタスクを委任でき、チームの開発を加速します。

## Detailed Explanation
### Overview
- GitHub Copilot coding agent は、GitHub の非同期・自律型の開発者エージェントです。新機能の実装、バグ修正、テストカバレッジ改善など、幅広いタスクを委任でき、チームの開発を加速します。
- Copilot coding agent には従来から幅広い組み込みのセキュリティ保護が含まれていましたが、このリリースでさらに前進しました。Copilot coding agent が生成した新しいコードは、GitHub のセキュリティおよび品質検証ツールによって自動的に分析されます。
- Copilot coding agent は、自身が作成したコードに対してセキュリティと品質の分析を先回りして実行するようになりました。Copilot が新しいコードを書くと、CodeQL を用いて潜在的なセキュリティ脆弱性を分析し、新規に導入された依存関係を GitHub Advisory Database と照合し、secret scanning で API キーやトークンなどの機密情報を検出します。さらに、コード品質の問題を評価するためのコードレビューも自動的に実施します。セキュリティ検証やコードレビューのツールが問題を見つけた場合、Copilot はプルリクエストを完了する前に解決を試み、実施した内容をプルリクエストサマリーで要約します。
- Copilot coding agent の自動セキュリティ/品質検証は、GitHub Advanced Security ライセンスや追加設定を必要としません。これらのセキュリティツールは通常の Copilot coding agent 利用にシームレスに含まれます。Copilot coding agent は、有料の Copilot プランで利用でき、GitHub 上に保管されたすべてのリポジトリで利用できます（管理対象ユーザーアカウントが所有し、明示的に無効化されているリポジトリを除く）。

## Caveats / Limitations
- Copilot coding agent は、有料の Copilot プランで利用でき、GitHub 上に保管されたすべてのリポジトリで利用できます（管理対象ユーザーアカウントが所有し、明示的に無効化されているリポジトリを除く）。

## Article Content (cleaned)
GitHub Copilot coding agent は、GitHub の非同期・自律型の開発者エージェントです。新機能の実装、バグ修正、テストカバレッジ改善など、幅広いタスクを委任でき、チームの開発を加速します。


Copilot coding agent には従来から [幅広い組み込みのセキュリティ保護](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent#built-in-security-protections?utm_source=changelog-docs-cca-auto-validates&utm_medium=changelog&utm_campaign=universe25) が含まれていましたが、このリリースでさらに前進しました。Copilot coding agent が生成した新しいコードは、GitHub のセキュリティおよび品質検証ツールによって自動的に分析されます。


Copilot coding agent は、自身が作成したコードに対してセキュリティと品質の分析を先回りして実行するようになりました。Copilot が新しいコードを書くと、[CodeQL](https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql?utm_source=changelog-docs-copilot-cca-auto-validates&utm_medium=changelog&utm_campaign=universe25) を用いて潜在的なセキュリティ脆弱性を分析し、新規に導入された依存関係を [GitHub Advisory Database](https://docs.github.com/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database?utm_source=changelog-docs-copilot-cca-auto-validates&utm_medium=changelog&utm_campaign=universe25) と照合し、[secret scanning](https://docs.github.com/code-security/secret-scanning/introduction/about-secret-scanning?utm_source=changelog-docs-copilot-cca-auto-validates&utm_medium=changelog&utm_campaign=universe25) で API キーやトークンなどの機密情報を検出します。さらに、コード品質の問題を評価するためのコードレビューも自動的に実施します。セキュリティ検証やコードレビューのツールが問題を見つけた場合、Copilot はプルリクエストを完了する前に解決を試み、実施した内容をプルリクエストサマリーで要約します。


Copilot coding agent の自動セキュリティ/品質検証は、GitHub Advanced Security ライセンスや追加設定を必要としません。これらのセキュリティツールは通常の Copilot coding agent 利用にシームレスに含まれます。Copilot coding agent は、有料の Copilot プランで利用でき、GitHub 上に保管されたすべてのリポジトリで利用できます（管理対象ユーザーアカウントが所有し、明示的に無効化されているリポジトリを除く）。
