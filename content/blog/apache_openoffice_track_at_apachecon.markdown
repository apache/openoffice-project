---
layout: post
title: 'Apache OpenOffice track at ApacheCon: Day 2'
date: '2012-11-08T14:41:05+00:00'
permalink: apache_openoffice_track_at_apachecon
---
<p>Here are a few selected topics from Day 2 of the Apache OpenOffice track at <a href="http://www.apachecon.eu/">ApacheCon Europe</a>.</p> 

<p><em>For full coverage, see the reports from <a href="http://s.apache.org/openoffice-aceu2012-day-1">Day 1</a> and <a href="http://s.apache.org/openoffice-aceu2012-day-3">Day 3</a>.</em></p> 

  <h3>OpenOffice in the cloud: online version</h3> 
  <p>Judging by the number of questions made during the presentation and by the number of &quot;new&quot; faces in the audience, the star of Day 2 at the Apache OpenOffice track in ApacheCon Europe was Jian Hong Cheng and Fan Zheng's presentation about &quot;Cloud Apache OpenOffice Based on HTML 5&quot;. The prototype implementation shown during the presentation relies on a &quot;headless&quot; instance of Apache OpenOffice that runs on a remote server, listens to the actions the user performs in the browser, and provides XML snippets in response, which are in turn rendered in the browser. Although the code is still at an early stage, this is an exciting development! Many Apache folks attending the session provided feedback and suggested technologies, so this looks like a project where Apache OpenOffice can benefit from input from the Apache community at large.</p> 
  <div align="center"> 
    <p><a target="_new" href="http://www.slideshare.net/pescetti/cloud-apache-openoffice-based-on-html5"><img src="http://people.apache.org/~pescetti/roller/20121107/cloud.png" /></a></p> 
  </div> 
  <p>In related news, the presentation by Xiu Li Xu, Kejia Ye, qi hui, Shenfeng Liu, DaLi Liu focused on how to <a href="http://www.apachecon.eu/schedule/presentation/48/">integrate OpenSocial with Apache OpenOffice</a> to accelerate the content sharing and support the business in cloud. Two social extensions for Apache OpenOffice were demonstrated. These improvements will already be implemented in Apache OpenOffice 4.0, coming in early 2013.</p> 
  <h3>Bashing Apache OpenOffice for a good cause</h3> 
  <p>A series of talks today had a peculiarity in common: they were all highly critical of specific technical features of Apache OpenOffice. But they did it for a good cause: these parts have recently been improved, or will be soon, in the undergoing major effort towards a more maintainable code base, offering easier entry points to developers but preserving the current stability of the code:</p> 
  <ul> 
    <li>Andre Fischer <a href="http://www.apachecon.eu/schedule/presentation/50/">destroyed the current slide show functionality</a> with a great talk on how we can achieve smoother, eye-pleasant animations in Apache OpenOffice Impress. As he put it, currently &quot;Impress... doesn't&quot;, but a proper redesign will allow a better integration of video and audio and direct support for 3D effects. Andre concluded his presentation by showing an experiment of smooth video playing with on-the-fly 3D transformations.</li> 
    <li>Herbert Duerr <a href="http://www.apachecon.eu/schedule/presentation/70/">pointed out the opportunities with platform integration</a>: the issues we are now having with system integration require work on many areas, including 64-bit ports and multi-threading. And the Apache OpenOffice code is written at a level that makes some basic system integrations difficult, but support for specific features such as some &quot;gestures&quot; in Mac OS X is coming in 4.0.</li> 
    <li>Pedro Giffuni showed how <a href="http://www.apachecon.eu/schedule/presentation/54/">outdated dependencies were making the early Apache OpenOffice code unnecessarily complex and easy to break</a>. The &quot;IP clearance&quot; period, one of the first actions taken during incubation, allowed to get rid of useless dependencies and to replace some outdated code, while preserving the previous functonality and stability and making ports (like the FreeBSD port) easier.</li> 
    <li>Dwayne Bailey, one of the main <a href="https://translate.apache.org/projects/OOo_34/">Pootle</a> developers, and Juergen Schmidt made a comprehensive analysis of what can be improved in Pootle and in the Apache OpenOffice localization process respectively. The new Pootle will include an easy-to-use AJAX interface and direct support for translation memories and suggestions. Dwayne will be looking into extending Pootle with functionality useful for a new, simplified localization process currently in early stages of development at Apache OpenOffice. It is worth noting that the Apache OpenOffice repositories already support more than 100 languages, but only 20 are released since the project policy is to release only complete translations. Version 4.0 is already scheduled to be released in at least 8 new languages and we welcome <a href="http://incubator.apache.org/openofficeorg/translate.html">translation volunteers</a> for other languages.</li> 
  </ul> 
  <div align="center"> 
    <table> 
      <tbody> 
        <tr> 
          <td><a href="http://people.apache.org/~pescetti/roller/20121107/andre-1024.jpg" target="_new"><img src="http://people.apache.org/~pescetti/roller/20121107/andre-320.jpg" /></a></td> 
          <td>Andre demonstrating his work on real-time video rendering in Impress: impressive!</td> 
        </tr> 
        <tr> 
          <td><a href="http://people.apache.org/~pescetti/roller/20121107/herbert-1024.jpg" target="_new"><img src="http://people.apache.org/~pescetti/roller/20121107/herbert-320.jpg" /></a></td> 
          <td>Herbert explaining support for mobile devices</td> 
        </tr> 
        <tr> 
          <td><a href="http://people.apache.org/~pescetti/roller/20121107/juergen-1024.jpg" target="_new"><img src="http://people.apache.org/~pescetti/roller/20121107/juergen-320.jpg" /></a></td> 
          <td>Juergen showing the many languages we support in Pootle (the source code has even more); only a few dozens are at 100% and thus conform to the Apache OpenOffice release policy</td> 
        </tr> 
      </tbody> 
    </table> 
  </div> 
  <h3>Community activities</h3> 
  <p>Several talks mentioned how Apache OpenOffice can better integrate with the Apache community at large: opportunities for cooperation are huge and we definitely look forward to exploiting them.</p> 
  <p>And those who still had energy after a full day of talks gathered just before dinner for a community panel. A lot of ideas came out of the group, including: creating a new entry point for Apache OpenOffice press requests, welcoming requests in different languages; getting Apache OpenOffice published in App Stores; packaging Apache OpenOffice for the most common (or all!) GNU/Linux distributions; setting goals for version 4.0, like doubling the number of supported languages.</p> 
  <p>You can see a 3D rendering of the group here (courtesy Andrew Rist): <a href="http://360.io/LWdsMb">http://360.io/LWdsMb</a> ; if you are curious to know who's who, in the flat version at <a href="http://360.io/LWdsMb/f">http://360.io/LWdsMb/f</a> you see (left to right): half Juergen, Oliver, Andrea, Mechtilde, Herbert, Caroline, imacat, Christoph, Michael, Svante, Dwayne, Pedro, Andre, Rony, empty, Svante again (!), Armin, half Juergen.</p>
