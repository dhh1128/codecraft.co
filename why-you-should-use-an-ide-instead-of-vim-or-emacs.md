---
title: Why you should use an IDE instead of vim or emacs
date: 2014-05-13
slug: why-you-should-use-an-ide-instead-of-vim-or-emacs
redirect_from:
  - /2014/05/13/why-you-should-use-an-ide-instead-of-vim-or-emacs
comments:
  - author: kc5tja
    date: 2014-05-13 17:40:35
    comment: |
      It's not uncommon for me to have up to three different editors open at once on a single project (Vim, ACME, and Sublime Text 2).  Sometimes, they'll even be editing the same file.  Depending on the project, I might replace ST2 with NetBeans.
  - author: Daniel Hardman
    date: 2014-05-13 17:43:53
    comment: |
      I'm chuckling because that sounds so much like me. I often have vim running in 3 or 4 different windows, and half the time I open the same file more than once. I'll get in the middle of making mods with one tool, and then switch to another when I have some other change that's easier to do in the other window. Thank goodness all good tools warn you about changes to the file you're editing. :-)
  - author: Nitsan
    date: 2014-05-14 05:51:43
    comment: |
      Very nice read, thank you.
      But what can you do when most of your work deals with editing files on a production server, where Vim/nano are the only options you have, and you are forced to leave your beloved text-editor?
  - author: Daniel Hardman
    date: 2014-05-14 13:28:00
    comment: |
      That is an excellent question, Nitsan &mdash; and I have no doubt that you already know the correct answer. You use vim/nano. Usually, this is not the classic "software engineering" scenario where you have git, a ticketing system, scrum, and all sorts of process and complexity. But it *is* an important scenario to most of us, at one time or another.
      
      I have one other compelling reason why all of us should also learn a good text editor &mdash; not use it by preference for everything we do, but have it in our repertoire, as a useful skill. I'll discuss that in a follow-up post.
  - author: Nitsan
    date: 2014-05-15 05:47:14
    comment: |
      I believe a short video like this:
      https://www.youtube.com/watch?v=E2t2614cNAs
      can show the true power of sublime's workflow, which is easy to master, and vastly improve productivity.
      
      sublime is my tool of craft
  - author: lol internet
    date: 2015-05-10 06:06:30
    comment: |
      I use sshfs to mount remote filesystems in userspace.
  - author: Daniel Hardman
    date: 2015-05-11 10:55:56
    comment: |
      Yep, that also works, and I've done the same thing from time to time. Thanks for chiming in!
---
With a title like the one above, you may be expecting a rant from an IDE bigot. I know there are plenty of flame wars on this topic, on both sides, and if I raised your hackles (or whet your appetite), I'm sorry.

This is not that kind of post. For one thing, I don't take myself so seriously:

<figure><img src="http://imgs.xkcd.com/comics/real_programmers.png" alt="" width="740" height="406" /><figcaption>There's a keystroke for that! Image credit: xkcd.com</figcaption></figure>

What I'm hoping to do here is point out some subtleties to this debate that don't get a lot of airtime, and explain to my supercharged-text-editor friends why I work the way I do. However, I also plan to write a companion to this post, explaining why you need to learn a tool in the vim/emacs category, and I'll have plenty to say on that topic as well. Hopefully that buys me a few minutes of an open mind. :-)
<h3>From a distance</h3>
If you step back from the debate over IDEs vs. supercharged text editors, and squint to suppress the details, you'll see that most exchanges on this topic look like this:

<strong>Variant 1</strong>
<div style="padding-left:2em;"><em>IDE fan</em>: "You should use an IDE because it has cool feature X. Text editors are weak sauce!"</div>
<div style="padding-top:1em;padding-left:2em;margin-bottom:1.5em;"><em>VIM fan</em>: "You don't know what you're talking about. If I install plugin Y and edit my cfg file, I can have all the goodness you're so fond of, and a whole lot more."</div>
<strong style="margin-top:1.5em;">Variant 2</strong>
<div style="padding-left:2em;"><em>EMACS fan</em>: "IDEs are so dumb. They take all this time to load, use ridiculous amounts of memory, and force you to use a mouse. They are slow. They just get in my way. Real programmers can extract a block of code into its own separate function, generate a unit test stub, and grep the entire codebase for similar refactor candidates with a single keystroke."</div>
<div style="padding-top:1em;padding-left:2em;margin-bottom:1.5em;"><em>IDE fan</em>: "That's the 'Extract' button on my toolbar."</div>
I tend to roll my eyes at <a href="http://www.quora.com/Computer-Programming/Why-are-tools-like-Vim-and-Emacs-still-used-for-coding" target="_blank">conversational threads like these</a>, because:

<dl><dt>Those who are really proficient in one of these environments, but not the other, usually overestimate the feature disparity.</dt><dd>This cuts both ways. All you vim experts, did you know that IDE black-belts slice and dice text as quickly as you, that they compile and debug with the keyboard, and that they have very powerful macro capabilities like the ones you love? All you IDE lovers, did you know vim and emacs can do tabs and outline collapsing and go-to-declaration and cross-project refactoring? If it's a question of power, and if we're talking about what's possible rather than what's standard, then I think it's six of one, half dozen of the other.</dd><dt>The shared assumption &mdash; that feature richness is the right yardstick for comparison &mdash; is wrong.</dt><dd>Theoretical power isn't very interesting. Most of us use only 10% of what either toolset offers.</dd></dl>But more importantly...
<h3>Observation 1: It's not about you.</h3>
As I plan to discuss at length in a different post, <em style="color:#004080;">software engineering is a team sport</em>. Yet if you look at the argument templates above, you won't see much focus on teamwork.

We probably don't notice this misalignment because we assume that what's best for individual team members is best for the team as a whole. Often, this is true &mdash; but there are important counterexamples. John Stockton scored less points than he might have, because he was superb at dishing out assists to Karl Malone. Would a higher-scoring John Stockton have been better for the Utah Jazz? I think not. It was team points, not individual points, that Stockton optimized.

In programming, optimizing your own work while disregarding the habits, expectations, skills, and needs of others on your team might be a bad tradeoff. If you pick a coding standard that's vim-friendly, but half the team is using an editor that can't emulate it well, have you been smart? If your IntelliJ wizardry leaves your buddy in the dust during pair programming, have you transferred knowledge as effectively as you should? If you despise doc comments because you have no use for hover text in emacs, but half your team uses eclipse, are you playing nice? If you use a refactor wizard all the time, but it drastically bloats the diffs on a maintenance branch, are you really boosting team productivity as much as you think?

I think that this observation weakens arguments on both sides of the debate, but on balance, it undermines the supercharged text editor crowd more. No two emacs gurus configure their environment the same way, and souping up the out-of-the-box editor is usually a labor of love for the fan. Go read all the web pages that discuss how to customize vim or emacs, and then tell me I'm wrong. Unless your whole team is cut from identical cloth, you're more likely to have more in common, and to have a higher level of out-of-the-box functionality, with an IDE.

Don't forget the impact of the broader community in your calculations about team value. You can absoely write java code efficiently in emacs or vim &mdash; but the vast majority of java developers use Eclipse or NetBeans or IntelliJ. Why? What does this buy them? Well, their IDEs are constantly educating them about the latest and greatest thinking in the community. When Java 7 or 8 comes out, their IDE nags them to update. Help topics get refreshed. New samples, new project templates, new static code analysis features just show up. And the programmers learn, just by the nature of their toolset. Plus, their skillsets are more likely to transfer, to generate useful help for others on StackOverflow, and to be <a title="Humility" href="humility.md">honed by others</a>, if they're in the mainstream.

A programmer who's <a title="Julie Jones: Learn voraciously." href="six-learning-tips-for-tech-folks.md">plugged in to community best practice</a>, is likely to contribute more value to his or her team, over time, than one who's learned an efficient way to work and isn't interested in newfangled ideas. All other things being equal, of course.

A final thought about teamwork: consider the rising generation. In my experience, most young programmers leave school with more comfort in IDEs than in text editors. Since young programmers are continuously arriving, the value of working within their world view is worth pondering.
<h3>Observation 2: Software engineering ain't just coding</h3>
Besides reading, writing, and debugging code, what do you have to do to release software? If your world is like mine, you have to:
<ul>
	<li>make install scripts</li>
	<li>configure continuous integration, build promotion, and deployment mechanisms</li>
	<li>model <a title="Example RPCD Interaction" href="example-rpcd-interaction.md">people and their behaviors</a></li>
	<li>create and update database and XSD schemas</li>
	<li>design multimedia collateral like icons, sound, color palettes, and video</li>
	<li>encrypt and decrypt license files</li>
	<li>write, run, and re-run unit and integration tests</li>
	<li>generate and consume XML, JSON, and YAML</li>
	<li>tweak CSS and XSLT transforms</li>
	<li>fire up virtual machines in private or public clouds</li>
	<li>feed content to tech writers</li>
	<li>create animations and other visual behaviors</li>
	<li>interface with translation memories and localizers</li>
	<li>react to bug reports from static code analysis tools</li>
	<li>push bugs and enhancement requests through their lifecycle in a ticketing system</li>
	<li>update a wiki</li>
</ul>
... and on and on.

You can certainly live and thrive in that complex world if you're a fan of a powerful text editor. However, I've come to believe that a text-editor-centric worldview is a little too comfortable thinking of every problem as a <a title="Features are not chunks of code" href="why-mental-models-matter.md">mental models</a> remain simplistic. After all, the tool you're using bills itself as an editor, not an "integrated development environment." Isn't that suggestive?

The greatest advocates of unit testing, continuous integration, refactoring, and best practice that I have known in my career have all been IDE proponents. Most (but not all) of the best system thinkers I know are IDE-centric, as well.

I don't think this is an accident.

IDEs show you a gestalt; they encourage you to <a title="Metrics, Plumb Lines, and System Think" href="measurements-plumb-lines-and-system-thinking.md">think holistically</a> about what you're doing. If you write a method, and you don't like the hover text that pops up to coach you when you call it later, then you are incented to change the doc comment for it, then and there &mdash; because the IDE <em>integrates</em> the whole experience. If you rename a method, and 7 red regions suddenly appear along the scrollbar for your file, you learn immediately how much you've broken. If you tweak the model in an MVC architecture, and the IDE is displaying the ER diagram and the table layout from the backing DB in a callout below your edit window, you are more likely to remember to make a complementary edit in that other layer at the same time. You are more likely to care about test coverage if your tool of choice tells you how you're doing, constantly.
<h3>Where I'm at</h3>
If you peruse my archives, you'll see that <a title="Earned Pragmatism" href="earned-pragmatism.md">I'm a pragmatist</a>. I use IDEs as often as I can, but I'm willing to drop into vim when it makes sense. I speak passable vim, but it's not my first language.

I have no doubt that some of the folks who read this post will be awesome team players, great gestalters, and hard-core text editor gurus, all at the same time. That's a cool combination of skill/personality, and I know it's possible to achieve. And if you're there, and you're well into your career, maybe staying there makes sense.

However, what I'm suggesting is that on balance, for most engineers, the usual tool of choice ought to be an IDE instead &mdash; specifically, an IDE that other team members and the larger community use and like. This choice will pay off in enhanced teamwork benefits, and it will <a title="Learned Helplessness, Rats, and People Power" href="smart-geeks-think-like-cheerleaders.md">broad, integrated thinking</a> that characterizes the best software efforts.

Right now, I actively participate in half a dozen codebases. Some consist of venerable, unix-style C; one is cutting-edge C++11; others are in java or python. The teams that maintain the older code cut their teeth on vim and gdb, and they still mostly live there. I wish I could convince them to try out IDE-land for a while; I think they'd find it easier to generate momentum on unit tests, to <a title="Courage Counts" href="paying-off-technical-debt.md">see their way past nagging tech debt</a>. However, bigger concerns have kept me from pushing them hard in that direction.

Maybe this blog post will move the needle. :-)

As I've worked on developing my <a title="On bread recipes, maps, and intentions" href="what-should-code-look-like-when-we-squint-at-it.md">more likely to be realized in an IDE</a>; where I'm headed, text editors won't be enough.

My next blog post will be for the folks who live in the other codebases, and who may think that an IDE is all they'll ever need. They have something to learn from the other worldview, as well...
