---
title: "hostedランナーでのDockerおよびDocker Composeバージョンのアップグレード"
date: "2026-01-30"
type: "Improvement"
labels: ["actions"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-30-docker-and-docker-compose-version-upgrades-on-hosted-runners"
fetched_at: "2026-02-03T14:50:49.211063Z"
lang: "ja"
---

# hostedランナーでのDockerおよびDocker Composeバージョンのアップグレード

## Overview
2026年2月9日に、ubuntu-slimを除くすべてのWindowsおよびUbuntuランナーイメージでDockerおよびDocker Composeが更新されます。この更新により、これらのツールの最新機能を活用できるようになります。

## Detailed Explanation
### 概要
- 2026年2月9日に、ubuntu-slimを除くすべてのWindowsおよびUbuntuランナーイメージでDockerおよびDocker Composeが更新されます。この更新により、これらのツールの最新機能を活用できるようになります。

### 新しいバージョン
- Docker Engine：v29.1
- Docker Compose：v2.40（変更前に新しいv2マイナーバージョンがリリースされた場合はそれ以上）
- v29で削除が予定されているDocker機能に依存している場合、ワークフローを更新する必要がある場合があります。

### 今後のランナーイメージの変更について最新情報を入手
- パフォーマンスの向上、機能の強化、セキュリティの改善のために、ランナーイメージを定期的に更新しています。runner-imagesリポジトリでランナーイメージへの今後の変更、更新、非推奨のリストを確認できます。定期的にチェックして、ランナーイメージが予定されている更新の影響を受けないことを確認してください。

## Key Changes
- パフォーマンスの向上、機能の強化、セキュリティの改善のために、ランナーイメージを定期的に更新しています。runner-imagesリポジトリでランナーイメージへの今後の変更、更新、非推奨のリストを確認できます。定期的にチェックして、ランナーイメージが予定されている更新の影響を受けないことを確認してください。

## Caveats / Limitations
- 2026年2月9日に、ubuntu-slimを除くすべてのWindowsおよびUbuntuランナーイメージでDockerおよびDocker Composeが更新されます。

## Article Content (cleaned)
2026年2月9日に、`ubuntu-slim`を除くすべてのWindowsおよびUbuntuランナーイメージでDockerおよびDocker Composeが更新されます。この更新により、これらのツールの最新機能を活用できるようになります。


### [New Versions](https://github.blog/changelog/feed/#new-versions)


* Docker Engine：`v29.1`
* Docker Compose：`v2.40`（変更前に新しいv2マイナーバージョンがリリースされた場合はそれ以上）


v29で[削除が予定されているDocker機能](https://docs.docker.com/engine/deprecated/)に依存している場合、ワークフローを更新する必要がある場合があります。


### [Keep up to date on upcoming runner image changes](https://github.blog/changelog/feed/#keep-up-to-date-on-upcoming-runner-image-changes)


パフォーマンスの向上、機能の強化、セキュリティの改善のために、ランナーイメージを定期的に更新しています。[runner\-imagesリポジトリ](https://github.com/actions/runner-images/labels/Announcement)でランナーイメージへの今後の変更、更新、非推奨のリストを確認できます。定期的にチェックして、ランナーイメージが予定されている更新の影響を受けないことを確認してください。
