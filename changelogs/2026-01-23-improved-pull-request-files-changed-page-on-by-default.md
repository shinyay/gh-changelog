---
title: "Improved pull request “Files changed” page on by default"
date: "2026-01-23"
type: "improvements"
labels: ["collaboration tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-22-improved-pull-request-files-changed-page-on-by-default"
fetched_at: "2026-02-03T14:50:54.715531Z"
---

# Improved pull request “Files changed” page on by default

## Overview
The improved pull request “Files Changed” experience, currently in public preview, is rolling out as the default experience to all users! 🎉

## Detailed Explanation
### Overview
- The improved pull request “Files Changed” experience, currently in public preview, is rolling out as the default experience to all users! 🎉
- This improved experience is designed to be familiar to our existing pull request users, but offers better performance, accessibility, and user productivity. If you need to switch back to the classic experience, the option to opt-out is still available.

### ✨ What’s new
- If you are coming from the classic experience, the new experience should feel familiar but adds some significant improvements:
- Comment on any line: You can now comment on any line of a changed file , not just the lines surrounding a change.
- View the description without switching pages: You can now view the pull request description from the new Overview panel on the “Files changed” page.
- Reviewing made easier Enhanced file tree: The file tree is now resizable with indicators showing the files with comments, errors, and warnings. Review your pending comments: Pending comments are now shown in the review submission panel, so you can double-check your feedback before submitting. Draft comments: New comments and replies are saved locally so you won’t lose them if you accidentally close your browser or refresh the page.
- Fewer page reloads: Clicking Refresh to pull in new changes, switching between split and unified modes, and other tasks will no longer force a full page refresh.
- Accessibility & readability: Keyboard navigation, screen reader landmarks, and increased line spacing options are now available to make the experience available to everyone.
- Enhanced file tree: The file tree is now resizable with indicators showing the files with comments, errors, and warnings.
- Review your pending comments: Pending comments are now shown in the review submission panel, so you can double-check your feedback before submitting.
- Draft comments: New comments and replies are saved locally so you won’t lose them if you accidentally close your browser or refresh the page.

### 🚀 Improvements for large pull requests
- A new experimental mode for reviewing large pull requests is now available in the new “Files changed” experience. This mode uses virtualization to reduce the number of DOM elements and event listeners that the browser must manage. This can significantly improve memory utilization and the responsiveness of the page, especially on slower machines. It also avoids many of the usability challenges caused by single file mode .
- To try this new mode, click Try a new experimental mode in the banner that appears when viewing a large pull request:
- Because the full set of changes is not rendered by the browser, some browser functions might not work as expected:
- Finding diff content (e.g., searching for a function name).
- Selecting all text (e.g., to be able to copy and process elsewhere).
- Printing or exporting the page.
- Using browser extensions that need all diff content on the page.
- To switch back to single file mode when in this mode, click the Switch to single file mode link in the banner when viewing a large pull request.

### 🔧 Fixes and improvements
- Improved: Commenting workflows in diffs are more intuitive and reliable, with better multi-line selection, line number click selection, correct focus behavior for new comments, and fully functional diff hunks.
- Fixed: Issues where suggested changes were applied incorrectly, partially applied, deleted lines unexpectedly, or behaved incorrectly on modified or context lines.
- Fixed: Multiple bugs where users could not add, edit, delete, reply to, or jump to comments and outdated threads during an active review.
- Fixed: Comment side panel issues where filters, scrolling, and navigation to the correct thread did not work as expected.
- Fixed: Delayed typing and interaction lag in comment replies, especially on Safari.
- Fixed: Keyboard shortcuts for navigating between commits using P and N now work reliably again.
- Fixed: “Files Changed” UI issues such as incorrect scroll positioning, sticky headers behaving incorrectly, viewed file count mismatches, and unexpected scroll jumps on mobile.
- Fixed: Visual and interaction bugs affecting comment previews, toolbars, dropdowns, and overlays that could block or confuse common review actions.
- Fixed: Accessibility issues impacting screen reader announcements, keyboard navigation, tooltip labeling, focus order, and content visibility on smaller screens.

### ♥️ Feedback
- Your feedback is essential to helping us improve this experience. Please use the “Files Changed” preview feedback discussion to report problems, ask questions, and review known issues.

## Key Changes
- A new experimental mode for reviewing large pull requests is now available in the new “Files changed” experience. This mode uses virtualization to reduce the number of DOM elements and event listeners that the browser must manage. This can significantly improve memory utilization and the responsiveness of the page, especially on slower machines. It also avoids many of the usability challenges caused by single file mode .
- To try this new mode, click Try a new experimental mode in the banner that appears when viewing a large pull request:
- Because the full set of changes is not rendered by the browser, some browser functions might not work as expected:
- Finding diff content (e.g., searching for a function name).
- Selecting all text (e.g., to be able to copy and process elsewhere).
- Printing or exporting the page.
- Using browser extensions that need all diff content on the page.
- To switch back to single file mode when in this mode, click the Switch to single file mode link in the banner when viewing a large pull request.
- Improved: Commenting workflows in diffs are more intuitive and reliable, with better multi-line selection, line number click selection, correct focus behavior for new comments, and fully functional diff hunks.
- Fixed: Issues where suggested changes were applied incorrectly, partially applied, deleted lines unexpectedly, or behaved incorrectly on modified or context lines.
- Fixed: Multiple bugs where users could not add, edit, delete, reply to, or jump to comments and outdated threads during an active review.
- Fixed: Comment side panel issues where filters, scrolling, and navigation to the correct thread did not work as expected.
- Fixed: Delayed typing and interaction lag in comment replies, especially on Safari.
- Fixed: Keyboard shortcuts for navigating between commits using P and N now work reliably again.
- Fixed: “Files Changed” UI issues such as incorrect scroll positioning, sticky headers behaving incorrectly, viewed file count mismatches, and unexpected scroll jumps on mobile.
- Fixed: Visual and interaction bugs affecting comment previews, toolbars, dropdowns, and overlays that could block or confuse common review actions.
- Fixed: Accessibility issues impacting screen reader announcements, keyboard navigation, tooltip labeling, focus order, and content visibility on smaller screens.

## Impact / Who’s Affected
- The improved pull request “Files Changed” experience, currently in public preview, is rolling out as the default experience to all users! 🎉 This improved experience is designed to be familiar to our existing pull request users, but offers better performance, accessibility, and user productivity.
- Accessibility & readability: Keyboard navigation, screen reader landmarks, and increased line spacing options are now available to make the experience available to everyone. 🚀 Improvements for large pull requests A new experimental mode for reviewing large pull requests is now available in the new “Files changed” experience.

## Article Content (cleaned)
The improved pull request “Files Changed” experience, currently in public preview, is rolling out as the default experience to all users! 🎉


This improved experience is designed to be familiar to our existing pull request users, but offers better performance, accessibility, and user productivity. If you need to switch back to the classic experience, the option to opt\-out is still available.


## [✨ What’s new](#%e2%9c%a8-whats-new)


If you are coming from the classic experience, the new experience should feel familiar but adds some significant improvements:


* **Comment on any line:** You can now [comment on any line of a changed file](https://github.blog/changelog/2025-09-25-pull-request-files-changed-public-preview-now-supports-commenting-on-unchanged-lines/), not just the lines surrounding a change.
* **View the description without switching pages:** You can now view the pull request description from the new [Overview panel](https://github.blog/changelog/2025-11-20-pull-request-files-changed-public-preview-november-20-updates/) on the “Files changed” page.
* **Reviewing made easier**
	+ **Enhanced file tree:** The file tree is now resizable with indicators showing the files with comments, errors, and warnings.
	+ **Review your pending comments:** Pending comments are now shown in the review submission panel, so you can double\-check your feedback before submitting.
	+ **Draft comments:** New comments and replies are saved locally so you won’t lose them if you accidentally close your browser or refresh the page.
* **Fewer page reloads:** Clicking **Refresh** to pull in new changes, switching between split and unified modes, and other tasks will no longer force a full page refresh.
* **Accessibility \& readability:** Keyboard navigation, screen reader landmarks, and increased line spacing options are now available to make the experience available to everyone.


## [🚀 Improvements for large pull requests](#%f0%9f%9a%80-improvements-for-large-pull-requests)


A new experimental mode for reviewing large pull requests is now available in the new “Files changed” experience. This mode uses virtualization to reduce the number of DOM elements and event listeners that the browser must manage. This can significantly improve memory utilization and the responsiveness of the page, especially on slower machines. It also avoids many of the usability challenges caused by [single file mode](https://github.blog/changelog/2025-09-11-pull-request-files-changed-public-preview-experience-september-11-updates/).


To try this new mode, click **Try a new experimental mode** in the banner that appears when viewing a large pull request:


![Screen shot of the new files changed experience showing an informational banner explaining the option to view the pull request using this new experimental mode.](https://github.com/user-attachments/assets/bc8b6426-8f0c-4644-a80d-2c7729a6f9e3)


Because the full set of changes is not rendered by the browser, some browser functions might not work as expected:


* Finding diff content (e.g., searching for a function name).
* Selecting all text (e.g., to be able to copy and process elsewhere).
* Printing or exporting the page.
* Using browser extensions that need all diff content on the page.


To switch back to single file mode when in this mode, click the **Switch to single file mode** link in the banner when viewing a large pull request.


## [🔧 Fixes and improvements](#%f0%9f%94%a7-fixes-and-improvements)


* **Improved:** Commenting workflows in diffs are more intuitive and reliable, with better multi\-line selection, line number click selection, correct focus behavior for new comments, and fully functional diff hunks.
* **Fixed:** Issues where suggested changes were applied incorrectly, partially applied, deleted lines unexpectedly, or behaved incorrectly on modified or context lines.
* **Fixed:** Multiple bugs where users could not add, edit, delete, reply to, or jump to comments and outdated threads during an active review.
* **Fixed:** Comment side panel issues where filters, scrolling, and navigation to the correct thread did not work as expected.
* **Fixed:** Delayed typing and interaction lag in comment replies, especially on Safari.
* **Fixed:** Keyboard shortcuts for navigating between commits using `P` and `N` now work reliably again.
* **Fixed:** “Files Changed” UI issues such as incorrect scroll positioning, sticky headers behaving incorrectly, viewed file count mismatches, and unexpected scroll jumps on mobile.
* **Fixed:** Visual and interaction bugs affecting comment previews, toolbars, dropdowns, and overlays that could block or confuse common review actions.
* **Fixed:** Accessibility issues impacting screen reader announcements, keyboard navigation, tooltip labeling, focus order, and content visibility on smaller screens.


## [♥️ Feedback](#%e2%99%a5%ef%b8%8f-feedback)


Your feedback is essential to helping us improve this experience. Please use the [“Files Changed” preview feedback discussion](https://gh.io/new-files-changed-feedback) to report problems, ask questions, and review known issues.
