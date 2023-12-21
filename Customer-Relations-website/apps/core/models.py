from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class TimeStampedModel(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

    # db_note = models.TextField(default=None, null=True)

    # history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
