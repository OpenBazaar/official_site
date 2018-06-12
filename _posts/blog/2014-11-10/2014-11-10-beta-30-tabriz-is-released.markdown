---
title: "Beta 3.0 \"Tabriz\" is released" 
layout: post
date: '2014-11-10 00:30:00 -0300'
---
        
_Note: This blog post is outdated. Read [this article](https://blog.openbazaar.org/three-openbazaar-code-repositories-created/) for the latest code._ The third OpenBazaar beta release is now available. With this release, we're starting the tradition of naming our releases after great bazaars from all around the world, with the first being [Tabriz](http://en.wikipedia.org/wiki/Bazaar_of_Tabriz), a market in Iran which is one of the oldest bazaars in the Middle East. Tabriz represents a significant amount of work for our developers, with more than 350 commits, and merging more than 70 pull requests from the community. We thank everyone who contributed. One of the major improvements in Tabriz is the ability to run on Windows. If you'd like to become a [beta tester](https://blog.openbazaar.org/openbazaar-beta-1-0-tutorial/), download the [Windows binary](https://openbazaar.org/downloads/openbazaar-beta-3.0.zip) \[[signature here](https://openbazaar.org/downloads/openbazaar-beta-3.0.zip.sig)\], unzip the file and run the OpenBazaar.exe file. In case our site goes down, you can get a [torrent](https://openbazaar.org/downloads/openbazaar-beta-3.0.zip.torrent) with this [magnet link](magnet:?xt=urn:btih:282b503223bb9150aeb47a301d78cbd42c5ea764&dn=openbazaar-beta-3.0.zip&tr=dht%3a%2f%2f239E0DA5815B578C96EF9E65ED461A06B5357BF6.dht%2fannounce&ws=https%3a%2f%2fopenbazaar.org%2fdownloads%2fopenbazaar-beta-3.0.zip). For a full list of changes in Tabriz, check out [the changelog](https://github.com/OpenBazaar/OpenBazaar/releases/tag/v0.3.0).

Testing
-------

If you want to become a [beta tester](https://blog.openbazaar.org/openbazaar-beta-1-0-tutorial/) and are running on Mac or Linux, follow these instructions in your terminal:

> If you don’t have Git installed on Linux, open terminal (Ctrl+Alt+T) and type: `sudo apt-get install git` If you don’t have Git installed for OSX, download [here](http://git-scm.com/downloads) and install. Now run: `git clone https://github.com/OpenBazaar/OpenBazaar.git` Once that’s complete, change directories: `cd OpenBazaar` Run the configure with this command: `./configure.sh`

If you've already been running OpenBazaar, you need to update the code. In terminal, run the following commands: `git pull` `./configure.sh` To start your node: `./openbazaar start` To stop your node: `./openbazaar stop` To get help on the commands you can use with OpenBazaar: `./openbazaar help` If you find a bug, please let us know on our [Github](https://github.com/OpenBazaar/OpenBazaar/wiki/github.com/OpenBazaar/OpenBazaar/issues) or on the bug reporting thread in our [subreddit](http://www.reddit.com/r/OpenBazaar/).