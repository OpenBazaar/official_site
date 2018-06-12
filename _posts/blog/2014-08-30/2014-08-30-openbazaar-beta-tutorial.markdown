---
title: "OpenBazaar Beta Tutorial" 
layout: post
date: '2014-08-30 00:30:00 -0300'
---
        
_Note: This blog post is outdated. Read [this article](https://blog.openbazaar.org/three-openbazaar-code-repositories-created/) for the latest code._

Should I participate in the beta?
---------------------------------

Thanks for wanting to be involved with the OpenBazaar beta. We need the community to tell us what works and what doesn't, so we appreciate your help. However, participation in the beta is not for everyone, and not without risks. The platform is far from being complete, and those looking for a fully functional ecommerce platform are better off waiting until the full release, or at least later beta versions. We will be releasing new beta versions each month. The beta is for testing, and while you can engage in real trade, the purpose will be to test the platform, not actually run a store. Consider these points when deciding whether or not to enter the beta:

*   **Beta participation will require some level of technical expertise.** Installation details below. You will need to install quite a few dependencies.
*   **Users are not anonymous on the OpenBazaar network.** Your IP is visible to other nodes and is tied to the contracts you sell, purchase, or notarize. Tor will eventually be integrated, but for now privacy-conscious users must either wait for a later release or use a VPN they trust. It is up to each user to comply with local laws and their own conscience.
*   **The client and network will be undergoing constant change during beta.** You do have the ability to back up your data, but major changes may force a database reset which may cause lost data or other inconveniences.
*   **There will be bugs; real bitcoin could be lost.** Please be aware that that funds could be lost because of a bug or user error. We discourage users from making large transactions with real coins during beta. We aren't responsible for lost coins, and we're going to be too busy developing to be able to assist all the individuals who have coins trapped in multisig or otherwise have problems (though we obviously would like to know about the bug).
*   **OpenBazaar is run by part-time volunteers with little funding.** Our team is growing, but is still a small group of passionate folks who all have full-time jobs (and most have families as well). We are dedicated to giving the community a platform that finally allows people to trade directly with each other online. This is no small task, and we ask for patience from the community while we fix the bugs and improve the platform. Constructive criticism is very welcome - indeed, it's a primary goal of beta - but if you disagree with our approach on an issue, feel free to join the team and fix it, or fork the project entirely. Also, we will tend not to respond to basic questions that have already been discussed in our blog posts and documentation.

If you understand these points and wish to participate in the beta, then continue reading. I'll walk you through how to install OpenBazaar, how to run and use the client, and how to report bugs or make suggestions for improvement.

How do I install OpenBazaar?
----------------------------

### Linux and OSX

If you don't have Git installed in Linux, open terminal (Ctrl+Alt+T) and type: `sudo apt-get install git` If you don't have Git installed for OSX, download [here](http://git-scm.com/downloads) and install. Now run: `git clone https://github.com/OpenBazaar/OpenBazaar.git` Once that's complete, change directories: `cd OpenBazaar` Run the configure with this command: `./configure.sh` If the package doesn't install correctly, please issue a [bug report](#submit_bug). You can start and stop OpenBazaar from terminal with the following commands: `./openbazaar start` `./openbazaar stop`

### Windows

Download the [Windows binary](https://openbazaar.org/downloads/openbazaar-beta-3.0.zip) \[[signature here](https://openbazaar.org/downloads/openbazaar-beta-3.0.zip.sig)\], unzip the file and run the OpenBazaar.exe file. In case our site goes down, you can get a [torrent](https://openbazaar.org/downloads/openbazaar-beta-3.0.zip.torrent) with this [magnet link](magnet:?xt=urn:btih:282b503223bb9150aeb47a301d78cbd42c5ea764&dn=openbazaar-beta-3.0.zip&tr=dht%3a%2f%2f239E0DA5815B578C96EF9E65ED461A06B5357BF6.dht%2fannounce&ws=https%3a%2f%2fopenbazaar.org%2fdownloads%2fopenbazaar-beta-3.0.zip).

How to run
----------

It may take a few moments to start OpenBazaar, since on the first run it is generating keys pairs for you to use. The program will automatically open a browser with the right address to view the network. You should see a message which gives you warnings about using OpenBazaar during beta. **Read them carefully**. Now go to your settings, and fill in whatever details you like in the "Store Info" tab. [![Store Info](Screenshot-from-2014-08-31-215726.png)](https://blog.openbazaar.org/wp-content/uploads/2014/08/Screenshot-from-2014-08-31-210819.png) If you want to give other users more trust that you are an honest player in the network, you can participate in a [Reputation Pledge](https://blog.openbazaar.org/proof-of-burn-and-reputation-pledges/). Please note this burns the coins, so during beta we recommend just a very small amount to test with. In settings, if you go to the "Communication" section on the left, you can put in your email address or Bitmessage address in order to communicate with others on the network. [![Communications](https://blog.openbazaar.org/wp-content/uploads/2014/08/Screenshot-from-2014-08-31-210900-1024x563.png)](https://blog.openbazaar.org/wp-content/uploads/2014/08/Screenshot-from-2014-08-31-210900.png) Once you've finished your settings, go to the "Backup" tab and create a new backup. This will store your keys and information in case you need to import them later. Keep those keys safe as if they were bitcoin private keys. [![Backup](https://blog.openbazaar.org/wp-content/uploads/2014/08/Screenshot-from-2014-08-31-210923-1024x563.png)](https://blog.openbazaar.org/wp-content/uploads/2014/08/Screenshot-from-2014-08-31-210923.png) Now you're ready to use OpenBazaar. You can search for products or stores with the search bar up top. If you find a test product you'd like to practice on, or you want to get a real product, open up the item and click Next. If you see a warning that you don't have notaries, then go to a store you trust (for testing you can use the seeds), click on "Services," then "Make Trusted Notary." [![notary](https://blog.openbazaar.org/wp-content/uploads/2014/08/Screenshot-from-2014-08-31-212522-1024x563.png)](https://blog.openbazaar.org/wp-content/uploads/2014/08/Screenshot-from-2014-08-31-212522.png) Once they're trusted, you can go back to a seller's store and purchase their products, and select the notary you chose. In early beta, there probably isn't much to find on the network yet, so you should feel welcome to put out your own contracts. Open the "Contract" tab beneath the search bar. Click "Add Contract" and fill in the details. If this contract is just a test, please select note "Test" in the title and description so that others don't think your offer is a real one. [![test product](https://blog.openbazaar.org/wp-content/uploads/2014/08/Screenshot-from-2014-08-31-212658-1024x563.png)](https://blog.openbazaar.org/wp-content/uploads/2014/08/Screenshot-from-2014-08-31-212658.png) Once you find an item you want, select your notary and purchase it. Then go to your "My Purchases" drop-down menu under the Orders tab. [![mypurcahses](https://blog.openbazaar.org/wp-content/uploads/2014/08/Screenshot-from-2014-08-31-215704-1024x563.png)](https://blog.openbazaar.org/wp-content/uploads/2014/08/Screenshot-from-2014-08-31-215704.png) Open up your orders, and note that you need to pay the amount listed to the address displayed. This is funding the multisig which needs two of three parties to release. You can pay with your smartphone wallet using the QR code, or hit the "Pay in your Wallet" option to open your Bitcoin wallet and fill out a payment request. Once you've paid, be sure to mark the "Mark as Paid" option. [![itemtopayfor](https://blog.openbazaar.org/wp-content/uploads/2014/08/Screenshot-from-2014-08-31-215726-1024x563.png)](https://blog.openbazaar.org/wp-content/uploads/2014/08/Screenshot-from-2014-08-31-215726.png) The seller looks at the "My Sales" drop-down menu under the Orders the orders tab, verifies that the buyer has paid (this isn't automatic yet, so please check the hyperlink for payment), and then ships the product if the multisig has been funded correctly. Once shipped, they mark "Request Payment" and enter their bitcoin address where they want to receive the funds.

### Tips and Tricks

Here are a few things that might help you when using OpenBazaar. 1. Be patient. Items such as stores, products, or contracts you've published may take a little while to register. Wait a few seconds longer than you think you should need to, and then refresh your page and try again. If it still doesn't work, then report a bug. Also, finalizing a transaction may take longer than you expect as well. 2. Don't trust "Paid" as a seller. Right now, the buyer selects "Mark as Paid" to let the seller know when to ship the item. However, they can mark as paid without having actually paid. The seller needs to check the multisig address in the order (which is already hyperlinked) to make sure they actually did pay. In the future the client should check automatically, but for now, seller beware! 3. If you experience trouble connecting to other nodes, stop your node, and port forward 12345 on your router (both TCP and UDP), then try again. 4. We'll be making frequent changes to the code, so occasionally stop your node, run 'git pull' in the OpenBazaar folder to get the most recent changes, and start the node again.

Notaries and Arbitration
------------------------

If you are beta testing, please familiarise yourself with the concept of notaries and arbitration on OpenBazaar [here](https://gist.github.com/drwasho/405d51bd1b1a32e38145). In short, the roles for both agents are:

*   Notaries: to witness contracts between merchants and buyers using a cryptographic digital signature, and manage a bitcoin signing key for a multisignature escrow address in the event of a dispute between the merchant and buyer
*   Arbiter: to resolve a dispute between a merchant and buyer after careful examination of evidence presented by both parties

For reasons delineated in the article reference above, these roles should be handled by separate agents. However, only notaries are currently supported. The arbitration market isn't ready yet. If you want to become a notary to help out the network, you can do this in the settings under the notary tab, by checking the box “Make me a notary.” Please only become a notary if you are willing to:

1.  Automatically witness contracts for other parties
    *   This generally means having your node online close to 24/7
2.  Create and sign multisig transactions for all parties
    *   This means you must have experience with multisignature transactions and are a responsible key manager
3.  Possibly handle disputes between parties
    *   If all goes well, the notary is required to do very little as the client manages contract signing and key creation in the background
    *   In the event of a dispute, the notary must be able to respond to the parties rapidly (i.e. within 24 hours at a maximum)
    *   As the arbitration market is not supported just yet, the notary will also need to wear the hat of an arbiter

Becoming a notary requires you to have some technical knowledge of how to sign, verify, and broadcast multisignature transactions. If you do not know how to do this confidently, please do not become a notary just yet. We expect that notaries will charge a fee for handling disputes or releasing funds from the multisignature escrow address for other reasons. Part of beta will be watching how the notaries are rewarded. Future releases will allow the merchant and buyer to come to a consensus in the selection of a notary to minimise the risk of collusion. If you are a merchant trying to sell real goods for bitcoin, we again urge you to do so cautiously.

How do I submit a bug report?
-----------------------------

There are multiple ways to submit bug reports, depending on what you prefer. If you're a developer, or are otherwise knowledgeable about Github, you can [open an issue](https://github.com/OpenBazaar/OpenBazaar/issues) there directly. If you're not a developer or don't want to use Github, we also have a [thread in our subreddit](http://www.reddit.com/r/OpenBazaar/comments/2db46w/beta_testing_how_to_submit_bug_reports/) for bugs. Again, please follow the suggested format in the post. We'd like bugs submitted for any problems you run into, but if you see someone else reporting the same bug, you can just make a post noting that you have the same issue (if your OS or browser are different, let us know). Users can feel free to drop into our IRC room at #openbazaar on Freenode (if you don't have an IRC client use [this link](http://webchat.freenode.net/?channels=openbazaar)). If it's an installation issue we should be able to walk you through getting your node running properly.

How do I make suggestions for improvement?
------------------------------------------

We don't only want your feedback if something is broken; the point of the beta is to hear from the community on what they want in a peer to peer online trading platform. We encourage users to give us their thoughts on how to make OpenBazaar better. Again, you can open an issue on the Github, though we ask that it is specifically related to the code. For Redditors, we have a [thread for suggestions](http://www.reddit.com/r/OpenBazaar/comments/2db4la/beta_testing_how_to_make_suggestions_for/) as well.

### Begin testing

Thanks for reading, and testing. We'll be releasing a new beta version each month until we've got it running smoothly, then will release a full client. We'll be doing fixes along the way, so check back occasionally to see if that bug you submitted got fixed. Lastly, come join us on our IRC on Freenode at #openbazaar if you need help, or just want to chat.