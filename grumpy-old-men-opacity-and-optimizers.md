---
title: Grumpy Old Men, Opacity, and Optimizers
date: 2014-09-09
slug: grumpy-old-men-opacity-and-optimizers
redirect_from:
  - /2014/09/09/grumpy-old-men-opacity-and-optimizers
---

Today I'm channeling my inner grumpy old man. And these guys are helping. (I am not old enough to pull off such a face by myself, although life is rapidly helping me get there. ;-)

<figure>
<img src="assets/grumpy.jpg"/>
<figcaption>Image credit: Midjourney</figcaption>
</figure>

The reason I'm feeling grumpy is that I've had another in a long, long line of conversations about how to write faster code.\nIt's not that optimization experts are dumb. Far from it. They are invariably smart, and in general, they are better informed than I am about how pipeline burst cache and GPUs and RAM prefetch algorithms work. I generally learn a lot when I talk to guys like this.\nI applaud their passion, even if I think <a title="3 Commandments of Performance Optimization" href="steve-tolman-it-depends.md">it depends</a>. :-)

My point today is not about inlines, though. It's not even about performance dogma. Rather, it's about opacity.

The optimization choices that a compiler makes about inlining and sundry other issues are <em>opaque</em> to most coders. And I claim that it is this fact &mdash; not irrational zealots &mdash; at the heart of a lot of holy wars, debates, and FUD about optimization. The classic paper by <a href="http://www.drdobbs.com/cpp/c-and-the-perils-of-double-checked-locki/184405726" target="_blank">Meyers and Alexandrescu about how compiler optimization defeats the intent of the double-checked locking pattern</a> provides eloquent examples of this opacity. If you haven't read it, I encourage you to do so.

We should fix this.

Compiler makers, I hereby request a feature. Please add the ability to generate an "optimization plan" for a function, analogous to the "explain query plan" feature that DB admins have used to tune their work for decades.\nI can imagine this working as a compiler switch, similar to <code>-E</code> which dumps preprocessor output to stdout. If I add <code> &mdash; explain-optimizations</code> to the cmdline, I would like a report that tells me:

* What sorts of loop unwinding, reordering, and other shortcuts will be used. Please tie them back to the specific switches that are active.
* How optimizations were constrained by block, function, and translation unit scope &mdash; and how optimizations might change naive assumptions about scope that a programmer would form by looking at the high-level representation of the code.
* What additional optimizations might be possible if additional switches were added or removed.
* What guesses were made about likely versus unlikely branches in conditionals.
* What additional optimizations might be possible if not for a certain characteristic of the code. Please be specific: "I could not optimize out the extra assignment to foo, because codepath X requires it."
* How micro optimization decisions conflict with macro ones, and what assumptions and priorities were used to resolve these conflicts.

I realize I am not asking for something easy. But I believe explaining optimization choices cannot be harder than making those choices in the first place &mdash; and the problem must be somewhat tractable, since the SQL crowd has an analogous tool.

Let's shine some light on this black magic, and turn performance tradeoffs into a science based on common, abundant knowledge. I think it could improve the whole industry.