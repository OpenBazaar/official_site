---
title: "Three OpenBazaar Code Repositories Created" 
layout: post
date: '2015-08-18 00:30:00 -0300'
---
        
OpenBazaar has had a [single repository](https://github.com/OpenBazaar/OpenBazaar) since it began. Through the beta releases, users ran all the code in the single repository, which contained the networking, Bitcoin handling and user interface together. Front and back end weren't separate. Now that we are rebuilding OpenBazaar from the ground up, we've decided to take a different approach. Our new code based is split into three repositories; [OpenBazaar-Server](https://github.com/OpenBazaar/OpenBazaar-Server), [OpenBazaar-Client](https://github.com/OpenBazaar/OpenBazaar-Client), and [OpenBazaar-Installer](https://github.com/OpenBazaar/OpenBazaar-Installer). This separates our back end entirely from the client. Users will now be able to run an OpenBazaar server alone without needing the client. The client can be directed to an OpenBazaar server that isn't run locally. This also allows for new clients to be built other than the OpenBazaar reference client. This modular approach, together with the APIs, will also make mobile implementation simpler.

### OpenBazaar-Server

This repository manages the back end: The p2p networking; creation, signing and verification of the Ricardian contracts; and management of multisig Bitcoin keys. This repository is the furthest along in development and we could use review on it now, especially the networking portion.

### OpenBazaar-Client

This repository manages the front end and is the reference client for the project. It uses both a websocket and REST API to talk to the server. This repository is currently taking the client prototype and implementing it. It should be ready for basic review within the next week.

### OpenBazaar-Installer

This repository manages the installation of the other two repositories. It will support installation on Windows, OSX, and the majority of Linux distributions. Work has only just begun on the repository. We welcome users familiar with creating packages to reach out and help us build them.