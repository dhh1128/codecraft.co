---
title: Why Your Software Should Cry
date: 2013-05-06
slug: why-your-software-should-cry
redirect_from:
  - /2013/05/06/why-your-software-should-cry
comments:
  - author: dougbert
    date: 2013-05-06 12:53:08
    comment: |
      great thoughts
  - author: Gene Hughson
    date: 2013-05-06 19:17:17
    comment: |
      very interesting...I think the increasing interest in resilience is a sign of growing industry maturity.
  - author: François Reynald
    date: 2013-05-07 02:15:19
    comment: |
      What you describes already exists in Apple's UIKit framework. ViewControllers get notified by the system of low memory situations. It's the developer's responsibility to implement the didReceiveMemoryWarning method. I have copied the relevant excerpt from the class reference page below.
      
      didReceiveMemoryWarning
      Sent to the view controller when the app receives a memory warning.
      
      - (void)didReceiveMemoryWarning
      Discussion
      Your app never calls this method directly. Instead, this method is called when the system determines that the amount of available memory is low.
      
      You can override this method to release any additional memory used by your view controller. If you do, your implementation of this method must call the super implementation at some point.
  - author: Daniel Hardman
    date: 2013-05-07 07:24:08
    comment: |
      François: Thanks for the information. I was not aware of this feature in UIKit. I'm glad Apple has added it. Do they also have a way to be notified about low disk space, or is that not considered an issue in iOS?
      
      Resource exhaustion is only one of many possible situations where software needs sensors. Another obvious one is connectivity problems; those plague software all the time and are poorly diagnosed and handled in most software that I've seen. There are many other sources of "pain" as well.
  - author: Daniel Hardman
    date: 2013-05-07 07:24:52
    comment: |
      Yes, I think the industry is gradually starting to "get it." I'm just impatiently trying to hurry us along. :-)
  - author: François Reynald
    date: 2013-05-07 07:46:59
    comment: |
      Daniel: That is the only notification I know of but I am not (yet) an UIKit expert. It may be because memory is such a big deal for mobile devices.
  - author: RalfMC
    date: 2013-05-24 14:39:07
    comment: |
      This is an interesting line of thought. Personally, I would generalize to conditioning pretty fast, as pain is 'just' a kind of reinforcement. Maybe take a look at classical and operant conditioning.
      
      Coincidentally, Bayesian statistics seem like a related subject and have indeed found their way into spam filters, for instance ("hey, this message smells like a rotten apple").
      
      I think one important thing to remember is that life is driven by heuristics, averages, etc. Stuff works 'most of the time' and 'in general'; however, by the time my programming gives me 95% reliable software, I will not have gained much.
  - author: Daniel Hardman
    date: 2013-05-24 15:41:25
    comment: |
      Nice connection to Bayesian statistics. I used to work on search, and hit ranking uses Bayesian models (in a subset of search products); I should have seen that link more quickly. Very good point to ponder.
      
      Totally agree about life being driven by heuristics.
      
      Thanks for the comment!
---
The problem of pain has bothered philosophers &mdash; particularly those with a religious bent &mdash; for a long time. What might be the purpose of suffering, they've wondered, and how does it relate to the human experience?

But pain barely impinges on the thinking of software engineers at all. Computers never wince, or complain, or mourn the loss of a favorite program (Marvin the paranoid android excepted). An OS runs at full speed until the instant when its kernel "panics" without warning; once you reboot, it acts as if nothing ever happened. No sniffles, no whimpers, no scabs...

<figure><img alt="" src="http://farm3.staticflickr.com/2717/4480361923_229a1eb003.jpg" width="500" height="333" /><figcaption>photo credit: nanny snowflake (Flickr)</figcaption></figure>

This is unfortunate.

Reaction to stimuli is one of the <a title="The 8th Characteristic" href="the-8th-characteristic.md">8 characteristics of life</a>. That means that living things are aware, in some sense, of their relationship to the larger environment. They distinguish between good and bad stimuli. They hurt. And they learn from their pain.

<strong>Lessons from a protist</strong>

This ability to use pain is not limited to complex organisms. The lowly <em>Stentor roeselii</em> (a single-celled protozoan that anchors for filter feeding) exhibits an incredible repertoire of behaviors to optimize its relationship with the environment. Squirt it with water from a pipette, and it contracts for defense. 30 seconds later, it unfurls again. Keep squirting, and it eventually learns to ignore the false alarms.

Gently introduce a poison into the water current, and <em>Stentor roeselii</em> will do nothing at first. However, after a short time it senses that something is "wrong," and bends itself out of the path of the noxious particles. If that doesn't work, the cell begins contracting cilia in a sequence that ejects the undesirable particles. This strategy may be combined with bending one way or another.

If that still doesn't achieve the necessary effect, this cell will contract into a protective sheath and stop feeding altogether. It will stay cocooned for a while, then cautiously extend feelers to see if the poison is gone. Repeated encounters with the poison will cause faster and faster triggers of the sheathing reaction, until, finally, the reaction is violent enough that the foot attachment breaks, and the protozoa swims away, looking for a better home (see <em>Wetware: a Computer in Every Living Cell</em>, by Dennis Bray, p. 14-17). This is a single cell, folks, less than a milimeter in size &mdash; a blob of protoplasm and proteins in a semi-permeable membrane!

<figure><img src="http://upload.wikimedia.org/wikipedia/commons/5/5a/Stentor_roeseli_composite_image.jpg" width="461" height="287" /><figcaption>Stentor roeseli. photo credit: Protist Image Database (Wikimedia Commons)</figcaption></figure>

I believe that pain &mdash; and, more generally, optimized reactions to stimuli &mdash; is one reason why life is capable of organizing into complex ecosystems that put our most sophisticated software constructions to shame. Make zebras careless of crocodile bites, and half the herd will die when they migrate across an African river. Make ants insensitive to heat and moisture, and they'll build a hill where the whole colony will bake or drown. Subtract neurological feedback from humans, and you get the disfiguring of leprosy—spreading freely, since nobody feels a need for quarantine.

Life values pain.

Not all software needs neurology, I suppose. Prions and viruses are important players in the game of life, and they're hardly more than mindless algorithms; in software, it's remarkable how much we can accomplish in a good script with a few lines of code. However, if we want to truly <a title="6 Strategies to Simplify Software" href="the-power-of-simplicity.md">growth of complexity</a> in the universe of bits and bytes, we need pain. And we need to pay attention to it.

<strong>Modest beginnings</strong>

I see isolated, simplistic examples that give me hope.

Fail2Ban is a nifty little utility that monitors logs of sshd, httpd, and similar daemo and instructs the firewall to block connections from IP addresses that have been guilty of repeated, failed login attempts. Kind of sounds like <em>Stentor roeselii</em> bending away from the poison, doesn't it?

The <a title="Don’t forget the circuit breakers" href="dont-forget-the-circuit-breakers.md">circuit breaker pattern</a> that I described a while back is another example of reacting to stimuli.

<a href="http://techtripper.com/fijibot-is-an-autonomous-solar-powered-robot-that-lives-by-finding-light-on-its-own/" target="_blank">Fijibot</a> is a colittle machine that fights hunger pains by parking itself in the light to recharge batteries.

Unfortunately, examples like this are few and far between. It's hard enough to <a title="Good Code Plans for Problems" href="good-code-plans-for-problems.md">bake a rational error-handling strategy into software</a>, let alone make it sophisticated enough to monitor its environment and take proactive steps to avoid problems.

<strong>Thought experiment</strong>

What would be different if software had pain receptors?

Let's take a simple problem that all software ought to handle: resource exhaustion. I wager that all of us have written routines that call malloc, or that write files to disk. Most of us probably have at least one scar from a time that the software failed miserably when RAM or disk space was unavailable. Perhaps that experience taught us to check the return value of malloc, or to trap I/O exceptions more carefully. But if that's where our vision stops, the lowly protist is still way out of our league.

What if we wrote our software so that it grew increasingly "uncomfortable" as RAM became more and more scarce? Maybe under ideal conditions, malloc returns immediately, with no pain. In a semi-constrained system, malloc returns after a modest pause, because it incurs the extra overhead of some quick garbage collecting, AND it also signals a central sensor in its app that memory is becoming a problem. <em>Ouch!</em> In a highly constrained environment, a pain-savvy malloc might do a very aggressive garbage collection, plus issue an urgent interrupt, possibly beyond the boundary of a single app, to make sure that it gets someone's attention.

What if programs could jostle one another, or "fight" (inflict pain) in a battle for scarce resources?

I've seen designs that pre-allocate a 1 GB disk file so they can have something that's guaranteed to be deleteable, as a failsafe, if disk space gets too low. This is a step in the right direction, but if they don't also propagate a pain signal, they're not taking the idea far enough.

What are some other ways that software might use pain to its advantage?
<ul>
	<li>Since all software dies, pain might be an indicator of old age (impending EOL, breakages in compatibility, etc).</li>
	<li>In the context of security, software might notice when it's under attack, and take protective measures (Fail2Ban's strategy, replicated in a hundred other contexts).</l
	<li>We might introduce "error memory" into our software. One thrown exception, once in a blue moon, might be something we just log &mdash; but if we start seeing it happen many times in rapid succession, we might treat it as a different problem entirely. This is the analog to humans telling the difference between a slight itch and a blister from our hand in the fire.</li>
	<li>Similarly, we might aim for an "error gestalt" &mdash; the ability to <a title="Metrics, Plumb Lines, and System Thinking" href="measurements-plumb-lines-and-system-thinking.md">notice system-level phenomena</a> as the aggregate of many isolated signals. This would be analogous to a doctor diagnosing flue from the combination of sore throat, fever, chills, headache, and extreme fatigue.</li>
	<li>Could software develop protective "fear" based on repeated exposure to "pain"?</li>
</ul>
I was writing recently about <a title="My First Tangle With the Tower of Babel" href="my-first-tangle-with-the-tower-of-babel.md">my adventures designing a programming language</a>. I concluded that more sugary syntax isn't really a great value to the community &mdash; but a language that allows programmers to reason about, describe, and react to various kinds of pain might do wonders for the health of the ecosystems we build.

<span style="color:#000080;">What do you think? Please drop me a line</span> in the comments or through the "Contact" tab at the top. Include your ideas about pain and software, and maybe (with your permission) I can refer to them in my upcoming book about what software has to learn from living systems.
