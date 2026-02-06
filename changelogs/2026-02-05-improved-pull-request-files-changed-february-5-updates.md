---
title: "Improved pull request “Files changed” – February 5 updates"
date: "2026-02-05"
type: "Improvement"
labels: ["collaboration tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-02-05-improved-pull-request-files-changed-february-5-updates"
fetched_at: "2026-02-06T15:31:38.720070Z"
---

# Improved pull request “Files changed” – February 5 updates

## Overview
This release brings CODEOWNERS validation to the new “Files changed” experience and includes broad performance improvements across common review workflows. Navigation between pull request tabs is faster and more reliable, especially when moving between Conversations and Files changed . Review interactions are smoother for the largest pull requests, with better scrolling, reduced memory usage, and overall stability improvements.

## Detailed Explanation
### Overview
- This release brings CODEOWNERS validation to the new “Files changed” experience and includes broad performance improvements across common review workflows. Navigation between pull request tabs is faster and more reliable, especially when moving between Conversations and Files changed . Review interactions are smoother for the largest pull requests, with better scrolling, reduced memory usage, and overall stability improvements.

### 🗂️ Codeowner validation
- We added CODEOWNERS validation, filling a gap from the classic “Files changed” experience. Required reviewers are now correctly surfaced based on CODEOWNERS rules, ensuring review requirements are accurately enforced before merge.

### 📲 Small screens improvements
- We are rolling out improvements to the “Files changed” experience on small screens by fixing multiple layout, spacing, and overflow issues, ensuring diffs, comments, headers, and controls render and behave correctly on mobile and smaller viewports.

### 🚀 Performance improvements
- Performance is a top priority for us. Based on your feedback, we’ve shipped several improvements in the past week that directly address lag issues, with a focus on larger pull requests:
- Pull request diffs have been optimized for greater responsiveness when clicking, typing, and scrolling on the page. Early data shows large pull requests in the new files changed experience respond up to 67% faster to these kinds of interactions.
- Only the largest pull requests use virtualization to enhance performance while scrolling and interacting.
- It’s now quicker to navigate between the Conversations and Files tabs, with load times from 10+ seconds to a few seconds.
- Resizing the file tree is now smoother and more responsive, even for large pull requests with many files.
- Improved performance and stability when reviewing pull requests in Safari.
- Fixed high memory usage when reviewing large pull requests.

### 🔧 More fixes and improvements
- Fixed: The issue where opening a notification directly into the Files changed tab did not mark the notification as read. Notifications now correctly update their read state when viewed, matching the behavior of the classic experience.
- Fixed: An issue where the file diff header was not consistently sticky when scrolling.
- Fixed: An issue where code snippets in thread replies had a background color that was hard to distinguish from the reply background.
- Fixed: An error that occurred when commenting across large index differences in diffs.

### ❤ Feedback
- Your feedback is important. You can report problems, ask questions, and view known issues in the “Files changed” preview feedback discussion .

## Key Changes
- We are rolling out improvements to the “Files changed” experience on small screens by fixing multiple layout, spacing, and overflow issues, ensuring diffs, comments, headers, and controls render and behave correctly on mobile and smaller viewports.
- Performance is a top priority for us. Based on your feedback, we’ve shipped several improvements in the past week that directly address lag issues, with a focus on larger pull requests:
- Pull request diffs have been optimized for greater responsiveness when clicking, typing, and scrolling on the page. Early data shows large pull requests in the new files changed experience respond up to 67% faster to these kinds of interactions.
- Only the largest pull requests use virtualization to enhance performance while scrolling and interacting.
- It’s now quicker to navigate between the Conversations and Files tabs, with load times from 10+ seconds to a few seconds.
- Resizing the file tree is now smoother and more responsive, even for large pull requests with many files.
- Improved performance and stability when reviewing pull requests in Safari.
- Fixed high memory usage when reviewing large pull requests.
- Fixed: The issue where opening a notification directly into the Files changed tab did not mark the notification as read. Notifications now correctly update their read state when viewed, matching the behavior of the classic experience.
- Fixed: An issue where the file diff header was not consistently sticky when scrolling.
- Fixed: An issue where code snippets in thread replies had a background color that was hard to distinguish from the reply background.
- Fixed: An error that occurred when commenting across large index differences in diffs.

## Impact / Who’s Affected
- Only the largest pull requests use virtualization to enhance performance while scrolling and interacting.

## Caveats / Limitations
- Only the largest pull requests use virtualization to enhance performance while scrolling and interacting.
- Fixed: An error that occurred when commenting across large index differences in diffs. ❤ Feedback Your feedback is important.

## Article Content (cleaned)
This release brings `CODEOWNERS` validation to the new “Files changed” experience and includes broad performance improvements across common review workflows. Navigation between pull request tabs is faster and more reliable, especially when moving between **Conversations** and **Files changed**. Review interactions are smoother for the largest pull requests, with better scrolling, reduced memory usage, and overall stability improvements.


## [🗂️ Codeowner validation](https://github.blog/changelog/feed/#%f0%9f%97%82%ef%b8%8f-codeowner-validation)


We added `CODEOWNERS` validation, filling a gap from the classic “Files changed” experience. Required reviewers are now correctly surfaced based on `CODEOWNERS` rules, ensuring review requirements are accurately enforced before merge.


![Screenshot showing social CODEOWNERS validation in the new Files changed tab](https://github.com/user-attachments/assets/0fe2bf99-9603-48da-ae1e-d56293eb4df6)


## [📲 Small screens improvements](https://github.blog/changelog/feed/#%f0%9f%93%b2-small-screens-improvements)


We are rolling out improvements to the “Files changed” experience on small screens by fixing multiple layout, spacing, and overflow issues, ensuring diffs, comments, headers, and controls render and behave correctly on mobile and smaller viewports.


## [🚀 Performance improvements](https://github.blog/changelog/feed/#%f0%9f%9a%80-performance-improvements)


Performance is a top priority for us. Based on your feedback, we’ve shipped several improvements in the past week that directly address lag issues, with a focus on larger pull requests:


* Pull request diffs have been optimized for greater responsiveness when clicking, typing, and scrolling on the page. Early data shows large pull requests in the new files changed experience respond up to 67% faster to these kinds of interactions.
* Only the largest pull requests use virtualization to enhance performance while scrolling and interacting.
* It’s now quicker to navigate between the **Conversations** and **Files** tabs, with load times from 10\+ seconds to a few seconds.
* Resizing the file tree is now smoother and more responsive, even for large pull requests with many files.
* Improved performance and stability when reviewing pull requests in Safari.
* Fixed high memory usage when reviewing large pull requests.


## [🔧 More fixes and improvements](https://github.blog/changelog/feed/#%f0%9f%94%a7-more-fixes-and-improvements)


* **Fixed:** The issue where opening a notification directly into the **Files changed** tab did not mark the notification as read. Notifications now correctly update their read state when viewed, matching the behavior of the classic experience.
* **Fixed:** An issue where the file diff header was not consistently sticky when scrolling.
* **Fixed:** An issue where code snippets in thread replies had a background color that was hard to distinguish from the reply background.
* **Fixed:** An error that occurred when commenting across large index differences in diffs.


## [❤ Feedback](https://github.blog/changelog/feed/#heart-feedback)


Your feedback is important. You can report problems, ask questions, and view known issues in the [“Files changed” preview feedback discussion](https://gh.io/new-files-changed-feedback).
