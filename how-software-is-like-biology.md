---
title: How Software Is Like Biology
date: 2012/08/14
slug: how-software-is-like-biology
---

No, I'm not going to talk about genetic algorithms. (Not yet, anyway.)

<figure><img class=" " title="DNA" src="http://farm1.staticflickr.com/176/439737660_7505789a45_m_d.jpg" alt="" width="151" height="178" /><figcaption>DNA ~ subroutines. Photo credit: dullhunk on Flickr.</figcaption></figure>

Consider the scope of concerns (roughly maps onto need for expertise) of various folks that do biological science for a living. You have organic chemists. They might not know much about why zebra mussel infestation is a problem in the Great Lakes, but they can tell you all kinds of things about why cellular respiration works or how prions replicate. You have cellular biologists, who know all about protein transcription, meiosis, and telomeres. At higher levels of abstraction/generalization, you need experts on tissues, organs, or entire organisms -- and beyond them, you need folks who study speciation, ecosystems, genetic drift in populations...

Same deal with computers. At the lowest level, there are hardware folks who are all about making the chip or the bus efficient. Then there are algorithm specialists who will hone a sort or a data structure till it hums. Their expertise is critical, but not sufficient. You also need folks who are good at building well-encapsulated classes (cell membrane ~ encapsulation; nucleus ~ private methods; abstract factories = ribosomes... interesting...), folks who understand libraries (tissues/organs), folks who can see how each library and class fits into a coherent application (organism). Many analyses of software stop at the application level, but you can keep going: distributed applications clump in "herds"; herds participate in even larger and more complex (eco)systems that suffer from predation, evolution, and all the rest.

Morals to the story?
<ol>
	<li>Just as not all great biological scientists are experts in protein transcription, <a href="puzzle-solving-not-the-driving-function-of-software-construction.md">not all great computer pros are experts at low-level algorithms and data structures</a>.</li>
	<li>Biology has a lot to teach us about building stable systems. There's a reason organisms develop defense mechanisms, excretory capabilities, etc. Apps that evolve without analogs will die. Next time you are solving a tricky computer problem, ask yourself how biology solves the equivalent...</li>
</ol>