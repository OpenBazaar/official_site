---
title: "Weekly Development Update, January 19, 2016" 
layout: post
date: '2016-01-19 00:30:00 -0300'
---
        
### Back end

We now use p2p relaying for hole punching and symmetric nats instead of relying on a server for it. Various bug fixes and API improvements. Windows Installers are updated and we're working on incorporating the Squirrel auto-updater into the installers.

### Front end

Transaction flow is getting close to completion. Buyers can pay for unfunded purchases and complete confirmed purchases and leave ratings, and vendors can confirm funded purchases and send information on shipping and URLs and passwords for digital items (This is not yet available on the master branch). Search has been added to user pages in the items, followers, and following tabs. You can click on categories in the store breadcrumbs to filter items. Tabbing in the onboarding section was improved by volunteer contributor Nissim Karpenstein. Timezone preselecting in onboarding was added by volunteer contributor Taku. Language updates from volunteer contributors Squirrel2020 and Kirvx. Built in design elements to block nodes in the UI (both in discover and chat). http://i.imgur.com/GNq6uht.png Added edit/delete actions to your store page. http://i.imgur.com/aC66kvP.png Added a markdown editor for both the about section on your page and the descriptions on your listings. http://i.imgur.com/9x9NthH.png http://i.imgur.com/LxbloKk.png Added edit buttons to your about page for the social media accounts, about section and avatar that display on hover. http://i.imgur.com/U9zczHR.png