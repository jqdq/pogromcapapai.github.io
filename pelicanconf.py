AUTHOR = 'Jakub Dakowski'
SITENAME = 'jakdak.online'
SITEURL = 'https://jakdak.online'

TYPOGRIFY = False

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "theme"

# Render settings
PATH = 'content'
DEFAULT_CATEGORY = 'misc'
PAGE_PATHS = ['../pages']

USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True
DEFAULT_DATE='fs'
