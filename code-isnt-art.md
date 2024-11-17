---
title: Code Isn't Art
date: 2012/09/23
slug: code-isnt-art
---

<a href="/category/guest-posts/"><img class="alignright size-full wp-image-553" title="guest post" src="http://codecraft.co/wp-content/uploads/2012/09/guest-post.png" alt="" width="183" height="40" /></a>Programmers, tell your inner artist to shut up.

One of the defining aspects of the Ruby programming language is that it is very flexible. It takes a very UNIX-like approach of having a few simple and well-defined functions that allow you to build rather complex systems. Unfortunately, it also ends up encouraging programmers to start thinking of their code as art, and then they start writing “clever” code. There’s nothing necessarily wrong with finding an unconventional solution to a coding problem, but that often falls apart when you have to involve another human in reading your “art”.

Let’s use an example from SQL of a “clever” solution. Take a look at the following query:
<p style="padding:10px;margin:10px 20px;font-family:courier, fixedsys;font-size:90%;background-color:#eee;border:solid 1px #ccc;">SELECT cl.Language, c.Name AS “Country Name” FROM CountryLanguage AS cl INNER JOIN Country AS c ON cl.CountryCode=c.Code SORT BY c.Code</p>
How long did it take you to read that query? Probably a good minute or two because you had to expand out all of the aliases to figure out what it’s doing. Compare that to the unaliased version below:
<p style="padding:10px;margin:10px 20px;font-family:courier, fixedsys;font-size:90%;background-color:#eee;border:solid 1px #ccc;">SELECT CountryLanguage.Language, Country.Name AS “Country Name” FROM Country Language INNER JOIN Country on CountryLanguage.CountryCode=Country.Code SORT BY Country.Code</p>
As you can see, it isn’t a “clever” query, but it sure is a lot more readable to a third party.

A lot of programmers will probably come back with “so what? I can read my own code and it gives me the result I want.” The fatal flaw here is that code is written not for machines, but for people. (Odds are good you’re also not going to be the only person that sees that code.) If we were writing for machines, you’d be using pure binary. All programming languages are made to give humans a way to express this in terms that are much more easily understood. Heck, SQL had an explicit design goal to be easily understood by accountants that needed to work with a database. The human element is crucial.

This is especially frustrating for those of us in support roles. I have a long history with SQL, some PHP experience, and I’ve done some dabbling with Ruby on Rails, but that’s atypical. Most support people don’t have any programming experience. What if they’re in a situation where they need to decipher the scripts that support a product or, heaven forbid, peruse the source code to try and find the cause of a particular error? They can probably figure out verbose code from having dealt with pseudo-code examples but will run straight into a brick wall if a programmer decided to be “clever”. Now the engineering team has to be drawn into something that could have potentially been resolved by support.

The question you have to ask yourself is if the ego boost from “clever” code is worth the increased work created when others don’t understand your “art”. I’m going to bet that your team members, members of supporting teams, and any management you report to won’t look favorably upon it.

<hr />

<img style="margin-right:20px;" title="Jesse Harris" src="https://lh5.googleusercontent.com/-JeFtN8B6Ogc/AAAAAAAAAAI/AAAAAAAABQc/SgA4WJc7j20/s250-c-k/photo.jpg" alt="" width="100" height="100" align="left" />

<em><a href="https://plus.google.com/108404514060536763555/posts" target="_blank">Jesse Harris</a> has been a geek since cutting his teeth on the Commodore 64 in pre-school. He currently works in support at RSA, the security division of EMC, and has been doing support, systems administration, and web development for 13 years.</em>
<p style="padding-top:1em;"></p>

---

Daniel (2012-09-23 17:55:58)

I see echoes of Martin Fowler ("any fool can write code a computer can understand; good programmers write code that humans can understand") in your thinking, Jesse. Also, you remind me of Richard Gabriel's notion of "habitability" (from _Patterns of Software_). He deplores cleverness and instead advocates making code approachable and comfortable for others.

BTW, in the subtitle of my blog, I assert that software = science + art + people. This might sound like we're at odds, but I don't think so. I'm claiming that human creativity, not just hard-core algorithms, is an essential ingredient of software; you're warning coders not to get carried away. I think that's good advice.