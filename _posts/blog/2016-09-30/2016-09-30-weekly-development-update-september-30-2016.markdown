---
title: "Weekly Development Update: September 30, 2016" 
layout: post
date: '2016-09-30 00:30:00 -0300'
---
        
Front End
---------

This week we completed work on the 1.1.8 release for the OpenBazaar reference client. The following features were added:

*   If the connection with the server is lost, the client will attempt to reconnect 5 times before showing the connection modal, and the status bar at the bottom of the app will show a connecting message when this is happening
*   The avatar can be rotated and saved in Settings/Page
*   The addresses in Settings/Addresses can be re-ordered by dragging and dropping--the first address is the default address
*   The follower, following, and store tabs have been made more efficient, so they take up less browser resources--this should speed up those views on slower computers
*   All languages have been updated with the latest translations from [Transifex](https://www.transifex.com/ob1/openbazaar)
*   Incoming data is now more effectively sanitized, preventing unwanted HTML tags
*   A bug where addresses that start with handles were malformed if you refreshed the app and loaded them from memory was fixed

**2.0** ![OpenBazaar 2.0 In Client Search](OpenBazaar-2.0-In-Client-Search-697x1024.png)

*   Designed the 3rd party search experience within the client
*   Avatar and header images can now be loaded in the Settings/Page modal, and will show on the navigation bar and the user page
*   The guid is shown above the social information on the user page and clicking it will copy the guid
*   Various improvements to the styling of the views

**SPECIAL EXTRAS!** We have finished the build process and are almost done with deployment on a tool that will make setting up an [OpenBazaar](http://openbazaar.org) shop incredibly simple. We are finishing testing it in production right now then will work on beautifying it a bit before rolling it out in the next couple of weeks!