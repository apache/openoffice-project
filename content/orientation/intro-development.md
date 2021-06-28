Title:     Introduction to Development
Notice: http://www.apache.org/licenses/LICENSE-2.0

## Introduction

In this orientation module you will learn how to get started programming OpenOffice.

To complete this module, read through the material on this page, including the linked references. There will also be some start-up tasks for you to perform, such as signing up for an account in our defect tracking database.

Your first task is to subscribe to our Recruitment mailing list. You can subscribe by sending an email to [volunteer-subscribe@openoffice.apache.org](mailto:volunteer-subscribe@openoffice.apache.org).

Then you can introduce yourself by [sending an email to the list](mailto:volunteer@openoffice.apache.org?subject=New Dev Volunteer). We'd love to hear who you are, where you are from, what your background is, etc. Also as you work through the items on this page, if you have questions or problems, please feel free to ask for help by sending a note to this same list.

Note: In parallel with the Dev-specific items on this page, you may want to also review the [Level 1 and Level 2 Orientation Modules](http://openoffice.apache.org/orientation/index.html). They have useful background information on The Apache Way, mailing list etiquette, decision making in the project, etc. A quick review is a good idea, especially if you are new to working in Apache-style open source projects.

Now with the introductions out of the way, let's get started!

## OpenOffice Development: Good, the Bad and the Ugly

Let's be honest. The size, age and complexity of OpenOffice's C++ codebase makes coding a challenge. This is not a trivial codebase to learn. But if you like a good challenge then you'll love this project! There are tasks suitable for programmers with a range of programming experience, and we have many veteran OpenOffice hackers in the project who are happy to answer your questions.

And in its favor, there are few other programs that you can help develop, that have the reach of OpenOffice. Many millions of users depend on OpenOffice, with another half a million downloads every week, from almost every country in the world. So the work you do, the bugs you fix, the features you add, will benefit millions of users around the world.


## Building OpenOffice

It all starts by establishing a local build environment. Building OpenOffice on Linux or Mac is relatively easy, but expect the first attempt to require some trial and error. Every configuration is slightly different.

Building on Windows is more complicated, due to the need to install more prerequisite tools.

Our [Building Guide](https://wiki.openoffice.org/wiki/Documentation/Building_Guide_AOO) on the wiki is your starting point. Follow the instructions there, step by step. Ask questions on the dev list if you get stuck. If you get an error it can be useful to search our [mailing list archives](https://markmail.org/search/+list:org.apache.incubator.ooo-dev) to see if it is a known problem with a known solution.

Note also the current list of configuration flags used in building the development snapshot builds at the bottom of the [development snapshot builds page](https://cwiki.apache.org/confluence/display/OOOUSERS/Development+Snapshot+Builds#DevelopmentSnapshotBuilds-AOO3.4.1).
Although there are many other combinations of flags you can use, some of which are very useful for development, the flags on that page are what we use in our official releases.

Once you have a successful build, [post a note to the dev list](mailto:dev@openoffice.apache.org?subject=Successful 1st Build!) for some well-earned congratulations!

## Orienting Yourself

A few suggestions to help you find your way around this massive codebase:

  - An explanation of the purpose/function of the various [source directories](https://wiki.openoffice.org/wiki/Source_code_directories)
  - We have an [instance of Atlassian Fisheye](https://fisheye.apache.org/changelog/openoffice) which can be useful for browsing the code base and understanding dependencies.

## Finding Easy Tasks

As a new developer you will want to find some easy coding tasks. These are tasks that generally can be done with good C++ skills, but do not require comprehensive knowledge of how OpenOffice is put together. The tasks are more localized. By doing easy tasks you gain experience and confidence hacking with the code base.

We use a [Bugzilla issue tracker](https://bz.apache.org/ooo/) to track reported defects in OpenOffice. Some of us also use Bugzilla for tracking feature and enhancement tasks as well. The value of tracking all coding-related tasks in Bugzilla is that it helps our QA volunteers know which areas to test. Whether code was changed to fix a bug or enhance a feature -- the QA impact is pretty much the same.

If you have not done so already, please [sign up for a Bugzilla account](https://issues.apache.org/ooo/createaccount.cgi). This will allow you to enter new bugs or tasks, but also assign yourself existing ones.

Many tasks are classified in the "difficulty" field. The ones classified as "easy" or "simple" (one level harder than "easy") are good ones to start with. You can find these with the [easy-hacks](https://issues.apache.org/ooo/buglist.cgi?f1=cf_fix_difficulty&o1=equals&resolution=---&query_format=advanced&v1=easy&list_id=42478) and [simple-hacks](https://issues.apache.org/ooo/buglist.cgi?f1=cf_fix_difficulty&o1=equals&resolution=---&query_format=advanced&v1=simple&list_id=42478) queries.

Once you pick a bug and assign it to yourself, you might want to post a note to the dev list, letting us know. We might have some helpful hints to get you started.

## Coding Standards

For reference note the following coding standards for the project:

  - [Coding Standards](https://wiki.openoffice.org/wiki/Coding_Standards)
  - [Writer/Code Conventions](https://wiki.openoffice.org/wiki/Writer/Code_Conventions)

The Geneva Convention prevents us from forcing you to read all of those rules, but know that they are there, and when your code is reviewed your reviewer might refer to some of those rules if there is an issue. So you'll absorb them over time.

## Submitting Patches

As you read in the [Introduction to Contributing to OpenOffice module](https://openoffice.apache.org/orientation/intro-contributing.html), contributors who have demonstrated merit via their project contributions can be voted in as Committers. Committers have the ability to check code into project's source control. Contributors who are not (yet) Committers must submit their patches and have them be reviewed first.

Please review these [guidelines for submitting patches](https://openoffice.apache.org/svn-basics.html#creating_and_submitting_patches). A good practice is to attach the patch to the Bugzilla issue and then send a link to the issue to the Dev list, asking for someone to review and commit the patch.

##Other Useful Resources

  * The [OpenOffice.org for Developers](https://www.openoffice.org/development/) web area has useful information for getting started.
  * The [OpenOffice.org Development Wiki Area](https://wiki.openoffice.org/wiki/Development) has a lot of good general development information.
  * The [commits mailing list](https://openoffice.apache.org/mailing-lists.html#commits-mailing-list) echos every checkin made to the code base. Developers are encouraged to subscribe so they are aware of other changes, and can help review.

## Module Completion

Once you have completed this Module, go to our our [Directory of Volunteers](https://cwiki.apache.org/confluence/display/OOOUSERS/Directory+of+Volunteers) wiki page and add or update your information. Congratulations! Please send a note to [volunteer@openoffice.apache.org](mailto:volunteer@openoffice.apache.org?subject=Completed Introduction to Development) so we know.
