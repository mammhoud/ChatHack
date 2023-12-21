from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.crypto import get_random_string

# import apps.channels.models as channels_models
# from apps.accounts.models import Profile
from apps.core.models import TimeStampedModel
from apps.customers.models import Customer
from apps.organizations.models import Organization, Department


# Create your models here.


class Ticket(TimeStampedModel):
    TICKET_SECTIONS = (
        ('Software', 'Software'),
        ('Hardware', 'Hardware'),
        ('Applications', 'Applications'),
        ('Infrastructure and Networking', 'Infrastructure and Networking'),
        ('Database Administrator', 'Database Administrator'),
        ('Other', 'Other')
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    ref = models.SlugField(max_length=8, unique=True, blank=True)
    title = models.CharField(max_length=50)
    issue_description = models.TextField(max_length=1000, null=True, blank=True)
    ticket_section = models.CharField(
        max_length=30, choices=TICKET_SECTIONS, null=True, blank=True)
    urgent_status = models.BooleanField(default=False)
    completed_status = models.BooleanField(default=False, null=True, blank=True)
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='assigned_to', null=True, blank=True)
    resolved_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='resolved_by', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    resolved_date = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def generate_client_id(self):
        return get_random_string(8, allowed_chars='0123456789abcdefzxyv')

    def get_absolute_url(self):
        return reverse("tickets:ticket-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.ticket_id = self.generate_client_id()
        super(Ticket, self).save(*args, **kwargs)


class Comment(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    created_date = models.DateTimeField(null=True, auto_now_add=True)
