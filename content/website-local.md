type=page
title=Website Development
notice=https://www.apache.org/licenses/LICENSE-2.0
~~~~~~
Making updates to the Apache OpenOffice project's websites is simple. It's even easy 
for non-committers (new contributors - like you) to create a patch to request that 
pages are updated by the project community.

[TOC]

## Two Websites

The Apache OpenOffice project maintains two websites:

* The [project website](https://openoffice.apache.org/), primarily for development and technical information (which you're viewing now). 
 All content for this website uses [Markdown](http://daringfireball.net/projects/markdown/) syntax (.mdtext files).
* The user portal, [www.openoffice.org](https://www.openoffice.org), primarily for end user information and support.
 Content for the user portal primarily uses html, but some content is in
 [Markdown](http://daringfireball.net/projects/markdown/) syntax (.mdtext files).

Both of these sites use the [Apache Content Management System](https://www.apache.org/dev/cms.html) (CMS) to manage editing, submitting changes, and updating the live websites.
In essence, regardless of how you make changes to either web area, the changes first go
the staging sites for these areas, respectively (below), and then are copied to the production websites.

* The [project staging site](http://openofficeorg.staging.apache.org/)
* The [user portal staging site](http://ooo-site.staging.apache.org/)


## Version Control

We use [Apache Subversion][1] for version control. You can [browse the project 
repository][2] or [browse the user portal repository][9] source files directly in your web browser.



## How To Make or Request Changes to the Websites

### Using SVN Directly (for technical users)
You can make changes to either site using svn (subversion). This typically involves 
doing an svn checkout, making changes to files and --

* committing your changes
if you are an "Apache committer", or 
* submitting a "patch" (an svn "diff" file) if you are a contributor but not a "committer". 

Consult your local svn implementation for how to do commits or create patches. (See also, the [SVN Book](http://svnbook.red-bean.com/) ). 

Patches, svn "diff" files can be submitted in a variety of ways:

* File an issue using [OpenOffice Bugzilla](https://bz.apache.org/ooo/) and select the "www"
category to file it. You should then use your saved patch as an attachment to the
issue. Please send a follow-up e-mail to [dev](mailto:dev@openoffice.apache.org) and provide the
issue number so we can follow-up.

* Patches can be submitted as attachments to e-mail to the 
[Apache OpenOffice developer](mailto:dev@openoffice.apache.org) list.

Changes committed with SVN commit your changes to the "staging area". These changes will need to be published to become active on the "production" site.

### Using the Apache CMS Bookmarklet (simpler method)

Quick editing of the site is available for committers and contributors using the Apache CMS
[from your browser.][6] If you are a committer and use the bookmarklet in your web browser, you should use
your Apache credentials to log in, make changes and submit them to staging.
If you are not a committer, you can still use the bookmarklet by signing in to the bookmarklet as *anonymous*.
See detailed how-to steps in the [Apache CMS Reference](https://www.apache.org/dev/cmsref.html#non-committer) for non-committers.

### More Details

Additional details on the above methods can be found on  [How to edit the Apache OpenOffice website](https://openoffice.apache.org/docs/edit-cms.html).

## Publishing Changes to the Production Websites

### For Committers
As previously noted, changes you make, either through an svn commit or using the CMS GUI tool, 
are enacted on the staging sites. Once you review your changes on the staging site,
you can "publish" the site -- enacting your changes on the production site. Only Apache "committers" can actually publish sites.  


* You can use the CMS GUI tool to also commit, review, and publish your changes from the 
staging site. 
* Or, you can use the "publish" link for a site from the [CMS Web Site](https://cms.apache.org/)
after reviewing it in staging from a "commit" operations.
* Or, you can use the command line, **publish.pl "site-name"**. For our purposes,
**"site-name"** will either be **"openofficeorg"** or **"ooo-site"**. 

Generally speaking, unless you have established a full **Complete Local Website Development** environment as described in the next
section, you will likely be running **publish.pl** from your "people.apache.org" account.

### For Contributors -- non-committers
If you are not a committer, you will need
to follow the procedures for "contributors" in the
[Developer FAQ](https://openoffice.apache.org/developer-faqs.html#im_not_a_committer)
for getting your changes published by a committer of the project, after you submit a patch.

## Complete Local Website Development (for technical users and committers)

The following information provides instructions on doing website development for either of the OpenOffice websites 
on your local computer. If you feel a need to change anything on the websites that effect site processing by the CMS -- e.g. the templates, processing for new file types not included  in /lib/path.pm, additional Django template capabilities, etc. -- you will need to setup a local website development area for testing changes.

These instructions assume you have setup a webserver in your local environment. Details are
provided on setting up the resources needed to process "Markdown" on your local server
and how to publish to the production Apache OpenOffice sites from your local environment. 

* [Setup](#setup) - How to download the AOO project site repos and setup the Apache CMS.
* [Directory Layout](#directory_layout) - Where to find the content, templates, and scripts.
* [Local Development](#local_development) - How to build and test locally.
* [Submitting Your Results](#submitting_your_results) - How to contribute your edits.

### Setup

#### Create a directory on your computer for the Apache CMS work with both the project's
site and the migrating openoffice.org website.

    mkdir aoo-web
    cd aoo-web

#### Download the svn repos for the AOO  project site.

    svn co https://svn.apache.org/repos/asf/openoffice/site/trunk site

#### Download the svn repos for the migrated OpenOffice.org website.

    svn co https://svn.apache.org/repos/asf/openoffice/ooo-site/trunk ooo-site

#### Download the svn repos for the Apache CMS.

    svn co https://svn.apache.org/repos/infra/websites/cms/ cms

You will have three sub-directories in your local website directory -- `site`, `ooo-site`, and `cms`.
The "cms" directory will contain scripts needed to build either of the websites using the ASF CMS in a local environment. This is 
necessary to see how changes to templates or other ASF CMS internal files will affect the website. See:
[https://www.apache.org/dev/cms.html](https://www.apache.org/dev/cms.html) for more information on the 
ASF CMS directory structure.

#### Install Python dependencies.

Adapted from the [Apache CMS Reference][3]

The easiest way to install the dependencies is to use Python setuptools.

#### Check that your version of Python is 2.7 or greater

    python --version

#### Follow the installation instructions for [setuptools][4].

#### Install dependencies

    sudo easy_install Pygments
    sudo easy_install ElementTree
    sudo easy_install Markdown

### Directory Layout

#### Content directories

The `site/content/openofficeorg` and `ooo-site/content/` directories contain web content - markdown, html, javascript, css, images and other files. Files that do not fit recognized patterns from `site/lib/path.pm` or `ooo-site/lib/path.pm` are copied as is to the web site during the build.

#### Templates directory

The `site/templates` and `ooo-site/templates` directories contain the html skeletons used during the site build.

* `skeleton.html` - our current html page template.
* `sidenav.mdtext` - markdown of the side navigation panel.
* `html_page.html` - wrapping for html pages.
* `single_narrative.html` - extends skeleton.html.

You may see other template files here as well that are used by Django during the site construction.

#### Lib directory

The `site/lib` and `ooo-site/lib` directories contain two perl modules that determine how content files are processed during the site build.

* `path.pm` - maps file patterns like `.mdtext` into the view building routines. We can expand to cover other patterns.
* `view.pm` - a set of python subroutines for converting content into web pages.

#### Build tools

You can find the CMS build tools in the `cms` directory.

* `cms/build/` - perl scripts for building the site and markdown extensions.
* `cms/conversion-utilities/` - scripts used by various projects for conversion including `cwiki` conversion.
* `cms/webgui/` - the webgui behind the `bookmarklet`.

These can be extended locally. Before any changes become part of our process they will need to be cleared with Apache Infrastructure. We'll need to submit patches. These should be additive or be bug fixes.

This area should be updated, via svn update, as changes do take place on these routines.

### Local Development

#### Edit the site

Using your favorite editors edit the site content, templates, and lib scripts.

#### Python Markdown Daemon

Start the Python Markdown daemon.

    export MARKDOWN_SOCKET=`pwd`/markdown.socket PYTHONPATH=`pwd`
    python cms/build/markdownd.py

#### Build the sites.

Using the directory names from Download sections above --

    cms/build/build_site.pl --source-base site --target-base www
    cms/build/build_site.pl --source-base ooo-site --target-base www
    
This will generate the web content for the project site, "site", or the openoffice site, "ooo-site"
to directory "www". 

#### Copy the site to an area your computer's web server.

On my Mac:

    sudo scp -rp www/content /Library/WebServer/Documents/.

The site is then available with [http://localhost/openofficeorg/][5] or [http://localhost/][8]


### Submitting your results.

#### Committer

Do the appropriate combination of svn status, svn add, and svn commits. Commits will cause staging rebuilds.
See [How to Edit the Apache OpenOffice Website][6]

Please note that if you have removed any files or directories from your source tree then you must also remove
these from the staging build. The staging for the project site is 
`https://svn.apache.org/repos/infra/websites/staging/openofficeorg`. Check the staging builf out,
svn remove and commit the same files and directories.

#### Contributor

Use SVN to submit svn "diffs".

For further information see the [Apache Source Code Repository][7] page.


## Google Analytics

We use Google Analytics on key webpages to gather information on website
usage patterns. This information is then used to help us prioritize what
areas of the website should get more attention.

To enable a page for Google Analytics you need to added the following block 
of JavaScript immediately before the closing &lt;/head&gt; in the HTML.


    <script type="text/javascript">
    
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-98607986-1']);
      _gaq.push(['_setDomainName', 'openoffice.org']);
      _gaq.push(['_trackPageview']);
    
      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();
    
    </script>


Note: This is not needed for the project website, only for the openoffice.org pages.
        
It is not necessary to add this to every single web page. The greatest benefit for
the effort comes from adding it to the key destination pages.


[1]: https://subversion.apache.org
[2]: https://svn.apache.org/repos/asf/openoffice/site/trunk/
[3]: https://www.apache.org/dev/cmsref.html#local-build
[4]: http://pypi.python.org/pypi/setuptools
[5]: http://localhost/openofficeorg
[6]: https://cms.apache.org/#bookmark
[7]: https://www.apache.org/dev/version-control.html
[8]: http://localhost/
[9]: https://svn.apache.org/repos/asf/openoffice/ooo-site/trunk/
