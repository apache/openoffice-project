Title: Subversion Basics
Notice:    Licensed to the Apache Software Foundation (ASF) under one
           or more contributor license agreements.  See the NOTICE file
           distributed with this work for additional information
           regarding copyright ownership.  The ASF licenses this file
           to you under the Apache License, Version 2.0 (the
           "License"); you may not use this file except in compliance
           with the License.  You may obtain a copy of the License at
           .
             http://www.apache.org/licenses/LICENSE-2.0
           .
           Unless required by applicable law or agreed to in writing,
           software distributed under the License is distributed on an
           "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
           KIND, either express or implied.  See the License for the
           specific language governing permissions and limitations
           under the License.

We use [Apache Subversion][1] for version control. For a complete reference on Subversion see the [Subversion Book][2]. You can [browse our repository][3] in your web browser.

This page gives instructions on performing basic development tasks using the Subversion Command-Line Client. This instruction assumes you have Apache Subversion installed.

* [Overview](#overview) 
* [Sub-commands and Abbreviations](#sub-commands_and_abbreviations) 
* [Client Configuration](#client_configuration)
* [Repository Layout](#repository-layout)
* [Getting the source code](#getting-the-source-code)
* [Basic Work Cycle](#basic_work_cycle)
* [Committing Changes](#committing_changes)
* [Commit Message](#commit_message)
* [Committing Changes By Others](#committing_changes_by_others)
* [Creating and Submitting Patches](#creating_and_submitting_patches)
* [Merging changes to a branch](#merging_changes)
* [Further Information](#further_information)

## <a id="overview"></a>Overview

You begin using Subversion by copying a directory from a remote repository to a local directory on your file system. This is known as a checkout of a working copy.

Subversion uses a copy-modify-merge model meaning that you can add and edit files and directories in your working copy like any other files on your system, but you should use subversion commands for everything else such as `svn copy` and `svn move` instead of the operating system commands.

## <a id="sub-commands_and_abbreviations"></a>Sub-commands and Abbreviations

Subversion commands can be run from a command shell such as Bash on Linux. The subversion client command is `svn` followed by optional sub-commands, options, and arguments.

Show the program version and modules

    $ svn --version

Run a sub-command

    $ svn <subcommand> [options] [args]

Most sub-commands take file and/or directory arguments, recursing on the directories. If no arguments are supplied to such a command, it recurses on the current directory (inclusive) by default. (from `svn help`)

The following is only a partial list of sub-commands relating to this instruction. For a complete list, see the [Subversion Book][2], or use `svn help`.

* `add` - Schedule a new file or directory (including contained files) for inclusion in the repository
* `checkout`, `co` - Create a local working copy of a remote repository
* `commit`, `ci` - Commit (check in) local changes to the repository
* `copy`, `cp` - Copy one or more files in a working copy or in the repository
* `delete`, `del`, `remove`, `rm` - Items specified are scheduled for deletion upon the next commit. Working copy files not yet committed are deleted immediately.
* `diff`, `di` - Displays differences in files from the directory
* `help`, `?`, `h` - Subversion help and help on sub-commands
* `move`, `mv`, `rename`, `ren` - Moves files or directories in your working copy or repository
* `resolve` - Resolve conflicts on working copy files or directories
* `revert` - Undo all local edits or optionally a file or directory
* `status` - Print the status of working copy files and directories
* `update` - Bring changes from the repository into your working copy

## <a id="client_configuration"></a>Client Configuration

Committers need to [configure their Subversion client][6] to handle the differences in line endings of text files on different operating systems.

There are instances where Subversion may need to open an editor. You need to have the environment variable EDITOR set to the editor you would like to use. To set it for the current terminal session in Bash (your path may differ):

    $ export EDITOR=/usr/bin/vim

## <a id="repository_layout"></a>Repository Layout

The AOO repository layout uses the following top-level directories `branches`, `site`, `tags`, and `trunk`.

* `branches` - Contains branches used for continued development of a specific version, experimental versions, or for  developing features to be merged into the trunk or a branch later. (needs examples)
* `site` - Contains the web site source code. Also contains it's own trunk directory.
* `tags` - Contains specific versions of the project. These tags are not to be revised. (needs examples)
* `trunk` - Contains the current source code.
For more information see the [Contributors Tech Guide][7].

## Getting the source code

From the parent directory of where you want the working copy. In this example the `aoo-trunk` directory will be created if it does not exist.

    $ svn co https://svn.apache.org/repos/asf/openoffice/trunk aoo-trunk
    A    aoo-trunk/tools
    A    aoo-trunk/tools/dev
    A    aoo-trunk/tools/dev/fetch-all-cws.sh
    A    aoo-trunk/tools/dev/cws-list.txt
    A    aoo-trunk/tools/dev/fetch-all-web.sh
    A    aoo-trunk/tools/dev/web-list.txt
    A    aoo-trunk/tools/dev/single-hg.sh
    Checked out revision 1145818.

"A" indicates file or directory is "Added" to working copy

## <a id="basic_work_cycle"></a>Basic Work Cycle

* Update your working copy - For this you use the `svn update` command
*  Make changes - For this you may edit files in an editor, or use the `svn add`, `svn delete`, `svn copy`, `svn-move` commands
* Review Changes - For this you use the `svn status` and `svn diff`
* Fix Mistakes - Make additional edits to files or you can use the `svn revert` to restore files or directories to an unmodified state
* Resolve Conflicts - There is a chance others have committed changes while you have been changing your working copy. You should run the `svn update` command to bring your copy up to date. This may create a local conflict where someone may have added a file with a name that you also want to add, or may have made changes to the same line of a file as you. For this use the `svn resolve` command.
* Publish Changes - For this you use the `svn commit` command

### Adding a File

After creating the file "test-file.txt" in the working copy.

    $ svn status
    ?       test-file.txt

? indicates test-file.txt is not under version control

### Scheduling a file for addition to repository

    $ svn add test-file.txt
    A         test-file.txt

    $ svn status
    A       test-file.txt

"A" indicates file is scheduled for addition

### Running a diff

    $ svn diff
    Index: test-file.txt
    ===================================================================
    --- test-file.txt	(revision 0)
    +++ test-file.txt	(revision 0)
    @@ -0,0 +1 @@
    +This is a test file for svn-basics.

    Property changes on: test-file.txt
    ___________________________________________________________________
    Added: svn:eol-style
       + native

### Committing a file

    $ svn commit test-file.txt -m "added test-file.txt"
    Adding         test-file.txt
    Transmitting file data .
    Committed revision 2.

### Update the working copy

    $ svn update
    U    test-file.txt
    Updated to revision 3.

"U" indicates an "Update" to a file or directory

Modify the file (this example uses the vim editor)

    $ vim test-file.txt

### Check the Status

    $ svn status
    M       test-file.txt

"M" indicates the file has been "Modified"

    $ svn diff
    Index: test-file.txt
    ===================================================================
    --- test-file.txt	(revision 3)
    +++ test-file.txt	(working copy)
    @@ -1,2 +1,3 @@
     This is a test file for svn-basics.
     This is a new line added by someone else.
    +This line added by me.

### Resolving Conflicts

Suppose someone edits the same line as you before you commit

    $ svn update
    Conflict discovered in 'test-file.txt'.
    Select: (p) postpone, (df) diff-full, (e) edit,
            (mc) mine-conflict, (tc) theirs-conflict,
            (s) show all options: 

This is just like if you had ran the `svn resolve` command

Selecting `df` displays this:

    --- .svn/text-base/test-file.txt.svn-base	Sun Jul 17 17:38:52 2011
    +++ .svn/tmp/test-file.txt.tmp	Sun Jul 17 21:35:09 2011
    @@ -1,2 +1,7 @@
     This is a test file for svn-basics.
     This is a new line added by someone else.
    +<<<<<<< .mine
    +This line added by me.
    +=======
    +This line is added by someone else also.
    +>>>>>>> .r4
    Select: (p) postpone, (df) diff-full, (e) edit, (r) resolved,
            (mc) mine-conflict, (tc) theirs-conflict,
            (s) show all options:

If you choose `e`, Subversion will launch an editor with both sets of changes included for you to edit. You can save your changes in the editor and then select `r` (for resolved).

    G    test-file.txt
    Updated to revision 4.

"G" indicates "merGed"

## <a id="committing_changes"></a>Committing Changes

Only Committers can commit directly to the repository. The following example shows using your Apache ID and password.

    $ svn commit test-file.c --username your-name --password your-password \
      -m "added new C file"
    Sending        test-file.txt
    Transmitting file data .
    Committed revision 5.

In general, you may not have to include always your username or password if you do a proper setup of your ssh key or have subversion store the password.

Always check your changes with "svn diff" and "svn status". Also be careful to specify the files and/or directories you want to change, if
you don't specify, SVN will commit **all** your changes.

For further information see the [Basic Work Cycle][8] page from [Subversion Book][2].

## <a id="commit_message"></a>Commit Message
The examples in the previous sections use a simple commit message with the "-m" option.

This is fine for some quick testing or for large bulk commits of code that you wrote.

We ask that your commits include special tagging to appropriately credit the patch.
See the [crediting section](http://subversion.apache.org/docs/community-guide/conventions.html#crediting) of the Coding and Commit
Conventions of the Apache Subversion project.

Log comments are important.
Information like author, where the change start/ends, the date, the bugzilla issue, and the author don't really belong
in the code as SVN can keep it much more effectively without altering the coding style.
Always try to use a log file for your commits. The previous commit when done by an experienced committer
should actually look like this:

    $ svn ci -F test-log.txt test-file.c 
    Sending        test-file.c
    Transmitting file data .
    Committed revision 5.


Use of the special fields will enable processing by scripts like the
[contribulyzer](http://www.red-bean.com/svnproject/contribulyzer/) to help quickly identify
contributors.


## <a id="committing_changes_by_others"></a>Committing Changes By Others

See the [Applying Patches][9] section of the Committer FAQ page. Please use the special fields 
described in the previous Commit Message section to commit changes supplied by others. 

Example similar to one on Committer FAQ:

    #i999999# Added some cool new feature.
    Patch by: John Doe <john.doe.at.null.org>
    Suggested by: Jane Brown <janeb.at.notnull.org>

<!-- Using the `-m (--message)` option only allows a single line log message. To commit a multi-line message use the `-F (--file)` option (with a previously created file) or use neither -m or -F and an editor will be started. -->

An alternative way is the following command. It adds a new line with "\n":

    $ svn commit -m $'#i999999# Added some cool new feature.\nPatch by: /
      John Doe <john.doe.at.null.org>\nSubmitted by: John Doe /
      <john.doe.at.null.org>' test-file.txt

## <a id="creating_and_submitting_patches"></a>Creating and Submitting Patches

See the [Sending in Patches][10] section on the Contributors Tech Guide page.

Create the patch file from `svn diff` where `your-patch-name.patch` is the full path to the patch file to create.

    svn diff > your-patch-name.patch

## <a id="merging_changes"></a>Merging changes to a branch

New development is done in the "trunk", development area, of the tree. Stable, release branches, are specifically named and can be found
in the [branches](http://svn.apache.org/viewvc/openoffice/branches/)  area of the openoffice svn tree. With few exceptions you do **NOT** do direct commits to the stable, release,
branches. Changes, commits, to stable branch are typically only done during a formal release cycle and must be discussed on the "dev" list.

When a new release is in preparation, bug fixes are reviewed, and fixes that have been made to "trunk" get applied to the stable, release, branch. This is done using the "svn merge" command which finds  previous changes and replays them.  SVN also keeps a record
of the specific commits that have been merged so the changes are much easier to track down.

The first step is to do a check out of the stable, release, branch. The following examples use the AOO34 release branch, and assume
you want to apply changes from trunk for a new release, maybe AOO341.

You can do a complete checkout of the release branch or you can save some space by using the "--depth=empty" option:

     % svn co --depth=empty https://svn.apache.org/repos/asf/openoffice/branches/AOO34 aoo-stable
     U   aoo-stable
     Checked out revision 1347362.

This will put a placeholder branch for the AOO34 in directory "aoo-stable".


In the aoo-stable directory, you can keep saving space (rather convenient) until you reach the directory where you want to make changes:

     % svn up --depth=empty main
     Updating 'main':
     A    main
     Updated to revision 1347363.
     % svn up --depth=empty jvmfwk
     Updating 'jvmfwk':
     A    jvmfwk
     Updated to revision 1347366.

At this point, there are svn placeholder entries for /main/jvmfwk.

To do a complete checkout from there:

     svn up --set-depth=infinity
     Updating '.':
     A    source
     A    source/elements.hxx
     A    source/fwkbase.cxx
     ... (and so on)

Now merge the specific revision(s) you want (in this case r1333165):

     svn merge -c1333165 https://svn.apache.org/repos/asf/openoffice/trunk/main/jvmfwk .
     --- Merging r1333165 into '.':
     U    distributions/OpenOfficeorg/javavendors_unx.xml

At this point, you have merged r1333165 into r1347366. (For release from trunk to a new release, it's likely you would be merging a higher revision to a lower existing release revision.)

After you finish merging, check your changes with "svn status" and "svn diff"
and commit from the aoo-update directory:

     svn commit -m "Merge r1329539, r1329547, 1333165 - Add Oracle as a Java vendor on unix." distributions/OpenOfficeorg/javavendors_unx.xml distributions/OpenOfficeorg/javavendors_freebsd.xml
     Sending        distributions/OpenOfficeorg/javavendors_freebsd.xml
     Sending        distributions/OpenOfficeorg/javavendors_unx.xml
     Transmitting file data ..
     Committed revision 1347377.

## <a id="further_information"></a>Further Information

For more information see: 

* [Apache Subversion Project][1]
* [Subversion Book][2]
* [Apache Developer Information][11]


[1]: http://subversion.apache.org
[2]: http://svnbook.red-bean.com
[3]: http://svn.apache.org/viewvc/openoffice/trunk
[4]: https://svn.apache.org/repos/asf/openoffice
[5]: http://www.apache.org/dev/version-control.html
[6]: http://www.apache.org/dev/version-control.html#https-svn-config
[7]: http://www.apache.org/dev/contributors.html#svnbasics
[8]: http://svnbook.red-bean.com/nightly/en/svn.tour.cycle.html
[9]: http://www.apache.org/dev/committers.html#applying-patches
[10]: http://www.apache.org/dev/contributors.html#patches
[11]: http://www.apache.org/dev/
