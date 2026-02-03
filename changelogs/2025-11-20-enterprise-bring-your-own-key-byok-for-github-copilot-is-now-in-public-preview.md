---
title: "Enterprise bring your own key (BYOK) for GitHub Copilot is now in public preview"
date: "2025-11-20"
type: "new releases"
labels: ["copilot"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-11-20-enterprise-bring-your-own-key-byok-for-github-copilot-is-now-in-public-preview"
fetched_at: "2026-02-03T14:40:05.920420Z"
---

# Enterprise bring your own key (BYOK) for GitHub Copilot is now in public preview

## Overview
Enterprise developers have asked for more flexibility in how they use Copilot. Many teams already work with specific large language model (LLM) providers and maintain custom models tailored to their needs. Copilot has long provided high‑quality GitHub‑hosted models by default, but until now, teams could not connect their own organization’s preferred models directly.

## Detailed Explanation
### Overview
- Enterprise developers have asked for more flexibility in how they use Copilot. Many teams already work with specific large language model (LLM) providers and maintain custom models tailored to their needs. Copilot has long provided high‑quality GitHub‑hosted models by default, but until now, teams could not connect their own organization’s preferred models directly.
- Bring your own key (BYOK) now makes it possible to connect API keys from supported providers including Anthropic, Microsoft Foundry, OpenAI, and xAI to GitHub Copilot. Once connected, all models tied to that key can be used in Copilot Chat on GitHub.com and in supported IDEs. Usage through BYOK is billed directly by your chosen provider and does not count against GitHub Copilot request quotas. This allows teams to take advantage of existing contracts or credits while keeping access managed at the organization or enterprise level.

### Here’s what’s new
- Connect your provider’s API key to Copilot Enterprise admins can add API keys at the enterprise level, and organization admins can add keys at the organization level. Connecting a key lets you choose models from the linked provider for use with GitHub Copilot.
- Manage models centrally Once models are available through a connected key, enterprise admins decide which organizations in the enterprise can use them. Organization admins configure access within their organization. Both enterprise and organization admins can enable, disable, and configure models from a single settings area. This centralized control ensures consistent setup and allows teams to quickly adapt as needs change.
- Use BYOK models in supported IDEs BYOK is available in Agent, Plan, Ask, and Edit modes in the latest releases of Visual Studio Code, JetBrains IDEs, Eclipse, and Xcode.
- Billing handled by your provider API calls made through BYOK are billed according to your provider’s terms and do not count against GitHub Copilot usage quotas. You can use your existing credits or enterprise agreements with your provider.

### Known limitation
- BYOK does not support the OpenAI Responses API . Models configured to use a Responses endpoint will not work. BYOK requires the OpenAI Completions API.

### Start using BYOK today
- BYOK is available now in public preview for GitHub Enterprise and Business customers. Connect your LLM provider’s API key in your enterprise or organization settings and start using your models in Copilot Chat and supported IDEs. Learn more by visiting our documentation .

### Help us shape the future
- We are just getting started and your feedback will help guide what comes next. Join the discussion within the GitHub Community to share feedback and connect with other developers.

## Impact / Who’s Affected
- BYOK requires the OpenAI Completions API.
- Start using BYOK today BYOK is available now in public preview for GitHub Enterprise and Business customers.

## Caveats / Limitations
- BYOK requires the OpenAI Completions API.

## Insights (derived from article language)
- BYOK requires the OpenAI Completions API.
- Learn more by visiting our documentation .

## Article Content (cleaned)
Enterprise developers have asked for more flexibility in how they use Copilot. Many teams already work with specific large language model (LLM) providers and maintain custom models tailored to their needs. Copilot has long provided high‑quality GitHub‑hosted models by default, but until now, teams could not connect their own organization’s preferred models directly.


Bring your own key (BYOK) now makes it possible to connect API keys from supported providers including Anthropic, Microsoft Foundry, OpenAI, and xAI to GitHub Copilot. Once connected, all models tied to that key can be used in Copilot Chat on GitHub.com and in supported IDEs. Usage through BYOK is billed directly by your chosen provider and does not count against GitHub Copilot request quotas. This allows teams to take advantage of existing contracts or credits while keeping access managed at the organization or enterprise level.



### [Here’s what’s new](#heres-whats-new)


**Connect your provider’s API key to Copilot**  

Enterprise admins can add API keys at the enterprise level, and organization admins can add keys at the organization level. Connecting a key lets you choose models from the linked provider for use with GitHub Copilot.


**Manage models centrally**  

Once models are available through a connected key, enterprise admins decide which organizations in the enterprise can use them. Organization admins configure access within their organization. Both enterprise and organization admins can enable, disable, and configure models from a single settings area. This centralized control ensures consistent setup and allows teams to quickly adapt as needs change.


**Use BYOK models in supported IDEs**  

BYOK is available in Agent, Plan, Ask, and Edit modes in the latest releases of Visual Studio Code, JetBrains IDEs, Eclipse, and Xcode.


**Billing handled by your provider**  

API calls made through BYOK are billed according to your provider’s terms and do not count against GitHub Copilot usage quotas. You can use your existing credits or enterprise agreements with your provider.


### [Known limitation](#known-limitation)


BYOK does not support the OpenAI [Responses API](https://platform.openai.com/docs/api-reference/responses). Models configured to use a Responses endpoint will not work. BYOK requires the OpenAI Completions API.


### [Start using BYOK today](#start-using-byok-today)


BYOK is available now in public preview for GitHub Enterprise and Business customers. Connect your LLM provider’s API key in your enterprise or organization settings and start using your models in Copilot Chat and supported IDEs. Learn more by visiting our [documentation](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-your-own-api-keys).


### [Help us shape the future](#help-us-shape-the-future)


We are just getting started and your feedback will help guide what comes next. Join the discussion within the [GitHub Community](https://github.com/orgs/community/discussions/179954) to share feedback and connect with other developers.
