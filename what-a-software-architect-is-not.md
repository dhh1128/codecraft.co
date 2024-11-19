---
title: What a Software Architect is NOT
date: 2012-06-26
slug: what-a-software-architect-is-not
redirect_from:
  - /2012/06/26/what-a-software-architect-is-not
comments:
  - author: What is a &#8220;Software Architect?&#8221; &laquo; Software, Wetware, Webware
    date: 2012-06-26 08:58:53
    comment: |
      [...] also might be worth highlighting some things that I *don’t* consider part of an architect’s job, for the sake of clarity. I’ll do that in a separate post. Like this:LikeBe the first to like [...]
---
In <a href="what-is-a-software-architect.md">another post</a>, I defined the role of a software architect. This post points out some duties that are not necessarily part of his or her job, for clarity.

<figure><img class="  " title="An architect is not a lead engineer or a foreman..." src="http://farm4.staticflickr.com/3567/3770093556_30c3c38029_n_d.jpg" alt="foreman" width="240" height="320" align="right" /><figcaption>A foreman--vital but usually not the same person as the architect. Photo credit: USFS Region 5 (Flickr).</figcaption></figure>

* An architect is not necessarily a lead engineer. Lead engineers translate architectural guidelines and vision into implementation, not just in the design phase, but all the way through RTM. Lead engineers work for dev managers and are accountable directly to them. Lead engineers might have a technical director pay grade, but whether they are asked to function as architects is a separate question. When lead engineers push back, it's usually about whether an implementation works or is reasonable, not about whether a vision is the right one. Lead engineers may "own" a particular facet of the technology portfolio through multiple release cycles, and this cross-release perspective is architect-like. However, lead engineers are far less likely to radically question the value of what they own than an architect, because an architect is looking at a bigger picture over a longer horizon. When Bill Gates told every MS employee to drop what they were doing and spend a month thinking about the Internet because the company wasn't "getting it," he was being an architect. The lead engineers on all the projects and components that ultimately got ditched so MS could go chase the web wave would never have done that.

* An architect is not a dev manager or dev director. Dev management coordinates the work of a team that delivers product to spec. Dev management scopes work and speaks with authority on whether something is doable with what schedule and what resources. Dev management is extremely focused on release cycles. If we were constructing buildings, dev managers would be foremen -- reading blueprints, hiring and monitoring subcontractors, cutting checks, giving status reports. A dev director or Sr. Dev Director would be the general contractor. But neither the general contractor nor the foremen would decide to put an elevator shaft in a different spot without talking to the architect who calculated the load-bearing capacity of the walls. Like lead engineers, dev management should understand technical guidelines provided by an architect, and should be accountable to work within them, pushing back to the architect as necessary. This is parallel and analogous to the push-back that dev management provides to PM when the schedule is threatened.

* An architect is not a product manager. A product manager proxies customers and builds business plans for releases of products. A product manager says with authority, "This is what the market wants, and we can make X selling it." These business plans should represent our best understanding of revenue-maximizing choices. But without an architect to provide feedback, these plans typically have a one-release horizon -- whatever maximizes revenue in the next release is assumed to be best. Or else we have a long-term business perspective, but implementers receive little guidance about technical tradeoffs that are aligned with an appropriate evolutionary path; the technology becomes a patchwork quilt of kludges and dead-ends that is progressively more expensive to enhance and less useful as a competitive weapon.
