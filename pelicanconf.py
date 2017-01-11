#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fundor333'
SITENAME = u'Fundor 333'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'it'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget with fontawesome implementation
SOCIAL = (('facebook', 'https://www.facebook.com/fundor333'),
          ('twitter', 'https://twitter.com/fundor333'),
          ('linkedin', 'https://it.linkedin.com/in/matteo-scarpa-78969263'),
          ('github', 'https://github.com/fundor333'),
          ('gitlab', 'https://gitlab.com/fundor333'),)

# Link edited for more than 2-tuples
LINKS_F333 = (
    ('name', 'relative url', 'long text descrition'),
    ('ciao','altro','altro')
)

TWITTER_USERNAME = 'fundor333'
GITHUB_URL = 'https://github.com/fundor333'
SEARCH_BOX = False

DEFAULT_PAGINATION = 8

DEFAULT_ORPHANS = 4
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Specify theme

THEME = "theme"

PATH = 'content/'
PAGE_PATHS = ['../pages/']
PATH_METADATA = '../pages/(?P<fullpath>.+)[.].+'

# Leave .html alone; I only use it for static attachments, not posts
READERS = dict(html=None)

# For the landing page
TEMPLATE_PAGES = {
    '../theme/templates/home.html': 'index.html',
}

# URL schema; compatible with Octopress, but i happen to like it anyway
ARCHIVES_URL = 'everything/archives/'
ARCHIVES_SAVE_AS = 'everything/archives/index.html'
ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
CATEGORIES_URL = 'everything/categories/'
CATEGORIES_SAVE_AS = 'everything/categories/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
# This is the /blog/ index specifically
INDEX_SAVE_AS = 'everything/index.html'
INDEX_URL = 'everything/'
PAGE_URL = '{fullpath}/'
PAGE_SAVE_AS = '{fullpath}/index.html'
TAG_URL = 'everything/tags/{slug}/'
TAG_SAVE_AS = 'everything/tags/{slug}/index.html'
TAGS_URL = 'everything/tags/'
TAGS_SAVE_AS = 'everything/tags/index.html'

# Octopress-compatible filename metadata parsing
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

# Specify the plugins
PLUGIN_PATHS = ["plugin"]
PLUGINS = [
    'tag_cloud',
    'custom_article_urls'
]
