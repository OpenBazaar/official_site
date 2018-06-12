---
title: "OpenBazaar v1.0 Is Updating" 
layout: post
date: '2017-08-30 00:30:00 -0300'
---
        
[OpenBazaar version 1.x](https://openbazaar.org/download) is currently down for updating.

The present version of OpenBazaar relies on a few federated Libbitcoin servers, which are Bitcoin full nodes, to interact with the Bitcoin blockchain. This was a remnant of when the project was DarkMarket. Unfortunately, after [the recent SegWit activation](https://www.openbazaar.org/blog/openbazaar-wallet-integrates-segwit/) they had issues and became corrupted. They are now resyncing the blockchain, which takes quite a while, but they should be caught up this evening.

To avoid similar problems in [OpenBazaar version 2.0](https://medium.com/@therealopenbazaar/openbazaar-2-0-p2p-trade-takes-the-next-step-4d75b7f23ec8#.m82tjvq47) we not only made the decision to move away from Libbitcoin but from servers entirely. 2.0 contains a peer-to-peer wallet that connects directly to nodes in the Bitcoin network. This removes the need for us to run infrastructure and removes a potential source of outages.

Thank you for your patience and we apologize for any inconvenience this has caused.