---
title: How to point in code
date: 2014-09-25
slug: how-to-point-in-code
redirect_from:
  - /2014/09/25/how-to-point-in-code
comments:
  - author: trevharmon
    date: 2014-09-29 22:51:25
    comment: |
      I have a question and then a comment.
      
      Question: I find what essentially amounts to inline comments described in #2 as an interesting idea. I am curious, though. Is Intent going to require those inline "comments" in order for it to compile? If not, that seems to allow programmers to just skip them, leaving us with code that's essentially the same as what we have today in terms of conveying additional meaning.
      
      Comment: Going back to one of my favorite languages, Perl (I know I'm an oddity), I find this idea of anchors to be interesting. Perl has a concept of Labels, which effectively behave very similar to HTML anchors. They can be applied to not only arbitrary code blocks (used for GOTO calls--yeah, if you really want to do that), but also for fine-grain nested loop control. Essentially, they allow the programmer to put down "anchors" at specific parts of the code, independent of line numbers, and then use them to control execution flow. Granted, this isn't exactly what you are getting at here in the article, but I've found it very useful (if used correctly) to make the code more readable. I believe this adds additional credence to what you are trying to accomplish overall.
      
      If you are interested, a discussion on Perl Labels can be found here: http://www.perlmonks.org/?node_id=616302
  - author: Daniel Hardman
    date: 2014-09-30 07:24:52
    comment: |
      Trev: thanks for the thoughtful comment.
      
      Perl labels are interesting. I had run across them once before, and the use case that I saw for them was the same one described in the post you linked--transferring control with precision in nested loops. I have never seen an answer to that problem that's as elegant as the one Perl offers. The alternatives in other languages--pure gotos, or nested loop state variables with conditionals--are uglier and far less clear.
      
      Are there other scenarios where you like to use them?
      
      Maybe they need to go into intent...
      
      Regarding your question: my current plan is to make the inline comments optional. As you point out, this means people are free to omit them, making code no more expressive than it is today. However, I can't see a good justification for requiring them, for three reasons: 1) if code has good variable names, and a parenthesized expression is simple, the comment would often be redundant; 2) I have no algorithmic way to evaluate the appropriateness of the comment, so requiring something might just cause people to grumble and put in placeholder text; 3) although I want every place it code to be name-able, I don't want to require names everywhere. Some blocks may not be name-worthy.
  - author: In Link 3&#8217;s Example &#8211; Foame
    date: 2024-08-29 15:30:55
    comment: |
      […] is just a tenet, and nothing can change checking the domains manually. Make sure that to solely construct hyperlinks that can contribute positively to your total online presence. Still acquired almost 9,000. Let’s […]
---
In my <a title="Exploring the Power of Deixis" href="exploring-the-power-of-deixis.md">previous post</a>, I explored why deixis is helpful, how it shows up in our language, and how its use in source code is hampered by limitations in our current programming ecosystems.

I promised I'd explain how we could remedy this problem to increase the expressiveness of our code... That's what this post is all about.
<h3>It starts with names</h3>
The magic that makes the web "hyper" is not really in tags. Sure, we use <code><a href="x">...</a></code> to point at something--but there are other ways to point. As I said in my previous post, line numbers point. Method names in source code point at their decl or their impl. Statements like <code>using namespace std</code> point. Names of build-time dependencies in maven pom.xml files point.

The <em>real</em> magic is that the web has so many things to point <em>to</em>. It has <em>names</em> (notice where "name" appears in the previous paragraph). Every resource--even ones that are dynamically generated--has a URL. Individual paragraphs or tables or images <em>inside</em> a resource can have names, which lets us point to them, too.

We value names.

<figure><img class="" src="http://imgs.xkcd.com/comics/permanence.png" alt="" width="740" height="650" /><figcaption>image credit: xkcd.com</figcaption></figure>

So, if names are so valuable, part of how we make code more "hyper" is to increase the availability of names. Here are some ways to do that.

<!--more-->

<dl><dt><strong>1</strong>. Every piece of structure in source code should have automatic names that derive from its position in a DOM, as specified by <a href="http://en.wikipedia.org/wiki/XPath" target="_blank">XPath</a> or something similar. Positional names are akin to the way humans describe things that they haven't bothered to name, as in “I like those blue flowers”; “Go 2 blocks straight ahead, then take your first left”. Examples of automatic positional names might include:</dt><dd>
<ul>
	<li>The first parameter to the <code>take_evasive_action()</code> method of the <code>spaceship</code> class might be accessible as <code>spaceship / take_evasive_action / params[1]</code> (XPath arrays are 1-based). If that parameter is named <code>threats_by_proximity</code>, then it should also be available as <code>spaceship / take_evasive_action / params / threats_by_proximity</code>.</li>
	<li>The second assignment statement made to variable <code>ticker_symbol</code> in function <code>divest_least_performing_stock</code> could be referenced as <code> divest_least_performing_stock / variables / ticker_symbol / assignments[2]</code>.</li>
	<li>The call graph for any element in code could be referenced as <code><em style="color:red;">URL_of_the_element</em> / call_graph</code></li>
	<li>The comment directly above a <code>for</code> loop could be referenced as <co<em style="color:red;">URL_of_the_for_loop</em> / comments_before[last()]</code></li>
</ul>
Note how the <a title="Introducing Marks" href="mountains-molehills-and-markedness.md">discussed</a> in previous posts provide a powerful way to qualify and query this sort of DOM. To find all classes that have GPL'ed code, you could use <code>my_project / classes[@marked(gpl)]</code>. To isolate all code that's sensitive to an AOP-style aspect such as the current logging strategy for the app, I can query for marks as well.


When you combine this with compile-time reflection, you have extraordinary power to make the compiler analyze, generate, and connect code.

</dd><dt><strong>2</strong>. Constructs in code that are currently anonymous (e.g., <code><em style="color:red;">URL_of_the_for_loop</em></code> in the example above) need to be explicitly nameable.</dt><dd>In the <code>intent</code> programming language that I'm designing, all block-level elements that would take a parenthesized expression in C++ are nameable with a phrase after their keyword:

<strong>C++</strong>
<pre style="font-size:90%;padding:.4em;border:solid 1px #dddddd;"><span style="color:green;">// If we can do more processing</span>
<span style="color:blue;">if</span> (remaining_item_count < total && available_time > 0) {
    <span style="color:green;">// body of the anonymous "if" block</span>
}</pre>
<code><strong>intent</strong></code>
<pre style="font-size:90%;padding:.4em;border:solid 1px #dddddd;"><span style="color:blue;">if</span> <span style="color:red;">we can do more processing</span> (remaining_item_count
... < total && available_time > 0):
    <span style="color:green;">// body of the named "if" block</span>
</pre>
In <code>intent</code>, the name of the <code>if</code> block above is <code><span style="color:blue;">if</span> <span style="color:red;">we can do more processing</span></code>. You can imagine similar names, like <code><span style="color:blue;">switch</span> <span style="color:red;">on the type of the most recent file</span></code>, <code><span style="color:blue;">while</span> <span style="color:red;">user can't log in</span></code>, <code><span style="color:blue;">try</span> <span style="color:red;">to connect to db</span></code>, <code><span style="color:blue;">else if</span> <span style="color:red;">backup storage is available</span></code>, <code><span style="color:blue;">closure</span> <span style="color:red;">that sorts IPAddr</span></code>, and so forth. Adding these names to the code is easy and intuitive, and it often allows us to subtract a comment that conveyed the same semantics in a clumsier way, making the code at least as terse. As a plus, when you move the block, you automatically move its name--you can't accidentally forget to move the explanatory comment.

Comments and string literals in intent are nameable by their first few words. And all nameable items can be targeted with shorter forms of the name in hyperlinks, as long as the words that remain in the name are unambiguous. So <code><span style="color:blue;">else if</span> <span style="color:red;">backup storage is available</span></code> and <code><span style="color:blue;">else if</span> <span style="color:red;">backup available</span></code> refer to the same place.

</dd><dt><strong>3</strong>. Code needs to be able to hyperlink to any nameable constructs in code, or to any other globally meaningful URL.</dt><dd>This allows arbitrary, rich content to be associated with code. (We can already do this, sort of, inside of comments, but the power of links in comments is limited. I want to hyperlink to a UML diagram or a use case, for example, and have the code fail to compile if my link is invalid. I want my hyperlink to cause a license file, a font, an SSL cert, or an icon to become a binary resource inside my executable. I want to be able to use something akin to the <a href="http://www.w3schools.com/tags/att_a_rel.asp" target="_blank">"rel" attribute on an html <code></code> tag</a> to specify the semantics of the link.)</dd><dt><strong>4</strong>. It needs to be possible to embed an explicit anchor in code.</dt><dd>While most linking should be possible with the previous 3 changes, it is conceivable that embedding an explicit anchor will occasionally be desirable. One use case is to allow external entities (not part of the programming ecosystem) to hyperlink inside code without needing to understand the DOM.


Another use case is to name paths or flows through code. Suppose you have a complex function that can flow in a couple dozen different ways due to permutations from conditionals and switch statements. How do you hyperlink to one of the paths that's dangerous, or that has performance problems? You can name branch points in the logic, and then hyperlink to the composite: <code><span style="color:green;">// Be careful when you edit code path <span style="text-decoration:underline;color:blue;">#A->C->C.1->G->X</span>; it is very sensitive to timing.</span></code>.</dd></dl>
<h3>Triangulation</h3>
Having more and better names is good, but it's not enough by itself. You may remember that in my previous post, I complained about the fragility of line numbers--we can't use them as permanent hyperlinks, because they change too often.

The positional names I mentioned above are subject to this same limitation--and to a lesser extent, some of the other names might "break" over time as well.

The way we fix this is to diff and triangulate. A given construct has multiple names--positional, natural, perhaps explictly assigned anchors... During compilation, as hyperlinks are evaluated, the compiler could store the main name that was used to construct a hyperlink, but also alternate names that resolve the same place. During refactors or subsequent compilation passes, alternate names could be used to repair broken links. Much as a diffing algorithm finds sequences of identical lines and then narrows in on what's changed to establish correspondence in a before-and-after view, a name diffing algorithm could repair links by isolating just those sequences of names that have changed, and then automatically updating broken variants when a majority of remaining names still agrees.

This allows warnings to hyperlink to their associated location in code, and to preserve that mapping across maintenance and evolution of the codebase. It makes other hyperlinks far more robust as well.

<a name="proxies"></a>
<h3>And we need proxies</h3>
Names and triangulation still aren't enough. I've alluded on previous posts to the idea that <a title="Lacunas Everywhere" href="lacunas-everywhere.md">code should be able to describe constructs that are not coded today</a>: use cases, personas, business requirements, etc.

The presence of these constructs in code does not have to be heavy. In fact, they can be proxied with light, declarative files that simply enumerate some key properties--and that hyperlink to external systems for greater details in a "native" non-code environment. Imagine a .yaml or .json file that describes key attributes of a persona, for example -- name, goals, typical permissions, use cases. Perhaps such a file contains a link to a usability database or a Product Management release plan with much richer detail; in such cases, the file is a sort of proxy for a larger concept that other professionals own.

Having that proxy can be enormously valuable. I can now assert that I have a test case that exercises each use case for each persona--and have the compiler walk hyperlinks to see if the assertion is true. I can assert that every feature used by a given persona is firewalled away from escalated privileges--and again, have the compiler walk hyperlinks to code paths and security marks and menu items and user input functions to see whether I'm right.

Proxies allow us to point to otherwise unpointable things like performance bottlenecks, design priorities, temporal boundaries, lifecycle phases in an app, and so forth. They complement and enhance the rest of the hyperlinking strategy.
<h3>The Value of Pointing</h3>
I said in my previous post that I got frustrated when my daughter used words like "that" and "here" without pointing. I couldn't understand her intent. Talking around this semantic deficit was time-consuming and error-prone.

By making it easy to point at any idea in the daily experience of a coder, I think the quality and terseness of our communication will grow dramatically. I gave a few <a href="../../../2014/09/23/exploring-the-power-of-deixis/#examples">examples</a> of how that power might generate innovation. (And btw, notice how my hyperlink to "examples" in that last sentence is a lot more useful because I can point to a specific paragraph).

Like all innovations, though, I don't think the exciting stuff is in the obvious examples. I believe we'll discover cool new ideas that we haven't even imagined yet, once the power of an improved paradigm permeates our coding lives.
