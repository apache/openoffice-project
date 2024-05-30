
import datetime
# Basic information about the site.
SITENAME = 'Apache OpenOffice'
SITEDESC = 'The official developer website of the Apache OpenOffice open source project, home of OpenOffice Writer, Calc, Impress, Draw and Base.'
SITEDOMAIN = 'openoffice.apache.org'
SITEURL = 'https://openoffice.apache.org'
SITELOGO = 'https://openoffice.apache.org/images/AOO4_website_logo.png'
SITEREPOSITORY = 'https://github.com/apache/openoffice-project/blob/main/content/'
CURRENTYEAR = datetime.date.today().year
TRADEMARKS = 'OpenOffice, Open Office, Apache OpenOffice, Apache Open Office, OpenOffice.org, Developer, Project, Website, Official, Writer, Calc, Impress, Draw, Base, ODF, Open Document Format'
TIMEZONE = 'UTC'
# Theme includes templates and possibly static files
THEME = 'theme/openoffice'
# Specify location of plugins, and which to use
PLUGIN_PATHS = [ 'theme/plugins',  ]
# If the website uses any *.ezmd files, include the 'asfreader' plugin
PLUGINS = [ 'gfm', 'asfgenid',  ]
# All content is located at '.' (aka content/ )
PAGE_PATHS = [ 'pages' ]
STATIC_PATHS = [ '.',  ]
# Where to place/link generated pages

PATH_METADATA = 'pages/(?P<path_no_ext>.*)\\..*'

PAGE_SAVE_AS = '{path_no_ext}.html'
# Don't try to translate
PAGE_TRANSLATION_ID = None
# Disable unused Pelican features
# N.B. These features are currently unsupported, see https://github.com/apache/infrastructure-pelican/issues/49
FEED_ALL_ATOM = None
INDEX_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
# Disable articles by pointing to a (should-be-absent) subdir
ARTICLE_PATHS = [ 'blog' ]
# needed to create blogs page
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
# Disable all processing of .html files
READERS = { 'html': None, }

# Configure the asfgenid plugin
ASF_GENID = {
 'unsafe_tags': True,
 'metadata': False,
 'elements': True,
 'permalinks': True,
 'tables': True,

 'headings': True,
 'headings_re': '^h[1-4]',


 'toc': True,
 'toc_headers': '^h[1-6]',

 'debug': False,
}








