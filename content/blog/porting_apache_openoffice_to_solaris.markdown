title: Porting Apache OpenOffice (incubating) to Solaris, an interview with Nicolas Christener of Adfinis SyGroup
layout: post
date: '2012-06-18T01:24:10+00:00'
permalink: porting_apache_openoffice_to_solaris

<div align="center"> 
    <p><img src="http://www.robweir.com/solaris.jpg" /></p> 
  </div> 
  <p> </p> 
  <p>The Swiss company Adfinis SyGroup is active in the <a href="http://incubator.apache.org/openofficeorg/">Apache OpenOffice project</a>, contributing the Solaris build, as well hosting an <a href="http://opengrok.adfinis-sygroup.org/source/">OpenGrok index</a> of the OpenOffice source code.&nbsp;&nbsp; The following interview was conducted via email between PMC member Rob Weir (R) and Nicolas Christener of Adfinis SyGroup (N).</p> 
  <p>(Apache OpenOffice is currently undergoing
      Incubation at the Apache Software Foundation.)</p> 
  <p> </p> 
  <p>R: <i>Please tell our readers a little about yourself and Adfinis SyGroup</i>.</p> 
  <p>N:<a href="http://adfinis-sygroup.ch/"> Adfinis SyGroup AG</a> was founded a few months ago as a result of the merge of the two companies (Adfinis and SyGroup). We have two offices in Switzerland (one in Berne and one in Basel) and around 35 employees whereof most of them are engineers.</p> 
  <p>We strongly focus on services around OpenSource technologies and have two departments. The system engineering team builds and operates server and services built on Linux/Unix and the software team develops/customizes applications based on OpenSource.</p> 
  <p>Currently we have five people involved in our work on Apache OpenOffice: David, Denis, Hans, Nicolas and Matthias.<br /> <br />
(In the above photograph, from left to right are: Nicolas, Denis, Hans, Matthias, Dave)</p> 
  <p>R: <i>What got you interested in Apache OpenOffice? &nbsp;Were you involved at all in OpenOffice.org previously?</i></p> 
  <p>N: I started to build OpenOffice.org packages for the Paldo Linux distribution a few years ago and acquired a decent knowledge about the needed steps to get a proper OOo build. This involvement enabled us to make contacts in the OpenOffice community in Switzerland and concluded our first contracts for OOo consulting and engineering. Oracle's end-of-support for OOo enabled us to step in and provide services and support for other customers as well.</p> 
  <p>R: <i>Describe some of the technical work you did to get a successful Solaris port of Apache OpenOffice 3.4?</i></p> 
  <p>N: As the previous builds on Solaris were mostly done by Sun and Oracle the information about this topic were quite sparse. For example, we did not know the exact compiler which was used, we didn't know what flavor of Solaris was used, and it seemed that the people who knew those things disappeared.</p> 
  <p>We decided to start with the latest OOo version, which was released on Solaris, because we knew that this one is buildable on Solaris. With the knowledge we gained during this process, we took a stab at the development version of AOO 3.4 and got a working build quite fast, which was very motivating. Most of the build breakers could be solved by patching the build system (only one modification in the code).</p> 
  <p>As one of our customers uses 3rd-party binary extensions we were concerned to maintain <a href="http://en.wikipedia.org/wiki/Application_binary_interface">ABI</a> compatibility - therefore we used the SolarisStudio compilers for our work. After we delivered a first build to our customer, they reported two major bugs which we had to fix in order to make a deployment on their system possible. It took us some time to find proper solutions for those bugs, but thanks to the great support by the community we were able to fix them and build a new version which seems to work as expected.</p> 
  <p>Finding suitable SPARC hardware is a bit of an issue too. Our current machine runs OpenSolaris 2009.06 - we hope to get better hardware soon which would also be capable of running Solaris 11.</p> 
  <p>R: <i>What items remain before it is complete?</i></p> 
  <p>N: We are currently in the QA phase and wait for a final feedback from our customer. As soon as our customer decides that the build can be used for deployment (&gt;200 workstations, many documents with several hundred or even over thousand pages, Writer is one of the most essential tool in their daily work-flow) we will build AOO 3.4 for all languages and if possible also as Solaris packages (*.pkg).</p> 
  <p>We'll make those builds available for free download and try to do this upcoming versions as well. It is important to us that the Solaris SPARC build stays well maintained. Therefore we'd like to have a continuous/nightly build, where developers can check the build logs in order to see whether their latest check-in works on Solaris SPARC. We are working on providing an official build bot for the project.</p> 
  <p>R: <i>If someone wants to help test this port, where can they find it?</i></p> 
  <p>We upload all our builds to our website:<br /> <a target="_blank" href="http://adfinis-sygroup.ch/aoo-solaris-sparc"></a></p> 
  <ul> 
    <li><a target="_blank" href="http://adfinis-sygroup.ch/aoo-solaris-sparc">http://adfinis-sygroup.ch/aoo-<wbr />solaris-sparc</a><a target="_blank" href="http://adfinis-sygroup.ch/aoo-solaris-x86"></a></li> 
    <li><a target="_blank" href="http://adfinis-sygroup.ch/aoo-solaris-x86">http://adfinis-sygroup.ch/aoo-<wbr />solaris-x86</a><br /></li> 
  </ul> 
  <p>We are also interested in creating official community builds for AOO and would be glad to talk about such opportunities.</p> 
  <p>R: <i>Do you have maybe top three tips for Linux application developers, on things to be careful about, if they want their applications to be more portable?</i></p> 
  <p>N: Especially concerning AOO we would like to point out that many large companies/organizations use software in their data-center (i.e., for thin-clients). In such an environment Solaris/SPARC is still a big player and a great many users depend on well-maintained ports. Therefore these deployments/technologies concern all developers and we encourage everyone to keep in mind:</p> 
  <ul> 
    <li>There are other processors than Intel.</li> 
    <li>There are other operating systems than Windows/Linux/OS X.</li> 
    <li>There are other tool chains than GNU.</li> 
  </ul> 
  <p>Buildbots are a great help to keep up this awareness.</p> 
  <p>Thank you very much for the interview! We would also like to thank Raphael Bircher for his continuous support and the whole community which does a great job in delivering a high quality office productivity suite.</p>
