---
title: "Secrets in unlisted GitHub gists are reported to secret scanning partners"
date: "2025-11-25"
type: "improvements"
labels: ["application security"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-25-secrets-in-unlisted-github-gists-are-now-reported-to-secret-scanning-partners"
fetched_at: "2026-02-03T14:50:55.141909Z"
---

# Secrets in unlisted GitHub gists are reported to secret scanning partners

## Overview
Starting today, GitHub will report any publicly leaked secrets found in unlisted GitHub gists to the respective secret scanning partner.

## Detailed Explanation
### Overview
- Starting today, GitHub will report any publicly leaked secrets found in unlisted GitHub gists to the respective secret scanning partner.
- GitHub gists can be listed (denoted with a public label) or unlisted (denoted with a secret label).
- There is no such thing as a private GitHub gist , and all gists can be viewed by anyone with the URL. Due to this common misconception, secret gists represent a significant blind spot for leaked secrets. Secrets leaked in GitHub gists should be treated like any other publicly leaked secret.

### What is the secret scanning partnership program?
- To protect the developer community, GitHub partners with hundreds of secret scanning partners to identify leaked secrets.
- GitHub works directly with industry partners like AWS, OpenAI, and Stripe to build detectors for their specific secret formats, ensuring high accuracy and a low number of false positives. GitHub notifies the secret issuer when publicly leaked secrets are found, allowing the partner to take immediate action. For repositories where secret scanning is enabled, GitHub will also notify the developer with a secret scanning alert.

### What is a GitHub gist?
- Gists provide a simple way to share code snippets with others. If you are signed in to GitHub when you create a gist, the gist will be associated with your account, and you will see it in your list of gists when you navigate to your gist home page.
- Gists can be public or secret. Public gists show up in Discover, where people can browse new gists as they’re created. They’re also searchable, so you can use them if you’d like other people to find and see your work. Secret gists don’t show up in Discover and are not searchable unless you are logged in and are the author of the secret gist. Secret gists aren’t private; if you send the URL of a secret gist to a friend, they’ll be able to see it. However, if someone you don’t know discovers the URL, they’ll also be able to see your gist. If you need to keep your code away from prying eyes, you may want to create a private repository instead.
- Learn more about GitHub secret scanning , GitHub gists , and the GitHub secret scanning partnership program .

## Caveats / Limitations
- GitHub gists can be listed (denoted with a public label) or unlisted (denoted with a secret label).

## Insights (derived from article language)
- Learn more about GitHub secret scanning , GitHub gists , and the GitHub secret scanning partnership program .

## Article Content (cleaned)
Starting today, GitHub will report any publicly leaked secrets found in unlisted GitHub gists to the respective secret scanning partner.


GitHub gists can be listed (denoted with a `public` label) or unlisted (denoted with a `secret` label).


**There is no such thing as a private GitHub gist**, and all gists can be viewed by anyone with the URL. Due to this common misconception, `secret` gists represent a significant blind spot for leaked secrets. Secrets leaked in GitHub gists should be treated like any other publicly leaked secret.


### [What is the secret scanning partnership program?](#what-is-the-secret-scanning-partnership-program)


To protect the developer community, GitHub partners with hundreds of secret scanning partners to identify leaked secrets.


GitHub works directly with industry partners like AWS, OpenAI, and Stripe to build detectors for their specific secret formats, ensuring high accuracy and a low number of false positives. GitHub notifies the secret issuer when publicly leaked secrets are found, allowing the partner to take immediate action. For repositories where secret scanning is enabled, GitHub will also notify the developer with a secret scanning alert.


### [What is a GitHub gist?](#what-is-a-github-gist)


Gists provide a simple way to share code snippets with others. If you are signed in to GitHub when you create a gist, the gist will be associated with your account, and you will see it in your list of gists when you navigate to your gist home page.


Gists can be public or secret. Public gists show up in Discover, where people can browse new gists as they’re created. They’re also searchable, so you can use them if you’d like other people to find and see your work. Secret gists don’t show up in Discover and are not searchable unless you are logged in and are the author of the secret gist. Secret gists aren’t private; if you send the URL of a secret gist to a friend, they’ll be able to see it. However, if someone you don’t know discovers the URL, they’ll also be able to see your gist. If you need to keep your code away from prying eyes, you may want to create a private repository instead.


Learn more about [GitHub secret scanning](https://docs.github.com/enterprise-cloud@latest/code-security/secret-scanning/introduction/about-secret-scanning), [GitHub gists](https://docs.github.com/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists), and the [GitHub secret scanning partnership program](https://docs.github.com/code-security/secret-scanning/secret-scanning-partnership-program/secret-scanning-partner-program).
