---
title: Why you should be proficient in a tool like vim or emacs
date: 2014/05/15
slug: why-you-should-be-proficient-in-a-tool-like-vim-or-emacs
---

In my last post, I pointed out <a title="Why you should use an IDE instead of vim or emacs" href="why-you-should-use-an-ide-instead-of-vim-or-emacs.md">two little-discussed reasons why I think most engineers should spend most of their time in an IDE</a>.

I knew I was venturing into the realm of religious wars to make such a claim. When I shared the post, the first comment I got was, "Do you have a death wish?" :-) I had to laugh.

[caption id="attachment_5591" align="aligncenter" width="646"]<a href="http://uploads0.wikipaintings.org/images/gustave-dore/the-army-of-the-second-crusade-find-the-remains-of-the-soldiers-of-the-first-crusade-1877.jpg"><img class="size-large wp-image-5591" src="http://codecraft.co/wp-content/uploads/2014/05/screen-shot-2014-05-15-at-1-47-38-am.png?w=646" alt="Religious wars aren't pretty. "The Second Crusaders Encounter the Remains of the First Crusaders", by Gustav Dore (wikipaintings.org)" width="646" height="789" /></a> Religious wars: not so pretty. "The Second Crusaders Encounter the Remains of the First Crusaders", by Gustav Dore (wikipaintings.org)[/caption]

It turns out that my experience with the ensuing comments has been quite positive. Plenty of people disagreed with me, which is fine. I've heard good arguments from many different perspectives, which is part of the reason why I blog and post on social media in the first place; <a title="Humility" href="humility.md">I need to be pushed</a>. I hope my assertions about teamwork and gestalt were at least interesting.

Now, I promised that I'd write a follow-up post about the flip side of my advice. This isn't because I can't make up my mind; it's because I see these two toolings as complements with some overlap rather than symmetrical alternatives.

So today, I'm going to try to convince all the IDE zealots in the world that they're doing themselves and their teammates a disservice if they don't <a title="Julie Jones: Learn voraciously." href="julie-jones-learn-voraciously.md">take the time to become proficient</a> in a powerful text editor.

Death wish part 2. :-)<!--more-->
<h3>The obvious reason</h3>
In response to my first post, plenty of people pointed out the one use case where text editors totally crush IDEs: when a console is all you have to work with.
<p style="padding-left:30px;"><span style="color:#003366;"><em>"I really love to <code>ssh -X</code> to a server, get permission from the sysadmin to monkey with packages and consume scarce resources, install KDE or gnome, install an IDE, run <code>startx</code>, browse to the folder where the IDE's binary is installed, launch it, and then wait 5 minutes while it loads in the local X-server on whatever workstation I happen to be using"</em> </span><strong>... said no one ever.</strong></p>
The need to edit files on remote machines with minimal cruft installed is never going to die. For some developers, this is a constant workflow; for others, it's occasional. But almost none of us can ignore it entirely. In fact, given the surging tide of mobile computing and "Internet of Things" innovation, every passing day is probably increasing the probability that software pros will need to tweak files and debug in very resource-constrained, streamlined environments.

This reason by itself justifies the claim that every developer should at least be <em>functional</em> in a high-powered text editor--and I think it's incontrovertible.

But is that the same as proving that every engineer should be <em>proficient</em>?

To justify the stronger form of my assertion, I need to tell you a story.
<h3>Learning the web</h3>
I first encountered http and web browsers when a friend showed me Mosaic 1.0 in about 1993. That is ancient history in Internet time. "I grow old, I grow old; I shall wear the bottoms of my trousers rolled."

An hour after my first exposure, I had scanned an html tutorial and was attempting my first experiments with <code><b></code> and <code><hr></code>. Wow! I could make pretty stuff appear on the screen!

Since then, I have debugged over-the-wire web interactions in ethereal (now wireshark); discovered Netscape's newfangled "cookie" mechanism; suffered through javascript 1.0 implementations in (gag!) IE 3.0; designed my own server-side directive language before finding ColdFusion; explored ASP and modcgi, then JSP, then raw PHP, then MVC; played with modwsgi and modrewrite; played with SOAP; become a veteran of RESTful web services; stumbled upon CSS 1.0 and user-agent sniffing, then waited impatiently for enhancements; written C++ and python and java implementations of http 1.0, then http 1.1; and on and on.

All of these battlescars change the way I understand the web.

Some of my younger coworkers got their first technical introductions to the web after the dot com boom, when Google was a billion-dollar company, Facebook had already been invented, and CSS 2.0 was supported by every browser on the planet.

Sheesh.

They may understand some things better than I do. I'm not fully up-to-speed on html5, for example, and I never got around to mastering actionscript. My jquery kung fu is weak.

However, I really, truly get what is happening under the layers that we've added in the past two decades, and there are lots of times when that knowledge pays off. I don't need WYSIWYG or wordpress themes to make html pretty (in fact, I detest their interference). I have an intuitive sense for when an ajax call is going to be inefficient. I know how caching proxies and http etags interact.

Other engineers could tell similar stories from their own careers--about how they learned assembly first, and then migrated through C to C++--and how that foundation helps them write <a title="What Is “Good Code”?" href="what-is-good-code.md">better code</a> than a young upstart who learned first in C++.

What does this have to do with vim and emacs?

<strong>Back-to-basics programming</strong>

Well, I claim that if you only ever see the <a title="The Power of Simplicity" href="the-power-of-simplicity.md">complexity of software engineering</a> through the lens of an IDE, you have missed an important--even revelatory--learning experience.

When you code and debug in a text editor, living and dying by your proficiency there, you are essentially repeating the learning curve that the entire world computer science community lived through in the first several decades of its existence. You know the difference between a compiler and a linker and an assembler. Makefiles start making sense. The vagaries of preprocessor troubleshooting and the paths that a debugger uses to resolve symbols <a title="Why Mental Models Matter" href="why-mental-models-matter.md">lose their mystery</a>. You master regular expressions. Arcane command-line options in git may even feel self-explanatory. (Maybe. :-)

Euclid said there was no royal road to geometry. You have to pay the price to learn the foundations before you can soar with the fancy stuff.

To me, that's the most compelling reason to go beyond "functional" and actually get productive with vim or emacs--if you specialize in an IDE without a text editor in your repertoire, you have <a title="On SEPs, Squirrels, and Meta Questions" href="on-seps-squirrels-and-meta-questions.md">gaps in your experience</a>. An IDE makes parts of your ecosystem invisible; a text editor teaches you just how robust and amazing and satisfying that underlying ecosystem is. You learn some humility toward the pioneers in the field, who did so much with such a lean toolkit. And you learn not to drink all the IDE kool-aid without at least rolling your eyes occasionally.

<strong>Where I'm at</strong>

I said in my last post that most developers should prefer to use an IDE, and I stand by that recommendation, for the reasons that I gave. I cheerfully admit that there are exceptions to my rule; don't flame me if you can duel in elisp with one hand tied behind your back.

But in addition, I also recommend that all developers take the time, at least during one stage in their career, to become proficient in the more spare, more low-level experience that text editors offer.

And I stand by that recommendation, too.

---

Scott (2015-09-25 15:49:42)

> get permission from the sysadmin to monkey with packages 

Umm, no.

---

digitallyfreeblog (2017-03-19 03:07:11)

I just saw your blog post.  I have moved from Eclipse (well almost ) to Emacs for Python programming.  I stress the word Python, because for Java I think Eclipse still rocks.  But for all other reasons you rightly mentioned, plus the fact that now Emacs is also kind of IDE, auto completion, intelisence, code highlighting, Project system through plugins, integration with things like git and on and on.  I always knew that this potential existed at least in Emacs.  So I always kept my touch on Emacs.  And now it pays off.