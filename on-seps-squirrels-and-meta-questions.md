---
title: On SEPs, Squirrels, and Meta Questions
date: 2012/10/23
slug: on-seps-squirrels-and-meta-questions
---

In <a class="zem_slink" title="Douglas Adams" href="http://douglasadams.com/" target="_blank" rel="homepage noopener">Douglas Adams</a>' novel, <em>Life, the Universe, and Everything</em>, a spaceship lands in the middle of a stadium of screaming fans during a cricket match, and nobody notices. The ship doesn't use a Klingon-style cloaking device to accomplish this amazing feat; instead, it is hidden by a "Somebody Else's Problem" field, which operates on the principle that if something is perceived to be somebody else's problem, the brain of onlookers will treat it as if it were invisible.

Adams was a sci-fi author, but I see applications of his metaphor in the day-to-day work of software engineering.

To one degree or another, we all exhibit <a class="zem_slink" title="Inattentional blindness" href="http://en.wikipedia.org/wiki/Inattentional_blindness" target="_blank" rel="wikipedia noopener">inattentional blindness</a> from time to time. And that can be a good thing. Being able to zero in on a particular block of code, to the exclusion of the guy sneezing or yawning in the next cube, is healthy. We don't want to be like the dogs in Pixar's <em>Up!</em>, who keep getting distracted by squirrels.

[youtube=https://youtu.be/SSUXXzN26zg]

However, truly superb engineers have a capacity to see through the cloak of somebody else's problem; they think simultaneously on multiple levels of abstraction. They tend to ask "meta questions" (judiciously) that poke at larger issues, broader contexts, or more distant time horizons. Not coincidentally, <!--more-->this <a title="Unencapsulate Yourself" href="unencapsulate-yourself.md">breaks them out of the tidy horizontal layers or vertical silos that sometimes constrain the thinking of organizations</a>.

<strong>Levels of Zen</strong>

Here's an example of what meta thinking looks like.
<p style="padding-left:30px;">Product Manager: Could you provide us with some estimates on time/effort to integrate our error messages with the Windows event log?</p>
<p style="padding-left:30px;">Engineer 1 <span style="color:#008000;">(thinking to himself)</span>: <em>I could probably code what they're asking for in a week or two. However, is this really the right way to build this feature? I think integrating with the Windows event log might break our cross-platform goal; I'll have to fork the code path when we log, so we do something different on Linux.</em> <span style="color:#008000;">(Speaking out loud...)</span> "I could probably do that in a week or two. But I think your proposed implementation has some drawbacks that ought to be considered..."</p>
This engineer thinks more broadly than the strict parameters of the question, and as a result, product management gets a much more helpful answer. Many engineers that I know think at this level, and they deserve kudos. But consider another level of talent:
<p style="padding-left:30px;">Engineer 2 <span style="color:#008000;">(thinking to herself)</span>: <em>A half-baked implementation of this feature would probably take week or two. However, is this really the right way to build this feature? It would have implications for cross-platform, and localization... Even if we do it right, it would change the way support troubleshoots. We'd have to document a different workflow. The overall cost is probably closer to a man-month. And then there are ongoing carrying costs, because Windows' security model has changed slightly in the past couple releases, and we'll have to be prepared to verify that we've got elevation of privilege right in several OS variations, across various patch levels, as we write to the log. And then there's the issue of opportunity cost; if I build this, I'm unlikely to have the bandwidth to make the first-time user experience better.</em> <span style="color:#008000;">(Speaking out loud...)</span> "The short answer is that this might cost a man-month, plus or minus a week. It will depend on a few variables. Could I ask some questions about priorities so I know how this fits into the larger picture?..."</p>
Notice that this Engineer 2 considers a broader array of implications. Notice, also, that she answers with a question rather than just asserting a viewpoint like Engineer 1. Engineer 2 doesn't necessarily take the question, as asked, as the definitive constraint on scope. But she doesn't just ask questions indiscriminately, either; she knows that's a recipe for rat holes and frustration. She selects those meta questions that test assumptions or uncover misalignments as rapidly as possible.

Engineer 2 still has things to learn, though:
<p style="padding-left:30px;">Engineer 3 <span style="color:#008000;">(has essentially the same inner dialog as Engineer 2, but adds the following)</span>: ... <em>Besides all that, I'm uncomfortable with the architectural consequences of changing our logging right now, given the fragility of the codebase... Product management has been feeling frustrated about how hard it is to troubleshoot for a long time, now. I wonder if they'd entertain a different solution to that problem, that doesn't couple us so tightly to the OS. If we could postpone the fancier work, we might make customers and professional services happier, remove the same sales inhibitors from this release, and be able to do a more thorough job once some other tech debt has been cleared away. Hmm... </em> <span style="color:#008000;">(Speaking out loud...)</span> "Could I explore some alternate ways to address the need for diagnostics, that might be cheaper and easier to reconcile to our architectural roadmap?"</p>
Notice how the scope of concerns under consideration in Engineer 3's inner dialog has grown. He's now considering multiple stakeholders and multiple time horizons. He also has enough people awareness to recognize that perception, momentum, and cooperation are important goals of the conversation. No SEPs block his vision.

Yet even Engineer 3 has room to grow. Engineer 4 is a zen master, and her answer looks like this:
<p style="padding-left:30px;">Engineer 4: <span style="color:#008000;">(speaking out loud)</span> Remember the logging notion we kicked around at lunch the other day? I did a little proof of concept, and I think we could have that done for you in a couple weeks.</p>
Wait a minute! What happened to the inner dialog?

Engineer 4 still had it--in spades. Some of it may have been subliminal, because by now, asking meta questions has become almost automatic for her. But even if it had all been conscious, we wouldn't show it here, because Engineer 4 thought about all of this days or weeks ago. To the skills of Engineer 3, our zen master has added hefty doses of foresight, pragmatism, and proactivity. She saw need coming to a head, understood that the simple answer would not be satisfactory for many reasons, and knew that it would be hard to make the right choice. Across multiple time horizons, multiple departments, and multiple lines of business, she asked herself: <em>What is the best answer for our company?</em> She encountered a few distracting squirrels as she explored her questions, but her pragmatism allowed her to ignore them. She probably identified key thought leaders and consulted them, either formally or informally, to inform and test her thinking, and to gauge feasibility. Then she asked herself: <em>How can I make that answer easier?</em> She did some research. She planted a seed with product management by discussing the problem casually. She decided that a <em>fait accompli</em> would grease the skids, and she came to the meeting thoroughly prepared.

<strong>Don't Panic!</strong>

If this all feels mind-boggling complex, remember the reminder printed in large letters on the cover of <em>The Hitchhiker's Guide to the Galaxy</em>: "Don't Panic!"

Plenty of problems don't merit deep thinking; the zen master found time for our example issue by judiciously ignoring others. Even with important issues, you don't have to think at all these levels all the time. Just being aware of broader contexts and probing them occasionally will bring great benefits to your team.

<strong>Broader Application</strong>

If you've been asking meta questions about my post, you'll no doubt agree that the SEP phenomenon, and the meta question habit, apply beyond just in software engineering. Asking big meta questions caused all sorts of adventure and hilarity in Douglas Adams' books, but there's a serious side. Consummate product managers and marketers and business executives use these principles across all industries. Great scientists and generals and statesmen and religious leaders are serial meta questioners. Great parents and great friends are as well.

You might even see a link between asking meta questions and two other virtues I've written about before--<a title="Lynn Bendixsen: Listen." href="humility.md">being humble</a>.

I'd like to hear about other connections you see. Please comment. (See how I'm posing a meta question of my own? :-) And please follow my blog so we can discuss the craft of coding together.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Do a post-mortem on a recent conversation you've had--perhaps something like the estimation example I gave above. What questions could you have asked to deliver greater value faster? Could you have anticipated the conversation and prepped for it, like our zen master?</span></em></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://www.nj.com/news/index.ssf/2012/10/nutty.html" target="_blank" rel="noopener">Nutty: Squirrel responsible for Amtrak delays along Northeast corridor</a> (nj.com)</li>
</ul>

---

Why you should be proficient in a tool like vim or emacs | Codecraft (2014-05-15 08:46:23)

[…] or emacs–if you specialize in an IDE without a text editor in your repertoire, you have gaps in your experience. An IDE makes parts of your ecosystem invisible; a text editor teaches you just how robust and […]

---

On pains and brains | Codecraft (2016-01-01 14:30:10)

[…] evolution of thinking, in which I initially focus on technical details, but come to zen only as I recognize the role of people in software architecture, has repeated several times in my […]

---

On Forests and Trees | Codecraft (2015-09-02 08:48:50)

[…] we should have, with surprise at the cause and head-scratching about how to fix it. We hadn’t generalized from one problem to a systemic weakness very […]

---

God, Evolution, Systems, and Eternity &#8211; An Eye of Faith (2018-12-07 15:49:12)

[…] I see this constantly in software. Building something complex like the Facebook ecosystem is more than just building the pieces. It involves the mustering of technical, legal, business, and cultural forces in multiple dimensions, across large spans of time. There’s incredible interplay and feedback loops. I’ve blogged about this, more than once. […]