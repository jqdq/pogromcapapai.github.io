# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *
from run_before_deploy import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://jakdak.online'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

# STATIC_PATHS = ['magics']
STATIC_PATHS = ['images', 'magics']
_d1 = {f"magics/{i}":{"path":i} for i in FAVI_NAMES}
_d2 = {'magics/CNAME': {'path': 'CNAME'}}
EXTRA_PATH_METADATA = {**_d1, **_d2}

JINJA_GLOBALS = {
    'FAVI_HTML':FAVI_HTML
}
