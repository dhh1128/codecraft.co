---
title: How to turn coding standards into epic fails -- or not
date: 2012-09-27
slug: coding-standards
---

[caption id="attachment_580" align="alignright" width="285"]<a href="http://www.epicfail.com/2012/08/31/todays-special-fail/todays-special-fail/"><img class="size-full wp-image-580" title="sign-fail" alt="" src="http://codecraft.co/wp-content/uploads/2012/09/sign-fail.png" width="285" height="525" /></a> Yes, a restaurant really displayed this sign. I doubt it influenced anybody's behavior...[/caption]

Some attempts to influence the behavior of other people succeed; others are doomed from the get-go.

Coding standards are usually written because we want to influence the structure or style of code produced by engineering teams. Sometimes they're helpful; more often they're ignored and forgotten; occasionally they provoke fireworks or bitter resentment.

I'm not sure there's a guaranteed formula for success, but there's a guaranteed formula for failure; let's cover that first, and then see what helpful suggestions we can derive.

<strong>How to turn coding standards into epic fails</strong>

<em>1. Micromanage.</em>

Leave no room for personal style and creativity. Make no attempt to distinguish between meaty issues and utter trivialities. State all rules in absolutes; allow no exceptions. Announce enforcement in code reviews. Bonus points if you actually follow through on the threat, and double bonus points if you display some other developer's code in front of the team as an example of egregious violations.
<p style="margin-left:2em;margin-right:2em;padding:.5em 1em;background-color:#eee;border:solid 1px px #ddd;font-family:times;">"Always put a space between an identifier and a curly brace, except in nested struct initializers where the first member is a string literal (other than NULL) or a #define'ed constant."</p>
<p style="margin-left:2em;margin-right:2em;padding:.5em 1em;background-color:#eee;border:solid 1px px #ddd;font-family:times;">"Begin every function with a comment that specifies the name of the coder, the date the function was last modified, the purpose of the function, an annotated history of how the function has evolved over time, a list of functions called by your function, your zodiac sign, and the names of all parameters. Make sure that parameters are listed alphabetically (case-insensitive), with a blank line between each, and the explanatory text after the param name indented 8 - (len(param name) mod 4) spaces."</p>
<em><!--more-->2. Overreach.</em>

Make sure your coding standards cover every language, platform, compiler, and IDE. Don't forget macros in Excel. For the sake of consistency, keep all rules invariant across all environments; if you like pep8 in python, you should definitely use it in VBA and java and C++ as well. Disallow javascript minify because it violates your naming conventions; make sure all environments use parens the way eLisp expects. Roll all of the standards out at once. Put multi-part version numbers on your standards, preferably derived from the year, month, day, hour, minute, second, and timezone. Check the standards into version control. Arrange to have the standards in the new hire orientation packet.

<em>3. Mandate redundancy.</em>

Choose rules that make code say the same thing in several different ways -- preferably separating the redundancy as much as possible so it's hard to modify correctly.
<p style="margin-left:2em;margin-right:2em;padding:.5em 1em;background-color:#eee;border:solid 1px px #ddd;font-family:times;">"End every function with a comment that says the function has ended. Make sure you include the function name in this comment. That way, we can find unterminated functions by looking for function identifiers with an odd number of hits when grepping through headers."</p>
<p style="margin-left:2em;margin-right:2em;padding:.5em 1em;background-color:#eee;border:solid 1px px #ddd;font-family:times;">"At the top of every module, put a comment that gives the name of the module, a description of the module's purpose, then 'Copyright © Acme Corporation Inc., 20??, all rights reserved.' (Use the copyright symbol, not (c), and add correct digits for year...) At the top of every class, put a comment that gives the name of the class and a description of the class's purpose. Group all static methods together, and put <code style="color:green;">//static methods</code> on a line above them."</p>
<em>4. Beat a dead horse.</em>

Tell, don't show; every rule should be described in careful detail. Put your standards in a Word doc; make sure it has a title page, table of contents, index, and a header and footer that contain an embedded version stamp, author name, and last print date. Use bold, italics, and all caps liberally (through styles, not one-off formats; remember that you'll be releasing updates...). Export the doc to help those who can't read your format. Attach four versions (doc, docx, pdf, eps) to a wiki page, and to a department-wide email. Print a master copy on the color laser printer, then go to Kinkos and have a color copy printed and bound for each employee. Arrange to have it delivered to their desks.

Make a powerpoint slide or two highlighting key areas in the table of contents; attach that to the wiki as well. Ask for time in a company meeting to show your slides, so people are mentally prepared for the doc that's been delivered to their desks. Apologize for making some decisions by fiat instead of consensus; give a few specific examples.

A few days later, broadcast a follow-up email asking for feedback and reminding everyone of new enforcement procedures. After you realize that you didn't repeat your original attachments in the follow-up email, reply to all with the missing attachments. After that, reply to all with a hyperlink to the wiki page that has all the attachments, since that page will be guaranteed to be kept up to date as the standard evolves.

<hr />

<strong>Suggestions for success</strong>

If the foregoing ideas don't excite your enthusiasm, I endorse the following:
<ul>
	<li>"Simple, clear purpose and principles give rise to complex, intelligent behavior. Complex rules and regulations give rise to simple, stupid behavior." (Dee Hock)</li>
	<li>Happy teams are built on trust and mutual respect. Most tech folks are smart and share these values. Preserve pride of ownership and individual creativity.</li>
	<li>Some standards have more business and/or technical value than others. Seek biggest bang-for-the-buck.</li>
	<li>"A foolish consistency is the hobgoblin of little minds." (Emerson)</li>
	<li>Concision counts. If you can't fit it on a single page, forget it.</li>
	<li>Show, don't tell. Text = blah blah blah. Screenshot = good. Code that models correct behavior = better (momentum, fait accompli, copy/paste benefits, etc).</li>
</ul>
If you read that list and think: "Well, then, why have coding standards at all?", then I have done you a disservice. Teams <em>definitely can</em> benefit from conventions and standards, in many cases. Here are a few rules I might propose in the next coding standards I work on.

<strong>Sample suggestions (not "rules") from a wise coding standard</strong>

In general, model new code after the conventions embodied by recent and clean code you see in the codebase. The following modules are known to be good examples: moduleA, moduleB, ... <em>(Value: high. Cost: low. Pointing out some good examples will do more than a dozen pages of text. Also, pointing people to new code allows wisdom about conventions to accrete organically.)</em>

<a title="Small Files Are Your Friends" href="small-files-are-your-friends.md">Keep files small</a>. <em>(Value: high for casual maintainers. Cost: usually low. Many good habits are tied to this guideline, including loose coupling, encapsulation, refactoring, and modularity.)</em>

Clean up messes. Delete unused files, functions, and blocks. <em>(Value: high. Cost: low. C<em>asual maintainers don't have to wonder about the significance of something inert. Reinforces refactoring.</em>)</em>

Use descriptive names for classes, functions, variables, and files, so you don't have to document what should be obvious semantics. <em>(Value: high. Cost: low. Eliminates redundancy and encourages good refactoring habits. <a title="Good Code Is Named Right" href="good-code-is-named-right.md">Good code is named right</a>.)</em>

<a title="// Comments on Comments" href="comments-on-comments.md">Comment what can't be made obvious</a>. <em>(Example where comment might be helpful: subtle precondition or postcondition on a function. Value: high. Cost: low.)</em>

Carefully follow the codebase's <a title="Good Code Plans for Problems" href="good-code-plans-for-problems.md">error and exception strategy</a>. <em>(Example: "In C++, use RAII to guarantee exception safety. Make sure all errors are complete sentences, since they'll appear in logs and be read by end users." Value: high. Cost: medium.)</em>

Name files and directories with a consistent pattern. <em>(Example 1: use all lower-case, with underscores between words. Example 2: use Java's conventions. Value: high. Cost: low. Eliminates #include "WrongCase.h" problems on *nix; makes batch processing easier.)</em>

Roughly, follow formatting conventions common to your language and recommended by your IDE. Use the team's standard indent (e.g., 4 spaces) so different editors don't produce ragged gobbledygook. <em>(Value: medium. Cost: low. Mainstream formatting is usually pretty readable. This rule is stated with enough flexibility to leave moderate room for personal preference.)</em>

Name unit tests after their main assertion, so you know what's wrong when you see what failed. <em>(Example: test_removeChild_throws_when_container_empty. Value: medium. Cost: low.)</em>

<strong>Benefits</strong>

Stupid coding standards are offensive and a complete waste of everybody's time. If you promulgate standards like the ones I offered at the top of this post, you deserve to fail. On the other hand, rational, reasonable standards can help a team enjoy working together, flatten the learning curve for new folks, promote good habits, cheapen automated analysis, and foster pride of ownership.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">If you have existing coding standards, look at a few guidelines and decide A) how much technical and business value they provide; B) how easy they are to learn and follow; C) how well they're implemented. Do you see any places where you want to adjust?</span></em></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">If you want to create a coding standard, make a list of rules that have a high ratio of value to cost. Pick the top 10 (or as many as you can fit on one (1) sheet of paper with a normal font and margins). Float a few past other thought leaders. Keep the best ones only.</span></em></p>

---

Add some more extra redundancy again | Codecraft (2014-01-15 08:39:13)

[…] precisely because they create redundancy that’s difficult to understand and maintain. Foolish coding standards and dumb comments are notorious for creating busywork this […]

---

Wheeljack (2018-06-18 08:16:59)

I caught this way too late to matter but I would say that the "standard" (because we all know it's not one) should be available not just for new hires but interviewers as well.  Concealing an insane set of half-baked rules really just wastes competent programmers' time and reinforces the notion that you did this deliberately to trap them.  Let me just walk out of the interview or turn down the offer before we get to the point and save us all alot of trouble.

Because the instant some framework monkey struggling with Hello World gets on my case about bracket placement, that's it, I'm done.  I'll hang around and collect a paycheck until I find something else but you won't get anything of value out of me for whatever time remains.

---

Daniel Hardman (2018-06-18 11:43:04)

Agreed!

---

On Forests and Trees | Codecraft (2015-09-02 08:48:55)

[…] is partly why small files and small functions are your friends. It also explains why boilerplate comments are worse than useless, and bears on why encapsulation and loose coupling are so […]

---

Lacunas Everywhere | Codecraft (2014-07-16 13:58:41)

[…] like to enforce coding standards–formatting and naming conventions, maybe, but also trickier stuff, like “we strictly […]

---

Thoughts On Bridging the &#8220;Lacuna Humana&#8221; | Codecraft (2014-07-21 08:49:29)

[…] to the point where they actually create unnecessary confusion. They are not mandatory (except by human fiat, which is usually ignored), and everybody’s judgment about where they’re valuable seems to vary. Some coders are […]