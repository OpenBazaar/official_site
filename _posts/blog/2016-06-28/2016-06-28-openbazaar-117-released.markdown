---
title: "OpenBazaar 1.1.7 released" 
layout: post
date: '2016-06-28 00:30:00 -0300'
---
        
OpenBazaar version 1.1.7 has been released. Installers can be downloaded [here](https://openbazaar.org/) and the full release notes are available [here](https://github.com/OpenBazaar/OpenBazaar-Installer/releases/tag/v1.1.7).

Changes
-------

Transactions that have updates to their status that need attention now have an indicator bar and are moved to the top of the transactions list. This allows users to quickly see which transactions need attention. [![unreadtransactions](unreadtransactions.png)](unreadtransactions.png)  

### Image fixes

Image scaling on the user page was fixed. The bug that removed images from the about section on the user page was fixed.

### Improved internationalization

More areas of the app that were not translatable, such as dates, are now translatable. Default text on drop downs is now translatable. Additionally, the columns have max-widths to prevent long single words from forcing them to be too wide. When a product has worldwide shipping, the confusing international shipping text will no longer appear below it. An issue with the international formatting of Bitcoin prices defaulting to 2 decimal places was fixed, now Bitcoin prices will always show 8 decimal places, with trailing zeroes truncated.

### Bug fixes and other changes

*   multiple bugs were fixed in the transactions view. Sorting will work much better now.
*   the dotted line around the user page now appears correctly and is sized right when customizing the user page.
*   fixed the notifactions badge sometimes showing a negative number.
*   the Libbitcoin not connected message text was changed to be more clear.
*   a bug where the wrong tab would load in Settings after saving was fixed.
*   the settings page no longer caches, to prevent stale data when changes are made from the user page.
*   the My Page link in the top right navigation always goes to the user's page now.
*   wallets are randomized, and CoinKite was removed
*   images in the about section will no longer be set to 100% wide. Images instead have a maximum width of 100%.
*   when your own page is NSFW, and your account is set to block NSFW content, your own page will no longer be blocked.
*   the minimum Bitcoin price has been reduced to 0.0002 from 0.002.
*   the buyer guid is shown in the summary tab of the case in the transaction page transaction modal.

Special thanks to everyone that contributed to translations on Transifex ([https://www.transifex.com/ob1/openbazaar](https://www.transifex.com/ob1/openbazaar)).

Hashes
------

**openbazaar\_1.1.7\_i386.deb** 4a58b061a8d3da12de1b7b353a80b5459fdc389ddff3a5491f67d2801cd97cde **openbazaar\_1.1.7\_amd64.deb** 8f9aa15411305271bd588af12f5cd7a8c25ea35029bdbbaf35620830c44c7e42 **OpenBazaar-1.1.7\_Setup\_x64.exe** e9f74dec0333ffb97c245ca1fe3bf13098f78d926fbdb109d74e523a94c5f644 **OpenBazaar-1.1.7\_Setup\_i386.exe** 5370d29154b24f19f0fe012fad2a8d196cac4175b32ab5d2898fe9737a07a1a7 **OpenBazaar-1.1.7.dmg** 790c5303a42fe055f3d4b2cd5af6246ec06ee23395ca001b5365962b63abfd05