---
title: "Merchant's Guide to OpenBazaar Beta 0.4" 
layout: post
date: '2015-04-21 00:30:00 -0300'
---
        
_Note: This blog post is outdated. Read [this article](https://blog.openbazaar.org/three-openbazaar-code-repositories-created/) for the latest code._ For the fourth beta release, we're issuing guides for each of the three user types in OpenBazaar: [buyer](https://blog.openbazaar.org/buyers-guide-to-openbazaar-beta-0-4), merchant, and [notary](https://blog.openbazaar.org/notarys-guide-to-openbazaar-beta-0-4/). The [installation instructions](https://blog.openbazaar.org/openbazaar-beta-0-4-0-portobello-is-released/) are the same for each user. These guides assume that installation was successful and that the user can reach the client interface in their browser. If you can't, please check the [Github issues](https://github.com/OpenBazaar/OpenBazaar/issues) and our [Help Desk](https://openbazaar.zendesk.com/hc/en-us) to see if it's a known issue; if not then open a new issue on the Github or ask a question at our Help Desk.

Quick Start Guide
=================

This guide is meant to get merchants set up and offering goods and services as quickly as possible. For a detailed overview of the entire client, visit [here](https://blog.openbazaar.org/detailed-overview-of-openbazaar/).

#### Step One: Set up Store

![Settings Tab](http://i.imgur.com/28L8coh.gif)

1.  Click the Settings tab.
2.  Enter a new Nickname for your store. This is how other users will see your store.
3.  If you want a unique image for your store, put in a URL for an image in the Avatar URL field.
4.  Input a Bitcoin address _that you control_ into the Bitcoin Receiving Address field. This is where you receive funds from multisig if the notary needs to take action manually.
5.  Describe your store in the Store Description field.
6.  Click Save.

#### Step Two: Set Communication Information

[![communicationOB](communicationOB.png)](https://blog.openbazaar.org/wp-content/uploads/2015/04/communicationOB.png)

1.  Click on the Communication section.
2.  Enter an email address if you want to communicate with other parties via email.
3.  If you have a website that you want displayed, enter the URL in the Your Web Site field.
4.  Enter a Bitmessage address if you want to communicate with other parties via Bitmessage.
5.  Click Save.

#### Step Three: Create Backup

[![backupOB](backupOB.png)](https://blog.openbazaar.org/wp-content/uploads/2015/04/backupOB.png)

1.  Click on the Backup section.
2.  Click Create New Backup.

#### Step Four: List your Goods or Services

![Create Contract](http://i.imgur.com/jAtFHXV.gif)

1.  Click on the Contract tab.
2.  Click Add Contract.
3.  Input product details, including a title and description of your product, as well as the price (in Bitcoin), the cost of shipping, how many items are available, and what condition the items are in.
4.  Add up to three externally hosted images in the photos section.
5.  Make sure you click on the Keyword section next to Photos and input keywords that describe your product. This is how users find your items through the search function. If you don't add keywords, your items cannot be found via search.
6.  Click Save. This publishes your product to the network.

#### Step Five: Manage Trade

[![sellerOB](sellerOB.png)](https://blog.openbazaar.org/wp-content/uploads/2015/04/sellerOB.png)

1.  Manage your sales by viewing the My Sales section under the Orders tab. If you have an order, click on it to display details.
2.  If someone purchases your product, the item will display "Buyer Paid." **Please double check** the linked multisig account in the order description to verify; at this point a buyer can mark an item as paid without actually paying.
[![productOB](productOB.png)](productOB.png)4.  Determine if you trust the notary involved. Since at this point the buyer chooses the notary, if the two parties are colluding, they can cheat you out of the Bitcoin. You can view the notary involved by clicking "Contract Details" in the item description. Early in the beta, we recommend test transactions or small transactions until trusted notaries become established.
5.  If you verify the buyer has sent the funds to multisig, and that you trust the notary, then ship the item to the buyer at the address they provided. This address is displayed in the "Shipping Information" tab when viewing the order.
6.  Once you've shipped the item, input your Bitcoin address into the Shipping & Payment section of the order view, where it asks "Where would you like payment sent to?"
7.  Once the buyer receives the item, they should release payment. If they don't in a reasonable time, contact the buyer and request they release funds. If they are non-responsive, contact the notary involved in the transaction and request they release funds.

#### Step Six: Give Feedback

To make this network and client the best it can be, we need your feedback on how to improve. Bug reports are obviously very helpful, but feedback can be about which new features you'd like to see, or changes to the interface, or anything you like. Please submit these ideas by opening up new [Github issues](https://github.com/OpenBazaar/OpenBazaar/issues) or by posting at out [Help Desk](https://openbazaar.zendesk.com/hc/en-us).