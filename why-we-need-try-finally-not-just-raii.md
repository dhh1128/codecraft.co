---
title: Why we need try...finally, not just RAII
date: 2013-10-31
slug: why-we-need-try-finally-not-just-raii
redirect_from:
  - /2013/10/31/why-we-need-try-finally-not-just-raii
comments:
  - author: Tianyu Zhu
    date: 2013-10-31 21:21:06
    comment: >
      Just a thought: what if your RAII object stored a lambda to the expression you wanted to evaluate?
      
      Actually, that's exactly what scope_guard does, which I believe solves both of your problems nicely.
  - author: Daniel Hardman
    date: 2013-10-31 21:57:01
    comment: >
      Hmm. I'm going to go study scope_guard and lambdas in C++ 11/14 again and see. You're right that that a closure lambda would make the postcondition macro better (good catch! thanks). I'll have to ponder whether it makes the first use case cleaner.
  - author: tianyuzhu
    date: 2013-11-01 21:26:44
    comment: >
      The bad thing about using RAII for post conditions is that you'd have to instantiate the RAII object as soon as possible. If your code throws before the object is instantiated, then it won't run.
      
      So you're forced to think about when a post condition might become applicable. The good thing, though, is that you'd have to think about that anyways, and RAII actually allows you to not have a whole bunch of nested try...finally blocks.
      
      Here's an example. Using RAII:
      
      // First act
      Performer singer;
      scope_guard { singer.bow(); }
      singer.perform();
      
      // Second act
      Performer dancer;
      scope_guard { dancer.bow(); }
      perform_together(singer, dancer);
      
      Using try..finally:
      
      Performer singer;
      try {
          //  First act
          singer.perform();
      
          // Second act
          Performer dancer;
          try {
              perform_together(singer, dancer);
          } finally {
              dancer.bow();
          }
      } finally {
          singer.bow();
      }
  - author: sstereomatchingkiss
    date: 2013-11-02 18:55:17
    comment: >
      this blog(http://the-witness.net/news/2012/11/scopeexit-in-c11/) introduce a very interesting solution
      
      in short
      
      template 
      struct ScopeExit {
          ScopeExit(F f) : f(f) {}
          ~ScopeExit() { f(); }
          F f;
      };
      
      template 
      ScopeExit MakeScopeExit(F f) {
          return ScopeExit(f);
      };
      
      #define SCOPE_EXIT(code) \
          auto STRING_JOIN2(scope_exit_, __LINE__) = MakeScopeExit([=](){code;});
      
      
      example :
      something A;
      SCOPE_EXIT(A.clean());
      //..........
      
      
      I still like the way of RAII better than try...finally
  - author: earwicker
    date: 2013-11-03 17:06:38
    comment: >
      Here's another way of implementing try-finally in C++11, no need to declare a wrapper object explicitly:
      
      http://stackoverflow.com/a/385081/27423
  - author: Daniel Hardman
    date: 2013-11-04 08:38:12
    comment: >
      Very nice! Thanks for teaching me something I hadn't fully understood. I have been away from C++ for a few years, and somehow ScopeGuard didn't make it on my radar. The big thing I learned when I went back and read <a href="http://www.drdobbs.com/cpp/generic-change-the-way-you-write-excepti/184403758" title="scopeguard" target="_blank" rel="nofollow">Alexandrescu's original ScopeGuard article</a> is that C++ 98 allows reference variables to extend the lifetime of temporaries. That little gem had not been one I'd understood; it is the major reason why his technique can get around my complaint that if you declare your postcondition early, you're stuck snapshotting an early version of state against which postconditions are evaluated.
      
      I also tracked down Alexandrescu's talk about the C++ version of ScopeGuard, and did a little studying about how lambdas make this so much better. Hooray!
      
      I still think it's symptomatic of unfortunate language design that someone with that much brainpower had to get involved, just to solve a straightforward problem that every user of the language ought to care about.
  - author: Daniel Hardman
    date: 2013-11-04 08:45:54
    comment: >
      Thanks for pointing this out. I write software that runs on supercomputers, and the compilers there are way behind the times. (I'm just barely convincing people to move from C to C++ 98. Sigh...) Anyway, I had run across ScopeGuard and its variants in the past, but understood it only as a nice way to do cleanup on exit. I thought it evaluated code when the ScopeGuard class was created, which wouldn't work for postconditions. After a little study this past weekend, I realize that the technique solved my postcondition problem as well. It's nice to see that in C++11, the technique has become fully mainstreamed. (And I agree with Castaño, who you referred to, that the idiom in D is super slick.)
  - author: Daniel Hardman
    date: 2013-11-04 08:48:25
    comment: >
      Daniel: You were quick to pick up on the implications of lambdas, if you realized you could have try...finally back in 2008! Wow. Thanks for the link, and for the smart answer on StackOverflow. I've up-voted that answer.
  - author: earwicker
    date: 2013-11-08 03:37:52
    comment: >
      Thank you, but certainly not my insight/foresight :) Dates back to Lisp and Smalltalk (40 years?) http://www.ai.mit.edu/projects/iiip/doc/CommonLISP/HyperSpec/Body/mac_with-open-file.html Same idea in Java: http://www.octopull.co.uk/java/ACCU-Spring-2001/img15.htm
  - author: J
    date: 2014-11-11 06:04:55
    comment: >
      D has had scoped exit from the beginning. Unfortunately there are no big companies supporting it, but that may well be the language you should be using instead of c++11
  - author: Daniel Hardman
    date: 2014-11-11 08:34:42
    comment: >
      Yes, that is a nifty feature of D. I have debated switching to D on some of my projects...
  - author: Bastian
    date: 2015-10-20 11:48:34
    comment: >
      Yet another try/finally:
      
      try { try { // alias "TRY"
      //     try this
      throw Finally(); } catch (...) { // alias "FINALLY" 
      //     always to that
      throw; } catch (Finally const &) { } // alias "END"
  - author: Daniel Hardman
    date: 2015-10-20 11:54:40
    comment: >
      That gave me a good chuckle. Yuck! But it definitely works...
  - author: quicknir
    date: 2015-12-28 14:30:30
    comment: >
      As soon as I read this I thought of scopeguard, which I see that other people have mentioned. I'm curious, does this cause you to recant the position in the title of your article? I actually think that scopeguard is nicer than try/finally in every way, it avoids the complicated nasty nesting. And practically, the majority of the time, the finally block is just cleaning up non-memory resources anyhow, which RAII does much more nicely.
  - author: Daniel Hardman
    date: 2015-12-28 18:00:37
    comment: >
      I'd say it takes a lot of the teeth out of my argument. Scopeguard does have many great features that mostly make my concern go away. However, you mentioned one virtue of scopeguard that I don't actually like so much: the lack of nesting. I am not a fan of massively nested stuff, of course, but sometimes I kind of *like* the curly braces of try...finally to make the guarded scope totally explicit. I guess if I really want curlies, I can add them just for form... :-)
  - author: whatsbottle
    date: 2016-03-11 09:04:41
    comment: >
      I totally disagree your point. As a daily Java developer, I hate try-finally with passion. RAII initially looks more efforts, in fact it save time and make code cleaner and correct. C++'s RAII is "repeatable", you write the class once and forget it forever. With try-finally, people tend to copy-paste it here and there, or just ignore it. There is nothing to ensure they won't forget to write the "finally" block.
  - author: Daniel Hardman
    date: 2016-03-15 07:31:31
    comment: >
      I agree that RAII has some nice benefits. Those benefits are more apparent if the cleanup you want to do is very standardized (e.g., close a file handle, release memory). But if the cleanup you want to do is unique to the particular block of code you are in--such as my example about having an avatar take a bow--then creating a custom class for just that one block of code seems less desirable. In other words, repeatability is only useful if you need to repeat something. :-)
---
The claim has been made that because C++ supports <a class="zem_slink" title="Resource Acquisition Is Initialization" href="http://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization" target="_blank" rel="wikipedia">RAII</a> (resource acquisition is initialization), it doesn't need <span style="font-family:courier, fixedwidth;">try...finally</span>. I think this is wrong. There is at least one use case for <span style="font-family:courier, fixedwidth;">try...finally</span> that's very awkward to model with RAII, and one that's so ugly it ought to be outlawed.

<strong style="color:#000080;">The awkward use case</strong>

What if what you want to do during a <span style="font-family:courier, fixedwidth;">...finally</span> block has nothing to do with freeing resources? For example, suppose you're writing the next version of Guitar Hero, and you want to guarantee that when your avatar leaves the stage, the last thing she does is take a bow--even if the player interrupts the performance or an error occurs.

<figure><img src="http://farm3.staticflickr.com/2765/4162745269_6989a977bd.jpg" alt="" width="336" height="500" /><figcaption>...finally, take a bow. Photo credit: <a href="http://www.flickr.com/photos/gavinzac/4162745269" target="_blank">gavinzac (Flickr)</a></figcaption></figure>

Of course you can ensure this behavior with an RAII pattern, but it's silly and artificial. Which of the following two snippets is cleaner and better expresses intent?<!--more-->
<p style="font-weight:bold;font-family:arial, helvetica, sans serif;margin-left:2em;">RAII solution</p>

<pre style="font-size:9pt;margin-left:2em;padding:1em;border:solid 1px #606060;background-color:#e8e8e8;margin-bottom:2em;"><span style="color:blue;">void</span> perform(Avatar <span style="color:blue;">const</span> & avatar) {
    <span style="color:blue;">class</span> BowGuarantee {
        Avatar <span style="color:blue;">const</span> & avatar;
    <span style="color:blue;">public</span>:
        Bow(Avatar <span style="color:blue;">const</span> & avatar) : avatar(avatar) {}
        ~Bow() {
            avatar.take_a_bow();
        }
    } my_bow_guarantee(avatar);

        <span style="color:green;">// Do all the heavy lifting in the function.

    // The bow silently but reliably takes place when 
    // my_bow_guarantee is destroyed.</span>
}</pre>
Or this:
<p style="font-weight:bold;font-family:arial, helvetica, sans serif;margin-left:2em;">Solution with try...finally</p>

<pre style="font-size:9pt;margin-left:2em;padding:1em;border:solid 1px #606060;background-color:#e8e8e8;margin-bottom:2em;"><span style="color:blue;">void</span> perform(Avatar const & avatar) {
    <span style="color:blue;">try</span> {
        <span style="color:green;">// Do all the heavy lifting in the function.</span>
    } <span style="color:blue;">finally</span> {
        avatar.take_a_bow();
    }
}</pre>
Don't get me wrong. I like RAII, and I use it as a best practice. But you gotta admit, <span style="font-family:courier, fixedwidth;">try...finally</span> is a far slicker way to address this use case. It takes one less variable, one less class, and many less lines.

My own experience tells me that this use case crops up regularly; it's not so exotic that language designers can marginalize it.

<strong style="color:#000080;">The so-ugly-it-ought-to-be-outlawed use case</strong>

Here's a problem that's a bit trickier. I won't go so far as to claim that you can't solve it with RAII--I just claim that no software developer who cares about high-quality code ought to be happy with the solution that RAII offers. <span style="color:#800000;">(Update: Thanks to Tianyu Zhu [see comment stream] for challenging me to clean up this ugliness with C++ 11 closures. I'll write a follow-up post about as soon as I fiddle a bit, and we'll see how much better it looks... In the meantime, read the following with a pre-C++ 11 mindset.)</span>

Today I was trying to implement <a title="Postcondition" href="http://en.wikipedia.org/wiki/Postcondition" target="_blank" rel="wikipedia">postconditions</a> in one of my C++ codebases. This is a "<a href="http://www.eiffel.com/developers/design_by_contract.html" target="_blank">design-by-contract</a>" technique that enforces a guarantee about the state that a function provides on exit. My first attempt used a macro (so I could string-ize expr with the # prefix; this is one of the few use cases where I love macros...) to define a postcondition more or less like this:
<pre style="font-size:9pt;margin-left:2em;padding:1em;border:solid 1px #606060;background-color:#e8e8e8;margin-bottom:2em;"><span style="color:blue;">#define</span> POSTCONDITION(expr) \
<span style="color:blue;">    if</span> (!expr) \
<span style="color:blue;">        throw</span> ContractViolation(#expr, __FILE__, __LINE__)</pre>
Looks pretty straightforward, right? I flipped over to a function where I wanted to test postconditions, and invoked the macro a few times at the bottom:
<pre style="font-size:9pt;margin-left:2em;padding:1em;border:solid 1px #606060;background-color:#e8e8e8;margin-bottom:2em;">RecordID insert_new_record(Tuple const & fields,
        Transaction & trans, File & main_table, 
        vector<File &> const & indexes) {

    <span style="color:green;">// Declare some local variables.</span>
    <span style="color:blue;">size_t</span> bytes_written = 0;
    RecordID new_record_id;
    <span style="color:blue;">size_t</span> indexes_updated = 0;

        <span style="color:green;">// Do all the heavy lifting. (50 lines omitted)</span>

    <span style="color:green;">// Guarantee that we've fulfilled our contract.</span>
    POSTCONDITION(trans.committed() == (new_record_id != 0));
    POSTCONDITION(trans.committed() == (bytes_written > 0));
    POSTCONDITION(trans.committed() ? 
        indexes_updated == indexes.size() : 
        indexes_updated == 0);
}</pre>
For about thirty seconds after I wrote this, I was feeling cheerful. And then I groaned.

I'd fallen victim to the classic problem that RAII is supposed to solve--in the 50 omitted lines, if I threw exceptions or rejected input, my postconditions wouldn't ever be tested. Since the postconditions were supposed to guarantee compliance to a contract under all cases, without RAII, I'd sort of defeated the whole purpose.

So I went back and rewrote the macro:
<pre style="font-size:9pt;margin-left:2em;padding:1em;border:solid 1px #606060;background-color:#e8e8e8;margin-bottom:2em;"><span style="color:blue;">#define</span> POSTCONDITION(expr) \
    <span style="color:blue;">class</span> _postcond_##__LINE__ { \
        <span style="color:blue;">char const</span> * expr_text;
        <span style="color:blue;">bool</span> value;
        _postcond_##__LINE__(<span style="color:blue;">bool</span> e, <span style="color:blue;">char const</span> * etxt) : \
            expr_text(etxt), value(e) {} \
        ~_postcond##__LINE__() { \
            <span style="color:blue;">if</span> (!value) \
                <span style="color:blue;">throw</span> ContractViolation(#expr, __FILE__, __LINE__); \
    } my_postcond_##__LINE__</pre>
Setting aside the increasingly yucky macro, can you see why I was groaning again after another 30 seconds?

Yes, this macro uses RAII to test the postcondition when the code goes out of scope. But when does it <em>store</em> the value of the expression it's going to test?

Yep. When it's <em>created</em>. And that, in a nutshell, is my beef with RAII. It requires you to snapshot state at the top of a lexical scope, even when that's just the opposite of what you need.

You can hit a square peg into a round hole. C++ is nothing if not flexible. But it's so ugly it makes me shudder. In C++ 98, what you have to do is create state reference variables in your postcondition class for every entity that will participate in the eventually evaluated expression. In C++ 11 you can use a closure that captures reference variables, which is a bit better. But I'm not sure how much; I'll do a follow-up post about that. Here, sans macro for the sake of clarity, is what a correct C++ 98 implementation of the idea would look like in my function that updates a database record:
<pre style="font-size:9pt;margin-left:2em;padding:1em;border:solid 1px #606060;background-color:#e8e8e8;margin-bottom:2em;">RecordID insert_new_record(Tuple const & fields, 
        Transaction & trans, File & main_table, 
        vector<File &> const & indexes) {

    <span style="color:green;">// Declare some local variables.</span>
    <span style="color:blue;">size_t</span> bytes_written = 0;
    RecordID new_record_id;
    <span style="color:blue;">size_t</span> indexes_updated = 0;

    <span style="color:green;">// Declare a postcondition class that stores references
    // to all the variables it will test when it goes out of
    // scope. In this example, it requires us to duplicate
    // each local variable, plus 2 of the function parameters.
    // Not only does it take a ridiculous amount of code--it's
    // fragile during maintenance, and it totally obscures
    // our relatively straightforward intent.</span>
    <span style="color:blue;">class</span> postcondition {
        <span style="color:blue;">size_t</span> & _bytes_written;
        RecordID & _new_record_id;
        <span style="color:blue;">size_t</span> & _indexes_updated;
        Transaction & _trans;
        vector<File &> & _indexes; 
    <span style="color:blue;">public</span>:
        postcondition(<span style="color:blue;">size_t</span> & bw, RecordID & recid, 
            <span style="color:blue;">size_t</span> & iup, Transaction & trans):
            _bytes_written(bw), _new_record_id(recid),
            _indexes_updated(iup), _trans(trans) {}
        ~postcondition() {
            <span style="color:blue;">char const</span> * expr_text = NULL;
            <span style="color:blue;">if</span> (trans.committed()) {
                <span style="color:blue;">if</span> (_new_record_id == 0) 
                    expr_text = "expected new record id != 0";
                <span style="color:blue;">else if</span> (_bytes_written < 1) 
                    expr_text = "expected bytes written > 0";
                <span style="color:blue;">else if</span> (_indexes_updated < indexes.size()) 
                    expr_text = "expected all indexes to be updated";
            } else {
                <span style="color:blue;">if</span> (_new_record_id != 0) 
                    expr_text = "expected no new record id"
                <span style="color:blue;">else if</span> (_bytes_written > 0)
                    expr_text = "expected 0 bytes written";
                <span style="color:blue;">else if</span> (_indexes_updated > 0)
                    expr_text = "expected 0 indexes updated";
            }
            <span style="color:blue;">if</span> (expr_text) {
                throw ContractViolation(expr_text, __FILE__, __LINE__);
            }
        }
    } mypostcondition;

        <span style="color:green;">// Do all the heavy lifting. (50 lines omitted)</span>

    <span style="color:green;">// Postcondition is enforced no matter how or when we exit.</span>
}</pre>
If you can read that code without wincing, you have a stronger constitution than I do. It's awful. And good luck macro-izing it; even with __VA_ARGS__ to give you variadic macros, you end up with something messy enough to curl the hair on your toes. Given the choice between hand-rolled, bespoke postcondition classes in every function, a macro nightmare, or nothing, most of us would (sensibly) choose nothing. Forget postconditions. Off the top of my head, I can't think of another coding goal besides postconditions that needs to interact with final state on exit, and that is thus a nightmare to work with using RAII. But I wouldn't be surprised if there are others.

What would it look like if C++ supported <span style="font-family:courier, fixedwidth;">try...finally</span>? My first macro definition would work just fine, and the function body would be simple and clean:
<pre style="font-size:9pt;margin-left:2em;padding:1em;border:solid 1px #606060;background-color:#e8e8e8;margin-bottom:2em;">RecordID insert_new_record(Tuple fields, Transaction & trans, 
        File & main_table, vector<File &> indexes) {
<span style="color:green;">    // Declare some local variables.</span>
    <span style="color:blue;">size_t</span> bytes_written = 0;
    RecordID new_record_id;
    <span style="color:blue;">size_t</span> indexes_updated = 0;    <span style="color:blue;">try</span> {
        <span style="color:green;">// Do all the heavy lifting. (50 lines omitted)</span>
    } <span style="color:blue;">finally</span> {
        <span style="color:green;">// Guarantee that we've fulfilled our contract.</span>
        POSTCONDITION(trans.committed() == (new_record_id != 0));
        POSTCONDITION(trans.committed() == (bytes_written > 0));
        POSTCONDITION(trans.committed() ? 
            indexes_updated == indexes.size() : 
            indexes_updated == 0);
    }
}</pre>
RAII and <span style="font-family:courier, fixedwidth;">try...finally</span> may be able to achieve the same things, but they are definitely not equally good alternatives in all use cases.

I understand some of the complex choices that C++'s standardization committee has to wrestle with; I can imagine how they might have concluded that the extra benefit of <span style="font-family:courier, fixedwidth;">try...finally</span> was not worth the compiler burden they'd be imposing. I also admit that if C++ had <span style="font-family:courier, fixedwidth;">try...finally</span>, it might diminish RAII's status as the recommended C++ solution to resource management, which could be a bad thing. But those pragmatic argums are biased toward compiler creators, not toward us humble programmers who make a living writing code. So much for user-centered design...

The lack of <span style="font-family:courier, fixedwidth;">try...finally</span> is a shortcoming of C++ that some of the smartest programmers on the planet have worked around. Alexandrescu's ScopeGuard for C++ 98 is pretty amazing, and would clean up a lot of the code that I've shown above; the C++ 11 version is a huge improvement. But it feels to me like we shouldn't have to work this hard to do something that's conceptually so straightforward. I want a more satisfying answer in <a href="on-bread-recipes-maps-and-intentions.md">my "better programming language" project called "intent."</a> Stay tuned for more discussion as intent matures.
