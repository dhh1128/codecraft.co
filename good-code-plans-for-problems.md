---
title: Good Code Plans for Problems
date: 2012-09-03
slug: good-code-plans-for-problems
redirect_from:
  - /2012/09/03/good-code-plans-for-problems
comments:
  - author: How to turn coding standards into epic fails &#8212; or not &laquo; Codecraft
    date: 2012-09-27 02:04:55
    comment: |
      [...] follow the codebase’s error and exception strategy. (Example: “In C++, use RAII to guarantee exception safety. Make sure all errors are [...]
  - author: Why Exceptions Aren&#8217;t Enough &laquo; Codecraft
    date: 2012-10-09 23:14:34
    comment: |
      [...] (This post is a logical sequel to my earlier musings about having a coherent strategy to handle problems.) [...]
  - author: Don&#8217;t forget the circuit breakers &laquo; Codecraft
    date: 2013-01-11 18:01:57
    comment: |
      [...] One design pattern that Nygard recommends was new to me, but it rang true as soon as I saw its description. Like many classic patterns, I’ve implemented variations on it without knowing the terminology. I like Nygard’s formulation, so I thought I’d summarize it here; as I’ve said before, good code plans for problems. [...]
---
<p style="text-align:right;"><em>(Another post in my "<a title="What Is “Good Code”?" href="what-is-good-code.md">What is 'Good Code'?</a>" series...)</em></p>
What should you do when software doesn't work the way you expect?

[caption id="attachment_360" align="aligncenter" width="500"]<a href="president-bush-fail.md"><img class="size-full wp-image-360" title="bush-fail" src="http://codecraft.co/wp-content/uploads/2012/09/bush-fail.jpg" alt="" width="500" height="458" /></a> Surprising behavior. Photo credit: epicfail.com.[/caption]

You have to have a plan. The plan could bring one (or several) of the following strategies to bear:
<ul>
	<li>Reject bad input as early as possible using preconditions.</li>
	<li>Get garbage in, put garbage out.</li>
	<li>Throw an exception and make it someone else's problem.</li>
	<li>Return a meaningful error.</li>
	<li>Log the problem.</li>
</ul>
These choices are not equally good, IMO, and there are times when each is more or less appropriate. Perhaps I'll blog about that in another post...

Regardless of which strategy or strategies you pick, the overriding rule is: <strong>develop, announce, and execute a specific plan for handling problems.</strong>

This rule applies at all levels of code &mdash; low-level algorithms, modules, applications, entire software ecosystems (see <a title="How Software Is Like Biology" href="how-software-is-like-biology.md">my post about how software is like biology</a>). The plan can be (perhaps should be) different in different places. But just as the actions of dozens of squads or platoons might need to be coordinated to take a hill, the individual choices you make about micro problem-handling should contribute to a cohesive whole at the macro level.

Notice that I've talked about "problems," not "exceptions" or "errors." Problems certainly include exceptions or errors, but using either of those narrower terms tends to confine your thinking. Exceptions are a nifty mechanism, but they don't propagate across process boundaries (at least, not without some careful planning). Sometimes a glut of warnings is a serious problem, even if no individual event rises to the level of an "error."
<p style="padding-left:30px;text-align:center;"><span style="color:#000080;"><strong>Action Item</strong></span></p>
<p style="padding-left:30px;"><span style="color:#000080;"><em>Evaluate the plan(s) for problem-handling in one corner of your code. Is the plan explicit and understood by all users and maintainers? Is it implemented consistently? Is it tested? Pick one thing you can do to improve the plan.</em></span></p>
