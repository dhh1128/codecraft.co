---
title: Variadic macros tricks
date: 2014-11-25
slug: variadic-macros-tricks
redirect_from:
  - /2014/11/25/variadic-macros-tricks
comments:
  - author: Jason Ivey
    date: 2015-01-05 18:23:11
    comment: |
      I love the preprocessor for exactly this kind of work.  Although macros get a bad name these days, the preprocessor itself is still a powerful and wonderful tool when used for the problems you described.  
      
      What I've discovered recently as I have been writing custom macros is that many, if not all, of the underlying code I invent is already written in the boost.preprocessor library.  I'm not sure if it has an identical solution to what you have created above but I know it has a macro to convert the var_args to a count and list. (BOOST_PP_VARIADIC_TO_LIST)
      
      I was also pleased to discover that they have the mechanics to quickly implement my favorite preprocessor pattern you taught me years ago, the enum-declaration-via-include-file.  (BOOST_PP_ITERATION)
      
      In my opinion, the boost.preprocessor library documentation leaves a little to be desired in terms of examples and descriptions.  But there is a lot there to work with.
  - author: Daniel Hardman
    date: 2015-01-05 18:57:03
    comment: |
      Jason: I've run into boost.preprocessor a few times, but I haven't used it much. Shame on me! Thanks for reminding me to learn about it.
      
      When I run into a programming problem that I don't know how to solve, I often like to write my own solution &mdash; not so much because I want to *use* my own solution, as because I want to learn what it takes to solve the problem. Once I've solved it to my own satisfaction (and, sometimes, written about it so I understand how it works well), then I can appreciate a more elegant or general solution, and chuck my own. I'll have to look into boost.preprocessor to see if it solves the problem I was seeing in the intent codebase; if so, I'll gladly switch over, since I'm already using boost a fair amount.
  - author: Franz G
    date: 2017-10-25 10:01:29
    comment: |
      "Use Boost" doesn't make for compelling blog posts ;)
  - author: Mattias
    date: 2017-12-14 05:44:02
    comment: |
      Hi. I try the example "macros_overridden_by_arg_count" but I get the warning "not enoug parameter for macro '_GET_OVERRIDE'
  - author: cormacc
    date: 2018-03-26 05:40:19
    comment: |
      Hi Daniel,
      I found this recursive implementation useful in some mocking/unit testing work &mdash; thanks! Wrapped it and some extensions in a ruby generator script for an arbitrary number of arguments here  if it's of any use to anyone else:
      <a href="https://github.com/cormacc/va_args_iterators">https://github.com/cormacc/va_args_iterators</a>
  - author: Rune Paamand
    date: 2019-10-01 01:35:40
    comment: |
      Mind that your examples will not work on MSVC where the variadic macro does not expand. You need an expansion step to achieve the `COUNT_VARARGS`:
      
      <pre>
      // Count how many args are in a variadic macro. Only works for up to N-1 args.
      #define RETURN_ARG_COUNT(_1, _2, _3, _4, N, ...) N
      #define EXPAND_ARGS(args) args
      // Notice double parenthesis for expansion single to var arguments
      #define COUNT_VARARGS(...) RETURN_ARG_COUNT EXPAND_ARGS((__VA_ARGS__, 4, 3, 2, 1, 0))
      <pre>
  - author: Daniel Hardman
    date: 2019-10-02 07:03:03
    comment: |
      Thank you! I think I ran my code through a version of MSVC at one point, but I've long since let any insight about it grow stale, so this is a great help. I appreciate the improvement.
  - author: metablaster
    date: 2019-10-04 13:53:31
    comment: |
      Hi Daniel, thank you a lot for these macro hacks which are awesome, I knew all of them except the "for each" macro, it doesn't work in MSVC out of the box, here is a trick for those who want to make it work!
      
      <pre>
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
      </pre>
  - author: Daniel Hardman
    date: 2019-10-04 15:31:27
    comment: |
      Thanks for improving this content! I really appreciate the note about MSVC.
  - author: Dave MacLachlan
    date: 2020-07-29 09:41:39
    comment: |
      Thanks so much for the article. Just an FYI that you have a typo in your second <code>eprintf</code> block. I think you want <code>#__VA_ARGS__</code> as opposed to </code>#__VA_ARGS</code>
  - author: Daniel Hardman
    date: 2020-08-04 08:43:14
    comment: |
      Thanks, Dave, for the comment and for the catch on the typo. I've updated the gist.
  - author: 为什么我的可变参数宏不能正确接受参数？ &#8211; FIXBBS
    date: 2020-09-09 08:10:27
    comment: |
      […] https://codecraft.co/2014/11/25/variadic-macros-tricks/ […]
---
Have you ever wanted to write a "for each" loop over all the args of a variadic macro? Or have you ever wanted to overload a macro on the number of arguments? (If you're saying to yourself, "good grief, why?" &mdash; I'll describe a use case at the bottom of this post.)

I learned how to do this today, and I wanted to blog about it to cement the technique in my own mind. (And I hereby put all the code I show here into the public domain.)

<figure>
<img class="" src="http://imgs.xkcd.com/comics/automation.png" width="404" height="408">
<figcaption>What happened when I decided to learn this technique. I'm trying to spare you... :-) Image credit: xkcd.com</figcaption>
</figure>

### Simple variadic macros

The first piece of magic you need to do something like this is <code>__VA_ARGS__</code>. This allows you to write macros that take an arbitrary number of arguments, using <code>...</code> to represent the macro's parameters:

```cpp
#define eprintf(fmt, ...) \
    fprintf(stderr, fmt, __VA_ARGS__)
```

Nice. <code>__VA_ARGS__</code> is a standard feature of C99, and I've known about it for a long time. I've also known about GCC (and Clang's) extension, which attaches special meaning to <code>##__VA_ARGS__</code> if it's preceded by a comma &mdash; it removes the comma if <code>##__VA_ARGS__</code> expands to nothing. If I change my macro definition to:

```cpp
#define eprintf(fmt, ...) \
    fprintf(stderr, fmt, ##__VA_ARGS__)
```

...I can now call <code>eprintf("hello, world");</code> without a complaint from the compiler.

### But it's not enough

That doesn't let me do a "for each" loop, though. All the args that I pass are expanded, but I can't do anything with them, individually. I have no names for my macro's parameters &mdash; just the anonymous <code>...</code>

I went poking around, not expecting to find a solution, but I was pleasantly surprised.

### The "paired, sliding arg list" trick

The next building block we need is a technique that uses two complementary macros plus <code>__VA_ARGS__</code> to select something specific out of a macro arg list of unknown size. I found it in an <a href="http://stackoverflow.com/a/11763277" target="_blank" rel="noopener">answer on stackoverflow.com</a>, and you can parse it all out directly from there, but the magic's a little opaque. Here's an explanation that takes it one step at a time:

```cpp
// Accept any number of args >= N, but expand to just the Nth one. In this case,
// we have settled on 5 as N. We could pick a different number by adjusting
// the count of throwaway args before N. Note that this macro is preceded by
// an underscore--it's an implementation detail, not something we expect people
// to call directly.
#define _GET_NTH_ARG(_1, _2, _3, _4, N, ...) N

// Count how many args are in a variadic macro. Only works for up to N-1 args.
#define COUNT_VARARGS(...) _GET_NTH_ARG(__VA_ARGS__, 4, 3, 2, 1)

int main() {
    printf("one arg: %d\n", COUNT_VARARGS(1));
    printf("three args: %d\n", COUNT_VARARGS(1, 2, 3));
}
 
// ------ output --------
one arg: 1
three args: 3
```

See how it works? The first macro, <code>_GET_NTH_ARG()</code>, takes any number of args >= <em>N</em>, but always returns item <em>N</em> (in this case, <em>N</em>=5). The second macro, <code>COUNT_VARARGS(...)</code>, takes an arbitrary number of args < <em>N</em>, pads with candidate values it wants to extract, and uses its args to call <code>_GET_NTH_ARG()</code> in a way that puts the right candidate value in the known <em>N</em> position. In this case, the meaningful piece of info that we want in position <em>N</em> is an arg count; we've provided the values <code>4, 3, 2, 1</code> as candidate values, and one of those values will be in position <em>N</em> on expansion.

Tweaking this macro pair to handle a different <em>N</em> is a matter of adjusting what comes before <em>N</em> in the first macro, and what comes after <code>__VA_ARGS__</code> in the second macro. I'll leave that as an exercise for the reader. :-)

We don't have to select a numeric count with this technique; we could use it to select arg names with the <code>#</code> operator, or even other macros. This will come in handy in a moment. But first, let's address one shortcoming: <code>COUNT_VARARGS(...)</code> doesn't handle the case of zero args. Here's the fix:

```cpp
// Accept any number of args >= N, but expand to just the Nth one. The macro
// that calls us still only supports 4 args, but the set of values we might
// need to return is 1 larger, so we increase N to 6.
#define _GET_NTH_ARG(_1, _2, _3, _4, _5, N, ...) N
 
// Count how many args are in a variadic macro. We now use GCC/Clang's extension to
// handle the case where ... expands to nothing. We must add a placeholder arg before
// ##__VA_ARGS__ (its value is totally irrelevant, but it's necessary to preserve
// the shifting offset we want). In addition, we must add 0 as a valid value to be in
// the N position.
#define COUNT_VARARGS(...) _GET_NTH_ARG("ignored", ##__VA_ARGS__, 4, 3, 2, 1, 0)

int main() {
    printf("zero args: %d\n", COUNT_VARARGS());
    printf("three args: %d\n", COUNT_VARARGS(1, 2, 3));
}

// ------ output --------
zero args: 0
three args: 3
```

### Macro overrides
Now, we can build on this to define a variadic macro that has an expansion overridden by how many args it receives. This is what the original stackoverflow answer did. Something like this:

```cpp
// Define two overrides that can be used by the expansion of 
// our main macro.
#define _MY_CONCAT3(a, b, c) a b c
#define _MY_CONCAT2(a, b) a b

// Define a macro that uses the "paired, sliding arg list"
// technique to select the appropriate override. You should
// recognize this as similar to the GET_NTH_ARG() macro in
// previous examples.
#define _GET_OVERRIDE(_1, _2, _3, NAME, ...) NAME

// Define a macro that concats either 3 or 2 strings together.
#define MY_CONCAT(...) _GET_OVERRIDE(__VA_ARGS__, \
    _MY_CONCAT3, _MY_CONCAT2)(__VA_ARGS__)

int main() {
    printf("3 args: %s\n", MY_CONCAT("a", "b", "c"));
    printf("2 args: %s", MY_CONCAT("a", "b"));
}
 
// ------ output --------
3 args: abc
2 args: ab
```

Now we're getting close to being able to code a "for each" loop over all the args to a variadic macro. If the macro that gets overridden has a "for each" flavor, it all comes together:

```cpp
// Accept any number of args >= N, but expand to just the Nth one.
// Here, N == 6.
#define _GET_NTH_ARG(_1, _2, _3, _4, _5, N, ...) N

// Define some macros to help us create overrides based on the
// arity of a for-each-style macro.
#define _fe_0(_call, ...)
#define _fe_1(_call, x) _call(x)
#define _fe_2(_call, x, ...) _call(x) _fe_1(_call, __VA_ARGS__)
#define _fe_3(_call, x, ...) _call(x) _fe_2(_call, __VA_ARGS__)
#define _fe_4(_call, x, ...) _call(x) _fe_3(_call, __VA_ARGS__)

/**
 * Provide a for-each construct for variadic macros. Supports up
 * to 4 args.
 *
 * Example usage1:
 *     #define FWD_DECLARE_CLASS(cls) class cls;
 *     CALL_MACRO_X_FOR_EACH(FWD_DECLARE_CLASS, Foo, Bar)
 *
 * Example usage 2:
 *     #define START_NS(ns) namespace ns {
 *     #define END_NS(ns) }
 *     #define MY_NAMESPACES System, Net, Http
 *     CALL_MACRO_X_FOR_EACH(START_NS, MY_NAMESPACES)
 *     typedef foo int;
 *     CALL_MACRO_X_FOR_EACH(END_NS, MY_NAMESPACES)
 */
#define CALL_MACRO_X_FOR_EACH(x, ...) \
    _GET_NTH_ARG("ignored", ##__VA_ARGS__, \
    _fe_4, _fe_3, _fe_2, _fe_1, _fe_0)(x, ##__VA_ARGS__)
```

### Okay, but why?
I said I'd provide some explanation of why this technique could be useful. In general, I am not a fan of macros rewriting the syntax of a programming language; that can obscure what's really happening, and make for a steeper learning curve.

On the other hand, sometimes they are really helpful. They can make code much less verbose/repetitive by eliminating noise and boilerplate. Occasionally, I run into cases where that tradeoff seems worth it to me.

More importantly, macros have a property that you can't get any other way &mdash; the same fragment of code can have multiple meanings, and can maintain this semantic parallelism without being susceptible to human memory errors, laziness, or misunderstanding. I have previously blogged about how valuable this can be in <a title="How Enums Spread Disease — And How To Cure It" href="on-bread-recipes-maps-and-intentions.md">my project to create a new programming language</a>, I have to create some foundation packages and classes &mdash; the analog to <code>java.lang</code> in java, or <code>System</code> and <code>My</code> in .NET. This foundation needs to written in C/C++ to avoid a chicken-and-egg problem. That means I need some way to use namespaces, classes, and other C++ constructs in the source code, but also generate package and class constructs visible to my <code>intent</code> compiler. Macros were an obvious answer.

The only problem was that some of my macros needed to be variadic &mdash; and I needed for-each-style semantics. Hence my research. :-)

How about you? Have you ever had a need for something like this?
