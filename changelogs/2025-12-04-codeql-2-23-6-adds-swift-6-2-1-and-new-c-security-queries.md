---
title: "CodeQL 2.23.6 adds Swift 6.2.1 and new C# security queries"
date: "2025-12-04"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-04-codeql-2-23-6-adds-swift-6-2-1-and-new-c-security-queries"
fetched_at: "2026-02-03T14:50:55.066341Z"
---

# CodeQL 2.23.6 adds Swift 6.2.1 and new C# security queries

## Overview
CodeQL is the static analysis engine behind GitHub code scanning , which finds and remediates security issues in your code. We’ve recently released CodeQL 2.23.6 , which adds support for Swift 6.2.1, promotes two C# cookie security queries, and includes various accuracy improvements across languages.

## Detailed Explanation
### Overview
- CodeQL is the static analysis engine behind GitHub code scanning , which finds and remediates security issues in your code. We’ve recently released CodeQL 2.23.6 , which adds support for Swift 6.2.1, promotes two C# cookie security queries, and includes various accuracy improvements across languages.

### Language and framework support
- Swift : CodeQL now supports analysis of apps built with Swift 6.2.1.
- Rust : We’ve added models for cookie methods in the poem crate.

### Query changes
- C# : The cs/web/cookie-secure-not-set and cs/web/cookie-httponly-not-set queries have been promoted from experimental to the main query pack. These queries detect cookies created without proper security attributes. We’ve improved the Guards library for recognizing disjunctions, resulting in improved precision for cs/constant-condition , cs/inefficient-containskey , and cs/dereferenced-value-may-be-null queries.
- Rust : We’ve added taint flow barriers to the rust/regex-injection , rust/sql-injection , and rust/log-injection queries, reducing the frequency of false positive results.
- Java/Kotlin : We’ve reduced the security-severity score of java/overly-large-range and java/insecure-cookie from 5.0 to 4.0 to better reflect their impact.
- JavaScript/TypeScript : We’ve increased the security-severity score of js/xss-through-dom from 6.1 to 7.8 to align with other XSS queries, and reduced the score of js/overly-large-range from 5.0 to 4.0.
- Python : We’ve reduced the security-severity score of py/overly-large-range from 5.0 to 4.0 to better reflect its impact.
- Ruby : We’ve reduced the security-severity score of rb/overly-large-range from 5.0 to 4.0 to better reflect its impact.
- The cs/web/cookie-secure-not-set and cs/web/cookie-httponly-not-set queries have been promoted from experimental to the main query pack. These queries detect cookies created without proper security attributes.
- We’ve improved the Guards library for recognizing disjunctions, resulting in improved precision for cs/constant-condition , cs/inefficient-containskey , and cs/dereferenced-value-may-be-null queries.
- For a full list of changes, please refer to the complete changelog for version 2.23.6 . Every new version of CodeQL is automatically deployed to users of GitHub code scanning on github.com. The new functionality in CodeQL 2.23.6 will also be included in GitHub Enterprise Server (GHES) 3.20 release. If you use an older version of GHES, you can manually upgrade your CodeQL version .

## Key Changes
- C# : The cs/web/cookie-secure-not-set and cs/web/cookie-httponly-not-set queries have been promoted from experimental to the main query pack. These queries detect cookies created without proper security attributes. We’ve improved the Guards library for recognizing disjunctions, resulting in improved precision for cs/constant-condition , cs/inefficient-containskey , and cs/dereferenced-value-may-be-null queries.
- Rust : We’ve added taint flow barriers to the rust/regex-injection , rust/sql-injection , and rust/log-injection queries, reducing the frequency of false positive results.
- Java/Kotlin : We’ve reduced the security-severity score of java/overly-large-range and java/insecure-cookie from 5.0 to 4.0 to better reflect their impact.
- JavaScript/TypeScript : We’ve increased the security-severity score of js/xss-through-dom from 6.1 to 7.8 to align with other XSS queries, and reduced the score of js/overly-large-range from 5.0 to 4.0.
- Python : We’ve reduced the security-severity score of py/overly-large-range from 5.0 to 4.0 to better reflect its impact.
- Ruby : We’ve reduced the security-severity score of rb/overly-large-range from 5.0 to 4.0 to better reflect its impact.
- The cs/web/cookie-secure-not-set and cs/web/cookie-httponly-not-set queries have been promoted from experimental to the main query pack. These queries detect cookies created without proper security attributes.
- We’ve improved the Guards library for recognizing disjunctions, resulting in improved precision for cs/constant-condition , cs/inefficient-containskey , and cs/dereferenced-value-may-be-null queries.
- For a full list of changes, please refer to the complete changelog for version 2.23.6 . Every new version of CodeQL is automatically deployed to users of GitHub code scanning on github.com. The new functionality in CodeQL 2.23.6 will also be included in GitHub Enterprise Server (GHES) 3.20 release. If you use an older version of GHES, you can manually upgrade your CodeQL version .

## Impact / Who’s Affected
- Query changes C# : The cs/web/cookie-secure-not-set and cs/web/cookie-httponly-not-set queries have been promoted from experimental to the main query pack.

## Caveats / Limitations
- Query changes C# : The cs/web/cookie-secure-not-set and cs/web/cookie-httponly-not-set queries have been promoted from experimental to the main query pack.

## Article Content (cleaned)
CodeQL is the static analysis engine behind [GitHub code scanning](https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql), which finds and remediates security issues in your code. We’ve recently released [CodeQL 2\.23\.6](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.6/), which adds support for Swift 6\.2\.1, promotes two C\# cookie security queries, and includes various accuracy improvements across languages.


## [Language and framework support](#language-and-framework-support)


* **Swift**: CodeQL now supports analysis of apps built with Swift 6\.2\.1\.
* **Rust**: We’ve added models for cookie methods in the `poem` crate.


## [Query changes](#query-changes)


* **C\#**:
	+ The `cs/web/cookie-secure-not-set` and `cs/web/cookie-httponly-not-set` queries have been promoted from experimental to the main query pack. These queries detect cookies created without proper security attributes.
	+ We’ve improved the Guards library for recognizing disjunctions, resulting in improved precision for `cs/constant-condition`, `cs/inefficient-containskey`, and `cs/dereferenced-value-may-be-null` queries.
* **Rust**: We’ve added taint flow barriers to the `rust/regex-injection`, `rust/sql-injection`, and `rust/log-injection` queries, reducing the frequency of false positive results.
* **Java/Kotlin**: We’ve reduced the `security-severity` score of `java/overly-large-range` and `java/insecure-cookie` from 5\.0 to 4\.0 to better reflect their impact.
* **JavaScript/TypeScript**: We’ve increased the `security-severity` score of `js/xss-through-dom` from 6\.1 to 7\.8 to align with other XSS queries, and reduced the score of `js/overly-large-range` from 5\.0 to 4\.0\.
* **Python**: We’ve reduced the `security-severity` score of `py/overly-large-range` from 5\.0 to 4\.0 to better reflect its impact.
* **Ruby**: We’ve reduced the `security-severity` score of `rb/overly-large-range` from 5\.0 to 4\.0 to better reflect its impact.


For a full list of changes, please refer to the complete [changelog for version 2\.23\.6](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.6/). Every new version of CodeQL is automatically deployed to users of GitHub code scanning on github.com. The new functionality in CodeQL 2\.23\.6 will also be included in GitHub Enterprise Server (GHES) 3\.20 release. If you use an older version of GHES, you can [manually upgrade your CodeQL version](https://docs.github.com/enterprise-server@3.17/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access).
