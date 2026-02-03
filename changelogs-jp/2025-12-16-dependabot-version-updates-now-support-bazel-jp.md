---
title: "DependabotバージョンアップデートがBazelをサポート"
date: "2025-12-16"
type: "new releases"
labels: ["supply chain security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-16-dependabot-version-updates-now-support-bazel"
fetched_at: "2026-02-03T14:50:54.911102Z"
lang: "ja"
---

# DependabotバージョンアップデートがBazelをサポート

## Overview
開発者は、DependabotをつかってBazel依存関係を自動的に最新に保つことができるようになりました。Bazel（BzlmodまたはWORKSPACE）を使用するプロジェクトでは、Dependabotバージョンアップデートが依存関係を最新のリリースで最新の状態に保つことができます。

## Detailed Explanation
### Overview
- 開発者は、DependabotをつかってBazel依存関係を自動的に最新に保つことができるようになりました。Bazel（BzlmodまたはWORKSPACE）を使用するプロジェクトでは、Dependabotバージョンアップデートが依存関係を最新のリリースで最新の状態に保つことができます。
- Bazelチームによる貢献とコラボレーションにより、Dependabotへのサポートがもたらされたことに大きな感謝を申し上げます。

### 背景
- DependabotのBazelサポートに対するオープンソースコミュニティの主な要求には以下が含まれます：
- 適切なロックファイル生成
- `*.MODULE.bazel`サポート
- WORKSPACEサポート（今後の廃止予定にもかかわらず、まだ広く使用されている）
- Bazelは2つの依存関係システムを使用しており、最新のBzlmodシステム（`MODULE.bazel`ファイル）とレガシーWORKSPACEシステムの両方があります。コミュニティのフィードバックは、多くのチームがまだWORKSPACEに依存していることを示したため、両方のサポートを構築しました。さらに、Bazelの`MODULE.bazel.lock`ファイルは、モジュール拡張とリポジトリルールを含む複雑な推移的依存関係グラフをキャプチャします。不正なロックファイル生成は再現可能なビルドを壊すため、Bazelコミュニティと緊密に協力してこれを正しく行いました。

### コミュニティパートナーシップ
- Bazelコミュニティは重要なガイダンスを提供しました：
- Fabian Meumertzheim：ロックファイルのセマンティクスと動作のマッチング
- Yun Peng：テスト、検証、実装データ
- Alex Eagle：ファイル命名規則と`*.MODULE.bazel`パターン
- これらの方々、そしてこのエコシステムのプレビューサポート中にテストしてフィードバックを提供してくれたすべての方々に特に感謝します。

### 仕組み
- 依存関係の検出：Dependabotは`MODULE.bazel`、`*.MODULE.bazel`、またはWORKSPACEファイルをスキャンし、Bazel中央レジストリで更新をチェックします。
- ロックファイル管理：Dependabotはロックファイルを再生成して、再現可能なビルドを維持します。
- プルリクエスト：Dependabotは、更新された宣言、再生成されたロックファイル、リリースノート、互換性情報を含むプルリクエストを開きます。

### 開始方法
- 要件には以下が含まれます：
- Bazel 7、8、または9
- リポジトリルートの`MODULE.bazel`または`WORKSPACE`ファイル
- Bazelサポートのトピックについて、Dependabotオープンソースコミュニティとエンゲージしてください。
- Dependabotバージョンアップデートドキュメントで詳しく学びましょう。
- Bazelについて詳しく学びましょう。
- リポジトリルートの`MODULE.bazel`または`WORKSPACE`ファイル
- Bazelサポートのトピックについて、Dependabotオープンソースコミュニティとエンゲージしてください。

## Caveats / Limitations
- プルリクエスト：Dependabotは、更新された宣言、再生成されたロックファイル、リリースノート、互換性情報を含むプルリクエストを開きます。

## Insights (derived from article language)
- Dependabotバージョンアップデートドキュメントで詳しく学びましょう。
- Bazelについて詳しく学びましょう。

## Article Content (cleaned)
開発者は、DependabotをつかってBazel依存関係を自動的に最新に保つことができるようになりました。Bazel（BzlmodまたはWORKSPACE）を使用するプロジェクトでは、Dependabotバージョンアップデートが依存関係を最新のリリースで最新の状態に保つことができます。


Bazelチームによる貢献とコラボレーションにより、Dependabotへのサポートがもたらされたことに大きな感謝を申し上げます。


## [Background](#background)


DependabotのBazelサポートに対する[オープンソースコミュニティの主な要求](https://github.com/bazelbuild/bazel/discussions/27142)には以下が含まれます：


* 適切なロックファイル生成
* `*.MODULE.bazel`サポート
* WORKSPACEサポート（今後の廃止予定にもかかわらず、まだ広く使用されている）


Bazelは2つの依存関係システムを使用しており、最新のBzlmodシステム（`MODULE.bazel`ファイル）とレガシーWORKSPACEシステムの両方があります。コミュニティのフィードバックは、多くのチームがまだWORKSPACEに依存していることを示したため、両方のサポートを構築しました。さらに、Bazelの`MODULE.bazel.lock`ファイルは、モジュール拡張とリポジトリルールを含む複雑な推移的依存関係グラフをキャプチャします。不正なロックファイル生成は再現可能なビルドを壊すため、Bazelコミュニティと緊密に協力してこれを正しく行いました。


## [Community partnership](#community-partnership)


Bazelコミュニティは重要なガイダンスを提供しました：


* **Fabian Meumertzheim：** ロックファイルのセマンティクスと動作のマッチング
* **Yun Peng：** テスト、検証、実装データ
* **Alex Eagle：** ファイル命名規則と`*.MODULE.bazel`パターン


これらの方々、そしてこのエコシステムのプレビューサポート中にテストしてフィードバックを提供してくれたすべての方々に特に感謝します。


## [How it works](#how-it-works)


1. **依存関係の検出：** Dependabotは`MODULE.bazel`、`*.MODULE.bazel`、またはWORKSPACEファイルをスキャンし、Bazel中央レジストリで更新をチェックします。
2. **ロックファイル管理：** Dependabotはロックファイルを再生成して、再現可能なビルドを維持します。
3. **プルリクエスト：** Dependabotは、更新された宣言、再生成されたロックファイル、リリースノート、互換性情報を含むプルリクエストを開きます。


## [Getting started](#getting-started)


要件には以下が含まれます：


* Bazel 7、8、または9
* リポジトリルートの`MODULE.bazel`または`WORKSPACE`ファイル
* Bazelサポートのトピックについて、[Dependabotオープンソースコミュニティ](https://github.com/dependabot/dependabot-core/issues/2196)とエンゲージしてください。
* [Dependabotバージョンアップデートドキュメント](https://docs.github.com/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates)で詳しく学びましょう。
* [Bazel](https://bazel.build/)について詳しく学びましょう。
