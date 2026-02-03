---
title: "Dependabotのセルフホストおよび大規模GitHub-hosted Actionsランナー向けのカスタムラベル設定オプションが組織レベルで一般提供開始"
date: "2025-11-25"
type: "improvements"
labels: ["supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-25-custom-labels-configuration-option-for-dependabot-self-hosted-and-larger-github-hosted-actions-runners-now-generally-available-at-the-organization-level"
fetched_at: "2026-02-03T14:50:55.148651Z"
lang: "ja"
---

# Dependabotのセルフホストおよび大規模GitHub-hosted Actionsランナー向けのカスタムラベル設定オプションが組織レベルで一般提供開始

## Overview
Dependabot更新ジョブは、カスタムラベルを使用して特定のセルフホストおよび大規模GitHub-hosted Actionsランナーをターゲットにできるようになりました。以前は、Dependabotには単一のdependabotラベルが必要でした。この変更により、より細かい制御が可能になり、1つのラベルに制限された環境（一部のKubernetesベースのランナーコントローラーなど）でのガバナンスが改善され、組織レベルで設定されたランナー用のカスタムラベルを定義することで、セキュリティまたはパフォーマンスのためにワークロードをセグメント化できます。

## Detailed Explanation
### Overview
- Dependabot更新ジョブは、カスタムラベルを使用して特定のセルフホストおよび大規模GitHub-hosted Actionsランナーをターゲットにできるようになりました。以前は、Dependabotには単一のdependabotラベルが必要でした。この変更により、より細かい制御が可能になり、1つのラベルに制限された環境（一部のKubernetesベースのランナーコントローラーなど）でのガバナンスが改善され、組織レベルで設定されたランナー用のカスタムラベルを定義することで、セキュリティまたはパフォーマンスのためにワークロードをセグメント化できます。
- 新機能：– 任意のカスタムラベル（dependabotだけでなく）を使用して、Dependabotジョブを一致するセルフホストおよび大規模GitHub-hostedランナーにルーティング – オプションでランナーグループ名でランナーをスコープして、より細かい制御を実現 – 以前は固定のdependabotラベル専用にランナーを割り当てる必要があったセットアップの運用上の摩擦を軽減 – 好みに応じてデフォルトのdependabotラベルを引き続き使用できます。カスタムターゲティングが不要な場合、変更は不要です
- dependabotラベルに依存する既存のワークフローは、変更なしで引き続き機能します。**指定されたラベルにオンラインのランナーがない場合、Dependabotは一致するランナーが利用可能になるまでジョブをキューに入れます**。設定エラーを避けるため、ラベルのスペルが正しいことを確認してください。
- セルフホストランナーでのカスタムラベルの使用と、セルフホストランナーでのDependabotの管理について詳しく学ぶには、ドキュメントをご覧ください。
- GitHub Communityのディスカッションに参加してください。

## Insights (derived from article language)
- セルフホストランナーでのカスタムラベルの使用と、セルフホストランナーでのDependabotの管理について詳しく学ぶには、ドキュメントをご覧ください。

## Article Content (cleaned)
Dependabot更新ジョブは、カスタムラベルを使用して特定のセルフホストおよび大規模GitHub\-hosted Actionsランナーをターゲットにできるようになりました。以前は、Dependabotには単一の`dependabot`ラベルが必要でした。この変更により、より細かい制御が可能になり、1つのラベルに制限された環境（一部のKubernetesベースのランナーコントローラーなど）でのガバナンスが改善され、組織レベルで設定されたランナー用のカスタムラベルを定義することで、セキュリティまたはパフォーマンスのためにワークロードをセグメント化できます。


新機能：  

– 任意のカスタムラベル（`dependabot`だけでなく）を使用して、Dependabotジョブを一致するセルフホストおよび大規模GitHub\-hostedランナーにルーティング  

– オプションでランナーグループ名でランナーをスコープして、より細かい制御を実現  

– 以前は固定の`dependabot`ラベル専用にランナーを割り当てる必要があったセットアップの運用上の摩擦を軽減  

– 好みに応じてデフォルトの`dependabot`ラベルを引き続き使用できます。カスタムターゲティングが不要な場合、変更は不要です


`dependabot`ラベルに依存する既存のワークフローは、変更なしで引き続き機能します。**指定されたラベルにオンラインのランナーがない場合、Dependabotは一致するランナーが利用可能になるまでジョブをキューに入れます**。設定エラーを避けるため、ラベルのスペルが正しいことを確認してください。


セルフホストランナーでの[カスタムラベルの使用](https://docs.github.com/actions/how-tos/manage-runners/self-hosted-runners/apply-labels)と、[セルフホストランナーでのDependabotの管理](https://docs.github.com/code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners)について詳しく学ぶには、ドキュメントをご覧ください。


[GitHub Community](https://github.com/orgs/community/discussions/categories/announcements)のディスカッションに参加してください。
