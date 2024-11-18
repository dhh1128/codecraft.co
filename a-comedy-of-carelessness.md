---
title: A Comedy of Carelessness
date: 2013/12/09
slug: a-comedy-of-carelessness
---

<h2>Act I</h2>
The day after Thanksgiving I went on a long road trip to eastern Wyoming. Total driving time: about 7 hours, each way.

At a gas station about 2 hours from home, on the way back, my credit card was declined. Apparently, fraud prevention algorithms at my credit card company had decided that it was suspicious for me to use my credit card out of state. This was rather irritating, since I'd just driven 12 hours on this same highway, using this same credit card to fill up the car, out of state, 2 other times in the previous 24 hours.

<figure><img alt="" src="http://farm3.staticflickr.com/2002/2069439389_37db50cb39.jpg" width="500" height="375" /><figcaption>Photo credit: herzogbr (Flickr)</figcaption></figure>

I used an alternate card and finished my trip. When I got home, I called American Express to get the card unblocked. (The block didn't just apply to gas stations in Wyoming--once suspicious, the company wouldn't let me buy gas a block from my house, either.) I spent 5-10 minutes working my way through an automated phone queue. It asked for several pieces of info to prove I was, indeed, the card holder--all 16 digits of the card, the 3-digit code on the back, last 4 digits of my social security number, phenotype of my dog... I had to call back twice--once because a family member asked me a question while I was fishing my card out of the wallet, and the system lost patience waiting for a response, and once because I pushed the wrong key and had no way to backspace.

Finally, on my third attempt, I got to the concluding challenge in this interview with mindless software: "Enter the first four letters of your place of birth."

I was flummoxed. Of course I know where I was born, but which place did they want? I didn't know whether this question was soliciting a city name, a state name, a hospital name... I hesitated. I guessed that city name was most likely to be the answer I'd provided to this security question in the past, but I can think of one or two accounts where hospital or state is what's wanted.

While I was biting my lip, the system rejected my answer, and I was back to square one. I called in again and remained silent until I got routed to a live operator. She unblocked the card and offered to give me a link to an app that I could download, to make it convenient for me to unblock my card whenever this happens in the future.

Well, sorry, American Express--despite your cheerful customer service representative, you did not make a happy customer with this experience. If you're going to challenge me when I go out of state, <!--more-->don't do it at the end of a journey, when I'm up a creek without a paddle and all the potential fraud has already happened. Don't make me wade through an automated phone queue that's inflexible and hard to use, with no option to talk to a human. Don't write a stupid security question that's ambiguous. And don't make me download an app to correct your mistakes after the fact. Just give me an email address or text-capable phone number where I can tell you I'm headed on a trip. Or ask me a challenge question at the pump; you asked me my zip code when I swiped the card, so entering the digits of my street address wouldn't be much of a stretch...
<h2>Act II</h2>
I needed to register an LLC, so I went to the state's web site, found the tax commission portal, and began the workflow. It requires a login. I'd done this before, so I was pretty sure I'd created a login already, but I had no idea what it was. I went through password recovery, entered the email address that I thought I'd registered, and was promised by the system that it had emailed instructions to choose a new password.

Then I waited.

No email came. Spam folder empty.

<a href="../../../wp-content/uploads/2013/12/screen-shot-2013-12-07-at-4-31-19-pm.png"><img class="size-full wp-image-2096 alignright" alt="Best of the Web award for utah.gov" src="http://codecraft.co/wp-content/uploads/2013/12/screen-shot-2013-12-07-at-4-31-19-pm.png" width="317" height="157" /></a> Sigh. Gritted teeth. I guess the system lied about sending an email, and I had never registered that email address. (Security nazis: don't tell me the system needed to lie to prevent account discovery by nefarious hackers. The system could have said, "If you've given us an email address that we recognize, we've sent a message." That wouldn't be lying, and it also wouldn't disclose info about whether a particular user exists.)

I started over, creating a new login. On the "Create Account" screen, I noticed that the site was proud of awards it had won. Hmm.

<span style="line-height:1.5em;">I entered my name, address, phone number, and desired password. The system pre-screened my password (gotta force dumb users to pick something robust!) and made sure I typed it the same way twice, then allowed me to press Submit.</span>

Whoop! Sorry, Charlie. Your phone number wasn't formatted correctly. You entered 123 456 7890, but we needed (123) 456-7890. Please try again. And oh by the way, we've erased both password fields and the phone number you provided, since you didn't format your input correctly.

<span style="line-height:1.5em;">I eventually got everything just right, and "Submit" displayed an icon to show me the gears were turning. Then it took me to a screen that said this:</span>
<p style="text-align:center;"><a href="../../../wp-content/uploads/2013/12/screen-shot-2013-12-07-at-4-31-40-pm.png"><img class="size-large wp-image-2097 aligncenter" alt="Screen Shot 2013-12-07 at 4.31.40 PM" src="http://codecraft.co/wp-content/uploads/2013/12/screen-shot-2013-12-07-at-4-31-40-pm.png?w=500" width="500" height="77" /></a></p>
You're sorry for the inconvenience? Hmm. I betcha you're not as sorry as I am. If the site is down for scheduled maintenance, then why not tell me before I started that I was about to be interrupted? And why not tell me when the scheduled maintenance window ends, so I know when to check back?

I came back half an hour later. The site appeared to be up. I tried to enter my new login. I accidentally entered my email address instead of my username in the login field; I got two errors before I figured that one out. Once I logged in, I got to step 1 of the "Register an LLC" process before I saw the "Temporarily Unavailable" message again.
<h2>Act III</h2>
My phone's battery was completely dead, so I hooked it up to the charger. I really needed to make a phone call, so I tried to turn it on once charging had begun. I had to hold down the power for 15 seconds or so before it reacted (why?). I saw the Android logo, waited till the phone completed its boot sequence, and lifted the phone to my ear.

Unfortunately, the act of moving the phone jiggled the plug enough to interrupt power for a split second, which triggered the phone's uninterruptible 30-second shutdown sequence.

Why does it make sense to do a 30-second shutdown sequence if the battery's totally dead? Certainly it's not to preserve the battery. To save state, maybe? My user session had lasted all of 1 or 2 seconds; there was no state to preserve. Wouldn't it be smarter to try to wait out a brief power loss, if you have nothing to lose?
<h2><span style="line-height:1.5em;">Critical Analysis</span></h2>
You can probably tell that I'm frustrated. Of course life isn't going to be smooth sailing all the time, and of course each of these lousy experiences arises from complex situations where engineers and business people had to make tradeoffs. Perhaps developing a smarter fraud detection algorithm at AmEx is too expensive. Perhaps a government website's first priority is protecting privacy and not losing data, and creating user accounts is a less frequent process that they haven't had time to polish yet. Perhaps Android phones would rather force orderly shutdown than risk OS corruption.

My beef is not that we make tradeoffs--it's that we don't regret them enough, communicate them enough, acknowledge enough the bad that comes with the good. And we pass the buck, way too often. The lowly "user" at the bottom of the food chain has a pretty lousy experience.
<h2>A Higher Vision</h2>
While I was writing this post, my internet connection kept dropping due to a snow storm. Look what I saw at the top of Wordpress's edit window:
<p style="text-align:center;"><a href="../../../wp-content/uploads/2013/12/screen-shot-2013-12-07-at-4-16-32-pm.png"><img class="size-large wp-image-2095 aligncenter" alt="Screen Shot 2013-12-07 at 4.16.32 PM" src="http://codecraft.co/wp-content/uploads/2013/12/screen-shot-2013-12-07-at-4-16-32-pm.png?w=500" width="500" height="34" /></a></p>
Now that's more like it! <a title="Good Code Plans for Problems" href="dont-forget-the-circuit-breakers.md">Take steps to cope</a>, without panicking or inconveniencing the user. I'm not super happy that my internet connection's been flaky, but Wordpress has a reasonably cheerful "net promoter" right now.

We MUST have a vision that encompasses this mindset in the software we build, because I believe software is getting ever more complex. Layer depends upon layer depends upon layer... If we write each layer using only the most convenient assumptions, the multiplicative effect of all those shortcuts will eventually make our users miserable.

I don't want to use software like that, and I don't want to write software like that, either.

---

Jared (2013-12-14 21:48:38)

Ambiguous challenge questions is a pet peeve of mine.  "What is the name of your elementary school?"  Forget that I don't know if I would have put "Lincoln Elementary" or "lincoln", I can't be the only one who attended multiple elementary schools.  The school where my children attend has something like a 10% turnover PER YEAR.  First pet?  My older siblings talk about dogs I barely remember, would I have put one of those names, or the one I remember clearest?  

I laughed the other day when I was prompted at a new site with a question I had never seen before: What is the name of the girl you first kissed?  Now that I remember!

I am currently doing a lot of work with a very poorly-designed component of my company's software.  I can understand that a complex function call takes longer in the real world than in the dev lab, but why do I stare at a status bar that reads "Ready" while the function runs for hours without feedback except what is see in debugview? Is it still running?  Did I type something wrong?  Was my mouse click lost over the RDP connection?  I don'e expect perfection, but feedback is necessary.

---

Embedded Link Roundup | UpEndian (2014-03-08 08:01:46)

[…] A Comedy of Carelessness (Codecraft) […]

---

trevharmon (2013-12-09 09:58:06)

I think one of the most egregious examples I've recently run into was the hoops necessary to jump through to buy rail tickets online for India. Now the IRCTC (Indian Railway Catering and Tourism Corporation Limited irctc.co.in) is arguably one of the largest ticketing/booking systems in the entire world, and is by far the easiest method for booking train tickets (unless you happen to live in a country that has an IndRail pass agency, of which the U.S. is not).

Here's the issue.

In order to create an account you're required to provide a never-before-used +91 Indian cell phone number. This is clearly problematic for foreigners. The workaround (http://www.seat61.com/India.htm#book%20-%20from%20outside) is to provide a fake (i.e., valid, but not yours) cell number and then contact support to get the all important SMS security code that you didn't get (but someone else might have gotten) sent to the provided cell number.

This is obviously problematic on so many different levels.

On a slightly different note, the other night I helped my father set up his new iPad, which necessitated the creation of a new Apple ID. That process wasn't perfect, but when we got to the security question/answer creation part, the questions provided by Apple were completely unambiguous at to what was being asked for. For example, "What was the last name of your favorite teacher in elementary school?" Every possible ambiguous section was preceded by a needed descriptor.

So, I think we are slowly getting better.

---

Daniel Hardman (2013-12-09 13:25:25)

Yes, when we ask crisper questions (your Apple example), we definitely improve the user experience.

Your story about railway tickets in India reminds me of a great short story by Stanislaw Lem, called "Trurl's Prescription." It's about a society that has an intrusive beast settle on their planet. They can't get rid of it. They try everything up to and including nuclear bombs, and it seems impervious to influence. So they hire Trurl (a great inventor). He immediately serves a writ of dense legalese on the creature, requiring a notarized signature in triplicate. Things get progressively sillier from there, until eventually the creature vanishes. Trurl's parting observation is that when all else fails, you can always use bureaucracy--no way has ever been found out of its insidious clutches. :-)

---

lkafle (2013-12-10 02:19:36)

Reblogged this on <a href="a-comedy-of-carelessness.md" rel="nofollow">healthcare software solutions lava kafle kathmandu nepal lava prasad kafle lava kafle on google+ <a href="https://plus.google.com/102726194262702292606" rel="publisher">Google+</a></a>.

---

doug thompson (2013-12-10 13:23:06)

SOOOOOOO BTDT!!!!!!!!!!!!!!!!
(been there done that)

Was in Las Vegas at a CNG refueling station. System was so old, I had to swipe 3 times, each taking about 1 cent of fuel.

THEN I get the phone call about suspicous activity and was it I. I had used the card all the way down I-15 in Utah, but once outside the state I got flagged.

Same issues on the other acts, BTDT.
Very frustrating.
Yet the charges that came from Paris France, still went through and I noticed them on my montly statement....Go figure


Later found a better station near the airport.

---

Daniel Hardman (2013-12-10 17:09:26)

I had to laugh (groan) a bit about your triple-swipe example. I've bought stuff at Wal-mart, realized I forgot something, and circled back through checkout 3 minutes later enough times--and triggered a fraud alert enough times--to recognize that scenario all too well. I now work around it without even thinking, by using an alternate card the second time through. Ugh. We shouldn't have to think this hard to do something simple...

---

Error Handling &#8211; No News is Really Bad News | Form Follows Function (2013-12-11 11:56:30)

[…] the other cases. This is not only a matter of technical professionalism, but also a business issue. End users are likely to be annoyed if our applications leave them stranded out of town or jumping through […]

---

Add some more extra redundancy again | Codecraft (2014-01-15 08:39:33)

[…] code aren’t an afterthought. Even if they’re less likely on average, the chances that their behavior will be important to our users sooner or later are virtually 100%. We need circuit breakers, helpful error messages, documentation about what to do when things […]

---

Error Handling &#8211; No News is Really Bad News | IasaGlobal (2015-03-18 14:09:13)

[…] the other cases. This is not only a matter of technical professionalism, but also a business issue. End users are likely to be annoyed if our applications leave them stranded out of town or jumping through […]

---

A grumble about buckets | Codecraft (2015-04-08 13:39:39)

[…] bugs me is that software with poorly chosen buckets also tends to be software that–either by carelessness or intent–provides no way whatsoever for its creators to find out if they’ve got the […]

---

Error Handling &#8211; No News is Really Bad News | Iasa Global (2014-08-20 12:25:12)

[…] the other cases. This is not only a matter of technical professionalism, but also a business issue. End users are likely to be annoyed if our applications leave them stranded out of town or jumping through […]