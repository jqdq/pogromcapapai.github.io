from favicons import Favicons
from cdnget import Unpkg

# Generating favicons

_YOUR_ICON = "raw_files/favicon.png"
_WEB_SERVER_ROOT = "content/magics"
_PICO_NAME = "@picocss/pico"

with Favicons(_YOUR_ICON, _WEB_SERVER_ROOT) as favicons:
    favicons.generate()
    FAVI_NAMES = favicons.filenames()
    FAVI_HTML = "\n".join(favicons.html())
    
Unpkg().download(_PICO_NAME, Unpkg().latest_version(_PICO_NAME), "theme/static/css", quiet=True)