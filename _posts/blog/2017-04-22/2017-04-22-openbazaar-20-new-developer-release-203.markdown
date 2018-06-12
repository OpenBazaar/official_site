---
title: "OpenBazaar 2.0 - New Developer Release - 2.0.3" 
layout: post
date: '2017-04-22 00:30:00 -0300'
---
        
_This is the third release according to our [new schedule](https://blog.openbazaar.org/new-version-2-0-development-release-schedule/) of publishing releases on a two week sprint cycle. As a reminder, these releases are for developers and those looking to test only; the product **is not ready** for real transactions yet!_

* * *

Yesterday we released a new developer release – **[version 2.0.3](https://github.com/OpenBazaar/openbazaar-desktop/releases)** – of OpenBazaar. Here is a brief overview of the new features available:

**Back End:**

*   We’ve done some housecleaning, making the code more consistent and robust.
*   The ability to use images for variants was added. This is not yet supported in the reference client.
*   An API was added to get an estimate of the fee for a transaction.
*   An API was added to get the estimated total for a transaction.
*   Accepted currency was added to the moderator information.
*   The listing format was updated to return an object instead of an array.
*   Endpoints were added to get the avatar and header of a user via their peerID.

[![Wallet in Version 2.0.3 of OpenBazaar](Wallet-in-Version-2.0.3.png)](https://blog.openbazaar.org/wp-content/uploads/2017/04/Wallet-in-Version-2.0.3.png)

**Front End:**

*   Search has been added to the reference client. It defaults to use the OB1 search service (this can be changed in the user’s settings).
*   The wallet can now send and receive funds. **Make sure to set your node to use the testnet if you use the wallet.**
*   The wallet will show a list of your transactions now.
*   Various bugs were fixed.

* * *

**Are you a developer who wants to get involved in this early stage of Version 2.0 development?**  
_Get the details [here](https://blog.openbazaar.org/milestone-1-developer-release-for-openbazaar-2-0/#.WJuWRxIrLOR)!_

**Want to start RIGHT NOW buying and selling with Bitcoin or other altcoins using Version 1.0?**  
_[Download OpenBazaar](http://openbazaar.org/)_