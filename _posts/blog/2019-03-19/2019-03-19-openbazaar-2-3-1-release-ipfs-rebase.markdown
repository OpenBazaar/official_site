---
title: "OpenBazaar 2.3.1 is Released <span class='post-title-extra'>with IPFS Rebase</span>"
layout: post
date: '2019-03-19 08:30:00 -0600'
social_title: 'New OpenBazaar Release with IPFS Rebase'
social_description: 'New OpenBazaar release allows you to use multiple cryptocurrencies in peer-to-peer marketplace'
---

OpenBazaar version 2.3.1 has [been released](https://github.com/OpenBazaar/openbazaar-desktop/releases/tag/v2.3.1) and was primarily focused on upgrading the underlying [IPFS](https://ipfs.io) library to 0.4.18. This release prepares the development team to enable some features which will improve message deliverability and discovery on the network. In addition to the IPFS update, we have several minor fixes and improvements which resolve some painful timing bugs and general code improvements and reorganizations.

This is a minor release but we do recommend that you [backup your OpenBazaar data](https://openbazaar.zendesk.com/hc/en-us/articles/115002761312-How-do-I-backup-my-store-) before you update.


Release Notes
-----------------------------

This is a minor release, focused on an IPFS rebase in the go server. It is important to back up your store before running this update.

This release uses version 0.13.1 of the openbazaar-go server. You can view server changes at this link:
https://github.com/OpenBazaar/openbazaar-go/releases/tag/v0.13.1

**New Features**

* A bulk coin accepted updater control was added in settings/store. This allows a seller to update all the coins accepted by all their listings at the same time.
  
**Improvements**

* Blockbooth was removed from the list of default search providers.
* Improvements were made in how moderators are loaded in the purchase screen, so the spinner doesn't continue forever if one of them fails to load.
* Code was added to handle upcoming changes to the peerID format.
* A few changes were made to the metrics collected.
* Some code clean up. 
* When coping a contract in the order details screen, the JSON is now formatted nicely. 
* Inputs are sanitized, to prevent any issues with a user entering invalid or harmful characters.

**Bug Fixes**

* An adjustment was made to prevent security software from incorrectly flagging the OB update as malware. 
* A bug that caused the dispute resolve button to not appear in disputes using ZCash was fixed.
* If the url is missing a protocol in the fulfillment of a digital order, it will now open correctly. 
* An issue where the user page wouldn't update the user's name if it was changed was corrected. 
* A bug with the warning about external links showing when using Tor was fixed.
* Minor fixes.

**Internationalization**

We are actively translating the text in the OpenBazaar reference client. If you are interested in volunteering as a translator, you can sign up at [https://www.transifex.com/ob1/openbazaar](https://www.transifex.com/ob1/openbazaar)

**Special Thanks**

A special thank you goes out to the many volunteers that provide translations, and to our testers that discovered important issues.

For more development details, please see [the release notes on Github](https://github.com/OpenBazaar/openbazaar-desktop/releases/tag/v2.3.1).

