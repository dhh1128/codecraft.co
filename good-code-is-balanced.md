---
title: Good Code Is Balanced
date: 2012-08-27
slug: good-code-is-balanced
redirect_from:
  - /2012/08/27/good-code-is-balanced
comments:
  - author: Metrics, Plumb Lines, and System Thinking &laquo; Codecraft
    date: 2012-11-12 08:37:28
    comment: |
      [...] I’m also a big believer in balance, as I’ve written about before. Good software balances many considerations. [...]
  - author: 3 Commandments of Performance Optimization &laquo; Codecraft
    date: 2013-01-08 09:08:29
    comment: |
      [...] On the other hand, it is possible to be too passionate about performance; optimizing the performance of the dev team (by decreasing coding and testing time) is often a better business choice than optimizing execution speed in ways that make code more complex and harder to verify. I have encountered performance zealots disqualifying a perfectly good design on the grounds that it’s not performant enough in a use case that only 2 customers on the entire planet would ever care about. Not smart. As I’ve said many times, good code is balanced. [...]
  - author: Earned Pragmatism &laquo; Codecraft
    date: 2013-01-18 08:53:32
    comment: |
      [...] you can be a pragmatist, you have to understand what’s possible, what’s good and bad about each alternative, and why certain considerations might trump others given a certain business context and time [...]
  - author: Smart Geeks Think Like Cheerleaders &laquo; Codecraft
    date: 2013-02-05 08:57:45
    comment: |
      [...] We champion the ideal implementation, programming language, product schedule, or architecture–so much so that we lose momentum or balance. [...]
---
In my <a href="what-is-good-code.md">first post about what constitutes "good code,"</a> I claimed we were dealing with a complex question. This is why I distrust short answers.

So many competing concerns must be balanced to achieve goodness:
<ul>
	<li>Testability</li>
	<li>Maintainability</li>
	<li>Short-term revenue pressures</li>
	<li>Long-term strategic value</li>
	<li>Performance (many aspects)</li>
	<li>Scalability (up, down, across)</li>
	<li>Ease of use</li>
	<li>Supportability</li>
	<li>Conceptual integrity</li>
	<li>Alignment with the skills, temperament, interests, and tools of the team that owns it</li>
	<li>Cost vs. benefit (for some problems, quick and dirty is definitely "right")</li>
	<li>Simplicity (separation of concerns)</li>
</ul>
More items undoubtedly belong on the list. Quite a balancing act!

<figure><img class=" " title="Balancing Act" src="http://farm4.staticflickr.com/3193/2991130266_7f315f456b_n.jpg" alt="" width="320" height="240" /><figcaption>Someone's got this "balance" thing down! Photo credit: joãokẽdal (Flickr).</figcaption></figure>
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Pick a module, application, or subsystem that you know well, and grade its code according to how much its coders emphasize a few different dimensions (e.g., performance, testability, scalability, ease of use). Do you like the balance? Are any attributes being neglected?</span></em></p>
