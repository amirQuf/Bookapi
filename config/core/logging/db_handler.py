import logging


class TestDBHandler(logging.Handler):
    def emit(self, record):
        try:
            from core.models import TestLog

            TestLog.objects.create(
                level=record.levelname,
                logger_name=record.name,
                message=record.getMessage(),
                test_name=getattr(record, "test_name", None),
            )

        except Exception as e:
            # فقط برای debug
            print("DB LOGGING ERROR:", e)
            raise
