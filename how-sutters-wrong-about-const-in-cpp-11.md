---
title: How Sutter's Wrong About const in C++ 11
date: 2013/01/02
slug: how-sutters-wrong-about-const-in-cpp-11
---

Herb Sutter <a href="http://channel9.msdn.com/posts/C-and-Beyond-2012-Herb-Sutter-You-dont-know-blank-and-blank">recently gave a talk</a> about how the <code>const</code> keyword and the <code>mutable</code> keyword have subtle but profoundly different semantics in C++ 11. In a nutshell, he says that C++ 11 corrects the wishy-washy definition of <code>const</code> in C++ 98; <code>const</code> used to mean "logically constant," but now it means thread-safe. And <code>mutable</code> now means thread-safe as well. His summary slide says:
<p style="padding-left:30px;"><code>const</code> == <code>mutable</code> == thread safe (bitwise const or internally synchronized)</p>
<p style="border:solid 1px black;margin:2em;background-color:#e0e0e0;font-style:italic;padding:1em;">Editor's note: Since this post was written, Herb has updated his slide. See Herb's note in the comment stream below.</p>
Now, I think Herb's talk is quite informative, and I don't dispute the core of what he was trying to convey. It's a good insight, well worth the community's attention. I learned something important; I recommend that you watch the talk. <a title="Put Your Const Foot Forward" href="../../../2012/11/14/put-your-const-foot-forward/">Using <code>const</code> well is an essential skill</a>. But I think in his enthusiasm about the way the language has evolved to make semantics clearer, Herb does us a disservice by oversimplifying.

When Herb uses the C++ == operator to boil his point down to a pithy summary, he's implying true equivalence; what's on one side of the operator is, for all intents and purposes, identical to or indistinguishable from what's on the other side. And while <code>const</code> and <code>mutable</code> and <em>thread-safe</em> are highly related concepts, they are not equivalent enough to each other for ==.

To understand why, answer the following question: <em>Why would good code use </em><code>const</code><em> and/or </em><code>mutable</code><em> even if it's single-threaded?</em>

Ah. I imagine you nodding your head sagely. You see where I'm going, don't you?

These two keywords don't just define semantics for cross-thread access; they define the semantics a variable or object supports when accessed by various scopes (e.g., subroutines or code blocks) on the <em>same</em> thread. If you pass a <code>const Widget &</code> to a function, that function can't call <code>Widget::modifyState()</code> even if it's the only thread in the universe. If you declare a <code>m_lazy_init</code> member variable to be <code>mutable</code>, you are telling the compiler to let you change it where it would normally be disallowed, including on the same thread.

So: <code>const</code> means <em>unchangeable in whatever scope sees const (including many threads)</em>, which is why it also implies <em>thread-safe (if all threads see const)</em>; <code>mutable</code> means <em>changing safely in one or many threads</em>, which is why it also implies <em>thread-safe (if all threads see const)</em>. In C++ 98, these semantics were a bit loose. You could use them carelessly, cast away parts of their guarantees, and generally operate as a law unto yourself. In C++ 11 the semantics of <code>const</code> and <code>mutable</code> are explicit and exacting; the standard library demands thread-safe copy construction. As a result, their role in thread safety is clarified, and we all write better code. Mutexes and atomics and certain kinds of queues are inherently safe to change from any thread; they deserve and require the <code>mutable</code> keyword.

Instead of Herb's final equation, I'd propose a Venn diagram:

[caption id="attachment_888" align="aligncenter" width="300"]<img class="size-medium wp-image-888" alt="The const and mutable keywords are not equivalent in C++ 11, but they do share guarantees about thread safety." src="http://codecraft.co/wp-content/uploads/2013/01/screen-shot-2013-01-01-at-1-25-14-pm.png?w=300" width="300" height="206" /> The const and mutable keywords are not equivalent in C++ 11, but they do share guarantees about thread safety.[/caption]
<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://herbsutter.com/2013/01/01/video-you-dont-know-const-and-mutable/" target="_blank">Video: You Don't Know const and mutable</a> (herbsutter.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://stackoverflow.com/questions/13471628/impossible-to-be-const-correct-when-combining-data-and-its-lock" target="_blank">Impossible to be const-correct when combining data and its lock?</a> (stackoverflow.com)</li>
</ul>

---

Julie (2013-01-02 09:36:06)

I had much the same reaction. Const was extremely useful for both documentation and correctness long before multi-threading was common.

---

Daniel Hardman (2013-01-09 15:40:17)

When I said "unchanging in one or many threads," I meant that it is unchanging whether the context is one thread or many, not that a few threads of const enforcement are enough for safety. You are quite correct that something wouldn't be thread-safe if it is visible in some threads that don't treat it as const.

I love the D language; the distinction between immutable and const is a nice enhancement over C++. Thanks for the link and the thoughtful comment.

---

Herb Sutter (2013-01-03 13:08:02)

Thanks, good point. I've updated my slides to use the "implies" sign (=>) rather than "==" to clarify.

---

Daniel (2013-01-03 14:04:02)

Herb: you're a good sport to read my post after the over-the-top title. :-) Thanks for an informative and though-provoking talk--and thanks for all the good work on C++ 11. I haven't felt this much energy on C++ (from myself or others) for a long time!

---

Daniel (2013-01-02 10:26:32)

I'm glad you mentioned const's use in documentation; that had slipped my mind, but I've often noticed it in the past. One of the codebases that I currently work on has C-style comments next to every parameter for every function, noting whether the parameter is an "in" or an "out" parameter. Using "const" instead would tell the programmer the same thing while using the compiler instead of the programmer's attention to detail to enforce it.

---

sandforddene (2013-01-09 12:46:35)

> So: const means unchanging in one or many threads, which is why it also implies thread-safe;

Incorrect. To be thread safe, an object must be unchanging in _all_ threads. I.e. the object must be immutable. The D programming language's page has a decent overview of the concepts of const and immutable, including comparisons to their C++ equivalents (http://dlang.org/const3.html)

P.S. Compilers that assume const implies an unchanging object generate incorrect code.

---

Daniel Hardman (2013-02-11 20:40:09)

My understanding is as follows: If the state that's mutating is externally visible (e.g., can be read by a public getter), then you can't mark it const. If you're only mutating something like, for example, a private flag that tells you whether you've done lazy init, and if the method is threadsafe, then const is very appropriate. If the method is not threadsafe but does not modify publicly visible state, then you're in a gray area, and the best choice would be to get out of the gray by making the method threadsafe.

---

Brian Cole (2013-02-11 17:52:29)

So we're confused around our company. Should methods that mutate state internally, but are thread safe, be marked as "const"? For example, concurrent_queue::push be marked "const"?

---

Jam (2013-12-17 10:24:11)

Just to understand - 
1. The definition of const in C++ 11 is still "logically" or "observably" const, just like C++ 98. 
2. However, new to C++ 11, const also implies thread safety. 

Right? 

That however implies that the definition of const-ness in C++ 11 is still as ambiguous as ever. For example... 

In one case, Foo.GetValue() could delay load some internal variable, making it reasonable to make GetValue() const. 

In another case, Foo.GetValue() could cause an expensive load of an internal cache that the user of that method should know about. Even if the change is thread safe - would/should I make the method const? I assume I (still) shouldn't. 

Right?

---

Daniel Hardman (2013-12-17 20:46:24)

Under C++ 98, I could write class Widget with an == operator that was not thread-safe, and I was not violating any requirement other than my own good judgment. I could expect to use such a class with the standard library. Writers of the standard library might have wanted me to declare my operator const, but they couldn't reason about potential race conditions and justify their reasoning by pointing to any standard.

Under C++11, my understanding is that Widget::operator == must be declared const to be used by the standard library, or my templates won't compile. Further, if I write Widget in such a way that == isn't thread-safe, I am out of compliance with the guarantees in the standard library, and writers of the library are justified in telling me that misbehavior is my fault, not theirs.

These changes do have consequences. In one recent port from c++98 to c++11, I had to declare a mutex mutable that had not been qualified that way before, before I could make the compiler happy. However, such examples are unusual.

My original beef with Sutter's claim was that it ignored all the semantics of const within the context of a single thread. Those semantics are important, and they remain useful and unchanged in C++ 11.

Since writing the post, I've also had various commenters point out another problem with Sutter's assertion. They note that constness in one scope doesn't guarantee constness in all other scopes--and a single writer in a non-const context throws all guarantees about thread safety and race conditions out the window. For that reason, I won't disagree if you say that effectively, we still have a squishy definition of const, and one that's not as tied to thread safety as Sutter claimed. But I also think Sutter is correct that our guarantee is stronger than it used to be.

Re. Foo.GetValue() -- I wouldn't decide to qualify the method as const based on whether it does something expensive; I'd still go back to the tried and true "is the state of the object observably different after calling the method" question. I know that's a C++98 mindset, but Sutter didn't move the needle for me.

---

Daniel Hardman (2013-12-20 09:06:37)

Jam: That is an excellent and thought-provoking question. As I pondered your example, I began to realize how fuzzy the concept of object state truly is.  I started to answer several times, but my responses left me unsatisfied because I realized I couldn't give a clear enough rule to decide. In a lot of cases, object state is easy to understand--but there are enough corner cases to give me pause.

In some of my other posts, I've been talking about how I want to write a different programming language. One of the concepts I'd been playing around with is formalizing object state (basically, making it super easy to describe the state machine for each class, and the semantics that attach to it, such as "function X can only be called when I'm in state 1 or state 3"). I hadn't spent a lot of time taking that idea from vague to crisp, but your comment makes me think I should ponder the issue a lot more carefully.

---

Jam (2013-12-19 10:40:35)

Thanks for the reply and the original post - I do follow the points made in the post and subsequent follow ups, and realize my question is a bit orthogonal to the discussion on what const means for thread safety in C++ 11. I had really found Herb's video (and your follow up) when I was searching for whether I should make my method const. 

I guess a part of my confusion in the Foo.GetValue() example I mentioned earlier has more to do with what makes a method "observably" const. I think the confusion is in part because what's "observable" is a little ambiguous for me, and it seemed  that C++ 11 didn't really help to remove that ambiguity like Herb may have indirectly mentioned in his (excellent) presentation. 

Not sure if this blog is the best place to continue this, but lets say we have a method like - 
<code>
shared_ptr  ResourceManager::GetSomeResource(). 
</code>

Assume we remove thread safety concerns - say access to SomeResource is synchronized. 

If calling GetSomeResource() results in SomeResource getting loaded into memory, should I (as the designer of ResourceManager) make the above method "const" or not? 

It seems that depends on how I (as the user of ResourceManager) would figure if *it* has gone to an "observably" different state after the call to GetSomeResource(). 

Possibility 1:
It is observably different if there exists some API on ResourceManager that will return a different answer before and after my call to ResourceManager.GetSomeResource(). 

Possibility 2:
It's observably different if I there exists some API on either <i>SomeResource</i> or ResourceManager that will return a different answer before and after my call to ResourceManager.GetSomeResource(). 

Would the answer change depending on whether the resource manager is holding on the resource internally? Lets say, resource manager has a CollectGarbage() call that I need to make after I make calls like GetSomeResource(). Wouldn't making GetSomeResource() const make me think I don't have to call CollectGarbage()? 

Like you mention, seems it shouldn't matter if the resource is expensive or not - that makes it even more ambigous, and more dependent on perspective - what's expensive for a mobile client need not be the case for a desktop client.

---

earwicker (2013-06-28 11:10:23)

"So: const means unchanging in one or many threads,"

But const &v means either one of the following:

1. v doesn't change ("bitwise immutable")
2. changes to v are synchronized against reads from other threads

That is:

void reader(const Thing &v)
{
    std::cout << v.message();
    std::cout << v.message();
    std::cout << v.message();
}

Now, suppose other references to v exist on other threads, and these are non-const. So v may be mutated by those threads such that the message is altered. So as foo is executing, it may print a variety of messages, not necessarily the same message three times. This is perfectly okay under the new C++11 rules.

That is, const still doesn't mean unchanging (in any number of threads).

And it should be noted that this whole thing is totally _optional_. The above restriction only applies if the object is visible to multiple threads. One widely used sure-fire way to stop that is to put a comment in capital letters on the class saying it's not thread-safe! :)

In fact, that's the situation for most classes in the standard library, because they would perform horribly if they always protected all mutations against reads from other threads.

---

Daniel Hardman (2013-06-28 12:12:40)

Excellent point. Well made.

Const isn't claiming that an object can't be changed somewhere else; it's claiming that it can't be changed by the thing that sees it as const.

If I were to fix my verbiage above, I'd probably revise by saying "const means not allowing change from whichever thread(s) see constness".

---

Always declare std::mutex as mutable in C++11? - ExceptionsHub (2017-12-08 00:18:03)

[…] What Sutter got wrong about Const in C++11 […]

---

Lacunas Everywhere | Codecraft (2014-07-16 14:14:17)

[…] Perhaps you’re saying to yourself: “Language X has a way to solve problem Y.” At the micro level, I don’t necessarily disagree. I have written unit tests that (sort of) proved thread-safety in a codebase. I’ve created scripts that proved copyright/license compliance. I have found clever ways to enforce one or two high-value coding standards. I know about Ada’s numeric range types. I’ve decorated python code in such a way that prototype code was discoverable, so we wouldn’t ship it. I’ve used @Override in java. The const and constexpr keywords in C++ tell you something about thread safety. […]