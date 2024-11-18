---
title: Know Your Limits
date: 2015-02-05
slug: know-your-limits
redirect_from:
  - /2015/02/05/know-your-limits
---

I just finished the nastiest debugging experience of my career--nearly 3 weeks on a single bug. After days and days of staring at code, swearing at core dumps, tailing logs, connecting to gdbserver via a multi-hop ssh tunnel from inside a secure environment, and general programmer misery, I felt like doing cartwheels when I finally figured it out, tweaked a few lines of code, and observed stability again.

Hindsight teaches me this lesson: <em style="color:#706;">undocumented, unhandled constraints waste enormous amounts of time and energy</em>. If you're interested in writing good code, you must know your limits, and you must communicate them. This especially matters when the constraints are obscure or surprising.

<figure><img class="" src="https://farm4.staticflickr.com/3084/3137178654_0796758be3.jpg" alt="" width="500" height="313" /><figcaption>image credit: ericdege (Flickr)</figcaption></figure>
<h3>Naive optimism</h3>
My bug seemed simple enough at first blush:<!--more--> I was seeing crashes in a daemon that uses machine learning to classify internet traffic. I'd just rewritten the app's DNS subsystem to increase throughput, and the crashes often happened in my new event-processing loop. The loop fired off callbacks to service sockets as they became unblocked; I assumed I had some kind of off-by-one error in my sockets array, or maybe I wasn't cleaning up sockets consistently.

No such luck.

The more I dug, the deeper the mystery grew. Sometimes I got core dumps, sometimes I didn't. Sometimes I got a <code>SIGSEGV</code>, sometimes not. Sometimes my core dumps were usable, sometimes they were corrupted. The values displayed in the debugger when I analyzed a core dump didn't make sense. The exact site of the crash seemed to vary. I began to suspect that a heap or stack corruption at an unrelated, innocent-looking, "stable" place in the code might be crashing DNS because it's so heavily threaded and high-performance.

I ran valgrind. I ran a specially instrumented <a href="http://clang.llvm.org/docs/AddressSanitizer.html" target="_blank">Clang address sanitizer</a> build. They yielded lots of noise, but no consistent smoking gun.
<h3>Who knew?</h3>
After a few days of semi-informed guesswork, I finally got methodical. I started tracking my theories and disproving each of them with a series of experiments. This revealed layers of undocumented, lurking problems that cloaked the real issue. Each is a place where an engineer failed to communicate or plan around a constraint:
<ol>
	<li>I suspected that the bind server I was calling to do DNS resolution might be experiencing brown-outs, and that the resulting backlog of pending DNS requests might be a trigger for my crash. I had to dig around for a while to see what kind of timeouts DNS used, because <em>most DNS documentation doesn't consider this to be worth mentioning!</em> Wanna guess? 5 seconds. And you have to multiply that by 2 or 3, since DNS is usually UDP-based and uses retries to compensate. Since my daemon needed to respond within a couple seconds, and since it gets tens to hundreds of queries per second, having a 15-second DNS timeout was a real problem... Fortunately, the DNS library I was using, <a href="http://c-ares.haxx.se" target="cares">c-ares</a>, lets you <a href="http://c-ares.haxx.se/ares_init.html" target="cares">customize both the timeouts and the retries</a>, so I worked past this.</li>
	<li>Since I wasn't always getting a core dump, I wondered whether the signal causing the abend might be inconsistent. It turned out that the daemon installed handlers for a few signals, but not all, and it didn't report which signal triggered the crash. Getting disciplined about signal handling eliminated the confusion caused at this layer.</li>
	<li>The app had configurable limits on max sockets and max threads, but it didn't seem to follow them reliably; it took me a while to realize that it was ignoring interactions with hard and soft resource limits imposed by the OS (see the <a href="http://linux.die.net/man/2/getrlimit" target="_blank"><code>getrlimit()</code></a> posix API).</li>
	<li>The app used the <code>select()</code> posix API to discover which sockets became ready or timed out. But it turns out that <code>select()</code> blows up if you are monitoring more than <code>FD_SETSIZE</code> (=1024) sockets, although none of the example usages showed that, and the <a href="http://linux.die.net/man/2/select" target="_blank">man page for <code>select()</code></a> only mentions it in a cryptic aside. I had to stumble upon this particular wisdom via google and <a href="http://stackoverflow.com/questions/7976388/increasing-limit-of-fd-setsize-and-select" target="_blank">stackoverflow</a>. (Even after I capped open sockets safely below this limit, I had a performance problem because <code>select()</code> scans linearly across as many sockets as you have open; I need to switch to <code>epoll()</code> asap...)</li>
	<li>The c-ares library is all about asynchronous resolution with lots of overlapping, parallelized I/O on many sockets. It's great code, and I appreciate the generosity that made it open-source. It provides a <code>channel</code> construct to manage many pending requests, and users such as the curl dev team cite examples of thousands of pending requests. However, I learnedter much pain that 16 pending requests per channel is what c-ares was designed for, and one request per channel is more standard; you can scale super-high, but only by using many channels. It took <a href="taming-side-agreements.md">informal side agreement</a> in the API.</li>
	<li>During spikes in traffic to the app, if the open socket count exceeded the OS's soft limit but not the limit in the config file, it was possible to get in a state where we couldn't bind an incoming socket to return an http <code>503 Server Busy</code> status to the client. This made it difficult to decide whether a traffic spike was a trigger for our problem, since we were identifying spikes by looking for 503 errors. I fixed this problem by reserving some sockets for returning errors.</li>
	<li>To make matters worse, when a socket failed to bind for this reason, some very low-level code (possibly in the kernel's underlying TCP/IP stack) issued a retry... over and over again. I was seeing logs flood with over 200k retry attempts per second in this unusual state. I had to fix this by <a title="Why Your Software Should Cry" href="dont-forget-the-circuit-breakers.md">circuit breaker</a> to keep the logs moderately quiet.</li>
</ol>
<h3>The rest of the story</h3>
Eventually I waded through all these layers of undocumented, improperly handled constraints on program behavior, and my app was still crashing, still unpredictable. In desperation, I downloaded the source for c-ares, built it with debug symbols, captured a stack trace, and analyzed the code path. I discovered to my surprise that nowhere was the channel parameter mutexed in the call graph of <code>ares_gethostbyname()</code>. This triggered some more targeted googling than I had previously managed, and I found an <a href="http://c-ares.haxx.se/mail/c-ares-archive-2008-05/0039.shtml" target="cares">email thread from 2008</a> where the author of the library clarifies the undocumented mutexing rules. A light went on; 5 minutes later I had fixed the bug.

I feel a little silly; the library code is solid and reasonable, and the need for this particular mutex should have occurred to me long ore. But in my defense, the library is all about parallelism, the channel object that needed mutexing is intended to support many simultaneous requests, and the docs are utterly silent about the topic. So are all the samples I found; not one shows a mutex. (That's because all the samples are asynchronous but single-threaded; I should have been more careful as I extrapolated to my slightly different use case...)

Anyway, I'm a sadder but wiser programmer now. :-) I need to add <a title="Introducing Marks" href="on-bread-recipes-maps-and-intentions.md"><code>intent</code> programming language I'm creating</a>, so that this type of issue is easy to formally communicate. But even without fancy new languages, the programming ecosystems that we all work in today would benefit from more attention to understanding, handling, and communicating limits.

---

Daniel Hardman (2015-02-05 23:19:02)

For me, this is proof that fixing something "right", instead of just kludging something good enough, is often (not always, but often) the most efficient approach. The quick-and-dirty solution might feel faster, but by the time we add in the cost of a learning curve, future maintenance, testing, and support, making haste more slowly is often better.

Of course there are exceptions to every rule...

---

David H (2015-02-05 20:08:09)

Interesting how a really hard-to-find bug motivated you to really "clean house" and address a bunch of other issues. "If it aint broke don't fix it", but since it was broke you got to fix some things.

---

mordachaiwolf (2015-02-05 10:15:27)

Thanks for sharing this!  And congrats on tracking it down.

---

Daniel Hardman (2015-02-05 13:00:27)

Since I complain about not communicating limits, I would be remiss if I didn't record what I learned so it's at least findable in a web search. :-) I don't think I've ever been more relieved to put a stake through the heart of a bug.

---

Moray King (2015-02-09 22:01:52)

Double kudos to you Daniel:
1. A well written piece that was fun to read.
2. You resolved the bug!

Your essay confirms a point I always believed: Care must be taken when designing and coding a multi-threaded system where concurrent sharing is involved. Concurrency bugs are notoriously difficult to resolve especially if they are intermittent and difficult to trigger. At least you had a trigger, and with it you skillfully converged onto the bug. Well done, Daniel!

---

Daniel Hardman (2015-02-10 07:31:07)

So good to hear from you, Moray! I think that years ago I told you that I thought concurrency wasn't that hard. This makes me eat my words. :-) It may not be that hard in theory, or when a codebase is in its infancy--but by the time we get to hundreds of thousands of lines of code, with large numbers of threads interacting in complex and unpredictable ways, we better have it right, or we can find ourselves in deep trouble.

I thought of your clean and robust epoll-based http server while I was doing this work...

---

earwicker (2015-02-27 04:10:24)

Congrats on fixing it. I spent a couple of weeks in the late 90s connecting to customer machines and looking at stack traces of several threads that were either deadlocking or trashing each other's data. This was enough to make me back away from that school of currency whose motto is "Just keep adding mutexes until it seems to stay up!" Since then I've stuck to threads that communicate only via queues that contain very simplistic/immutable "work item" objects, or I go the whole hog and use process isolation, with a pool of single-threaded worker processes orchestrated by a single-threaded manager. I also avoid languages with undefined behaviour (like they are plague-carrying rats). This is why I'm not touching Go with a barge pole (undefined behaviour under race conditions).

---

Daniel Hardman (2015-02-27 07:33:55)

It's so interesting to me that people who have deep experience debugging a concurrency problem are usually changed by the experience. They begin to value features of their language or their tools differently when they've experienced the bleak prospect of not being able to figure something out except with a lot of blood, sweat, and tears. And maybe not even then.

I did not know anything about Go and race conditions; that's troubling.

I, too, have had good experiences with cross-thread communication only via queues. That's essentially the same solution that the designer of zmq advocated: http://zeromq.org/blog:multithreading-magic