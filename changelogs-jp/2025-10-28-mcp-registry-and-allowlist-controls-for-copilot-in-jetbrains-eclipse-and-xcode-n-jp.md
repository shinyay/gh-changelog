---
title: "JetBrains、Eclipse、Xcode の Copilot 向け MCP レジストリと許可リストコントロールがパブリックプレビューに"
date: "2025-10-28"
type: "improvements"
labels: ["copilot", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-mcp-registry-and-allowlist-controls-for-copilot-in-jetbrains-eclipse-and-xcode-now-in-public-preview"
fetched_at: "2026-02-03T14:50:55.637824Z"
lang: "ja"
---

# JetBrains、Eclipse、Xcode の Copilot 向け MCP レジストリと許可リストコントロールがパブリックプレビューに

## Overview
エンタープライズおよび組織の管理者は、JetBrains、Eclipse、Xcode の nightly およびプレリリースビルドで、開発者が検索して使用できる MCP サーバーを設定できるようになりました。

## Detailed Explanation
### Overview
- エンタープライズおよび組織の管理者は、JetBrains、Eclipse、Xcode の nightly およびプレリリースビルドで、開発者が検索して使用できる MCP サーバーを設定できるようになりました。

### MCP registry
- MCP レジストリは、Model Context Protocol (MCP) サーバーのディレクトリです。JetBrains IDE、Eclipse、Xcode を使用する開発者は、IDE 内のレジストリから直接 MCP サーバーを参照してインストールでき、検索とセットアップが効率化されます。

### Allowlist controls
- 管理者は、開発者が利用できる MCP サーバーをより詳細に監視できるようになりました。
- 注意: これらの機能は初期のパブリックプレビューであり、フィードバックを収集する過程で進化する可能性があります。現在の実施は MCP サーバー名のマッチングに基づいており、追加の検証とより詳細なポリシーオプションが将来のリリースで計画されています。

### For admins: Configure registry controls
- 許可リストコントロールは、Copilot Business および Copilot Enterprise のお客様のみが利用できます。
- 新しい AI Controls タブの GitHub Enterprise 設定で「MCP」を見つけます。または、組織レベルで、組織設定 → ポリシー → Copilot → ポリシー。
- Copilot で MCP サーバーを有効にします。
- MCP レジストリ URL を追加します。
- 実施モードを選択します: すべて許可(デフォルト): 開発者は任意の MCP サーバーを使用できます。レジストリサーバーは推奨として表示されます。 レジストリのみ: 開発者はレジストリのサーバーのみを実行できます。その他は実行時にブロックされます。
- すべて許可(デフォルト): 開発者は任意の MCP サーバーを使用できます。レジストリサーバーは推奨として表示されます。
- レジストリのみ: 開発者はレジストリのサーバーのみを実行できます。その他は実行時にブロックされます。
- 詳細なセットアップとレジストリフォーマットの仕様については、MCP セットアップドキュメントを参照してください。

### For developers: MCP registry in your IDE
- 表示される内容は、組織のポリシーによって異なります:
- すべて許可: すべてのサーバーが機能します。レジストリサーバーは簡単に検索できます。
- レジストリのみ: レジストリにないサーバーは実行時に警告付きでブロックされます。

### JetBrains IDEs (nightly)
- サインインして Copilot チャットを開き、MCP レジストリアイコンをクリックします。
- レジストリから MCP サーバーを参照、インストール、またはアンインストールします。
- オプションで、カスタムレジストリを使用するには、MCP レジストリ URL を設定をクリックします。

### Eclipse (prerelease)
- Copilot チャットパネルの上部バーで、MCP レジストリアイコンをクリックします。
- レジストリから MCP サーバーを参照、インストール、またはアンインストールします。
- オプションで、カスタムレジストリを使用するには、レジストリ URL を設定をクリックします。

### Xcode (prerelease)
- GitHub Copilot for Xcode を開いてサインインし、チャットパネルで MCP サーバーを設定をクリックします。
- MCP レジストリ URL の下で、MCP サーバーを参照... をクリックして、サーバーを表示および管理します。
- オプションで、カスタムレジストリを使用するには、URL を編集をクリックします。

### Installation
- JetBrains 向け Copilot の最新 nightly リリース、および Eclipse と Xcode 向け Copilot のプレリリースバージョンでこれを試すことができます。次のいずれかの場所からインストールしてください:
- GitHub Copilot for JetBrains IDEs (nightly)
- GitHub Copilot for Eclipse (prerelease)
- GitHub Copilot for Xcode (prerelease)
- また、有効な Copilot ライセンスも必要です。

### Share your feedback
- フィードバックをお待ちしています! 以下のチャネルを通じて体験を共有してください:
- GitHub Copilot for JetBrains IDEs
- GitHub Copilot for Eclipse
- GitHub Copilot for Xcode

## Impact / Who’s Affected
- MCP レジストリが IDE 内で直接利用可能になり、MCP サーバーの検索とインストールが効率化
- 管理者が許可リストコントロールで利用可能な MCP サーバーを制御可能
- すべて許可モードまたはレジストリのみモードを選択可能

## Caveats / Limitations
- Copilot Business および Copilot Enterprise のお客様が許可リストコントロールを利用可能
- JetBrains (nightly)、Eclipse (prerelease)、Xcode (prerelease) のユーザーが対象
- 機能は初期のパブリックプレビューで、進化する可能性があります

## Article Content (cleaned)
- 機能は初期のパブリックプレビューで、フィードバックを収集する過程で進化する可能性があります
- 現在の実施は MCP サーバー名のマッチングに基づいています
- 許可リストコントロールは Copilot Business および Copilot Enterprise のお客様のみが利用可能

## [What’s new](#whats-new)
- 追加の検証とより詳細なポリシーオプションが将来のリリースで計画されています
- レジストリフォーマットの仕様についてはドキュメントを参照

## [Set up your MCP registry](#set-up-your-mcp-registry)
エンタープライズおよび組織の管理者は、JetBrains、Eclipse、Xcode の nightly およびプレリリースビルドで、開発者が検索して使用できる MCP サーバーを設定できるようになりました。


## [Installation](#installation)


### [MCP registry](#mcp-registry)


MCP レジストリは、Model Context Protocol (MCP) サーバーのディレクトリです。JetBrains IDE、Eclipse、Xcode を使用する開発者は、IDE 内のレジストリから直接 MCP サーバーを参照してインストールでき、検索とセットアップが効率化されます。


### [Allowlist controls](#allowlist-controls)


管理者は、開発者が利用できる MCP サーバーをより詳細に監視できるようになりました。



> **注意:** これらの機能は初期のパブリックプレビューであり、フィードバックを収集する過程で進化する可能性があります。現在の実施は MCP サーバー名のマッチングに基づいており、追加の検証とより詳細なポリシーオプションが将来のリリースで計画されています。


### [For admins: Configure registry controls](#for-admins-configure-registry-controls)


許可リストコントロールは、Copilot Business および Copilot Enterprise のお客様のみが利用できます。


1. 新しい **AI Controls** タブの GitHub Enterprise 設定で「MCP」を見つけます。または、組織レベルで、**組織設定** → **ポリシー** → **Copilot** → **ポリシー**。
2. **Copilot で MCP サーバー**を有効にします。
3. MCP レジストリ URL を追加します。
4. 実施モードを選択します:
	* すべて許可(デフォルト): 開発者は任意の MCP サーバーを使用できます。レジストリサーバーは推奨として表示されます。
	* レジストリのみ: 開発者はレジストリのサーバーのみを実行できます。その他は実行時にブロックされます。


詳細なセットアップとレジストリフォーマットの仕様については、[MCP セットアップドキュメント](https://docs.github.com/copilot/how-tos/administer-copilot/configure-mcp-server-access?utm_source=changelog-docs-mcp-registry-allowlist&utm_medium=changelog&utm_campaign=universe25)を参照してください。


### [For developers: MCP registry in your IDE](#for-developers-mcp-registry-in-your-ide)


表示される内容は、組織のポリシーによって異なります:


* すべて許可: すべてのサーバーが機能します。レジストリサーバーは簡単に検索できます。
* レジストリのみ: レジストリにないサーバーは実行時に警告付きでブロックされます。


## [Share your feedback](#share-your-feedback)


### [JetBrains IDEs (nightly)](#jetbrains-ides-nightly)


1. サインインして Copilot チャットを開き、**MCP レジストリ**アイコンをクリックします。
2. レジストリから MCP サーバーを参照、インストール、またはアンインストールします。
3. オプションで、カスタムレジストリを使用するには、**MCP レジストリ URL を設定**をクリックします。


### [Eclipse (prerelease)](#eclipse-prerelease)


1. Copilot チャットパネルの上部バーで、**MCP レジストリ**アイコンをクリックします。
2. レジストリから MCP サーバーを参照、インストール、またはアンインストールします。
3. オプションで、カスタムレジストリを使用するには、**レジストリ URL を設定**をクリックします。


### [Xcode (prerelease)](#xcode-prerelease)


1. GitHub Copilot for Xcode を開いてサインインし、チャットパネルで **MCP サーバーを設定**をクリックします。
2. MCP レジストリ URL の下で、**MCP サーバーを参照...** をクリックして、サーバーを表示および管理します。
3. オプションで、カスタムレジストリを使用するには、**URL を編集**をクリックします。


## [Installation](#installation)


JetBrains 向け Copilot の最新 nightly リリース、および Eclipse と Xcode 向け Copilot のプレリリースバージョンでこれを試すことができます。次のいずれかの場所からインストールしてください:


* [GitHub Copilot for JetBrains IDEs (nightly)](http://aka.ms/copilot-jb-mcpreg-allowlist-preview)
* [GitHub Copilot for Eclipse (prerelease)](https://aka.ms/copilot-ecl-mcpreg-allowlist-preview)
* [GitHub Copilot for Xcode (prerelease)](http://aka.ms/copilot-xd-mcpreg-allowlist-preview)


また、有効な [Copilot ライセンス](https://github.com/features/copilot?utm_source=changelog-copilot-mcp-registry-allowlist&utm_medium=changelog&utm_campaign=universe25)も必要です。


## [Share your feedback](#share-your-feedback)


フィードバックをお待ちしています! 以下のチャネルを通じて体験を共有してください:


* [GitHub Copilot for JetBrains IDEs](https://github.com/microsoft/copilot-intellij-feedback/issues?utm_source=changelog-jetbrains-mcp-registry-allowlist&utm_medium=changelog&utm_campaign=universe25)
* [GitHub Copilot for Eclipse](https://github.com/microsoft/copilot-eclipse-feedback/issues?utm_source=changelog-eclipse-mcp-registry-allowlist&utm_medium=changelog&utm_campaign=universe25)
* [GitHub Copilot for Xcode](https://github.com/github/CopilotForXcode/issues?utm_source=changelog-xcode-mcp-registry-allowlist&utm_medium=changelog&utm_campaign=universe25)
