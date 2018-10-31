---
title: "Why We Are Integrating <span class='post-title-extra'>Ethereum</span> into OpenBazaar"
layout: post
date: '2018-10-31 08:30:00 -0600'
social_title: 'Why We Are Integrating Ethereum into OpenBazaar'
social_description: 'Why We Are Integrating Ethereum into OpenBazaar'
---

In a previous article we explained [how we’re integrating Ethereum into OpenBazaar](https://openbazaar.org/blog/Escrow-Smart-Contract-Specification-in-OpenBazaar/). In this article we want to talk about _why_ we're integrating [Ethereum](https://www.ethereum.org/).

#### Bitcoin Beginnings

OpenBazaar began as a Bitcoin-only project, with the intention of creating an open, permissionless marketplace with no fees and no middlemen. From the beginning, users wanted the ability to accept payments in cryptocurrencies other than bitcoin. While that was possible via our [Shapeshift](https://shapeshift.io/) integration, such payments weren't really trustless. Non-bitcoin payments would just be Shapeshifted into bitcoin payments. Users effectively had to use Shapeshift as a middleman, had to trust them not to steal their funds, and had to pay them for the privilege. In that sense, non-bitcoin payments weren't really _native_ to OpenBazaar.

Then, in late 2017, bitcoin transaction fees began to rise. [A lot](https://bitinfocharts.com/comparison/bitcoin-transactionfees.htm). Using bitcoin for payments on OpenBazaar became impractical for months. Since payments in non-bitcoin currencies weren't native on OpenBazaar (they were simply Shapefshifted into bitcoin payments) that meant _all_ payments on OpenBazaar were impractical. Users wanted to use alternative currencies, but we were -- effectively -- forcing them to use bitcoin. Use of the platform ground to a halt. It was obvious something needed to change.

#### Becoming Crypto-Inclusive

We want users to be able to trade using **any cryptocurrency they desire**, without exposure to risks caused by other chains. In early 2018, in response to urgent demand from our users, we began integrating native altcoin payments into OpenBazaar. We're refactoring our codebase to make it much easier to integrate new cryptocurrencies natively. The low hanging fruit are coins that are forks of Bitcoin, as their codebases are closest to what OpenBazaar was already supporting. [Bitcoin Cash](https://www.bitcoincash.org/) and [Zcash](https://z.cash/) were the first such integrations, and [Litecoin](https://litecoin.org/) integration is almost complete.

#### Enter Ethereum

A natural continuation of that effort is to integrate Ethereum. Since Ethereum doesn't share Bitcoin's codebase, it will be more challenging to integrate than forks of Bitcoin. But we think it's worth the effort because:

- Ethereum has the largest community outside of Bitcoin.
- Developer activity on Ethereum is huge and enthusiastic.
- The community has a special eagerness for its coin and tokens to be used for real-world commerce. 
  
Integrating **ETH** and **ERC20 payments** is a natural next-step for OpenBazaar.

Beyond simple payments, **smart contracts** built on Ethereum -- with its rich Turing-complete scripting language -- may allow us to support markets that would be extremely challenging to support with Bitcoin-like script-based cryptocurrencies. Trustless auctions, DAO-based stores, insurance contracts, and affiliate marketing are just a few of the ideas we are exploring. Integrating Ethereum has the potential expand the types of products and services offered on the platform.

#### In Summary

In short, the landscape isn’t what is was when OpenBazaar first started. There is a rich ecosystem we cannot afford to ignore, and Ethereum is a huge part of that. We’re excited about implementing ETH and ERC20 payments, and are looking forward to working with the Ethereum community as we explore how we can leverage smart contracts in OpenBazaar.
