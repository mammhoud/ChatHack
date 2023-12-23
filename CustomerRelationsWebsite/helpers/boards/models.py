from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User
from apps.users.models import Profile
from apps.consumers.models import Ticket


# import apps
# models_for_history = apps.get_app_config().labels()
# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True)
    board_unique_id = models.CharField(max_length=30,unique=True, null=True, blank=True)
    title = models.CharField(max_length=30, default='Board')
    board_type = models.CharField(max_length=30, null=True, blank=True)
    board_url = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    days = models.IntegerField(default=0)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    created_for = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, blank=True)
    period = models.CharField(max_length=30, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.title


class Statistics(models.Model):
    id = models.AutoField(primary_key=True)
    customer_count = models.IntegerField(default=0)
    ticket_count = models.IntegerField(default=0)
    title = models.CharField(max_length=30)
    # board_count = models.IntegerField(default=0)
    user_count = models.IntegerField(default=0)
    message_count = models.IntegerField(default=0)
    # api_count = models.IntegerField(default=0)
    task_count = models.IntegerField(default=0)
    note_count = models.IntegerField(default=0)
    # poduct_count = models.IntegerField(default=0)
    # order_count = models.IntegerField(default=0)
    # payment_count = models.IntegerField(default=0)
    # invoice_count = models.IntegerField(default=0)
    # post_count = models.IntegerField(default=0)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    #history = HistoricalRecords()

    def __str__(self):
        return self.title