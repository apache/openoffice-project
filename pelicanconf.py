#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
from datetime import date

import sys
import os

AUTHOR = u'OpenOffice Community'
SITENAME = 'Apache OpenOffice'
SITEURL = ''
CURRENTYEAR = date.today().year

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_DATE = 'fs'
DEFAULT_LANG = u'en'

# Save pages using full directory preservation
PAGE_PATHS = [ '.' ]
STATIC_PATHS = [ '.' ]
PATH_METADATA= '(?P<path_no_ext>.*)\..*'
PAGE_SAVE_AS= '{path_no_ext}.html'
PAGE_URL= '{path_no_ext}.html'
PAGE_TRANSLATION_ID = None
# SLUGIFY_SOURCE = 'basename'
# PAGE_SAVE_AS = '{slug}.html'

# We don't use articles, but we don't want pelican to think
# that content/ contains articles.
ARTICLE_PATHS = [ 'articles' ]

# Disable these pages
ARCHIVES_SAVE_AS = ''
ARTICLE_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
INDEX_SAVE_AS = ''
TAGS_SAVE_AS = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Configure the asfgenid plugin                                                                                                                                                                                    
ASF_GENID = {
    'unsafe_tags': True,
    'metadata': False,
    'elements': True,
    'headings': True,
    'headings_re': '^h[1-4]',
    'permalinks': True,
    'toc': True,
    'toc_headers': '^h[1-6]',
    'tables': True,
    'debug': False
}

# TOC Generator
PLUGIN_PATHS = ['./theme/plugins']
PLUGINS = ['asfgenid', 'pelican-gfm']

# Unused links
LINKS = ( )
SOCIAL = ( )

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

