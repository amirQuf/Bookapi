from django.db import models


class TestLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=20)
    logger_name = models.CharField(max_length=255)
    message = models.TextField()
    test_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"[{self.level}] {self.logger_name}"
