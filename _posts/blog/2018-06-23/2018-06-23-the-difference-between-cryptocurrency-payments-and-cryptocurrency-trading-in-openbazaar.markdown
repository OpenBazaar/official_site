---
title: "The Difference Between <span class='post-title-extra'>Cryptocurrency Payments</span> and <span class='post-title-extra'>Cryptocurrency Trading</span> in OpenBazaar"
layout: post
date: '2018-06-23 08:30:00 -0600'
social_title: 'The Difference Between Cryptocurrency Payments and Cryptocurrency Trading in OpenBazaar'
social_description: 'We’ve been working hard to help users to do more things with the cryptocurrencies they love which now includes trading coins as well as buying things, both completely peer-to-peer. These two particular features are distinct though and we wanted to tell you a bit more about how they work.'
social_image: OB1 CEO Brian Hoffman and Toronto Crypto Community.png
---

Cryptocurrencies are very exciting to us, which we think we’ve made pretty apparent. We did, after all, build the **world’s first fully decentralized marketplace** to help cryptocurrency users find each other and buy and sell goods and services anywhere in the world using this groundbreaking new kind of money.

> While the “currency” part of cryptocurrency is particularly important to us, there are quite a few things other you can do with this technology, too.

Another important attribute they have is how they store and move value even when not measured against things like physical items or government-controlled currencies. With OpenBazaar we’ve been working hard to help users to do more things with the cryptocurrencies they love which now includes **trading coins** as well as **buying things**, both completely peer-to-peer. These two particular features are distinct though and we wanted to tell you a bit more about how they work.

![Setting Up a New Server Node Wallet on OpenBazaar](Setting-Up-a-New-Server-Node-Wallet-on-OpenBazaar-1.gif "Setting Up a New Server Node Wallet on OpenBazaar")

## Cryptocurrency Payments in OpenBazaar

Right now, sending and receiving payments for listings in OpenBazaar can be done with [Bitcoin](https://bitcoin.org/), [Bitcoin Cash](https://bitcoin.org/) or [Zcash](https://z.cash/) (this integration is in Beta). These payments require that both the buyer and seller have wallets running the same coin.

Users can **choose which of these 3 coins** they would like to run when they first set up their profile and/or store. If they would like to add additional coins they can easily set up additional profiles/stores to do so that are easy to switch between.

## Setting Up a New Server Node Wallet on OpenBazaar

They can also choose to add funds to their OpenBazaar wallets using any other coin they may have in an external wallet as enabled by the [Shapeshift](https://shapeshift.io/) Shifty Button integration. The coins will change and resolve to whichever of the 3 integrated coins the wallet is set to.

On the development side, integrating additional coins for payments like these 3 coins are is complicated to add and maintain with the current infrastructure. OpenBazaar requires that coins have certain technical attributes to be compatible with the checkout flow, they must have their own separate wallets within OpenBazaar, and users must run separate OpenBazaar nodes in order to support them.

> While we’ve made it easy to set up & toggle between different nodes running these different coins, we know this setup is far from ideal.

## Why is it set up this way?

This setup is the result of a choice we made to bridge a gap that opened up with Bitcoin when network transaction fees jumped very high at the end of 2017. We integrated Bitcoin Cash and Zcash quickly because of their technical similarity to Bitcoin, their supportive community and the ease of their implementation just to give users a couple more payment options that could allow them to circumvent these high fees if they wanted to.

Our plans now are to phase the network into a more inclusive structure starting with first **combining these 3 payment coins into just one wallet**. This **multicoin wallet** will allow users to easily use multiple coins at once rather than in separate nodes.

The long term goal is to expand the interface allow for any individual user to easily decide and set up whatever payment coins they would like to use.

## Cryptocurrency Trading in OpenBazaar

Cryptocurrency trading is a completely separate feature from the payment coins available in OpenBazaar. It’s enabled by a custom listing type that makes it easy for users to list and search for they coins they want to sell and buy. Users can buy and sell a variety of other coins but again, right now, they must use Bitcoin, Bitcoin Cash or Zcash for the actual payments.


![Setting Up a Cryptocurrency Listing for Sale on OpenBazaar](Setting-up-a-cryptocurrency-listing-on-OpenBazaar.gif "Setting Up a Cryptocurrency Listing for Sale on OpenBazaar")


Right now OpenBazaar uses third parties to pull in token information for our cryptocurrency trading. We started with [BitcoinAverage](https://bitcoinaverage.com/) which provides 44 different coins users can list. Soon we will also be adding [CoinMarketCap](https://coinmarketcap.com/)’s index which will shoot the available coins up to over 1,500. All coins available on these two platforms will also be available in OpenBazaar for trading. In the future we will also be able to add individual coins and we will soon be sharing a process for getting your coin listed if it is not already available through these providers.


![Cryptocurrency Trading on The OpenBazaar.com Home Page](Cryptocurrency-Trading-on-OpenBazaar-Home-Page.png "Cryptocurrency Trading on The OpenBazaar.com Home Page")
*See how it works on OpenBazaar.com!*
 

Now that you’re an expert in the existing structure of payment coins vs. trading coins, perhaps you’d be interested in what our development team is doing next with [Ethereum](http://bit.ly/2tynK31)?
 
If you're ready put your cryptocurrencies to work, [download OpenBazaar](https://openbazaar.org/download) now!