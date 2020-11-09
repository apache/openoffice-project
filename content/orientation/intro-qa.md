type=page
title=Introduction to QA
notice=https://www.apache.org/licenses/LICENSE-2.0
~~~~~~
## Introductions

In this orientation module you will learn how Quality Assurance is done in our community. You will also learn about basic tasks that are easiest to do for new QA Volunteers.

To complete this module, read through the material on this page, including the linked references. There will also be some start-up tasks for you to perform, such as signing up for an account in our defect tracking database.

Your first task is to subscribe to our QA mailing list and to introduce yourself to the other QA volunteers. You can subscribe by sending an email to [qa-subscribe@openoffice.apache.org](mailto:qa-subscribe@openoffice.apache.org). 

Then you can introduce yourself by [sending an email to the list](mailto:qa@openoffice.apache.org?subject=New QA Volunteer). We'd love to hear who you are, where you are from, what your background is, etc. Also as you work through the items on this page, if you have questions or problems, please feel free to ask for help by sending a note to  this same list.

Note:  In parallel with the QA-specific items on this page, you may want to first review the [Level 1 and Level 2 Orientation Modules](http://openoffice.apache.org/orientation/index.html) as well. They have useful background information on The Apache Way, mailing list etiquette, decision making in the project, etc. A quick review is a good idea, especially if you are new to working in Apache-style open source projects.

Now with the introductions out of the way, let's get started with the QA!

## The Purpose of QA

Our goal is to maintain and improve the quality of Apache OpenOffice. We primarily accomplish this by finding defects (bugs) in the product before it is released to the general public. The defects are found by a combination of manual and automated tests that we perform on pre-release builds of OpenOffice. We also review and try to reproduce 
defects reported by end-users and submitted to us.

Since OpenOffice is a core software application for millions of users, the role of QA is critical. Although our programmers are wonderful, talented and very experienced, they do make mistakes. Our task is to find these mistakes, report, prioritize them, and verify the fixes when they are made.

QA is a discipline with many best-practices related to process and methodology, tools, techniques and theory. Although professional QA practitioners are welcome in this project, we are also happy to welcome those with no prior experience, or those who are learning about QA, perhaps as a possible career. Aside from the satisfaction of improving the Apache OpenOffice product, you can learn or practice new skills.

## Why Help with QA?

As a volunteer why would you want to help with OpenOffice QA?  A few things to consider:

  - We're a fun, international group of testers, of a range of skills and experience, dedicated to free software and making OpenOffice a high quality choice for users.
  - This is a good way to learn about QA and get some practical experience. This is useful, for example, if you are thinking about Software Quality Engineering (SQE) as a possible career choice.
  - Helping as a tester is a good way to "give back" to the open source community in a way that makes a direct difference in the product, but doesn't require programming skills.
  - It is a good way to raise the visibility of bugs in your particular interest area. For example, maybe you personally are concerned about bugs that cause problems on the Mac, or bugs that impact color blind users, or bugs related to bidirectional text. Participating on the QA team is a good way to ensure that areas of personal interest are adequately tested.
  - We have tasks for volunteers with a range of skills. From novices who can help with manual testing and fix verifications, to experts who can help with our test automation framework, we have a full range of QA activities.
  - As an extremely popular open source product, with many millions of users, there are opportunities here to do some new and exciting things on the QA front, including possibilities of crowd sourcing some kinds of testing.

## QA Activities

QA activities within the Apache OpenOffice project include:

  - Reviewing incoming bug reports from users to see if the reported issues can be reproduced
  - Verifying bugs that the developers say they have fixed, to confirm that they actually have been fixed
  - Testing new builds of OpenOffice against a functional test plan
  - Defining new test cases
  - Running automated regression tests
  - Specialized tests in areas such as performance, accessibility, localization, security, etc.
  - Analyzing defect reports to gauge how we are doing, in terms of quality level, defect find and fix rates, etc.
  - Reporting summary defect data and recommending whether a give build of OpenOffice has reached a sufficient quality level for release.
  - Making recommendations for improving product quality and testing effectiveness.

## Skills Wanted

The skills we need on the QA team include:

  - Familiarity with OpenOffice as a user.
  - Attention to detail. In QA we find the bugs that the developers missed. And our developers are pretty good.
  - Access to a Windows, Mac or Linux machine for testing
  - Good written communications
  - Interest, enthusiasm and teamwork.
  - Ability to volunteer at least 2 hours/week, on average.

QA is as much an attitude as it is a skill set. A tester likes solving puzzles, likes a methodical approach, likes the challenge of finding an elegant way to reproducibly break software.

## Mailing List

As mentioned above, QA volunteers need to subscribe to our dedicated QA mail list.

The mailing list is for bug reports, quality assurance for release, beta tests, manual test, automated tests, etc. This is where the QA community coordinates its activities.

Subscribe: [qa-subscribe@openoffice.apache.org](mailto:qa-subscribe@openoffice.apache.org)<br>Post (after subscription): [qa@openoffice.apache.org](mailto:qa@openoffice.apache.org)<br> Unsubscribe: [qa-unsubscribe@openoffice.apache.org](mailto:qa-unsubscribe@openoffice.apache.org)

Archives:

  - [Markmail](http://markmail.org/search/+list:org.apache.incubator.ooo-qa)
  - [Apache](http://mail-archives.apache.org/mod_mbox/openoffice-qa/)

We use the following special subject tags to identify QA activities:

 * [QA REPORT] - topic related with  status report
 * [QA AUTOMATION] - topic related with automation tools, scripts and scope
 * [QA BUG] - topic related with bug discussion
 * [QA CRITICAL] - important information related with QE
 * [QA CALLFORREVIEW] - topic with some review
 * [QA CALLFORVOLUNTEER] - if you want to call for volunteer for testing some features
 * [QA] default if others don't fit. 

After you subscribe QA mail list then you can post your topic in the mail group.

## Apache OpenOffice Test Builds

Since our job is to find bugs in OpenOffice, we must run pre-release builds that contain many bugs. These bugs could be major or minor. They could include document corruption bugs, crashes, even (in rare cases) bugs that could make your system unstable. So QA volunteers generally try to separate their QA work from their normal desktop activities. You don't want to write your thesis on a test build!

Some volunteers simply use two machines: one dedicated to their testing work. If things become unstable they can then reinstall the operating system and start fresh.

A more sophisticated approach is to use virtual machines, which can work quite well. [VirtualBox](https://www.virtualbox.org) is a popular virtualization package.

Feel free to ask questions on the QA list about effective ways to manage a test environment.

Once you have your test environment set up, you need to download and install the latest OpenOffice build.

  - [AOO nightly build](http://ci.apache.org/projects/openoffice/index.html) are built each night and are our "rawest" builds, with many possibilities for finding new bugs.
  - [Snapshot builds](http://ci.apache.org/projects/openoffice/index.html), (tagged with the word "Snapshot") are made weekly against a code branch that is being considered for a release candidate.

## Bug Handling

Apache Bugzilla is where we track defects:

 * [https://bz.apache.org/ooo/](https://bz.apache.org/ooo/)

Bugzilla related documents:

 * Bug lifecycle introduction [Issue Lifecycle](http://wiki.openoffice.org/wiki/Issue_lifecycle)<br>
 * A guide for reporting a new bug: [How to file bug](http://wiki.openoffice.org/wiki/QA/HowToFileIssue)

Bugzilla related mailing list:

 * [issues@openoffice.apache.org](http://markmail.org/search/+list:org.apache.incubator.ooo-issues). Actvity on issues goes to this mailing list.

Everyone in QA needs a Bugzilla account, which you can get [here](https://bz.apache.org/ooo/createaccount.cgi). Once you have a Bugzilla account, you should send a note to the QA list asking to be added to the "qa-team" group in Bugzilla. This will give you some additional permissions in Bugzilla. Include your Bugzilla login ID in your request.

## Easy QA Task: Confirm New Defect Reports

Most new volunteers start by reviewing incoming defect reports and attempting to "confirm" them. The defect reports are often from users and are often not very clearly written. You learn to "read between the lines" and ask the user clarifying questions in order to turn the raw report into a reproducible defect that the developers can debug and fix.

You can get a list of unconfirmed defect reports with from [this query](https://issues.apache.org/ooo/buglist.cgi?bug_status=UNCONFIRMED&f2=keywords&f3=cf_bug_type&known_name=NeedConfirm&list_id=39759&o2=notsubstring&o3=equals&query_format=advanced&resolution=---&v2=needmoreinfo&v3=DEFECT&order=bug_id%20DESC&query_based_on=NeedConfirm).

Or, if you are just starting out, you can post a note to the QA mailing list and ask for a small batch of reports to be assigned to you. This can be a good first step, since we'll try to give you easier reports to review at first.

Here's what to do to confirm a new defect report:

 1. First, assign the report to yourself by setting your Bugzilla username (your email address) in the "QA Contact" field. If you are not able to add yourself, then send a note to the QA mailing list asking to be added to the "qa-team" group in Bugzilla.
 1. Then read over the report. What are they really saying?  Are they reporting a bug?  Asking for a new feature?  Asking a support question?  Just because it is in Bugzilla does not mean that it is a defect report.
 1. Ask yourself:  Are they saying that something is working incorrectly?  Or are they asking for new functionality?
If they are asking for a new feature, change the Issue Type field to "FEATURE". If they are asking for an enhancement of an existing feature, set the Issue Type field to "ENHANCEMENT".
You can now set the Status to CONFIRMED and then save your changes. You are done with the report.
 1. Otherwise, search Bugzilla for keywords related to the bug report to see if this is a duplicate defect report. If it is, change the Status to RESOLVED/DUPLICATE and type in the defect number that this report is a duplicate of. You are now done with this report.
     1. If the report is actually reporting a defect, then you have more work to do. Try to reproduce it with the latest release of OpenOffice. If you can reproduce the defect. set the Status to CONFIRMED, set the "Last Confirmation" field to the release that you tested with, and set the Importance field to an appropriate value, depending on the severity of the defect.
     1. If the report is not clear enough to reproduce, enter a comment asking the user for more information and add the "needmoreinfo" to the Keyword field. Be specific about what information you need:  more detailed steps, a test document, clarification about what version they are running, etc. When the user responds you will be copied on their response and can continue with this report. But for now you are done with this report.
     1. If your testing cannot reproduce the bug, and you **do not** need more information from the user, then change the status to RESOLVED/IRREPRODUCIBLE.
     1. If the user was confused, did not understand the functionality or was asking a support question, then point them to the [Community Support Forums](http://forum.openoffice.org) and mark the issue as RESOLVED/INVALID. Of course, you can help if it is a simple question, but the forums are the better place for a user to find help. Bugzilla is not for support. It is for reporting bugs.

Note: Once you have reviewed a bug report, it should only be left in the UNCONFIRMED state if you are waiting for more information from the user, in which case you should also set the "needmoreinfo" value into the Keyword field. In all other cases you should push the report forward to a new status, either CONFIRMED, RESOLVED/IRREPRODUCIBLE, RESOLVED/INVALID or RESOLVED/DUPLICATE, or by changing the Issue Type to FEATURE or ENHANCEMENT.

It is a judgement call on whether to immediately mark an issue RESOLVED/IRREPRODUCIBLE or to send the user a question and wait for a response. An intermediate approach, when confirming defects report written against older versions of OpenOffice, is to mark the bug as RESOLVED/IRREPRODUCIBLE and at the same time add a comment saying, "I was not able to confirm the 
bug given these steps in the current version of OpenOffice (AOO 4.1.3), so I'm closing this report. If you are still seeing this problem after upgrading to AOO 4.1.3 please post the details and we can reopen the report".

Finally, think of the confirmation process as the opportunity for the QA Team to improve the value of information we receive from users. We're taking the raw bug reports, sorting through them, eliminating the ones that do not report new bugs, and then passing on the good ones to the programmers. So anything you can do to improve the quality of the incoming defect reports will help. This includes clarifying the steps needed to reproduce the problem, attaching sample documents that you might create to reproduce the
problem, improving report titles to make them more accurate/relevant to the real issue, correcting classifications and adjusting defect priorities.

## Easy QA Task: Verifying Fixed Defects

Verifying bug fixes (re-testing a bug report after a developer has fixed it) is also very important, since some bug fixes either fail to fix the bug, or cause a new bug.

You can get a list of fixed bugs from this query: [All fixed bugs after AOO 3.4 release](https://issues.apache.org/ooo/buglist.cgi?cmdtype=dorem&remaction=run&namedcmd=Fixed_After_340&sharer_id=248432)

Select the bug you want to verify:

 1. First you need to understand which problem the defect report is referring to.
 1. Install the latest build.
 1. Follow the steps to reproduce and check to see if the defect has been fixed.
 1. Add additional comments to the bug with your test result. e.g. build revision number, platform you have been tested etc.
 1. "Test around" the bug to make sure that nothing was broken when fixing it. You will develop and intuition for this as you learn to "think like a bug".
 1. Change defect status to "Verified" 

## Easy QA Task: Manual Testing

Manual testing gains you further familiarity with QA process, by executing pre-defined test cases and writing up defect reports for any new defects found.

To get more familiar with AOO, now you can try to perform some manual test cases.

  - Browse test management tool, [Testlink](http://aootesting.adfinis-sygroup.org) to find available test cases.  
  - Read this guide if you are not familiar with Testlink tool. [Testlink usage guide](http://wiki.openoffice.org/wiki/QA/Testlink)

## Easy QA Task: Test Case Authoring

This is a more advanced topic, but after mastery of the above two steps, and learning to "think like a bug", you will be ready for this.

After some practice on test case execution, now you can start writing new test cases.

Useful guide for writing manual test cases:

 * [A guide for writing test case](https://wiki.openoffice.org/wiki/QA/Testcase/How_to_write_test_case)
 * [A simple test case sample](https://wiki.openoffice.org/wiki/QA/Testcase/Sample)

## Module Completion

Once you have done the above, go to our our [Directory of Volunteers](https://cwiki.apache.org/confluence/display/OOOUSERS/Directory+of+Volunteers) wiki page and add or update your information. Also, add an entry for yourself to the [QA Testing Preferences](https://cwiki.apache.org/confluence/display/OOOUSERS/QA+Testing+Preferences) page. Congratulations! Please send a note to [qa@openoffice.apache.org](mailto:qa@openoffice.apache.org?subject=Completed Introduction to QA) so we know.
