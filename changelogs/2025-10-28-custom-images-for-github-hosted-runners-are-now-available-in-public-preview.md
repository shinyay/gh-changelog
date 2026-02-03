---
title: "Custom images for GitHub-hosted runners are now available in public preview"
date: "2025-10-28"
type: "new releases"
labels: ["actions", "universe25"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-10-28-custom-images-for-github-hosted-runners-are-now-available-in-public-preview"
fetched_at: "2026-02-03T14:50:55.686887Z"
---

# Custom images for GitHub-hosted runners are now available in public preview

## Overview
Custom images for GitHub-hosted runners are now available in public preview. This feature allows you to start with a GitHub-curated base image and build your own virtual machine image tailored to your workflow needs.

## Detailed Explanation
### Overview
- Custom images for GitHub-hosted runners are now available in public preview. This feature allows you to start with a GitHub-curated base image and build your own virtual machine image tailored to your workflow needs.
- Custom images can include your repository code, prepulled container images, required binaries, certificates, and other dependencies. Developers benefit from:
- Faster workflows: Start jobs with preinstalled tools and dependencies, reducing setup time and dramatically speeding up builds.
- Hardened security: Standardize your build environments, enforce organization-wide image policies, and minimize vulnerabilities by reducing the attack surface.
- Cost optimization: Faster job starts mean fewer billed minutes, helping you lower your overall CI/CD costs.
- Enterprise-grade customization: Preinstall exactly what your teams need. From certificates and proxies to monitoring agents, all while maintaining full control over image lifecycle and rollout.
- Lifecycle management: Administrators can set policies for the number of versions per image, removal of images that have not been used for a predetermined amount of time, and the maximum image age before it is disabled, to align with organizational security and compliance requirements.

### How to get started
- Custom images let you define exactly what your GitHub Actions runner environment looks like, so every workflow starts with the tools, dependencies, and configurations you need already in place. Here’s how to get started:
- 1. Create a larger runner that can generate custom images. Begin by setting up a runner capable of building custom images. This runner uses a base image (either a GitHub partner image or one you’ve already generated) as the foundation for your new image. This layered approach lets you build on trusted environments and add only what you need.
- 2. Run an image-generating workflow. In your workflow file, add a new snapshot type to your job. This tells GitHub Actions to capture the state of your runner after installing all required tools and packages.
- 3. Add your runner to a runner group with the custom image. Once your image is built, a larger runner uses it and is then assigned to a runner group. Runners already using the named image will automatically pick up new versions of the image. In your workflows, you still need to reference the runner or runner group name—you cannot target runners solely by the image name. All subsequent workflow runs using this runner will start with your custom environment, saving time and ensuring consistency. Please allow 10-15 minutes after the image has been created before the new version is ready to use.
- 4. Use your custom image in future workflows. To use your custom image, set the runs-on target in your workflow to the name of the runner (or runner group with a runner) using the custom image. Every job will start with your dependencies preinstalled, so you can focus on building and shipping faster.

### Learn more
- For detailed instructions, advanced configuration options, and troubleshooting tips, see our official documentation on managing larger runners . You’ll find step-by-step guides, workflow examples, and best practices for using custom images with GitHub-hosted runners.
- Join the discussion within GitHub Community .

## Impact / Who’s Affected
- Custom images for GitHub-hosted runners are now available in public preview.
- This layered approach lets you build on trusted environments and add only what you need.

## Caveats / Limitations
- This layered approach lets you build on trusted environments and add only what you need.

## Insights (derived from article language)
- This feature allows you to start with a GitHub-curated base image and build your own virtual machine image tailored to your workflow needs.
- Learn more For detailed instructions, advanced configuration options, and troubleshooting tips, see our official documentation on managing larger runners .

## Article Content (cleaned)
Custom images for GitHub\-hosted runners are now available in public preview. This feature allows you to start with a GitHub\-curated base image and build your own virtual machine image tailored to your workflow needs.


Custom images can include your repository code, prepulled container images, required binaries, certificates, and other dependencies. Developers benefit from:


* **Faster workflows:** Start jobs with preinstalled tools and dependencies, reducing setup time and dramatically speeding up builds.
* **Hardened security:** Standardize your build environments, enforce organization\-wide image policies, and minimize vulnerabilities by reducing the attack surface.
* **Cost optimization:** Faster job starts mean fewer billed minutes, helping you lower your overall CI/CD costs.
* **Enterprise\-grade customization:** Preinstall exactly what your teams need. From certificates and proxies to monitoring agents, all while maintaining full control over image lifecycle and rollout.
* **Lifecycle management:** Administrators can set policies for the number of versions per image, removal of images that have not been used for a predetermined amount of time, and the maximum image age before it is disabled, to align with organizational security and compliance requirements.


### [How to get started](#how-to-get-started)


Custom images let you define exactly what your GitHub Actions runner environment looks like, so every workflow starts with the tools, dependencies, and configurations you need already in place. Here’s how to get started:


**1\. Create a larger runner that can generate custom images.**  

Begin by setting up a runner capable of building custom images. This runner uses a base image (either a GitHub partner image or one you’ve already generated) as the foundation for your new image. This layered approach lets you build on trusted environments and add only what you need.


**2\. Run an image\-generating workflow.**  

In your workflow file, add a new `snapshot` type to your job. This tells GitHub Actions to capture the state of your runner after installing all required tools and packages.


**3\. Add your runner to a runner group with the custom image.**  

Once your image is built, a larger runner uses it and is then assigned to a runner group. Runners already using the named image will automatically pick up new versions of the image. In your workflows, you still need to reference the runner or runner group name—you cannot target runners solely by the image name. All subsequent workflow runs using this runner will start with your custom environment, saving time and ensuring consistency. Please allow 10\-15 minutes after the image has been created before the new version is ready to use.


**4\. Use your custom image in future workflows.**  

To use your custom image, set the `runs-on` target in your workflow to the name of the runner (or runner group with a runner) using the custom image. Every job will start with your dependencies preinstalled, so you can focus on building and shipping faster.


### [Learn more](#learn-more)


For detailed instructions, advanced configuration options, and troubleshooting tips, see our official documentation on [managing larger runners](https://docs.github.com/en/actions/how-tos/manage-runners/larger-runners/manage-larger-runners?utm_source=changelog-docs-github-hosted-runners&utm_medium=changelog&utm_campaign=universe25). You’ll find step\-by\-step guides, workflow examples, and best practices for using custom images with GitHub\-hosted runners.


Join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/177495?utm_source=changelog-community-github-hosted-runners&utm_medium=changelog&utm_campaign=universe25).
