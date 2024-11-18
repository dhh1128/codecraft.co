---
title: Features are not chunks of code
date: 2013-07-25
slug: features-are-not-chunks-of-code
redirect_from:
  - /2013/07/25/features-are-not-chunks-of-code
---

Before the industrial age, "features" were noteworthy aspects of a face or a geography: a patch of color, abundant wrinkles, a scar... The human brain is stunningly good at identifying and comparing such features--perhaps because that ability has been central to our nurture as children, our bonding into family units, and our survival as a species.

<img class="size-full wp-image-6794 aligncenter" src="https://codecraft.co/wp-content/uploads/2013/07/danie-franco-o1pkm7-8ah4-unsplash.jpg" alt="danie-franco-o1PKM7-8AH4-unsplash" width="5731" height="3821" />
<p style="text-align:center;">Photo by <a href="https://unsplash.com/@dani_franco?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Danie Franco</a> on <a href="https://unsplash.com/s/photos/face-wrinkles-scars?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></p>
When we want to say what a face looks like, we describe its features. They are an entrée into experience with it.

At the dawn of the computer age, the advertising and publishing industries were already talking about how products--or aspects of them--could be "featured" in media. Highlighted characteristics were called "features", and this metaphor transferred seamlessly into digital language. Software product managers now traffic in "features" and "feature sets."

We use the term so comfortably that we sometimes forget what it has to teach us.

<!--more-->I have met software pros--brilliant ones!--who think features and coded output are good functional equivalents. They think that if they embody a capability in a function or a class or a command-line switch, and check it in, they've added a feature. And if they undo their checkin, the feature is gone. That's the way they talk about it.

There is a certain truth to this simple view. But it's a dangerous simplification, and the roots of the metaphor tell us why.

<strong>Layers and regions and teamwork</strong>

First of all, no facial feature is simple. A nose has internal structure--bone and cartilage, skin and capillaries and nerves. It has layers and regions. It demands a certain context. Likewise, a software feature is more than code; it includes documentation, an attendant set of upgrade and forward/backward compatibility assumptions, visual and perhaps auditory manifestations, a test matrix, security implications, localization work, perhaps some install tweaks or an API with versioning constraints.

Anybody who tells you they can add a new feature in a "mere <em>X</em> hours" has forgotten this.

I cannot count the number of times I've heard the naive assertion that a feature is done because the ing is complete. I periodically fall into this trap myself. But it remains a lie, no matter how often it's repeated.

In most production codebases, smart coders don't create codebases. <a title="Humility" href="humility.md">Teams do</a>. That takes time and coordination from multiple disciplines.

<strong>Pieces and gestalt</strong>

Secondly, facial features are experienced together, not in isolation. The portion of the face that constitutes an eyebrow is hard to define without speaking of eyes, lids, forehead, and temples. Likewise, any given feature in a software package relies on other features (can't add a command-line switch unless your app already has a CLI), and the presence or absence of a feature alters the whole. This means that adding and subtracting features is not nearly as surgical as we sometimes pretend. If we added a dialog to edit widgets, but the middleware that supports those edits has a fatal flaw, have we really added a feature? Or do we have a nose that's only half-attached to the face behind it? If we subtract a "little" feature but the UX goes from wonderful to abominable, have we done more damage than we realized?

<strong>Tempus fugit</strong>

Thirdly, facial features evolve over time. The DNA code that tells a body how to build a nose gets expressed pretty early in a human's lifetime, and we may be able to distinguish some uniqueness of the code from the outset. Maybe big noses show up early. :-) But that code has only built one version of the nose by babyhood; all the other versions of that same nose are still waiting to manifest in the future.

What this means, in practical terms, is that, even if you can code a feature in <em>X</em> hours, and even if it's a simple feature with unusually minor demands on the rest of a team, its cost is <strong>never</strong> <em>X</em> hours. All features have a carrying cost, which is the ongoing expense of keeping the feature alive and connected to the blood supply on the rest of the face, through all future incarnations. In this sense, features are never "done." Sticking our heads in the sand to avoid this truth is a surefire way to <a title="Paying Off Technical Debt" href="coping-with-organizational-alzheimers.md">sin of omission</a>.

<strong>Three eyes</strong>

A final lesson of the feature metaphor is that it's possible to have too much of a good thing. Two beautiful eyes might lure a mate; three, not so much. <a title="Good Code Is Balanced" href="good-code-is-balanced.md">Balance and proportion matter</a>.

In software, we often make the mistake of adding new features when we ought to be improving the ones we have, or even subtracting a scar here or there.

<strong>Summary</strong>

Features are great. I've spent most of my career building them. They sell product. And coders should be proud when they execute quickly to contribute code for features. But let's be a little more <a title="Lynn Bendixsen: Listen." href="ken-ebert-kill-three-birds.md">value in the overall scheme of things</a>, their ongoing cost, and the commitments they imply.

That'll put more smiles on our faces.



