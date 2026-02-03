---
title: "CodeQL 2.24.0 adds Swift 6.2 and .NET 10 support, and improves file handling for minified JavaScript"
date: "2026-01-29"
type: "Improvement"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-29-codeql-2-24-0-adds-swift-6-2-support-net-10-compatibility-and-file-handling-for-minified-javascript"
fetched_at: "2026-02-03T14:40:04.767297Z"
---

# CodeQL 2.24.0 adds Swift 6.2 and .NET 10 support, and improves file handling for minified JavaScript

## Overview
CodeQL is the static analysis engine behind GitHub code scanning , which finds and remediates security issues in your code. We’ve recently released CodeQL 2.24.0 , which adds support for new language versions, expands framework coverage, and improves query accuracy across multiple languages.

## Detailed Explanation
### Overview
- CodeQL is the static analysis engine behind GitHub code scanning , which finds and remediates security issues in your code. We’ve recently released CodeQL 2.24.0 , which adds support for new language versions, expands framework coverage, and improves query accuracy across multiple languages.

### Language and framework support
- Swift
- We’ve updated CodeQL to support analysis of apps built with Swift 6.2.2 and 6.2.3.
- C#
- We’ve added support for .NET 10 and C# 14.
- JavaScript/TypeScript
- CodeQL now treats JavaScript files with an average line length greater than 200 as minified and won’t analyze them. For scenarios where minified JavaScript files should be analyzed, you can set the environment variable CODEQL_EXTRACTOR_JAVASCRIPT_ALLOW_MINIFIED_FILES=true .
- We’ve added support for Next.js 16’s use cache directives.
- We’ve added support for the React useRef hook, with improved data flow tracking through the current property.
- Python
- The py/decompression-bomb query now supports the compression.zstd library (added in Python 3.14).
- We’ve added taint flow models for urllib.parse and remote flow sources for the python-socketio package.
- The extractor now analyzes files in hidden directories by default.
- Java/Kotlin
- We’ve added sink models for com.couchbase supporting SQL injection and hardcoded credentials queries.
- We’ve added more dataflow models of org.apache.commons.fileupload.FileItem , javax/jakarta.servlet.http.Part , and org.apache.commons.fileupload.util.Streams .
- C/C++
- We’ve added support for more Windows APIs, including file read functions, command-line and environment variable APIs, and flow models for SQLite and OpenSSL libraries.
- Rust
- Method resolution now considers the Deref trait, which means method calls on receivers implementing the Deref trait will correctly resolve to methods defined on the target type.
- We’ve added support for the Axum web application framework.
- We’ve improved type inference for raw pointers, including type inference for the raw borrow operators and dereferencing of raw pointers.

### Query changes
- C#
- We’ve extended the Missing cross-site request forgery token validation query to support ASP.NET Core.
- We’ve added NHibernate.ISession.CreateSQLQuery , NHibernate.IStatelessSession.CreateSQLQuery , and NHibernate.Impl.AbstractSessionImpl.CreateSQLQuery as SQL injection sinks.
- We’ve added implicit reads of System.Collections.Generic.KeyValuePair.Value at taint-tracking sinks and at inputs to additional taint steps. As a result, taint-tracking queries will now produce more results when a container is tainted.
- JavaScript/TypeScript
- We’ve fixed a bug in the Next.js model that would cause the analysis to miss server-side taint sources in files named route or page appearing outside api and pages folders.
- new Response(x) is no longer seen as a reflected XSS sink when no content-type header is set, since the content type defaults to text/plain .
- Java/Kotlin
- Java thread safety analysis now understands initialization to thread-safe classes inside constructors.
- We’ve added a sanitizer to java/ssrf to remove alerts when a regular expression check verifies that the value is safe.
- URI template variables of all Spring RestTemplate methods are now considered as request forgery sinks, which may lead to more alerts for the query java/ssrf .
- C/C++
- We’ve improved the accuracy of the cpp/constant-comparison query to reduce false positives.
- Rust
- We’ve improved the accuracy of the rust/unused-variable , rust/unused-value , rust/access-invalid-pointer , and rust/access-after-lifetime-ended queries to reduce false positives.
- We’ve extended the rust/hard-coded-cryptographic-value query with new heuristic sinks identifying passwords, initialization vectors, nonces, and salts.
- For a full list of changes, please refer to the complete changelog for version 2.24.0 . Every new version of CodeQL is automatically deployed to users of GitHub code scanning on github.com. The new functionality in CodeQL 2.24.0 will also be included in a future GitHub Enterprise Server (GHES) release. If you use an older version of GHES, you can manually upgrade your CodeQL version .

## Key Changes
- C#
- We’ve extended the Missing cross-site request forgery token validation query to support ASP.NET Core.
- We’ve added NHibernate.ISession.CreateSQLQuery , NHibernate.IStatelessSession.CreateSQLQuery , and NHibernate.Impl.AbstractSessionImpl.CreateSQLQuery as SQL injection sinks.
- We’ve added implicit reads of System.Collections.Generic.KeyValuePair.Value at taint-tracking sinks and at inputs to additional taint steps. As a result, taint-tracking queries will now produce more results when a container is tainted.
- JavaScript/TypeScript
- We’ve fixed a bug in the Next.js model that would cause the analysis to miss server-side taint sources in files named route or page appearing outside api and pages folders.
- new Response(x) is no longer seen as a reflected XSS sink when no content-type header is set, since the content type defaults to text/plain .
- Java/Kotlin
- Java thread safety analysis now understands initialization to thread-safe classes inside constructors.
- We’ve added a sanitizer to java/ssrf to remove alerts when a regular expression check verifies that the value is safe.
- URI template variables of all Spring RestTemplate methods are now considered as request forgery sinks, which may lead to more alerts for the query java/ssrf .
- C/C++
- We’ve improved the accuracy of the cpp/constant-comparison query to reduce false positives.
- Rust
- We’ve improved the accuracy of the rust/unused-variable , rust/unused-value , rust/access-invalid-pointer , and rust/access-after-lifetime-ended queries to reduce false positives.
- We’ve extended the rust/hard-coded-cryptographic-value query with new heuristic sinks identifying passwords, initialization vectors, nonces, and salts.
- For a full list of changes, please refer to the complete changelog for version 2.24.0 . Every new version of CodeQL is automatically deployed to users of GitHub code scanning on github.com. The new functionality in CodeQL 2.24.0 will also be included in a future GitHub Enterprise Server (GHES) release. If you use an older version of GHES, you can manually upgrade your CodeQL version .

## Insights (derived from article language)
- Rust Method resolution now considers the Deref trait, which means method calls on receivers implementing the Deref trait will correctly resolve to methods defined on the target type.
- URI template variables of all Spring RestTemplate methods are now considered as request forgery sinks, which may lead to more alerts for the query java/ssrf .

## Article Content (cleaned)
CodeQL is the static analysis engine behind [GitHub code scanning](https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql), which finds and remediates security issues in your code. We’ve recently released [CodeQL 2\.24\.0](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.24.0/), which adds support for new language versions, expands framework coverage, and improves query accuracy across multiple languages.


## [Language and framework support](https://github.blog/changelog/feed/#language-and-framework-support)


**Swift**


* We’ve updated CodeQL to support analysis of apps built with Swift 6\.2\.2 and 6\.2\.3\.


**C\#**


* We’ve added support for .NET 10 and C\# 14\.


**JavaScript/TypeScript**


* CodeQL now treats JavaScript files with an average line length greater than 200 as minified and won’t analyze them. For scenarios where minified JavaScript files should be analyzed, you can set the environment variable `CODEQL_EXTRACTOR_JAVASCRIPT_ALLOW_MINIFIED_FILES=true`.
* We’ve added support for Next.js 16’s `use cache` directives.
* We’ve added support for the React `useRef` hook, with improved data flow tracking through the `current` property.


**Python**


* The `py/decompression-bomb` query now supports the `compression.zstd` library (added in Python 3\.14\).
* We’ve added taint flow models for `urllib.parse` and remote flow sources for the `python-socketio` package.
* The extractor now analyzes files in hidden directories by default.


**Java/Kotlin**


* We’ve added sink models for `com.couchbase` supporting SQL injection and hardcoded credentials queries.
* We’ve added more dataflow models of `org.apache.commons.fileupload.FileItem`, `javax/jakarta.servlet.http.Part`, and `org.apache.commons.fileupload.util.Streams`.


**C/C\+\+**


* We’ve added support for more Windows APIs, including file read functions, command\-line and environment variable APIs, and flow models for SQLite and OpenSSL libraries.


**Rust**


* Method resolution now considers the `Deref` trait, which means method calls on receivers implementing the `Deref` trait will correctly resolve to methods defined on the target type.
* We’ve added support for the Axum web application framework.
* We’ve improved type inference for raw pointers, including type inference for the raw borrow operators and dereferencing of raw pointers.


## [Query changes](https://github.blog/changelog/feed/#query-changes)


**C\#**


* We’ve extended the `Missing cross-site request forgery token validation` query to support ASP.NET Core.
* We’ve added `NHibernate.ISession.CreateSQLQuery`, `NHibernate.IStatelessSession.CreateSQLQuery`, and `NHibernate.Impl.AbstractSessionImpl.CreateSQLQuery` as SQL injection sinks.
* We’ve added implicit reads of `System.Collections.Generic.KeyValuePair.Value` at taint\-tracking sinks and at inputs to additional taint steps. As a result, taint\-tracking queries will now produce more results when a container is tainted.


**JavaScript/TypeScript**


* We’ve fixed a bug in the Next.js model that would cause the analysis to miss server\-side taint sources in files named `route` or `page` appearing outside `api` and `pages` folders.
* `new Response(x)` is no longer seen as a reflected XSS sink when no `content-type` header is set, since the content type defaults to `text/plain`.


**Java/Kotlin**


* Java thread safety analysis now understands initialization to thread\-safe classes inside constructors.
* We’ve added a sanitizer to `java/ssrf` to remove alerts when a regular expression check verifies that the value is safe.
* URI template variables of all Spring `RestTemplate` methods are now considered as request forgery sinks, which may lead to more alerts for the query `java/ssrf`.


**C/C\+\+**


* We’ve improved the accuracy of the `cpp/constant-comparison` query to reduce false positives.


**Rust**


* We’ve improved the accuracy of the `rust/unused-variable`, `rust/unused-value`, `rust/access-invalid-pointer`, and `rust/access-after-lifetime-ended` queries to reduce false positives.
* We’ve extended the `rust/hard-coded-cryptographic-value` query with new heuristic sinks identifying passwords, initialization vectors, nonces, and salts.


For a full list of changes, please refer to the complete [changelog for version 2\.24\.0](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.24.0/). Every new version of CodeQL is automatically deployed to users of GitHub code scanning on github.com. The new functionality in CodeQL 2\.24\.0 will also be included in a future GitHub Enterprise Server (GHES) release. If you use an older version of GHES, you can [manually upgrade your CodeQL version](https://docs.github.com/enterprise-server@3.19/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access).
