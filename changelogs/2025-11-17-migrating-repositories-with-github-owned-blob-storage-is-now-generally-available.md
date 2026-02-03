---
title: "Migrating repositories with GitHub-owned blob storage is now generally available"
date: "2025-11-17"
type: "improvements"
labels: ["enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-17-migrating-repositories-with-github-owned-blob-storage-is-now-generally-available"
fetched_at: "2026-02-03T14:50:55.266030Z"
---

# Migrating repositories with GitHub-owned blob storage is now generally available

## Overview
You can now migrate repositories to GitHub Enterprise Cloud (GHEC) with GitHub Enterprise Importer (GEI) using GitHub-owned blob storage. You no longer need to provide GEI with shared access keys to a storage account you own to perform repository migrations. Instead, migrations can now be performed by uploading repository archives directly to github.com or ghe.com.

## Detailed Explanation
### Overview
- You can now migrate repositories to GitHub Enterprise Cloud (GHEC) with GitHub Enterprise Importer (GEI) using GitHub-owned blob storage. You no longer need to provide GEI with shared access keys to a storage account you own to perform repository migrations. Instead, migrations can now be performed by uploading repository archives directly to github.com or ghe.com.
- You can start a repository migration using GitHub-owned storage using the gh gei and gh bbs2gh command line extensions by passing in the --use-github-storage flag.
- To migrate repositories with GitHub-owned blob storage, you can follow our documentation for migrating repositories from GitHub Enterprise Server to GitHub Enterprise Cloud or migrating repositories from Bitbucket Server to GitHub Enterprise Cloud . Interested in migrating your GitLab repositories using GitHub-owned blob storage? Please reach out to our Expert Services team.

## Article Content (cleaned)
You can now migrate repositories to GitHub Enterprise Cloud (GHEC) with GitHub Enterprise Importer (GEI) using GitHub\-owned blob storage. You no longer need to provide GEI with shared access keys to a storage account you own to perform repository migrations. Instead, migrations can now be performed by uploading repository archives directly to github.com or ghe.com.


You can start a repository migration using GitHub\-owned storage using the `gh gei` and `gh bbs2gh` command line extensions by passing in the `--use-github-storage` flag.


![Repository migrations using `gh gei --use-github-storage` in the terminal](https://github.com/user-attachments/assets/5da7b312-2c43-4f1e-a6fe-1a92b3db05de)


To migrate repositories with GitHub\-owned blob storage, you can follow our documentation for [migrating repositories from GitHub Enterprise Server to GitHub Enterprise Cloud](https://docs.github.com/enterprise-cloud@latest/migrations/using-github-enterprise-importer/migrating-between-github-products/migrating-repositories-from-github-enterprise-server-to-github-enterprise-cloud) or [migrating repositories from Bitbucket Server to GitHub Enterprise Cloud](https://docs.github.com/enterprise-cloud@latest/migrations/using-github-enterprise-importer/migrating-from-bitbucket-server-to-github-enterprise-cloud/migrating-repositories-from-bitbucket-server-to-github-enterprise-cloud). Interested in migrating your GitLab repositories using GitHub\-owned blob storage? Please reach out to our [Expert Services](https://github.com/services) team.
