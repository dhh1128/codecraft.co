---
title: 3 Commandments of Performance Optimization
date: 2013-01-08
slug: 3-commandments-of-performance-optimization
redirect_from:
  - /2013/01/08/3-commandments-of-performance-optimization
comments:
  - author: dougbert
    date: 2013-01-08 10:19:35
    comment: >
      Can't improve it if you can't measure it!
      
      Measuring twice is key, because then you have two points to compare to each other. Otherwise, one data point is simply a factoid for some tabloid to sell paper.
  - author: Daniel Hardman
    date: 2013-01-08 22:45:09
    comment: >
      I agree; it's awfully hard to get the slope of a line from one point...
  - author: Andy Lawrence
    date: 2013-01-09 22:00:01
    comment: >
      Personally I tend to err toward the "passionate" side of optimization. While I am sure that I have wasted some time fine-tuning some code that only ended up being called once or twice; I have also been pleasantly surprised in many cases where the whole product became much more functional just because some code I wrote worked faster than the spec required.
      
      With my current project, I have had a number of features just "fall out" of the design and work simply because the code ran so fast that it became trivial to process some query.
      
      Performance coding is becoming a lost art. Too many programmers think that faster processors or bigger pipes can overcome bad algorithms. That can work in some cases until a competitor comes along who does it right.
  - author: Daniel Hardman
    date: 2013-01-10 08:43:47
    comment: >
      Andy: I strongly agree with a lot of your comment--especially the part about "too many programmers think that faster processors or bigger pipes can overcome bad algorithms." One of the big insights that should be developed during the CS data structures classes is that some data structures, and some algorithms that work those data structures, are inherently faster that others at large scale. Programmers that choose a solution that's adequate at one scale, but woefully inefficient at another, may be doing themselves and their team a great disservice.
---
In my experience, most programmer attitudes on speed fall into one of these categories:

<em>laissez-faire</em>
<p style="padding-left:30px;">Programmers with this mindset think about performance on occasion, but it's not a big focus. Occasionally they're forced to tackle problems because a particular design is too slow, a customer is unhappy, or new scaling requirements materialize. In such cases, they experiment until behavior improves, and then go back to the work they really care about.</p>
<em>passionate</em>
<p style="padding-left:30px;">Programmers with this mindset have a hard time <em>not</em> thinking about performance. Every design they do reflects elaborate consideration of how to minimize footprint and/or how to complete a task in the shortest possible time. (Note that those two priorities often conflict.) Programmers who are passionate about performance often feel like their laissez-faire counterparts are derelict in their duty.</p>
I don't think either of these extremes is healthy in all cases. I have seen programmers who chronically think about performance too late,  creating large refactoring burdens and sabotaging their company's success. Sometimes when you go from "make it work" to "make it fast" you find that all your original work is a waste, because a totally different design (even different tests, conceivably) is the only way forward; I wrote about this in "<a title="A Quibble With Martin’s “Optimize Later” Notion" href="a-quibble-with-martins-optimize-later-notion" target="_blank">A Quibble with Martin's 'Optimize Later' Notion</a>".

On the other hand, it is possible to be <em>too</em> passionate about performance; optimizing the performance of the dev team (by decreasing coding and testing time) is often a better business choice than optimizing execution speed in ways that make code more complex and harder to verify. I have encountered performance zealots disqualifying a perfectly good design on the grounds that it's not performant enough in a use case that only 2 customers on the entire planet would ever care about. Not smart. As I've said many times, <a title="Good Code Is Balanced" href="good-code-is-balanced" target="_blank">good code is balanced</a>.

<figure><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/0/06/ThrustSSC_front.jpg/800px-ThrustSSC_front.jpg" width="480" height="320" /><figcaption>ThrustSSC -- the first car to break the sound barrier. Sometimes speed is the ultimate criterion. However, most money is made on cars with more modest performance requirements. Photo credit: cmglee (Wikimedia Commons)</figcaption></figure>

Let's assume you buy my criticism of the extremes, and you're willing to apply the <a title="Steve Tolman: It depends." href="steve-tolman-it-depends" target="_blank">"it depends" doctrine</a>. <!--more-->In some cases, you do nothing about performance, because the stakes are low. (Yes, all you performance zealots, there really are cases like this.) In other cases, you have to bring your A game. You want to strive for a pragmatic position that preps the code to be scalable up and down for years to come, that delights customers with its responsiveness, that's not overly complex or expensive to create or maintain, that makes wise use of scarce resources, and that will be friendly to innovations like massive parallelism and faster disk, network, and CPUs.

A tall order.

Here are 3 principles that I believe that will maximize your chances for success.

<strong>I. Thou shalt measure.</strong>

How many of the following doctrines have been preached to you?
<ul>
	<li>The stack is faster than the heap.</li>
	<li>RAM is faster than disk.</li>
	<li>Inlines are faster than normal function calls, which are faster than virtuals.</li>
	<li>Hand-coded classes are faster than STL.</li>
	<li>Arrays are faster than linked lists.</li>
	<li>Parallel is faster than serial.</li>
	<li>Qsort is faster than bubble sort.</li>
	<li>"Native code" is faster than interpreted or garbage-collected languages.</li>
	<li>Atomics are faster than mutexes.</li>
	<li>In-proc is faster than out-of-proc.</li>
</ul>
Want to know the truth?

The truth is, it depends.

It is useful to learn certain rules of thumb. We have to have a <a title="Why Mental Models Matter" href="why-mental-models-matter" target="_blank">mental model</a> that lets us make simplifying predictions, such as "It's probably going to be a waste of my time to make command-line parsing faster if my program runs as a daemon." We also want to code using techniques that are perennial best-of-breed winners as far as performance is concerned, all other things being equal.

But.

Not all rules of thumb are not equally true or useful to begin with. What's more, not all rules of thumb are equally true for all types of hardware, and most rules of thumb do not hold constant over time. The landscape has shifted repeatedly in recent years due to the advent of mobile devices, NVRAM, GPUs, ultra-low-power CPUs, radically faster networks, hadoop, JVMs hosted in hardware, virtualization, cloud, and dozens of other innovations. You can expect regular flux for the foreseeable future.

The reason our profession is called computer science is because it traffics in provable hypotheses, not hunches. In order to do any serious performance optimization, you must have data. And generic data is suspect; it's probably not good enough to say "I called each function a million times; the one that uses disk is 4000 times slower than the one that uses RAM on my machine." This sort of report sounds good, but it doesn't tell you whether the functions are called with the same frequency and parameters as they would be in production. Your data should reflect the environment most relevant to your customers, under conditions that are likely to matter to your customers. Or as close to it as you can get, given constraints on time and resources.

If you are optimizing by rule of thumb, instead of using cold, hard data, then you are breaking the first commandment of optimization.

Repent!

Side benefit A: Measurement defuses holy wars among passionate developers. We tend to argue more about dogma, and less about data.

Side benefit B: Measurement provides numbers that other smart people (managers, product managers, executives) can use to participate in tradeoff calculations. Saying that a rewrite will make things "faster" is hard for a business person to evaluate; saying that it will make a particular use case 73% faster for the average customer, on a system with average daytime load, is easier.

<strong>II. Thou shalt work the bottleneck.</strong>

If you have not already read <a href="http://www.amazon.com/Goal-Process-Ongoing-Improvement/dp/0884271951/" target="_blank"><em>The Goal</em>, by Eliyahu Goldratt</a>, then add it to your backlog. Or at least spend a few minutes with the cliff notes. In the book, a manager in a production facility is trying to make more widgets. He tries all sorts of improvements. He threatens and cajoles and "motivates" the troops. Some experiments are fruitless. Some experiments actually make things worse.

Eventually he realizes a profound truth: <em>effort spent on anything other than the current bottleneck will have no immediate benefit.</em>

Engineers, write this down on a 3x5 card and staple it to your forehead.

If a process is I/O bound, then a better sort algorithm ain't gonna matter, even if the better sort is 1000x faster. Likewise, if you take four milliseconds to read a config file, half a second to query a database, and half a second to format an http response, then building a more efficient config file parser ain't gonna matter.

In order to work the bottleneck (or bottlenecks!) correctly, you must construct a mental model of a processing pipeline, backed by the data you collect, that looks something like this:

[caption id="attachment_901" align="aligncenter" width="500"]<img class="size-full wp-image-901" alt="Sample diagram of a process that might be optimized (in this case, a browser requesting a page that requires database query support). Greater height = greater throughput of a subsection of the process. Current bottleneck = shortest rectangle." src="http://codecraft.co/wp-content/uploads/2013/01/pipeline.png" width="500" height="500" /> Sample pipeline diagram for a process that might be optimized (in this case, a browser requesting a page that requires database query support). Greater height = greater throughput of a subsection of the process. Current bottleneck = shortest rectangle (in this case, security filter).[/caption]

Once you have such a model, the proper focus for optimization should become obvious. (It should also be clear when/whether work on secondary bottlenecks might pay off. For example, if you can increase the capacity of the most constrained section of your pipeline, then perhaps the next-most-constrained section's capacity will become relevant...)

<strong>III. Thou shalt measure.</strong>

This is not redundant, and it is not simply repeated for dramatic effect.

After you've measured and made your tradeoffs, you must continue to measure, at least often enough to notice if the tradeoffs you made become invalid. Remember the part about how often rules of thumb change? Don't make the assumption that the right tradeoffs today will always be the right tradeoffs tomorrow.

I have worked several times in my career on technologies that were orders of magnitude faster than their competitors in the marketplace. In each case, the faster tech was disruptive, and the established and slower equivalent was long in the tooth. And in each case, the slower technology wasn't nearly so slow to begin with; its performance eroded steadily over time as it became more complex and addressed more and more corner cases. (Consider how the introduction of security affects performance in the pipeline diagram above.) So a word of warning to all purveyors of disruptive, radically faster coolness: if you don't continue to measure the performance of your stuff, on an on-going basis, I predict that you will lose a lot of your edge.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Build a pipeline diagram for a process that you want to optimize. Identify bottlenecks. What aspects of the process should you ignore?</span></em></p>
