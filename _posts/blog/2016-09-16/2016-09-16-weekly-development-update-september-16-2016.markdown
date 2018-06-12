---
title: "Weekly Development Update: September 16, 2016" 
layout: post
date: '2016-09-16 00:30:00 -0300'
---
        
This week we're [giving away](https://blog.openbazaar.org/giveaway-win-1-of-3-copies-of-the-internet-of-money-by-andreas-antonopoulos/) three copies of Andreas Antonopoulos's new book "The Internet of Money."

Front End
---------

Current version update: made address fields flexible, added a contact field to the address, removed time zones, improved the purchasing flow interface and fixed various bugs. 2.0 version update: improvements to the user page to allow dynamic lists of social information and live updates when data changes.

### Designs

Designed the [listing detail](Screenshot-from-2016-09-16-16-36-13.png) screen to open in an overlay instead of a new page. This will provide a better experience for the user and ensure they do not lose their spot within a store or channel grid view of listings. Also worked in listing variant options and touched up the checkout modal to work well with these new changes. [![Listing modal design](Screenshot-from-2016-09-16-16-36-13.png)](Screenshot-from-2016-09-16-16-36-13.png)    

Back End
--------

API [documentation](https://cpacia.github.io/) and authentication work. Build process being revamped on current version.