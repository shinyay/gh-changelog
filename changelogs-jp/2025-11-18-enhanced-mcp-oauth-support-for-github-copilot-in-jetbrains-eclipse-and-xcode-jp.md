---
title: "JetBrains、Eclipse、Xcode用GitHub CopilotでMCP OAuth対応を強化"
date: "2025-11-18"
type: "improvements"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-18-enhanced-mcp-oauth-support-for-github-copilot-in-jetbrains-eclipse-and-xcode"
fetched_at: "2026-02-03T14:50:55.198967Z"
lang: "ja"
---

# JetBrains、Eclipse、Xcode用GitHub CopilotでMCP OAuth対応を強化

## Overview
JetBrains、Eclipse、Xcode用のGitHub Copilotプラグインに、Dynamic Client Registration（DCR）とフォールバックメカニズムを使用した、より多くのサードパーティOAuthプロバイダーをサポートする、安全で柔軟なアプローチによる強化された認証機能を導入しました。

## Detailed Explanation
### Overview
- JetBrains、Eclipse、Xcode用のGitHub Copilotプラグインに、Dynamic Client Registration（DCR）とフォールバックメカニズムを使用した、より多くのサードパーティOAuthプロバイダーをサポートする、安全で柔軟なアプローチによる強化された認証機能を導入しました。

### What's new
- JetBrains、Eclipse、Xcode用のGitHub CopilotプラグインがOAuth 2.0およびOAuth 2.1標準を使用して、GitHub MCPサーバーを超えた、より多くのアイデンティティプロバイダー（IdP）の認証をサポートするようになりました。
- MCPはまず、クライアントの自動セットアップのためにDynamic Client Registration（DCR）ハンドシェイクを試みます。IdPがDCRをサポートしていない場合、Copilotはクライアントクレデンシャルワークフローにフォールバックし、静的なクライアントIDとシークレットを手動で構成できるようにします。これらの改善により、開発者はセキュリティとコンプライアンスを維持しながら、エンタープライズIdPまたはカスタムアイデンティティサービスを統合する柔軟性が高まります。

### Try it out
- これらの機能強化はプレビュー段階で、すべてのJetBrains IDE、Eclipse、Xcodeユーザーに本日から利用可能です。最新バージョンにプラグインまたはアプリを更新する必要があり、有効なCopilotライセンスも必要です。
- MCP認証の詳細については、公式ドキュメントをご参照ください。

### Share your feedback
- フィードバックをお待ちしています！以下のチャネルで経験を共有してください：– GitHub Copilot for JetBrains IDEs – GitHub Copilot for Eclipse – GitHub Copilot for Xcode

## Insights (derived from article language)
- MCP認証の詳細については、公式ドキュメントをご参照ください。

## Article Content (cleaned)
JetBrains、Eclipse、Xcode用のGitHub Copilotプラグインに、Dynamic Client Registration（DCR）とフォールバックメカニズムを使用した、より多くのサードパーティOAuthプロバイダーをサポートする、安全で柔軟なアプローチによる強化された認証機能を導入しました。


## [What's new](#whats-new)


JetBrains、Eclipse、Xcode用のGitHub CopilotプラグインがOAuth 2.0およびOAuth 2.1標準を使用して、GitHub MCPサーバーを超えた、より多くのアイデンティティプロバイダー（IdP）の認証をサポートするようになりました。


MCPはまず、クライアントの自動セットアップのためにDynamic Client Registration（DCR）ハンドシェイクを試みます。IdPがDCRをサポートしていない場合、Copilotはクライアントクレデンシャルワークフローにフォールバックし、静的なクライアントIDとシークレットを手動で構成できるようにします。これらの改善により、開発者はセキュリティとコンプライアンスを維持しながら、エンタープライズIdPまたはカスタムアイデンティティサービスを統合する柔軟性が高まります。


## [Try it out](#try-it-out)


これらの機能強化はプレビュー段階で、すべての[JetBrains IDE](https://plugins.jetbrains.com/plugin/17718-github-copilot)、[Eclipse](https://marketplace.eclipse.org/content/github-copilot)、[Xcode](https://github.com/github/copilotforXcode/)ユーザーに本日から利用可能です。最新バージョンにプラグインまたはアプリを更新する必要があり、有効な[Copilotライセンス](https://github.com/features/copilot)も必要です。


MCP認証の詳細については、公式[ドキュメント](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)をご参照ください。


## [Share your feedback](#share-your-feedback)


フィードバックをお待ちしています！以下のチャネルで経験を共有してください：  

– [GitHub Copilot for JetBrains IDEs](https://github.com/microsoft/copilot-intellij-feedback/issues)  

– [GitHub Copilot for Eclipse](https://github.com/microsoft/copilot-eclipse-feedback/issues)  

– [GitHub Copilot for Xcode](https://github.com/github/CopilotForXcode/issues)
