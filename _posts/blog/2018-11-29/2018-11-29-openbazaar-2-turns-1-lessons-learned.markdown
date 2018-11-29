---
title: "OpenBazaar 2 Turns 1: <span class='post-title-extra'>Lessons Learned</span>"
layout: post
date: '2018-11-29 06:30:00 -0300'
social_title: 'OpenBazaar 2 Turns 1: Lessons Learned'
social_description: 'OpenBazaar started more than four years ago, and for everyone involved it has been a learning experience. Here are a few lessons we’ve learned over the years, with a particular emphasis on the past year.'
---

This month we’ve been celebrating [the one year anniversary of OpenBazaar 2.0](https://openbazaar.org/blog/these-5-openbazaar-stats-are-really-exciting/). To read a summary of the last year, read [Brian Hoffman’s piece](https://openbazaar.org/blog/big-change-hard-work-and-strong-growth-openbazaar-2-turns-1/).

OpenBazaar started more than four years ago, and for everyone involved it has been an incredible learning experience. Here are a few lessons we’ve learned over the years, with a particular emphasis on the past year.

#### 1. Expect politics.

Just like Bitcoin, OpenBazaar is an open source piece of software and network of people running the software. As such, it’s incapable of having a “position” on any given issue. However, the individuals and companies building OpenBazaar do have opinions about issues in the cryptocurrency space. When they promote these beliefs – particularly on controversial issues – others will often claim “OpenBazaar believes X” instead of correctly attributing the opinion to the individual or company.

When we started building OpenBazaar in mid-2014 the community of people using cryptocurrencies was smaller, primarily focused on Bitcoin, and the majority of people agreed that building infrastructure in order to use cryptocurrency was worthwhile and necessary for broader adoption.

Over the next few years the community got larger and also began to disagree on the future of Bitcoin, such as how (or even if) it should scale. OpenBazaar itself played no role in this “scaling debate,” remaining neutral and following whichever chain the market decided upon. While the project itself was neutral, the individuals and companies working on OpenBazaar weren’t. In the new tribalist atmosphere created during the block size debate, this caused many to ascribe the individual positions of developers to the project itself, leading some to withdrawal their support and no longer use the marketplace.

For better or worse, the cryptocurrency space has become politicized over the past few years, and we now recognize the importance of emphasizing the project’s neutrality.

#### 2. Plan for all possible future scenarios—including unfavorable ones.

This lesson learned is also related to the scaling debate mentioned above. We recognized the possibility that fees could get high enough to prevent people from using Bitcoin for commerce. As individuals and as a company we supported efforts to keep Bitcoin functioning and not get to that point. Unfortunately, it happened anyway. 

> On the day OpenBazaar 2.0 launched the average Bitcoin fee was ~$5 per transaction and rising.

Even though we already knew high fees were a possibility, this all happened in a very short timeframe and forced us to react as quickly as possible. Since Bitcoin **wasn’t usable for commerce at the moment**, we decided to add support for new, usable cryptocurrencies into the client immediately.

This put us in the situation of publishing a Bitcoin-only product in November of 2017 and then needing to put all our developer efforts into making it a multi-coin product immediately afterwards, which was several months of work. Had we decided at the beginning to build OpenBazaar 2.0 with support for multiple coins it likely would have been simpler and the resulting UX would have been better.

Knowing about future scenarios and trying to make or prevent them from happening isn’t sufficient. You need to have plans in place for facing whatever reality meets your product.

#### 3. Don't get overly focused on a single product.

OpenBazaar is a desktop application. This is primarily for technical reasons; building a completely peer-to-peer application is tough for desktop only and even more so in a web browser or on a mobile device. 

The second reason is due to momentum. We started on desktop and have continued iterating on desktop because, while it has been difficult undertaking, it was one we became very familiar with.

[Web](https://openbazaar.com) and [mobile](http://ob1.io/) are implementations we are actively working on and have dreamed of realizing since the beginning, but they require very different engineering approaches and even philosophies. For them to begin development we had to deliberately choose to direct significant resources to them and many of the decisions made along these paths have not been easy.

Web-connected technology is evolving quickly now and organizations working in a sector like cryptocurrencies need to demonstrate 2 extremes: **focus** and **flexibility**. People are solving hard problems every day using this very new technology while also facing a growing market with changing desires. They need to be both steadfast _and_ nimble to tackle each day that may change all of their grandest plans.

We’ve learned a lot about developing open source software, managing a community and dealing with the changes and growth of cryptocurrencies over the past few years, and we certainly haven't been perfect. We appreciate the knowledge we have gained though and are executing against it in our daily work. We look forward to learning much, much more as we continue building the largest and most free decentralized ecommerce platform on the internet.

