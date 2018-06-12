---
title: "OpenBazaar Developer Call - March 1, 2018" 
layout: post
date: '2018-01-05 00:30:00 -0300'
excerpt: OpenBazaar Developer Call - March 1, 2018
---
        
**Attendees:**

*   OB1 team – 4
*   Guests – 5

**Upcoming releases:**

*   Verified moderators program –
*   45 day auto-release – After 45 days there’s an auto-release to sellers on offline and moderated payments & we’ve made it easier to release these funds. This is in response to times when buyers don’t know that completing their orders is what releases the funds to a seller.
*   Listing types for cryptocurrencies –
*   Automatic downloads for digital sales –

**Server updates:**

The OB1 team is working on ways to make it easier easier for development community members to invest their effort into the OpenBazaar codebase more effectively.

**Questions & Discussion:**

One attendee offered that he’s been working on a JavaScript library to aide his own development work and OB1 encouraged anyone that is interested in contributing in this way to jump right in without waiting for the core development team to start the activity.

_How has OB1 integrated Tor & what was that experience like?_

OB1 briefly discussed how OpenBazaar relies on users having their own Tor browser set up. This requires some configuration work on the user’s part on Windows and Mac and further questions were parlayed to OB1’s Lead Backend Developer, Chris, for deeper answers when he returns.

_How can users best connect other chains to OB without forking OpenBazaar?_

Another attendee has been looking at permissioned hyperledger channels for patient/provider profiles and an Ethereum ERC20 token as a payment method and they wondered about the interoperability of OpenBazaar with other chains.

OpenBazaar is 2 pieces, server & client. The nature of OpenBazaar is that it is not controlled by any one party, which makes restricting what nodes or listings anyone using it interacts with impossible. You would need to create a custom client and/or server that used a 3rd party service that provided a list of allowed content the custom app would be able to see. It’s important to note though that the rest of the OB network would still see that content, and be able to interact with it.

OpenBazaar content is stored using IPFS, they have some new technology they are releasing in the near future that may help with restricting content to certain viewers.

Finally, another attendee is working to gather support for a non-profit type coalition to raise awareness of the economic situation in Venezeuela & get solutions to the people there in the form of Bitcoin. You can read more about his agenda [here](https://medium.com/@jonathan.wheeler/leveraging-bitcoin-to-solve-venezuelas-hyperinflation-9f60c71d380b). At this time the scheduled call resolved but those who were interested continued for almost 45 more minutes to discuss this idea.

**Up next: **

Due to the increasing demand for participation in this call we are working to choose a more scalable tool to use so that more community members can join. These are the top 5 that we have been recommended. Do you have thoughts on any of these? Please share them in our Slack!

*   YouTube Live
*   Zoom
*   GoToWebinar
*   Crowdcast.io
*   Big Blue Button