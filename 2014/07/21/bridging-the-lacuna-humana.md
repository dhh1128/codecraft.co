---
title: Thoughts On Bridging the "Lacuna Humana"
date: 2014/07/21
slug: bridging-the-lacuna-humana
---

In my <a title="Lacunas Everywhere" href="../../../2014/07/16/lacunas-everywhere/">previous post</a>, I discussed the semantic gaps that afflict current programming languages. These gaps are caused by tools focusing on syntax and parsing, and mostly neglecting human factors.<sup>[<a href="#1">1</a>]</sup> I'm not just talking about the fact that languages are clumsy for us to use (more about this later); I'm saying that they ignore our need to talk about important realities of software development: security, coding habits, testability, maintenance plans, dependency management, requirements, intellectual property, and much more.

All this stuff falls within our scope of concern, but none of it is describable in our languages. That's weird. Imagine we hired a general contractor to build our house, and he was great at swinging hammers and leveling studs. But as soon as we asked him questions about building permits or hiring subs or choosing the right kind of concrete for the foundation, he acted like he didn't have a clue what we were talking about. We'd be likely to end up with lots of false starts, poorly met requirements, endless kludges, tons of frustration, a heavy QA burden. Hmm... That sounds familiar.

I call this lack of semantic continuity the <em>lacuna humana</em> -- the human gap.

The good news is, gaps can often be bridged.

<figure><img src="https://farm4.staticflickr.com/3462/3892862441_b574a8f9e7_z.jpg" alt="" width="640" height="428" /><figcaption>image credit: <a href="https://www.flickr.com/photos/vestman/3892862441/sizes/z/" target="_blank">vestman</a> (Flickr)</figcaption></figure>

I promised I would describe a bridge that has a lot of virtues, and I'm going to begin that work here. It might take us a couple posts to get all the way across, though. Thanks for hanging with me...

<!--more-->
<h3>How We Transmit Meaning With Normal Language</h3>
Before I lay out my solution, let's think about possibilities.

Human languages have a rich toolkit to draw from. Meaning is conveyed through words and sentences, of course--but also, through intonation, register, gesture, pronunciation, cultural allusion, and a host of other techniques. Importantly, all of these mechanisms depend in one way or another on shared context. If I say "What is your favorite color?" with just the right intonation and just the right British accent, and you're a Monty Python fan, I suspect I can get a laugh out of you, due to many of these extra channels of meaning. If you point out misbehavior, and I say, "I'm shocked! Shocked!"--and you've seen <em>Casablanca</em>--you'll grin cynically, for similar reasons.

http://www.youtube.com/watch?v=HMIyDf3gBoY

In this post, I'm making heavy use of metaphor (lacuna, bridge, toolkit). If you speak a latin-based language, you might have picked up on the common origin of "lacuna" and English "lagoon", and appreciated the way these metaphors relate to the picture above. You might even have snorted at the whiff of double entendre in my Monty Python allusion, since the scene is all about a "bridge of death."

Meaning is a layered, complex, fascinating phenomenon...
<h3>How We Transmit Meaning Through Code</h3>
The core content-carrying mechanisms in programming languages are obvious: sequences of declarations, assignments, and conditionals; functions; classes; and so forth. Those help us build words and sentences out of <a title="nouns and verbs in programming languages" href="http://steve-yegge.blogspot.com/2006/03/execution-in-kingdom-of-nouns.html" target="_blank">nouns and verbs</a>. But what are the analogs to the rest of the toolkit? And could any of them help us build a bridge?

<strong>Keywords</strong> are one possibility. The <code>const</code> keyword in C++ carries important semantics, and in doing so it extends the semantic inventory that C originally provided. D's <code>immutable</code> and java's <code>final</code> and <code>abstract</code> play similar semantic-expanding roles. Several languages support <code>static</code>. Could we just add lots of new keywords? Walter Bright (creator of D) <a href="http://www.drdobbs.com/architecture-and-design/so-you-want-to-write-your-own-language/240165488?pgno=1" target="_blank">pointed out</a> that we have no shortage of words we could formalize...

I appreciate the power of keywords, but unfortunately, I think this approach has limited value. The problem is that the set of possible semantics we want to talk about is very large, and impossible to predict <em>in toto</em> at the time a standard is written. Partly, this is due to semantic innovation in the community. If you move in usability circles, you've certainly encountered the notion of Human-Centered Design (HCD)--but maybe not the new-fangled idea of <a title="Role-Play Centered Design" href="../../../2012/06/20/role-play-centered-design/" target="_blank">Role-Play Centered Design</a> (RPCD). First we had Test-Driven Development (TDD); then we got <a title="BDD" href="http://dannorth.net/introducing-bdd/" target="_blank">Behavior-Driven Development</a> (BDD). The other day I ran across <a href="https://code.google.com/p/robotframework/wiki/ATDDWithRobotFrameworkArticle" target="_blank">ATDD</a>, and who knows what *DD we'll come up with next year.

More importantly, some of the meanings we need to talk about are unique to a particular team. My current employer categorizes the entire Internet into roughly 100 different content buckets--sites might be identified as Sports, Gambling, Porn, Malware Sources, etc. These categories are somewhat fluid; Pay To Surf used to be a meaningful category, but has long since faded from the radar. When a committee meets and determines that adjustments to the category inventory are warranted, software needs to react. Tests need to be recoded, and their input data files adjusted; weighting algorithms in Bayesian filters require tweaking. And these changes need to be delicately calibrated against milestones in our release cycle.

Our team needs to talk about these organizational realities in the code that embodies our major work product. We can't depend on standards committees to anticipate all our conversation topics and pre-load programming languages with keywords to help us.

<strong>Compiler Extensions</strong> are another useful way to imbue code with extra meaning. The industry has a long history of using this technique as a pressure-release valve for standards that have lagged behind the needs of the community. MSVC has lots of compiler-specific extensions. Or maybe you're familiar with GCC's <a href="http://unixwiz.net/techtips/gnu-c-attributes.html" target="_blank"><code>__attribute__((format(printf,m,n)))</code></a> or <a href="http://pimiddy.wordpress.com/2012/04/20/pure-functions-in-cc/" target="_blank"><code>__attribute__((pure))</code></a>. Have a look at <a href="http://gcc.gnu.org/onlinedocs/gcc/Function-Attributes.html" target="_blank">this page from gcc docs</a> to get a flavor for all the other cool things you can do.

Extensions have their place, but I see them as filling a few targeted gaps, rather than the whole gulf of the <em>lacuna humana</em>. Like keywords, you just can't get enough of them to enable all (or even a significant subset) of the possible conversations coders need to have with their teammates. And since these extensions are inherently non-standard, you have a portability headache. What happens when you upgrade your compiler, or when you're handcuffed to an old version by some frustrating platform dependency?

Besides, compiler extensions have very narrow, pre-defined applicability. You can decorate a structure with packing and alignment notations using a compiler extension, but can you decorate a conditional block with notations about which is the expected branch? Each new site for extension attachment requires additional compiler work.

<strong>Compiler Plugins</strong> are a variant on the extension idea. <a title="clang plugins" href="http://clang.llvm.org/docs/ClangPlugins.html" target="_blank">Clang</a> and <a title="gcc plugins" href="https://gcc.gnu.org/onlinedocs/gccint/Plugins.html" target="_blank">GCC</a> both support rich plugin models; the option to write your own frees you from many constraints that extensions impose. You see the entire abstract syntax tree (AST) at several different points in the compilation process, and you can modify it or validate it to your heart's content.

It seems to me that this mechanism is much closer to what we want, but it still has important problems. For one, the bar for writing such plugins is very high. You have a steep learning curve, and you may need to repeat it each time the compiler evolves. The ASTs that you examine are not the same from one compiler to another, because the language spec says nothing about what AST must be used to represent higher-level constructs--or about the interface that ASTs must provide.

Another problem with plugins is that you have to write them in the language your compiler was written in, not the language the compiler is processing. If you're a C/C++ coder, this may not sound like a big deal--but it may be tougher if you just want to live in python or ruby or C#.

Perhaps you're looking at my list of tools and wondering why I haven't mentioned<strong> enhanced runtimes and additional libraries</strong>. They might seem like an obvious answer. Java doesn't natively support Erlang-style actors, but if you use <a href="http://akka.io/" target="_blank">Akka</a>, you get a rich, full-featured implementation of them. If your language is even halfway worth its salt, can't you just extend its capabilities this way in unbounded fashion? Don't people do that every day, with great success?

It's important to understand that the semantic gap I'm complaining about is not particularly focused on what happens at runtime; nor is it a problem with what languages can make computers do. This is a gap in what languages can help <em>human beings</em> do. <em><a title="Why Mental Models Matter" href="../../../2012/11/05/why-mental-models-matter/">Human knowledge</a> and behaviors are <a title="Users Aren’t The Only People In Your Software" href="../../../2012/09/04/users-arent-the-only-people-in-your-software/">crucial outputs of dev teams</a>.</em> And cool add-on libraries, or even the most powerful runtimes in the world, do not change that dynamic all that much. Just because you start using Akka for distributed, coordinated behaviors in your code doesn't mean that your dev team gets better coordinated. You might still struggle to track requirements or get correct test coverage.

Another possibility is <strong>comments</strong>. This has been the <a title="When good comments mean bad language" href="../../../2013/08/22/when-good-comments-mean-bad-language/">answer of choice</a>, for years. You can say anything you want in comments. (Hmm. Notice the semantic power in that, and how it's tied to <em>human</em> language...) If a coder is never supposed to tweak strings in a .properties file, after the "UI Freeze" milestone, without consulting the localization team, you can spell that out in capital letters at the top of the file.

But comments are pretty darn weak. They may be inaccurate even when they're first written, and they tend to become more so over time, to the point where they actually <a title="// Comments on Comments" href="../../../2012/10/31/comments-on-comments/">create unnecessary confusion</a>. They are not mandatory (except by <a title="How to turn coding standards into epic fails — or not" href="../../../2012/09/27/coding-standards/" target="_blank">human fiat, which is usually ignored</a>), and everybody's judgment about where they're valuable seems to vary. Some coders are excellent comment-writers; others are lousy. Only coders are influenced by comments; testers and tech writers and product managers and others in the orbit of a dev team never see them. In fact, comments often become a <a title="When good comments mean bad language" href="../../../2013/08/22/when-good-comments-mean-bad-language/">crutch</a> to compensate for bad behaviors.

You might also be a fan of <strong>javadoc- or doxygen-style documentation</strong>. Or you may think that <strong>RDF and the semantic web</strong> are the ultimate answer for decorating a corpus with rich knowledge, using unbounded human language.

I claim that these approaches have most of the same advantages and disadvantages of commenting in general. They have their place. However, they are no panacea. You are expressing semantics in a parallel channel, and this often means you must pay the price for considerable time-wasting redundancy. Coders don't want to write docs, or they would have become tech writers. I have never seen these sources of information be popular with the teams that produce functionality, or the teams that consume them. They're simply too incomplete, too stale, and too reliant on unenforced and non-existent cooperation between humans that don't understand one another's jobs very well. Visual Studio and java IDEs have done a nice job of integrating them into the editing experience, but most other environments don't even use or validate the doc comments that you painstakingly create.

Of all the possibilities, the one I like the best is <strong>decorators</strong> (python's term), <strong>annotations</strong> (java), or <strong>attributes</strong> (.NET). If you look at my beefs with other techniques, you can see where these little guys show promise. You write them in the same language you're using. You can invent new ones any time you like, and the learning curve is low. The set of topics you can address with decorators is unbounded, and demands no reaction from the language or its compiler.

I predict that languages will make more use of decorators as they evolve, because of these virtues. Trace their growing importance in python, and you'll see what I mean.

However, decorators aren't perfect. For one thing, compilers are not on the hook, in any language I know, to react to the presence of decorators in any special way. There are a few hard-coded exceptions--<code>@Override</code> in java, <code>@staticmethod</code> and <code>@property</code> in python, for example. Pyunit makes great use of them with nose. But generally, you can't write a new decorator and change the behavior of the compiler at compile-time, the way you can with an extension. Decorators don't have access to the AST. You mainly access them at run-time, through reflection. They are nouns that you mainly attach to other nouns, and as the name implies, today they're mostly tinsel and brick-brack; they don't <em>mean</em> anything that has serious consequences.
<h3>A Better Way</h3>
The word count is getting away from me; I don't have time in this post to lay out my full solution. Shoot! Still, I think the tool inventory has been helpful, and some of what I will say in the next post will now make a lot more sense.

I <em>have</em> dropped a couple hints in this post about where I'm headed, though. Did you notice where I referred to nouns and verbs? Nouns are variables and objects and data types and decorators; verbs are functions and methods and (sometimes) keywords.

Have you ever wondered where the adjectives and adverbs are?

In my <a href="../../../2014/07/24/introducing-marks/">next post</a>, I'll describe my bridge more concretely. Even before I do, though, the discussion above should help you predict some of the shortcomings it must address. Do I have your creative juices flowing?

My solution is terse, natural, and easy to learn and use. It helps coders get more done by thinking naturally, instead of demanding an awkward new set of expensive habits. And it's eminently implement-able. However, it requires us to stop thinking of compilation as the process of translating syntax to machine code, and start thinking of it as the translation of all <em>intentions</em>--computational and human. I'm not sure any existing language is willing to buy into that assumption, which is why I'm still creating my own. Hopefully the language name I've chosen, <em>intent</em>, now resonates a bit...

<hr style="margin-top:4em;width:60%;" />
<p style="font-size:90%;margin-left:2em;"><a name="1"></a><sup>[1]</sup> Interestingly enough, this same over-emphasis on parseable structure has afflicted the discipline of linguistics for decades. Back in the 60s, at the same time that compilers were getting traction in computer science, linguists zeroed in on universal grammar and its cousins as a sort of "grand unified theory" of language. Our brains were wired for certain linguistic structures, they said--and each human language just activated or turned off certain nodes in the shared uber-inventory, the same way programming languages could vary as long as they were Turing-complete. Machine translation was just around the corner, as soon as we codified the overall conceptual ontology and invented a formal algebra to express transformations of structure. It was a nice theory, but (IMO) fatally flawed... by the same "lacuna humana" fallacy. Humans are agents, possessing free will and the capacity to create meaning in novel ways. We bend language to whatever uses suit us. Yes, there are deep harmonies in the structures that we select to express our ideas, across all known languages--but semantics is more than structure. If this sort of thing interests you, consider reading <em>Women, Fire, and Dangerous Things</em> (Lakoff), <em>The Possibility of Language</em> (Melby), or <em>LANGUAGE in Capital Letters</em> (Lytle).</p>

---

Mountains, Molehills, and Markedness | Codecraft (2014-07-28 08:44:39)

[…] are not as rich as they could be. I pointed out some symptoms of that deficit, and then made recommendations about bridging the gap. Finally I introduced “marks”–a feature of the intent programming language […]

---

Lacunas Everywhere | Codecraft (2015-06-15 10:15:17)

[…] lots of noise or bother. I’ll be explaining this feature, “marks,” in a series of follow-on posts. I hope you’ll subscribe or check back to see where I’m […]

---

A grumble about buckets | Codecraft (2015-04-08 13:39:55)

[…] thought to the buckets we offer–and let’s make sure we have a way of discovering and tracking whether our buckets are […]

---

In Which Warnings Evolve Wings | Codecraft (2014-08-06 08:46:12)

[…] know more about your intent. (Does this sound like the “lacuna humana” that I have been harping on […]

---

Introducing Marks | Codecraft (2014-07-24 08:49:24)

[…] my previous two posts (here and here), I described how and why programming languages can’t talk about many issues that affect […]