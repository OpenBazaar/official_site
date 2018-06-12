---
title: "Milestone 1 Developer Release for OpenBazaar 2.0" 
layout: post
date: '2017-01-17 00:30:00 -0300'
---
        
 Today we've reached the milestone 1 version of the OpenBazaar 2.0 software. This release is meant solely for developers and those building or intending to build on top of the OpenBazaar platform. The release is _not_ meant for end users and is missing numerous core features needed for engaging in real transactions. Before the launch of the full version of the 2.0 software we will have a formal beta with a fully featured release; details of this formal beta will be posted on this blog soon. We define milestone 1 as such:

> Beta Users can download and install the client and server from github, and use it to fill in their profile, store info, and post listings. The network can host listings, stores, and user profiles.

This is the bare level of functionality needed for developers to use and understand key aspects of the new design in the 2.0 software. Developers can now begin using the software to post and retrieve data from the OpenBazaar / IPFS network, enabling the building of crawlers, search engines, and other tools.

Instructions
------------

Developers can install the [server](https://github.com/OpenBazaar/openbazaar-go) and [client](https://github.com/OpenBazaar/openbazaar-desktop) from source, or use the [bundled release](https://github.com/OpenBazaar/openbazaar-desktop/releases). You can find API documentation [here](https://cpacia.github.io/). If the 2.0 software has been installed on your machine previously, you'll need to delete the existing OpenBazaar2.0 data directory before installation. When running the program the first time, you may need to wait a few moments and click "Retry" if the connection fails. Developer releases include a "Feedback" button to send feedback to our development team. Note the button on the bottom right of the client in the following image.

Milestone 2
-----------

The next milestone focuses on product discovery and communication. Users will be able to search for listings using third party services, and browse listings using the new "channels" feature. Direct chat between users will also be completed.   