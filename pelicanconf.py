#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Theme setting
THEME = "../pelican-themes/blueidea"

# Use alias plugin [source: https://github.com/Nitron/pelican-alias]
# Use render_math plugin for MathJax
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['pelican_alias','render_math']

AUTHOR = u'Phillip Kent'
SITENAME = 'Phillip Kent'
SITESUBTITLE = 'design science education research'
SITEURL = 'http://www.phillipkent.net'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()
##LINKS = (('Pelican', 'http://getpelican.com/'),
##         ('Python.org', 'http://python.org/'),
##         ('Jinja2', 'http://jinja.pocoo.org/'),
##         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = ()
##SOCIAL = (('You can add links in your config file', '#'),
##          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
