---
title: Evolving Software Politics
date: 2012/09/11
slug: evolving-software-politics
---

I find a lot of insight in <a title="soft-con and soft-lib" href="https://plus.google.com/u/2/110981030061712822816/posts/KaSKeg4vQtz" target="_blank">Steve Yegge's suggestion</a> that we think about the world views of software engineers along a conservative (risk-averse) versus liberal (change-friendly) axis. I have some quibbles, to be sure:
<ul>
	<li>I'm not sure how well Steve's labels resonate outside the U.S.</li>
	<li>I think software conservatism is more focused on permanence than risk aversion.</li>
	<li>I don't think programmers are all that consistent in their views. I can find evidence of both soft-con and soft-lib thinking in my own philosophies.</li>
</ul>
That said, I think I've evolved from a conservative to a more liberal perspective over the years. At one point in my career I got quite annoyed at C++ coders who were careless about how they used <code>const</code>. It still bothers me a bit--but now I care about productivity more, and I buy the value of languages enforcing best practices less, than I used to. I love python and "<a href="role-play-centered-design.md" target="_blank">teams should deploy evolving software by assigning humans to role play architectural components, and see what happens</a>--that's about as ultra liberal as it gets.

[polldaddy poll=6531418]

 

Why has my world view evolved?

I think I've come to agree very strongly with Steve's observation that software is impermanent. Little if any software stands the test of time. In the mid '90s I worked on some Visual Basic code that had ancient Basic modules in it, with comments from the mid 70's. I hated that code--imagine the worst features of spaghetti code, hungarian notation with obsolete data types, deep technical debt, tight coupling, poor encapsulation...--this was a poster child. The code wasn't dead, but it should have been. 20 years is too long for almost all code. (I'm adding a chapter about the profound benefits of death in my biology~software metaphor, in my forthcoming book, <em>Lifeware</em>.)

When you accept that software is impermanent, you can relax. There doesn't have to be a centrally planned vision that remains constant over time; you can discover things as you go, and it's <em>all right</em>.

Don't confuse this with me being lazy. I think code should be clean and cohesive; see <a href="/category/good-code/" target="_blank">my posts on "good code"</a> for more on that. I'm simply saying that you should embrace the idea that things change. Requirements shift. Teams go through learning curves. Staff has turnover. Products lose or gain competitive advantage. The market adjusts. Better frameworks come out. New OS features appear. And the implication of this change is that today's right answer might need some tweaking tomorrow.

Faced with that change, the ability to react quickly and calmly, to be entrepreneurial and experiment-driven, is often of greater business value than a perfect piece of code.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">List three things about your project's landscape (market, team, technology, ...) that have changed in the past year. Do any of these make earlier decisions more or less appropriate?</span></em></p>