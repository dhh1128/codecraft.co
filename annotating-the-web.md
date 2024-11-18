---
title: Annotating the Web
date: 2008-09-05
slug: annotating-the-web
---

Bookmarks just remember a location. That's kind of nifty, but even with all the power of <a target="del" href="http://del.icio.us">del.icio.us</a> or a similar service, it's not something that keeps me awake at night with enthusiasm.

Why don't we move beyond simple bookmarks? Let's let people remember what they were thinking when they read a particular piece of content. Let's figure out a way to annotate web pages so that if you come back to that same page, your annotations show up again.

Annotations could take the form of text (with all the hypertext and multimedia features of html itself), ink (to scribble or draw on top of a page, circle key elements, etc.), audio... Annotations could be a layer on top of a web page -- something you could toggle on or off. You could even share your annotations with someone else so they could turn on your layer or compare yours to theirs.

Imagine this in an educational setting. An instructor wants you to read an essay about existentialism in <cite>Waiting for Godot</cite>. The instructor takes a few minutes to highlight the parts of the essay that she finds particularly interesting -- underlining a couple sentences, jotting a note about a section that's out of sync with her own research, etc. When you read the essay, you can turn on the instructor's criticism of the essay and add your own. Maybe other classmates can share their ideas with you as well.

To make this maximally powerful, you'd want to be able to anchor your comments to particular slices of content on the page. Over time, if the content of the page or the rendering of the page changed, you'd want your annotations to adapt. Example: you disagree with an author who claims that "peptide bonds are a boring subject that any first-year biology student can afford to sleep through." You highlight that sentence on the page, bring up a context menu with a right-click or control-click, and on the menu one of the options is "annotate." You create your annotation much the same way you'd create a bookmark. (You could also anchor annotations to graphics or other elements on the page pretty easily.)

You visit the same page 3 weeks later. The .css behind the page is different now, and the content has been extended (e.g., it's a blog and a dozen people have commented). And you're using a different browser, on a different OS, possibly in high contrast / large font mode where you were in normal mode before. The point is, visually the page looks completely different. But the annotation engine searches for the anchor text for your annotation, finds it, and basically offers a tooltip to pop your annotation at the correct location on the page.

(By the way, the annotation mechanism I'm describing here might be a more interesting way to accumulate blog comments than the current way which is email thread-like. Instead of reproducing the salient portion of an earlier thread contributor's text in your own, and then adding your words after, just anchor your annotation to the relevant portion of existing content...)

Lastly, imagine what we could do if we allowed a user to enumerate all their annotations. Annotations could be organized by key word of the page they apply to (and, to make them even more findable, by key word in their anchor text). A simple query to the annotation back end server would give you a sort of personal knowlege base on any subject.

<b>Update</b>: I went out and did a little research and found that some of the features I'm dreaming of already exist. If you're interested, check out <a target="wikipedia" href="http://en.wikipedia.org/wiki/Web_annotation">this article</a> on wikipedia.