---
title: "Notary's Guide to OpenBazaar Beta 0.4" 
layout: post
date: '2015-04-21 00:30:00 -0300'
---
        
_Note: This blog post is outdated. Read [this article](https://blog.openbazaar.org/three-openbazaar-code-repositories-created/) for the latest code._ For the fourth beta release, we're issuing guides for each of the three user types in OpenBazaar: [buyer](https://blog.openbazaar.org/buyers-guide-to-openbazaar-beta-0-4), [merchant](https://blog.openbazaar.org/merchants-guide-to-openbazaar-beta-0-4/), and notary. The [installation instructions](https://blog.openbazaar.org/openbazaar-beta-0-4-0-portobello-is-released/) are the same for each user. These guides assume that installation was successful and that the user can reach the client interface in their browser. If you can't, please check the [Github issues](https://github.com/OpenBazaar/OpenBazaar/issues) and our [Help Desk](https://openbazaar.zendesk.com/hc/en-us) to see if it's a known issue; if not then open a new issue on the Github or ask a question at our Help Desk.

Quick Start Guide
=================

This guide is meant to get notaries set up and offering their services to buyers and merchants as quickly as possible. For a detailed overview of the entire client, visit [here](https://blog.openbazaar.org/detailed-overview-of-openbazaar/).

#### Step One: Personalize your Client

![Settings Tab](http://i.imgur.com/28L8coh.gif)

1.  Click the Settings tab.
2.  Enter a new Nickname for yourself. This is how other users will see you.
3.  If you want a unique image for your avatar, put in a URL for an image in the Avatar URL field.
4.  Input a Bitcoin address _that you control_ into the Bitcoin Receiving Address field. This is where you receive funds from multisig if your services are needed.
5.  Click Save.

#### Step Two: Set Communication Information

[![communicationOB](communicationOB.png)](communicationOB.png)

1.  Click on the Communication section.
2.  Enter an email address if you want to communicate with other parties via email.
3.  If you have a website that you want displayed, enter the URL in the Your Web Site field.
4.  Enter a Bitmessage address if you want to communicate with other parties via Bitmessage.
5.  Click Save.

#### Step Three: Create Backup

[![backupOB](backupOB.png)](backupOB.png)

1.  Click on the Backup section.
2.  Click Create New Backup.

#### Step Four: Set up your Notary Details

In Settings, select the Notary section.

1.  **Make me a notary**. By clicking Yes in this section, you allow others to choose you as a notary. They will see this option when they click on your store front and see the "Services" tab, or by manually entering your GUID into the Trusted Notaries section. The default option is set to No; users aren't notaries unless they choose to be.
2.  **Fees**. As a notary, you can charge a percentage fee for providing dispute resolution. If the buyer and seller finish their transaction without needing the notary, there is no payment. If the notary is needed to refund buyer or release payment to merchant, then they will receive the percentage from the multisig that they set in this section. A notaries' fee is visible in the "Services" tab in their store front.
3.  **Description of your services**. Notaries can explain their terms and conditions in this area, as well as their credentials and any other information they wish to share.

#### Step Five: Manage your Orders

Note that at this point, offering notary services means you automatically accept all transactions which choose you as a notary. In the future, notaries will be able to screen transactions, or only accept them manually. If a buyer or seller contacts a notary asking for funds to be released, it's the notary's responsibility to do their best to determine which party should receive funds. Once they've made their decision and contacted the parties, they can release funds by opening up the order in the notarizations tab. [![OBnotary](OBnotary.png)](OBnotary.png) In the 0.4 client, the notary has two options. "Refund the Buyer" releases all the funds from multisig to the buyer, minus the percentage fee which is paid to the notary for dispute resolution. "Release money to the Merchant" does the same for the merchant. The notary must click "Send Resolution" for the transaction to process.

#### Step Six: Give Feedback

To make this network and client the best it can be, we need your feedback on how to improve. Bug reports are obviously very helpful, but feedback can be about which new features you'd like to see, or changes to the interface, or anything you like. Please submit these ideas by opening up new [Github issues](https://github.com/OpenBazaar/OpenBazaar/issues) or by posting at out [Help Desk](https://openbazaar.zendesk.com/hc/en-us).