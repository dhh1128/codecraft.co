---
title: All I Really Need To Know I Didn't Learn In Compugarten
date: 2012-11-15
slug: all-i-really-need-to-know-i-didnt-learn-in-compugarten
redirect_from:
  - /2012/11/15/all-i-really-need-to-know-i-didnt-learn-in-compugarten
comments:
  - author: matt
    date: 2012-11-15 10:20:24
    comment: |
      effective logging techniques.  what, when
  - author: matt
    date: 2012-11-15 10:20:52
    comment: |
      what constitutes good code documentation...
  - author: shawn
    date: 2012-11-15 10:26:35
    comment: |
      I think more information about life cycles would be good to teach, I was taught the basics, but we never went into waterfall or agile, or anything else for that matter.
  - author: Brian Bellon
    date: 2012-11-15 10:52:06
    comment: |
      Coding to facilitate effective QA Automation - Hows, Whys, Benefits
      
      Working with a QA Engineer - What to expect from them - and what should be expected of you as a developer.
  - author: Daniel
    date: 2012-11-15 10:55:06
    comment: |
      Good ones, Brian! Automation is absolutely fundamental, nowadays. And it's definitely the case that some codebases are easier to automate than others.
      
      Working with QA is another great focus. So many developers don't make interactions with testers as productive as they could be. Maybe you should come guest lecture to set us straight. :-)
  - author: Daniel
    date: 2012-11-15 10:56:38
    comment: |
      Yes. It surprises me how little process/methodologies get discussed. CS classes where you have team assignments might be a good way to expose students to pair programming, sprints and scrum masters, and the rest of that part of what we do.
  - author: Daniel
    date: 2012-11-15 10:58:01
    comment: |
      Ooh, yes! Just yesterday I was meeting with a customer who was complaining that at normal verbosity, our log files had way too much detail about certain routine operations. Knowing what to put in a log, when &mdash; and knowing how to make the info that's written as useful as possible &mdash; would be a great topic.
  - author: Erik Dietrich (@daedtech)
    date: 2012-11-15 11:50:22
    comment: |
      I think it would be interesting and beneficial to have a CS program where students started a project as freshmen and it extended beyond the "boundaries" of the semester long course.  There are a lot of good lessons to be learned from having to live with your code for months and years rather than days and maybe weeks.
  - author: Daniel
    date: 2012-11-15 11:54:06
    comment: |
      Great idea. This might be particularly useful if students had to collaborate on the code with others. Imagine seniors having freshmen edit their code, and trying to manage the mentoring and communication to keep the design pure.
      
      Your idea reminds me of a <a href="http://www.ted.com/talks/shimon_schocken_the_self_organizing_computer_course.html" rel="nofollow">TED talk</a> I saw recently. A professor decided to have students start by building logic gates, then integrated circuits, then CPUs, then a compiler and programming language, and finally a game. Very cool. I want to take that class.
  - author: Daniel
    date: 2012-11-15 12:41:47
    comment: |
      Forgot one obvious biggie: antipatterns. Really great opportunity to discuss lots of Dilbert cartoons. :-)
  - author: Shawn Holmstead
    date: 2012-11-15 15:36:04
    comment: |
      Effective refactoring... learning to live with code that has been around for a long time and how to make it better.  Putting in time in a schedule to refactor.
      Test driven development (unit, integration, and acceptance tests).
      Communicating with product managers through acceptance tests (Required Reading: <a href="http://www.amazon.com/Bridging-Communication-Gap-Specification-Acceptance/dp/0955683610" rel="nofollow">Bridging the Communication Gap</a>)
  - author: Carl Appellof
    date: 2012-11-15 19:08:48
    comment: |
      Ways of suppressing repeated errors in logs would be good too.  It does no good to fill a log with the same critical message 10,000 times in a row, even if the error occurs 10,000 times in one minute. Even better if you really CAN record all the errors in compact form, with a smart viewer.  I can't count the times I've asked a customer - "Could you run that failed backup one more time, but with the verbosity turned up just a little?"
  - author: Carl Appellof
    date: 2012-11-15 19:10:53
    comment: |
      How to persuade your boss something really IS worth doing, even if it's not in the schedule, not vetted by a product manager, and doesn't look cool on the surface.
  - author: Daniel
    date: 2012-11-15 19:17:02
    comment: |
      Now <em>that</em> is a skill we all need! Are you sure you don't want a career in politics? :-)
  - author: Daniel
    date: 2012-11-15 19:18:04
    comment: |
      This is a great sidebar topic. Maybe logging systems need some kind of a logIfThisHasntHappenedRecently() function. What ideas do you have about how to achieve this?
  - author: Brian
    date: 2012-11-16 15:45:57
    comment: |
      Daniel - a few additional ones that come to mind:
      
      SOWs, Contract Negotiations, Open Source Rules (GPL, etc.), IP Protection, Escrows, Legal issues - Engineers often get pulled into these areas but don’t have the formal background or introduction in many of these topics, aside from what they learn on the job. They will get pulled in at some point.
      
      Roles and Responsibilities &mdash; a holistic review of cross-functional players most engineers will interact with throughout their careers.  PGM, PM, Marketing, Sales, Architects, Account Managers, Legal, Support, Q/A, etc.  Building a good software product isn't the end of the line, it’s only the beginning.  Need to have a holistic view of how a functioning software company/division operates, who the players are, what their roles are, and how the rest of the business operates. 
      
      Speaking with and Presenting to Customers &mdash; The difference between the language of internal speak vs. external speak, tech speak vs, customer speak.  How to present and speak with customers, partners, OEMs.  What NOT to say is just as important as what to say.
      
      Customer Focus at ALL Times / Usability &mdash; Customers are not as smart as you are!  It’s a lot more difficult to take a complex problem and make it easy to understand than it is to take a simple problem and complicate the heck out of it.  There is always a tendency toward the latter &mdash; avoid that tendency if you want to sell your products to customers.
      
      The Value of Accurate Velocity Estimation &mdash; it impacts all layers of the business, from internal and external roadmap predictability, to budgets, to commitments with customers and partners, to revenues, to reputation, to image, to long-term viability and sustainability.
      
      Globalization / Localization &mdash; The world is a small place today.  Most engineers will need to understand good localization techniques and strategies as their products will be shipped all over the world, in a wide variety of different languages, markets, channels, etc.
      
      Competitive Understanding &mdash; Where the market’s going, who the players are, who is considered “the best” even if they’re not, what the analysts are saying, how to beat the competition.  NOTE:  It’s not always a technical answer.
      
      Consistency!  Consistency!  Consistency!  - Repeatable, best-practice processes that ensure the success of each release.  Plow improvements into the process with each successive release.  You’d be surprised how few companies actually have good process in place, or how many have no process whatsoever.  Fly-by-the-seat of your pants programming doesn't cut it, unless you’re building your own Angry Birds knockoff in your basement for iTunes.
  - author: Linda Hardman
    date: 2012-11-16 16:50:31
    comment: |
      Love my awesome, smart, husband Daniel.
  - author: Daniel
    date: 2012-11-16 16:51:03
    comment: |
      Wow, Brian. You should be teaching this imaginary class &mdash; and just with your list, I think there'd be material for a semester or two, easily.
      
      Your first time items, especially, had me slapping my forehead. All the legal issues around software development need to be more broadly understood. No doubt about it. And understanding what a healthy tech company looks like, in terms of all the different disciplines it takes to build a business, is absolutely critical.
      
      I agree about the value of velocity estimation. I'm curious to know what techniques you think have been the most helpful on that one; it still feels pretty elusive to me.
      
      The competitive understanding discussion is one that you and the rest of the gang from Symantec could talk about at length. Some of the price/performance analysis you did, (the beating-the-streets aspect, the research through IDC/Gartner databases, the linear regression, the analyst and customer calls), deserves to be legendary. It's too much of a well-kept secret.
  - author: Daniel
    date: 2012-11-16 17:02:34
    comment: |
      Okay, Sean. You've added a book to my reading list!
---
I'm glad newly minted software engineers are exposed to data structures, compilers, concurrency, graph theory, assembly language, and the other goodies that constitute a computer science curriculum. All that stuff is important.

But it's not enough.

<figure><img src="assets/cs-lecture.jpg" /><figcaption>Not all classroom material for CS folks should be technical. Image credit: Midjourney.</figcaption></figure>

Since I'm half way to curmudgeon-hood, I frequently find myself lamenting educational blindspots in the young. I've even toyed with the idea of teaching at the nearest university, some day when I Have More Time™. If academia would take me, my lesson plans might cover some of the following topics:
<ul>
	<li>How to work with smart but misaligned teammates, manage opinioand personalities, and contribute to a cohesive team. (Software development is a <em>team</em> sport, young padawan.)</li>
	<li>The power of metaphor in software design. (See <a title="Good Code Is Named Right" href="good-code-is-named-right.md">this post</a>.)</li>
	<li><a title="Why Exceptions Aren’t Enough" href="why-exceptions-arent-enough.md">Choosing a good error raising and error handling strategy</a>. (Assignment: find half a dozen error messages in open source projects, and rewrite them to make them intelligible to the Average Human.)</li>
	<li>The art of <a title="Good Code Is Balanced" href="good-code-is-balanced.md">tradeoffs</a>. (Usually, there ain't no such thing as a free lunch.)</li>
	<li><a title="Coping With Organizational Alzheimers" href="coping-with-organizational-alzheimers.md">Managing technical debt</a>.</li>
	<li>Using version control, especially somewhat diverged branches.</li>
	<li>Communicating effectively with remote collaborators, including those whose native language is not your own.</li>
	<li>Data- and <a title="Good Code Is Optimized" href="good-code-is-optimized.md">user-driven optimization</a>. (Required reading: <em><a class="zem_slink" title="The Goal: A Process of Ongoing Improvement" href="http://www.amazon.com/Goal-Process-Ongoing-Improvement/dp/0884271781%3FSubscriptionId%3D0G81C5DAZ03ZR9WH9X82%26tag%3Dzemanta-20%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3D0884271781" target="_blank" rel="amazon">The Goal</a></em>, by Eliyahu M. Goldratt).</li>
	<li>Understanding and speaking the language of business.</li>
	<li><a title="Six Learning Tips For Tech Folks" href="six-learning-tips-for-tech-folks.md">Learning how to learn</a>, to keep up with the industry after you leave school.</li>
	<li>Estimating wisely.</li>
	<li>Finding the non-obvious human and process levers in an organization to get things done.</li>
	<li><a title="// Comments on Comments" href="comments-on-comments.md">Effective commenting</a>.</li>
	<li>Coding for maintainability.</li>
	<li>Great role models in software development.</li>
	<li>Common newbie and journeyman mistakes.</li>
	<li>A running contest where any student is invited to stump the rest of the class to find some problem that doesn't already have at least one useful open-source library you could use as a starting point. (Newton: "I have stood on the shoulders of giants.")</li>
</ul>
This is only the beginning of my lesson topics; I'm sure I could come up with dozens more, if I thought for a while.

What would you add to the list?<strong> <span style="color:#000080;"><em>Please comment. And please subscribe to my blog (top of right sidebar) for explorations of these topics.</em></span></strong>
