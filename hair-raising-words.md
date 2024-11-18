---
title: Hair-Raising Words
date: 2012-10-12
slug: hair-raising-words
---

My daughter just got back from touring a "haunted circus" with her friends. She reports that the clowns were terrifying. (For those who aren't living in North America, the Halloween holiday is a time when the macabre and spooky are in vogue.)

<figure><img title="scary clown" alt="" src="http://upload.wikimedia.org/wikipedia/commons/e/ea/Scary_clown.jpg" height="351" width="468" /><figcaption>Coulrophobia--the fear of clowns. Image credit: Graeme Maclean (Wikimedia Commons).</figcaption></figure>

Well, I'm a programmer; I can get chills down my spine without paying an entrance fee. All I have to do is go to a meeting where certain words get tossed around casually. Blood drains from my face; my heart starts racing; visions of apocalypse dance before my eyes.

Okay, maybe I'm exaggerating a <em>teeny</em> bit--but I <em>have</em> found a few words that have a near-magical capacity to provoke stress, worry, and miscommunication in companies that make software. Here is my short list:<!--more-->

<strong>"Integration"</strong>
<p style="padding-left:30px;">It is not crazy to think that two systems need to cooperate to provide good business value for a customer. And it <em>is</em> possible to have success doing integration work.</p>
<p style="padding-left:30px;">However.</p>
<p style="padding-left:30px;">Almost no word in the lexicon of spiky haired bosses is more strongly correlated with underestimates, surprises, and misaligned expectations than this one.</p>
<p style="padding-left:30px;">Usually someone who hasn't done a deep analysis describes the work of the integration as "just a ___" (fill in the blank with "couple of web service calls", "hyperlink or two", "joint branding effort", "documentation task", or something similar). But once you look at it more closely, you discover that the two systems don't share a common security model, which means that the simple click-and-redirect you hoped for will need to be interrupted by a login, will have a security hole, or both. Then you realize that there's an impedance mismatch around localization. Then you find that one of the apps requires admin rights to run, but the other doesn't. Then you learn that the platform support matrix is different, so the integration is only possible on half your targets. Then it becomes clear that the apps use mutually exclusive versions of the same embedded database. Then someone mentions that a new version of the other app is approaching beta, at the most inconvenient time in your schedule. Then your QA team asks for money so they can license the other app for proper testing.</p>
<p style="padding-left:30px;">Then the spiky haired boss is incredulous when you tell him it will take 6 programmers 47 months to finish.</p>
<p style="padding-left:30px;">Time spent on integration is typically not time spent on innovation at the core of what makes your product valuable and unique.</p>
<strong>"Upgrade"</strong>
<p style="padding-left:30px;">Most product evolutions begin with a core technology. Typically it is the "baby" of a visionary type who has deep knowledge of a particular problem domain.</p>
<p style="padding-left:30px;">Given time, traction, and effort, the technology evolves into a bona fide product.</p>
<p style="padding-left:30px;">About the time the second major release with meaningful customers ships, someone usually wants to talk about the upgrade experience. As with integration, this is quite rational; how else can you get a second sale out of existing customers?</p>
<p style="padding-left:30px;">But upgrades are another one of those time-and-energy sinks, if you're not careful. Especially if you were careless about install protocols in the early days, and especially if you have a lot of config/deploy possibilities, it can be almost impossible to make an upgrade seamless. This only gets worse if you have a centralized or client-server architecture, schema changes, or integration complexities.</p>
<strong>"Security"</strong>
<p style="padding-left:30px;">Another can of worms.</p>
<p style="padding-left:30px;">Security is a lot like legal advice--the most conservative strategy is the one the experts will recommend, because they know how bad things can get when you're careless.</p>
<p style="padding-left:30px;">The problem is that ultra-conservative choices about security (and legal advice) usually don't maximize business value. It's just too darn expensive to operate that way.</p>
<p style="padding-left:30px;">Security = annoyance. People don't buy most products (unless you're Symantec or McAfee) because they want to be challenged for passwords or warned about insecure behaviors; they buy it to get a job done. Security is closer to a necessary evil than it is to a product improvement.</p>
<p style="padding-left:30px;">Another insidious problem with "security" as a requirement is that it's too darn vague. Will you meet the requirements for security by using encrypted protocols and data files, by integrating with LDAP, by using cookies and DBMS logins, by reducing attack surfaces, by performing a security audit, or by one of a dozen other strategies?</p>
<p style="padding-left:30px;">Be prepared for blank stares if you ask these questions.</p>
<strong>"Compliance"</strong>
<p style="padding-left:30px;">This particular word, and its close cousin, "certification", are favorite of government agencies. They want <a class="zem_slink" title="Data loss prevention software" href="http://en.wikipedia.org/wiki/Data_loss_prevention_software" target="_blank" rel="wikipedia">HIPAA compliance</a>, <a href="http://www.section508.gov" target="_blank">508 compliance</a>, <a href="http://en.wikipedia.org/wiki/FIPS_140-2" target="_blank">FIPS certification</a>, and compliance with regulations of a hundred other stripes.</p>
<p style="padding-left:30px;">Commercial enterprises have a few of their own; <a class="zem_slink" title="Sarbanes–Oxley Act" href="http://en.wikipedia.org/wiki/Sarbanes%E2%80%93Oxley_Act" target="_blank" rel="wikipedia">Sarbanes-Oxley</a> is a favorite.</p>
<p style="padding-left:30px;">With few exceptions, getting this checkbox will have a significant one-time cost as well as an ongoing carrying cost in all future releases.</p>
<strong>"Port"</strong>
<p style="padding-left:30px;"><a class="zem_slink" title="Danger, Will Robinson" href="http://en.wikipedia.org/wiki/Danger%2C_Will_Robinson" target="_blank" rel="wikipedia">Danger, Will Robinson</a>! Taking your Windows application onto OSX and Android might seem easy; after all, you wrote it in java just so you could have portability. But often, porting is much more than just tweaking for a new compiler. You have to grow the expertise of your team, expand the scope of continuous integration, buy licenses and hardware that used to be irrelevant. You have to find workarounds for those obscure platform APIs that don't work quite the way the documentation claims--and you have to discover that you need those workarounds in the first place.</p>
<p style="padding-left:30px;">Again, porting may be the right decision, and it can certainly be successful. However, I have seen ports abandoned because the carrying cost was just too high--and the people who walked away were brilliant and dedicated folks.</p>
<p style="padding-left:30px;">Don't underestimate the initial and ongoing costs.</p>
I could list other scary words, but I think I'll refrain. The common thread in all of these words is that they sound innocuous but often turn out to be harbingers of stress and frustration.

What do you think of these words?

Do you have your own that you'd like to add to the list?
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Next time you are asked to estimate the work implied by one of these dangerous words, think about it carefully. Don't try to torpedo the idea; just explore it in a disciplined fashion. Make sure that all stakeholders have a shared understanding of scope and implications.</span></em></p>