---
title: "Development Update: February 3, 2017" 
layout: post
date: '2017-02-03 00:30:00 -0300'
---
        
The [Milestone 1 developer release of OpenBazaar 2.0](https://blog.openbazaar.org/milestone-1-developer-release-for-openbazaar-2-0/#.WJTcdrYrLOQ) is available--now with a little bonus: **Tor integration!** Tor has been the most requested feature by far since we started the project. This encrypted browser masks your IP address, improving privacy. Normally Tor isn't too difficult to integrate, but since OpenBazaar is more complex than your typical app we needed to write a custom transport for IPFS and programmatically configure the node to run as a hidden service. In version 2.0 users will be able to run their stores with more privacy than ever before. We are now waiting to give developer users some time to review the PR before merging it and would appreciate your contributions if you are familiar with the setup! You can check it out [here](https://github.com/OpenBazaar/openbazaar-go/pull/342). **Milestone 1 Summary** This release is meant solely for developers and those building or intending to build on top of the OpenBazaar platform. You can read more about what the release entails [here](https://blog.openbazaar.org/milestone-1-developer-release-for-openbazaar-2-0/#.WIJ8GrYrKV4). _Since this is a release meant for development, the functions available in Milestone 1 are very minimal._ They include:

*   Users can download and install the client and server from Github, and use it to fill in their profile, store info, and post listings
*   The network can host listings, stores, and user profiles
*   Users can follow and unfollow

**Here's a short walkthrough video of the Tor integration in 2.0 by OpenBazaar developer Chris Pacia:**   https://youtu.be/QlbDEKew1SU  

* * *

**Are you a developer who wants to get involved in this early stage?** _Get the details [here](https://blog.openbazaar.org/milestone-1-developer-release-for-openbazaar-2-0/#.WJuWRxIrLOR)!_ **Want to start RIGHT NOW buying and selling with Bitcoin using version 1.0?** _[Download OpenBazaar now](http://openbazaar.org/) and have at you!_