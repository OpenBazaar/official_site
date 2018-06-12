---
title: "Proof-of-burn and Reputation Pledges" 
layout: post
date: '2014-08-22 00:30:00 -0300'
---
        
OpenBazaar uses a particular implementation of proof-of-burn that we call _Reputation Pledges_ in order to help build trust among members of the network. This post will give you a quick overview of what this means, why it's necessary, and how you can use Reputation Pledges yourself.

Proof-of-burn
-------------

[![bitfiregray](bitfiregray.png)](bitfiregray.png) Proof-of-burn is a term used to describe the intentional and provable destruction of bitcoin for a particular purpose. When engaging in a proof-of-burn, funds are intentionally sent to an address that is unspendable, meaning those coins are gone forever. Why would someone destroy bitcoin on purpose? In the past, this has primarily been used to bootstrap one cryptocurrency from another. Distribution of a new cryptocurrency can be determined by people burning their coins in exchange for the new currency, thus showing they are invested. For an example of this, read through Counterparty's [explanation](https://wiki.counterparty.io/w/Proof_of_Burn) of their proof-of-burn.

Reputation Pledges
------------------

OpenBazaar implements proof-of-burn in a different way. On the OpenBazaar network, users can choose to be pseudonymous, meaning you don't know their true identity. As such, it can sometimes be difficult to determine if they are trustworthy or should be avoided. A reputation system is important to help inform the network of which participants have acted honestly in the past, and which haven't. There are several facets to the OpenBazaar reputation system, which is still being built, and you can read about the overall system [here](https://gist.github.com/dionyziz/e3b296861175e0ebea4b). One part of this system is Reputation Pledges. This means that a user has chosen to prove their commitment to their OpenBazaar identity by burning a certain amount of bitcoin. The act of burning coins shows the network that the user is committed to their identity because they've now expended resources on it, and if they incur a negative reputation then those resources will have gone to waste. To help understand the importance of this, consider a similar example in the real world. Travelling salesmen were often treated with skepticism by the inhabitants of the towns they visited. Apart from the annoyance of their house calls, why would people be reluctant to purchase items from travelling salesmen? Two reasons. One, they cannot rely on reputation to determine if the salesman is selling quality merchandise or not; the other customers of this salesmen aren't located nearby. Two, the salesman has nothing to lose if their products turn out to be poor quality - there is no reputation damage if they leave, and since there is no brick-and-mortar store they've invested in, they can simply peddle their wares elsewhere. You can think of it similarly to OpenBazaar users. If there's no cost to creating a new identity, or if there is no brick-and-mortar store to keep you in one place, you can simply abandon an identity once it has received negative feedback. Obviously online, you don't have a physical store, but a Reputation Pledge is a similar concept: you've invested resources that create an incentive to keep a good reputation and impose a significant cost for abandoning that reputation.

How it works
------------

Engaging in a Reputation Pledge is simple. I'll have a complete walk-through of this very soon, for now you can view the Reputation Pledge in the "settings" tab.