---
title: "CodeQL 2.23.7 and 2.23.8 add security queries for Go and Rust"
date: "2025-12-18"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-18-codeql-2-23-7-and-2-23-8-add-security-queries-for-go-and-rust"
fetched_at: "2026-02-03T14:40:05.304384Z"
---

# CodeQL 2.23.7 and 2.23.8 add security queries for Go and Rust

## Overview
CodeQL is the static analysis engine behind GitHub’s Code Scanning and Code Quality products, which find and remediate issues relating to code quality and security. We’ve recently released CodeQL 2.23.7 and 2.23.8 . These releases bring new security queries for Go and Rust, improved overall analysis accuracy, and framework updates across several languages.

## Detailed Explanation
### Overview
- CodeQL is the static analysis engine behind GitHub’s Code Scanning and Code Quality products, which find and remediate issues relating to code quality and security. We’ve recently released CodeQL 2.23.7 and 2.23.8 . These releases bring new security queries for Go and Rust, improved overall analysis accuracy, and framework updates across several languages.

### Query changes
- Go
- Added a new query, go/cookie-secure-not-set , to detect cookies without the Secure flag set, potentially leading to sensitive information exposure.
- Added a new query, go/weak-crypto-algorithm , to detect the use of broken or weak cryptographic algorithms.
- Added a new query, go/weak-sensitive-data-hashing , to detect the use of broken or weak cryptographic hash algorithms on sensitive data.
- The go/cookie-http-only-not-set query has been promoted from the experimental query pack, to identify cookies that do not use the HttpOnly flag, potentially leading to cross-site scripting vulnerabilities.  This query was originally contributed by GitHub user @edvraa.
- Rust
- Added a new query, rust/xss , to detect cross-site scripting security vulnerabilities.
- Added a new query, rust/disabled-certificate-check , to detect disabled TLS certificate checks.
- Added three example queries ( rust/examples/empty-if , rust/examples/simple-sql-injection , and rust/examples/simple-constant-password ) to help you learn to write CodeQL queries for Rust.

### Language and framework support
- Java/Kotlin
- Java analysis no longer forces --source and --target compiler flags for Maven builds. Maven will now use the project’s own compiler configuration, improving build compatibility.
- Operations that extract only a fixed-length prefix or suffix of a string (like substring in Java or take in Kotlin), when limited to 7 characters or fewer, will now be treated as sanitizers for the java/sensitive-log query, given the contents of the log message will be truncated.
- JavaScript/TypeScript
- Fixed a bug in the Next.js model that caused the analysis to miss server-side taint sources in the app/pages folder.
- Rust
- The rust/access-invalid-pointer query has been improved with new flow sources and barriers.
- C#
- Compilation errors are now included in the debug log when using buildless analysis (which is used by default).
- Added a new extractor option to specify a custom directory for dependency downloads in buildless mode.  Use -O buildless_dependency_dir=<path> to configure the target directory.
- Python
- Fixed a bug in the Python extractor’s import handling where failing to find an import in find_module would cause a KeyError to be raised. This is a contribution from GitHub user @akoeplinger to the open-source CodeQL repository.
- For a full list of changes, refer to the complete changelogs for versions 2.23.7 and 2.23.8 . Every new version of CodeQL is automatically deployed to users of GitHub Code Scanning and GitHub Code Quality on GitHub.com. The features and fixes introduced in these releases will be included in GitHub Enterprise Server (GHES) version 3.20. If you use an older version of GHES, you can manually upgrade your CodeQL version .

## Key Changes
- Go
- Added a new query, go/cookie-secure-not-set , to detect cookies without the Secure flag set, potentially leading to sensitive information exposure.
- Added a new query, go/weak-crypto-algorithm , to detect the use of broken or weak cryptographic algorithms.
- Added a new query, go/weak-sensitive-data-hashing , to detect the use of broken or weak cryptographic hash algorithms on sensitive data.
- The go/cookie-http-only-not-set query has been promoted from the experimental query pack, to identify cookies that do not use the HttpOnly flag, potentially leading to cross-site scripting vulnerabilities.  This query was originally contributed by GitHub user @edvraa.
- Rust
- Added a new query, rust/xss , to detect cross-site scripting security vulnerabilities.
- Added a new query, rust/disabled-certificate-check , to detect disabled TLS certificate checks.
- Added three example queries ( rust/examples/empty-if , rust/examples/simple-sql-injection , and rust/examples/simple-constant-password ) to help you learn to write CodeQL queries for Rust.

## Impact / Who’s Affected
- The go/cookie-http-only-not-set query has been promoted from the experimental query pack, to identify cookies that do not use the HttpOnly flag, potentially leading to cross-site scripting vulnerabilities.
- Operations that extract only a fixed-length prefix or suffix of a string (like substring in Java or take in Kotlin), when limited to 7 characters or fewer, will now be treated as sanitizers for the java/sensitive-log query, given the contents of the log message will be truncated.

## Caveats / Limitations
- The go/cookie-http-only-not-set query has been promoted from the experimental query pack, to identify cookies that do not use the HttpOnly flag, potentially leading to cross-site scripting vulnerabilities.
- Operations that extract only a fixed-length prefix or suffix of a string (like substring in Java or take in Kotlin), when limited to 7 characters or fewer, will now be treated as sanitizers for the java/sensitive-log query, given the contents of the log message will be truncated.

## Article Content (cleaned)
CodeQL is the static analysis engine behind GitHub’s [Code Scanning](https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql) and [Code Quality](https://docs.github.com/code-security/code-quality/concepts/about-code-quality) products, which find and remediate issues relating to code quality and security. We’ve recently released [CodeQL 2\.23\.7 and 2\.23\.8](https://codeql.github.com/docs/codeql-overview/codeql-changelog/). These releases bring new security queries for Go and Rust, improved overall analysis accuracy, and framework updates across several languages.


## [Query changes](#query-changes)


**Go**


* Added a new query, `go/cookie-secure-not-set`, to detect cookies without the `Secure` flag set, potentially leading to sensitive information exposure.
* Added a new query, `go/weak-crypto-algorithm`, to detect the use of broken or weak cryptographic algorithms.
* Added a new query, `go/weak-sensitive-data-hashing`, to detect the use of broken or weak cryptographic hash algorithms on sensitive data.
* The `go/cookie-http-only-not-set` query has been promoted from the experimental query pack, to identify cookies that do not use the `HttpOnly` flag, potentially leading to cross\-site scripting vulnerabilities. This query was originally contributed by GitHub user @edvraa.


**Rust**


* Added a new query, `rust/xss`, to detect cross\-site scripting security vulnerabilities.
* Added a new query, `rust/disabled-certificate-check`, to detect disabled TLS certificate checks.
* Added three example queries (`rust/examples/empty-if`, `rust/examples/simple-sql-injection`, and `rust/examples/simple-constant-password`) to help you learn to write CodeQL queries for Rust.


## [Language and framework support](#language-and-framework-support)


**Java/Kotlin**


* Java analysis no longer forces `--source` and `--target` compiler flags for Maven builds. Maven will now use the project’s own compiler configuration, improving build compatibility.
* Operations that extract only a fixed\-length prefix or suffix of a string (like `substring` in Java or `take` in Kotlin), when limited to 7 characters or fewer, will now be treated as sanitizers for the `java/sensitive-log` query, given the contents of the log message will be truncated.


**JavaScript/TypeScript**


* Fixed a bug in the Next.js model that caused the analysis to miss server\-side taint sources in the `app/pages` folder.


**Rust**


* The `rust/access-invalid-pointer` query has been improved with new flow sources and barriers.


**C\#**


* Compilation errors are now included in the debug log when using [buildless analysis](https://docs.github.com/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages#codeql-build-modes) (which is used by default).
* Added a new extractor option to specify a custom directory for dependency downloads in buildless mode. Use `-O buildless_dependency_dir=<path>` to configure the target directory.


**Python**


* Fixed a bug in the Python extractor’s import handling where failing to find an import in `find_module` would cause a `KeyError` to be raised. This is a [contribution](https://github.com/github/codeql/pull/20908) from GitHub user @akoeplinger to the open\-source CodeQL repository.




---


For a full list of changes, refer to the complete changelogs for versions [2\.23\.7](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.7/) and [2\.23\.8](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.23.8/). Every new version of CodeQL is automatically deployed to users of GitHub Code Scanning and GitHub Code Quality on GitHub.com. The features and fixes introduced in these releases will be included in GitHub Enterprise Server (GHES) version 3\.20\. If you use an older version of GHES, you can [manually upgrade your CodeQL version](https://docs.github.com/enterprise-server@3.18/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access).
