from simple_history.models import HistoricalRecords
from django.db import models


# Create your models here.

class FileInfo(models.Model):
    path = models.URLField()
    info = models.CharField(max_length=255)
    history = HistoricalRecords()

    def __str__(self):
        return self.path
