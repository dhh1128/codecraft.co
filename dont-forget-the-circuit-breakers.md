---
title: Don't forget the circuit breakers
date: 2013-01-11
slug: dont-forget-the-circuit-breakers
redirect_from:
  - /2013/01/11/dont-forget-the-circuit-breakers
comments:
  - author: Rob Stutton
    date: 2013-01-11 18:25:47
    comment: |
      I'm loving coding a fat client UI in JavaScript - and learning to worry less about comms errors; I never change my state unless the call succeeds and just report any failures to the user with no retries or logging. Since all I/O is tied directly to user actions, they are free to retry whatever they did ... it's very relaxing :-)
  - author: Daniel Hardman
    date: 2013-01-11 19:09:02
    comment: |
      Interesting. I hadn't considered the benefits of running inside a robust and well implemented browser &mdash; but you've certainly put your finger on one of them. +1 for not solving problems when you don't have to!
  - author: Don
    date: 2013-01-13 06:42:43
    comment: |
      I call this subject, defensive architecture. Its common to write code within an architecture and design based upon a story working. In architecture I think that there is an opportunity to use "circuit breaker" techniques but I also think there is an opportunity to build in sensors and diagnostics that can run inline or better yet in "white space". 
      Enterprise code should be written with sensors that pass information to another system whose purpose it is to monitor performance, stability and analyze potential failure. This system could also decide on routing the code another way in case of failure. In this case the routing switches would replace circuit breakers and the "service" essentially reroutes around a failure or poorly functioning element......
      Bottom line is that we have lots of sensors in most hardware, few in software ....
      I see this need for monitoring from within code becoming more critical as the use of open source increases and enterprises provision their code inside the likes of AWS. I bet that Netflix would agree with this notion after the holiday fiasco .......
  - author: Daniel Hardman
    date: 2013-01-13 15:05:00
    comment: |
      Don: Your background with hardware gives you a valuable angle on this that those of us who are pure software folks miss. Thanks for chiming in. I agree with your prediction about this becoming more and more important as software gets more complex. In fact, I've been meaning for quite a while to write a post about how living systems (in biology) profit from the ability that all living things share, to react to stimuli. Your observation about sensors points to the same truth.
  - author: LisaAn
    date: 2013-01-13 16:40:32
    comment: |
      I have often found it interesting that over half the code is devoted to checking for error conditions and dealing with errors but we don't often test error conditions but the "golden path" instead. Perhaps the "circuit breaker" would push us to test errors more often.
  - author: Daniel Hardman
    date: 2013-01-13 19:28:59
    comment: |
      One of my favorite job interview questions (for potential dev or QA hires) is to ask someone how they'd test a simple program. Some people stare at me blankly. Some just regurgitate the golden path. The ones I like to hire are the ones that immediately reel off half a dozen ways that they could imagine the code being broken. That kind of thinker is not only better at writing error-resistant code and better at writing comprehensive tests, but is also more creative and fun to work with overall.
  - author: Architects: manage risk like a Vegas bookie &laquo; Codecraft
    date: 2013-02-21 09:31:31
    comment: |
      [...] Is my architecture properly accounting for risk of environmental problems such as DDOS, routing failures, brownouts, and temporary loss of an internal component? (See my article about circuit breakers.) [...]
---
Recently I've been pondering an interesting book called <a href="http://pragprog.com/book/mnee/release-it"><em>Release It!</em>, by Michael Nygard</a>. It's full of anecdotes from someone who has spent a major portion of his career troubleshooting high-profile crashes of some of the most complex production <a class="zem_slink" title="Software system" href="http://en.wikipedia.org/wiki/Software_system" target="_blank" rel="wikipedia">software systems</a> in the world &mdash; airline reservations, financial institutions, leading online retailers, and so forth.

<figure><img src="assets/circuit-breaker.jpg" /><figcaption>A circuit breaker. Image credit: Midjourney</figcaption></figure>

One <a class="zem_slink" title="Design pattern (computer science)" href="good-code-plans-for-problems.md">good code plans for problems</a>.

The pattern is called <strong>circuit breaker</strong>, and its purpose is to prevent runaway failures.

In systems without circuit breakers, failures in an external call may cause an exception on the caller's side; this can cause the caller to log, retry, and/or execute other specialized logic. Since errors are supposed to be the <a class="zem_slink" title="Corner case" href="http://en.wikipedia.org/wiki/Corner_case" target="_blank" rel="wikipedia">corner case</a>, the blocks of code that handle them are often expensive to execute. The very slowness of the error-handling codepath can be the source of further failures, because locks are held longer than normal, or because we poll until a connection is restored, overwhelming a system that's already limping.

Or, to borrow an old idiom, "it never rains but it pours."

In the circuit breaker pattern, on the other hand, the caller assigns each "circuit" (a codepath that invokes an external entity) to one of three possible states: <span style="color:#993366;">closed</span>, <span style="color:#993366;">open</span>, or <span style="color:#993366;">half-open</span>. In the <span style="color:#993366;">closed</span> state, all is copacetic; calls succeed quickly. However, if the caller starts seeing failures or brownouts, and if these failures eventually create enough resistance on the circuit, the circuit's state is considered <span style="color:#993366;">open</span> &mdash; all traffic on the circuit is suspended for a while, allowing backlogs to clear and former equilibrium to return. While in the open state, code that attempts to use the circuit gets an immediate and cheap failure. After enough time has passed, the circuit breaker assumes a <span style="color:#993366;">half-open</span> state, where it is willing to try again to see if things are now better. With success, the circuit transitions back to <span style="color:#993366;">closed</span> (normal); with failure, it reverts to <span style="color:#993366;">open</span> for more waiting.

Nygard's war stories are an excellent argument for building circuit breakers. I see eloquent support in other contexts as well.

Consider biology. Life manages incredible complexity to equilibrium, at both micro and macro scales, in ways that software barely begins to contemplate. In fact, <a class="zem_slink" title="Homeostasis" href="the-8th-characteristic.md">life's 8 key characteristics</a>. I find it interesting that in many cases, life achieves this balance using <a class="zem_slink" title="Feedback" href="http://en.wikipedia.org/wiki/Feedback" target="_blank" rel="wikipedia">feedback loops</a> that temporarily suspend or throttle complex processes in much the same way as the circuit breaker pattern we're discussing here. A cell regulates its internal <a class="zem_slink" title="PH" href="http://en.wikipedia.org/wiki/PH" target="_blank" rel="wikipedia">pH</a> and salinity based on signals exchanged with the external environment; predator populations grow, shrink, and migrate based upon the abundance of prey; our bodies develop hunger when they need energy, and fatigue when they need time to repair.

If biology isn't your thing, what about finances? Remember the cascading failures in the financial system that led to the <a href="http://en.wikipedia.org/wiki/2010_Flash_Crash" target="_blank">"flash crash" of 2010</a>? Remember how <a class="zem_slink" title="Bear Stearns" href="http://en.wikipedia.org/wiki/Bear_Stearns" target="_blank" rel="wikipedia">Bear Stearns</a> and <a class="zem_slink" title="Lehman Brothers" href="http://en.wikipedia.org/wiki/Lehman_Brothers" target="_blank" rel="wikipedia">Lehman Brothers</a> and <a class="zem_slink" title="American International Group" href="http://en.wikipedia.org/wiki/American_International_Group" target="_blank" rel="wikipedia">AIG</a> fell like dominoes before that? The NYSE has instituted <a href="http://en.wikipedia.org/wiki/Trading_curb" target="_blank">trading curbs</a> that temporarily suspend normal activity when danger signals are observed. Smart.

We need software built with this same "expect failure and plan to handle it" mindset.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Next time you are designing an interaction with an external component or subsystem, consider implementing a circuit breaker to make the interaction less fragile and more prone to auto-balancing.</span></em></p>
