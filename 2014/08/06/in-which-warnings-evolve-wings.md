---
title: In Which Warnings Evolve Wings
date: 2014/08/06
slug: in-which-warnings-evolve-wings
---

Ignoring warnings is a bad idea. At some level, we all know this. If we see a sign that says "Warning: Dangerous Undertow" at the beach, we pause (I hope!) and think twice before we get in the water.

[caption id="" align="aligncenter" width="538"]<a href="http://xkcd.com/1247/"><img class="" src="http://imgs.xkcd.com/comics/the_mother_of_all_suspicious_files.png" alt="" width="538" height="234" /></a> Ignore warnings at your peril. :-) Image credit: xkcd.com[/caption]

Yet we sometimes get cavalier about warnings in software. Specifially, I have heard programmers describe compiler warnings as being <em>less severe</em> than errors--as if worrying about them is optional.

This is simply not true.
<!--more-->

You have probably seen plenty of warnings that highlight serious problems; I know I have. And you've probably wrestled with annoying "errors" that tools should have fixed without bothering you--or suppressed in the first place.

<strong>What's your intent?</strong>

In general, compiler warnings aren't less severe than errors--they are simply <em>more ambiguous</em>. The compiler isn't sure whether a signed/unsigned comparison is evidence of logic mistakes, or is perfectly harmless. So it warns you, and lets you decide.

Warnings are evidence that the compiler needs to know more about your <em>intent</em>. (Does this sound like the "<a title="Lacunas Everywhere" href="http://codecraft.co/2014/07/16/lacunas-everywhere/">lacuna humana</a>" that I have been <a title="Thoughts On Bridging the “Lacuna Humana”" href="http://codecraft.co/2014/07/21/bridging-the-lacuna-humana/">harping</a> on lately?)

<strong>Messy ways to answer</strong>

One evidence that ambiguous intent is in play is that our usual method for eliminating warnings is to tweak code until the ambiguity is gone. If you're assigning a 64-bit number to a 32-bit number, and you explicitly cast the right-hand side to a 32-bit value, then there's no longer any question about whether you intend the truncation. The compiler notices your tweak, and the warning disappears.

Some warnings aren't susceptible to this approach. If the compiler warns you that you have unreachable code, you can delete it or <code>#ifdef</code> it, but there's no way to tell the compiler you intend it that way.<sup>[<a href="#1">1</a>]</sup> If you get a warning about a function being deprecated, you either have to stop calling the function, or live with the nag. If you want to avoid warnings about alignment and packing, you probably have to use <code>#pragma</code>.

<strong>Marks make it better</strong>

The <a title="Introducing Marks" href="http://codecraft.co/2014/07/24/introducing-marks/">marks</a> that I've <a title="Mountains, Molehills, and Markedness" href="http://codecraft.co/2014/07/28/mountains-molehills-and-markedness/">recently described</a> provide a nice, uniform solution to this hodgepodge of warning-answering mechanisms. Since they're evaluated at compile-time, they can play the same role that <code>#pragma</code> does in some languages. Sophisticated attachment and propagation get you away from all the silly push/pop gyrations. They can attach to any portion of the code DOM--functions, variables, statements, code blocks, classes, packages, applications--and they can express arbitrary semantics, including answers to any question the compiler dreams up. One simple, clean technique across the board.

<strong>But there's more...</strong>

However, I want to push our vision even further.

Imagine that you could address the compiler's questions (aka warnings) in powerful new ways:
<ul>
	<li>Yes, it's okay that I'm calling deprecated functions--but only on the old OS where I'm currently working, and only until we reach beta.</li>
	<li>I'm not worried about this exception as long as I have a unit test that proves we handle it in every caller in the call graph.</li>
	<li>Assume I know what I'm doing and build the binary anyway, because right now my goal is just to figure out what libraries I need on this new platform to make the port work. But don't let me accidentally check in anything that hides warnings from others.</li>
	<li>Ignore all the reassuring answers (about warnings) that I gave you in the past; if you went back to your paranoid state, what would you ask me about?</li>
	<li>Automatically expire all my answers about warnings next week, after we deliver a prototype that exhibits stubs for key features.</li>
	<li>Warn about problem X, and get an answer from every developer who edits this module, individually.</li>
	<li>I want to warn about constructs that are not traditionally represented in code, such as impractical use cases, insecure features, ill-defined personas, and so forth.</li>
</ul>
In order to provide this sort of experience to developers, you don't just need marks. You also need the ability to record answers about warnings <em>outside the code itself</em>, because different developers might have different answers for different circumstances, and because answers must expire or vary without the code changing.

But as soon as you answer warnings outside the code, you have a stability problem. Code changes; what was line 72 in your module yesterday might be line 93 today. It does no good to remember Fred's answer to warning W-2046 on line 72 of moduleX, if line 72 might have a different meaning each time we compile.

I want to support this powerful approach to warnings in the <code>intent</code> programming language, so I've been pondering the problem of stable references to code. I think I have some satisfying answers that make this vision for warnings achievable. I'll blog about code as hypertext soon. In the meantime, just assume it's possible--and not onerous for the developer.

Imagine, then, that in addition to baking answers to warnings directly into the code with marks, developers can layer additional answers like masks or filters. The team that's porting to Windows might have one shared mask; Fred and Sally might have their own personal filters on top of the team one. These filters can be checked in with code, and the compiler smartly decides what applies in the active context.

You can achieve something a bit like this today, if you create custom projects for each unique perspective on the same codebase, or if you make projects depend on environment variables to adjust their behavior. However, this is a maintenance nightmare, and you're working with a very blunt instrument, against the grain of the compiler. I've never seen it work well.

What I'm proposing is different because flexible, context-sensitive warning filters would be a first-class feature of the compiler. The expressiveness and propagation of marks, the code DOM and stable hyperlinks, and the ability to express sophisticated answers all combine synergistically to help warnings evolve wings.

I think those wings could lift the quality and artistry of our software.

[caption id="" align="aligncenter" width="640"]<img class="" src="https://farm6.staticflickr.com/5317/5876849912_6e0a74ee6d_z.jpg" alt="" width="640" height="427" /> Image credit: <a href="https://www.flickr.com/photos/pixx0ne/5876849912/sizes/z/">[ changó ]</a> (Flickr)[/caption] 

<hr style="width:60%;" />

<sup><a name="1"></a>[1]</sup> I can think of several reasons why you might want to do this. One is that you're making a temporary change, and you don't want to be bothered to delete something, only to have to reinsert it later. Another is that you may want to use dead code to force linkage. Or maybe you just want to be able to explore an alternate path by resetting EIP while you debug. A final reason is that you want to prove the code compiles (e.g., because it's quoted in documentation), even though you will never run it. This is the reason why you <a title="disabling gtest methods" href="https://code.google.com/p/googletest/wiki/AdvancedGuide#Temporarily_Disabling_Tests" target="_blank">disable gtest methods</a> but do not #ifdef them; continuing to compile them prevents staleness.

---

Exploring the Power of Deixis | Codecraft (2014-09-23 08:34:47)

[…] developers never notice, because we only worry about warnings until our current build succeeds. But what if you use a static code analyzer like Coverity? […]

---

Daniel Hardman (2014-08-07 11:35:49)

Thank you so much for thinking about this in depth, and asking smart questions, David!

I relate to your comment about getting warm fuzzies from a clean build. I also agree that deterministic build results is a big deal. A HUGE deal, actually. Having a build which is noisy on some platforms, or which becomes noisy in surprising ways, is not good. Perhaps the idea of expiring warnings on a date or after a milestone is therefore iffy.

However, I don't think this invalidates the whole idea. Git has a requirement that before you push, you must declare your identity. Take that one step further and imagine that the compiler wants to know who it's dealing with--a code owner, a casual downloader/reuser, a build slave... It might be the case that code owners invoke a much more demanding posture with respect to warnings than a casual downloader/reuser, and that build slaves refuse to ignore any warnings that could change their status non-deterministically. Just last night I was working with CMake and got a warning that said, "This warning is for internal project developers; if you're just using somebody else's cmake project, you can ignore it." So I know I'm not imagining this use case. That doesn't mean this is a good idea, though. Certainly, if you can drive ambiguity out of the codebase for everyone, permanently, that's better than leaving questions unaddressed.

Maybe the right solution is to allow warning filters to be changed, but only manually. I guess that's not much different from hand-editing a Makefile to add or remove -W switches; what I'm proposing is just a bit easier to use.

Regarding "TODO" lists, I'm not sure. Gonna have to noodle on that. Warnings as described here are basically questions intended to resolve ambiguity. Extending them to items that must be completed might or might not be a good idea.

---

David H (2014-08-07 06:58:11)

I often download and compile open-source software. As I watch the compile messages scroll by, I get a warm, fuzzy feeling when it just quietly compiles without warnings. On the other hand, when I get lots of noise about incompatible integer sizes and such, I don't feel so good about the software. Maybe some projects use gcc flags that suppress all warnings, but usually it seems like they either care about warnings and address them all, or else they don't care about whatever noise spews out at compile time.

I like the idea of more intelligent suppressing of warnings, where you have to more explicitly say why the warning does not apply in your situation.

I'm not as sure about warning suppression outside of the code itself: "different developers might have different answers for different circumstances, and because answers must expire or vary without the code changing." Typically the goal is to have deterministic build results. Having a whole boatload of warnings show up today that weren't there yesterday, or having one developer see warnings the other developer doesn't see, makes the build results less repeatable.

In the case of using warning suppressions that expire after the demo shipped -- The day after the demo ships, now all your pragmatic stubbed code generates warnings. Will you just ignore the warnings your build system produces while you transition from stubs to full production code? That could take weeks or months. Then are we back to habitually ignoring warnings? Or are you saying that the warning system has become the development TODO list? In that case, are you going to place the other development TODO items in the code as artificially generated warnings, to keep all of your TODO items in once place?

Sorry Daniel, just thinking this through out loud, I hope it helps.

---

David H (2014-08-07 16:26:27)

Having different sets of warning levels for different roles (maintainer, automated build system, end user) seems like it could be useful. I assume there would be a command-line switch that let's you easily switch roles. This of course resembles the warning level switches that compilers already support. But you are describing something more complicated that just an integer level for filtering warnings.

I wasn't really advocating using warnings as TODO lists, it just seemed like the particular use case was headed that direction. I believe warnings should be dealt with immediately. As you said, they represent ambiguity, and I don't want ambiguity to persist.

---

trevharmon (2014-09-08 23:49:52)

This article caused me to reflect on some of my coding experience with Perl where one has the ability in code through pragmas to not only disable different types of warnings (assuming they were turned on in the first place), but also disable strict code checking (e.g., variable declaration) (also assuming they were turned on) inline in the code. Annoying warning? Disable warnings in that particular block.

I've done this many times, almost always for one of the reasons you've listed above (i.e., the warning doesn't apply in this one particular case, "No, I really know what I'm doing", "sudo make me a sandwich", etc.). I din't always do it for the "right" reasons either.

Here's my concern, though. If it's in a bit of truly isolated code that no one else is ever going to call, fine. I no longer believe any code falls into that category. I have to assume anything I code will be called by someone else, for likely a completely different reason than its original design. I once saw an entire project of mine hijacked in that way. Oddly, they had issues later.

Any time I find a 3rd-party module that I'm calling deciding to suppress warnings in this way, I always get nervous. It isn't good to believe the compiler is omnipotent, but those warning rules have been put in there for a reason... usually because someone screwed something up... badly.

I know it's a royal pain to have to clean up warnings--especially the "silly" ones. I just wonder, do we want to encourage any of the behaviors that push us to not clean up warnings? I don't know. Clearly, we want a balance to be struck. Maybe marks can provide enough context to solve this problem without encouraging bad behavior.

I'm going to have to think on this a bit.

Thanks for always providing good food for thought!

---

Daniel Hardman (2014-09-09 09:04:58)

Trev: you have a dry sense of humor. "Oddly, they had issues later." First I chuckled. Then I cried. I can so, so relate. :-)

I totally agree that we don't want to encourage behaviors that make "cleaning up warnings" less important or less of a best practice. I wasn't thinking of marks having such an effect; instead, I was imagining that by making it possible to drive ambiguity out of code, they'd make warnings that remain much more likely to get the attention of coders. But now you've got me wondering whether marks might unintentionally become a big, clumsy hammer that encourages bad behavior. If so, that's awful.

Wheels are turning in my head...

Thanks for the thoughtful response.