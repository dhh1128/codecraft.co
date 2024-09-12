---
title: Variadic macros tricks
date: 2014/11/25
slug: variadic-macros-tricks
---

Have you ever wanted to write a "for each" loop over all the args of a variadic macro? Or have you ever wanted to overload a macro on the number of arguments? (If you're saying to yourself, "good grief, why?" -- I'll describe a use case at the bottom of this post.)

I learned how to do this today, and I wanted to blog about it to cement the technique in my own mind. (And I hereby put all the code I show here into the public domain.)

[caption id="" align="aligncenter" width="404"]<a href="http://xkcd.com/1319/"><img class="" src="http://imgs.xkcd.com/comics/automation.png" width="404" height="408"></a> What happened when I decided to learn this technique. I'm trying to spare you... :-) Image credit: xkcd.com[/caption]
<h3>Simple variadic macros</h3>
The first piece of magic you need to do something like this is <code>__VA_ARGS__</code>. This allows you to write macros that take an arbitrary number of arguments, using <code>...</code> to represent the macro's parameters:

https://gist.github.com/dhh1128/4f2e50c5aa23589ad4ad

Nice. <code>__VA_ARGS__</code> is a standard feature of C99, and I've known about it for a long time. I've also known about GCC (and Clang's) extension, which attaches special meaning to <code>##__VA_ARGS__</code> if it's preceded by a comma--it removes the comma if <code>##__VA_ARGS__</code> expands to nothing. If I change my macro definition to:

https://gist.github.com/dhh1128/a0972d8750c3d57f4c0a004dd04a5416

...I can now call <code>eprintf("hello, world");</code> without a complaint from the compiler.
<h3>But it's not enough</h3>
That doesn't let me do a "for each" loop, though. All the args that I pass are expanded, but I can't do anything with them, individually. I have no names for my macro's parameters--just the anonymous <em>...</em>.

I went poking around, not expecting to find a solution, but I was pleasantly surprised.

<!--more-->
<h3>The "paired, sliding arg list" trick</h3>
The next building block we need is a technique that uses two complementary macros plus <code>__VA_ARGS__</code> to select something specific out of a macro arg list of unknown size. I found it in an <a href="http://stackoverflow.com/a/11763277" target="_blank" rel="noopener">answer on stackoverflow.com</a>, and you can parse it all out directly from there, but the magic's a little opaque. Here's an explanation that takes it one step at a time:

https://gist.github.com/dhh1128/62770dd17c6632cf0abe

See how it works? The first macro, <code>_GET_NTH_ARG()</code>, takes any number of args >= <em>N</em>, but always returns item <em>N</em> (in this case, <em>N</em>=5). The second macro, <code>COUNT_VARARGS(...)</code>, takes an arbitrary number of args < <em>N</em>, pads with candidate values it wants to extract, and uses its args to call <code>_GET_NTH_ARG()</code> in a way that puts the right candidate value in the known <em>N</em> position. In this case, the meaningful piece of info that we want in position <em>N</em> is an arg count; we've provided the values <code>4, 3, 2, 1</code> as candidate values, and one of those values will be in position <em>N</em> on expansion.

Tweaking this macro pair to handle a different <em>N</em> is a matter of adjusting what comes before <em>N</em> in the first macro, and what comes after <code>__VA_ARGS__</code> in the second macro. I'll leave that as an exercise for the reader. :-)

We don't have to select a numeric count with this technique; we could use it to select arg names with the <code>#</code> operator, or even other macros. This will come in handy in a moment. But first, let's address one shortcoming: <code>COUNT_VARARGS(...)</code> doesn't handle the case of zero args. Here's the fix:

https://gist.github.com/dhh1128/0cf088f4f681f619b051
<h3>Macro overrides</h3>
Now, we can build on this to define a variadic macro that has an expansion overridden by how many args it receives. This is what the original stackoverflow answer did. Something like this:

https://gist.github.com/dhh1128/36bc220b10f6dafefa33

Now we're getting close to being able to code a "for each" loop over all the args to a variadic macro. If the macro that gets overridden has a "for each" flavor, it all comes together:

https://gist.github.com/dhh1128/d1dd24b492819c65f1e1
<h3>Okay, but why?</h3>
I said I'd provide some explanation of why this technique could be useful. In general, I am not a fan of macros rewriting the syntax of a programming language; that can obscure what's really happening, and make for a steeper learning curve.

On the other hand, sometimes they are really helpful. They can make code much less verbose/repetitive by eliminating noise and boilerplate. Occasionally, I run into cases where that tradeoff seems worth it to me.

More importantly, macros have a property that you can't get any other way--the same fragment of code can have multiple meanings, and can maintain this semantic parallelism without being susceptible to human memory errors, laziness, or misunderstanding. I have previously blogged about how valuable this can be in <a title="How Enums Spread Disease — And How To Cure It" href="http://codecraft.co/2012/10/29/how-enums-spread-disease-and-how-to-cure-it/">eliminating encapuslation problems with enums</a>, but I recently found another need for it. In <a title="On bread recipes, maps, and intentions" href="http://codecraft.co/2013/10/24/on-bread-recipes-maps-and-intentions/">my project to create a new programming language</a>, I have to create some foundation packages and classes -- the analog to <code>java.lang</code> in java, or <code>System</code> and <code>My</code> in .NET. This foundation needs to written in C/C++ to avoid a chicken-and-egg problem. That means I need some way to use namespaces, classes, and other C++ constructs in the source code, but also generate package and class constructs visible to my <code>intent</code> compiler. Macros were an obvious answer.

The only problem was that some of my macros needed to be variadic--and I needed for-each-style semantics. Hence my research. :-)

How about you? Have you ever had a need for something like this?

---

cormacc (2018-03-26 05:40:19)

Hi Daniel,
I found this recursive implementation useful in some mocking/unit testing work -- thanks! Wrapped it and some extensions in a ruby generator script for an arbitrary number of arguments here  if it's of any use to anyone else:
https://github.com/cormacc/va_args_iterators

---

Daniel Hardman (2015-01-05 18:57:03)

Jason: I've run into boost.preprocessor a few times, but I haven't used it much. Shame on me! Thanks for reminding me to learn about it.

When I run into a programming problem that I don't know how to solve, I often like to write my own solution--not so much because I want to *use* my own solution, as because I want to learn what it takes to solve the problem. Once I've solved it to my own satisfaction (and, sometimes, written about it so I understand how it works well), then I can appreciate a more elegant or general solution, and chuck my own. I'll have to look into boost.preprocessor to see if it solves the problem I was seeing in the intent codebase; if so, I'll gladly switch over, since I'm already using boost a fair amount.

---

Jason Ivey (2015-01-05 18:23:11)

I love the preprocessor for exactly this kind of work.  Although macros get a bad name these days, the preprocessor itself is still a powerful and wonderful tool when used for the problems you described.  

What I've discovered recently as I have been writing custom macros is that many, if not all, of the underlying code I invent is already written in the boost.preprocessor library.  I'm not sure if it has an identical solution to what you have created above but I know it has a macro to convert the var_args to a count and list. (BOOST_PP_VARIADIC_TO_LIST)

I was also pleased to discover that they have the mechanics to quickly implement my favorite preprocessor pattern you taught me years ago, the enum-declaration-via-include-file.  (BOOST_PP_ITERATION)

In my opinion, the boost.preprocessor library documentation leaves a little to be desired in terms of examples and descriptions.  But there is a lot there to work with.

---

Mattias (2017-12-14 05:44:02)

Hi. I try the example "macros_overridden_by_arg_count" but I get the warning "not enoug parameter for macro '_GET_OVERRIDE'

---

metablaster (2019-10-04 13:53:31)

Hi Daniel, thank you a lot for these macro hacks which are awesome, I knew all of them except the "for each" macro, it doesn't work in MSVC out of the box, here is a trick for those who want to make it work!

#define EXPAND(x) x

#define _GET_NTH_ARG(_1, _2, _3, _4, N, ...) N

#define _fe_0(_call, ...)
#define _fe_1(_call, x) _call(x)
#define _fe_2(_call, x, ...) _call(x) _fe_1(_call, __VA_ARGS__)
#define _fe_3(_call, x, ...) _call(x) EXPAND(_fe_2(_call, __VA_ARGS__))
#define _fe_4(_call, x, ...) _call(x) EXPAND(_fe_3(_call, __VA_ARGS__))

#define CALL_MACRO_X_FOR_EACH(x, ...) \
	EXPAND(_GET_NTH_ARG(__VA_ARGS__, _fe_4, _fe_3, _fe_2, _fe_1, _fe_0)(x, __VA_ARGS__))

#define FWD_DECLARE_CLASS(cls) class cls;

void test()
{
	CALL_MACRO_X_FOR_EACH(FWD_DECLARE_CLASS, Foo, Bar, Baz, Fubar);
}

---

Daniel Hardman (2019-10-04 15:31:27)

Thanks for improving this content! I really appreciate the note about MSVC.

---

Dave MacLachlan (2020-07-29 09:41:39)

Thanks so much for the article. Just an FYI that you have a typo in your second `eprintf` block. I think you want `#__VA_ARGS__` as opposed to `#__VA_ARGS`

---

Daniel Hardman (2019-10-02 07:03:03)

Thank you! I think I ran my code through a version of MSVC at one point, but I've long since let any insight about it grow stale, so this is a great help. I appreciate the improvement.

---

Franz G (2017-10-25 10:01:29)

"Use Boost" doesn't make for compelling blog posts ;)

---

Rune Paamand (2019-10-01 01:35:40)

Mind that your examples will not work on MSVC where the variadic macro does not expand. You need an expansion step to achieve the `COUNT_VARARGS`:

// Count how many args are in a variadic macro. Only works for up to N-1 args.
#define RETURN_ARG_COUNT(_1, _2, _3, _4, N, ...) N
#define EXPAND_ARGS(args) args
// Notice double parenthesis for expansion single to var arguments
#define COUNT_VARARGS(...) RETURN_ARG_COUNT EXPAND_ARGS((__VA_ARGS__, 4, 3, 2, 1, 0))

---

为什么我的可变参数宏不能正确接受参数？ &#8211; FIXBBS (2020-09-09 08:10:27)

[…] https://codecraft.co/2014/11/25/variadic-macros-tricks/ […]

---

Daniel Hardman (2020-08-04 08:43:14)

Thanks, Dave, for the comment and for the catch on the typo. I've updated the gist.