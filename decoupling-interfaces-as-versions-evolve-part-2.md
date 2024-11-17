---
title: Decoupling Interfaces as Versions Evolve, Part 2
date: 2008/08/19
slug: decoupling-interfaces-as-versions-evolve-part-2
---

<em>This is part 2 of a series. You can read <a href="/codecraft/2008/07/29/decoupling-interfaces-as-versions-evolve-part-1/">part 1</a> and <a title="Decoupling Interfaces as Versions Evolve, Part 3" href="../../../2008/08/19/decoupling-interfaces-as-versions-evolve-part-3/">part 3</a> as well.</em>
<h3>Alternative Approaches to Interface Versioning</h3>
Lublinsky wrote a great article about interface versioning a while back (see page 38 of <a href="http://www.msarchitecturejournal.com/pdf/Journal11.pdf" target="ms">this issue of Microsoft's Architecture Journal</a>). This describes the state-of-the-art thinking about interface versioning in the web services world. Essentially he recommends versioning each method in an interface separately. (Sounds a lot like Win32's approach of adding <em>...Ex</em> to every function when the original behavior no longer sufficed...) This approach is based on the insight that many parts of an interface will be stable for long periods of time, and that the most common kind of change to an interface is an addition. By increasing the granularity of the versioning, incompatibilities are less likely to arise for spurious reasons. This solves the classic problem where a .wsdl describes a dozen classes, a client uses only the first three, and yet the client breaks when something in the fourth class changes. However, it proliferates .wsdls and points of presence.

Another important discussion of this issue is <a href="http://www.theserverside.net/tt/articles/showarticle.tss?id=SOAVersioningCovenant" target="soa">"A SOA Versioning Covenant", by Rocky Lhotka</a>. This is an excellent review of the problem. (Note that the Lublinsky article, which is newer, discusses the covenant idea briefly.) Essentially Lhotka recommends that all objects accept messages (parameter lists to functions, recast as documents or self-contained packages of information); since each logical function will always have the signature <code>DoSomething(message)</code>, the need to version interfaces goes away as long as changes just involve new message types. Instead, the messages are versioned using schema capabilities. Lhotka further recommends changing from contract-oriented thinking (X is required) to a covenant (If you do X, I will do Y). This approach has some of the same benefits as the invention, but it still relies on versioning a full interface rather than the subset someone wishes to use, and the difficulty of managing versions of messages is ignored.

Although both of these treatments (and the sources they cite in their own reviews of the problem) are nifty, they leave me unsatisfied. The bottom line is that I want to evolve interfaces whenever it makes sense, without worrying about breaking people -- and I also want people who use my interface to be able to do so with confidence.

Tune in to <a title="Decoupling Interfaces as Versions Evolve, Part 3" href="../../../2008/08/19/decoupling-interfaces-as-versions-evolve-part-3/">part 3</a> of this series for my proposed solution.

---

Decoupling Interfaces As Versions Evolve, Part 1 &laquo; Codecraft (2013-02-21 11:54:55)

[...] to interface versioning with the flexibility of late binding to get the best of both worlds. In part 2 of this series, I’ll look at some approaches to that goal, and discuss why they still leave [...]

---

Julie (2013-03-08 17:40:07)

Such a timely post. I am right in the middle of moving a distributed system from a custom RPC style communication to a messaging system. My current thought is to at least use the document mechanism to at least allow some compatibility among components running different versions. I am looking forward to part 3.

---

Daniel Hardman (2013-03-08 18:32:54)

Synchronicity! I just wrote my first RabbitMQ client last week. Great minds think alike! :-)