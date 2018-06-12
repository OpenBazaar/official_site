---
title: "OpenBazaar 1.1.8 Released; New Features Added" 
layout: post
date: '2016-10-20 00:30:00 -0300'
---
        
Today we've released [version 1.1.8](https://github.com/OpenBazaar/OpenBazaar-Installer/releases/tag/v1.1.8), the first release in a few months. This release adds several new features for vendors as well as a significant amount of bug fixes and code improvements. You can download this new version on the [openbazaar.org](https://openbazaar.org/) page. We've also created an installer which only contains the client for users who have a server hosted remotely (such as a VPS) and don't need a local server installation. If you want to use the client-only installer, visit the [Download page](https://openbazaar.org/download.html?v1.1.8) and choose the "Client Only" installer for your operating system.

Features
--------

#### Pinned listings

Vendors can now choose certain listings they want highlighted in their stores. When creating a listing, or editing an existing listing, vendors can select "Pinned" if they want that listing to be displayed to buyers at the top of their storefront. There is no limit to how many listings may be Pinned, all Pinned listings will be shown before un-Pinned listings.

#### Hidden listings

Vendors can now create Hidden listings. When creating a listing, or edit an existing listing, vendors can select "Hidden" if they don't want visitors to their store to see that listing. The vendor can still see it, though it will be faded out to indicate it is hidden. However, these listings can still be visited with the listing address, allowing vendors to create private listings that are only visible to people they give the listing address. This feature allows vendors to have more control over who can access their listings, and when. (_Note that the client will not display listings with a “hidden” flag to people using the client, but third parties crawling nodes can still see the listings)._

#### Maximum Quantity

Vendors can now set a maximum quantity on their listings, which prevents a buyer from purchasing more than the number of items they specify in one order. This gives vendors a simple inventory management system. If the Max Quantity is set to zero, the item is still visible, but cannot be purchased. \[caption id="attachment_1111" align="aligncenter" width="648"\][![New listing features shown in red](NewfeaturesOB.png)](NewfeaturesOB.png) New listing features shown in red\[/caption\]

Improvements
------------

#### Addresses

We've made the following improvements to addresses:

1.  The first address in the Addresses tab of Settings is now marked as the Default Address.
2.  Addresses in the Addresses tab of Settings can now be reordered by dragging.
3.  Addresses are now more flexible. Only the name and country are required, and a new contact method field has been added.
4.  The appearance of very long addresses in the purchase flow has been improved.

#### Images

We've made the following improvements to images:

1.  The Avatar in the Page tab of Settings can now be rotated with rotation buttons.
2.  The buyer and seller avatar pictures now appear on the close dispute form for moderators.
3.  When images are uploaded to listings, if the image has an orientation in its EXIF data (for example, if it was taken on a phone in landscape mode), the image will automatically be rotated to match the orientation.

#### Shipping

We've made the following improvements to shipping:

*   The list of shippable countries in the address panel of the purchase modal has been removed, it was made obsolete by the Shipping tab in the listing page.
*   The "ships to" field in the edit listing screen now has a clear all button.
*   Listings have a "Ships From" field now, so each listing can have a different shipping origin. It defaults to the Country value set in Settings/General.

#### Miscellaneous

*   Various optimizations have been made to the following, follower, and store tabs in the User Page, and to the Discover view, which should speed up rendering and reduce the strain on the Chromium browser.
*   The last view is now saved per-node. This means if you connect the client to a different node, the last view saved for that node will be loaded, instead of trying to load the view the current node was on.
*   Listings in the Store tab are now ordered by most recently saved.
*   Tags have a maximum length of 40 characters. Old longer tags are truncated at 90px wide.
*   Chat messages are never shown for blocked GUIDs.
*   The language for NSFW was updated to "Adult or Offensive Content" from "18+ (Adult Content)" since the definition of adult is not 18 in all countries, which caused confusion.

#### Bug fixes

This release has a significant number of bug fixes. For the full list, check out the [release notes](https://github.com/OpenBazaar/OpenBazaar-Installer/releases/tag/v1.1.8).

Statistics
----------

15 commits made in the master branch and six issues closed on the [server repository](https://github.com/OpenBazaar/OpenBazaar-Server).

123 commits made in the master branch and thirty-four issues closed on the [client repository](https://github.com/OpenBazaar/OpenBazaar-Client).

The 1.1.7 installers were downloaded more than 37,000 times since release in late June.