# Apache OpenOffice Project Site - openoffice.apache.org

This is the content and theme for https://openoffice.apache.org/

## Contributing to the website content

You can fork from https://github.com/apache/openoffice-project, test your changes as described below
and raise a pull request.

You can simply raise a pull request with a set of simple changes.

Use the [dev@openoffice.a.o](https://lists.apache.org/list.html?dev@openoffice.apache.org) mailing list to contact
the OpenOffice PMC which manages this website.

## Automated publishing

Commits to the `main` branch are automatically published using Pelican using the instructions in the `.asf.yaml` file.
Information about `.asf.yaml` is found [here](https://cwiki.apache.org/confluence/display/INFRA/git+-+.asf.yaml+features).

Any build failures are reported to [commits@openoffice.a.o](https://lists.apache.org/list.html?commits@openoffice.apache.org)
mailing list.

## Quick updates to a single file

Updating a single file is simple. Simply edit the file online and save with your commit message. The website will be published in a minute or two.

## Prerequisites for building the website locally

The website is built using [Pelican](https://docs.getpelican.com/en/latest/quickstart.html) and a custom theme.
The builds for the website do require internet access.

- Install Pelican and Markdown.
- Python 3 is used.


## Clone the Git Repository

To get a copy of the repository you can either point to `Gitbox` or `GitHub`.

```
cd ~/Development/openoffice
rm -rf site.git
git clone https://gitbox.apache.org/repos/asf/openoffice-project.git site.git
git fetch
git pull
git checkout main
```

## Building & testing the site locally

To test the site locally, use 

    pelican content -t theme/openoffice
    pelican --listen
    
This builds the site, serves it locally at  http://localhost:8000/.

## Markdown

All of the pages in the site are in Markdown in `md` files.

## OpenOffice Theme

Pelican templates are included in the `theme` directory. The site templates are written in `html`.
`sidenav.html` is used and was derived specially from `sidenav.md`. To change the side navigation edit the `html`.

## Pages and Assets are in the Content Tree.

All content - pages and assets are in the content tree.

    https://github.com/apache/openoffice-project/tree/main/content

