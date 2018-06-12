---
title: "Weekly Development Update, January 12, 2016" 
layout: post
date: '2016-01-12 00:30:00 -0300'
---
        
### Announcement

The OpenBazaar team will be visiting and presenting at the d10e conference, and we'll also be hosting our own event in Amsterdam on February 19th. You can find more details on [this page](http://www.meetup.com/Amsterdam-OpenBazaar-Meetup/events/227939541/). A 64 bit Windows Installer is available for testing (not yet feature complete). You can find it in our [community Slack](https://openbazaar-slackin-drwasho.herokuapp.com/).

### Back end

Holepunching and symmetric NAT relaying now works peer to peer. Various bug fixes.

### Front end

Search and the follow/unfollow buttons now work on the discover view. Client updated to match changes in the server to how data is structured. Improvements made to the languages, in particular cleaned up areas where phrases should be used instead of words. [Search UI documentation](https://docs.google.com/document/d/1aj9vWi1v2Vj5Y4T2yNuzONGs4qSrpJ9jA_r1-YABaGo/edit?usp=sharing) is completed. Once a user completes onboarding, they'll now see a callout for the Discover section. This will help first time users find the market easier. http://i.imgur.com/8OhCsT4.png The primary_color options are no longer random, it only pulls from a list of higher quality choices. http://i.imgur.com/t7H4kqe.png Added icons throughout the interface. http://i.imgur.com/OnOp11t.png The user page is now displaying follower and following count within the tabs. http://i.imgur.com/oEUprEr.png Changed the about page to a modal. http://i.imgur.com/vbE1SH4.png Various bug fixes.