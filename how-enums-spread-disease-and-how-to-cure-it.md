---
title: How Enums Spread Disease -- And How To Cure It
date: 2012-10-29
slug: how-enums-spread-disease-and-how-to-cure-it
redirect_from:
  - /2012/10/29/how-enums-spread-disease-and-how-to-cure-it
---

Poorly handled enums can infect code with fragility and tight coupling like a digital <a href="http://en.wikipedia.org/wiki/Typhoid_Mary" target="_blank" rel="wikipedia">Typhoid Mary</a>.

Say you're writing software that optimizes traffic flow patterns, and you need to model different vehicle types. So you code up something like this:
<p style="background-color:#eeeeee;padding-left:31px;font-weight:bold;border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:black;margin-top:2em;">vehicle_type.h</p>

<pre style="padding-left:30px;margin-bottom:1em;">enum VehicleType {
    eVTCar,
    eVTMotorcycle,
    eVTTruck,
    eVTSemi,
};</pre>
Then you press your enum into service:
<p style="background-color:#eeeeee;padding-left:31px;font-weight:bold;border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:black;margin-top:2em;">route.cpp</p>

<pre style="padding-left:30px;margin-bottom:1em;">if (vehicle.vt == eVTSemi || vehicle.vt == eVTTruck) {
    <span style="color:#008000;">// These vehicle types sometimes have unusual weight, so we 
    // have to test whether they can use old bridges...</span>
    if (vehicle.getWeight() > bridge.getMaxWeight()) {</pre>
Quickly your enum becomes handy in lots of other places as well:
<pre style="padding-left:30px;margin-bottom:1em;">if (vehicle.vt == eVTMotorcycle) {
    <span style="color:#008000;">// vehicle is particularly sensitive to slippery roads</span></pre>
And...
<pre style="padding-left:30px;margin-bottom:1em;">switch (vehicle.vt) {
case eVTTruck:
case eVTSemi:
    <span style="color:#008000;">// can't use high-occupancy/fuel-efficient lane</span>
case eVTMotorcycle:
    <span style="color:#008000;">// can always use high-occupancy/fuel-efficient lane</span>
default:
    <span style="color:#008000;">// can only use lane during off-peak hours</span>
}</pre>
<strong>Diagnosis</strong>

The infection from your enum is already coursing through the bloodstream at this point. Do you recognize the warning signs?
<ul>
	<li>Knowledge about the semantics of each member of the enum are spread throughout the code.</li>
	<li>The members of the enum are incomplete. How will we account for cranes and bulldozers and tractors and vans?</li>
	<li>Semantics are unsatisfying. We're saying cars are never gas guzzlers or gas savers; what about massive old steel-framed jalopies and tiny new hybrids?</li>
</ul>
<figure><img alt="" src="http://farm2.staticflickr.com/1193/3165350717_bf8656ba38.jpg" height="374" width="500" /><figcaption>A vehicle that challenges our tidy enum. Photo credit: Manila Imperial Motor Sales (Flickr)</figcaption></figure>

The infection amplifies when we want to represent the enum in a config file or a UI. Now we need to <!--more-->convert to and from strings, and we use the classic shadow array of string literals, indexed by enum:
<pre style="padding-left:30px;margin-bottom:1em;"><span style="color:#339966;">// THIS ARRAY ***MUST*** BE KEPT IN SYNC WITH THE ENUM DECLARED
// AT THE TOP OF vehicle_type.h!!!</span>
char const * VEHICLE_TYPE_NAMES[] = { 
    "car", 
    "motorcycle", 
    "truck", 
    "semi"
};

char const * getVehicleTypeName(VehicleType vt) {
    return VEHICLE_TYPE_NAMES[vt];
}</pre>
Lest you think this ugliness is unique to C/C++, the Java or C# equivalent isn't all that pretty, either:
<pre style="padding-left:30px;margin-bottom:1em;">@override
String toString() {
    <span style="color:#339966;">// eVTxyz --> xyz</span>
    return super.toString().toLowerCase().substring(3);
}

static VehicleType fromString(String vt) {
    if (vt.equals("truck")) return eVTTruck;
    if (vt.equals("semi")) return eVTSemi;
    ...
}</pre>
You might be rolling your eyes at the clumsy conversions. Yes, we could do error checking to make <code>getVehicleTypeName()</code> safer. Yes, we could use reflection in some languages to automate these conversions.

That misses the point.

We're still propagating knowledge indiscriminately. If the UI is involved, chances are there's a view, or an html <select> tag, or a javascript validation function, or--heaven help us--a localized message table--that has knowledge about the possible values of this enum. As the enum grows over time, your maintenance must regularly touch many different modules, possibly at many different layers. This is a recipe for bugs.

The code is sick.

Pretty soon symptoms become externally visible: code is measurably buggy; unit tests require lots of maintenance when you make a change; you have debates about how to accommodate strange new vehicle types; the high priest/grand wizard of the codebase regularly corrects acolytes that attempt "simple" tweaks; people advocate a coding standard that requires comments on every member of the enum to explain its ramifications.

<strong>Treatment</strong>

The good news is that this particular sickness has an effective and straightforward cure.

The root cause of our disease is semantic diffusion and coupling, and the essence of the cure is encapsulation through a form of <a href="http://en.wikipedia.oriki/Declarative_programming" target="_blank">declarative programming</a>.

I'll present a formula for our prescription in C++ (where I first learned it from <a title="Julie Jones: Learn voraciously." href="julie-jones-learn-voraciously.md">Julie Jones</a>, years ago); then we can explore what it's doing, and what its analogs might be in other languages.
<p style="background-color:#eeeeee;padding-left:31px;font-weight:bold;border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:black;">vehicle_type_tuples.h</p>

<pre style="padding-left:30px;margin-bottom:1em;"><span style="color:#888888;"><span style="color:#339966;">// No sentry. This is deliberate.</span>

<span style="color:#339966;">// TUPLE(id, max_wheels, max_weight_kg, max_passengers, avg_km_per_liter)</span></span>
TUPLE(Car, 4, 1800, 6, 8)
TUPLE(Truck, 4, 5700, 4, 5.5)
TUPLE(Motorcycle, 2, 450, 18)
TUPLE(Semi, 18, 19000, 2, 4)

<span style="color:#0000ff;">#undef</span> TUPLE</pre>
<p style="background-color:#eeeeee;padding-left:31px;font-weight:bold;border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:black;margin-top:2em;">vehicle_type.h</p>

<pre style="padding-left:30px;margin-bottom:1em;"><span style="color:#0000ff;">#ifndef</span> VEHICLETYPE_H
<span style="color:#0000ff;">#define</span> VEHICLETYPE_H

enum VehicleType {
<span style="color:#0000ff;">#define</span> TUPLE(id, max_wheels, max_weight_kg, max_passengers, avg_km_per_liter) eVT##id,
<span style="color:#0000ff;">#include</span> "vehicle_type_tuples.h"
};

char const * getVehicleTypeName(VehicleType vt);
int getVehicleTypeMaxWheels(VehicleType vt);
int getVehicleTypeMaxWeightKg(VehicleType vt);
int getVehicleTypeMaxPassengers(VehicleType vt);
double getVehicleTypeFuelEconomy(VehicleType vt);

<span style="color:#0000ff;">#endif</span> <span style="color:#339966;">// sentry</span></pre>
<p style="background-color:#eeeeee;padding-left:31px;font-weight:bold;border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:black;margin-top:2em;">vehicle_type.cpp</p>

<pre style="padding-left:30px;margin-bottom:1em;"><span style="color:#0000ff;">#include</span> "vehicle_type.h"

static struct VehicleTypeTuple {
    VehicleType id;
    char const * name;
    int max_wheels;
    int max_weight_kg;
    int max_pasengers;
    double avg_km_per_liter;
};

static VehicleTypeTuple const TUPLES[] = {
<span style="color:#0000ff;">#define</span> TUPLE(id, max_wheels, max_weight_kg, max_passengers, avg_km_per_liter) \
    { eVT##id, #id, max_wheels, max_weight_kg, max_passengers, avg_km_per_liter },
<span style="color:#0000ff;">#include</span> "vehicle_type_tuples.h"
};

static const size_t TUPLE_COUNT = sizeof(TUPLES) / sizeof(TUPLES[0]);

char const * getVehicleTypeName(VehicleType vt) {
    if (static_cast<size_t>(vt) < TUPLE_COUNT) {
        return TUPLES[vt].name;
    }
    return "unknown";
};

<span style="color:#339966;">... other functions ...</span></pre>
<p style="background-color:#eeeeee;padding-left:31px;font-weight:bold;border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:black;margin-top:2em;">bridge.cpp</p>

<pre style="padding-left:30px;margin-bottom:1em;">bool mayBeTooHeavy(VehicleType vt) {
    return getVehicleMaxWeightKg(vt) > 5000;
}</pre>
<p style="background-color:#eeeeee;padding-left:31px;font-weight:bold;border-bottom-style:solid;border-bottom-width:1px;border-bottom-color:black;margin-top:2em;">route.cpp</p>

<pre style="padding-left:30px;margin-bottom:1em;">if (Bridge::mayBeTooHeavy(vehicle.vt)) {</pre>
Setting aside the last two snippets for a moment, the obvious ingredients in the C++ version of our formula are:
<ul>
	<li>Our vehicle enum values, and their associated attributes or semantics, are declared by calling a macro, TUPLE.</li>
	<li>This macro is called once for each enum value, in a header that contains no sentry (vehicle_type_tuples.h). Essentially, this creates a table of data that can be manipulated at compile time.</li>
	<li>The TUPLE macro is #defined to mean different things in different places (in vehicle_type.h, and again in vehicle_type.cpp). Each time the meaning of the macro changes, we #include our table of data and generate more code.</li>
</ul>
How does this help us?
<ul>
	<li>All knowledge about possible enum values is concentrated in one file.</li>
	<li>We no longer have to hand-edit a parallel shadow array with an obnoxious (and ignorable) comment to keep it in sync with our enum. It is impossible to get out of sync.</li>
	<li>The set of attributes that we can associate with our enum is unbounded; we can add as many fields to our tuple as we wish.</li>
	<li>Our file of tuples is extraordinarily simple to parse; it contains nothing other than a series of TUPLE() calls. If we need to validate enum values in some other language or environment, we can process the file during the build to generate a javascript function, an xml example, a sample config file, and so forth.</li>
</ul>
<strong>Separation of Concerns</strong>

Another characteristic of the solution deserves deeper discussion. Why did we include the snippet from bridge.cpp in our solution? Isn't another function there unnecessary? Why not do the following in vehicle_type_tuples.h?
<pre style="padding-left:30px;margin-bottom:1em;"><span style="color:#339966;">// TUPLE(id, heavy_risk, slides_easily, fuel_consumption)</span>
TUPLE(Car, false, false, average)
TUPLE(Motorcycle, false, true, low)
TUPLE(Truck, true, false, high)
TUPLE(Semi, true, true, high)</pre>
Then we could do this in route.cpp:
<pre style="padding-left:30px;margin-bottom:1em;">if (vehicle.vt.heavy_risk) {</pre>
After all, if our goal is to figure out which vehicles are heavy enough to cause problems on bridges, shouldn't we just say that in our tuples?

The answer involves coupling. The second, less optimal form of the TUPLE macro builds into each vehicle type assumptions about how and why the vehicle type's inherent characteristics will be analyzed, while the earlier and better form does not. Instead, it leaves judgement about the ramifications of these characteristics to other parts of the system (like bridges) that know about <em>their own</em> problem domain.

In other words, the better version couples vehicle type and traffic routing more loosely.

Which version will require less maintenance if you decide that the threshold for vehicles that are too heavy for a bridge is 10,000 kg instead of 5,000? Which will require less maintenance if you decide you now need 4 gradations of ranking on fuel economy, or if the average fuel economy on your vehicles changes?

<strong>Other Languages</strong>

Only a few modern programming languages provide a preprocessor, but this doesn't mean that lack of macros makes enum encapsulation impossible. All languages that I know support some form of tabular data structure, and quite a few offer first-class tuples.

In Java, for example, you could write a static initializer block that builds a HashMap of attributes for each value in an enum. In Python, you could populate a dict indexed by string constants. The basics of the technique are replicable anywhere.

<strong>Pragmatism</strong>

Of course, not every enum is worth handling in this careful and encapsulated way. If you have an enum that's got three items, and it will never change, and you have no interesting semantics to manage, and you're not converting it to and from strings, and the enum is only visible in a single module, then (to quote my friend Moray King), the juice is probably not worth the squeeze.

For the more critical enums in your codebase, however, I think a careful approach will pay big dividends.

<strong>Signs of Health</strong>

You'll know you're handling enums right if it's difficult or impossible to add a new value to an enum without also specifying that value's attributes, and if you stop seeing tests for one or more enum values, scattered in conditionals all over the code. Statements like this:
<p style="padding-left:30px;"><code>if (vehicle.vt == eVTTruck || vehicle.vt == eVTSemi)</code></p>
or...
<p style="padding-left:30px;"><code>switch (vehicle.vt)</code></p>
... will be hidden in functions that capture (encapsulate) the semantic condition you really want to test. In fact, enum values themselves will only appear in places where an object's state is set directly; even in semantic wrappers, you'll often be testing a characteristic (like weight [mass], in our example) instead of actual enum values themselves. Certainly, all other code works off of semantics. When you add a new enum value, you only have to examine a handful of semantic functions to tease out ramifications, and your confidence in the tweak is high. Unit tests break in predictable and isolated ways, and the fixes become obvious.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Find one enum that's problematic in your code, and clean it up.</span></em></p>



---

Daniel (2012-10-29 09:32:04)

They say great minds think alike... :-)

Seriously, I'm bummed that we didn't get to work together longer. I can tell that we would have been good allies on lots of issues.

---

Brian Saville (2012-10-29 09:38:55)

I like the idea.  I think that the power of Java enums is not as widely known, and this merges very well with your macro concept.  Enums in Java behave a little like classes, you can even have private constructors and additional properties in the classes (unlike C# or other languages).  

We discovered this a couple of years ago and it is used quite extensively in some places in our code base.  I wish that more knew of the power of enums in Java honestly.

---

dougbert (2012-10-29 09:53:56)

timing....it either voltage or timing.....that is what a good hardware debugger tech told when I was working with him....

---

Daniel (2012-10-29 09:58:39)

Yes, I agree that java enums are quite powerful. They allow you to encapsulate everything about an enum, including its semantics. We often pay the cost in poor code elsewhere, when we fail to take advantage of that power. So many java enum classes are just as rudimentary as their C ancestors...

---

dougbert (2012-10-29 08:24:21)

EXACTLY! Well put

---

Daniel (2012-10-30 07:38:53)

Nathan: That's a great insight--how enums force the question of type extensibility. I'd never thought of their ramifications that way. Thanks for chiming in.

---

nwwells (2012-10-30 06:03:37)

Enums have always been an interesting topic for me. I think they really force you to make important decisions about your domain, in terms of type extensibility. Great post.

---

dougbert (2012-10-29 10:06:05)

one of descriptions that I use in describing the opposite of a "single point of implementation" encapsulation  is "distributed implementation of the same logic".  And the use of the term "Typoid Mary" is a beautiful description of the consequences of that.



---

Daniel Hardman (2015-04-15 14:12:47)

I appreciate the thoughtful comment, Antoine.

Although it's nice to assert that enums should only store state, most enums that I'm familiar with eventually get messier than that. They may start simple, but we programmers don't leave them that way. Take the state machine in a parser, for example (a place where "state" is surely the key interest.) Even there, there are logical relationships between the states that we need to represent somewhere in the code: which states are allowed to precede and follow which other states? which states represent recoverable versus unrecoverable error conditions? Etc. Even an enum points_of_the_compass {north, south, east, west} has interesting semantics such as the fact that it's legal to compose a new direction north+west or south+east, but not north+south--or the fact that north and south are special because they retain meaning at a pole, whereas east and west do not. About the only "pure" enum that I'm sure would meet your criteria would be boolean {true, false}.

Your comment about OOP is insightful. It is true that the VehicleTypeTuple struct is not full-blown OOP, and that it could be. However, it would be read-only OOP, since all of the attributes (semantics) we're declaring for a vehicle type are known at compile-time and are thus constant for the life of the application. This means we never need setters, and we never need more than one instance of each tuple. To me, it felt like managing that data as POD instead of objects made more sense, but I guess that's more of a stylistic choice.

---

Daniel Hardman (2015-04-15 13:59:02)

Thanks for the thoughtful response!

Whether or not the set of items in an enum is well bounded is interesting, and I agree with you that making bad choices about what to model as an enum can have negative consequences. However, I think some of your examples are just as fuzzy as mine. When I studied linguistics I learned that some languages recognize only 3 or 4 colors. We may be used to the ROYGBIV set, but artists and interior designers would probably want many more items in their color enum. Classification is a very deep topic that is far more subjective than most people think. Even the set of species in the genus "homo" changes as scientists debate whether homo heidelbergensis and homo sapiens rhodesiensis are really separate species.

Days of the week and months of the year are a bit crisper, though of course different calendars slice and dice time differently.

But let's set that issue aside for a moment and say we settle on simple, stable enums, and they never prove to be controversial. Fine. We still have the problem of how/where additional semantics for each item in the enum are expressed in code. Take color again. How do we decide if a color is "warm" or "cool"? How do we decide which colors are complimentary? How do we map the colors to traffic signal meanings? How do we know which colors are most likely to be problematic for different kinds of color blindness, or which colors carry which connotations in different cultures (black=mourning in many western cultures, but white=mourning in Asia)?

You might claim that really *good* enums are never like this; if the enum is ever used for something other than a totally opaque numeric constant, it's a bad example. Again, I don't buy it. Take the state machine in a TCP/IP stack. I guarantee that implementations of network protocols have switch statements that clump certain states together--they treat FIN and CLOSE the same way under certain conditions, for example. What this means is that these enumerated states have some common semantic meaning that the code needs to address. 

Of course, a particular codebase may not need lots of rich semantics for its enums, but what I'm claiming is that usually, it needs one or two. They grow like weeds, without any management. And the typical way to address this need, in all the languages I know, is to write helper functions (or, far worse, random blocks of code sprinkled everywhere) that switch based on members of the enum. This is true almost independent of how simple and stable your enum is. There is no place where you can gather all the semantics together and edit them as a single unit. If you want to add a new semantic dimension to your enum, or adjust how an existing semantic dimension works, you have to hunt through the code and analyze semantics from scratch, with every edit. Good unit tests help, but they catch the symptom, not the kernel of the problem.

The *real* problem is that we don't acknowledge all the meaning that attaches to our enums, and we make no effort to encapsulate that meaning.

---

crystal_traveler (2015-04-16 01:50:13)

Nice article. Advice seems more general than enum usage and reminds me more of overuse of special cases. Reminds me of  Rule 5 of Rob Pike's 5 rules (http://users.ece.utexas.edu/~adnan/pike.html):

"write stupid code that uses smart objects"

I haven't written code with lots of special cases like this in years though I can imagine it's a bad habit many new programmers never eventually shake. Disclaimer: I'm not a Rob Pike fanboy, on the whole I think he is closed minded, dogmatic, and stuck in his ways.

BTW That C macro trick has no place in modern C++. You should be using templates meta-programming instead. There are ways to guarantee consistency between the Enum definitions and that data definition without needing a shared intermediate include file. Look into constexpr and static_assert().



---

J Henry (2015-04-15 13:15:42)

The type of data you describe in your example is not appropriate for enumerations, as the type of vehicles in existence is not a finite list.  Enumerations are more appropriate for finite lists that change extremely rarely, if at all, and represent discreet pieces of information such as days in the week, months in the year, colors, types of mammals...you get the message.  

You would not create an enumeration with a value of 'Primate', because there are many different types of primates.  You could however create an enumeration that has a value of 'Homo Sapien' because that is a discreet classification.

Enumerations are a powerful way to build assumptions into your code that you want to enforce on other parties that are using your code.  When used incorrectly, like in your example, they serve as a way to shoot yourself in the foot.

---

Antoine Ménard (@Enthouan) (2015-04-15 12:19:52)

I guess the way to solve this disease is just to use Enum for what they are supposed to be used for. Which is storing a state, that's it.

This article really lacks of OOP concept. In the first example the enum is a property on the 'vehicule' object, it would be way better to add all the properties needed to that class instead of creating a weird 'VehicleTypeTuple' struct...

---

Daniel Hardman (2015-04-18 10:39:22)

Thanks for the reference to Pike. I'd run across his rules years ago, then forgotten all about them. He puts some good wisdom into words.

Regarding the comment about macros and modern C++: I am curious. I don't consider myself a template black-belt, but I'm maybe a blue belt or brown belt. I can tell you what SFINAE is, anyway. Yet I'm not aware of a way to replicate this technique in any meaningful way without macros. Could you give me a hint what you are thinking?



---

joao vasconcelos (2017-05-30 05:29:10)

Good read, I was looking into other uses for enums in C# and stumbled on this post which made me rethink my design, although i am not sure i would follow the example in any language apart from .C because as far as im aware all other languages mentioned (including c++) allow a OO solution to be achieved   

I haven't touched C++ for a while but im pretty sure it supports interfaces, as well as the dreaded multiple inheritance (which i personally enjoy having at my disposal although never found the need for it). 

with an IVehicle interface. you can then create your 
"Car : IVehicle" 
bool IsLowerThan(int heightInCentimeters);

and do somthing like 
IVehicle car = new Car(400);

on the usage file you invert the responcibility and do 

bool Bridge:CanVehiclePass(Ivehicle vehicle)
{
  return vehicle.IsLowerThan(_heigh);
}

---

Daniel Hardman (2017-05-30 21:03:37)

Good point about solving this problem with interfaces, João. It can totally be done that way, and sometimes that is the better answer.