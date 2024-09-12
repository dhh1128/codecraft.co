---
title: Don Kleinschnitz: Put a stake in the ground.
date: 2012/09/14
slug: don-kleinschnitz-stake
---

<p style="text-align:right;"><em>(A post in my “<a href="/category/role-models/">Role Models</a>” series…)</em></p>
My huddle was not going well. I'd called a meeting to debate a tricky architectural problem with other senior engineers, and consensus was scarcer than working markers for our whiteboard. We were going round and round in circles.

<a href="http://www.linkedin.com/pub/don-kleinschnitz/1/779/6a4" target="_blank">Don Kleinschnitz</a> walked in. It was our first interaction--he'd only been introduced to the company as our new CTO a few days before--and I wondered whether he'd help us get off the dime.

Five minutes later, the meeting was over, and the controversy was settled. Don had "put a stake in the ground," as he called it -- picked a spot and made a tangible, semi-permanent choice to anchor our behavior.

[caption id="" align="aligncenter" width="320"]<a href="http://en.wikipedia.org/wiki/File:Wooden_stake_holding_guy_rope.jpg"><img title="wooden stake" src="http://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Wooden_stake_holding_guy_rope.jpg/320px-Wooden_stake_holding_guy_rope.jpg" alt="" width="320" height="240" /></a> A stake in the ground. :-) Photo credit: Wikimedia Commons.[/caption]

<strong>Answer the hard questions</strong>

I don't remember the question or the answer, but I do remember some of Don's solution. He immediately pushed us from generalities into specifics--what use case, <em>exactly</em>, would be affected by the decision? How much, <em>exactly</em>, would tradeoffs pay or cost in either direction?

Of course we couldn't answer Don's questions very well; nothing is more certain than ambiguity in software. But Don refused to let us off the hook, because he understood that <em>imperfect but specific answers are better than vague generalizations. Even if you have to guess.</em> (More rationale for this principle is elaborated in <a title="Role-Play Centered Design" href="/2012/06/20/role-play-centered-design/" target="_blank">the RPCD manifesto</a>.)

By putting a stake in the ground, Don wasn't being arrogant or unwilling to listen. He was simply recognizing that we had incomplete input, that the right answer was maybe guessable but not clear-cut, and that we'd be better off making a tangible experiment instead of debating intuitions. Maybe our answer would be wrong; if so, we'd adjust later. The cost of altering our trajectory would not be so high that it would invalidate the benefit of immediate progress.

<strong>Understand your assumptions</strong>

I saw Don model this pattern again when he was general manager of a newly created business unit inside Symantec. We were planning the first release of a suite melded from independently acquired products; the sales force's compensation and training were in flux; our outbound marketing strategy was unknown.

I think product management gulped when Don asked them for a credible sales forecast, a granular competitive analysis, a rationalized pricing strategy, and a business case justifying the feature sets they proposed to map to line items in budgets. Who wouldn't gulp? It was a <em>tall</em> order.

But Don wouldn't settle for finger-in-the-air answers. He dug out a set of spreadsheets from his MBA days and tweaked it. Hundreds of cells held our best-guess scores for the usefulness of features in our products and those of our competitors. Sheets captured assumptions. More sheets ran linear regressions to see if our price/performance fell in line with the industry.

He got pushback. "You've got so many assumptions that the model can't possibly be correct."

"Yes," Don would admit. "But insight, not perfect correctness, is what we're after. You get insight out of specifics. Should we give our installation's ease-of-use a 5 out of 10, or a 6? Not sure. But notice that the overall price/performance of our product doesn't change at all when we vary that number. We wouldn't know that unless we'd plugged in <em>something</em>. Forcing ourselves to give an answer has taught us something about our assumptions."

Don's model enabled smart action in the face of tremendous uncertainty.

<strong>Show, don't tell</strong>

Don is always tinkering with tools and processes that instill this habit in his troops. On another memorable occasion, we were wrestling with long, dry requirements documents. They were auto-generated from a requirements database, and they ran into the scores--maybe hundreds--of pages. Because they were so long, nobody liked to read them carefully. And because nobody liked to read them, they weren't producing the interlock we needed to keep five development sites aligned in a healthy way.

Don asked us to build a UI that manifested the existence of all features that would be exposed in our next release. It didn't have to <em>do</em> anything--just display what sorts of things would be possible.

At first I thought he was crazy. I told him it would take a long time.

"Not as long as requirements docs," he said.

"It will be ugly--completely lacking in any usability."

"So? We're not trying to model the customer experience. We can throw it away. The value is in forcing ourselves to be specific about what features we have."

I built the UI. And I learned <em>a ton</em>. A picture--even a sloppy one--is easily worth a thousand words. Especially if it's interactive.

Product managers saw the UI. After a suitable re-education so they knew not to worry about ugliness or awkward workflow, they started saying really insightful things, like: "If we expose features A and C but not B, a user who wants to do A→B→C will be frustrated." The concreteness of the UI was almost like magic.

I could go on and on about how Don lives this principle, but you get the idea: pose hard questions, get the best answers you can… then force yourself to put a stake in the ground, experiment with specifics, and learn from it.

Thanks for the lesson, Don.
<p style="padding-left:30px;text-align:center;"><span style="color:#000080;"><strong>Action Item</strong></span></p>
<p style="padding-left:30px;"><span style="color:#000080;"><em>Consider a current (or past) design decision that's been difficult to make. How could you make the decision easier by guessing about the likelihood of a use case, the preference of a user, or other aspects of context? If you got the answer wrong, how soon would you be likely to discover your mistake, and how expensive would it be to adjust your trajectory?</em></span></p>

---

Steve Tolman (2012-09-14 18:47:07)

Oh the memories!  I think you correctly described Don's ability to *enthusiastically* put a stake in the ground, but you are a little short in describing the amount of pain that caused, even after we were accustomed to this behavior.  I agree that it did wonders for our ability to make decisions, but it also yanked us through multiple knotholes on the way.  Looking back, I think they were necessary knotholes because we learned how to do multiple things.
1. We learned to deal with the discomfort of guessing and actually became quite good at using the available tools to sort through the uncertainty
2. We stopped fearing the unknown and became fearless at working through it all
3. We learned to apply this kind of thinking throughout the organization - at all levels
4. We became extremely effective and efficient at nailing what the customer wanted (although it took a while to work through the learning curve) - it allowed our engineering teams and our product management teams to learn to work together so much better
5. We were able to modify multiple processes to accommodate this approach - something our sister sites never could figure out

---

Daniel (2012-09-14 19:27:57)

Your point about pain is well taken. Putting a stake in the ground sometimes hurts. It can be disruptive. You should do it when you calculate that it's a net win--not thoughtlessly. Although this particular principle was an obvious part of Don's style, I also saw him be thoughtful and deliberative on many occasions. That's a better choice if the human stakes are high and the pay-off for quick momentum is not especially compelling.

I should probably add another caveat to my inaugural post about role models, admitting that none of the principles I want to highlight are <em>always</em> the right answer. Smart tradeoffs -- balance -- that's the eternal dance. Or, to borrow a phrase from another mentor I admire (you know who you are, but I won't let you remain anonymous forever... :-) -- "It depends." :-)

---

Don (2012-09-15 10:05:24)

You guys were on a team that in my career of 30+ years exceeded the performance of any team that I worked on before or after. 75 revolutionary features in one release is what rings in my ears as a benchmark that has yet to be beaten.
The more I learn about the craft of NPD the more I realize and we prove that at its foundation is learning and adaptability.
Most legacy NPD systems are based on "planning-do-act" kind of thinking. This assumes that NPD is a deterministic environment. ITS NOT!
The alternate is an adaptive system which operates on shortest possible start-work-failure-correct cycles .... like any adaptive control system would.
In an uncertain environment everyone especially us engineers seek precision but that will come only with learning cycles. So the STAKE starts the learning cycle....:)
Yes, change is always painfull, uncertainty is painful, but the eventual success and the excitement and fun of innovative engineering can make it worth it!

---

Baby Steps &laquo; Codecraft (2012-10-24 20:15:11)

[...] You might also think that baby steps are a repeat of my advice to put a stake in the ground. [...]

---

Daniel (2012-10-05 07:02:44)

Don: just came across a post from Seth Godin that teaches this same principle in a slightly different way: http://sethgodin.typepad.com/seths_blog/2012/10/waiting-for-all-the-facts.html

---

Interrupting my interruptions &laquo; Codecraft (2013-01-24 11:48:51)

[...] (or calling) are how I develop shared mental models, motivate and teach, manage momentum, and put a stake in the ground. Those wikipedia pages and chat sessions and interesting blog posts are part of learning [...]