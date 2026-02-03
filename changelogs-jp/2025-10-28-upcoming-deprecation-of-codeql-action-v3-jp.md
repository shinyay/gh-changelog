---
title: "CodeQL Action v3 の今後の廃止予定"
date: "2025-10-28"
type: "deprecations"
labels: ["actions", "application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-upcoming-deprecation-of-codeql-action-v3"
fetched_at: "2026-02-03T14:50:55.519073Z"
lang: "ja"
---

# CodeQL Action v3 の今後の廃止予定

## Overview
2025年10月7日に、Node.js 24 ランタイムで動作する CodeQL Action v4 をリリースしました。CodeQL Action v3 は、GHES 3.19 と同時に廃止される予定で、現在2026年12月に予定されています。

## Detailed Explanation
### Overview
- 2025年10月7日に、Node.js 24 ランタイムで動作する CodeQL Action v4 をリリースしました。CodeQL Action v3 は、GHES 3.19 と同時に廃止される予定で、現在2026年12月に予定されています。

### Default setup
- コードスキャニングのデフォルトセットアップのユーザーは、CodeQL Action v4 に自動的に移行するためのアクションを実行する必要はありません。

### Advanced setup
- コードスキャニングの高度なセットアップのユーザーは、CodeQL Action v4 の使用を開始するためにワークフローファイルを変更する必要があります。
- 次のプラットフォーム上の GitHub Actions で GitHub コードスキャニング（デフォルトで CodeQL 解析エンジンを使用）を使用しているすべてのユーザーは、ワークフローファイルを更新する必要があります：
- github.com（オープンソースリポジトリ、GitHub Teams および GitHub Enterprise Cloud のユーザーを含む）
- GitHub Enterprise Server（GHES）3.20 以降
- 上記のプラットフォームのユーザーは、CodeQL Action の新しい v4 バージョンを参照するように CodeQL ワークフローファイルを更新する必要があります。今後リリースされる GitHub Enterprise Server 3.20 には、CodeQL Action の v4 が含まれます。
- GHES 3.19 は Node.js 24 Actions をサポートしていますが、CodeQL Action v4 は同梱されていません。GHES 3.19 で v4 に移行したいユーザーは、ワークフローファイルを更新する前に、システム管理者に GitHub Connect を有効にして v4 を GHES にダウンロードするよう依頼する必要があります。
- GHES 3.18 以前のバージョンは、Node.js 24 ランタイムを使用する Actions の実行をサポートしていません。したがって、CodeQL Action v4 を実行できません。CodeQL Action ワークフローファイルを変更する前に、新しいバージョンの GitHub Enterprise Server にアップグレードしてください。

### Exactly what do I need to change?
- CodeQL Action v4 にアップグレードするには、リポジトリの `.github` ディレクトリにある CodeQL ワークフローファイルを開き、次の参照を探します：
- github/codeql-action/init@v3
- github/codeql-action/autobuild@v3
- github/codeql-action/analyze@v3
- github/codeql-action/upload-sarif@v3
- これらのエントリを、v4 相当のものに置き換える必要があります：
- github/codeql-action/init@v4
- github/codeql-action/autobuild@v4
- github/codeql-action/analyze@v4
- github/codeql-action/upload-sarif@v4

### Can I use Dependabot to help me with this upgrade?
- はい、できます！詳細については、Dependabot を構成して Actions の依存関係を自動的にアップグレードする方法に関するドキュメントをご覧ください。

### What happens in December 2026?
- 2026年12月に、CodeQL Action v3 が正式に廃止されます（GHES 3.19 の廃止と同時）。その時点で、CodeQL Action v3 に対する新しい更新は行われなくなり、新しい CodeQL 解析機能は CodeQL Action v4 のユーザーのみが利用できるようになります。GitHub 全体での移行の進捗状況を注視します。多くのワークフローファイルが依然として CodeQL Action v3 を参照している場合、認知度を高めるために、年内に1回以上のブラウンアウト期間をスケジュールすることを検討する可能性があります。

## Impact / Who’s Affected
- CodeQL Action v3 は、GHES 3.19 と同時に廃止される予定で、現在2026年12月に予定されています。
- 2026年12月に、CodeQL Action v3 が正式に廃止されます（GHES 3.19 の廃止と同時）。
- その時点で、CodeQL Action v3 に対する新しい更新は行われなくなり、新しい CodeQL 解析機能は CodeQL Action v4 のユーザーのみが利用できるようになります。

## Caveats / Limitations
- 今後リリースされる GitHub Enterprise Server 3.20 には、CodeQL Action の v4 が含まれます。
- その時点で、CodeQL Action v3 に対する新しい更新は行われなくなり、新しい CodeQL 解析機能は CodeQL Action v4 のユーザーのみが利用できるようになります。

## Insights (derived from article language)
- Advanced setup コードスキャニングの高度なセットアップのユーザーは、CodeQL Action v4 の使用を開始するためにワークフローファイルを変更する必要があります。
- 今後リリースされる GitHub Enterprise Server 3.20 には、CodeQL Action の v4 が含まれます。
- 詳細については、Dependabot を構成して Actions の依存関係を自動的にアップグレードする方法に関するドキュメントをご覧ください。
- 多くのワークフローファイルが依然として CodeQL Action v3 を参照している場合、認知度を高めるために、年内に1回以上のブラウンアウト期間をスケジュールすることを検討する可能性があります。

## Article Content (cleaned)
2025年10月7日に、Node.js 24 ランタイムで動作する CodeQL Action v4 をリリースしました。CodeQL Action v3 は、GHES 3\.19 と同時に廃止される予定で、現在2026年12月に予定されています。


## [How does this affect me?](#how-does-this-affect-me)


### [Default setup](#default-setup)


[コードスキャニングのデフォルトセットアップ](https://docs.github.com/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)のユーザーは、CodeQL Action v4 に自動的に移行するためのアクションを実行する必要はありません。


### [Advanced setup](#advanced-setup)


[コードスキャニングの高度なセットアップ](https://docs.github.com/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning)のユーザーは、CodeQL Action v4 の使用を開始するためにワークフローファイルを変更する必要があります。


#### [Users of github.com and GitHub Enterprise Server 3\.20 and newer](#users-of-github-com-and-github-enterprise-server-3-20-and-newer)


次のプラットフォーム上の GitHub Actions で GitHub コードスキャニング（デフォルトで CodeQL 解析エンジンを使用）を使用しているすべてのユーザーは、ワークフローファイルを更新する必要があります：


* github.com（オープンソースリポジトリ、GitHub Teams および GitHub Enterprise Cloud のユーザーを含む）
* GitHub Enterprise Server（GHES）3\.20 以降


上記のプラットフォームのユーザーは、CodeQL Action の新しい v4 バージョンを参照するように CodeQL ワークフローファイルを更新する必要があります。今後リリースされる GitHub Enterprise Server 3\.20 には、CodeQL Action の v4 が含まれます。


#### [Users of GitHub Enterprise Server 3\.19](#users-of-github-enterprise-server-3-19)


GHES 3\.19 は Node.js 24 Actions を**サポートしていますが**、CodeQL Action v4 は**同梱されていません**。GHES 3\.19 で v4 に移行したいユーザーは、ワークフローファイルを更新する前に、システム管理者に [GitHub Connect](https://docs.github.com/enterprise-server@3.11/admin/github-actions/managing-access-to-actions-from-githubcom/using-the-latest-version-of-the-official-bundled-actions#using-github-connect-to-access-the-latest-actions) を有効にして v4 を GHES にダウンロードするよう依頼する必要があります。


#### [Users of GitHub Enterprise Server 3\.18 and older](#users-of-github-enterprise-server-3-18-and-older)


GHES 3\.18 以前のバージョンは、Node.js 24 ランタイムを使用する Actions の実行をサポートしていません。したがって、CodeQL Action v4 を実行できません。CodeQL Action ワークフローファイルを変更する前に、新しいバージョンの GitHub Enterprise Server にアップグレードしてください。


## [Exactly what do I need to change?](#exactly-what-do-i-need-to-change)


CodeQL Action v4 にアップグレードするには、リポジトリの `.github` ディレクトリにある CodeQL ワークフローファイルを開き、次の参照を探します：


* `github/codeql-action/init@v3`
* `github/codeql-action/autobuild@v3`
* `github/codeql-action/analyze@v3`
* `github/codeql-action/upload-sarif@v3`


これらのエントリを、v4 相当のものに置き換える必要があります：


* `github/codeql-action/init@v4`
* `github/codeql-action/autobuild@v4`
* `github/codeql-action/analyze@v4`
* `github/codeql-action/upload-sarif@v4`


## [Can I use Dependabot to help me with this upgrade?](#can-i-use-dependabot-to-help-me-with-this-upgrade)


はい、できます！詳細については、[Dependabot を構成して Actions の依存関係を自動的にアップグレードする方法に関するドキュメント](https://docs.github.com/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot)をご覧ください。


## [What happens in December 2026?](#what-happens-in-december-2026)


2026年12月に、CodeQL Action v3 が正式に廃止されます（GHES 3\.19 の廃止と同時）。その時点で、CodeQL Action v3 に対する新しい更新は行われなくなり、新しい CodeQL 解析機能は CodeQL Action v4 のユーザーのみが利用できるようになります。GitHub 全体での移行の進捗状況を注視します。多くのワークフローファイルが依然として CodeQL Action v3 を参照している場合、認知度を高めるために、年内に1回以上のブラウンアウト期間をスケジュールすることを検討する可能性があります。
