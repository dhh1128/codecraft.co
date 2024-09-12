---
title: Decoupling Interfaces as Versions Evolve, Part 3
date: 2008/08/19
slug: decoupling-interfaces-as-versions-evolve-part-3
---

<em>This is part 3 of a series. You can read <a href="http://techknowledgeme.wordpress.com/2008/07/29/decoupling-interfaces-as-versions-evolve-part-1/">part 1</a> and <a href="http://techknowledgeme.wordpress.com/2008/07/30/decoupling-interfaces-as-versions-evolve-part-2/">part 2</a> as well.</em>
<h3>Quick Review</h3>
We want all the encapsulation and data hiding benefits that interfaces provide. We want to be able to version our interfaces so consumers can depend on them reliably, but we don't want the producer and consumer of an interface to have to coordinate tightly. We don't want the producer of an interface to have to version so often that there's a built-in disincentive to follow best practice. And we want all the compiler and IDE benefits that early binding typically offers to a programmer.

I claim that no current solution really provides all of this -- not COM, not SOAP-based web services, not late-bound REST web services.

Fear not. 

<h3>Summary of Solution</h3>
<ol>
	<li>The provider of an interface and the consumer of an interface each conform to a compiler-enforceable contract (.wsdl/.idl/etc.), but unlike the traditional approach, these contracts are allowed to differ.</li>
	<li>The test of whether the two interfaces are compatible is not done by traditional casting, but by testing the contents of the two sides for semantic equivalence – a consumer has a compatible interface if it is a <em>semantic</em> subset of the provider’s.</li>
	<li>The consumer is required to write wrapper classes that forward from its own interface to that of the provider. (Using a language that supports reflection, like Java or C#, makes this task trivial).</li>
</ol>
<h3>

[caption id="attachment_45" align="alignnone" width="128" caption="Alternative Approach"]<a href="http://codecraft.co/wp-content/uploads/2008/07/alternative.png"><img class="size-thumbnail wp-image-45" src="http://codecraft.co/wp-content/uploads/2008/07/alternative.png?w=128" alt="Alternative Approach" width="128" height="84" /></a>[/caption]</h3>
<h3>The Gory Details</h3>
This solution could be built on top of COM, RPC-over-soap-style web services, or a RESTful service interface more analogous to document-oriented web services. Other environments such as CORBA/EJB may also be candidates, though I am less familiar with the details there.

Most SOAP comm pipelines get a remote object and deserialize it to a tightly bound object type in a single step, using a type cast as a runtime check that the remote source meets the calling code’s expectations. Such code would have to change so a remote object is fetched and deserialized in an initial step, and subsequently, the standard cast is replaced with a function that creates a wrapper object from the local interface if compatibility tests pass.

[caption id="attachment_46" align="alignnone" width="128" caption="TryCast Pseudocode"]<a href="http://codecraft.co/wp-content/uploads/2008/07/trycast.png"><img class="size-thumbnail wp-image-46" src="http://codecraft.co/wp-content/uploads/2008/07/trycast.png?w=128" alt="TryCast Pseudocode" width="128" height="76" /></a>[/caption]

In COM code, the analogous initial step must return an IUnknown; the second step consists of composing the semantic union of all interfaces the IUnknown supports, and then using that überinterface as the basis for compatibility testing. Since IUnknown does not support enumeration, the semantic union of all interfaces in an IUnknown would require a list of possible IIDs to perform a series of QueryInterface calls, or a low-level analysis of the object’s vtable.

In a RESTful document-oriented web service, a URL returns an xml document that describes an arbitrary object using structural elements that do not vary across returned object type. For example, instead of
<blockquote><code><book><title>Dragon’s Egg</title><author><fname>Stephen</fname><lname>King</lname></book></code></blockquote>
you have
<blockquote><code><doc><prop name=”title” type=”string”>Dragon’s Egg</prop><prop name=”author”>Stephen King</prop></doc>
</code></blockquote>
or something similar. This conveys the object’s semantic constraints along with its data, much like sending a table definition along with a tuple in response to a DB query. The initial step of deserialization constructs a generic object; the second step tests compatibility against the semantic constraints embedded directly in the document and constructs an instance of a wrapper class on success.

It’s important to distinguish between read-only and read-write usage patterns in this mechanism. Consumers of an interface that only intend to display data are infinitely backward compatible if the runtime check for semantic compatibility passes, regardless of the version numbers/guids in play under a given scenario, because the wrapper classes depend on an interface mapping that’s generated dynamically at runtime. However, if a consumer of an object wants to update its state at the source, the wrapper class must contain every property that the provider will require – or else the provider must set such properties either before serving the object or when the update is requested. Using wrapper classes rather than the traditional generated SOAP stubs is an important element of this mechanism because this allows mods to objects that a client does not fully understand.

[caption id="attachment_55" align="alignnone" width="128" caption="New Approach - Pros and Cons"]<a href="http://codecraft.co/wp-content/uploads/2008/07/alternative-pros-and-cons.png"><img class="size-thumbnail wp-image-55" src="http://codecraft.co/wp-content/uploads/2008/07/alternative-pros-and-cons.png?w=128" alt="New Approach - Pros and Cons" width="128" height="79" /></a>[/caption]

---

Decoupling Interfaces as Versions Evolve, Part 2 &laquo; Codecraft (2013-02-21 11:58:39)

[...] is part 2 of a series. You can read part 1 and part 3 as [...]

---

Decoupling Interfaces As Versions Evolve, Part 1 &laquo; Codecraft (2013-02-21 11:54:59)

[...] look at some approaches to that goal, and discuss why they still leave me unsatisfied. In part 3, I’ll offer my own [...]