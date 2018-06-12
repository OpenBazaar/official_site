---
title: "Launching OpenBazaar Beta 2.0" 
layout: post
date: '2014-09-30 00:30:00 -0300'
---
        
_Note: This blog post is outdated. Read [this article](https://blog.openbazaar.org/three-openbazaar-code-repositories-created/) for the latest code._ Today we're launching OpenBazaar [beta 2.0](https://github.com/OpenBazaar/OpenBazaar), with the following changes:

*   Multiple bug fixes.
*   New feature: "Add Node" by entering Store GUID.
*   New feature: Shutdown from within the web client. (Settings > Advanced)
*   New feature: Web port is now randomized by default.
*   New feature: Automatically opens preferred web browser by default on start.
*   UX-Upgrade: stores on home page are now scrollable.
*   Tests converted to formal unit tests, travis integration.
*   Code reorganization, normalization, cleanup, refactors.
*   Debian binary now lintian error and warning free.
*   Compatibility and stability improvements in configure.sh
*   Search improvements

The instruction installations are the same as 1.0, which you can read [here](Screenshot-from-2014-09-30-142335.png). Please note that we have dropped support of Python 2.6 in this release. For more information on the current state of the code, read Brian's [State of the Code](https://blog.openbazaar.org/openbazaar-state-of-the-code-september-2014) for September 2014. We've had a huge increase in community participation since our 1.0 launch last month. Since OpenBazaar launched at the end of April this year, we've had over 700 issues opened and pull requests (new code) submitted. More than _400 of the 700_ have come in the last month alone, from 40 different contributors. We also passed 600 stars on Github. You can check out [more stats](https://github.com/OpenBazaar/OpenBazaar/pulse/monthly) on our Github page. [![Github stats](https://blog.openbazaar.org/wp-content/uploads/2014/09/Screenshot-from-2014-09-30-142335.png)](https://blog.openbazaar.org/wp-content/uploads/2014/09/Screenshot-from-2014-09-30-142335.png)