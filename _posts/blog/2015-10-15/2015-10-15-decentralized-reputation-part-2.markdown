---
title: "Decentralized Reputation - Part 2" 
layout: post
date: '2015-10-15 00:30:00 -0300'
---
        


In [part 1](https://medium.com/@therealopenbazaar/decentralized-reputation-in-openbazaar-4e3a3d0b0899), we introduced the reputation system for OpenBazaar.

We learned that Vendor or Moderator reputation is composed of individual _transaction ratings_. Transaction ratings feed into a **reputation score**, with granular detail related to their activity as either a Vendor or Moderator. Transaction ratings are tied to a bitcoin transaction and recorded as a JSON-formatted _transaction summary_ of the trade.

[![Tx summary](Tx-summary.png)](Tx-summary.png)

_Transaction summaries_ contain the minimum amount of metadata required to provably link a Vendor to a bitcoin transaction and listing contract, while maintaining the privacy of the Buyer by default.

Users that desire to know the reputation of a Vendor can download the full history of _transaction summaries_ directly from the Vendor or a third party (e.g. Moderator).

Towards the end of the article, I hinted that third parties could take the _transaction summaries_ as ‘units of reputation data’ to calculate their own version of a reputation score, which would be different from OpenBazaar’s native algorithm.

In this article we will explore these concepts in greater detail, and unpack how _transaction summaries_ can be processed to add value to reputation score in OpenBazaar.

Cost of Identity
----------------

A frequent obstacle in any system where reputation is involved is the threat of _Sybil_ attacks.

> In a [Sybil attack](https://en.wikipedia.org/wiki/Sybil_attack) the attacker subverts the [reputation system](https://en.wikipedia.org/wiki/Reputation_system "Reputation system") of a [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer "Peer-to-peer") [network](https://en.wikipedia.org/wiki/Computer_network "Computer network") by creating a large number of [pseudonymous](https://en.wikipedia.org/wiki/Pseudonymity "Pseudonymity") identities, using them to gain a disproportionately large influence. A reputation system’s vulnerability to a Sybil attack depends on how cheaply identities can be generated, the degree to which the reputation system accepts inputs from entities that do not have a chain of trust linking them to a trusted entity, and whether the reputation system treats all entities identically. ([Source](https://en.wikipedia.org/wiki/Sybil_attack))

[Previously](https://medium.com/@therealopenbazaar/decentralized-reputation-in-openbazaar-4e3a3d0b0899) we described the first-line of defense against Sybil attack in OpenBazaar, which was the proof-of-work required to generate a global unique identifier (GUID) for the network. Using non-specialized hardware, generating a GUID will take approximately 30 seconds. However, given the prevalence of a specialized hardware related to various proof-of-work systems, we cannot exclusively depend on this approach to impose a cost per identity.

A _financial_ cost can be associated with an OpenBazaar GUID to help combat _Sybil_ attacks and enhance the value of a reputation score (when the GUID of the Buyer is disclosed in the _transaction summary_).

Like a proof of work, a _financial_ cost for a GUID means that contributing data to the network, in the form of ratings and reviews, is **not free**. This cost or **_reputation pledge_**, at some point, makes it economically irrational to create fake identities and thus fake ratings.

There are a variety of ways to make a **reputation pledge**:

1.  Proof of burn
2.  CHECKLOCKTIMEVERIFY
3.  Security deposit

We will briefly touch on each approach below with an example of a market price of $5 (~0.02 BTC at the time of writing) for a reputation pledge.

### Proof of Burn

Proof of burn involves sending bitcoin to an address where the private key will be virtually impossible to calculate. The funds sent to this address are permanently unspendable and represent the _purest_ form of commitment. Nevertheless, for many (including the author) there is an unsettling emotional cost, despite the net economic benefit it gives to all users.

For example, an attacking Vendor would need to burn $100 (0.4 BTC) to create 20 **reputation pledges** for each fake identity making a positive rating. However, the $100 burn only represents the _present cost_ to creating these identities. There is a future cost, in terms of deflationary value, in losing 0.4 BTC that may be worth significantly more than $100 months or years from now.

In terms of implementation, OpenBazaar may support this feature, but would be unsurprised if few use it in favor over other alternatives.

### CHECKLOCKTIMEVERIFY

[CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) would have a user send bitcoin to themselves (i.e. another address that the user controls) in such a way that these funds would be ‘unspendable’ until a future date. The funds in this type of transaction will not be accepted into a block until a specific Unix time or block height.

Unlike proof of burn, the $100 reputation pledge would not be permanently lost but temporarily inaccessible to a Vendor. The time period may be anywhere from weeks, months, or even years.

This approach isn’t particularly effective against attackers with a long time preference, but should be sufficient for most users when the value of items being traded are less than the locked funds.

### Security Deposit

A third party, or federation of third parties, hold a sum of funds from a user in multisignature escrow for a period of time as a _security deposit_. In the event of poor behavior by the user in a transaction or interaction, damages can be deducted from the security deposit to: 1) compensate the offended party, or 2) impose a punitive action.

The weakness of this approach is that the user must trust the third party, and the rest of the network must value the integrity of the third party. While certainly not ideal from a pure decentralist, zero-trust point of view, this service may emerge as a popular choice if reputable players enter this market.

### Counting the Cost

Irrespective of the approach used to make a reputation pledge, we can arrive at an estimate of the _total cost_ of a Sybil attack for the overall reputation score of a Vendor or Moderator. This is calculated by:

1.  Assuming all users that contributed to the reputation score are sockpuppets
2.  Summing the reputation pledges of each identity.

\[caption id="attachment_633" align="aligncenter" width="678"\][![Assuming each identity is secretly created by Alice, it would have cost her $100 in reputation pledges.](Reputation-Pledge-Calc.png)](Reputation-Pledge-Calc.png) Assuming each identity is secretly created by Alice, it would have cost her $100 in reputation pledges.\[/caption\]

The _Sybil cost_ represents the maximum amount Alice would have paid to create a 100% fake reputation score; the _actual_ cost may be lower if other users have legitimately rated her positively. Ancillary costs involved in a Sybil attack are not included in this estimate, only the **reputation pledge** values for each identity.

Users can have some assurance when dealing with a counterparty that has a _Sybil cost_ larger than the value to be traded. For example, if Fred wanted to sell a music track to Alice for $3, it is economically irrational for Alice to spend $100 to defraud Bob out of a $3 item. If the value of the item was $1000, then Bob would need to carefully consider his counterparty risk if Alice’s _Sybil cost _is only $100.

While seemingly complex, this economic reputation calculation exists in TaoBao, where Vendors put up security deposits in exchange for a badge to solicit trust from potential Buyers. The larger the security deposit, the more likely Buyers will feel safer transacting with the Vendor.

Transaction Summaries
---------------------

The aggregate history of _transaction summaries_ of a user is the data-set to calculate the **reputation score**. However, _transaction summaries_ can be excluded from the calculation based on certain criteria. The purpose of this is to enhance the value of a reputation score to more accurately predict the integrity of a user in future trades.

### The 3 Seashells

One approach is to break up the reputation score, of the Vendor or Moderator, into 3 classes or the ‘3 seashells’.

\[caption id="attachment_634" align="aligncenter" width="648"\][![The 3 Seashells… yes I’m a fan of Demolition Man](3-Seashells.jpg)](3-Seashells.jpg) The 3 Seashells… yes I’m a fan of Demolition Man\[/caption\]

#### **Seashell 1: All (red; low reliability)**

The reputation score is calculated from **all _transaction summaries_** that can be found on the network for a Vendor or Moderator. The GUID of the Buyer does not need to be disclosed. Equal weight is assigned to all _transaction summaries_ on the assumption they are all from authentic trades_._

\[caption id="attachment_635" align="aligncenter" width="648"\][![All transaction summaries are counted, even if the Buyer’s GUID isn’t not disclosed.](Red-Seashell.png)](Red-Seashell.png) All transaction summaries are counted, even if the Buyer’s GUID isn’t not disclosed.\[/caption\]

If Buyer’s GUID is undisclosed, they are represented by the Bitcoin address (and signature) from the payout transaction from multisignature escrow address or input address in a direct transaction.

#### **Seashell 2: Public (yellow: some reliability)**

The reputation score is calculated from _transaction summaries_ where the **GUID of the Buyer is disclosed**. Any _transaction summaries_ where the Buyer is **only** represented by a Bitcoin address (i.e. an anonymous transaction) are discarded.

\[caption id="attachment_636" align="aligncenter" width="648"\][![Transaction summaries without the Buyer GUID disclosed are discarded.](Yellow-Seashell.png)](Yellow-Seashell.png) Transaction summaries without the Buyer GUID disclosed are discarded.\[/caption\]

The assumption here is that the requirement of the Buyer’s GUID subjects the rating to:

1.  A minimum proof-of-work to create an OpenBazaar identity
2.  Transparency on the network
3.  An association of a GUID with a bitcoin transaction; coin analysis can be performed

#### **Seashell 3: Web-of-Trust (green: excellent reliability)**

The reputation score is calculated from _transaction summaries_ where the**Buyer’s GUID is within the user’s web-of-trust** **graph** (WoT).

\[caption id="attachment_637" align="aligncenter" width="648"\][![If Alice is the target and Ed is the observer, only the transaction summaries in Ed’s web-of-trust are accepted when calculating Alice’s reputation score.](Green-Seashell.png)](Green-Seashell.png) If Alice is the target and Ed is the observer, only the transaction summaries in Ed’s web-of-trust are accepted when calculating Alice’s reputation score.\[/caption\]

The assumption here is that you are more likely to believe ratings made by people you trust compared to pseudonymous or random identities on the network.

### Web-of-Trust

There are several WoT architectures to choose from. In OpenBazaar, the WoT can be as simple as a graph of nodes that the user follows. Alternatively, there are more complex proposals that we will briefly touch on below.

#### **_Web-of-trust #1:_** _Zindros_

\[caption id="attachment_638" align="aligncenter" width="648"\][![Zindros web-of-trust](Dio-WoT.jpg)](Dio-WoT.jpg) Zindros web-of-trust\[/caption\]

This approach was named after OpenBazaar core contributor [Dionysis Zindros](https://twitter.com/dionyziz), who wrote up a comprehensive specification [outlined here](https://gist.github.com/dionyziz/e3b296861175e0ebea4b).

The _Zindros_ WoT uses proof-of-burn to introduce a cost to create an identity. Only partial knowledge of the whole web-of-trust graph is known by any one user.

To calculate the reputation score of a target node Bob (in context of transaction summaries used in OpenBazaar), Alice queries her friends (i.e. nodes within her WoT) to return:

1.  _Transaction summaries_ of Bob
2.  _Transaction summaries_ of Bob that their friends and friends-of-friends (up to _n_ degrees of freedom) may have

The overall **reputation score** would be calculated based transaction ratings _weighted_ based on the proximity of the target (Bob) to Alice’s friends in her WoT.

#### **_Web-of-trust #2:_** _Line of Credit_

This designs differs from traditional web-of-trust designs in that is uses a Bitcoin _line of credit_ as the trust edges (i.e. the connections between nodes) rather than _esoteric_ ratings, vouches, or points. If a user on the network has large and multiple lines of credit from other nodes, then this would be a quantifiable _financial_ indicator of trust.

The line-of-credit (LoC) may either be a 1-of-2 (high liquidity, high trust) **or **2-of-2 (low liquidity, low trust) escrow address where funds are deposited between two nodes. If Alice is added to Bob’s WoT, Bob would deposit bitcoin in a 1-of-2 escrow address that Alice can draw from at any time for any purpose.

\[caption id="attachment_639" align="aligncenter" width="777"\][![Trust is measured by the total amount of credit a user can draw from other users on the network.](LoC-WoT.png)](LoC-WoT.png) Trust is measured by the total amount of credit a user can draw from other users on the network.\[/caption\]

The OpenBazaar application would keep track of funds borrowed, interest levels, repayment schedules etc, which would contribute to more public metadata to assess the _trustworthiness_ of a user_._ Users are incentivized to open a _line of credit_ to a reputable Vendor, who is likely to earn them interest.

One advantage of this approach is that it simultaneously requires a cost for each identity to establish trust, creating a financial disincentive for _Sybil _attacks.

Some variations of this idea may be extended to bi-directional micropayment channels to be used in the [lightning network](https://lightning.network/).

### Filters

In addition to the three major classes above, _transaction summaries_ can be filtered according various parameters to calculate the reputation score.

#### **Blockchain ID**

Only _transaction summaries_ with a disclosed GUID **and** a Blockchain ID are included in the reputation score calculation. Furthermore, transaction ratings may be weighted based on the number of external verified accounts associated with a Blockchain ID (i.e. Facebook, Twitter, PGP etc). This approach would attempt to favor transaction ratings from verifiable real world identities rather than anonymous or purely pseudonymous users.

#### **Coin Analysis**

Each _transaction summary_ is tied to bitcoin transaction where funds are released to the Vendor as a result of a successful OpenBazaar trade. This transaction can be analysed in conjunction with other transactions associated with the user to assess the likelihood the same coins were used for both transactions.

If the same coins were used, then there is a high chance that the user is attempting to fake a rating, and the associated _transaction summary_ with the rating data can be discarded from calculating the reputation score (in addition to any punitive measures).

This filter may become less effective as tools such as JoinMarket and confidential transactions are deployed.

Reputation Score Algorithm
--------------------------

Irrespective of what pool of _transaction summaries_ will be sampled for ratings, users or items will need to be sorted from _most reputable_ to _least reputable_. The reputation score can be a contentious issue, but there are several factors to consider when selecting a reputation score algorithm. These factors are reviewed in this [excellent article](http://www.evanmiller.org/how-not-to-sort-by-average-rating.html), and a slightly easier to understand version [here](http://alecb.me/blog/how-to-sort-ratings/).

In short, OpenBazaar will use the **lower bound of the Wilson score** confidence interval, for a Bernoulli parameter, calculate the _reputation score_ of a user. Incidentally, Reddit also [uses this approach](http://amix.dk/blog/post/19588) to rank stories.

Third party services can collect _transaction summaries_, filter, and experiment with alternative algorithms to calculate the **reputation score** of a user.

Conclusion
----------

_Transaction summaries_ are units of reputation data in OpenBazaar. This data can be parsed in a variety of ways to either enhance the reputation score or form an alternative reputation score that is more relevant to a subset of users. Thus, OpenBazaar is a platform for developing decentralized reputation systems as well as for marketplaces.

While most of these ideas will not be implemented in time for our upcoming release, they may serve as a foundation/inspiration for new contributors and/or third party developers to build on the reputation platform.

Acknowledgements
----------------

*   [Dionysis Zindros](https://twitter.com/dionyziz)
*   [Austin Williams](https://twitter.com/onewayfunction)
*   [Chris Pacia](https://twitter.com/ChrisPacia)
*   [Dr David Strayhorn](https://www.linkedin.com/pub/david-strayhorn/2/7a9/52)
*   [Ian Grigg](https://twitter.com/iang_fc)
*   [Chrisopher Allen](https://twitter.com/ChristopherA)
*   [Dr Bulukani Mlalazi](https://twitter.com/drBuluM)

