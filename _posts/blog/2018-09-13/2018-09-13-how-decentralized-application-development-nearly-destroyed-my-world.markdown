---
title: "How <span class='post-title-extra'>Decentralized Application Development</span> Nearly <span class='post-title-extra'>Destroyed My World</span>"
layout: post
date: '2018-09-13 08:30:00 -0300'
social_title: 'How Decentralized Application Development Nearly Destroyed My World'
social_description: 'Ok, that title is a little hyperbolic, but decentralized applications with modern user experiences are few and far between and present some unique challenges for front-end developers.'
social_image: 
---

_By Rob Misiorowski, OpenBazaar Front End Developer_

Ok, that title is a little hyperbolic, but decentralized applications with modern user experiences are few and far between and present some unique challenges for front-end developers. In this post I'll describe some of these challenges and give examples of how we addressed them when developing the OpenBazaar desktop client.

### Fundamentally Different Paradigms

> In a **centralized application**, the data is primarily stored in and retrieved from one central source. 

For example, an app has 10,000 thing-a-magoos and they are all stored on a central server that's administered by professional engineers and has professional quality hardware and software behind it. It's optimized to process large numbers of client requests for data in a highly streamlined way.

This is useful when you need to retrieve and organize many pieces of data, like on a webpage that displays the top 50 thing-a-magoos on the network. With a centralized server, a client can efficiently retrieve the data it needs for all 50 thing-a-magoos in one single call.

> Now, let's consider a similar app, but one that is **decentralized**. 

The data doesn't live in one central location. Each user stores their own data and distributes it to other peers on the network as those peers view the data. Instead of highly optimized hardware, this is a blend of computers ranging from Joe's 8 year old desktop PC to Jennie's brand new macbook pro. While some of these may be high end, it's doubtful that most of these users will have production server level hardware or software. Now, instead of retrieving data from one central location, you likely have to go through all types of home routers and firewalls to get it.

Going back to our landing page example from above, instead of making a _single_ call to retrieve data for 50 thing-a-magoos, now we need to make _50 calls_ (one to each user) to retrieve the data. Actually, it will almost certainly be many multiple multiples of 50, since P2P libraries like [IPFS](https://ipfs.io) will retrieve the same pieces of data from multiple nodes to compare for authenticity.

### What Challenges Does This Cause?

It's hopefully getting clearer why there is much more leg-work involved in retrieving data in a decentralized way, but what challenges does this pose for clients?

- **Latency**

The speed difference is significant between retrieving a single piece of data from a highly optimized production server verses from the home computer of the average person. For example, in the centralized world, if the average server request takes more than a fraction of a second to return—let's say 250ms—it would often be considered slow and teams of engineers would be having meetings on how to reduce this. In our desktop client, we routinely have requests taking upwards of a minute before possibly timing out. And that's just for a single request. I'm sure you can imagine the difference between retrieving a list of 50 thing-a-magoos in one request from a central server versus having to make a call for each one across a network of distributed nodes.

- **Frequent data retrieval errors**

Consider a popular centralized app like Facebook. How often do you enter a legitimate url and have some type of error return? I would venture to say hardly ever. In a decentralized app this world is destroyed because quite regularly calls for data fail. Perhaps the user isn't online, nor are any seeders of the data? Perhaps some are online, but are unreachable? Perhaps you're even making a call for a piece of data that no longer exists (e.g. a deleted listing)? Further complicating the issue is that we often don't know the root cause of the failure. The error message could basically just be a large "shrug" emoji.

![Shrug Emoji](Shrug_Emoji.png "Shrug Emoji")

- **Browsers live in a centralized world**

The OpenBazaar front end is developed with Electron, which uses Chromium, the tech behind the Google Chrome browser. As such, it's subject to many of the browser’s restrictions. One of those is that you are limited to 6 concurrent requests to the same domain. Even though we're ultimately getting the data from many nodes, the requests are proxied through each node's server. In other words, from the browser's point of view, a fetch of 20 different user profiles are all coming from the same domain.

If latency weren't an issue this wouldn't be so bad. Even if a request took a less than ideal 250ms, you would be able to fully display a grid of 24 users in one second. But when requests routinely take 30 seconds, 45 seconds or 1 minute plus, suddenly it takes a whole lot of time to fully display a page. Even more problematic is that your request queue can clog up. Let's say one profile comes back in a lightning fast 100ms and we display a user box for that user with a Follow button. If there are still 23 pending requests, even if the user clicks that Follow button, it will be put at the end of the queue and not even be called until all but 5 requests remain, which may easily be a few minutes.

### An Example of How We Addressed These Challenges

OpenBazaar has an integrated chat section that's really an app within an app. The chat app is present from the time your server starts and remains perpetually in the sidebar. Initially, this was a world destroyer because the little **chat heads** (the user icons you click to open a conversation with a user) require some profile data from the party you’re conversing with (e.g. avatar, name). If a user is even slightly chatty and has engaged in at least 6 conversations, then those 6 profile calls would be enough to clog up the request queue and potentially prevent critical app functionality from being available.

![Chat Heads in OpenBazaar](Chat Heads in OpenBazaar.png "Chat Heads in OpenBazaar")

#### Here's how we handled some of the challenges decentralization presented us in OpenBazaar chat:

- **Latency**

The server stores a list of your conversations. Within that data set is the peer ID of each person you are chatting with and the last message in the conversation. This allows us to create a chat head with a default avatar and use the peer ID as the name. The peer ID is also enough to make a link to the user's page. While it may take up to a minute for the user's avatar and name show up, at least you'll have something showing in the client and you won't be prevented from starting the conversation.

Additionally, we implement multiple layers of caching. We can't do this for all requests because for some it's important you have fresh data. In this case, however, the user's name and avatar will likely not change that often and if you do see data that is a few minutes (or occasionally a few days) old, it doesn't degrade your experience.

One level of caching is done on the server where it will store the user's profile on disk. Then, when you make a call and indicate a cached response is acceptable, the server will immediately send back the cached version and behind-the-scenes make an IPFS query to update the cache. In theory, the cached version will never be more than one revision behind.

The other layer of cache is an in-memory client cache. The next time you request a profile where a cached version is ok, it won't even go to the server, it would use what the client has in-memory. Since this is in-memory, it will only be available until you shut down the app.

- **Frequent data retrieval errors**

Our approach here is exactly the same as our approach to latency: The user will initially see a default avatar and a peer ID but still have everything they need to start a conversation. The fact that the profile fetch may not succeed is really just a visual shortcoming. This is a form of progressive enhancement where we are starting with the bare minimum functionality and attempting to augment the experience along the way.

- **Browsers live in a centralized world**

This challenge was almost literally a world destroyer. If my memory serves me well, in OpenBazaar version 1.0 we had the chat app initialize before other important start-up functionality. For instance, while the chat app would be waiting on it's multiple profiles to come back, the Notifications mini-app would be showing you a spinner. Even worse, if you wanted to actually navigate to a page in the app, the data needed to show the page would be queued until all those profile calls finished...which, lest we forget, could be minutes.

It was a user experience deal breaker for those requests to be clogging up the queue and preventing critical functionality. But our hands were tied. If the browser imposes such a restriction, what could we do? Eventually, we stumbled upon the fact that the restriction is limited to HTTP requests. Incoming socket messages (which use TCP) have no such restriction. We added an `async` flag to most of our APIs so that the HTTP request would immediately return with a unique `requestId`. Subsequently, the profiles would come individually via socket messages. They would each include the `requestId` so we could map the profile to the initial request.

Boom! We could kick off as many profile calls as we wanted and have virtually no impact on the HTTP request queue.

### In Summary

While "world destroying" is a bit dramatic, these challenges were indeed _quite_ challenging! Decentralized applications with an intended user base of non-engineers (i.e. a client not meant to be used from the shell of your favorite exotic Unix distribution), are still rare and there just aren't that many best practices in place yet. Existing best practices for front end development are for centralized apps and a lot of them go right out the window when you introduce the challenges of decentralized data retrieval.

Decentralization is important though and, in my humble opinion, is here to stay. Over time, we'll get there. Client developers will continue to come up with clever solutions and P2P libraries and browsers will iterate and improve. Similar to how email clients have come from being limited to the engineering labs of universities to now being used by your Grandma on her iPad, decentralized computing is coming soon to a grandma near you.


