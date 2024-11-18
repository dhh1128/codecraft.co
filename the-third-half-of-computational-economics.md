---
title: The third half of computational economics
date: 2013-08-09
slug: the-third-half-of-computational-economics
---

If you look up "computational economics" on wikipedia, you'll find out all about software models that economists use to study game theory, recessions, scarcity, and so forth.

Tweak your search terms a bit, and google takes you to discussions about the economics of the computer industry--how Moore's Law plays out in changing prices for compute power, why cloud computing and cheap GPUs are changing how much we expect to pay, how the mobile revolution is killing traditional PCs, what the job market looks like for us software geeks.

That's all well and good.

But there is a third half of the computer+economics interaction that I don't hear anybody talking about.

[caption id="attachment_1252" align="aligncenter" width="500"]<img class="size-full wp-image-1252" alt="3-fingers" src="http://codecraft.co/wp-content/uploads/2013/08/3-fingers.jpg" width="500" height="385" /> My buddy <a href="ken-ebert-kill-three-birds.md">Ken Ebert</a> likes to joke about incomplete thinking by saying, "There are 2 aspects of the issue..." -- while he raises three fingers. :-) Interestingly, this three-fingered gesture is a symbol of sustainable development, which connects nicely to our theme of economics. Photo credit: <a href="http://www.flickr.com/photos/dragonpreneur/2918061941">\!/_PeacePlusOne (Flickr)</a>[/caption]

<!--more-->Why don't we use economic principles to model scarcity and tradeoffs within our applications and ecosystems?

I suspect that most of us have written an application that is a bit too cavalier with its use of resources. We want to allocate 9 GB of RAM to store a monster bitmap, so we call malloc. It might fail, but if it doesn't, we have no sense at all of how much burden we've placed on a scarce resource. We don't "pay" for the allocation in any way. There's <a title="Why Your Software Should Cry" href="why-your-software-should-cry.md">no pain</a>.

This same scenario plays out in how applications bottleneck a network pipe, how disks fill up, how threads contend, how jobs are scheduled and pre-empted in a supercomputer, how data is moved back and forth in <a class="zem_slink" title="Hierarchical storage management" href="http://en.wikipedia.org/wiki/Hierarchical_storage_management" target="_blank" rel="wikipedia">HSM</a>, and how heads move across a spinning platter to satisfy I/O requests...

The general approach in industry is to introduce some kind of prioritization algorithm that arbitrates between competing consumers. We talk about "fair share" and "starvation."

This feels a bit like the centralized planning of communist regimes. History tells us that despite the theoretical attractiveness of such models, in practice they are much less efficient than Adam Smith's invisible hand.

So why not apply the free market in software?
<ul>
	<li>Give independent entities in software (applications, threads, users, etc) a certain amount of capital with which to purchase resources.</li>
	<li>Also give them a goal to maximize "profit". Profit would be defined differently for each entity, but would probably involve getting their work done while maximizing speed or other metrics.</li>
	<li>Allow resource providers to "sell" their wares as they see fit, and give them the goal of maximizing "profit" as well.</li>
</ul>
I don't think a system like this would be worth building in all cases, and it might have some unpleasant side effects like starvation of a humble process that can't adequately compete for resources. It would require <a title="3 Commandments of Performance Optimization" href="my-first-tangle-with-the-tower-of-babel.md">better programming language</a>...
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">What complications do you foresee in such an approach? And how would you enhance it?</span></em></p>



---

tianyuzhu (2013-08-09 16:17:49)

I'm going to argue that free markets aren't necessary in *general* in software development because economics assumes that everyone is selfish.

For example, when you're writing a function, you establish a contract saying, "If you provide me with the proper resources and fulfill the preconditions, I will perform this service for you." Now the function trusts that it will be used properly, and the user trusts that the function will do its job. In software development, you don't try to sneakily call the function without satisfying all of its preconditions. In fact, you probably go to extra lengths to meet them.

Take another example. When you're writing an application for a certain OS, the OS, the kernel tells you, "your process can have these resources and do its work provided that it is well-behaved and that it doesn't consume more than this much memory/file descriptors/etc." In return, when you write this well-behaved application, you trust that the kernel won't starve your process, etc.

In short, selfishness isn't an issue in software development, since every entity strives to trust and be trustworthy in the name of getting stuff done. Now it's true that things might seem a bit communist at times. Misbehaving processes are ruthlessly terminated by the kernel. But in return well-behaving processes have peace of mind that they will get their fair share of resources -- and that's important, because watching your back all the time is an expensive endeavour.

So if we introduced free market mechanics into software development, what might happen? I suspect it will be similar to the real world. Some entities who think they're more important than others will try to manipulate the system and hog all the resources. "My process has better performance because it messes up other processes' stack pointers, causing them to crash. MUAHAHA." Everybody will have to start watching their backs. It'll be impossible to program for.

The thing is, you see economic models in programming all the time. All you have to do is look at systems where humans can make certain parts of the system more selfish. For example, ISPs give you higher bandwidth and limits if you pay more.

---

Daniel Hardman (2013-08-09 17:07:12)

Thanks for the thoughtful response.

I agree that software doesn't translate perfectly into the economic metaphor. There are some examples where it shows up -- the ISP example you mention is a good one -- and there are also examples where central planning is very helpful.

Your example about processes getting resources from the kernel is worth pondering. In my experience, it is very common for processes to be selfish and to abuse the kernel's generosity. There are some kernels that are more militant about enforcing good behavior, but it's not at all difficult for me in most cases to write software that uses all resources with utter disregard to the needs of other processes on a box. That's a case where I wonder if economics might help. However, as you point out, watching your back at all times is expensive, so introducing the extra complexity of modeling resource allocation economically would have to provide a fairly big benefit to be worthy of consideration.