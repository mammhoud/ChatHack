from django.db import models
from simple_history.models import HistoricalRecords

class FileInfo(models.Model):
    path = models.URLField()
    info = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.path
