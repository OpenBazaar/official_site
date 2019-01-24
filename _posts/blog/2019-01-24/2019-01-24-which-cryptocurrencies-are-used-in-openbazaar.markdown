---
title: "Which Cryptocurrencies are used in OpenBazaar, <span class='post-title-extra'>and Why?</span>"
layout: post
date: '2019-01-24 08:30:00 -0600'
social_title: 'Which Cryptocurrencies are used in OpenBazaar, and Why?'
social_description: 'Explaining which cryptocurrencies are supported in OpenBazaar, and why they've been picked'
---

The decentralized marketplace OpenBazaar supports several different cryptocurrencies for buying and selling goods and services between users. This post explains which currencies, and why were they chosen.

## Cryptocurrencies Supported in OpenBazaar
* Bitcoin
* Bitcoin Cash
* Litecoin
* Zcash

## Why we Support these Cryptocurrencies

OpenBazaar was originally developed with only Bitcoin in mind. At the beginning of 2018 we [introduced](https://youtu.be/H4yW20txnB0) a handful of new coins, and in early 2019 version 2.3 was released which added Litecoin and a new wallet which supports multiple coins per instance, which made it easier to integrate new coins moving forward.

Because of the original reliance on Bitcoin, it’s always been a requirement for any supported cryptocurrency to be architecturally similar to Bitcoin for it to work properly. All the coins supported are forks of Bitcoin, unless otherwise noted.

Another requirement is multisig. OpenBazaar uses multisig for moderated and offline payments (escrow), and coins must have this feature - or the ability to support escrow payments another way - to be supported.

### Bitcoin
[Bitcoin](https://bitcoin.org/en/) is the original cryptocurrency. It is the most secure, with a large industry of miners devoting energy to securing the blockchain. It has the most users of any cryptocurrency, and is used for commerce more frequently.

Bitcoin was the only currency used in OpenBazaar from the beginning of the project in 2014 until early 2018. It is the most used cryptocurrency within the platform by a wide margin.

### Bitcoin Cash
[Bitcoin Cash](https://www.bitcoincash.org/) was forked from Bitcoin in August 2017. The creators of Bitcoin Cash disagreed with the development decisions of Bitcoin (particularly around scaling), and created new consensus rules. They focus on their cryptocurrency being usable for commerce on-chain.

OpenBazaar adopted Bitcoin Cash because adoption was technically simple due to its similarity to Bitcoin, and because community members were willing to offer support for the implementation.

### Litecoin
[Litecoin](https://litecoin.org/) was one of the earliest altcoins. It is very similar to Bitcoin in design, with a few differences such as having a quicker block generation time and different hash algorithm.

As one of the oldest altcoins it has well-established industry support, and a substantial community of users.

Just like Bitcoin Cash, OpenBazaar adopted Litecoin because adoption was technically simple due to its similarity to Bitcoin, and because community members were willing to offer support for the implementation.

### Zcash

[Zcash](https://z.cash/) is a cryptocurrency that focuses on privacy. It was forked from Bitcoin, but adds the ability to do “shielded transactions” using zk-SNARKs, which aren’t traceable on the blockchain like typical Bitcoin transactions.

Within OpenBazaar at the moment, shielded transactions using Zcash aren’t possible, and only transparent transactions (which aren’t private) are possible. At some point we hope to change that.

As with the other currencies mentioned,  OpenBazaar adopted Zcash because adoption was technically simple due to its similarity to Bitcoin, and because community members were willing to offer support for the implementation.

## Other cryptocurrencies
Ethereum support is being actively developed now.

Some ERC-20 tokens will also be supported after Ethereum support is added.

There is discussion about Monero support, but because of Monero’s multisig design it might only allow direct transactions, not escrowed.

This post will be updated when new coins are supported, or when new development is occurring.

