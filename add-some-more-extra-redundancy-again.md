---
title: Add some more extra redundancy again
date: 2014-01-15
slug: add-some-more-extra-redundancy-again
redirect_from:
  - /2014/01/15/add-some-more-extra-redundancy-again
---

It's the season for coughs and sniffles, and last week I took my turn. I went to bed one night with a stuffy nose, and it got me thinking about software.

What's the connection between sniffles and software, you ask?

Let's talk redundancy. It's a familiar technique in software design, but I believe we compartmentalize it too much under the special topic of "high availability"--as if only when that's an explicit requirement do we need to pay any attention.

<figure><img alt="" src="http://farm5.staticflickr.com/4001/4542478114_1a3356d435.jpg" width="500" height="333" /><figcaption>Redundancy can be a big deal. Image credit: ydant (Flickr)</figcaption></figure>

<span style="color:#333399;"><strong>Redundancy in nature</strong></span>

Mother Nature's use of redundancy is so pervasive that we may not even realize it's at work. We could learn a thing or two from how she weaves it--seamlessly, consistently, tenaciously--into the tapestry of life.

Redundancy had everything to do with the fact that I didn't asphyxiate as I slept with a cold. People have more than one sinus, so sleeping with a few of them plugged up isn't life-threatening. If nose breathing isn't an option, we can always open our mouths. We have two lungs, not one--and each consists of huge numbers of alveoli that does part of the work of exchanging oxygen and carbon dioxide. <!--more-->Even when one lung is damaged and the other is clogged, we keep on oxygenating our blood. Amazing, when you think about it.

<strong><span style="color:#333399;">One example of redundancy in software</span></strong>

It's not hard to find examples of redundancy in software. Consider streaming video on demand. You are probably well aware of the redundancy involved in TCP's reliable and ordered delivery guarantees. You can imagine the redundancy in Netflix's data centers, and maybe you know all about CDNs and adaptive routing on the internet. But giving you a good viewing experience goes well beyond that. The video source you select often includes multiple sources--high, medium, and low quality--and your browser selects among them based on auto-detected bandwidth constraints. There's a fallback mechanism to gracefully degrade. The browser downloads video in chunks, and it tries to stay ahead of the point of playback. That means it's got both a live and a cached source of data to manage. Codecs are designed to be able to interpolate missed frames if bandwidth gets scarce. Audio is separable from video so video frames can be dropped while preserving continuous sound. If you're watching on your iPad, you may have both a wireless and a cell phone network that the device can use to stream content. The CPU that renders video can offload chunks of work to a GPU when it's more efficient--but it can also decompress and rasterize and texturize and all the rest of it, all on its own. The list goes on and on.

<span style="color:#333399;"><strong>Not always good</strong></span>

Of course, not all redundancy is useful. You can get carried away with it :-)

<figure><img alt="" src="http://farm4.staticflickr.com/3083/2784568095_f01a2324a2.jpg" width="500" height="375" /><figcaption>image credit: da.bo (Flickr)</figcaption></figure>

In coding tasks, redundancy is often your enemy. Lots of antipatterns are undesirable precisely because they create redundancy that's difficult to understand and maintain. <a title="How to turn coding standards into epic fails — or not" href="comments-on-comments.md">dumb comments</a> are notorious for creating busywork this way.

<span style="color:#333399;"><strong>Food for thought</strong></span>

With caveats acknowledged, here are a few ways that redundancy might be under-represented in our design and coding:
<ol>
	<li><strong>Do we create user experiences that convey the same information in more than one way?</strong>
<div style="color:#777;padding:1em;">For example, do we highlight selected items by color, size, and a visual "wiggle," instead of only by drawing a rectangle? When we finish an operation, do we reset the focus AND play a sound AND display a message? This is best practice for busy users that pay imperfect attention. It's also a big help for folks who are color blind or visually impaired, which is why it's a requirement for <a title="UX, usability, Section 508" href="http://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973" target="_blank">Section 508 compliance</a>.</div></li>
	<li><strong>Do we have multiple ways to <a title="Why Your Software Should Cry" href="why-your-software-should-cry.md">get someone's attention</a> when something goes wrong?</strong>
<div style="color:#777;padding:1em;">It's all well and good to log errors--but what if the error we're logging is that we just ran out of disk space on the volume where the log file lives? Whoops...</div></li>
	<li><strong>Do our architectures distribute responsibilities, instead of assuming a single, centralized point of failure?</strong>
<div style="color:#777;padding:1em;">This is more than just recognizing the dangers in having one box on a diagram labeled "manager" or "database" or "authentication master", and compensating in "HA mode" by having a backup. It means thinking about network pipes and protocols and firewalls with a redundancy mindset. It means figuring out how clients can be temporly autonomous to tolerate hiccups, how to use caching intelligently, and so forth.</div></li>
	<li><strong>Do we sanity check in enough places?</strong>
<div style="color:#777;padding:1em;">Of course we need to sanitize user input to avoid SQL injection. We need transactions and CRCs. But do we build byte order detection and version stamp checks and sizeof and alignment tests in the right places? Are we using design-by-contract to <a title="On bread recipes, maps, and intentions" href="why-exceptions-arent-enough.md">test for errors</a> in enough places?</div></li>
	<li><strong>Do we avoid depending on a single person to make our system work or to troubleshoot?</strong>
<div style="color:#777;padding:1em;">If we say, "the admin will solve that problem if the user runs into it," we're probably letting ourselves off too easy. If we say, "the admin will call tech support," we're probably letting selves off too easy.</div></li>
	<li><strong>Do we carefully plan, code, test, and document for graceful degradation?</strong>
<div style="color:#777;padding:1em;">Less than ideal paths through code aren't an afterthought. Even if they're lelikely on average, the chances that <a title="A Comedy of Carelessness" href="dont-forget-the-circuit-breakers.md">circuit breakers</a>, helpful error messages, documentation about what to do when things aren't perfect, APIs that protect themselves from unwise callers, retries, timeouts, and alternate solutions.</div></li>
</ol>
Redundancy has a cost. We need to use it judiciously; <a title="Good Code Is Balanced" href="good-code-is-balanced.md">good code balances many considerations</a>. Nonetheless, I think pondering the issues above is likely to improve the robustness and aptness of our software in many cases. Our users will love us for it.

Now go out and add some extra redundancy again. And don't forget to not neglect to build in some secondary alternate failsafes, while you're at it. :-)