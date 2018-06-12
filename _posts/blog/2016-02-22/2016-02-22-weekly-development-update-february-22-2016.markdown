---
title: "Weekly Development Update, February 22, 2016" 
layout: post
date: '2016-02-22 00:30:00 -0300'
---
        
### Back end

Updated protobufs. More work on refunds and moderation flow. Hardened seed and libbitcoin infrastructure.

### Front end

Clone item was added, to make it easy to duplicate items in your store. Items with ratings will now display those ratings. When the window is closed with command W, the app also closes. The SSL button was moved to the server config modal. You can see if a user follows you when you look at their page. The block button on a user's page is functional now. When you look at a blocked user's page, it is hidden, with a message asking if you want to unhide it. If you don't have anyone in your blocked list, a message is shown to indicate that. S status bar was added to the bottom of the screen to alert the user when a 3rd party service was taking a while to load (currently used for bitcoin price exchanges). Timeouts were lengthened or removed for the user page. Language updates from Kirvx, pryds, saltduck. Transactions chats are now working. Disputes can be created, and moderators can chat with sellers and buyers. All server settings can be changed from the settings/advanced view. Photos uploaded to a listing are limited to 10. If the connection to the server is lost, the server config modal appears automatically. Cleaned up all the assets: icons, tray icons, installer images, etc across all operating systems. The server configuration on startup has been greatly enhanced. http://i.imgur.com/kLBNiRV.png Cleaned up the Update OpenBazaar notifier and added a Test Mode flag http://i.imgur.com/lVPSerK.png