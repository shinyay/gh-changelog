---
title: "Actionsのworkflow dispatchワークフローが25個の入力をサポートするようになりました"
date: "2025-12-04"
type: "improvements"
labels: ["actions"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-04-actions-workflow-dispatch-workflows-now-support-25-inputs"
fetched_at: "2026-02-03T14:50:55.052244Z"
lang: "ja"
---

# Actionsのworkflow dispatchワークフローが25個の入力をサポートするようになりました

## Overview
`workflow_dispatch`トリガーで起動されるワークフローで、最大25個の入力を使用できるようになりました。

## Detailed Explanation
### Overview
- `workflow_dispatch`トリガーで起動されるワークフローで、最大25個の入力を使用できるようになりました。
- 以前の制限は10でしたが、これはコミュニティにとって課題でした。この新しい制限により、手動またはAPI経由でワークフローをトリガーする際により柔軟性が得られ、複数の入力を単一のJSON文字列に統合するなどの回避策が不要になります。

## Article Content (cleaned)
`workflow_dispatch`トリガーで起動されるワークフローで、最大25個の入力を使用できるようになりました。


以前の制限は10でしたが、これは[コミュニティにとって課題](https://github.com/orgs/community/discussions/8774)でした。この新しい制限により、手動またはAPI経由でワークフローをトリガーする際により柔軟性が得られ、複数の入力を単一のJSON文字列に統合するなどの回避策が不要になります。
