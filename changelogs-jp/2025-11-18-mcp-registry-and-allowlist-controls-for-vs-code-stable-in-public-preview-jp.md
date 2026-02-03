---
title: "VS Code Stable向けMCPレジストリと許可リストコントロールがパブリックプレビューに"
date: "2025-11-18"
type: "improvements"
labels: ["copilot", "platform governance"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-18-internal-mcp-registry-and-allowlist-controls-for-vs-code-stable-in-public-preview"
fetched_at: "2026-02-03T14:50:55.263280Z"
lang: "ja"
---

# VS Code Stable向けMCPレジストリと許可リストコントロールがパブリックプレビューに

## Overview
エンタープライズおよび組織の管理者は、最新リリースのVS StableでMCPレジストリを構成し、許可リストポリシーを実施できるようになり、これらのガバナンスコントロールが大多数のCopilotユーザーに提供されます。さらに、最新バージョンのVisual StudioがレジストリDiscoveryをサポートし、実施機能は今後のリリースで提供されます。

## Detailed Explanation
### Overview
- エンタープライズおよび組織の管理者は、最新リリースのVS Code StableでMCPレジストリを構成し、許可リストポリシーを実施できるようになり、これらのガバナンスコントロールが大多数のCopilotユーザーに提供されます。さらに、最新バージョンのVisual StudioがレジストリDiscoveryをサポートし、実施機能は今後のリリースで提供されます。

### Understanding MCP registries and allowlists
- MCPレジストリはMCPサーバーのカタログです。GitHub管理者は、エンタープライズまたは組織のCopilotポリシーページで内部レジストリのURLをアップロードできます。レジストリには2つの目的があります：
- Discovery：承認されたMCPサーバーをMCP互換のCopilotホストアプリケーション（VS CodeのCopilotなど）で表示し、簡単にインストールできるようにします。
- 許可リスト：Registry-onlyポリシーと組み合わせると、内部レジストリで定義されていないMCPサーバーの使用（実行時）を防ぎます。
- アップロードされたレジストリを推奨ベンダーリストと考え、「Restrict MCP access to registry servers」ポリシーがそのリストを厳格に実施するか、単に推奨するかを決定します。

### Setting up your registry
- MCPレジストリは次のいくつかの方法でホストできます：
- Azure API Center：動的なレジストリ管理とエンタープライズMCPガバナンス機能を備えたMicrosoftのマネージドAzure API Centerサービスを使用できます。
- セルフホスティング：オープンソースのMCP Registryをフォークしてセルフホストするか、URLルーティングをサポートする独自のカスタム実装を公開できます。セルフホストレジストリはv0.1 MCPレジストリ仕様に従う必要があります。レジストリは必要なエンドポイントをサポートし、適切なCORSヘッダーを含める必要があります。

### Current availability
- VS Code Stableで完全なエクスペリエンスが利用可能になりました：– レジストリサーバーがMCPサーバーサイドバーパネルに表示されます。 – Registry-onlyポリシーがレジストリにないサーバーを実行時に積極的にブロックします。 – どの組織またはエンタープライズが制限を実施しているかを示す明確なポリシーメッセージが表示されます。
- Visual StudioがGitHub.comで構成された内部MCPレジストリをサポートするようになりました：– レジストリサーバーがDiscovery用のMCPサーバーインターフェイスに表示されます。 – 許可リストの実施はまだ利用できません。ポリシー設定に関係なく、すべてのサーバーを実行できます。
- このVS Code Stableリリースにより、MCPガバナンスコントロールが大多数のCopilotユーザーに提供され、エンタープライズと組織が開発者ベース全体で会社のポリシーを実施できるようになります。Visual Studioユーザーは、内部レジストリを通じて承認されたサーバーを発見し始めることができ、許可リスト実施のサポートは今後のリリースで提供されます。
- Copilotホストアプリケーション別のサポート状況については、会社でのMCP使用のサポートサーフェスを参照してください。

### Policy options
- MCPアクセスポリシーを構成する際、2つの選択肢があります：
- すべて許可（デフォルト）：レジストリサーバーが推奨として表示されますが、開発者は任意のMCPサーバーを使用できます。
- レジストリのみ：開発者はレジストリにリストされているサーバーのみを使用できます。その他はすべて明確なポリシーメッセージでブロックされます。
- ローカルとリモートサーバーの実施：リモートMCPサーバーは、サーバー名とリモートインストールURLの両方に対して検証され、厳格な実施を提供します。ローカルサーバーの実施は現在、サーバー名のみに対して検証されるため、構成をローカルで編集できます。厳格なセキュリティ要件を持つエンタープライズの場合、レジストリにリモートサーバーのみを構成することをお勧めします。

### Getting started
- この機能はCopilot BusinessおよびCopilot Enterpriseのお客様が利用できます。VS Code Stableサポートにより、組織全体でMCPガバナンスコントロールをより広く展開および実施できるようになりました。
- セットアップ手順とレジストリフォーマット仕様については、組織またはエンタープライズのMCPレジストリの構成を参照してください。

## Impact / Who's Affected
- 許可リスト：Registry-onlyポリシーと組み合わせると、内部レジストリで定義されていないMCPサーバーの使用（実行時）を防ぎます。
- Current availability VS Code Stableで完全なエクスペリエンスが利用可能になりました：– レジストリサーバーがMCPサーバーサイドバーパネルに表示されます。 – Registry-onlyポリシーがレジストリにないサーバーを実行時に積極的にブロックします。 – どの組織またはエンタープライズが制限を実施しているかを示す明確なポリシーメッセージが表示されます。
- レジストリのみ：開発者はレジストリにリストされているサーバーのみを使用できます。
- ローカルサーバーの実施は現在、サーバー名のみに対して検証されるため、構成をローカルで編集できます。
- 厳格なセキュリティ要件を持つエンタープライズの場合、レジストリにリモートサーバーのみを構成することをお勧めします。

## Caveats / Limitations
- 許可リスト：Registry-onlyポリシーと組み合わせると、内部レジストリで定義されていないMCPサーバーの使用（実行時）を防ぎます。
- Current availability VS Code Stableで完全なエクスペリエンスが利用可能になりました：– レジストリサーバーがMCPサーバーサイドバーパネルに表示されます。 – Registry-onlyポリシーがレジストリにないサーバーを実行時に積極的にブロックします。 – どの組織またはエンタープライズが制限を実施しているかを示す明確なポリシーメッセージが表示されます。
- レジストリのみ：開発者はレジストリにリストされているサーバーのみを使用できます。
- ローカルサーバーの実施は現在、サーバー名のみに対して検証されるため、構成をローカルで編集できます。
- 厳格なセキュリティ要件を持つエンタープライズの場合、レジストリにリモートサーバーのみを構成することをお勧めします。

## Insights (derived from article language)
- 厳格なセキュリティ要件を持つエンタープライズの場合、レジストリにリモートサーバーのみを構成することをお勧めします。

## Article Content (cleaned)
エンタープライズおよび組織の管理者は、[最新リリースのVS Code Stable](https://code.visualstudio.com/updates/v1_106#_mcp-server-access-for-your-organization)でMCPレジストリを構成し、許可リストポリシーを実施できるようになり、これらのガバナンスコントロールが大多数のCopilotユーザーに提供されます。さらに、[最新バージョンのVisual Studio](https://learn.microsoft.com/en-us/visualstudio/releases/2026/release-notes)がレジストリDiscoveryをサポートし、実施機能は今後のリリースで提供されます。


## [Understanding MCP registries and allowlists](#understanding-mcp-registries-and-allowlists)


MCPレジストリはMCPサーバーのカタログです。GitHub管理者は、エンタープライズまたは組織のCopilotポリシーページで内部レジストリのURLをアップロードできます。レジストリには2つの目的があります：


* **Discovery**：承認されたMCPサーバーをMCP互換のCopilotホストアプリケーション（VS CodeのCopilotなど）で表示し、簡単にインストールできるようにします。
* **許可リスト**：Registry-onlyポリシーと組み合わせると、内部レジストリで定義されていないMCPサーバーの使用（実行時）を防ぎます。


アップロードされたレジストリを推奨ベンダーリストと考え、「Restrict MCP access to registry servers」ポリシーがそのリストを厳格に実施するか、単に推奨するかを決定します。


## [Setting up your registry](#setting-up-your-registry)


MCPレジストリは次のいくつかの方法でホストできます：


* **Azure API Center**：動的なレジストリ管理とエンタープライズMCPガバナンス機能を備えたMicrosoftのマネージド[Azure API Center](https://learn.microsoft.com/azure/api-center/overview)サービスを使用できます。
* **セルフホスティング**：オープンソースの[MCP Registry](https://github.com/modelcontextprotocol/registry)をフォークしてセルフホストするか、URLルーティングをサポートする独自のカスタム実装を公開できます。セルフホストレジストリは[v0.1 MCPレジストリ仕様](https://registry.modelcontextprotocol.io/docs)に従う必要があります。レジストリは必要なエンドポイントをサポートし、適切なCORSヘッダーを含める必要があります。


## [Current availability](#current-availability)


**VS Code Stable**で完全なエクスペリエンスが利用可能になりました：  

– レジストリサーバーがMCPサーバーサイドバーパネルに表示されます。  

– Registry-onlyポリシーがレジストリにないサーバーを実行時に積極的にブロックします。  

– どの組織またはエンタープライズが制限を実施しているかを示す明確なポリシーメッセージが表示されます。


**Visual Studio**がGitHub.comで構成された内部MCPレジストリをサポートするようになりました：  

– レジストリサーバーがDiscovery用のMCPサーバーインターフェイスに表示されます。  

– 許可リストの実施はまだ利用できません。ポリシー設定に関係なく、すべてのサーバーを実行できます。


このVS Code Stableリリースにより、MCPガバナンスコントロールが大多数のCopilotユーザーに提供され、エンタープライズと組織が開発者ベース全体で会社のポリシーを実施できるようになります。Visual Studioユーザーは、内部レジストリを通じて承認されたサーバーを発見し始めることができ、許可リスト実施のサポートは今後のリリースで提供されます。


Copilotホストアプリケーション別のサポート状況については、[会社でのMCP使用のサポートサーフェス](https://docs.github.com/en/copilot/concepts/mcp-management#supported-surfaces)を参照してください。


## [Policy options](#policy-options)


MCPアクセスポリシーを構成する際、2つの選択肢があります：


* **すべて許可**（デフォルト）：レジストリサーバーが推奨として表示されますが、開発者は任意のMCPサーバーを使用できます。
* **レジストリのみ**：開発者はレジストリにリストされているサーバーのみを使用できます。その他はすべて明確なポリシーメッセージでブロックされます。


**ローカルとリモートサーバーの実施**：リモートMCPサーバーは、サーバー名とリモートインストールURLの両方に対して検証され、厳格な実施を提供します。ローカルサーバーの実施は現在、サーバー名のみに対して検証されるため、構成をローカルで編集できます。厳格なセキュリティ要件を持つエンタープライズの場合、レジストリにリモートサーバーのみを構成することをお勧めします。


## [Getting started](#getting-started)


この機能はCopilot BusinessおよびCopilot Enterpriseのお客様が利用できます。VS Code Stableサポートにより、組織全体でMCPガバナンスコントロールをより広く展開および実施できるようになりました。


セットアップ手順とレジストリフォーマット仕様については、[組織またはエンタープライズのMCPレジストリの構成](https://docs.github.com/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-server-access)を参照してください。
