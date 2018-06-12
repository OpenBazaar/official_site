---
title: "OpenBazaar 2.1 Released - <span class='post-title-extra-alternative'>Bitcoin Cash and Zcash Integrated</span>" 
layout: post
date: '2018-01-30 00:30:00 -0300'
---
        
Today we are proud to announce Bitcoin Cash and Zcash (Beta) integration in OpenBazaar! With this update users will have the option to create new nodes for processing Bitcoin Cash and Zcash (Beta) payments, respectively.

OpenBazaar already allows buyers to fund their wallets with a variety of cryptocurrencies through [Shapeshift](https://shapeshift.io), but before this release all transactions were still resolved with Bitcoin. With[ the rise in Bitcoin network fees in 2017](https://www.openbazaar.org/blog/openbazaar-bitcoin-fees/), it became clear that OpenBazaar users needed support for cryptocurrencies with fees that are more suited for small to medium sized transactions ASAP.

This release is the first step towards allowing more options for cryptocurrencies in OpenBazaar. It includes native support for nodes using one cryptocurrency at a time, Bitcoin, Bitcoin Cash, or ZCash.

More currencies and multiple currency support per node are on our roadmap for future releases.

OpenBazaar 2.1  Release Notes
-----------------------------

This is a major milestone release, which incorporates support for Bitcoin Cash and ZCash into the OpenBazaar platform.

**New Features**

*   Users can now choose BTC, BCH, or ZEC when installing OpenBazaar, and can switch between currencies by creating and using a new server.
*   Users can now block nodes they no longer want to see content from.  
    A warning about potential scams that links to an external page about scam prevention was added to the purchase flow.

**Improvements**

*   The way the client shuts down the server when closing was improved.
*   The link to the obsolete docs page was replaced by a link to the main OB website in the right click menu.
*   The Rawflood search provider is no longer being supported by its creator, it has been removed as a default.
*   When in search, the search provider call automatically includes the user’s current crypto currency.
*   Ratings are now shown if they are zero, so it’s more clear if a listing or user has zero ratings.
*   Electron was updated to v1.7.11.
*   If a default search provider’s logo doesn’t load, the local version is used instead.
*   The code for getting the version from package.json was simplified.
*   Line breaks are now preserved in the order details chat and the order memo.
*   Search now supports checkboxes in filters.
*   Moderators now show the crypto currency (currently just one per node) they support, and users cannot add one if they don’t support the same currency the user’s node is set to.

**Bug Fixes**

*   Fixed typos.
*   Fixed an issue with categories.
*   The name of the store in the note on a transaction is no longer missing from the order details.
*   The order details avatar no longer gets stuck in a loading state.
*   Formatting was fixed on the reviews page.
*   A bug in moderating orders was corrected.
*   The payment details address in a moderated case is now correct.
*   The missing shipping method was added to the order details screen.
*   If an order is disputed, sellers can no longer refund it.
*   The QR code was fixed for all supported cryptocurrencies.
*   A bug in the View Listing link was fixed.
*   Order IDs are no longer incorrectly treated as links in chat.

**Internationalization**  
We are actively translating the text in the OpenBazaar reference client. If you are interested in volunteering as a translator, you can sign up at https://www.transifex.com/ob1/openbazaar

**Special Thanks**  
A special thank you goes out to contributors BillStrait, hegjon and ab10460ef3, the many volunteers that provide translations, and to our testers that discovered important issues.

For more development details, please see [the release notes on Github](https://github.com/OpenBazaar/openbazaar-desktop/releases/tag/v2.1.0)