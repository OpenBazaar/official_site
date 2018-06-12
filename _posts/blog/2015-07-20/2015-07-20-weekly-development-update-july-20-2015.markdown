---
title: "Weekly Development Update - July 20, 2015" 
layout: post
date: '2015-07-20 00:30:00 -0300'
---
        
In order to better keep the community up to date on the latest development on OpenBazaar, the OB1 team will now do regular updates on this blog, and cross post to our subreddit. We'll review last week's work and lay out where we're going for next week.

### Last week

#### Back end

After putting out the two new libraries, we started mapping out the messages that we plan to send between buyer-seller nodes and how we plan to implement it in the code. Some of the existing code for this will be reused, but it will mostly be a rewrite. A preliminary design can be seen in this image: \[caption width="2838" align="alignnone"\]![](https://i.imgur.com/AlZUIvd.png) Network Stack for OpenBazaar\[/caption\] We clarified the contract schema for all three contract types: physical goods, digital goods, and services, in addition to adding the flow diagrams for trade. [Documentation here](https://gist.github.com/SamPatt/8e8b1d749721ebe32486).

#### Front end

Lots of changes in the prototype. - wired up some missing pieces in the trade flow, specifically the final step - added a discover store section on the main screen - updated the transaction pages to use the tab navigation and list view - added search functionality to all list views - started integrating keyboard shortcuts into the list view (hit down or up to highlight a row) - built quick search into the address bar (example: @rp few) - finished onename integration to onboarding (as much as I could) - lots of misc clean up Store headers can also be GIFs, though there will be size limitations. Here's a short clip showing this (don't forget this will be an Electron app eventually, it won't be in browser).

### This week

We will continue integrating the DHT and txrudp code together, and begin implementation of the messaging between nodes started last week. UI development continues, with a focus on allowing store editing and publishing new listings.