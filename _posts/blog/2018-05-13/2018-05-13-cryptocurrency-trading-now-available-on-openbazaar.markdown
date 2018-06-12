---
title: Cryptocurrency Trading <span class='post-title-extra-alternative'>Now Available
  on OpenBazaar</span>
layout: post
date: '2018-05-13 00:49:16 -0300'
---

OpenBazaar **version 2.2.0** was released today. For the full list of new features and improvements in this release, check out the release notes at the end of the post.

The biggest new feature is the ability to ** buy and sell cryptocurrencies**.

## Cryptocurrency Trading on OpenBazaar

{% include modules/embeded-video.html url="https://www.youtube.com/embed/q6ki3_1Io-U"%}

Vendors are now able to use a special new listing type to **sell cryptocurrencies on OpenBazaar**. They can choose from 44 different cryptocurrencies right now and more will be added over time. Payment must be settled in whichever coin they have chosen for their OpenBazaar store, either Bitcoin, Bitcoin Cash, or Zcash.

![crypto listings](cryptolistings.gif)

Because OpenBazaar is completely peer-to-peer, **this is not an exchange**. This new feature doesn’t include an order book with the ability to choose a target price for buying or selling. This new feature only allows people to trade cryptocurrencies directly with each other at market prices. It benefits from OpenBazaar’s main advantages; users trading cryptocurrencies on the platform **won’t need to pay any fees** and **they aren’t forced to reveal any identifying information**.

We’ve released this new feature with the goal of listening to the community about how they believe cryptocurrency trading on OpenBazaar can be improved. We plan to rapidly iterate as we receive feedback from users.

**Please join us on [Slack](https://openbazaar.org/slack) and [Twitter](https://twitter.com/openbazaar) to give us your thoughts on this new feature!**

## Opt-in Analytics
Because OpenBazaar has been built with privacy in mind, the development team isn’t able to gain much information about how people use the software. This is good for privacy, but can sometimes hinder development. In order to gain more insight on how OpenBazaar is being used – and how to improve it – we’re introducing an **opt-in analytics package**. Users who choose to opt in will share non-identifying data with the development team. The list of data being shared is displayed when opening the new release for the first time. Users can start or stop sharing data at any time in their Settings.

## Release Notes
This is a major release, which adds buying and selling cryptocurrencies, opt in analytics, and many optimizations and bug fixes.

## New Features
– The ability to buy and sell cryptocurrencies was added. The currencies can be sold at market rates. This feature is experimental, and is expected to be rapidly iterated on as we recieve feedback from users. #1308
– An opt-in analytics package was added. Users are able to choose to share non-identifying data with the development team. This will facilitate identifying bugs and improving the app. Users can start or stop sharing data at any time. #1277

## Improvements

- Norweigan, Polish, and Ukranian translations reached the 80% translated requirement, and were added as options for the client. #1324
- When viewing your sales, unfunded orders will now be hidden by default, since you cannot take action on those orders, and they clutter up the list of orders. You can still chose to view those orders. #1310
- Listing card image loads will now cancel when the image card is no longer on the screen. This primarily improves the experience when changing pages in the search results or navigating away from a page of search results that hasn’t finished loading. #1309
- Verified moderators are now lazy-loaded. This will speed up startup, and notify the user if the list of verified moderators changes while they are looking at information that will be affected by that change. #1298
- Verified moderators are loaded from a Tor endpoint if the user is in Tor mode. #1284

## Bug Fixes
- Blockdozer changed their URL for viewing BCH transactions, the URL used when viewing details of transactions has been updated. #1320
- An issue where the no valid moderators error would show on an error at the same time as the no verified moderators message, and with the wrong formatting, was corrected. #1307
- A problem where invalid mods would never stop loading was fixed. #1306
- Error messages meant for only the purchase flow no longer appear in the settings/store tab. #1306
- Some layout issues with moderator cards were corrected. #1300
- In the settings/store tab, if a moderator assigned to your store has become invalid, now the only option is to de-select them. #1300
- An unused memo parameter was removed from the purchase call. #1314
- A minor layout issue was corrected in the transactions list. #1285
- The bug where pages stats are changed to zero in the page tabs on the user page when the page settings are updated was fixed. #1287
- A layout issue with verified moderators was fixed. #1270
- Store pages will now open if one of the listings in them has an unrecognized currency value. #1269

## Internationalization
We are actively translating the text in the OpenBazaar reference client. If you are interested in volunteering as a translator, you can sign up [here](https://www.transifex.com/ob1/openbazaar). 

## Special Thanks
A special thank you goes out to the many volunteers that provide translations, and to our testers that discovered important issues.