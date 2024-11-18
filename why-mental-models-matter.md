---
title: Why Mental Models Matter
date: 2012-11-05
slug: why-mental-models-matter
---

As they leave school and embark on professional adventures, naive engineers believe their purpose is more or less summed up by this equation:
<p style="text-align:center;font-size:140%;">product = software = code</p>
As they get deeper into their careers, good engineers gradually realize that the raw code baked into a product is not everything. They come to appreciate the role that support folks and tech writers, marketers and professional services play in delivering value to the customer. Eventually many arrive at :
<p style="text-align:center;font-size:140%;">product = (software = code) + augment</p>
I'd put this equation into words as follows: the purpose of dev teams is to create products, which consist of software (a synonym for code) plus auxiliary offerings like support, documentation, and services.

<figure><img alt="" src="http://imgs.xkcd.com/comics/teaching_physics.png" height="226" width="500" /><figcaption>Equations capture mental models... Image credit: xkcd</figcaption></figure>

This is the level of sophistication at which much of the software industry operates. It is taught by academia (at least, if you <a href="http://www.marketingteacher.com/lesson-store/lesson-three-levels-of-a-product.html" target="_blank">listen to business professors</a>), and it's the philosophy that underpins lots of outsourcing decisions, as well as strategic mergers and acquisitions.

I think the second equation is better than the first, but it's still woefully inadequate.

<strong>Easy Critiques</strong>

For one thing, it ignores the interrelationships among software, hardware, enabling ecosystems, and customer communities. Products don't exist in isolation; they are part of an embedded system made possible (and relevant) by societal conventions and other technologies. "Microsoft Word" and "Adobe Photoshop" are not "products" for <a class="zem_slink" title="Bushmen" href="http://en.wikipedia.org/wiki/Bushmen" target="_blank" rel="wikipedia">Kalahari bushmen</a>.

For another, software is more than code. Notice the subtitle of my blog... Software includes people as a fundamental ingredient. In the shadows of every architecture diagram is an assumed human being (or an army of them), providing input or accepting output. How else do we think our systems will be installed, configured, optimized? How will our databases get populated, our backups get mounted, our e-books get typeset, or our web searches get chosen? (See my posts about <a title="Why People Are Part of A Software Architecture" href="what-role-are-you-playing-in-rpcd.md">role-playing in design</a>.)

Both of those critiques are important, I think. But today I have a different bone to pick.

<strong>The Deeper Issue</strong>

Whenever we put "product" at the front of equations that describe our industry's output, we make the implicit assumption that product is the major--or even the entire--output of tech companies. This assumption is ubiquitous and almost never articulated, let alone challenged. Ask a tech buddy about what his company does; he'll say something like "We build products that ___."

Of course, tech companies <em>do</em> build products--or solve customer problems by delivering products and services, if you want to make economists happy. But they also create another output, and I think this neglected stepchild deserves far more attention.

Besides products, tech companies produce and propagate mental models. Or in other words, they enable and shape our view of the world.

<figure><img class="zemanta-img-inserted zemanta-img-configured " title="Mental Model II" alt="" src="http://farm5.static.flickr.com/4057/4612823598_a82864475e_m.jpg" height="164" width="240" /><figcaption>Photo credit: daveelf (Flickr)</figcaption></figure>

These mental models of the world matter. They--not products--are the nuggets of gold for which we prospect. Ask Galileo.

How much of popular culture is built on scaffolding provided by an idea that used to exist only in the mind of an engineer? Engineers didn't just dream up plasma TVs or radios; they enabled the very idea of broadcasting. They didn't just figure out how to download files from the internet; they convinced us to think of data blobs in terms of files and folders in the first place. They didn't just populate the App Store; they thought the concept of "app" into existence. I could go on and on with examples, but I'll leave that as an exercise for the reader.

As I said in <a title="// Comments on Comments" href="comments-on-comments.md" target="_blank">my post the other day about comments</a>, the mental models created by engineers are the most valuable output of the tech industry.

<strong>MVP</strong>

Products are directly sellable, and we have to have them. But products without mental models are pretty darn useless. If you doubt me, try using a sophisticated piece of software without any idea how to think about its <a class="zem_slink" title="Problem domain" href="http://en.wikipedia.org/wiki/Problem_domain" target="_blank" rel="wikipedia">problem domain</a>. If you know nothing about accounting, try to use Great Plains to be a bookkeeper. If you know nothing about graphics, try airbrushing an image in Photoshop. If you know nothing about <a class="zem_slink" title="High-performance computing" href="http://en.wikipedia.org/wiki/High-performance_computing" target="_blank" rel="wikipedia">HPC</a>, try keeping <a href="http://www.npr.org/blogs/alltechconsidered/2012/10/29/163894669/why-is-this-supercomputer-so-superfast" target="_blank">Cray's latest supercomputer</a> busy doing protein folding.

Code is important, but without a <a class="zem_slink" title="Mental model" href="http://en.wikipedia.org/wiki/Mental_model" target="_blank" rel="wikipedia">mental model</a> of how that code works, it's not much of a foundation for a product. (This is why outsourcing that doesn't involve bi-directional knowledge transfer is usually foolish, and why acquiring a company and RIFing all its employees nets the acquirer a lot less than they bargained for.)

Patents look nice in a war chest, but it's sophisticated mental models, not patents, that are the prerequisite of innovation.

<strong>Implications</strong>

If you understand that tech companies produce mental models, then certain issues take on new significance.

<a title="Paying Off Technical Debt" href="paying-off-technical-debt.md">Tech debt</a> isn't just insidious because it makes code ugly. A kludge lets us get by with a flawed, ill-developed mental model of a problem domain--and if we build on that model, eventually we create a house of cards. Bad mental models bite us, sooner or later.

Competition in a turbulent market is often decided by who has the better mental model. "Better" might mean the one closer to the predilections of the customer, or the one that has better long-term applicability.

Usability is all about conveying a mental model with minimum effort on the part of the receiver--and then using that model consistently and easily.

A product that doesn't improve the mental model of the customer (e.g., by pruning unnecessary clutter, by visualizing connections that were previously impossible to see, by accounting for a neglected issue that's been a thorn in the side) is not innovative, no matter which features it touts. It is providing little of value, and will end up on the dust heap of history.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Take a minute to ponder how much of your passion and talent is actually centered on the "other" output from product development. What contribution have you made to a helpful mental model for a customer? Where have you invented a term that resonated, or formalized a process that used to be chaos? </span></em></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="on-usability-evaluations-and-mental-models.md" target="_blank">On Usability Evaluations and Mental Models</a> (jackskchang.wordpress.com)</li>
	<li class="zemanta-article-ul-li"><a href="export-print-save-as-the-evolution-of-mental-models-along-with-mechanical-models.md" target="_blank">Export, Print, Save As: The evolution of mental models along with mechanical models</a> (jackskchang.wordpress.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://java.dzone.com/articles/knowledge-vs-superstition" target="_blank">Knowledge vs Superstition</a> (java.dzone.com)</li>
</ul>

---

Julie (2012-11-06 09:53:14)

You finally put into words what has been bothering me for years. I often compare some of the early successes in personal computing to the current offerings, MacWrite vs MS Word for example. The mental model was so clean and clear that understanding and use was intuitive. For all the complaints people have about functionality, or lack thereof, Notes on the iPhone has a usable mental model. I challenge anyone to produce a good mental model of MS Word.
Finally, from a developer perspective a good mental model lowers the cost of implementation and maintenance. Even more, a good mental model produces a simpler design which makes software more reliable and scalable. The catch is (of course there is always a catch) that a really good mental model takes hard work to develop.



---

Daniel (2012-11-07 22:14:50)

Trev: very astute observation that there are horrible, mediocre, and good mental models. I've seen a lot of cases where a program wants people on the outside of a program to think in terms of its internal data structures, which is very regrettable. Sigh...

I had forgotten the eject-via-trash problem on the Macs, but that example brought it all back. I winced many times myself. When I was unfamiliar with the expected behavior, I think I may have actually used a pin to manually eject from a disk drive rather than try the trash. Definitely a case where the chosen metaphor did the user a horrible disservice.







---

Daniel (2012-11-05 11:44:36)

Low effort on the part of the developer is always desirable, of course. :-)

---

dougbert (2012-11-05 08:43:22)

wow - "Usability is all about conveying a mental model with minimum effort on the part of the receiver--and then using that model consistently and easily."  and add "on the part of the sender (developer) as well".



---

Trev Harmon (2012-11-07 21:45:12)

I think one thing forgotten by many programmers is by its very existence a program requires a mental model. In the worst case, the mental model is not even considered by the programmer, leaving one with a convoluted representation of a stream of conscience--not particularly helpful beyond the original implementation session. This is closely followed by a "designed" mental model that is simply an outward manifestation of the internal data structures. I find it infinitely frustrating to be presented with a program or API that requires me to fully understand the entire mental model before being allowed to do the simplest task because I must fully "explain" the context to the system through complex calls or data structure construction.

One principle from general design is that of intent. In order for a physical object to truly have meaning to a human, it must be imbued with intent. Not only must the object exist, it must exist in order to fulfill an intent of its owner. [ See http://www.ted.com/talks/john_hockenberry_we_are_all_designers.html ]

I think programmers often get confused when putting together mental models, meaning they imbue the mental model with their own intents and not those of their users. The mental model is the basis upon which rests all the rest of usability, as it is what will determine, to some extent, affordances, natural interactions and expected cause-effect relationships. Of course, when designing APIs, the model will naturally bend more towards that held by the original programmer. But, in almost every other case, the mental model held by the programmer would become a ball and chain when shackled to the user.

Bad mental models will always result in poor UI decisions and bad usability, because UI is really just a visual/tactile projection of the mental model. If at all possible, mental models should mimic the real world in which we live. At a minimum, they should not contradict it. I think the best example of this, tying together mental model, UI and usability, comes from some of the dark years in Apple's past. Every time--every single time--I ejected by floppy disk by dropping it into the trash can, there was a twinge of fear, "Perhaps this time, instead of preserving and returning that which held many hours of work, the trash can would perform its other function, the complete and utter destruction of all that entered into it." To preserve something I cherished, I would never through it in the trash. Reality contradicted... mental model broken... intent subverted... UI failure.

---

3 Commandments of Performance Optimization &laquo; Codecraft (2013-01-08 09:08:38)

[...] is useful to learn certain rules of thumb. We have to have a mental model that lets us make simplifying predictions, such as “It’s probably going to be a waste [...]

---

Daniel (2012-11-06 10:32:48)

Good point about MS Word, Julie. You made me think of the old adage that eventually all programs evolve to send email. :-)

>>> Good mental model takes hard work to develop

Amen. Albert Einstein: “Any fool can make things bigger, more complex, and more violent. It takes a touch of genius-and a lot of courage-to move in the opposite direction.”

---

Interrupting my interruptions &laquo; Codecraft (2013-01-24 11:48:44)

[...] is both a tool and an end unto itself. Those meetings I’m attending (or calling) are how I develop shared mental models, motivate and teach, manage momentum, and put a stake in the ground. Those wikipedia pages and chat [...]





---

Why Software Artisans Should Manage Their Influence &laquo; Codecraft (2013-02-07 08:49:25)

[...] of his thinking to our field. Since so much of what we do requires buy-in, coordination and shared mental models, we have to be savvy about how we communicate, advocate, and train. Assuming equal technical [...]























