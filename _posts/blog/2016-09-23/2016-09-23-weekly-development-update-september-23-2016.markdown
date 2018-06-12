---
title: "Weekly Development Update: September 23, 2016" 
layout: post
date: '2016-09-23 00:30:00 -0300'
---
        
Front End
---------

Many new features and changes were made for upcoming 1.1.8 release. **Significant changes**:

1.  Added the ability for sellers to pin listings, so that they appear first in their store.
2.  Added the ability for sellers to set a Maximum Quantity to listings. Buyers can't buy more than that number in a single order.
3.  If the Maximum Quantity is set to zero, the listing will still be visible, but cannot be purchased. This allows sellers to have listings that are "out of stock" or "coming soon".
4.  Added the ability for sellers to set listings to "hidden". Hidden listings will not appear in the store tab of their page when other users look at the page (the owner can still see the hidden listings).
5.  If a user enters the address of the hidden listing in the address bar, they can still see and purchase it. This allows for private listings \[_note that the client will not display listings with a "hidden" flag to people using the client, but third parties crawling nodes can still see the listings_\].
6.  Addresses are now more flexible. The street, state/territory/region and postal code fields are all optional, and a contact field has been added, where buyers can add information like an email address or phone number.
7.   Changed stores to list the most recently saved listings first, after pinned listings \[frequently requested by vendors\].

\[caption id="attachment_1111" align="aligncenter" width="648"\][![New listing features shown in red](NewfeaturesOB.png)](https://blog.openbazaar.org/wp-content/uploads/2016/09/NewfeaturesOB.png) New listing features shown in red\[/caption\] **Minor changes**:

1.  Uploaded photos for listings will now auto-rotate based on their EXIF data. Photos that are sideways due to being taken on a mobile device will not have the correct orientation.
2.  A bug was fixed with the review stars that caused fraction in the reviews to add an extra star.
3.  Timezones were removed, they were intended for features that turned out not to be needed.
4.  The list of shippable countries was removed from the purchase modal. That information is shown in the main listing page under the shipping tab.
5.  If a buyer looks at a listing page and has no saved addresses, the section of the page that shows shippable countries will instead show a message that the user does not yet have any saved addresses.
6.  When changing servers, the client will load the last page that specific server was on. That removes the issue where when changing servers the new server would try to load the page the previous server "remembered".

Back End
--------

### Current version

Added multiple [new features](https://github.com/OpenBazaar/OpenBazaar-Server/pull/486) for upcoming 1.1.8 release.

1.  Added "pinned" flag to listing contracts, allowing vendors to pin favored listings and have them displayed at the top of their store.
2.  Added max quantity to listing contracts, allowing vendors to set a maximum quantity a buyer can purchase during a sale.
3.  Added a "hidden" flag to listing contracts, allowing vendors to make certain listings visible or invisible to buyers \[_note that the client will not display listings with a "hidden" flag, but third parties crawling nodes will still see the listings_\].
4.  Added an optional alternative contact field to give buyers and sellers the ability to give each other more relevant contact information easily.

### 2.0

Developer Chris Pacia got a 2.0 OpenBazaar node running over Tor earlier this week, having made the necessary adjustments to IPFS to allow Tor traffic. This is still early and needs more work, but it appears likely that OpenBazaar 2.0 will be able to use Tor. An option has been added for users to choose their preferred bitcoind node over the built-in SPV wallet.