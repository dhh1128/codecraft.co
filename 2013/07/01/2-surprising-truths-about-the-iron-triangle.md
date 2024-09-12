---
title: 2 Surprising Truths About The Iron Triangle
date: 2013/07/01
slug: 2-surprising-truths-about-the-iron-triangle
---

Project management 101 teaches that, when managing outcomes, you cannot alter scope, schedule, or cost (resources) without affecting at least one of the other dimensions. This interrelationship is known colloquially as the "Iron Triangle." Sometimes we put "quality" in the middle to show how it is unavoidably shaped by choices on the other constraints:

[caption id="" align="aligncenter" width="429"]<a href="http://en.wikipedia.org/wiki/Project_triangle"><img class=" " alt="" src="http://upload.wikimedia.org/wikipedia/commons/a/a6/The_triad_constraints.jpg" width="429" height="313" /></a> Image credit: John M. Kennedy T (Wikimedia Commons)[/caption]

Lots of Dilbert cartoons derive their humor from the unwillingness of the Pointy Haired Boss (PHB) to acknowledge this relationship. These cartoons are funny because they are so eerily similar to conversations we've all had, where someone wants us to deliver ultra-high quality, on a limited budget, in an aggressive timeframe, with a boatload of features.

It ain't gonna happen, folks. We engineers are clever, but we're not magicians. Triangles don't work that way.

You've learned some good principles when you can articulate this geometry lesson.

But there's more.

<strong>Truth 1: Scope is a trickster</strong>

Many well meaning managers and executives understand this trilemma, and they distance themselves from Dilbert's PHB by acknowledging that something has to give. "I pick scope," they'll say. "We absolutely must have the product before the summer doldrums, and we only have <em>X</em> dollars to spend, but I'm willing to sacrifice a few features."

This can give product management heartburn--feature sets sometimes hang together in ways that make slicing and dicing dangerous. An airplane that's good at takeoffs but that can't land is unlikely to be a commercial success. Good product managers will point this out, and they'll be right.

<!--more-->Can feature-cutting be done judiciously? Yes. If you're careful. But that's <em>still</em> not the whole story.

Most software projects are not building version 1.0. This means that what you're releasing at the end of the project is your new features PLUS all the old features that you already had. On mature products, the ratio of old to new features may be enormous--easily 100:1. I've worked on software that was 15 years old, had millions of lines of code in the codebase, and represented hundreds or thousands of man-years of investment. When you pull 1 or 2 features out of the next release in that kind of a codebase, how much are you really saving?

The PHB is foolishly optimistic. "We have 6 major initiatives slated for the next release, and I'm cancelling 2. We just reduced scope by 33%."

Well, sorry, Charlie. The trickster got the better of you.

<strong>Elastic quality</strong>

What usually happens in these scenarios, if engineering is not able to articulate the carrying cost of old features in a way that execs grok, is that cost and schedule remain fixed, and the scope vertex shifts much less than execs believe. Pressure is not alleviated; instead, it steadily mounts. Since all vertices are fixed, the nice straight lines that define the sides of the triangle begin to bow inward, squeezing the area available to quality. Result: an on-time, on-budget release, with the constrained feature set, but far less quality than anybody wanted. Nobody is happy.

If the execs, PMs, customers, and engineers in your orbit talk regularly about quality, but you can't seem to make headway, I predict that this phenomenon is at least partly to blame.

The problem of sacrificing quality when we meant to reduce scope is so ubiquitous that sometimes the iron triangle is formulated like this:

[caption id="" align="aligncenter" width="400"]<a href="http://en.wikipedia.org/wiki/File:Project-triangle.svg"><img class=" " alt="" src="http://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Project-triangle.svg/500px-Project-triangle.svg.png" width="400" height="393" /></a> cosmocatalano (Wikimedia Commons)[/caption]

Fast. Good. Cheap. Pick any 2.

In this world view, scope is not a lever, and the tradeoffs with quality are explicit.

If you've learned truth 1, then you're probably an <a title="Earned Pragmatism" href="http://codecraft.co/2013/01/18/earned-pragmatism/">industry veteran with battle scars</a>, and you're the kind of person I want on my team when we do project planning.

But there's more.

<strong>Truth 2: Quality vs. speed is a false dichotomy</strong>

This assertion is bound to raise some eyebrows. In fact, I nearly got in a shouting match about it with a brilliant coworker who has lots of wisdom. Think of the TV show MASH. How many times does Hawkeye lament that he can't save the lives of the wounded because he doesn't have the time to operate properly? How often do we see young soldiers die because he's too tired, or has to improvise solutions because there's no time to requisition proper equipment?

Trying to do too much, with too little, is a recipe for quality failure. No question.

But.

Flip the scenario on its head for a minute. Focus less on the quality of Hawkeye's work, and more on the quality of the <em>patients</em>. Is it faster to operate on lightly wounded soldiers who were physically healthy before their injury, or on those who are riddled with shrapnel, and went into battle with a bad heart, diabetes, kidney failure, tuberculosis, and cancer?

Now translate. Think of a codebase like a patient, and an engineer like a doctor.

Can engineers get more done in a high-quality codebase, or a low-quality one? I claim the former, <em>even if the high-quality codebase disallows kludges that look like they save time in the short run.</em>

I have personally worked in codebases that are modular, well encapsulated, thoroughly unit tested, and automated to the hilt. And I have worked in codebases that were just the opposite. There is no question where an engineer is more productive. The comparison is not even close. The speed with which you can reproduce, isolate, and fix a bug is greater in high-quality code. Adding incremental features can be orders of magnitude faster. Altering architecture to reinvent functionality is doable in such a codebase, and virtually impossible in spaghetti code.

<strong>But can we handle the truth?</strong>

Part of the reason why my colleague had strong emotion about this claim is because he'd been burned by the facile belief that you can hold quality constant (or increase it) as you push relentlessly for speed. That belief is dangerous. If a Dilbertesque PHB is told that he can have both, misery will ensue. That's not opinion--it's historical fact, as most of us can witness.

That way lies madness.

<strong>Quality yields speed</strong>

In a way, I'm suggesting the opposite strategy: if you push on quality <em>in the right way</em>, speed will accrue organically. Not at first, <em>especially</em> if you're starting with an unhealthy codebase. Not with every checkin; sometimes you have to take one step back to take two steps forward. But over time, if you continue to invest in quality, your patient will get more healthy, and you will see your speed go up, not down. The <a title="Why Mental Models Matter" href="http://codecraft.co/2012/11/05/why-mental-models-matter/">mental models</a> of your engineers and the <a title="Users Aren’t The Only People In Your Software" href="http://codecraft.co/2012/09/04/users-arent-the-only-people-in-your-software/">entire value chain</a> will align. You'll create virtuous cycles that perpetuate the right kinds of <a title="Good Code Is Balanced" href="http://codecraft.co/2012/08/27/good-code-is-balanced/">tradeoffs</a> for <a title="3 Commandments of Performance Optimization" href="http://codecraft.co/2013/01/08/3-commandments-of-performance-optimization/">performance</a>, <a title="The Scaling Fallacy" href="http://codecraft.co/2012/12/19/the-scaling-fallacy/">scalability</a>, and <a title="Good fences make good neighbors" href="http://codecraft.co/2013/05/15/good-fences-make-good-neighbors/">encapsulation</a>.

There are limits, of course. Hawkeye might be amazingly fast with mostly healthy patients, but he'll never operate on a thousand patients an hour.

Within those limits, though, it's amazing what quality can do for you.

In order to pursue this strategy, you have to get management to take their foot off the gas pedal and let you build things right. That can be a difficult (maybe even impossible) task. I'm not claiming it's easy. I'm not offering a recipe to convince them (though <a title="Roland Whatcott: Manage momentum." href="http://codecraft.co/2012/09/21/roland-whatcott-manage-momentum/">momentum</a> will probably be an ingredient). I'm just saying it's worth the effort, because there is a happy land on the other side of the rainbow where you get better and faster at the same time.

I've been there.
<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://www.codypowell.com/taods/2013/06/tragedy-of-the-common-library.html" target="_blank">Tragedy of the Common Library</a> (codypowell.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://thinkrelevance.com/blog/2013/05/21/entropy-and-evolution-of-a-codebase" target="_blank">Entropy and Evolution of a Codebase</a> (thinkrelevance.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://agile.dzone.com/articles/pair-programming-0" target="_blank">On Pair Programming</a> (agile.dzone.com)</li>
</ul>

---

dougbert (2013-07-22 13:08:15)

great insight, and codebases do have a health metric - bad or good.
We are the "doctors" who work to better that metric - or do something else when things look bad

dougbert

---

Gene Hughson (2013-07-02 10:48:36)

Dan,

Excellent analogy re: the codebase is like a doctor's patient.  One of the best reasons for managing technical debt is to avoid the situation where the patient is too fragile to withstand the surgery it needs to live.

Great post.

---

Daniel Hardman (2013-07-02 09:02:20)

Don: Thanks for a meaty response. I had not heard of KANO before, so your comments led me to some interesting study. I really like distinguishing between BASIC, STANDARD, and EXCITING. This makes explicit a set of tradeoffs that I've usually seen being managed entirely by intuition.

When are we going to see a book with all your accumulated wisdom? :-)

---

Don (2013-07-02 07:01:22)

You struck a cord :)
I have been using the iron triangle with teams for years successfully and I think it works but there are alot of misconceptions about its use in management especially as it relates to quality (Q).

In fact some agile seekers look for speed from agile and I think speed is not the main focus, cadence, velocity and value is.  Optimizing the area under the time and value curve is the management challenge.

The core idea is to deliver the most valuable payload in each increment for the capacity that the team has been given. The increments timing is based on the minimal impactful payload delivered at an estimated velocity and capacity. My experience is that in most cases it is better to deliver a small valuable payload on time than a killer payload late. My experience also is that teams are late because they do not have the capacity to perform the planned work within the time envelope when all unknows ar finially realized. That is why you start with a balanced triangle and keep it that way, sprint to sprint until you deliver. When the triangle balance is communicated transparently it allows management to participate in making critical decisions, like to add resources or to change the arrival time vs loosing function. It also drives an appreciation for what the development team is facing when unknowns arrive.

Now Quality? This has bothered me for some time in that I always assumed that Q, the center of the triangle was held constant but that seemed more thoretical than practice. The key to adding Q into the equation lies in the KANO model. It outlines NPD quality (which is different than the quality that manufacturing provides) in three dimensions BASIC-STANDARD-EXCITING.
The constant part is "BASIC" and that cannot be traded off. When you ship below BASIC, customers stop buying and talking with you. The core design process must have artifacts that get to BASIC within the iron triangle constraints. That means there is standard work on every backlog that defines BASIC Q and BASIC Q eclipses all other tradeoffs. Now it gets complex (as NPD is). The remaining two dimensions (standard and exciting) can be traded for each other. They are chosen based on the competitions function (standard) and functions that eclipse the competition (exciting). Explaining these tradeoffos would require alot of posting realestate so I will stop here. Suffice it to say that that the balance of STANDARD + EXCITING while not trading off BASIC is the key to a balanced release using the triangle.

Lastly how do you plan and communicate this balance. The secret is "DONENESS". In agile DONENESS=Q! Part of every releases plan should include identifying DONENESS. This is where BASIC and any other "you arent done until this is done" criterea is documented. When you add these to the backog of STANDARD and EXCITING tradeoffs you have the release plan and the "TOTALLY DONE" criterea. This is the intersection of NPD-Q and the triangle.

---

Gene Hughson (2013-07-03 10:14:13)

I agree...in fact, in one of my posts I've discussed platform rot (e.g. not keeping up with .Net, OS, and SQL Server versions) as an example of technical debt.  Sometimes debt is justified to reach a goal, but if it's not managed, chances are it will come back to haunt you.

---

Daniel Hardman (2013-07-02 14:56:36)

Good connection, Gene. I heard someone yesterday try to define "technical debt" primarily in terms of unimplemented features. I think that's too narrow. No matter how complete the feature matrix, you're in debt if your codebase is unhealthy.

---

donkleinschnitz (2013-07-06 07:37:27)

Sorry but I don't buy this death ...... I would also like to know what practical tool replaced it? I have witnessed the improper use of this tool and in fact the link provided to the PMI and the comments and dialog seem to prove such. For example, this is not a strategic planning tool it is a tool that is used to adjust sprint payloads based on a teams velocity as it works down a backlog. Its the only "reality check" in the agile process.

Perhaps the problem is in the missuse of this tool and that is its application as a project management tool, which it is not. This tool is used by architects, product owners and designers to make design tradeoffs based on balancing work capacity, function and time. I can't imagine how a scrum team rationally adjusts its payload without such a tool used at each increment review.

Is it the old way of just hoping that there is enough capacity or guessing what is needed to deliver some content on some optomistic date, then punishing developers when things didn't happen like project management imagined. How about we return to time carding and track every move a software developer makes to see how productive she is ...... then there is PERT planning, we could return to critical path planning and relearn that in NPD everything is new and uncertain and underfunded and changing ...... and....

I would like to see some clarity around what has replaced the triangle, in the mean time I wll continue to coach my 300 scrum teams on its use?

---

PM Hut (2013-07-05 09:13:36)

Hi Daniel,

The iron triangle has been proclaimed dead years ago. See: http://www.pmhut.com/the-death-of-the-project-management-triangle

It was killed by PMBOK 4.

---

Daniel Hardman (2013-07-05 22:44:12)

Interesting. I knew that there were many competing theories, but not that the discipline believes it is "dead." I still think it's a useful source of insight.

Thanks for the link to the blog post; very helpful.