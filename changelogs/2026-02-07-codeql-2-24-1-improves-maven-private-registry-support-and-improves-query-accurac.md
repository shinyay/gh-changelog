---
title: "CodeQL 2.24.1 improves Maven private registry support and improves query accuracy"
date: "2026-02-07"
type: "Improvement"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-02-06-codeql-2-24-1-improves-maven-private-registry-support-and-improves-query-accuracy"
fetched_at: "2026-02-07T07:18:40.680515Z"
---

# CodeQL 2.24.1 improves Maven private registry support and improves query accuracy

## Overview
CodeQL is the static analysis engine behind GitHub code scanning , which finds and remediates security issues in your code. We’ve recently released CodeQL 2.24.1 , improving support for Maven private package registries,  support for the latest version of Kotlin, and various other improvements that enhance the accuracy of your code scanning results.

## Detailed Explanation
### Overview
- CodeQL is the static analysis engine behind GitHub code scanning , which finds and remediates security issues in your code. We’ve recently released CodeQL 2.24.1 , improving support for Maven private package registries,  support for the latest version of Kotlin, and various other improvements that enhance the accuracy of your code scanning results.

### Language and framework support
- Java/Kotlin
- Kotlin versions up to 2.3.0 are now supported for analysis.
- We’ve added support for Struts 7.x package names in the Struts framework library.
- When you configure Maven-compatible private package registries for an organization for Default Setup, CodeQL will now configure Maven to also use these as plugin repositories, allowing you to obtain Maven plugins from private registries.
- Note : As previously announced , support for Kotlin 1.6.x and 1.7.x series has been dropped.
- C/C++
- We’ve added support for C23 and C++26 #embed preprocessor directives.
- C#
- C# 14: We’ve added support for null-conditional assignments.
- Python
- It’s now possible to refer to list elements in the Python models-as-data language, via the ListElement path.
- We’ve added taint flow and type models for the agents and openai modules, and have modeled remote flow sources for the websockets package.

### Query changes
- C/C++
- We’ve fixed a bug in the GuardCondition library which sometimes prevented binary logical operators from being recognized as guard conditions. As a result, queries using GuardCondition may see improved results.
- We’ve improved accuracy of measuring buffer sizes, reducing the number of false positives in the cpp/static-buffer-overflow , cpp/overflow-buffer , cpp/badly-bounded-write , cpp/overrunning-write , cpp/overrunning-write-with-float , and cpp/very-likely-overrunning-write queries.
- Java
- We’ve improved the accuracy of the java/unreleased-lock query.
- Python
- We’ve added an experimental query py/prompt-injection to detect potential prompt injection vulnerabilities in code using LLMs.
- GitHub Actions
- We’ve fixed a crash when analyzing a ${{ ... }} expression over around 300 characters in length.
- For a full list of changes, please refer to the complete changelog for version 2.24.1 . Every new version of CodeQL is automatically deployed to users of GitHub code scanning on github.com. The new functionality in CodeQL 2.24.1 will also be included in a future GitHub Enterprise Server (GHES) release. If you use an older version of GHES, you can manually upgrade your CodeQL version .

## Key Changes
- C/C++
- We’ve fixed a bug in the GuardCondition library which sometimes prevented binary logical operators from being recognized as guard conditions. As a result, queries using GuardCondition may see improved results.
- We’ve improved accuracy of measuring buffer sizes, reducing the number of false positives in the cpp/static-buffer-overflow , cpp/overflow-buffer , cpp/badly-bounded-write , cpp/overrunning-write , cpp/overrunning-write-with-float , and cpp/very-likely-overrunning-write queries.
- Java
- We’ve improved the accuracy of the java/unreleased-lock query.
- Python
- We’ve added an experimental query py/prompt-injection to detect potential prompt injection vulnerabilities in code using LLMs.
- GitHub Actions
- We’ve fixed a crash when analyzing a ${{ ... }} expression over around 300 characters in length.
- For a full list of changes, please refer to the complete changelog for version 2.24.1 . Every new version of CodeQL is automatically deployed to users of GitHub code scanning on github.com. The new functionality in CodeQL 2.24.1 will also be included in a future GitHub Enterprise Server (GHES) release. If you use an older version of GHES, you can manually upgrade your CodeQL version .

## Impact / Who’s Affected
- Language and framework support Java/Kotlin Kotlin versions up to 2.3.0 are now supported for analysis.

## Caveats / Limitations
- Note : As previously announced , support for Kotlin 1.6.x and 1.7.x series has been dropped.

## Article Content (cleaned)
CodeQL is the static analysis engine behind [GitHub code scanning](https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql), which finds and remediates security issues in your code. We’ve recently released [CodeQL 2\.24\.1](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.24.1/), improving support for Maven private package registries, support for the latest version of Kotlin, and various other improvements that enhance the accuracy of your code scanning results.


## [Language and framework support](https://github.blog/changelog/feed/#language-and-framework-support)


**Java/Kotlin**


* Kotlin versions up to 2\.3\.0 are now supported for analysis.
* We’ve added support for Struts 7\.x package names in the Struts framework library.
* When you configure Maven\-compatible private package registries for an organization for Default Setup, CodeQL will now configure Maven to also use these as plugin repositories, allowing you to obtain Maven plugins from private registries.
* **Note**: [As previously announced](https://github.blog/changelog/2026-01-20-codeql-2-23-9-has-been-released/), support for Kotlin 1\.6\.x and 1\.7\.x series has been dropped.


**C/C\+\+**


* We’ve added support for C23 and C\+\+26 `#embed` preprocessor directives.


**C\#**


* C\# 14: We’ve added support for null\-conditional assignments.


**Python**


* It’s now possible to refer to list elements in the Python models\-as\-data language, via the `ListElement` path.
* We’ve added taint flow and type models for the `agents` and `openai` modules, and have modeled remote flow sources for the `websockets` package.


## [Query changes](https://github.blog/changelog/feed/#query-changes)


**C/C\+\+**


* We’ve fixed a bug in the `GuardCondition` library which sometimes prevented binary logical operators from being recognized as guard conditions. As a result, queries using `GuardCondition` may see improved results.
* We’ve improved accuracy of measuring buffer sizes, reducing the number of false positives in the `cpp/static-buffer-overflow`, `cpp/overflow-buffer`, `cpp/badly-bounded-write`, `cpp/overrunning-write`, `cpp/overrunning-write-with-float`, and `cpp/very-likely-overrunning-write` queries.


**Java**


* We’ve improved the accuracy of the `java/unreleased-lock` query.


**Python**


* We’ve added an experimental query `py/prompt-injection` to detect potential prompt injection vulnerabilities in code using LLMs.


**GitHub Actions**


* We’ve fixed a crash when analyzing a `${{ ... }}` expression over around 300 characters in length.


For a full list of changes, please refer to the complete [changelog for version 2\.24\.1](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.24.1/). Every new version of CodeQL is automatically deployed to users of GitHub code scanning on github.com. The new functionality in CodeQL 2\.24\.1 will also be included in a future GitHub Enterprise Server (GHES) release. If you use an older version of GHES, you can [manually upgrade your CodeQL version](https://docs.github.com/enterprise-server@3.19/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access).
