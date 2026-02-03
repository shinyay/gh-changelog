---
title: "不変リリースが一般提供開始"
date: "2025-10-28"
type: "improvements"
labels: ["supply chain security", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-immutable-releases-are-now-generally-available"
fetched_at: "2026-02-03T14:50:55.650701Z"
lang: "ja"
---

# 不変リリースが一般提供開始

## Overview
GitHub リリースが不変性をサポートし、サプライチェーンセキュリティに新しいレイヤーが追加されました。不変リリースでは、公開後にアセットやタグが改ざんから保護されるため、公開するソフトウェア、そしてユーザーが使用するソフトウェアの安全性と信頼性が維持されます。

## Detailed Explanation
### Overview
- GitHub リリースが不変性をサポートし、サプライチェーンセキュリティに新しいレイヤーが追加されました。不変リリースでは、公開後にアセットやタグが改ざんから保護されるため、公開するソフトウェア、そしてユーザーが使用するソフトウェアの安全性と信頼性が維持されます。

### About immutable releases
- 不変リリースが提供する機能:
- 不変アセット : リリースを不変として公開すると、そのアセットは追加、変更、削除ができなくなります。これにより、配布されるアーティファクトをサプライチェーン攻撃から保護できます。
- タグ保護 : 新しい不変リリースのタグは保護され、削除や移動ができなくなります。
- リリース証明 : 不変リリースには署名付き証明が付与されるため、GitHub 上でも外部環境でも、アセットの真正性と完全性を簡単に検証できます。

### How to enable immutable releases
- リポジトリレベルまたは組織レベルの設定で不変リリースを有効にできます。有効にすると:
- すべての新しいリリースが不変になります(つまり、アセットがロックされ、タグが保護されます)。
- 既存のリリースは、再公開しない限り可変のままです。
- 不変性を無効にしても、有効時に作成されたリリースには影響しません。それらは不変のままです。

### Release attestations and verification
- リリース証明を使用すると、アーティファクトが本物で変更されていないことを、GitHub 外でも検証できます。証明は Sigstore バンドル形式を使用しているため、GitHub CLI を使用してリリースとアセットを簡単に検証したり、Sigstore 互換ツールと統合して CI/CD パイプラインでポリシー適用を自動化したりできます。リリースの完全性を検証する方法については、リリースの完全性を検証するドキュメントを参照してください。
- フィードバックをお待ちしています。GitHub Community で考えや質問を共有してください。
- 詳細については、不変リリースのドキュメントを参照してください。

## Key Changes
- 不変アセット: リリースを不変として公開すると、アセットの追加、変更、削除ができなくなる
- タグ保護: 新しい不変リリースのタグは保護され、削除や移動ができない
- リリース証明: 署名付き証明により、アセットの真正性と完全性を検証可能

## Impact / Who's Affected
- リポジトリレベルまたは組織レベルで不変リリースを有効化できます
- 既存のリリースは再公開しない限り可変のまま
- 無効化しても有効時に作成されたリリースは不変のまま

## Caveats / Limitations
- 既存のリリースは、再公開しない限り可変のままです
- 不変性を無効にしても、有効時に作成されたリリースには影響しません

## Insights (derived from article language)
- Sigstore バンドル形式を使用することで、GitHub CLI や Sigstore 互換ツールと簡単に統合できます
- CI/CD パイプラインでポリシー適用を自動化できます

## Article Content (cleaned)
GitHub リリースが不変性をサポートし、サプライチェーンセキュリティに新しいレイヤーが追加されました。不変リリースでは、公開後にアセットやタグが改ざんから保護されるため、公開するソフトウェア、そしてユーザーが使用するソフトウェアの安全性と信頼性が維持されます。


### [About immutable releases](#about-immutable-releases)


不変リリースが提供する機能:


* **不変アセット**: リリースを不変として公開すると、そのアセットは追加、変更、削除ができなくなります。これにより、配布されるアーティファクトをサプライチェーン攻撃から保護できます。
* **タグ保護**: 新しい不変リリースのタグは保護され、削除や移動ができなくなります。
* **リリース証明**: 不変リリースには署名付き証明が付与されるため、GitHub 上でも外部環境でも、アセットの真正性と完全性を簡単に検証できます。


### [How to enable immutable releases](#how-to-enable-immutable-releases)


リポジトリレベルまたは組織レベルの設定で不変リリースを有効にできます。有効にすると:


* すべての新しいリリースが不変になります(つまり、アセットがロックされ、タグが保護されます)。
* 既存のリリースは、再公開しない限り可変のままです。


不変性を無効にしても、有効時に作成されたリリースには影響しません。それらは不変のままです。


### [Release attestations and verification](#release-attestations-and-verification)


リリース証明を使用すると、アーティファクトが本物で変更されていないことを、GitHub 外でも検証できます。証明は [Sigstore バンドル形式](https://docs.sigstore.dev/about/bundle/)を使用しているため、GitHub CLI を使用してリリースとアセットを簡単に検証したり、Sigstore 互換ツールと統合して CI/CD パイプラインでポリシー適用を自動化したりできます。リリースの完全性を検証する方法については、[リリースの完全性を検証するドキュメント](https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/verifying-the-integrity-of-a-release?tool=cli?utm_source=changelog-docs-immutable-releases&utm_medium=changelog&utm_campaign=universe25)を参照してください。


フィードバックをお待ちしています。[GitHub Community](https://gh.io/immutable-releases-ga?utm_source=changelog-community-immutable-releases&utm_medium=changelog&utm_campaign=universe25) で考えや質問を共有してください。


詳細については、[不変リリースのドキュメント](https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/immutable-releases?utm_source=changelog-docs-immutable-releases&utm_medium=changelog&utm_campaign=universe25)を参照してください。
