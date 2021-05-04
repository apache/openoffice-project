Title:     Source Control
Notice: http://www.apache.org/licenses/LICENSE-2.0

As of August, 2019, we use GIT for version control. You can [browse our
repository][10] using the "tree" view from gitbox in your web browser. The [README.md](https://github.com/apache/openoffice) at github.com provides useful information on how to download and build Apache OpenOffice.

The previous svn repository, now read only, using [Apache Subversion][1] for version control is [still viewable][2] in your web browser.

Currently, subversion is still used for the two OpenOffice web sites.
See our [Subversion Basics](http://openoffice.apache.org/svn-basics.html)
for more information on using subversion (svn) for the Apache OpenOffice project.

<!--- For further information see the [Apache Source Code Repository][3] page.-->

## Getting the source code

### Using GIT

<!--- You can use our git repository for downloading source but not committing (read only):
    [https://github.com/apache/openoffice](https://github.com/apache/openoffice)-->

Instructions provided in [README.md](https://github.com/apache/openoffice) from github.com can be used successfully to get a local copy of the complete source for Apache OpenOffice.

### Using SVN (applies to code through July, 2019)

This will get you everything, including the language files:

    svn co https://svn.apache.org/repos/asf/openoffice/trunk aoo

Including SVN overhead, this requires approximately 4 GB of storage.


### Source archive of the latest release

An archive of the source for the latest release can be obtainted from the Apache Software Foundation repository:
    [https://archive.apache.org/dist/openoffice](https://archive.apache.org/dist/openoffice/)


## Browsing/Searching Source Code

<!--- We have an instance of [Atlassian FishEye][4] for source browsing, searching,
reporting and visualization of main trunk (main development area).-->

We host an [OpenGrok](http://opengrok.openoffice.org/) instance for our
main repository areas.

## Building and Running

See the [Apache OpenOffice Building Guide page][5]
    for an overview on building.

The [Development Snapshots builds][7] page, pre-release builds, also provide additional information on building.

## Testing Developer Installation Sets

See [Development Snapshot Builds: Full installation sets][8], pre-release builds, or [Development Builds][9], nightly builds from the buildbots, for complete installation sets for available platforms.

Install developer builds to a new directory if you don't want to overwrite your
existing Apache OpenOffice installation.

* Linux: Create a new directory for the AOO developer install.
Install the RPM pack with --prefix="some new AOO directory" option.
* Windows: Use the custom install option, and choose a new directory location for the
AOO developer install.
* Mac: create a new folder for AOO developer install. Download the ".dmg" file there, and install
to the new directory.


## Code and Contribution Statistics

<!--- Our SVN tree is read by the [Open Hub tracker][6] to generate some various statistics.
Note that the migration from the legacy Mercurial repository to SVN at Apache has
caused pre-existing files to be double-counted. But the contribution history should
be intact.-->

[The Apache OpenOffice Gitbox site][10] provides useful statistics on code contributions and changes.

## Special Development Branches

For larger, extensive code modifications, specialized branches are created. These branches can also be found in our git repository.

<!--- You can find out more information on them from the Wiki [Source Code](https://wiki.openoffice.org/wiki/Source_Code) page.-->

[1]: https://subversion.apache.org/
[2]: https://svn.apache.org/viewvc/openoffice/trunk/
[3]: https://www.apache.org/dev/version-control.html
[4]: https://fisheye.apache.org/changelog/openoffice
[5]: https://wiki.openoffice.org/wiki/Documentation/Building_Guide_AOO
[6]: https://www.openhub.net/p/openoffice
[7]: https://cwiki.apache.org/confluence/display/OOOUSERS/Development+Snapshot+Builds#DevelopmentSnapshotBuilds-buildflags
[8]: https://cwiki.apache.org/confluence/display/OOOUSERS/Development+Snapshot+Builds#DevelopmentSnapshotBuilds-fullsets
[9]: https://www.openoffice.org/download/devbuilds.html
[10]: https://gitbox.apache.org/repos/asf?p=openoffice.git
