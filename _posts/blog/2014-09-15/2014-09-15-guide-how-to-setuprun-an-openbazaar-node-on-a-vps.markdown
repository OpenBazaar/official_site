---
title: "Guide - How to Setup/Run an OpenBazaar Node on a VPS" 
layout: post
date: '2014-09-15 00:30:00 -0300'
---
        
_Note: This blog post is outdated. Read [this article](https://blog.openbazaar.org/three-openbazaar-code-repositories-created/) for the latest code._ If you want to test out _OpenBazaar_, but don't want to install it (or can't) on your own computer, you can rent a Virtual Private Server (VPS) instead. If you already have a VPS, you can run the [OpenBazaar installation](https://blog.openbazaar.org/openbazaar-beta-1-0-tutorial/) and then skip to [this section.](#ssh) There are many different VPS services available, and they typically provide the same services. One of the more popular is [Digital Ocean](https://www.digitalocean.com/). You can sign up and start running a VPS with their service easily, or shop around and choose another service. You can choose how large you want the space to be. _OpenBazaar_ and it's dependencies are around 5 GB, so we recommend 7 GBs or more. You don't need large amounts of RAM or anything fancy. These types of installs are typically inexpensive, $5 or $10 a month. You can then choose your OS. I recommend Ubuntu, either 12 or 14 should be fine. Once you've rented a VPS, chosen and installed your OS, you should receive instructions on how to ssh into your machine, or some VPS allow you to access the terminal via web interface. Either way, you can now install _OpenBazaar_ by following [these instructions](https://blog.openbazaar.org/openbazaar-beta-1-0-tutorial/). One tip: it can sometimes take a long time to generate a key pair. If you run this command first, it will speed up that process considerably: `sudo apt-get install haveged`

### Configuring Your SSH Client

For your desktop or laptop, I recommend using [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/ "Putty"). vSSH is the clear winner for [iPhone](Putty-02.png) or [Android](Putty-02.png); please purchase the full featured app to support the devs for making an excellent application. The configuration is somewhat similar for PuTTY and vSSH. Firstly, add in the host IP address of your VPS (remember to save your configuration once your done to save time): [![Putty 01](Putty-02.png)](Putty-02.png) Depending on how you configured your VPS above, you may have a password or private key for authenticating your session. If you have a ppk (like me), select the file's location on laptop or mobile device (this may be more difficult with iOS as it lacks any sort of accessible file system, so you may be better off going with a password): [![Putty 02](Putty-02.png)](Putty-02.png) Setup your port forwarding so that port 8888 from your VPS is forwarded to your localhost port 8888.

*   Your **source port** is '8888' and **source IP** is 127.0.0.1
*   Your **destination port** is '8888' and **destination IP** is 127.0.0.1
*   Type = Local

[![Putty 03](Putty-04.png)](Putty-04.png) In PuTTY, the end result should look like this: [![Putty 04](Putty-04.png)](Putty-04.png)

Running Your Node
-----------------

Assuming you have configured your VPS and SSH client correctly, all you have to do is start a session with your VPS and navigate to your OpenBazaar folder to run the node [as instructed](https://blog.openbazaar.org/openbazaar-beta-1-0-tutorial/ "Beta Tutorial"). The best way to do that is to run your node with UPnP disabled and forcing the node to use port 8888 (doesn't have to be port 8888, you can select any port number you want... just make sure your SSH client is forwarding the right port to your local host). This can be achieved through the following command: `./openbazaar -q 8888 --disable-open-browser start` **Recommended:** Your node will go down the moment you disconnect your SSH session. To keep running your _OpenBazaar_ node after your session has ended, enter the following command to run your node (instead of above): `$ nohup ./openbazaar -q 8888 --disable-open-browser start &` Open up your browser and enter the following address to access your OB node: `127.0.0.1:8888` This works surprisingly well on mobile devices using vSSH and is a testament to how powerful _OpenBazaar_ can become in the future!