---
title: Learned Helplessness, Rats, and People Power
date: 2012-11-26
slug: learned-helplessness-rats-and-people-power
redirect_from:
  - /2012/11/26/learned-helplessness-rats-and-people-power
comments:
  - author: dougbert
    date: 2012-11-26 10:40:35
    comment: |
      good model to follow.
      
      dead rat here
  - author: Daniel
    date: 2012-11-26 21:05:15
    comment: |
      Aw, c'mon, Doug! Maybe a bedraggled and waterlogged rat. You were still cracking jokes last time I saw you coding, so you must be alive and kickin'... :-)
  - author: LisaAn
    date: 2012-11-27 09:46:59
    comment: |
      I have often wondered why teams don't take the approach of grabbing a few backlog items and stuffing them in the cracks, so to speak, to chip away at the technical debt. Perhaps we are overwhelmed by the task.
  - author: Daniel
    date: 2012-11-27 10:03:20
    comment: |
      One of the more insidious consequences of always stretching to fit in "just one more feature," late in the game, is that all ability to mine nooks and crannies in the schedule is lost. We spend every last cent on new bells and whistles, instead of on cleaning the workshop. Sigh...
  - author: dougbert
    date: 2012-11-28 09:12:53
    comment: |
      alright, alright - good reality check - thanks, but I definitely felt the pattern you are describing.  We are having an issue with a grandson who is "helpless" if you will due to a parent who is a corrections officer, and this pattern applies here too.  Hope is key to working in a "tight" environment anywhere.
  - author: Trev
    date: 2012-12-05 10:10:55
    comment: |
      A professional kitchen needs to be cleaned each and every night, with an occasional deep clean where one pulls out all of the equipment and cleans everywhere. If its not done, Health and Safety will eventually come by close it all down.
      
      The suggested approach reminds me of Old Man Yu (http://ancientchinesestories.com/2009/04/04/ancient-chinese-stories-the-tale-of-old-man-yu-gong-and-the-mountain/). So, the question is how does one combine Eastern long-term thinking with the Western reliance on quarterly earnings?
  - author: Daniel
    date: 2012-12-10 13:49:50
    comment: |
      I think all of us that have been educated in Western universities need a crash course in gestalt, system thinking. And then we need regular reminders, until we understand that analysis (in the sense of its original meaning, of reducing everything to smaller units) is not the be-all, end-all outcome of serious thought.
  - author: Ian Nate
    date: 2012-12-28 23:46:03
    comment: |
      Profound and applicable. Love this post. Reminds me of Frank Abignale, Sr., played by the indubitable Christopher Walken, from "Catch Me If You Can": http://youtu.be/51lFmdChOA0
  - author: Daniel
    date: 2012-12-29 11:06:50
    comment: |
      Ian: I had not made that connection, but it is a *great* one. Thanks for pointing it out!
  - author: Earned Pragmatism &laquo; Codecraft
    date: 2013-01-18 08:53:29
    comment: |
      [...] this type of “architect” tend to be rife with tech debt, with no roadmap or process to haul the team up and out. Where there is no vision, the people [...]
---
In the 1950s, researchers at Johns Hopkins conducted some very troubling experiments. They caught wild rats and squeezed them in their hands until they stopped struggling, teaching them that nothing they did would let them escape the crushing grip of their human captors. Then they dropped the rats in a bucket of water and watched them swim.

Now, wild rats are superb swimmers. On average, rats that had not received the squeeze treatment lasted around 60 hours in the bucket before they gave up from exhaustion and allowed themselves to drown. One unsqueezed rat swam for 81 hours.

<figure><img alt="" src="http://farm1.staticflickr.com/77/203388870_598e4417bf.jpg" height="391" width="400" /><figcaption>A later rats-in-bucket experiment (not quite so brutal). Photo credit: MBK (Marjie) (Flickr).</figcaption></figure>

The average squeezed rat sank after 30 minutes.

In the 1960s and 1970s, <a class="zem_slink" title="Martin Seligman" href="http://en.wikipedia.org/wiki/Martin_Seligman" target="_blank" rel="wikipedia">Martin Seligman</a> became interested in this phenomenon--he called it "<a class="zem_slink" title="Learned helplessness" href="http://en.wikipedia.org/wiki/Learned_helplessness" target="_blank" rel="wikipedia">learned helplessness</a>"--and he was able to trigger similar "giving up" behavior in dogs and other animals. <a href="http://www.annualreviews.org/doi/abs/10.1146/annurev.me.23.020172.002203?journalCode=med" target="_blank">He theorized</a> that human depression<!--more--> is a reaction to learned helplessness in the face of emotional or mental challenges against which we repeatedly make zero headway. <a href="http://www.hsu.edu/uploadedFiles/Faculty/Academic_Forum/2000-1/2000-1afHelplessness%20and%20Spatial%20Memory%20in%20Swimming%20Rats.pdf" target="_blank">Other researchers showed</a> that not only did squeezed rats stop swimming faster, they also lost some of their spatial reasoning and memory abilities.

Hopefully, this experiment disturbs you on many levels. Even putting aside ethical questions, the implications are enough to make your skin crawl. At least one pundit has <a href="http://www.washingtonmonthly.com/archives/individual/2009_04/017869.php" target="_blank">connected the rat experiment with waterboarding at Guantanamo</a>. Probably there are interesting insights about addiction, interpersonal relationships, bullying, politics, and many other social issues to be gleaned as well.

I see interesting connections to tech debt.

<strong>Working In Debt</strong>

If you've ever worked on a truly yucky codebase--one littered with #ifdefs, massive and arcane functions, and undocumented and surprising logic; one having organizational principles known only to long-gone creators; one possessing far too few unit or regression tests; one smack dab in the middle of the strategic path of the company--then you know what it's like to be squeezed like a rat in a researcher's gloved fist.

You have to fix bugs, but every change causes you to grit your teeth and cross ayour fingers and toes, because you have no confidence that the fix won't break something else. <em>Squeeze</em>.

You know your <a title="Why Mental Models Matter" href="why-mental-models-matter.md" target="_blank">mental model</a> is incomplete--in fact, the mental model of everybody on the team is insufficient, even in the aggregate. You avoid dark corners of the codebase; here there be dragons. <em>Squeeze</em>.

You desperately want to refactor--but you know the Keepers of the Budget and Schedule™ will never consent to let you rewrite to nearly the degree that you need. And worse, you know that you really can't start this effort anyway, because the risk of destabilizing things is just too high. (Remember, you don't have enough unit or regression tests.) <em>Squeeze.</em>

In that kind of codebase, you can come to feel like every breath of creativity, every spark of excitement, every hope that you can make a difference, is being squeezed right out of you.

Although this discouraging perspective is not unfamiliar to me, I firmly believe that humans are smarter than rats.

And that matters.

<strong>The Power of Habit</strong>

I've previously written about my <a title="Tech Debt, Leverage, and Grandma’s Envelope" href="tech-debt-leverage-and-grandmas-envelope.md">Grandma paying off her mortgage</a> after many years of diligent effort. This was the harvest of a good habit, applied consistently.

With financial and tech debt, after big setbacks there is a temptation to throw up our hands. "What's the use?" we want to say. "Nothing we do will make any difference." We sympathize with the guy who, saddled with a million dollar medical expense, tells himself that living within his means is irrelevant, and goes on a shopping spree.

This is the equivalent of the squeezed rats giving up after 30 minutes in the bucket. We have to be smarter.

If you are working in a codebase with deep tech debt, you have to be disciplined about good habits. Write unit tests. Name your functions well. Make things as modular as you can. Chip away. And away. And away.

If you are saying: "That's not going to erode the big debts--at least, not fast enough to make any difference!"--then I hear you. Believe me. But:
<ul>
	<li>Being the kind of engineer who pays down tech debt as a matter of habit, instead of the kind who gives up, will make a dramatic difference to your own morale, and to the morale of your team. In other words, having good habits lets you believe.</li>
	<li>If you can inspire others on your team, you'll be surprised how tractable even large problems become.</li>
	<li>Things change. M&A, partnerships, and competitor's moves disrupt the natural evolution of codebases in surprising, and sometimes hopeful, ways.</li>
</ul>
Over the long haul, thinking about best practice, talking about it, and then doing it, day in and day out, really does pay off. As <a href="http://en.wikipedia.org/wiki/Lao_tse" target="_blank">Lao Tse</a> (supposedly) observed:
<blockquote>“Watch your thoughts; they become words. Watch your words; they become actions. Watch your actions; they become habit. Watch your habits; they become character. Watch your character; it becomes your destiny.”</blockquote>
Although I feel for every engineer struggling in a yucky codebase, I don't have much sympathy for those who use the struggle as an excuse for bad habits.

<strong>The Power of Imagination</strong>

Besides having a capacity to consciously choose our habits, human beings also surpass rats in their ability to find creative solutions to problems. Remember <a href="http://en.wikipedia.org/wiki/Kobayashi_Maru" target="_blank">Kirk and the Kobiyashi Maru</a>?

[youtube=http://youtu.be/bDg674aS-F4]

Brainstorm with like-minded engineers, and see what ideas emerge. Here are a few tried-and-true options to ponder:
<ul>
	<li>Can you (without being disingenuous) associate needed big-ticket changes with a strategically important initiative that everybody has already bought into? This would give you instant <a title="Roland Whatcott: Manage momentum." href="roland-whatcott-manage-momentum.md" target="_blank">momentum</a> to make things better.</li>
	<li>Can you subdivide the problem? "Refactor the whole stinkin' mess" is less likely to get done, but "refactor class X" might.</li>
	<li>Can you make a small change that's highly visibile and highly popular, and then spend your newly acquired political capital on a more expensive pay-off?</li>
	<li>Can you deploy a tool that makes the problem more obvious? Or better yet, a tool that solves part of the problem in an automated way? (If such a tool doesn't exist, could you write one? Or commission one?)</li>
	<li>Can you outsource a routine task to free up key resources for a frontal assault?</li>
	<li>Can you place a bounty on an improved design in open source circles?</li>
</ul>
Importantly, imagination isn't just a problem-solving tool; independent of answering the "how", it also gives us a "why" to our efforts. In the rat experiment, all the subjects saw during their time in the bucket was a metal wall, with no conceivable egress. The learned helplessness that defeated the squeezed rats was mostly a death of imagination. When Shackleton climbed into a lifeboat to attempt <a href="http://en.wikipedia.org/wiki/Voyage_of_the_James_Caird" target="_blank">the 1500 km crossing to South Georgia Island</a>, his goal was just as invisible. But he survived because he could imagine climbing out again, his journey behind him. And he kept imagining that, day after day, until his keel hit pebbles.

So...

Never underestimate the power of habit. Never underestimate the power of imagination.

And keep swimming. :-)
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="text-align:left;padding-left:30px;"><em><span style="color:#000080;">Find a good coding habit that you've neglected, and re-commit to do it with discipline and vision.</span></em></p>
