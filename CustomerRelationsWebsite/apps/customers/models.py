from django.db import models
from apps.core.models import TimeStampedModel
from apps.accounts.models import Profile
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from apps.core.models import TimeStampedModel
from apps.organizations.models import Organization, Department


class Customer(TimeStampedModel):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    phone = models.CharField(max_length=100, default='')
    updated_at = models.DateTimeField(auto_now=True, null=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.profile.user.username)
        super().save(*args, **kwargs)
