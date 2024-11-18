---
title: Why Cannibalism May Be Smart Business
date: 2012-10-05
slug: why-cannibalism-may-be-smart-business
---

Get out your fork. I've got a story for you...

<figure><img title="fork, meat" src="http://farm3.staticflickr.com/2282/2362260782_c834e5bc13_n.jpg" alt="" width="240" height="320" /><figcaption>Dig in. Don't hold back. Photo credit: AleBonvini (Flickr)</figcaption></figure>

At the beginning of 2005, Symantec acquired Veritas. Together, Veritas's <a class="zem_slink" title="Backup Exec" href="http://www.symantec.com/backupexec/" rel="homepage" target="_blank">BackupExec</a> and NetBackup products accounted for something like 70-80% of the world's enterprise backup market. As I recall, BackupExec had annual sales of around $600M, and NetBackup was similar.

I worked for the only technology group within Symantec that overlapped the backup space at the time. We were making a disk-based backup product named LiveState Recovery; its revenues were in the tens of millions of dollars and we were growing at >100% <a class="zem_slink" title="Compound annual growth rate" href="http://en.wikipedia.org/wiki/Compound_annual_growth_rate" rel="wikipedia" target="_blank">CAGR</a>.

<strong>Integration gets hairy</strong>

Our growth stemmed from the fact that we were approaching backup in a radically different way. Instead of capturing changed files and streaming them through a centralized media server to a tape library, we took <a class="zem_slink" title="Disk image" href="http://en.wikipedia.org/wiki/Disk_image" rel="wikipedia" target="_blank">disk images</a> based on snapshotting technology. We were faster (many times faster, often); we had a distributed architecture that scaled out much more easily; we never missed a bit; we captured application state perfectly; we could mount backups or convert them to virtual machines.

As the acquisition finalized, Symantec charged us and the BE folks <!--more-->to devise a coherent market strategy. The instructions were a no-brainer, but the details were messy. The product management folks with Veritas heritage didn't put much stock in our upstart product line; our revenue was smaller than some of BE's optional upsells. They decided that our disk-based product would become another BE option; that way, BE would get to claim immediate victory in the disk-based backup space.

<strong>Fear of cannibalism</strong>

I thought this was unwise. Sales was trained and incented to sell traditional BE, and marketing was trained to talk about traditional BE to the market. Rolling disk-based backup support into BE would make our innovation almost invisible. Our dev team would be starved for investment dollars, and sales would dry up. When I raised my concern and argued for a different strategy based on our CAGR, PM shot back: "That growth isn't coming from a vacuum; it's coming from cannibalizing <em>our</em> [BE] revenue! Do you want to undercut a revenue titan, and market some upstart product instead? It'll create market confusion. We should spend our money and energy where the biggest bucks are."

This analysis sounded fairly rational. Many in the higher echelons of management bought it. But it missed a critical insight:<em> If Symantec's upstart backup product didn't cannibalize BE's revenue, competitors would.</em> A market upswell was underway; Symantec could surf or paddle foolishly away, but the wave was coming regardless.

Our team advocated strongly enough that we got a compromise of sorts. Disk-based backup adopted the BE brand, and "BackupExec System Recovery" (BESR) was born. The teams and codebases remained somewhat independent.

However, my concerns about sales and marketing misalignment proved well-founded. A year or two after the transition, BESR was growing at 10% per year instead of 100%, even though competitors like Acronis and StorageCraft were growing by leaps and bounds. We didn't have the market momentum and corresponding dev funding to pursue critical initiatives like cloud integration. The product began to starve. Ultimately dev work was shipped overseas and the team that built BESR was laid off. I don't know exactly what BE revenues are today, but I suspect growth is pretty flat, and <a href="http://www.wired.com/cloudline/2012/08/cloud-backup-vendors/" target="_blank">seriously threatened by virtualization and cloud</a>. Traditional backup isn't quite irrelevant, but it's getting there...

<figure><img class="  " title="traditional backup gets long in the tooth" src="http://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Disruptivetechnology.gif/634px-Disruptivetechnology.gif" alt="" width="444" height="336" /><figcaption>Virtualization and cloud are disruptive technologies for traditional backup. Result: traditional backup gets displaced at higher and higher bars of functionality as you move right. Image credit: Megapixie (Wikimedia Commons).</figcaption></figure>

<strong>The moral</strong>

The metaphor of cannibalism is apt. If you had a visceral "yuck" reaction to my fork comment... well, business people have a visceral "yuck" reaction to anything that endangers a current revenue stream. And they should. We wouldn't have much of an economy if we failed to protect the value of business investments.

However...

I am satisfied that the essence I've given here is true: in business, fear of cannibalism is frequently irrational. Cannibalism happens with change, and change is unavoidable. If you have two products, and A is truly cannibalizing B's revenue, then <em>the market is sending you a signal</em>: A has value over B for at least a segment of your customer base. Ignore that signal at your peril; heed it with discipline (and some savvy maneuvering, not to be underestimated), and you'll end up with a full stomach.

Even if the process is a bit grisly.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Examine your current product through the lens of disruptive innovation (described by <a class="zem_slink" title="Clayton M. Christensen" href="http://www.claytonchristensen.com" rel="homepage" target="_blank">Clayton Christensen</a> in The <a class="zem_slink" title="Disruptive technology" href="http://en.wikipedia.org/wiki/Disruptive_technology" rel="wikipedia" target="_blank">Innovator's Dilemma</a> and graphed above). Are you new and disruptive, long-in-the-tooth, or somewhere else? What does this suggest about wise strategy?</span></em></p>



---

Daniel (2012-10-06 01:01:32)

Thanks for the extra detail, Dano. You're quite right to include GSS and Continuous Protection. For that matter, the products from Waltham, though focused on systems mgmt, also had some interesting application in the backup space.

The history of BE and BESR (and of the SEA business unit before that) has some frustrating parts, and this is one of them. But it also has some happy parts. I had the chance to work with many talented, hard-working people (from all backgrounds, not just on my own team), and I learned a lot.

---

Dano (2012-10-05 17:40:54)

Daniel,

It actually was worse than that.  The SMB product line was in total disarray and when I got involved with this shortly after 2006 our Sr VP was trying to create unique solutions for 5 backup products and how to Market and Sell then without disrupting the current revenue streams.

The products at the time were NBU, BE, GSS, LSR (BESR), and the complementary products for Continuous Protection for both server and desktop.

This was a marketing nightmare! More time and market research should have been spent leveraging the markets needs.  There was a ton of money out there to made, but we didn't have the infrastructure in place to go after the SMB MID markets.  We couldn't sell in there and we couldn't support it if we sold it there thus without a proper plan we have failure.

BESR was a solid product and had a image market all to it's own that was different than the rest of Symantec's product line.  Yes Symantec/VERITAS products that were also good and solved many problems, but executive management didn't know how to handle the overlap when it came to the image technology and traditional backup which made some very bad decisions.

From 2001 - 2012 I seen the demise of many good backup products produced by Symantec/VERITAS and I have told this story to anyone who had an ear to hear.

I could go on and on, but I'd rather say thank you for speaking up.

Dano



