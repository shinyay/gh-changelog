---
title: "Copilot コーディングエージェントをルールセットのバイパスアクターとして設定"
date: "2025-11-13"
type: "improvements"
labels: ["copilot", "platform governance"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-13-configure-copilot-coding-agent-as-a-bypass-actor-for-rulesets"
fetched_at: "2026-02-03T14:50:55.289918Z"
lang: "ja"
---

# Copilot コーディングエージェントをルールセットのバイパスアクターとして設定

## Overview
ルールセットを使用すると、さまざまなアクターがリポジトリとどのようにやり取りできるかを制御できます。ルールセットを使用して、次のようなルールを適用できます:

## Detailed Explanation
### 概要
- ルールセットを使用すると、さまざまなアクターがリポジトリとどのようにやり取りできるかを制御できます。ルールセットを使用して、次のようなルールを適用できます:
- 特定のパターンに一致するメールアドレスからのコミットのみを許可する。
- コミットメッセージが特定の構造に従うことを保証する。
- コミットに署名することを要求する。
- Copilot コーディングエージェントは、バックグラウンドで動作する非同期開発者エージェントです。すべてのルールに常に準拠できるわけではありません。たとえば、コミットに署名することはできません。エージェントが準拠できないルールがリポジトリに含まれている場合、エージェントは自動的に無効になります。
- これで、Copilot コーディングエージェントを選択したルールセットのバイパスアクターとして設定することで、コーディングエージェントの使用をブロック解除できます。これにより、人間がプッシュするコードの要件を緩和することなく、特定のルールから Copilot を除外できます。
- Copilot コーディングエージェントの詳細については、GitHub Docs の「GitHub Copilot コーディングエージェントについて」を参照してください。

## Impact / Who's Affected
- ルールセットを使用して、次のようなルールを適用できます: 特定のパターンに一致するメールアドレスからのコミットのみを許可する。

## Caveats / Limitations
- ルールセットを使用して、次のようなルールを適用できます: 特定のパターンに一致するメールアドレスからのコミットのみを許可する。

## Insights (derived from article language)
- Copilot コーディングエージェントの詳細については、GitHub Docs の「GitHub Copilot コーディングエージェントについて」を参照してください。

## Article Content (cleaned)
[ルールセット](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)を使用すると、さまざまなアクターがリポジトリとどのようにやり取りできるかを制御できます。ルールセットを使用して、次のようなルールを適用できます:


* 特定のパターンに一致するメールアドレスからのコミットのみを許可する。
* コミットメッセージが特定の構造に従うことを保証する。
* コミットに署名することを要求する。


[Copilot コーディングエージェント](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent)は、バックグラウンドで動作する非同期開発者エージェントです。すべてのルールに常に準拠できるわけではありません。たとえば、コミットに署名することはできません。エージェントが準拠できないルールがリポジトリに含まれている場合、エージェントは自動的に無効になります。


これで、[Copilot コーディングエージェントを選択したルールセットのバイパスアクターとして設定](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository#granting-bypass-permissions-for-your-branch-or-tag-ruleset)することで、コーディングエージェントの使用をブロック解除できます。これにより、人間がプッシュするコードの要件を緩和することなく、特定のルールから Copilot を除外できます。


Copilot コーディングエージェントの詳細については、GitHub Docs の[「GitHub Copilot コーディングエージェントについて」](https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent)を参照してください。
