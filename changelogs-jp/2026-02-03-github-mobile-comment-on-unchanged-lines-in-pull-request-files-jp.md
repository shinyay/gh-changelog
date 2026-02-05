---
title: "GitHub Mobile: プルリクエストのファイルで未変更行にもコメント可能に"
date: "2026-02-03"
type: "Release"
labels: ["client apps"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-02-03-github-mobile-comment-on-unchanged-lines-in-pull-request-files"
fetched_at: "2026-02-05T04:46:41.087476Z"
lang: "ja"
---

# GitHub Mobile: プルリクエストのファイルで未変更行にもコメント可能に

## Overview
GitHub Mobile で、変更のあるファイル内ならどこにでもコメントできるようになりました。これまでは「Files Changed」ビューで、変更箇所の前後の行にしかコメントできませんでしたが、今回の機能により差分を展開して未変更のコードを表示し、必要な箇所にコメントや提案変更（suggested change）を残せます。

## Detailed Explanation
### 概要
- GitHub Mobile で、変更のあるファイル内の任意の場所にコメントできるようになりました。
- 以前は Files Changed ビューで、変更箇所の周辺行にのみコメント可能でした。

### どう使うか
- 差分を展開して未変更のコードを表示し、必要な箇所にコメントや提案変更を追加できます。

### Web との整合性
- github.com 上で未変更行に追加されたコメントも GitHub Mobile に表示されます。
- そのため、モバイルでも文脈を見失わずにレビューや返信ができます。

### 期待される効果
- 差分の近くだけでは指摘できなかった修正点（本来入るべき変更）を指摘しやすくなります。
- 未変更箇所にレビューの補足情報を残すなど、レビューの表現力が上がります。

### 提供状況
- iOS / Android の GitHub Mobile の最新プロダクションビルドで利用できます。

## Impact / Who’s Affected
- GitHub Mobile でプルリクエストをレビューする人は、差分の周辺行に限らず、ファイル内の必要な位置に対してフィードバックできるようになります。
- github.com 側で未変更行に付いたコメントも表示されるため、モバイルでのレビュー/返信がしやすくなります。

## Caveats / Limitations
- 利用には GitHub Mobile の最新プロダクションビルドが必要です。

## Article Content (cleaned)
GitHub Mobile で、変更のあるファイル内ならどこにでもコメントできるようになりました。これまでは **Files Changed** ビューで、変更箇所の前後の行にしかコメントできませんでした。今回の機能により差分を展開して未変更のコードを表示し、必要な箇所にコメントや提案変更を残せます。


github.com 上で未変更行に追加されたコメントも GitHub Mobile に表示されるため、スマートフォンからでも文脈を見失わずにレビューや返信ができます。


これにより、差分の文脈を超えた更新提案や、未変更箇所に対するレビューの補足などがしやすくなります。


この新しい体験は、GitHub Mobile の最新プロダクションビルドの [iOS](https://apps.apple.com/us/app/github/id1477376905) と [Android](https://play.google.com/store/apps/details?id=com.github.android) で利用できます。


[GitHub Community](https://github.com/orgs/community/discussions/categories/announcements) のディスカッションにも参加できます。
