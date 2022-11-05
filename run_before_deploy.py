from favicons import Favicons

# Generating favicons

_YOUR_ICON = "raw_files/favicon.png"
_WEB_SERVER_ROOT = "content/magics"

with Favicons(_YOUR_ICON, _WEB_SERVER_ROOT) as favicons:
    favicons.generate()
    FAVI_NAMES = favicons.filenames()
    FAVI_HTML = "\n".join(favicons.html())