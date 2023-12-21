from django.db import models
from simple_history.models import HistoricalRecords
from apps.users.models import Profile
# Create your models here.
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.title
