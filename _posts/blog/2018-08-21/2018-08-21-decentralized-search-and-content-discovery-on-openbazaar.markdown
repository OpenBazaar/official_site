---
title: "Decentralized <span class='post-title-extra'>Search and Content Discovery</span> on OpenBazaar"
layout: post
date: '2018-08-21 08:30:00 -0600'
social_title: 'Decentralized Search and Content Discovery on OpenBazaar'
social_description: 'Decentralized Search and Content Discovery on OpenBazaar'
---

_by OpenBazaar Developer Tyler Smith_

**Content discovery** is a crucial component to any ecommerce system, especially 2-sided marketplaces where users are both the buyers and the sellers. Even if vendors have listed a number of great products, if users can't find things they want then they won't become buyers. **Centralized** 2-sided marketplaces like Amazon and Etsy have been able to build robust discovery tools because they control the platform and are able to collect every bit of user data generated there. 

A **decentralized** marketplace like OpenBazaar removes the opportunity for a single organization to own and control all data which creates advantages for users in giving them more freedom and privacy but it also presents some challenges for creating a good content discovery system.

A truly decentralized answer to easy and elegant content discovery does not yet exist but we have developed an approach to help buyers find things they want and need in this growing marketplace while still honoring a valuable principle that decentralization provides: **choice.**

![Search Providers in OpenBazaar](Search Providers in OpenBazaar.gif "Search Providers in OpenBazaar")

### Federation: A stop between centralization and full decentralization
In version 1.0 of OpenBazaar we tried our hand at a truly decentralized search index but the results were less than ideal. The technology is just not there yet. In response to the search deficiencies then, the market acted in the form of DuoSearch, which was a company that decided to build a crawler for the network and maintain their own centralized index. Users had to leave the OpenBazaar app and go to the DuoSearch website to easily browse items. Once they discovered items they wanted to by, they had to return to the app to make the purchase.

For version 2.0 we knew we wanted a system that could be as nice to use as DuoSearch, from inside the app, and without requiring all users to use a single, centralized search engine. The solution is **a federated search system** that anybody can participate in. In version 2.0, each search provider can build and maintain their own view of the network but conform with a common interface that allows them to be used interchangeably in systems. Nobody has an upper hand and everybody can compete on quality and features.

### Basics of building a search API for OpenBazaar
Anybody can build a search provider that can be added to the client by ensuring their API is compliant with [OBIP2](https://gist.github.com/tyler-smith/44b5cc8065042f221630cb5c8be505bf) which defines a spec for how the OpenBazaar client and search providers interact. Any API following the spec can be consumed by OBIP2 clients which means anybody can build their own search engine any way they'd like to. They show any listings they want, any filters they want, and score results any way they want.

In order to serve search results a, search developer needs to crawl the network using the OpenBazaar server API and index the results into a system like [Elasticsearch](https://www.elastic.co/) or [Algolia](https://www.algolia.com/). They also need to frequently re-check their data to ensure the content is still available on the network.

After indexing all the data they need to build an API satisfying the OBIP2 interface so that OpenBazaar users can add the root URL to their client and begin using the search engine.

### Customizing your search experience
A search provider could be completely free for use, monetize their search by selling paid promotion slots, or sell premium search endpoints. It's entirely up to them how they'd like to run it.

Every provider decides what results to show for any given query and they define their own filtering and sorting options. This allows them do things like experiment with new features or specialize in only certain types of listings.

Someone could create a food-oriented search where users can filter by types of food or ingredients and sort by nutritional value. Or a search engine for clothing with options related sizes and styles. The OpenBazaar protocol and applications have no concern for what data is being served, as long as it's being served in the proper format for users to access.

### Common issues and future improvements
Crawling the network and keeping the data fresh is the most challenging part of building a search provider. Search providers want to make sure everything they serve is still available on the network. They also don't want to serve listings whose names have expired on the network which can be tricky to track.

In the future we plan to make this much easier and more reliable by utilizing [PubSub in IPFS](https://ipfs.io/blog/25-pubsub/) to broadcast updates that anybody can listen for. Providers will only need to listen on the update channel to get all the information necessary to update their index.

We're aware that the tooling and documentation around the lower level details on how to build a working crawler could stand to be improved. We are working on a future post that goes into more technical details and explanations and are considering how we can create open tooling to make it as easy as possible for anybody to participate in the OpenBazaar content provider ecosystem.
