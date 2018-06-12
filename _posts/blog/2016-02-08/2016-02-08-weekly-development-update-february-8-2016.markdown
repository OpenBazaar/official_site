---
title: "Weekly Development Update, February 8, 2016" 
layout: post
date: '2016-02-08 00:30:00 -0300'
---
        
### Back End

Moderation is finished server side. This includes opening and closing disputes, releasing funds, and maintaining a separate chat conversation with all three parties per dispute. We have brought up two new libbitcoin servers in preparation for testing and launch. One is on the main net, located at [http://libbitcoin3.openbazaar.org/](http://libbitcoin3.openbazaar.org/). The other is on the test net, located at [http://libbitcoin4.openbazaar.org/](http://libbitcoin4.openbazaar.org/).

### Front End

Transactions have been updated so disputes can now be filed, and buyers, vendors, and moderators can discuss the dispute. If a url is typed into the about or item description fields, it will automatically be turned into a clickable link when someone views it. Several updates to chat and notifications to improve display of avatars and other data. Added notifications for transactions changing states and disputes being filed, clicking on a transaction notification opens that tab in the transaction view. Contributor Kirvx added new phrase translations. Integrated a few new steps into the checkout process to make setting up a bitcoin wallet easier for first time users, see video below. Cleaned up the design of the _Become a Moderator_ modal. http://i.imgur.com/Li8oQqf.png During the onboarding process, a random theme is now selected for each user. http://i.imgur.com/9Juzy6T.png