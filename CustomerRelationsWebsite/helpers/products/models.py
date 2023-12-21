from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100, default='')
    price = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.name
