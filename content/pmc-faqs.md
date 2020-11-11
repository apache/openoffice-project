Title:     PMC FAQs
Notice: http://www.apache.org/licenses/LICENSE-2.0

Here are a number of FAQ's about how the Apache OpenOffice project governance works.

**Contents**

[TOC]

# What is the PMC? # {#pmc}

The Project Management Committee (PMC) is the government of the project. The committee
is responsible for the project and decides what to do and which direction to go.
<br> ([see here for a list of PMC members][1])


# Who is the Admin/Moderator/Owner for X? # {#moderator}

Although Apache projects have few formal roles, there are some technical subsystems
which have admin or similar roles filled by project volunteers. If you have a question
with one of these systems, these are the people you might want to contact first,
before escalating to Apache Infrastructure.

# Resources inside ASF

## Mailing lists

Each mailing list has one or more moderators. See the
[Mailing List page](mailing-lists.html) for how to contact a moderator.
Responsibilities of mailing list moderators include:

- Review messages that have been held for moderation, reject spam posts and allow the
  valid messages through.
- Assist users who are having difficulties subscribing or unsubscribing from the list.
- Provide reports to the PMC on request, on the number of current subscribers.
- For private lists, approve subscription requests for authorized subscribers only.
- When needed, escalate technical issues to Infra and privacy issues to the PMC.

## SVN / Git

All committers have equal access. If you need to do something beyond ordinary commit
rights, such as importing a dump file, [enter a JIRA issue][12] with Apache Infra.

## Confluence, MediaWiki and Forums

Registered users on any of these services generally have equal access.
Contact the admins for these services using the links provided for the service.

## Blog

Blog authors: You must be a committer. To establish a Roller account
[contact Infrastructure][1].

| ID            |  Author #         |
|---------------|-------------------|
| rbircher	|  Raphael Bircher  |
| dpharbison	|  Don Harbison     |
| khirano	|  Kazunari Hirano  |
| alg		|  Armin Le Grand   |
| clippka	|  Christian Lippka |
| jsc		|  Jürgen Schmidt   |
| robweir	|  Rob Weir         |
| orw		|  Oliver-Rainer Wittmann |

Blog admins: Admins authorize new authors once they have first established a Roller
account.

| ID            |  Admin #         |
|---------------|------------------|
| wave		|  Dave Fisher     |
| marcus	|  Marcus Lange    |

## Bugzilla

Admins: Marcus Lange, Rob Weir, Herbert Duerr.

# Resources outside ASF

## [YouTube](https://www.youtube.com/openoffice)

Admins: Matthias Seidel, Peter Kovacs, Kay Schenk

## [Facebook](https://www.facebook.com/ApacheOO)

Admins: Peter Kovacs, Shane Curcuru, Don Harbison, Samer Mansour, Juergen Schmidt,
Rob Weir, (Apache id) imacat

## [Pinterest](https://www.pinterest.de/openoffice)

Admin: Matthias Seidel

## [Twitter](https://twitter.com/ApacheOO)

Admin: vacant (was: Roberto Galoppini)<p>

# How to participate? # {#participate}

First of all you have to think how you want to participate as we have different
kind of roles like user, developer, committer. The easiest way is to use what we
build as user. If you want to improve parts of the software, or documentation,
write to our [mailing lists][2] what should be modified and how it should be done.
On the [community wiki][3] you can just create an account and start to work on it
right away. There is a [Help Wanted][13] page that has ideas for getting started.

The following are conditions to become a committer:

1. You have sent in patches that were well-respected to improve the software.
2. You have added documentation to the Wiki or website that were well-respected to
   improve the non-code part of the project.
3. You have shown that you can discuss in the mailing lists and that this has
   brought us forward.
4. You are well known to the established members, who you are and what you have
   done in the past. Regarding this project, a former-one or another project.

If 1 of the 4 statements above are true, then you can be voted in as committer.

When the vote result is positive, you will be asked for some information to setup
your committer status. [Read the Participation guide for more information.][4]

## I was invited/voted as committer, so what's next?

The following is a brief summary of what to expect as committer:

1. After your (individual Contributor License Agreement ([iCLA][5]) has been
   received and registered, you will be invited to specify one or more preferred
   Apache user names.

   **Important**: <br>
   The e-mail address you provide in your iCLA will be used for the following
   communications with you.

   Please note that there is also a [Corporate Contributor License Agreement
   (CCLA)][6] if you want/have to commit in the name of a company or organization.

2. Choose one or more user name(s) that would be acceptable to you. These are short
   names or abbreviation that will be used for a Unix account login.

   **Example:** <br>
   Your name is "John Doe", so an ID could be "johnd" or "jdoe". [Here you can see
   if the ID is still free][7] or already given to another committer.

   Supply all other information that is requested. Return the ID requests as
   instructed.

3. When your choices are returned, the first request that does not conflict with
   an already-issued ID will be used to generate an Apache ID. Write them in
   the order you would like to have, so the first one is the most wanted.

4. You will receive an e-mail, from "root@apache.org", that confirms the Apache
   user name for you and also provides you with an initial password. There are also
   instructions for changing your password. Please be patient as this mail can take
   some days.

5. The ID will also be your Apache e-mail address. Note that the account will be
   set up to forward all received mails to the e-mail address you supplied on your
   iCLA. It is not a normal mail account but just for forwarding. After you have
   the account there is also a way to associate your Apache e-mail address with
   additional e-mail addresses that you have. (**ToDo**: Add a link to a how-to)

6. The ID and password will allow you to check in changes and new additions on the
   Apache SVN repository for the Apache OpenOffice repository. The ability
   to check in material on the SVN repository is important for more than code. All
   committers will have an use for it.

7. The ID and password will allow you to login to a personal Unix account on the
   Apache server "people.apache.org". You can produce a personal website at this
   account as well as use it as a regular Unix (specifically, FreeBSD) account. You
   do not need to be able to use this account. You may find it useful as you become
   more accomplished as a committer.

8. Being a committer also grants access to some non-public resources and mailing
   lists. There are details in the [private committers SVN tree][8].

See the [Guide for new committers][9] and the [Committers' FAQ][10] for more
information.

# How and when to vote? # {#voting}

Voting is done when a formal decision has to be made or due to legal reasons, e.g.,
to vote in new members as committers. In any case avoid voting as the normal way is
to come to a decision by discussions. The initiator is responsible for the vote,
that means also to count the votes and present the result. Every member has 1 vote.
<br> ([see here for more information][11])

# Information for Release Managers # {#release_managers}

* ASF General Information:
[Publishing Releases](https://www.apache.org/dev/release-publishing.html)
* The Apache OpenOffice dist area svn location containing distribution artifacts and
keys: [https://dist.apache.org/repos/dist/release/openoffice](https://dist.apache.org/repos/dist/release/openoffice).

[1]: https://people.apache.org/committers-by-project.html#openoffice-pmc
[2]: https://openoffice.apache.org/mailing-lists.html
[3]: https://cwiki.apache.org/confluence/display/OOOUSERS/Wiki+Home
[4]: https://incubator.apache.org/guides/participation.html
[5]: https://www.apache.org/licenses/icla.txt
[6]: https://www.apache.org/licenses/cla-corporate.txt
[7]: https://people.apache.org/committer-index.html
[8]: https://svn.apache.org/repos/private/committers
[9]: https://www.apache.org/dev/new-committers-guide.html
[10]: https://www.apache.org/dev/committers.html
[11]: https://openoffice.apache.org/docs/governance/voting.html
[12]: https://issues.apache.org/jira/browse/INFRA/
[13]: https://cwiki.apache.org/confluence/display/OOOUSERS/Help+Wanted
