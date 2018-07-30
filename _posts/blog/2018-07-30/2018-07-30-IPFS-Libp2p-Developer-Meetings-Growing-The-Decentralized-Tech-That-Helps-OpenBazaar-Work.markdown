---
title: "IPFS & Libp2p Developer Meetings - Growing The <span class='post-title-extra'>Decentralized Tech</span> That Helps OpenBazaar Work"
layout: post
date: '2018-07-30 08:30:00 -0600'
social_title: 'IPFS & Libp2p Developer Meetings - Growing The Decentralized Tech That Helps OpenBazaar Work'
social_description: 'OB1 Lead Developer Chris Pacia gives a recap of the IPFS & Libp2p Developer Meetings in Berlin.'
---

![IPFS and Libp2p Developer Meetings in Berlin 2018](IPFS and Libp2p Developer Meetings in Berlin 2018.jpg "IPFS and Libp2p Developer Meetings in Berlin 2018")


This month I had the opportunity to attend the [IPFS/Libp2p Developer Meeting](https://github.com/ipfs/conf) in Berlin. [IPFS](https://ipfs.io/) development is of great importance to us as OpenBazaar is built on top of it and relies heavily on it for most of its functionality. Overall the meeting was very productive. It was nice to meet the new members of the [Protocol Labs](https://protocol.ai/) team and see how they are growing. They have an enormous amount of talent on their team and in the IPFS community and they’re genuinely solving very hard problems in decentralized web development. 

![IPFS and Libp2p Developer Meetings in Berlin 2018 - Presentation](IPFS and Libp2p Developer Meetings in Berlin 2018-2.jpg "IPFS and Libp2p Developer Meetings in Berlin 2018 - Presentation")

Here are some of the key takeaways from this event as they relate directly to OpenBazaar:

## QUIC

They’ve been able to integrate [QUIC](https://www.chromium.org/quic) as a transport for IPFS. For those who don’t what QUIC is, it’s a new transport created by Google which offers all around better performance than TCP. Not only will QUIC make OpenBazaar faster, but it will help slightly with NAT traversal. 

## IPNS Pubsub

Pubsub isn’t yet hooked up in the IPFS coreapi package but will be shortly. While we will still need to make a DHT crawl the first time an IPNS query is made as well as when coming back from absence, all subsequent queries will return the most up-to-date record instantly. We should see a nice speed boost in browsing as a result. 

## NAT Traversal

I learned that IPFS is already doing more for NAT traversal than I realized but more work is still needed. Currently a high percentage of nodes on the IPFS network are not reachable and I presume it’s probably a similar percentage of OpenBazaar nodes. We had some nice discussion about improving NAT traversal. The first action item is to wire up the libp2p-autonat package which will help detect if users are behind restricted NATs. Moving forward we’d like to develop some heuristics for deciding if and how to relay packets through other nodes using the libp2p-circuit-relay.

## New onion-transport

They’ve done some preliminary work on a new onion transport for libp2p. Our currentl transport was written by me and will at minimum need to be changed to conform to planned changes to the transport interface. I believe the goal, however, will be to have the new transport ready by the time that new interface goes live so we can easily make their switch. There’s also a possibility we can use a library which statically compiles the Tor daemon and maybe resolve some issues running OpenBazaar on Tails and Whonix. 

There was plenty more talked about and presented, some of which will likely be in OpenBazaar under the hood but also plenty of projects that are genuinely interesting in the own right. 

We’ll look forward to seeing everyone again for IPFS conference in Lisbon in November. 
