---
title: "CodeQL 2.23.5 adds support for Swift 6.2, new Java queries, and improved analysis accuracy"
date: "2025-11-19"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-19-codeql-2-23-5-adds-support-for-swift-6-2-new-java-queries-and-improved-analysis-accuracy"
fetched_at: "2026-02-03T14:50:55.179992Z"
---

# CodeQL 2.23.5 adds support for Swift 6.2, new Java queries, and improved analysis accuracy

## Overview
CodeQL is the static analysis engine behind GitHub code scanning, which finds and remediates security issues in your code. We’ve recently released CodeQL 2.23.5 , introducing three new Java security queries for detecting concurrency issues and improving the accuracy of your code scanning results.

## Detailed Explanation
### Overview
- CodeQL is the static analysis engine behind GitHub code scanning, which finds and remediates security issues in your code. We’ve recently released CodeQL 2.23.5 , introducing three new Java security queries for detecting concurrency issues and improving the accuracy of your code scanning results.
- Language and framework support
- Swift : CodeQL now supports Swift 6.2, ensuring you can analyze projects built with this version.
- Rust : We’ve added support for the actix-web web framework and extended support for the mysql and mysql_async libraries.
- C# : We’ve added tracer support for macOS and Linux when the .NET CLI ( dotnet ) directly invokes the C# compiler ( csc ), providing basic tracing and extraction capabilities for .NET 10 RC2 on these platforms.
- Query changes
- C#
- We’ve completely rewritten the cs/dereferenced-value-may-be-null query, which removes a very significant number of false positives. This query has also been changed from a path-problem query to a problem query, so paths are no longer reported.
- We’ve updated the cs/constant-condition query to report a wider range of high confidence results.
- We’ve improved the cs/web/missing-x-frame-options query, so it now correctly handles configuration nested in root “ elements.
- Java/Kotlin
- We’ve promoted the java/sensitive-cookie-not-httponly query from experimental to the main query pack.
- We’ve added three new queries to detect concurrency issues in classes marked as @ThreadSafe : java/escaping detects values escaping from thread-safe classes. java/not-threadsafe detects data races in thread-safe classes. java/safe-publication detects unsafe publication in thread-safe classes.
- Calls to String.matches are now treated as sanitizers for the java/ssrf query, which can reduce the occurrence of false positives.
- java/escaping detects values escaping from thread-safe classes.
- java/not-threadsafe detects data races in thread-safe classes.
- java/safe-publication detects unsafe publication in thread-safe classes.
- Python
- We’ve split the py/insecure-cookie query into multiple queries: py/insecure-cookie checks for cases where the Secure flag isn’t set. py/client-exposed-cookie checks for cases where the HttpOnly flag isn’t set. py/samesite-none checks for cases where the SameSite attribute is set to None .
- These queries now only alert when the cookie is detected to contain sensitive data.
- py/insecure-cookie checks for cases where the Secure flag isn’t set.
- py/client-exposed-cookie checks for cases where the HttpOnly flag isn’t set.
- py/samesite-none checks for cases where the SameSite attribute is set to None .
- For a full list of changes, refer to the complete changelog for version 2.23.5 .
- Availability
- Each new version of CodeQL is automatically deployed to users of GitHub code scanning on github.com. The new functionality in CodeQL 2.23.5 will also be included in GitHub Enterprise Server (GHES) release 3.20. If you use an older version of GHES, manually upgrade your CodeQL version .

## Impact / Who’s Affected
- Java/Kotlin We’ve promoted the java/sensitive-cookie-not-httponly query from experimental to the main query pack.
- Python We’ve split the py/insecure-cookie query into multiple queries: py/insecure-cookie checks for cases where the Secure flag isn’t set. py/client-exposed-cookie checks for cases where the HttpOnly flag isn’t set. py/samesite-none checks for cases where the SameSite attribute is set to None .
- These queries now only alert when the cookie is detected to contain sensitive data.

## Caveats / Limitations
- Java/Kotlin We’ve promoted the java/sensitive-cookie-not-httponly query from experimental to the main query pack.
- Python We’ve split the py/insecure-cookie query into multiple queries: py/insecure-cookie checks for cases where the Secure flag isn’t set. py/client-exposed-cookie checks for cases where the HttpOnly flag isn’t set. py/samesite-none checks for cases where the SameSite attribute is set to None .
- These queries now only alert when the cookie is detected to contain sensitive data.

## Article Content (cleaned)
CodeQL is the static analysis engine behind GitHub code scanning, which finds and remediates security issues in your code. We’ve recently released [CodeQL 2\.23\.5](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.5/), introducing three new Java security queries for detecting concurrency issues and improving the accuracy of your code scanning results.


**Language and framework support**


* **Swift**: CodeQL now supports Swift 6\.2, ensuring you can analyze projects built with this version.
* **Rust**: We’ve added support for the `actix-web` web framework and extended support for the `mysql` and `mysql_async` libraries.
* **C\#**: We’ve added tracer support for macOS and Linux when the .NET CLI (`dotnet`) directly invokes the C\# compiler (`csc`), providing basic tracing and extraction capabilities for .NET 10 RC2 on these platforms.


**Query changes**


**C\#**


* We’ve completely rewritten the `cs/dereferenced-value-may-be-null` query, which removes a very significant number of false positives. This query has also been changed from a `path-problem` query to a `problem` query, so paths are no longer reported.
* We’ve updated the `cs/constant-condition` query to report a wider range of high confidence results.
* We’ve improved the `cs/web/missing-x-frame-options` query, so it now correctly handles configuration nested in root “ elements.


**Java/Kotlin**


* We’ve promoted the `java/sensitive-cookie-not-httponly` query from experimental to the main query pack.
* We’ve added three new queries to detect concurrency issues in classes marked as `@ThreadSafe`:
	+ `java/escaping` detects values escaping from thread\-safe classes.
	+ `java/not-threadsafe` detects data races in thread\-safe classes.
	+ `java/safe-publication` detects unsafe publication in thread\-safe classes.
* Calls to `String.matches` are now treated as sanitizers for the `java/ssrf` query, which can reduce the occurrence of false positives.


**Python**


* We’ve split the `py/insecure-cookie` query into multiple queries:
	+ `py/insecure-cookie` checks for cases where the `Secure` flag isn’t set.
	+ `py/client-exposed-cookie` checks for cases where the `HttpOnly` flag isn’t set.
	+ `py/samesite-none` checks for cases where the `SameSite` attribute is set to `None`.
* These queries now only alert when the cookie is detected to contain sensitive data.


For a full list of changes, refer to the complete [changelog for version 2\.23\.5](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.5/).


**Availability**


Each new version of CodeQL is automatically deployed to users of GitHub code scanning on github.com. The new functionality in CodeQL 2\.23\.5 will also be included in GitHub Enterprise Server (GHES) release 3\.20\. If you use an older version of GHES, [manually upgrade your CodeQL version](https://docs.github.com/enterprise-server@3.18/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access).
