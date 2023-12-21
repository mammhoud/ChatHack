from django.db import models
from apps.core.models import TimeStampedModel
from simple_history.models import HistoricalRecords

from django.template.defaultfilters import slugify


class Ptoduct_Type(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + " " + str(self.id)


class Product(TimeStampedModel):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100, default='')
    price = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Ptoduct_Type, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name + " " + self.info + " " + str(self.price) + " " + str(self.category)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)
