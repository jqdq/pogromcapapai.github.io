from favicons import Favicons
from cdnget import Unpkg
import os

# Generating favicons

_YOUR_ICON = "raw_files/favicon.png"
_WEB_SERVER_ROOT = "content/magics"

print("Generating favicons")
with Favicons(_YOUR_ICON, _WEB_SERVER_ROOT) as favicons:
    favicons.generate()
    FAVI_NAMES = favicons.filenames()
    FAVI_HTML = "\n".join(favicons.html())

if all(i != "@picocss" for i in os.listdir("theme/static/css")):
    Unpkg().download("@picocss/pico", "1.5.6", "theme/static/css")
else:
    print("Found pico.css")