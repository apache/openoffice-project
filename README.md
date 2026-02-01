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
Information about `.asf.yaml` is found [here](https://github.com/apache/infrastructure-asfyaml/blob/main/README.md).

Any build failures are reported to [commits@openoffice.a.o](https://lists.apache.org/list.html?commits@openoffice.apache.org)
mailing list.


## Quick updates to a single file

Updating a single file is simple. Simply edit the file online and save with your commit message. The website will be published in a minute or two.

## For large changes create a feature branch

Create a branch named `preview/*` where `*` is the name of your new feature. For example if your feature branch is named `preview/refresh`
then commits are automatically staged to https://openoffice-refresh.staged.apache.org

Once your features are ready you can create a PR and do a squash & merge.

## ASF Pelican

See [ASF Pelican documentation](https://infra.apache.org/asf-pelican.html)

## Markdown

All the pages in the site are in GitHub Flavored Markdown in `md` files. See [GFM](https://infra.apache.org/gfm.html).

## OpenOffice Theme

Pelican templates are included in the `theme/openoffice/templates` directory. The site templates are written in `html`.

- `base.html` is the main page template.
- `page.html` extends the base template for the pages.
- `topnav.html` is the navigation menu and is included.

The CSS stylesheet is in `theme/openoffice/static/css/openoffice.css`.

## Pages and Assets are in the Content Tree.

All content - pages and assets are in the content tree.

    https://github.com/apache/openoffice-project/tree/main/content
