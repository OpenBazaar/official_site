---
title: "First Look: Super Fast Checkout Process In OpenBazaar 2.0" 
layout: post
date: '2017-06-30 00:30:00 -0300'
---
        
Yesterday our designer, Mike Wolf, shared this great tweet about the speed of the purchasing time within OpenBazaar 2.0:

We want to be clear that this is an example of how fast it can be to get through the _checkout process_ within the application, not the time it takes the _transaction to clear on Bitcoin_. That will still be dependent on the bitcoin network itself.

**Why is the checkout process this fast, now?**

> Because of the internal wallet!

In the current version of OpenBazaar there is no built-in wallet so users need to use a wallet external to the app in order to make purchases. This gif shows the new process for OpenBazaar 2.0, launching soon, which has a wallet built into the application. Instead of being forced to use an external wallet, you will be able to pay bitcoin into the OpenBazaar wallet–where you still control your own keys locally–and then make payments as shown in the gif.

This new wallet is an SPV wallet where each user owns their own keys. Users will have this wallet by default though they can swap it out for bitcoind if they prefer. The wallet talks directly to the Bitcoin network, meaning all transactions are on-chain and there are no servers.

**Okay…but what’s an SPV wallet? **

The most secure way to use Bitcoin is to run a “full node” which means you have the entire copy of the blockchain and you verify all new transactions in new blocks yourself. However, running a full node is inconvenient, requiring a significant amount of disk space and other resources. The average user isn’t going to download the entire blockchain.

> That’s where **Simplified Payment Verification (SPV)** wallets come in.

The basic idea is that an SPV wallet doesn’t verify everything in blocks as accurate, so it doesn’t need to download the entire chain. It relies on a trusted node for verification.

We’re very excited about this new internal wallet because it offers a greater level of convenience and access to users that is reflected in this checkout time.  The whole purchasing flow is smooth and we cannot wait to get OpenBazaar 2.0 into users hands this summer.

* * *

**Are you ready to check it out?**

_Sign up for our newsletter [here](https://www.openbazaar.org/newsletter) for opportunities to be one of the first users of version 2.0[  
](https://openbazaar.org/)Join us on [Slack](http://slack.openbazaar.org/), [Twitter](https://twitter.com/openbazaar) or [Facebook](https://facebook.com/openbazaarproject)_

_And of course, you can still download [OpenBazaar v.1](https://openbazaar.org/) to shop right now!_