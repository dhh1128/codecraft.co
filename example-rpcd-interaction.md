---
title: Example RPCD Interaction
date: 2012/06/21
slug: example-rpcd-interaction
---

In my <a href="role-play-centered-design.md">last post on RPCD</a>, I explained its key tenets. In this one, I'll imagine one way to put it into practice.

Suppose a team is chartered to build a tool that locates birth mothers of adopted children. The team's received some vague marching orders ("make it as easy as possible; we want to sell this as a service on facebook and the iTunes app store"). Maybe they're using "agile" methods or even full-blown XP to guarantee that the customer's viewpoint is represented, and that small units of work are fully processed into releasable systems on a regular basis. Or maybe they're doing traditional waterfall, with an elaborate design phase followed by a long implementation.

Regardless, adding RPCD to this team's behaviors might result in interactions like the following:

<strong>Step 1. Team discusses charter.</strong> They frame the charter in terms of a concrete use case. Since they don't have a specific "real-life" customer to talk to, they postulate one. It might look like this:
<p style="padding-left:30px;">Rafael just turned 18. He knows he was adopted, and he wants to find his birth mother. He knows he was born in Portland, OR on Sep 3, 1993, that his birth mother's name was "Cindy" or "Cynthia", and that his birth mother might have been a twin. He will interact with this product via an app on Facebook.</p>
<strong>Step 2. Team imagines how the problem would be solved with people only</strong>, assuming that money and time is no object, and that a "white gloves" treatment is the goal. This analysis helps crystallize roles for later role play. For example:
<p style="padding-left:30px;">Rafael (role = client) requests the services of a "birthmother locator" firm. The firm immediately sends an intake interviewer, Summer (role = liason) to Rafael's home. Summer records all of Rafael's contact info so she can interact with him in the future, clarifies Rafael's goals, and records all information Rafael can contribute. Summer then returns to the office and arranges for Jenny (role = case mgr) to convene a group to work on Rafael's case. The group consists of Summer and Jenny, plus Oscar (role = researcher) and Mike (role = gopher). Oscar and Mike are to begin work immediately and to report back on a daily basis. After two days, Oscar has identified 62 women whose life facts might overlap with what is known about Rafael's birth mother. Summer contacts Rafael to report status and ask a follow-up question: does Rafael know whether his birth mother was athletic? Rafael says yes, he thinks she might have been a swimmer. Based on Rafael's confidence in this new info, Oscar decides to narrows the search to women who appeared in high school yearbooks within +/- 5 years of 1993 and who were involved in sports. He dispatches Mike to get some HS yearbooks. He also looks in yearbooks for any girls who have a peer in the same grade, with the same last name. After three more days, Oscar has narrowed the list of candidates to two. He reports back to Summer and Jenny. Summer presents the list of candidates to Rafael and asks if he'd like them to contact the women. Rafael says no; he'll do the final part himself. Rafael is delighted with the results and the "white gloves" treatment, and happily pays for services rendered. Summer asks him to be a reference customer, and he agrees. In fact, Rafael is so happy he can't wait to tell all of his friends about the cool service.</p>
<strong>Step 3. Team builds a diagram of the system</strong>, using boxes for the roles that people play. The draft a "job description" for each role.

<strong>Step 4. Team assigns roles to team members</strong>. "Fred, you're going to pretend the client. Sally, you get to be the liason..."

<strong>Step 5. The system is deployed and goes live -- in "role play" mode.</strong>
<p style="padding-left:30px;">Yes, you read right. After some very early design work that can probably complete in an hour or so, the system goes into "production". Not in its final form. Not with ultra-high standards. But in a form that allows the team to learn and refine through repeated role plays. These role plays vett the roles and the model that the team has postulated.</p>
<p style="padding-left:30px;">Role play #1 is a walk-through of exactly the scenario that the team just imagined. Fred (playing Rafael) walks to a computer, pretends to be using an app on Facebook, and says "Okay, I'm now pressing enter to submit my request." Then Sally (playing Summer) looks at a computer screen and says, "Oh, I see that we have a new potential client. I'll go visit him." Already, some interesting questions should be coming to the team's mind: <em>Will clients be happy to be contacted by the app/service as soon as a liason like Summer is available? If so, what info should the "request help" form require so the client can be contacted? Or could a wizard automate Summer's job? How about a chat with an online representative? Do different clients need different priorities, so that if Summer is busy when a new request arrives, she knows whether to be interrupted? Does a case manager like Jenny have to assign Summer before Summer will pay attention? </em>The team works through these questions and continues with role play #1. Lots more questions come up as they get to the work of the researcher and the gopher. <em>What resources will researchers have? What is the latency of getting info from those resources? How much will it cost to access those resources? Who bills the customer for expenses, and what accounting procedure must be followed? Should researchers report breakthroughs as they occur, or only once a day?</em></p>
<p style="padding-left:30px;">After the team works through the role play #1, it should have some intuition about which parts of the system are going to be easiest to automate. It should also have a long and ever-growing list of questions. Not all of the questions are of equal value. The team should look for ones that have major ramifications on the user experience and the scope of work, and explore those first.</p>
<p style="padding-left:30px;">Exploration takes the form of additional role plays. Since Fred was assigned the role of Rafael, his job is critical. He gets to introduce variation into the system. He shouldn't go hog-wild all at once ("Can you bring me a pizza with your next status report?"). But he might do something like try to call his liason after a pretend hour has elapsed, to find out if any status report is available. <em>That</em> should cause the team some debate and head-scratching. :-) What if he asks to be notified by text in the middle of the night, no matter the hour, with new developments?</p>
<strong>Step 6. Boundaries between automated and human components of the system are clarified</strong>. More traditional design work begins.

<strong>Step 7. The team returns to role plays whenever additional clarity is needed</strong>.

<strong>Step 8. When "the system" is delivered, it is always done as both code AND people</strong>. This means at the end of an iteration, for example, you don't just provide a build with no bugs. You provide a role play of the system. This role play is more than a canned demo; it is an interactive demo, with people filling roles that code is not yet mature enough to handle. By viewing delivery of a "system" as delivery of a code+people ecosystem, the team is forced to consider things like how tech support will be staffed, how help will be delivered, and so forth.

---

Role-Play Centered Design &laquo; Software, Wetware, Webware (2012-06-21 08:56:40)

[...] my next post, I’ll give an example about how RPCD works. Like this:LikeOne blogger likes [...]

---

Long-Term Benefits of RPCD &laquo; Software, Wetware, Webware (2012-06-21 10:24:30)

[...] for designing software that has role-playing at it’s heart. If you take a look at the example RPCD interaction, I think some benefits will be immediately [...]

---

Why you should use an IDE instead of vim or emacs | Codecraft (2014-05-13 10:16:16)

[…] model people and their behaviors […]