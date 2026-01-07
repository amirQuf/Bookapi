import logging
import functools
import time

logger = logging.getLogger(__name__)


def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug("→ calling %s", func.__name__)
        result = func(*args, **kwargs)
        logger.debug("← finished %s", func.__name__)
        return result

    return wrapper


def log_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            logger.exception("exception in %s", func.__name__)
            raise

    return wrapper


def test_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f" START  Testing {func.__name__}.")
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            duration = time.perf_counter() - start
            logger.info("%s took %.3f sec", func.__name__, duration)

    return wrapper
