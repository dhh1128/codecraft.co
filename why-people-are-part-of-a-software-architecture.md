---
title: Why People Are Part of A Software Architecture
date: 2008-06-25
slug: why-people-are-part-of-a-software-architecture
item_id: CC-080601
tags: [meta, org]
series: "The Architect's Role"
redirect_from:
  - /2008/06/25/why-people-are-part-of-a-software-architecture
comments:
  - author: Workflows, People and Processes
    date: 2014-05-05 03:52:54
    comment: |
      […] almost every process out there (aside from some automated production), humans form an important part. The process is in place because it is solving a human-provided “problem.” In many cases, it is […]
  - author: Workflows, People and Processes
    date: 2014-05-10 13:36:45
    comment: |
      […] almost every process out there (aside from some automated production), humans form an important part. The process is in place because it is solving a human-provided “problem.” In many […]
---
I've been reading an interesting book &mdash; <a href="http://books.google.com/books?id=7nF6nuLC7m4C&printsec=frontcover&dq=beyond+software+architecture&ei=0_CQSNHgHqXKjgGPsO31Dg&sig=ACfU3U0yo_wtkIjvxJKzoz6HE8HS3ZtO_Q" target="luke">Beyond Software Architecture</a>, by <a target="luke" href="http://www.lukehohmann.com/">Luke Hohmann</a>. In his first chapter he discusses the more people- and business-related aspects of architecture, and makes the following points:
<ul>
	<li>Systems are designed to manage people dependencies, not just esoteric "code" dependencies.</li>
	<li>Systems are designed by people with non-technical motivations.</li>
</ul>

Point well taken.

<img align="right" src="http://farm7.staticflickr.com/6101/6230395373_1d7576f8ce_d.jpg" alt="Schrödinger's Cat, from http://www.flickr.com/photos/drlovecherry/" />I wanted to chime in with one additional observation. An architecture and the people who actively develop and maintain it are difficult to separate. I'd argue that a company that owns the source code of a so-called "architecture" but that has no engineer that understands it doesn't really have an architecture &mdash; as with <a href="http://en.wikipedia.org/wiki/Schroedinger%27s_cat">Schrödinger's cat</a>, the human observer matters.

A stark example of this has cropped up several times as I've done M&A work during my career. I have seen less technical executives repeatedly assume that the source code of a system = the system. In other words, they think people are fungible and an architecture can be purchased and transferred *only* by shifting source. In practice, that assumption causes problems. The boundaries around modules don't always exist cleanly in files and directories on disk; sometimes they are more of a mental construct in the minds of those who build and service them. If you grab a wad of source and plop it down in front of people who've never worked with it before, the institutional knowledge that contextualized the system in the minds of its creators is missing. This is why a mediocre engineer well-versed in the context of a given architecture is likely to be more productive than a world-class engineer dropped into the architecture cold. It is also why layoffs and RIFs are more dangerous than you'd guess by simply looking at raw staffing numbers.
