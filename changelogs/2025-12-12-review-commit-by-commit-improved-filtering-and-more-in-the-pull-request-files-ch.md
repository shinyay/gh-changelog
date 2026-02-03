---
title: "Review commit-by-commit, improved filtering, and more in the pull request “Files changed” public preview"
date: "2025-12-12"
type: "improvements"
labels: ["collaboration tools"]
author: "Allison"
source_url: "https://github.blog/changelog/2025-12-11-review-commit-by-commit-improved-filtering-and-more-in-the-pull-request-files-changed-public-preview"
fetched_at: "2026-02-03T14:50:54.967279Z"
---

# Review commit-by-commit, improved filtering, and more in the pull request “Files changed” public preview

## Overview
A major feature gap with the classic “Files changed” page ( review commit-by-commit ) is now closed and commit filtering has been improved in this update to the pull request “Files changed” experience!

## Detailed Explanation
### Overview
- A major feature gap with the classic “Files changed” page ( review commit-by-commit ) is now closed and commit filtering has been improved in this update to the pull request “Files changed” experience!

### 🔍 Review commit-by-commit
- You can now review all commits, a subset of commits, or a single commit directly from the new “Files changed” page. Previously, filtering to a single commit redirected you to the classic view in the Commits tab. With this update, you remain on the “Files changed” page whether you are viewing all commits, selected commits, or an individual commit.
- We’ve also simplified all “Files changed” URL routes under a new path ( /changes ). All existing /files (and /commits/:sha ) URLs will continue to work, but they will redirect to the equivalent /changes route when you have the new feature enabled.
- We’ve also improved the commit filter, and it requires fewer clicks to choose a range or a single commit! You can open it from the toolbar or by pressing C if you’ve enabled single-key shortcuts.

### 📁 File filter improvements
- We’ve also improved the file filter to show a blue dot indicator to help you understand when filters are applied. A new Clear filters option also now appears on the filter menu to make it easy to reset all filters back to their default state.

### 🚀 Performance
- Improving performance is one of our top priorities and you will continue to see both small and large improvements over the coming weeks. Recent improvements:
- Improved responsiveness of resizing the file tree
- Improved performance when toggling Minimize comments or Split / Unified settings

### 🔧 More fixes and improvements
- Improved : Clicking the Refresh button when new changes are pushed to the pull request no longer does a full (and often slow) page refresh.
- Fixed : The Comments side panel should no longer report an error when resolving a comment that is already resolved.
- Fixed : Nonstandard characters in the file path (like a comma) no longer cause diffs to not load correctly.
- Fixed : The linguist-generated attribute in .gitattributes is now appropriately respected.
- Fixed : The T keyboard shortcut once again focuses on the file filter field and shows the file tree if necessary.
- Fixed : The C keyboard shortcut once again opens the commit filter.

### 🧪 Try it out
- The new commit-by-commit review and commit selector are available in the new “Files changed” experience. If you are still using the classic experience, click Try the new experience at the top of the classic “Files changed” page.

### ❤ Feedback
- Your feedback is important. You can report problems, ask questions, and view known issues in the “Files changed” preview feedback discussion .

## Key Changes
- We’ve also improved the file filter to show a blue dot indicator to help you understand when filters are applied. A new Clear filters option also now appears on the filter menu to make it easy to reset all filters back to their default state.
- Improved : Clicking the Refresh button when new changes are pushed to the pull request no longer does a full (and often slow) page refresh.
- Fixed : The Comments side panel should no longer report an error when resolving a comment that is already resolved.
- Fixed : Nonstandard characters in the file path (like a comma) no longer cause diffs to not load correctly.
- Fixed : The linguist-generated attribute in .gitattributes is now appropriately respected.
- Fixed : The T keyboard shortcut once again focuses on the file filter field and shows the file tree if necessary.
- Fixed : The C keyboard shortcut once again opens the commit filter.

## Impact / Who’s Affected
- We’ve also improved the commit filter, and it requires fewer clicks to choose a range or a single commit!

## Caveats / Limitations
- We’ve also improved the commit filter, and it requires fewer clicks to choose a range or a single commit!
- If you are still using the classic experience, click Try the new experience at the top of the classic “Files changed” page. ❤ Feedback Your feedback is important.

## Insights (derived from article language)
- We’ve also improved the commit filter, and it requires fewer clicks to choose a range or a single commit!

## Article Content (cleaned)
A major feature gap with the classic “Files changed” page (**review commit\-by\-commit**) is now closed and commit filtering has been improved in this update to the pull request “Files changed” experience!


## [🔍 Review commit\-by\-commit](#%f0%9f%94%8d-review-commit-by-commit)


You can now review all commits, a subset of commits, or a single commit directly from the new “Files changed” page. Previously, filtering to a single commit redirected you to the classic view in the **Commits** tab. With this update, you remain on the “Files changed” page whether you are viewing all commits, selected commits, or an individual commit.


![The new commit selector menu with options to show all commits, show commits since last review (which is disabled), or choose a list of commits](https://github.com/user-attachments/assets/27e65cc2-614d-414a-9b82-37aa845b79f1)


We’ve also simplified all “Files changed” URL routes under a new path (`/changes`). All existing `/files` (and `/commits/:sha`) URLs will continue to work, but they will redirect to the equivalent `/changes` route when you have the new feature enabled.


We’ve also improved the commit filter, and it requires fewer clicks to choose a range or a single commit! You can open it from the toolbar or by pressing `C` if you’ve enabled single\-key shortcuts.


## [📁 File filter improvements](#%f0%9f%93%81-file-filter-improvements)


We’ve also improved the file filter to show a blue dot indicator to help you understand when filters are applied. A new **Clear filters** option also now appears on the filter menu to make it easy to reset all filters back to their default state.


![The improved file filter menu that shows a blue dot when any filters are applied and provides a "clear filter" button to reset all filters](https://github.com/user-attachments/assets/9e894002-0157-4dc0-ad64-e26ada7a017a)


## [🚀 Performance](#%f0%9f%9a%80-performance)


Improving performance is one of our top priorities and you will continue to see both small and large improvements over the coming weeks. Recent improvements:


* Improved responsiveness of resizing the file tree
* Improved performance when toggling **Minimize comments** or **Split / Unified** settings


## [🔧 More fixes and improvements](#%f0%9f%94%a7-more-fixes-and-improvements)


* **Improved**: Clicking the **Refresh** button when new changes are pushed to the pull request no longer does a full (and often slow) page refresh.
* **Fixed**: The Comments side panel should no longer report an error when resolving a comment that is already resolved.
* **Fixed**: Nonstandard characters in the file path (like a comma) no longer cause diffs to not load correctly.
* **Fixed**: The `linguist-generated` attribute in `.gitattributes` is now appropriately respected.
* **Fixed**: The `T` keyboard shortcut once again focuses on the file filter field and shows the file tree if necessary.
* **Fixed**: The `C` keyboard shortcut once again opens the commit filter.


## [🧪 Try it out](#test_tube-try-it-out)


The new commit\-by\-commit review and commit selector are available in the new “Files changed” experience. If you are still using the classic experience, click **Try the new experience** at the top of the classic “Files changed” page.


## [❤ Feedback](#heart-feedback)


Your feedback is important. You can report problems, ask questions, and view known issues in the [“Files changed” preview feedback discussion](https://gh.io/new-files-changed-feedback).
