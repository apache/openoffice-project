Title:     Infrastructure
Notice: http://www.apache.org/licenses/LICENSE-2.0

In this Orientation Module you will learn about tools and servers that are part of the daily operations of the project. You will interact with many of these on a regular basis, or at least hear them discussed on the lists, so it is important to know what they are, and where to go if you need more information or run into problems.

1. First, Please send an email to [recruitment@openoffice.apache.org](mailto:recruitment@openoffice.apache.org?subject=Starting%20Infrastructure%20Module) to let us know you are working on this module.

1. List of tools and services we use

   * ezmlm: This is the time-tested EZ Mailing List Manager application that manages our mailing lists. You control ezmlm by sending commands to a list address. For example, if the list address is dev@openoffice.apache.org then you subscribe to the list with the command dev-**subscribe**@openoffice.apache.org. Some other popular commands are listed [here](https://www.apache.org/foundation/mailinglists.html). You can get a full list of commands available to you by sending the *help* command, as in dev-**help**@openoffice.apache.org. Each list has moderators who have additional capabilities. You can find the moderators for our lists [here](/pmc-faqs.html#mailing-lists).

   * Our two websites: [www.openoffice.org](https://www.openoffice.org) and [openoffice.apache.org](/). Why two? There is some logic here, although it is not perfectly executed (yet). The www.openoffice.org website is our primary user-facing website. It is where we put content intended for end-users to use, so downloads, product documentations, support and other related materials. The openoffice.apache.org website, on the other hand, is the main portal for project members, the contributors to the project. We run the project on openoffice.apache.org, and the www.openoffice.org website is a service we provide to users.

   * MediaWiki (also called MWiki) is used for the wiki on the [wiki.openoffice.org](https://wiki.openoffice.org/wiki/Main_Page) website. We use MWiki for many of the user-facing pages on the website, especially in the areas of documentation and support. If you are familiar with Wikipedia and the syntax used for authoring articles there, then you will find our MediaWiki very easy to use, since Wikipedia also uses MediaWiki. If you are new to MediaWiki please read over this [introduction to the basics](https://meta.wikimedia.org/wiki/Help:Editing).

   * Confluence Wiki (also called CWiki) is used for some [project management webpages](https://cwiki.apache.org/confluence/display/OOOUSERS/Wiki+Home)

   * [Pootle](https://translate.apache.org) is our translation management server, an online service used by translators to translate the UI and help files of OpenOffice into various languages. Unless you are involved with translations or builds you probably will never use Pootle. But you will hear it mentioned on the mailing lists.

   * **OBSOLETE** Apache CMS (Content Management System) is the software that manages our websites, including the application of side-wide templates used to apply, for example, the common page footers that occur on each page). There is a web interface to the Apache CMS that makes it easy to make small updates to a page. If you are interested in adding or editing the website you can watch this video on the [Apache CMS's Anonymous Mode](https://www.youtube.com/watch?v=7fvg1pfHLhE) now. Otherwise this is a valuable skill you can pick up later.

   * **OBSOLETE** Subversion is the Version Control System (VCS) used by the project. Subversion is also its own Apache project. The source code for the OpenOffice product as well as the files for the websites are all stored in Subversion. Developers use Subversion heavily in their work. Advanced work in QA and bulk website changes also involve using Subversion.

   * phpBB is the software that runs our [Community Forums](https://forum.openoffice.org/en/forum/), used for technical support of our users.

   * [Bugzilla](https://issues.apache.org/ooo/) is used to track defect OpenOffice (bug) report.

   * [JIRA](https://issues.apache.org/jira/) is another issue tracking application. Some Apache projects use JIRA instead of Bugzilla. We mainly use JIRA when we need to raise an issue with another group at Apache that uses JIRA, for example the Apache Infrastructure Team.

1. It is important to understand the role of the [Apache Infrastructure Team](https://www.apache.org/dev/infrastructure.html) (Infra or Infra@. The Infrastructure team are essentially the system administrators for all Apache-wide servers and services, including many of the services described above. As you can imagine, with all the projects that are part of Apache, this is huge job. In order to support this number of projects and provide good service levels in this shared infrastructure environment, we align ourselves with the common services that are made available to other projects. In other words, we have a "menu" of services that we can enable for the project, and the ability to do some customization, within defined bounds, but we cannot easily use a service outside of that menu.

1. What to do if you have a problem:

   * Questions on how to use the service: First, look for instructions on the website. If that fails, post a note to the dev mailing list for hints.
   * Outages: [Current status](https://monitoring.apache.org/status/) is posted. You might also want to subscribe to Infra's [Twitter feed](https://twitter.com/infrabot). If you see an outage not noted there already, you can notify Infra via IRC channel #asfinfra on Freenode.
   * Requests to enhance or modify the service: Propose something on dev. Even though Infra is required to carry out some tasks, you still should get consensus first on the project's mailing list.

1. Congratulations! You have completed this Module. Please send a note to [recruitment@openoffice.apache.org](mailto:recruitment@openoffice.apache.org?subject=Completed%20Infrastructure%20Module) so we all know you have completed this level. This is also a good opportunity to send along any feedback or questions you might have on this Orientation Module.
