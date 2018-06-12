---
title: "OpenBazaar and <span class='post-title-extra-alternative'>Bitcoin Fees</spam>" 
layout: post
date: '2017-11-16 00:30:00 -0300'
---
        
OpenBazaar currently uses Bitcoin for all payments, which allows us to enjoy the primary benefit of the leading cryptocurrency: secure payments without needing to trust a third party. No payment processors or banks needed, you control your own trade and your own money.

Bitcoin has many advantages over other payment methods, but there are disadvantages as well. One disadvantage is obvious to anyone using OpenBazaar at the moment: Bitcoin fees are extremely high.

OpenBazaar started in mid-2014, when fees averaged less than $0.10, and fees still averaged only around $0.20 when we began work on OpenBazaar 2.0 in summer 2016. In the past year we’ve seen rapid increases in fees, and the past week has seen fees at levels that severely inhibit lower value ecommerce transactions (fees are now well over $5).

The reasons for the increase in fees is complicated and not the purpose of this article. It’s also important to note that these fees are not guaranteed to stay this high forever – it’s possible that fees will drop to more ecommerce-friendly levels soon – but we aren’t just crossing our fingers waiting for this to happen.

> ### The question is, what has OpenBazaar done about high Bitcoin fees, and what more can be done?

What we’ve done
---------------

The new version of OpenBazaar, released Nov 1st, has a built-in Bitcoin wallet. We choose to build a wallet into the software because it gave users a better experience and because it allowed us to do more complicated Bitcoin transactions, such as multisig escrow and timelock.

The OpenBazaar development team decided to implement **Segwit** (a change to Bitcoin that can create cheaper transactions) in order to alleviate fee pressure and so that OpenBazaar wallets were compatible with other wallets as Segwit adoption increased. Segwit was implemented at launch, and is used by default when possible in transactions.

As fees increased we also saw the need to limit user’s actions to prevent transactions from being stuck in the escrow multisig. We use **2-of-3 multisig** for **moderated payments** and a **1-of-2 multisig** for **offline ordering**. Multisig transactions are powerful tools, but they require two Bitcoin fees instead of one. Not normally a problem with $0.10 fees, but when you are purchasing a $5 item and there’s a $5 fee, your payment will never be released to the vendor. Also, vendors are naturally upset to pay a $5 fee when receiving payment for a $10 item, which is effectively a 50% fee. For a detailed look at how Bitcoin fees work in OpenBazaar, you can read point #5 in our [vendor guide](https://www.openbazaar.org/blog/openbazaar-vendor-guide-what-to-expect-when-selling-on-the-worlds-largest-decentralized-marketplace/).

We have addressed this by preventing users from purchasing items which aren’t significantly higher than the current fee price. This prevents stuck transactions and angry vendors, but it also prevents people from using OpenBazaar for buying or selling inexpensive items. We want OpenBazaar to be a free marketplace for anyone to buy and sell anything, regardless of the overall price of the good or service, so this solution wasn’t something we were happy to implement.

What we will do
---------------

Though we’ve adopted Segwit in an effort to help our users reduce Bitcoin fees, second layer solutions like the Lightning Network aren’t available for end users yet so that will remain a bit of a waiting game.

Next, however, we are working to **integrate other cryptocurrencies** into OpenBazaar. Work on this has already begun and several community members from other coins have been working on integration. Initially we’ll likely offer just two or three other cryptocurrencies in addition to Bitcoin, but the long term goal is for OpenBazaar to be coin agnostic and allow payments in any cryptocurrency.

Because OpenBazaar is a fully decentralized p2p network, supporting various cryptocurrencies isn’t a simple change. This is currently the development team’s top priority, but users will need to wait more than Two Weeks™ to be able to use the new coins.

What you can do
---------------

There are a few things you can do that will reduce the impact of high fees.

1.  1.  **Everyone: Be mindful of prices and fees**  
           
        If you’re a vendor, consider listing higher value items while fees are high and being clear with buyers about why you are or aren’t willing to sell certain items and / or have certain prices. Buyers should pay attention to the fees when purchasing as well.
    
    3.  **Vendors: Keep your stores online**  
           
        When buyers place an order while the vendor is offline, the vendor pays an extra Bitcoin fee when they fulfill the order. Vendors who want to avoid paying that extra fee should keep their store running as often as possible.
    
    5.  **Developers: Help get your favorite coin added to OpenBazaar!**  
           
        If you’re a developer, particularly if you’re knowledgeable with cryptocurrencies, you can help us integrate these new coins.  
           
        If you’re not a developer, but you want another cryptocurrency integrated into OpenBazaar, try to get some community support to urge the coin’s developer community to contribute. Either way, please join us on [Reddit](https://reddit.com/r/openbazaar) or [click here](https://docs.google.com/forms/d/e/1FAIpQLSdEXqnREdncZYEXYSaE_wK41UV6JkBqNxqY5X-6J3oFNlZ72Q/viewform) to be invited to join us on Slack to contribute to the discussion!
    
    * * *
    
    **Still want to get started as we share some growing pains?**  
    [Download OpenBazaar](https://openbazaar.org/download) now!