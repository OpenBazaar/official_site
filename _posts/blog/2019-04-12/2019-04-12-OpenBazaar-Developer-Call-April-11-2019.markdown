---
title: "OpenBazaar Developer Call - April 11, 2019"
layout: post
date: '2019-04-12 08:30:00 -0600'
social_title: 'OpenBazaar Developer Call - April 11, 2019'
social_description: 'This is a video recording of the OpenBazaar Developer call on April 11, 2019. '
---

This is a video recording of the OpenBazaar Developer call on April 11, 2019. 

Want to join the call in real time? Sign up at [openbazaar.org/developers](https://openbazaar.org/developers)

Join our ongoing conversations on [Slack](https://openbazaar.org/slack)

Browse OpenBazaar now at [openbazaar.com](https://openbazaar.com)

{% include modules/embeded-video.html url="https://www.youtube.com/embed/2z1UZo5S7WU"%}

**Chat log:**

[10:04]  mg (ob1): Good morning all, FYI we monitor and interact in the chat during the call. If you think of questions, feel free to post them here and we'll get them answered. :)

[10:07] DiarioBitcoin.com: are the relay servers custom relay servers for the OB protocol, or are they generic protocol agnostic relay servers (TURN)?

[10:10]  mg (ob1): The relay servers are specific to IPFS but are transport agnostic.

[10:10]  mg (ob1): They were designed to ensure that if one transport were blocked, the IPFS relay could bridge across transports as needed.

[10:11]  mg (ob1): More information: [https://github.com/ipfs/js-ipfs/tree/master/examples/circuit-relaying](https://github.com/ipfs/js-ipfs/tree/master/examples/circuit-relaying)

[10:11] DiarioBitcoin.com: thanks!

[10:11] DiarioBitcoin.com: Q: when DAI support?

[10:12]  mg (ob1): We'll get that one at the end. :)

[10:15]  mg (ob1): Thanks :) [https://github.com/OpenBazaar/samulator](https://github.com/OpenBazaar/samulator)

[10:20] Matt: what platform will tokens be based on?

[10:20]  mg (ob1): ERC-20

[10:20] Matt: you should consider [https://github.com/Bitcoin-com/slp-sdk](https://github.com/Bitcoin-com/slp-sdk)

[10:21]  mg (ob1): We might depending on our initial token success. SLP was barely ready when we began work on the token development.

[10:22] Rod: Has there been any news on the web buying/client side?

[10:22] DiarioBitcoin.com: thanks!

[10:22] MatthewZipkin: Possible to start signing releases? And post dev public keys

[10:24]  mg (ob1): Yes and on our radar in the near future. We do sign the commits but I don't think those keys are public.

[10:24]  mg (ob1): (but github.com verifies them, if you trust them)

[10:25] Rod: Thanks for the update 👍

[10:25]  mg (ob1): I think we'd end up with something like signed checksums per release. If you have something specific in mind, LMK.

[10:30]  mg (ob1): That's a great update Rod! Thanks for sharing.

[10:31] Matt: how will the import aliexpress thing prevent spoofing?

[10:31] Rod: ^^ Appreciate it mg 😄

[10:32] Matt: pretending to be a user on aliexpress

[10:32] Matt: yes thats what i mean

[10:32] Matt: thanks

[10:33] John: Thank you for the updates
