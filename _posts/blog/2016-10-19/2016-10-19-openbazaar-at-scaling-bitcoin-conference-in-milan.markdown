---
title: "OpenBazaar at Scaling Bitcoin Conference in Milan" 
layout: post
date: '2016-10-19 00:30:00 -0300'
---
        
###### by Chris Pacia

[![Chris Milan 6](Chris-Milan-6.jpg)](Chris-Milan-6.jpg)   This month I had the opportunity to attend the third [Scaling Bitcoin conference in Milan](https://scalingbitcoin.org/event/milan2016). My purpose for going was to stay on top of the latest developments in Bitcoin and keep an eye out for collaboration opportunities for [OpenBazaar](http://openbazaar.org) and [OB1](http://ob1.io) related projects. Now that I’m back, I can give a review of sorts and talk about some of the cool ideas that were proposed and discussed. Firstly, the Scaling Bitcoin conferences seems to be evolving away from being exclusively about scaling and to a more general technical conference where bleeding edge ideas are presented. There were still a good number of presentations that were scaling-related, of course, but also a good mix of other ideas to improve Bitcoin. All of the presentations were of high quality, but I’ll comment on a few standouts.

MimbleWimble
------------

The darling of the conference in my opinion, [mimblewimble](https://scalingbitcoin.org/transcript/milan2016/mimblewimble), was dropped on the internet by an anonymous mailing list poster as picked up by Andrew Poelstra and others. The basic idea is to use the same technology behind confidential transactions to turn blocks into a sort of big coinjoin transaction. Blockchain sleuths would not be able to use the transaction history to figure out who paid whom the way they can do today. A side benefit of this format is that much of the data in the blocks can be dropped allowing the blockchain to be compressed to a very small size. Possibly one downside is that transactions still need to be broadcasted to each node, meaning there is still an opportunity for active attackers to record all transactions and link transactions together. This attack could possibly be foiled by grouping transaction together before broadcasting. Most attendees I talked to about mimblewimble were very hot on it, but were holding back their enthusiasm until it could be demonstrated that it could scale (for example if they can make the lightning network work on it).

TumbleBit
---------

I spent a good deal of time talking to Ethan Heilman who presented [TumbleBit](Chris-Milan-3.jpg) ― an anonymous coin mixer/payment hub. Whereas previous tumblers required users to trust the person running the tumbler to not keep logs which could de-anonymize users, TumbleBit makes that impossible through the clever use of cryptography. In addition to unlinkability, payments made through the tumbler would largely happen off chain. Over the years there has been some talk about building these type mixing protocol directly into wallets to encourage their use, improving fungibility and increasing the anonymity set, but we’ve seen little movement in that regard. Maybe going forward there will be an opportunity to collaborate and get TumbleBit--or something like it--into OpenBazaar. Ethan also offered to take a look at the OpenBazaar protocol to see if he can find ways to break it which, of course, would be great to have more eyes and more people with technical expertise reviewing it. It will only make the protocol stronger.   [![Chris Milan 3](https://blog.openbazaar.org/wp-content/uploads/2016/10/Chris-Milan-3.jpg)](https://blog.openbazaar.org/wp-content/uploads/2016/10/Chris-Milan-3.jpg)  

Notable Mentions
----------------

**In the interest of time I’ll just offer a few more highlights:**

*   I found **Peter Todd’s** talk about [having miners skip validation](https://scalingbitcoin.org/transcript/milan2016/client-side-validation) and just focus on ordering, while requiring nodes to do their own validation to be an interesting rethinking of how consensus is achieved.
*   **Emin Gun Sirer’s** presentation on [Bitcoin covenants](https://scalingbitcoin.org/transcript/milan2016/covenants) was cool. People I spoke to about it liked the concept of covenants and suggested some ways of extending them further with Merkelized Abstract Syntax Trees.
*   Side note: It was nice to seem movement on bip 150/151. I’ve been waiting for this for a long time.
*   I also had a short chat with Pierre who recently published a simulation of the FLARE routing for the lightning network. I talked to him about a routing simulator I wrote recently (which I didn’t publish since it was just a hack job to give me a rough idea of how well it would work). I think we both kind of agreed that there is still more work needed to optimizing routing and give us the greatest probability of finding routes from any one random node to another random node for a range of values. The routing needs to be very reliable for lightning to become widely used, in my opinion.
*   I had a really interesting chat with **Mark Friedenbach** from [Blockstream](https://blockstream.com/) about some of the advanced things they are working on. I won’t publish what they are as I don’t think they have made them public yet and I’ll let them talk about it when they’re ready, but they are super cool and at least one of the projects is something I’ve been wanting to work on myself and would probably be working on if I wasn’t working on OpenBazaar.
*   I spoke with **Joseph** and **Laolu** ([Lightning Network](https://lightning.network/)) about collaborating on an SPV wallet implementation in Go. Tadge Dryja wrote a small (and incomplete) SPV library for their lightning network project which I forked and have done some work on to beef it up. There is still a good way to go though and I’m hoping we have the opportunity to work together to get a solid implementation for both of us to use.
*   I didn’t get to attend **Roger Ver’s** free speech party and was disappointed that it was held at the same time as the main reception. Both parties ended up smaller than they would have been and it reduced the opportunities to network. If it was scheduled as an after party, or better yet a party on Sunday night, I’m willing to bet most conference attendees would have gone. There were lots of people looking for a party on Sunday night but there wasn’t one scheduled! Maybe a missed opportunity.

So all around the conference was very productive and it was good opportunity to make connections and stay on top of the latest developments. Assuming future Scaling Bitcoin conferences follow the same format I will be looking to attend them as well.