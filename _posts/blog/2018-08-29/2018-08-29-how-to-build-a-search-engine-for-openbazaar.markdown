---
title: "How To Build a <span class='post-title-extra'>Search Engine</span> for OpenBazaar"
layout: post
date: '2018-08-21 08:30:00 -0600'
social_title: 'How To Build a Search Engine for OpenBazaar'
social_description: 'How To Build a Search Engine for OpenBazaar'
---

_by OpenBazaar Lead Backend Developer Chris Pacia_

When we were designing [OpenBazaar](https://openbazaar.org/download), now the world's largest decentralized marketplace, we knew the general approach to creating a **search engine** that delivered high quality results was to use a centralized server to index listings and run search queries. A centralized search experience, however, was completely out of line with the **freedom** and **flexibility** this open-source marketplace represents. We knew there had to still be some intermediate step we could take.

### A Federated Approach

We decided to do what few other platforms have done and open it up so that [anyone can create a search engine that is compatible with the OpenBazaar app](https://openbazaar.org/blog/decentralized-search-and-content-discovery-on-openbazaar/). This would allow us to start by building our own search engine to help users navigate the network but would relieve their total reliance on it. All the data that needs to be indexed is **public** and anyone can create and run a search engine of their own.

### Building a Search Engine for OpenBazaar

I have written a brief overview of how to build a search engine for OpenBazaar and described some of the outstanding issues we are still working on. It does take some technical skill to build a search engine, but developers with previous experience building and maintaining online infrastructure should be able to create a simple version without too much difficulty.

### Step 1 - Finding Peers

Step one is to build a database of all the peers you want index. There are several ways you can do this:

**1) Actively crawl the network**

The openbazaar-go API provides a couple of APIs to make this easy. `/ob/peers` returns a list of peers you’re connected to:

![ob peers - How To Build a Search Engine on OpenBazaar](ob peers.png "ob peers - How To Build a Search Engine on OpenBazaar")

And `/ob/closestpeers/<peerID>` returns a list of “closer” peers from the DHT. One can crawl the network for more nodes just by iterating over your current peer database and fetching closer peers. 

![ob closest peers - How To Build a Search Engine on OpenBazaar](ob closest peers.png "ob closest peers - How To Build a Search Engine on OpenBazaar")

You can also use the `/ob/peerinfo/<peerID>` endpoint to look at their IP address if you wanted to index only Tor stores, for example. 

**2) Passively listen for new peers**

For this you’d likely want several nodes running at the same time. From there you could stream
peerIDs to your database every time one of your nodes receives a new connection. You might not get all peers this way but you should find most. `openbazaar-go` nodes do not expose an API which streams new peer connections so you’d have to patch a node to get this data. Creating such an API should be relatively easy and it’s something we are considering doing.

**3) Subscribe to pubsub**

We are just now starting to make use of the libp2p’s pubsub capabilities. Currently only IPNS data is broadcast to pubsub channels but hopefully relatively soon we will have all nodes announce new publishes over a pubsub channel. Normal users will not be subscribed to this data--as it is a lot of data--but for people who are building search engines this would be perfect. 

Depending on what data we include in the publish, you should be able to subscribe to the appropriate channel and receive streaming updates from every peer. We’ll be sure to announce and document this functionality when it is available. 

**4) Manual curation**

You could also just manually enter the peerIDs of stores you find interesting in your database. This isn’t actually a bad strategy if you want your search engine to target specific types of products. Complex machine learning algorithms would likely also work for this if you are particularly adventurous.

### Step 2 - Indexing Stores

Now that you have a list of stores it’s time to index them. `/ob/listings/<peerID>` will give you a list of all the store’s listings. 

![Indexing Stores on OpenBazaar](indexing stores on openbazaar.png "Indexing Stores on OpenBazaar")

And if you grab the hash from a listing you can get the full details by using `/ob/listing/<peerID>/<hash>`

![ob listing peerid hash - How To Build a Search Engine on OpenBazaar](ob listing peerid hash.png "ob listing peerid hash - How To Build a Search Engine on OpenBazaar")

You will also need the user’s profile which you can get from `/ob/profile/<peerID>`

![ob profile peerid - How To Build a Search Engine on OpenBazaar](ob profile peerid.png "ob profile peerid - How To Build a Search Engine on OpenBazaar")

From there you can put the listings in whatever database you please to index and search on them. Your API just needs to conform to the specification in [OBIP2](https://github.com/OpenBazaar/obips/blob/master/obip-0002.md) and it will be compatible with the client.

To see your search engine when your stores are indexed, enter the URL here in the OpenBazaar client:

![Add your search engine to OpenBazaar - How To Build a Search Engine on OpenBazaar](add your search engine to openbazaar.png "Add your search engine to OpenBazaar - How To Build a Search Engine on OpenBazaar")

### Step 3 - Keeping Content Fresh

The biggest challenge with running a search engine is avoiding serving stale content. Given that OpenBazaar is still fairly new, users may come and go fairly quickly. You want to avoid serving listings for stores where the owner has not been online in a long time to make sure to give potential buyers a fresh discovery experience.

Further, listings are not guaranteed to persist on the network longer than a week after a vendor has gone offline. It still _may_ be visible to some users due to caching, but not everyone may be able to see the listing. If you serve old listings, a potential buyer might click on it only to get a Not Found error. We recommend not serving listings from vendors which have not been identified as being online at least once within the past week. 

How do you determine that? Admittedly this is an area where we are still working to improve but there are a few ways. 

First, make sure your database of peerIDs also tracks the last seen or last good timestamp for the peer. From there you have several ways you could update the timestamp:

**1) Ping each peer**

The `/ob/status/<peerID>` endpoint will attempt to ping them and tell you if they are online.

![ob status peerid endpoint - How To Build a Search Engine on OpenBazaar](ob status peerid endpoint.png "ob status peerid endpoint - How To Build a Search Engine on OpenBazaar")

The problem, however, is that about 60% of nodes on the network are unreachable due to NAT traversal issues. Tor nodes tend to have even worse issues as many users run on operating systems like Tails and Whonix which lock down the control port and make it difficult to accept incoming connections. So this only gets you part of the way there.

**2) Passively listen for incoming connections**

This is similar to 2) above in Finding Peers. You could update the timestamp for a peer every time they connect to you but again this will either require patching your node or for us to provide an API to get the data. This also will not cover every peer you’re interested in unless you run many nodes.

**3) Disable caching**

If you set `"UsePersistentCache": false` in your node’s config file it will stop returning from cache and will do a new DHT crawl each time you request user data. If the data has dropped out of the network, you will know about it as the data will return not found. If it’s not found, you should generally not serve up that peer’s data. 

Additionally, you’ll likely also want to set `"BackUpAPI": ""` in the config as by default it will try to get the record from our gateway’s cache if the record cannot be found in the DHT.

**4) Use IPNS record validity**

Every time a user publishes new content they publish an IPNS record containing an expiration date in the DHT. That expiration date is the time at which the user’s listings will drop out of the network absent them re-publishing which happens automatically at startup and once a day thereafter. 

When you query for a user’s listings or profile or anything else, your node looks up the IPNS record. You could theoretically use this expiration date as a proxy for the last good timestamp for the peer and beyond that stop serving their listings. 

This data is not yet exposed in our API and it’s something that we have on our list to develop.

**5) Use pubsub**

Currently, whenever you query for a peer’s data, it subscribes to streaming updates for that peer. This means you’ll be notified immediately whenever they publish a new IPNS record. Not only does this tell you when they have signed online, but you could also get the latest IPNS record validity. 

Currently, disabling cache--3) above--also disables pubsub and would make this method ineffective. This is another issue that we are working on improving.  

### Step 4 - Making Money!

It's entirely possible for you to monetize your work on an OpenBazaar search engine by adding paid ads in your search results. In fact, you could pretty easy sell ad space for your search engine through your own OpenBazaar store! The only real missing piece is we’d like to create an ad badge for the UI that calls out which listings are ads. This would just require adding a single piece of data to the listing JSON in your search results. 

### Issues and Improvements

This is a general overview of the technical work required for building an OpenBazaar search engine. We're aware of some areas we would like to improve upon such as creating an API that allows us to stream newly found peerIDs and also have APIs that allow us to inspect IPNS records or pubsub publishes to update our timestamp associated with each peer. We could likely combine all of this into one streaming API that pulls data from all these sources and streams not only new peerIDs that it finds, but also the most up-to-date timestamp for that peer that it is able to decipher. This way search engines only need a single API to update their peers database. 

We are constantly working to make it easier for anyone to jump right in and start building on the OpenBazaar platform. If you have any questions or comments about any of this, please join our conversation in [Slack](https://openbazaar.org/slack) and tell us what you think.
