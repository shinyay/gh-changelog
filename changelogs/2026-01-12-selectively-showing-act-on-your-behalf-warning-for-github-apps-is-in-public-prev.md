---
title: "Selectively showing \"act on your behalf\" warning for GitHub Apps is in public preview"
date: "2026-01-12"
type: "improvements"
labels: ["ecosystem and accessibility"]
author: "Allison"
source_url: "https://github.blog/changelog/2026-01-12-selectively-showing-act-on-your-behalf-warning-for-github-apps-is-in-public-preview"
fetched_at: "2026-02-03T14:40:05.248288Z"
---

# Selectively showing "act on your behalf" warning for GitHub Apps is in public preview

## Overview
Today we’ve released an update to the consent page to be less alarming when using GitHub Apps only as a form of sign-in. The consent page for GitHub Apps, where a user decides whether to authorize an app or not, has been updated to only show the “Act on your behalf” note if the app is going to access resources or make writes on the user’s behalf.

## Detailed Explanation
### Overview
- Today we’ve released an update to the consent page to be less alarming when using GitHub Apps only as a form of sign-in. The consent page for GitHub Apps, where a user decides whether to authorize an app or not, has been updated to only show the “Act on your behalf” note if the app is going to access resources or make writes on the user’s behalf.
- Many GitHub Apps sign in users as a sign in service. They don’t actually access any data on GitHub, they just want to know who the user is as the basis for an account system. We found that upwards of 50% of application authorizations were of this nature—only requesting the ability to read user profile data. In all of these cases, the user signing in was met with a warning that the app would be allowed to act on behalf of the user, followed by a list of permissions they’d be able to leverage. When the app was asking to read the user’s profile, this was confusing to the end user; what else would the app be allowed be allowed to do? This confusion resulted in support tickets for developers and users choosing not to sign in because they thought it was a security risk.
- This change removes the “Act on your behalf” note in the consent page if the app is requesting only read permissions against the user account itself. If the app is requesting any kind of repository, organization, or enterprise permission (read or write) then the note still appears. This allows applications to sign in users and get their profile information and email addresses (if requested) without undue alarm.
- Before
- After
- If you have any thoughts or comments, feel free to drop a message in our Community discussion .

## Impact / Who’s Affected
- Today we’ve released an update to the consent page to be less alarming when using GitHub Apps only as a form of sign-in.
- The consent page for GitHub Apps, where a user decides whether to authorize an app or not, has been updated to only show the “Act on your behalf” note if the app is going to access resources or make writes on the user’s behalf.
- We found that upwards of 50% of application authorizations were of this nature—only requesting the ability to read user profile data.
- This change removes the “Act on your behalf” note in the consent page if the app is requesting only read permissions against the user account itself.

## Caveats / Limitations
- Today we’ve released an update to the consent page to be less alarming when using GitHub Apps only as a form of sign-in.
- The consent page for GitHub Apps, where a user decides whether to authorize an app or not, has been updated to only show the “Act on your behalf” note if the app is going to access resources or make writes on the user’s behalf.
- We found that upwards of 50% of application authorizations were of this nature—only requesting the ability to read user profile data.
- This change removes the “Act on your behalf” note in the consent page if the app is requesting only read permissions against the user account itself.
- If the app is requesting any kind of repository, organization, or enterprise permission (read or write) then the note still appears.

## Article Content (cleaned)
Today we’ve released an update to the consent page to be less alarming when using GitHub Apps only as a form of sign\-in. The consent page for GitHub Apps, where a user decides whether to authorize an app or not, has been updated to only show the “Act on your behalf” note if the app is going to access resources or make writes on the user’s behalf.


Many GitHub Apps sign in users as a sign in service. They don’t actually access any data on GitHub, they just want to know who the user is as the basis for an account system. We found that upwards of 50% of application authorizations were of this nature—only requesting the ability to read user profile data. In all of these cases, the user signing in was met with a warning that the app would be allowed to act on behalf of the user, followed by a list of permissions they’d be able to leverage. When the app was asking to read the user’s profile, this was confusing to the end user; what **else** would the app be allowed be allowed to do? This confusion resulted in support tickets for developers and users choosing not to sign in because they thought it was a security risk.


This change removes the “Act on your behalf” note in the consent page if the app is requesting only **read** permissions against the user account itself. If the app is requesting any kind of repository, organization, or enterprise permission (read or write) then the note still appears. This allows applications to sign in users and get their profile information and email addresses (if requested) without undue alarm.


**Before**  

![This image shows the consent screen when authorizing a GitHub app with the 'Act on your behalf' warning](https://github.com/user-attachments/assets/8d28e80b-3d35-4a1f-ac5a-4c9ce69d93a0)


**After**  

![This image shows the consent screen when authorizing a GitHub app without the 'Act on your behalf' warning](https://github.com/user-attachments/assets/1a995399-f3c5-4c03-b501-38c306e29961)


If you have any thoughts or comments, feel free to drop a message in our [Community discussion](https://github.com/orgs/community/discussions/184117).
