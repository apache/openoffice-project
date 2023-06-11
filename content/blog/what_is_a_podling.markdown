title: Incubation, podling, IP Clearance, oh my!
layout: post
date: '2011-10-18T20:10:51+00:00'
permalink: what_is_a_podling

<a href="https://www.flickr.com/photos/floridamemory/3310996545/" title="Chicken eggs inside a chicken hatchery: Jacksonville Region, Florida by State Library and Archives of Florida, on Flickr"><img src="https://farm4.static.flickr.com/3588/3310996545_44ea9f96fb.jpg" width="400" height="500" alt="Chicken eggs inside a chicken hatchery: Jacksonville Region, Florida" /></a> 
  <h1><font face="arial, helvetica, sans-serif"></font></h1><hr /> 
  <p>The Apache OpenOffice.org project is currently in the incubation phase. We're a 'podling'. It's where all new Apache projects begin, regardless of
how mature your source code base is. In this post I'll attempt to explain a bit about incubation, and a bit about the 'Apache Way', and our current effort to meet the requirements for 3rd party code review and clearance. In future posts, I'll attempt to tackle other aspects of the project. If we all have a better understanding of how the work is becoming organized, those of you interested to volunteer will have a better idea of where to start, and those who are interested to follow our progress will have an easier way to check up on things.&nbsp;</p> 
  <p>First off, a podling is not from
'Invasion of the Body Snatchers' – a human being wrapped up to look
like a large vegetable, or furry cute puppets from the Dark Crystal
Cave of Jim Henson's imagination. It's the term we use here at
Apache to describe the first phase of a prospective project; a podling is a
project that is 'incubating'. Egg,
podling, new thing with promise needing special care and attention. I
think you get the idea.</p> 
  <p>It's that special care and attention
part that is consuming the efforts of the PPMC or &quot;Podling Project
Management Committee&quot; at the moment. If we are going to hatch, 'graduate' to a TLP or &quot;Top Level Project&quot; in Apache-speak, we are required to meet certain criteria evolved out of deep experience accumulated through Apache's 12 year history and its involvement with many other successful projects.</p> 
  <p>Apache defines a podling as “A
codebase and its community while in the process of being incubated.”
You can find the details on the complete <a href="http://incubator.apache.org/incubation/Incubation_Policy.html" title="Apache Incubation Policy">Apache Incubation Policy</a> here.</p> 
  <p>OK, so we have the code base, thanks to
Oracle's decision, and we have a community signed in to the project
already, 75 committers and growing. So where are we with the  process?</p> 
  <p>When do podlings hatch, and become
Apache TLP or Top Level Projects?</p> 
  <p>The abbreviated answer requires the
podling to:</p> 
  <p> </p> 
  <ul> 
    <li>Deliver an official Apache release</li> 
    <li>Demonstrate you have successfully
	created an open and diverse community</li> 
    <li>Follow the 'Apache Way' through
	the process, documenting status, conducting ballots, maintaining a
	fully open and transparent process, etc.</li> 
  </ul> 
  <p> </p> 
  <p> </p> 
  <p>OpenOffice is a very large chunk of
code, many millions of lines of code. The PPMC has now successfully
migrated all the source files into the Apache infrastructure nestled
into its new nest within the Apache Subversion repository
environment. We've run a build test on Linux and we know we've got
the code we need to begin to build a release. 
</p> 
  <p> </p> 
  <p>But wait, before we can meet the requirement of producing an official release, Apache requires that we conduct a thorough&nbsp;<a href="http://incubator.apache.org/ip-clearance/index.html" title="IP or Intellectual Property review and clearance process.">IP or Intellectual Property review and clearance process</a>. This means that the resulting Apache
release may be licensed under the Apache License 2. It requires
that all...</p> 
  <blockquote style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 40px; border-top-style: none; border-right-style: none; border-bottom-style: none; border-left-style: none; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; " class="webkit-indent-blockquote"> 
    <p>“incoming code
is fully signed off before any release. This simply reinforces the
Apache requirements: all code must have appropriate licenses....The
process of preparing an <a href="http://incubator.apache.org/guides/releasemanagement.html#rules" title="Apache release">Apache release</a> should include an audit of the code to
ensure that all files have appropriate headers and that all
dependencies complies with Apache policy.</p> 
  </blockquote> 
  <p>This means that the resulting Apache
OpenOffice release(s) will provide the maximum opportunity for the
development of a broader spectrum of OpenOffice derivatives than we
see today. The OpenOffice of the past, will look very different in
the future as more developers become familiar with the code, and see
new opportunities not previously available.&nbsp;<span style="font-family: arial, verdana, 'Bitstream Vera Sans', helvetica, sans-serif; font-size: 16px; font-weight: bold; "> </span></p> 
  <p>Right now, our
immediate task is to resolve the licensing incompatibilities for 3<sup>rd</sup>
party code modules used by OpenOffice. Since Oracle did not possess
the copyright for these modules, they were not included in the original Oracle Software Grant Agreement, and therefore we are working to either
deprecate, or find a replacement that may be used either as a binary
file or an alternative source file that fills the function needed.
We're confident that the process will be concluded in the next weeks,
but it is detail-oriented work, and must be done thoroughly and
correctly in order to clear the path for an official podling release
of Apache OpenOffice.</p> 
  <p>Before we can produce an Apache release, we must complete the code clearance step, ensuring that the license headers include License and Notification files for all
artifacts in the build be done to the satisfaction of the PPMC
and the Incubator PMC which governs the Apache OpenOffice podling. This will clear the way forward to develop a realistic target date for issuing our first 'Apache OpenOffice.org' release&nbsp;</p> 
  <p>In future posts, I'll sketch out
how the project is being organized, mapping out the areas that offer
interesting and exciting opportunities needing new volunteers to step
up and take on. &nbsp;</p> 
  <p>- Don Harbison, PPMC Member, Apache OpenOffice.org </p> 
  <p> </p>
