---
title: "Buyer's Guide to OpenBazaar Beta 0.4" 
layout: post
date: '2015-04-21 00:30:00 -0300'
---
        
_Note: This blog post is outdated. Read [this article](https://blog.openbazaar.org/three-openbazaar-code-repositories-created/) for the latest code._ For the fourth beta release, we're issuing guides for each of the three user types in OpenBazaar: buyer, [merchant](https://blog.openbazaar.org/merchants-guide-to-openbazaar-beta-0-4/), and [notary](https://blog.openbazaar.org/notarys-guide-to-openbazaar-beta-0-4/). The [installation instructions](https://blog.openbazaar.org/openbazaar-beta-0-4-0-portobello-is-released/) are the same for each user. These guides assume that installation was successful and that the user can reach the client interface in their browser. If you can't, please check the [Github issues](https://github.com/OpenBazaar/OpenBazaar/issues) and our [Help Desk](https://openbazaar.zendesk.com/hc/en-us) to see if it's a known issue; if not then open a new issue on the Github or ask a question at our Help Desk.

Quick Start Guide
=================

This guide is meant to get buyers set up and shopping for goods and services as quickly as possible. For a detailed overview of the entire client, visit [here](https://blog.openbazaar.org/detailed-overview-of-openbazaar/).

#### Step One: Personalize your Client

![Settings Tab](http://i.imgur.com/28L8coh.gif)

1.  Click the Settings tab.
2.  Enter a new Nickname for yourself. This is how other users will see you.
3.  If you want a unique image for your avatar, put in a URL for an image in the Avatar URL field.
4.  Input a Bitcoin address _that you control_ into the Bitcoin Receiving Address field. This is where you receive funds from multisig if the notary needs to take action manually.
5.  Click Save.

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

#### Step Four: Find & Trust a Notary

![Trusting a Notary](http://i.imgur.com/xp8kgug.gif) Notaries are a vital part of OpenBazaar. They are the third key holder in the 2 of 3 multisig, meaning that if there is a dispute between buyer and merchant, only the notary has the power to work with one of the parties to release the funds. As such, it's important that buyer and merchant trust the notary not to collude with the other party. In beta we recommend smaller transactions until reputable notaries emerge in the market. When viewing stores on the Home tab, look for users that offer services. This is only visible if the user offers notary services. If they do, it will display their percentage fee, a description of their services, and allow users to select them as notaries by clicking "Make Trusted Notary." You can also manually add a notary in Settings if you know their GUID (string of letters and numbers under the store name).

#### Step Five: Find & Purchase Goods or Services

[![PipeExampleOB](orderdetailsOB.png)](https://blog.openbazaar.org/wp-content/uploads/2015/04/PipeExampleOB.png) If you click on an item in a store in the Home tab, a new window opens to give more product details, including the product title, price in Bitcoin, product description, cost of shipping and handling, quantity available, the item's condition, and up to three photos. There is also a "Raw Contract" button which allows users to view the contract details directly. [![orderdetailsOB](https://blog.openbazaar.org/wp-content/uploads/2015/04/orderdetailsOB-1024x621.png)](https://blog.openbazaar.org/wp-content/uploads/2015/04/orderdetailsOB.png) Clicking on "Order Details" on the bottom left will bring you to a screen that allows you to purchase the product. You can determine the quantity desired, and attach a comment for the merchant to see along with your order. If you haven't entered your shipping address in Settings already, a red warning will ask you to do so before proceeding. The price for the product and shipping and handling are displayed again. At the bottom the user needs to input a Bitcoin Address that they control. This will be used in case of a refund. Once this section is completed, the user selects "Choose a Notary." A list of online notaries that the user has trusted is displayed. If the user hasn't trusted any notaries, or if none of those notaries are online, they must choose another notary in order to continue. The user then completes the order by selecting "Submit Order." This sends the order to the notary and merchant.

#### Step Six: Finish the Purchase

When a buyer views "My Purchases" it will display the status of their orders. If they've just submitted an order, the status will indicate "Need to Pay" and the buyer needs to open the order to complete payment. [![needtopayOB](needtopayOB.png)](https://blog.openbazaar.org/wp-content/uploads/2015/04/needtopayOB.png) A QR code is displayed which, if scanned, will input the multisignature address and amount. If the user selects "Pay in your Wallet," it will open a wallet on their device and pull in the same information. Once the payment is completed, the buyer must manually select "Mark as Paid." This lets the merchant know to ship the item. If the buyer marked the order as paid, but the merchant didn't receive this message due to being offline, the buyer can re-open the order and click on "Resend Payment Notice" when the merchant is online. Once the item has arrived or service is provided, the buyer can then release the funds from multisig by opening the order and selecting "Release Payment to Merchant." Again, if the merchant didn't receive this message due to being offline, the buyer can try releasing again when they are online.

#### Step Seven: Give Feedback

To make this network and client the best it can be, we need your feedback on how to improve. Bug reports are obviously very helpful, but feedback can be about which new features you'd like to see, or changes to the interface, or anything you like. Please submit these ideas by opening up new [Github issues](https://github.com/OpenBazaar/OpenBazaar/issues) or by posting at out [Help Desk](https://openbazaar.zendesk.com/hc/en-us).