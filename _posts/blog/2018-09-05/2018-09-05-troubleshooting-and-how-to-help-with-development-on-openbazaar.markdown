---
title: "<span class='post-title-extra'>Troubleshooting</span> and How to Help with The <span class='post-title-extra'>Development</span> of OpenBazaar"
layout: post
date: '2018-09-05 08:30:00 -0600'
social_title: 'Troubleshooting and How to Help with The Development of OpenBazaar'
social_description: 'Troubleshooting and How to Help with The Development of OpenBazaar'
---

_By Mike Greenberg, OpenBazaar Backend Developer_

When we use any kind of software we are likely to encounter issues from time to time. With closed-source software, or software that we generally pay for, there's usually an easy way to contact someone for support as needed. You pay them, they fix your issues and it's a very closed, one-on-one discussion.

But there's a tradeoff: if that company changes their policies, pumps up their prices, or shuts down, that will have some effect on your ability to get that help—or even _keep using the software at all._ 

[Open source software](https://coincenter.org/entry/what-is-open-source-and-why-is-it-important-for-cryptocurrency-and-open-blockchain-projects) is a different kind of animal. It's the result of many people coming together, sometimes from all around the world, to build programs that are transparent and inclusive, where contribution to the code base is easy and collaborative. This decentralization of technology is a major part of what we love about cryptocurrencies like [Bitcoin](https://bitcoin.org/) because **it's all about giving power back to individual users and contributors**. It allows them to be in control and make decisions for themselves.

[OpenBazaar](https://openbazaar.org/download) is an open source application that is designed to be the fabric of future ecommerce with no middlemen involved and sometimes it presents some unique challenges. As the development leaders of this marketplace, we at [OB1](https://ob1.io) are focused on providing a quality user experience _within_ the app but also want to ensure users are empowered _outside_ of it as well so they can troubleshoot issues and help the platform keep growing. Which brings us to today’s topic...

#### Troubleshooting and Reporting Issues with OpenBazaar! (Cue applause)

OpenBazaar not only has the benefit of a company like OB1 ensuring its team is available, transparent and engaged with the community when people need assistance, it also has the communal benefits of an open source project.

Being able to navigate the resources of an open source project efficiently could save you time and headaches but may be different than what you're accustomed to. This post should help clear up the support options that are available when you need help and show you how to give back to the OpenBazaar community at the same time.

Let’s dig in.

### What Just Happened?

Uh oh. Your screen is displaying a cryptic error or the thing you expected never happened. Now what? The next steps are important to follow specifically in order to get to the bottom of it.

The first thing to do is record the specific error messages you see and/or take screenshots of the problem. **This part is critical for the developers to properly identify the root cause**. You are an archeologist making an archive of this bizarre behavior and you need to ensure it is preserved perfectly. 

* Text errors should always be copied and pasted where possible. 
* Visual anomalies should be screen captured. 
* Original file output relevant to the failure should be saved. 

Capturing these artifacts up-front will make sure they don't accidentally get lost by the application changing state automatically or losing power on your computer.

### Finding Solutions

Now that you have the details of the problem, we should make sure that someone else hasn't already reported the problem or found a fix. Often a problem has already been discussed and it's just a matter of using the right tools to find some answers. As a developer on the project, I usually spend 2-3 minutes searching for unique phrases in the error or picking search terms which are going to identify my problem uniquely from other problems. 

For example, consider the following error message:

![OpenBazaar error message indicating error following](There was an error following.png "OpenBazaar error message indicating error following")

The unique parts of this error are **error following** and the phrase **cannot start a transaction within a transaction**. Pay extra attention for developer misspellings if you're transcribing an error from a screengrab too. While misspellings are embarrassing, they may occur sometimes. Pasting these search phrases into your search engine of choice should reveal pretty quickly if anyone else has reported this issue yet. Making use of double-quotes around phrases which should match exactly is recommended to filter out unrelated results.

![Searching for OpenBazaar error message indicating error following"](Searching for OpenBazaar error following.png "Searching for OpenBazaar error message indicating error following")


A search for **OpenBazaar "error following"** produced a Github issue which was reporting the same error. However, when we open the issue we find that the cause of the error is due to something different and probably not related to our problem. I will leave a search for the other phrase as an exercise for you to try. Finding a discussion around an existing problem could lead to a solution that you might be able to apply yourself.

### Researching Resources

If a solution doesn't already exist, you will need to get your new problem report into the right hands. We have quite a few places across the internet where the OpenBazaar community offers help to each other. Take advantage of the open community by sharing your challenge in the appropriate channel.

Let's quickly walk through the **common resources** available and how they may be useful.

**1) [Frequently Asked Questions and Knowledge Base](https://openbazaar.zendesk.com/)**

Here we keep instructions for common tasks such as software setup, establishing your store, and handling moderation tasks. There’s also information about features which are unique to OpenBazaar like our multi-signature escrow or how vacation mode is used. This is primarily a read-only site which will surface the most regular questions from our users.

**2) Active Updates on [Twitter](https://twitter.com/openbazaar)**

Twitter can be a good source of up-to-the-minute news as well as a way to reach out to our team for urgent requests. Here you can find dialogue with fans, critics, news, updates, and promotions from our marketing team. It is an open platform for discussion with a short-form approach to dialogue.

**3) Community Discussion on [Reddit](https://reddit.com/r/openbazaar)**

Reddit allows for topical, threaded discussions and lets users discuss all sorts of things. Some leading topics in the OpenBazaar subreddit include: new stores, decentralized ecommerce news, cryptocurrency mechanics and issues which are hard to track down. The discussion on Reddit shifts over time but its persistence gives a good archive of past issues and thought-provoking conversation. Participating in the OpenBazaar subreddit can be anonymous and has no barrier to posting a question or comment short of creating a Reddit account. Most anything even slightly related to OpenBazaar can be posted here.

**4) Real-time Discussion on [Slack](https://openbazaar.org/slack) and [Telegram](https://t.me/OpenBazaarGroup)**

For high-bandwidth conversation with other users and contributors, our team and community congregate in these 2 discussion forums that function a lot like real-time chatrooms. Some areas of these communities focus on 3rd party search providers, moderators and escrow, and new ideas being tested on OpenBazaar, as well as offering each other help and support on common issues. Slack, by far the more popular of the two, has the most regular activity, as the OB1 team and many other developers are engaged there. Telegram is not quite as active but is a nice addition to Slack were people can pop in to ask quick questions about OpenBazaar or determine their next steps troubleshooting an issue.

**5) Development on [Github](https://github.com/openbazaar)**

Github contains the technical discussions and objectives of our various projects. Each repository contains a history of commits from previous contributors, a list of issues that represent pending work, and in some cases further technical documentation which is coupled to the software. This is where the rubber meets road as far as where improvements are discussed and added. It's safe to assume if a problem or issue is not being tracked in Github, it is not being worked on.

### Reporting The Problem

Okay, so what happens when you have exhausted all avenues of personal research and are still stumped? OB1 funnels all code changes through [Github's issue tracker](https://github.com/OpenBazaar/openbazaar-desktop/issues). When providing a bug report, including enough information in order to reproduce--and then fix--the problem is the primary objective. 

**Here is a brief checklist of useful information that should be included in the report:**

1. Mention your **operating system (OS) and version**. If the OS type and version is unknown for your computer, you can visit [http://whatsmyos.com](http://whatsmyos.com/) to help. (ex: Windows 10, MacOS 10.12.16, Ubuntu 16.04)
   
2. Mention your **OpenBazar software version**. This is indicated in the top right corner of the About screen, which can be launched from the navigation menu in the upper right. (ex: client 2.2.4, server 0.12.3)
   
3. Share any **specific error messages and screenshots** you have previously recorded.
   
4. Describe any **context or steps leading up to the error**. A bug may be unique to the original environment it was created in or it may only be triggered by following steps in a specific order. Developers will use this information to attempt to reproduce the error in a controlled environment. Only once the problem can be demonstrated can developers begin to isolate and repair the root cause. 
   
5. Clearly indicate **what you expected to happen**. The error you're experiencing may not be completely obvious to the developer that is reading your report. You may consider including your reason for wanting the problem to be solved the way you described. A developer may value this insight for improving the user experience of the feature.

Reporting a bug is as simple as opening an issue in the appropriate Github repository, which will most often be [openbazaar-go](https://github.com/OpenBazaar/openbazaar-go) or [openbazaar-desktop](https://github.com/OpenBazaar/openbazaar-desktop). OB1 separates the repositories for the frontend user interface and the backend server. If you are unsure which repository a report should be put into, take a good guess and we'll fix it if necessary. Once you have the information prepared, you can visit the Issues tab and click "New Issue" and paste the prepared information.

![Submitting an OpenBazaar Issue on Github](Submitting an OpenBazaar Issue on Github.png "Submitting an OpenBazaar Issue on Github")

What if you don't have a Github account to report the issue? That's okay. 
If you are unfamiliar with Github then you may also file a report using [Zendesk](https://openbazaar.zendesk.com/hc/en-us/requests/new).

Posting your report in Github is likely to get a faster solution, but you can also share your issue in any of the other official channels mentioned to begin a discussion. Who knows, you might even find another user is having the same issue later and puts both of your reports into Github. Our community IS pretty helpful!

### Following Up and Fixing

There may be some additional questions the team has. Please be sure to check back on your report from time to time to see if progress on your fix is being made and if more information about your problem may be needed.

### Conclusion

Reporting an issue to the OpenBazar community can be a bit of work but you can be an active part of finding or even building the solution. Since OpenBazaar is open source software, this is a huge part of how the marketplace grows. By taking the time to share your experiences with OB1 and other community developers you can contribute to making this software better for everyone—and maybe make some friends along the way.

If you haven't already, please make sure you come join us on [Slack](https://openbazaar.org/slack), our most active community forum, and say hello!
