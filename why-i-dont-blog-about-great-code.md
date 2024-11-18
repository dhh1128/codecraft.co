---
title: Why I don't blog about "great code"
date: 2012/10/03
slug: why-i-dont-blog-about-great-code
---

<p style="text-align:left;padding-left:30px;"><em>Last week I heard <a href="http://ttbook.org/book/carol-dweck-psychology-failure-and-success" target="_blank">a Stanford researcher describe</a> how failure can be a good thing, if we are prepared to learn from it.</em></p>
<p style="padding-left:30px;"><em>I agree, although this mindset is easier to describe than to achieve. So here I'm kicking off a new series of posts about mistakes I've made over the years, and what I've learned from them. Look in the "Mistakes" category for more like this.</em></p>
If you've followed my blog at all, you'll know that I regularly return to the theme of <a href="/category/good-code/" target="_blank">what constitutes good code</a>. Ever wonder why I don't get more ambitious and talk about "great code" instead?

A big reason is that in software, <em>great can be the enemy of good</em>.

If you're a fan of aphorisms, you've probably heard the opposite statement a few times: "good is the enemy of great." People who say this are emphasizing the value of setting lofty goals, and then aligning our day-to-day lives to deeply held priorities. They remind us that settling for mediocrity is almost guaranteed not to create deep meaning or purpose. And they are quite right.

However, I submit that the greatness you should be pursuing in software is less about producing great code, and more about becoming a great <em>producer</em> of code. And great producers of code know that most of their creations will not <a title="Good Code Is Optimized" href="good-code-is-optimized.md" target="_blank">optimize business value</a> if they aim for a magnum opus. Not every commission can be the Sistine Chapel.

[caption id="attachment_620" align="aligncenter" width="500"]<a href="http://en.wikipedia.org/wiki/File:Creaci%C3%B3n_de_Ad%C3%A1n_(Miguel_%C3%81ngel).jpg"><img class="size-full wp-image-620" title="Screen Shot 2012-10-02 at 10.10.04 PM" src="http://codecraft.co/wp-content/uploads/2012/10/screen-shot-2012-10-02-at-10-10-04-pm.png" alt="" width="500" height="222" /></a> Detail from the Sistine Chapel, by Michaelangelo. Image credit: Wikimedia Commons.[/caption]

Don't get me wrong. I care about the quality and artistry of code, and there is definitely great code out there. It's just that I've got these battle scars...

<strong>Daniel builds a tower</strong>

In 2001, I helped design and code <!--more-->a library--FileAccess--that isolated our cross-platform file system management applications from the quirks of various storage back-ends. Think of it as an early analog to FUSE. Traditional file systems would be wrapped by the library; so would robotic tape loaders, virtual tape drives, sockets, ftp and http endpoints, cloud storage, SANs, ISOs, and much more. Dependency injection would keep client code assumption-free; mixins would allow transform on file copy, depth- and breadth-first tree traversals, etc. The scope of what we were undertaking was ambitious, but we had our reasons; many C++ I/O libraries were primitive at the time, and we were doing industrial-strength disk-based backup.

One of the FileAccess tasks that fell to me was the design and implementation of a Path class to represent a URI in its most general form. Today, I'd just use boost::filesystem::path, but that wasn't an option back then. Our code was full of messy, error-riddled, redundant blocks that calculated file extensions, appended to a path, found a parent directory, and did similar calculations; we needed to factor it all into one place where the logic was thoroughly unit tested, and done right. We also needed the path to handle correct codepage conversions transparently, so file and folder names could be read from/written to on-disk structures appropriately.

In many ways, FileAccess was a great success. However, I look back on what I did with Path, and I think I got carried away.

<strong>Daniel builds a tower to get to heaven</strong>

Without a lot of justification, I decided to make Path do canonical casing (pass "hello.txt" to ctor, get "Hello.TXT" back after FS normalizes). I also figured that for logical completeness, it should calculate relative paths between A and B, allow non-contiguous multisegment subsets to be extracted in a single operation, whistle "Yankee Doodle," and walk the dog.

I wouldn't go so far as to say that Path was a disaster. In fact, it was pretty darn useful. But:
<ol>
	<li>It was complex. Bugs were subtle, with such far-reaching ramifications that only black-belt engineers were willing to modify what I'd written.</li>
	<li>Some of the features I implemented were never used.</li>
	<li>The canonical casing behavior incurred a performance penalty. Every ctor required a disk read. I later wrote a caching layer to compensate, but this had its own problems with complexity, order of destruction, and thread safety.</li>
	<li>The work I put into Path had an unknown but perhaps significant opportunity cost. What could I have written instead, if I'd kept Path simpler? After a few RIFs, you get religion about getting ideas into production asap, so you can earn revenue; distractions aren't innocuous.</li>
</ol>
These flaws only came into focus for me with 20:20 hindsight. At the time, I was young enough, and I <a title="Humility" href="humility.md">undervalued humility</a> enough, and Path was useful enough, that I only saw the upside.

<strong>The moral</strong>

I've had that same sort of experience many times since. Occasionally a tower I build creates chaos; more often, I realize after a while that I've overdesigned and overbuilt. Maybe I need to post these lines by Carl Sandburg near my desk:
<p style="margin-left:4em;">It has happened before.
Strong men put up a city and got a nation together,
And paid singers to sing and women
to warble: We are the greatest city,
the greatest nation,
nothing like us ever was.
And while the singers sang
and the strong men listened
and paid the singers well
and felt good about it all,
there were rats and lizards who listened
… and the only listeners left now
… are … the rats … and the lizards.</p>
<p style="margin-left:6em;font-style:italic;">(from "Four Preludes on Playthings of the Wind")</p>
I'd summarize the principle like this: Don't take your code too seriously. Write good stuff that solves the problems that clearly matter, and allow time and experience and the contributions of others to influence you. <em>You</em> are what should be great, not the code so much. Maybe this is another way of agreeing with Jesse Harris that code--most of it, at least--<a title="Code Isn’t Art" href="code-isnt-art.md" target="_blank">isn't best thought of as art</a>...
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Identify something that you've overdesigned or overbuilt. Try to quantify the opportunity cost.</span></em></p>

---

6 Strategies to Simplify Software | Codecraft (2013-03-12 08:57:31)

[...] In many, many cases, the complexity we wrestle with comes from an overly ambitious scope. Overbuilding is probably my greatest weakness as an architect; I’ve made the mistake way too often. [...]