import tempfile

API_BASE_URL = None
LOG_LOGGER = "a1_zoo"
LOG_FILE = "a1_zoo.log"
CACHE_DIR = "%s/" % tempfile.mkdtemp(prefix="a1_zoo")
