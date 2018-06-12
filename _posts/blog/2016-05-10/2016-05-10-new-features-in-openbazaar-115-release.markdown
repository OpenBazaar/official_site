---
title: "New features in OpenBazaar 1.1.5 release" 
layout: post
date: '2016-05-10 00:30:00 -0300'
---
        
OpenBazaar version 1.1.5 has just been released ([download here](https://openbazaar.org/)). You can read the full changelog at the bottom of this post. This release includes several new features, including email notifications, multiple server management, CSV export for order management, and improved display of listing information.

Email notifications
-------------------

Users can now enter the details of an SMTP server in Settings > Advanced, and the server will connect to it to send email notifications about their OpenBazaar store. This feature is still early in development; users will need to have knowledge of their SMTP server to get this working, and the emails received are very simple. We will be making email notification easier to use in future releases, and the email notifications themselves will be more robust (we welcome help on improving this feature). [![OB Email](OBEmail.png)](https://blog.openbazaar.org/wp-content/uploads/2016/05/Screenshot-from-2016-05-10-15-19-36.png)   \[caption id="attachment_986" align="aligncenter" width="826"\][![Example email when an OB store receives an order](https://blog.openbazaar.org/wp-content/uploads/2016/05/OBEmail.png)](https://blog.openbazaar.org/wp-content/uploads/2016/05/OBEmail.png) Example email when an OB store receives an order\[/caption\]  

Server management
-----------------

Previous releases made it difficult to use a single client to switch between multiple servers. The new release greatly simplifies this process by saving server information and allowing switching within the same client. This video shows this new feature being used.  

CSV export
----------

Stores with a large number of products or orders need the ability to take data from their store and use it outside the client. We've added the ability to export this data into a CSV file. When viewing your transactions, click the Export CSV button to see the options. [![OBExport](OBExport.png)](OBExport.png)  

Listing information
-------------------

Listings now have more information about them available when viewing them in the Discover section. New listings created will now have a tag in the top right corner which shows the type of listing they are: Physical, Digital, or a Service. \[caption id="attachment_992" align="aligncenter" width="648"\][![Listings with the Physical item tag](noshipping.png)](https://blog.openbazaar.org/wp-content/uploads/2016/05/Listingtag.png) Listings with the Physical item tag\[/caption\] Users will also know now if the vendor isn't able to ship the item to their location with a new tag in the bottom right of the image. [![noshipping](https://blog.openbazaar.org/wp-content/uploads/2016/05/noshipping.png)](https://blog.openbazaar.org/wp-content/uploads/2016/05/noshipping.png)

[Changelog](https://github.com/OpenBazaar/OpenBazaar-Installer/releases/tag/v1.1.5)
-----------------------------------------------------------------------------------

 The following significant changes have been made in this release: ​

*   you can now save and edit server configurations, and quickly switch your client between different servers.
*   the navigation menu has shortcuts for switching between saved server configurations.
*   you can now set a SMTP server in settings/advanced to send email messages when various events occur.
*   if a listing can't be shipped to you, it is marked with an icon in the Discover and Store views.
*   listings are marked whether they are a physical, digital, or service listing. This only applies to listings made since the server was updated with the code to show this data.
*   basic information about your transactions can be exported to CSV from the transactions page
*   follower data on your store page is now lazy loaded, which should dramatically improve performance for stores with many followers.
*   chats with unread messages are positioned at the top of your chat list
*   the local node is only started if the client is currently set to connect to it
*   the shortcuts were changed to avoid colliding with common system shortcut keys. The reload the app shortcut is now 'f', and refresh the current view is 'r'.
*   you can add and remove a user as a moderator for your store from their user page.
*   Bitcoin prices are now formatted according to the language of the user.
*   a bug in the link for a listing in the transaction modal was fixed.
*   you can no longer attempt to purchase your own listings (the final step in the purchase flow is not clickable)

​ ​Special thanks to our contributors for code submissions to this release: ​ - Dekker3D - dsmurrell - mariodian ​ And special thanks to everyone that contributed to translations on Transifex (https://www.transifex.com/ob1/openbazaar).