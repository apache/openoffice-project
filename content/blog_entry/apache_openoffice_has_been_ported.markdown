title: Porting Apache OpenOffice (incubating) to FreeBSD -- Ready to test!
layout: post
date: '2012-02-29T14:52:05+00:00'
permalink: apache_openoffice_has_been_ported

<p>We are pleased to note that NAKATA, Maho and Pedro Giffuni have ported <a href="http://incubator.apache.org/openofficeorg/">Apache OpenOffice</a> to <a href="http://www.freebsd.org/">FreeBSD</a>.&nbsp;&nbsp; The results of their porting effort are now in the FreeBSD <a href="http://www.freebsd.org/cgi/cvsweb.cgi/ports/editors/openoffice-3-devel/">ports tree</a>, so everyone can easily build and use it.&nbsp;&nbsp; FreeBSD users are invited to help test this port and report bugs.<br /> <br /> FreeBSD is a free operating system based on Berkeley's 4.4 BSD source release. The code base has undergone over thirty years of continuous development, improvement, and optimization by large number of individuals. There are approximately 400 FreeBSD committers (those who can commit to the source code repository).&nbsp; Development is especially focused on networking, security, performance and porting applications (they have over 20,000 well-maintained applications).&nbsp; FreeBSD is used as a platform for devices and products from many of the world's largest IT companies, including, Apple, Cisco, Juniper and NetApp.&nbsp; It has broken ftp 
performance records and powers important sites like Yahoo, Hotmail and 
the Apache Software Foundation's infrastructure.<br /> <br />
Historically, the FreeBSD port of OpenOffice has been very active, stable and well maintained.&nbsp; There are the legacy OpenOffice.org 3.3 and 3.4Beta ports, no longer being maintained, and the active version 3.4 port, for ongoing development.&nbsp; Notably, Jung-uk Kim ported to amd64, and fixed many technical 
issues, and Jack Low provided builds until development 
migration to Apache.<br /> <br />
Maho@, Pfg@ and other volunteers are working with each other, and with the Apache OpenOffice project, in this work.&nbsp; The FreeBSD team did not fork.&nbsp; They are working as Apache OpenOffice committers, directly with the Apache project.&nbsp; <br /></p> 
  <p>Technically, porting has not been very difficult.&nbsp; It has required only small, almost trivial patches, since Linux and FreeBSD are 
very similar.&nbsp; MacOSX and FreeBSD also share many similarities which 
has helped improve both ports.&nbsp;&nbsp; Porting to other BSDs would be easy as well,&nbsp; 
since the developers have marked their fixes by adding &quot;FREEBSD&quot; or &quot;BSD&quot; comments in the code, and they wrote up many Bugzilla issues. Many build fixes for other BSDs would be 
same as those needed for FreeBSD's port.<br /></p> 
  <p>Since the OpenOffice project migrated to Apache, upstreaming has become much easier than before.&nbsp; Pfg@ joined the project and has pushed upstream over 30 patches.&nbsp; Currently, Maho@ is concentrating on porting and consulting frequently with Pfg@.&nbsp; Of course, Pfg@ not only pushes patches upstream, but also is actively working on porting.&nbsp; Maho@ will commit directly to Apache's Subversion repository very soon.&nbsp;&nbsp; <br /> <br /> Final words: This is not the end.&nbsp;&nbsp; Maho@ and Pfg@ continue their work on porting.&nbsp; Bug reports are always welcome to {pfg,<a href="mailto:maho%7D@apache.org">maho}@apache.org</a>.&nbsp; And if you are interested in learning more about the FreeBSD port of Apache OpenOffice, you can join our mailing list: office@FreeBSD.org. <br /></p> 
  <p>Finally, please remember that porting to FreeBSD also is a benefit for all OpenOffice users, since it increases the overall portability of the code and provides another valuable testing environment.</p> 
  <p>Thanks, </p> 
  <p>Nakata Maho </p> 
  <p> <img src="https://blogs.apache.org/OOo/mediaresource/bc1d3f35-8a7a-47c6-8b90-3788b71a7e5d" /></p>
