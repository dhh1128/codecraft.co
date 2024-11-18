---
title: Small Files Are Your Friends
date: 2013-03-21
slug: small-files-are-your-friends
redirect_from:
  - /2013/03/21/small-files-are-your-friends
---

Yesterday I was discussing refactoring priorities with a colleague who's a brilliant engineer, and I happened to mention my strong desire for smaller files in our codebase. I told him that I thought .h and .cpp (or .py or .java or .whatever) files with thousands of lines were a problem.

He asked me why.

He told me that he wasn't opposed to the idea, but he always felt like it was more of a stylistic choice than a true imperative for good code. And he was curious to see if I could convince him differently.

After I pondered his question for a while, I realized that some of my opinion really is traceable to prejudice. I usually use IDEs instead of vim/emacs, and I think that promotes <em>click-back-and-forth-and-hyperlink-in-many-little-files</em> instead of <em>open-a-big-file-and-scroll</em>. My compatriots that are more console-centric are just as smart and effective--maybe more. So I'll write that part off.

However, I also found some arguments for the small-file principle that feel more substantive. Small files are your friends.

<figure><img alt="" src="http://farm5.staticflickr.com/4002/5166773331_bb50dfa3b0.jpg" width="500" height="320" /><figcaption>More small friends. Photo credit: miguelandresen (Flickr)</figcaption></figure>

<strong>Named scopes and cognitive complexity</strong>

The case for small functions is more discussed than the case for small files, and it has been made by almost every luminary in computer science. My colleague immediately conceded it, and I won't repeat it here--but I will claim that many of the same arguments apply to files as well, because <em>files as well as functions are an important named scope in software development</em>. This in turn suggests some constraints on files with respect to cognitive complexity.

Studies of memory and human attention consistently demonstrate that <a title="short-term memory and cognitive complexity" href="http://www.simplypsychology.org/short-term-memory.html" target="_blank">we think best about small sets</a>. This fact is reflected by the amount of detail visible within any given named scope, both in programming and in other thought tasks. How many top-level menus in the average application? Colors in most cultures' divisions of the rainbow? Parameters in an easy-to-understand function? Sections in the average book store? Steps in easy-to-follow driving directions? (There's a whole field called cognitive ergonomics that explores why these questions always have similar answers.)

How many functions should we put in a reasonable file?

For me, 2 or 5 or 10 feels tractable. 50 feels excessive.

If a "good function" also respects the cognitive complexity constraints of the human brain--not being too big to read in a screen or two, for example--then you end up with a reasonable upper boundary on file sizes of, maybe, 500 or 1000 lines. (See Steve Yegge's insightful rant about <a title="code size (and complexity) make software development difficult" href="http://steve-yegge.blogspot.com/2007/12/codes-worst-enemy.html" target="_blank">code size being an engineer's worst enemy</a>. He focuses on codebase size, but much of what he says applies just as well at the next level down.)

I suppose that this argument is weakened by the features of some IDEs, which collapse tangential code blocks, display treeviews of functions, and support lots of hypertext-style igation. But not all programmers use the same IDEs, and not all interactions with code are IDE-driven; file size remains relevant. There's a reason why C# created <a class="zem_slink" title="Class (computer programming)" href="http://en.wikipedia.org/wiki/Class_%28computer_programming%29" target="_blank" rel="wikipedia">partial classes</a> to improve on java's lump-it-all-in-a-single-file constraint...

When humans try to remember more than their brains can fit, stuff falls out. Big files mean that coders have to <a title="Why Mental Models Matter" href="why-mental-models-matter.md" target="_blank">mentally model</a> relationships between stuff that's separated by way too much screen real estate. This is a recipe for bugs. It is also a serious impediment to learnability.

<strong>Loose coupling and encapsulation</strong>

Files are a natural unit of coupling. In most programming languages, you can declare a construct (a variable, an internal function, or class) within a file, and have that construct be invisible to the side world. This means there is a built-in temptation for functions and classes to bind more tightly when they're in the same file, because they have access to common but private knowledge. By breaking large files apart, you remove the temptation, break unnecessary dependencies, and promote looser coupling.

Another way to say this is that file boundaries are an encapsulation barrier. Use them to hide data. (See my recent post about <a title="encapsulate to simplify" href="6-strategies-to-simplify-software.md" target="_blank">encapsulation as a simplicity strategy</a>.)

<strong>Code reuse and testability</strong>

A consequence of files hiding data is that when you have a function that might be useful in a dozen different modules, but the function is buried in a large file with lots of dependencies extraneous to that function, reuse and testability are both frustrated. If the function is in a file of its own, it's more discoverable, and it's reusable and testable without extra baggage.

<strong>Link optimization</strong>

A C/C++ corollary to the file boundary issue has to do with linkers and binary sizes. In many cases, linkers remove unused functions at <em><a class="zem_slink" title="Translation unit (programming)" href="http://en.wikipedia.org/wiki/Translation_unit_%28programming%29" target="_blank" rel="wikipedia">compilation unit</a></em> level, rather than at the individual function level. A .c or .cpp file is either in or out, as a unit. This means that if you have a .cpp file with 50 functions in it, and you call only 1 of them, all 50 get linked into the final binary. The result is bloated binaries. So: smaller .cpp files ==> smaller binaries. (Before you flame me about linker optimizations, I will admit that some linkers get more granular, depending on which switches you use. But it's surprising how hard it is to do better than what I've described. Experiment and comment with your results.)

<strong>Counter Argument</strong>

I suppose you could argue that by making lots of small files, you're <em>creating</em> more complexity in directories, in makefiles or projects, and so forth. Is 250 files in a folder worse than 15? Doesn't that violate the "cognitive complexity" guideline above?

My comeback is: use packages or subdirectories or libraries (another level of management). You can't subdivide forever, but you don't need to.

The bottom line for me is experiential, not theoretical. I nearly always have cruddy experiences in code bases where large files are common. Small files don't guarantee pleasant and productive work, but big ones seem to go hand-in-hand with other problems. I find it telling that codebases with big files are also codebases where people lament the <a title="// Comments on Comments" href="comments-on-comments.md" target="_blank">lack of comments</a> the most, for example. Over the years, I've become convinced that a simple rule of thumb about keeping files small will pay off more handsomely than almost any other coding best practice.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Leave a comment to tell me what you think. Am I making a mountain out of a molehill? Or do you feel strongly about small file sizes as well? Have I omitted any important pros and cons from the discussion?</span></em></p>





---

Andy Lawrence (2013-03-21 10:43:52)

Good article. I think you made some great points.

I think your strongest argument for small files is the loose coupling and encapsulation one. It can impose an artificial constraint that forces the programmer to think more about those issues. It is kind of like if your company has a coding standard that says "no function can be longer than x number of lines". This can force the programmer to think more about modular programming and break that mammoth function into several smaller ones which can enhance readability and code re-use.

Having every class definition and method in its own separate file can be great if your IDE makes it very easy to navigate and manage all related files as a group, but it can become a file management nightmare if using traditional editors and file folders. The benefit of having everything in a single file is that if you copy just one file, you get all your code. If every function is in a separate file, you run the risk of forgetting to copy one of them or having one of them in a folder that isn't backed up.

We have probably all had bad experiences with files and/or functions that were too big or too small. Finding the right balance is what keeps programming as much of an art as it is a science.

---

dougbert (2013-03-21 10:44:44)

Exactly my points as well, but again well presented by you.
My mind cache is 7-8 items, ANYWAY to factor things to have a 'collective' of that size is wonderful for my sanity. If more are added, then a refactor is needed to reduce the size by some sort of organization.

If some files is SO big, I ask: WHY?  Usually it is some huge monster OBJECT that has so many attributes, that action functions just plain explode.

Object relationship then need some refactoring.  Huge files are like huge objects, a mass of confusion and disorder

---

Daniel Hardman (2013-03-21 12:05:44)

Doug: I'm so grateful that you pushed on this issue in Moab. Although we're not very close to the ideal yet, we're much better off because of your efforts.

---

Daniel Hardman (2013-03-21 12:35:44)

Your observation about balance really resonates with me. That's one of my pet themes (see http://codecraft.co/2012/08/27/good-code-is-balanced/). 

One thing that I find interesting is the different nature of the consequences at the two ends of the spectrum. At the <em>files-are-too-big</em> end, the consequences seem a bit scary. They make problems less understandable; they steal velocity, accuracy, and quality of design from developers. At the <em>files-are-too-small</em> end, you start paying a "silliness tax" where you have to recurse down too many levels while coding and debugging. This can also make it hard to see the bigger picture (so in that respect the two ends of the continuum are similar) -- but I don't think it impedes loose coupling and code reuse. It's also easier to undo/change, I think.

---

Jason Law (2013-03-21 15:24:38)

Great points, Daniel. Early in my career, I found that small classes and small methods let me model more complex problems. Encapsulation is key, and it's how I think our brains work. Reminds me of some of the points made in Robert C. Martin's Clean Code. Nice article.

---

Daniel Hardman (2013-03-21 21:44:49)

Jason! Great to hear from you. Long time no see. Thanks for all the Oracle goodness you taught me.

Robert Martin is one of my heros, but I haven't read Clean Code. So now I've got something new for my reading list. Thanks!

---

Wally (2013-03-22 15:36:31)

I'm going to have to disagree that small files should be a "goal".  I think that the goal is to have good data encapsulation and boundaries.  Files are one way of accomplishing this via scoping, but they don't ensure that a project breaks itself up into manageable pieces.  Splitting a monstrous files into multiple small files that still utilize externs and global includes to share all the same data they had in the first place ends up being a zero-sum change.

The important goal should be to separate and isolate the various project components into logical divisions.  If they don't have logical cleavage planes, then refactor them until they do. The location of the pieces in specific files is really an afterthought that follows naturally.  Just splitting things into smaller files to achieve a certain line/function quota seems useless to me.  

I like to think of this from an organic perspective.  Many garden plants grow larger and larger until they start to choke themselves out.  They can be divided and replanted and you can get multiples from one original.  However, you don't just take a shovel and slice the thing apart indiscriminately.   You also don't want to leave roots and connections back to the parent plant.  Instead, you carefully disentangle roots and tubers and find places where things look like they belong together and then you make judicious cuts and sacrifices and end up with smaller plants that can survive on their own.  Cutting up a plant just to fit it in a smaller pot is never a good idea.   http://gardening.about.com/od/perennials/ss/DividingSBS.htm

---

Daniel Hardman (2013-03-22 15:51:25)

I think that's a very true and insightful analogy, Wally. Thanks so much for adding to the conversation!

I guess implicit in my thinking was the idea that if you have big files, and you split them, that the activity becomes an enabler for many of the forms of true goodness that you're highlighting.

I do think that it's harder to accomplish the encapsulation and logical division if you leave things in a single file -- mainly because the ugliness of globals and other forms of coupling aren't as obvious.





---

Doug (2019-07-08 12:28:49)

I came to software through a background in hardware at Bell Labs in the mid 1980s.

I learned embedded C development from a couple of DMTS level engineers and I still cherish how they bootstrapped my transition into software.

They had a few hard rules that required enormous justification to override.

Only one external function per file. You could have static helpers, but only one globally accessible function.

No function was more than 100 lines.

Those two were the biggies. There were other coding style rules, but the two above you would violate at your peril. Much for the reasons you list above, but one you did not. In most organizations of any size, your code is going to end up in a repository of some form, and over time, parts of it are going to be edited to either extend features, or to fix a defect, and likely be someone other than you.
If there are numerous functions in a single file, it increases the chance that a single file will be out being modified by more than one person, and then having to be merged. Small, single function files are less likely to face merge conflicts.

One other note that goes along with some of your other posts. When you write code, it is easy to fall into the trap of thinking you are writing for the machine, but you are really writing for other humans that will come after you. If you always design and code as if you are writing for people, you will be doing your future self a huge favor.

