---
title: "How OpenBazaar & Bitcoin Could Kill the <span class='post-title-extra'>American Pickers</span> Economy"
layout: post
date: '2018-12-13 06:30:00 -0300'
social_title: 'How OpenBazaar & Bitcoin Could Kill the "American Pickers" Economy'
social_description: 'Those of us in the western world often have a lot of stuff and the holiday season encourages us to acquire more. It made me think about how many of us even really know how much stuff we already have and my fascination with the TV show American Pickers.'
---

_By Sam Patterson, OB1 Co-Founder_

> _**Note:** This post is a bit of speculation on creative use cases for OpenBazaar recently re-inspired by [this community post on Reddit](https://www.reddit.com/r/OpenBazaar/comments/9x4p69/openbazaar_more_than_just_your_standard_storefront/). OpenBazaar is a simple cryptocurrency marketplace built on an open-source network that can be used, grown and changed by users around the world._

> _Let us know what your creative ideas for OpenBazaar are on [Reddit](https://reddit.com/r/openbazaar), in [Slack](https://openbazaar.org/slack), or on [Twitter](https://twitter.com/openbazaar)!_

It's the holiday season again. Like many people, I have been thinking a lot about the stuff we acquire and exchange as a demonstration of love this time of year.

_Stuff._ 

_Things._ 

_Posessions._

Those of us in the western world often have a lot of _stuff_ already and this season encourages us to acquire more. It made me think about how many of us even really _know_ how much stuff we already have and my fascination with the TV show American Pickers. If you haven't watched it before, take 2 minutes to watch this clip:

{% include modules/embeded-video.html url="https://www.youtube.com/embed/tKu-rCXkad4"%}

**This clip demonstrates a few common themes in the show:**

1. The owner of the item had lost track of where it was. Often in the show, the owners aren't even aware of the item's existence.
2. The method to determine a price to sell the item was informal, and time consuming. There's a good chance one of the parties in the trade was far away from a 'market price'.
3. Transactions are done in person, in cash.

The setting of the show is somewhat unique; they typically find rural collectors who have barns full of old items. But some of the themes of the show are mirrored in the broader economy as well, at least in developed economies.

#### How Do We Know What Stuff We Already Have?

Keeping track of personal possessions depends largely on the individual, but it is usually done informally. Few people formally track all the objects they own. One popular method is simple: don't keep track, and have periodic yard sales to deal with excess possessions. On a somewhat regular basis (typically each spring or summer), people will sort through their possessions and determine which items they want to keep, and which they are willing to sell. In this sense, a yard sale serves the following functions:

1. Periodically **updating your own knowledge** about your possessions and how much you value them.
2. **Transmitting some of that information** to your local community by displaying those items publicly and pricing them.
3. **Reducing the number of unwanted possessions** and **increasing cash** (or occasionally improve possessions through barter).

> (As an aside, this might explain how 'pickers' can be successful; their physical presence and interest in your possessions is a simpler method for achieving these three functions.)

This method of keeping track of possessions has worked well enough for most people, but it's far from ideal. The largest cost is **time**. Preparation requires manually sorting goods and determining their price, physically sorting them (and putting back what wasn't sold later), then waiting for others to take an interest in them. A yard sale typically takes at least a day's worth of activity. The haggling itself - similar to the pickers - benefits those who have more information about the product.

The advent of the Internet is already allowing better methods. Online platforms for buying and selling goods allow people to more effectively sell their unwanted possessions by opening up the information beyond the local community. However, these platforms have significant drawbacks:

1. The platforms **charge fees**, and the payment methods they use often charge fees as well.
2. The platforms **monitor the data** of the people listing their possessions, which is **typically tied to their real-world identity**.
3. The platforms have their own **restrictions around listing possessions**, from type of goods they allow to the length of time they can be hosted.

Using these platforms is an incremental improvement over the yard sale. It still requires manually assessing and valuing your own possessions.

#### How OpenBazaar and Bitcoin can Manage Personal Possessions

![Tracking Personal Inventory on OpenBazaar](tracking_personal_inventory_on_openbazaar.png "Tracking Personal Inventory on OpenBazaar")

[OpenBazaar](https://openbazaar.org/download) is a decentralized network for trade; users run the software locally and connect directly to other users to buy and sell goods and services. There is no central institution to take a cut, monitor data, or restrict trade.

[Bitcoin](https://bitcoin.org) is a digital currency and payment network; users control their own money locally and aren't reliant on banks or payment processors.

Together, these platforms could change the way we keep track of our personal possessions. Our own knowledge of our possessions - and their value - doesn't need to be manually re-evaluated informally and periodically, but instead continually tracked and updated. Nor does this information need to be manually transmitted to the local or global community; it can be automatically (and anonymously) displayed to the world, continuously, at no cost.

This can be achieved by representing possessions as **Ricardian contracts** (I'll just refer them them as contracts), and publishing them to the OpenBazaar network. Ricardian contracts are a data structure that allows goods and services to be represented electronically; these contracts allow users to put in any information about a possession as well as the price they value the good at. When a user creates a contract, the OpenBazaar client publishes the information to the network, and other users can view that contract. 

If they choose, the user could put in a price for which they'd be willing to sell the item. If anyone in the world values that possession more than the current owner, they could instantly make an offer.

If a user isn't willing to sell a possession, they could simply create a contract and choose to keep the information about it stored locally.

#### The Downside

Retroactively listing possessions as contracts would be time-consuming. However, if a user were to begin creating contracts for all new possessions they gain, eventually most or all of their possessions would be recorded as contracts in their OpenBazaar client. 

#### The Present and The Future

Fortunately, much of commerce is already moving to the Internet, and the process of recording information about possessions is moving from a manual task to one which could easily be automated. 

If you acquire an item via OpenBazaar, this could be done easily. Information about the contract purchased would simply change ownership to the new user. Using other major platforms could also be simple with importing tools, likely done via a browser plugin or something similar. Anything purchased via Amazon would automatically be represented as a contract. Apps using UPC scanners could automatically create contracts.

> This system would allow all possessions to have a continuous digital representation, and associated value, at no cost to the user.

What do you think? What other interesting use cases can you think of for a system like OpenBazaar? What would you like to see it do in the future? Tell us about it on [Reddit](https://reddit.com/r/openbazaar), in [Slack](https://openbazaar.org/slack), or on [Twitter](https://twitter.com/openbazaar)!

