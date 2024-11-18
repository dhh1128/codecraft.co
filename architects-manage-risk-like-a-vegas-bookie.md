---
title: Architects: manage risk like a Vegas bookie
date: 2013-02-21
slug: architects-manage-risk-like-a-vegas-bookie
---

In the world of cloud computing, "risk" is a big buzz word. Lots of analysts are debating how much risk is involved in using <a class="zem_slink" title="Software as a service" href="http://en.wikipedia.org/wiki/Software_as_a_service" target="_blank" rel="wikipedia">SaaS</a> offerings like Salesforce, or hosting corporate applications with a public <a class="zem_slink" title="Cloud computing" href="http://en.wikipedia.org/wiki/Cloud_computing" target="_blank" rel="wikipedia">IaaS</a> provider like Amazon's EC2. They're worried about <a title="Amazon offline, downtime costs 5 million" href="http://www.networkworld.com/news/2013/013113-amazoncom-suffers-outage-nearly-5m-266314.html" target="_blank">outages (Amazon's had several ugly ones</a>, most recently for 49 minutes in January), about security, about <a class="zem_slink" title="Regulatory compliance" href="http://en.wikipedia.org/wiki/Regulatory_compliance" target="_blank" rel="wikipedia">regulatory compliance</a>, and so forth.

[caption id="attachment_1004" align="alignright" width="300"]<a href="http://vimeo.com/1386054#at=0"><img class="size-medium wp-image-1004" alt="Werner Vogels, Amazon CTO, NextWeb 2008: "Everything fails, all the time."" src="http://codecraft.co/wp-content/uploads/2013/02/screen-shot-2013-02-21-at-9-14-21-am.png?w=300" width="300" height="217" /></a> Werner Vogels, Amazon CTO, NextWeb 2008: "Everything fails, all the time."[/caption]

These worries are well founded. However, I pointed out today on <a title="think about cloud risk in terms of diversification" href="http://www.adaptivecomputing.com/the-cloud-isnt-risky-in-the-way-you-think/" target="_blank">Adaptive Computing's blog that the question "Can I take the risk to use the cloud?" is a bit naive</a>. Sometimes you can just avoid risk altogether. In many cases, however, risk is endemic, and the smart course is to manage it.

How does risk figure in your architectural vision? You should think about it all the time. You should count it, weigh and balance alternative outcomes in ways that would impress even the gaming industry.

Here are 6 key questions to kick-start your pondering:
<ul>
	<li>Is my architecture properly accounting for risk of environmental problems such as DDOS, routing failures, brownouts, and temporary loss of an internal component? (See my article about <a title="circuit breaker -- enterprise design pattern" href="dont-forget-the-circuit-breakers.md" target="_blank">circuit breakers</a>.)</li>
	<li>When one of my components crashes, will its state be cleanly recoverable (e.g., on transaction boundaries) rather than corrupt? What data loss contract am I targeting?</li>
	<li>Will it be easy for users or admins to notice when theoretical risks I've planned for become true emergencies? How will they be notified?</li>
	<li>Is it possible to put the system in a "scabbed" state that's degraded and safe, but functional, while more extensive repairs take place?</li>
	<li>Am I assuming success too often? (<a title="Werner Vogels at NextWeb 2008: everything fails, all the time" href="http://vimeo.com/1386054#at=0" target="_blank">Werner Vogels, Amazon's CTO, is fond of saying "everything fails, all the time."</a> That's on my top 5 list of major insights to remember.)</li>
	<li>Am I diversifying intelligently, and enabling my customers to do so as well?</li>
</ul>
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Make a list of a handful of important risks from your customer's perspective. How many of them can you help with?</span></em></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://www.sys-con.com/node/2528403" target="_blank">Cloud Computing Service Models</a> (sys-con.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://cloudcomputing.sys-con.com/node/2539596" target="_blank">Cloud Compliance in IaaS Is Mainly Your Responsibility</a> (cloudcomputing.sys-con.com)</li>
	<li class="zemanta-article-ul-li"><a style="font-size:13px;line-height:19px;" href="the-enterprise-hey-aws-you-wanna-piece-of-me.md" target="_blank">AWS Needs To Figure Out Its Enterprise Plan</a><span style="color:#333333;font-size:13px;line-height:19px;"> (techcrunch.com)</span></li>
	<li class="zemanta-article-ul-li"><a href="top-5-benefits-of-effective-risk-management.md" target="_blank">Top 5 Benefits of Effective Risk Management</a> (precision-blog.com)</li>
	<li class="zemanta-article-ul-li"><a href="clouds-without-fear-the-big-bang-theory-of-cloud-sprawl.md" target="_blank">Clouds Without Fear: The Big Bang Theory of Cloud Sprawl</a> (devopsangle.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://blogs.gartner.com/chris-gaun/how-can-public-clouds-reduce-business-risk-for-users/" target="_blank">How Can Public Clouds Reduce Business Risk For Users?</a> (blogs.gartner.com)</li>
</ul>

---

Daniel Hardman (2013-02-22 11:55:25)

Anthony: Thanks so much for the pointer to the ENISA report. I downloaded a copy and ripped through it this morning. Great reading. I know stuff like this is out there, but I don't see it enough.

---

Gene Hughson (2013-02-21 10:02:03)

Risk, like complexity, is one of those things that people love to talk about removing.  You can safely remove unnecessary complexity/risk, however, just as there is inherent complexity, there's also inherent risk.  That which is inherent can't be removed, but must be managed.  Great post.

---

Daniel Hardman (2013-02-21 19:08:04)

Gene: the connection to complexity is an interesting one--both because the parallel is very strong, and because risk and complexity can be mutually reinforcing. Lots of risk can lead to compensating complexity, and lots of complexity can exacerbate risk. Thanks for pointing it out; I hadn't seen that connection quite so clearly before.

The other day I was observing that simplicity has power, but I didn't give any satisfying suggestions about how to manage it, and I think when I come back to the topic, I need to start with your observation: a lot of complexity is unavoidable. When that's the case, the rest of our job is to encapsulate/hide it, manage it predictably, make its cost apparent to the right people, etc.

---

Anthony Langsworth (2013-02-22 05:58:48)

From what I have read, we are not at the same stage of statistical modelling with IT that actuaries use for insurance. However, I would be very willing to be convinced otherwise. 

What we do have in IT is good risk checklists. For example, the European Network and Information Security Agency (ENISA) produces a very thorough list of risks for cloud computing at "http://www.enisa.europa.eu/act/rm/files/deliverables/cloud-computing-risk-assessment".

As for specific examples of non-technical controls for risks, there are things like contractual obligations and clauses in outsourcing arrangements, restrictive licensing, NDAs and background checks for developers and administrators, personnel rotation and segregation of duties. Apart from risk mitigation, there is also risk transference (e.g. insurance), avoidance (dropping a product or feature) or acceptance (deal with it when or if it happens).

---

Daniel Hardman (2013-02-21 19:01:56)

Quantifying is definitely a challenge. I know actuaries quantify all kinds of insurance risks, but I'm not aware of anybody doing work to formalize risks to business continuity in a widely accepted way. I'm sure something like that exists, but now I've realized my own ignorance and have a learning project. Thanks!

Your last line also resonates strongly for me. Lots of problems aren't best solved with technology--that's for sure. Providing support with a friendly human being instead of a recorded message comes to mind. Did you have any specific examples? This is the sort of statement that I'd love to be able to illustrate better when I teach people the principle.

Thanks for the thoughtful comments.

---

Anthony Langsworth (2013-02-21 18:33:12)

Nice post, particularly the emphasis on defensive architecture. One of the biggest challenges I have found is quantifying risks, particularly for non technical stakeholders. Humans are inherently bad judges of risk and IT is particularly difficult because it usually involves unknowns (e.g. undiscovered bugs) or third parties (e.g. outsourcers, cloud providers, hackers). I would also suggest designers and architects remember that technical solutions are not always the best solution to mitigate risk.

---

A Comedy of Carelessness | Codecraft (2013-12-09 08:35:05)

[…] that’s more like it! Plan for trouble. (It always happens, after all.) Notice the problem. Communicate it. Take steps to cope, without panicking or […]

---

Taming Side Agreements | Codecraft (2014-10-28 08:36:12)

[…] you can retrofit discipline into an Enron-like software monstrosity. Understand your risk, and manage it wisely as part of your […]