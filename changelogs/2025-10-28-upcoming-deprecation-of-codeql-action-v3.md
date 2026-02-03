---
title: "Upcoming deprecation of CodeQL Action v3"
date: "2025-10-28"
type: "deprecations"
labels: ["actions", "application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-upcoming-deprecation-of-codeql-action-v3"
fetched_at: "2026-02-03T14:40:06.444814Z"
---

# Upcoming deprecation of CodeQL Action v3

## Overview
On October 7, 2025, we released CodeQL Action v4, which runs on the Node.js 24 runtime. CodeQL Action v3 will be deprecated at the same time as GHES 3.19, which is currently scheduled for December 2026.

## Detailed Explanation
### Overview
- On October 7, 2025, we released CodeQL Action v4, which runs on the Node.js 24 runtime. CodeQL Action v3 will be deprecated at the same time as GHES 3.19, which is currently scheduled for December 2026.

### Default setup
- Users of code scanning default setup do not need to take any action in order to automatically move to CodeQL Action v4.

### Advanced setup
- Users of code scanning advanced setup need to change their workflow files in order to start using CodeQL Action v4.
- All users of GitHub code scanning (which by default uses the CodeQL analysis engine) on GitHub Actions on the following platforms should update their workflow files:
- github.com, including open source repositories as well as users of GitHub Teams and GitHub Enterprise Cloud
- GitHub Enterprise Server (GHES) 3.20 and newer
- Users of the above-mentioned platforms should update their CodeQL workflow files to refer to the new v4 version of the CodeQL Action. Note that the upcoming release of GitHub Enterprise Server 3.20 will ship with v4 of the CodeQL Action included.
- While GHES 3.19 does support Node.js 24 Actions, it does not ship with CodeQL Action v4. Users who want to migrate to v4 on GHES 3.19 should request that their system administrator enables GitHub Connect to download v4 onto GHES before updating their workflow files.
- GHES 3.18 and older versions do not support running Actions using the Node.js 24 runtime. They are therefore unable to run CodeQL Action v4. Please upgrade to a newer version of GitHub Enterprise Server prior to changing your CodeQL Action workflow files.

### Exactly what do I need to change?
- To upgrade to CodeQL Action v4, open your CodeQL workflow files in the .github directory of your repository and look for references to:
- github/codeql-action/init@v3
- github/codeql-action/autobuild@v3
- github/codeql-action/analyze@v3
- github/codeql-action/upload-sarif@v3
- These entries need to be replaced with their v4 equivalents:
- github/codeql-action/init@v4
- github/codeql-action/autobuild@v4
- github/codeql-action/analyze@v4
- github/codeql-action/upload-sarif@v4

### Can I use Dependabot to help me with this upgrade?
- Yes, you can! For more details, see our docs on how to configure Dependabot to automatically upgrade your Actions dependencies .

### What happens in December 2026?
- In December 2026, CodeQL Action v3 will be officially deprecated (at the same time as the GHES 3.19 deprecation). At that point, no new updates will be made to CodeQL Action v3, which means that new CodeQL analysis capabilities will only be available to users of CodeQL Action v4. We will keep a close eye on the migration progress across GitHub. If many workflow files still refer to CodeQL Action v3, we might consider scheduling one or more brownout moments later in the year to increase awareness.

## Impact / Who’s Affected
- CodeQL Action v3 will be deprecated at the same time as GHES 3.19, which is currently scheduled for December 2026.
- In December 2026, CodeQL Action v3 will be officially deprecated (at the same time as the GHES 3.19 deprecation).
- At that point, no new updates will be made to CodeQL Action v3, which means that new CodeQL analysis capabilities will only be available to users of CodeQL Action v4.

## Caveats / Limitations
- Note that the upcoming release of GitHub Enterprise Server 3.20 will ship with v4 of the CodeQL Action included.
- At that point, no new updates will be made to CodeQL Action v3, which means that new CodeQL analysis capabilities will only be available to users of CodeQL Action v4.

## Insights (derived from article language)
- Advanced setup Users of code scanning advanced setup need to change their workflow files in order to start using CodeQL Action v4.
- Note that the upcoming release of GitHub Enterprise Server 3.20 will ship with v4 of the CodeQL Action included.
- For more details, see our docs on how to configure Dependabot to automatically upgrade your Actions dependencies .
- If many workflow files still refer to CodeQL Action v3, we might consider scheduling one or more brownout moments later in the year to increase awareness.

## Article Content (cleaned)
On October 7, 2025, we released CodeQL Action v4, which runs on the Node.js 24 runtime. CodeQL Action v3 will be deprecated at the same time as GHES 3\.19, which is currently scheduled for December 2026\.


## [How does this affect me?](#how-does-this-affect-me)


### [Default setup](#default-setup)


Users of [code scanning default setup](https://docs.github.com/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning) do not need to take any action in order to automatically move to CodeQL Action v4\.


### [Advanced setup](#advanced-setup)


Users of [code scanning advanced setup](https://docs.github.com/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning) need to change their workflow files in order to start using CodeQL Action v4\.


#### [Users of github.com and GitHub Enterprise Server 3\.20 and newer](#users-of-github-com-and-github-enterprise-server-3-20-and-newer)


All users of GitHub code scanning (which by default uses the CodeQL analysis engine) on GitHub Actions on the following platforms should update their workflow files:


* github.com, including open source repositories as well as users of GitHub Teams and GitHub Enterprise Cloud
* GitHub Enterprise Server (GHES) 3\.20 and newer


Users of the above\-mentioned platforms should update their CodeQL workflow files to refer to the new v4 version of the CodeQL Action. Note that the upcoming release of GitHub Enterprise Server 3\.20 will ship with v4 of the CodeQL Action included.


#### [Users of GitHub Enterprise Server 3\.19](#users-of-github-enterprise-server-3-19)


While GHES 3\.19 **does** support Node.js 24 Actions, it **does not** ship with CodeQL Action v4\. Users who want to migrate to v4 on GHES 3\.19 should request that their system administrator enables [GitHub Connect](https://docs.github.com/enterprise-server@3.11/admin/github-actions/managing-access-to-actions-from-githubcom/using-the-latest-version-of-the-official-bundled-actions#using-github-connect-to-access-the-latest-actions) to download v4 onto GHES before updating their workflow files.


#### [Users of GitHub Enterprise Server 3\.18 and older](#users-of-github-enterprise-server-3-18-and-older)


GHES 3\.18 and older versions do not support running Actions using the Node.js 24 runtime. They are therefore unable to run CodeQL Action v4\. Please upgrade to a newer version of GitHub Enterprise Server prior to changing your CodeQL Action workflow files.


## [Exactly what do I need to change?](#exactly-what-do-i-need-to-change)


To upgrade to CodeQL Action v4, open your CodeQL workflow files in the `.github` directory of your repository and look for references to:


* `github/codeql-action/init@v3`
* `github/codeql-action/autobuild@v3`
* `github/codeql-action/analyze@v3`
* `github/codeql-action/upload-sarif@v3`


These entries need to be replaced with their v4 equivalents:


* `github/codeql-action/init@v4`
* `github/codeql-action/autobuild@v4`
* `github/codeql-action/analyze@v4`
* `github/codeql-action/upload-sarif@v4`


## [Can I use Dependabot to help me with this upgrade?](#can-i-use-dependabot-to-help-me-with-this-upgrade)


Yes, you can! For more details, see [our docs on how to configure Dependabot to automatically upgrade your Actions dependencies](https://docs.github.com/code-security/dependabot/working-with-dependabot/keeping-your-actions-up-to-date-with-dependabot).


## [What happens in December 2026?](#what-happens-in-december-2026)


In December 2026, CodeQL Action v3 will be officially deprecated (at the same time as the GHES 3\.19 deprecation). At that point, no new updates will be made to CodeQL Action v3, which means that new CodeQL analysis capabilities will only be available to users of CodeQL Action v4\. We will keep a close eye on the migration progress across GitHub. If many workflow files still refer to CodeQL Action v3, we might consider scheduling one or more brownout moments later in the year to increase awareness.
