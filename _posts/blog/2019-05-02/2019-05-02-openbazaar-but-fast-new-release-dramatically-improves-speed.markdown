---
title: "OpenBazaar, but Fast: New Release <span class='post-title-extra'>Dramatically</span> Improves Speed"
layout: post
date: '2019-05-02 08:30:00 -0600'
social_title: 'OpenBazaar, but Fast: New Release Dramatically Improves Speed'
social_description: 'This is a minor release, focused on improvements to the network and an enhanced Discover experience.'
---

OpenBazaar 2.3.3 released today. This is a minor release, but delivers substantial improvements to the user experience, such as rapid loading of listings from search.

We recommend that you [backup your OpenBazaar data](https://openbazaar.zendesk.com/hc/en-us/articles/115002761312-How-do-I-backup-my-store-) before you update.

{% include modules/embeded-video.html url="https://www.youtube.com/embed/PoVWVLSH7Tg"%}

[Release Notes - Client](https://github.com/OpenBazaar/openbazaar-desktop/releases)
-----------------------------

**Improvements**

* Listings in the Discover page and user's stores are now loaded by IPFS hash as well as IPNS lookup. In most cases this will cause the listing to load very quickly from IPFS. When the IPNS listing loads, if it is different from the IPFS data it will replace it.
* When using the OB1 search provider, a category-based experience will be provided as a default. This more closely matches the experience on openbazaar.com. Other providers will use a normal search experience, as we can't be sure if they would supply the same data in the same format needed for the OB1 design. 
* When using a search provider that does not provide Tor endpoints, the search calls will use the provider's non-Tor endpoints instead. This is still secure, as traffic is still routed through Tor. Tor endpoints are used by some search provider's to get around issues with CDNs like Cloudflare. 
* The app is now using Electron version 4.1.3. 
* The block explorers have been updated to more privacy-focused websites.

**Bug Fixes**

* A layout issue with some buttons was corrected.
* Conditions on listings were not being shown due to a typo, they are now working.
* An issue that caused the default image to sometimes not load in avatars with no data was fixed.

[Release Notes - Server](https://github.com/OpenBazaar/openbazaar-go/releases)
-----------------------------

The focus of this release is updating underlying [go-ipfs to v0.4.19](https://github.com/ipfs/go-ipfs/releases/tag/v0.4.19) and improving IPNS resolution. Notable to this release are the AutoNAT and AutoRelay features (which are disabled by default, but a necessary component for connectivity for mobile and clients which are unreachable via inbound connection (which are typical in NAT scenarios). Additionally, IPNS resolution (the process which converts the peer ID to the most-recently-updated "content root" for that peer) is now improved with the addition of OB1-provided infrastructure.

In addition to this release, the multiwallet API /wallet/spend endpoint now supports a "sweep wallet" behavior that allows the wallet to be emptied without clever math from the user.

**Enhancements**

* Rebase onto IPFS v0.4.19
* Added Method check for HEAD to validate undefined endpoint
* Add spend all functionality to wallets
* Improve multiwallet logging; Failure handling
* Add EnableAutoRelay/EnableAutoNAT options to config
* Add API router functionality

**Refactoring**

* Remove stubbed subcommands Stop and Restart

**Testing**

* Update go for internal testing/building to v1.11

**Bug Fixes**

* Fix unhandled error in sign methods
* Fix IPFS protocol identifier handling
* Proper network lookup fix

**Documentation**

* Add a blurb about min Golang version in README

**Internationalization**

We are actively translating the text in the OpenBazaar reference client. If you are interested in volunteering as a translator, you can sign up at [https://www.transifex.com/ob1/openbazaar](https://www.transifex.com/ob1/openbazaar)

**Special Thanks**

A special thank you goes out to the many volunteers that provide translations, and to our testers that discovered important issues.

For more development details, please see the release notes on Github:

* [Client](https://github.com/OpenBazaar/openbazaar-desktop/releases)
* [Server](https://github.com/OpenBazaar/openbazaar-go/releases)