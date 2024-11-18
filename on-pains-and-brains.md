---
title: On pains and brains
date: 2016-01-01
slug: on-pains-and-brains
---

A while back, I wrote a post on <a href="why-your-software-should-cry.md">why software should feel pain</a>. Since then, I've had that lesson reinforced in my mind, and I've also understood some nuances that weren't obvious to me before, so I'm revisiting the topic.

<strong>The Reinforcer</strong>

What brought this topic back to my mind was a root cause analysis I did to diagnose a recent system failure. I'll spare you the gory details, but here's what happened in a nutshell: a daemon got bad data files and began behaving strangely as a result. The replication process for its data files had been impaired because the app producing the data files finished much later than normal. That app in turn was impacted by anomalous network brownouts which began with a partly damaged network cable.

<strong>The Obvious but Naive Lesson</strong>

The final step in my root cause analysis was to make recommendations, and I was quick to offer some: the daemon should double-check the integrity of its data file; the originating app should monitor its timing and complain about anomalies.

The more I thought about it, however, the more unhappy I became. Surely, such monitoring is a good idea. So why did I <em>not</em> believe my recommendations would really make things better?

[caption id="attachment_6224" align="aligncenter" width="418"]<img class=" size-full wp-image-6224 aligncenter" src="https://codecraft.co/wp-content/uploads/2016/01/descartes-reflex.jpeg" alt="Descartes-reflex" width="418" height="442" /> The pain pathway is more than nerves in the toes; it runs all the way back to the brain. From René Descartes's <em>Treatise of Man</em>. (Wikimedia Commons)[/caption]

<!--more-->Eventually, a light went on: the <em>real</em> root cause wasn't just the frayed cable--it was a lack of human attention. We already had rudimentary pain signals in the form of log files and alerts, but nobody was paying attention. It was like nerves with no link back to the brain. Building better alarms was only half a solution; my recommendations needed to cover changes in the behavior of <em>people</em> to really make a difference.

<strong>The Deeper Lesson</strong>

This evolution of thinking, in which I initially focus on technical details, but <a href="why-people-are-part-of-a-software-architecture.md">the role of people in software architecture</a>, has repeated several times in my career, but I guess I needed to discover it again.

In my original post on pain sensors in software, I suggested several creative ways to apply the principle. I still think ideas like <a href="why-your-software-should-cry.md"><em>error memory, </em><em>error gestalt</em>, and <em>protective fear</em></a> are worth pondering, but I now realize that they are not going to deliver significant value unless we connect them to people.

When we diagram systems as part of architecture and design activities, we rarely include boxes for users. Even if we are UX-savvy and include "users", we almost always take the <a href="the-8th-characteristic.md">system obsolescence and death</a> that its owners should watch?

<strong>Recommendation</strong>

I propose that we add two new documents to the artifacts that we use to describe our architecture:
<ul>
	<li><strong>Health Checklist</strong>: lists key indicators of health, and troubling symptoms that ought to be watched. For example, "needs about 100Mbps of network capacity during peak business hours; 50 Mbps is problematic, and <25 Mbps is a crisis."</li>
	<li><strong>Who's Who</strong>: lists people (NOT just users) that have a role in the lifecycle of the app, and their responsibilities. For example, "App is installed by IT, who have to set up DNS and mail relay for it. IT typically won't hear anything about the app after initial config, but may receive zenoss alarms about DNS and mail relay failures. Also depends on data dumps that are uploaded at the end of each business day by accounting; accounting only sees the web upload dialog and may be out of the office on holidays."</li>
</ul>
Do you think such artifacts would be helpful? Do you have any ideas to enhance the nerve~brain connections in your software systems?