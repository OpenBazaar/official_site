---
title: "Weekly Development Update: September 2, 2016" 
layout: post
date: '2016-09-02 00:30:00 -0300'
---
        
Work on OpenBazaar 2.0 is fully underway, so we're now resuming our weekly development updates with an emphasis on the 2.0 repositories. You can follow along with development in our Github repositories, both [server](https://github.com/OpenBazaar/openbazaar-go) and [client](https://github.com/OpenBazaar/openbazaar-desktop).

Front End
---------

Following other users is now working, you can view another user's page and follow or unfollow them, and see them on your own page's list of who you are following, and who is following you. All "user cards" (mini views of a user) have a follow/unfollow button, this means you can see if you are following another user and follow or unfollow them anywhere a user card is displayed. For instance, if you're looking at the list of who another user follows, and you want to follow the same people, you can see which of the people they follow you're already following, and easily follow the ones you don't yet without leaving that screen.

### Design

Made many design & experience improvements in the [transaction section](Screenshot-from-2016-09-02-13-23-14.png) & transaction modal, including order status progress bar. Updated the design and experience for [providing feedback](Screenshot-from-2016-09-02-13-23-14.png) on an order. In 2.0, the buyer will have the ability to optionally include their identity in the review and also include photos. [![OBreviews](Screenshot-from-2016-09-02-13-23-14.png)](Screenshot-from-2016-09-02-13-23-14.png) Greatly simplified the 2.0 [checkout experience](https://invis.io/PE8F38SAU#/184735730_Openbazaar-2-0-Page-Listing-Detail) (2 clicks to buy for returning users), worked in shipping options and an input to optional provide a backup contact method.

Back End
--------

Completing documentation of best practices for production mode. Began work on making a public AWS image (current version). 2.0 work focused on order placement and processing.