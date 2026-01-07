from .base import *


DEBUG = True
ALLOWED_HOSTS = []


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
        "test_db": {
            "class": "core.logging.db_handler.TestDBHandler",
        },
    },
    "root": {
        "handlers": ["console", "test_db"],
        "level": "DEBUG",
    },
}
