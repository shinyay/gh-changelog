---
title: "非公開GitHubギストのシークレットがシークレットスキャニングパートナーに報告されるようになりました"
date: "2025-11-25"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-25-secrets-in-unlisted-github-gists-are-now-reported-to-secret-scanning-partners"
fetched_at: "2026-02-03T14:50:55.141909Z"
lang: "ja"
---

# 非公開GitHubギストのシークレットがシークレットスキャニングパートナーに報告されるようになりました

## Overview
本日より、GitHubは非公開GitHubギストで見つかった公開漏洩シークレットをそれぞれのシークレットスキャニングパートナーに報告します。

## Detailed Explanation
### Overview
- 本日より、GitHubは非公開GitHubギストで見つかった公開漏洩シークレットをそれぞれのシークレットスキャニングパートナーに報告します。
- GitHubギストは、公開（publicラベルで示される）または非公開（secretラベルで示される）にできます。
- プライベートGitHubギストというものは存在せず、すべてのギストはURLを持っている人なら誰でも表示できます。この一般的な誤解により、secretギストは漏洩シークレットの重要な盲点となっています。GitHubギストで漏洩したシークレットは、他の公開漏洩シークレットと同様に扱う必要があります。

### What is the secret scanning partnership program?
- 開発者コミュニティを保護するため、GitHubは数百のシークレットスキャニングパートナーと提携して漏洩シークレットを特定しています。
- GitHubは、AWS、OpenAI、Stripeなどの業界パートナーと直接協力して、特定のシークレット形式のディテクターを構築し、高精度と低誤検出を確保しています。GitHubは、公開漏洩シークレットが見つかったときにシークレット発行者に通知し、パートナーが即座にアクションを取れるようにします。シークレットスキャニングが有効になっているリポジトリの場合、GitHubはシークレットスキャニングアラートで開発者にも通知します。

### What is a GitHub gist?
- ギストは、他の人とコードスニペットを共有する簡単な方法を提供します。GitHubにサインインしているときにギストを作成すると、ギストはアカウントに関連付けられ、ギストホームページに移動したときにギストリストに表示されます。
- ギストは公開またはシークレットにできます。公開ギストはDiscoverに表示され、作成された新しいギストを閲覧できます。また、検索可能なので、他の人に作品を見つけて見てもらいたい場合に使用できます。シークレットギストはDiscoverに表示されず、ログインしてシークレットギストの作成者でない限り検索できません。シークレットギストはプライベートではありません。シークレットギストのURLを友人に送信すると、友人は表示できます。ただし、知らない誰かがURLを発見した場合、その人もギストを表示できます。詮索好きな目からコードを守りたい場合は、代わりにプライベートリポジトリを作成することをお勧めします。
- GitHubシークレットスキャニング、GitHubギスト、GitHubシークレットスキャニングパートナーシッププログラムについて詳しく学びましょう。

## Caveats / Limitations
- GitHubギストは、公開（publicラベルで示される）または非公開（secretラベルで示される）にできます。

## Insights (derived from article language)
- GitHubシークレットスキャニング、GitHubギスト、GitHubシークレットスキャニングパートナーシッププログラムについて詳しく学びましょう。

## Article Content (cleaned)
本日より、GitHubは非公開GitHubギストで見つかった公開漏洩シークレットをそれぞれのシークレットスキャニングパートナーに報告します。


GitHubギストは、公開（`public`ラベルで示される）または非公開（`secret`ラベルで示される）にできます。


**プライベートGitHubギストというものは存在せず**、すべてのギストはURLを持っている人なら誰でも表示できます。この一般的な誤解により、`secret`ギストは漏洩シークレットの重要な盲点となっています。GitHubギストで漏洩したシークレットは、他の公開漏洩シークレットと同様に扱う必要があります。


### [What is the secret scanning partnership program?](#what-is-the-secret-scanning-partnership-program)


開発者コミュニティを保護するため、GitHubは数百のシークレットスキャニングパートナーと提携して漏洩シークレットを特定しています。


GitHubは、AWS、OpenAI、Stripeなどの業界パートナーと直接協力して、特定のシークレット形式のディテクターを構築し、高精度と低誤検出を確保しています。GitHubは、公開漏洩シークレットが見つかったときにシークレット発行者に通知し、パートナーが即座にアクションを取れるようにします。シークレットスキャニングが有効になっているリポジトリの場合、GitHubはシークレットスキャニングアラートで開発者にも通知します。


### [What is a GitHub gist?](#what-is-a-github-gist)


ギストは、他の人とコードスニペットを共有する簡単な方法を提供します。GitHubにサインインしているときにギストを作成すると、ギストはアカウントに関連付けられ、ギストホームページに移動したときにギストリストに表示されます。


ギストは公開またはシークレットにできます。公開ギストはDiscoverに表示され、作成された新しいギストを閲覧できます。また、検索可能なので、他の人に作品を見つけて見てもらいたい場合に使用できます。シークレットギストはDiscoverに表示されず、ログインしてシークレットギストの作成者でない限り検索できません。シークレットギストはプライベートではありません。シークレットギストのURLを友人に送信すると、友人は表示できます。ただし、知らない誰かがURLを発見した場合、その人もギストを表示できます。詮索好きな目からコードを守りたい場合は、代わりにプライベートリポジトリを作成することをお勧めします。


[GitHubシークレットスキャニング](https://docs.github.com/enterprise-cloud@latest/code-security/secret-scanning/introduction/about-secret-scanning)、[GitHubギスト](https://docs.github.com/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)、[GitHubシークレットスキャニングパートナーシッププログラム](https://docs.github.com/code-security/secret-scanning/secret-scanning-partnership-program/secret-scanning-partner-program)について詳しく学びましょう。
