---
title: "GitHub Dependabotプルリクエストコメントコマンドの変更"
date: "2026-01-27"
type: "deprecations"
labels: ["supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-27-changes-to-github-dependabot-pull-request-comment-commands"
fetched_at: "2026-02-03T14:50:54.700278Z"
lang: "ja"
---

# GitHub Dependabotプルリクエストコメントコマンドの変更

## Overview
2025年10月に発表したとおり、GitHubのネイティブプルリクエスト機能を優先して、本日いくつかのDependabot固有のプルリクエストコメントコマンドを非推奨にしました。

## Detailed Explanation
### 概要
- 2025年10月に発表したとおり、GitHubのネイティブプルリクエスト機能を優先して、本日いくつかのDependabot固有のプルリクエストコメントコマンドを非推奨にしました。
- この変更は、混乱を減らし、信頼性を向上させ、プルリクエストを操作するためのGitHubプラットフォームの組み込みツールの使用を促進することを目的としています。

### Dependabotコメントコマンドの非推奨化
- 以下のコメントコマンドはサポートされなくなりました：
- @dependabot merge
- @dependabot cancel merge
- @dependabot squash and merge
- @dependabot close
- @dependabot reopen

### 移行ガイダンス
- GitHubのネイティブ機能に依存するようにワークフローを更新してください。プルリクエストのマージ、クローズ、または再オープンには、GitHubの組み込みUI、GitHub CLI、およびプルリクエストのREST APIエンドポイントの使用をお勧めします。

## Impact / Who’s Affected
- 2025年10月に発表したとおり、GitHubのネイティブプルリクエスト機能を優先して、本日いくつかのDependabot固有のプルリクエストコメントコマンドを非推奨にしました。

## Insights (derived from article language)
- プルリクエストのマージ、クローズ、または再オープンには、GitHubの組み込みUI、GitHub CLI、およびプルリクエストのREST APIエンドポイントの使用をお勧めします。

## Article Content (cleaned)
[2025年10月に発表した](https://github.blog/changelog/2025-10-07-upcoming-changes-to-github-dependabot-pull-request-comment-commands/)とおり、GitHubのネイティブプルリクエスト機能を優先して、本日いくつかのDependabot\-固有のプルリクエストコメントコマンドを非推奨にしました。


この変更は、混乱を減らし、信頼性を向上させ、プルリクエストを操作するためのGitHubプラットフォームの組み込みツールの使用を促進することを目的としています。


### [Dependabot comment command deprecations](#dependabot-comment-command-deprecations)


以下のコメントコマンドはサポートされなくなりました：


* `@dependabot merge`
* `@dependabot cancel merge`
* `@dependabot squash and merge`
* `@dependabot close`
* `@dependabot reopen`


### [Migration guidance](#migration-guidance)


GitHubのネイティブ機能に依存するようにワークフローを更新してください。プルリクエストのマージ、クローズ、または再オープンには、GitHubの組み込みUI、[GitHub CLI](https://cli.github.com/manual/gh_pr)、および[プルリクエストのREST APIエンドポイント](https://docs.github.com/rest/pulls?apiVersion=2022-11-28)の使用をお勧めします。
