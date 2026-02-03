---
title: "Update to GitHub Actions pricing"
date: "2025-12-16"
type: "new releases"
labels: ["actions"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-16-coming-soon-simpler-pricing-and-a-better-experience-for-github-actions"
fetched_at: "2026-02-03T14:50:54.926273Z"
---

# Update to GitHub Actions pricing

## Overview
We’ve read your posts and heard your feedback.

## Detailed Explanation
### Update:
- We’ve read your posts and heard your feedback.
- We’re postponing the announced billing change for self-hosted GitHub Actions to take time to re-evaluate our approach.
- We are continuing to reduce hosted-runners prices by up to 39% on January 1, 2026.
- We have real costs in running the Actions control plane. We are also making investments into self-hosted runners so they work at scale in customer environments, particularly for complex enterprise scenarios. While this context matters, we missed the mark with this change by not including more of you in our planning.
- We need to improve GitHub Actions. We’re taking more time to meet and listen closely to developers, customers, and partners to start. We’ve also opened a discussion to collect more direct feedback and will use that feedback to inform the GitHub Actions roadmap. We’re working hard to earn your trust through consistent delivery across GitHub Actions and the entire platform.

### Below is the original announcement from December 16, 2025:
- On January 1, 2026 , GitHub will reduce the price of GitHub-hosted runners by up to 39% depending on the machine type used . The free usage minute quotas will remain the same.
- On March 1, 2026, GitHub will introduce a new $0.002 per minute GitHub Actions cloud platform charge that will apply to self-hosted runner usage. Any usage subject to this charge will count toward the minutes included in your plan, as explained in our GitHub Actions billing documentation .
- Runner usage in public repositories will remain free. There will be no changes in price structure for GitHub Enterprise Server customers.

### Deeper investment in the Actions self-hosted experience
- We are increasing our investment into our self-hosted experience to ensure that we can provide autoscaling for scenarios beyond just Linux containers. This will include new approaches to scaling, new platform support, Windows support, and more as we move through the next 12 months.
- For more details about the product investments we’re making in Actions, please visit our Executive Insights page .

### FAQ
- Why am I being charged to use my own hardware? Historically, self-hosted runner customers were able to leverage much of GitHub Actions’ infrastructure and services at no cost. This meant that the cost of maintaining and evolving these essential services was largely being subsidized by the prices set for GitHub-hosted runners. By updating our pricing, we’re aligning costs more closely with usage and the value delivered to every Actions user,  while fueling further innovation and investment across the platform. The vast majority of users, especially individuals and small teams, will see no price increase.
- You can see the Actions pricing calculator to estimate your future costs.
- What are the new GitHub-hosted runner rates? See the GitHub Actions runner pricing reference for the updated rates that will go into effect on January 1, 2026. These listed rates include the new $0.002 per-minute Actions cloud platform charge.
- Why is .002/minute the right price for self-hosted runners on cloud? We determined per-minute was deemed the most fair and accurate by our users, and compared to other self-hosted CI solutions in the market. We believe this is a sustainable option that will not deeply impact our lightly- nor heavily-active customers, while still delivering fast, flexible workloads for the best end user experience.
- Which job execution scenarios for GitHub Actions are affected by this pricing change?
- Jobs that run in private repositories and use standard GitHub-hosted or self-hosted runners
- Any jobs running on larger GitHub-hosted runners
- Standard GitHub-hosted or self-hosted runner usage on public repositories will remain free. GitHub Enterprise Server pricing is not impacted by this change.
- When will this pricing change take effect?
- The price decrease for GitHub-hosted runners will take effect on January 1, 2026. The new charge for self-hosted runners will apply beginning on March 1, 2026. The price changes will impact all customers on these dates.
- Will the free usage quota available in my plan change? Beginning March 1, 2026, self-hosted runners will be included within your free usage quota, and will consume available usage based on list price the same way that Linux, Windows, and MacOS standard runners work today.
- Will self-hosted runner usage consume from my free usage minutes? Yes, billable self-hosted runner usage will be able to consume minutes from the free quota associated with your plan.
- How does this pricing change affect customers on GitHub Enterprise Server?
- This pricing change does not affect customers using GitHub Enterprise Server. Customers running Actions jobs on self-hosted runners on GitHub Enterprise Server may continue to host, manage, troubleshoot and use Actions on and in conjunction with their implementation free of charge.
- Can I bill my self-hosted runner usage on private repositories through Azure?
- Yes, as long as you have an active Azure subscription ID associated with your GitHub Enterprise or Organization(s).
- What is the overall impact of this change to GitHub customers?
- 96% of customers will see no change to their bill. Of the 4% of Actions users impacted by this change, 85% of this cohort will see their Actions bill decrease and the remaining 15% who are impacted across all face a median increase around $13.
- Did GitHub consider how this impacts individual developers, not just Enterprise scale customers of GitHub? From our individual users (free & Pro plans) of those who used GitHub Actions in the last month in private repos only 0.09% would end up with a price increase, with a median increase of under $2 a month. Note that this impact is after these users have made use of their included minutes in their plans today, entitling them to over 33 hours of included GitHub compute, and this has no impact on their free use of public repos. A further 2.8% of this total user base will see a decrease in their monthly cost as a result of these changes. The rest are unimpacted by this change.
- How can I figure out what my new monthly cost for Actions looks like?
- GitHub Actions provides detailed usage reports for the current and prior year . You can use this prior usage alongside the rate changes that will be introduced in January and March to estimate cost under the new pricing structure. We have created a Python script to help you leverage full usage reports to calculate your expected cost after the price updates.
- We have also updated our Actions pricing calculator , making it easier to estimate your future costs, particularly if your historical usage is limited or not representative of expected future usage.

### Recommended resources
- See the GitHub Actions runner pricing documentation for the new GitHub-hosted runner rates effective January 1, 2026.
- For more details on upcoming GitHub Actions releases, see the GitHub public roadmap .
- For help estimating your expected Actions usage cost, use the newly updated Actions pricing calculator .
- To see your current or historical Actions usage, see our documentation for viewing and downloading detailed usage reports .
- If you are interested in moving existing self-hosted runner usage to GitHub-hosted runners, see the SHR to GHR migration guide in our documentation.

## Impact / Who’s Affected
- From our individual users (free & Pro plans) of those who used GitHub Actions in the last month in private repos only 0.09% would end up with a price increase, with a median increase of under $2 a month.
- We have also updated our Actions pricing calculator , making it easier to estimate your future costs, particularly if your historical usage is limited or not representative of expected future usage.

## Caveats / Limitations
- From our individual users (free & Pro plans) of those who used GitHub Actions in the last month in private repos only 0.09% would end up with a price increase, with a median increase of under $2 a month.
- Note that this impact is after these users have made use of their included minutes in their plans today, entitling them to over 33 hours of included GitHub compute, and this has no impact on their free use of public repos.
- We have also updated our Actions pricing calculator , making it easier to estimate your future costs, particularly if your historical usage is limited or not representative of expected future usage.

## Insights (derived from article language)
- We’re taking more time to meet and listen closely to developers, customers, and partners to start.
- For more details about the product investments we’re making in Actions, please visit our Executive Insights page .
- Did GitHub consider how this impacts individual developers, not just Enterprise scale customers of GitHub?
- Note that this impact is after these users have made use of their included minutes in their plans today, entitling them to over 33 hours of included GitHub compute, and this has no impact on their free use of public repos.
- For more details on upcoming GitHub Actions releases, see the GitHub public roadmap .

## Article Content (cleaned)
## [Update:](#update)


**We’ve read your posts and heard your feedback.**


1. **We’re postponing the announced billing change for self\-hosted GitHub Actions to take time to re\-evaluate our approach.**
2. **We are continuing to reduce hosted\-runners prices by up to 39% on January 1, 2026\.**


**We have real costs in running the Actions control plane. We are also making investments into self\-hosted runners so they work at scale in customer environments, particularly for complex enterprise scenarios. While this context matters, we missed the mark with this change by not including more of you in our planning.**


**We need to improve GitHub Actions. We’re taking more time to meet and listen closely to developers, customers, and partners to start. We’ve also [opened a discussion to collect more direct feedback](https://github.com/orgs/community/discussions/182186) and will use that feedback to inform the GitHub Actions roadmap. We’re working hard to earn your trust through consistent delivery across GitHub Actions and the entire platform.**


## [Below is the original announcement from December 16, 2025:](#below-is-the-original-announcement-from-december-16-2025)


On **January 1, 2026**, GitHub will **reduce the price of GitHub\-hosted runners by up to 39%** [depending on the machine type used](https://docs.github.com/billing/reference/actions-runner-pricing). The free usage minute quotas will remain the same.


On **March 1, 2026,** GitHub will introduce a new **$0\.002 per minute GitHub Actions cloud platform charge** that will apply to self\-hosted runner usage. Any usage subject to this charge will count toward the minutes included in your plan, as explained in [our GitHub Actions billing documentation](https://docs.github.com/billing/concepts/product-billing/github-actions#free-use-of-github-actions).


Runner usage in public repositories will **remain free.** There will be no changes in price structure for GitHub Enterprise Server customers.


### [Deeper investment in the Actions self\-hosted experience](#deeper-investment-in-the-actions-self-hosted-experience)


We are increasing our investment into our self\-hosted experience to ensure that we can provide autoscaling for scenarios beyond just Linux containers. This will include new approaches to scaling, new platform support, Windows support, and more as we move through the next 12 months.


For more details about the product investments we’re making in Actions, please visit our [Executive Insights page](https://resources.github.com/actions/2026-pricing-changes-for-github-actions).


### [FAQ](#faq)


**Why am I being charged to use my own hardware?**  

Historically, self\-hosted runner customers were able to leverage much of GitHub Actions’ infrastructure and services at no cost. This meant that the cost of maintaining and evolving these essential services was largely being subsidized by the prices set for GitHub\-hosted runners. By updating our pricing, we’re aligning costs more closely with usage and the value delivered to every Actions user, while fueling further innovation and investment across the platform. The vast majority of users, especially individuals and small teams, will see no price increase.


You can see the [Actions pricing calculator](https://github.com/pricing/calculator#actions) to estimate your future costs.


**What are the new GitHub\-hosted runner rates?**  

See the GitHub Actions [runner pricing reference](https://docs.github.com/billing/reference/actions-runner-pricing) for the updated rates that will go into effect on January 1, 2026\. These listed rates include the new $0\.002 per\-minute Actions cloud platform charge.


**Why is .002/minute the right price for self\-hosted runners on cloud?**  

We determined per\-minute was deemed the most fair and accurate by our users, and compared to other self\-hosted CI solutions in the market. We believe this is a sustainable option that will not deeply impact our lightly\- nor heavily\-active customers, while still delivering fast, flexible workloads for the best end user experience.


**Which job execution scenarios for GitHub Actions are affected by this pricing change?**


* Jobs that run in private repositories and use standard GitHub\-hosted or self\-hosted runners
* Any jobs running on larger GitHub\-hosted runners


Standard GitHub\-hosted or self\-hosted runner usage on public repositories will remain free. GitHub Enterprise Server pricing is not impacted by this change.


**When will this pricing change take effect?**


The price decrease for GitHub\-hosted runners will take effect on January 1, 2026\. The new charge for self\-hosted runners will apply beginning on March 1, 2026\. The price changes will impact all customers on these dates.


**Will the free usage quota available in my plan change?**  

Beginning March 1, 2026, self\-hosted runners will be included within your free usage quota, and will consume available usage based on list price the same way that Linux, Windows, and MacOS standard runners work today.


**Will self\-hosted runner usage consume from my free usage minutes?**  

Yes, billable self\-hosted runner usage will be able to consume minutes from the free quota associated with your plan.


**How does this pricing change affect customers on GitHub Enterprise Server?**


This pricing change does not affect customers using GitHub Enterprise Server. Customers running Actions jobs on self\-hosted runners on GitHub Enterprise Server may continue to host, manage, troubleshoot and use Actions on and in conjunction with their implementation free of charge.


**Can I bill my self\-hosted runner usage on private repositories through Azure?**


Yes, as long as you have an active Azure subscription ID associated with your GitHub Enterprise or Organization(s).


**What is the overall impact of this change to GitHub customers?**


96% of customers will see no change to their bill. Of the 4% of Actions users impacted by this change, 85% of this cohort will see their Actions bill decrease and the remaining 15% who are impacted across all face a median increase around $13\.


**Did GitHub consider how this impacts individual developers, not just Enterprise scale customers of GitHub?**  

From our individual users (free \& Pro plans) of those who used GitHub Actions in the last month in private repos only 0\.09% would end up with a price increase, with a median increase of under $2 a month. Note that this impact is after these users have made use of their included minutes in their plans today, entitling them to over 33 hours of included GitHub compute, and this has no impact on their free use of public repos. A further 2\.8% of this total user base will see a decrease in their monthly cost as a result of these changes. The rest are unimpacted by this change.


**How can I figure out what my new monthly cost for Actions looks like?**


GitHub Actions provides [detailed usage reports for the current and prior year](https://docs.github.com/billing/how-tos/products/view-productlicense-use). You can use this prior usage alongside the [rate changes](https://docs.github.com/billing/reference/actions-runner-pricing) that will be introduced in January and March to estimate cost under the new pricing structure. We have created a [Python script](https://docs.github.com/billing/tutorials/estimate-actions-costs) to help you leverage [full usage reports](https://docs.github.com/billing/how-tos/products/view-productlicense-use#downloading-usage-reports) to calculate your expected cost after the price updates.


We have also updated our [Actions pricing calculator](https://github.com/pricing/calculator#actions), making it easier to estimate your future costs, particularly if your historical usage is limited or not representative of expected future usage.


## [Recommended resources](#recommended-resources)


* See the [GitHub Actions runner pricing documentation](https://docs.github.com/billing/reference/actions-runner-pricing) for the new GitHub\-hosted runner rates effective January 1, 2026\.
* For more details on upcoming GitHub Actions releases, see the [GitHub public roadmap](https://github.com/orgs/github/projects/4247).
* For help estimating your expected Actions usage cost, use the newly updated [Actions pricing calculator](https://github.com/pricing/calculator#actions).
* To see your current or historical Actions usage, see our documentation for [viewing and downloading detailed usage reports](https://docs.github.com/billing/how-tos/products/view-productlicense-use).
* If you are interested in moving existing self\-hosted runner usage to GitHub\-hosted runners, see the [SHR to GHR migration guide](http://docs.github.com/actions/tutorials/migrate-to-github-runners) in our documentation.
