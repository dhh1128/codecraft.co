---
title: Taming Side Agreements
date: 2014/10/28
slug: taming-side-agreements
---

When I was a technical director at Symantec, I had to formally certify at the end of each quarter that I had not entered into any "side agreements" with customers.

A side agreement is any arrangement that takes place out-of-band, off-the-books, or using private channels not normally examined by accountants. In business, they are usually a bad thing; they can be used to build Enron- or Madoff-style house-of-cards revenue pipelines that are gleaming and glittery at first glance, but that are ripe for collapse because they're full of hidden caveats and preconditions.

<figure><img src="https://farm4.staticflickr.com/3593/3389046866_c642884f48_z_d.jpg" width="640" height="283" /><figcaption>The former Enron towner, now owned by Chevron. Image credit: DaveWilsonPhotography (Flickr)</figcaption></figure>

The problem of side agreements might not impinge on the consciousness of software engineers much, except when they grumble that sales or execs or product management is "selling the roadmap" instead of shipping features. But would you believe me if I said that engineers perpetrate their own Enron-esque side agreements all the time?

<!--more-->

<h3>How agreements are formalized in software</h3>

Think about what embodies the formal contract between the producer and the consumer of a chunk of code. Whether you describe an API with IDL, WSDL, an XSD, a grammar, a function decl in a header, an abstract base class, or loose Go-style implicit interfaces, the scope of issues you can describe is largely confined to those expressible with data type and function signature primitives. You basically get to say, "I support a [verb/function/method/action] named X, which takes the formal parameters A [of type x] and B [of type y] and returns C." You may be able to specify some overloading and versioning, if you're lucky, and you may be able to group a set of these statements together into a larger unit.

Some crucial topics are entirely missing from your contract:

<dl>
<dt>What ordering constraints govern which APIs can be called, when?</dt>
<dd>We know that you can't call fclose() until you've called fopen(), but can you tell by reading the interface to a class that some methods are only valid when an object is "fully" inited? Do we always have to follow method A with method B? Although these constraint may sometimes be (somewhat accurately) documented, they're not in a function signature anywhere, and docs could change without a hiccup from the compiler.</dd>
<dt>What security constraints govern API success and failure?</dt>
<dd>Same story as ordering--we document this stuff, but compilers punt all enforcement to run-time.</dd>
<dt>What expectations does an API have about available resources--and what guarantees does it make about how those resources will be used?</dt>
<dd>Obviously (to a human), an API that downloads from the internet is going to fail if the network is down... unless it uses a locally cached version of the file... Some APIs fail in low-memory situations--though the exact boundaries that trigger the failure may change depending on unpredictable factors. Will an API peg all available CPUs, or only one? How much disk space will the API need? Does it need write access to /tmp, or to ~/?</dd>
<dt>What performance guarantees does an API require or provide?</dt>
<dd>This includes classic "Big O" notation, but it goes well beyond that. How long will it take for the API to time out? How many times will it retry, and how expensive will the retries be?</dd>
<dt>How often can an API be called?</dt>
<dd>Does it cache values for efficiency? If so, what policies govern caching? Is the expense of the call such that calling it a hundred times a second is a ridiculous violation of its coder's assumptions?</dd>
</dl>

<h3>Reality bites</h3>

Eliminating such issues is one of the benefits often touted by fans of functional programming. Pure functions <em>do</em> have less side effects, and therefore, less potential for misuse. But when the intent of a function call is to <em>cause</em> certain effects, pure functions don't help us; all these messy issues crowd in. Just because they aren't expressible in an interface contract in code, doesn't mean we don't code against them. If we're lucky, documentation is thorough and accurate, and behavior across versions is mostly stable, and we figure out how to get what we want by coding just so. Basically, we create side agreements: <em>I will do this or that extra thing that's not part of the contract, and you'll do this or that extra thing that's not part of the contract, either.</em>

Does that make you squirm?

It should. Like a shell game that hides risky debt, this sort of invisible <em>quid pro quo</em> can permeate a code base, riddling it with invisible tech debt and setting it up for future maintenance headaches. We end up with subtle temporal coupling, runaway transitive dependencies, impossible compatibility constraints, and worse.

What makes this problem particularly insidious is that we often stumble into these side agreements after a lot of painful trial and error. And we have to repeat that trial and error at the most inopportune times. I can't count the number of hours I've wasted, discovering by monotonous debugging that such-and-such a function can't be called until some other function has properly initialized a context that nobody told me I needed. Or the times I've debugged a mysterious slowdown, only to discover that an OS API doesn't perform the same way after a service pack.

<h3>What can we do?</h3>

I don't know that there's a silver bullet to eliminate all side agreements in code, but I think we can learn some lessons from the world of finance.

First, <em>sunshine helps</em>. The more light you can shine on the dark corners of an interaction, the less likely it is that side agreements will surprise you. World-class API documentation (Microsoft's Win32 KB, Oracle's java docs, the full posix standard) makes a concerted effort to expose many of the subtleties I listed above, although I think <a href="mountains-molehills-and-markedness.md" title="Mountains, Molehills, and Markedness">"marks" feature</a> that I'm building for the <code>intent</code> programming language lights up all kinds of nether regions that lurk in perpetual gloom.

Second, <em>auditors [automated tests] are vital</em>. It's popular in some circles to say that you only need to test the public interface to a class/module--and in theory, I agree. But remember that the true breadth of the interface you're coding against goes well beyond function signatures. A human auditor is pretty useless if she or he only checks the obvious stuff. Make your tests thorough.

Third, <em>we need whistleblowers</em>. I have previously written about <a href="dont-forget-the-circuit-breakers.md" title="Don’t forget the circuit breakers">circuit breakers</a> in code. We need ways to find out that everything isn't working right--ways that are smarter than log files that get ignored until we have a full-blown crisis.

Fourth, <em>the size of your accounting staff depends on the scale of your operation</em>. In other words, be <a href="architects-manage-risk-like-a-vegas-bookie.md" title="Architects: manage risk like a Vegas bookie">manage it wisely</a> as part of your architecture.

<h3>Your battlescars</h3>

How about you? When have you been bit by "side agreements" in code? What techniques have you used to drive them out? Please share.


---

David H (2014-10-29 07:12:42)

"But when the intent of a function call is to cause certain effects, pure functions don’t help us; all these messy issues crowd in."

For those of us who write code for a living, an important side effect of a function is that the customer gives us money. I'm glad you said that there is no silver bullet, because that whole making-the-customer-happy thing is very difficult to automatically verify at compile time. :)

For purposes of expressing and enforcing the "real" contract, I have found test-driven-development to be helpful. A docstring on a recent test: "The save() method creates a file that is only readable and writable by the owner." How's that for a contract?

The problem with my test suite is that no one seems to want to read over my unit tests to see what the code does. :) Tests in one place are enforcing what docs in another place are saying, and hopefully the two match. Python doctests [1] can help with this, for certain types of tests and certain types of code.

[1] https://docs.python.org/2/library/doctest.html

---

Daniel Hardman (2014-10-29 07:21:42)

David: thank you for pointing out the "side effect" of getting paid. Very à propos! :-)

I agree about the value of TDD. I haven't used doctests very often, but I am at a loss to explain why--they're quite nifty. One thing that I particularly like about them is that they are embedded in the code, *not* stored in a separate file. This makes it more likely that a programmer will actually read/be aware of the semantics they enforce.

---

Know Your Limits | Codecraft (2015-02-05 08:47:41)

[…] but only by using many channels. It took an email exchange with the author to discover this informal side agreement in the […]