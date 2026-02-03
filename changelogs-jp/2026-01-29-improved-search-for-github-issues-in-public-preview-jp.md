---
title: "GitHub Issuesの改善された検索がパブリックプレビューに"
date: "2026-01-29"
type: "Release"
labels: ["projects &amp; issues"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-29-improved-search-for-github-issues-in-public-preview"
fetched_at: "2026-02-03T14:50:49.349952Z"
lang: "ja"
---

# GitHub Issuesの改善された検索がパブリックプレビューに

## Overview
GitHub Issuesの改善された検索により、探しているissueを見つけることがこれまで以上に簡単になりました。新しいセマンティックインデックスに基づいて構築されており、使用するキーワードだけでなく、クエリの意味に基づいて結果を見つけることができるようになりました。

## Detailed Explanation
### 概要
- GitHub Issuesの改善された検索により、探しているissueを見つけることがこれまで以上に簡単になりました。新しいセマンティックインデックスに基づいて構築されており、使用するキーワードだけでなく、クエリの意味に基づいて結果を見つけることができるようになりました。

### 新機能
- 「モバイルで認証が失敗する」や「面白いタイムライン動作」のような自然言語を使用してissueを検索すると、issueのタイトルや説明が完全に異なる表現を使用している場合でも、GitHubは概念的に類似した結果を返します。クエリがより詳細であるほど、結果は良くなります。
- プレリリーステストでは、これがユーザーにとって大幅な改善であることがわかりました。全体として、結果は従来の検索と比較してセマンティック検索で39%優れています。

### 仕組み
- セマンティック検索は、自然言語で探しているものを説明するときにアクティブになります。これを最大限に活用するために、結果は自動的に「Best match」で並べ替えられ、最も関連性の高いissueが最初に表示されます。
- 完全一致が必要な検索（引用符を含むクエリなど）の場合、GitHubは従来のレキシカル検索エンジンを使用して、必要な精度を提供します。
- パブリックプレビュー中は、機能プレビューダイアログを使用してオプトアウトできます。

### 試し方
- 任意のリポジトリのIssuesタブに移動して、自然言語を使用して検索します。ご意見をお聞かせください。コミュニティディスカッション投稿で体験を共有してください。

### issuesとprojectsへの追加の改善
- EdgeとSafariでラベルを検索する際の遅いパフォーマンスの原因となっていたバグを修正しました。
- GitHub Issuesに影響するSafariベースのスクロールバグを修正し、よりスムーズなスクロール動作を実現しました。
- マイルストーンの順序が、オープンissueとクローズissueの両方で一貫して機能するようになりました。

## Key Changes
- EdgeとSafariでラベルを検索する際の遅いパフォーマンスの原因となっていたバグを修正しました。
- GitHub Issuesに影響するSafariベースのスクロールバグを修正し、よりスムーズなスクロール動作を実現しました。
- マイルストーンの順序が、オープンissueとクローズissueの両方で一貫して機能するようになりました。

## Impact / Who's Affected
- パブリックプレビュー中は、機能プレビューダイアログを使用してオプトアウトできます。

## Article Content (cleaned)
GitHub Issuesの改善された検索により、探しているissueを見つけることがこれまで以上に簡単になりました。新しいセマンティックインデックスに基づいて構築されており、使用するキーワードだけでなく、クエリの意味に基づいて結果を見つけることができるようになりました。


# [What's new](https://github.blog/changelog/feed/#whats-new)


「モバイルで認証が失敗する」や「面白いタイムライン動作」のような自然言語を使用してissueを検索すると、issueのタイトルや説明が完全に異なる表現を使用している場合でも、GitHubは概念的に類似した結果を返します。クエリがより詳細であるほど、結果は良くなります。


プレリリーステストでは、これがユーザーにとって大幅な改善であることがわかりました。全体として、結果は従来の検索と比較してセマンティック検索で39%優れています。


![Line chart showing a major improvement in search ranking for GitHub Issues. Lexical Search averages a low position of 4, while the new Semantic Search consistently finds results closer to position 1 or 2](https://github.com/user-attachments/assets/64116472-5acb-4245-ace1-c79eb91c9903)


## [How it works](https://github.blog/changelog/feed/#how-it-works)


セマンティック検索は、自然言語で探しているものを説明するときにアクティブになります。これを最大限に活用するために、結果は自動的に「Best match」で並べ替えられ、最も関連性の高いissueが最初に表示されます。


完全一致が必要な検索（引用符を含むクエリなど）の場合、GitHubは従来のレキシカル検索エンジンを使用して、必要な精度を提供します。


パブリックプレビュー中は、[機能プレビューダイアログ](https://docs.github.com/get-started/using-github/exploring-early-access-releases-with-feature-preview)を使用してオプトアウトできます。


## [How to try it](https://github.blog/changelog/feed/#how-to-try-it)


任意のリポジトリの**Issues**タブに移動して、自然言語を使用して検索します。ご意見をお聞かせください。[コミュニティディスカッション](https://github.com/orgs/community/discussions/185760)投稿で体験を共有してください。


# [Additional improvements to issues and projects](https://github.blog/changelog/feed/#additional-improvements-to-issues-and-projects)


* EdgeとSafariでラベルを検索する際の遅いパフォーマンスの原因となっていたバグを修正しました。
* GitHub Issuesに影響するSafariベースのスクロールバグを修正し、よりスムーズなスクロール動作を実現しました。
* マイルストーンの順序が、オープンissueとクローズissueの両方で一貫して機能するようになりました。
