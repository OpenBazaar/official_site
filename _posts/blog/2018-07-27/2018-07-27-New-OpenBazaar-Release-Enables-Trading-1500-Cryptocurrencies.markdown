---
title: "New OpenBazaar Release Enables <span class='post-title-extra'>Trading 1500+ Cryptocurrencies</span>"
layout: post
date: '2018-07-27 08:30:00 -0600'
social_title: 'New OpenBazaar Release Enables Trading 1500+ Cryptocurrencies'
social_description: 'A new version of OpenBazaar has been released that makes several improvements to cryptocurrency trading.'
---

OpenBazaar [version 2.2.2](https://github.com/OpenBazaar/openbazaar-desktop/releases/tag/v2.2.2) was just released, and this update gives users several new improvements to the cryptocurrency trading feature. This release also includes other improvements and bug fixes; for full details read the release notes posted below.

## Cryptocurrency trading

This release includes two major improvements to the cryptocurrency trading feature within OpenBazaar.
The first is the ability for users offering to trade coins to mark up or discount their price. Instead of only being able to offer a trade at market price, they can choose to add a markup, which will automatically increase the price to the buyer based on the percentage they choose. They can also choose to offer a discount from market price.

The software constantly is updating the market price of the cryptocurrencies involved in the trade, and will add the markup or discount at the moment the trade happens.

![Setting a markup or discount on OpenBazaar](Cryptocurrency Listing Type Chose from Over 1500 Coins.gif "Setting a markup or discount on OpenBazaar")  


The second improvement to cryptocurrency listings is a major expansion of how many coins can be bought and sold on the platform. Previously there were about 60 available. Now we're integrated price data from CoinMarketCap and there are more than 1,500 coins you can trade on OpenBazaar.  

![Choosing from over 1500 cryptocurrencies](Cryptocurrency Listing Type Price Modifier.gif "Choosing from over 1,500 cryptocurrencies")  

As always, there are no fees to pay and no accounts to sign up for. It's a direct swap of cryptocurrencies between you and the other party, and if you choose a moderated payment (highly recommended) then there's a third party available in case of dispute.

If you want to buy or sell coins without fees or without signing up for an account, [give OpenBazaar a try](https://www.openbazaar.org/download/) and let us know what you think.

# Release Notes

This is a minor release, focused on adding improvements to cryptocurrency listings, such as the ability to set their price above or below the market.

## New Features

* The ability to adjust the price of a cryptocurrency listing by a percentage relative to the market is now available. #1416, #1438
* A view on web feature was added to several screens. This provides a link to the same data on openbazaar.com. #1403, #1413, #1430, #1441
  
## Improvements

* The name of each address in the settings modal is now bold. #1459
* The order of the items in the nav menu was adjusted, and your name is now clickable. #1459
* New details were added to the opt-in metrics. #1440, #1446
* The trumbowyg text editor will now be translated if it has the required language files. #1436
* Moderators that don't use the same cryptocurrency as the user cannot be added as a moderator. If they were already added, they will be marked as invalid so they can be removed. #1420
* Non-translated text is now translated. #1392, #1382, #1435
* When a cryptocurrency order is fulfilled, the tx sent by the seller can be clicked if it is a URL. If HTML is included in the data, the HTML is removed. The data is validated to not be more than 512 characters. #1386, #1396, #1397
* A script to download and implement new cryptocurrency data for cryptocurrency listings was implemented. This is run manually before each release. #1384, #1422, #1423, #1429, #1479
  
## Bug Fixes

* A rare problem where the debug log can have an error has been corrected. #1480
* A new node will now have a default value of 0 for their reviews instead of showing an error. #1477
* A bug preventing a user from looking at their own moderator details modal has been fixed. #1473
* The memo in a purchase will no longer be cleared on a screen rerender. #1467
* When an order times out, but has not been fulfilled, when the seller claims the payment the buyer will no longer be told they can complete the order. #1463
* A potential race condition in the order details screen was corrected. #1452
* Some minor issues with disputes when only one party's contract has been received by the moderator were cleaned up. #1448
* BCH QR codes will not always have the proper prefix. #1418
* A problem with the shipping option selection resetting when interacting with the purchase page was corrected. #1402, #1442, #1447
* An issue with the free shipping tag not being horizontally aligned in the store screen was fixed. #1385
  
## Internationalization

We are actively translating the text in the OpenBazaar reference client. If you are interested in volunteering as a translator, you can sign up at https://www.transifex.com/ob1/openbazaar

## Special Thanks

A special thank you goes out to the many volunteers that provide translations, contributor rhcastilhos, and to our testers that discovered important issues.

