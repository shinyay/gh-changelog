---
title: "未設定ポリシー向けの GitHub Copilot ポリシーアップデート"
date: "2025-11-04"
type: "improvements"
labels: ["copilot", "enterprise management tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-04-github-copilot-policy-update-for-unconfigured-policies"
fetched_at: "2026-02-03T14:50:55.463138Z"
lang: "ja"
---

# 未設定ポリシー向けの GitHub Copilot ポリシーアップデート

## Overview
エンタープライズポリシーが `Unconfigured` に設定されている場合に、組織の Copilot ポリシーが誤ったオプションを表示することがあった問題を修正しました。

## Detailed Explanation
### 概要
- エンタープライズポリシーが `Unconfigured` に設定されている場合に、組織の Copilot ポリシーが誤ったオプションを表示することがあった問題を修正しました。

### 変更内容
- Copilot ポリシーの更新により、エンタープライズと組織間のポリシー委譲の本来の流れが復元されます。現在、エンタープライズポリシーが `Unconfigured` に設定されている場合、対応する組織ポリシーは組織が `Enabled` に設定できるのではなく、デフォルトで `Disabled` になります。
- これにより、エンタープライズ管理者が明示的にポリシーを有効化または委譲しない限り、ポリシーは制限されたままになります。
- 望まないサービス中断を防ぐため、以前影響を受けていた組織ポリシーで現在 `Enabled` に設定されているものは、この更新によって変更されません。ただし、管理者がポリシーを `Disabled` に設定すると、エンタープライズポリシーが許可するよう更新されない限り、組織レベルで再度変更することはできません。今後のリリースの組織ポリシーは、エンタープライズポリシーが `Unconfigured` の場合、自動的に正しい `Disabled` 設定を継承します。

### 詳細
- 詳細については、Copilot ポリシーの管理に関するドキュメントをご覧ください。

## Insights (derived from article language)
- 詳細 詳細については、Copilot ポリシーの管理に関するドキュメントをご覧ください。

## Article Content (cleaned)
エンタープライズポリシーが `Unconfigured` に設定されている場合に、組織の Copilot ポリシーが誤ったオプションを表示することがあった問題を修正しました。


## [変更内容](#whats-changed)


Copilot ポリシーの更新により、エンタープライズと組織間のポリシー委譲の本来の流れが復元されます。現在、エンタープライズポリシーが `Unconfigured` に設定されている場合、対応する組織ポリシーは組織が `Enabled` に設定できるのではなく、デフォルトで `Disabled` になります。


これにより、エンタープライズ管理者が明示的にポリシーを有効化または委譲しない限り、ポリシーは制限されたままになります。


望まないサービス中断を防ぐため、以前影響を受けていた組織ポリシーで現在 `Enabled` に設定されているものは、この更新によって変更されません。ただし、管理者がポリシーを `Disabled` に設定すると、エンタープライズポリシーが許可するよう更新されない限り、組織レベルで再度変更することはできません。今後のリリースの組織ポリシーは、エンタープライズポリシーが `Unconfigured` の場合、自動的に正しい `Disabled` 設定を継承します。


## [詳細](#learn-more)


詳細については、[Copilot ポリシーの管理に関するドキュメント](https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies)をご覧ください。
