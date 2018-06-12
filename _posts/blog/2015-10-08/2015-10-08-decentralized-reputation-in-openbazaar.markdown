---
title: "Decentralized Reputation in OpenBazaar" 
layout: post
date: '2015-10-08 00:30:00 -0300'
---
        
 **Decentralized reputation** is one of the most sought after prizes in the cypherpunk community: to invent a censorship-resistant protocol to make and parse unforgeable trust relationships between pseudonymous identities. The problem is that _trust_ and _reputation_ are both abstract concepts that aggregate the subjective value judgements of unrelated experiences between people. Fundamentally, trust and reputation are highly contextual, and merely attributing a number or karma points to ascertain the overall trustworthiness of an identity is [not very informative](http://www.lifewithalacrity.com/2005/12/collective_choi.html) or useful. OpenBazaar's reputation system is **granular** and **contextual** to trade that takes place within the network.

*   _Granular_ in that ratings are made according to multiple criteria evaluating different components of an e-commerce transaction
*   _Contextual_ in that ratings are made on a per-transaction basis, rather than _goodwill points_

The reputation of a user is the weighted-average of their transaction ratings. In summary, you cannot make a rating without showing evidence of a transaction over OpenBazaar. While [we earlier explored the web of trust (WoT) model](https://gist.github.com/dionyziz/e3b296861175e0ebea4b), the system described in this article is **not** a _web of trust_. OpenBazaar's reputation system is similar to eBay and Taobao in that it is _transaction-based._ Where necessary, we have made some improvements that are described below. To get a sense of how the reputation system works, we must examine the following components in the OpenBazaar protocol:

1.  Identity
2.  Ricardian Contracts and the Trade Flow
3.  Ratings and Reviews
4.  Reputation Score

This article is adapted from [slides we published earlier](http://www.slideshare.net/drwasho/openbazaar-ratings-reviews-and-reputation?from_m_app=android).  

Identity
========

Any reputation system begins with a network of _identities_. In OpenBazaar, these identities are _pseudonymous_, which is to say that they are not inherently tied to your real world identity. The OpenBazaar network uses a Kademlia-style distributed hash table (DHT) to connect peers, similar to BitTorrent. Public key cryptography is used to generate a global unique identifier (GUID), which represents a pseudonymous node on the network. The GUID is a _key_ that multiple _values_ can be attributed to (e.g. an IP address and port). The _key_ remains immutable (unchangeable) while the _value_ is mutable (changeable). For example, Alice's GUID on the OpenBazaar network remains constant even though her IP address/port changes depending on whether she connects to the network from home or work.

**1 GUID = 1 node on OpenBazaar**

In OpenBazaar, a large random number (2^256) is initially generated, which is the private key of the GUID keypair. A corresponding public key is generated from the private key. The GUID is generated using a _proof-of-work_ scheme to introduce computational difficulty in generating identities, to mitigate against a variety of sock-puppet attacks. With the target difficulty, GUID generation should take approximately 30 seconds. `GUID = first 20 bytes of SHA256(self-signed public key), where the last 32 bytes < a difficulty target`

OpenBazaar uses Ed25519 for digital signatures.

The GUID keys are used for:

1.  Authenticating network messages between peers
    *   GUID keys used for initial authentication
    *   Ephemeral key pair generated to encrypt subsequent messages between peers for _forward secrecy_
2.  Digitally signing Ricardian contracts
    *   Digital agreements on the subject and terms of trade
3.  Generate a hierarchical deterministic (HD) keychain for multisignature transactions
    1.  HD master private key = SHA256(GUID private key)

 

**The GUID is the network identity of OpenBazaar**
--------------------------------------------------

The GUID is long, complex, and prohibitively difficult for people to remember. Fortunately, we have added option support for Onename's Blockchain ID to register an OpenBazaar GUID to a memorable handle (e.g. @drwasho). A Blockchain ID can also be associated with other real world and digital identities such as Facebook, Twitter, Github, or your PGP keys. This allows users to leverage their real world identities to build initial trust connections for trade. Alternatively, a user can not associate any real world identity with their Blockchain ID to preserve a purely pseudonymous identity. If a user registers their OpenBazaar GUID to a Blockchain ID handle, you will be able to search for that identity by that handle in the application. Future features include 'sub-domain' namespaces that can link to the same root identity, but map to different OpenBazaar GUIDs. Similarly, a user can acquire multiple handles that map to the same OpenBazaar GUID. ![](https://i.imgur.com/KkWwO32.jpg) As an OpenBazaar identity is based on the generation of a cryptographic keypair, rather than divulging personally identifiable information, the user ultimately retains control over their privacy and can choose the level of association with their real world identity. Upon this foundation of identity we can begin to construct reputation based on transaction ratings.  

Ricardian Contracts & the Trade Flow
====================================

**[Ricardian contracts](http://iang.org/papers/ricardian_contract.html)** are simply _digital documents_ that define the terms and conditions of an interaction, between two or more peers, which is cryptographically signed and verified. It is a tamper-proof contract that is formatted in XML or **JSON** and designed to be both human and machine readable. Ricardian contract have the following components:

1.  **Cryptographic keys** to establish _identity_
2.  **Semantic data** to establish the terms and conditions of an interaction (e.g. money exchanged for a good/service)
3.  **Digital signatures** to create fraud-proof evidence that an identity agreed to these terms and conditions
4.  **Cryptographic hash** of the contract, as a reference identifier, to create a tamper-proof record of the contract

OpenBazaar extends the utility of the Ricardian contract, originally designed by the eminent [Ian Grigg](https://twitter.com/iang_fc), to act as a ledger of the transaction or _trade flow_ between the contracting parties. The final version of the Ricardian contract, with a completed and digitally signed record of the execution of the contract, is called a _trade receipt_. The data within the contract is signed with the GUID keys of the participants. _OpenBazaar's Ricardian contract schema for physical items_: [![](http://i.imgur.com/Pm7PrNA.jpg)](http://i.imgur.com/Pm7PrNA.jpg)     The contract itself is broken up into the 4 stages of the **trade flow**: **Stage 1: Listing/Vendor Offer**

*   The Vendor lists what is for sale (physical item, digital content, services etc)
*   There are some prior steps regarding Moderator selection that won't be elaborated on in this article

**Stage 2: Buyer Order**

*   The Buyer sends an order to the Vendor
*   The Vendor acknowledges the order, sending a digital signature that will serve as a Vendor authentication of the order (prevents attackers from making fake ratings of the Vendor)
*   Buyer funds the multisignature escrow address
*   Order processing time begins: ~1-3 days to ship the item

**Stage 3: Vendor Order Confirmation**

*   The Vendor confirms to the Buyer that the order has been processed and the item has been shipped
*   Gives the Buyer any shipping related data, for physical goods
*   Gives the Buyer a download address and password, for digital content
*   Gives the Buyer any relevant data to perform the service
*   Sends partially signed transaction releasing funds from the multisignature escrow address to the Vendor (still requires Buyer to sign after receiving the item)

**Stage 4: Buyer Receipt**

*   Buyer acknowledges that the item, content, or service was delivered/performed
*   Signs a transaction releasing funds from multisignature escrow
*   Makes a rating and review of the Vendor, sends the _transaction summary_ to the Vendor and Moderator for storage

There is more detail to each of these stages, but for the purpose of this article we'll move on.  

Ratings and Reviews
===================

Initially, OpenBazaar will support ratings for Vendors (including the product/service they sell) and Moderators, who play a crucial role in the trust infrastructure of the network.

We expect that in the early days of OpenBazaar’s release, Moderators will need to leverage their external reputation to gain trust from users on the network. This represents a unique opportunity for groups such as [BitRated](https://www.bitrated.com/) to extend their services into a decentralized markeplace.

Rating a Vendor
---------------

As mentioned earlier, the rating model for Vendors is comparable to eBay and TaoBao, and thus leverages the user experience most e-commerce users are familiar with.

Vendors will be rated in 5 categories:

1.  _Feedback_ rating
2.  Item/content/service _quality_
3.  Item/content/service listing _description_
4.  Item/content/service delivery
5.  Customer service

Each rating criteria will be rated out of 5 stars.

Unlike eBay and TaoBao though, the meaning of these stars are not left open to _subjective interpretation_, but reflect an objective assessment criteria in order to more accurately standardize Buyer ratings.

In addition to these ratings, the Buyer can also write a text review of the transaction.

#### Feedback Rating

What was the overall feedback when purchasing the product from the Vendor?

*   **5 stars** = I would do business with them again without hesitation.
*   **4 stars** = I will probably to do business with them again.
*   **3 stars** = I would only do business with them if I couldn’t find anyone else.
*   **2 stars** = I will not do business with them again.
*   **1 star** = This is a scam, avoid at all costs.

#### Item/Content/Service Quality

What was the quality of the item, content, or service from the vendor?

*   **5 stars** = I would purchase it again and recommend it to others without hesitation.
*   **4 stars** = I might purchase it again and recommend it, but I’d still look for alternatives first.
*   **3 stars** = I would only purchase and recommend it if I couldn’t find anything else like it first.
*   **2 stars** = I wouldn’t purchase it again or recommend it.
*   **1 star** = It is a scam, avoid this product.

#### Item/Content/Service Listing Description

How accurate was the listing description of the item, content or service?

*   **5 stars** = Perfectly accurate.
*   **4 stars** = Mostly accurate.
*   **3 stars** = Barely acceptable.
*   **2 stars** = Mostly inaccurate.
*   **1 star** = 100% false.

#### Item/Content/Service Delivery

How quickly was the item sent, content accessible, or service performed after ordering?

*   **5 stars** = Delivered earlier than the estimated delivery date.
*   **4 stars** = Delivered by the estimated delivery date.
*   **3 stars** = Delivered <5 days later after the estimated delivery date.
*   **2 stars** = Delivered >5 days after the estimated delivery date.
*   **1 star** = Never delivered.

#### Customer Service

How do you rate the quality of the Vendor’s communication?

*   **5 stars** = The Vendor kept in contact with me at every stage of the trade. The Vendor answered my questions, clearly and concisely, <12 hours after I asked.
*   **4 stars** = The Vendor only contacted me if there was a problem. The Vendor answered my questions, with some clarity, <24 hours after I asked.
*   **3 stars** = The Vendor only contacted me after I reached out to them. The Vendor answered some questions, with passable clarity, >24 hours after I asked.
*   **2 stars** = The Vendor rarely responded. The Vendor was not clear or understandable.
*   **1 star** = The Vendor never communicated.

#### Text Review

Similar to eBay, written reviews have a size limit of 80 characters.

### Making a Rating

Ratings are made in the last stage of the trade flow (see above; Stage 4 Buyer Receipt). When a user receives an item, they need to confirm that the item was received in order to release funds from escrow to the Vendor. During that process, they will be asked to make a rating and write a text review as described above.

While the data is stored within the _trade receipt_, it isn’t efficient (and doesn’t scale) to download a Vendor’s entire trade receipt history just to extract the rating and review data for that user (or for an item they sell).

Instead of a trade receipt, Vendors will serve _transaction summaries_ that contain the relevant data to validate a transaction and calculate the reputation score.

The schema of a transaction summary is:

    {

One of the most important elements of the _transaction summary_ is the vendor’s signature of the **transaction object**, which contains the listing hash, bitcoin address, price etc. When the Buyer places the initial order with the Vendor, the Vendor’s client will send a digital signature of the **transaction object**. This will be a cryptographic proof of the Vendor’s involvement in the trade, which is necessary before any rating is made — otherwise a Vendor could refuse to attribute themselves to a _transaction summary_ with a negative rating.

The rest of data such as transaction ID (txid), the trade receipt hash, the rating and review text is added at the conclusion of the transaction and sent to the Vendor for their records. The _transaction summary_ can also be sent to the Moderator for storage, in case the Vendor omits summaries with negative ratings.

Overall, the transaction summary is a more compact proof of the Vendor and Buyer’s exchange and subsequent rating than the entire _trade receipt_. Future releases will address the issue of long term storage of transaction summaries and Vendor transparency, potentially with technologies such as Blockstore and/or [IPFS](https://ipfs.io).

Rating a Moderator
------------------

Rating a Moderator for their service is significantly more complex task. To our knowledge, it is entirely without precedent. Users should expect this area of reputation to evolve as we learn what transpires over the network in the years to come. Below we describe a system we feel comfortable launching and learning from.

The task of Moderation is to pick a winning and losing side from a dispute between two parties (the Vendor and Buyer). Unfortunately, the rating of a Moderator will be heavily biased depending on whether the user has won or lost the dispute.

In other words, if the Moderator decides that you are the winner in a dispute, you are more likely to rate the Moderator positively for their ‘wise and noble decision’. The opposite is true if you are on the losing side.

As a result, OpenBazaar must show the rating/review — for each disputed transaction — from both sides. The goal is to highlight any potential agreement between the winner/loser in the _rating criteria_.

Moderators will be rated in 4 categories:

1.  Feedback Rating
2.  Dispute Resolution Listing _D__escription_
3.  Resolution Time
4.  Customer Service

As with Vendors, each rating criteria will be rated out of 5 stars. Each star has an objective meaning that will be displayed to the user. Users can also submit a text review of the Moderator.

#### Feedback Rating

What was the overall feedback to the Moderator?

*   **5 stars** = I would choose them again without hesitation.
*   **4 stars** = I will probably do business with them again.
*   **3 stars** = I would only do business with them if I couldn’t find anyone **​**better.
*   **2 stars** = I will not do business with them again.
*   **1 star** = This is a scam, avoid at all costs.

#### Dispute resolution listing description

How accurate was the Moderator's dispute resolution description service?

*   **5 stars** = Perfectly.
*   **4 stars** = Mostly accurate.
*   **3 stars** = Barely acceptable.
*   **2 stars** = Mostly inaccurate.
*   **1 star** = 100% false.

#### Dispute resolution time

How quickly was the dispute resolved by the Moderator?

*   **5 stars** = Resolved earlier than the estimated time.
*   **4 stars** = Resolved earlier the estimated time.
*   **3 stars** = Resolved <5 days later after the estimated time.
*   **2 stars** = Delivered >5 days after the estimated time.
*   **1 star** = Never delivered.

#### Customer Service

How do you rate the quality of the Moderator’s communication?

*   **5 stars** = The Moderator kept in contact with me and answered my questions, clearly and concisely, <12 hours after I asked.
*   **4 stars** = The Moderator only contacted me if they had a specific question/resquest from me. The Moderator answered my questions, with some clarity, <24 hours after I asked.
*   **3 stars** = The Moderator only contacted me after I reached out to them. The Vendor answered some questions, with passable clarity, >24 hours after I asked.
*   **2 stars** = The Moderator rarely responded. The Moderator was not clear or understandable.
*   **1 star** = The Vendor never communicated.

#### Text Review

Written reviews have a size limit of 80 characters.

### Making a Rating

Broadly speaking, there are 2 classes of dispute that may arise:

1.  The Buyer failing to release funds from escrow
2.  The Buyer being unsatisfied with the contents or delivery of the item

#### **Dispute:** The Buyer failing to release funds from escrow

This scenario will be due to the Buyer being incapacitated or forgetting to release funds. If the Buyer fails to respond after a reasonable number of attempts over time, the Moderator will collaborate with the Vendor to release the funds.

This process is initiated by the Vendor, who flags a dispute to the Moderator and Buyer (if online). To flag the dispute, the Vendor sends the _dispute claim_ (with a digital signature) to the Moderator and Buyer:

1.  The hash of the **transaction object**
2.  Who the claimant is (i.e. the Vendor in this example)
3.  The written claim (80 characters long)

If the Buyer fails to respond to the Moderator, the Moderator will issue their _resolution_. The _resolution_, digitally signed by the Moderator, will include:

1.  The hash of the _dispute claim_
2.  The written resolution outcome and justification (character length to be decided)

The resolution is then sent to both the Vendor and Buyer (if online) and a transaction releasing the funds from escrow to the Vendor is created and signed.

A _transaction summary_ is automatically generated at the end of this process, as described earlier, that also includes the _dispute claim_, the _resolution_, and the Moderator review.

Both the Vendor and Moderator will host and serve this transaction summary to other users.

_Vendor transaction summary_

    {

#### Dispute: The Buyer being unsatisfied with the contents or delivery of the item

This dispute will arise if the Buyer claims that the item was not delivered or if the item delivered was incorrect, damaged, or significantly different from the product description. Whatever the circumstance, the Buyer will be attempting to obtain a full refund.

Typically, the Buyer will be the one to initiate a dispute and submit a _dispute claim_ to the Moderator and Buyer. After this step, most of the dispute resolution process will transpire over the internal messaging channel we have built into OpenBazaar, which is encrypted with the participants’ public keys.

After the Moderator has come to a decision to who the winning party is, they will issue a _resolution_ as described above.

When the funds are finally released from escrow to the winning party, both the Buyer and Vendor can generate a _transaction summary_. Here they will both have an opportunity to rate the Moderator on the dispute resolution. The Buyer’s _transaction summary_ will also have the rating/review of the Vendor, which may not be counted in the final reputation score of the Vendor if the Buyer lost the dispute.

The Moderator will host the _transaction summaries_ from both parties, which will be available for users to inspect.

_Buyer transaction summary_

{
  "tx_summary" : {
      "vendor" : {
        "guid" : "",
        "pubkey" : ""
      },
      "transaction" : {
        "listing" : "",
        "bitcoin_address" : "",
        "price" : "",
        "buyer_pubkey" : "",
        "moderator_guid" : "",
        "moderator_pubkey" : ""
      },
      "vendor\_tx\_signature" : "",
      "txid" : "",
      "trade\_receipt\_hash160" : "",
      "dispute" : {
        "transaction_hash160" : "",
        "claimant" : "",
        "claim" : ""
      },
      "claimant_signature" : "",
      "moderator_resolution" : {
        "dispute_hash160" : "",
        "summary" : ""
      },
      "moderator_signature" : "",
      "vendor_rating" : {
        "feedback": 0,
        "quality" : 0,
        "description" : 0,
        "delivery_time" : 0,
        "customer_service" : 0,
        "review" : ""
      },
      "moderator_rating" : {
        "feedback" : 0,
        "description" : 0,
        "time" : 0,
        "customer_service" : 0,
        "review" : ""
      }
  },
  "buyer_signature" : ""
}

_Vendor transaction summary_

{
  "tx_summary" : {
      "vendor" : {
        "guid" : "",
        "pubkey" : ""
      },
      "transaction" : {
        "listing" : "",
        "bitcoin_address" : "",
        "price" : "",
        "buyer_pubkey" : "",
        "moderator_guid" : "",
        "moderator_pubkey" : ""
      },
      "vendor\_tx\_signature" : "",
      "txid" : "",
      "trade\_receipt\_hash160" : "",
      "dispute" : {
        "transaction_hash160" : "",
        "claimant" : "",
        "claim" : ""
      },
      "claimant_signature" : "",
      "moderator_resolution" : {
        "dispute_hash160" : "",
        "summary" : ""
      },
      "moderator_signature" : "",
      "moderator_rating" : {
        "feedback" : 0,
        "description" : 0,
        "time" : 0,
        "customer_service" : 0,
        "review" : ""
      }
  },
  "vendor_signature" : ""
}

Reputation Score
================

The reputation score of a Vendor is the average **feedback rating** from all of their transactions. A user can expand the reputation score to see a Vendor’s average ratings for item quality, listing description, delivery time, and customer service.

[![Vendor Reputation Score](Vendor-Reputation-Score.png)](Vendor-Reputation-Score.png)

The reputation scores of a Moderator are the average **feedback ratings** from the winning and losing sides of disputed transactions. As with the Vendors, the average ratings for each criteria can be expanded from both sides.

[![Moderation Reputation Score](Moderation-Reputation-Score.png)](Moderation-Reputation-Score.png)

Challenges
==========

To put it plainly, no reputation system is resistant to a Vendor purchasing their own items and making false-positive ratings.

This is especially true of a pseudonymous decentralized marketplace, where Buyer identities are - by default - undisclosed. Even a web-of-trust model, which is excellent at detecting suspicious _islands_ of 'reputable' users, will not be able to distinguish between real and fake ratings of a Vendor. Why? As discussed, Buyer identities are not disclosed in the _transaction summaries_ (unlike trade receipts, which is necessary for dispute resolution); Buyers are only represented by a bitcoin address. This is the equivalent of a single-use pseudonymous identity that would be the cause of suspicion in a web-of-trust model. As the GUID is directly mapped to the IP address (DHT), disclosing the GUID may compromise the real world privacy and security of the Buyer (as well as their spending habits).

![](http://i.imgur.com/L6LbifI.jpg)

That said, a web-of-trust graph based off _transaction summaries _where the Buyer **is known** (i.e. the GUID and Blockchain ID is _voluntarily_ disclosed) would be a useful tool.

As transaction ratings in OpenBazaar must be tied to a bitcoin transaction, there is a cost - albeit a small one - to making a rating. Furthermore, the _bitcoin transaction graph_ may emerge as a useful filter to assess/score the legitimacy of a transaction rating. For example, if an attacking Vendor uses the same coins to make 100 transactions in order to create 100 _transaction ratings_, this can be easily spotted with little analytical sophistication. There are many opportunities for third parties to build entire services on assessing the reputation of a Vendor.

The Future
==========

A reputation system within OpenBazaar may facilitate the emergence of new types of markets to be supported on the network. The reputation of a Vendor may be used to assess the risk associated with that identity for loans or insurance policies issued over OpenBazaar. This is an fascinating subject that we’ll be exploring in future articles.

Going forward, past the initial release, will be the development of:

1.  **Asynchronous ordering and network message caching** Needs to be compatible with the rating system
2.  **Rating system for Buyers?** Is there any value in implementing a rating system for Buyers, or would this lead to a negative rating Mexican standoff?

 

Final Thoughts
==============

OpenBazaar doesn’t claim to create or try to create a global decentralized reputation system for **everything**. What we have designed is a highly contextual rating system, similar to the standard e-commerce experience (with some improvements in our view), which will establish Vendor and Moderator reputations. The latter is really breaking new ground, which will undoubtedly be the subject of revision after seeing it run in the wild.

Finally, the transaction rating data can be parsed by third party developers to analyse and calculate the reputation scores according to the other approaches such as the Bayesian average. A high priority for future releases will be the long-term distributed _free_ storage of transaction summaries.

