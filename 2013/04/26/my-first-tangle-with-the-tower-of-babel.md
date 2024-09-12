---
title: My First Tangle With the Tower of Babel
date: 2013/04/26
slug: my-first-tangle-with-the-tower-of-babel
---

A while back, I was reading the blog of somebody smart (can't remember who), and a comment jumped out at me: "If you <em>really</em> want a black belt in computer science, try writing a programming language. The depth and breadth of experience you get when you invent Python or Lisp or Smalltalk or C++ or C#--and implement its ecosystem, not just code a parser for a CS class--gives you a wisdom and education that's rare and precious." (I'm paraphrasing here, but that's the gist of it.)

<em>Sounds good</em>, I thought. <em>I think I'll give it a shot.</em>

[caption id="" align="alignright" width="289"]<img class=" " alt="" src="http://upload.wikimedia.org/wikipedia/commons/a/af/Confusion_of_Tongues.png" width="289" height="334" /> "Confusion of Tongues", by Gustave Doré. The Tower of Babel resonates beyond moral history. Image credit: Wikimedia Commons.[/caption]

I began doing research and taking notes. I thought hard about which features I liked and detested in programming languages. I read critiques and tributes to various languages by detractors and fans. I identified pieces of syntactic sugar that I wanted to support. I took a wad of existing code and tried to rewrite it using the language I was drafting. I picked some conventions for filenames. I played with yacc and antlr and experimented with definitions of context-free grammars.

And then I stalled.

It wasn't good enough.

My new language was nifty. It combined a lot of the best features of my favorite languages: closures, list comprehensions, lambdas, static if, robust type inference, unified function call syntax, with blocks, variadic templates, mixins, nullable primitives, built-in support for design by contract, and more. I actually believed (perhaps naively) that I knew how to implement a good portion of these ideas in a compiler.

But I began to intuit that nifty != great. And the longer and harder I thought about it, the more convinced I became.

<!--more-->Some of you know that I have a background in linguistics (which may explain why this project appealed to me). One of the lessons I learned in my graduate program is that language and world view are profoundly related. Choices we make in our languages affect our thinking, not just our productivity. My favorite example is the from <em>Women, Fire, and Dangerous Things</em>, by George Lakoff: the Dyirbal language in Australia has four "gender" categories for nouns, and one of them includes everything in Lakoff's title. You can't talk about nouns in this language without using its gender mechanism, and this requires you to perceive and communicate categories according to its system. <a title="Why Mental Models Matter" href="../../../2012/11/05/why-mental-models-matter/">Mental models matter</a>.

I connected this insight from natural human language to my experiment with computer language creation like this: <em>All of the coolness I was throwing into my language wasn't changing the way a programmer would think about a coding problem all that much.</em> Sure, some of these innovations would let you short-circuit a problem, eliminate redundancy, write tighter or simpler code. But if I could port java or python into it more or less directly, then the languages were kissing cousins, and I didn't feel like I could go out and evangelize my creation as being <em>better enough</em> to be worth the bother of a new learning curve. Programmers have better things to do than learn languages just for fun, and I have better things to do than to write a vanity language.

I turned to deeper investigations. I was intrigued by <a title="Alan Kay OOP Messaging" href="http://c2.com/cgi/wiki?AlanKayOnMessaging" target="_blank">Alan Kay claiming that OOP was misnamed and should have highlighted messages, with objects as a secondary concern</a>. I downloaded Smalltalk and played around a little.

I spent some time studying bugs. Why do they happen? Is there a way to make a language discourage or prevent them, and is the juice worth the squeeze? Can a language be immune to certain kinds of <a title="Tech Debt, Leverage, and Grandma’s Envelope" href="../../../2012/10/30/tech-debt-leverage-and-grandmas-envelope/">tech debt</a>, by design?

I investigated some more exotic (largely functional) languages: Erlang, Haskell, OCaml, Clojure. I learned a little Lisp. I read an <a href="http://www.winestockwebdesign.com/Essays/Lisp_Curse.html" target="_blank">insightful essay</a> that made me think about the social aspects of programming languages and about the personality and zen of language communities.

I have concluded that in order for a new, general-purpose programming language to provide significant value to the community, it doesn't just have to be Turing complete and cool. It must:
<ul>
	<li><span style="color:#000080;">Have a consistent and powerful organizing paradigm that inspires creativity and design insight.</span> <span style="color:#808080;">(Lisp and Smalltalk are both outstanding in this dimension; Java's a bit anal about OOP but I think misses the forest for the trees [<a href="http://steve-yegge.blogspot.com/2006/03/execution-in-kingdom-of-nouns.html" target="_blank"><span style="color:#808080;">nod to Yegge</span></a>]. PHP is awful on this dimension, IMO.)</span></li>
	<li><span style="color:#000080;">Solve compelling problems unusually well.</span> <span style="color:#808080;">(C or C++ is the go-to answer for performance; Perl used to be the de facto solution for serious text crunching, before other languages matured their regex libraries; Ruby's great for MVC web apps...)</span></li>
	<li><span style="color:#000080;">Attract a community of people that are disposed to cooperate and that buy into the zen of the language.</span> <span style="color:#808080;">(This is Lisp's fatal weakness; it attracted a community, but it was a community of maverik loner geniuses who used immense power to reinvent everything per personal preference. Java, Python, Ruby, and C++ are strong here.)</span></li>
	<li><span style="color:#000080;">Advance the state of the art in significant ways.</span> <span style="color:#808080;">(I'm not sure a language has truly changed the way we think about programming problems for a generation. See Alan Kay's Turing Award lecture. D pushes the limits of a C/C++ worldview pretty darn far, but it's a proximate evolution, not a quantum leap. Some experimental languages out of academia are promising, but are too weak on the other dimensions to get any traction. Am I wrong?)</span></li>
</ul>
So I've had my first tangle with the Tower of Babel, and I'm now in ponder mode. What would truly change programming paradigms for the better in a basic way?

I think the answer may lie in <a title="6 Strategies to Simplify Software" href="../../../2013/03/12/6-strategies-to-simplify-software/">finding new accommodations</a> for all the <a title="The Power of Simplicity" href="../../../2013/02/15/the-power-of-simplicity/">complexity</a> we wrestle. New ways to think about concurrency, distributed architectures, object lifecycle, and communication may be involved. A facilitation of <a title="Smart Geeks Think Like Cheerleaders" href="../../../2013/02/05/smart-geeks-think-like-cheerleaders/">system thinking</a> may help. I'm now studying shared transactional memory, actor systems, variants of declarative programming, and so forth. I'm not sure where I'll end up, but I plan to blog about my discoveries as I go along. Look for posts in the "better programming language" category...

I am also very interested in your insights. <span style="color:#000080;">What do you think would make a new programming language not just fun or interesting, but so compelling that you'd have to master it and tell all your friends?</span>
<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://redmonk.com/dberkholz/2013/03/25/programming-languages-ranked-by-expressiveness/" target="_blank">Programming languages ranked by expressiveness</a> or <a href="http://redmonk.com/sogrady/2013/02/28/language-rankings-1-13/" target="_blank">popularity</a> (redmonk.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://www.javacodegeeks.com/2013/04/choosing-a-programming-language.html" target="_blank">Choosing a Programming Language</a> (javacodegeeks.com)</li>
</ul>

---

The genesis of a new realm called &#8220;possibility&#8221; | power of language blog: partnering with reality by JR Fibonacci (2013-04-26 15:04:24)

[...] My First Tangle With the Tower of Babel (codecraft.co) [...]

---

Why Your Software Should Cry | Codecraft (2013-05-06 11:51:03)

[...] was writing recently about my adventures designing a programming language. I concluded that more sugary syntax isn’t really a great value to the community–but a [...]

---

Programming Language Popularity Index | Codecraft (2013-05-31 01:28:48)

[…] It’s interesting to ponder what commonalities exist between sets such as languages that are growing quickly, languages that are stale and neglected, and so forth. Fodder for my experiments with language design… […]

---

Good fences make good neighbors | Codecraft (2013-05-15 08:50:36)

[…] my pondering on programming languages leads me to believe that encouraging correct thinking about encapsulation is a desirable attribute. […]

---

Headers, babies, and bathwater | Codecraft (2013-08-12 11:02:33)

[…] simple interface that consumers can read. This is the basic idea behind Lazy C++, but if I were writing my own programming language, I’d take it much […]

---

Julie Jones (2013-09-08 22:19:18)

I think you really hit the nail on the head with "change the way we think". Of all the languages that come and gone none have really changed the way we think about solving problems in the last thirty years. There have been a few that had potential, but I can't think of any that brought a new paradigm to light. Erlang is the only one I can think of that has picked up a decent following by managing to make one previously hard thing easy (multi-processing), but it is hardly revolutionary.

---

The third half of computational economics | Codecraft (2013-08-09 11:58:48)

[…] I don’t think a system like this would be worth building in all cases, and it might have some unpleasant side effects like starvation of a humble process that can’t adequately compete for resources. It would require measurement and tuning. It might require some variant of genetic algorithms so initial profit formulas would evolve. But I can imagine this approach having nice benefits for a certain class of thorny problems. I wonder if I could build this concept into a better programming language… […]

---

Programmers: learn how to &#8220;cloudify&#8221; | Codecraft (2013-07-23 11:43:09)

[…] new installments. I’ll be making connections back to concepts here on codecraft, such as what the programming language of the future ought to look like, how to encapsulate for cloud, and so […]

---

Exploring the Power of Deixis | Codecraft (2014-09-23 08:34:56)

[…] of the goals of the intent programming ecosystem I’ve begun to create is to empower this sort of deixis without creating any new overhead for engineering teams. As […]