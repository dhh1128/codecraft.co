---
title: Decoupling Interfaces As Versions Evolve, Part 1
date: 2008-07-29
slug: decoupling-interfaces-as-versions-evolve-part-1
redirect_from:
  - /2008/07/29/decoupling-interfaces-as-versions-evolve-part-1
comments:
  - author: Decoupling Interfaces as Versions Evolve, Part 2 &laquo; Software, Wetware, Webware
    date: 2008-08-19 11:10:44
    comment: >
      [...] Interfaces as Versions Evolve, Part 2    This is part 2 of a series. You can read part 1 and part 3 as [...]
  - author: Decoupling Interfaces as Versions Evolve, Part 3 &laquo; Software, Wetware, Webware
    date: 2008-08-19 11:27:41
    comment: >
      [...] Interfaces as Versions Evolve, Part 3    This is part 3 of a series. You can read part 1 and part 2 as [...]
---
<em>This is part 1 of a series. You can read <a title="Decoupling Interfaces as Versions Evolve, Part 2" href="decoupling-interfaces-as-versions-evolve-part-3.md">part 3</a> as well.</em>
<h3>The Goal</h3>
Software interfaces were invented to promote <a href="http://en.wikipedia.org/wiki/Encapsulation_(classes_-_computers)" target="wikipedia">encapsulation</a> and <a href="http://www.cs.unc.edu/~stotts/COMP145/modules.html" target="_blank">loose coupling</a>. In theory this enables developing and deploying without undue interdependence, which is a <em>very</em> good thing.

"Why the 'in theory' caveat?", I hear you saying. "Surely interfaces deliver on their promise..."

Well, yes and no. Interfaces certainly provide a nifty mechanism for information hiding if your scope of concern is a tidy programming problem over the horizon of one implementation. That's just the sort of scenario that CS academics love to use to teach their acolytes.

But most commercial software development is done in a messier world. Versioning interfaces can cause enough headaches to water down their benefits considerably, and mainstream software development tools have not done enough to address the issue.
<h3>Immutability and Versioning</h3>
Current thinking on interface versioning calls for an interface to be immutable; each change to its semantics (as manifest in an .idl, a .h, or a .wsdl, for example) should cause a change to the interface number/name/guid. Consumers of an interface bind to a specific interface version to allow compile-time validation of interface usage. Modern IDEs typically leverage early binding to provide extra goodies like autocomplete, UML class diagrams, and doc comment generation.

This immutability is less than perfect. In non-ivory-tower development, it is common to alter the semantics of an interface dozens or hundreds of times during a given dev cycle as a team converges on the final implementation. Bob adds the <code>DoNothing()</code> and <code>DoSomething()</code> functions to <code>IWidget</code> on day 1, then realizes a week later that he also needs <code>DoSomethingElse()</code> for a corner case he hadn't fully explored. On week 23, he decides to collapse the <em>DoSomething</em> functions both to <code>DoSomethingEx()</code> because by then the differences between them feel like they should be generalized.

If all code were written by Bob as part of a single cohesive deliverable, this evolution would be uninteresting. But suppose that on week 15, Sally gets a snapshot of Bob's .idl, and begins to build a new component to interact with <code>IWidget</code>. It is critical that Sally's expectations about <code>IWidget</code> semantics line up with Bob's.

What makes this ugly is that in today's highly distributed, highly oursourced, complex projects, Bob may not actually know that Sally is using his .idl. He may think it's okay to keep cheating on interface immutability. Either Bob has to be obsessive about versioning his interface with each change -- ending up with IWidget497 by the end of the project -- or else Sally is forced to communicate with Bob that she is using his interface and needs it to be stable. Neither alternative is very attractive.
<h3>Evolution Isn't Always Forward</h3>
Best practice is usually to require that <code>IWidget5</code> be a strict superset of <code>IWidget4</code>. Despite enthusiastic lip service, practical considerations force us to cheat here as well. A security vulnerability forces us to start encrypting the string we return from a function. A change to the underlying OS forces us to throw an exception on a function that used to be exceptionless. Over time the assumptions about semantics attached to an interface accumulate enough drift that it is impractical to ever treat an <code>IWidget9</code> as an instance of <code>IWidget2</code>. How does Sally know when that threshold has been passed by Bob?
<h3>And What About Deployment and Upgrade?</h3>
If you want to tease out mistakes in interface versioning, just poke at the deployment and upgrade scenarios you're going to support. Do you require that a central manager be at least as new as all the components it's managing? Or worse, do you require the whole system to be at the same revision level? In theory, this should be unnecessary; producers (managees) are free to expose functionality in new interfaces that older consumers (managers) don’t know about, and consumers can progressively downcast until they find a mutually supported interface, so it ought to be possible to have free variation in versions. However, in practice in rich, interdependent fabrics of services, the same actor may simultaneously provide one interface while consuming another, and the intermingled dependencies often cause ISVs to force broader upgrades than a customer would like. My favorite recent, real-world example of deployment problems is the infamous <a href="http://episteme.arstechnica.com/eve/forums/a/tpc/f/99609816/m/494009191831" target="ms">IE7 dwmapi.dll problem</a> (see also <a href="http://blogs.misdn.com/nikolad/articles/427101.aspx" target="ms">this useful discussion</a> of the problem).

[caption id="attachment_37" align="alignnone" width="128"]<a href="../../../wp-content/uploads/2008/07/traditional-pros-and-cons.png"><img class="size-thumbnail wp-image-37" alt="" src="http://codecraft.co/wp-content/uploads/2008/07/traditional-pros-and-cons.png?w=128" width="128" height="75" /></a> Traditional Approach - Pros and Cons[/caption]
<h3>What Can Be Done?</h3>
So if interfaces don't provide as much separation of concerns as we wish, how do we cope?

Well, one alternative to traditional interface versioning is to do “late binding”. Only the most general characteristics of language syntax are validated when code is written; whether a particular object has a particular property of a particular data type is not tested until code actually executes. This is how interpreted languages like Python, PHP, and javascript work. It provides tremendous flexibility, and it is often the solution of choice in the free-wheeling, ad hoc universe of general web apps. I am a big fan, in many cases. I love the way <a href="http://en.wikipedia.org/wiki/Representational_State_Transfer" target="wikipedia">RESTful interfaces</a> support ad-hoc connections, for example.

But late binding is not a panacea. For one thing, late binding typically means that development tools can't help you validate your usage very much. You end up writing and maintaining a lot of manual glue. For another, QA teams often push back against late-bound solutions because it increases the testing burden. Where a compiler could effectively validate millions of potential code paths at compile time for early bound code, testers struggle to achieve similar coverage. Result: bugs discovered later in the process. There is also a cost in performance and robustness that typically deters ISVs building standard enterprise or consumer applications.

There are subtler costs as well. When you late bind, you still have to use the interface you ultimately invoke, and the knowledge about how to use it has to be baked into the code ahead of time. It may not be baked in in the same way -- maybe you use reflection or <code>GetProcAddress</code> to find the <code>DoSomething</code> function you're after -- but to late bind an interface, you have to early bind all the logic that handles the cases where <code>GetProcAddress</code> fails.

Another disadvantage of late binding is that you introduce a new dependency -- this time on the supporting infrastructure. Maybe you're using a great SOAP toolkit for PHP and that toolkit makes it easy to late bind to a web service. But now you depend on your SOAP toit. What if another actor in your system doesn't have the same version of the toolkit?

What we'd like is a mechanism that combines the predictability and robust tool support of the traditional approach to interface versioning with the flexibility of late binding to get the best of both worlds. In <a href="decoupling-interfaces-as-versions-evolve-part-3.md">part 3</a>, I'll offer my own solution.
