---
title: "OpenBazaar Beta 0.4.0 \"Portobello\" is released for Linux and OSX" 
layout: post
date: '2015-04-21 00:30:00 -0300'
---
        
_Note: This blog post is outdated. Read [this article](https://blog.openbazaar.org/three-openbazaar-code-repositories-created/) for the latest code._ The fourth OpenBazaar beta has been released, named after the famed [Portobello Road Market](http://www.portobelloroad.co.uk/history/) in London. Please note this is still a beta and for users with some level of technical expertise. This isn't a consumer ready release. Binaries will be released soon. Windows users will need to wait for binaries. You can install beta 0.4.0 on Linux or OSX using the following instructions. For a detailed overview of the 0.4 beta client, visit [this post](https://blog.openbazaar.org/detailed-overview-of-openbazaar-beta-0-4/). We've also released quick start guides, visit these links for [buyer](https://blog.openbazaar.org/buyers-guide-to-openbazaar-beta-0-4), [merchant](https://blog.openbazaar.org/merchants-guide-to-openbazaar-beta-0-4/), and [notary](https://blog.openbazaar.org/notarys-guide-to-openbazaar-beta-0-4/). This release includes a substantial number of new features and improvements. Most notable are the networking changes, which should allow better connectivity and largely eliminate the need for port forwarding. Also greatly improved is stability. Other improvements include:

*   Signing keys are now HD for increased privacy;
*   Internal messaging system for online parties to communicate;
*   Users can now select their avatars;
*   Images are now externally hosted and listings can support three images (including gifs);
*   Notaries can now offer refunds to buyer or release funds to seller;
*   Notaries can now set their fee (as a percentage) if their services are utilized;
*   The order workflow has been significantly improved;
*   Addition of simple walk-through on start up ;
*   Search improvements.

### New Installation

If you don’t have Git installed on Linux, open terminal (Ctrl+Alt+T) and type: `sudo apt-get install git` If you don’t have Git installed for OSX, download [here](http://git-scm.com/downloads) and install. Now run: `git clone https://github.com/OpenBazaar/OpenBazaar.git` Once that’s complete, change directories: `cd OpenBazaar` Run the configure with this command: `./configure.sh` Please note that as of the 0.4 beta release, the default branch will be develop instead of master. This means that beta testers will receive more frequent updates if they run 'git pull'. If you prefer to keep to the more stable releases only, then switch to the master branch by running this command: `git checkout master` To start your node: `./openbazaar start` To stop your node: `./openbazaar stop` To get help on the commands you can use with OpenBazaar: `./openbazaar help`

### Existing Users

If you've run a previous release, you need to delete your existing database: `rm db/ob.db` Run git pull: `git pull` And also run ./configure.sh again: `./configure.sh` If you find a bug, please let us know on our [Github](https://github.com/OpenBazaar/OpenBazaar/wiki/github.com/OpenBazaar/OpenBazaar/issues) or on the bug reporting thread in our [subreddit](http://www.reddit.com/r/OpenBazaar/).