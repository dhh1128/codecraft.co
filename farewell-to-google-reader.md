---
title: Farewell to Google Reader
date: 2013-03-14
slug: farewell-to-google-reader
redirect_from:
  - /2013/03/14/farewell-to-google-reader
comments:
  - author: Jesse Harris
    date: 2013-03-14 17:58:50
    comment: |
      I'm investigating options such as Tiny Tiny RSS and Fever since I can install them on my server and basically use them forever. We all need to take more control of our software that way.
  - author: Daniel Hardman
    date: 2013-03-14 21:52:24
    comment: |
      Let me know how you like those options. Seems like a good way to go, if you have a server where installing arbitrary packages is possible.
  - author: Jesse Harris
    date: 2013-03-17 23:19:51
    comment: |
      I've tried out Tiny Tiny RSS and Fever. The former is a pretty faithful recreation of the Google Reader interface (provided it is setup correctly), but I'd have to write some plugins to get all of the sharing options I want. I can understand not having something for HootSuite, but nothing for Facebook? That's just weird. And Google Reader would let you easily setup your own sharing links.
      
      Fever is an interested approach to RSS. You classify feeds into "kindling" and "sparks". The sparks are feeds with a low signal-to-noise that helps bump other posts higher on the food chain. You can then use a "hot" view to show you a summary of the items that are getting the most buzz. If you're a news junkie, this is a great way to follow what's going on without reading 50 different takes on the same story.
      
      One problem with both solutions is that they update feeds with a cron job. I've gotten spoiled by Google's scale that updates feeds almost instantly. I guess that's a required trade-off. I still need to try out the self-install version of NewsBlur to see if it offers anything distinctive.
  - author: Daniel Hardman
    date: 2013-03-18 06:59:43
    comment: |
      Really good info, Jesse. Fever sounds kind of intriguing. I assume both packages just install by calling yum/apt-get or the equivalent package mgr? Are they hard to configure?
  - author: Jesse Harris
    date: 2013-03-18 09:07:25
    comment: |
      I downloaded Tiny Tiny RSS directly, but it's possible it could be in a repository. It doesn't have an installer, so there's a few manual steps. It's about as easy as decompress, run the DB install script for MySQL or Postgres, and either setup the cron job or run the PHP daemon script in a screen session. You shouldn't have any issues with it, but Joe User sure wouldn't. (Fun note: it supports self-registration and multiple users, so you can host an instance for your friends.)
      
      Fever is a paid app, but it's just $30. You upload the installer, it verifies compatibility, then completes the install once you buy a key. Even if I don't use it long-term, it was worth $30 to give it a spin. Heck, it might be a good supplemental reader for when I get busy and just need to see the biggest news items.
---
If you've been following blogs with Google Reader, you were probably unhappy with Google's recent decision to kill it.

<strong>Observation</strong>: this is a great illustration of the <a title="The 8th Characteristic" href="the-8th-characteristic.md">phenomenon of software death</a> that I wrote about a few months ago.

<strong>Suggestion 1</strong>: If you're following my blog in Google Reader, click on the "Follow" button at the top of the right sidebar so you can follow this blog by email. I need your email address more than your launch coordinates. ;-)

<figure><img src="http://imgs.xkcd.com/comics/the_important_field.png" width="500" height="217" /><figcaption>image credit: xkcd.com</figcaption></figure>

<strong>Suggestion 2</strong>: For any other sites you're following in Google Reader, look for an email subscription link as a replacement. Or use <a href="http://blogtrottr.com/" target="_blank">blogtrottr</a> to scan RSS feeds and email you updates at whatever frequency you prefer. Or check out <a href="http://marketingland.com/12-google-reader-alternatives-36158" target="_blank">feedly, taptu, and other reader alternatives</a>.
