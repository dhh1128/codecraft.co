---
title: Long-Term Benefits of RPCD
date: 2012-06-21
slug: long-term-benefits-of-rpcd
redirect_from:
  - /2012/06/21/long-term-benefits-of-rpcd
---

In a <a href="example-rpcd-interaction.md">example RPCD interaction</a>, I think some benefits will immediately become apparent.

But there are subtler advantages that might not be obvious:

<strong>The system never needs to wait for functional code to be deployable.</strong>

As soon as you have a set of reasonably clear roles defined, and at least one specific use case, you can observe the system in action. Granted, you're observing people instead of software, but the full complexity and dynamism springs to life right before your eyes. People can hold clipboards and use checklists to model how wizards populate databases; they can move post-notes on a whiteboard to explore organizational algorithms. Seeing <em>in toto</em>, from the beginning, is incredibly useful.

<img src="http://farm3.staticflickr.com/2722/4439276478_8bb7a50ab8_d.jpg" alt="checklist, from http://www.flickr.com/photos/alancleaver/" />

The first deployments you do are demos. I am a big fan of demos; you should demo something at the end of every sprint or milestone, to guarantee that you've actually accomplished something useful and that it's aligned with the needs of stakeholders. But with RPCD, you take demos to a whole new level, because your demos become <em>interactive</em>. If sales asks "What happens when the user pushes the big red button?", you don't have to say, "Sorry, we can't demo that today." You walk over to the person modeling the UI, push the red button on the piece of paper or the whiteboard that they're holding, and let the system chug.

Later in the evolution of code, when most parts of the system are automated, the roles that humans still have to model give you critical information. Are these roles something that you ought to <em>permanently</em> delegate to human intelligence? Is the wizard you expected to build so complex and error-prone that online chat with a human is a better option, at least in this release? Perhaps you should hire an online chat person as a component of your system, take the risk out of the near-term release, and then study the behavior of that person intensely to learn how to automate in the next release... If your system has always used humans for cogs, adapting it in this way will be natural, not a major departure from expectations.

Another possible insight is that roles where humans are forced to continue to work represent the <em>high-value</em> aspects of the problem. Solve those problems, and customers will <em>really</em> love you, because you've radically changed their work.

<strong>The needs of <em>all</em> humans interacting with the system are inherently "baked in" and obvious, instead of being implicit.</strong>

UCD says to center your design on the user. But so often we forget support, sales, IT, executive management, and so forth. If you're writing an app for the iPad that uses social ranking to recommend shows airing in the next hour on cable channels, you probably have a team of data managers that maintains current listings for all channels, and a team of backroom IT that keeps your DB running. These people are part of the system; if one day your data center dies, and no IT people show up to fix it, or one day your channel listings goes stale and no data manager steps in to solve the problem, you don't have a product.

These people should all have roles in your role plays, and by regularly representing them, you can't help but make better decisions. Overhead and cost centers become obvious. Risks jump out at you.

<strong>The clumsiness of certain touch points becomes obvious.</strong>

Or in other words, user feedback and usability testing are built in, because actual people, not abstract boxes on your system, are interacting from the very beginning.
