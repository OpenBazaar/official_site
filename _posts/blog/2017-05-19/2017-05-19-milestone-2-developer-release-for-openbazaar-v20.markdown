---
title: "Milestone 2 Developer Release for OpenBazaar v2.0" 
layout: post
date: '2017-05-19 00:30:00 -0300'
---
        
Development of the OpenBazaar 2.0 software continues according to [our roadmap](https://trello.com/b/dF6ymHGU/openbazaar-high-level-roadmap), and today we publish the [Milestone 2 developer release](https://github.com/OpenBazaar/openbazaar-desktop/releases/tag/v2.0.4). Please note that this release is not yet feature complete, and cannot be used for real transactions yet.

Milestone 2 focuses on discoverability of listings / stores, as well as communication. Third party search is now accessible within the client. Chat is also fully functional. Channels were planned for Milestone 2, but have been moved to later in development. Full release notes below.

[![Search in v2 client](Screenshot-from-2017-05-19-15-18-03.png)](Screenshot-from-2017-05-19-15-18-03.png)

Release notes
-------------

**Server changes:**

*   Added wallet tests. Made profile caching smarter. Various bug fixes.

**Client changes:**

**Transactions**

*   The transactions screen is now viewable with partial functionality.

**Purchasing**

*   The purchasing screen is now viewable with partial functionality.

**Context Menu**

*   The context menu will now appear on a right click.
*   The context menu has commands for zooming the screen in and out.
*   The screen can also be zoomed in and out using the keyboard (command or control plus – or =).

**Moderators**

*   The message button in the moderator details screen is now functional.

**Default User Name**

*   The default user name is now a shorter random string of characters.

**Wallet**

*   Transactions are shown as confirmed on the 6th confirmation now, instead of the 7th.

**Profile**

*   The profile now uses a local url instead of a ipns url.

**Cached Profiles**

*   A new functionality was added to use cached profile data in situations were it is not critical that the data be fresh. This has been implemented in the chat sidebar.

**Bug Fixes**

*   A bug where radio buttons were not always sized the same was fixed. #434
*   A bug that caused the QR code in about/donate to be horizontally compressed was fixed. #433
*   The contentBox style was set to break and wrap very long words so they would not extend past their container. #396
*   A bug was fixed where old profiles were identified as moderators, but did not have moderation data.
*   The handling of emojis was made more flexible and consistent.
*   The QR code in the wallet is now correct.
*   The sort by drop down in search now works correctly.
*   Layout bugs with the filter labels and emojis in the search screen were fixed.
*   A bug where the categories parameter in a store page can be null was fixed.
*   A bug with routing to a listing address was fixed.
*   The server name is now shown correctly in the page navigation menu. #454

* * *

**Are you a developer who wants to get involved in this early stage of Version 2.0 development?**  
_Get the details [here](https://blog.openbazaar.org/milestone-1-developer-release-for-openbazaar-2-0/#.WJuWRxIrLOR)!_

**Want to start RIGHT NOW buying and selling with Bitcoin or other altcoins using Version 1.0?**  
_[Download OpenBazaar](http://openbazaar.org/)_