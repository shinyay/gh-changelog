---
title: "GitHub所有のBlobストレージを使用したリポジトリ移行が一般提供に"
date: "2025-11-17"
type: "improvements"
labels: ["enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-17-migrating-repositories-with-github-owned-blob-storage-is-now-generally-available"
fetched_at: "2026-02-03T14:50:55.266030Z"
lang: "ja"
---

# GitHub所有のBlobストレージを使用したリポジトリ移行が一般提供に

## Overview
GitHub Enterprise Importer（GEI）を使用して、GitHub所有のBlobストレージでリポジトリをGitHub Enterprise Cloud（GHEC）に移行できるようになりました。リポジトリ移行を実行するために、所有するストレージアカウントへの共有アクセスキーをGEIに提供する必要がなくなりました。代わりに、リポジトリアーカイブをgithub.comまたはghe.comに直接アップロードすることで移行を実行できるようになりました。

## Detailed Explanation
### Overview
- GitHub Enterprise Importer（GEI）を使用して、GitHub所有のBlobストレージでリポジトリをGitHub Enterprise Cloud（GHEC）に移行できるようになりました。リポジトリ移行を実行するために、所有するストレージアカウントへの共有アクセスキーをGEIに提供する必要がなくなりました。代わりに、リポジトリアーカイブをgithub.comまたはghe.comに直接アップロードすることで移行を実行できるようになりました。
- `gh gei`および`gh bbs2gh`コマンドライン拡張機能を使用し、`--use-github-storage`フラグを指定することで、GitHub所有のストレージを使用したリポジトリ移行を開始できます。
- GitHub所有のBlobストレージでリポジトリを移行するには、GitHub Enterprise ServerからGitHub Enterprise Cloudへのリポジトリ移行、またはBitbucket ServerからGitHub Enterprise Cloudへのリポジトリ移行に関するドキュメントに従ってください。GitHub所有のBlobストレージを使用してGitLabリポジトリを移行することに興味がありますか？Expert Servicesチームにお問い合わせください。

## Article Content (cleaned)
GitHub Enterprise Importer（GEI）を使用して、GitHub所有のBlobストレージでリポジトリをGitHub Enterprise Cloud（GHEC）に移行できるようになりました。リポジトリ移行を実行するために、所有するストレージアカウントへの共有アクセスキーをGEIに提供する必要がなくなりました。代わりに、リポジトリアーカイブをgithub.comまたはghe.comに直接アップロードすることで移行を実行できるようになりました。


`gh gei`および`gh bbs2gh`コマンドライン拡張機能を使用し、`--use-github-storage`フラグを指定することで、GitHub所有のストレージを使用したリポジトリ移行を開始できます。


![Repository migrations using `gh gei --use-github-storage` in the terminal](https://github.com/user-attachments/assets/5da7b312-2c43-4f1e-a6fe-1a92b3db05de)


GitHub所有のBlobストレージでリポジトリを移行するには、[GitHub Enterprise ServerからGitHub Enterprise Cloudへのリポジトリ移行](https://docs.github.com/enterprise-cloud@latest/migrations/using-github-enterprise-importer/migrating-between-github-products/migrating-repositories-from-github-enterprise-server-to-github-enterprise-cloud)、または[Bitbucket ServerからGitHub Enterprise Cloudへのリポジトリ移行](https://docs.github.com/enterprise-cloud@latest/migrations/using-github-enterprise-importer/migrating-from-bitbucket-server-to-github-enterprise-cloud/migrating-repositories-from-bitbucket-server-to-github-enterprise-cloud)に関するドキュメントに従ってください。GitHub所有のBlobストレージを使用してGitLabリポジトリを移行することに興味がありますか？[Expert Services](https://github.com/services)チームにお問い合わせください。
