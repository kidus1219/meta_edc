from multisite import SiteID
from .defaults import *  # noqa

print(f"Settings file {__file__}")


SITE_ID = SiteID(default=1)
EDC_SITES_UAT_DOMAIN = False
ALLOWED_HOSTS = [
    "147.182.196.153",
    "0.0.0.0",
    "127.0.0.1",
    "localhost",
    "amana.tz.meta3.clinicedc.org",
    "hindu-mandal.tz.meta3.clinicedc.org",
    "mbagala.tz.meta3.clinicedc.org",
    "mnazi-moja.tz.meta3.clinicedc.org",
    "mwananyamala.tz.meta3.clinicedc.org",
    "temeke.tz.meta3.clinicedc.org",
]
EDC_MODEL_ADMIN_CSS_THEME = "edc_indigo"
LIVE_SYSTEM = True
