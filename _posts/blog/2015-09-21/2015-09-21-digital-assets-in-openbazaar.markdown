---
title: "Digital Assets in OpenBazaar" 
layout: post
date: '2015-09-21 00:30:00 -0300'
---
        
**Digital assets** are obligations to real-world items, content, or services that are digitally recorded. Digital assets are issued by individuals or corporations, and the bearers of the assets are entitled to the obligation promised by the issuer. In simple terms, they are the digital equivalent of a poker chip in a casino, redeemable for cash at the end of a game. To make digital assets immutable and unforgeable, they are issued and transferred over Bitcoin's blockchain as transactional metadata and is associated with a unique Bitcoin address. Using public key encryption, only the private key associated with that address can be used to authenticate and receive a digital asset obligation. Digital assets can be used in a number of different ways. Here are three concrete examples:

1.  Gold certificates
    *   The bearer can redeem physical ounces of gold from a depository institution after proving ownership of the address through a digital signature
2.  Keys
    *   A electronically-activated lock can be triggered on/off only with the digital signature from the private key of the digital asset bearer
    *   After selling the car, the digital asset is transferred to the new owner's address; the lock will now exclusively respond to the new owner
3.  Coupons and Gift Certificates
    *   The bearer can digitally sign a message to claim a shopping discount or gift certificate issued by a Vendor

The applications of digital assets are limited by a combination of tools and creativity. Over the past several years, the tools and protocols to create and transfer digital assets have matured. Presently there are three major digital asset protocols (not counting metacoin/altcoin-based protocols):

1.  [Open Assets](https://github.com/OpenAssets)
2.  [CoinSpark ](http://coinspark.org/)
3.  [Colored coins ](http://coloredcoins.org/)

\[caption id="attachment_578" align="aligncenter" width="648"\][![DAP Transaction Share](DAP-Transaction-Share.jpg)](DAP-Transaction-Share.jpg) Transaction share covers the past week\[/caption\] These protocols generally share the same approach: \[caption id="" align="aligncenter" width="646"\]![](https://i.imgur.com/sSDzI4m.jpg) Generalised Digital Asset Protocol\[/caption\] Bitcoin transactions make use of `OP_RETURN` to embed metadata to create or transfer digital assets to an output(s). These outputs can be audited for transactions on the blockchain to determine who the rightful owner of a digital asset is and how much of it they have.  

### The Bottleneck

The challenge with digital assets is **discovery** and **security** (i.e. secured vs unsecured loan). In the _gold certificate_ example, how do I find gold certificates to purchase, with the intention of taking delivery of physical ounces at some later date? How does the buyer know that the issuer of gold certificates will deliver physical ounces to the bearer? Is the depository institution reputable? Can I purchase gold certificates at a lower premium from someone else? All of these questions are solved by **OpenBazaar**.  

### Selling Digital Assets over OpenBazaar

The core of **OpenBazaar** is a combination of the following components:

1.  A contracting platform
    *   Allows a buyer and seller to lock in the terms of trade for the transfer of a digital asset via a [Ricardian contract](http://docs.openbazaar.org/03.-OpenBazaar-Protocol/#322-ricardian-contracts).
2.  A discovery network
    *   Permits users to scan the distributed peer-to-peer network for users selling digital assets you're interested in.
3.  A marketplace for dispute resolution
    *   Empowers contracting users to find a reputable agent to resolve any potential disputes, or release locked funds in escrow if one is unresponsive or incapacitated.
4.  A distributed reputation system
    *   Allows users to assess the transactional history and ratings of a Vendor within **OpenBazaar**.
5.  Bitcoin for payments
    *   Enables rapid and global payments as well as a powerful escrow system to prevent any one person from stealing funds.

For _issuers_ to sell their digital assets, they would firstly need to create a listing or 'ask order' on their node. Listings are simply JSON-formatted text files that fit the properties of a Ricardian contract, which are parsed and formatted in a user-friendly interface for buyers. The Ricardian contract schema for selling physical items, digital content (e.g. music), or services is not well suited for listing digital assets. As a result, we have created a new contract schema to list digital assets for sale. \[caption id="" align="aligncenter" width="377"\]![](https://drwasho.tinytake.com/media/1bb8eb?&filename=1442561731567_18-09-2015-05-33-21.png&type=attachment&&&_felix_session_id=b1d684167a98535482f2c5cd74797482&salt=MzA1MTc3XzE4MTY4MTE) Listing Schema for the Digital Asset in the Ricardian Contract.\[/caption\] Schema objects:

*   Issuance
    *   Boolean value to indicate whether the contract is issuing a digital asset or not
*   Asset
    *   **ID** \- what is the identity of the digital asset (typically defined by the protocol used to create it)
    *   **Source** - the transaction ID and bitcoin address that the digital asset is associated with, as well as the protocol used to issue/transfer the asset
    *   **Properties **- the schema nested within this object would be unique to the type of the digital asset; in the above example, the schema is for an equity security (i.e. stocks)
*   Quantity
    *   Number of units of the digital asset to be transferred
*   Price per asset
    *   **Bitcoin** \- if the digital asset is to be priced in bitcoin directly
    *   **Fiat** \- if the digital asset is to be priced in fiat, the seller needs to identity the fiat currency and price (at the time of sale, the necessary quantity of bitcoin will be calculated based on the exchange rate)

As with all Ricardian contracts in OpenBazaar, each stage of the _trade flow_ will be signed using the Seller and Buyer GUID keys. Trade Flow for Digital Assets

1.  The Seller creates a listing for the digital asset (equivalent of an ask order)
2.  Buyer sends a purchase order to the Seller
    *   The order includes an unsigned transaction
    *   Transaction has _n_ inputs and 1 output to send the purchase amount of the digital asset to the Seller
3.  The Seller acknowledges the order and replies with a signed transaction
    *   The Seller adds two components to the unsigned transaction:
        *   1 input from their digital asset address, transferring the equivalent of a miner's fee to the Buyer's new digital asset address
        *   An `OP_RETURN` output embedded with data (recognized by a specific digital asset protocol) releasing assets to the Buyer's digital asset address
4.  The Buyer receives the transaction, signs it, and broadcasts it to the network

_Final state:_ the funds are released to the Seller, and the digital asset is transferred to the Buyer. Note that for direct exchanges of Bitcoin for a digital asset, no multisignature escrow is required as a single transaction with multiple inputs and outputs can simultaneously fund the Seller and transfer the digital asset to the Buyer.  

### Securitized Digital Assets

Every digital asset has an underlying value it represents. A _gold certificate -_ it is a promise to redeem physical ounces of gold. A _gift certificate -_ any items purchased at a store up to a certain value. A _concert ticket -_ the price of admission to the concert. For the digital asset _holder_, they must have trust in _issuer_ to fulfill their obligation. For large and reputable institutions that are legally accessible, a Buyer may feel comfortable trusting their counterparty. However, this approach means that smaller institutions or pseudonymous individuals are unlikely to solicit enough trust from potential buyers. One possible solution is to _secure_ (financially) these digital assets by placing the purchase amount in multisignature escrow. This way, a Buyer can be refunded if the _issuer_ fails to deliver on their obligation. This comes with a trade-off to digital asset _liquidity_, and therefore may only be practical to certain high value digital assets where trust is low and risk is high. Alternatively, if a Moderator is involved in the transaction, they can purchase the escrow amount (to be released in the future) for a discounted present value. For example:

1.  Alice purchases 1 BTC worth of gold as a digital asset from Bob
2.  Charlie (the Moderator) sell 0.9 BTC to Bob in exchange for the 1 BTC in escrow to be released in the future
3.  Bob gets the funds immediately, while Charlie makes a profit at a later time point

This scenario breaks down if Bob fails to deliver any gold to Alice, defaulting on his obligation that triggers a refund to Alice. As a result, Charlie is taking a _risk_ with this approach for the chance for profit, all the while Alice is protected.  

### When will it be ready?

We aim to release a completely overhauled version of the client in the next few months that is focused on e-commerce (physical items, digital content, and services). Shortly after this, we will be progressively adding support to new types of Ricardian contracts and their corresponding trade flows to expand the use-cases of OpenBazaar. If you're a developer who wants to see this vision completed sooner rather than later, get in touch with us at `project [at] openbazaar dot org` or join our [community in Slack](https://openbazaar-slackin-drwasho.herokuapp.com/).     **Written by:** [Dr Washington Sanchez](https://twitter.com/drwasho) (drwasho)   **Special thanks to:**

*   [Amos Meiri](https://twitter.com/AmosMeiri)
*   [Ian Grigg](https://twitter.com/iang_fc)
*   [Austin Williams](https://twitter.com/onewayfunction)