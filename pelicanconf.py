#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


# Use alias plugin [source: https://github.com/Nitron/pelican-alias]
PLUGINS = ['pelican_alias',]

AUTHOR = u'Phillip Kent'
SITENAME = 'Phillip Kent [SITE UNDER RE-CONSTRUCTION]'
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
