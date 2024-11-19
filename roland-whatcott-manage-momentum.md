---
title: Roland Whatcott: Manage momentum.
date: 2012-09-21
slug: roland-whatcott-manage-momentum
redirect_from:
  - /2012/09/21/roland-whatcott-manage-momentum
comments:
  - author: Coping With Organizational Alzheimers &laquo; Codecraft
    date: 2012-10-12 11:37:24
    comment: >
      [...] big problem with most companies,” said Roland, “is that they have no institutional [...]
  - author: Kim
    date: 2012-10-19 08:08:46
    comment: >
      Daniel,
      
      Thanks for sharing. 
      
      "He went looking for momentum." - I wonder if starting on the portion of a project that seems less interesting architecturally may be more value because of the momentum it brings into the picture.
      
      Kim
  - author: Daniel
    date: 2012-10-19 11:02:17
    comment: >
      Momentum is not equally important in all circumstances, but as a general rule, I think this is a very astute observation, Kim. Part of the balance you have to strike is to be able to recognize very early (often based on battle scars and/or intuition) when focusing on architectural questions is necessary, and when getting momentum on more humdrum stuff is a bigger benefit. (These two orientations are not necessary mutually exclusive, but they *do* compete to some degree.)
  - author: Interrupting my interruptions &laquo; Codecraft
    date: 2013-01-24 11:48:47
    comment: >
      [...] I’m attending (or calling) are how I develop shared mental models, motivate and teach, manage momentum, and put a stake in the ground. Those wikipedia pages and chat sessions and interesting blog posts [...]
  - author: Smart Geeks Think Like Cheerleaders &laquo; Codecraft
    date: 2013-02-05 08:57:43
    comment: >
      [...] programming language, product schedule, or architecture–so much so that we lose momentum or [...]
---
<p style="text-align:right;"><em>(A post in my “<a href="/category/role-models/">Role Models</a>” series…)</em></p>
<p style="text-align:left;">In late 2000, I joined a small team tasked with rewriting the core technology at PowerQuest. The old codebase--despite embodying a number of patent-pending concepts, and serving as the foundation for all our revenue--was fragile, rife with technical debt, and unfriendly to localization, new platforms, and other roadmap priorities.</p>


<figure><img title="rocket engine" src="http://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Viking_5C_rocketengine.jpg/320px-Viking_5C_rocketengine.jpg" alt="" width="320" height="480" /><figcaption>Building our new engine wasn't exactly rocket science, but we expected our output to be cool and generate lots of thrust. We took our work as seriously as NASA... Photo Credit: Wikimedia Commons</figcaption></figure>
<p style="text-align:left;">This rewrite had been attempted before--more than once, by some of the brightest engineers I've ever worked with. Each time, the press of looming releases, and the lack of obvious progress, culminated in a "we'll have to come back to this later" decision.</p>
<p style="text-align:left;">Our little team was confident that This Would Not Happen To Us. We were going to build an engine that was cross-platform from the ground up. No weird dependencies, no assumptions about compiler quirks or endianness, would permeate the code. Internationalization (i18n) and localization (l10n) support would be baked in. Errors would be clearer. Modules would be small, beautiful, and loosely coupled. Gotos would disappear. Vestiges of C dialect would be replaced by best-practice STL, boost, metaprogramming, and other cutting-edge C++ ideas.</p>
<p style="text-align:left;"><strong>Experience Versus Enthusiasm</strong></p>
<p style="text-align:left;">Before I tell the rest of the story, make a prediction. Do you think we crashed and burned, muddled through, or succeeded wildly?</p>
<p style="text-align:left;">How you answer will say a lot about you.</p>
<p style="text-align:left;">If you're young and optimistic, you may expect me to tell a story with a happy ending. But if you're an industry veteran, you probably expect I'm going to tell a cautionary tale framed by failure. You know that rewriting a core technology from scratch almost never succeeds, and you can give a dozen excellent reasons why that's the case.</p>
<p style="text-align:left;">If you've got Roland Whatcott's genius, you can imagine either outcome -- and more importantly, you know how you can choose the future you want.</p>
<p style="text-align:left;"><strong><!--more-->Roland Arrives</strong></p>
<p style="text-align:left;">Fast forward a few months. A couple senior programmers had been pulled onto other assignments. They'd been back-filled, sort of, although replacements were part-time loaners, with competing priorities elsewhere. We had the working skeleton of an engine, and it could do some cool things. We could compile it for different processor architectures--or so we claimed. It had so far avoided a lot of the warts that made the old engine ugly. We had automated builds and a working unit test framework. We'd written tests for many aspects of the system. When management asked us for a demo, we'd launch our testrunner and show how everything turned green.</p>
<p style="text-align:left;">Most importantly, the new engine had its first "customer" -- an internal team was planning to build a new product on top of our codebase/API.</p>
<p style="text-align:left;">At this point, I was functioning as a technical team lead as well as an ad hoc manager. I remember attending iteration meetings for the product team that was our customer, listening to their requirements, and going back to my own team with long lists of tasks, interdependencies, and action items.</p>
<p style="text-align:left;">When I heard that a newly hired manager named Roland Whatcott would soon take over the management side of my responsibilities, I was elated. Now I could get back to my major interest, which was writing code. He'd take care of all the "other stuff."</p>
<p style="text-align:left;">Roland saw our demos, reviewed the codebase, got to know the team, went to meetings... And he became concerned. Yes, our team was making steady progress. Yes, we had been productive, by many measures. But our customer team was not happy. We were delivering what we planned in our iterations, largely on time and on target; yet the set of features ready for prime time was not yet broad enough for a complex layer of business logic, let alone a UI, to build upon. Many of the features we delivered would "work" in some sense, but with so many caveats that they didn't yet have a lot of practical value. Our "demos" were actually de-motivating to many, since they ran in debuggers or shells, quite divorced from any useful product context. And most troubling, upper management was strained to keep funding the new engine instead of building revenue-producing features on top of what already worked.</p>
<p style="text-align:left;">Roland told me he was worried. I could understand some of what bothered him, but I didn't have a lot of problem-solving vision. The smartest course seemed to be to double down and get through faster.</p>
<p style="text-align:left;">Roland believed in stretch goals, but he didn't think heroism alone would see us through. He saw clearly that our momentum was faltering toward zero.</p>
<p style="text-align:left;">This, he knew, was a serious problem.</p>
<p style="text-align:left;">Momentum matters.</p>
<p style="text-align:left;"><strong>Intervention</strong></p>
<p style="text-align:left;">Roland's response to this quandry was both astute and creative.</p>
<p style="text-align:left;">He went looking for momentum.</p>
<p style="text-align:left;">He'd heard talk about HP's need for a disk imaging product that would support its new itanium server line. Itanium was a totally unfamiliar processor architecture, with crude compiler support. The old engine didn't have a snowball's chance in Phoenix of supporting Itanium. But the new engine did. We were endian- and bitness-agnostic, right?</p>
<p style="text-align:left;">In fairly short order, we were signed up to ship a product to HP. The timetable was whirlwind short. Our mainstream product team customers were 9 months away from shipping; the HP product needed to be in customer hands in a couple months.</p>
<p style="text-align:left;">I remember complaining to Roland about the ridiculousness of this release. We'd have to hurry the development of some features that we'd been planning to mature over a much longer timeframe, and neglect capabilities that were already halfway implemented. How were we supposed to do continuous integration, if we didn't have any 64-bit itaniums to run our unit tests, and the compiler barely worked? Our automated build system would lose most of its value. And we didn't even know that the itanium release would make money; it was barely on product management's radar.</p>
<p style="text-align:left;">All of my objections were reasonable, I think. But they were irrelevant. Roland knew that without a momentum boost, our initiative would be scrapped, and we'd be right back in the old engine quagmire all over again.</p>
<p style="text-align:left;"><strong>Long Story Short</strong></p>
<p style="text-align:left;">We pulled it off. We shipped the world's first disk imaging product for itanium, on a schedule so aggressive it even made the customer's head spin. It was not easy. There was pain--for those on our team, and for the product team that was waiting for more mainstream features to mature. Kudos to lots of smart engineers, to Roland's savvy management, and to the courage and vision of upper management, who let us try.</p>
<p style="text-align:left;">We emerged with momentum. Those unit tests we'd worked so hard to create now had a track record of stabilizing the code on the shifting sand of alpha-generation compilers and alpha-generation c runtimes--to the point where the new engine was demonstrably more stable than the code it proposed to supersede. Managers talked about it. The decoupling we created with abstract factories and dependency injection had clearly kept the worst of platform differences at bay; nobody wondered anymore if we could do a Linux port. Teams wondering if they could depend on the new engine folks to come through in the clutch no longer woke up sweating in the middle of the night.</p>
<p style="text-align:left;">A few months later, the product team that had been our original internal customer shipped. Disk-based backup entered the imaging age, and "the new engine" turned into "the engine" to folks in our department.</p>
<p style="text-align:left;"><strong>The Moral</strong></p>
<p style="text-align:left;">Just because momentum is a state of mind doesn't mean it lacks real-world consequences. Make sure that ambitious undertakings have plenty of momentum all along the way. Win early and often, not just in a big bang at the end; if you wait too long, the big bang might never materialize.</p>
<p style="text-align:left;">Like all principles, this one can be misapplied. You can hype to get temporary momentum spikes; you can make too many short-term compromises for the sake of brownie points, and sabotage your future.</p>
<p style="text-align:left;">But if you do it right, momentum will carry you through some incredibly difficult challenges with flying colors.</p>
<p style="text-align:left;">Thanks for the lesson, Roland.</p>
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="text-align:left;padding-left:30px;"><em><span style="color:#000080;">Analyze the momentum for a recent or current project. What challenges to momentum do you have? How can you overcome them.</span></em></p>
