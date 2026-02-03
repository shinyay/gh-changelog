---
title: "New GitHub Actions OIDC token claims"
date: "2025-11-13"
type: "improvements"
labels: ["actions"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-13-github-actions-oidc-token-claims-now-include-check_run_id"
fetched_at: "2026-02-03T14:40:06.113074Z"
---

# New GitHub Actions OIDC token claims

## Overview
GitHub Actions OpenID Connect (OIDC) token claims now include check_run_id

## Detailed Explanation
### Overview
- GitHub Actions OpenID Connect (OIDC) token claims now include check_run_id
- This enhancement enables fine-grained, attribute-based access control and improves auditability for workflows that integrate with external services. Platform teams often need to correlate an OIDC token back to the specific job and compute that generated it for compliance and traceability. For example, when workflows call internal services hosted on Azure, teams need to link the token to the job run for auditing. Previously, the token lacked a way to identify the exact job. With check_run_id alongside existing claims like run_id and run_attempt , you can now:
- Trace tokens to the exact job and compute that executed the request.
- Implement least-privilege policies without enumerating every repository.
- Reduce secret exposure risk and accelerate revocation.
- Improve compliance and audit workflows by mapping access to governed repository states.
- For more information on OIDC and how to configure the token, see our documentation .

## Article Content (cleaned)
GitHub Actions OpenID Connect (OIDC) token claims now include `check_run_id`


This enhancement enables fine\-grained, attribute\-based access control and improves auditability for workflows that integrate with external services. Platform teams often need to correlate an OIDC token back to the specific job and compute that generated it for compliance and traceability. For example, when workflows call internal services hosted on Azure, teams need to link the token to the job run for auditing. Previously, the token lacked a way to identify the exact job. With `check_run_id` alongside existing claims like `run_id` and `run_attempt`, you can now:


* Trace tokens to the exact job and compute that executed the request.
* Implement least\-privilege policies without enumerating every repository.
* Reduce secret exposure risk and accelerate revocation.
* Improve compliance and audit workflows by mapping access to governed repository states.


For more information on OIDC and how to configure the token, see our [documentation](https://docs.github.com/actions/concepts/security/openid-connect).
