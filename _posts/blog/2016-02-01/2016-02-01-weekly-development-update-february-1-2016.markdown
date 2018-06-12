---
title: "Weekly Development Update, February 1, 2016" 
layout: post
date: '2016-02-01 00:30:00 -0300'
---
        
### Back end

Full transaction flow working. Funds release from direct payment and from escrow.

### Front end

Handles integrated. Handles go into a temporary state until they are validated with OneName. They can be used in the address bar, and are automatically displayed there once they have been validated. Network connection type is now displayed in your settings (for troubleshooting). Users can be blocked from chat. Disputes added to the transaction UI (soon published to master). Language updates from Kirvx, tenthirtyone, and Polish added thanks to Mido. Cleaned up the design of the Transactions section. http://i.imgur.com/nSzhrkd.png Purchase flow [optimizations](https://projects.invisionapp.com/share/V65TEAMW4#/screens/131540522) (integrating the changes into the client this week). Down to a [handful](https://github.com/OpenBazaar/OpenBazaar-Client/issues/475#issuecomment-177667150) of features needed for client to be feature complete.