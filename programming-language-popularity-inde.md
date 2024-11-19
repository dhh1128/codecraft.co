---
title: Programming Language Popularity Index
date: 2013-03-22
slug: programming-language-popularity-inde
redirect_from:
  - /2013/03/22/programming-language-popularity-inde
comments:
  - author: Erik Prusse
    date: 2013-03-23 11:38:28
    comment: |
      What about COBOL, Pascal, Modula-2 and the other languages I learned in school? OK, I didn't learn COBOL in school; I'm not that old.
  - author: Daniel Hardman
    date: 2013-03-23 17:30:37
    comment: |
      Hah! I'm old enough that I learned Pascal and had teachers threaten to teach me Fortran, but I also missed the COBOL fun. Too bad; I could have made a mint on the Y2K bug. :-)
---
Here's an<a href="http://langpop.corger.nl/" target="_blank"> interesting chart</a>, giving a realtime view of which programming languages have high mindshare. The chart has one axis devoted to number of lines in code commits on GitHub, and another to how often the language shows up in tags on StackOverflow.

[caption id="attachment_1075" align="aligncenter" width="500"]<a href="http://langpop.corger.nl/" target="_blank"><img class="size-full wp-image-1075" alt="langpop" src="http://codecraft.co/wp-content/uploads/2013/03/langpop.png" width="500" height="372" /></a> Programming languages: what's hot (top right), what's not (bottom left). Top 3 rows of buttons are clearly where mindshare is at in the industry. Click for details.[/caption]

I don't think the chart is perfect. I've seen it billed as a "popularity index," but I think it might be better described as a measure of how busy the coders are who use each language. If most of the coders who use a language hate it, I don't think it's fair to call it "popular." Some apples-to-apples issues are glossed over, such as the fact that certain languages are very verbose, and some languages tend to get used mostly for "big" projects or for "small" ones. And the chart says nothing about the quality of systems built with the languages, or about the velocity of teams.

Nonetheless, it's an insightful view. I'm not surprised to see C#, Java, Javascript, PHP, C++, C, and Python as the clear hotspots. It's interesting to see where some older and less glamorous languages fall, like Perl and Visual Basic. If you're wondering which languages you ought to learn, this view might tell you the relative value of, say, Haskell vs. Erlang vs. F# vs. D.

<strong>Observations</strong>
<ul>
	<li>There are <em>a lot</em> of languages out there. What a busy world we live in! All the more reason to <a title="Julie Jones: Learn voraciously." href="julie-jones-learn-voraciously.md">learn voraciously</a>.</li>
	<li>Languages with a mediating runtime (JVM, .NET) are very popular, with languages that compile at runtime as a large subset. I don't think bare bones C/C++/Assembly/Objective C will ever go away, but the evolution toward higher level environments is clear.</li>
	<li>It's interesting to ponder what commonalities exist between sets such as languages that are growing quickly, languages that are stale and neglected, and so forth. Fodder for <a title="My First Tangle With the Tower of Babel" href="my-first-tangle-with-the-tower-of-babel.md">my experiments with language design</a>...</li>
</ul>
<strong>Questions</strong>
<ul>
	<li><span style="line-height:13px;">What languages are on your list for learning?</span></li>
	<li>What other comparisons of programming languages would you like to see? Average bugs per KLOC? Length of learning curve? Average team size? Geographical distribution? ...</li>
</ul>
