---
title: A grumble about buckets
date: 2015-04-08
slug: a-grumble-about-buckets
redirect_from:
  - /2015/04/08/a-grumble-about-buckets
comments:
  - author: Sean
    date: 2015-04-08 16:07:46
    comment: |
      I agree with all the principles you have mentioned: gather customer feedback, keep interactions simple, you can't please everyone, etc. I also recognize that your posts, Daniel, usually describe lofty, but worthy ideals. We should always strive to be better and do better, but perhaps it's my role as a project manager that has me scratching my head over how to handle the trade-offs that often exists between the ideal and what is good enough. I'm not talking about ethical trade-offs but rather those trade-offs between two good things when you are only staffed for one.
      
      Whether you blame the financial institution or the third-party software integration package that your financial institution probably used, my question is this: aren't those security questions good enough? How many users honestly don't have a good answer for any of those "bucket" questions? In the case of Netflix, put yourself in the Product Manager's shoes: even if you had the feedback that the buckets are too general, would you feel a greater urgency to fix that or address streaming issues that are impacting most customers?
      
      As a consumer, does imagining a better user experience diminish the value you are already getting from Netflix (you are still a customer, right)?
      
      Forgive the devil's advocacy - I'm not at all opposed to encouraging developers and designers to keep these problems in mind, which I believe is the intent of this article. Design is probably one of the easiest stages of development to address and resolve such concerns.
      
      Perhaps I'm barking up the wrong tree. Maybe I'm speaking to Louis CK's hilarious exchange with Conan O'Brien about "everything is amazing and nobody's happy" (https://www.youtube.com/watch?v=uEY58fiSK8E). Perhaps I get a little too defensive of software development teams who, in my experience, are usually making sincere efforts to identify and meet user needs (ofttimes before users even know they "need" it), whilst navigating a constantly changing landscape of business pressures and deadlines, software platforms and technologies, federal and state laws and regulations, industry standards and best practices, etc., etc., etc.
      
      In summary, I totally agree that businesses should be doing everything they can to provide users with great value and great experiences - and I believe businesses that listen to customers and find ways to quickly turn customer requests into customer value do very well. All I'm asking is that we as consumers (especially those of us who understand a lot about software development) cut our service providers a little slack when they are clearly trying to provide you with a secure login experience while at the same time giving you a variety of financial services that let you manage your finances from the comfort of your own office chair (or mobile device).
      
      
      
      P.S. - A tip for security questions: I've discovered that you don't have to have a pet to imagine one up. My "imaginary" first car and pet are actually quite more memorable than some of the other questions because I picked wild answers that are funny / memorable to me. I just make sure to use that same pet for every site that asks the question. Plus I have the added bonus that no one will ever be able to discover my answers because they never actually existed! I'll bet your first car was really a Ferrari, wasn't it? ;)
  - author: Daniel Hardman
    date: 2015-04-08 16:31:45
    comment: |
      Sean! How wonderful to hear from you. Very thought-provoking comment.
      
      Yes, it is true that dev teams usually do their darndest (or want to) to anticipate customer needs and make things easy. As I said, I'm more irked at companies that make it impossible to get feedback to such folks, and less irked with initial mistakes. You're so right &mdash; dev teams are usually overcommitted and doing the best they can. But sometimes, I just can't help crying "shame!" on companies for not letting them do better. And I don't think it's a bad thing for developers to exhibit a little "divine discontent" with their customer-aiding constraints.
      
      I'm not a Netflix customer anymore. The parental control issue is one of the reasons why I left. It really is a poor fit for my needs, and I suspect many other parents would say something similar. There is noise about it on public forums &mdash; but unfortunately, deafening silence on the topic from Netflix. I grant you that if I were a PM at Netflix, I would probably vote to fix service interruptions before working the parental control problem. But I seriously doubt that a whitelist feature would be that hard to implement. I'm not letting 'em off *that* easy... :-)
      
      I love your tip about first cars. You may have freed my alter ego in ways I'm only beginning to imagine. :-)
---
Sometimes developers limit the choices that are offered to their users as a <a title="6 Strategies to Simplify Software" href="6-strategies-to-simplify-software">way to simplify</a>. This can be a good thing; I’m a big fan of <a href="the-power-of-simplicity">simplicity</a>.

However, this strategy comes with an important caveat:
<div style="margin-left:2em;margin-right:2em;border:solid 1px black;font-size:105%;font-weight:bold;font-style:italic;text-align:center;background-color:#f0f0f0;padding:1em;margin-bottom:1.5em;">If you're going to force all choices into a few predefined buckets, you better provide buckets that <a href="why-mental-models-matter">match the needs</a> of your <a href="why-people-are-part-of-a-software-architecture" title="Why People Are Part of A Software Architecture">users</a>.</div>
Broken buckets will not earn you brownie points. Or revenue.

<figure><img src="assets/broken-bucket.jpg" alt="" width="640" height="480" /><figcaption>image credit: Midjourney</figcaption></figure>

Today I was adjusting my 401k contribution. Here's the broken buckets I saw when I logged in to the financial services website:

<img src="assets/security-questions.png" alt="security questions" />

See, here's the problem. I have 3 favorite restaurants ("<em>what's your favorite ___?</em>" security questions are <em>all</em> useless to me), I'm not a pet person, I don't remember what kind of car I first drove, I lived in 20 different places by the time I was 18, I didn't have just one best friend in high school, and I don't have a security keyword that I reuse.

None of these buckets works. But I had to choose one, and I couldn't log in to the web site (even to send a note about my dissatisfaction to customer service) until I did.

I have a similar beef about parental controls on Netflix. Last time I checked, there was a slider that gave you 3 positions: no controls, "older teen", and "kid". So what if I've got a teen who's not interested in <em>Sesame Street</em> and <em>My Little Pony</em>, but who has childhood trauma as an orphan in a third-world country, and who thus needs to not be offered certain movies in the "older teen" category? What if I'm sick of the promo images for raunchy R-rated movies, but I want to watch an occasional PG-13 thriller? What if I want to watch a show which is unrated (and therefore available only the most wide-open adult setting), but I can't risk leaving Netflix in wide-open mode all the time (since a kid profile can switch to its parent profile without a password)? I could solve this bucket problem if Netflix gave me a whitelist and/or blacklist feature &mdash; but apparently the all-wise, childless 20-somethings who wrote the parental control features at Netflix thought three buckets was plenty. What could <a href="lynn-bendixsen-listen" title="Lynn Bendixsen: Listen." target="_blank">listening</a> teach them?

<h3>The true sin</h3>

I'm grumbling about my choice of buckets, but in the end, it's not the bucket menu, in and of itself, that bugs me. Like I said above, I get why developers might need to simplify. You <a href="flexibility-is-no-virtue" title="Flexibility is No Virtue" target="_blank">can't please everyone</a>.

No. What <em>really</em> bugs me is that software with poorly chosen buckets also tends to be software that &mdash; either by <a href="users-arent-the-only-people-in-your-software" title="Users Aren’t The Only People In Your Software">humans they serve</a>. And I dare you to find any way for a Netflix customer to contact the dev team or product manager that owns parental controls. I tried and failed.

Seth Godin recently blogged about how <a href="http://sethgodin.typepad.com/seths_blog/2015/03/what-is-customer-service-for.html" target="_blank">different corporate cultures approach customer interactions differently</a> &mdash; and why that makes a world of difference. He was nice and non-controversial; he didn't take a strong position on whether certain approaches are unethical.

I'm going to be less diplomatic. As the <a href="http://trevharmon.com/standard-of-business/">Conscious Business Ethics Manifesto</a> says, we have a duty to provide real value to those who pay us for our goods and services&mdash;not merely to provide a glitzy facade. If we’re going to force users into buckets, let’s give some <a href="role-play-centered-design">careful thought to the buckets we offer</a>&mdash;and let’s make sure we have a way of discovering and <a href="bridging-the-lacuna-humana" title="Thoughts On Bridging the “Lacuna Humana”">tracking</a> whether our buckets are useful.
