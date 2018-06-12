---
title: "Development Update: Using IPFS for Encrypted Chat" 
layout: post
date: '2017-02-17 00:30:00 -0300'
---
        
_For the past couple of weeks, [OpenBazaar](https://blog.openbazaar.org) front-end developer **Rob Misiorowski** has been elbows-deep in the development of the 2.0 chat feature. Here is a look into some of the work he’s been doing:_

For the past few weeks I’ve been working on the chat function for version 2.0 which is similar to current 1.0 chat, with a few enhancements on the user’s side. Notably planned is emoji support, typing & message read indicators, and an Unread Messages badge indicating offscreen threads with unread messages.

There are new things going on under the hood, though. To get certain data needed for the Chat UI (handle, avatar hash, location), individual profiles for each user in the UI need to be obtained. These need to be obtained via IPNS, which has been quite slow (calls often take 10+ seconds). The problem with having to make an individual call for each chat head is that the browser has a limit of 6 concurrent HTTP requests to the same domain. So, if we clog that up with bulky time-consuming IPNS calls, the rest of the app will be blocked. For example, if the user tries to navigate to another page, any data required for that page will go to the end of the HTTP request queue and would need to wait until no more than 5 of the chat IPNS calls are left. That could be a while and in the meantime the user would just be looking at a loading spinner which is a great way to ruin the usability of a feature.

_**What is IPNS?**  
It’s new. Here’s a digest from back-end developer Tyler Smith: IPNS is like DNS for [IPFS](https://ipfs.io/) content. It let’s you find IPFS data by a name if you don’t know the hash. The hashes verify integrity so IPFS only needs to find one copy of the content when you search by hash. But when you search by name it has to talk to many nodes and find a quorum of what hash a name points at which makes it much slower._

So what we decided to do was expose an HTTP endpoint on the server where you could request profiles in bulk. For example, if we need 10 profiles, we could request them in 1 call, instead of 10. Furthermore, the endpoint has an ‘async’ option, which if true would send the profiles back via sockets as they are obtained by the server. Long story short, we’re not clogging up the UI and we still get the profiles as they’re available. Hooray!

**Additional thoughts about IPFS/IPNS from Rob:**

In our experience, direct IPFS calls have been fairly performant. IPNS calls, on the other hand, have been quite slow. Apparently the bottleneck is that it takes quite a bit of time for the IPFS system to get the mapping of peerId to hash. When we were at [Coindesk’s Construct 2017](http://www.coindesk.com/events/construct-2017/) event a couple of weeks ago we brought this up with the IPFS team and they gave us an idea of how we could improve this performance. It basically involves having the server register in a pub / sub system with other nodes so that as soon as a node has its hash available, it publishes it in real time and any subscribed servers could cache that mapping. That way, the expensive lookup wouldn’t have to happen as the UI is trying to get data. We haven’t looked into implementing that yet and it’s unknown how much of an improvement that would give us, but it does sound quite promising!

### ICYMI

**In case you missed it,** here is other notable news from the last couple of weeks:

[Openbazaar Integrates Tor – The Platform’s Most Requested Feature](https://news.bitcoin.com/openbazaar-integrates-tor-platforms-requested-feature) – _news.bitcoin.com_

* * *

**Are you a developer who wants to get involved in this early stage?**  
_Get the details [here](https://blog.openbazaar.org/milestone-1-developer-release-for-openbazaar-2-0)!_

**Want to start RIGHT NOW buying and selling with Bitcoin using version 1.0?**  
_[Download OpenBazaar now](http://openbazaar.org/) and do the thing!_