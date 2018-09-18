---
layout: pages/openbazaar-dispute-resolution-guidelines
title: "OpenBazaar Dispute Resolution Guidelines"
permalink: openbazaar-dispute-resolution-guidelines/
---

These are our guidelines for being a successful moderator on the OpenBazaar network.

#### 1. Moderators must be responsive
The biggest problem users have with moderators is when they are unresponsive. If a moderator is chosen for a dispute, and then is unresponsive, the transaction is stuck and both parties will be angry. If you are a moderator on the network you must not abandon your users. If you choose to no longer offer your services, you can remove yourself as a moderator in settings.

#### 2. Moderators _must_ be responsive
Seriously, this is so important that’s it’s #1 and #2. You need to respond quickly when a dispute is open. It’s crucial that moderators never go unresponsive.

#### 3. Moderators need to do their best to contact both parties involved
Moderators should set up their own rules to determine how long they’ll wait before settling a dispute. Only giving a day or two to respond isn’t long enough, but if you wait a month that’s probably too long. You must make a good faith effort to contact both parties to get their side of the story before resolving a dispute. Make sure to look for alternative contact information on their page instead of just using the built-in chat.

#### 4. Moderators need to be unbiased
You need to resolve disputes based on the information provided by both parties. If you can’t provide professional, unbiased dispute resolution, please don’t become a moderator.

#### 5. Moderators need to resolve disputes quickly and understand how the timeout works
Bitcoin prices are volatile, and the longer you take the more likely your customers will lose patience. Ensure that you’ve contacted both parties and gotten the information needed, but once you have, make sure to resolve as soon as possible.

If funds stay in the escrow for approximately 45 days, they will then be automatically released to the vendor. This “timeout” feature is included to prevent funds from being stuck in case parties become unresponsive. It also means that unscrupulous vendors can play the waiting game and receive the funds even if they didn’t deliver the product. Moderators must be aware of when funds will automatically release in order to prevent a vendor from receiving the funds if they don’t deserve them.

#### 6. Moderators should be clear about their own terms
If you refuse to moderate certain transactions, or only moderate for certain size transactions, or only in certain jurisdictions – or whatever your terms are – make sure to spell these out in the “Terms” section in moderator settings. This will reduce the number of cases people open that you won’t take because they violate your terms.

There are lots of examples of moderators setting their own terms. You can follow these links to see examples:

- [OB Central Moderation Agreement](https://gist.github.com/tyler-smith/44a1165975fdb670ba69041f02c986f5)
- [@Serp Moderation](https://mod.serpco.com/)
- [Lunokhod Moderation](https://gist.github.com/lunokhod/cd8a6dd45f6d8f6e813c959db79b742f)

If you need a refresher on how moderated payments work in OpenBazaar, you can read the section below.

### How Moderated Payments Work

OpenBazaar uses 2-of-3 multisig addresses for moderated payments. When a buyer wants to purchase a listing, instead of sending the funds directly to the seller, he will send the funds to the multisig account. The three people who control this account are the buyer, the seller, and a trusted third party selected beforehand. We call these trusted third parties ‘moderators’.

Now there are five possible ways for the funds to be released from the multisig address:

1. The seller sends the product or delivers the service and the buyer is satisfied. The buyer and seller are the two of three parties needed for the multisig, and together they release the funds to the seller. _This is what a normal transaction will look like._

2. The seller cannot deliver the listing as promised or the buyer is unhappy with the listing, and **they mutually agree to refund the buyer**. Again, the buyer and seller are the two of three parties needed for the multisig. This time they join together and release the funds to the buyer.

3. The buyer and seller are in a dispute and cannot agree how to release funds. The moderator comes in and decides that the **seller is at fault**. The moderator then joins with the buyer to release a refund to the buyer.

4. The buyer and seller are in a dispute and cannot agree how to release funds. The moderator comes in and decides that the **buyer is at fault**. The moderator then joins with the seller and releases the funds to the seller.

5. The buyer and seller are in a dispute and cannot agree how to release funds. The moderator comes in and decides that neither or both parties are at fault, and the moderator joins with either party to release funds in a split between buyer and seller.

In this fashion fraud is prevented by only allowing funds to be sent to the seller or refunded to buyer when either 1) buyer and seller mutually agree or 2) an independent third party decides which party is at fault and joins with the winning party to release funds.

